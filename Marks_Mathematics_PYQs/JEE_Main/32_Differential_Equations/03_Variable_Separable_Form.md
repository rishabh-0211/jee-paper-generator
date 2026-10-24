# JEE Main Mathematics - Differential Equations

## Topic 3: Variable Separable Form

**Total Questions:** 46

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $y = y(x)$ be the solution of the differential equation $(x^2 - x\sqrt{x^2 - 1})dy + (y(x - \sqrt{x^2 - 1}) - x)dx = 0$, $x \geq 1$. If $y(1) = 1$, then the greatest integer less than $y(\sqrt{5})$ is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

The given differential equation is:

$(x^2 - x\sqrt{x^2 - 1})dy + (y(x - \sqrt{x^2 - 1}) - x)dx = 0$

Dividing the entire equation by $dx$ and rearranging, we get:

$x(x - \sqrt{x^2 - 1}) \dfrac{dy}{dx} + y(x - \sqrt{x^2 - 1}) = x$

Dividing by $x(x - \sqrt{x^2 - 1})$, we obtain a linear differential equation:

$\dfrac{dy}{dx} + \dfrac{1}{x}y = \dfrac{1}{x - \sqrt{x^2 - 1}}$

The integrating factor (I.F.) is:

$\text{I.F.} = e^{\int \dfrac{1}{x} dx} = e^{\ln x} = x$

Multiplying the differential equation by the integrating factor $x$, we get:

$x \dfrac{dy}{dx} + y = \dfrac{x}{x - \sqrt{x^2 - 1}}$

$\dfrac{d}{dx}(xy) = \dfrac{x(x + \sqrt{x^2 - 1})}{(x - \sqrt{x^2 - 1})(x + \sqrt{x^2 - 1})}$

$\dfrac{d}{dx}(xy) = \dfrac{x^2 + x\sqrt{x^2 - 1}}{x^2 - (x^2 - 1)}$

$\dfrac{d}{dx}(xy) = x^2 + x\sqrt{x^2 - 1}$

Integrating both sides with respect to $x$:

$\int d(xy) = \int (x^2 + x\sqrt{x^2 - 1}) dx$

$xy = \dfrac{x^3}{3} + \dfrac{(x^2 - 1)^{3/2}}{3} + C$

Given $y(1) = 1$, we substitute $x = 1$ and $y = 1$:

$1(1) = \dfrac{1^3}{3} + 0 + C \Rightarrow C = 1 - \dfrac{1}{3} = \dfrac{2}{3}$

So, the particular solution is:

$xy = \dfrac{x^3}{3} + \dfrac{(x^2 - 1)^{3/2}}{3} + \dfrac{2}{3}$

To find $y(\sqrt{5})$, we substitute $x = \sqrt{5}$:

$\sqrt{5} y(\sqrt{5}) = \dfrac{(\sqrt{5})^3}{3} + \dfrac{(5 - 1)^{3/2}}{3} + \dfrac{2}{3}$

$\sqrt{5} y(\sqrt{5}) = \dfrac{5\sqrt{5}}{3} + \dfrac{4^{3/2}}{3} + \dfrac{2}{3}$

$\sqrt{5} y(\sqrt{5}) = \dfrac{5\sqrt{5}}{3} + \dfrac{8}{3} + \dfrac{2}{3} = \dfrac{5\sqrt{5} + 10}{3}$

$y(\sqrt{5}) = \dfrac{5}{3} + \dfrac{10}{3\sqrt{5}} = \dfrac{5 + 2\sqrt{5}}{3}$

Since $\sqrt{5} \approx 2.236$, we have $2\sqrt{5} \approx 4.472$.

$y(\sqrt{5}) \approx \dfrac{5 + 4.472}{3} = \dfrac{9.472}{3} \approx 3.157$

The greatest integer less than $y(\sqrt{5})$ is $3$.

Answer: $3$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y = y(x)$ be the solution of the differential equation $\dfrac{dy}{dx} = (1 + x + x^2)(1 - y + y^2)$, $y(0) = \dfrac{1}{2}$. Then $(2y(1) - 1)$ is equal to:

**Options:**

- **(A)** $\sqrt{3}\tan\left(\dfrac{11\sqrt{3}}{6}\right)$
- **(B)** $\dfrac{\sqrt{3}}{2}\tan\left(\dfrac{11\sqrt{3}}{12}\right)$
- **(C)** $\sqrt{3}\tan\left(\dfrac{11\sqrt{3}}{12}\right)$
- **(D)** $\dfrac{\sqrt{3}}{2}\tan\left(\dfrac{11\sqrt{3}}{6}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sqrt{3}\tan\left(\dfrac{11\sqrt{3}}{12}\right)$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = (1 + x + x^2)(1 - y + y^2)$.

Separating the variables:

$\dfrac{dy}{y^2 - y + 1} = (x^2 + x + 1) dx$

Integrating both sides:

$\int \dfrac{dy}{\left(y - \dfrac{1}{2}\right)^2 + \dfrac{3}{4}} = \int (x^2 + x + 1) dx$

$\dfrac{2}{\sqrt{3}} \tan^{-1}\left(\dfrac{y - \dfrac{1}{2}}{\dfrac{\sqrt{3}}{2}}\right) = \dfrac{x^3}{3} + \dfrac{x^2}{2} + x + C$

$\dfrac{2}{\sqrt{3}} \tan^{-1}\left(\dfrac{2y - 1}{\sqrt{3}}\right) = \dfrac{x^3}{3} + \dfrac{x^2}{2} + x + C$

Given $y(0) = \dfrac{1}{2}$, substituting $x = 0$ and $y = \dfrac{1}{2}$:

$\dfrac{2}{\sqrt{3}} \tan^{-1}(0) = C \Rightarrow C = 0$

Substituting $x = 1$ to find $y(1)$:

$\dfrac{2}{\sqrt{3}} \tan^{-1}\left(\dfrac{2y(1) - 1}{\sqrt{3}}\right) = \dfrac{1^3}{3} + \dfrac{1^2}{2} + 1$

$\dfrac{2}{\sqrt{3}} \tan^{-1}\left(\dfrac{2y(1) - 1}{\sqrt{3}}\right) = \dfrac{11}{6}$

$\tan^{-1}\left(\dfrac{2y(1) - 1}{\sqrt{3}}\right) = \dfrac{11\sqrt{3}}{12}$

$2y(1) - 1 = \sqrt{3}\tan\left(\dfrac{11\sqrt{3}}{12}\right)$

Answer: $\sqrt{3}\tan\left(\dfrac{11\sqrt{3}}{12}\right)$

</details>

---

### Q3. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y = y(x)$ be the solution curve of the differential equation $(1 + \sin x)\dfrac{dy}{dx} + (y+1)\cos x = 0$, $y(0) = 0$. If the curve $y = y(x)$ passes through the point $\left(\alpha, \dfrac{-1}{2}\right)$, then a value of $\alpha$ is :

**Options:**

- **(A)** $\dfrac{\pi}{6}$
- **(B)** $\dfrac{\pi}{4}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\pi}{2}$**

**Detailed Solution:**

The given differential equation can be written as:

$(1 + \sin x)dy + (y+1)\cos x dx = 0$

$d((y+1)(1 + \sin x)) = 0$

Integrating both sides:

$(y+1)(1 + \sin x) = C$

Given $y(0) = 0$, substituting $x = 0$ and $y = 0$:

$(0+1)(1 + \sin 0) = C \Rightarrow C = 1$

The equation of the curve is $(y+1)(1 + \sin x) = 1$

Since the curve passes through $\left(\alpha, \dfrac{-1}{2}\right)$, substituting $x = \alpha$ and $y = \dfrac{-1}{2}$:

$\left(\dfrac{-1}{2} + 1\right)(1 + \sin \alpha) = 1$

$\dfrac{1}{2}(1 + \sin \alpha) = 1$

$1 + \sin \alpha = 2$

$\sin \alpha = 1$

$\alpha = \dfrac{\pi}{2}$

Answer: $\dfrac{\pi}{2}$

</details>

---

### Q4. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the curve $y = f(x)$ passes through the point $(1, e)$ and satisfies the differential equation $dy = y(2 + \log_e x)\,dx$, $x > 0$, then $f(e)$ is equal to :

**Options:**

- **(A)** $e^e$
- **(B)** $e^{e^2}$
- **(C)** $e^{2e}$
- **(D)** $e^{2e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^{2e}$**

**Detailed Solution:**

Given differential equation is $\dfrac{dy}{y} = (2 + \log_e x) dx$

Integrating both sides, we get:

$\int \dfrac{dy}{y} = \int (2 + \log_e x) dx$

$\log_e y = 2x + x \log_e x - x + C$

$\log_e y = x + x \log_e x + C$

Since the curve passes through $(1, e)$, substitute $x = 1$ and $y = e$:

$\log_e e = 1 + 1 \cdot \log_e 1 + C$

$1 = 1 + 0 + C \Rightarrow C = 0$

The equation of the curve is $\log_e y = x + x \log_e x$

To find $f(e)$, substitute $x = e$:

$\log_e y = e + e \log_e e$

$\log_e y = e + e(1) = 2e$

$y = e^{2e}$

Answer: $e^{2e}$

</details>

---

### Q5. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $f$ be a twice differentiable non-negative function such that $(f(x))^{2}=25+\int_{0}^{x}\left((f(\mathrm{t}))^{2}+\left(f^{\prime}(\mathrm{t})\right)^{2}\right) \mathrm{dt}$. Then the mean of $f\left(\log _{\mathrm{e}}(1)\right), f\left(\log _{\mathrm{e}}(2)\right), \ldots.., f\left(\log _{\mathrm{e}}(625)\right)$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1565**

**Detailed Solution:**

Differentiating $(f(x))^2 = 25 + \int_0^x((f(t))^2 + (f'(t))^2)\,dt$:
$2ff' = f^2 + (f')^2 \Rightarrow (f - f')^2 = 0 \Rightarrow f' = f$.
$f(x) = Ce^x$. At $x = 0$: $f(0)^2 = 25 \Rightarrow f(0) = 5$ (non-negative), so $f(x) = 5e^x$.
$f(\log_e k) = 5k$ for $k = 1, 2, \ldots, 625$.
Mean $= \frac{5(1+2+\cdots+625)}{625} = \frac{5 \times 625 \times 626}{2 \times 625} = \frac{5 \times 626}{2} = 1565$.

</details>

---

### Q6. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $y=y(x)$ satisfies the differential equation $16(\sqrt{x+9 \sqrt{x}})(4+\sqrt{9+\sqrt{x}}) \cos y \mathrm{~d} y=(1+2 \sin y) \mathrm{d} x, x>0$ and $y(256)=\frac{\pi}{2}, y(49)=\alpha$, then $2 \sin \alpha$ is equal to :

**Options:**

- **(A)** $2(\sqrt{2}-1)$
- **(B)** $3(\sqrt{2}-1)$
- **(C)** $2 \sqrt{2}-1$
- **(D)** $\sqrt{2}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \sqrt{2}-1$**

**Detailed Solution:**

$\int \frac{\cos y}{1+2 \sin y} d y=\int \frac{d x}{16(\sqrt{9 \sqrt{x}+x})(4+\sqrt{9+\sqrt{x}})}$
$4+\sqrt{9+\sqrt{x}}=t$
$\frac{1}{2 \sqrt{9+\sqrt{x}}} \times \frac{d x}{2 \sqrt{x}}=1 d x$
$\frac{1}{2} \ell n|1+2 \sin y|=\int \frac{4 d t}{16 t}+C$
$\left.\frac{1}{2} \ell n|1+2 \sin y|=\frac{1}{4} \ell n \right\rvert\, 4+\sqrt{9+\sqrt{x}}+C$
$\frac{1}{2} \ell n(2 \sin y+1)=\frac{1}{4} \ell n|4+\sqrt{9+\sqrt{x}}|+C$

Substituting $\left(256, \frac{\pi}{2}\right)$
$\frac{1}{2} \ell n 3=\frac{1}{2} \ell n 3+C \quad C=0$

Substituting $(49, \alpha)$
$\frac{1}{2} \ell \mathrm{n}(2 \sin \alpha+1)=\frac{1}{4} \ell \mathrm{n} 8$
$\ell \mathrm{n}(2 \sin \alpha+1)=\frac{1}{2} \ell \mathrm{n} 8$
$\ell \mathrm{n}(2 \sin \alpha+1)=\ell \mathrm{n} 2 \sqrt{2}$
$2 \sin \alpha+1=2 \sqrt{2}$
$2 \sin \alpha=2 \sqrt{2}-1$

</details>

---

### Q7. JEE Main 2025 (2 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $f: \mathbf{R} \rightarrow \mathbf{R}$ be a thrice differentiable odd function satisfying $f^{\prime}(\mathrm{x}) \geq 0, f^{\prime}(\mathrm{x})=f(\mathrm{x}), f(0)=0, f^{\prime}(0)=3$. Then $9 f\left(\log _{\mathrm{c}} 3\right)$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

$\begin{aligned} & \mathrm{f}^{\prime \prime}(\mathrm{x})=\mathrm{f}(\mathrm{x}) \\ & \Rightarrow \mathrm{f}^{\prime}(\mathrm{x}) \cdot \mathrm{f}^{\prime \prime}(\mathrm{x})=\mathrm{f}^{\prime}(\mathrm{x}) \cdot \mathrm{f}(\mathrm{x}) \\ & \Rightarrow \frac{\left(\mathrm{f}^{\prime}(\mathrm{x})\right)^2}{2}=\frac{(\mathrm{f}(\mathrm{x}))^2}{2}+\mathrm{C} \\ & \Rightarrow\left(\mathrm{f}^{\prime}(\mathrm{x})\right)^2=(\mathrm{f}(\mathrm{x}))^2+\mathrm{C}^{\prime}\end{aligned}$
$\mathrm{f}(0)=0, \mathrm{f}^{\prime}(0)=3 \quad \Rightarrow \mathrm{C}^{\prime}=9$
$\therefore\left(\mathrm{f}^{\prime}(\mathrm{x})\right)^2=(\mathrm{f}(\mathrm{x}))^2+9$
$\mathrm{f}^{\prime}(\mathrm{x})=\sqrt{(\mathrm{f}(\mathrm{x}))^2+9} \quad \because \mathrm{f}^{\prime}(\mathrm{x}) \geq 0$
$\int \frac{\mathrm{dy}}{\sqrt{\mathrm{y}^2+9}}=\int \mathrm{dx} \Rightarrow \ln \left|\mathrm{y}+\sqrt{\mathrm{y}^2+9}\right|=\mathrm{x}+\mathrm{C}$
$\Rightarrow \mathrm{f}(0)=0 \Rightarrow \mathrm{C}=\ln 3$
$\Rightarrow \mathrm{y}+\sqrt{\mathrm{y}^2+9}=3 \mathrm{e}^{\mathrm{x}}$
at $x=\ln 3 ; y=4$
$\therefore 9 \mathrm{f}(\ln 3)=36$

</details>

---

### Q8. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\left(x^2+y^2\right) \mathrm{d} x-5 x y \mathrm{~d} y=0, y(1)=0$, is :

**Options:**

- **(A)** $\left|x^2-2 y^2\right|^6=x$
- **(B)** $\left|x^2-4 y^2\right|^6=x$
- **(C)** $\left|x^2-4 y^2\right|^5=x^2$
- **(D)** $\left|x^2-2 y^2\right|^5=x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left|x^2-4 y^2\right|^5=x^2$**

**Detailed Solution:**

$\begin{aligned}
& \left(x^2+y^2\right) d x=5 x y d y \\
& \Rightarrow \frac{d y}{d x}=\frac{x^2+y^2}{5 x y}
\end{aligned}$
Put $y=V x$
$\begin{aligned}
& \Rightarrow \mathrm{V}+\mathrm{x} \frac{\mathrm{dv}}{\mathrm{dx}}=\frac{1+\mathrm{V}^2}{5 \mathrm{~V}} \\
& \Rightarrow \frac{\mathrm{xdv}}{\mathrm{dx}}=\frac{1-4 \mathrm{~V}^2}{5 \mathrm{~V}} \\
& \Rightarrow \int \frac{\mathrm{V}}{1-4 \mathrm{~V}^2} \mathrm{dV}=\int \frac{\mathrm{dx}}{5 \mathrm{x}}
\end{aligned}$
Let $1-4 \mathrm{~V}^2=\mathrm{t}$
$\Rightarrow-8 \mathrm{~V} \mathrm{dV}=\mathrm{dt}$
$\begin{aligned} & \Rightarrow \int \frac{\mathrm{dt}}{(-8)(\mathrm{t})}=\int \frac{\mathrm{dx}}{5 \mathrm{x}} \\ & \Rightarrow \frac{-1}{8} \ln |\mathrm{t}|=\frac{1}{5} \ln |\mathrm{x}|+\ln \mathrm{C} \\ & \Rightarrow-5 \ln |\mathrm{t}|=8 \ln |\mathrm{x}|+\ln \mathrm{K} \\ & \Rightarrow \ln \mathrm{x}^8+\ln \left|\mathrm{t}^5\right|+\ln \mathrm{K}=0 \\ & \Rightarrow \mathrm{x}^8\left|\mathrm{t}^5\right|=\mathrm{C} \\ & \Rightarrow \mathrm{x}^8\left|1-4 \mathrm{~V}^2\right|^5=\mathrm{C} \\ & \Rightarrow \mathrm{x}^8\left|\frac{\mathrm{x}^2-4 \mathrm{y}^2}{\mathrm{x}^2}\right|^5=\mathrm{C} \\ & \Rightarrow\left|\mathrm{x}^2-4 \mathrm{y}^2\right|^5=\mathrm{Cx} \mathrm{x}^2 \\ & \text { given } \mathrm{y}(1)=0 \\ & \Rightarrow|1|^5=\mathrm{C} \Rightarrow \mathrm{C}=1 \\ & \Rightarrow\left|\mathrm{x}^2-4 \mathrm{y}^2\right|^5=\mathrm{x}^2\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $\left(1+y^2\right) e^{\tan x} d x+\cos ^2 x\left(1+e^{2 \tan x}\right) d y=0, y(0)=1$. Then $y\left(\frac{\pi}{4}\right)$ is equal to

**Options:**

- **(A)** $\frac{2}{e}$
- **(B)** $\frac{2}{e^2}$
- **(C)** $\frac{1}{e}$
- **(D)** $\frac{1}{e^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{e}$**

**Detailed Solution:**

$\begin{aligned} & \left(1+y^2\right) e^{\tan x} d x+\cos ^2 x\left(1+e^{2 \tan x}\right) d y=0 \\ & \int \frac{\sec ^2 x e^{\tan x}}{1+e^{2 \tan x}} d x+\int \frac{d y}{1+y^2}=C \\ & \Rightarrow \tan ^{-1}\left(e^{\tan x}\right)+\tan ^{-1} y=C \\ & \text { for } x=0, y=1, \tan ^{-1}(1)+\tan ^{-1} 1=C\end{aligned}$
$\mathrm{C}=\frac{\pi}{2}$
$\tan ^{-1}\left(e^{\tan x}\right)+\tan ^{-1} y=\frac{\pi}{2}$
Put $x=\pi, \tan ^{-1} e+\tan ^{-1} y=\frac{\pi}{2}$
$\tan ^{-1} y=\cot ^{-1} e$
$y=\frac{1}{e}$

</details>

---

### Q10. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the solution $y(x)$ of the given differential equation $\left(\mathrm{e}^y+1\right) \cos x \mathrm{~d} x+\mathrm{e}^y \sin x \mathrm{~d} y=0$ passes through the point $\left(\frac{\pi}{2}, 0\right)$, then the value of $\mathrm{e}^{y\left(\frac{\pi}{6}\right)}$ is equal to_________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$\begin{aligned}
& \left(\mathrm{e}^{\mathrm{y}}+1\right) \cos \mathrm{x} \mathrm{dx}+\mathrm{e}^{\mathrm{y}} \sin \mathrm{x} d \mathrm{y}=0 \\
& \Rightarrow \mathrm{d}\left(\left(\mathrm{e}^{\mathrm{y}}+1\right) \sin \mathrm{x}\right)=0 \\
& \left(\mathrm{e}^{\mathrm{y}}+1\right) \sin \mathrm{x}=\mathrm{C}
\end{aligned}$
It passes through $\left(\frac{\pi}{2}, 0\right)$
$\Rightarrow \mathrm{c}=2$
Now, $x=\frac{\pi}{6}$
$\Rightarrow \mathrm{e}^{\mathrm{y}}=3$

</details>

---

### Q11. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the solution $y=y(x)$ of the differential equation $\left(x^4+2 x^3+3 x^2+2 x+2\right) \mathrm{d} y-\left(2 x^2+2 x+3\right) \mathrm{d} x=0$ satisfies $y(-1)=-\frac{\pi}{4}$, then $y(0)$ is equal to :

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $-\frac{\pi}{2}$
- **(C)** 0
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \int d y=\int \frac{\left(2 x^2+2 x+3\right)}{x^4+2 x^3+3 x^2+2 x+2} d x \\ & y=\int \frac{\left(2 x^2+2 x+3\right)}{\left(x^2+1\right)\left(x^2+2 x+2\right)} d x \\ & y=\int \frac{d x}{x^2+2 x+2}+\int \frac{d x}{x^2+1} \\ & y=\tan ^{-1}(x+1)+\tan ^{-1} x+C \\ & y(-1)=\frac{-\pi}{4} \\ & \frac{-\pi}{4}=0-\frac{\pi}{4}+C \Rightarrow C=0 \\ & \Rightarrow y=\tan ^{-1}(x+1)+\tan ^{-1} x \\ & y(0)=\tan ^{-1} 1=\frac{\pi}{4}\end{aligned}$

</details>

---

### Q12. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>tan</mi><mi>x</mi><mo>+</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>{</mo><mn>1</mn><mo>-</mo><mi>sin</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>}</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>{</mo><mi>sin</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>1</mn><mo>}</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>tan</mi><mi>x</mi><mo>+</mo><mi>x</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>sec</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>tan</mi><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>d</mi><mi>y</mi><mo>=</mo><mfenced close="]" open="["><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>∫</mo><mfenced close="]" open="["><mrow><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>∫</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>∫</mo><mn>2</mn><mo>(</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mfenced close="]" open="["><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>(</mo><mi>sin</mi><mi>x</mi><mo>)</mo><mo>-</mo><mo>∫</mo><mo>(</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mi>λ</mi></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mfenced><mrow><mn>0</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mi>sin</mi><mn>0</mn><mo>+</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>+</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>×</mo><mn>2</mn></mrow></mfenced><mi>sin</mi><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q13. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>&gt;</mo><mn>0</mn></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mfrac><mrow><mi>α</mi><mo>-</mo><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow><mrow><mi>β</mi><mo>+</mo><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mi>x</mi></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mi>log</mi><mi>x</mi></mrow><mi>x</mi></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>log</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi mathvariant="normal">C</mi></math></p><p>This curve passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mfrac><mrow><mo>(</mo><mi>log</mi><mfenced><mn>1</mn></mfenced><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>C</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>x</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>log</mi><mi>x</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p>Now, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mi>e</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>log</mi><mi>e</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mi>tan</mi><mfenced><mrow><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mi>tan</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>-</mo><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow></mfrac></math></p><p>Hence, on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mi>β</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>+</mo><mn>2</mn><mi>β</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q14. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> is the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mi>dy</mi><mo>-</mo><mfenced><mrow><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi mathvariant="normal">y</mi></mrow></mfenced><mi>dx</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&gt;</mo><mn>2</mn><mo>,</mo><mi mathvariant="normal">y</mi><mo>(</mo><mn>4</mn><mo>)</mo><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> and the slope of the curve is never zero, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>(</mo><mn>10</mn><mo>)</mo></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mo>(</mo><mn>8</mn><msup><mo>)</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>1</mn><mo>-</mo><mo>(</mo><mn>8</mn><msup><mo>)</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mo>(</mo><mn>8</mn><msup><mo>)</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mi>dy</mi><mo>-</mo><mfenced><mrow><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi mathvariant="normal">y</mi></mrow></mfenced><mi>dx</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mi>dy</mi><mrow><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi mathvariant="normal">y</mi></mrow></mfrac><mo>=</mo><mo>∫</mo><mfrac><mi>dx</mi><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>∫</mo><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mo>(</mo><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">y</mi><mo>(</mo><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow></mfrac><mi>dy</mi><mo>=</mo><mo>∫</mo><mfrac><mi>dx</mi><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>∫</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mi mathvariant="normal">y</mi></mfrac></mrow></mfenced><mi>dy</mi><mo>=</mo><mo>∫</mo><mfrac><mi>dx</mi><mrow><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mi>log</mi><mo>|</mo><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn><mo>|</mo><mo>-</mo><mi>log</mi><mo>|</mo><mi mathvariant="normal">y</mi><mo>|</mo></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo> </mo><mi mathvariant="normal">y</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle><mo>-</mo><mn>3</mn></mrow><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mo>-</mo><mi>log</mi><msup><mfenced close="|" open="|"><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">C</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">x</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>log</mi><mfenced close="|" open="|"><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>log</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced close="|" open="|"><mfrac><mrow><mi mathvariant="normal">y</mi><mo>-</mo><mn>3</mn></mrow><mi mathvariant="normal">y</mi></mfrac></mfenced><mo>=</mo><mi>log</mi><mfenced><msup><mn>2</mn><mfrac><mn>3</mn><mn>4</mn></mfrac></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mi mathvariant="normal">y</mi><mo>+</mo><mn>3</mn><mo>=</mo><msup><mn>8</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>·</mo><mi mathvariant="normal">y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mo>=</mo><mfenced><mrow><msup><mn>8</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><msup><mfenced><mn>8</mn></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mrow></mfrac><mo>=</mo><mi>y</mi></math></p>

</details>

---

### Q15. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo></math> be solutions of the differential equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dx</mi><mi>dt</mi></mfrac><mo>+</mo><mi>ax</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dy</mi><mi>dt</mi></mfrac><mo>+</mo><mi>by</mi><mo>=</mo><mn>0</mn></math> respectively, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>,</mo><mi mathvariant="normal">b</mi><mo>∈</mo><mi mathvariant="normal">R</mi></math>. Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo> </mo><mo>;</mo><mo> </mo><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo> </mo><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo> </mo><mi>x</mi><mo>(</mo><mn>1</mn><mo>)</mo></math>, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, for which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>(</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>y</mi><mo>(</mo><mi>t</mi><mo>)</mo></math>, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msub><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>4</mn></msub><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>3</mn></msub><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msub><mn>2</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dx</mi><mi>dt</mi></mfrac><mo>+</mo><mi>ax</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>dx</mi><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mo>-</mo><mi>adt</mi></math></p><p>Integrating both sides,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∫</mo><mfrac><mi>dx</mi><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mo>-</mo><mi mathvariant="normal">a</mi><mo>∫</mo><mi>dt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mo>|</mo><mi mathvariant="normal">x</mi><mo>|</mo><mo>=</mo><mo>-</mo><mi>at</mi><mo>+</mo><mi mathvariant="normal">c</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mn>2</mn><mo>=</mo><mn>0</mn><mo>+</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>logx</mi><mo>=</mo><mo>-</mo><mi>at</mi><mo>+</mo><mi>log</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>logx</mi><mo>-</mo><mi>log</mi><mn>2</mn><mo>=</mo><mo>-</mo><mi>at</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mfrac><mi>x</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mi>at</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi mathvariant="normal">x</mi><mn>2</mn></mfrac><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>at</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">x</mi><mo>=</mo><mn>2</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>at</mi></mrow></msup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo></math></p><p>It is also given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dy</mi><mi>dt</mi></mfrac><mo>+</mo><mi>by</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>dy</mi><mi mathvariant="normal">y</mi></mfrac><mo>=</mo><mo>-</mo><mi>bdt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mo>|</mo><mi mathvariant="normal">y</mi><mo>|</mo><mo>=</mo><mo>-</mo><mi>bt</mi><mo>+</mo><mi mathvariant="normal">λ</mi></math></p><p>At, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mo>=</mo><mn>0</mn><mo>+</mo><mi>λ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>bt</mi></mrow></msup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>ii</mi><mo>)</mo></math></p><p>According to question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo> </mo><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>2</mn><mo> </mo><mi>x</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">b</mi></mrow></msup><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">a</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">e</mi><mrow><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">b</mi></mrow></msup><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>For</mtext><mo> </mo><mi>x</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><mi>y</mi><mfenced><mi>t</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>at</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>bt</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>(</mo><mi mathvariant="normal">a</mi><mo>-</mo><mi mathvariant="normal">b</mi><mo>)</mo><mi mathvariant="normal">t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><msup><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced><mi mathvariant="normal">t</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>log</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mo>×</mo><mi>log</mi><mfenced><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>log</mi><mfrac><mn>4</mn><mn>3</mn></mfrac></msub><mn>2</mn><mo>=</mo><mi mathvariant="normal">t</mi></math></p>

</details>

---

### Q16. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> be the solution curves the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mo>+</mo><mn>7</mn></math> with initial conditions <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> respectively. Then the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> intersect at</p>

**Options:**

- **(A)** no point
- **(B)** two points
- **(C)** one point
- **(D)** infinite number of points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) no point**

**Detailed Solution:**

<blockquote><p>We have been given that<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mo>+</mo><mn>7</mn><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi><mo>+</mo><mn>7</mn></mrow></mfrac><mo>=</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mo>|</mo><mi>y</mi><mo>+</mo><mn>7</mn><mo>|</mo><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>y</mi><mo>+</mo><mn>7</mn><mo>|</mo><mo>=</mo><mi>k</mi><mo>.</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>k</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>7</mn><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mi>k</mi><mo>-</mo><mn>7</mn><mo>&#8658;</mo><mn>8</mn><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced><mo>&#8658;</mo><mn>8</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>7</mn><mo>=</mo><mn>7</mn><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>7</mn></math></p><p>Hence, No point of intersection.</p><p>This is the required option.</p></blockquote>

</details>

---

### Q17. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mi mathvariant="normal">k</mi><mo>&#62;</mo><mn>0</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>k</mi><mn>2</mn></msup></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>X</mi><mo>,</mo><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>Y</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>X</mi><mo>+</mo><mi>Y</mi></mrow><mrow><mi>X</mi><mo>-</mo><mi>Y</mi></mrow></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>V</mi><mi>X</mi><mo>&#160;</mo><mfrac><mrow><mi>d</mi><mi>Y</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac><mo>=</mo><mi>V</mi><mo>+</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac></math></p><p>Putting the value in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>+</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>V</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>V</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>X</mi><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>X</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>V</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>V</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>V</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>V</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>V</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>X</mi></mrow><mi>X</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>V</mi><mn>2</mn></msup></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>V</mi><mi>d</mi><mi>V</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>V</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>X</mi></mrow><mi>X</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>V</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>V</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>X</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mi>Y</mi><mi>X</mi></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mi>Y</mi><mn>2</mn></msup><msup><mi>X</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mi>ln</mi><mfenced><mi>X</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><msup><mfenced><mrow><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now given curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mn>1</mn><mo>=</mo><mi>ln</mi><mn>1</mn><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Now given curve also passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>In</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">k</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mi>ln</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><mo>In</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow><msup><mi>k</mi><mn>2</mn></msup></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>ln</mi><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mn>1</mn><mi>k</mi></mfrac></mfenced><mo>=</mo><mo>In</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced></math></p></blockquote>

</details>

---

### Q18. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>y</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mi>C</mi><mfenced open="|" close="|"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mi>C</mi><mfenced open="|" close="|"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced><mo>=</mo><mi>C</mi><msup><mfenced><mrow><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>4</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced><mo>=</mo><mi>C</mi><msup><mfenced><mrow><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>4</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mi>C</mi><mfenced open="|" close="|"><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>y</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>After rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi></mrow><mrow><mi>y</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math> </p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>v</mi><mo>&#8658;</mo><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mi>y</mi></mrow></mfrac><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>v</mi><mo>-</mo><mi>x</mi></mrow><mrow><mi>y</mi><mfenced><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mi>v</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><mi>v</mi><mo>-</mo><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mi>v</mi></mrow></mfrac></mfenced></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>k</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>k</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mfrac><mrow><mi>k</mi><mi>x</mi><mo>-</mo><mi>x</mi></mrow><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mi>k</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>k</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mrow><mi>k</mi><mo>+</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><mn>5</mn><mo>+</mo><mi>k</mi></mrow></mfenced><mrow><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>k</mi><mo>=</mo><mo>&#8747;</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mn>4</mn><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>3</mn><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>k</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>ln</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><mi>ln</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><msup><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mi>c</mi><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>v</mi><mi>x</mi></mfrac></mstyle><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><msup><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>v</mi><mi>x</mi></mfrac></mstyle><mo>+</mo><mn>2</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mi>c</mi><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><msup><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow></mfenced><mn>4</mn></msup></math></p></blockquote>

</details>

---

### Q19. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The slope of the tangent to a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>:</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo></math> on it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></msup><mo>-</mo><mn>6</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msup><mo>+</mo><mn>9</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>9</mn><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn><mi mathvariant="normal">x</mi></mrow></msup></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> passes through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></msup></mrow></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>&#945;</mi></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>6</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>9</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>9</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p>On rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mrow><mn>6</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>9</mn></mrow></mfrac></math></p><p>Integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>-</mo><msqrt><mn>2</mn></msqrt><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>3</mn></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p>If the curve passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math></p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, curve will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>-</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>3</mn></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Again curve passes through the point</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></msup></mrow></mfenced></math> </p><p>Putting the value in curve equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></msup><mn>2</mn></mfrac><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>2</mn><mi>&#945;</mi></mrow></msup><mn>2</mn></mfrac><mo>-</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>&#945;</mi></msup></mrow><mn>3</mn></mfrac></mfenced><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>&#945;</mi></msup></mrow><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>&#945;</mi></msup></mrow><mn>3</mn></mfrac><mo>=</mo><mi>tan</mi><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>&#945;</mi></msup></mrow><mn>3</mn></mfrac><mo>=</mo><mfenced><mfrac><mrow><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><msup><mi>tantan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#215;</mo><msup><mi>tantan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><msup><mi>e</mi><mi>&#945;</mi></msup></mrow><mn>3</mn></mfrac><mo>=</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><msqrt><mn>2</mn></msqrt><mn>3</mn></mfrac></mrow></mfrac></mfenced></math>  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">e</mi><mi>&#945;</mi></msup><mo>=</mo><mfrac><mn>3</mn><msqrt><mn>2</mn></msqrt></mfrac><mfenced><mfrac><mrow><mn>3</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow><mrow><mn>3</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math></p></blockquote>

</details>

---

### Q20. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><mi>y</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>+</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mrow><msub><mi>log</mi><mi mathvariant="italic">c</mi></msub><msqrt><mn>3</mn></msqrt></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> .........(i)</p><p>Now integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>+</mo><mn>2</mn><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#8658;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> ....(ii)</p><p>Now from equation (i), we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>From equation (ii) we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> (In <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mo>)</mo><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced close="" open="["><mrow><mi>y</mi><mo>&#39;</mo><mfenced><mn>0</mn></mfenced><mo>+</mo><mo>(</mo><mi>y</mi></mrow></mfenced></math> In <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mrow><msqrt><mn>3</mn></msqrt><msup><mo>)</mo><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>6</mn><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn></math>.</p>

</details>

---

### Q21. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msub><mi>log</mi><mrow><mo>-</mo><mn>2</mn></mrow></msub><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>2</mn><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now rearranging and integrating both side of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mi>y</mi></msup><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><msup><mn>2</mn><mi>y</mi></msup><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>y</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><msup><mn>2</mn><mi>x</mi></msup><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac><mo>&#8747;</mo><mfrac><mrow><msup><mn>2</mn><mi>y</mi></msup><mi>ln</mi><mn>2</mn></mrow><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msup><mi>ln</mi><mn>2</mn></msup></mfrac><mo>&#8747;</mo><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><mi>ln</mi><mn>2</mn></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>ln</mi><mn>2</mn></mrow></mfrac><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p>Putting this values in above equation we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mn>4</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn><mo>=</mo><mn>2</mn><mo>-</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></math></p>

</details>

---

### Q22. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>2</mn><mi>&#960;</mi></mrow></mfenced><mo>-</mo><mfenced close="}" open="{"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac><mo>,</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></mrow></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>S</mi></math>, be the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. If the sum of abscissas of all the points of intersection of the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> with the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **42**

**Detailed Solution:**

<p>Given differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>C</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>1</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac></math></p><p>Solving this equation with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>tan</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;&#160;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>=</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p>or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>=</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mi>&#960;</mi><mo>-</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo><mn>2</mn><mi>&#960;</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>,</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>13</mn><mi>&#960;</mi></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>23</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math></p><p>Hence sum of abscissas of all the points of intersection</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#960;</mi><mo>+</mo><mfrac><mrow><mn>7</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>+</mo><mfrac><mrow><mn>23</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>12</mn><mi>&#960;</mi><mo>+</mo><mn>7</mn><mi>&#960;</mi><mo>+</mo><mn>23</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mn>42</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>k</mi><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><mn>42</mn><mi>&#960;</mi></mrow><mn>12</mn></mfrac><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>42</mn></math></p>

</details>

---

### Q23. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup><mo>&#183;</mo><msup><mn>2</mn><mi>x</mi></msup></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>,</mo></math> the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> lies in the interval :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]"><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>&#183;</mo><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup><mo>&#183;</mo><msup><mn>2</mn><mi>x</mi></msup></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>+</mo><msup><mn>2</mn><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mi>x</mi></msup><mfenced><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mi>x</mi></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfrac><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfenced></mrow><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>C</mi><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced></mrow><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mfenced><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mi>y</mi><mo>+</mo><msup><mn>2</mn><mi>y</mi></msup></mrow></mfenced><mo>=</mo><mi>x</mi></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>ln</mi><mn>3</mn><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q24. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>y</mi></mrow><mrow><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><mo>-</mo><msup><mn>2</mn><mi>x</mi></msup></mrow><msup><mn>2</mn><mi>y</mi></msup></mfrac><mo>,</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>2</mn><mi mathvariant="normal">e</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>2</mn><mo>+</mo><mi mathvariant="normal">e</mi><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>1</mn><mo>+</mo><mi>e</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>1</mn><mo>+</mo><mi>e</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><mo>-</mo><msup><mn>2</mn><mi>x</mi></msup></mrow><msup><mn>2</mn><mi>y</mi></msup></mfrac><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mfenced><mfrac><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>y</mi></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><msup><mn>2</mn><mi>y</mi></msup><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mn>2</mn><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p>By using Variable Separable method</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><msup><mn>2</mn><mi>y</mi></msup><mi>d</mi><mi>y</mi></mrow><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><msup><mn>2</mn><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mi>ln</mi><mfenced><mn>2</mn></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mi>t</mi></mfrac><mfrac><mn>1</mn><mrow><mi>&#8467;</mi><mi>n</mi><mn>2</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><msup><mn>2</mn><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#8747;</mo><msup><mi>a</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><msup><mi>a</mi><mi>x</mi></msup><mrow><mi>ln</mi><mfenced><mi>a</mi></mfenced></mrow></mfrac><mo>+</mo><mi>c</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>ln</mi><mfenced><mi>t</mi></mfenced></mrow><mrow><mi>ln</mi><mfenced><mn>2</mn></mfenced></mrow></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mi>x</mi></msup><mrow><mi>ln</mi><mfenced><mn>2</mn></mfenced></mrow></mfrac><mo>+</mo><mfrac><mi>c</mi><mrow><mi>ln</mi><mfenced><mn>2</mn></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mi>t</mi></mfenced><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi mathvariant="normal">x</mi></msup><mo>+</mo><mi>c</mi></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>ln</mi><mfenced><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msup><mn>2</mn><mn>0</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced><mrow><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>e</mi><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><msup><mn>2</mn><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><msup><mn>2</mn><mi>y</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>1</mn></msup><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mo>(</mo><mn>1</mn><mo>+</mo><mi>e</mi><mo>)</mo></math></p>

</details>

---

### Q25. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>y</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>x</mi><mo>+</mo><mi>y</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>;</mo><mi>&#945;</mi><mo>&#8712;</mo><mi>N</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to ___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>x</mi></mrow></msup><mi>&#945;</mi></mfrac><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> </p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mi>&#8467;</mi><mi>n</mi><mn>2</mn><mo>,</mo><mi>&#8467;</mi><mi>n</mi><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><msup><mn>2</mn><mi>&#945;</mi></msup><mi>&#945;</mi></mfrac><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced><mo>&#8801;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mi>&#8467;</mi><mi>n</mi><mn>2</mn></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mi>&#945;</mi></mfrac><mo>+</mo><mi>c</mi></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>2</mn><mi>&#945;</mi></msup><mo>-</mo><mn>1</mn></mrow><mi>&#945;</mi></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>(</mo></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>N</mi><mo>)</mo></math>.</p>

</details>

---

### Q26. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mfenced open="["><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sec</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>-</mo><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sec</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>y</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>y</mi><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mn>0</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p>So, the particular solution is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mi>tan</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>y</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mn>5</mn></math></p><p>Here, differentiate both sides of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>,</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>sec</mi><mn>2</mn></msup><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q27. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi><mo>,</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>=</mo><mi>&#945;</mi><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>y</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>y</mi></mrow></msup><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>y</mi></mrow></msup><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mn>3</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>7</mn><mn>12</mn></mfrac></math></p><p>So, the particular solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>y</mi></mrow></msup><mrow><mo>-</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>7</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>y</mi></mrow></msup><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>7</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>y</mi></mrow></msup><mo>=</mo><mfrac><mn>3</mn><mrow><mn>7</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>&#8658;</mo><mn>4</mn><mi>y</mi><mo>=</mo><mi>ln</mi><mfenced><mfrac><mn>3</mn><mrow><mn>7</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mrow><mn>3</mn><mi>x</mi></mrow></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>y</mi><mo>=</mo><mi>&#8467;</mi><mi>n</mi><mfenced><mfrac><mn>3</mn><mn>6</mn></mfrac></mfenced></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#8467;</mi><mi>n</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>&#8467;</mi><mi>n</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mi>&#8467;</mi><mi>n</mi><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q28. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be given by the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><msqrt><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mi>d</mi><mi>y</mi></math>. If it intersects <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>-axis at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>, and the intersection point of the curve with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math>axis is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mn>0</mn></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>&#945;</mi></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><msqrt><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msup></mfenced><mo>=</mo><mi>&#952;</mi><mo>,</mo><mo>&#160;</mo><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="["><mrow><mn>0</mn><mo>,</mo><mi>&#960;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>&#952;</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>&#952;</mi><mn>2</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><msqrt><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></msqrt></math></p><p>Hence, by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mfenced><mfrac><mi>&#952;</mi><mn>2</mn></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><msqrt><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></msqrt><mi>d</mi><mi>x</mi><mo>=</mo><msqrt><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>-</mo><mn>1</mn></msqrt><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><msqrt><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></msqrt></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><msqrt><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mfenced><msqrt><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></msqrt></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msqrt><msup><mi>e</mi><mi>x</mi></msup></msqrt><msqrt><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math></p><p>Put  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>d</mi><mi>t</mi><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>e</mi><mi>x</mi></msup><msqrt><msup><mi>e</mi><mi>x</mi></msup></msqrt><msqrt><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>t</mi><msqrt><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi></msqrt></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mi>z</mi></mfrac><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>z</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><msup><mi>z</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><msup><mi>z</mi><mn>2</mn></msup></mfrac></mrow><mrow><mfrac><mn>1</mn><mi>z</mi></mfrac><msqrt><mfrac><mn>1</mn><msup><mi>z</mi><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></msqrt></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>z</mi></mrow><msqrt><mn>1</mn><mo>-</mo><mi>z</mi></msqrt></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>z</mi><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><msqrt><mn>2</mn></msqrt><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p>Now, it meets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo><mtext>axis</mtext></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><msqrt><mn>2</mn></msqrt><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>It passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><msup><mi>e</mi><mi>&#945;</mi></msup><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q29. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mn>3</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mn>6</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>e</mi><mn>3</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>4</mn><msup><mi>e</mi><mn>6</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mn>6</mn></msup></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>+</mo><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>&#160;</mo><mi>dx</mi><mo>=</mo><mfenced><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><mi>x</mi></mfrac></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>y</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn><mo>=</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn><msup><mi>e</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><msup><mi>e</mi><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mn>3</mn></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>e</mi><mn>6</mn></msup></math></p>

</details>

---

### Q30. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>tan</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mi>y</mi><mo>&#160;</mo><mi>tan</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>1</mn><mo>,</mo><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>.</mo></math> Then the area of the region bounded by the curves <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> in the upper half plane is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <p style="text-align: justify;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>3</mn></mrow></mfenced></math></p>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac><mfenced><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

We have,<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><mfenced><mrow><mstyle displaystyle="true"><mfrac><mi>y</mi><mi>x</mi></mfrac></mstyle><mo>&#183;</mo><mi>tan</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>y</mi><mi>x</mi></mfrac></mstyle></mfenced><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mi>tan</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>y</mi><mi>x</mi></mfrac></mstyle></mfenced></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>-</mo><mi>cot</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfenced><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced></math></p><p>Now, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>+</mo><mi>x</mi><mfenced><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mi>v</mi><mo>-</mo><mi>cot</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mi>tan</mi><mi>v</mi><mi>d</mi><mi>v</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>v</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mi>c</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mi>ln</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mn>2</mn><mo>+</mo><mi>ln</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mn>2</mn><mo>-</mo><mi>ln</mi><mn>2</mn><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>sec</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mfenced><mfrac><mi>y</mi><mi>x</mi></mfrac></mfenced><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>x</mi><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>x</mi></mfenced></math></p><p>So, required bounded area</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup><mfenced><munder><munder><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow><mo>&#9183;</mo></munder><mi mathvariant="normal">I</mi></munder></mfenced></mrow><munder><mi>x</mi><mi>II</mi></munder><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><msup><mi>cos</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>&#183;</mo><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup><mfenced><mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>-</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msubsup><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></mrow></mfenced><mn>0</mn><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac></mfenced></math> sq. units</p>

</details>

---

### Q31. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Which of the following is true for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> that satisfies the differential equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mi>y</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mo>(</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Integrate both the sides we get, </p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><msup><mi>e</mi><mfenced><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced></msup><mo>-</mo><mn>1</mn></math></p>

</details>

---

### Q32. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math> (where C is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></msqrt><mo>+</mo><mi>x</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p>Integrating,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mrow><mn>2</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mi>x</mi><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mi>x</mi><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math> to solve RHS 2nd integration, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>-</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mo>&#8747;</mo><mfrac><mi>t</mi><mrow><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>t</mi></mrow></mfrac><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt><mo>+</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced close="]" open="["><mfrac><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mn>1</mn></mrow><mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p>

</details>

---

### Q33. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mrow><mn>2</mn><mo>+</mo><mi>y</mi></mrow></mfrac><mo>&#8901;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mn>0</mn></math> satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><msub><mi>log</mi><mi>e</mi></msub><mn>13</mn><mo>)</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>2</mn><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mn>2</mn><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mi>C</mi><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>C</mi><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>18</mn><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><msub><mi>log</mi><mi>e</mi></msub><mn>13</mn><mo>)</mo><mo>=</mo><mfrac><mn>18</mn><mrow><mn>5</mn><mo>+</mo><msup><mi>e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mn>13</mn></mfenced></mrow></msup></mrow></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>(</mo><msub><mi>log</mi><mi>e</mi></msub><mn>13</mn><mo>)</mo><mo>=</mo><mfrac><mn>18</mn><mrow><mn>5</mn><mo>+</mo><mn>13</mn></mrow></mfrac><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>y</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mn>13</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p> </p>

</details>

---

### Q34. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math> is
(where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is a constant of integration)

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>C</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mi>C</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>C</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mi>C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>C</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>3</mn><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi></mrow><mrow><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow><mrow><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></math>
Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><mo>=</mo><mi>d</mi><mi>t</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>tdt</mi><mo>=</mo><mo>&#8747;</mo><mi>dx</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>(</mo><mi>ln</mi><mo>(</mo><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>

</details>

---

### Q35. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mi>x</mi><mi>y</mi><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>y</mi><mi>d</mi><mi>x</mi><mo>;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>e</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>4</mn></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mi>e</mi></msqrt><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><msqrt><mi>e</mi></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><msqrt><mi>e</mi></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><msqrt><mi>e</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><msqrt><mi>e</mi></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mi>x</mi><mi>y</mi><mo>&#183;</mo><mi>d</mi><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>y</mi><mi>d</mi><mi>x</mi></math></p></blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>y</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p>Integrating both sides with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>k</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>A</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><mi>B</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>C</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mi>A</mi><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>B</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>2</mn><mo>=</mo><mo>-</mo><mi>B</mi><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>=</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>1</mn></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>2</mn><mo>=</mo><mi>A</mi><mfenced><mn>2</mn></mfenced><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>B</mi><mfenced><mn>1</mn></mfenced><mo>+</mo><mi>C</mi><mfenced><msup><mn>2</mn><mn>2</mn></msup></mfenced><mo>&#8658;</mo><mn>2</mn><mi>A</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>k</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mi>e</mi></math> i.e. at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>e</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mn>2</mn></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mo>-</mo><mi>ln</mi><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>+</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mi>ln</mi><mn>2</mn></math></p><p>Putting in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mn>4</mn><mo>+</mo><mfrac><mn>2</mn><mn>4</mn></mfrac><mo>+</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mn>4</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>ln</mi><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>ln</mi><mn>3</mn><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>ln</mi><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>ln</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>ln</mi><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mn>3</mn></mfrac><mo>=</mo><msup><mi>e</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msqrt><mi>e</mi></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><msqrt><mi>e</mi></msqrt></math></p>

</details>

---

### Q36. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution curve of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math> which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mi>y</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mi>y</mi><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>2</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow><mn>2</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>2</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p>Separate variables</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p>Integrate both side</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>ln</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Since curve pass through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>=</mo><mi>ln</mi><mfenced><mrow><msup><mi>e</mi><mn>0</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>ln</mi><mfenced><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>ln</mi><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mi>y</mi></mfrac><mo>=</mo><mi>ln</mi><mfenced><mfrac><mrow><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup></mrow><mn>2</mn></mfrac></mfenced></math></p>

</details>

---

### Q37. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>.</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>&#8722;</mo><mi>cos</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>=</mo><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi mathvariant="normal">&#960;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mtext>&#8201;</mtext><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mtext>&#8201;</mtext><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>ln</mi><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>ln</mi><mi>c</mi></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>c</mi></math></p><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>So<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>c</mi><mo>=</mo><mn>4</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mn>1</mn><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>&#960;</mi></mfenced><mo>=</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#183;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;</mtext><mi>x</mi><mo>=</mo><mi>&#960;</mi><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q38. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><msup><mrow><mi>f</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>,</mo><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mrow></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> , then <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mi>π</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi><mo>-</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi><mo>+</mo><mn>2</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mi>π</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>sin</mi><mo>&#8289;</mo><mi>x</mi></mrow><mrow><mi>cos</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>f</mi><mo>'</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8289;</mo><mfenced separators="|"><mfrac><mrow><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn><mi>sin</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mi>cos</mi><mo>&#8289;</mo><mfenced separators="|"><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><msup><mi>f</mi><mi>'</mi></msup><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>So, <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math></p>

</details>

---

### Q39. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> be a solution of the differential equation, <math><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msqrt><mn>1</mn><mo>-</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></msqrt><mo>=</mo><mn>0</mn><mo>,</mo><mi></mi><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>&#60;</mo><mn>1</mn><mo>.</mo></math> If <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></msqrt></mfrac><mo>+</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>+</mo><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mi>c</mi></math>
At,<math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mo>&#8201;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8658;</mo><mo>&#8201;</mo><mi>c</mi><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8658;</mo><mo>&#8201;</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math>
Hence, <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><msup><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p></blockquote>

</details>

---

### Q40. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The solution of the differential equation, $\frac{\mathrm{d} y}{\mathrm{~d} x}=(x-y)^{2}$, when $y(1)=1,$ is:

**Options:**

- **(A)** $\quad \log _{e}\left|\frac{2-x}{2-y}\right|=x-y$
- **(B)** $-\log _{e}\left|\frac{1-x+y}{1+x-y}\right|=2(x-1)$
- **(C)** $-\log _{e}\left|\frac{1+x-y}{1-x+y}\right|=x+y-2$
- **(D)** $\log _{\mathrm{e}}\left|\frac{2-y}{2-x}\right|=2(y-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\log _{e}\left|\frac{1-x+y}{1+x-y}\right|=2(x-1)$**

**Detailed Solution:**

The given differential equation

$\frac{d y}{d x}=(x-y)^{2}$

Let $x-y=t \Rightarrow 1-\frac{d y}{d x}=\frac{d t}{d x}$

$\Rightarrow \frac{d y}{d x}=1-\frac{d t}{d x}$

Now, from equation (1)

$\left(1-\frac{d t}{d x}\right)=(t)^{2}$

$\Rightarrow \quad 1-t^{2}=\frac{d t}{d x} \Rightarrow \int d x=\int \frac{d t}{1-t^{2}}$

$\Rightarrow-x=\frac{1}{2 \times 1} \ln \left|\frac{t-1}{t+1}\right|+c$

$\Rightarrow-x=\frac{1}{2} \ln \left|\frac{x-y-1}{x-y+1}\right|+c$

$\because$ The given condition $y(1)=1$

$-1=\frac{1}{2} \ln \left|\frac{1-1-1}{1-1+1}\right|+c \Rightarrow c=-1$

Hence, $2(x-1)=-\ln \left|\frac{1-x+y}{1-y+x}\right|$

</details>

---

### Q41. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> be the solution of the differential equation <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="" open="{" separators="|"><mtable><mtr><mtd><mn>1</mn><mo>,</mo></mtd><mtd><mi>x</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>1</mn></mrow></mfenced></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>&#160;</mi><mfenced separators="|"><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></math> is

**Options:**

- **(A)** <math><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mi>e</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn><mi>e</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn><mi>e</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn><mi>e</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> is a linear differential equation.</p><p>Integrating Factor <math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mrow><mo stretchy="false">&#8747;</mo><mrow><mn>2</mn><mi>d</mi><mi>x</mi></mrow></mrow></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p>Solution of the above equation is</p><p><math><mi>y</mi><mo>.</mo><mi>&#160;</mi><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></mrow></mrow><mo>+</mo><mi>C</mi></math></p><p><math><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mrow><msubsup><mo stretchy="false">&#8747;</mo><mrow><mn>0</mn></mrow><mrow><mi>x</mi></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo></mrow></mrow><mi>C</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced><mo>.</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mfenced separators="|"><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><msubsup><mo>&#8747;</mo><mn>0</mn><mn>1</mn></msubsup><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msubsup><mn>0</mn><mo>.</mo><mi>d</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mn>2</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>e</mi><mn>3</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q42. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $\frac{d y}{d x}+2 y=f(x)$, where
$$
f(x)=\left\{\begin{array}{lc}
1, & x \in[0,1] \\
0, & \text { otherwise }
\end{array}\right.
$$
If $y(0)=0$, then $y\left(\frac{3}{2}\right)$ is

**Options:**

- **(A)** $\frac{e^2-1}{2 e^3}$
- **(B)** $\frac{e^2-1}{e^3}$
- **(C)** $\frac{1}{2 e}$
- **(D)** $\frac{e^2+1}{2 e^4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{e^2-1}{2 e^3}$**

**Detailed Solution:**

When $x \in[0,1]$, then $\frac{d y}{d x}+2 y=1$
$$
\begin{aligned}
&\Rightarrow \mathrm{y}=\frac{1}{2}+C_1 e^{-2 x} \\
&\because y(0)=0 \Rightarrow y(x)=\frac{1}{2}-\frac{1}{2} e^{-2 x} \\
&\text { Here, } y(1)=\frac{1}{2}-\frac{1}{2} e^{-2}=\frac{e^2-1}{2 e^2}
\end{aligned}
$$
When $x \notin[0,1]$, than $\frac{d y}{d x}+2 y=0$
$$
\begin{gathered}
\Rightarrow y=c_2 e^{-2 x} \\
\therefore y(1)=\frac{e^2-1}{2 e^2} \Rightarrow \frac{e^2-1}{2}=c^2 e^{-2} \Rightarrow C_2=\frac{e^2-1}{2} \\
\therefore y(x)\left(\frac{e^2-1}{2}\right) e^{-2 x} \Rightarrow y\left(\frac{3}{2}\right)=\frac{e^2-1}{2 e^3}
\end{gathered}
$$

</details>

---

### Q43. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>cos</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mi>x</mi><mo>=</mo><mi>t</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is the constant of integration.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>C</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mi>log</mi><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>log</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>log</mi><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math> in the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>log</mi><mfenced separators="|"><mn>3</mn></mfenced><mo>-</mo><mi>log</mi><mfenced separators="|"><mn>4</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><mi>log</mi><mfenced separators="|"><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>log</mi><mfenced separators="|"><mfrac><mn>4</mn><mn>3</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>.</p></blockquote>

</details>

---

### Q44. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>y</mi><mi>&#160;</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution of the differential equation <math><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>9</mn><mo>,</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mi>&#160;</mi><mo>&#8800;</mo><mi>&#160;</mi><mo>-</mo><mn>2</mn><mi>&#160;</mi></math> and <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math><mi>y</mi><mo>(</mo><mo>-</mo><mn>4</mn><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>4</mn><mo>-</mo><mn>13</mn></math>

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mi>&#160;</mi><mfrac><mrow><mn>13</mn></mrow><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>y</mi><mo>=</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mfrac><mn>13</mn><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math>

<math><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>13</mn><mrow><mrow><msub><mrow><mi mathvariant="normal">log</mi></mrow><mrow><mi>e</mi></mrow></msub></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></mrow></mrow></math>

If <math><mi>x</mi><mo>=</mo><mn>0</mn></math> then <math><mi>y</mi><mo>=</mo><mn>0</mn></math>

<math><mn>0</mn><mo>=</mo><mi>&#160;</mi><mn>0</mn><mo>+</mo><mn>0</mn><mo>-</mo><mn>13</mn><mi>&#160;</mi><mi>l</mi><mi>o</mi><mi>g</mi><mfenced close="|" open="|" separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>&#160;</mi><mo>=</mo><mn>13</mn><mi>log</mi><mo>&#8289;</mo><mrow><mo>(</mo><mn>2</mn><mo>)</mo></mrow></math>

If <math><mi>x</mi><mo>=</mo><mi>&#160;</mi><mo>-</mo><mn>4</mn><mo>,</mo></math> then <math><mi>y</mi></math>

<math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>16</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>8</mn><mo>-</mo><mn>13</mn><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>13</mn><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>&#8289;</mo><mrow><mo>|</mo><mn>2</mn><mo>|</mo></mrow></mrow></mrow></mrow></math>

<math><mi>y</mi><mo>=</mo><mn>0</mn></math>

Hence, answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.

</details>

---

### Q45. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `1`

If $\frac{d y}{d x}=y+3>0$ and $y(0)=2$, then $y(\ln 2)$ is equal to

**Options:**

- **(A)** 5
- **(B)** 13
- **(C)** -2
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 7**

**Detailed Solution:**

$\frac{d y}{d x}=y+3 \Rightarrow \frac{d y}{y+3}=d x$
$\ln (y+3)=x+c$
$x=0 \Rightarrow y=2$
$\Rightarrow \ln 5=0+c$
$c=\ln 5$
$\ln (y+3)=x+\ln 5$
$y+3=e^{x+\ln 5} \Rightarrow y+3=e^{\ln 2+\ln 5}$
$y+3=10 \Rightarrow y=7$

</details>

---

### Q46. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

The solution of the equation $\frac{d^2 y}{d x^2}=e^{-2 x}$

**Options:**

- **(A)** $\frac{e^{-2 x}}{4}$
- **(B)** $\frac{e^{-2 x}}{4}+c x+d$
- **(C)** $\frac{1}{4} e^{-2 x}+c x^2+d$
- **(D)** $\frac{1}{4} e^{-4 x}+c x+d$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{e^{-2 x}}{4}+c x+d$**

**Detailed Solution:**

$\frac{d^2 y}{d x^2}=e^{-2 x} ; \frac{d y}{d x}=\frac{e^{-2 x}}{-2}+c ; y=\frac{e^{-2 x}}{4}+c x+d$

</details>

---

