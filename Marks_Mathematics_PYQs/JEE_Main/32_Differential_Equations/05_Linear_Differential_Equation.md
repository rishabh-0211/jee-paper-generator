# JEE Main Mathematics - Differential Equations

## Topic 5: Linear Differential Equation

**Total Questions:** 130

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $x\sqrt{1-x^2}\,dy + \left(y\sqrt{1-x^2} - x\cos^{-1}x\right)dx = 0$, $x \in (0, 1)$, $\displaystyle\lim_{x\to 1^-} y(x) = 1$. Then $y\left(\dfrac{1}{2}\right)$ equals:

**Options:**

- **(A)** $3 - \dfrac{\pi}{\sqrt{3}}$
- **(B)** $4 - \sqrt{3}\pi$
- **(C)** $4 - \dfrac{2\pi}{\sqrt{3}}$
- **(D)** $3 - \dfrac{\pi}{2\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 - \dfrac{\pi}{\sqrt{3}}$**

**Detailed Solution:**

The given differential equation is:

$x\sqrt{1-x^2}\,dy + \left(y\sqrt{1-x^2} - x\cos^{-1}x\right)dx = 0$

Rearranging the terms, we get:

$x\sqrt{1-x^2}\,dy + y\sqrt{1-x^2}\,dx = x\cos^{-1}x\,dx$

Dividing the entire equation by $\sqrt{1-x^2}$:

$x\,dy + y\,dx = \dfrac{x\cos^{-1}x}{\sqrt{1-x^2}}\,dx$

The left side is the exact differential of $xy$:

$d(xy) = \dfrac{x\cos^{-1}x}{\sqrt{1-x^2}}\,dx$

Integrating both sides:

$xy = \int \dfrac{x\cos^{-1}x}{\sqrt{1-x^2}}\,dx + C$

To evaluate the integral, use integration by parts. Let $u = \cos^{-1}x$ and $dv = \dfrac{x}{\sqrt{1-x^2}}\,dx$.

$du = -\dfrac{1}{\sqrt{1-x^2}}\,dx$ and $v = -\sqrt{1-x^2}$

$\int u\,dv = uv - \int v\,du$

$\int \dfrac{x\cos^{-1}x}{\sqrt{1-x^2}}\,dx = -\sqrt{1-x^2}\cos^{-1}x - \int \left(-\sqrt{1-x^2}\right)\left(-\dfrac{1}{\sqrt{1-x^2}}\right)\,dx$

$= -\sqrt{1-x^2}\cos^{-1}x - \int 1\,dx$

$= -\sqrt{1-x^2}\cos^{-1}x - x$

Substituting this back into the equation:

$xy = -\sqrt{1-x^2}\cos^{-1}x - x + C$

It is given that $\lim_{x\to 1^-} y(x) = 1$. Substituting $x = 1$ and $y = 1$:

$1(1) = -\sqrt{1-1^2}\cos^{-1}(1) - 1 + C$

$1 = 0 - 1 + C \Rightarrow C = 2$

The particular solution is:

$xy = 2 - x - \sqrt{1-x^2}\cos^{-1}x$

To find $y\left(\dfrac{1}{2}\right)$, substitute $x = \dfrac{1}{2}$:

$\dfrac{1}{2}y\left(\dfrac{1}{2}\right) = 2 - \dfrac{1}{2} - \sqrt{1 - \left(\dfrac{1}{2}\right)^2}\cos^{-1}\left(\dfrac{1}{2}\right)$

$\dfrac{1}{2}y\left(\dfrac{1}{2}\right) = \dfrac{3}{2} - \dfrac{\sqrt{3}}{2}\left(\dfrac{\pi}{3}\right)$

$\dfrac{1}{2}y\left(\dfrac{1}{2}\right) = \dfrac{3}{2} - \dfrac{\pi}{2\sqrt{3}}$

Multiplying by $2$:

$y\left(\dfrac{1}{2}\right) = 3 - \dfrac{\pi}{\sqrt{3}}$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $y = y(x)$ be the solution of the differential equation $(\tan x)^{1/2}\,dy = (\sec^3 x - (\tan x)^{3/2} y)\,dx$, $0 < x < \dfrac{\pi}{2}$, $y\left(\dfrac{\pi}{4}\right) = \dfrac{6\sqrt{2}}{5}$. If $y\left(\dfrac{\pi}{3}\right) = \dfrac{4}{5}\alpha$, then $\alpha^4$ equals _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **48**

**Detailed Solution:**

The given differential equation can be rewritten as:

$\dfrac{dy}{dx} + (\tan x)y = \dfrac{\sec^3 x}{(\tan x)^{1/2}}$

This is a linear differential equation of the form $\dfrac{dy}{dx} + P(x)y = Q(x)$.

Integrating Factor (IF) = $e^{\int \tan x \, dx} = e^{\ln(\sec x)} = \sec x$

Multiplying both sides by the IF and integrating, we get:

$y \sec x = \int \dfrac{\sec^4 x}{(\tan x)^{1/2}} \, dx + C$

$y \sec x = \int \dfrac{(1 + \tan^2 x)\sec^2 x}{(\tan x)^{1/2}} \, dx + C$

Let $\tan x = t$, then $\sec^2 x \, dx = dt$.

$y \sec x = \int \dfrac{1 + t^2}{t^{1/2}} \, dt + C$

$y \sec x = \int (t^{-1/2} + t^{3/2}) \, dt + C$

$y \sec x = 2t^{1/2} + \dfrac{2}{5}t^{5/2} + C$

$y \sec x = 2(\tan x)^{1/2} + \dfrac{2}{5}(\tan x)^{5/2} + C$

Given $y\left(\dfrac{\pi}{4}\right) = \dfrac{6\sqrt{2}}{5}$, substituting $x = \dfrac{\pi}{4}$:

$\dfrac{6\sqrt{2}}{5} \cdot \sqrt{2} = 2(1)^{1/2} + \dfrac{2}{5}(1)^{5/2} + C$

$\dfrac{12}{5} = 2 + \dfrac{2}{5} + C \Rightarrow C = 0$

The solution is $y \sec x = 2(\tan x)^{1/2} + \dfrac{2}{5}(\tan x)^{5/2}$.

Substituting $x = \dfrac{\pi}{3}$:

$y\left(\dfrac{\pi}{3}\right) \cdot 2 = 2(\sqrt{3})^{1/2} + \dfrac{2}{5}(\sqrt{3})^{5/2}$

$y\left(\dfrac{\pi}{3}\right) = 3^{1/4} + \dfrac{1}{5} \cdot 3^{5/4} = 3^{1/4}\left(1 + \dfrac{3}{5}\right) = \dfrac{8}{5} \cdot 3^{1/4}$

Given $y\left(\dfrac{\pi}{3}\right) = \dfrac{4}{5}\alpha$, we have:

$\dfrac{4}{5}\alpha = \dfrac{8}{5} \cdot 3^{1/4} \Rightarrow \alpha = 2 \cdot 3^{1/4}$

Therefore, $\alpha^4 = (2 \cdot 3^{1/4})^4 = 16 \cdot 3 = 48$

Answer: $48$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation: $\dfrac{dy}{dx}+\left(\dfrac{6x^2+(3x^2+2x^3+4)e^{-2x}}{(x^3+2)(2+e^{-2x})}\right)y=2+e^{-2x}$, $x \in (-1,2)$, satisfying $y(0)=\dfrac{3}{2}$. If $y(1)=\alpha(2+e^{-2})$, then $\alpha$ is equal to:

**Options:**

- **(A)** $\dfrac{13}{8}$
- **(B)** $\dfrac{6}{13}$
- **(C)** $\dfrac{12}{13}$
- **(D)** $\dfrac{13}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{13}{12}$**

**Detailed Solution:**

The given differential equation is a linear differential equation of the form $\dfrac{dy}{dx} + P(x)y = Q(x)$, where

$P(x) = \dfrac{6x^2 + (3x^2 + 2x^3 + 4)e^{-2x}}{(x^3+2)(2+e^{-2x})}$ and $Q(x) = 2 + e^{-2x}$.

We can rewrite $P(x)$ as:

$P(x) = \dfrac{3x^2(2+e^{-2x}) + 2e^{-2x}(x^3+2)}{(x^3+2)(2+e^{-2x})} = \dfrac{3x^2}{x^3+2} + \dfrac{2e^{-2x}}{2+e^{-2x}}$

The integrating factor (IF) is given by:

$IF = e^{\int P(x) dx} = e^{\int \left( \dfrac{3x^2}{x^3+2} + \dfrac{2e^{-2x}}{2+e^{-2x}} \right) dx}$

$IF = e^{\ln(x^3+2) - \ln(2+e^{-2x})} = \dfrac{x^3+2}{2+e^{-2x}}$

The general solution of the differential equation is:

$y \cdot (IF) = \int Q(x) \cdot (IF) dx + C$

Substituting the values, we get:

$y \left( \dfrac{x^3+2}{2+e^{-2x}} \right) = \int (2+e^{-2x}) \left( \dfrac{x^3+2}{2+e^{-2x}} \right) dx + C$

$y \left( \dfrac{x^3+2}{2+e^{-2x}} \right) = \int (x^3+2) dx + C$

$y \left( \dfrac{x^3+2}{2+e^{-2x}} \right) = \dfrac{x^4}{4} + 2x + C$

Given $y(0) = \dfrac{3}{2}$, substituting $x = 0$:

$\dfrac{3}{2} \left( \dfrac{0+2}{2+e^0} \right) = 0 + 0 + C$

$\dfrac{3}{2} \left( \dfrac{2}{3} \right) = C \Rightarrow C = 1$

Thus, the particular solution is:

$y \left( \dfrac{x^3+2}{2+e^{-2x}} \right) = \dfrac{x^4}{4} + 2x + 1$

To find $y(1)$, substitute $x = 1$:

$y(1) \left( \dfrac{1+2}{2+e^{-2}} \right) = \dfrac{1}{4} + 2 + 1$

$y(1) \left( \dfrac{3}{2+e^{-2}} \right) = \dfrac{13}{4}$

$y(1) = \dfrac{13}{12}(2+e^{-2})$

Comparing this with $y(1) = \alpha(2+e^{-2})$, we get:

$\alpha = \dfrac{13}{12}$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $x \frac{\mathrm{~d} y}{\mathrm{~d} x}-y=x^{2} \cot x, x \in(0, \pi)$. If $y\left(\frac{\pi}{2}\right)=\frac{\pi}{2}$, then $6 y\left(\frac{\pi}{6}\right)-8 y\left(\frac{\pi}{4}\right)$ is equal to :

**Options:**

- **(A)** $3 \pi$
- **(B)** $\pi$
- **(C)** $-\pi$
- **(D)** $-3 \pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\pi$**

**Detailed Solution:**

The differential equation $x\frac{dy}{dx} - y = x^2 \cot x$ can be rewritten as $\frac{dy}{dx} - \frac{y}{x} = x \cot x$.
The integrating factor is $\mu(x) = \frac{1}{x}$. Multiplying by $\mu(x)$ gives $\frac{d}{dx}\left(\frac{y}{x}\right) = \cot x$.
Integrating: $\frac{y}{x} = \ln|\sin x| + C$, so $y = x\ln(\sin x) + Cx$.
Using $y\left(\frac{\pi}{2}\right) = \frac{\pi}{2}$: we get $\frac{\pi}{2} = 0 + C\frac{\pi}{2}$, thus $C = 1$.
Therefore $y = x(1 + \ln(\sin x))$.
Now: $y\left(\frac{\pi}{6}\right) = \frac{\pi}{6}(1 - \ln 2)$ and $y\left(\frac{\pi}{4}\right) = \frac{\pi}{4}\left(1 - \frac{\ln 2}{2}\right)$.
Thus $6y\left(\frac{\pi}{6}\right) - 8y\left(\frac{\pi}{4}\right) = \pi(1 - \ln 2) - 2\pi\left(1 - \frac{\ln 2}{2}\right) = -\pi$.

</details>

---

### Q5. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $x \frac{d y}{d x}-\sin 2 y=x^{3}\left(2-x^{3}\right) \cos ^{2} y, x \neq 0$. If $y(2)=0$, then $\tan (y(1))$ is equal to

**Options:**

- **(A)** $-\frac{3}{4}$
- **(B)** $\frac{3}{4}$
- **(C)** $-\frac{7}{4}$
- **(D)** $\frac{7}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7}{4}$**

**Detailed Solution:**

Divide the equation by $\cos^2 y$:
$x\sec^2 y \frac{dy}{dx} - 2\tan y = x^3(2-x^3)$.
Let $v = \tan y$, so $\sec^2 y \frac{dy}{dx} = \frac{dv}{dx}$.
The equation becomes $x\frac{dv}{dx} - 2v = x^3(2-x^3)$.
Dividing by $x$: $\frac{dv}{dx} - \frac{2v}{x} = x^2(2-x^3)$.
Using integrating factor $\mu = x^{-2}$: $\frac{d}{dx}(x^{-2}v) = 2 - x^3$.
Integrating: $x^{-2}v = 2x - \frac{x^4}{4} + C$.
From $y(2) = 0$, we have $\tan 0 = 0 = 16 - 16 + 4C$, giving $C = 0$.
Therefore $\tan y = 2x^3 - \frac{x^6}{4}$.
At $x = 1$: $\tan(y(1)) = 2 - \frac{1}{4} = \frac{7}{4}$.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be a differentiable function in the interval $(0, \infty)$ such that $y(1)=2$, and $\lim _{t \rightarrow x}\left(\frac{t^{2} y(x)-x^{2} y(t)}{x-t}\right)=3$ for each $x>0$. Then $2 y(2)$ is equal to

**Options:**

- **(A)** 23
- **(B)** 27
- **(C)** 12
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 23**

**Detailed Solution:**

Given the limit $\lim_{t \to x} \frac{t^2 y(x) - x^2 y(t)}{x - t} = 3$.
The limit is in $\frac{0}{0}$ form. Applying L'Hopital's Rule with respect to $t$:
$\lim_{t \to x} \frac{\frac{d}{dt}(t^2 y(x) - x^2 y(t))}{\frac{d}{dt}(x - t)} = 3$
$\lim_{t \to x} \frac{2t y(x) - x^2 y'(t)}{-1} = 3$
Substituting $t = x$:
$\frac{2x y(x) - x^2 y'(x)}{-1} = 3$
$x^2 y'(x) - 2x y(x) = 3$
Dividing by $x^4$ to make it a linear differential equation or recognizing the quotient rule form:
$\frac{x^2 y'(x) - 2x y(x)}{x^4} = \frac{3}{x^4}$
$\frac{d}{dx} \left( \frac{y(x)}{x^2} \right) = \frac{3}{x^4}$
Integrating both sides with respect to $x$:
$\frac{y(x)}{x^2} = \int 3x^{-4} dx = \frac{3x^{-3}}{-3} + C = -\frac{1}{x^3} + C$
Given $y(1) = 2$:
$\frac{2}{1^2} = -\frac{1}{1^3} + C \implies 2 = -1 + C \implies C = 3$
So, $\frac{y(x)}{x^2} = -\frac{1}{x^3} + 3$
$y(x) = -\frac{1}{x} + 3x^2$
We need to find $2y(2)$:
$y(2) = -\frac{1}{2} + 3(2^2) = -\frac{1}{2} + 12 = \frac{23}{2}$
$2y(2) = 2 \times \frac{23}{2} = 23$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `3`

If the solution curve $y=f(x)$ of the differential equation 
 $\left(x^{2}-4\right) y^{\prime}-2 x y+2 x\left(4-x^{2}\right)^{2}=0, x>2$,
  passes through the point $(3,15)$, then the local maximum value of $f$ is $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

Rewriting: $\frac{dy}{dx} - \frac{2x}{x^2-4}y = -2x(x^2-4)$.
IF $= e^{-\int \frac{2x}{x^2-4}dx} = \frac{1}{x^2-4}$.
$\frac{d}{dx}\left(\frac{y}{x^2-4}\right) = -2x \Rightarrow \frac{y}{x^2-4} = -x^2 + C$.
$y = (x^2-4)(C-x^2)$. At $(3,15)$: $15 = 5(C-9) \Rightarrow C = 12$.
$y = (x^2-4)(12-x^2)$.
$y' = 4x(8-x^2) = 0 \Rightarrow x = 2\sqrt{2}$ (for $x > 2$).
$y'' = 32 - 12x^2 = -64 < 0$ at $x = 2\sqrt{2}$, confirming local maximum.
$f(2\sqrt{2}) = (8-4)(12-8) = 16$.

</details>

---

### Q8. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $x^{4} \mathrm{~d} y+\left(4 x^{3} y+2 \sin x\right) \mathrm{d} x=0, x>0, y\left(\frac{\pi}{2}\right)=0$. Then $\pi^{4} y\left(\frac{\pi}{3}\right)$ is equal to :

**Options:**

- **(A)** 72
- **(B)** 92
- **(C)** 64
- **(D)** 81

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 81**

**Detailed Solution:**

$x^4\,dy + 4x^3 y\,dx + 2\sin x\,dx = 0 \Rightarrow d(x^4 y) + 2\sin x\,dx = 0$.
Integrating: $x^4 y - 2\cos x = C$.
$y(\pi/2) = 0$: $(\pi/2)^4 \cdot 0 - 2\cos(\pi/2) = 0 \Rightarrow C = 0$.
$x^4 y = 2\cos x$.
At $x = \pi/3$: $(\pi/3)^4 y(\pi/3) = 2\cos(\pi/3) = 1$.
$\pi^4 y(\pi/3) = 81 \cdot (\pi/3)^4 y(\pi/3) \cdot \frac{1}{(\pi/3)^4} \cdot \frac{\pi^4}{81}$... Directly: $y(\pi/3) = \frac{81}{\pi^4}$, so $\pi^4 y(\pi/3) = 81$.

</details>

---

### Q9. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:[1, \infty) \rightarrow \mathbb{R}$ be a differentiable function. If $6 \int_{1}^{x} f(t) d t=3 x f(x)+x^{3}-4$ for all $x \geq 1$, then the value of $f(2)-f(3)$ is

**Options:**

- **(A)** -4
- **(B)** 3
- **(C)** 4
- **(D)** -3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

Differentiating $6\int_1^x f(t)dt = 3xf(x) + x^3 - 4$:
$6f(x) = 3f(x) + 3xf'(x) + 3x^2 \Rightarrow f(x) - xf'(x) = x^2$.
$\frac{d}{dx}\left(\frac{f(x)}{x}\right) = \frac{xf'(x)-f(x)}{x^2} = -1$.
Integrating: $\frac{f(x)}{x} = -x + C \Rightarrow f(x) = -x^2 + Cx$.
At $x = 1$: $0 = 3f(1) - 3 \Rightarrow f(1) = 1$. So $-1 + C = 1 \Rightarrow C = 2$.
$f(x) = -x^2 + 2x$. $f(2) = 0$, $f(3) = -3$.
$f(2) - f(3) = 3$.

</details>

---

### Q10. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $\sec x \frac{\mathrm{~d} y}{\mathrm{~d} x}-2 y=2+3 \sin x, x \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, $y(0)=-\frac{7}{4}$. Then $y\left(\frac{\pi}{6}\right)$ is equal to :

**Options:**

- **(A)** $-\frac{5}{4}$
- **(B)** $-\frac{5}{2}$
- **(C)** $-3 \sqrt{3}-7$
- **(D)** $-3 \sqrt{2}-7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{5}{2}$**

**Detailed Solution:**

The differential equation is $\sec x \frac{dy}{dx} - 2y = 2 + 3\sin x$, or $\frac{dy}{dx} - 2\cos x \cdot y = (2 + 3\sin x)\cos x$.
This is a linear ODE with integrating factor $\mu(x) = e^{-2\sin x}$.
Multiplying both sides and integrating: $\frac{d}{dx}[ye^{-2\sin x}] = (2 + 3\sin x)\cos x \cdot e^{-2\sin x}$
Computing the integral: $\int 2\cos x \cdot e^{-2\sin x} dx = -e^{-2\sin x}$
For the second term, using integration by parts: $\int 3\sin x \cos x \cdot e^{-2\sin x} dx = \frac{3}{4}e^{-2\sin x}(-2\sin x - 1)$
Thus: $ye^{-2\sin x} = -e^{-2\sin x} + \frac{3}{4}e^{-2\sin x}(-2\sin x - 1) + C$
Simplifying: $y = -\frac{7}{4} - \frac{3}{2}\sin x + Ce^{2\sin x}$
Using $y(0) = -\frac{7}{4}$ gives $C = 0$.
Therefore: $y(\frac{\pi}{6}) = -\frac{7}{4} - \frac{3}{2} \cdot \frac{1}{2} = -\frac{5}{2}$

</details>

---

### Q11. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution curve of the differential equation $\left(1+x^{2}\right) \mathrm{d} y+\left(y-\tan ^{-1} x\right) d x=0, y(0)=1$. Then the value of $y(1)$ is :

**Options:**

- **(A)** $\frac{4}{\mathrm{e}^{\pi / 4}}+\frac{\pi}{2}-1$
- **(B)** $\frac{2}{\mathrm{e}^{\pi / 4}}+\frac{\pi}{4}-1$
- **(C)** $\frac{2}{\mathrm{e}^{\pi / 4}}-\frac{\pi}{4}-1$
- **(D)** $\frac{4}{e^{\pi / 4}}-\frac{\pi}{2}-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{\mathrm{e}^{\pi / 4}}+\frac{\pi}{4}-1$**

**Detailed Solution:**

Rewrite as $\frac{dy}{dx} + \frac{y}{1+x^2} = \frac{\tan^{-1}x}{1+x^2}$.
IF $= e^{\tan^{-1}x}$.
$y \cdot e^{\tan^{-1}x} = \int \frac{\tan^{-1}x}{1+x^2} \cdot e^{\tan^{-1}x} dx$.
Let $t = \tan^{-1}x$: $= \int te^t dt = e^t(t-1) + C$.
$y = \tan^{-1}x - 1 + Ce^{-\tan^{-1}x}$.
Using $y(0) = 1$: $C = 2$.
$y(1) = \frac{\pi}{4} - 1 + \frac{2}{e^{\pi/4}}$.

</details>

---

### Q12. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f(x)=x-1$ and $g(x)=e^x$ for $x \in \mathbb{R}$. If $\frac{d y}{d x}=\left(e^{-2 \sqrt{x}} g(f(f(x)))-\frac{y}{\sqrt{x}}\right), y(0)=0$, then $y(1)$ is :-

**Options:**

- **(A)** $\frac{1-e^2}{e^4}$
- **(B)** $\frac{2 e-1}{e^3}$
- **(C)** $\frac{e-1}{e^4}$
- **(D)** $\frac{1-e^3}{e^4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{e-1}{e^4}$**

**Detailed Solution:**

$\begin{aligned}
& f(x)=x-1 \\
& f(f(x))=f(x)-1=x-1-1=x-2 \\
& g(f(f(x)))=e^{x-2} \\
& \therefore \frac{d y}{d x}=e^{-2 \sqrt{x}} \times e^{x-2}-\frac{1}{\sqrt{x}} y \\
& \frac{d y}{d x}+\frac{1}{\sqrt{x}} y=e^{x-2 \sqrt{x}-2} \text { which is L.D.E } \\
& \text { I.F. }=e^{\int \frac{d y}{\sqrt{x}}}=e^{2 \sqrt{x}}
\end{aligned}$
Its solution is
$\begin{aligned}
& y \times e^{2 \sqrt{x}}=\int e^{2 \sqrt{x}} \times e^{x-2 \sqrt{x}-2} d x+c \\
& y \times e^{2 \sqrt{x}}=\int e^{x-2} d x+c \\
& y \times e^{2 \sqrt{x}}=e^{x-2}+c
\end{aligned}$
$\text { Given } \mathrm{x}=0, \mathrm{y}=0 \Rightarrow 0=\mathrm{e}^{-2}+\mathrm{c} \quad ; \mathrm{c}=-\mathrm{e}^{-2}$
$\therefore \mathrm{y} \times \mathrm{e}^{2 \sqrt{\mathrm{x}}}=\mathrm{e}^{\mathrm{x}-2}-\mathrm{e}^{-2}$
$\text { when } \mathrm{x}=1, \mathrm{y} \times \mathrm{e}^2=\mathrm{e}^{-1}-\mathrm{e}^{-2}$
$y=\frac{e^{-1}-e^{-2}}{e^2}=\frac{\frac{1}{e}-\frac{1}{e^2}}{e^2}=\frac{e^2-e}{e^5}=\frac{e-1}{e^4}$
Option (1) is correct

</details>

---

### Q13. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $\left(x^2+1\right) y^{\prime}-2 x y=\left(x^4+2 x^2+1\right) \cos x$, $y(0)=1$. Then $\int_{-3}^3 y(x) d x$ is :

**Options:**

- **(A)** 24
- **(B)** 36
- **(C)** 30
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 24**

**Detailed Solution:**

$\begin{aligned}
& \left(x^2+1\right) \frac{d y}{d x}-2 x y=\left(x^4+2 x^2+1\right) \cos x \\
& \frac{d y}{d x}-\left(\frac{2 x}{x^2+1}\right) y=\frac{\left(x^2+1\right)^2 \cos x}{\mathrm{cx}^2+1}=\left(\mathrm{x}^2+1\right) \cos x \\
& \text { (Linear D.E) } \\
& P=\frac{-2 x}{x^2+1}, Q=\left(x^2+1\right) \cos x \\
& \text { I.F }=e^{\int P d x}=e^{\int \frac{-2 x}{x^2+1} d x}=\frac{1}{x^2+1} \\
& y \cdot \frac{1}{x^2+1}=\int\left(x^2+1\right) \cos x \cdot \frac{1}{x^2+1} d x \\
& \frac{y}{x^2+1}=\sin x+c \Rightarrow y \cos =1 \Rightarrow c=1 \\
& y=\left(x^2+1\right)(\sin x+1) \\
& \int_{-3}^3 y d x=\int_{-3}^3\left(x^2+1\right)(\sin x+1) \\
& d x=\int_{-3}^3 x^2 \sin x+x^2 \sin x+1 d x \\
& \Rightarrow \int_{-3}^3 x^2 \sin x d x+\int_{-3}^3 x^2 d x+\int_{-3}^3 \sin x d x+\int_{-3}^3 1 d x \\
& =0+18+0+6=24
\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution curve of the differential equation
$x\left(x^2+e^x\right) d y+\left(e^x(x-2) y-x^3\right) d x=0, x \gt 0$ passing through the point $(1,0)$. Then $y(2)$ is equal to :

**Options:**

- **(A)** $\frac{4}{4-\mathrm{e}^2}$
- **(B)** $\frac{2}{2+\mathrm{e}^2}$
- **(C)** $\frac{2}{2-\mathrm{e}^2}$
- **(D)** $\frac{4}{4+\mathrm{e}^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{4+\mathrm{e}^2}$**

**Detailed Solution:**

$\begin{aligned} & x\left(x^2+e^x\right) d y+\left(e^x(x-2) y-x^3\right) d x=0 \\ & x\left(x^2+e^x\right) \frac{d y}{d x}+e^x(x-2) y=x^3 \\ & \frac{d y}{d x}+\frac{e^x(x-2)}{x\left(x^2+e^x\right)} y=\frac{x^2}{x^2+e^x} \\ & \text { I.F. }=e^{\int \frac{e^x(x-2)}{x\left(x^2+e^x\right)} d x}=e^{\int \frac{e^x\left(\frac{1}{x^2}-\frac{2}{x^2}\right) d x}{\left(1+\frac{e^x}{x^2}\right)} d x}\end{aligned}$
Let $1+\frac{e^x}{x^2}=t \Rightarrow \frac{x^2 e^x-e^x 2 x}{x^4} d x=d t$
$\Rightarrow \text { I.F. } \mathrm{e}^{\ln \left(1+\frac{\mathrm{e}^2}{\mathrm{x}^2}\right)}=1+\frac{\mathrm{e}^{\mathrm{x}}}{\mathrm{x}^2}$
Now $y\left(1+\frac{e^x}{x^2}\right)=\int \frac{x^2}{x^2+e^x} \cdot \frac{x^2+e^x}{x^2} d x+C$
$y\left(1+\frac{e^x}{x^2}\right)=x+C$
Passing through $(1,0)$
$\begin{aligned}
& \Rightarrow C=-1 \\
& y=\frac{x-1}{1+\frac{e^x}{x^2}} \\
& y(2)=\frac{1}{1+\frac{e^2}{4}}=\frac{4}{4+e^2}
\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a curve $y=y(x)$ passes through the point $\left(1, \frac{\pi}{2}\right)$ and satisfies the differential equation $\left(7 x^4 \cot y-e^x \operatorname{cosec} y\right) \frac{d x}{d y}=x^5, x \geq 1$, then at $x=2$, the value of cosy is:

**Options:**

- **(A)** $\frac{2 \mathrm{e}^2-\mathrm{e}}{64}$
- **(B)** $\frac{2 \mathrm{e}^2+\mathrm{e}}{64}$
- **(C)** $\frac{2 \mathrm{e}^2-\mathrm{e}}{128}$
- **(D)** $\frac{2 \mathrm{e}^2+\mathrm{e}}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2 \mathrm{e}^2-\mathrm{e}}{128}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{7 \cot y}{x}-\frac{e^x \operatorname{cosec} y}{x^5} \\ & \frac{d y}{d x}=\frac{7 \cot y}{\sin y \cdot x}-\frac{e^x}{\sin y x^5} \\ & \sin y \frac{d y}{d x}-\cos y \cdot \frac{7}{x}=\frac{-e^x}{x^5} \\ & \text { let }-\cos y=t \\ & \sin y \frac{d y}{d x}=\frac{d t}{d x}\end{aligned}$
$\begin{aligned} & \frac{d t}{d x}+\frac{7 t}{x}=\frac{-e^x}{x^5} \\ & \text { I.F. }=x^7 \\ & \text { t. } x^7=-\int x^2 e^x d x \\ & \operatorname{cosy} x^7=x^2 e^x-2 \int x e^x d x \\ & \operatorname{cosy} x^7=x^2 e^x-2 x e^x+2 e^x+c \\ & x=1, y=\frac{\pi}{2}, c=-e \\ & \operatorname{cosy}=\frac{2 e^2-e}{128} \\ & \text { option }(3)\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:[0, \infty) \rightarrow \mathbb{R}$ be differentiable function such that $f(\mathrm{x})=1-2 \mathrm{x}+\int_0^x e^{x-t} f(t) \mathrm{dt}$ for all $\mathrm{x} \in[0, \infty)$.
Then the area of the region bounded by $\mathrm{y}=f(\mathrm{x})$ and the coordinate axes is

**Options:**

- **(A)** $\sqrt{5}$
- **(B)** $\frac{1}{2}$
- **(C)** $\sqrt{2}$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

$\begin{aligned} & y=1-2 x+e^x \int_0^x e^{-t} f(t) d t \\ & \frac{d y}{d x}=-2+e^{-x} \cdot e^x f(x)+e^x \int_0^x e^{-t} f(t) d t \\ & \frac{d y}{d x}=-2+y+y+2 x-1 \\ & \frac{d y}{d x}-2 y=(2 x-3) \\ & y e^{-2 x}=\int(2 x-3) d x \cdot e^{-2 x} \\ & y e^{-2 x}=\frac{-(2 x-3)}{2} e^{-2 x}+\int e^{-2 x} d x \\ & y e^{-2 x}=\frac{-(2 x-3)}{2} e^{-2 x}-\frac{1}{2} e^{-2 x}+c \\ & f(0)=1 \Rightarrow c=1-\frac{3}{2}+\frac{1}{2}=0\end{aligned}$
$\begin{aligned} & y=-\frac{(2 x-3)}{2}-\frac{1}{2} \\ & y=-x+1 \\ & x+y=1 \\ & \text { area }=\frac{1}{2}(1)(1)=\frac{1}{2}\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $\frac{d y}{d x}+3\left(\tan ^2 x\right) y+3 y=\sec ^2 x$
$y(0)=\frac{1}{3}+e^3$. Then $y\left(\frac{\pi}{4}\right)$ is equal to

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{4}{3}$
- **(C)** $\frac{4}{3}+\mathrm{e}^3$
- **(D)** $\frac{2}{3}+\mathrm{e}^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{3}$**

**Detailed Solution:**

$\begin{aligned}
& \frac{d y}{d x}+3\left(\sec ^2 x\right) y=\sec ^2 x, y(0)=\frac{1}{3}+e^3 \\
& \text { If }=e^{3 \int \sec ^2 x d x}=e^{3 \tan x}
\end{aligned}$
$\therefore$ Solution is
$\begin{aligned}
& e^{3 \tan x} y=\int e^{3 \tan x} \sec ^2 x d x \\
& e^{3 \tan x} y=\frac{e^{3 \tan x}}{3}+c \\
& \because y(0)=\frac{1}{3}+e^3 \Rightarrow c=e^3 \\
& \therefore y\left(\frac{\pi}{4}\right)=\frac{\frac{e^3}{3}+e^3}{e^3}=\frac{4}{3}
\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $g$ be a differentiable function such that $\int_0^x g(t) d t=x-\int_0^x \operatorname{tg}(t) d t, x \geq 0$ and let $y=y(x)$ satisfy the differential equation $\frac{d y}{d x}-y \tan x=$ $2(x+1) \sec x g(x), x \in\left[0, \frac{\pi}{2}\right)$. If $y(0)=0$, then $y\left(\frac{\pi}{3}\right)$ is equal to

**Options:**

- **(A)** $\frac{2 \pi}{3 \sqrt{3}}$
- **(B)** $\frac{4 \pi}{3}$
- **(C)** $\frac{2 \pi}{3}$
- **(D)** $\frac{4 \pi}{3 \sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4 \pi}{3}$**

**Detailed Solution:**

Diff. w.r.t. x
$\begin{aligned}
& g(x)=1-x g(x) \\
& g(x)=\frac{1}{1+x} \\
& \text { so } \frac{d y}{d x}-y \tan x=2 \sec x \\
& I F=e^{-\int \tan d x}=e^{\log \cos x}=\cos x
\end{aligned}$
solution of D.E.
$\begin{aligned}
& y \cos x=\int 2 d x+c \\
& y \cos x=2 x+c \\
& y(0)=0
\end{aligned}$
$\mathrm{c}=0$
$\begin{aligned} & y=\frac{2 x}{\cos x} \\ & y=2 x \sec x \\ & y\left(\frac{\pi}{3}\right)=2 \cdot \frac{\pi}{3} \cdot 2=\frac{4 \pi}{3}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (2 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $\frac{d y}{d x}+2 y \sec ^2 x=2 \sec ^2 x+3 \tan x \cdot \sec ^2 x$ such that $\mathrm{y}(0)=\frac{5}{4}$. Then $12\left(\mathrm{y}\left(\frac{\pi}{4}\right)-\mathrm{e}^{-2}\right)$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

$\begin{aligned} \text { I.F. } & =\mathrm{e}^{\int 2 \sec ^2 x d x} \\ & =\mathrm{e}^{2 \tan x}\end{aligned}$
Solution of diff. eq.
$\begin{gathered}y \cdot e^{2 \tan x}=\int e^{2 \tan x}\left(2 \sec ^2 x+3 \tan x \cdot \sec ^2 x\right) d x \\ y \cdot e^{2 \tan x}=\int e^{2 \tan x} \cdot\left(2 \sec ^2 x\right) d x+\int e^{2 \tan x} \cdot\left(3 \tan x \cdot \sec ^2 x\right) d x\end{gathered}$
y. $\mathrm{e}^{2 \tan x}=\mathrm{e}^{2 \tan x} \cdot 2 \tan x-\int \mathrm{e}^{2 \tan x} \cdot 2 \sec ^2 x \times 2 \tan x d x+\int \mathrm{e}^{2 \tan x} \cdot 3 \tan x \cdot \sec ^2 x d x$
$\begin{aligned} & y \cdot e^{2 \tan x}=2 \tan x \cdot e^{2 \tan x}-\int \mathrm{e}^{2 \tan x} \cdot \tan x \sec ^2 x d x \\ & y . e^{2 \tan x}=2 \tan x \cdot e^{2 \tan x}-\frac{\tan x \cdot e^{2 \tan x}}{2}+\frac{e^{2 \tan x}}{4}+C\end{aligned}$
$\begin{aligned} & y=2 \tan x-\frac{\tan x}{2}+\frac{1}{4}+\mathrm{Ce}^{-2 \tan x} \\ & x=0, y=\frac{5}{4} \\ & c=1\end{aligned}$
$\mathrm{y}\left(\frac{\pi}{4}\right)=\frac{7}{4}+\mathrm{e}^{-2}$
Then $12\left(y\left(\frac{\pi}{4}\right)-\mathrm{e}^{-2}\right)=12\left(\frac{7}{4}\right)=21$

</details>

---

### Q20. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f:[1, \infty) \rightarrow[2, \infty)$ be a differentiable function, If $10 \int_1^{\mathrm{x}} f(\mathrm{t}) \mathrm{dt}=5 \mathrm{x} f(\mathrm{x})-\mathrm{x}^5-9$ for all $\mathrm{x} \geq 1$, then the value of $f(3)$ is :

**Options:**

- **(A)** $18$
- **(B)** $32$
- **(C)** $22$
- **(D)** $26$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $32$**

**Detailed Solution:**

$\begin{aligned}
& 10 \frac{\mathrm{~d}}{\mathrm{dx}} \int_1^{\mathrm{x}} \mathrm{f}(\mathrm{t}) \mathrm{dt}=\frac{\mathrm{d}}{\mathrm{dx}}\left(5 \mathrm{xf}(\mathrm{x})-\mathrm{x}^5-9\right) \\
& \Rightarrow 10 f(x)=5 f(x)+5 \mathrm{xf}^{\prime}(\mathrm{x})-5 \mathrm{x}^4 \\
& \Rightarrow \mathrm{f}(\mathrm{x})+\mathrm{x}^4=\mathrm{xf}^{\prime}(\mathrm{x}) \\
& \Rightarrow \mathrm{y}+\mathrm{x}^4=\mathrm{x} \frac{\mathrm{dy}}{\mathrm{dx}} \\
& \Rightarrow \frac{d y}{d x}+y\left(-\frac{1}{x}\right)=x^3 \\
& \Rightarrow y e^{\int-\frac{1}{x} d x}=\int x^3 e^{\int-\frac{1}{x} d x}+c \\
& \Rightarrow \mathrm{ye}^{-\operatorname{tn}|x|}=\int \mathrm{x}^3 \mathrm{e}^{-\operatorname{tr}|x|}+\mathrm{c} \\
& \Rightarrow \frac{\mathrm{y}}{|\mathrm{x}|}=\int \frac{\mathrm{x}^3}{|\mathrm{x}|}+\mathrm{c} \\
& \Rightarrow \frac{\mathrm{y}}{\mathrm{x}}=\int \mathrm{x}^2+\mathrm{c} \\
& \Rightarrow \frac{\mathrm{y}}{\mathrm{x}}=\frac{\mathrm{x}^3}{3}+\mathrm{c}
\end{aligned}$
Put $x=1$ in given equation
$\begin{aligned}
& \Rightarrow 0=5 \mathrm{f}(1)-1-9 \Rightarrow \mathrm{f}(1)=2 \\
& \Rightarrow \frac{2}{1}=\frac{1}{3}+\mathrm{c} \Rightarrow \mathrm{c}=\frac{5}{3} \\
& \Rightarrow \frac{\mathrm{f}(3)}{3}=\frac{27}{3}+\frac{5}{3} \\
& \Rightarrow \mathrm{f}(3)=32
\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If for the solution curve $y=f(x)$ of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}+(\tan x) y=\frac{2+\sec x}{(1+2 \sec x)^2}$, $x \in\left(\frac{-\pi}{2}, \frac{\pi}{2}\right), f\left(\frac{\pi}{3}\right)=\frac{\sqrt{3}}{10}$, then $f\left(\frac{\pi}{4}\right)$ is equal to :

**Options:**

- **(A)** $\frac{\sqrt{3}+1}{10(4+\sqrt{3})}$
- **(B)** $\frac{5-\sqrt{3}}{2 \sqrt{2}}$
- **(C)** $\frac{9 \sqrt{3}+3}{10(4+\sqrt{3})}$
- **(D)** $\frac{4-\sqrt{2}}{14}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4-\sqrt{2}}{14}$**

**Detailed Solution:**

$\begin{aligned} & \text { If } \mathrm{e}^{\int \tan \mathrm{xdx}}=\mathrm{e}^{\ln (\sec \mathrm{x})}=\sec \mathrm{x} \\ & \therefore \mathrm{y} \cdot \sec \mathrm{x}=\int\left\{\frac{2+\sec \mathrm{x}}{(1+2 \sec \mathrm{x})^2}\right\} \sec \mathrm{xdx} \\ & =\int \frac{2 \cos \mathrm{x}+1}{(\cos \mathrm{x}+2)^2} \mathrm{dx} \text { Let } \cos \mathrm{x}=\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2} \\ & =\int \frac{2\left(\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}\right)+1}{\left(\frac{1-\mathrm{t}^2}{1+\mathrm{t}^2}+2\right)^2} 2 \mathrm{dt}\end{aligned}$

$\begin{aligned}
& =\int \frac{2-2 t^2+1+t^2}{\left(1-t^2+2+2 t^2\right)^2} \times 2 \mathrm{dt} \\
& =2 \int \frac{3-t^2}{\left(t^2+3\right)^2} \mathrm{dt}
\end{aligned}$

Let $\mathrm{t}+\frac{3}{\mathrm{t}}=\mathrm{u}$
$\begin{aligned}
& \left(1-\frac{3}{\mathrm{t}^2}\right) \mathrm{dt}=\mathrm{du} \\
& =-2 \int \frac{\mathrm{du}}{\mathrm{u}^2}
\end{aligned}$
$\begin{aligned}
& y \cdot(\sec x)=\frac{2}{u}+c \\
& y \cdot \sec x=\frac{2}{t+\frac{3}{t}}+c...(I)
\end{aligned}$
$\text { At } \mathrm{x}=\frac{\pi}{3}, \mathrm{t}=\tan \frac{\mathrm{x}}{2}=\frac{1}{\sqrt{3}}$
$2 \cdot \frac{\sqrt{3}}{10}=\frac{2}{\frac{1}{\sqrt{3}}+3 \sqrt{3}}+\mathrm{c}$
$\begin{aligned} & \text { 2. } \frac{\sqrt{3}}{10}=\frac{2 \sqrt{3}}{10}+\mathrm{c} \Rightarrow \mathrm{C}=0 \\ & \text { At } \mathrm{x}=\frac{\pi}{4}, \mathrm{t}=\tan \frac{\mathrm{x}}{2}=\sqrt{2}-1 \\ & \therefore \mathrm{y} \cdot \sqrt{2}=\frac{2}{\sqrt{2}-1+\frac{3}{\sqrt{2}-1}} \\ & \mathrm{y} \cdot \sqrt{2}=\frac{2(\sqrt{2}-1)}{6-2 \sqrt{2}} \\ & \mathrm{y}=\frac{\sqrt{2}(\sqrt{2}-1)}{2(3-\sqrt{2})}=\frac{1}{\sqrt{2}} \times \frac{2 \sqrt{2}-1}{7} \\ & =\frac{4-\sqrt{2}}{14}\end{aligned}$

</details>

---

### Q22. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let \(y=y(x)\) be the solution of the differential equation \(\cos x\left(\log _{\mathrm{e}}(\cos x)\right)^2 \mathrm{dy}+\left(\sin x-3 y \sin x \log _{\mathrm{e}}(\cos x)\right) \mathrm{d} x=0, x \in\left(0, \frac{\pi}{2}\right)\). If \(y\left(\frac{\pi}{4}\right)=\frac{-1}{\log _{\mathrm{e}} 2}\), then \(y\left(\frac{\pi}{6}\right)\) is equal to :

**Options:**

- **(A)** \(\frac{1}{\log _e(3)-\log _e(4)}\)
- **(B)** \(\frac{2}{\log _e(3)-\log _e(4)}\)
- **(C)** \(\frac{1}{\log _e(4)-\log _e(3)}\)
- **(D)** \(-\frac{1}{\log _e(4)}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \(\frac{1}{\log _e(3)-\log _e(4)}\)**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}-\frac{3 \sin x}{\cos x \ln \cos x} y=-\frac{\sin x}{\cos x(\ln \cos x)^2} \\ & \text { I.F. }=e^{-\int \frac{3 \tan x}{\ln \cos x} d x} \\ & \text { Let } \ln \cos x=t \\ & -\tan x d x=d t \\ & e^{3 \int^{\frac{d t}{t}}}=e^{3 \ln t}=t^3=(\ln \cos x)^3 \\ & \therefore \quad \text { Solution will be } \\ & \quad y(\ln \cos x)^3=-\int(\tan x)(\ln \cos x) d x \\ & y(\ln \cos x)^3=\frac{(\ln \cos x)^2}{2}+c \\ & \because \quad y\left(\frac{\pi}{4}\right)=-\frac{1}{\ln 2} \\ & \Rightarrow \quad c=0 \\ & \therefore \quad y=\frac{1}{2(\ln \cos x)} \\ & y\left(\frac{\pi}{6}\right)=\frac{1}{2} \times \frac{1}{\ln \left(\cos \frac{\pi}{6}\right)} \\ & =\frac{1}{2}\left[\frac{1}{\ln \left(\frac{\sqrt{3}}{2}\right)}\right] \\ & =\frac{1}{2} \times \frac{1}{\ln \sqrt{3}-\ln 2} \\ & =\frac{1}{\ln 3-\ln 4}\end{aligned}$

</details>

---

### Q23. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

If $y=y(x)$ is the solution of the differential equation,
$\sqrt{4-x^2} \frac{\mathrm{~d} y}{\mathrm{~d} x}=\left(\left(\sin ^{-1}\left(\frac{x}{2}\right)\right)^2-y\right) \sin ^{-1}\left(\frac{x}{2}\right),-2 \leq x \leq 2, y(2)=\frac{\pi^2-8}{4}$, then $y^2(0)$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+\frac{\left(\sin ^{-1} \frac{x}{2}\right)}{\sqrt{4-x^2}} y=\frac{\left(\sin ^{-3} \frac{x}{2}\right)^3}{\sqrt{4-x^2}} \\ & y e^{\frac{\left(\sin ^{-1} \frac{x}{2}\right)^2}{2}}=\int \frac{\left(\sin ^{-3} \frac{x}{2}\right)^3}{4-x^2} e^{\frac{\left(\sin ^{-1} \frac{x}{2}\right)^2}{2}} d x \\ & y=\left(\sin ^{-1} \frac{x}{2}\right)^2-2+c \cdot e^{\frac{-\left(\sin ^{-1} \frac{x}{2}\right)^2}{2}} \\ & y(2)=\frac{\pi^2}{4}-2 \Rightarrow c=0 \\ & y(0)=-2\end{aligned}$

</details>

---

### Q24. JEE Main 2025 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let $y=y(x)$ be the solution of the differential equation $2 \cos x \frac{\mathrm{~d} y}{\mathrm{~d} x}=\sin 2 x-4 y \sin x, x \in\left(0, \frac{\pi}{2}\right)$. If $y\left(\frac{\pi}{3}\right)=0$, then $y^{\prime}\left(\frac{\pi}{4}\right)+y\left(\frac{\pi}{4}\right)$ is equal to $\qquad$ ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+2 y \tan x=\sin x \\ & \text { I.F. }=e^{2 \int \tan x d x}=\sec ^2 x \\ & y \sec ^2 x=\int \frac{\sin x}{\cos ^2 x} d x \\ & =\int \tan x \sec x d x \\ & =\sec x+C \\ & C=-2\end{aligned}$


$\begin{aligned} & y=\cos x-2 \cos ^2 x \\ & y\left(\frac{\pi}{4}\right)=\frac{1}{\sqrt{2}}-1 \\ & y^{\prime}=-\sin x+4 \cos x \sin x \\ & y^{\prime}\left(\frac{\pi}{4}\right)=-\frac{1}{\sqrt{2}}+2 \\ & y^{\prime}\left(\frac{\pi}{4}\right)+y\left(\frac{\pi}{4}\right)=1\end{aligned}$

</details>

---

### Q25. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f:(0, \infty) \rightarrow \mathbf{R}$ be a function which is differentiable at all points of its domain and satisfies the condition $x^2 f^{\prime}(x)=2 x f(x)+3$, with $f(1)=4$. Then $2 f(2)$ is equal to :

**Options:**

- **(A)** 39
- **(B)** 19
- **(C)** 29
- **(D)** 23

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 39**

**Detailed Solution:**

$\begin{aligned} & x^2 f^{\prime}(x)-2 x f(x)=3 \\ & \left(\frac{x^2 f^{\prime}(x)-2 x f(x)}{\left(x^2\right)^2}\right)=\frac{3}{\left(x^2\right)^2} \\ & \Rightarrow \frac{d}{d x}\left(\frac{f(x)}{x^2}\right)=\frac{3}{x^4}\end{aligned}$


Integrating both sides
$\begin{aligned}
& \frac{f(x)}{x^2}=-\frac{1}{x^3}+C \\
& f(x)=-\frac{1}{x}+C x^2 \\
& \text { put } x=1 \\
& 4=-1+C \Rightarrow C=5 \\
& f(x)=-\frac{1}{x}+5 x^2 \\
& \text { Now } 2 \times f(2)=2 \times\left[-\frac{1}{2}+5 \times 2^2\right] \\
& =39
\end{aligned}$

</details>

---

### Q26. JEE Main 2025 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $f$ be a differentiable function such that $2(x+2)^2 f(x)-3(x+2)^2=10 \int_0^x(t+2) f(t) d t, x \geq 0$. Then $f(2)$ is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

$2(x+2)^2 f(x)-3(x+2)^2=10 \int_0^x(t+2) f(t) d t$
Differentiating both side
$\begin{aligned}
& 4(x+2) f(x)+2 f(x)(x+2)^2-6(x+2)=10(x+2) f(x) \\
& =(x+2) \frac{d y}{d x}-3 y=3 \\
& \frac{1}{3} \int \frac{d y}{y+1}=\int \frac{d x}{x+2} \\
& \ln |y+1=3 \ln | x+2 \mid+\ln c \\
& y+1=(x+2)^3 c \\
& \because y(0)=\frac{3}{2} \\
& \Rightarrow \frac{5}{16}=c \\
& \therefore \quad y=\frac{5}{16}(x+2)^3-1 \\
& y(2)=\frac{5}{16} \times 64-1=19
\end{aligned}$

</details>

---

### Q27. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{y}=\mathrm{y}(\mathrm{x})$ be the solution of the differential equation $\left(x y-5 x^2 \sqrt{1+x^2}\right) d x+\left(1+x^2\right) d y=0, y(0)=0$. Then $y(\sqrt{3})$ is equal to

**Options:**

- **(A)** $\sqrt{\frac{15}{2}}$
- **(B)** $\frac{5 \sqrt{3}}{2}$
- **(C)** $2 \sqrt{2}$
- **(D)** $\sqrt{\frac{14}{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5 \sqrt{3}}{2}$**

**Detailed Solution:**

$\begin{aligned} & \left(1+x^2\right) \frac{d y}{d x}+x y=5 x^2 \sqrt{1+x^2} \\ & \frac{d y}{d x}+\frac{x y}{1+x^2}=\frac{5 x^2}{\sqrt{1+x^2}} \\ & \therefore \text { I.F. }=\mathrm{e}^{\int \frac{\mathrm{x}}{1+x^2} \mathrm{dx}}=\mathrm{e}^{\frac{\ln \left(1+x^2\right)}{2}}=\sqrt{1+\mathrm{x}^2} \\ & \therefore \mathrm{y} \sqrt{1+\mathrm{x}^2}=\int \frac{5 \mathrm{x}^2}{\sqrt{1+\mathrm{x}^2}} \cdot \sqrt{1+\mathrm{x}^2} \mathrm{dx} \\ & \therefore \mathrm{y} \sqrt{1+\mathrm{x}^2}=\int \frac{5 \mathrm{x}^2}{\sqrt{1+\mathrm{x}^2}} \cdot \sqrt{1+\mathrm{x}^2} \mathrm{dx} \\ & \mathrm{y} \sqrt{1+\mathrm{x}^2}=\frac{5 \mathrm{x}^3}{3}+\mathrm{C} \\ & \because \mathrm{y}(0)=0 \Rightarrow 0=0+\mathrm{C} \Rightarrow \mathrm{C}=0\end{aligned}$


$\begin{aligned} & \therefore y=\frac{5 x^3}{3 \sqrt{1+x^2}} \\ & y(\sqrt{3})=\frac{15 \sqrt{3}}{32}=\frac{5 \sqrt{3}}{2}\end{aligned}$

</details>

---

### Q28. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a curve $y=f(x)$ pass through the points $(0,5)$ and $\left(\log _e 2, k\right)$. If the curve satisfies the differential equation $2(3+y) e^{2 x} d x-\left(7+e^{2 x}\right) d y=0$, then $k$ is equal to

**Options:**

- **(A)** $4$
- **(B)** $32$
- **(C)** $8$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{2(3+y) \cdot e^{2 x}}{7+e^{2 x}} \\ & \frac{d y}{d x}-\frac{2 y e^{2 x}}{7+e^{2 x}}=\frac{6 \cdot e^{2 x}}{7+e^{2 x}} \\ & \text { I.F. }=e^{-\int \frac{2 e^{2 x}}{7+e^{2 x}} d x} \\ & \Rightarrow e^{-\ln \left(7+e^{2 x}\right)} \\ & =\frac{1}{7+e^{2 x}} \\ & y \cdot \frac{1}{7+e^{2 x}}=\int \frac{6 e^{2 x}}{\left(7+e^{2 x}\right)^2} d x \\ & \frac{y}{7+e^{2 x}}=\frac{-3}{7+e^{2 x}+C} \\ & \therefore y(0)=5 \\ & \Rightarrow \frac{5}{8}=\frac{-3}{8}+C \\ & \Rightarrow C=1 \\ & \therefore y=-3+7+e^{2 x} \\ & y=e^{2 x}+4 \\ & \therefore k=8\end{aligned}$

</details>

---

### Q29. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $y=f(x)$ be the solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}+\frac{x y}{x^2-1}=\frac{x^6+4 x}{\sqrt{1-x^2}},-1 \lt x \lt 1$ such that $f(0)=0$. If $6 \int_{-1 / 2}^{1 / 2} f(x) \mathrm{d} x=2 \pi-\alpha$ then $\alpha^2$ is equal to _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27**

**Detailed Solution:**

I.F. $\mathrm{e}^{-\frac{1}{2} \int \frac{2 \mathrm{x}}{1-\mathrm{x}^2} \mathrm{dx}}=\mathrm{e}^{-\frac{1}{2} \ln \left(1-\mathrm{x}^2\right)}=\sqrt{1-\mathrm{x}^2}$

$y \times \sqrt{1-x^2}=\int\left(x^6+4 x\right) d x=\frac{x^7}{7}+2 x^2+c$

Given $y(0)=0 \Rightarrow c=0$
$y=\frac{\frac{x^7}{7}+2 x^2}{\sqrt{1-x^2}}$

Now, $6 \int_{-\frac{1}{2}}^{\frac{1}{2}} \frac{\frac{x^7}{7}+2 \mathrm{x}^2}{\sqrt{1-\mathrm{x}^2}} \mathrm{dx}=6 \int_{-\frac{1}{2}}^{\frac{1}{2}} \frac{2 \mathrm{x}^2}{\sqrt{1-\mathrm{x}^2}} \mathrm{dx}$
$\begin{aligned} & =24 \int_0^{\frac{1}{2}} \frac{x^2}{\sqrt{1-x^2}} d x \\ & \text { Put } x=\sin \theta \\ & d x=\cos \theta d \theta \\ & =24 \int_0^{\frac{\pi}{6}} \frac{\sin ^2 \theta}{\cos \theta} \cos \theta d \theta \\ & =24 \int_0^{\frac{\pi}{6}}\left(\frac{1-\cos 2 \theta}{2}\right) d \theta=12\left[\theta-\frac{\sin 2 \theta}{2}\right]_0^{\frac{\pi}{6}} \\ & =12\left(\frac{\pi}{6}-\frac{\sqrt{3}}{4}\right) \\ & =2 \pi-3 \sqrt{3} \\ & \alpha^2=(3 \sqrt{3})^2=27\end{aligned}$

</details>

---

### Q30. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x=f(y)$ is the solution of the differential equation
$\left(1+y^2\right)+\left(x-2 \mathrm{e}^{\tan ^{-1} y}\right) \frac{\mathrm{d} y}{\mathrm{~d} x}=0, y \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$
with $f(0)=1$, then $f\left(\frac{1}{\sqrt{3}}\right)$ is equal to :

**Options:**

- **(A)** $e^{\pi / 12}$
- **(B)** $e^{\pi / 4}$
- **(C)** $e^{\pi / 3}$
- **(D)** $e^{\pi / 6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $e^{\pi / 6}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{dx}}{\mathrm{dy}}+\frac{\mathrm{x}}{1+\mathrm{y}^2}=\frac{2 \mathrm{e}^{\tan ^{-1} \mathrm{y}}}{1+\mathrm{y}^2} \\ & \text { I.F. }=\mathrm{e}^{\tan ^{-1} \mathrm{y}} \\ & \mathrm{xe}^{\tan ^{-1} \mathrm{y}}=\int \frac{2\left(\mathrm{e}^{\tan ^{-1} \mathrm{y}}\right)^2 \mathrm{dy}}{1+\mathrm{y}^2} \\ & \text { Put } \tan ^{-1} \mathrm{y}=\mathrm{t}, \frac{\mathrm{dy}}{1+\mathrm{y}^2}=\mathrm{dt} \\ & \mathrm{xe}^{\tan ^{-1} \mathrm{y}}=\int 2 \mathrm{e}^{2 \mathrm{t}} \mathrm{dt} \\ & \mathrm{xe}^{\tan ^{-1} \mathrm{y}}=\mathrm{e}^{2 \tan ^{-1} \mathrm{y}}+\mathrm{c} \\ & \mathrm{x}=\mathrm{e}^{\tan ^{-1} \mathrm{y}}+\mathrm{ce}^{-\tan ^{-1} \mathrm{y}} \\ & \because \mathrm{y}=0, \mathrm{x}=1 \\ & 1=1+\mathrm{c} \Rightarrow \mathrm{c}=0 \\ & \mathrm{y}=\frac{1}{\sqrt{3}}, \mathrm{x}=\mathrm{e}^{\pi / 6}\end{aligned}$

</details>

---

### Q31. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $x=x(y)$ be the solution of the differential equation $y^2 \mathrm{~d} x+\left(x-\frac{1}{y}\right) \mathrm{d} y=0$. If $x(1)=1$, then $x\left(\frac{1}{2}\right)$ is :

**Options:**

- **(A)** $\frac{1}{2}+\mathrm{e}$
- **(B)** $3+e$
- **(C)** $3-e$
- **(D)** $\frac{3}{2}+e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3-e$**

**Detailed Solution:**

$\begin{aligned}
& y^2 d x+\left(x-\frac{1}{y}\right) d y=0 \\
& y^2 d x=\left(\frac{1}{y}-x\right) d y \\
& \Rightarrow y^2 \frac{d x}{d y}=\frac{1}{y}-x \\
& \Rightarrow \frac{d x}{d y}+\frac{x}{y^2}=\frac{1}{y^3} \\
& \text { I.F. }=e^{\int \frac{1}{y^2} d y}=e^{\frac{-1}{y}}
\end{aligned}$
$\therefore$ Solution is
$x e^{\frac{-1}{y}}=\int e^{-\frac{1}{y}} \times \frac{1}{y^3} d y+C$
Let $\frac{-1}{y}=t$
$\begin{aligned}
& \Rightarrow \frac{1}{y^2} d y=d t \\
& \Rightarrow x e^{-\frac{1}{y}}=-\int e^t t d t+C \\
& \Rightarrow x e^{-\frac{1}{y}}=-e^t(t-1)+C \\
& \Rightarrow x e^{-\frac{1}{y}}=-e^{\frac{-1}{y}}\left(\frac{-1}{y}-1\right)+C
\end{aligned}$
$x(1)=1$
$\Rightarrow e^{-1}=-e^{-1}(-2)+C$
$\Rightarrow C=-e^{-1}$
$\Rightarrow x=\frac{1}{y}+1-e^{-1+\frac{1}{y}}$
$x\left(\frac{1}{2}\right)=3-e$

</details>

---

### Q32. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution curve of the differential equation $\sec y \frac{\mathrm{d} y}{\mathrm{~d} x}+2 x \sin y=x^3 \cos y, y(1)=0$. Then $y(\sqrt{3})$ is equal to :

**Options:**

- **(A)** $\frac{\pi}{3}$
- **(B)** $\frac{\pi}{6}$
- **(C)** $\frac{\pi}{12}$
- **(D)** $\frac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\pi}{4}$**

**Detailed Solution:**

$\begin{aligned} & \sec ^2 y \frac{d y}{d x}+2 x \sin y \text { secy }=x^3 \cos y \text { secy } \\ & \sec ^2 y \frac{d y}{d x}+2 x \tan y=x^3 \\ & \operatorname{tany}=t \Rightarrow \sec ^2 y \frac{d y}{d x}=\frac{d t}{d x} \\ & \frac{d t}{d x}+2 x t=x^3, \text { If }=e^{\int 2 x d x}=e^{x^2} \\ & t x^{x^2}=\int x^3 \cdot e^{x^2} d x+c \\ & x^2=Z \Rightarrow t \cdot e^Z=\frac{1}{2} \int e^Z \cdot Z d Z=\frac{1}{2}\left[e^Z \cdot Z-e^Z\right]+c \\ & 2 \tan y=\left(x^2-1\right)+2 e^{-x^2} \\ & y(1)=0 \Rightarrow c=0 \Rightarrow y(\sqrt{3})=\frac{\pi}{4}\end{aligned}$

</details>

---

### Q33. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $\left(2 x \log _e x\right) \frac{d y}{d x}+2 y=\frac{3}{x} \log _e x, x>0$ and $y\left(e^{-1}\right)=0$. Then, $y(e)$ is equal to

**Options:**

- **(A)** $-\frac{3}{\mathrm{e}}$
- **(B)** $-\frac{3}{2 e}$
- **(C)** $-\frac{2}{3 e}$
- **(D)** $-\frac{2}{\mathrm{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\frac{3}{\mathrm{e}}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+\frac{y}{x \ell \ln x}=\frac{3}{2 x^2} \\ & \therefore \text { I.F. }=e^{\int \frac{1}{x \ln x} d x}=e^{\ln (\ln (x))}=\ln x \\ & \therefore y \ell \ln x=\int \frac{3 \ln x}{2 x^2} d x \\ & =\frac{3 \ln x}{2} \int x^{-2} d x-\int\left(\frac{3}{2 x} \cdot \int x^{-2} d x\right) d x \\ & =\frac{3 \ln x}{2}\left(-\frac{1}{x}\right)-\int \frac{3}{2 x}\left(-\frac{1}{x}\right) d x \\ & \text { y. } \ln x=\frac{-3 \ell n x}{2 x}-\frac{3}{2 x}+C\end{aligned}$
$\begin{aligned} & \because \mathrm{y}\left(\mathrm{e}^{-1}\right)=0 \\ & \therefore 0(-1)=\frac{3 \mathrm{e}}{2}-\frac{3 \mathrm{e}}{2}+\mathrm{C} \Rightarrow \mathrm{C}=0 \\ & \therefore \mathrm{y}=\frac{-3 \ell \mathrm{nx}}{2 \mathrm{x}}-\frac{3}{2 \mathrm{x}} \\ & \therefore \mathrm{y}(\mathrm{e})=\frac{-3}{2 \mathrm{e}}-\frac{3}{2 \mathrm{e}}=\frac{-3}{\mathrm{e}}\end{aligned}$

</details>

---

### Q34. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $\left(1+x^2\right) \frac{d y}{d x}+y=e^{\tan ^{-1} x}$, $y(1)=0$. Then $y(0)$ is

**Options:**

- **(A)** $\frac{1}{2}\left(e^{\pi / 2}-1\right)$
- **(B)** $\frac{1}{2}\left(1-e^{\pi / 2}\right)$
- **(C)** $\frac{1}{4}\left(1-e^{\pi / 2}\right)$
- **(D)** $\frac{1}{4}\left(e^{\pi / 2}-1\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}\left(1-e^{\pi / 2}\right)$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+\frac{y}{1+x^2}=\frac{e^{\tan ^{-1} x}}{1+x^2} \\ & \text { I.F. }=e^{\int \frac{1}{1+x^2} d x}=e^{\tan ^{-1} x} \\ & y \cdot e^{\tan ^{-1} x}=\int\left(\frac{e^{\tan ^{-1} x}}{1+x^2}\right) e^{\tan ^{-1} x} \cdot d x \\ & \text { Let } \tan ^{-1} x=z \quad \therefore \frac{d x}{1+x^2}=d z \\ & \therefore y \cdot e^z=\int e^{2 z} d z=\frac{e^{2 z}}{2}+C \\ & y \cdot e^{\tan ^{-1} x}=\frac{e^{2 \tan ^{-1} x}}{2}+C \\ & \Rightarrow y=\frac{e^{\tan ^{-1} x}}{2}+\frac{C}{e^{\tan ^{-1} x}}\end{aligned}$
$\begin{aligned} & \because \mathrm{y}(1)=0 \Rightarrow 0=\frac{\mathrm{e}^{\pi / 4}}{2}+\frac{\mathrm{C}}{\mathrm{e}^{\pi / 4}} \Rightarrow \mathrm{C}=\frac{-\mathrm{e}^{\pi / 2}}{2} \\ & \therefore \mathrm{y}=\frac{\mathrm{e}^{\tan ^{-1} \mathrm{x}}}{2}-\frac{\mathrm{e}^{\pi / 2}}{2 \mathrm{e}^{\tan ^{-1} \mathrm{x}}} \\ & \therefore \mathrm{y}(0)=\frac{1-\mathrm{e}^{\pi / 2}}{2}\end{aligned}$

</details>

---

### Q35. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation
$\frac{\mathrm{d} y}{\mathrm{~d} x}+\frac{2 x}{\left(1+x^2\right)^2} y=x \mathrm{e}^{\frac{1}{\left(1+x^2\right)}} ; y(0)=0 .$
Then the area enclosed by the curve $f(x)=y(x) \mathrm{e}^{-\frac{1}{\left(1+x^2\right)}}$ and the line $y-x=4$ is__________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

$\begin{aligned} & I F=e^{\int \frac{2 x}{\left(1+x^2\right)^2} d x}=e^{\frac{-1}{1+x^2}} \\ & y \cdot e^{\frac{-1}{1+x^2}}=\int x \cdot e^{\frac{1}{1+x^2}} \cdot e^{\frac{-1}{1+x^2} d x} \\ & y \cdot e^{\frac{-1}{1+x^2}}=\frac{x^2}{2}+c \\ & (0,0) \Rightarrow C=0 \\ & y(x)=\frac{x^2}{2} e^{\frac{1}{1+x^2}} \\ & f(x)=\frac{x^2}{2}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TCQQkoBtJmbqKsrrVBHqnnMXLYJnuZgXOleXKg1W230.original.fullsize.png">
$A=\int_{-2}^4(x+4)-\frac{x^2}{2} d x=18$

</details>

---

### Q36. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=y(x)$ is the solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}+2 y=\sin (2 x), y(0)=\frac{3}{4}$, then $y\left(\frac{\pi}{8}\right)$ is equal to:

**Options:**

- **(A)** $\mathrm{e}^{\pi / 8}$
- **(B)** $\mathrm{e}^{\pi / 4}$
- **(C)** $\mathrm{e}^{-\pi / 4}$
- **(D)** $\mathrm{e}^{-\pi / 8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{e}^{-\pi / 4}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+2 y=\sin 2 x, y(0)=\frac{3}{4} \\ & \text { I.F }=e^{\int 2 d x}=e^{2 x} \\ & y \cdot e^{2 x}=\int e^{2 x} \sin 2 x d x \\ & y \cdot e^{2 x}=\frac{e^{2 x}(2 \sin 2 x-2 \cos 2 x)}{4+4}+C \\ & x=0, y=\frac{3}{4} \Rightarrow \frac{3}{4} \cdot 1=\frac{1(0-2)}{8}+C \\ & \frac{3}{4}=-\frac{1}{4}+C \\ & 1=C \\ & y=\frac{2 \sin 2 x-2 \cos 2 x}{8}+1 \cdot e^{-2 x} \\ & x=\frac{\pi}{8}, y=\frac{1}{8}\left(2 \sin \frac{\pi}{4}-2 \cos \frac{\pi}{4}\right)+e^{-2\left(\frac{\pi}{8}\right)} \\ & y=0+e^{-\frac{\pi}{4}}\end{aligned}$

</details>

---

### Q37. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $\left(x^2+4\right)^2 d y+\left(2 x^3 y+8 x y-2\right) d x=0$. If $y(0)=0$, then $y(2)$ is equal to

**Options:**

- **(A)** $\frac{\pi}{32}$
- **(B)** ${2}{\pi}$
- **(C)** $\frac{\pi}{8}$
- **(D)** $\frac{\pi}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\pi}{32}$**

**Detailed Solution:**

$\begin{aligned}
& \frac{d y}{d x}+y\left(\frac{2 x^3+8 x}{\left(x^2+4\right)^2}\right)=\frac{2}{\left(x^2+4\right)^2} \\
& \frac{d y}{d x}+y\left(\frac{2 x}{x^2+4}\right)=\frac{2}{\left(x^2+4\right)^2} \\
& \text { IF }=e^{\int \frac{2 x}{x^2+4} d x} \\
& \text { IF }=x^2+4 \\
& y \times\left(x^2+4\right)=\int \frac{2}{\left(x^2+4\right)^2} \times\left(x^2+4\right) \\
& y\left(x^2+4\right)=2 \int \frac{d x}{x^2+2^2} \\
& y\left(x^2+4\right)=\frac{2}{2} \tan ^{-1}\left(\frac{x}{2}\right)+c \\
& 0=0+c=c=0 \\
& y\left(x^2+4\right)=\tan ^{-1}\left(\frac{x}{2}\right) \\
& y \text { at } x=2 \\
& y(4+4)=\tan ^{-1}(1) \\
& y(2)=\frac{\pi}{32}
\end{aligned}$

</details>

---

### Q38. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the solution $y=y(x)$ of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}-y=1+4 \sin x$ satisfy $y(\pi)=1$. Then $y\left(\frac{\pi}{2}\right)+10$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

$\begin{aligned} & y e^{-x}=\int\left(e^{-x}+4 e^{-x} \sin x\right) d x \\ & y e^{-x}=-e^{-x}-2\left(e^{-x} \sin x e^{-x} \cos x\right)+C \\ & y=-1-2(\sin x+\cos x)+c e^x \\ & \because y(\pi)=1 \Rightarrow c=0 \\ & y(\pi / 2)=-1-2=-3 \\ & \text { Ans }=10-3=7\end{aligned}$

</details>

---

### Q39. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>−</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mi>y</mi></mfrac><mo>,</mo><mi>x</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>x</mi><mfenced><mn>2</mn></mfenced></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>1</mn><mo>+</mo><mi>x</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mstyle><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mi>y</mi></mfrac><mo>-</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mo>-</mo><mi>y</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>x</mi><mo>=</mo><mi>t</mi><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mfrac><mi>t</mi><mi>y</mi></mfrac><mo>=</mo><mo>-</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>∫</mo><mo>-</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mi>d</mi><mi>y</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>log</mi><mi>y</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>log</mi><mfrac><mn>1</mn><mi>y</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mfrac><mn>1</mn><mi>y</mi></mfrac></math></p><p>So, the solution of the given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>t</mi><mi>y</mi></mfrac><mo>=</mo><mo>∫</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>×</mo><mfenced><mrow><mo>-</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>y</mi></mfrac><mo>=</mo><mo>∫</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>×</mo><mfenced><mrow><mo>-</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mstyle><mstyle displaystyle="true"><mi>y</mi></mstyle></mfrac><mo>=</mo><mo>-</mo><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>1</mn></mstyle></mfrac><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mstyle><mstyle displaystyle="true"><mi>y</mi></mstyle></mfrac><mo>=</mo><mo>-</mo><mi>y</mi><mo>+</mo><mn>3</mn></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mstyle displaystyle="true"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mi>x</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q40. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> be a non-zero real number. Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>R</mi></math> is a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>α</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>3</mn></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>∈</mo><mi>R</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>−</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced></math> is equal to ________.</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math> </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>−</mo><mi>α</mi><mo>·</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>−</mo><mi>α</mi><mo>·</mo><mi>y</mi><mo>=</mo><mn>3</mn></math></p><p>Which is a linear differential equation, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>α</mi><mi>x</mi></mrow></msup></math></p><p>Solution of the differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><msup><mi>e</mi><mrow><mo>−</mo><mi>α</mi><mi>x</mi></mrow></msup></mfenced><mo>=</mo><mo>∫</mo><mn>3</mn><mo>·</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>α</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>⋅</mo><mfenced><msup><mi>e</mi><mrow><mo>−</mo><mi>α</mi><mi>x</mi></mrow></msup></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><msup><mi>e</mi><mrow><mo>−</mo><mi>α</mi><mi>x</mi></mrow></msup></mrow><mrow><mo>−</mo><mi>α</mi></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mo>−</mo><mn>3</mn></mrow><mi>α</mi></mfrac><mo>+</mo><mi>c</mi><mo>·</mo><msup><mi>e</mi><mrow><mi>α</mi><mi>x</mi></mrow></msup></math></p><p>Now, taking case I: when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>&gt;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mfrac><mrow><mo>−</mo><mn>3</mn></mrow><mi>α</mi></mfrac><mo>+</mo><mi>c</mi><mfenced><mn>0</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mo>−</mo><mn>3</mn></math> (rejected)</p><p>Case-II: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>&lt;</mo><mn>0</mn></math></p><p>as <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>→</mo><mo>−</mo><mi>∞</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mfrac><mrow><mo>−</mo><mn>3</mn></mrow><mi>α</mi></mfrac><mo>=</mo><mn>1</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mrow><mo>-</mo><mo>∞</mo></mrow></mfenced></mrow></msup><mo>→</mo><mo>∞</mo><mo>,</mo><mo> </mo><mtext>so </mtext><mi>c</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mo>−</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math> and also  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math> is constant function, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mrow><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q41. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mfenced><mi>t</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi><mo>,</mo><mi>x</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mn>1</mn></mfenced></math> equals ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mrow><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>∫</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>log</mi><mfenced close="|" open="|"><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p>Solution of the differential equations is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>×</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mo>∫</mo><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>2</mn><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>0</mn><mn>2</mn></mfrac><mo>+</mo><mn>0</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>t</mi><mo>+</mo><mn>2</mn></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>1</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><msup><mn>1</mn><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>x</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q42. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>3</mn></msup><mo>−</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>−</mo><mn>1</mn><mo>,</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>+</mo><mi>y</mi><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></mfenced><mn>2</mn></msup></math> equals:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mn>4</mn><mo>+</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><mn>3</mn><mo>−</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>−</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>−</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>3</mn></msup><mo>−</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>−</mo><mn>1</mn></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>−</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>x</mi><msup><mi>t</mi><mn>3</mn></msup><mo>−</mo><mi>x</mi><mi>t</mi><mo>−</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><msup><mi>t</mi><mn>3</mn></msup><mo>−</mo><mi>x</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>x</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>x</mi><msup><mi>t</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>3</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>x</mi><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msup><mi>t</mi><mn>3</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><msup><mi>t</mi><mn>3</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>Putting this value in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>x</mi><mi>u</mi><mo>=</mo><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>u</mi><mo>=</mo><mo>-</mo><mn>4</mn><mi>x</mi></math></p><p>Integrating factor, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>∫</mo><mo>-</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p>So, solution of the given differential equation is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>×</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><mo>∫</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mfenced><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><msup><mi>t</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>∫</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mfenced><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>-</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mo>∫</mo><mn>2</mn><msup><mi>e</mi><mi>z</mi></msup><mi>d</mi><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><msup><mi>e</mi><mi>z</mi></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mo>+</mo><mi>C</mi><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></math></p><p>It is given that, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>−</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></mrow></mfrac></math></p><p>Putting, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>y</mi><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>−</mo><msup><mi>e</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mo>−</mo><msqrt><mi>e</mi></msqrt></mrow></mfrac></mfenced></math></p>

</details>

---

### Q43. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>tan</mi><mstyle displaystyle="true"><mi>x</mi></mstyle></mrow></mfenced><mstyle displaystyle="true"><mo>+</mo></mstyle><mstyle displaystyle="true"><mi>y</mi></mstyle></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mfenced><mrow><mi>sec</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mi>tan</mi><mi>x</mi></mrow></mfenced></mstyle></mrow></mfrac><mo>,</mo><mo> </mo><mi>x</mi><mo>∈</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mo> </mo><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced></math> satisfying the condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>3</mn></mfrac></mfenced></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msqrt><mn>3</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mfenced><mrow><mi>sec</mi><mi>x</mi><mo>-</mo><mi>sin</mi><mi>x</mi><mi>tan</mi><mi>x</mi></mrow></mfenced></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mfenced><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mi>sin</mi><mstyle displaystyle="true"><mi>x</mi><mi>cos</mi><mi>x</mi></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mo>∫</mo><mi>cosec</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>cosec</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>cosec</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mi>cosec</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cot</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>IF</mi><mo>=</mo><mi>cot</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>×</mo><mi>cot</mi><mi>x</mi><mo>=</mo><mo>∫</mo><mi>cot</mi><mi>x</mi><mo>×</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>×</mo><mi>cot</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo>∫</mo><mi>cosec</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mi>cot</mi><mi>x</mi><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>cosec</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mi>cot</mi><mfrac><mi>π</mi><mn>4</mn></mfrac><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>cosec</mi><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>-</mo><mi>cot</mi><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mi>cot</mi><mi>x</mi><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>cosec</mi><mn>2</mn><mi>x</mi><mo>-</mo><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>3</mn></mfrac></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mi>cot</mi><mfrac><mi>π</mi><mn>3</mn></mfrac><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mi>cosec</mi><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mi>cot</mi><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>×</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mi>log</mi><mfenced close="|" open="|"><mrow><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>×</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>log</mi><mn>3</mn><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>log</mi><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mi>log</mi><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q44. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced close="]" open="["><mrow><mi>x</mi><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn><mo>,</mo><mo> </mo><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">m</mi><mi mathvariant="normal">n</mi></mfrac><mo>,</mo><mi mathvariant="normal">m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> are coprime numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>+</mo><mi mathvariant="normal">n</mi></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **97**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced close="]" open="["><mrow><mi>x</mi><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>The above equation is a linear differential equation,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>∫</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></msup><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p>Now, the solution of the differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>∫</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>×</mo><msqrt><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></msqrt><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>∫</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>3</mn></msqrt><mfenced><mrow><mfrac><mn>1</mn><mrow><msup><mn>2</mn><mn>4</mn></msup><mo>·</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mo>·</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>32</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>65</mn><mn>32</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>97</mn></math></p>

</details>

---

### Q45. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math> with condition <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>y</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>y</mi><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mo>+</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>∫</mo><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mi>log</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p>So, solution of the equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>∫</mo><mfrac><mrow><mi>sin</mi><mi>x</mi></mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>∫</mo><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>It is given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>0</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mi>cos</mi><mn>0</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>C</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>cos</mi><mn>2</mn></msup><mfrac><mi>π</mi><mn>2</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mfenced><mfrac><mi>π</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q46. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mfenced><mi>y</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#62;</mo><mo>-</mo><mn>1</mn></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><msup><mi>e</mi><mn>9</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>4</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mi>u</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>u</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mi>d</mi><mi>v</mi></math></p><p>So, the equation becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>v</mi><mo>&#160;</mo><mi>ln</mi><mi>v</mi></mrow></mfenced><mi>du</mi><mo>=</mo><mo>-</mo><mfenced><mrow><mi>u</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>ln</mi><mi>v</mi></mrow></mfenced><mi>d</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>v</mi><mo>&#160;</mo><mi>ln</mi><mi>v</mi><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>v</mi></mrow></mfrac><mo>+</mo><mi>u</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>ln</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mrow><mi>d</mi><mi>v</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>v</mi><mo>&#160;</mo><mi>ln</mi><mi>v</mi></mrow></mfrac><mo>.</mo><mo>&#160;</mo><mi>u</mi><mo>=</mo><mfrac><mn>1</mn><mi>v</mi></mfrac></math></p><p>Which is a linear differential equation,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>v</mi><mo>&#160;</mo><mi>ln</mi><mi>v</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced></mrow></msup><mo>=</mo><msup><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math></p><p>Now solution of differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>u</mi><mo>&#183;</mo><msup><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>v</mi></mfrac><mo>&#183;</mo><msup><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mi>d</mi><mi>v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>u</mi><mo>&#183;</mo><msup><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>ln</mi><mi>v</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now using given value, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>v</mi><mo>=</mo><msup><mi>e</mi><mn>4</mn></msup><mo>&#160;</mo><mo>&#8658;</mo><mi>u</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#183;</mo><mfenced><msup><mn>4</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#183;</mo><msup><mfenced><mn>4</mn></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mo>=</mo><mfrac><mn>16</mn><mn>3</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mn>9</mn></msup><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>v</mi><mo>=</mo><mi>y</mi><mo>+</mo><mn>2</mn><mo>=</mo><msup><mi>e</mi><mn>9</mn></msup></math></p><p>Now putting the value in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">u</mi><mo>&#183;</mo><mn>3</mn><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>27</mn><mo>+</mo><mfrac><mn>14</mn><mn>3</mn></mfrac><mo>=</mo><mn>18</mn><mo>+</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>4</mn><mo>=</mo><mi>u</mi><mo>=</mo><mn>6</mn><mo>+</mo><mfrac><mn>14</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>14</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>32</mn><mn>9</mn></mfrac></math></p></blockquote>

</details>

---

### Q47. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></mfrac><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>&#160;&#160;</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><msqrt><mn>2</mn></msqrt></mfenced><mo>=</mo><mi>&#945;</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msqrt><mi>&#945;</mi></msqrt><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>+</mo><mi>&#946;</mi><mo>-</mo><msqrt><mi>&#947;</mi></msqrt><mo>,</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>&#946;</mi><mi>&#947;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<blockquote><p>Given differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></mfrac><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>&#160;&#160;</mo></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p>The required equation will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>ln</mi><mfenced><mfenced close="|" open="|"><mrow><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>+</mo><mi>x</mi></mrow></mfenced></mfenced><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt><mo>+</mo><mi>C</mi></math></p><p>Now using, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mo>&#183;</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mi>ln</mi><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>=</mo><mn>2</mn><mi>ln</mi><mfenced><mrow><mn>2</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mrow></mfenced><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><msqrt><mn>3</mn></msqrt></math></p><p>Now finding the value of function at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>+</mo><mn>1</mn><mo>-</mo><msqrt><mn>3</mn></msqrt></math></p><p>Now on comparing we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>&#946;</mi><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>6</mn></math></p><p>Hence, this is the required answer.</p></blockquote>

</details>

---

### Q48. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> be a solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced><mo>=</mo><mi>&#946;</mi><mo>,</mo></math> then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>e</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>e</mi><mfenced><mrow><mn>5</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mfenced><mrow><mn>5</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>e</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>y</mi><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>t</mi></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><msup><mi>y</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>So, the equation becomes,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p>So, solution of the differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>&#8747;</mo><mfrac><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></msqrt></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>&#946;</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>3</mn><mi>&#946;</mi></mfrac><mo>=</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>&#946;</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>+</mo><mi>ln</mi><mfenced open="|" close="|"><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>e</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>e</mi><mfenced><mrow><mn>3</mn><mo>+</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfenced></math></p>

</details>

---

### Q49. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><msup><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mi>x</mi><mn>7</mn></msup></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>637</mn><mn>128</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>679</mn><mn>128</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>693</mn><mn>128</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>697</mn><mn>128</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>693</mn><mn>128</mn></mfrac></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced><mn>2</mn></msup></mstyle><msup><mi>x</mi><mn>7</mn></msup></mfrac></math></p><p>This is linear differential equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>5</mn><mrow><mi>x</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn>5</mn><msup><mi>x</mi><mn>5</mn></msup></mrow><mrow><msup><mi>x</mi><mn>6</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>5</mn><mrow><msup><mi>x</mi><mn>6</mn></msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><msup><mi>x</mi><mn>6</mn></msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup><mspace linebreak="newline"/></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mfenced><mrow><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p>So, solution is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfrac><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><msup><mi>x</mi><mn>5</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>&#215;</mo><mfrac><msup><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mi>x</mi><mn>7</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>y</mi><msup><mi>x</mi><mn>5</mn></msup></mrow><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mo>&#8747;</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>y</mi><msup><mi>x</mi><mn>5</mn></msup></mrow><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>y</mi><msup><mi>x</mi><mn>5</mn></msup></mrow><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mi>C</mi></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>2</mn></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mn>1</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><msup><mi>x</mi><mn>5</mn></msup></mrow><mfenced><mrow><msup><mi>x</mi><mn>5</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>&#215;</mo><mn>32</mn></mrow><mn>33</mn></mfrac><mo>=</mo><mfrac><mn>16</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mn>21</mn><mo>&#215;</mo><mn>33</mn></mrow><mn>128</mn></mfrac><mo>=</mo><mfrac><mn>693</mn><mn>128</mn></mfrac></math></p>

</details>

---

### Q50. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#160;</mo><mi>d</mi><mi>t</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mi>x</mi><mo>=</mo><mn>4</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mi>x</mi></msubsup><mi>t</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>t</mi></mfenced><mo>&#160;</mo><mi>d</mi><mi>t</mi></math></p><p>Now Differentiating both side w.r.t. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mn>2</mn><mi>x</mi><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn><mi>x</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>2</mn><mi>x</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>Let</mi><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced></math></p><p>Which is a linear differential equation,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>&#160;</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mfrac><mn>2</mn><mi mathvariant="normal">x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>ln</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p>Now solution of the differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>4</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, the function will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>So, the required value is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo><mi>f</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mn>18</mn><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>+</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>160</mn></math></p></blockquote>

</details>

---

### Q51. JEE Main 2023 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mo>(</mo><mi>y</mi><mo>)</mo><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>y</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>, of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>cos</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mi>cos</mi><mi>y</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>cos</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mi>sin</mi><mi>y</mi><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>  satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>m</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>n</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are coprime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>cos</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mi>cos</mi><mi>y</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>cos</mi><mi>y</mi></mrow></mfenced></mrow></mfenced><mi>sin</mi><mi>y</mi><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn><mi>tan</mi><mi>y</mi></mrow><mrow><mi>lncos</mi><mi>y</mi></mrow></mfrac></mfenced><mi>x</mi><mo>=</mo><mfrac><mrow><mi>sin</mi><mi>y</mi></mrow><mrow><msup><mfenced><mrow><mo>In</mo><mi>cos</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>&#183;</mo><mi>cos</mi><mi>y</mi></mrow></mfrac></math></p><p>Which is a linear differential equation,</p><p>So, Integrating factor will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mn>3</mn><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>tan</mi><mi>y</mi></mrow><mrow><mi>lncos</mi><mi>y</mi></mrow></mfrac><mi>d</mi><mi>y</mi></mrow></msup><mo>=</mo><msup><mfenced><mrow><mi>lncos</mi><mi>y</mi></mrow></mfenced><mn>3</mn></msup></math></p><p>So, solution of differential equation is given by,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mfenced><mrow><mi>lncos</mi><mi>y</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>sin</mi><mi>y</mi></mrow><mrow><mi>cos</mi><mi>y</mi></mrow></mfrac><mfenced><mrow><mi>lncos</mi><mi>y</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mfenced><mrow><mi>lncos</mi><mi>y</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mfenced><mrow><mi>lncos</mi><mi>y</mi></mrow></mfenced><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p>Now using the given value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>ln</mi><mn>2</mn></mrow></mfrac></math>
We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>ln</mi><mi>cos</mi><mo>&#160;</mo><mi>y</mi></mrow></mfrac></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>ln</mi><mstyle displaystyle="true"><mfenced><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mfenced></mstyle></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>ln</mi><mn>4</mn><mo>-</mo><mi>ln</mi><mn>3</mn></mrow></mfrac></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msub><mi>log</mi><mi>e</mi></msub><mi>m</mi><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mi>n</mi></mrow></mfrac></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mi>n</mi><mo>=</mo><mn>12</mn></math></p></blockquote>

</details>

---

### Q52. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>If the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>(</mo><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math> passes through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>e</mi><mo>,</mo><mo>&#160;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mi>e</mi><mn>4</mn></msup><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi><mo>+</mo><mo>(</mo><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>ln</mi><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>ln</mi><mi>x</mi><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>where</mtext><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>=</mo><mi>ln</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mrow><mn>2</mn><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p>Which is linear differential equation,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac></mrow></msup><mo>=</mo><msqrt><mi>ln</mi><mi>x</mi></msqrt></math></p><p>Now, solution of the equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msqrt><mi>ln</mi><mi>x</mi></msqrt><mo>=</mo><mo>&#8747;</mo><mfrac><msqrt><mi>ln</mi><mi>x</mi></msqrt><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msqrt><mi>ln</mi><mi>x</mi></msqrt><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mi>q</mi><mo>.</mo><mo>(</mo><mi>i</mi><mo>)</mo></math> passes through point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>e</mi><mo>,</mo><mo>&#160;</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Hence, solution of differential equation will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mi>ln</mi><mi>x</mi></msqrt><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>ln</mi><mi>x</mi></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Also given, above equation passes through point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msup><mi>e</mi><mn>4</mn></msup><mo>,</mo><mo>&#160;</mo><mi>&#945;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><msqrt><mi>ln</mi><msup><mi>e</mi><mn>4</mn></msup></msqrt><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mrow><mi>ln</mi><msup><mi>e</mi><mn>4</mn></msup></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mfenced><mn>4</mn></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>8</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q53. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>)</mo><mo>=</mo><mn>0</mn></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>=</mo><msup><mi>e</mi><mi>y</mi></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> passes through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mi>a</mi></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msup><mi>e</mi><mrow><mn>2</mn><mi>e</mi></mrow></msup><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><msup><mi>e</mi><mn>2</mn></msup></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msup><mi>e</mi><msqrt><mn>2</mn><mi>e</mi></msqrt></msup><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>2</mn><mi>e</mi><msqrt><mn>2</mn></msqrt></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msup><mi>e</mi><mrow><mn>2</mn><mi>e</mi></mrow></msup><mn>2</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>The given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mi>x</mi><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>y</mi></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>ln</mi><mfenced><mi>x</mi></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>dt</mi><mi>dy</mi></mfrac><mo>-</mo><mi>t</mi><mo>=</mo><msup><mi>e</mi><mi>y</mi></msup></math> which is a linear differential equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mi>d</mi><mi>y</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup></math></p><p>The solution of the differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>&#215;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>d</mi><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mo>=</mo><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>ln</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>y</mi><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>+</mo><mi>c</mi><mo>&#160;</mo><msup><mi>e</mi><mi>y</mi></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>ln</mi><mfenced><mi>a</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>a</mi><mi>a</mi></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></mrow></msup></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q54. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be a solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>y</mi><mo>+</mo><mo>(</mo><mi>x</mi><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><msup><mi>y</mi><mo>&#34;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><msup><mi>y</mi><mo>'</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><mfenced><mrow><mi>x</mi><mi>y</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mi>y</mi><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mfenced><mfrac><mrow><mi>x</mi><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p>Which is a linear differential equation of form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mfenced><mi>x</mi></mfenced><mi>y</mi><mo>=</mo><mi>Q</mi><mfenced><mi>x</mi></mfenced></math></p><p>Now we know that integrating factor will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfenced><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>ln</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi><mo>&#183;</mo><mi>sec</mi><mi>x</mi></math></p><p>Hence, solution of linear differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>&#160;</mo><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>&#160;</mo><mi>sec</mi><mi>x</mi></mrow><mrow><mi>x</mi><mo>&#160;</mo><mi>cos</mi><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>&#160;</mo><mi>sec</mi><mi>x</mi><mo>=</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac><mi>y</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>3</mn></msqrt></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mi>sec</mi><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>=</mo><mi>tan</mi><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>&#160;</mo><mi>sec</mi><mi>x</mi><mo>=</mo><mi>tan</mi><mi>x</mi><mo>+</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now differentiating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>cos</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Now again differentiating we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mi>y</mi><mo>&#34;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>2</mn><msup><mi>y</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced></math></p><p>Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><msup><mi>y</mi><mo>&#34;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><msup><mi>y</mi><mo>&#39;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><msup><mi>y</mi><mo>&#34;</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><msup><mi>y</mi><mo>'</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q55. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>=</mo><mi>exp</mi><mfenced><mrow><msup><mi>x</mi><mi>&#946;</mi></msup><msup><mi>y</mi><mi>&#947;</mi></msup></mrow></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mi>d</mi><mi>y</mi><mo>-</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msqrt><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></msqrt></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given the solution of differential equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mi>x</mi><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mi>&#946;</mi></msup><mo>&#183;</mo><msup><mi>y</mi><mi>&#947;</mi></msup></mrow></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Now calculating the solution of differential equation, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mn>2</mn><mfrac><mrow><mo>d</mo><mi>y</mi></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>d</mo><mi>t</mi></mrow><mrow><mo>d</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mi>x</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dt</mi><mi>dx</mi></mfrac><mo>+</mo><mfrac><mi>t</mi><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Above differential equation is linear in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math></p><p>We know solutions of differential equation of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>dx</mi></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mo>.</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>)</mo></math></p><p>Now calculating, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>Therefore, the solution of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>.</mo><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>&#183;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#183;</mo><mi>x</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><msqrt><mi>ln</mi><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mo>.</mo><mi>ln</mi><mn>2</mn><mo>=</mo><mi>ln</mi><mn>2</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mi>ln</mi><mn>2</mn></math></p><p>Hence, solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>ln</mi><mn>2</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>ln</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mi>x</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>x</mi><mo>&#183;</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>On comparing equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#946;</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#947;</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q56. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo><mi mathvariant="normal">&#8477;</mi><mo>&#8594;</mo><mi mathvariant="normal">&#8477;</mi></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>+</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>2</mn></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math></p><p>Now, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>+</mo><msup><mi>f</mi><mo>'</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mi>k</mi></math></p><p>This is a linear differential equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Solution of the given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>k</mi><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>k</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mi>C</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math>, so</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>k</mi><msup><mi>e</mi><mi>x</mi></msup><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>k</mi><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>t</mi></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mn>0</mn><mn>2</mn></msubsup><mfenced close="]" open="["><mrow><mi>k</mi><mo>+</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><msubsup><mfenced close="]" open="["><mrow><mi>k</mi><mi>t</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup></mrow></mfenced><mn>0</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>2</mn><mi>k</mi><mo>-</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>k</mi></mrow></mfenced><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>f</mi><mfenced><mn>0</mn></mfenced><mo>-</mo><mi>f</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q57. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>x</mi><mi>sec</mi><mi>x</mi><mo>,</mo><mo>&#160;&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mrow><mi>e</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mi mathvariant="normal">e</mi></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow><mi mathvariant="normal">e</mi></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mn>2</mn><mrow><mi mathvariant="normal">e</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mrow><mi>e</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>x</mi><mi>sec</mi><mi>x</mi></math></p><p>This is a linear differential equation.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>sec</mi><mi>x</mi></math></p><p>Then solution of differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mi>tan</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mi>tan</mi><mi>x</mi><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>x</mi><mi>tan</mi><mi>x</mi><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>sec</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mi>tan</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>sec</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mfenced><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>-</mo><mi>ln</mi><mfenced><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>ln</mi><mfenced><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mi>ln</mi><mfenced><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac></mfenced><mo>-</mo><mi>ln</mi><mi>e</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>12</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>2</mn><mrow><mi>e</mi><msqrt><mn>3</mn></msqrt></mrow></mfrac></mfenced></math></p><p> </p>

</details>

---

### Q58. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>6</mn></msup></msqrt></mfrac></math> pass through the origin. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is equal to:</p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mfrac><mrow><mn>4</mn><mo>-</mo><mi>&#960;</mi></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mfrac><mrow><mi>&#960;</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>&#960;</mi></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mfrac><mrow><mn>4</mn><mo>+</mo><mi>&#960;</mi></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>exp</mi><mfenced><mfrac><mrow><mn>4</mn><mo>-</mo><mi>&#960;</mi></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Given differential equation is<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mfenced><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mfenced open="{" close="}"><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>6</mn></msup></msqrt></mfrac></mfenced></msup></math></p><p>This is a linear differential equation of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi></math>.</p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfenced><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>u</mi><mo>&#8658;</mo><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>u</mi><mi>tan</mi><mi>u</mi></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>u</mi></msqrt></mfrac><mi>d</mi><mi>u</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>u</mi><mi>tan</mi><mi>u</mi></mrow><mrow><mi>sec</mi><mi>u</mi></mrow></mfrac><mi>d</mi><mi>u</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mi>u</mi><mi>sin</mi><mi>u</mi><mi>d</mi><mi>u</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced open="[" close="]"><mrow><mo>-</mo><mi>u</mi><mi>cos</mi><mi>u</mi><mo>+</mo><mo>&#8747;</mo><mi>cos</mi><mi>u</mi><mi>d</mi><mi>u</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mi>u</mi><mi>cos</mi><mi>u</mi><mo>-</mo><mi>sin</mi><mi>u</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mfenced open="{" close="}"><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mfenced><mfrac><mn>1</mn><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced><mo>-</mo><mfenced><mfrac><msup><mi>x</mi><mn>3</mn></msup><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></mrow></mfenced></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mfenced open="{" close="}"><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup></math></p><p>Solution of differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></msup><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><msup><mi>e</mi><mfenced><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup><mo>&#183;</mo><msup><mi>e</mi><mfenced><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>x</mi><mn>3</mn></msup></mfenced><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mfenced open="{" close="}"><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mfenced open="{" close="}"><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>C</mi></math></p><p>Also, it passes through the origin then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mfenced open="{" close="}"><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow><msqrt><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>6</mn></msup></msqrt></mfrac></mfenced></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><msup><mi>e</mi><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mn>1</mn></mfenced><mo>-</mo><mn>1</mn></mrow><msqrt><mn>2</mn></msqrt></mfrac></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><msup><mi>e</mi><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><msup><mi>e</mi><mfenced><mfrac><mrow><mi mathvariant="normal">&#960;</mi><mo>-</mo><mn>4</mn></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>e</mi><mfrac><mrow><mn>4</mn><mo>-</mo><mi>&#960;</mi></mrow><mrow><mn>4</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></msup></math></p>

</details>

---

### Q59. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math>  be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>,</mo><mo>(</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>)</mo></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>e</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>ln</mi><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>ln</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mrow><mi>x</mi><mi>ln</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi></math></p><p>This is a linear differential equation.</p><p>Now, finding integrating factor we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>xlnx</mi></mfrac><mi>dx</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mi>ln</mi><mfenced><mi>lnx</mi></mfenced></mrow></msup><mo>=</mo><mi>lnx</mi></math></p><p>Now, solution of the differential equation is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi mathvariant="normal">x</mi><mo>&#215;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mi>ln</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>xlnx</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mi>ln</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>&#183;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mi>ln</mi><mn>2</mn><mo>=</mo><mi>ln</mi><mn>2</mn><mo>&#183;</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>So, equation will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>ln</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mi>x</mi><mo>&#183;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>e</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>ln</mi><mi>e</mi><mo>=</mo><mi>ln</mi><mi>e</mi><mo>&#183;</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>1</mn><mo>&#183;</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow><mn>4</mn></mfrac></math></p>

</details>

---

### Q60. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">f</mi><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>d</mi><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mi>e</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>e</mi></mfrac></math></p><p> </p>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi>d</mi><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mi>y</mi></mfrac></math></p><p>Now integrating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi><mo>+</mo><mi>c</mi></math></p><p>Now on using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mi>e</mi></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>So, the equation of curve becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>y</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><msup><mi>e</mi><mrow><mi>ln</mi><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>2</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8734;</mo></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math>.</p>

</details>

---

### Q61. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>t</mi></mfenced></math> be a solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>=</mo><mi>&#947;</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>&#946;</mi><mi>t</mi></mrow></msup></math> Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>&#62;</mo><mn>0</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mo>Lim</mo><mrow><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></msub><mo>&#160;</mo><mi>y</mi><mfenced><mi>t</mi></mfenced></math>

**Options:**

- **(A)** is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** does not exist
- **(C)** is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><mi>&#945;</mi><mi>y</mi><mo>=</mo><mi>&#947;</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#946;</mi><mi>t</mi></mrow></msup></math></p><p>Which is a linear differential equation,</p><p>So, integrating factor will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>&#945;</mi><mi>d</mi><mi>t</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>t</mi></mrow></msup></math></p><p>So, the solution of differential equation is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>t</mi></mrow></msup><mo>=</mo><mi>&#947;</mi><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#946;</mi><mi>t</mi></mrow></msup><mo>&#215;</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>t</mi></mrow></msup><mo>=</mo><mi>&#947;</mi><mo>&#8747;</mo><msup><mi>e</mi><mrow><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mi>t</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mi>&#945;</mi><mi>t</mi></mrow></msup><mo>=</mo><mi>&#947;</mi><mfrac><msup><mi>e</mi><mrow><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mi>t</mi></mrow></msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>&#947;</mi><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>&#946;</mi><mi>t</mi></mrow></msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mfrac><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi><mi>t</mi></mrow></msup></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>y</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>y</mi><mo>=</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mi>&#947;</mi><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>&#946;</mi><mi>t</mi></mrow></msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></mfrac><mo>+</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>&#945;</mi><mi>t</mi></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>y</mi><mo>=</mo><mi>&#947;</mi><mo>&#215;</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>&#215;</mo><mn>0</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8734;</mo></mrow></msup><mo>&#8594;</mo><mn>0</mn></mrow></mfenced></math></p>

</details>

---

### Q62. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">y</mi><mfenced><mi mathvariant="normal">x</mi></mfenced></math>  be the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced></mrow></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup><mo>(</mo><mi mathvariant="normal">x</mi><mo>)</mo></mrow><mn>9</mn></mfrac></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>5</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mo>-</mo><mn>3</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>2</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>7</mn><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>5</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given differential equation can be rewritten as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><msup><mi>y</mi><mn>3</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi mathvariant="normal">y</mi><mn>3</mn></msup></mfrac><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mi>xy</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi mathvariant="normal">x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi mathvariant="normal">y</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">t</mi><mo>&#8658;</mo><mfrac><mn>2</mn><msup><mi mathvariant="normal">y</mi><mn>3</mn></msup></mfrac><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>=</mo><mfrac><mi>dt</mi><mi>dx</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mi>dt</mi><mrow><mn>2</mn><mi>dx</mi></mrow></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">t</mi><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi mathvariant="normal">x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>dt</mi><mi>dx</mi></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">t</mi></mrow><mi mathvariant="normal">x</mi></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi mathvariant="normal">x</mi></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>We know the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>ye</mi><mrow><mo>&#8747;</mo><mi>Pdx</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>Qe</mi><mrow><mo>&#8747;</mo><mi>Pdx</mi></mrow></msup><mo>+</mo><mi mathvariant="normal">C</mi><mo>&#160;</mo><mo>&#160;</mo><mo>(</mo><mi>Where</mi><mo>&#160;</mo><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mi>Pdx</mi></mrow></msup><mo>)</mo></math></p><p>Therefore, on solving equation(1) we get,</p><p>I.F.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></mfenced><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mfrac><mn>5</mn><mn>9</mn></mfrac></math></p><p>Now putting value of C in equation(2) we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>y</mi><mn>2</mn></msup><mn>9</mn></mfrac><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>5</mn><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mfenced><mrow><mn>2</mn><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mrow></mfrac></math></p>

</details>

---

### Q63. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>&#160;</mo><mi>d</mi><mi>y</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>(</mo><mi>x</mi><mi>y</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mi>d</mi><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#62;</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>3</mn><mo>-</mo><mi>e</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><mi>e</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mfenced><mrow><mi>x</mi><mi>y</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mi>y</mi></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mo>-</mo><mfrac><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></math></p><p>This is a linear differential equation.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IF</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup></math></p><p>Solution of a given linear differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mo>-</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>t</mi><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mi>t</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>+</mo><mi>C</mi><msup><mi>e</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn><mo>+</mo><mo>&#160;</mo><mi>C</mi><msup><mi>e</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, then </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mi>e</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mi>C</mi><msup><mi>e</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mfenced><msup><mi>e</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></msup></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q64. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mfrac><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo><mi>x</mi><mo>&#62;</mo><mo>-</mo><mn>1</mn></math>, which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><mi></mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>&#215;</mo><mi>p</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>q</mi><mfenced><mi>x</mi></mfenced></math>
We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfrac></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>6</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p>Now finding the integration we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>p</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow></mfenced><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle><mstyle displaystyle="true"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mstyle></mrow></mfrac></math></p><p>Using partial fraction we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>11</mn><mi>x</mi><mo>+</mo><mn>13</mn></mrow><mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>A</mi><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mi>B</mi><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mi>C</mi><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math></p><p>On solving we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>4</mn><mn>2</mn></mfrac><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>p</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>A</mi><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>B</mi><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>c</mi><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>ln</mi><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>p</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mfrac></math></p><p>Now solution of differential equation is given by</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mfenced><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mfenced><mfrac><mrow><msup><mstyle displaystyle="true"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle><mn>2</mn></msup><mstyle displaystyle="true"><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle></mrow><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Now given curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#215;</mo><mfenced><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>0</mn><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle><mrow><mn>0</mn><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><msup><mn>0</mn><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>0</mn><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>So, curve becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mfenced><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle><mrow><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mfenced><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><msup><mn>1</mn><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>1</mn><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><mn>3</mn><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q65. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> pass through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><msup><mi>e</mi><mi>x</mi></msup><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mfenced><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now on rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></math></p><p>We can see it is a linear differential equation,</p><p>So integrating factor is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>&#8747;</mo><mn>1</mn><mo>&#183;</mo><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p>So solution will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>&#215;</mo><mi>I</mi><mi>F</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac><mo>&#215;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now as curve is passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> so </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p><p>Now calculating the limit <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>=</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msup><mi>e</mi><mi>x</mi></msup></mfenced><mo>+</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q66. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>y</mi><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>1</mn></math> passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><msqrt><mfrac><mn>1</mn><mn>3</mn></mfrac></msqrt></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>7</mn></msqrt><mi mathvariant="normal">y</mi><mfenced><mn>8</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>+</mo><mn>6</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>-</mo><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>-</mo><mn>6</mn><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>-</mo><mn>6</mn><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msup><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></math> is a linear differential equation.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mfenced></mrow></msup><mo>=</mo><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt></math></p><p>General solution will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>2</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p>So, the equation of the curve is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></msqrt><mo>=</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>ln</mi><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msqrt><mn>7</mn></msqrt><mi>y</mi><mfenced><mn>8</mn></mfenced></mrow><mn>3</mn></mfrac><mo>=</mo><mn>8</mn><mo>-</mo><mn>4</mn><mi>ln</mi><mn>3</mn><mo>+</mo><mn>2</mn><mi>ln</mi><mn>3</mn><mo>-</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msqrt><mn>7</mn></msqrt><mi>y</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mn>19</mn><mo>-</mo><mn>6</mn><mi>ln</mi><mn>3</mn></math></p></blockquote>

</details>

---

### Q67. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> be the solution curve of the differential equation</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>8</mn><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>,</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#960;</mi></mrow></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>8</mn><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mn>4</mn><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced></math> </p><p>Now rewriting the given differential equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>8</mn><mo>+</mo><mn>4</mn><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></msup></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced></math></p><p>Which is a linear differential equation.</p><p>Now calculating  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mfenced><mrow><mn>8</mn><mo>+</mo><mn>4</mn><mi>cot</mi><mn>2</mn><mi mathvariant="normal">x</mi></mrow></mfenced><mi>dx</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>8</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>ln</mi><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mn>8</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></math></p><p>Now solution of differential equation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac><mo>&#215;</mo><mi>I</mi><mi>F</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>8</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mn>2</mn><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mfenced><mrow><mn>2</mn><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><msup><mi>e</mi><mrow><mn>8</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mn>4</mn><mi>x</mi></mrow></msup><mo>&#183;</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>&#960;</mi></mrow></msup><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>So, the equation of curve is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mi>x</mi></mrow></msup><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p>So, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>4</mn><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></msup><mrow><mi>sin</mi><mfenced><mrow><mn>2</mn><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><msqrt><mn>3</mn></msqrt></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></msup></math></p></blockquote>

</details>

---

### Q68. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> be two distinct solutions of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mi>y</mi></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math> respectively. Then, the number of points of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msub><mi>y</mi><mn>2</mn></msub><mfenced><mi>x</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><mi>x</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mn>1</mn><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p>Now solution is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>-</mo><mi>x</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>+</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub><mo>-</mo><msub><mi>y</mi><mn>1</mn></msub><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>y</mi><mn>2</mn></msub><mo>&#8800;</mo><msub><mi>y</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Number of points of intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mn>2</mn></msub></math> is zero.</p></blockquote>

</details>

---

### Q69. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution curve to the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is finite. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are respectively the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>-</mo></math>intercept of the tangent to the curve at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mo>=</mo><mn>2</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p>Linear differential equation,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>&#160;</mo><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mi>dx</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">x</mi></mrow></msup></math></p><p>Now solution of differential equation is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><mo>&#215;</mo><mi>I</mi><mi>F</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mo>-</mo><mn>2</mn><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>+</mo><mi>C</mi><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mi>y</mi></math> is finite</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><mo>&#8734;</mo></mrow></munder><mfenced><mrow><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mn>2</mn></mfrac><mo>+</mo><mi>C</mi><mo>&#183;</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>&#8594;</mo></math>finite</p><p>This is possible only when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>Hence<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mn>2</mn></mfrac></math></p><p>Now finding the slope <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="right"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></menclose><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></msub><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>m</mi><mo>,</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>Now equation of tangent will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>x-intercept <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>,</mo></math> y-intercept <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>4</mn><mi>b</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q70. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> pass through the origin. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mrow><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mi>y</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math> is a linear differential equation.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>ln</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math>$\quad \because x \in(-1,1)$</p><p>So, solution of the differential equation is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mo>&#183;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><msup><mi>x</mi><mn>5</mn></msup><mn>5</mn></mfrac><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>C</mi></math></p><p>Since the curve passes through origin</p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>5</mn></msup><mrow><mn>5</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p></blockquote><blockquote><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>x</mi><mn>5</mn></msup><mrow><mn>5</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>5</mn></msup><mrow><mn>5</mn><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfrac></math> is an odd function and<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math>  is an even function)</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac><mi>d</mi><mi>x</mi></math></p><p>Assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>t</mi><mi>d</mi><mi>t</mi><mo>=</mo><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mi>t</mi><mi>d</mi><mi>t</mi></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></mrow><mi>t</mi></mfrac><mfenced><mrow><mo>-</mo><mfrac><mi>t</mi><msqrt><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mo>&#8747;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mi>t</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>t</mi><mn>2</mn></msup></msqrt><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>t</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><msqrt><mn>3</mn></msqrt></mrow><mn>2</mn></mfrac><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msubsup><mfenced close="]" open="["><mrow><mo>-</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mn>0</mn><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sin</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>4</mn></mfrac></math></p></blockquote>

</details>

---

### Q71. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>, then the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>We know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mfenced><mrow><mn>2</mn><mi>tan</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mi>sin</mi><mi>x</mi></math> is a linear differential equation so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p>The general solution will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>sin</mi><mi>x</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>sec</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Hence the particular solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mi>sec</mi><mi>x</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>-</mo><mn>2</mn><msup><mfenced><mrow><mi>cos</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p>So, the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p></blockquote>

</details>

---

### Q72. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math>, be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>4</mn></msup></mrow><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mi>&#945;</mi></msup><mo>+</mo><mn>1</mn></mrow><mrow><mi>&#946;</mi><msup><mi>e</mi><mi>&#945;</mi></msup></mrow></mfrac></math>. then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>&#183;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>&#215;</mo><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p>Solution will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mo>&#215;</mo><mi>I</mi><mo>.</mo><mi>F</mi></math></p><p>Solving above with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>4</mn></msup></mrow><mrow><mn>2</mn><msup><mi>e</mi><mn>4</mn></msup></mrow></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mfenced open="[" close="]"><mfrac><mrow><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></mrow></mfrac></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>8</mn><msup><mi>e</mi><mn>6</mn></msup></mrow></mfrac></math>, now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>3</mn></mfenced><mo>=</mo><mfrac><mrow><msup><mi>e</mi><mi>&#945;</mi></msup><mo>+</mo><mn>1</mn></mrow><mrow><mi>&#946;</mi><msup><mi>e</mi><mi>&#945;</mi></msup></mrow></mfrac></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q73. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msqrt><mn>2</mn></msqrt><mi>y</mi></mrow><mrow><mn>2</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>32</mn></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mi>&#945;</mi></mfenced></mrow></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><msqrt><mn>2</mn></msqrt><mrow><mn>2</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mi>y</mi><mo>=</mo><mi>x</mi><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p>This is a linear differential equation.</p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mfenced><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mstyle><mo>+</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>&#8747;</mo><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mn>2</mn><mi>x</mi></mrow></mfrac></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mn>2</mn><mi>x</mi><mo>=</mo><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfrac><mrow><mi>tan</mi><mn>2</mn><mi>x</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mfrac><mrow><mi>tan</mi><mn>2</mn><mi mathvariant="normal">x</mi></mrow><msqrt><mn>2</mn></msqrt></mfrac></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p>So general solution will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mrow><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>x</mi><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup><msup><mi>e</mi><mrow><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>e</mi><mrow><msup><mi>cot</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></msup><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>32</mn></mfrac><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mn>2</mn><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>&#945;</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>&#945;</mi></mrow></msup><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><mrow><msqrt><mn>2</mn></msqrt><mi>cot</mi><mfrac><mrow><mn>2</mn><mi>&#960;</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt></mfenced></mrow></msup></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><msqrt><mfrac><mn>2</mn><mn>3</mn></mfrac></msqrt><mo>&#8658;</mo><mn>3</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q74. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>3</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>18</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><mi>y</mi><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mfrac></math></p><p>This is a linear differential equation of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mfrac><mi>dt</mi><mi mathvariant="normal">t</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>ln</mi><mi>t</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mi>t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></math></p><p>So the general solution of the differential equation will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mo>&#215;</mo><mi>I</mi><mi>F</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mn>3</mn></msup></mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></math></p><p>Substituting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mi>z</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>d</mi><mi>z</mi></mrow><msup><mi>z</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mi>z</mi></mfrac></mrow></mfenced><mo>+</mo><mi>c</mi><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p>Hence the solution of the differential equation becomes </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>-</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>3</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Hence the particular solution will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mn>1</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mrow><mn>3</mn><mo>-</mo><mn>27</mn></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>-</mo><mn>9</mn></mrow></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mrow><mo>-</mo><mn>24</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>y</mi><mn>24</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfenced><mrow><mo>-</mo><mn>24</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>18</mn></math></p>

</details>

---

### Q75. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math>
and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>y</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>k</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **320**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow></mfenced><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn></mrow><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>IF</mi><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>&#183;</mo><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></msqrt><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></math></p><p>So,required value <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mo>&#8747;</mo><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mfenced><mrow><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#183;</mo><mn>2</mn><msubsup><mo>&#8747;</mo><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><msup><mi>x</mi><mn>4</mn></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><msubsup><mfenced><msup><mi>x</mi><mn>5</mn></msup></mfenced><mn>0</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>320</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>320</mn></math></p>

</details>

---

### Q76. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></mfenced><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math> then the abscissa of the point on the curve whose ordinate is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mn>1</mn></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>e</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mi>e</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>e</mi></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>x</mi><mo>=</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>I.F. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>y</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></math></p><p>General solution will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup><mo>&#215;</mo><mfrac><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfrac><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mfenced><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mfenced><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></mfenced><mo>-</mo><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup><mo>+</mo><mi>C</mi></math></p><p>Since the curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>C</mi><mo>=</mo><mn>2</mn></math></p><p>So, the curve reduces to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></mfenced><mo>=</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mfenced><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup></mfenced><mo>-</mo><msup><mi>e</mi><mrow><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi></mrow></msup><mo>+</mo><mn>2</mn></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>tan</mi><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mn>1</mn><mfenced><mi>e</mi></mfenced><mo>-</mo><mi>e</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mi>e</mi></mfrac></math></p>

</details>

---

### Q77. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn></mrow></mfenced><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p>It is linear differential equation so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>2</mn><mo>&#8747;</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mi>d</mi><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>2</mn><mfenced close="]" open="["><mrow><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup></math></p><p>Now solution is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>&#215;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><msup><mi>e</mi><mrow><mn>2</mn><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>&#215;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math></p><p>Now let  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>=</mo><mi>t</mi></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mo>+</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>t</mi></msup><mo>&#215;</mo><mi>t</mi><mo>&#215;</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mi>t</mi></msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Now at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#215;</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mfenced><mrow><mn>0</mn><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mi>c</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn></math> we get the equation as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></mrow></msup><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> in equation we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mrow><mfenced><mrow><mn>4</mn><mo>-</mo><mn>4</mn></mrow></mfenced><msup><mi>e</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mfenced><mrow><mn>4</mn><mo>-</mo><mn>4</mn></mrow></mfenced><msup><mi>e</mi><mn>2</mn></msup></mrow></msup><mfenced><mrow><mfenced><mrow><mn>4</mn><mo>-</mo><mn>4</mn></mrow></mfenced><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#215;</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><msup><mi>e</mi><mn>0</mn></msup><mfenced><mrow><mfenced><mn>0</mn></mfenced><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q78. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mi>x</mi><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math> then the local maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mi>e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mi>e</mi></mfrac><mo>-</mo><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mi>e</mi></mfrac><mo>-</mo><mi>e</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mi>x</mi></mfrac><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>ln</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> General solution: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mi>d</mi><mi>x</mi></math></p><p>We know that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>e</mi><mi>x</mi></msup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><msup><mi>f</mi><mo>&#39;&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>-</mo><msup><mi>f</mi><mo>&#39;&#39;&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mfenced open=""><mrow><mo>+</mo><mo>&#8943;</mo><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><msup><mi>f</mi><mi>n</mi></msup><mfenced><mi>x</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced><mn>0</mn></mfenced><mfenced><mn>1</mn></mfenced><mo>=</mo><msup><mi>e</mi><mn>1</mn></msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mfenced><mn>1</mn></mfenced><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mo>=</mo><mfrac><msup><mi>e</mi><mi>x</mi></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>e</mi></math>     (from eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mfrac><msup><mi>e</mi><mi>x</mi></msup><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>e</mi><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mi>e</mi><mo>-</mo><msup><mi>e</mi><mi>x</mi></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>x</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced close="]" open="["><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
To find local maxima, put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>z</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>x</mi></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>e</mi><mi>x</mi></msup><mo>&#62;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mi>x</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fac5d3d8-0ca7-4c9f-afbe-28e56422d7b3-image.png" style="width: 331px; height: 50px;" /></p><p>It is clear from the sign scheme method, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mfenced><mi>x</mi></mfenced></math> has local maximum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> and has local minimum value at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  The local maximum value is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>e</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mi>e</mi></mfrac><mo>-</mo><mi>e</mi></math></p>

</details>

---

### Q79. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the solution curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math> pass through the origin. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>6</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>6</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac></math></p><p>This is of the form of linear differential equation</p><p>I.F. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mn>6</mn><mi>x</mi></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></msup><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac></math></p><p>So the solution of the differential equation will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><mfrac><mn>1</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>8</mn><mi>x</mi></mrow><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>=</mo><mi>t</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><msup><mi>t</mi><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>Since the curve passes through origin <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>16</mn></mrow></mfrac><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>32</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>32</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn></mrow></mfenced><mn>3</mn></msup><mn>32</mn></mfrac></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mo>-</mo><mfrac><mn>8</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>8</mn></mrow><mn>32</mn></mfrac><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q80. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mfrac><mi>e</mi><mn>3</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>1</mn></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><mn>3</mn><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p>Dividing by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><mi>p</mi><mo>,</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mi>d</mi><mi>p</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mfenced><mi>p</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>General solution will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mn>3</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mn>3</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi>ln</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>y</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mfrac><mi>e</mi><mn>3</mn></mfrac><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>ln</mi><mi>x</mi><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> is the particular solution.</p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>;</mo><mo>&#160;&#160;</mo><mi>y</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q81. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>x</mi><mfenced><mi>y</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mo>&#160;</mo><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>y</mi></msup><mo>,</mo><mi>x</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>0</mn></math>; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mi>e</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mi>e</mi></msup><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mfenced><mrow><msup><mi>e</mi><mi>e</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>e</mi></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mi>e</mi></msup><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>3</mn></msup><mfenced><mrow><msup><mi>e</mi><mi>e</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mi>y</mi></mfrac><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>y</mi></msup></math>   </p><p>Finding integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mo>&#8722;</mo><mn>2</mn></mrow><mi>y</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8722;</mo><mn>2</mn><mi>ln</mi><mi>y</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><msup><mi>y</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mi>y</mi></msup><mi>d</mi><mi>y</mi></math>   </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mi>e</mi><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mi>e</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>y</mi><msup><mi>e</mi><mi>y</mi></msup><mo>-</mo><mi>e</mi></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>e</mi></math> in the equation we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><msup><mi>e</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>e</mi><mo>.</mo><msup><mi>e</mi><mi>e</mi></msup><mo>-</mo><mi>e</mi></math></p><p>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mfenced><mrow><msup><mi>e</mi><mi>e</mi></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math> </p>

</details>

---

### Q82. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>y</mi><mo>+</mo><mfenced><mrow><mi>y</mi><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mi mathvariant="normal">e</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mi mathvariant="normal">e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><mi mathvariant="normal">e</mi></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mi mathvariant="normal">e</mi></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mi mathvariant="normal">e</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>&#183;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;Let&#160;</mtext><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mi>x</mi></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mo>&#8747;</mo><mo>-</mo><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mo>&#183;</mo><mi>d</mi><mi>t</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mi>t</mi><msup><mi>e</mi><mi>t</mi></msup><mo>-</mo><msup><mi>e</mi><mi>t</mi></msup></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;Put&#160;</mtext><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mn>1</mn></mfrac><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">C</mi><mo>=</mo><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>e</mi><mfrac><mn>1</mn><mi>x</mi></mfrac></msup><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;At&#160;</mtext><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><msup><mi>e</mi><mn>2</mn></msup><mi>e</mi></mfrac><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>3</mn><mo>-</mo><mi>e</mi></math></p>

</details>

---

### Q83. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>10</mn><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>, passes through the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mi>&#946;</mi><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> is a root of the equation?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Given that: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>&#8722;</mo><mn>10</mn><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mn>10</mn><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mi>y</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mn>10</mn><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mtext>&#160;I.F.&#160;</mtext><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mo>&#8747;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>x</mi><mo>&#8901;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mo>&#8747;</mo><mn>10</mn><msup><mi>y</mi><mn>4</mn></msup><mi>d</mi><mi>y</mi><mo>+</mo><mi>C</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>x</mi><mo>&#8901;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>5</mn></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Put</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mspace width="1em"/><mi>c</mi><mo>=</mo><mo>&#8722;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>x</mi><mo>&#8901;</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>5</mn></msup><mo>&#8722;</mo><mn>2</mn></math></p><p>Passing Through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>,</mo><mi>&#946;</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mn>2</mn><mo>&#8901;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><msup><mi>&#946;</mi><mn>5</mn></msup><mo>&#8722;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><msup><mi>&#946;</mi><mn>5</mn></msup><mo>&#8722;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>&#8722;</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>
root of the equations
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>5</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q84. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mi>y</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mi>x</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>7</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>&#960;</mi><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><msup><mi>e</mi><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></msup><mo>+</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></msup><mo>+</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></msup><mo>+</mo><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>e</mi><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></msup><mo>+</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup></msup><mo>+</mo><mn>5</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mi>x</mi><mo>-</mo><mn>2</mn><mi>cos</mi><mo>&#160;</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mfenced><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><mn>2</mn><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mn>2</mn><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfenced><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mfenced><mrow><mn>5</mn><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>5</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mi>x</mi><mo>+</mo><mi>C</mi><mo>&#183;</mo><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></math></p><p>Given at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mo>=</mo><mn>5</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>5</mn><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>e</mi><msup><mi>x</mi><mn>2</mn></msup></msup></math></p><p>Now at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>5</mn><mo>+</mo><mn>2</mn><msup><mi>e</mi><msup><mi>&#960;</mi><mn>2</mn></msup></msup></math></p>

</details>

---

### Q85. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let us consider a curve, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and the slope of the tangent to the curve at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mi>x</mi><msup><mi>f</mi><mo>&#39;</mo></msup><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>.</mo></math> Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>12</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>Solution of differential equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>&#183;</mo><mi>x</mi><mo>&#160;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p>Passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>, So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn><mo>=</mo><mo>-</mo><mn>8</mn><mo>+</mo><mn>3</mn><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mn>3</mn><mi>x</mi><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn></math></p><p>i.e <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>&#183;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>&#160;</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q86. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi>y</mi><mo>+</mo><mfenced><mrow><msup><mi mathvariant="normal">e</mi><mi>y</mi></msup><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi mathvariant="normal">e</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mo>(</mo><mn>2</mn><mi mathvariant="normal">e</mi><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mi>y</mi></msup></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mo>=</mo><mi>t</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>t</mi><mi>x</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><msubsup><mo>=</mo><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msubsup><mo>=</mo><msup><mi>e</mi><mrow><mi>l</mi><mi>n</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>&#183;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#8467;</mi><mi>n</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>e</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mi>y</mi></mrow></msup><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>(</mo><mn>1</mn><mo>+</mo><mi>&#8467;</mi><mi>n</mi><mi>x</mi><mo>)</mo></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>&#8467;</mi><mi>n</mi><mn>2</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>&#160;</mo></math></p>

</details>

---

### Q87. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be a solution curve of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>x</mi><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>+</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>d</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>tan</mi><mi>x</mi><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mi>tan</mi><mi>x</mi><mo>=</mo><mo>-</mo><mi>y</mi><mi>cot</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mfenced><mrow><mi>tan</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mi>tan</mi><mi>x</mi></math></p><p>This is a linear differential equation of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mfenced><mi>x</mi></mfenced><mi>y</mi><mo>=</mo><mi>Q</mi><mfenced><mi>x</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;I.F&#160;</mtext><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>(</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mi>cot</mi><mi>x</mi><mo>)</mo><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfenced><mfrac><mrow><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>tan</mi><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfenced><mfrac><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mi>tan</mi><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>tan</mi><mi>x</mi><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p>Solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mi>x</mi><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mfenced><mfrac><mi>x</mi><mrow><mi>tan</mi><mi>x</mi></mrow></mfrac></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>(</mo><mn>0</mn><mo>-</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>Then the function is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>x</mi><mo>-</mo><mi>tan</mi><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mi>tan</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><mi>tan</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q88. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be solution of the following differential equation </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><msup><mi>e</mi><mi>y</mi></msup><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>(</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>)</mo></math> is equal to <u>           </u>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mo>=</mo><mi>t</mi><mo>&#8658;</mo><msup><mi>e</mi><mi>y</mi></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mi>y</mi></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>2</mn><msup><mi>e</mi><mi>y</mi></msup><mi>sin</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>t</mi><mo>=</mo><mo>-</mo><mi>sin</mi><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p>So, the integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup></math></p><p>So, the solution of differential equation is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>&#183;</mo><mfenced><mrow><mo>-</mo><mi>sin</mi><mi>x</mi><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mi>y</mi></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>z</mi></mrow></msup><mo>&#183;</mo><msup><mi>z</mi><mn>2</mn></msup><mo>&#160;</mo><mi>d</mi><mi>z</mi></math>  (Assume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>cos</mi><mi>x</mi><mo>&#8658;</mo><mi>d</mi><mi>z</mi><mo>=</mo><mo>-</mo><mi>sin</mi><mi>x</mi></math>)</p><p>Using integration by parts,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">e</mi><mi>y</mi></msup><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><msup><mi>z</mi><mn>2</mn></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>z</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>z</mi><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>z</mi></mrow></msup><mo>+</mo><mfrac><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>z</mi></mrow></msup><mn>4</mn></mfrac><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">e</mi><mi>y</mi></msup><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mi>x</mi><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mo>+</mo><mfrac><msup><mi mathvariant="normal">e</mi><mrow><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup><mn>4</mn></mfrac><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p>at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">e</mi><mi>y</mi></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>cos</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#183;</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi></mrow></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>log</mi><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q89. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>,</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>y</mi><mo>+</mo><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><msup><mo>cosec</mo><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>d</mi><mi>x</mi><mo>=</mo><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>2</mn><mi>x</mi><mo>=</mo><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>x</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>=</mo><mi>y</mi><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mi>cos</mi><mn>2</mn><mi>x</mi></math></p></blockquote><blockquote><p>This is a linear differential equation of the type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8201;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi></math> are the functions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> or constants.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mo>-</mo><mi>cos</mi><mn>2</mn><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>cos</mi><mn>2</mn><mi>x</mi></math></p><p>Now, we have integrating factor I.F.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mi>c</mi><mi>o</mi><mi>s</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup></math></p><p>And, the solution of the given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi>cos</mi><mn>2</mn><mi>x</mi></mrow></mfenced><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mi>t</mi><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>cos</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mstyle></mfenced></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>2</mn><mi>x</mi></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>0</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mfrac><mrow><mi>sin</mi><mn>0</mn></mrow><mn>2</mn></mfrac></mfenced></mrow></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>&#183;</mo><msup><mi>e</mi><mn>0</mn></msup><mo>=</mo><mo>-</mo><msup><mi>e</mi><mn>0</mn></msup><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mo>-</mo><mn>1</mn><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>.</mo></math></p></blockquote>

</details>

---

### Q90. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>y</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>&#960;</mi><mo>)</mo><mo>=</mo><mi>&#960;</mi><mo>+</mo><mn>2</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mi>&#960;</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>&#960;</mi></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#960;</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>&#960;</mi></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mi>&#960;</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mi>&#960;</mi></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>y</mi></mtd><mtd><mi>sin</mi><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mi>x</mi></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mo>-</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced close="|" open="|"><mi>A</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>I.F.</mtext><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>Solution is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mfenced><mrow><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>(</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mi>x</mi><mfenced><mrow><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#8747;</mo><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mi>&#960;</mi><mo>+</mo><mn>2</mn></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mi mathvariant="normal">&#960;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi mathvariant="normal">&#960;</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>0</mn><mo>+</mo><mi mathvariant="normal">c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> becomes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></math>, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mi>y</mi><mo>=</mo><msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>&#183;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mi>cos</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>sin</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mi>y</mi><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mi mathvariant="normal">&#960;</mi></mfrac></math></p>

</details>

---

### Q91. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mfenced><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mi>x</mi></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>.</mo><mn>1</mn></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mrow><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mrow><mn>5</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><msup><mi>e</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><msup><mi>e</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><msup><mfenced><mrow><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mi>Y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><mi>d</mi><mi>Y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>Y</mi><mn>2</mn></msup><msup><mi>e</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></msup><mo>-</mo><mi>x</mi><mi>Y</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mi>Y</mi></mfrac><mo>=</mo><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>k</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>k</mi><mfenced><mrow><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>k</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mfenced><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>/</mo><mn>2</mn></mrow></msup></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mi>y</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mi>c</mi><mo>)</mo><msup><mi>e</mi><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><msup><mi>e</mi><mn>2</mn></msup></mfrac></math></p><p>Differentiate equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">i</mi><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo></math> put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></msub><mo>=</mo><mo>-</mo><mfrac><msup><mi>e</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></mfrac></math></p>

</details>

---

### Q92. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mi>y</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>9</mn><mo>/</mo><mn>4</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> which passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>16</mn><mo>)</mo></math> is equal to <gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>3</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Given differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>-</mo><mi>y</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>9</mn><mo>/</mo><mn>4</mn></mrow></msup><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mrow><mn>9</mn><mo>/</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>y</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mrow><mn>9</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>y</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>x</mi><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mrow><mn>9</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow><mrow><mn>2</mn><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mi>y</mi><mrow><mn>2</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mi>x</mi><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p>This is a linear differential equation of the type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><mi>x</mi><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p>Now, we have integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><msub><mi>log</mi><mi>e</mi></msub><msup><mi>x</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></mrow></msup><mo>=</mo><msup><mi>x</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></msup></math></p><p>Now, the solution of the linear differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mo>&#215;</mo><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>x</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mo>&#8747;</mo><mfrac><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mi>t</mi><mn>4</mn></msup><mo>&#8658;</mo><mi>d</mi><mi>x</mi><mo>=</mo><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>&#183;</mo><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup><mi>d</mi><mi>t</mi></mrow><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mn>4</mn><mo>&#8747;</mo><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mn>4</mn><mo>&#8747;</mo><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi><mo>-</mo><mn>4</mn><mo>&#8747;</mo><mfrac><msup><mi>t</mi><mn>2</mn></msup><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>t</mi><mo>+</mo><mi>C</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mi>u</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mn>3</mn><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi><mo>=</mo><mi>d</mi><mi>u</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mn>4</mn><mo>&#8747;</mo><msup><mi>t</mi><mn>2</mn></msup><mi>d</mi><mi>t</mi><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>u</mi></mrow><mi>u</mi></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mi>u</mi></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>t</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p>Now, the curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msup><mi>x</mi><mrow><mn>5</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><msqrt><mi>x</mi></msqrt><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><msup><mi>x</mi><mrow><mn>3</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfrac><msqrt><mi>x</mi></msqrt><mn>3</mn></mfrac></math></p><p>Hence, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>16</mn><mo>,</mo></math> we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>16</mn><mo>)</mo><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>32</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><msub><mi>log</mi><mi>e</mi></msub><mn>9</mn><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>16</mn></mfenced><mo>=</mo><mfrac><mn>124</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>32</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mn>16</mn></mfenced><mo>=</mo><mn>4</mn><mfenced><mrow><mfrac><mn>31</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>3</mn></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q93. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>y</mi><mi>sin</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>9</mn></mrow><mn>6</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>10</mn></mrow><mn>11</mn></mfrac></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>8</mn></mrow><mn>4</mn></mfrac></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>10</mn></mrow><mn>11</mn></mfrac></mfenced></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>y</mi><mi>sin</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>)</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>y</mi><mi>sin</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>)</mo></mrow><mrow><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi><mi>sin</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>)</mo></mrow><mrow><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mo>(</mo><mi>tan</mi><mi>x</mi><mo>)</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mi>cos</mi><mi>x</mi></mrow></mfrac></math></p><p>This is a linear differential equation of the type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mo>-</mo><mi>tan</mi><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi><mfenced><mrow><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>.</mo></math></p><p>Now, the integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo>-</mo><mi>tanxdx</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mi>ln</mi><mfenced close="|" open="|"><mi>cosx</mi></mfenced></mrow></msup><mo>=</mo><mfenced close="|" open="|"><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>cos</mi><mi>x</mi><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>.</mo></math></p><p>The solution of the given differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mo>(</mo><mi>cos</mi><mi>x</mi><mo>)</mo><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi><mo>(</mo><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mn>3</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>tan</mi><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mstyle><mo>+</mo><mn>3</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mstyle displaystyle="true"><mn>6</mn><mi>tan</mi><mfrac><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mn>1</mn><mo>-</mo><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mstyle displaystyle="true"><mi>x</mi></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mstyle><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><msup><mi>tan</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfenced><mrow><mn>2</mn><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>6</mn><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>4</mn></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mo>&#8747;</mo><mfrac><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfenced><mrow><mn>2</mn><mfenced><mrow><msup><mi>tan</mi><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>3</mn><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>sec</mi><mn>2</mn></msup><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><msup><mi>t</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mfenced><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><mi>t</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mfenced><mfrac><mrow><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>1</mn></mrow><mrow><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced></mfenced></math></p><p>So, the solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced close="|" open="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>2</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>2</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><mi>C</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>.</mo></math></p><p>Now, it is given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">C</mi><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi mathvariant="normal">C</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow><mrow><mn>2</mn><mo>+</mo><mi>tan</mi><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p>Now, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mstyle></mrow><mrow><mn>2</mn><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mstyle></mrow></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mstyle displaystyle="true"><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mstyle></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mfenced><mfrac><mstyle displaystyle="true"><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>1</mn></mstyle></mfrac></mfenced><mo>&#215;</mo><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mstyle displaystyle="true"><mn>5</mn><mo>+</mo><msqrt><mn>3</mn></msqrt></mstyle><mstyle displaystyle="true"><mn>11</mn></mstyle></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mfenced><mfrac><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt><mo>+</mo><mn>10</mn></mrow><mn>11</mn></mfrac></mfenced><mo>.</mo></math></p>

</details>

---

### Q94. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math> is equal to<gwmw style="display:none;"></gwmw></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mn>2</mn></math>
- **(B)** <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac></mfenced><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mrow><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mi>sec</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>sec</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>cos</mi><mi>x</mi><mo>&#183;</mo><mi>ln</mi><mfenced close="|" open="|"><mrow><mi>sec</mi><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="right"><mi>y</mi></menclose><mrow><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msub><mo>=</mo><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mo>&#183;</mo><mi>ln</mi><msqrt><mn>2</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="right"><mi>y</mi></menclose><mrow><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt></mrow></mfrac><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p>

</details>

---

### Q95. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi><mo>,</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>, then the maximum value of the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced></math> over <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>15</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>ln</mi><mi>sec</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>sin</mi><mi>x</mi><mo>.</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>sec</mi><mi>x</mi><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><mfenced><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mo>=</mo><mi>sec</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mi>sec</mi><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mrow><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mo>=</mo><mi>cos</mi><mi>x</mi><mo>-</mo><mn>2</mn><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn><mo>&#8804;</mo><mi>t</mi><mo>&#8804;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>t</mi><mo>-</mo><mn>2</mn><msup><mi>t</mi><mn>2</mn></msup><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mn>4</mn><mi>t</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>Second-order derivative is negative</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>max</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p>

</details>

---

### Q96. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let slope of the tangent line to a curve at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi></mrow></mfenced></math> be given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>y</mi></mrow><mi>x</mi></mfrac></math>. If the curve intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>4</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>, for which the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mi>y</mi></mrow></mfenced></math> lies on the curve, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>18</mn><mn>35</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>18</mn><mn>19</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>18</mn><mn>11</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>18</mn><mn>19</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>y</mi></mrow><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mi>d</mi><mi>y</mi><mo>-</mo><mi>y</mi><mi>d</mi><mi>x</mi></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>d</mi><mfenced><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Curve intersects the line <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>4</mn></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo></math> point of intersection is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math>. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mn>2</mn><mo>+</mo><mi>c</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mi>x</mi></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p>Now put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mi>y</mi></mrow></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>18</mn></mrow><mn>19</mn></mfrac></math></p>

</details>

---

### Q97. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> is the solution of the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><mi>cos</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><mi>cos</mi><mi>x</mi><mo>=</mo><mi>cos</mi><mi>x</mi><mo>,</mo><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

Put <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><mo>=</mo><mi>t</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><mi>cos</mi><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">D</mi><mo>.</mo><mi mathvariant="normal">E</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>t</mi><mi>cos</mi><mi>x</mi><mo>=</mo><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>.</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>cos</mi><mi>x</mi><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>e</mi><mrow><mi>sin</mi><mi>y</mi></mrow></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>+</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q98. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If a curve passes through the origin and the slope of the tangent to it at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>8</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>,</mo></math> then this curve also passes through the point:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math>**

**Detailed Solution:**

Given<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>y</mi><mo>+</mo><mn>4</mn></mrow><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mi>y</mi><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfrac><mn>4</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>I</mi><mo mathvariant="italic">.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></math></p><p>Solution of L.D.E.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>y</mi><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mfenced><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfrac><mn>4</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>&#183;</mo><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>y</mi><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mi>x</mi><mo>-</mo><mfrac><mn>4</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>4</mn><mo>-</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi></math></p><p>This curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math></p>

</details>

---

### Q99. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If a curve <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math> and satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mo>&#160;</mo><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup><mo>,</mo></math> then for what value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>,</mo><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>62</mn><mn>5</mn></mfrac><mo>?</mo></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>62</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>So, solution of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">D</mi><mo>.</mo><mi mathvariant="normal">E</mi><mo>.</mo></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>b</mi><mo>&#183;</mo><msup><mi>x</mi><mn>3</mn></msup><mo>&#183;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mi>c</mi><mi>x</mi></mfrac><mo>+</mo><mfrac><mrow><mi>b</mi><msup><mi>x</mi><mn>4</mn></msup></mrow><mn>5</mn></mfrac></math></p><p>Passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>=</mo><mi>c</mi><mo>+</mo><mfrac><mi>b</mi><mn>5</mn></mfrac><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mo>&#8747;</mo><mn>1</mn><mn>2</mn></msubsup><mi>f</mi><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mn>62</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced close="]" open="["><mrow><mi>c</mi><mo mathvariant="italic">&#160;</mo><mi>ln</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mi>b</mi><msup><mi>x</mi><mn>5</mn></msup></mrow><mn>25</mn></mfrac></mrow></mfenced><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>62</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo mathvariant="italic">c</mo><mo mathvariant="italic">&#160;</mo><mi>ln</mi><mo mathvariant="italic">&#160;</mo><mn>2</mn><mo>+</mo><mfrac><mrow><mn>31</mn><mo>&#160;</mo><mi>b</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mfrac><mn>62</mn><mn>5</mn></mfrac><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>By equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q100. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mi>sin</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mn>2</mn><mi>x</mi><mo>,</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math>
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>(</mo><mi>&#960;</mi><mo>/</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>(</mo><mi>&#960;</mi><mo>/</mo><mn>4</mn><mo>)</mo></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>-</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mo>&#183;</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>sin</mi><mi>x</mi></math></p><p>I.F. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mn>2</mn><mi>tan</mi><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p>solution is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>&#183;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>2</mn><mi>sec</mi><mi>x</mi><mo>+</mo><mi>C</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mn>2</mn><mo>.</mo><mn>2</mn><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mo>-</mo><mn>4</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>2</mn><mi>sec</mi><mi>x</mi><mo>-</mo><mn>4</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q101. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><msup><mi>y</mi><mo>&#39;</mo></msup><mo>-</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>(</mo><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi><mo>)</mo></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>&#960;</mi><mo>)</mo><mo>=</mo><mi>&#960;</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#39;</mo><mo>&#39;</mo><mfenced><mfrac><mi>&#960;</mi><mn mathvariant="italic">2</mn></mfrac></mfenced><mo mathvariant="italic">+</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn mathvariant="italic">2</mn></mfrac></mfenced></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>&#8722;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced><mrow><mi>xcos</mi><mo>+</mo><mi>sinx</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>dy</mi><mi>dx</mi></mfrac><mo>&#8722;</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">x</mi><mfenced><mrow><mi>xcosx</mi><mo>+</mo><mi>sinx</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> I.F <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi>l</mi><mi>nx</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mi mathvariant="normal">x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>.</mo><mi>x</mi><mfenced><mrow><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi mathvariant="normal">d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mi>sin</mi><mi>x</mi></mrow></mfenced><mi>dx</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mi mathvariant="normal">C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi mathvariant="normal">y</mi><mfenced><mi mathvariant="normal">&#960;</mi></mfenced><mo>=</mo><mi mathvariant="normal">&#960;</mi><mo>&#160;</mo><mo>&#8658;</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>y</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mi>sin</mi><mi>x</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup><mi>y</mi></mrow><mrow><mi mathvariant="normal">d</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8722;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>sin</mi><mi>x</mi><mo>+</mo><mn>4</mn><mi>x</mi><mi>cos</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>sin</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>''</mo></msup><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>+</mo><mi>y</mi><mfenced><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mfenced><mrow><mo>&#8722;</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>0</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8722;</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mo>+</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></math>.</p>

</details>

---

### Q102. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

If for <math><mi>x</mi><mo>&#8805;</mo><mn>0</mn><mo>,</mo><mi></mi><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is the solution of the differential equation, <math><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mfenced separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>y</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mi>d</mi><mi>x</mi><mo>,</mo><mi>y</mi><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></math> is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi><mo>-</mo><mn>3</mn></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mrow></mfenced><mi></mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mfrac><mi>y</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>-</mo><mfrac><mn>3</mn><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac></math></p><p>I.F<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mfrac><mi>y</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>y</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi><mo>+</mo><mn>3</mn><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced open="[" close="]" separators="|"><mrow><mi>x</mi><mo>+</mo><mfrac><mn>3</mn><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>)</mo></mrow></mfrac><mo>+</mo><mi>c</mi></mrow></mfenced></math> , <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>=</mo><mn>3</mn><mfenced><mrow><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mi>c</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q103. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> is the solution of the differential equation <math><mo>,</mo><mi mathvariant="normal"></mi><msup><mrow><mi>e</mi></mrow><mrow><mi>y</mi></mrow></msup><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math> such that <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo><mi></mi></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>
- **(B)** <math><mn>2</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>
- **(C)** <math><mn>2</mn><mi>e</mi></math>
- **(D)** <math><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mi>e</mi></mrow></msub><mn>2</mn></math>**

**Detailed Solution:**

<p><math><msup><mrow><mi>e</mi></mrow><mrow><mi>y</mi></mrow></msup><mo>=</mo><mi>t</mi></math>
<math><msup><mrow><mi>e</mi></mrow><mrow><mi>y</mi></mrow></msup><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<math><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>t</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math><msup><mrow><mi>e</mi></mrow><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi><mo>+</mo><mn>1</mn></math>
<math><mi>y</mi><mo>=</mo><mi>x</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mrow></math>
at <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal"></mi><mi>y</mi><mo>=</mo><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></mrow></mrow></math></p>

</details>

---

### Q104. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider the differential equation, <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>. If value of <math><mi>y</mi></math> is <math><mn>1</mn></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn></math>, then the value of <math><mi>x</mi></math> for which <math><mi>y</mi><mo>=</mo><mn>2</mn><mo>,</mo><mi>&#160;</mi></math>is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><msqrt><mi>e</mi></msqrt></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>e</mi></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given differential equation is
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfenced separators="|"><mrow><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>-</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mn>2</mn></msup><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>+</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mi>y</mi></mfrac></math>
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math>
It is a linear differential equation whose integrating factor <math><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mi>&#160;</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mrow><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mrow></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup></math>
Solution of a given differential equation can be written as
<math><mi>x</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>y</mi><mo>=</mo><mi>I</mi></mrow></mrow></math>
Let <math><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mi>t</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>d</mi><mi>t</mi><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mfenced separators="|"><mrow><mo>-</mo><mi>t</mi></mrow></mfenced><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mi>&#160;</mi><mi>d</mi><mi>t</mi></mrow></mrow></math>
<math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>t</mi></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>t</mi></mrow></mfenced><mo>+</mo><mi>C</mi></math>, (Integrating by parts)
<math><mo>&#8658;</mo><mi>&#160;</mi></math> Solution of differential equation is <math><mi>x</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi>C</mi></math>
Since for <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi></math>we have <math><mi>y</mi><mo>=</mo><mn>1</mn></math>,
<math><mo>&#8658;</mo><mn>1</mn><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
<math><mo>&#8658;</mo></math> Solution with given condition is <math><mi>x</mi><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
or <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup></math>
So, <math><msub><mrow><mfenced close="|" open="" separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mi>y</mi><mo>=</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mi>e</mi></msqrt></mrow></mfrac></math></p>

</details>

---

### Q105. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced><mi>x</mi></mfenced></math> be the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>tan</mi><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>2</mn></mfrac></mrow></mfenced><mo>,</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mi mathvariant="normal">&#160;</mi><mn>1</mn><mo>.</mo></math> Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><msup><mi>y</mi><mo>'</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi mathvariant="normal">&#160;</mi><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>+</mo><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mi mathvariant="normal">&#160;</mi><msqrt><mn>2</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><mi>y</mi><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#160;</mi><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>+</mo><msup><mi mathvariant="normal">y</mi><mo>'</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><msup><mi mathvariant="normal">&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><msup><mi>y</mi><mo>'</mo></msup><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mi mathvariant="normal">&#960;</mi><mo>-</mo><mi mathvariant="normal">&#160;</mi><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>tan</mi><mi>x</mi></math></p><p>This is a linear differential equation of the type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>tan</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>tan</mi><mi>x</mi></math></p><p>Now, the integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mi>lnsec</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>sec</mi><mi>x</mi></math></p><p>And, the general solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#8901;</mo><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>sec</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">&#160;</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>2</mn></msup><mfenced separators="|"><mrow><mi>sec</mi><mi>x</mi><mo>&#8901;</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Using integration by parts in the second integral, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><mi>sec</mi><mi mathvariant="normal">&#160;</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8747;</mo><mfenced separators="|"><mrow><mi>sec</mi><mi>x</mi><mo>&#8901;</mo><mi>tan</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>&#8747;</mo><mfenced separators="|"><mrow><mi>sec</mi><mi>x</mi><mo>&#8901;</mo><mi>tan</mi><mi>x</mi></mrow></mfenced></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><mi>sec</mi><mi mathvariant="normal">&#160;</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>&#8747;</mo><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mn>2</mn><mi>x</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>+</mo><mi>c</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p>So, <math><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi></math></p><p>Hence, <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>16</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math> and <math><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>16</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac></math></p><p>Differentiating <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> with respect to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><mi>x</mi><mo>-</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mo>'</mo></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>y</mi><mo>'</mo></msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>-</mo><msup><mi>y</mi><mo>'</mo></msup><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mi>&#960;</mi><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>.</mo></math></p>

</details>

---

### Q106. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution of the differential equation <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mo>(</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>-</mo><mi>y</mi><mo>)</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></math> , <math><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> , such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>0</mn></math>, then <math><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac><mo>-</mo><mn>2</mn></math>
- **(B)** <math><mn>2</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
- **(C)** <math><mi>e</mi><mo>-</mo><mn>2</mn></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mi mathvariant="normal">e</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>e</mi><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<p>The given differential equation can be written as
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>.</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi></math>
Integrating factor <math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>&#8747;</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup></math>
Hence, solution of given differential equation,
<math><mi>y</mi><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>.</mo><msup><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">c</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>x</mi><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>.</mo><msup><mi>e</mi><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>.</mo><msup><mi>e</mi><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>-</mo><mo>&#8747;</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi><msup><mi mathvariant="normal">c</mi><mn>2</mn></msup><mi>x</mi><mo>.</mo><msup><mi>e</mi><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math>   (using integration by parts)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>.</mo><msup><mi>e</mi><mrow><mi>tan</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>tan</mi><mi>x</mi><mo>.</mo><msup><mi>e</mi><mrow><mi>tan</mi><mi>x</mi></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mi>tan</mi><mi>x</mi></mrow></msup><mo>+</mo><mi>c</mi></math></p><p>Given, <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi mathvariant="normal">c</mi><mo>=</mo><mn>1</mn></math></p><p>Solution of given differential is</p><p><math><mi>y</mi><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>=</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>.</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>x</mi></mrow></msup><mo>+</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfrac></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mi>e</mi><mo>-</mo><mn>2</mn></math></p>

</details>

---

### Q107. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">s</mi><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi>x</mi><mo>=</mo><mn>6</mn><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>4</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

The given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>.</mo><mi>E</mi><mo>.</mo></math> can be written as<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>-</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mn>6</mn><mi>x</mi><mi>sec</mi><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced><mo>,</mo></math> which is a liner differential equation of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8201;</mo><mo>&#38;</mo><mo>&#8201;</mo><mi>Q</mi></math> are the function of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> or constants.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mo>-</mo><mi>tan</mi><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mn>6</mn><mi>x</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi>x</mi></math></p><p>Integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>-</mo><mfenced><mrow><mo>-</mo><mi>ln</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced><mrow><mi>cos</mi><mi>x</mi></mrow></mfenced></mrow></msup><mo>=</mo><mi>cos</mi><mi>x</mi></math></p><p>And, the solution of the linear differential equation is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#8901;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mn>6</mn><mi>x</mi><mi>sec</mi><mi>x</mi></mrow></mfenced><mo>&#8901;</mo><mi>cos</mi><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#8901;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>6</mn><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mn>3</mn><msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p>Thus, the curve is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mi>cos</mi><mi>x</mi><mo>=</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p>Now, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>6</mn></mfrac><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>&#183;</mo><mi>cos</mi><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mn>3</mn><msup><mfenced><mfrac><mi mathvariant="normal">&#960;</mi><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>&#8901;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#8901;</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>36</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>&#8901;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>12</mn></mfrac><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>&#8901;</mo><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mrow><mn>2</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><mo>.</mo></math></p>

</details>

---

### Q108. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mo>(</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>)</mo></math> with <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math>, is

**Options:**

- **(A)** <math><mi>y</mi><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given, differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mi>y</mi><mo>=</mo><mi>x</mi></math></p><p>This is a linear differential equation of type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8201;</mo><mo>&#38;</mo><mo>&#8201;</mo><mi>Q</mi></math> are the functions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> or constants.</p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>x</mi></math></p><p>The integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>ln</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>.</mo></math></p><p>The solution of the linear differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#215;</mo><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced><mrow><mi>Q</mi><mo>&#215;</mo><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math> </p><p>So, the solution of the given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>&#183;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mo>&#8747;</mo><msup><mi>x</mi><mn>3</mn></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>C</mi></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><msup><mi>x</mi><mi>n</mi></msup><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>1</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#183;</mo><mn>1</mn><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac><mo>.</mo></math></p>

</details>

---

### Q109. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> be the solution of the differential equation, <math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>)</mo><mi>y</mi><mo>=</mo><mn>1</mn></math> such that <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>.</mo></math> If <math><msqrt><mi>a</mi></msqrt><mi>&#160;</mi><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>32</mn></mrow></mfrac><mo>,</mo></math> then the value of <math><mi>a</mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>x</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>y</mi><mo>=</mo><mn>1</mn></math>
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
Which is a linear differential equation with integrating factor
<math xmlns="http://www.w3.org/1998/Math/MathML"/>I.F. = <math><msup><mrow><mi>e</mi></mrow><mrow><mo>&#8747;</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>)</mo></mrow></msup><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></math>
The solution of the given differential equation will be,
<math><mi>y</mi><mo>.</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mi>d</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><mi mathvariant="normal">c</mi></math>
Now, <math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mn>0</mn></math> <math><mo>&#8658;</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>0</mn></math> and <math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mo>(</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi></math>
<math><msqrt><mi>a</mi></msqrt><mi>y</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>32</mn></mrow></mfrac><mo>&#8658;</mo><msqrt><mi>a</mi></msqrt><mo>=</mo><mfrac><mrow><mi>&#960;</mi><mo>/</mo><mn>32</mn></mrow><mrow><mi>&#960;</mi><mo>/</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

</details>

---

### Q110. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If a curve passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math> and has slope of the tangent at any point <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>y</mi></mrow></mfenced></math> on it as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>y</mi></mrow><mi>x</mi></mfrac></math>, then the curve also passes through the point

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>
- **(B)** <math><mo>(</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>)</mo></math>
- **(C)** <math><mo>(</mo><mo>-</mo><msqrt><mn>2</mn></msqrt><mo>,</mo><mn>1</mn><mo>)</mo></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>3</mn><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced><mi> </mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>y</mi><mo>=</mo><mi>x</mi></math>.  It is in linear form.</p><p>I.F.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>2</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>l</mi><mi>n</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mo>.</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>.</mo><msup><mi>x</mi><mn>2</mn></msup><mi>&#160;</mi><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math><mo>&#8757;</mo></math>At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>-</mo><mn>2</mn><mo>&#215;</mo><msup><mn>1</mn><mn>2</mn></msup><mo>=</mo><mfrac><msup><mfenced separators="|"><mn>1</mn></mfenced><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p><math><mo>&#8756;</mo></math>curve is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>.</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p><math><mo>&#8756;</mo></math>It passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msqrt><mn>3</mn></msqrt><mo>,</mo><mi>&#160;</mi><mn>0</mn></mrow></mfenced></math>.</p>

</details>

---

### Q111. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced></math> be the solution of the differential equation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mi>x</mi><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn><mo>-</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mi>e</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mi>e</mi><mn>2</mn></mfrac></math>
- **(B)** <math><mfrac><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>e</mi><mn>2</mn></msup><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mi>e</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>The given differential equation can be written as

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mi>x</mi></mfrac><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi></math>, which is a linear differential equation.</p><p>Now, integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>l</mi><mi>n</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>x</mi></math></p><p>Hence, the solution of the given differential equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>&#183;</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>&#8747;</mo><mi>x</mi><mi>d</mi><mi>x</mi><mo>-</mo><mo>&#8747;</mo><mfenced open="{" close="}"><mrow><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#8747;</mo><mi>x</mi><mi>d</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></math> (using integration by parts)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>-</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>&#183;</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><mi>x</mi><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mfenced><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced><mo>-</mo><mo>&#8747;</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><mi>d</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>4</mn></mfrac><mo>+</mo><mi>C</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mn>2</mn><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn><mo>-</mo><mn>1</mn><mo>+</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>y</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn><mo>-</mo><mn>1</mn><mo>+</mo><mi>C</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>y</mi><mfenced separators="|"><mn>2</mn></mfenced><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>4</mn><mo>-</mo><mn>1</mn></math></p><p>Then we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mn>0</mn></math> </p><p>Now, from the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mfrac><mi>x</mi><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mi>x</mi><mo>-</mo><mfrac><mi>x</mi><mn>4</mn></mfrac></math></p><p>Putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>e</mi></math> in above equation, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>e</mi></mfenced><mo>=</mo><mfrac><mi>e</mi><mn>2</mn></mfrac><msub><mi>log</mi><mi>e</mi></msub><mi>e</mi><mo>-</mo><mfrac><mi>e</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mi>e</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>e</mi><mn>4</mn></mfrac><mo>=</mo><mfrac><mi>e</mi><mn>4</mn></mfrac></math></p>

</details>

---

### Q112. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $y(x)$ is the solution of the differential equation $\frac{d y}{d x}+\left(\frac{2 x+1}{x}\right) y=e^{-2 x}, x>0,$ where $y(1)=\frac{1}{2} e^{-2},$ then:

**Options:**

- **(A)** $y\left(\log _{e} 2\right)=\log _{e} 4$
- **(B)** $y\left(\log _{e} 2\right)=\frac{\log _{e} 2}{4}$
- **(C)** $y(x)$ is decreasing in $\left(\frac{1}{2}, 1\right)$
- **(D)** $y(x)$ is decreasing in (0,1)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y(x)$ is decreasing in $\left(\frac{1}{2}, 1\right)$**

**Detailed Solution:**

Given differential equation is,

$\frac{d y}{d x}+\left(2+\frac{1}{x}\right) y=e^{-2 x}, x>0$

$\mathrm{IF}=e^{\int\left(2+\frac{1}{x}\right) d x}=e^{2 x+\ln x}=x e^{2 x}$

Complete solution is given by

$y(x) \cdot x e^{2 x}=\int x e^{2 x} \cdot e^{-2 x} d x+c$

$=\int x d x+c$

$y(x) \cdot e^{2 x} \cdot x=\frac{x^{2}}{2}+c$

Given, $y(1)=\frac{1}{2} e^{-2}$

$\therefore \quad \frac{1}{2} e^{-2} \cdot e^{2} \cdot 1=\frac{1}{2}+c \Rightarrow c=0$

$\therefore \quad y(x)=\frac{x^{2}}{2} \cdot \frac{e^{-2 x}}{x}$

$y(x)=\frac{x}{2} \cdot e^{-2 x}$

Differentiate both sides with respect to $x$

$y^{\prime}(x)=\frac{e^{-2 x}}{2}(1-2 x)  < 0 \forall x \in\left(\frac{1}{2}, 1\right)$

Hence, $y(x)$ is decreasing in $\left(\frac{1}{2}, 1\right)$

</details>

---

### Q113. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced></math> be a differentiable function such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>'</mo></msup><mfenced separators="|"><mi>x</mi></mfenced><mo>=</mo><mn>7</mn><mo>-</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfrac><mrow><mi>f</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow><mi>x</mi></mfrac><mo>,</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math> and <math><mi>f</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>&#8800;</mo><mn>4</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>lim</mi><mrow><mi>x</mi><mo>&#8594;</mo><msup><mn>0</mn><mo>+</mo></msup></mrow></munder><mo>&#8289;</mo><mi>x</mi><mi>&#160;</mi><mi>f</mi><mfenced separators="|"><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced></math>

**Options:**

- **(A)** does not exist.
- **(B)** exists and equals <math><mn>4</mn></math>.
- **(C)** exists and equals <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math>.
- **(D)** exists and equals <math><mn>0</mn></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) exists and equals <math><mn>4</mn></math>.**

**Detailed Solution:**

We have, <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>y</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mn>7</mn></math> <math><mo>(</mo></math> where <math><mi>y</mi><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>)</mo></math>

This is a linear differential equation.

Integrating factor, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>&#160;</mo></math><math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>&#8747;</mo><mfrac><mrow><mn>3</mn><mtext>&#8201;</mtext><mi>d</mi><mi>x</mi></mrow><mrow><mn>4</mn><mi>x</mi></mrow></mfrac></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mi>l</mi><mi>n</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>

So, integrating the given differential equation using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></math> 

<math><mo>&#8658;</mo><mi>y</mi><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>=</mo><mo>&#8747;</mo><mn>7</mn><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mi>d</mi><mi>x</mi></math>

<math><mo>&#8658;</mo><mi>y</mi><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>7</mn><mo>.</mo><mfrac><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math>

<math><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></mrow></mfenced><mo>=</mo><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>+</mo><mi>C</mi></math>

<math><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>4</mn><mi>x</mi><mo>+</mo><mi>C</mi><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>

<math><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>x</mi><mi>f</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>&#8658;</mo><munder><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>x</mi><mo>&#8594;</mo><msup><mrow><mn>0</mn></mrow><mrow><mo>+</mo></mrow></msup></mrow></munder><mi>x</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>+</mo><mi>C</mi><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></mrow></mfenced><mo>=</mo><mn>4</mn></math>

</details>

---

### Q114. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></math> , <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></mrow></mfenced><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></math> equals

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><msup><mi>e</mi><mn>3</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><msup><mi>e</mi><mn>6</mn></msup></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><mn>3</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></mrow></mfenced><mi>y</mi><mo>=</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi></math></p><p>This is linear differential equation, of the type <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi></math> are functions of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> or constants.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>3</mn><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi></math></p><p>Now, integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mn>3</mn><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup></math></p><p>Hence, the solution of the differential equation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mrow><mi>I</mi><mo>.</mo><mi>F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>&#183;</mo><msup><mi>sec</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mi>x</mi><mo>=</mo><mi>t</mi><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>s</mi><mi>e</mi><msup><mi>c</mi><mn>2</mn></msup><mi>x</mi><mi>d</mi><mi>x</mi><mo>=</mo><mi>d</mi><mi>t</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>t</mi></mrow></msup><mi>d</mi><mi>t</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>3</mn><mi>t</mi></mrow></msup><mn>3</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>=</mo><mfrac><msup><mi>e</mi><mrow><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mn>3</mn></mfrac><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#8658;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>=</mo><mi>c</mi><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mi>tan</mi><mi>x</mi></mrow></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mfenced><mrow><mi>tan</mi><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></mrow></mfenced></mrow></mfenced></mrow></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>3</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mn>3</mn></msup><mo>&#183;</mo><msup><mi>e</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><msup><mi>e</mi><mn>6</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q115. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>y</mi><mo>=</mo><mi>y</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> is the solution of the differential equation, <math><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mi>y</mi><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> satisfying <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>49</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>49</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given differential equation can be written as

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>x</mi></math> , which is a linear differential equation.

If <math><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>&#8747;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn><mtext>&#8201;</mtext><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mtext>&#8201;</mtext><mi>x</mi></mrow></msup><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

Solution is

<math><mi>y</mi><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>x</mi><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></math>

<math><mo>&#8658;</mo><mi>y</mi><mo>.</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mi>c</mi></math>

Since, given curve passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>

<math><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

Hence, <math><mi>y</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>.

So, <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>49</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>.

</details>

---

### Q116. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>y</mi><mfenced separators="|"><mi>x</mi></mfenced></math> be the solution of the differential equation <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mrow><mrow><mi mathvariant="normal">cos</mi><mi>x</mi></mrow><mo>&#8289;</mo><mrow><mo>=</mo><mn>4</mn><mi>x</mi><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></mrow></mrow><mo>.</mo></math> If <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then <math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mo>-</mo><mn>8</mn></mrow><mrow><mn>9</mn><msqrt><mn>3</mn></msqrt></mrow></mfrac><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>9</mn></mrow></mfrac><msup><mrow><mi>π</mi></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>cot</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>&#960;</mi></mrow></mfenced></math>

I.F. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>cot</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mo>&#8289;</mo><mi>sin</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>sin</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>y</mi><mi>&#160;</mi><mi>sin</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi></mrow></mfrac><mo>.</mo><mi>sin</mi><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>x</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>sin</mi><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>0</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><msup><mfenced separators="|"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfenced separators="|"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced></mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></mfrac><mo>=</mo><mfenced close="]" open="["><mrow><mfenced separators="|"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>18</mn></mfrac></mfenced><mo>-</mo><mfenced separators="|"><mfrac><msup><mi>&#960;</mi><mn>2</mn></msup><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>&#215;</mo><mn>2</mn></math>

<math><mo>=</mo><mfrac><mrow><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac><mo>-</mo><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><mo>=</mo><mo>-</mo><mfrac><mrow><mn>8</mn><msup><mrow><mi>&#960;</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>9</mn></mrow></mfrac></math>

</details>

---

### Q117. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The curve satisfying the differential equation, <math><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>3</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> and passing through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math> also passes through the point

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

Given differential equation, <math><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>d</mi><mi>y</mi><mo>-</mo><mn>3</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>&#160;</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math>

<math> <mo>&#8658;</mo> </math> <math><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>+</mo><mn>3</mn><mi>y</mi></math>

<math><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mn>3</mn><mi>y</mi></math>

I.F. = <math><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mi>&#160;</mi><mi>d</mi><mi>y</mi></mrow></mrow></mrow></msup><mi>&#160;</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>&#8289;</mo><mrow><mi>y</mi></mrow></mrow></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> solution is

<math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mi>&#160;</mi><mrow><mo stretchy="false">&#8747;</mo><mrow><mn>3</mn><mi>y</mi><mi>&#160;</mi><mo>.</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mi>d</mi><mi>y</mi></mrow></mrow></math>

<math> <mo>&#8658;</mo> </math> <math><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mn>3</mn><mi>y</mi><mo>+</mo><mi>c</mi></math>

Passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;</mo><mn>1</mn><mo>=</mo><mn>3</mn><mo>+</mo><mi>c</mi><mo>&#160;</mo><mo>;</mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>

Equation of required curve, <math><mi>x</mi><mo>=</mo><mn>3</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>y</mi></math>

Clearly, it passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mrow><mo>&#8722;</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math>.

</details>

---

### Q118. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mi>y</mi><mn>2</mn></mfrac><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mi>tan</mi><mo>&#8289;</mo><mi>x</mi></mrow><mrow><mn>2</mn><mi>y</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced separators="|"><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, is given by

**Options:**

- **(A)** <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>
- **(B)** <math><mi>y</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>
- **(C)** <math><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>
- **(D)** <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>**

**Detailed Solution:**

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow><mrow><mn>2</mn><mi>y</mi></mrow></mfrac></math>
<math><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math>
Put <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>t</mi><mi>&#160;</mi><mo>&#8658;</mo><mn>2</mn><mi>y</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>
<math><mfrac><mrow><mi>d</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>t</mi><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></math>
 <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mo>(</mo><mi>sec</mi><mo>&#8289;</mo><mrow><mi>x</mi><mo>+</mo><mi>t</mi><mi>a</mi><mi>n</mi><mi>x</mi><mo>)</mo></mrow></mrow></msup><mo>=</mo><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>x</mi></math>
<math><mo>&#8658;</mo><mi>t</mi><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mo stretchy="false">&#8747;</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow><mi>d</mi><mi>x</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mfenced separators="|"><mrow><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mo>+</mo><mi>tan</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mfenced separators="|"><mrow><mi>sec</mi><mo>&#8289;</mo><mi>x</mi><mi>tan</mi><mo>&#8289;</mo><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mo>&#8747;</mo><msup><mi>tan</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>x</mi><mi>d</mi><mi>x</mi></math>
<math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>-</mo><mi>x</mi><mo>+</mo><mi>c</mi></math>
<math><mi>y</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mi>&#160;</mi><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">sec</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>&#8289;</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac></math>

</details>

---

### Q119. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If a curve <math><mi>y</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></math> passes through the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math> and satisfies the differential equation, <math><mi>y</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mi>y</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>x</mi><mi>&#160;</mi><mi>d</mi><mi>y</mi><mo>,</mo></math> then <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given differential equation,

<math><mi>y</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>x</mi><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi><mo>=</mo><mi>x</mi><mi>d</mi><mi>y</mi></math>

<math><mo>&#8658;</mo></math> <math><mfrac><mrow><mi>x</mi><mi>d</mi><mi>y</mi><mo>-</mo><mi>y</mi><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mi>x</mi><mi>d</mi><mi>x</mi></math>

<math><mo>&#8658;</mo></math> <math><mo>-</mo><mi>d</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>d</mi><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>

On integrating we get,

<math><mo>&#8658;-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>C</mi></math>

<math><mo>&#8757;</mo></math> It passes through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>)</mo></math>.

<math><mo>&#8756;</mo></math> <math><mn>1</mn><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mi>C</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>C</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math>

<math><mo>&#8756;</mo></math> <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q120. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi mathvariant="normal">d</mi><mi>x</mi><mo>-</mo><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mi mathvariant="normal">d</mi><mi>y</mi><mo>=</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>f</mi><mfenced separators="|"><mi>y</mi></mfenced></math>. If <math><mi>f</mi><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>,</mo></math> then <math><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>d</mi><mi>y</mi><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mi>d</mi><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mi>d</mi><mi>x</mi><mo>-</mo><mi>x</mi><mi>d</mi><mi>y</mi></mrow><msup><mi>y</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>2</mn><mi>d</mi><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced separators="|"><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mn>2</mn><mi>d</mi><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8747;</mo><mi>d</mi><mfenced separators="|"><mfrac><mi>x</mi><mi>y</mi></mfrac></mfenced><mo>=</mo><mn>2</mn><mo>&#8747;</mo><mi>d</mi><mi>y</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>c</mi><mi>y</mi></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi>x</mi><mo>=</mo><mn>1</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mn>2</mn><mo>-</mo><mi>c</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>1</mn></math>

<math><mo>&#8756;</mo></math> Curve would be

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>y</mi></math>

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn><mi>&#160;</mi></math>.

</details>

---

### Q121. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow></math> be the solution of the differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mi>x</mi><mi>log</mi><mi>x</mi><mo>)</mo></mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mi>log</mi><mi>x</mi><mo>,</mo><mtext>&#8201;</mtext><mrow><mo>(</mo><mi>x</mi><mo>&#8805;</mo><mn>1</mn><mo>)</mo></mrow></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mrow><mo>(</mo><mi>e</mi><mo>)</mo></mrow></math> is equal to

**Options:**

- **(A)** <math> <mrow> <mn>2</mn><mi>e</mi> </mrow> </math>
- **(B)** <math> <mi>e</mi> </math>
- **(C)** <math> <mn>0</mn> </math>
- **(D)** <math > <mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math > <mn>2</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mi>x</mi><mi>log</mi><mi>x</mi><mo>)</mo></mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi><mi>log</mi><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced><mfrac><mn>1</mn><mrow><mi>x</mi><mi>log</mi><mi>x</mi></mrow></mfrac></mfenced><mi>y</mi><mo>=</mo><mn>2</mn></math>
Integrating factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>.</mo><mi>F</mi><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mn mathvariant="italic">1</mn><mrow><mi>x</mi><mi>log</mi><mo mathvariant="italic">x</mo></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mfrac><mrow><mn mathvariant="italic">1</mn><mo mathvariant="italic">/</mo><mi>x</mi></mrow><mrow><mi>log</mi><mo mathvariant="italic">x</mo></mrow></mfrac><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>log</mi><mfenced><mrow><mi>log</mi><mo mathvariant="italic">x</mo></mrow></mfenced></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>log</mi><mi>x</mi></math></p><p>The solution of the equation becomes </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mo>&#183;</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>P</mi><mi>d</mi><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> is the constant of integration.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>log x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>log x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>log x</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x log x</mi><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>c</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>1</mn><mi>,</mi><msub><mi>y</mi><mn>1</mn></msub></mrow></mfenced></math> be any point on the curve.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>y</mi><mn>1</mn></msub><mo>&#183;</mo><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>0</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>c</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>log</mi><mo>x</mo><mo>=</mo><mn>2</mn><mfenced><mrow><mi>x</mi><mi>log</mi><mo>x</mo><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mn>2</mn></math></p><p>Now, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>e</mi></math>, we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q122. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mo mathvariant="italic">x</mo><mo>=</mo><mo>sin</mo><mn>2</mn><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>&#960;</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>**

**Detailed Solution:**

<p>The given differential equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>y</mi><mi>tan</mi><mi>x</mi><mo>=</mo><mi>sin</mi><mn>2</mn><mi>x</mi></math> is linear differential equation of the form </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mfenced><mi>x</mi></mfenced><mi>y</mi><mo>=</mo><mi>Q</mi><mfenced><mi>x</mi></mfenced></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>tan</mi><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>sin</mi><mn>2</mn><mi>x</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mo mathvariant="italic">P</mo><mfenced><mi>x</mi></mfenced><mi>d</mi><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mo>&#8747;</mo><mi>tan</mi><mi>x</mi><mo mathvariant="italic">dx</mo></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mi>ln</mi><mfenced><mrow><mi>sec</mi><mo mathvariant="italic">x</mo></mrow></mfenced></mrow></msup><mo>=</mo><mi>sec</mi><mi>x</mi></math></p><p>And, the solution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mrow><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo></mrow></mfenced><mo>=</mo><mo>&#8747;</mo><mi>Q</mi><mfenced><mi>x</mi></mfenced><mfenced><mrow><mi mathvariant="normal">I</mi><mo>.</mo><mi mathvariant="normal">F</mi><mo>.</mo></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mi>sec</mi><mi>x</mi><mi>sin</mi><mn>2</mn><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mfrac><mn>1</mn><mrow><mi>cos</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mn>2</mn><mi>sin</mi><mi>x</mi><mi>cos</mi><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mo>&#8747;</mo><mn>2</mn><mi>sin</mi><mi>x</mi><mi>d</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>sec</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mi>c</mi></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mn>0</mn></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>&#183;</mo><mi>sec</mi><mn>0</mn><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mn>0</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mi>sec</mi><mo mathvariant="italic">x</mo><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>x</mi><mo>+</mo><mn>3</mn></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mi>&#960;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><mi>&#960;</mi></mfenced><mi>sec</mi><mi>&#960;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>cos</mi><mi>&#960;</mi><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mi>&#960;</mi></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mfenced><mi>&#960;</mi></mfenced><mo>=</mo><mo>-</mo><mn>5</mn><mo>.</mo></math></p>

</details>

---

### Q123. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If for a continuous function $\mathrm{f}(\mathrm{x})$, $\int_{-\pi}^t(f(x)+x d x)=\pi^2-t^2$, for all $t \geq-\pi$, then $\mathrm{f}\left(-\frac{\pi}{3}\right)$ is equal to:

**Options:**

- **(A)** $\pi$
- **(B)** $\frac{\pi}{2}$
- **(C)** $\frac{\pi}{3}$
- **(D)** $\frac{\pi}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\pi$**

**Detailed Solution:**

Let $\int_{-\pi}^t(f(x)+x) d x=\pi^2-t^2$
$$
\begin{aligned}
&\Rightarrow \int_{-\pi}^t f(x) d x+\int_{-\pi}^t x d x=\pi^2-t^2 \\
&\Rightarrow \int_{-\pi}^t f(x) d x+\left(\frac{t^2}{2}-\frac{\pi^2}{2}\right)=\pi^2-t^2 \\
&\Rightarrow \int_{-\pi}^t f(x) d x=\frac{3}{2}\left(\pi^2-t^2\right)
\end{aligned}
$$
differentiating with respect to $t$
$\frac{d}{d t}\left[\int_{-\pi}^t f(x) d x\right]=\frac{3}{2} \frac{d}{d t}\left(\pi^2-t^2\right)$
$f(t) \cdot \frac{d t}{d t}-f(-\pi) \frac{d}{d t}(-\pi)=-3 t$
$f(t)=-3 t$
$f\left(-\frac{\pi}{3}\right)=-3\left(-\frac{\pi}{3}\right)=\pi$

</details>

---

### Q124. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The equation of the curve passing through the origin and satisfying the differential equation $\left(1+x^2\right) \frac{d y}{d x}+2 x y=4 x^2$ is

**Options:**

- **(A)** $\left(1+x^2\right) y=x^3$
- **(B)** $3\left(1+x^2\right) y=2 x^3$
- **(C)** $\left(1+x^2\right) y=3 x^3$
- **(D)** $3\left(1+x^2\right) y=4 x^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3\left(1+x^2\right) y=4 x^3$**

**Detailed Solution:**

Given differential equation is
$$
\begin{aligned}
&\left(1+x^2\right) \frac{d y}{d x}+2 x y=4 x^2 \\
&\Rightarrow \frac{d y}{d x}+\left(\frac{2 x}{1+x^2}\right) y=\frac{4 x^2}{1+x^2}
\end{aligned}
$$
This is linear diff. equation
$$
\mathrm{I} . \mathrm{F}=e^{\int \frac{2 x}{1+x^2} d x}=e^{\log \left(1+x^2\right)}=1+x^2
$$
Solution is
$$
\begin{aligned}
&y\left(1+x^2\right)=\int \frac{4 x^2}{1+x^2} \times 1+x^2+\mathrm{C} \\
&\Rightarrow y\left(1+x^2\right)=\frac{4 x^3}{3}+\mathrm{C} \\
&\Rightarrow \text { Required curve is } \\
&3 y\left(1+x^2\right)=4 x^3(\because \mathrm{C}=0)
\end{aligned}
$$

</details>

---

### Q125. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $\left(x^2-1 \frac{d y}{d x}+2\right) x y=x$ is

**Options:**

- **(A)** $\frac{1}{x^2-1}$
- **(B)** $x^2-1$
- **(C)** $\frac{x^2-1}{x}$
- **(D)** $\frac{x}{x^2-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2-1$**

**Detailed Solution:**

Given differential equation is
$$
\begin{aligned}
& \left(x^2-1\right) \frac{d y}{d x}+2 x y=x \\
& \Rightarrow \quad \frac{d y}{d x}+\frac{2 x}{x^2-1} \cdot y=\frac{x}{x^2-1}
\end{aligned}
$$
This is in linear form.
$$
\begin{aligned}
& \text { Integrating factor }=\int \frac{2 x}{x^2-1} d x=\int_e \frac{d t}{t} \\
& \text { where } \begin{aligned}
& =x^2-1 \\
& =e^{\log t}=x^2-1
\end{aligned}
\end{aligned}
$$
Hence, required integrating factor $=x^2-1$.

</details>

---

### Q126. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{d y}{d x}+\frac{2}{x} y=x^2$ is

**Options:**

- **(A)** $y=c x^{-3}-\frac{x^2}{4}$
- **(B)** $y=c x^3-\frac{x^2}{4}$
- **(C)** $y=c x^2+\frac{x^3}{5}$
- **(D)** $y=c x^{-2}+\frac{x^3}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=c x^{-2}+\frac{x^3}{5}$**

**Detailed Solution:**

Given differential equation is
$$
\frac{d y}{d x}+\frac{2}{x} \cdot y=x^2
$$
This is of the linear form.
$$
\begin{aligned}
& \therefore P=\frac{2}{x}, Q=x^2 \\
& \text { I.F }=e^{\int \frac{2}{x} d x}=e^{\log x^2}=x^2
\end{aligned}
$$
Solution is
$$
\begin{aligned}
& y \cdot x^2=\int x^2 \cdot x^2 d x+c=\frac{x^5}{5}+c \\
& y=\frac{x^3}{5}+c x^{-2}
\end{aligned}
$$

</details>

---

### Q127. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $y(x)$ be a solution of $\frac{(2+\sin x}{(1+y)} \frac{d y)}{d x}=\cos x$. If $y(0)=2$, then $y\left(\frac{\pi}{2}\right)$ equals

**Options:**

- **(A)** $\frac{5}{2}$
- **(B)** 2
- **(C)** $\frac{7}{2}$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{2}$**

**Detailed Solution:**

Given differential equation is
$$
\frac{(2+\sin x}{(1+y)} \cdot \frac{d y}{d x}=\cos x
$$
which can be rewritten as
$$
\frac{d y}{1+y}=\frac{\cos x}{2+\sin x} d x
$$
Integrate both the sides, we get
$$
\begin{aligned}
& \int \frac{d y}{1+y}=\int \frac{\cos x d x}{2+\sin x} \\
& \Rightarrow \log (1+y)=\log (2+\sin x)+\log C \\
& \Rightarrow 1+y=C(2+\sin x) \\
& \text { Given } y(0)=2 \\
& \Rightarrow 1+2=C[2+\sin 0] \Rightarrow C=\frac{3}{2}
\end{aligned}
$$
Now, $y\left(\frac{\pi}{2}\right)$ can be found as
$$
1+y=\frac{3}{2}\left(2+\sin \frac{\pi}{2}\right) \Rightarrow 1+y=\frac{9}{2}
$$
$$
\Rightarrow \quad y=\frac{7}{2}
$$
Hence, $y\left(\frac{\pi}{2}\right)=\frac{7}{2}$

</details>

---

### Q128. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `3`

Solution of the differential equation $\cos x d y=y(\sin x-y) d x, 0 < x < \frac{\pi}{2}$ is

**Options:**

- **(A)** $y \sec x=\tan x+c$
- **(B)** $y \tan x=\sec x+c$
- **(C)** $\tan x=(\sec x+c) y$
- **(D)** $\sec x=(\tan x+c) y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sec x=(\tan x+c) y$**

**Detailed Solution:**

$$
\begin{aligned}
& \cos x d y=y(\sin x-y) d x \\
& \frac{d y}{d x}=y \tan x-y^2 \sec x \\
& \frac{1}{y^2} \frac{d y}{d x}-\frac{1}{y} \tan x=-\sec x \\
& \text { Let } \frac{1}{y}=t \\
& -\frac{1}{y^2} \frac{d y}{d x}=\frac{d t}{d x} \\
& -\frac{d y}{d x}-t \tan x=-\sec x \Rightarrow \frac{d t}{d x}+(\tan x) t=\sec x . \\
& \text { I.F. }=e^{f \tan x d x}=\sec x
\end{aligned}
$$
Solution is $t\left(\right.$ I.F) $=\int$ (I.F) $\sec x d x$
$\frac{1}{y} \sec x=\tan x+c$

</details>

---

### Q129. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

The solution of the differential equation $y d x+\left(x+x^2 y\right) d y=0$ is

**Options:**

- **(A)** $-\frac{1}{x y}=C$
- **(B)** $-\frac{1}{x y}+\log y=C$
- **(C)** $\frac{1}{x y}+\log y=C$
- **(D)** $\log y=C x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{1}{x y}+\log y=C$**

**Detailed Solution:**

$y d x+x d y+x^2 y d y=0$
$\frac{d(x y)}{x^2 y^2}+\frac{1}{y} d y=0 \Rightarrow-\frac{1}{x y}+\log y=C$

</details>

---

### Q130. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

The solution of the differential equation $\left(1+y^2\right)+\left(x-e^{\tan ^{-1} y}\right) \frac{d y}{d x}=0$, is

**Options:**

- **(A)** $x e^{2 \tan ^{-1} y}=e^{\tan ^{-1} y}+k$
- **(B)** $(x-2)=k e^{2 \tan ^{-1} y}$
- **(C)** $2 x e^{\tan ^{-1} y}=e^{2 \tan ^{-1} y}+k$
- **(D)** $x e^{\tan ^{-1} y}=\tan ^{-1} y+k$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 x e^{\tan ^{-1} y}=e^{2 \tan ^{-1} y}+k$**

**Detailed Solution:**

$\left(1+y^2\right)+\left(x-e^{\tan ^{-1} y}\right) \frac{d y}{d x}=0$
$\left(1+y^2\right) \frac{d x}{d y}+x=e^{\tan ^{-1} y} \Rightarrow \frac{d x}{d y}+\frac{x}{\left(1+y^2\right)}=\frac{e^{\tan ^{-1} y}}{\left(1+y^2\right)}$
I.F. $=e^{\int \frac{1}{\left(1+y^2\right)} d y}=e \tan ^{-1} y$
$x\left(e^{\tan ^{-1} y}\right)=\int \frac{e^{\tan ^{-1} y}}{1+y} e^{\tan ^{-1} y d y}$
$x\left(e^{\tan ^{-1} y}\right)=\frac{e^{2 \tan ^{-1} y}}{2}+C \quad \therefore 2 x e^{\tan ^{-1} y}=e^{2 \tan ^{-1} y}+k$

</details>

---

