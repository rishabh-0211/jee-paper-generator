# JEE Main Mathematics - Differential Equations

## Topic 4: Homogeneous DE

**Total Questions:** 27

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $y = y(x)$ be the solution of the differential equation $x\sin\left(\dfrac{y}{x}\right)dy = \left(y\sin\left(\dfrac{y}{x}\right) - x\right)dx$, $y(1) = \dfrac{\pi}{2}$ and let $\alpha = \cos\left(\dfrac{y(e^{12})}{e^{12}}\right)$. Then the number of integral values of $p$, for which the equation $x^2 + y^2 - 2px + 2py + \alpha + 2 = 0$ represents a circle of radius $r \leq 6$, is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Given the differential equation:

$x\sin\left(\dfrac{y}{x}\right)dy = \left(y\sin\left(\dfrac{y}{x}\right) - x\right)dx$

Rearranging the terms, we get:

$x\sin\left(\dfrac{y}{x}\right)dy - y\sin\left(\dfrac{y}{x}\right)dx = -xdx$

Dividing both sides by $x^2$:

$\sin\left(\dfrac{y}{x}\right)\left(\dfrac{xdy - ydx}{x^2}\right) = -\dfrac{dx}{x}$

$\sin\left(\dfrac{y}{x}\right)d\left(\dfrac{y}{x}\right) = -\dfrac{dx}{x}$

Integrating both sides:

$-\cos\left(\dfrac{y}{x}\right) = -\ln|x| - C$

$\cos\left(\dfrac{y}{x}\right) = \ln|x| + C$

Using the initial condition $y(1) = \dfrac{\pi}{2}$:

$\cos\left(\dfrac{\pi}{2}\right) = \ln(1) + C \Rightarrow C = 0$

Thus, the solution to the differential equation is:

$\cos\left(\dfrac{y}{x}\right) = \ln|x|$

We need to find $\alpha = \cos\left(\dfrac{y(e^{12})}{e^{12}}\right)$. Substituting $x = e^{12}$:

$\alpha = \ln(e^{12}) = 12$

The given equation of the circle is:

$x^2 + y^2 - 2px + 2py + \alpha + 2 = 0$

Substituting $\alpha = 12$:

$x^2 + y^2 - 2px + 2py + 14 = 0$

The radius $r$ of the circle is given by:

$r = \sqrt{(-p)^2 + p^2 - 14} = \sqrt{2p^2 - 14}$

For the equation to represent a real circle, $r > 0$:

$2p^2 - 14 > 0 \Rightarrow p^2 > 7$

We are given that $r \leq 6$:

$\sqrt{2p^2 - 14} \leq 6$

$2p^2 - 14 \leq 36$

$2p^2 \leq 50 \Rightarrow p^2 \leq 25$

Combining the inequalities:

$7 < p^2 \leq 25$

Since $p$ is an integer, the possible values for $p^2$ are $9, 16, 25$.

This gives $p \in \{-5, -4, -3, 3, 4, 5\}$.

Therefore, there are $6$ integral values of $p$.

Answer: $6$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $x = x(y)$ be the solution of the differential equation $2y^2 \dfrac{dx}{dy} - 2xy + x^2 = 0$, $y > 1$, $x(e) = e$. Then $x(e^2)$ is equal to:

**Options:**

- **(A)** $\dfrac{3}{2} e^2$
- **(B)** $\dfrac{2}{3} e^2$
- **(C)** $e^2$
- **(D)** $2e^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2}{3} e^2$**

**Detailed Solution:**

The given differential equation is $2y^2 \dfrac{dx}{dy} - 2xy + x^2 = 0$.

Dividing by $2y^2$, we get:

$\dfrac{dx}{dy} - \dfrac{x}{y} + \dfrac{x^2}{2y^2} = 0$

This is a homogeneous differential equation. Let $x = vy$, then $\dfrac{dx}{dy} = v + y \dfrac{dv}{dy}$.

Substituting these into the equation:

$v + y \dfrac{dv}{dy} - v + \dfrac{v^2}{2} = 0$

$y \dfrac{dv}{dy} = -\dfrac{v^2}{2}$

Separating the variables:

$\dfrac{dv}{v^2} = -\dfrac{dy}{2y}$

Integrating both sides:

$\int v^{-2} dv = -\dfrac{1}{2} \int \dfrac{dy}{y}$

$-\dfrac{1}{v} = -\dfrac{1}{2} \ln y - C$

Substituting $v = \dfrac{x}{y}$:

$\dfrac{y}{x} = \dfrac{1}{2} \ln y + C$

Given $x(e) = e$, substituting $x = e$ and $y = e$:

$\dfrac{e}{e} = \dfrac{1}{2} \ln e + C$

$1 = \dfrac{1}{2} + C \Rightarrow C = \dfrac{1}{2}$

The particular solution is:

$\dfrac{y}{x} = \dfrac{1}{2} \ln y + \dfrac{1}{2} = \dfrac{\ln y + 1}{2}$

$x = \dfrac{2y}{\ln y + 1}$

To find $x(e^2)$, substitute $y = e^2$:

$x(e^2) = \dfrac{2e^2}{\ln(e^2) + 1} = \dfrac{2e^2}{2 + 1} = \dfrac{2}{3} e^2$

Answer: $\dfrac{2}{3} e^2$

</details>

---

### Q3. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the solution curve of the differential equation $x d y-y d x=\sqrt{x^{2}+y^{2}} d x, x>0$, $y(1)=0$, be $y=y(x)$. Then $y(3)$ is equal to

**Options:**

- **(A)** 1
- **(B)** 4
- **(C)** 2
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

$xdy - ydx = \sqrt{x^2+y^2}\,dx$.
Put $y = vx$: $x^2 dv = x\sqrt{1+v^2}\,dx$.
$\frac{dv}{\sqrt{1+v^2}} = \frac{dx}{x}$.
Integrating: $\ln(v+\sqrt{1+v^2}) = \ln x + C$.
$y(1) = 0 \Rightarrow v = 0$ at $x = 1$: $C = 0$.
$v + \sqrt{1+v^2} = x \Rightarrow y + \sqrt{x^2+y^2} = x^2$.
At $x = 3$: $y + \sqrt{9+y^2} = 9$ 
$\Rightarrow 9+y^2 = (9-y)^2$ 
$\Rightarrow 18y = 72$ 
$\Rightarrow y = 4$.

</details>

---

### Q4. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $x=x(y)$ be the solution of the differential equation $y=\left(x-y \frac{\mathrm{~d} x}{\mathrm{~d} y}\right) \sin \left(\frac{x}{y}\right), y\gt0$ and $x(1)=\frac{\pi}{2}$. Then $\cos (x(2))$ is equal to :

**Options:**

- **(A)** $1-2\left(\log _e 2\right)^2$
- **(B)** $1-2\left(\log _{\mathrm{e}} 2\right)$
- **(C)** $2\left(\log _e 2\right)-1$
- **(D)** $2\left(\log _e 2\right)^2-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2\left(\log _e 2\right)^2-1$**

**Detailed Solution:**

$\begin{aligned} & y d y=(x d y-y d x) \sin \left(\frac{x}{y}\right) \\ & \frac{d y}{y}=\left(\frac{x d y-y d x}{y^2}\right) \sin \left(\frac{x}{y}\right) \\ & \frac{d y}{y}=\sin \left(\frac{x}{y}\right) d\left(-\frac{x}{y}\right) \\ & \rightarrow \ell n y=\cos \frac{x}{y}+C\end{aligned}$
$\begin{aligned} & x(1)=\frac{\pi}{2} \Rightarrow 0=\cos \frac{\pi}{2}+C \Rightarrow C=0 \\ & \text { lny }=\cos \frac{x}{y} \\ & \text { but } y=2 \Rightarrow \cos \frac{x}{2}=\ell n 2 \\ & \cos x=2 \cos ^2 \frac{x}{2}-1 \\ & =2(\ln 2)^2-1\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution curve, of the differential equation $2 y \frac{\mathrm{d} y}{\mathrm{~d} x}+3=5 \frac{\mathrm{d} y}{\mathrm{~d} x}$, passing through the point $(0,1)$ is a conic, whose vertex lies on the line:

**Options:**

- **(A)** $2 x+3 y=9$
- **(B)** $2 x+3 y=-9$
- **(C)** $2 x+3 y=-6$
- **(D)** $2 x+3 y=6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 x+3 y=9$**

**Detailed Solution:**

$\begin{aligned} & (2 y-5) \frac{d y}{d x}=-3 \\ & (2 y-5) d y=-3 d x \\ & 2 \cdot \frac{y^2}{2}-5 y=-3 x+\lambda\end{aligned}$
$\because$ Curve passes through $(0,1)$
$\Rightarrow \lambda=-4$
$\because$ Curve will be
$\left(y-\frac{5}{2}\right)^2=-3\left(x-\frac{3}{4}\right)$
$\therefore$ Vertex of parabola will be $\left(\frac{3}{4}, \frac{5}{2}\right)$
$\because 2 x+3 y=9$

</details>

---

### Q6. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $(x+y+2)^2 d x=d y, y(0)=-2$. Let the maximum and minimum values of the function $y=y(x)$ in $\left[0, \frac{\pi}{3}\right]$ be $\alpha$ and $\beta$, respectively. If $(3 \alpha+\pi)^2+\beta^2=\gamma+\delta \sqrt{3}, \gamma, \delta \in \mathbb{Z}$, then $\gamma+\delta$ equals ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **31**

**Detailed Solution:**

$\frac{d y}{d x}=(x+y+2)^2$ ...(1)
$y(0)=-2$
Let $\mathrm{x}+\mathrm{y}+2=\mathrm{v}$
$1+\frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{dv}}{\mathrm{dx}}$
from (1) $\frac{d v}{d x}=1+v^2$
$\begin{aligned}
& \int \frac{d v}{1+v^2}=\int d x \\
& \tan ^{-1}(v)=x+C \\
& \tan ^{-1}(x+y+2)=x+C \\
& \text { at } x=0 y=-2 \Rightarrow C=0
\end{aligned}$
$\begin{aligned}
& \Rightarrow \tan ^{-1}(\mathrm{x}+\mathrm{y}+2)=\mathrm{x} \\
& \mathrm{y}=\tan \mathrm{x}-\mathrm{x}-2 \\
& \mathrm{f}(\mathrm{x})=\tan \mathrm{x}-\mathrm{x}-2, \mathrm{x} \in\left[0, \frac{\pi}{3}\right]
\end{aligned}$
$\begin{aligned}
& f^{\prime}(x)=\sec ^2 x-1>0 \Rightarrow f(x) \uparrow \\
& f_{\min }=f(0)=-2=\beta \\
& f_{\max }=f\left(\frac{\pi}{3}\right)=\sqrt{3}-\frac{\pi}{3}-2=\alpha
\end{aligned}$
now $(3 \alpha+\pi)^2+\beta^2=\gamma+\delta \sqrt{3}$
$\begin{aligned}
& \Rightarrow(3 \alpha+\pi)^2+\beta^2=(3 \sqrt{3}-6)^2+4 \\
& \gamma+\delta \sqrt{3}=67-36 \sqrt{3} \\
& \Rightarrow \gamma=67 \text { and } \delta=-36 \Rightarrow \gamma+\delta=31
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>x</mi><mo>&gt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>&gt;</mo><mn>0</mn></math> passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>e</mi><mo>,</mo><mo> </mo><mn>1</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>y</mi><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>y</mi><mi>x</mi></mfrac></mrow></mfenced><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo> </mo><mi>x</mi><mo>&gt;</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mfenced close="]" open="["><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>v</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfenced><mfrac><mrow><mi>v</mi><mi>y</mi></mrow><mi>y</mi></mfrac></mfenced><mfenced close="]" open="["><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>v</mi><mi>y</mi></mrow><mi>y</mi></mfrac></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mfenced close="]" open="["><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>v</mi></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>v</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>v</mi></mfenced><mo>+</mo><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mi>v</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mi>v</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>v</mi><msub><mi>log</mi><mi>e</mi></msub><mi>v</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>v</mi><msub><mi>log</mi><mi>e</mi></msub><mi>v</mi></mrow></mfrac><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>v</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mi>v</mi></mfrac><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>t</mi><mo>=</mo><mi>log</mi><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>log</mi><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p>Using point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>e</mi><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>e</mi></mrow></mfenced><mo>=</mo><mi>log</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>log</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><msub><mi>log</mi><mi>e</mi></msub><mfrac><mi>x</mi><mi>y</mi></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi></math></p>

</details>

---

### Q8. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mo>|</mo><mi>x</mi><mo>|</mo><mo>+</mo><mfrac><mi>α</mi><mn>2</mn></mfrac></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>+</mo><mn>1</mn></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>cos</mi><mi>v</mi><mfenced><mrow><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>v</mi><mi>cos</mi><mi>v</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>v</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>v</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>cos</mi><mi>v</mi></mrow></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfenced><mrow><mi>cos</mi><mi>v</mi></mrow></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mi>v</mi><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mi>π</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mfenced><mfrac><mi>π</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mn>1</mn></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sin</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p>So, on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q9. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

If the solution curve, of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac></math> passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mi>β</mi></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>α</mi><mo>+</mo><msup><mfenced><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>β</mi><mo>+</mo><mi>α</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac></math></p><p>Now, finding the intersection point of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>x</mi><mo>=</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>≡</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>X</mi><mo>+</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>=</mo><mi>Y</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>Y</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>X</mi><mo>+</mo><mi>Y</mi></mrow><mrow><mi>X</mi><mo>-</mo><mi>Y</mi></mrow></mfrac></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>t</mi><mi>X</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>Y</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>+</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>t</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>+</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>t</mi><mo>-</mo><mi>t</mi><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mi>X</mi></mfrac><mi>d</mi><mi>X</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mn>1</mn><mi>X</mi></mfrac><mi>d</mi><mi>X</mi><mo>=</mo><mo>∫</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced close="|" open="|"><mi>X</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>It is given that the solution curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>0</mn></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mn>1</mn></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mi>β</mi><mo>+</mo><mi>α</mi><mo>=</mo><mn>11</mn></math>.</p>

</details>

---

### Q10. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

If the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>(</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>3</mn></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mi>x</mi><mo>+</mo><mi>β</mi><mi>y</mi><mo>+</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mo>|</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>γ</mi><mo>|</mo><mo>=</mo><mn>6</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>+</mo><mn>3</mn><mi>γ</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>(</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>7</mn><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mfenced><mrow><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>7</mn></mrow></mfenced></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>+</mo><mn>3</mn><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mfrac><mi>dt</mi><mi>dx</mi></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>2</mn><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi mathvariant="normal">x</mi><mo>+</mo><mn>6</mn><mi mathvariant="normal">y</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>2</mn><mi mathvariant="normal">t</mi><mo>-</mo><mn>3</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mi>t</mi></mrow><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>t</mi></mrow><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>4</mn><mi>t</mi><mo>-</mo><mn>6</mn></mrow><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>t</mi><mo>-</mo><mn>6</mn></mrow><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>3</mn></mrow><mrow><mi>t</mi><mo>-</mo><mn>6</mn></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mo>∫</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfenced><mrow><mfrac><mrow><mn>2</mn><mi>t</mi><mo>-</mo><mn>12</mn></mrow><mrow><mi>t</mi><mo>-</mo><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mn>9</mn><mrow><mi>t</mi><mo>-</mo><mn>6</mn></mrow></mfrac></mrow></mfenced><mo>·</mo><mi>d</mi><mi>t</mi><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>t</mi><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mi>t</mi><mo>-</mo><mn>6</mn><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>(</mo><mn>0</mn><mo>+</mo><mn>9</mn><mo>-</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mn>0</mn><mo>+</mo><mn>9</mn><mo>-</mo><mn>8</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>14</mn><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>14</mn></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>-</mo><mn>4</mn><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>6</mn><mi>y</mi><mo>+</mo><mn>9</mn><mi>log</mi><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mn>3</mn><mi>log</mi><mo>(</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mn>8</mn><mo>)</mo><mo>=</mo><mn>6</mn></math></p><p>Comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mi>x</mi><mo>+</mo><mi>β</mi><mi>y</mi><mo>+</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mo>|</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><mi>y</mi><mo>-</mo><mi>γ</mi><mo>|</mo><mo>=</mo><mn>6</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>β</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><mi>γ</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>+</mo><mn>3</mn><mi>γ</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>+</mo><mn>3</mn><mi>γ</mi><mo>=</mo><mn>29</mn></math></p>

</details>

---

### Q11. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The slope of tangent at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> on a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>0</mn></math>, then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>8</mn></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mn>2</mn><mi>x</mi><mi>y</mi></mstyle></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mn>2</mn><mi>v</mi></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mn>2</mn><mi>v</mi></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mfrac><mrow><mn>2</mn><mi>v</mi></mrow><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>C</mi><mi>x</mi></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mi>C</mi><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>C</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><msqrt><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><mn>16</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><msqrt><mn>48</mn></msqrt><mo>=</mo><mn>4</mn><msqrt><mn>3</mn></msqrt></math></p></blockquote>

</details>

---

### Q12. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>y</mi><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>(</mo><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><msup><mo>)</mo><mn>3</mn></msup><mo>-</mo><mn>12</mn><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>y</mi><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi><mfenced><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p>This is homogeneous differential equation</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>t</mi><mi>x</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>t</mi><mi>x</mi><mo>)</mo><mfenced><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>t</mi><mfenced><mrow><mn>5</mn><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>t</mi><mo>-</mo><mn>3</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mi>t</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup></mrow><mrow><mn>2</mn><mo>-</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>3</mn><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math></p><p>Taking integration on both sides we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced></mrow><mrow><mn>3</mn><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup><mo>=</mo><mi>z</mi><mo>&#8658;</mo><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>d</mi><mi>z</mi></math></p><p>Substitute in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><mi>z</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>ln</mi><mo>(</mo><mi mathvariant="normal">z</mi><mo>)</mo><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>z</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>=</mo><mi>c</mi><mi>x</mi><mo>&#8658;</mo><mi>z</mi><mo>=</mo><msup><mi>c</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>t</mi><mo>-</mo><msup><mi>t</mi><mn>3</mn></msup><mo>=</mo><msup><mi>c</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mi>y</mi></mrow><mi>x</mi></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><msup><mi>c</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>c</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>=</mo><mn>2</mn></math></p><p>So, equation becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>=</mo><mn>2</mn><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><msup><mi>y</mi><mn>3</mn></msup><mo>=</mo><mn>2</mn><msup><mi>x</mi><mfrac><mn>9</mn><mn>2</mn></mfrac></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>-</mo><msup><mfenced><mrow><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mn>2</mn><mo>(</mo><mn>2</mn><msup><mo>)</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></msup><mo>=</mo><mn>32</mn><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><mrow><msup><mfenced><mrow><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfenced><mn>3</mn></msup><mo>-</mo><mn>12</mn><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow></mfenced><mo>=</mo><mn>32</mn><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q13. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>Differential equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><msup><mi>v</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><msup><mfenced><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mrow><mn>3</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>v</mi></mrow><msup><mfenced><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><mi>d</mi><mi>v</mi></mrow><msup><mfenced><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>d</mi><mi>v</mi></mrow><msup><mfenced><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msup><mfenced><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mrow><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mi>x</mi></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>+</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q14. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>&#8211;</mo><mo>&#160;</mo><mn>3</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>)</mo><mi>dx</mi><mo>+</mo><mn>3</mn><mi>xy</mi><mo>&#160;</mo><mi>dy</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mfenced><mi mathvariant="normal">e</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Given equation is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>&#8211;</mo><mo>&#160;</mo><mn>3</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>)</mo><mi>dx</mi><mo>+</mo><mn>3</mn><mi>xydy</mi><mo>=</mo><mn>0</mn></math></p><p>We can re-write equation as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>3</mn><mi>xy</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mfrac><mi mathvariant="normal">y</mi><mi mathvariant="normal">x</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mi mathvariant="normal">x</mi><mi mathvariant="normal">y</mi></mfrac><mo>&#160;</mo></math>  ....(1)</p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi>vx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mi mathvariant="normal">v</mi><mo>+</mo><mi mathvariant="normal">x</mi><mfrac><mi>dv</mi><mi>dx</mi></mfrac></math></p><p>Equation (1) can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi><mo>+</mo><mi mathvariant="normal">x</mi><mfrac><mi>dv</mi><mi>dx</mi></mfrac><mo>=</mo><mi mathvariant="normal">v</mi><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>1</mn><mi mathvariant="normal">v</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>vdv</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi mathvariant="normal">x</mi></mrow></mfrac></math></p><p>Integrating both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi mathvariant="normal">v</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>ln</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mrow><mn>2</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mi>ln</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mi mathvariant="normal">c</mi></math>        .....(2)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi mathvariant="normal">y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>     (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi mathvariant="normal">c</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>       (from equation 2)</p><p>Equation (2) can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mrow><mn>2</mn><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mi>ln</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mi>ln</mi><mfenced><mi mathvariant="normal">x</mi></mfenced><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>(</mo><mi mathvariant="normal">e</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mi>ln</mi><mfenced><mi mathvariant="normal">e</mi></mfenced><mo>+</mo><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>(</mo><mi mathvariant="normal">e</mi><mo>)</mo><mo>=</mo><mn>2</mn><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></math></p>

</details>

---

### Q15. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>. If for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>&#8712;</mo><mo>[</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mfrac><mfenced><mrow><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mfrac><mfenced><mrow><mn>4</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>v</mi><mfenced><mrow><mn>4</mn><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mfenced><mrow><mn>3</mn><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mfenced><mfrac><mfenced><mrow><mn>4</mn><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>-</mo><mn>3</mn><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>3</mn><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mrow><mn>3</mn><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><msup><mi>v</mi><mn>3</mn></msup><mo>+</mo><mi>v</mi></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mi>v</mi><mn>3</mn></msup><mo>+</mo><mi>v</mi></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mi>ln</mi><mn>2</mn></math></p><p>So the equation becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math></p><p>So putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p> We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><mi>y</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mi>ln</mi><mn>2</mn><mo>&#8658;</mo><mfrac><msup><mi>y</mi><mn>3</mn></msup><mn>8</mn></mfrac><mo>+</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mi>y</mi><mfenced><mn>2</mn></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>&#8712;</mo><mo>[</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p>So on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>&#8712;</mo><mo>[</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>y</mi></mrow><mi>x</mi></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mi>t</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>t</mi><mo>=</mo><mi>t</mi><mo>+</mo><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn></msqrt></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p>Now integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn></msqrt></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>t</mi><mo>+</mo><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn></msqrt></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>x</mi></mfrac><mo>=</mo><mi>c</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>1</mn></mfrac><mo>+</mo><mfrac><msqrt><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>&#215;</mo><msup><mn>1</mn><mn>2</mn></msup></msqrt><mn>1</mn></mfrac><mo>=</mo><mi>c</mi><mo>&#215;</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>8</mn></math></p><p>So solution becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>x</mi></mfrac><mo>=</mo><mn>8</mn><mi>x</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>16</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup></msqrt><mn>2</mn></mfrac><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>+</mo><msqrt><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>64</mn></msqrt><mo>=</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q17. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mi>y</mi></math> pass through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>&#945;</mi><mo>,</mo><mi>&#945;</mi></mrow></mfenced><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>exp</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><msqrt><mi mathvariant="normal">e</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>exp</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><msqrt><mi>e</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><msqrt><mi mathvariant="normal">e</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>exp</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><msqrt><mi mathvariant="normal">e</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>exp</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><msqrt><mi mathvariant="normal">e</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mfenced><mrow><mfrac><mi>x</mi><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mo>+</mo><mi>x</mi></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> common &amp; cancelling them we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#215;</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced><mo>=</mo><mi>v</mi><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mfrac><mn>1</mn><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p>Integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup></mrow></mfenced><mi>d</mi><mi>v</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>v</mi><mo>+</mo><msup><mi>e</mi><mi>v</mi></msup><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>c</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>0</mn><mn>1</mn></mfrac></mfenced><mo>+</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mi>ln</mi><mn>1</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>+</mo><msup><mi>e</mi><mfrac><mi>y</mi><mi>x</mi></mfrac></msup><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mn>1</mn></math> ........(i)</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mn>2</mn><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mi>&#945;</mi></math> putting in equation (i) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>&#945;</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></mfrac></mfenced><mo>+</mo><msup><mi>e</mi><mfrac><mi>&#945;</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></mfrac></msup><mo>=</mo><mi>ln</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mi>ln</mi><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>1</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><msqrt><mi>e</mi></msqrt><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q18. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi mathvariant="normal">d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>, which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>x</mi></math> at the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced></math>, then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>v</mi><mi>y</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></math></p><p>Now putting in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>v</mi><mo>+</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mi>v</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>y</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mo>-</mo><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>v</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math> </p><p>Now Integrating Both side</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>v</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>v</mi><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>y</mi></mfenced><mo>+</mo><mi>c</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>y</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p>Also  this curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mn>1</mn></mfenced><mo>+</mo><mi>c</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mi>y</mi></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#945;</mi></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mi>x</mi><mrow><msqrt><mn>3</mn></msqrt><mi>x</mi></mrow></mfrac><mo>=</mo><mi>log</mi><mfenced open="|" close="|"><mrow><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mi>log</mi><mfenced><mrow><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mi>log</mi><mfenced open="|" close="|"><mrow><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced open="|" close="|"><mrow><msqrt><mn>3</mn></msqrt><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac></math></p>

</details>

---

### Q19. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfrac><mrow><mi mathvariant="normal">d</mi><mi>y</mi></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow><mrow><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfrac></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>&#981;</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#981;</mi><mfenced><mn>2</mn></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></math>**

**Detailed Solution:**

<p>Given:<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>x</mi></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow><mrow><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfrac></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> </p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>x</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>+</mo><mi>x</mi><mo>&#183;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>t</mi><mfenced><mrow><mi>t</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow><mrow><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>t</mi><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow><mrow><mi>&#981;</mi><mo>&#39;</mo><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>t</mi><mo>&#183;</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow><mrow><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math>
Integrating both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>t</mi><mo>&#183;</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow><mrow><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced></mrow></mfrac><mi>d</mi><mi>t</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced><mo>=</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#981;</mi><mo>&#39;</mo></msup><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced><mo>.</mo><mn>2</mn><mi>t</mi><mo>=</mo><mi>d</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mi>p</mi></mfrac><mi>d</mi><mi>p</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mi>p</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mi>&#981;</mi><mfenced><msup><mi>t</mi><mn>2</mn></msup></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p>Substituting value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> then </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mi>ln</mi><mn>4</mn><mo>+</mo><mi>ln</mi><mfenced><mrow><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p>SO, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi><mfenced><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>4</mn><mi>&#981;</mi><mfenced><mn>1</mn></mfenced></math></p>

</details>

---

### Q20. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> be the curve obtained by the solution of differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. Let the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> be the solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>. If both the curves pass through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo></math> then the area (in sq. units) enclosed by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#960;</mi><mo>+</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow></mfrac><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p>put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>v</mi><mo>=</mo><mfrac><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>v</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>v</mi></mrow><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>v</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p>Integrate,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mi>n</mi><mfenced><mrow><msup><mi>v</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi>l</mi><mi>n</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mi>n</mi><mfenced><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi>l</mi><mi>n</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>C</mi><mo>=</mo><mi>l</mi><mi>n</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mi>n</mi><mfenced><mrow><mfrac><msup><mi>y</mi><mn>2</mn></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi>l</mi><mi>n</mi><mi>x</mi><mo>+</mo><mi>l</mi><mi>n</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn></math> (Curve <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub></math>)</p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mi>y</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mo>&#160;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ec862e26-0ec9-4731-aeba-dc047d74e438-image.png" style="width: 272px; height: 204px;" /></p><p>Required area <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><mfenced><mrow><msqrt><mn>2</mn><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></math> sq. units</p>

</details>

---

### Q21. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math>, passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>, is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>t</mi><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math> </p><p>This is a linear differential equation,</p><p>with Integrating Factor : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced><mi>x</mi></mfenced></mrow></msup><mo>=</mo><mi>x</mi></math> </p><p>So, solution of the linear differential equation is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#183;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>-</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>C</mi></math></p><p> The curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi mathvariant="normal">C</mi><mo>&#8658;</mo><mi mathvariant="normal">C</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> </p><p>Hence, the particular solution to the differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced></mrow><mn>2</mn></mfrac><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mi>ln</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>2</mn></mfenced></mrow></mfrac></math></p>

</details>

---

### Q22. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>;</mo><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>;</mo></math> then a value of <math><mi>x</mi></math> satisfying <math><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>e</mi></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msqrt><mn>3</mn></msqrt><mi></mi><mi mathvariant="normal">e</mi></math>
- **(B)** <math><mfrac><mrow><mi>e</mi></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><msqrt><mn>2</mn></msqrt><mi></mi><mi mathvariant="normal">e</mi></math>
- **(D)** <math><msqrt><mn>3</mn></msqrt><mi></mi><mi mathvariant="normal">e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msqrt><mn>3</mn></msqrt><mi></mi><mi mathvariant="normal">e</mi></math>**

**Detailed Solution:**

<p>Put <math><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>v</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi>v</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>v</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mrow><mo stretchy="false">&#8747;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>v</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>v</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mi>d</mi><mi>v</mi><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></mrow></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mi mathvariant="script">l</mi><mi>n</mi><mi>v</mi><mo>=</mo><mo>-</mo><mi mathvariant="script">l</mi><mi>n</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mo>-</mo><mi mathvariant="script">l</mi><mi>n</mi><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p>When <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi></mi><mi>y</mi><mo>=</mo><mn>1</mn></math> then</p><p><math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>c</mi></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi mathvariant="script">l</mi><mi>n</mi><mi>y</mi></mrow></mfenced></math></p><p><math><mo>&#8658;</mo><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></math></p>

</details>

---

### Q23. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

The curve satisfying the differential equation, $\left(x^2-y^2\right) d x+2 x y d y=0$ and passing through the point $(1,1)$ is

**Options:**

- **(A)** a circle of radius two
- **(B)** a circle of radius one
- **(C)** a hyperbola
- **(D)** an ellipse

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a circle of radius one**

**Detailed Solution:**

$\left(x^2-y^2\right) d x+2 x y d y=0$
$$
\Rightarrow \frac{d y}{d x}=\frac{y^2-x^2}{2 x y}
$$
Let $y=v x$
$$
\begin{aligned}
& \frac{d y}{d x}=v+x \frac{d v}{d x} \\
\Rightarrow & v+x \frac{d v}{d x}=\frac{v^2 x^2-x^2}{2 v x^2} \\
\Rightarrow & v+x \frac{d v}{d x}=\frac{v^2-1}{2 v} \\
\Rightarrow & x \frac{d v}{d x}=\frac{-v^2-1}{2 v} \\
\Rightarrow & \frac{2 v d v}{v^2+1}=-\frac{d x}{x}
\end{aligned}
$$
After integrating, we get
$$
\begin{aligned}
&\ln \left|v^2+1\right|=-\ln |x|+\ln c \\
&\frac{y^2}{x^2}+1=\frac{c}{x}
\end{aligned}
$$
As curve passes through the point $(1,1)$, so $1+1=c \Rightarrow c=2$
$x^2+y^2-2 x=0$, which is a circle of radius one.

</details>

---

### Q24. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation, $\sin 2 x\left(\frac{d y}{d x}-\sqrt{\tan x}\right)-y=0$, is :

**Options:**

- **(A)** $y \sqrt{\tan x}=x+c$
- **(B)** $y \sqrt{\cot x}=\tan x+c$
- **(C)** $y \sqrt{\tan x}=\cot x+c$
- **(D)** $y \sqrt{\cot x}=x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y \sqrt{\cot x}=x+c$**

**Detailed Solution:**

Given, $\sin 2 x\left(\frac{d y}{d x}-\sqrt{\tan x}\right)-y=0$ or, $\frac{d y}{d x}=\frac{y}{\sin 2 x}+\sqrt{\tan x}$ or, $\frac{d y}{d x}-y \operatorname{cosec} 2 x=\sqrt{\tan x}$
Now, integrating factor (I.F) $=e^{\int-\operatorname{cosec} 2 x}$ or, I.F $=e^{-\frac{1}{2} \log |\tan x|}=e^{\log (\sqrt{\tan x})^{-1}}$ $=\frac{1}{\sqrt{\tan x}}=\sqrt{\cot x}$
Now, general solution of eq. (1) is written as
$$
\begin{aligned}
&\text { y (I. F.) }=\int \mathrm{Q}(\text { I.F.) } d x+c \\
&\therefore y \sqrt{\cot x}=\int \sqrt{\tan x} \cdot \sqrt{\cot x} d x+c \\
&\therefore y \sqrt{\cot x}=\int 1 . d x+c
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dXdl7fCMq5T1A8wnNuKIHujN-I3iGV7MzmHzzcN4FY8.original.fullsize.png">

</details>

---

### Q25. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Consider the differential equation :
$$
\frac{d y}{d x}=\frac{y^3}{2\left(x y^2-x^2\right)}
$$
Statement-1: The substitution $z=y^2$ transforms the above equation into a first order homogenous differential equation.
Statement-2: The solution of this differential equation is $y^2 e^{-y^2} / x=C$.

**Options:**

- **(A)** Both statements are false.
- **(B)** Statement-1 is true and statement- 2 is false.
- **(C)** Statement-1 is false and statement-2 is true.
- **(D)** Both statements are true.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Both statements are true.**

**Detailed Solution:**

Given differential equation is
$$
\frac{d y}{d x}=\frac{y^3}{2\left(x y^2-x^2\right)}
$$
By substituting $z=y^2$, we get diff. eqn. as
$$
\frac{d z}{d x}=\frac{2 z^2}{2\left(x z-x^2\right)}=\frac{z^2}{x z-x^2}
$$
Now, $\frac{d x}{d z}=\frac{x}{z}-\frac{x^2}{z^2}=\frac{x}{z}\left[1-\frac{x}{z}\right] \approx \mathrm{F}\left(\frac{x}{z}\right)$
Hence, statement-1 is true.
Now, $y^2 e^{-y^2 / x}=\mathrm{C}$ satisfies the given diff. equation
$\therefore$ It is the solution of given diff. equation. Thus, statement $-2$ is also true.

</details>

---

### Q26. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\frac{d y}{d x}=\frac{x+y}{x}$ satisfying the condition $y(1)=1$ is

**Options:**

- **(A)** $y=\ln x+x$
- **(B)** $y=x \ln x+x^2$
- **(C)** $y=x e^{(x-1)}$
- **(D)** $y=x \ln x+x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=x \ln x+x$**

**Detailed Solution:**

$$
y=v x
$$

$$
\begin{aligned}
& \frac{d y}{d x}=v+x \frac{d v}{d x} \\
& v+x \frac{d v}{d x}=1+v \\
& \Rightarrow d v=\frac{d x}{x} \\
& \therefore v=\log x+c \\
& \Rightarrow \frac{y}{x}=\log x+c
\end{aligned}
$$
Since, $y(1)=1$, we have
$$
y=x \log x+x
$$

</details>

---

### Q27. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If $x \frac{d y}{d x}=y(\log y-\log x+1)$, then the solution of the equation is

**Options:**

- **(A)** $y \log \left(\frac{x}{y}\right)=c x$
- **(B)** $x \log \left(\frac{y}{x}\right)=c y$
- **(C)** $\log \left(\frac{y}{x}\right)=c x$
- **(D)** $\log \left(\frac{x}{y}\right)=c y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log \left(\frac{y}{x}\right)=c x$**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{x d y}{d x}=y(\log y-\log x+1) \\
& \frac{d y}{d x}=\frac{y}{x}\left(\log \left(\frac{y}{x}\right)+1\right)
\end{aligned}
$$
Put $y=v x$
$\frac{d y}{d x}=v+\frac{x d v}{d x}$
$\Rightarrow v+\frac{x d v}{d x}=v(\log v+1)$
$\frac{x d v}{d x}=v \log v$
$\Rightarrow \frac{d v}{v \log v}=\frac{d x}{x}$
put $\log v=z$
$\frac{1}{v} d v=d z$
$\Rightarrow \frac{d z}{z}=\frac{d x}{x}$
$\ln z=\ln x+\ln c$
$z=c x$
$\log v=c x$
$\log \left(\frac{y}{x}\right)=c x$

</details>

---

