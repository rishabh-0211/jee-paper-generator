# JEE Main Mathematics - Application of Derivatives

## Topic 4: Maxima Minima

**Total Questions:** 132

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be a differentiable function such that $f\left(\dfrac{x+y}{3}\right) = \dfrac{f(x) + f(y)}{3}$ for all $x, y \in \mathbb{R}$, and $f'(0) = 3$. Then the minimum value of the function $g(x) = 3 + e^x f(x)$, is:

**Options:**

- **(A)** $3\left(\dfrac{e+1}{e}\right)$
- **(B)** $3\left(\dfrac{e-1}{e}\right)$
- **(C)** $\dfrac{3-e}{e}$
- **(D)** $3e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3\left(\dfrac{e-1}{e}\right)$**

**Detailed Solution:**

Given $f\left(\dfrac{x+y}{3}\right) = \dfrac{f(x) + f(y)}{3}$

Substituting $x = 0$ and $y = 0$, we get:

$f(0) = \dfrac{2f(0)}{3} \Rightarrow f(0) = 0$

Differentiating the given equation partially with respect to $x$, treating $y$ as a constant:

$f'\left(\dfrac{x+y}{3}\right) \cdot \dfrac{1}{3} = \dfrac{f'(x)}{3}$

$\Rightarrow f'\left(\dfrac{x+y}{3}\right) = f'(x)$

Substituting $x = 0$, we get:

$f'\left(\dfrac{y}{3}\right) = f'(0) = 3$

Since this is true for all $y \in \mathbb{R}$, $f'(x) = 3$ for all $x \in \mathbb{R}$.

Integrating both sides with respect to $x$:

$f(x) = 3x + C$

Using $f(0) = 0$, we get $C = 0$. Thus, $f(x) = 3x$.

Now, the function $g(x)$ is given by:

$g(x) = 3 + e^x f(x) = 3 + 3x e^x$

To find the minimum value, we differentiate $g(x)$ with respect to $x$:

$g'(x) = 3(e^x + x e^x) = 3e^x(1 + x)$

Setting $g'(x) = 0$ gives $x = -1$.

For $x < -1$, $g'(x) < 0$ and for $x > -1$, $g'(x) > 0$. Therefore, $x = -1$ is a point of global minimum.

The minimum value of $g(x)$ is:

$g(-1) = 3 + 3(-1)e^{-1} = 3 - \dfrac{3}{e} = 3\left(\dfrac{e-1}{e}\right)$

Answer: $3\left(\dfrac{e-1}{e}\right)$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\max_{0 \leq x \leq \pi}\left(16\sin\left(\dfrac{x}{2}\right)\cos^3\left(\dfrac{x}{2}\right)\right)$ is equal to:

**Options:**

- **(A)** $\dfrac{3\sqrt{3}}{2}$
- **(B)** $3\sqrt{3}$
- **(C)** $4\sqrt{3}$
- **(D)** $6\sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3\sqrt{3}$**

**Detailed Solution:**

Let $y = \dfrac{x}{2}$. Since $0 \leq x \leq \pi$, we have $0 \leq y \leq \dfrac{\pi}{2}$.

The given expression becomes $f(y) = 16\sin y \cos^3 y$.

Differentiating with respect to $y$:

$f'(y) = 16(\cos y \cdot \cos^3 y + \sin y \cdot 3\cos^2 y(-\sin y))$

$f'(y) = 16\cos^2 y(\cos^2 y - 3\sin^2 y)$

For maximum value, $f'(y) = 0$:

$\cos^2 y - 3\sin^2 y = 0 \Rightarrow \tan^2 y = \dfrac{1}{3}$

Since $y \in \left[0, \dfrac{\pi}{2}\right]$, $\tan y = \dfrac{1}{\sqrt{3}} \Rightarrow y = \dfrac{\pi}{6}$.

Substituting $y = \dfrac{\pi}{6}$ in $f(y)$:

$f\left(\dfrac{\pi}{6}\right) = 16\sin\left(\dfrac{\pi}{6}\right)\cos^3\left(\dfrac{\pi}{6}\right)$

$f\left(\dfrac{\pi}{6}\right) = 16 \times \dfrac{1}{2} \times \left(\dfrac{\sqrt{3}}{2}\right)^3$

$f\left(\dfrac{\pi}{6}\right) = 8 \times \dfrac{3\sqrt{3}}{8} = 3\sqrt{3}$

The maximum value is $3\sqrt{3}$.

Answer: $3\sqrt{3}$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)$ be a polynomial of degree $5$, and have extrema at $x = 1$ and $x = -1$. If $\displaystyle\lim_{x \to 0} \left(\dfrac{f(x)}{x^3}\right) = -5$, then $f(2) - f(-2)$ is equal to:

**Options:**

- **(A)** $0$
- **(B)** $50$
- **(C)** $92$
- **(D)** $112$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $112$**

**Detailed Solution:**

Let the polynomial of degree $5$ be $f(x) = ax^5 + bx^4 + cx^3 + dx^2 + ex + k$.

Given $\displaystyle\lim_{x \to 0} \left(\dfrac{f(x)}{x^3}\right) = -5$, the terms of degree less than $3$ must be zero, and the coefficient of $x^3$ must be $-5$.

Thus, $k = 0$, $e = 0$, $d = 0$, and $c = -5$.

The polynomial becomes $f(x) = ax^5 + bx^4 - 5x^3$.

Differentiating with respect to $x$, we get:

$f'(x) = 5ax^4 + 4bx^3 - 15x^2$

Since $f(x)$ has extrema at $x = 1$ and $x = -1$, we have $f'(1) = 0$ and $f'(-1) = 0$.

$f'(1) = 5a + 4b - 15 = 0$

$f'(-1) = 5a - 4b - 15 = 0$

Adding both equations, we get $10a - 30 = 0 \Rightarrow a = 3$.

Subtracting the equations, we get $8b = 0 \Rightarrow b = 0$.

So, the polynomial is $f(x) = 3x^5 - 5x^3$.

Now, we find $f(2)$ and $f(-2)$:

$f(2) = 3(2)^5 - 5(2)^3 = 3(32) - 5(8) = 96 - 40 = 56$

$f(-2) = 3(-2)^5 - 5(-2)^3 = 3(-32) - 5(-8) = -96 + 40 = -56$

Therefore, $f(2) - f(-2) = 56 - (-56) = 112$.

Answer: $112$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $f$ be a differentiable function satisfying $f(x)=1-2 x+\int_{0}^{x} \mathrm{e}^{(x-t)} f(t) \mathrm{dt}, x \in \mathbf{R}$ and let $\mathrm{g}(x)=\int_{0}^{x}(f(\mathrm{t})+2)^{15}(\mathrm{t}-4)^{6}(\mathrm{t}+12)^{17} \mathrm{dt}, x \in \mathbf{R}$. If p and q are respectively the points of local minima and local maxima of g, then the value of $|\mathrm{p}+\mathrm{q}|$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Given $f(x) = 1 - 2x + \int_0^x e^{(x-t)} f(t) \, dt$.
Differentiating and simplifying:
$e^{-x}f'(x) - e^{-x}f(x) = -2e^{-x} + (1-2x)e^{-x}(-1) + e^{-x}f(x)$
This reduces to:
$f'(x) - 2f(x) = 2x - 3$
Solving the linear ODE $\frac{dy}{dx} - 2y = 2x - 3$:
$y \cdot e^{-2x} = \int e^{-2x}(2x-3)\,dx$
On solving, we get $f(x) = 1 - x$.
Now, $g(x) = \int_0^x (3-t)^{15}(t-4)^6(t+12)^{17} \, dt$
$g'(x) = (3-x)^{15}(x-4)^6(x+12)^{17}$
$= -(x-3)^{15}(x-4)^6(x+12)^{17}$
Sign analysis of $g'(x)$:
$g'(x) $changes from $+ \to - $at $x = 3 $→ local maxima $(q = 3)$
$g'(x) $changes from $- \to + $at $x = -12 $→ local minima $(p = -12)$
$|p + q| = |-12 + 3| = 9$

</details>

---

### Q5. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $(2 \alpha, \alpha)$ be the largest interval in which the function $f(t)=\frac{|t+1|}{t^{2}}, t<0$, is strictly decreasing. Then the local maximum value of the function $g(x)=2 \log _{\mathrm{e}}(x-2)+\alpha x^{2}+4 x-\alpha, x>2$, is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

For $t < 0$, analyze $f(t) = \frac{|t+1|}{t^2}$ in two regions.
For $-1 < t < 0$: 
$f(t) = \frac{t+1}{t^2}$, so $f'(t) = \frac{-(t+2)}{t^3} > 0$ (increasing).
For $t < -1$: 
$f(t) = \frac{-t-1}{t^2}$, so $f'(t) = \frac{t+2}{t^3}$.
For $-2 < t < -1$:
$f'(t) < 0$ (decreasing).
For $t < -2$:
$f'(t) > 0$ (increasing).
Largest decreasing interval is $(-2, -1) = (2\alpha, \alpha)$, so $\alpha = -1$.
For $g(x) = 2\ln(x-2) - x^2 + 4x + 1$:
$g'(x) = \frac{2}{x-2} - 2x + 4 = 0$ gives $(x-2)^2 = 1$, so $x = 3$.
Since $g''(x) = -\frac{2}{(x-2)^2} - 2 < 0$, $x=3$ is maximum.
$g(3) = 2\ln(1) - 9 + 12 + 1 = 4$

</details>

---

### Q6. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x^{2025}-x^{2000}, x \in[0,1]$ and the minimum value of the function $f(x)$ in the interval $[0,1]$ be $(80)^{80}(n)^{-81}$. Then $n$ is equal to

**Options:**

- **(A)** -40
- **(B)** -41
- **(C)** -80
- **(D)** -81

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -81**

**Detailed Solution:**

$f(x) = x^{2025} - x^{2000}$, $f'(x) = x^{1999}(2025x^{25} - 2000) = 0$.
Critical point: $x^{25} = \frac{2000}{2025} = \frac{80}{81}$, i.e., $x = \left(\frac{80}{81}\right)^{1/25}$.
$f(0) = f(1) = 0$. At the critical point:
$f = x^{2000}(x^{25}-1) = \left(\frac{80}{81}\right)^{80}\left(\frac{80}{81}-1\right) = -\frac{80^{80}}{81^{81}}$.
This equals $(80)^{80}(n)^{-81}$, so $n^{-81} = -81^{-81} \Rightarrow n = -81$.

</details>

---

### Q7. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a polynomial function of degree four having extreme values at $x=4$ and $x=5$.
If $\lim _{x \rightarrow 0} \frac{f(x)}{x^2}=5$, then $f(2)$ is equal to :

**Options:**

- **(A)** 12
- **(B)** 10
- **(C)** 8
- **(D)** 14

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 10**

**Detailed Solution:**

$\begin{aligned}
& \lim _{x \rightarrow 0} \frac{f(x)}{x^2}=5 \\
& \lim _{x \rightarrow 0} \frac{\left.a x^4+b x^3+c x^2+d x+e\right)}{x^2}=5 \\
& c=5 \text { and } d=e=0 \\
& f(x)=a x^4+b x^3+5 x^2 \\
& f^{\prime}(x)=4 a x^3+3 b x^2+10 x \\
& =x\left(4 a x^2+3 b x+10\right)
\end{aligned}$
has extremes at 4 and so $f^{\prime}(4)=0 \& f^{\prime}(5)=0$
so $\mathrm{a}=\frac{1}{8} \& \mathrm{~b}=\frac{-3}{2}$
$\text { so } f(2)=\frac{1}{8} \times 2^4-\frac{3}{2} \times 2^3+5 \times 2^2$
$=2-12+20=10 $

</details>

---

### Q8. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $x=-1$ and $x=2$ be the critical points of the function $\mathrm{f}(\mathrm{x})=\mathrm{x}^3+\mathrm{ax}^2+\mathrm{b} \log _{\mathrm{c}}|\mathrm{x}|+1, \mathrm{x} \neq 0$. Let $m$ and $M$ respectively be the absolute minimum and the absolute maximum values of $f$ in the interval $\left[-2,-\frac{1}{2}\right]$. Then $|\mathrm{M}+m|$ is equal to (Take $\log _{\mathrm{c}} 2=0.7$ ):

**Options:**

- **(A)** 21.1
- **(B)** 19.8
- **(C)** 22.1
- **(D)** 20.9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 21.1**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{x})=\mathrm{x}^2+\mathrm{ax}^2+\mathrm{b} \ell \mathrm{n}|\mathrm{x}|+1, \quad \mathrm{x} \neq 0 \\
& \mathrm{f}^{\prime}(\mathrm{x})=3 \mathrm{x}^2+2 \mathrm{ax}+\frac{\mathrm{b}}{\mathrm{x}} \\
& \mathrm{f}^{\prime}(-1)=3-2 \mathrm{a}-\mathrm{b}=0 \\
& \mathrm{f}^{\prime}(-2)=12+4 \mathrm{a}-\frac{\mathrm{b}}{2}=0 \\
& \mathrm{a}=\frac{-9}{2}, \mathrm{~b}=12 \\
& \mathrm{f}^{\prime}(\mathrm{x})=3 \mathrm{x}^2-9 \mathrm{x}+\frac{12}{\mathrm{x}}=\frac{3(\mathrm{x}+1)(\mathrm{x}+2)^2}{\mathrm{x}}
\end{aligned}$
Max. at $\mathrm{n}=-1$
$f(x)=x^2-\frac{9}{2} x^2+12 \ln |x|+1$
$\begin{aligned}
& \mathrm{f}(-1)=-1-\frac{9}{2}+1=-\frac{9}{2} \\
& \mathrm{M}=-4.5
\end{aligned}$
Min. value at $\mathrm{x}=-2$
$\begin{aligned}
& \mathrm{f}(-2)=-8-18+12 \ell \mathrm{n} 2+1 \\
& \mathrm{~m}=-25+12 \ell \mathrm{n} 2=-16.6 \\
& |\mathrm{M}+\mathrm{m}|=21.1
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let f be a differentiable function on $\mathbf{R}$ such that $\mathrm{f}(2) = 1$, $f^{\prime}(2)=4$. Let $\lim _{x \rightarrow 0}(f(2+x))^{3 / x}=e^\alpha$. Then the number of times the curve $y=4 x^3-4 x^2-4(\alpha-7) x-\alpha$ meets x -axis is :-

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $0$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

$\begin{aligned} & \lim _{x \rightarrow 0}(f(2+x))^{\frac{3}{x}} \\ & \lim _{\mathrm{e}^{x \rightarrow 0}} \frac{(f(2+x)-1) 3}{x} \\ & \mathrm{e}^{3 f^{\prime}(2)}=(e)^{12}=(e)^a \Rightarrow a=12 \\ & y=4 x^3-4 x^2-4(a-7) x-a \\ & y=4 x^3-4 x^2-20 x-12 \\ & \text { roots } x=-1,-1,3 \\ & \text { option }(1)\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{a} \gt 0$. If the function $\mathrm{f}(\mathrm{x})=6 \mathrm{x}^3-45 \mathrm{a} \mathrm{x}^2+108 \mathrm{a}^2 \mathrm{x}+1$ attains its local maximum and minimum values at the points $x_1$ and $x_2$ respectively such that $x_1 x_2=54$, then $\mathrm{a}+\mathrm{x}_1+\mathrm{x}_2$ is equal to :-

**Options:**

- **(A)** $15$
- **(B)** $18$
- **(C)** $24$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $18$**

**Detailed Solution:**

$\begin{aligned} & f^{\prime}(x)=18 x^2-90 a x+108 a^2=0 \\ & x=2 a \& x=3 a \\ & x_1=2 a \quad x_2=3 a \\ & x_1 x_2=54 \\ & 6 a^2=54 \\ & a=3 \\ & a+x_1+x_2 \\ & 3+2 \times 3+3 \times 3=18 \\ & \text { option }(2)\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)=2 x^3-9 \mathrm{ax}^2+12 \mathrm{a}^2 \mathrm{x}+1$, where $\mathrm{a} \gt 0$, attains its local maximum and local minimum values at $p$ and $q$, respectively, such that $\mathrm{p}^2=\mathrm{q}$, then $f(3)$ is equal to:

**Options:**

- **(A)** 55
- **(B)** 10
- **(C)** 23
- **(D)** 37

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 37**

**Detailed Solution:**

$f^{\prime}(x)=6 x^2-18 a x+12 a^2$
$f^{\prime}(x)=6\left(x^2-3 a x+2 a^2\right)$
roots are $a, 2 a$
$\mathrm{p}^2=\mathrm{q} \Rightarrow \mathrm{a}^2=2 \mathrm{a}$
$a=2$
$f(x)=2 x^3-18 x^2+48 x+1$
$f(3)=37$

</details>

---

### Q12. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all local minimum values of the function
$$
f(x)=\left\{\begin{array}{lr}
1-2 x, & x \lt -1 \\
\frac{1}{3}(7+2|x|), & -1 \leq x \leq 2 \\
\frac{11}{18}(x-4)(x-5), & x\gt2
\end{array}\right.
$$
is

**Options:**

- **(A)** $\frac{157}{72}$
- **(B)** $\frac{131}{72}$
- **(C)** $\frac{171}{72}$
- **(D)** $\frac{167}{72}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{157}{72}$**

**Detailed Solution:**

$f(x)=\left\{\begin{array}{cl}1-2 x, & x < -1 \\ \frac{1}{3}(7-2 x), & -1 \leq x \leq 2 \\ \frac{1}{3}(7+2 x) & 0 \leq x < 2 \\ \frac{11}{18}(x-4)(x-5), & x>2\end{array}\right.$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5elSffJoIwzPqjwKGOnXGbNMbPXEU5-BewmmX_x_OWY.original.fullsize.png">




$\therefore$ Local minimum values at $\mathrm{A} \& \mathrm{~B}$
$\begin{aligned}
& \frac{7}{3}-\frac{11}{72} \\
& \Rightarrow \frac{168-11}{72} \Rightarrow \frac{157}{72}
\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (23 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If the set of all values of a, for which the equation $5 x^3-15 x-a=0$ has three distinct real roots, is the interval $(\alpha, \beta)$, then $\beta-2 \alpha$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

$\begin{aligned} & 5 x^3-15 x-a=0 \\ & f(x)=5 x^3-15 x \\ & f(x)=15 x^2-15=15(x-1)(x+1)\end{aligned}$



<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pUMvZVXXHIIlKQkmLbX2z8xh-4Y6nyyBgItkUqjQ6EY.original.fullsize.png">




$\mathrm{a} \in(-10,10)$
$\alpha=-10, \beta=10$
$\beta-2 \alpha=10+20=30$

</details>

---

### Q14. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the set of all positive values of $\lambda$, for which the point of local minimum of the function $\left(1+x\left(\lambda^2-x^2\right)\right)$ satisfies $\frac{x^2+x+2}{x^2+5 x+6} < 0$, be $(\alpha, \beta)$. Then $\alpha^2+\beta^2$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **39**

**Detailed Solution:**

$\begin{aligned} & \frac{x^2+x+2}{x^2+5 x+6} < 0 \\ & \Rightarrow \frac{1}{(x+2)(x+3)} < 0\end{aligned}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DTWKVEPpoy9UAJOw0XJAu3zFQLpIkgX_2BkhBZ8K30o.original.fullsize.png">
$\begin{aligned}
& x \in(-3,-2) \ldots \ldots \ldots . .(1) \\
& f(x)=1+x\left(\lambda^2-x^2\right)
\end{aligned}$
Finding local minima
$f^{\prime}(x)=\left(\lambda^2-x^2\right)+(-2 x) \cdot x$
Put $\mathrm{f}^{\prime}(\mathrm{x})=0$
$\begin{aligned}
& \Rightarrow \lambda^2=3 x^2 \\
& \Rightarrow x= \pm \frac{\lambda}{\sqrt{3}}
\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QaJ6UNnAmRG1F2UfM0ZfbS3oldd9AeNxUxM7pM44vTc.original.fullsize.png">
We want local min
$\Rightarrow \mathrm{x}=\frac{-\lambda}{\sqrt{3}}$
from (1)
$x \in(-3,-2)$
$\begin{aligned} & -3 < \frac{-\lambda}{\sqrt{3}} < -2 \\ & 3 \sqrt{3}>\lambda>2 \sqrt{3} \\ & \alpha=2 \sqrt{3}, \beta=3 \sqrt{3} \\ & \alpha^2+\beta^2=12+27=39\end{aligned}$

</details>

---

### Q15. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A variable line $L$ passes through the point $(3,5)$ and intersects the positive coordinate axes at the points $\mathrm{A}$ and $\mathrm{B}$. The minimum area of the triangle $\mathrm{OAB}$, where $\mathrm{O}$ is the origin, is :

**Options:**

- **(A)** 30
- **(B)** 25
- **(C)** 40
- **(D)** 35

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 30**

**Detailed Solution:**

$\begin{aligned} & \frac{x}{a}+\frac{y}{b}=1 \\ & \frac{3}{a}+\frac{5}{b}=1 \Rightarrow b=\frac{5 a}{a-3}, a>3\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vczTu120S0ym_kemOFBhnpc-16qUoeKlhBnwZuYepPM.original.fullsize.png">
$A=\frac{1}{2} a b=\frac{1}{2} a \frac{5 a}{(a-3)}=\frac{5}{2} \cdot \frac{a^2}{a-3}$
$\begin{aligned} & =\frac{5}{2}\left(\frac{\mathrm{a}^2-9+9}{\mathrm{a}-3}\right) \\ & =\frac{5}{2}\left(\mathrm{a}+3+\frac{9}{\mathrm{a}-3}\right) \\ & =\frac{5}{2}\left(\mathrm{a}-3+\frac{9}{\mathrm{a}-3}+6\right) \geq 30\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $\mathrm{A}$ be the region enclosed by the parabola $y^2=2 x$ and the line $x=24$. Then the maximum area of the rectangle inscribed in the region $\mathrm{A}$ is________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **128**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5Hm8bCZEI6J5LKZpnqqLo3UNAaPC2_MDWTnVf_j_3is.original.fullsize.png">
$\begin{aligned} & A=2\left(24-\frac{b^2}{2}\right) \cdot b \\ & \frac{d A}{d b}=0 \quad \Rightarrow \quad b=4 \\ & A=2(24-8) 4 \\ & =128\end{aligned}$

</details>

---

### Q17. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the function $f(x)=2 x^3-9 x^2+12 \mathrm{a}^2 x+1, \mathrm{a}>0$ has a local maximum at $x=\alpha$ and a local minimum at $x=\alpha^2$, then $\alpha$ and $\alpha^2$ are the roots of the equation :

**Options:**

- **(A)** $x^2-6 x+8=0$
- **(B)** $x^2+6 x+8=0$
- **(C)** $8 x^2+6 x-1=0$
- **(D)** $8 x^2-6 x+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^2-6 x+8=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jNI6V4Opdz9lKlGZqp2CuJNgokbWPfGBH9d-LUHmg1I.original.fullsize.png">
$\begin{aligned} & \alpha+\alpha^2=3 \mathrm{a} \& \alpha \times \alpha^2=2 \mathrm{a}^2 \\ & \quad \downarrow \\ & \left(\alpha+\alpha^2\right)^3=27 \mathrm{a}^3 \\ & \Rightarrow 2 \mathrm{a}^2+4 \mathrm{a}^4+3(3 \mathrm{a})\left(2 \mathrm{a}^2\right)=27 \mathrm{a}^3 \\ & \Rightarrow 2+4 \mathrm{a}^2+18 \mathrm{a}=27 \mathrm{a} \\ & \Rightarrow 4 \mathrm{a}^2-9 \mathrm{a}+2=0 \\ & \Rightarrow 4 \mathrm{a}^2-8 \mathrm{a}-\mathrm{a}+2=0 \\ & \Rightarrow(4 \mathrm{a}-1)(\mathrm{a}-2)=0 \Rightarrow \mathrm{a}=2 \\ & \text { so } 6 \mathrm{x}^2-36 \mathrm{x}+48=0\end{aligned}$
$\Rightarrow x^2-6 x+8=0$  ...(1)
If we take $\mathrm{a}=\frac{1}{4}$ then $\alpha=\frac{1}{2}$ which is not possible

</details>

---

### Q18. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=4 \cos ^3 x+3 \sqrt{3} \cos ^2 x-10$. The number of points of local maxima of $f$ in interval $(0,2 \pi)$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=4 \cos ^3(\mathrm{x})+3 \sqrt{3} \cos ^2(\mathrm{x})-10 ; \mathrm{x} \in(0,2 \pi) \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=12 \cos ^2 \mathrm{x}[-\sin (\mathrm{x})]+3 \sqrt{3}(2 \cos (\mathrm{x}))[-\sin (\mathrm{x})] \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x})=-6 \sin (\mathrm{x}) \cos (\mathrm{x})[2 \cos (\mathrm{x})+\sqrt{3}]\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BmAPFOFz4I5_2lxF_bzrQXlVrv8fQ2qVcN1H4g4ZYOs.original.fullsize.png">
local maxima at $\mathrm{x}=\frac{5 \pi}{6}, \frac{7 \pi}{6}$

</details>

---

### Q19. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)=\left(\frac{1}{x}\right)^{2 x} ; x>0$ attains the maximum value at $x=\frac{1}{\mathrm{e}}$ then :

**Options:**

- **(A)** $\mathrm{e}^\pi < \pi^{\mathrm{e}}$
- **(B)** $\mathrm{e}^\pi>\pi^{\mathrm{e}}$
- **(C)** $(2 e)^\pi>\pi^{(2 e)}$
- **(D)** $\mathrm{e}^{2 \pi} < (2 \pi)^{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{e}^\pi>\pi^{\mathrm{e}}$**

**Detailed Solution:**

Let $y=\left(\frac{1}{x}\right)^{2 x}$
$\begin{aligned}
& \ell \text { ny }=2 x \ell n\left(\frac{1}{x}\right) \\
& \ell \text { ny }=-2 x \ell \ln x \\
& \frac{1}{y} \frac{d y}{d x}=-2(1+\ell n x)
\end{aligned}$
for $\mathrm{x}>\frac{1}{\mathrm{e}} \mathrm{f}^{\mathrm{n}}$ is decreasing
$\text {so, } \mathrm{e} < \pi$
$\begin{aligned}
& \left(\frac{1}{\mathrm{e}}\right)^{2 \mathrm{e}}>\left(\frac{1}{\pi}\right)^{2 \pi} \\
& \mathrm{e}^\pi>\pi^{\mathrm{e}}
\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The interval in which the function $f(x)=x^x, x>0$, is strictly increasing is

**Options:**

- **(A)** $\left(0, \frac{1}{e}\right]$
- **(B)** $(0, \infty)$
- **(C)** $\left.\left[\frac{1}{e}, \infty\right)\right]_V$
- **(D)** $\left[\frac{1}{e^2}, 1\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left.\left[\frac{1}{e}, \infty\right)\right]_V$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{f}(\mathrm{x})=\mathrm{x}^{\mathrm{x}} ; \mathrm{x}>0 \\
& \ell \operatorname{nn}=\mathrm{x} \ell \mathrm{n} \mathrm{x} \\
& \frac{1}{\mathrm{y}} \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{x}}{\mathrm{x}}+\ln \mathrm{n} \\
& \frac{\mathrm{dy}}{\mathrm{dx}}=\mathrm{x}^{\mathrm{x}}(1+\ell \mathrm{n} x)
\end{aligned}$
for strictly increasing
$\begin{aligned}
& \frac{d y}{d x} \geq 0 \Rightarrow x^x(1+\ell n x) \geq 0 \\
& \Rightarrow \ell n x \geq-1
\end{aligned}$
$\begin{aligned} & x \geq e^{-1} \\ & x \geq \frac{1}{e} \\ & x \in\left[\frac{1}{e}, \infty\right)\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the maximum and minimum values of $\left(\sqrt{8 x-x^2-12}-4\right)^2+(x-7)^2, x \in \mathbf{R}$ be $\mathrm{M}$ and $\mathrm{m}$, respectively. Then $\mathrm{M}^2-\mathrm{m}^2$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1600**

**Detailed Solution:**

$\begin{aligned} & (x-7)^2+(y-4)^2 \\ & y=\sqrt{8 x-x^2-12} \\ & y^2=-(x-4)^2+16-12 \\ & (x-4)^2+y^2=4\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/WThTaKogzydNS5UDsgHmZqwudoBaGE_WTmt-oflPaBE.original.fullsize.png">
$\begin{aligned} & m=9 \\ & M=41 \\ & M^2-m^2=41^2-9^2=1600\end{aligned}$

</details>

---

### Q22. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the function
$f(x)=\sin x+3 x-\frac{2}{\pi}\left(x^2+x\right), \text { where } x \in\left[0, \frac{\pi}{2}\right],$
consider the following two statements :
(I) $\mathrm{f}$ is increasing in $\left(0, \frac{\pi}{2}\right)$.
(II) $f^{\prime}$ is decreasing in $\left(0, \frac{\pi}{2}\right)$.
Between the above two statements,

**Options:**

- **(A)** only (II) is true.
- **(B)** only (I) is true.
- **(C)** neither (I) nor (II) is true.
- **(D)** both (I) and (II) are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) both (I) and (II) are true**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}(\mathrm{x})=\sin \mathrm{x}+3 \mathrm{x}-\frac{2}{\pi}\left(\mathrm{x}^2+\mathrm{x}\right) \quad \mathrm{x} \in\left[0, \frac{\pi}{2}\right] \\ & \mathrm{f}^{\prime}(\mathrm{x})=\cos \mathrm{x}+3-\frac{2}{\pi}(2 \mathrm{x}+1)>0 \mathrm{f}(\mathrm{x}) \uparrow \\ & \mathrm{f}^{\prime}(\mathrm{x})=-\sin \mathrm{x}+0-\frac{\pi}{2}(2) \\ & =-\sin \mathrm{x}-\frac{4}{\pi} < 0 \quad \mathrm{f}^{\prime}(\mathrm{x}) \downarrow \\ & 0 < \mathrm{x} < \frac{\pi}{2}\end{aligned}$
$\Rightarrow-\frac{2}{\pi}(\underset{+1}{0}{ < \underset{+1}2 \mathrm{x}} < \underset{+1}\pi)$
$\begin{aligned} & \underset{+3}{-\frac{2}{\pi}}>\frac{-2}{\pi}(\underset{+3}2 \mathrm{x}+1)>-\frac{2}{\pi}(\underset{+3}\pi+1) \\ &   \underset{+ve} 3-\frac{2}{\pi}>3-\frac{2}{\pi}(2 x+1)>3-\frac{2}{\pi}(\underset{+ve}\pi+1) \\ & \end{aligned}$

</details>

---

### Q23. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a rectangle $A B C D$ of sides 2 and 4 be inscribed in another rectangle $P Q R S$ such that the vertices of the rectangle $A B C D$ lie on the sides of the rectangle $P Q R S$. Let $a$ and $b$ be the sides of the rectangle $P Q R S$ when its area is maximum. Then $(a+b)^2$ is equal to :

**Options:**

- **(A)** 72
- **(B)** 60
- **(C)** 64
- **(D)** 80

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 72**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/i05vVWEBBF5O4_CWNzP3pn1e3PEEmYKACgj_BqgrPIw.original.fullsize.png">
$\begin{aligned} & \text { Area }=(4 \cos \theta+2 \sin \theta)(2 \cos \theta+4 \sin \theta) \\ & =8 \cos ^2 \theta+16 \sin \theta \cos \theta+4 \sin \theta \cos \theta+8 \sin ^2 \theta \\ & =8+20 \sin \theta \cos \theta \\ & =8+10 \sin 2 \theta \\ & \text { Max Area }=8+10=18(\sin 2 \theta=1) \theta=45^{\circ} \\ & (a+b)^2=(4 \cos \theta+2 \sin \theta+2 \cos \theta+4 \sin \theta)^2 \\ & =(6 \cos \theta+6 \sin \theta)^2 \\ & =36(\sin \theta+\cos \theta)^2 \\ & =36(\sqrt{2})^2\end{aligned}$
$=72$

</details>

---

### Q24. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $f(x)=3 \sqrt{x-2}+\sqrt{4-x}$ be a real valued function. If $\alpha$ and $\beta$ are respectively the minimum and the maximum values of $f$, then $\alpha^2+2 \beta^2$ is equal to

**Options:**

- **(A)** 42
- **(B)** 38
- **(C)** 24
- **(D)** 44

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 42**

**Detailed Solution:**

$\begin{aligned}
& f(x)=3 \sqrt{x-2}+\sqrt{4-x} \\
& x-2 \geq 0 \& 4-x \geq 0 \\
& \therefore x \in[2,4]
\end{aligned}$
Let $x=2 \sin ^2 \theta+4 \cos ^2 \theta$
$\begin{aligned}
& \therefore \mathrm{f}(\mathrm{x})=3 \sqrt{2}|\cos \theta|+\sqrt{2}|\sin \theta| \\
& \therefore \sqrt{2} \leq 3 \sqrt{2}|\cos \theta|+\sqrt{2}|\sin \theta| \leq \sqrt{9 \times 2+2} \\
& \sqrt{2} \leq 3 \sqrt{2}|\cos \theta|+\sqrt{2}|\sin \theta| \leq \sqrt{20} \\
& \therefore \alpha=\sqrt{2} \quad \beta=\sqrt{20} \\
& \alpha^2+2 \beta^2=2+40=42
\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>,</mo><mi>x</mi><mo>∈</mo><mo>[</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>]</mo></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> are the maximum and minimum values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, respectively in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>]</mo></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>392</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>608</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>608</mn></math>**

**Detailed Solution:**

<blockquote><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>×</mo><mfenced><mn>3</mn></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mfenced><mn>2</mn></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mfenced close="]" open="["><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>×</mo><mfenced><mn>3</mn></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mn>2</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mfenced close="]" open="["><mrow><mn>3</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>5</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>For critical points, we put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo> </mo><mn>2</mn><mo>,</mo><mo> </mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><msup><mfenced><mrow><mo>-</mo><mn>3</mn></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mo>-</mo><mn>108</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mo>-</mo><mn>4</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>216</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>49</mn><mo>×</mo><mn>8</mn><mo>=</mo><mn>392</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>=</mo><mn>392</mn><mo>,</mo><mo> </mo><mi>m</mi><mo>=</mo><mo>-</mo><mn>216</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>392</mn><mo>+</mo><mn>216</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>608</mn></math></p></blockquote>

</details>

---

### Q26. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mi>R</mi></math>, has

**Options:**

- **(A)** exactly one point of local minima and no point of local maxima
- **(B)** exactly one point of local maxima and no point of local minima
- **(C)** exactly one point of local maxima and exactly one point of local minima
- **(D)** exactly two points of local maxima and exactly one point of local minima

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) exactly one point of local maxima and exactly one point of local minima**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>(</mo><mi>x</mi><msup><mo>)</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfrac></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0480c4ba-a295-4d9e-9f37-e9cfad158b09.png" style="width: 350px; height: 99px;"/></p><p>The function changes from positive to negative at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and from negative to positive at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>So, the point of local maxima <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">M</mi></mfenced></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and the point of local minima <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">m</mi></mfenced></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q27. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>max</mi><mrow><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mi>&#960;</mi></mrow></munder><mfenced open="{" close="}"><mrow><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>sin</mi><mn>3</mn><mi>x</mi></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>sin</mi><mn>3</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>3</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>sin</mi><mn>3</mn><mi>x</mi></math></p><p>For maxima/minima <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>4</mn><msup><mi>cos</mi><mn>3</mn></msup><mi>x</mi><mo>-</mo><mn>3</mn><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>)</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>)</mo><mo>(</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><msqrt><mn>3</mn></msqrt><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></math>is local maxima point</p><p>Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q28. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>If the total maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><msqrt><mn>3</mn><mi>e</mi></msqrt><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mi>e</mi></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>k</mi><mi>e</mi></mfrac></mfenced><mn>8</mn></msup><mo>+</mo><mfrac><msup><mi>k</mi><mn>8</mn></msup><msup><mi>e</mi><mn>5</mn></msup></mfrac><mo>+</mo><msup><mi>k</mi><mn>8</mn></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><msup><mi>e</mi><mn>11</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>5</mn></msup><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><msup><mi>e</mi><mn>11</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><msup><mi>e</mi><mn>10</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mn>5</mn></msup><mo>+</mo><msup><mi>e</mi><mn>11</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><msup><mi>e</mi><mn>11</mn></msup></math>**

**Detailed Solution:**

<p>Given function is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>e</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></msup></math></p><p>For maxima or minima <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mfenced close="]" open="["><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mo>&#215;</mo><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfrac><mrow><mn>1</mn><mo>&#215;</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><msqrt><mn>3</mn></msqrt><mi>e</mi></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi>e</mi></mrow><mn>2</mn></mfrac><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>&#215;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mfenced close="]" open="["><mrow><mi>sin</mi><mn>2</mn><mi>x</mi><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>-</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now on equation we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> (not possible)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi mathvariant="normal">e</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>&#215;</mo><msqrt><mi>e</mi></msqrt></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mi>max</mi></msub><mo>=</mo><msup><mfenced><mi>e</mi></mfenced><mfrac><mn>3</mn><mn>8</mn></mfrac></msup><mo>=</mo><mfrac><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>11</mn><mn>8</mn></mfrac></mstyle></msup><mi>e</mi></mfrac><mo>&#8658;</mo><mi>k</mi><mo>=</mo><msup><mi>e</mi><mfrac><mn>11</mn><mn>8</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mi>k</mi><mi>e</mi></mfrac></mfenced><mn>8</mn></msup><mo>+</mo><mfrac><msup><mi>k</mi><mn>8</mn></msup><msup><mi>e</mi><mn>5</mn></msup></mfrac><mo>+</mo><msup><mi>k</mi><mn>8</mn></msup><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><msup><mi>e</mi><mn>11</mn></msup></math></p>

</details>

---

### Q29. JEE Main 2023 (10 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>In the figure, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#952;</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mi>BE</mi></mfenced><mo>=</mo><mn>4</mn><mfenced><mi>AB</mi></mfenced></math>. If the area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>CAB</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn><mo>&#160;</mo><msup><mi>unit</mi><mn>2</mn></msup></math>, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><msub><mi mathvariant="normal">&#952;</mi><mn>1</mn></msub></mfrac></math> is the largest, then the perimeter (in unit) of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>CED</mi></math> is equal to</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fda1cbf6-3e39-4ed0-b45f-bcc47c23a9ee.png" style="width: 200px; height: 266px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f9f6bc8d-8f4c-47dc-80c8-449ab553b8f9.png" style="width: 200px; height: 267px;" /></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#952;</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p>Now, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AB</mi><mo>&#160;</mo><mo>=</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>BD</mi><mo>=</mo><mi>y</mi></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mi>BE</mi><mo>=</mo><mn>4</mn><mi>AB</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mi>y</mi><mo>+</mo><mi>DE</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>DE</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mi>y</mi></math></p><p>Now given area of triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>CAB</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>x</mi><mi>y</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><mi>x</mi></mfrac></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>tan&#952;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mi mathvariant="normal">y</mi></mrow></mfenced><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mrow><mo>(</mo><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn><mo>)</mo></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>tan&#952;</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p>Now taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi></math> both of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#952;</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>tan&#952;</mi><mn>1</mn></msub><mo>&#183;</mo><msub><mi>tan&#952;</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfrac><mn>4</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>&#183;</mo><mfenced><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><msub><mi mathvariant="normal">&#952;</mi><mn>1</mn></msub></mfrac></math> is maximum when <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>12</mn><mo>-</mo><mn>6</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>3</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#952;</mi><mn>2</mn></msub><mo>=</mo><mn>60</mn><mo>&#176;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><mi>DE</mi><mi>CD</mi></mfrac><mo>&#8658;</mo><mi>DE</mi><mo>=</mo><mi>x</mi><mo>&#183;</mo><msqrt><mn>3</mn></msqrt><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><mi>CD</mi><mi>CE</mi></mfrac><mo>&#8658;</mo><mi>CE</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>6</mn><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p><p>So, the Perimeter of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>CED</mi><mo>=</mo><mi>CD</mi><mo>+</mo><mi>DE</mi><mo>+</mo><mi>CE</mi><mo>=</mo><mn>6</mn></math></p></blockquote>

</details>

---

### Q30. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>&#945;</mi></msub></math> is the greatest term in the sequence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><msup><mi>n</mi><mn>3</mn></msup><mrow><msup><mi>n</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn></mrow></mfrac><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>We know that, for increasing function <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p>So, differentiating the given function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>441</mn></mrow></mfenced></mrow><mrow><mo>(</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>441</mn></mrow></mfenced></mrow><mrow><mo>(</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>441</mn></mrow></mfenced></mrow><mrow><mo>(</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>147</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>&#60;</mo><mn>441</mn></math></p><p>Now for maxima/minima <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>=</mo><mn>441</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#60;</mo><mi>&#945;</mi><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>64</mn><mn>403</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>=</mo><mfrac><mn>125</mn><mn>772</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>f</mi><mfenced><mn>5</mn></mfenced><mo>&#62;</mo><mi>f</mi><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q31. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the abosolute maximum and minimum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>8</mn></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>]</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn></mtd><mtd><mo>;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></mtd></mtr></mtable></mfenced></math></p><p>Now point of extrema will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math>which is not in domain and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Now for finding the value of global minima and maxima we will check the value of function at extrema points and boundary points,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>8</mn></math> will give, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>17</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn></math> will give, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mo>-</mo><mn>7</mn></math></p><p>Hence, absolute minima is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math> and maxima is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math></p><p>So, their sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn><mo>+</mo><mn>17</mn><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q32. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math> . If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> respectively are the maximum and the minimum values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msqrt><mi>&#945;</mi></msqrt><mo>=</mo><mfrac><mn>19</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msqrt><mi>&#945;</mi></msqrt><mo>=</mo><mfrac><mn>19</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msqrt><mi>&#945;</mi></msqrt><mo>=</mo><mfrac><mn>19</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>&#8594;</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub><mo>+</mo><msub><mi>C</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr></mtable></mfenced></math></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>-</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></math></p><p>Now, for </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>2</mn><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>4</mn><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mfrac><mn>19</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q33. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The absolute minimum value, of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>t</mi></mfenced></math> denotes the greatest integer function, in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mfenced close="|" open="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Now,</p><p>Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>For the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>&#39;</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math> attains its minimum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>min</mtext><mfenced open="[" close="]"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mtext>as</mtext><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> attains its minimum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>0</mn><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q34. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is to be cut into two pieces. A piece of length <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub></math> is bent to make a square of area <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> and the other piece of length <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>2</mn></msub></math> is made into a circle of area <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mo>&#160;</mo><msub><mi>A</mi><mn>2</mn></msub></math> is minimum then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#960;</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfenced><mo>:</mo><msub><mi>&#8467;</mi><mn>2</mn></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>:</mo><mo>&#160;</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mo>&#160;</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mo>&#160;</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mo>&#160;</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>:</mo><mo>&#160;</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>The length of wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>m</mi></math>.</p><p>According to the question:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#8467;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#8467;</mi><mn>2</mn></msub><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi mathvariant="normal">d</mi><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Let the side of the square be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>=</mo><msub><mi>&#8467;</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><msub><mi>&#8467;</mi><mn>1</mn></msub><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Let the radius of the circle be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>, then</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#960;</mi><mi>y</mi><mo>=</mo><msub><mi mathvariant="normal">&#8467;</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">&#8467;</mi><mn>2</mn></msub><mrow><mn>2</mn><mi mathvariant="normal">&#960;</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>=</mo><msup><mfenced><mfrac><msub><mi>&#8467;</mi><mn>1</mn></msub><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>=</mo><mi>&#960;</mi><msup><mfenced><mfrac><msub><mi>&#8467;</mi><mn>2</mn></msub><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>2</mn><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>A</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mrow><mo>(</mo><msub><mi>&#8467;</mi><mn>1</mn></msub><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>(</mo><msub><mi>&#8467;</mi><mn>2</mn></msub><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>S</mi></mrow><mrow><mi>d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><mi>d</mi><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mo>&#160;</mo><mi>d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> to be minimum,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>s</mi></mrow><mrow><mi mathvariant="normal">d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><mi>d</mi><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mo>&#160;</mo><mi>d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow><mn>8</mn></mfrac><mo>-</mo><mfrac><mrow><mn>6</mn><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mfrac><mrow><mi mathvariant="normal">d</mi><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>&#8467;</mi><mn>1</mn></msub><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><msub><mi>&#8467;</mi><mn>2</mn></msub></mrow><mrow><mn>4</mn><mi>&#960;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#960;</mi><msub><mi>&#8467;</mi><mn>1</mn></msub></mrow><msub><mi>&#8467;</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q35. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>7</mn><mo>)</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo><mi>x</mi><mo>-</mo><mn>6</mn></math> have a maxima for some value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#60;</mo><mn>0</mn></math> and a minima for some value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. Then, the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>7</mn><mo>)</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p>On taking differentiation w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>7</mn><mo>)</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>6</mn><mo>(</mo><mn>0</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>7</mn><mo>)</mo><mo>(</mo><mn>0</mn><mo>)</mo><mo>+</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo></math></p><p>Here, given that for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>0</mn></math> the function has maxima and for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> the function has minima so the function is decreasing function about <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>,</p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>&#60;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>(</mo><mn>2</mn><mi>p</mi><mo>-</mo><mn>9</mn><mo>)</mo><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">p</mi><mo>&#60;</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q36. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> be a local minima of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>18</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is local maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>33</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>31</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>33</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>31</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>33</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> be a local minima of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>18</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math></p><p>Now differentiating the above function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>8</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>36</mn><mi>x</mi><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>Now equating it to zero we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn><mo>&#177;</mo><msqrt><mn>24</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#177;</mo><msqrt><mn>6</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></math> {by checking sign change of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math> for maxima}</p><p>Now rewriting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>18</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi><mo>+</mo><mn>12</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></mrow></mfenced><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>.</mo><mn>5</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mrow><msqrt><mn>6</mn></msqrt><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>M</mi><mo>=</mo><mn>12</mn><msqrt><mn>6</mn></msqrt><mo>-</mo><mfrac><mn>33</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q37. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>4</mn></mrow></msup><mo>,</mo><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mi>R</mi></math>. Then which of the following statements are true?</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math> is a point of local minima of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> is a point of inflection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>:</mo><msup><mi>f</mi><mo>&#39;</mo></msup></math> is increasing for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><msqrt><mn>2</mn></msqrt></math></p>

**Options:**

- **(A)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(C)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(D)** All <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) All <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo><mi>Q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mn>4</mn></mrow></msup></math></p><p>Now on rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>81</mn><mo>.</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup></math></p><p>Now differentiating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>81</mn><mo>.</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mo>&#183;</mo><mi>ln</mi><mn>3</mn><mo>&#183;</mo><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#183;</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>81</mn><mo>&#215;</mo><mn>6</mn></mrow></mfenced><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mo>&#215;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mi>ln</mi><mn>3</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4a9f1e49-da48-4d49-a397-41cd3c9be7ff-image.png" style="width: 224px; height: 60px;" /></p><p>So by using first derivate test we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> is point of local minima</p><p>Now differentiating the function <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><munder><munder><mfenced><mrow><mn>486</mn><mo>&#183;</mo><mi>ln</mi><mn>3</mn></mrow></mfenced><mo>&#9183;</mo></munder><mi mathvariant="normal">k</mi></munder><munder><munder><mrow><msup><mn>3</mn><msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mi mathvariant="normal">x</mi><msup><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow><mo>&#9183;</mo></munder><mrow><mi mathvariant="normal">g</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></mrow></munder></math></p><p>We get,<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>&#183;</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mo>&#183;</mo><mn>4</mn><mi>x</mi><mo>&#183;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>x</mi><mo>&#183;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#183;</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mi>ln</mi><mn>3</mn><mo>&#183;</mo><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>&#183;</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>+</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mi>ln</mi><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced close="]" open="["><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mi>ln</mi><mn>3</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mo>&#183;</mo><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><msup><msqrt><mn>2</mn></msqrt><mo>+</mo></msup></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><msup><msqrt><mn>2</mn></msqrt><mo>-</mo></msup></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>Since double derivate is changing the sign at given point so we can say that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> is point of inflection</p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><msqrt><mn>2</mn></msqrt></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></math> is increasing</p></blockquote>

</details>

---

### Q38. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the absolute maximum and absolute minimum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced></math></p><p>Now differentiating the function we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now equating <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> to find critical points,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>-</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p><p>Now checking the value of function at critical point and boundary point we get,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 200px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>2</mn></msqrt></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></td>		</tr>	</tbody></table><p>So, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mtable><mtr><mtd><msub><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>max</mi></msub><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>2</mn></msqrt></mtd></mtr><mtr><mtd><mo>&#8756;</mo><mo>&#160;</mo><msub><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>min</mi></msub><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p>So, the sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>2</mn></msqrt><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a twice differentiable function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>5</mn></math>. If the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></math> intersects the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> at only two distinct points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, then the least number of points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, at which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a twice differentiable function in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>5</mn></math>. If the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></math> intersects the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> at only two distinct points in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, then the least number of points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>, at which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>, is</p><p>Now plotting the diagram of given data we have,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a16d3b2d-9e9a-4c7a-bba4-1fc660cf7d3a-4e693ce9-c855-4624-a288-4ae27cdf7822-image.png" style="width: 236px; height: 247px;" /></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> cuts <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></math> at two distinct point between<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>a</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>b</mi></mfenced><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>c</mi></mfenced><mo>=</mo><mn>2</mn></math> {as slope of given line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>}</p><p>So we can conclude that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mi>x</mi></mfenced></math> is zero for atleast <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#8712;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#8712;</mo><mfenced><mrow><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced></math></p></blockquote>

</details>

---

### Q40. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> be any points on the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math>, respectively. The distance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is minimum for some value of the abscissa of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> in the interval

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup></mrow></mfenced></math></p><p>Minimum distance will be obtained at common normal of the parabola and circle.</p><p>So for minimum <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi></math>, the distance between centre of circle and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> should be minimum.</p><p>Now, the distance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> from given circle,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><msqrt><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></math></p><p>For least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>, we need to minimize</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced><mo>=</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>4</mn><msub><mi>x</mi><mn>1</mn></msub><mfenced><mrow><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>From options</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>ve</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>ve</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msub><mi>x</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn></math> for some <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>&#8712;</mo><mfenced><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math> from IMVT</p></blockquote>

</details>

---

### Q41. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> Then the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has maximum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><msqrt><mn>6</mn></msqrt><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>2</mn><mo>,</mo><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>10</mn><mi>x</mi><mo>-</mo><mn>7</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8804;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#62;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>,</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>10</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is increasing</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>,</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math>  function is decreasing.</p><p>So, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> there is a point of maxima</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>1</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p>For maximum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>&#8805;</mo><mo>-</mo><mn>2</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mo>&#160;</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>32</mn><mo>&#8805;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>6</mn><mo>,</mo><mo>-</mo><mn>2</mn><mo>)</mo><mo>&#8746;</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>6</mn><mo>]</mo></math></p></blockquote>

</details>

---

### Q42. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mn>5</mn></math> touches the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and cuts the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at the point $\mathrm{Q}$, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>. Then the local maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>29</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mn>5</mn></math> pass through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> </p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Since the curve touches <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>, so its slope would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></p><p>i.e <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msub><mfenced><mrow><mn>3</mn><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mrow><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also given, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><msup><mi>y</mi><mo>&#39;</mo></msup><mrow><mo mathvariant="italic">(</mo><mi mathvariant="italic">x</mi><mo mathvariant="italic">)</mo></mrow><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Solving eq. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo mathvariant="italic">=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>For local maxima <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>x</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#34;</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> has local maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q43. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the absolute maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>7</mn></mrow></mfenced><msup><mi mathvariant="normal">e</mi><mfenced><mrow><mn>4</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>180</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>31</mn></mrow></mfenced></msup></math>in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>&#945;</mi></mfenced></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>7</mn></mrow></mfenced><msup><mi mathvariant="normal">e</mi><mfenced><mrow><mn>4</mn><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>180</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>31</mn></mrow></mfenced></msup></math></p><p>Now differentiating the function to find function is increasing or decreasing,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>180</mn><mi>x</mi><mo>+</mo><mn>31</mn></mrow></mfenced></msup><mfenced><mrow><mn>12</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>15</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mfenced><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>180</mn><mi>x</mi><mo>+</mo><mn>31</mn></mrow></mfenced></msup><mfenced><mrow><mn>12</mn><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">f</mi><mo>&#39;</mo></msup><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math>is decreasing function on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>The absolute maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q44. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>&#160;</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be a function defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><msub><mi>n</mi><mn>1</mn></msub></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><msub><mi>n</mi><mn>2</mn></msub></msup><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>&#8712;</mo><mi>N</mi></math>. The, which of the following is NOT true?

**Options:**

- **(A)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> attains local maxima.
- **(B)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> attains local maxima.
- **(C)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> attains local maxima.
- **(D)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> attains local maxima.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) For <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math>, there exists <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> attains local maxima.**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><msub><mi>n</mi><mn>1</mn></msub></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><msub><mi>n</mi><mn>2</mn></msub></msup></math></p><p>Differentiating the function to get maxima and minima, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>-</mo><mn>1</mn></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mrow><msub><mi>n</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>5</mn><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><msub><mi>n</mi><mn>2</mn></msub></mrow><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfrac></mrow></mfenced></math></p><p>Now checking the option, we get</p><p>Option (3) is incorrect since</p><p>for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>8</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><msup><mrow></mrow><mn>4</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>30</mn><mn>8</mn></mfrac></mrow></mfenced></math></p><p>minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>30</mn><mn>8</mn></mfrac></math>.</p>

</details>

---

### Q45. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mi mathvariant="normal">m</mi></math> is to be cut into two pieces. One of the pieces is to be made into a square and the other into an equilateral triangle. Then, the length of the side of the equilateral triangle, so that the combined area of the square and the equilateral triangle is minimum, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mrow><mn>9</mn><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>66</mn><mrow><mn>9</mn><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mrow><mn>4</mn><mo>+</mo><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>66</mn><mrow><mn>4</mn><mo>+</mo><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>66</mn><mrow><mn>9</mn><mo>+</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let the side of square be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>22</mn><mo>-</mo><mi>l</mi></mrow><mn>4</mn></mfrac></math> and side of triangle be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>l</mi><mn>3</mn></mfrac></math> ,</p><p>So, total area is given by  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><msup><mfenced><mfrac><mi>l</mi><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mfrac><mrow><mn>22</mn><mo>-</mo><mi>l</mi></mrow><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>12</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>&#183;</mo><msup><mi>l</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><msup><mfenced><mrow><mn>22</mn><mo>-</mo><mi>l</mi></mrow></mfenced><mn>2</mn></msup></math></p><p>Differentiating with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> to get maxima and minima points,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>&#916;</mi></mrow><mrow><mi>d</mi><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>&#183;</mo><mi>l</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced><mrow><mn>22</mn><mo>-</mo><mi>l</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>l</mi><mo>=</mo><mfrac><mrow><mn>66</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p>Also<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>&#916;</mi></mrow><mrow><mi>d</mi><msup><mi>l</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>6</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>ve</mi></math>. which is case of minima)</p><p>So, side of triangle will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>l</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>22</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>4</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>66</mn><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>9</mn></mrow></mfrac></math></p>

</details>

---

### Q46. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> respectively are the number of local maximum and local minimum points of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>+</mo><msup><mi>e</mi><mi>t</mi></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math>, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>m</mi><mo>,</mo><mi>n</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><msup><mi>x</mi><mn>2</mn></msup></msubsup><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>t</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>+</mo><msup><mi>e</mi><mi>t</mi></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p>We know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msubsup><mo>&#8747;</mo><mrow><mi>u</mi><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>v</mi><mfenced><mi>x</mi></mfenced></mrow></msubsup><mi>f</mi><mfenced><mi>v</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>f</mi><mfenced><mrow><mi>v</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>v</mi><mfenced><mi>u</mi></mfenced><mo>-</mo><mi>f</mi><mfenced><mrow><mi>u</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>u</mi><mfenced><mi>x</mi></mfenced></math></p><p>Using above formula we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>+</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mrow></mfrac></mfenced><mo>&#183;</mo><mn>2</mn><mi>x</mi></math></p><p>For critical points <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now by first derivative test we get,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d2de56a-3802-46ed-8b58-cf6d40fcc779-image.png" style="width: 300px; height: 41px;" /></p><p>Here points of maxima are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>  &amp; points of minima are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q47. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The lengths of the sides of a triangle are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></math>. If for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>k</mi></math>, the area of the triangle is maximum, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p>Area of triangle, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><msqrt><mn>20</mn><mfenced><mrow><mn>20</mn><mo>-</mo><mn>10</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>20</mn><mo>-</mo><mn>10</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>20</mn><mo>-</mo><mn>20</mn><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mo>=</mo><mn>2</mn><msqrt><mn>10</mn></msqrt><mi>x</mi><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>For maxima, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>&#916;</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><msqrt><mn>10</mn></msqrt><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>4</mn><msqrt><mn>10</mn></msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mo>&#8710;</mo></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q48. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider a cuboid of sides <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>,</mo><mn>4</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi></math> and a closed hemisphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>. If the sum of their surface areas is constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, then the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo><mi>r</mi></math>, for which the sum of their volumes is maximum, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>:</mo><mn>45</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>:</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>:</mo><mn>15</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>:</mo><mn>45</mn></math>**

**Detailed Solution:**

<p>Let sum of surface area</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>76</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>k</mi></math> is constant so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>k</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>6</mn><mi>&#960;</mi><mi>r</mi><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>76</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>76</mn><mi>x</mi></mrow><mrow><mn>3</mn><mi>&#960;</mi><mi>r</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now total volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mn>40</mn><msup><mi>x</mi><mn>3</mn></msup></math></p><p>For maximum volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>120</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mfenced><mrow><mo>-</mo><mfrac><mrow><mn>76</mn><mi>x</mi></mrow><mrow><mn>3</mn><mi>&#960;</mi><mi>r</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>120</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>8</mn><mi>x</mi><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mrow><mn>19</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mn>15</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mi>x</mi><mi>r</mi></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>45</mn></mfrac></math></p>

</details>

---

### Q49. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the absolute minimum and the absolute maximum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mn>3</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>x</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>5</mn></mrow><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable columnalign="left" columnspacing="1.4ex"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>,</mo></mtd><mtd><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></mtd></mtr><mtr><mtd><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>)</mo></mtd></mtr></mtable></mfenced></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mfrac><mrow><mn>3</mn><mo>-</mo><msqrt><mn>17</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p>Hece, absolute minimum value <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>and absolute maximum value <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn></math></p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mfrac><mrow><msqrt><mn>17</mn></msqrt><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p>

</details>

---

### Q50. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> are respectively the number of points of local minimum and local maximum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>M</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mfenced><mrow><mi>x</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>,</mo></mtd><mtd><mn>3</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></mtd><mtd><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>3</mn><mo>+</mo></msup></mfenced><mo>&#62;</mo><mn>0</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>3</mn><mo>-</mo></msup></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#8594;</mo></math> Minimum</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>1</mn><mo>+</mo></msup></mfenced><mo>&#62;</mo><mn>0</mn><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><msup><mn>1</mn><mo>-</mo></msup></mfenced><mo>&#60;</mo><mn>0</mn><mo>&#8594;</mo></math> Minimum</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> at one point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo></math> Maximum</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>0</mn></math></p><p>So points of minima are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn></math></p><p>and point of maxima is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q51. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of absolute maximum and absolute minimum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mrow><mi>sin</mi><mfenced><mn>1</mn></mfenced><msup><mi>cos</mi><mn>2</mn></msup><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced></mrow><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mi>sin</mi><mfenced><mn>1</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>sin</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>sin</mi><mfenced><mn>2</mn></mfenced></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mi>sin</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>cos</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced><mi>sin</mi><mfenced><mn>1</mn></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>4</mn></mfrac><mo>,</mo></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>4</mn></mfrac><mo>,</mo></mtd><mtd><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>1</mn></mrow></mfenced><mi>sin</mi><mn>1</mn></math></p>

</details>

---

### Q52. JEE Main 2021 (31 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a cubic polynomial with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>6</mn><mo>,</mo></math> and has a local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></math> has a local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced></math> is equal to <u>              </u> .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **22**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>x</mi><mo>+</mo><mi>d</mi></math></p><p>Diff w. r. t.  &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>&#39;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Again diff. w. r. t.  &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>&#39;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><mi>a</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>3</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mo>+</mo><mn>6</mn><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mo>-</mo><mn>9</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>10</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mo>-</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>6</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>-</mo><mfenced><mi>ii</mi></mfenced></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mo>-</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi><mo>-</mo><mn>5</mn></math></p><p>Hence,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>27</mn><mo>+</mo><mn>27</mn><mo>-</mo><mn>27</mn><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>22</mn></math></p>

</details>

---

### Q53. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> respectively be the maximum and minimum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>)</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>(</mo><mi>M</mi><mo>-</mo><mi>m</mi><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given, the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>)</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>
Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8804;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>&#8804;</mo><msqrt><mn>2</mn></msqrt><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>,</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><msqrt><mn>2</mn></msqrt><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>(</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>(</mo><mi>M</mi><mo>-</mo><mi>m</mi><mo>)</mo><mo>=</mo><mn>3</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q54. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>A box open from top is made from a rectangular sheet of dimension <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#215;</mo><mi>b</mi></math> by cutting squares each of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from each of the four corners and folding up the flaps. If the volume of the box is maximum, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>6</mn></mfrac></math>**

**Detailed Solution:**

<p>Given that:  A box open from top is made from a rectangular sheet dimension <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#215;</mo><mi>b</mi></math> by cutting squares each of side <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> from each of the four corners and folding up the flaps and the volume of the box is maximum.</p><p>dimensions of the box:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mi>a</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mi>b</mi><mo>-</mo><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>H</mi><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>L</mi><mo>&#215;</mo><mi>B</mi><mo>&#215;</mo><mi>H</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>)</mo><mo>(</mo><mi>b</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>x</mi><mo>)</mo><mo>&#160;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><mi>b</mi><mi>x</mi></math></p><p>For volume to be maximum:
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>V</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo><mi>x</mi><mo>+</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>)</mo><mo>-</mo><msqrt><mn>16</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>a</mi><mi>b</mi></msqrt></mrow><mn>24</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>+</mo><mo>&#160;</mo><mi>cannot</mi><mo>&#160;</mo><mi>be</mi><mo>&#160;</mo><mi>taken</mi><mo>&#160;</mo><mi>as</mi><mo>&#160;</mo><mi>x</mi><mo>&#60;</mo><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>,
for maximum volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><msqrt><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi></msqrt></mrow><mn>6</mn></mfrac></math></p>

</details>

---

### Q55. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is to be cut into two pieces. One of the pieces is to be made into a square and the other into a regular hexagon. Then the length of the side (in meters) of the hexagon, so that the combined area of the square and the hexagon is minimum, is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mrow><mn>2</mn><mo>+</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mrow><mn>3</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let the wire is cut into 2 pieces of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>20</mn><mo>-</mo><mi>y</mi></math></p><p>Therefore side of square will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>y</mi><mn>4</mn></mfrac></math> and hexagon will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mi>y</mi></mrow><mn>6</mn></mfrac></math></p><p>Area of square<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mi>y</mi><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p>Area of hexagon<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><msup><mfenced><mfrac><mrow><mn>20</mn><mo>-</mo><mi>y</mi></mrow><mn>6</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p>Total area<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>16</mn></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>20</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mrow><mn>24</mn></mfrac></math></p><p>On differentiating,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mfenced><mi>y</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mn>16</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>20</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mfenced><mi>y</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>a</mi><mi>t</mi><mo>&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>40</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p>Length of side of regular hexagon<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced><mrow><mn>20</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced><mrow><mn>20</mn><mo>-</mo><mfrac><mrow><mn>40</mn><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>10</mn><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p>

</details>

---

### Q56. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The local maximum value of the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>4</mn><msqrt><mi>e</mi></msqrt></mfrac></mfenced><mfrac><mi>e</mi><mn>4</mn></mfrac></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>e</mi><msup><mo>)</mo><mfrac><mn>2</mn><mi>e</mi></mfrac></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><msqrt><mi>e</mi></msqrt><msup><mo>)</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>e</mi><msup><mo>)</mo><mfrac><mn>2</mn><mi>e</mi></mfrac></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> for maximum value
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>ln</mi><mfrac><mn>2</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>y</mi></mfrac><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><mn>2</mn><mi>x</mi><mi>ln</mi><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mfrac><mn>1</mn><mfrac><mn>2</mn><mi>x</mi></mfrac></mfrac><mo>&#215;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><mo>(</mo><mi>x</mi><mi>y</mi><mo>)</mo><mfenced><mrow><mn>2</mn><mi>ln</mi><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><msup><mi>x</mi><mn>2</mn></msup></msup><mfenced><mi>x</mi></mfenced><mfenced><mrow><mn>2</mn><mi>ln</mi><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>ln</mi><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p>Then maximum value will be
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></mfrac></mfenced><mrow><mn>4</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mfrac><mn>2</mn><mi>e</mi></mfrac></msup></math></p>

</details>

---

### Q57. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mo>&#160;</mo><mi mathvariant="normal">m</mi></math> is cut into two pieces, one of the pieces is bent to form a square and the other is bent to form a circle. If the sum of the areas of the two figures is minimum, and the circumference of the circle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> (meter), then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>4</mn><mi>&#960;</mi></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mi>k</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<p>Let the side of square be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and radius of circle be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/db4e68c5-a3d7-402c-9687-0c4fee5a9738-image.png" style="width: 348px; height: 150px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#960;</mi><mi>y</mi><mo>=</mo><mn>36</mn></math> (given)</p><p>Area, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#960;</mi><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>&#960;</mi><msup><mfenced><mfrac><mrow><mn>36</mn><mo>-</mo><mn>4</mn><mi>x</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8658;</mo><mi>A</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mi>&#960;</mi></mfrac><msup><mfenced><mrow><mn>18</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>&#960;</mi></mfrac><mfenced><mrow><mn>18</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi><mi>x</mi><mo>+</mo><mo>(</mo><mn>36</mn><mo>-</mo><mn>4</mn><mi>x</mi><mo>)</mo><mo>(</mo><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mi>&#960;</mi></mfrac></math></p><p>For critical points</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#960;</mi><mi>x</mi><mo>-</mo><mn>72</mn><mo>+</mo><mn>8</mn><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>36</mn><mrow><mi>&#960;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>A</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mn>8</mn><mi>&#960;</mi></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>A</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p>Hence, area is minimized.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>18</mn><mrow><mi>&#960;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> [circumference of circle)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>&#960;</mi><mi>y</mi><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>36</mn><mi>&#960;</mi></mrow><mrow><mo>(</mo><mi>&#960;</mi><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced><mfrac><mrow><mn>4</mn><mo>+</mo><mi>&#960;</mi></mrow><mi>&#960;</mi></mfrac></mfenced><mo>&#215;</mo><mi>k</mi><mo>=</mo><mn>36</mn></math></p>

</details>

---

### Q58. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>If a rectangle is inscribed in an equilateral triangle of side length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math> as shown in the figure, then the square of the largest area of such a rectangle is _____.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1ad3b0a2-a500-4ced-aa96-c4d85192c510-image.png" style="width: 210px; height: 141px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d3836c55-89f3-4bed-8b32-74fba6e55210-image.png" style="width: 236px; height: 179px;" /></p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>D</mi><mi>B</mi><mi>F</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mn>60</mn><mo>&#176;</mo><mo>=</mo><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mi>&#8467;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mi>&#8467;</mi></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo></math>Area of rectangle</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#8467;</mi><mo>&#215;</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>&#8467;</mi><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mi>&#8467;</mi></mrow></mfenced></math></p><p>On differentiating, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>&#8467;</mi></mrow></mfrac><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mi>&#8467;</mi></mrow></mfenced><mo>-</mo><mfrac><mrow><mi>&#8467;</mi><mo>&#183;</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#8467;</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>&#8467;</mi><mo>&#215;</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#215;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q59. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of all the local minimum values of the twice differentiable function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> defined by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mi>x</mi><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>1</mn></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>22</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>27</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>27</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mi>x</mi><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>iii</mi></mfenced></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>12</mn><mo>-</mo><mn>6</mn><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>9</mn></math></p><p>For maxima/minima, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>12</mn><mo>&#60;</mo><mn>0</mn></math> (maxima)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>12</mn><mo>&#62;</mo><mn>0</mn></math> (minima)</p><p>Again</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mi>x</mi><mo>+</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>27</mn><mo>-</mo><mn>27</mn><mo>-</mo><mn>9</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mo>-</mo><mn>27</mn></math></p>

</details>

---

### Q60. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> be a real number such that the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>15</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math> and decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>. Then the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>15</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> has a

**Options:**

- **(A)** local maximum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(B)** local minimum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(C)** local maximum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(D)** local minimum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) local maximum at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mo>-</mo><mn>15</mn></math></p><p>Graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is shown below as it is increasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced></math> and decreasing in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a1ad4593-f1e8-49d9-a19d-9941e3bb8310-image.png" style="width: 328px; height: 250px;" /></p><p>Then, abscissa of vertex is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>B</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mo>(</mo><mn>6</mn><mo>)</mo></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>15</mn></math></p><p>Local maxima exists at the vertex of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math>, whose abscissa is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>B</mi></mrow><mrow><mn>2</mn><mi>A</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mfenced><mfrac><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mrow><mo>-</mo><mn>8</mn></mrow></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q61. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><mi>j</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mi>i</mi><mo>-</mo><mi>j</mi></mrow></mfenced><mo>=</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>otherwise</mi><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math>
Let a function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>det</mo><mfenced><mi>A</mi></mfenced></math>. Then the sum of maximum and minimum values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>20</mn><mn>27</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>88</mn><mn>27</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>27</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>88</mn><mn>27</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>88</mn><mn>27</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><mi>j</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mi>i</mi><mo>-</mo><mi>j</mi></mrow></mfenced><mo>=</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>,</mo></mtd><mtd><mo>&#160;</mo><mi>otherwise</mi><mo>&#160;</mo></mtd></mtr></mtable></mfenced></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable columnspacing="1em" rowspacing="4pt" columnalign="center center center"><mtr><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>&#8722;</mo><mi>x</mi></mtd><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>x</mi><mfenced><mrow><mo>-</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mfenced separators="|"><mrow><mn>3</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math></p><p>For maxima or minima, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mo>&#8722;</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mn>6</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mn>6</mn><mo>&#183;</mo><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>16</mn><mo>&#62;</mo><mn>0</mn></math>( point of minima)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>'</mo><mo>'</mo></mrow></msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mn>6</mn><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>16</mn><mo>&#60;</mo><mn>0</mn></math> ( point of maxima)</p><p>Hence, required sum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>f</mi><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>4</mn><mo>+</mo><mfrac><mn>20</mn><mn>27</mn></mfrac><mo>=</mo><mo>&#8722;</mo><mfrac><mn>88</mn><mn>27</mn></mfrac></math></p>

</details>

---

### Q62. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be a real polynomial of degree <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> which vanishes at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> have local minima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, local maxima at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><mi>P</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>18</mn></math>, then the sum of all the coefficients of the polynomial <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is equal to ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>a</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>a</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mo>&#8747;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>a</mi><mfenced><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><mo>-</mo><mfrac><mn>27</mn><mn>3</mn></mfrac><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#8230;</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mn>1</mn></mrow><mn>1</mn></msubsup><mfenced><mrow><mi>a</mi><mfenced><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>18</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p> From <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><mi>a</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>9</mn></math></p><p>Then, the Sum of coefficient<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q63. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>]</mo><mo>&#8594;</mo><mi>R</mi></math> be defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math> and for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> then the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo><mo>&#8594;</mo><mi>R</mi><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>a</mi></math></p><p>Given the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2</mn><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo></math></p><p>From the equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mfrac><mn>13</mn><mn>4</mn></mfrac><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>13</mn><mn>4</mn></mfrac></math></p><p>We know that, the vertex of the quadratic <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mi>x</mi><mo>+</mo><mi>C</mi></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mi>B</mi><mrow><mn>2</mn><mi>A</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mo>-</mo><mfrac><mrow><msup><mi>B</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>A</mi><mi>C</mi></mrow><mrow><mn>4</mn><mi>A</mi></mrow></mfrac></mrow></mfenced></math></p><p>Thus, the vertex of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>13</mn><mn>4</mn></mfrac></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> hence both the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#177;</mo><mn>1</mn></math> are on the same side of the vertex and the graph of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is given below.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5eb634b9-30f6-4753-a1ba-cd58f4616035-143.png" style="width: 353px; height: 187px;" /></p><p>For, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>]</mo><mo>,</mo></math> we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#8804;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#8804;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q64. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

The maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> in the following equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>&#8804;</mo><mn>100</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>&#8804;</mo><mn>75</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8805;</mo><mn>0</mn></math>
is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **904**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4cf86571-2d68-4e27-9557-765533d8e6f1-image.png" style="width: 347px; height: 315px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>y</mi><mo>(</mo><mn>6</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>&#8804;</mo><mn>100</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>&#8804;</mo><mn>75</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8804;</mo><mfrac><mrow><mn>75</mn><mo>-</mo><mn>3</mn><mi>y</mi></mrow><mn>4</mn></mfrac></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>y</mi><mo>(</mo><mn>6</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>&#8804;</mo><mi>y</mi><mfenced><mrow><mn>6</mn><mo>&#183;</mo><mfenced><mfrac><mrow><mn>75</mn><mo>-</mo><mn>3</mn><mi>y</mi></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><mi>y</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>z</mi><mo>&#8804;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>225</mn><mi>y</mi><mo>-</mo><mn>7</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>Now range of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>225</mn><mi>y</mi><mo>-</mo><mn>7</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mfrac><mrow><mo>(</mo><mn>225</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>7</mn></mrow></mfrac><mo>]</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>&#8804;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>225</mn><mi>y</mi><mo>-</mo><mn>7</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>&#8804;</mo><mfrac><mrow><mo>(</mo><mn>225</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>7</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>50625</mn><mn>56</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8776;</mo><mn>904</mn><mo>.</mo><mn>0178</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8776;</mo><mn>904</mn><mo>.</mo><mn>02</mn></math></p><p>It will be attained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>225</mn><mn>14</mn></mfrac></math></p>

</details>

---

### Q65. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The triangle of maximum area that can be inscribed in a given circle of radius &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>&#39; is :

**Options:**

- **(A)** An equilateral triangle having each of its side of length <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mi>r</mi></math>.
- **(B)** An isosceles triangle with base equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi></math>.
- **(C)** An equilateral triangle of height <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mn>3</mn></mfrac></math>.
- **(D)** A right angle triangle having two of its sides of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) An equilateral triangle having each of its side of length <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mi>r</mi></math>.**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi><mo>=</mo><mi>r</mi><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>r</mi></math></p><p>base <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>B</mi><mi>C</mi><mo>=</mo><mn>2</mn><mi>r</mi><mi>cos</mi><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9c03992d-e7a7-4cc3-b03f-2781416020cb-image.png" style="width: 221px; height: 230px;" /></p><p>Area of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mi>A</mi><mi>B</mi><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>B</mi><mi>C</mi></mrow></mfenced><mo>.</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mi>r</mi><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>.</mo><mfenced><mrow><mi>r</mi><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>r</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced><mrow><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>.</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi mathvariant="normal">&#916;</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mi>cos</mi><mi>&#952;</mi><mfrac><mi>d</mi><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mfrac><mi>d</mi><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mfenced><mrow><mi>cos</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi mathvariant="normal">&#916;</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mi>cos</mi><mi>&#952;</mi><mfenced><mrow><mn>0</mn><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi mathvariant="normal">&#916;</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi mathvariant="normal">&#916;</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi><mo>-</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mi>sin</mi><mi>&#952;</mi><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>-</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced open="[" close="]"><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mfenced><mrow><mi>sin</mi><mi>&#952;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><mrow><msup><mi>r</mi><mn>2</mn></msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mi>sin&#952;</mi></mrow></mfenced></mrow><mo>&#9183;</mo></munder><mi>positive</mi></munder><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/88a6ea7f-0503-4361-8635-0dabdf2a9fee-image.png" style="width: 215px; height: 80px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi></math> is maximum where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">&#916;</mi><mi>max</mi></msub><mo>=</mo><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow><mn>4</mn></mfrac><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo></math> area of equilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#916;</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>r</mi></math>.</p>

</details>

---

### Q66. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<div>The maximum slope of the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>18</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>19</mn><mi>x</mi></math> occurs at the point</div>

**Options:**

- **(A)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mfrac><mn>21</mn><mn>2</mn></mfrac></mrow></mfenced></math></div>
- **(B)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></div>
- **(C)** <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>9</mn></mrow></mfenced></math></div>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <div><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></div>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>15</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>x</mi><mo>-</mo><mn>19</mn></math><p>Since, slope is maximum so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>30</mn><mi>x</mi><mo>+</mo><mn>36</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>3</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>12</mn><mi>x</mi><mo>-</mo><mn>30</mn></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mfrac><mrow><msup><mi>d</mi><mn>3</mn></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>&#60;</mo><mn>0</mn></math></p><p>So, maxima</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>16</mn><mo>-</mo><mn>5</mn><mo>&#215;</mo><mn>8</mn><mo>+</mo><mn>18</mn><mo>&#215;</mo><mn>4</mn><mo>-</mo><mn>19</mn><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>-</mo><mn>40</mn><mo>+</mo><mn>72</mn><mo>-</mo><mn>38</mn><mo>=</mo><mn>80</mn><mo>-</mo><mn>78</mn><mo>=</mo><mn>2</mn></math></p><p>point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q67. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a polynomial of degree <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> in which the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>6</mn></msup></math> is unity and it has extrema at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#183;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **144**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>c</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>d</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>e</mi><mi>x</mi><mo>+</mo><mi>f</mi></math><p>as <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mn>1</mn></math> non-zero finite</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mi>e</mi><mo>=</mo><mi>f</mi><mo>=</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Now, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>5</mn><mi>a</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mo>+</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>b</mi><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>6</mn><mo>+</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>=</mo><mn>3</mn></math></p><p>Solving both we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>5</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>6</mn></msup><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><msup><mi>x</mi><mn>5</mn></msup><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>5</mn><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>5</mn><mfenced close="]" open="["><mrow><mn>64</mn><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>&#183;</mo><mn>32</mn><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#183;</mo><mn>16</mn><mo>+</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>320</mn><mo>-</mo><mn>96</mn><mo>-</mo><mn>120</mn><mo>+</mo><mn>40</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>144</mn></math></p>

</details>

---

### Q68. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The set of all real values <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#955;</mi></math> for which the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>.</mo><mo>&#160;</mo><mfenced><mrow><mi mathvariant="normal">&#955;</mi><mo>+</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x&#949;</mi><mo>&#160;</mo><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>, has exactly one maxima and exactly one minima, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced open="{" close="}"><mn>0</mn></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>2</mn><mi>&#955;</mi><mo>+</mo><mn>3</mn><mi>sin</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p>(one point)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math>    .....(1)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mn>0</mn></mfenced></math></p>

</details>

---

### Q69. JEE Main 2020 (06 Sep Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math> be two vertical poles at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>B</mi></math> respectively on a horizontal ground. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>D</mi><mo>=</mo><mn>8</mn><mi mathvariant="normal">m</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>BC</mi><mo>=</mo><mn>11</mn><mi mathvariant="normal">m</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AB</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal">m</mi><mo>;</mo></math> then the distance (in meters) of a point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> lying in between  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AB</mi></math> from the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MD</mi><mn>2</mn></msup><mo>+</mo><msup><mi>MC</mi><mn>2</mn></msup></math> is minimums, is__

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a2314cf6-78cb-4691-b7ba-2c333c2e611b-image.png" style="width: 238px; height: 193px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AM</mi><mo>=</mo><mi mathvariant="normal">x</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>=</mo><msup><mi>MD</mi><mn>2</mn></msup><mo>+</mo><msup><mi>MC</mi><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>MD</mi><mn>2</mn></msup><mo>+</mo><msup><mi>MC</mi><mn>2</mn></msup><mo>=</mo><mn>64</mn><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mn>121</mn><mo>+</mo><mo>(</mo><mn>10</mn><mo>-</mo><mi mathvariant="normal">x</mi><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">S</mi><mo>=</mo><mn>285</mn><mo>-</mo><mn>20</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dS</mi><mi>dx</mi></mfrac><mo>=</mo><mo>-</mo><mn>20</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">x</mi><mo>&#8658;</mo><mfrac><mi>dS</mi><mi>dx</mi></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mi mathvariant="normal">S</mi></mrow><msup><mi>dx</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>4</mn><mo>=</mo><mo>+</mo><mi>ve</mi></math></p>

</details>

---

### Q70. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The area (in sq. units) of the largest rectangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> whose vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> lie on the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis and vertices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> lie on the parabola, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math> below the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>-axis, is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7368ac2b-44fe-4c9a-b81d-e3f11930a48d-image.png" style="width: 234px; height: 199px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>(</mo><mi>&#945;</mi><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mi>&#946;</mi><mo>(</mo><mo>-</mo><mi>&#945;</mi><mo>,</mo><mn>0</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi><mfenced><mrow><mi>&#945;</mi><mo>,</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>r</mi><mi>e</mi><mi>a</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi><mo>)</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>(</mo><mi>A</mi><mi>B</mi><mo>)</mo><mo>&#160;</mo><mo>(</mo><mi>A</mi><mi>D</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mo>(</mo><mn>2</mn><mi>&#945;</mi><mo>)</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>s</mi></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mo>-</mo><mn>6</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;Area&#160;</mtext><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>2</mn><msup><mi>&#945;</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>-</mo><mfrac><mn>2</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math></p><p> </p>

</details>

---

### Q71. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mi>x</mi></mfenced></math> be a polynomial of degree three that has a local maximum value <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and a local minimum value <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mn>0</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>**

**Detailed Solution:**

<p> Clearly <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>&#955;</mi><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>&#62;</mo><mn>0</mn></math></p><p>Integrating both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#955;</mi><mfenced close="]" open="["><mrow><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi>&#955;</mi><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>C</mi><mo>=</mo><mn>8</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mi>&#955;</mi></mrow><mn>6</mn></mfrac><mo>+</mo><mi>C</mi><mo>=</mo><mn>8</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>&#955;</mi><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mn>6</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>4</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#955;</mi><mo>+</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>By <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>12</mn></math></p>

</details>

---

### Q72. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let a function <math><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi></mi><mn>5</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be continuous, <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>3</mn></math> and <math><mi>F</mi></math> be defined as:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><mi>g</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced separators="|"><mi>t</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>t</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>u</mi></mfenced><mi>d</mi><mi>u</mi><mo>.</mo></math></p><p>Then for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced><mi>x</mi></mfenced><mo>,</mo></math> the point <math><mi>x</mi><mo>=</mo><mn>1</mn></math> is:</p>

**Options:**

- **(A)** a point of local minima
- **(B)** not a critical point
- **(C)** a point of local maxima
- **(D)** a point of inflection

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a point of local minima**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mi>x</mi></msubsup><msup><mi>t</mi><mn>2</mn></msup><mi>g</mi><mfenced separators="|"><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p>By Leibnitz rule we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>'</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>.</mo><mi>g</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math> <math><mfenced separators="|"><mrow><mo>&#8757;</mo><mi></mi><mi></mi><mi>g</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>F</mi><mo>''</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>''</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mi>g</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>&#8757;</mo><msup><mi>g</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>''</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>F</mi><mo>''</mo></msup><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math></p><p><math><mi>F</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> has a local minimum at <math><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q73. JEE Main 2020 (08 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>, be a polynomial of degree <math><mn>3</mn></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mo>,</mo><mtext>&#8201;</mtext><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mo>,</mo><mtext>&#8201;</mtext><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>, has a critical point at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>'</mo><mfenced><mi>x</mi></mfenced></math>, has a critical point at <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></math>, has local minima at <math><mi>x</mi><mo>=</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#34;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#955;</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Integrating both the side with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#955;</mi><mfrac><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#955;</mi><mfrac><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mn>2</mn><mi>&#955;</mi></math></p><p>Integrating both the side with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mi>&#955;</mi><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow><mn>6</mn></mfrac><mo>-</mo><mn>2</mn><mi>&#955;</mi><mi>x</mi><mo>+</mo><mi>u</mi></math></p><p>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#10233;</mo><mo>-</mo><mn>2</mn><mi>&#955;</mi><mo>+</mo><mi>u</mi><mo>=</mo><mo>-</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mo>&#10233;</mo><mfrac><mrow><mn>2</mn><mi>&#955;</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mi>u</mi><mo>=</mo><mn>10</mn></math>
<math><mo>&#8756;</mo><mi>&#955;</mi><mo>=</mo><mn>6</mn></math> and <math><mi>u</mi><mo>=</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#10233;</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> or <math><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mn>3</mn></mfenced><mo>&#62;</mo><mn>0</mn></math>
<math><mo>&#8756;</mo><mi>x</mi><mo>=</mo><mn>3</mn></math>, is a point of local minima.</p>

</details>

---

### Q74. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> be a polynomial of degree <math><mn>5</mn></math> such that <math><mi>x</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math> are its critical points. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>4</mn><mo>,</mo></math> then which one of the following is not true?

**Options:**

- **(A)** <math><mi>f</mi></math> is an odd function
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>-</mo><mn>4</mn><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn></math> . <math><mi>x</mi><mo>=</mo><mn>1</mn></math> is a point of maximum and <math><mi>x</mi><mo>=</mo><mi></mi><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>is a point of local minimum and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> is a point of local maximum
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a point of local maxima of <math><mi>f</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is a point of local maxima of <math><mi>f</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>c</mi><msup><mi>x</mi><mn>3</mn></msup></math></p><p>Consider, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mo>&#8289;</mo><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mfrac><mrow><mi>a</mi><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>c</mi><msup><mi>x</mi><mn>3</mn></msup></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>+</mo><mi>c</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p>Differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>5</mn><mi>a</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>5</mn><mi>a</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></math></p><p>Critical points of the function are given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#177;</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>+</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>5</mn><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>
Solving both we get, <math><mi>b</mi><mo>=</mo><mn>0</mn></math>, <math><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
So, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>+</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>
And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>6</mn><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math><mo>=</mo><mo>-</mo><mn>6</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Hence, local minima at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and local maxima at <math><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q75. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>5</mn><mo>-</mo><mo>|</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>|</mo></math> and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> <math><mi>x</mi><mtext>&#160;</mtext><mo>&#8712;</mo><mi>&#160;</mi><mi>R</mi><mo>.</mo></math> If <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> attains maximum value at <math><mi>&#945;</mi></math> and <math><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> attains minimum value at <math><mi>&#946;</mi><mo>,</mo></math> then <math><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mrow></munder><mfrac><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfenced></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>6</mn><mi>x</mi><mo>+</mo><mn>8</mn></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Maxima of <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> will occur at <math><mi>x</mi><mo>=</mo><mn>2</mn></math> i.e., <math><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p><p>Minima of <math><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> will occur at <math><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> i.e. <math><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math><mo>&#8756;</mo><mtext>&#8201;</mtext><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><mn>2</mn></mrow></munder><mfrac><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>-</mo><mn>4</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>.</p>

</details>

---

### Q76. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>m</mi></math> is the minimum value of <math><mi>k</mi></math> for which the function <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><msqrt><mi>k</mi><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mi>&#160;</mi></math> is increasing in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0,</mn><mo>&#160;</mo><mn>3</mn><mo>]</mo></math> and <math><mi>M</mi></math> is the maximum value of <math><mi>f</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0,</mn><mo>&#160;</mo><mn>3</mn><mo>]</mo></math> when <math><mi>k</mi><mo>=</mo><mi>m</mi><mo>,</mo></math> then the ordered pair <math><mo>(</mo><mi>m</mi><mo>,</mo><mi>&#160;</mi><mi>M</mi><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>4,</mn><mo>&#160;</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>5,</mn><mo>&#160;</mo><mn>3</mn><msqrt><mn>6</mn></msqrt></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>,</mo><mi> </mi><mn>3</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>4,</mn><mo>&#160;</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><msqrt><mi>k</mi><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math> <math><msup><mrow><mo>&#8658;</mo><mi>&#160;</mi><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mi>k</mi><mi>x</mi><mo>-</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msqrt><mi>k</mi><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></mrow></mfrac></math>
As per the given condition <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0,</mn><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mn>3</mn><mi>k</mi><mi>x</mi><mo>-</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8805;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0,</mn><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mn>3</mn><mi>k</mi><mo>-</mo><mn>4</mn><mi>x</mi><mi>&#160;</mi><mo>&#8805;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0,</mn><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>k</mi><mo>&#8805;</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced open="[" close="]" separators="|"><mrow><mn>0,</mn><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
<math><mo>&#8658;</mo><mi>k</mi><mo>&#8805;</mo><mn>4</mn></math> . So minimum value of <math><mi>k</mi></math> is <math><mi>m</mi><mo>=</mo><mn>4</mn><mo>.</mo></math>
Now <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><msqrt><mn>4</mn><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
Since given function in increasing hence maximum value will occur at <math><mi>x</mi><mo>=</mo><mn>3</mn></math>
<math><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>3</mn><msqrt><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>,</mo><mtext>&#8201;</mtext><mi>M</mi><mo>=</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
Hence <math><mo>(</mo><mi>m</mi><mo>,</mo><mi>&#160;</mi><mi>M</mi><mo>)</mo><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mo>(</mo><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>)</mo></math>

</details>

---

### Q77. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">e</mi></mrow><mrow><mi mathvariant="normal">x</mi></mrow></msup><mo>-</mo><mi mathvariant="normal">x</mi></math> and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi mathvariant="normal">x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi mathvariant="normal">x</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>&#8704;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">x</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#1013;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">R</mi></math> . Then the set of all <math><mi mathvariant="normal">x</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#1013;</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">R</mi></math> , where the function <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mi>f</mi><mi>o</mi><mi>g</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is increasing, is:

**Options:**

- **(A)** <math><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>⋃</mo><mfenced open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>∞</mi></mrow></mfenced></math>
- **(B)** <math><mo>[</mo><mn>0</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>
- **(C)** <math><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mo>[</mo><mn>1</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>
- **(D)** <math><mfenced open="[" close="]" separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced><mo>∪</mo><mo>[</mo><mn>1</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced open="[" close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>∪</mo><mo>[</mo><mn>1</mn><mo>,</mo><mi>∞</mi><mo>)</mo></math>**

**Detailed Solution:**

<math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mi>o</mi><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></msup><mo>-</mo><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>
<math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>h</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow></msup><mo>&#215;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
<math><mo>&#8757;</mo><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is increasing <math><mo>&#8756;</mo><msup><mrow><mi>h</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math> <math><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math>
Case 1: <math><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8805;</mo><mn>0</mn></math> &amp; <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>x</mi><mo>&#8805;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mo>&#38;</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#8734;</mi></mrow></mfenced><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced open="[" separators="|"><mrow><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced></math>
Case 2: <math><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi><mo>&#8804;</mo><mn>0</mn></math>
<math><mi>x</mi><mo>&#60;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> and <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math> <math><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>&#8746;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mi>&#8734;</mi><mo>)</mo></math>

</details>

---

### Q78. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is a non-zero polynomial of degree four, having local extreme points at <math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>;</mo></math> then the set <math><mi>S</mi><mo>=</mo><mo>{</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mi>&#160;</mi><mo>:</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>}</mo></math> contains exactly

**Options:**

- **(A)** Two irrational and two rational numbers
- **(B)** Four rational numbers
- **(C)** Two irrational and one rational number
- **(D)** Four irrational numbers

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Two irrational and one rational number**

**Detailed Solution:**

<p><math><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> has extreme points at <math><mo>{</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>}</mo></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mi>&#160;</mi></math> at <math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>&#8211;</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>x</mi><mi>&#160;</mi><mi>&#160;</mi><mo>&#8757;</mo><mi>f</mi><mi>&#160;</mi><mfenced separators="|"><mi>x</mi></mfenced></math> is a polynomial</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mo>&#8747;</mo><mi>a</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>a</mi><mfenced separators="|"><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>&#160;</mi><mi>C</mi></math></p><p>Now the equation,</p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo></math></p><p><math><mo>&#8658;</mo><mi>a</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>&#160;</mi><mi>C</mi><mo>=</mo><mi>C</mi></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>0</mn><mi>&#160;</mi><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mo>&#177;</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mi>&#160;</mi><mo>{</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><msqrt><mn>2</mn></msqrt><mo>,</mo><mi>&#160;</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>}</mo><mo>.</mo></math></p><p>Hence, the set contains two irrational and one rational number.</p>

</details>

---

### Q79. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The height of a right circular cylinder of maximum volume inscribed in a sphere of radius <math><mn>3</mn></math> is:

**Options:**

- **(A)** <math><mi mathvariant="normal"> </mi><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math><msqrt><mn>6</mn></msqrt></math>
- **(D)** <math><mn>2</mn><mi> </mi><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn><mi> </mi><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b882fa1c-9f7f-48a4-ac2a-f58516bee039-image1.png"> 
From the diagram, we get radius of cylinder <math><mo>=</mo><msqrt><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>  
<math><mo>⇒</mo></math> Volume of cylinder <math><mi>V</mi><mo>=</mo><mi>π</mi><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mi>h</mi></math>  
For maximum volume: <math><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>h</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>  
<math><mo>⇒</mo><mi>π</mi><mfenced separators="|"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><msup><mrow><mn>3</mn><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>⇒</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>×</mo><mn>9</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mn>12</mn></math>  
<math><mo>⇒</mo><mi>h</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

</details>

---

### Q80. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> be a twice differentiable function such that <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> for all <math><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn></mrow></mfenced><mo>.</mo></math> If <math><mi>&#981;</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>+</mo><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mrow><mn>2</mn><mo>&#8211;</mo><mi>x</mi></mrow></mfenced><mo>,</mo></math> then <math><mi>&#981;</mi></math> is

**Options:**

- **(A)** decreasing on <math><mfenced separators="|"><mrow><mn>0,2</mn></mrow></mfenced><mi> </mi></math>
- **(B)** increasing on <math><mfenced separators="|"><mrow><mn>0,2</mn></mrow></mfenced><mi> </mi></math>
- **(C)** increasing on <math><mo>(</mo><mn>0,1</mn><mo>)</mo></math> and decreasing on <math><mfenced separators="|"><mrow><mn>1,2</mn></mrow></mfenced><mi> </mi></math>
- **(D)** decreasing on <math><mfenced separators="|"><mrow><mn>0,1</mn></mrow></mfenced><mi> </mi></math> and increasing on <math><mo>(</mo><mn>1,2</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreasing on <math><mfenced separators="|"><mrow><mn>0,1</mn></mrow></mfenced><mi> </mi></math> and increasing on <math><mo>(</mo><mn>1,2</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>:</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0,2</mn></mrow></mfenced><mo>&#8594;</mo><mi>R</mi></math> and <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mi>&#160;</mi><mn>0</mn><mi>&#160;</mi></math> for <math><mi>x</mi><mo>&#8712;</mo><mi>&#160;</mi><mo>[</mo><mn>0,2</mn><mo>]</mo></math>
    <math><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi mathvariant="normal">&#39;</mi></mrow></msup><mo>(</mo><mi>x</mi><mo>)</mo></math> is increasing for <math><mi>x</mi><mo>&#8712;</mo><mi>&#160;</mi><mo>[</mo><mn>0,2</mn><mo>]</mo></math>
Now, <math><mi>&#981;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>f</mi><mo>(</mo><mn>2</mn><mo>-</mo><mi>x</mi><mo>)</mo></math>
    <math><mo>&#8658;</mo><msup><mrow><mi>&#981;</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>-</mo><mi>f</mi><mi>&#39;</mi><mo>(</mo><mn>2</mn><mo>-</mo><mi>x</mi><mo>)</mo></math>
For <math><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>&#160;</mi><mo>[</mo><mn>0,1</mn><mo>)</mo></math> , <math><mi>x</mi><mi>&#160;</mi><mo>&#60;</mo><mi>&#160;</mi><mn>2</mn><mi>&#160;</mi><mo>&#8211;</mo><mi>&#160;</mi><mi>x</mi></math>  </p><p>    <math><mo>&#8658;</mo><mi>f</mi><mi>&#39;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#60;</mo><mi>f</mi><mi>&#39;</mi><mo>(</mo><mn>2</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>&#8658;</mo><mi>&#981;</mi><mi>&#39;</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>&#60;</mo><mn>0</mn></math>
For <math><mi>x</mi><mo>&#8712;</mo><mi>&#160;</mi><mo>(</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mo>]</mo></math> , <math><mi>x</mi><mi>&#160;</mi><mo>&#62;</mo><mi>&#160;</mi><mn>2</mn><mi>&#160;</mi><mo>&#8211;</mo><mi>&#160;</mi><mi>x</mi></math></p><p>    <math><mo>&#8658;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>&#8658;</mo><msup><mrow><mi>&#981;</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math>
Hence, <math><mi>&#981;</mi></math> is decreasing on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and increasing on <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math>.</p>

</details>

---

### Q81. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are respectively the sets of local minimum and local maximum points of the function, <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>12</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>36</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then

**Options:**

- **(A)** <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>{</mo><mn>0,1</mn><mo>}</mo></math>
- **(B)** <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mn>0,2</mn></mrow></mfenced></math>
- **(C)** <math><msub><mrow><mi> </mi><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2,0</mn></mrow></mfenced><mo>;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>{</mo><mn>1</mn><mo>}</mo></math>
- **(D)** <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2,1</mn></mrow></mfenced><mo>;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced open="{" close="}" separators="|"><mrow><mo>-</mo><mn>2,1</mn></mrow></mfenced><mo>;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mo>{</mo><mn>0</mn><mo>}</mo></math>**

**Detailed Solution:**

<p><math><mi>y</mi><mo>=</mo><mn>9</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>12</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>36</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>25</mn></math></p><p>Differentiating,</p><p><math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>36</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>36</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>72</mn><mi>x</mi></math>
       <math><mo>=</mo><mn>36</mn><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>       <math><mo>=</mo><mn>36</mn><mi>x</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Sign convention for <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4a85f398-3cbf-4e3c-a03e-856879ee773e-image3.png" />
<math><mo>&#8756;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mn>2,1</mn></mrow></mfenced></math> <math><mo>&#38;</mo><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q82. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum area (in sq. units) of a rectangle having its base on the <math><mi>x</mi><mo>-</mo></math> axis and its other two vertices on the parabola, <math><mi>y</mi><mo>=</mo><mn>12</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> such that the rectangle lies inside the parabola, is :

**Options:**

- **(A)** <math><mn>20</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>32</mn></math>
- **(C)** <math><mn>36</mn></math>
- **(D)** <math><mn>18</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>32</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dmrdtymthvjqmzwgdbtglfmvyiivqejeqzztzqmkgkclvokzaa.png" /></p><p>Since, given parabola is symmetric about the <math><mi>y</mi><mo>-</mo></math> axis, hence rectangle will also be symmetric about <math><mi>y</mi><mo>-</mo></math> axis.</p><p>Let one vertex of the rectangle on the <math><mi>x</mi><mo>-</mo></math> axis be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math>, then</p><p>Area of rectangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>.</mo><mfenced separators="|"><mrow><mn>12</mn><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>Differentiating both sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>24</mn><mo>-</mo><mn>6</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mtext>&#8201;</mtext><mo>-</mo><mn>2</mn></math></p><p>For area to be maximum, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn></math> in the equation for area of the rectangle, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mfenced><mrow><mn>12</mn><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q83. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x, y$ be positive real numbers and $m, n$ positive integers.

The maximum value of the expression $\frac{x^{\mathrm{m}} y^{\mathrm{n}}}{\left(1+x^{2 \mathrm{~m}}\right)\left(1+y^{2 \mathrm{n}}\right)}$

is :

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{m+n}{6 m n}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

$A=\frac{x^{m} y^{n}}{\left(1+x^{2 m}\right)\left(1+y^{2 n}\right)}=\frac{1}{\left(x^{-m}+x^{m}\right)\left(y^{-n}+y^{n}\right)}$

$\frac{x^{m}+y^{-m}}{2} \geq\left(x^{n+1}, x^{-m}\right)^{\frac{1}{2}} \Rightarrow x^{n+}+x^{-n} \geq 2$

In the same way, $y^{n}+y^{n} \geq 2$

Then $,\left(x^{n}+x^{-n}\right)\left(y^{-n}+y^{n}\right) \geq 4$

$\Rightarrow \frac{1}{\left(x^{\text {"1 }}+x^{-m}\right)\left(y^{-n}+y^{n}\right)} \leq \frac{1}{4}$

</details>

---

### Q84. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Themaximum value of the finction $f(x)=3 x^{3}-18 x^{2}+27 x-40$

on the set $\mathrm{S}=\left\{x \in R: x^{2}+30 \leq 11 x\right\}$ is :

**Options:**

- **(A)** -122
- **(B)** -222
- **(C)** 122
- **(D)** 222

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 122**

**Detailed Solution:**

Consider the function,

$f(x)=3 x(x-3)^{2}-40$

$\operatorname{Now} S=\left\{x \in \infty k: x^{2}+30 \leq 11 x\right\}$

So $x^{2}-11 x+30 \leq 0 \quad \Rightarrow \quad x \circ \in[5,6]$

$\therefore f(x)$ will have maximum value for $x=6$ The maximum value of function is,

$f(6)=3 \times 6 \times 3 \times 3-40=122$

</details>

---

### Q85. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The maximum volume <math><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#160;</mi><mi>c</mi><mi>u</mi><mo>.</mo><mi>m</mi></mrow></mfenced></math> of the right circular cone having slant height <math><mn>3</mn><mi>&#160;</mi><mi>m</mi></math> is:

**Options:**

- **(A)** <math><mn>2</mn><msqrt><mn>3</mn></msqrt><mi> </mi><mi>π</mi></math>
- **(B)** <math><mn>3</mn><msqrt><mn>3</mn></msqrt><mi> </mi><mi>π</mi></math>
- **(C)** <math><mn>6</mn><mi> </mi><mi>π</mi></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>2</mn><msqrt><mn>3</mn></msqrt><mi> </mi><mi>π</mi></math>**

**Detailed Solution:**

Given  <math><mi>l</mi><mo>=</mo><mn>3</mn></math> 

         <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bhsukapptpexeowjogqerqpmrmkikfycbcltnwvsfhexuhkppz.png" /> 

         <math><mo>⇒</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>9</mn></math> 

        Volume,  <math><mi>V</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>h</mi></math> 

         <math><mo>⇒</mo><mi>V</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mfenced separators="|"><mrow><mn>9</mn><mo>-</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>h</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mfenced separators="|"><mrow><mn>9</mn><mi>h</mi><mo>-</mo><msup><mrow><mi>h</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></math> 

         <math><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>h</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mfenced separators="|"><mrow><mn>9</mn><mo>-</mo><mn>3</mn><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> 

         <math><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>h</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>h</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math>     

         <math><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>V</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>h</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mfenced separators="|"><mrow><mo>-</mo><mn>6</mn><mi>h</mi></mrow></mfenced><mo>&lt;</mo><mn>0</mn></math> 

         <math><mo>∴</mo></math>  at  <math><mi>h</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math> , cone has maximum volume

         <math><mo>∴</mo></math>   <math><msub><mrow><mi>V</mi></mrow><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">x</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>π</mi><mfenced separators="|"><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>3</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt><mi>π</mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>3</mn></mrow></msup></math>

</details>

---

### Q86. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be respectively the absolute maximum and the absolute minimum values of the function, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>5</mn></math> in the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>]</mo></math> . Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>9</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>5</mn><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p>Differentiating w.r.t <math><mi>x</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>x</mi><mo>+</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mi>&#8242;</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>6</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p>For maxima/minima <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>12</mn><mi>x</mi><mo>-</mo><mn>18</mn></math></p><p>So at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>and at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>So, for absolute maxima/minima</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>5</mn></math></p><p><math><mo>&#8756;&#160;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q87. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)$ be a polynomial of degree 4 having extreme values at $x=1$ and $x=2$.
If $\lim _{x \rightarrow 0}\left(\frac{f(x)}{x^2}+1\right)=3$ then $f(-1)$ is equal to

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{2}$
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{2}$**

**Detailed Solution:**

$\because f(x)$ has extremum values at $x=1$ and $x=2$
$\because f^{\prime}(1)=0$ and $f^{\prime}(2)=0$
As, $f(x)$ is a polynomial of degree 4 .
Suppose $f(x)=A x^4+B x^3+C x^2+D x+E$
$$
\begin{aligned}
&\because \lim _{x \rightarrow 0}\left(\frac{f(x)}{x^2}+1\right)=3 \\
&\Rightarrow \lim _{x \rightarrow 0}\left(\frac{A x^4+B x^3+C x^2+D x+E}{x^2}+1\right)=3 \\
&\Rightarrow \lim _{x \rightarrow 0}\left(A x^2+B x+C+\frac{D}{x}+\frac{E}{x^2}+1\right)=3
\end{aligned}
$$
As limit has finite value, so $D=0$ and $E=0$
Now $A(0)^2+B(0)+C+0+0+1=3$
$$
\begin{aligned}
&\Rightarrow c+1=3 \Rightarrow c=2 \\
&f^{\prime}(x)=4 A x^3+3 B x^2+2 C x+D \\
&f^{\prime}(1)=0 \Rightarrow 4 A(1)+3 B(1)+2 C(1)+D=0
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow 4 A+3 B=-4 \\
f^{\prime}(2)=0 & \Rightarrow 4 A(8)+3 B(4)+2 C(2)+D=0 \\
& \Rightarrow 8 A+3 B=-2
\end{aligned}
$$
From equations (1) and (2), we get $A=\frac{1}{2}$ and $B=-2$
So, $f(x)=\frac{x^4}{2}-2 x^3+2 x^2$
Therefore, $f(-1)=\frac{(-1)^4}{2}-2(-1)^3+2(-1)^2$
$$
=\frac{1}{2}+2+2=\frac{9}{2}
$$
Hence $f(-1)=\frac{9}{2}$

</details>

---

### Q88. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)$ is a quadratic expression such that $f(1)+f$ (2) $=0$, and $-1$ is a root of $f(x)=0$, then the other root of $f(x)=0$ is

**Options:**

- **(A)** $-\frac{5}{8}$
- **(B)** $-\frac{8}{5}$
- **(C)** $\frac{5}{8}$
- **(D)** $\frac{8}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{8}{5}$**

**Detailed Solution:**

If $a$ and $-1$ are the roots of the polynomial, then we get
$$
\begin{aligned}
& f(x)=x^2+(1-a) x-a . \\
\therefore \quad & f(1)=2-2 a \\
\text { and } & f(2)=6-3 a \\
\text { As, } & f(1)+f(2)=0 \\
\Rightarrow & 2-2 a+6-3 a=0 \Rightarrow a=\frac{8}{5}
\end{aligned}
$$
Therefore, the other root is $\frac{8}{5}$

</details>

---

### Q89. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If a right circular cone, having maximum volume, is inscribed in a sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>c</mi><mi>m</mi></math>, then the curved surface area (in <math><msup><mrow><mi>cm</mi></mrow><mrow><mn>2</mn></mrow></msup></math>) of this cone is :

**Options:**

- **(A)** <math><mn>8</mn><msqrt><mn>2</mn></msqrt><mi>π</mi></math>
- **(B)** <math><mn>6</mn><msqrt><mn>2</mn></msqrt><mi>π</mi></math>
- **(C)** <math><mn>8</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></math>
- **(D)** <math><mn>6</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>8</mn><msqrt><mn>3</mn></msqrt><mi>π</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4d2e04ca-3c6e-4b36-a75e-8886c2a909b3-image.png" style="width: 233px; height: 250px;" /></p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi>A</mi><mi>M</mi><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>A</mi><mi>M</mi><mo>=</mo><mn>3</mn><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>M</mi><mi>C</mi><mo>=</mo><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mi>h</mi></math> where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is radius and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math> is height of cone</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>V</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mfenced separators="|"><mrow><mn>3</mn><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>3</mn><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mrow></mfenced></math></p><p>(since, radius of cone <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>A</mi><mi>M</mi></math> and height of cone <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>M</mi><mi>C</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>V</mi><mo>=</mo><mi>&#960;</mi><mfenced><mrow><mn>36</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mo>&#160;</mo><mspace linebreak="newline"></mspace><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi><mo>=</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>72</mn><mi>&#960;</mi><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>4</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></math></p><p>Differentiating both sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>72</mn><mi>&#960;</mi><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>5</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>3</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>3</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced></math></p><p>For maximum value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>&#952;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>72</mn><mi>&#960;</mi><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>5</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>-</mo><mn>4</mn><msup><mi>sin</mi><mn>3</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>3</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>tan</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Thus, volume is maximum when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mo>&#8289;</mo><mi>&#952;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p>Hence, curved surface area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mi>&#960;</mi><mi>r</mi><mi>l</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mi>r</mi><msqrt><msup><mfenced separators="|"><mrow><mn>3</mn><mo>+</mo><mn>3</mn><mi>cos</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mrow><mo>(</mo><mn>3</mn><mi>sin</mi><mo>&#8289;</mo><mrow><mn>2</mn><mi>&#952;</mi><mo>)</mo></mrow></mrow><mn>2</mn></msup></msqrt><mo>&#160;</mo><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mi>l</mi><mo>=</mo><msqrt><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>h</mi><mn>2</mn></msup></msqrt></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mfenced separators="|"><mrow><mn>3</mn><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><msqrt><mn>36</mn><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></msqrt><mo>=</mo><mn>18</mn><mi>&#960;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn><mi>&#960;</mi><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>.</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>24</mn><mi>&#960;</mi></mrow><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mn>8</mn><msqrt><mn>3</mn></msqrt><mi>&#960;</mi></math></p>

</details>

---

### Q90. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

If a right circularcone having maximum volume, is inscribed in a sphere of radius $3 \mathrm{~cm}$, then the curved surface area (in $\mathrm{cm}^2$ ) of this cone is

**Options:**

- **(A)** $8 \sqrt{3} \pi$
- **(B)** $6 \sqrt{2} \pi$
- **(C)** $6 \sqrt{3} \pi$
- **(D)** $8 \sqrt{2} \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8 \sqrt{3} \pi$**

**Detailed Solution:**

Sphere of radius $r=3 \mathrm{~cm}$
Let $b, h$ be base radius and height of cone respectively.
So, volume of cone $=\frac{1}{2} \pi b^2 h$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/lmA4uNjlVcHFVYHMGnLVxCs7EhzEbGXaxB5pKLhuRSg.original.fullsize.png">

In right angled $\triangle A B C$ by Pythagoras theorem
$$
\begin{aligned}
&(h-r)^2+b^2=r^2 \\
\Rightarrow & b^2=r^2-(h-r)^2=r^2-\left(h^2-2 h r+\mathrm{r}^2\right)=2 h r-h^2 \\
\therefore & \text { Volume }(v) \frac{1}{3} \pi h\left[2 h r-h^2\right]=\frac{1}{3}\left[2 h r^2-h^3\right] \\
& \frac{d v}{d h}=\frac{1}{3}\left[4 h r-3 h^2\right]=0 \Rightarrow h(4 r-3 h)=0 \\
& \frac{d^2 v}{d h^2}=\frac{1}{3}[4 r-6 h]
\end{aligned}
$$
At $h=\frac{4 r}{3}, \frac{d^2 v}{d h^2}=\frac{1}{3}\left[4 r-\frac{4 r}{3} \times 6\right]=\frac{1}{3}[4 r-8 r < ] 0$
$\Rightarrow$ maximum volume ocurs at $h$
$$
=\frac{4 r}{3}=\frac{4}{3} \times 3=4 \mathrm{~cm}
$$
As from (1),
$$
(h-r)^2+b^2=r^2
$$
$$
\Rightarrow b^2=2 h r-h^2=2 \cdot \frac{4 r}{3} r-\frac{16 r^2}{9}
$$
$$
\begin{aligned}
&=\frac{8 r^2}{3}-\frac{16 r^2}{9} \\
&=\frac{(24-16) r^2}{9}=\frac{8 r^2}{9} \\
&\Rightarrow b=\frac{2 \sqrt{2}}{3} r=2 \sqrt{2} \mathrm{~cm}
\end{aligned}
$$
Therefore curved surface area
$$
\begin{aligned}
&=\pi b l=\pi b \sqrt{h^2+r^2} \\
&=\pi 2 \sqrt{2} \sqrt{4^2+8}=8 \sqrt{3} \pi \mathrm{cm}^2
\end{aligned}
$$

</details>

---

### Q91. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math> and <math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced><mo>.</mo></math> If <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfrac></math> , then the local minimum value of <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is:

**Options:**

- **(A)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mo>-</mo><mn>3</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn></math>

<math><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

Let <math><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>t</mi></math>

<math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>g</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>t</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac></math>

<math><mi>t</mi><mo>&#8712;</mo><mi>R</mi><mo>-</mo><mfenced close="}" open="{" separators="|"><mrow><mn>0</mn></mrow></mfenced></math>

<math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>t</mi><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac></math>

<math><mi>A</mi><mi>M</mi><mo>&#8805;</mo><mi>G</mi><mi>M</mi></math>

Minimum of <math><mi>h</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#8658;</mo><mi>&#160;</mi><mfrac><mrow><mi>t</mi><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mo>&#8805;</mo><mi>&#160;</mi><msqrt><mi>t</mi><mo>&#215;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac></msqrt></math>

<math><mi>t</mi><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>t</mi></mrow></mfrac><mo>&#8805;</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

Local minimum <math><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

</details>

---

### Q92. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Twenty meters of wire is available for fencing off a flower-bed in the form of a circular sector. Then the maximum area (in sq. m) of the flower-bed, is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>**

**Detailed Solution:**

Perimeter <math><mo>=</mo><mn>2</mn><mi>r</mi><mo>+</mo><mi>r</mi><mi>&#952;</mi><mo>=</mo><mn>20</mn></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4c7fe611-e59b-4850-ad9c-e88c77439b60-image.png" style="width: 117px; height: 177px;" />

<math><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mn>2</mn><mi>r</mi></mrow><mrow><mi>r</mi></mrow></mfrac></math>

Now, Area <math><mi>A</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#952;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>2</mn></mfrac><mi>&#160;</mi><mfenced separators="|"><mfrac><mrow><mn>20</mn><mo>-</mo><mn>2</mn><mi>r</mi></mrow><mi>r</mi></mfrac></mfenced><mo>=</mo><mn>10</mn><mi>r</mi><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>r</mi></mrow></mfrac><mo>=</mo><mn>10</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>A</mi></mrow><mrow><mi>d</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mfenced separators="|"><mrow><mi>r</mi><mo>=</mo><mn>5</mn></mrow></mfenced></msub><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math> is the point of maxima

<math><msub><mrow><mi>A</mi></mrow><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>5</mn><mo>-</mo><mn>25</mn><mo>=</mo><mn>25</mn></math>

</details>

---

### Q93. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>.</mo></math> Then, <math><mi>f</mi></math> is an increasing function in the interval:

**Options:**

- **(A)** <math><mrow>  <mo>]</mo>  <mfrac>    <mrow>      <mn>5</mn>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>8</mn>    </mrow>  </mfrac>  <mtext>,</mtext>  <mfrac>    <mrow>      <mn>3</mn>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>4</mn>    </mrow>  </mfrac>  <mo>[</mo></mrow></math>
- **(B)** <math><mrow>  <mo>]</mo>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>2</mn>    </mrow>  </mfrac>  <mtext>,</mtext>  <mfrac>    <mrow>      <mn>5</mn>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>8</mn>    </mrow>  </mfrac>  <mo>[</mo></mrow></math>
- **(C)** <math><mrow>  <mo>]</mo>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>4</mn>    </mrow>  </mfrac>  <mtext>,</mtext>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>2</mn>    </mrow>  </mfrac>  <mo>[</mo></mrow></math>
- **(D)** <math><mrow>  <mo>]</mo>  <mn>0</mn>  <mtext>,</mtext>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>4</mn>    </mrow>  </mfrac>  <mo>[</mo></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mrow>  <mo>]</mo>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>4</mn>    </mrow>  </mfrac>  <mtext>,</mtext>  <mfrac>    <mrow>      <mi>&pi;</mi>    </mrow>    <mrow>      <mn>2</mn>    </mrow>  </mfrac>  <mo>[</mo></mrow></math>**

**Detailed Solution:**

<p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math>

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>4</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mn>4</mn><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mfenced separators="|"><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></math>

<math><mo>=</mo><mn>4</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mfenced separators="|"><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sin</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></math>

<math><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>2</mn><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mn>2</mn><mi>x</mi></mrow></mrow></math>

<math><mo>=</mo><mi>&#160;</mi><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>4</mn><mi>x</mi></mrow></mrow></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a5352541-bf3b-442e-a483-9c97b4f12d55-image.png" style="width: 227px; height: 170px;" /></p><p><math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, is increasing when <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mn>4</mn><mi>x</mi></mrow></mrow><mo>&#62;</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mo>&#8289;</mo><mn>4</mn><mi>x</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#960;</mi><mo>&#60;</mo><mn>4</mn><mi>x</mi><mo>&#60;</mo><mn>2</mn><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
<math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>&#160;</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p>

</details>

---

### Q94. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The minimum distance of a point on the curve <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></math> from the origin is

**Options:**

- **(A)** <math><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> units
- **(B)** <math><msqrt><mfrac><mrow><mn>19</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math> units
- **(C)** <math><msqrt><mfrac><mrow><mn>15</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math> units
- **(D)** <math><mfrac><mrow><msqrt><mn>19</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> units

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math> units**

**Detailed Solution:**

<p>A variable point on the given parabola can be taken as <math><mfenced separators="|"><mrow><mi>&#945;</mi><mo>,</mo><mi>&#160;</mi><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></mrow></mfenced></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b872f389-dd44-4f4a-9903-4500862b338d-image.png" style="width: 254px; height: 150px;" />

Distance from origin <math><mi>D</mi><mo>=</mo><mi>&#160;</mi><msqrt><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>

<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>16</mn><mo>-</mo><mn>8</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>=</mo><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>7</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>16</mn></math>

<math><mfrac><mrow><mi>d</mi><msup><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>d</mi><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>4</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>14</mn><mi>&#160;</mi><mi>&#945;</mi><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math> <math><mn>2</mn><mi>&#945;</mi><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo></math><math><mi>&#160;</mi><mi>&#945;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt><mo>,</mo><mi>&#160;</mi><mo>-</mo><msqrt><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></msqrt></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f6536e8d-5a56-4e56-b7e2-937c1180bf66-image.png" style="width: 307px; height: 100px;" />

<math><mo>&#8756;</mo><mi>&#160;</mi><msubsup><mrow><mi>D</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi><mi>&#160;</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mi>&#160;</mi><mi>a</mi><mi>t</mi><mi>&#160;</mi><msup><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><msubsup><mrow><mi>D</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>49</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>49</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>16</mn></math>

<math><mo>=</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>49</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>16</mn><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<math><msub><mrow><mi>D</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><msqrt><mn>15</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math></p>

</details>

---

### Q95. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> units is cut into two parts which are bent respectively to form a square of side <math><mo>=</mo><mi>x</mi></math> units and a circle of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>r</mi></math> units. If the sum of the areas of the square and the circle so formed is minimum, then

**Options:**

- **(A)** <math><mi>x</mi><mo>=</mo><mn>2</mn><mi>r</mi></math>
- **(B)** <math><mn>2</mn><mi>x</mi><mo>=</mo><mi>r</mi></math>
- **(C)** <math><mn>2</mn><mi>x</mi><mo>=</mo><mfenced separators="|"><mrow><mi>π</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>r</mi></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>4</mn><mo>-</mo><mi>π</mi></mrow></mfenced><mi>x</mi><mo>=</mo><mi>π</mi><mi>r</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>x</mi><mo>=</mo><mn>2</mn><mi>r</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/06a803ed-5bf7-423d-bcfd-445824318f3f-image.png" style="width: 153px; height: 150px;" />
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/78526718-1a4d-4924-9919-8ed9229bb967-image.png" style="width: 142px; height: 140px;" />

Given that <math><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>&#960;</mi><mi>r</mi><mo>=</mo><mn>2</mn></math>

i.e., <math><mn>2</mn><mi>x</mi><mo>+</mo><mi>&#960;</mi><mi>r</mi><mo>=</mo><mn>1</mn></math>

<math><mo>&#8756;</mo></math> <math><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><mi>&#960;</mi></mrow></mfrac></math> .......(i)

Area <math><mi>A</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>&#960;</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>&#960;</mi></mrow></mfrac><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

For min vale of area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>

<math><mfrac><mrow><mi>d</mi><mi>A</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> gives <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>&#960;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math> .......(ii)

From (i) and (ii)

<math><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>&#960;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></math> .......(iii)

<math><mo>&#8756;</mo></math> <math><mi>x</mi><mo>=</mo><mn>2</mn><mi>r</mi></math></p>

</details>

---

### Q96. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> be the minimum and the maximum values of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>0.6</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>0.6</mn></msup></mrow></mfrac><mi>&#160;</mi><mtext>in</mtext><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></math>, respectively, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>k</mi><mo>,</mo><mo>&#160;</mo><mi>K</mi><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mo>,</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.6</mn></mrow></msup><mo>,</mo><mi> </mi><mn>1</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mo>,</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><msup><mrow><mn>1,2</mn></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mo>,</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0.6</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfrac></math>

<math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#8242;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>0.6</mn><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced><mo>-</mo><mn>0.6</mn><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>0.4</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0.6</mn></mrow></msup></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<math><mo>=</mo><mn>0.6</mn><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mi>&#160;</mi><mfrac><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0.6</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>0.4</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0.4</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

Clearly it is always negative in <math><mo>[</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn><mo>]</mo></math>

minimum value would be at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.

<math><mfrac><mrow><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>0.6</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>0.6</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mo>=</mo><mi>k</mi></math>

&amp; maximum values would be at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>

<math><mfrac><mrow><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>)</mo></mrow><mrow><mn>0.6</mn></mrow></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced></mrow><mrow><mn>0.6</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mi>K</mi></math>

Hence <math><mfenced separators="|"><mrow><msup><mrow><mn>2</mn></mrow><mrow><mo>-</mo><mn>0.4</mn></mrow></msup><mo>,</mo><mn>1</mn></mrow></mfenced></math>

</details>

---

### Q97. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a polynomial of degree four and having its extreme values at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn><mo>&#160;</mo></mrow></munder><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi mathvariant="normal">f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>2</mn></mfenced></math> is equal to </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>a</mi><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>c</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>d</mi><mi>x</mi><mo>+</mo><mi>e</mi></math>

Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>+</mo><mfrac><mi>d</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn></math>

This limit exists when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mi>e</mi><mo>=</mo><mn>0</mn></math>.

So,  <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mn>0</mn></mrow></munder><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn></math>

It is given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> are the solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>4</mn><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>c</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><mrow><mn>4</mn><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>c</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></math> are the roots of the quadratic equation. 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>Sum of roots</mtext><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>b</mi></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>a</mi></math>

Product of roots <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>c</mi></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#183;</mo><mn>2</mn><mo>=</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mi>c</mi><mn>4</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mtext>,&#160;</mtext><mi>b</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>8</mn><mo>-</mo><mn>1</mn><mn>6</mn><mo>+</mo><mn>8</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q98. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If non-zero real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> are such that  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>i</mi><mi>n</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#62;</mo><mi>m</mi><mi>a</mi><mi>x</mi><mo>&#160;</mo><mi>g</mi><mfenced><mi>x</mi></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>c</mi><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math>; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mfrac><mi>c</mi><mi>b</mi></mfrac></mfenced></math> lies in the interval

**Options:**

- **(A)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msqrt> <mn>2</mn> </msqrt> <mtext>, </mtext> <mo>&infin;</mo> </mrow> </mfenced> </mrow> </math>
- **(B)** <math> <mrow> <mo>[</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mtext>, </mtext> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> <mo>)</mo> </mrow> </math>
- **(C)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>0</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(D)** <math> <mrow> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfrac> <mtext>, </mtext> <msqrt> <mn>2</mn> </msqrt> </mrow> </mfenced> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <msqrt> <mn>2</mn> </msqrt> <mtext>, </mtext> <mo>&infin;</mo> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>b</mi><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>c</mi><mi>x</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math></p><p>For finding the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mi>b</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>&#34;</mo></msup><mfenced><mrow><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#62;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> has minimum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mi>b</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup></math></p><p>      <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>f</mi><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup></math></p><p>Similarly, for finding the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>                        <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>-</mo><mi>c</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>g</mi><mo>&#34;</mo></msup><mfenced><mrow><mo>-</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#60;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mfenced><mi>x</mi></mfenced></math> has maximum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mi>c</mi></math>.</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>g</mi><mi>max</mi></msub><mo>=</mo><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math></p><p>      <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>g</mi><mi>max</mi></msub><mo>=</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>&#62;</mo><msub><mi>g</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#62;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;</mtext><mfenced><mrow><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;</mtext><mfenced><mrow><mi>c</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mi>b</mi></mrow></mfenced><mfenced><mrow><mi>c</mi><mo>+</mo><msqrt><mn>2</mn></msqrt><mi>b</mi></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfrac><mi>c</mi><mi>b</mi></mfrac><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mfenced><mrow><mfrac><mi>c</mi><mi>b</mi></mfrac><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>Using wavy curve method, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>b</mi></mfrac><mo>&#60;</mo><mo>-</mo><msqrt><mn>2</mn></msqrt></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>c</mi><mi>b</mi></mfrac><mo>&#62;</mo><msqrt><mn>2</mn></msqrt></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><mfrac><mi>c</mi><mi>b</mi></mfrac></mfenced><mo>&#8712;</mo><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>,</mi><mo>&#160;</mo><mo>&#8734;</mo></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q99. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the volume of a spherical ball is increasing at the rate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#960;</mi><mo>&#160;</mo><mi>cc</mi><mo>/</mo><mi>sec</mi></math> then the rate of increase of its radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>in</mi><mo>&#160;</mo><mi>cm</mi><mo>/</mo><mi>sec</mi></mrow></mfenced><mo>,</mo></math> when the volume is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>288</mn><mi>&#960;</mi><mo>&#160;</mo><mi>cc</mi></math> is

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> <mn>6</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> <mn>6</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<p>Volume of sphere of radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>288</mn><mi>&#960;</mi><mo>&#160;</mo><mi>cc</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>288</mn><mi>&#960;</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>288</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>216</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>cm</mi></math>.</p><p>Again, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msup><mi>r</mi><mn>3</mn></msup></math></p><p>Differentiate w.r.t. &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>&#39;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>4</mn><mi>&#960;</mi><msup><mi>r</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math></p><p>Put the given values, to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>&#960;</mi><mo>=</mo><mn>4</mn><mi>&#960;</mi><mo>&#215;</mo><msup><mn>6</mn><mn>2</mn></msup><mo>&#215;</mo><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>r</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mn>6</mn></mrow></mfrac><mo>&#160;</mo><mi>cm</mi><mo>/</mo><mi>sec</mi><mo>.</mo></math></p>

</details>

---

### Q100. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The volume of the largest possible right circular cylinder that can be inscribed in a sphere of radius $=\sqrt{3}$ is:

**Options:**

- **(A)** $\frac{4}{3} \sqrt{3} \pi$
- **(B)** $\frac{8}{3} \sqrt{3} \pi$
- **(C)** $4 \pi$
- **(D)** $2 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \pi$**

**Detailed Solution:**

Given, radius of sphere $=\sqrt{3}$
Now, In $\triangle \mathrm{OAB}$, by Pythagoras theorem
$$
(\mathrm{OA})^2=(\mathrm{OB})^2+(\mathrm{AB})^2
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5TH_ynCe3KrvxokFBBMBVXAj0eh7mUKQOSSiwcGHjPI.original.fullsize.png">

$$
\begin{aligned}
&(\sqrt{3})^2=\left(\frac{h}{2}\right)^2+r^2 \\
&3=\frac{h^2}{4}+r^2 \Rightarrow r^2=3-\frac{h^2}{4}
\end{aligned}
$$
Now, volume of cylinder $=\pi r^2 h$
$$
\begin{aligned}
&V=\pi\left(3-\frac{h^2}{4}\right) h \\
&V=3 \pi h-\frac{\pi h^3}{4}
\end{aligned}
$$
Now, for largest possible right circular cylinder the volume must be maximum
$\therefore$ For maximum volume, $\frac{d V}{d h}=0$ Now, Differentiating eq. (2) w.r.t. $h$ $V^1=\frac{d V}{d h}=3 \pi-\frac{3}{4} \pi h^2$
or $3 \pi-\frac{3}{4} \pi h^2=0 \Rightarrow 3 \pi=\frac{3}{4} \pi h^2$ $\Rightarrow h^2=4 \Rightarrow h=2$
Now, volume $(V)$ of the cylinder
$$
=\pi\left(3-\frac{h^2}{4}\right) h=\pi(6-2)=4 \pi
$$

</details>

---

### Q101. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mi>x</mi></msup><mo>+</mo><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mi>x</mi></msup><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo></math> then the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> has :

**Options:**

- **(A)** No solution
- **(B)** More than two solutions
- **(C)** One solution
- **(D)** Two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) One solution**

**Detailed Solution:**

<p><mi><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26106.PNG" style="width: 200px; height: 110px;" /></mi>


<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mi>x</mi></msup><mi>ln</mi><mfenced><mfrac><mn>3</mn><mn>5</mn></mfrac></mfenced><mo>+</mo><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mi>x</mi></msup><mi>ln</mi><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mo>&#60;</mo><mn>0</mn><mi mathvariant="normal">&#160;</mi><mo>&#8704;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><msup><mi>a</mi><mi>x</mi></msup><mo>=</mo><msup><mi>a</mi><mi>x</mi></msup><mi>ln</mi><mi>a</mi></mrow></mfenced></math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is monotonically decreasing.

Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>+</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mo>-</mo><mn>1</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mi>a</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>1</mn></mrow></mfenced></math>

and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mo>&#8734;</mo></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>&#8594;</mo><mo>&#8734;</mo></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mo>&#8757;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>-</mo><mo>&#8734;</mo></mrow></munder><msup><mi>a</mi><mi>x</mi></msup><mo>=</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>a</mi><mo>&#60;</mo><mn>1</mn></mrow></mfenced></math>

and there is only <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> solution for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q102. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> are extreme points of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><mi>log</mi><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>+</mo><mi>&#946;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></math>, then

**Options:**

- **(A)** <math> <mrow> <mi>α</mi> <mo>=</mo> <mn>2</mn> <mtext>, </mtext> <mi>β</mi> <mo>=</mo> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mi>&alpha;</mi> <mo>=</mo> <mn>2</mn> <mtext>, </mtext> <mi>&beta;</mi> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mi>&alpha;</mi> <mo>=</mo> <mo>-</mo> <mn>6</mn> <mtext>, </mtext> <mi>&beta;</mi> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mi>&alpha;</mi> <mo>=</mo> <mo>-</mo> <mn>6</mn> <mtext>, </mtext> <mi>&beta;</mi> <mo>=</mo><mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mi>α</mi> <mo>=</mo> <mn>2</mn> <mtext>, </mtext> <mi>β</mi> <mo>=</mo> <mo>-</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><mo>log</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>&#946;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8289;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><mo>log</mo><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>&#946;</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;</mo><mi>f</mi><msup><mo>&#8289;</mo><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mi>&#945;</mi></mrow><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced></mfrac><mo>+</mo><mn>2</mn><mi>&#946;</mi><mi>x</mi><mo>+</mo><mn>1</mn></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#62;</mo><mo>&#160;</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8289;</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>&#945;</mi><mi>log</mi><mo mathvariant="italic">x</mo><mo>+</mo><mi>&#946;</mi><msup><mo mathvariant="italic">x</mo><mn>2</mn></msup><mo>+</mo><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;&#160;</mo><mi>f</mi><msup><mo>&#8289;</mo><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>&#945;</mi><mi>x</mi></mfrac><mo>+</mo><mn>2</mn><mi>&#946;</mi><mi>x</mi><mo>+</mo><mn>1</mn></math>

<math> <mrow> <msup> <mrow> <mi></mi><mi>f</mi><mo>&#8289;</mo> </mrow> <mo>&#8242;</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> <mo>=</mo> <mo>-</mo> <mi>&#945;</mi> <mo>-</mo> <mn>2</mn> <mi>&#946;</mi> <mo>+</mo> <mn>1</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <msup> <mrow> <mi>f</mi><mo>&#8289;</mo> </mrow> <mo>&#8242;</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mn>2</mn> </mrow> </mfenced> <mo>=</mo> <mfrac> <mrow> <mi>&#945;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>+</mo> <mn>4</mn> <mi>&#946;</mi> <mo>+</mo> <mn>1</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mn>2</mn> <msup> <mrow> <mi>f</mi><mo>&#8289;</mo> </mrow> <mo>&#8242;</mo> </msup> <mfenced close=")" open="(" separators=","> <mrow> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> <mo>=</mo> <mo>-</mo> <mn>2</mn> <mi>&#945;</mi> <mo>-</mo> <mn>4</mn> <mi>&#946;</mi> <mo>+</mo> <mn>2</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>&#39;</mi></msup><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><mfrac><mi>&#945;</mi><mn>2</mn></mfrac><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

Adding,

<math> <mrow> <mo>-</mo> <mfrac> <mrow> <mn>3</mn> <mi>&#945;</mi> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mo>+</mo> <mn>3</mn> <mo>=</mo> <mn>0</mn> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mi>&#945;</mi> <mo>=</mo> <mn>2</mn> </mrow> </math>

<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <mi>&#946;</mi> <mo>=</mo> <mfrac> <mrow> <mo>-</mo> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q103. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(1)=-2$ and $f^{\prime}(x) \geq 4.2$ for $1 \leq x \leq 6$. The possible value of $f(6)$ lies in the interval :

**Options:**

- **(A)** $[15,19)$
- **(B)** $(-\infty, 12)$
- **(C)** $[12,15)$
- **(D)** $[19, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $[19, \infty)$**

**Detailed Solution:**

Given $f(1)=-2$ and $f^{\prime}(x) \geq 4.2$ for $1 \leq x \leq 6$
Consider $f^{\prime}(x)=\frac{f(x+h)-f(x)}{h}$ $\Rightarrow f(x+h)-f(x)=f^{\prime}(x) \cdot h \geq(4.2) h$
So, $f(x+h) \geq f(x)+(4.2) h$
put $x=1$ and $h=5$, we get
$f(6) \geq f(1)+5(4.2) \Rightarrow f(6) \geq 19$
Hence $f(6)$ lies in $[19, \infty)$

</details>

---

### Q104. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A spherical balloon is being inflated at the rate of $35 \mathrm{cc} / \mathrm{min}$. The rate of increase in the surface area (in $\mathrm{cm}^2 / \mathrm{min}$.) of the balloon when its diameter is $14 \mathrm{~cm}$, is :

**Options:**

- **(A)** 10
- **(B)** $\sqrt{10}$
- **(C)** 100
- **(D)** $10 \sqrt{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

Volume of sphere $\mathrm{V}=\frac{4}{3} \pi r^3$
$\frac{d \mathrm{~V}}{d t}=\frac{4}{3} \cdot \pi \cdot 3 r^2 \cdot \frac{d r}{d t}$
$35=4 \pi r^2 \cdot \frac{d r}{d t}$ or $\frac{d r}{d t}=\frac{35}{4 \pi r^2}$
Surface area of sphere $=\mathrm{S}=4 \pi r^2$
$\frac{d \mathrm{~S}}{d t}=4 \pi \times 2 r \times \frac{d r}{d t}=8 \pi r \cdot \frac{d r}{d t}$
$\frac{d \mathrm{~S}}{d t}=\frac{70}{r}$
Now, diameter $=14 \mathrm{~cm}, r=7$
$\therefore \quad \frac{d \mathrm{~S}}{d t}=10$

</details>

---

### Q105. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The cost of running a bus from $A$ to $B$, is $₹\left(a v+\frac{b}{v}\right)$, where $v \mathrm{~km} / \mathrm{h}$ is the average speed of the bus. When the bus travels at $30 \mathrm{~km} / \mathrm{h}$, the cost comes out to be $₹ 75$ while at $40 \mathrm{~km} / \mathrm{h}$, it is $₹ 65$. Then the most economical speed (in $\mathrm{km} / \mathrm{h}$ ) of the bus is :

**Options:**

- **(A)** 45
- **(B)** 50
- **(C)** 60
- **(D)** 40

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 60**

**Detailed Solution:**

Let $\operatorname{cost} \mathrm{C}=a v+\frac{b}{v}$
According to given question,
$$
\begin{aligned}
& 30 a+\frac{b}{30}=75 \\
& 40 a+\frac{b}{40}=65
\end{aligned}
$$
On solving (i) and (ii), we get $a=\frac{1}{2}$ and $b=1800$
Now, $C=a v+\frac{b}{v}$
$$
\begin{aligned}
& \Rightarrow \frac{d C}{d v}=a-\frac{b}{v^2} \\
& \frac{d C}{d v}=0 \Rightarrow a-\frac{b}{v^2}=0 \\
& \Rightarrow v=\sqrt{\frac{b}{a}}=\sqrt{3600} \\
& \Rightarrow v=60 \mathrm{kmph}
\end{aligned}
$$

</details>

---

### Q106. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The maximum area of a right angled triangle with hypotenuse $h$ is :

**Options:**

- **(A)** $\frac{h^2}{2 \sqrt{2}}$
- **(B)** $\frac{h^2}{2}$
- **(C)** $\frac{h^2}{\sqrt{2}}$
- **(D)** $\frac{h^2}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{h^2}{4}$**

**Detailed Solution:**

Let base $=b$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mge2TNH4GJMxZxcICG5WkqmSl_BA-XMfLFcVlcRlV4g.original.fullsize.png">

Altitude (or perpendicular) $=\sqrt{h^2-b^2}$ Area, $\mathrm{A}=\frac{1}{2} \times$ base $\times$ altitude $=\frac{1}{2} \times b \times \sqrt{h^2-b^2}$ $\Rightarrow \frac{d \mathrm{~A}}{d b}=\frac{1}{2}\left[\sqrt{h^2-b^2}+b \cdot \frac{-2 b}{2 \sqrt{h^2-b^2}}\right]$ $=\frac{1}{2}\left[\frac{h^2-2 b^2}{\sqrt{h^2-b^2}}\right]$
Put $\frac{d \mathrm{~A}}{d b}=0, \Rightarrow b=\frac{h}{\sqrt{2}}$
Maximumarea $=\frac{1}{2} \times \frac{h}{\sqrt{2}} \times \sqrt{h^2-\frac{h^2}{2}}=\frac{h^2}{4}$

</details>

---

### Q107. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the surface area of a sphere of radius $r$ is increasing uniformly at the rate $8 \mathrm{~cm}^2 / \mathrm{s}$, then the rate of change of its volume is:

**Options:**

- **(A)** constant
- **(B)** proportional to $\sqrt{r}$
- **(C)** proportional to $r^2$
- **(D)** proportional to $r$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) proportional to $r$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{V}=\frac{4}{3} \pi r^3 \Rightarrow \frac{d \mathrm{~V}}{d t}=4 \pi r^2 \cdot \frac{d r}{d t} \\
& \mathrm{~S}=4 \pi r^2 \Rightarrow \frac{d \mathrm{~S}}{d t}=8 \pi r \cdot \frac{d r}{d t} \\
& \Rightarrow 8=8 \pi r \frac{d r}{d t} \Rightarrow \frac{d r}{d t}=\frac{1}{\pi r}
\end{aligned}
$$
Putting the value of $\frac{d r}{d t}$ in (i), we get
$$
\frac{d \mathrm{~V}}{d t}=4 \pi r^2 \times \frac{1}{\pi r}=4 r
$$
$\Rightarrow \frac{d \mathrm{~V}}{d t}$ is proportional to $r$.

</details>

---

### Q108. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If a metallic circular plate of radius $50 \mathrm{~cm}$ is heated so that its radius increases at the rate of $1 \mathrm{~mm}$ per hour, then the rate at which, the area of the plate increases (in $\mathrm{cm}^2 /$ hour) is

**Options:**

- **(A)** $5 \pi$
- **(B)** $10 \pi$
- **(C)** $100 \pi$
- **(D)** $50 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10 \pi$**

**Detailed Solution:**

Let $A=\pi \mathrm{r}^2$ be area of metalic circular plate of $r=50 \mathrm{~cm}$.
Also, given $\frac{d r}{d t}=1 \mathrm{~mm}=\frac{1}{10} \mathrm{~cm}$

$$
\begin{aligned}
& \therefore A=\pi r^2 \\
& \Rightarrow \frac{d A}{d t}=2 \pi r \frac{d r}{d t}=2 \pi \cdot 50 \cdot \frac{1}{10}=10 \pi
\end{aligned}
$$
Hence, area of plate increases in $10 \pi \mathrm{cm}^2 /$ hour.

</details>

---

### Q109. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:(-\infty, \infty) \rightarrow(-\infty, \infty)$ be defined by $f(x)=x^3+1$
Statement 1: The function fhas a local extremum at $x=0$
Statement 2: The function $f$ is continuous and differentiable on $(-\infty, \infty)$ and $f^{\prime}(0)=0$

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.
- **(C)** Statement 1 is true, Statement 2 is true, Statement 2 is not the correct explanation for Statement 1.
- **(D)** Statement 1 is false, Statement 2 is true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement 1 is false, Statement 2 is true.**

**Detailed Solution:**

Let $f:(-\infty, \infty) \rightarrow(-\infty, \infty)$ be defined by $f(x)=x^3+1$.
Clearly, $f(x)$ is symmetric along $y=1$ and it has neither maxima nor minima.
$\therefore$ Statement - 1 is false.

</details>

---

### Q110. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The weight $W$ of a certain stock of fish is given by $W=n w$, where $n$ is the size of stock and $w$ is the average weight of a fish. If $n$ and $w$ change with time $t$ as $n=2 t^2+3$ and $w=t^2-t+2$, then the rate of change of $W$ with respect to $t$ at $t=1$ is

**Options:**

- **(A)** 1
- **(B)** 8
- **(C)** 13
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 13**

**Detailed Solution:**

Let $\mathrm{W}=n w$
$$
\Rightarrow \frac{d W}{d t}=n \frac{d w}{d t}+w \cdot \frac{d n}{d t}
$$
Given : $w=t^2-t+2$ and $n=2 t^2+3$ $\Rightarrow \frac{d w}{d t}=2 t-1$ and $\frac{d n}{d t}=4 t$
$\therefore$ Equation (1)
$$
\Rightarrow \frac{d w}{d t}=\left(2 t^2+3\right)(2 t-1)+\left(t^2-t+2\right)(4 t)
$$
Thus, $\left.\frac{d W}{d t}\right|_{t=1}=(2+3)(2-1)+(2)(4)$
$$
=5(1)+8=13
$$

</details>

---

### Q111. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Consider a rectangle whose length is increasing at the uniform rate of $2 \mathrm{~m} / \mathrm{sec}$, breadth is decreasing at the uniform rate of $3 \mathrm{~m} / \mathrm{sec}$ and the area is decreasing at the uniform rate of $5 \mathrm{~m}^2 / \mathrm{sec}$. If after some time the breadth of the rectangle is $2 \mathrm{~m}$ then the length of the rectangle is

**Options:**

- **(A)** $2 \mathrm{~m}$
- **(B)** $4 \mathrm{~m}$
- **(C)** $1 \mathrm{~m}$
- **(D)** $3 \mathrm{~m}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \mathrm{~m}$**

**Detailed Solution:**

Let $A$ be the area, $b$ be the breadth and $\ell$ be the length of the rectangle.
Given: $\frac{d A}{d t}=-5, \frac{d \ell}{d t}=2, \frac{d b}{d t}=-3$
We know, $A=\ell \times b$
$$
\begin{aligned}
& \Rightarrow \frac{d A}{d t}=\ell \cdot \frac{d b}{d t}+b \cdot \frac{d \ell}{d t}=-3 \ell+2 b \\
& \Rightarrow-5=-3 \ell+2 b .
\end{aligned}
$$
When $b=2$, we have
$$
-5=-3 \ell+4 \Rightarrow \ell=\frac{9}{3}=3 m
$$

</details>

---

### Q112. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `2`

If a circular iron sheet of radius $30 \mathrm{~cm}$ is heated such that its area increases at the uniform rate of $6 \pi \mathrm{cm}^2 / \mathrm{hr}$, then the rate (in $\mathrm{mm} / \mathrm{hr}$ ) at which the radius of the circular sheet increases is

**Options:**

- **(A)** $1.0$
- **(B)** $0.1$
- **(C)** $1.1$
- **(D)** $2.0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.1$**

**Detailed Solution:**

Let $A=\pi r^2$.
$$
\begin{aligned}
\frac{d A}{d t} & =2 \pi r \cdot \frac{d r}{d t} \\
6 \pi & =2 \pi(30) \cdot \frac{d r}{d t} \\
\Rightarrow \quad \frac{3}{30}= & \frac{d r}{d t} \Rightarrow \frac{d r}{d t}=\frac{1}{10}=0.1
\end{aligned}
$$
Thus, the rate at which the radius of the circular sheet increases is $0.1$

</details>

---

### Q113. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

Let $a, b \in R$ be such that the function $f$ given by $f(x)=\ln |x|+b x^2+a x, x \neq 0$ has extreme values at $x=-1$ and $x=2$.
Statement 1: $f$ has local maximum at $x=-1$ and at $x=2$.
Statement 2: $\mathrm{a}=\frac{1}{2}$ and $\mathrm{b}=\frac{-1}{4}$

**Options:**

- **(A)** Statement $1$ is false, statement $2$ is true
- **(B)** Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$
- **(C)** Statement $1$ is true, statement $2$ is true; statement $2$ is not a correct explanation for statement $1$
- **(D)** Statement $1$ is true, statement $2$ is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$**

**Detailed Solution:**

$f^{\prime}(x)=\frac{1}{x}+2 b x+a$
$f$ has extremevalues and differentiable
$\Rightarrow f^{\prime}(-1)=0 \quad \Rightarrow a-2 b=1$
$f^{\prime}(2)=0 \quad \Rightarrow a+4 b=-\frac{1}{2} \quad \Rightarrow a=\frac{1}{2}, b=-\frac{1}{4}$
$f^{\prime \prime}(-1), f^{\prime \prime}(2)$ are negative. $f$ has local maxima at $-1,2$

</details>

---

### Q114. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

A spherical balloon is filled with $4500 ~\pi$ cubic meters of helium gas. If a leak in the balloon causes the gas to escape at the rate of $72 ~\pi$ cubic meters per minute, then the rate (in meters per minute) at which the radius of the balloon decreases $49$ minutes after the leakage began is

**Options:**

- **(A)** $\frac{9}{7}$
- **(B)** $\frac{7}{9}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{9}$**

**Detailed Solution:**

$v=\frac{4}{3} \pi r^2$
After $49$ minutes volume $=4500 \pi-49(72 \pi)=972 \pi$
$\frac{4}{3} \pi r^3=972 \pi \quad \Rightarrow r^3=729 \quad \Rightarrow r=9$
$v=\frac{4}{3} \pi r^3$
$\frac{d v}{d t}=\frac{4}{3} \pi 3 r^2 \frac{d r}{d t}$
$72 \pi=4 \pi r^2 \frac{d r}{d t}$
$\frac{\mathrm{dr}}{\mathrm{dt}}=\frac{72}{4 \cdot 9 \cdot 9}=\frac{2}{9}$

</details>

---

### Q115. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between line $y-x=1$ and curve $x=y^2$ is

**Options:**

- **(A)** $\frac{3 \sqrt{2}}{8}$
- **(B)** $\frac{8}{3 \sqrt{2}}$
- **(C)** $\frac{4}{\sqrt{3}}$
- **(D)** $\frac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \sqrt{2}}{8}$**

**Detailed Solution:**

$$
P=\left(y^2, y\right)
$$
Perpendicular distance from $P$ to $x-y+1=0$ is $\frac{\left|y^2-y+1\right|}{\sqrt{2}}$
$$
\begin{aligned}
& \mathrm{y}^2-\mathrm{y}+1>0 \forall \mathrm{y} \in \mathrm{R} \\
& \therefore \text { Coefficient } \mathrm{y}^2>0 \\
& \therefore \text { Min value }=\frac{1}{\sqrt{2}}\left(\frac{4 \mathrm{ac}-\mathrm{b}^2}{4 \mathrm{a}}\right)=\frac{3}{4 \sqrt{2}}
\end{aligned}
$$

</details>

---

### Q116. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

Let $f: R \rightarrow R$ be defined by $f(x)=\left\{\begin{array}{ll}k-2 x, & \text { if } x \leq-1 \\ 2 x+3, & \text { if } x>-1\end{array}\right.$. If $f$ has a local minimum at $x=-1$, then a possible value of $\mathrm{k}$ is

**Options:**

- **(A)** 0
- **(B)** $-\frac{1}{2}$
- **(C)** $-1$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-1$**

**Detailed Solution:**

$f(x)=k-2 x \quad$ if $x \leq-1$
$=2 x+3 \quad$ if $x>-1$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HQjS1VPS4n_hujq-24XGdevmzQ49tDz6Eq1CosBhfO4.original.fullsize.png">

</details>

---

### Q117. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

The shortest distance between the line $\mathrm{y}-\mathrm{x}=1$ and the curve $\mathrm{x}=\mathrm{y}^2$ is

**Options:**

- **(A)** $\frac{3 \sqrt{2}}{8}$
- **(B)** $\frac{2 \sqrt{3}}{8}$
- **(C)** $\frac{3 \sqrt{2}}{5}$
- **(D)** $\frac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3 \sqrt{2}}{8}$**

**Detailed Solution:**

$$
\begin{aligned}
& x-y+1=0 \\
& x=y^2 \\
& 1=2 y \frac{d y}{d x} \Rightarrow \frac{d y}{d x}=\frac{1}{2 y}=\text { Slope of given line (1) } \\
& \frac{1}{2 y}=1 \Rightarrow y=\frac{1}{2} \Rightarrow y=\frac{1}{2} \Rightarrow x=\left(\frac{1}{2}\right)^2=\frac{1}{4} \Rightarrow(x, y)=\left(\frac{1}{4}, \frac{1}{2}\right)
\end{aligned}
$$

$\therefore$ The shortest distance is $\frac{\left|\frac{1}{4}-\frac{1}{2}+1\right|}{\sqrt{1+1}}=\frac{3}{4 \sqrt{2}}=\frac{3 \sqrt{2}}{8}$
Directions: Question number 86 to 90 are Assertion - Reason type questions. Each of these questions contains two statements
Statement-1 (Assertion) and Statement-2 (Reason).
Each of these questions also have four alternative choices, only one of which is the correct answer. You have to select the correct choice

</details>

---

### Q118. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `3`

Given $P(x)=x^4+a x^3+b x^2+c x+d$ such that $x=0$ is the only real root of $P^{\prime}(x)=0$. If $P(-1) < P(1)$, then in the interval $[-1,1]$

**Options:**

- **(A)** $P(-1)$ is the minimum and $P(1)$ is the maximum of $P$
- **(B)** $P(-1)$ is not minimum but $P(1)$ is the maximum of $P$
- **(C)** $P(-1)$ is the minimum and $P(1)$ is not the maximum of $P$
- **(D)** neither $P(-1)$ is the minimum nor $P(1)$ is the maximum of $P$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $P(-1)$ is not minimum but $P(1)$ is the maximum of $P$**

**Detailed Solution:**

$$
\begin{aligned}
& P(x)=x^4+a x^3+b x^2+c x+d \\
& P^{\prime}(x)=4 x^3+3 a x^2+2 b x+c \\
& \because x=0 \text { is a solution for } P^{\prime}(x)=0, \Rightarrow c=0 \\
& \therefore P(x)=x^4+a x^3+b x^2+d
\end{aligned}
$$
Also, we have $P(-1) < P(1)$
$$
\Rightarrow 1-a+b+d < 1+a+b+d \Rightarrow a>0
$$
$\because P^{\prime}(x)=0$, only when $x=0$ and $P(x)$ is differentiable in $(-1,1)$, we should have the maximum and minimum at the points $x=-1,0$ and 1 only
Also, we have $P(-1) < P(1)$
$\therefore$ Max. of $P(x)=\operatorname{Max} .\{P(0), P(1)\}$ \& Min. of $P(x)=\operatorname{Min} .\{P(-1), P(0)\}$
In the interval $[0,1]$,
$$
P^{\prime}(x)=4 x^3+3 a x^2+2 b x=x\left(4 x^2+3 a x+2 b\right)
$$
$\because P^{\prime}(x)$ has only one root $x=0,4 x^2+3 a x+2 b=0$ has no real roots.
$$
\begin{aligned}
& \therefore(3 a)^2-32 b < 0 \Rightarrow \frac{3 a^2}{32} < b \\
& \therefore b>0
\end{aligned}
$$
Thus, we have $a>0$ and $b>0$
$$
\therefore \mathrm{P}^{\prime}(\mathrm{x})=4 \mathrm{x}^3+3 a \mathrm{x}^2+2 \mathrm{bx}>0, \forall \mathrm{x} \in(0,1)
$$
Hence $P(x)$ is increasing in $[0,1]$
$\therefore$ Max. of $P(x)=P(1)$
Similarly, $P(x)$ is decreasing in $[-1,0]$
Therefore Min. $P(x)$ does not occur at $x=-1$

</details>

---

### Q119. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `3`

How many real solutions does the equation $x^7+14 x^5+16 x^3+30 x-560=0$ have?

**Options:**

- **(A)** 7
- **(B)** 1
- **(C)** 3
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

$$
\begin{aligned}
& x^7+14 x^5+16 x^3+30 x-560=0 \\
& \text { Let } f(x)=x^7+14 x^5+16 x^3+30 x \\
& \Rightarrow f^{\prime}(x)=7 x^6+70 x^4+48 x^2+30>0 \forall x
\end{aligned}
$$
$\therefore f(x)$ is an increasing function $\forall x$.

</details>

---

### Q120. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

Suppose the cube $x^3-p x+q$ has three distinct real roots where $p>0$ and $q>0$. Then which one of the following holds?

**Options:**

- **(A)** The cubic has minima at $\sqrt{\frac{\mathrm{p}}{3}}$ and maxima at $-\sqrt{\frac{\mathrm{p}}{3}}$
- **(B)** The cubic has minima at $-\sqrt{\frac{p}{3}}$ and maxima at $\sqrt{\frac{p}{3}}$
- **(C)** The cubic has minima at both $\sqrt{\frac{p}{3}}$ and $-\sqrt{\frac{p}{3}}$
- **(D)** The cubic has maxima at both $\sqrt{\frac{p}{3}}$ and $-\sqrt{\frac{p}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) The cubic has minima at $\sqrt{\frac{\mathrm{p}}{3}}$ and maxima at $-\sqrt{\frac{\mathrm{p}}{3}}$**

**Detailed Solution:**

Let $f(x)=x^3-p x+q$
Now for maxima/minima
$$
\begin{aligned}
& f^{\prime}(x)=0 \\
& \Rightarrow 3 x^2-p=0 \\
& \Rightarrow x^2=\frac{p}{3} \\
& \therefore x=\pm \sqrt{\frac{p}{3}}
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QrBlMiAGiedOj9zdToiqOOUlJFmZQx5C3Cs9yxiKf84.original.fullsize.png">

</details>

---

### Q121. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The function $f(x)=\frac{x}{2}+\frac{2}{x}$ has a local minimum at

**Options:**

- **(A)** x = 2
- **(B)** x = −2
- **(C)** x = 0
- **(D)** x = 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) x = 2**

**Detailed Solution:**

$\frac{x}{2}+\frac{2}{x}$ is of the form $x+\frac{1}{x} \geq 2$ \& equality holds for $x=1$

</details>

---

### Q122. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

If $x$ is real, the maximum value of $\frac{3 x^2+9 x+17}{3 x^2+9 x+7}$ is

**Options:**

- **(A)** 1/4
- **(B)** 41
- **(C)** 1
- **(D)** 17/7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 41**

**Detailed Solution:**

$y=\frac{3 x^2+9 x+17}{3 x^2+9 x+7}$
$3 x^2(y-1)+9 x(y-1)+7 y-17=0$
$D \geq 0 \quad \because x$ is real
$81(y-1)^2-4 x 3(y-1)(7 y-17) \geq 0$
$\Rightarrow(y-1)(y-41) \leq 0 \Rightarrow 1 \leq y \leq 41$

</details>

---

### Q123. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

If the equation
$a_n x^n+a_{n-1} x^{n-1}+\ldots \ldots+a_1 x=0, a_1 \neq 0, n \geq 2$, has a positive root $x=\alpha$, then the equation $n a_n x^{n-1}+(n-1) a_{n-1} x^{n-2}+\ldots . .+a_1=0$ has a positive root, which is

**Options:**

- **(A)** greater than $\alpha$
- **(B)** smaller than $\alpha$
- **(C)** greater than or equal to $\alpha$
- **(D)** equal to $\alpha$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) smaller than $\alpha$**

**Detailed Solution:**

$f(0)=0, f(\alpha)=0$
$\Rightarrow f^{\prime}(k)=0$ for some $k \in(0, \alpha)$

</details>

---

### Q124. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

A spherical iron ball $10 \mathrm{~cm}$ in radius is coated with a layer of ice of uniform thickness than melts at a rate of $50 \mathrm{~cm}^3 / \mathrm{min}$. When the thickness of ice is $5 \mathrm{~cm}$, then the rate at which the thickness of ice decreases, is

**Options:**

- **(A)** $\frac{1}{36 \pi} \mathrm{cm} / \mathrm{min}$
- **(B)** $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$
- **(C)** $\frac{1}{54 \pi} \mathrm{cm} / \mathrm{min}$
- **(D)** $\frac{5}{6 \pi} \mathrm{cm} / \min$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{18 \pi} \mathrm{cm} / \mathrm{min}$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{d v}{d t}=50 \\
& 4 \pi r^2 \frac{d r}{d t}=50 \\
& \Rightarrow \frac{d r}{d t}=\frac{50}{4 \pi(15)^2} \quad \text { where } r=15 \\
& =\frac{1}{16 \pi}
\end{aligned}
$$

</details>

---

### Q125. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

If $f$ is a real-valued differentiable function satisfying $|f(x)-f(y)| \leq(x-y)^2, x, y \in R$ and $f(0)=0$, then $f(1)$ equals

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

$$
\begin{aligned}
& f^{\prime}(x)=\lim _{h \rightarrow 0} \frac{f(x+h)-f(x)}{h} \\
& \left|f^{\prime}(x)\right|=\lim _{h \rightarrow 0}\left|\frac{f(x+h)-f(x)}{h}\right| \leq \lim _{h \rightarrow 0}\left|\frac{(h)^2}{h}\right| \\
& \Rightarrow\left|f^{\prime}(x)\right| \leq 0 \Rightarrow f^{\prime}(x)=0 \quad \Rightarrow f(x)=\text { constant } \\
& \text { As } f(0)=0 \Rightarrow f(1)=0 .
\end{aligned}
$$

</details>

---

### Q126. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

Area of the greatest rectangle that can be inscribed in the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ is

**Options:**

- **(A)** $2 a b$
- **(B)** $a b$
- **(C)** $3a b$
- **(D)** $\frac{a}{b}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 a b$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JfuFeNVYXEScUNVUUXkAqxRSrCP1nT0LsmP2Y2qhrYA.original.fullsize.png">

Area of rectangle $A B C D=(2 a\cos \theta)$
$(2 b \sin \theta)=2 a b \sin 2 \theta$
$\Rightarrow$ Area of greatest rectangle is equal to
$2 a b$
when $\sin 2 \theta=1$.

</details>

---

### Q127. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

If $2 a+3 b+6 c=0$, then at least one root of the equation $a x^2+b x+c=0$ lies in the interval

**Options:**

- **(A)** $(0,1)$
- **(B)** $(1,2)$
- **(C)** $(2,3)$
- **(D)** $(1,3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(0,1)$**

**Detailed Solution:**

Let $f^{\prime}(x)=a x^2+b x+c \Rightarrow f(x)=\frac{a x^3}{3}+\frac{b x^2}{2}+c x+d$ $\Rightarrow f(x)=\frac{1}{6}\left(2 a x^3+3 b x^2+6 c x+6 d\right)$, Now $f(1)=f(0)=d$, then according to Rolle's theorem $\Rightarrow f^{\prime}(x)=a x^2+b x+c=0$ has at least one root in $(0,1)$

</details>

---

### Q128. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

A function $y=f(x)$ has a second order derivative $f^{\prime \prime}(x)=6(x-1)$. If its graph passes through the point $(2,1)$ and at that point the tangent to the graph is $y=3 x-5$, then the function is

**Options:**

- **(A)** $(x-1)^2$
- **(B)** $(x-1)^3$
- **(C)** $(x+1)^3$
- **(D)** $(x+1)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(x-1)^3$**

**Detailed Solution:**

$f^{\prime \prime}(x)=6(x-1) \Rightarrow f^{\prime}(x)=3(x-1)^2+c$
and $f^{\prime}(2)=3 \Rightarrow c=0$
$\Rightarrow f(x)=(x-1)^3+k$ and $f(2)=1 \Rightarrow k=0$
$\Rightarrow f(x)=(x-1)^3$

</details>

---

### Q129. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

A point on the parabola $y^2=18 x$ at which the ordinate increases at twice the rate of the abscissa is

**Options:**

- **(A)** $(2,4)$
- **(B)** $(2,-4)$
- **(C)** $\left(\frac{-9}{8}, \frac{9}{2}\right)$
- **(D)** $\left(\frac{9}{8}, \frac{9}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{9}{8}, \frac{9}{2}\right)$**

**Detailed Solution:**

Any point be $\left(\frac{9}{2} t^2, 9 t\right) ;$ differentiating $y^2=18 x$
$$
\begin{aligned}
& \Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{9}{\mathrm{y}}=\frac{1}{\mathrm{t}}=2 \text { (given) } \Rightarrow \mathrm{t}=\frac{1}{2} . \\
& \Rightarrow \text { Point is }\left(\frac{9}{8}, \frac{9}{2}\right)
\end{aligned}
$$

</details>

---

### Q130. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

The real number $x$ when added to its inverse gives the minimum value of the sum at $x$ equal to

**Options:**

- **(A)** $-2$
- **(B)** 2
- **(C)** 1
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$y=x+\frac{1}{x} \text { or } \frac{d y}{d x}=1-\frac{1}{x^2}$
For $\max$. or $\min ., 1-\frac{1}{x^2}=0 \Rightarrow x=\pm 1$
$\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}^2}=\frac{2}{\mathrm{x}^3} \Rightarrow\left(\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{dx}^2}\right)_{\mathrm{x}=2}=2(+$ ve minima)
Therefore $x=1$

</details>

---

### Q131. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If the function $\mathrm{f}(\mathrm{x})=2 \mathrm{x}^2-9 a \mathrm{x}^2+12 \mathrm{a}^2 \mathrm{x}+1$, where $\mathrm{a}>0$, attains its maximum and minimum at $\mathrm{p}$ and $\mathrm{q}$ respectively such that $\mathrm{p}^2=\mathrm{q}$, then a equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 3
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

$f(x)=2 x^3-9 a x^2+12 a^2 x+1$
$f^{\prime}(x)=6 x^2-18 a x+12 a^2 ; f^{\prime \prime}(x)=12 x-18 a$
For max. or min. $6 x^2-18 a x+12 a^2=0 \Rightarrow x^2-3 a x+2 a^2=0$
$\mathrm{x}=\mathrm{a}$ or $\mathrm{x}=2 \mathrm{a}$, at $\mathrm{x}=\mathrm{a}$ max.and at $\mathrm{x}=2 \mathrm{a} \min$.
$p^2=q$
$a^2=2 a \Rightarrow a=2$ or $a=0$
but $\mathrm{a}>0$, therefore, $\mathrm{a}=2$.

</details>

---

### Q132. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The maximum distance from origin of a point on the curve $x=a \sin t-b \sin \left(\frac{a t}{b}\right)$ 
$y=a \cos t-b \cos \left(\frac{a t}{b}\right)$, both $a, b>0$ is

**Options:**

- **(A)** a - b
- **(B)** a + b
- **(C)** $\sqrt{a^2+b^2}$
- **(D)** $\sqrt{a^2-b^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a - b**

**Detailed Solution:**

Distance of origin from $(x, y)=\sqrt{x^2+y^2}$
$$
=\sqrt{a^2+b^2-2 a b \cos \left(t-\frac{a t}{b}\right)}=\sqrt{a^2+b^2-2 a b}\left[\because \max \cdot \cos \left(t-\frac{a t}{b}\right)=1\right]=a-b
$$

</details>

---

