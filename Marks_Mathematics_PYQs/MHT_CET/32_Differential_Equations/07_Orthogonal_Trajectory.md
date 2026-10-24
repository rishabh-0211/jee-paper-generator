# MHT CET Mathematics - Differential Equations

## Topic 7: Orthogonal Trajectory

**Total Questions:** 4

---

### Q1. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of a curve whose normal at any point has a slope which is the same as the ordinate and which passes through $(1,-1)$ is $2 x=\mathrm{k}\left(3-\mathrm{y}^2\right)$. Then k is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

Let the equation of the curve be $y = f(x)$.

The slope of the tangent at any point $(x, y)$ is $\dfrac{dy}{dx}$.

The slope of the normal at any point $(x, y)$ is $-\dfrac{dx}{dy}$.

Given that the slope of the normal is equal to the ordinate, we have:

$-\dfrac{dx}{dy} = y$

$dx = -y dy$

Integrating both sides, we get:

$\int dx = -\int y dy$

$x = -\dfrac{y^2}{2} + C$

$2x = -y^2 + 2C$

Since the curve passes through the point $(1, -1)$, we substitute $x = 1$ and $y = -1$:

$2(1) = -(-1)^2 + 2C$

$2 = -1 + 2C$

$2C = 3$

Substituting $2C = 3$ back into the equation of the curve, we get:

$2x = -y^2 + 3$

$2x = 1(3 - y^2)$

Comparing this with the given equation $2x = k(3 - y^2)$, we find:

$k = 1$

Answer: 1

</details>

---

### Q2. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $y=y(x)$ be the solution of the differential equation $(x \log x) \frac{\mathrm{d} y}{\mathrm{~d} x}+y=2 x \log x(x \geq 1)$ then $y(\mathrm{e})$ is equal to

**Options:**

- **(A)** 2
- **(B)** 2 e
- **(C)** e
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

The given differential equation is:

$(x \log x) \dfrac{\mathrm{d} y}{\mathrm{d} x} + y = 2 x \log x$

Dividing by $x \log x$, we get:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} + \dfrac{1}{x \log x} y = 2$

This is a linear differential equation of the form $\dfrac{\mathrm{d} y}{\mathrm{d} x} + P y = Q$, where $P = \dfrac{1}{x \log x}$ and $Q = 2$.

Integrating Factor (IF) = $e^{\int P \mathrm{d} x} = e^{\int \dfrac{1}{x \log x} \mathrm{d} x}$

Let $\log x = t \Rightarrow \dfrac{1}{x} \mathrm{d} x = \mathrm{d} t$

$\int \dfrac{1}{t} \mathrm{d} t = \log t = \log(\log x)$

So, IF = $e^{\log(\log x)} = \log x$

The general solution is given by:

$y \cdot (\text{IF}) = \int Q \cdot (\text{IF}) \mathrm{d} x + C$

$y \log x = \int 2 \log x \mathrm{d} x + C$

Using integration by parts:

$y \log x = 2 (x \log x - x) + C$

Since the solution is valid for $x \geq 1$, the function $y(x)$ must be defined at $x = 1$. Substituting $x = 1$ in the original differential equation $(x \log x) y' + y = 2 x \log x$, we get $y(1) = 0$.

Substituting $x = 1$ and $y = 0$ in the general solution:

$0 \cdot \log 1 = 2(1 \cdot \log 1 - 1) + C$

$0 = 2(0 - 1) + C \Rightarrow C = 2$

Thus, the particular solution is:

$y \log x = 2x \log x - 2x + 2$

To find $y(e)$, substitute $x = e$:

$y(e) \log e = 2e \log e - 2e + 2$

$y(e) \cdot 1 = 2e(1) - 2e + 2$

$y(e) = 2$

Answer: 2

</details>

---

### Q3. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all circles, passing through the origin and having their centres on the X-axis, is

**Options:**

- **(A)** $y^2=x^2+x y \frac{\mathrm{d} y}{\mathrm{~d} x}$
- **(B)** $x^2=y^2+2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}$
- **(C)** $y^2=x^2+2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}$
- **(D)** $x^2=y^2-x y \frac{\mathrm{d} y}{\mathrm{~d} x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y^2=x^2+2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}$**

**Detailed Solution:**

The system of circles which passes through origin and whose centre lies on $\mathrm{X}$-axis is $x^2+y^2-2 b x=0... (i)$
Differentiating w.r.t $x$, we get
$2 x+2 y \frac{\mathrm{d} y}{\mathrm{~d} x}=2 \mathrm{~b}... (ii)$
Substituting (ii) in (i), we get
$\begin{aligned}
& x^2+y^2-2 x^2-2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& \Rightarrow y^2-x^2-2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}=0 \\
& \Rightarrow y^2=x^2+2 x y \frac{\mathrm{d} y}{\mathrm{~d} x}
\end{aligned}$

</details>

---

### Q4. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation of all lines perpendicular to the line $5 x+2 y+7=0$ is

**Options:**

- **(A)** 3dy-2dx=0
- **(B)** 2dy-5dx=0
- **(C)** 2dy-3dx=0
- **(D)** 5dy-2dx=0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5dy-2dx=0**

**Detailed Solution:**

(C)
Given line $5 x+2 y+7=0$ has slope $\frac{-5}{2}$. Hence eq. of required line is
$\begin{aligned}
& y=\frac{2}{5} x+c \Rightarrow 2 x-5 y+c=0 \\
\therefore & 2-5 \frac{d y}{d x}=0 \Rightarrow 2=5 \frac{d y}{d x} \Rightarrow 2 d x=5 d y \Rightarrow 5 d y-2 d x=0
\end{aligned}$

</details>

---

