# MHT CET Mathematics - Differential Equations

## Topic 4: Homogeneous DE

**Total Questions:** 32

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x\dfrac{dy}{dx} = y(\log y - \log x + 1)$ and its solution is $y = [h(x)]e^{cx}$, then $h(x) = \ldots$

**Options:**

- **(A)** $2x$
- **(B)** $x$
- **(C)** $\log x$
- **(D)** $\dfrac{1}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x$**

**Detailed Solution:**

The given differential equation is $x\dfrac{dy}{dx} = y(\log y - \log x + 1)$.

This can be rewritten as:

$\dfrac{dy}{dx} = \dfrac{y}{x} \left( \log\left(\dfrac{y}{x}\right) + 1 \right)$

Let $y = vx$. Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = v + x\dfrac{dv}{dx}$

Substituting this into the differential equation:

$v + x\dfrac{dv}{dx} = v (\log v + 1)$

$v + x\dfrac{dv}{dx} = v \log v + v$

$x\dfrac{dv}{dx} = v \log v$

Separating the variables:

$\dfrac{dv}{v \log v} = \dfrac{dx}{x}$

Integrating both sides:

$\int \dfrac{dv}{v \log v} = \int \dfrac{dx}{x}$

$\log(\log v) = \log x + C$

$\log v = e^{\log x + C} = e^C x$

Let $e^C = c$, an arbitrary constant. Then:

$\log v = cx$

Substituting $v = \dfrac{y}{x}$:

$\log\left(\dfrac{y}{x}\right) = cx$

$\dfrac{y}{x} = e^{cx}$

$y = x e^{cx}$

Comparing this with the given solution $y = [h(x)]e^{cx}$, we get:

$h(x) = x$

Answer: $x$

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $x^2 y\,dx - (x^3 + y^3)\,dy = 0$ is

**Options:**

- **(A)** $\log|y| - \dfrac{x^3}{2y^3} = c$
- **(B)** $\log|y| + \dfrac{x^3}{2y^3} = c$
- **(C)** $\log|y| - \dfrac{x^3}{4y^3} = c$
- **(D)** $\log|y| - \dfrac{x^3}{3y^3} = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log|y| - \dfrac{x^3}{3y^3} = c$**

**Detailed Solution:**

The given differential equation can be written as:

$\dfrac{dx}{dy} = \dfrac{x^3 + y^3}{x^2 y}$

This is a homogeneous differential equation. Substituting $x = vy$, we get:

$\dfrac{dx}{dy} = v + y\dfrac{dv}{dy}$

Substituting this into the differential equation:

$v + y\dfrac{dv}{dy} = \dfrac{v^3 y^3 + y^3}{v^2 y^3}$

$v + y\dfrac{dv}{dy} = \dfrac{v^3 + 1}{v^2}$

$v + y\dfrac{dv}{dy} = v + \dfrac{1}{v^2}$

$y\dfrac{dv}{dy} = \dfrac{1}{v^2}$

Separating the variables:

$v^2\,dv = \dfrac{dy}{y}$

Integrating both sides:

$\int v^2\,dv = \int \dfrac{dy}{y}$

$\dfrac{v^3}{3} = \log|y| - c$

Substituting $v = \dfrac{x}{y}$ back into the equation:

$\dfrac{x^3}{3y^3} = \log|y| - c$

$\log|y| - \dfrac{x^3}{3y^3} = c$

Answer: $\log|y| - \dfrac{x^3}{3y^3} = c$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the general solution of the differential equation $y\sec^2\left(\dfrac{x}{y}\right)dx - \left(x\sec^2\left(\dfrac{x}{y}\right) - y\right)dy = 0$ is $\tan\left(\dfrac{x}{y}\right) + g(y) = c$, then $g(y) = \ldots$

**Options:**

- **(A)** $\log|y|$
- **(B)** $\tan\sqrt{y}$
- **(C)** $\cos 2y$
- **(D)** $3y^2 + 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log|y|$**

**Detailed Solution:**

The given differential equation is $y\sec^2\left(\dfrac{x}{y}\right)dx - \left(x\sec^2\left(\dfrac{x}{y}\right) - y\right)dy = 0$

Rearranging the terms, we get:

$y\sec^2\left(\dfrac{x}{y}\right)dx - x\sec^2\left(\dfrac{x}{y}\right)dy + y dy = 0$

Dividing the entire equation by $y^2$, we obtain:

$\sec^2\left(\dfrac{x}{y}\right)\left(\dfrac{y dx - x dy}{y^2}\right) + \dfrac{dy}{y} = 0$

Using the quotient rule for differentials, $d\left(\dfrac{x}{y}\right) = \dfrac{y dx - x dy}{y^2}$, the equation can be written as:

$\sec^2\left(\dfrac{x}{y}\right)d\left(\dfrac{x}{y}\right) + \dfrac{dy}{y} = 0$

Integrating both sides, we get:

$\int \sec^2\left(\dfrac{x}{y}\right)d\left(\dfrac{x}{y}\right) + \int \dfrac{dy}{y} = c$

$\tan\left(\dfrac{x}{y}\right) + \log|y| = c$

Comparing this with the given general solution $\tan\left(\dfrac{x}{y}\right) + g(y) = c$, we find:

$g(y) = \log|y|$

Answer: $\log|y|$

</details>

---

### Q4. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f(x)$ satisfying the equation $[f'(x)]^2 + 4f(x)f'(x) + f^2(x) = 0$, then $f(x) = $
(where $c$ is constant of integration)

**Options:**

- **(A)** $c \cdot e^{(2 \pm \sqrt{3})x}$
- **(B)** $c \cdot e^{(-3 \pm \sqrt{2})x}$
- **(C)** $c \cdot e^{(-2 \pm \sqrt{3})x}$
- **(D)** $c \cdot e^{(3 \pm \sqrt{2})x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $c \cdot e^{(-2 \pm \sqrt{3})x}$**

**Detailed Solution:**

Given the differential equation:

$[f'(x)]^2 + 4f(x)f'(x) + f^2(x) = 0$

This is a quadratic equation in $f'(x)$. Solving for $f'(x)$ using the quadratic formula:

$f'(x) = \dfrac{-4f(x) \pm \sqrt{16f^2(x) - 4(1)(f^2(x))}}{2}$

$f'(x) = \dfrac{-4f(x) \pm \sqrt{12f^2(x)}}{2}$

$f'(x) = \dfrac{-4f(x) \pm 2\sqrt{3}f(x)}{2}$

$f'(x) = (-2 \pm \sqrt{3})f(x)$

Separating the variables:

$\dfrac{f'(x)}{f(x)} = -2 \pm \sqrt{3}$

Integrating both sides with respect to $x$:

$\int \dfrac{f'(x)}{f(x)} dx = \int (-2 \pm \sqrt{3}) dx$

$\ln |f(x)| = (-2 \pm \sqrt{3})x + C$

$f(x) = e^{(-2 \pm \sqrt{3})x + C}$

$f(x) = e^C \cdot e^{(-2 \pm \sqrt{3})x}$

Replacing $e^C$ with a new constant $c$:

$f(x) = c \cdot e^{(-2 \pm \sqrt{3})x}$

Answer: $c \cdot e^{(-2 \pm \sqrt{3})x}$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $y^2 - x^2 \dfrac{dy}{dx} = xy \dfrac{dy}{dx}$ is ...

**Options:**

- **(A)** $\dfrac{y}{x} + \log|y| = c$
- **(B)** $\dfrac{y}{x} + \log|x| = c$
- **(C)** $\dfrac{y^2}{x} + \log|y| = c$
- **(D)** $\dfrac{y}{x^2} + \log|y| = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{y}{x} + \log|y| = c$**

**Detailed Solution:**

The given differential equation is $y^2 - x^2 \dfrac{dy}{dx} = xy \dfrac{dy}{dx}$

Rearranging the terms, we get:

$\dfrac{dy}{dx} = \dfrac{y^2}{x^2 + xy}$

This is a homogeneous differential equation. Substitute $y = vx$, which gives $\dfrac{dy}{dx} = v + x \dfrac{dv}{dx}$

$v + x \dfrac{dv}{dx} = \dfrac{v^2 x^2}{x^2 + v x^2} = \dfrac{v^2}{1 + v}$

$x \dfrac{dv}{dx} = \dfrac{v^2}{1 + v} - v = \dfrac{v^2 - v - v^2}{1 + v} = \dfrac{-v}{1 + v}$

Separating the variables:

$\dfrac{1 + v}{v} dv = -\dfrac{dx}{x}$

$\left( \dfrac{1}{v} + 1 \right) dv = -\dfrac{dx}{x}$

Integrating both sides:

$\int \left( \dfrac{1}{v} + 1 \right) dv = -\int \dfrac{dx}{x}$

$\log|v| + v = -\log|x| + c$

Substituting $v = \dfrac{y}{x}$:

$\log\left|\dfrac{y}{x}\right| + \dfrac{y}{x} = -\log|x| + c$

$\log|y| - \log|x| + \dfrac{y}{x} = -\log|x| + c$

$\dfrac{y}{x} + \log|y| = c$

Answer: $\dfrac{y}{x} + \log|y| = c$

</details>

---

### Q6. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} = \dfrac{x - y}{x + y}$, when $x = 0$ and $y = 0$ represents ....

**Options:**

- **(A)** Circle
- **(B)** Ellipse
- **(C)** Hyperbola
- **(D)** Pair of straight Lines

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Pair of straight Lines**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{x - y}{x + y}$

Rearranging the terms, we get:

$(x + y)dy = (x - y)dx$

$x dy + y dy = x dx - y dx$

$x dy + y dx = x dx - y dy$

This can be written as exact differentials:

$d(xy) = x dx - y dy$

Integrating both sides, we get:

$\int d(xy) = \int x dx - \int y dy$

$xy = \dfrac{x^2}{2} - \dfrac{y^2}{2} + C$

$x^2 - 2xy - y^2 = -2C$

Given that $x = 0$ when $y = 0$, substituting these values gives:

$0^2 - 2(0)(0) - 0^2 = -2C \Rightarrow C = 0$

Substituting $C = 0$ back into the equation, we obtain:

$x^2 - 2xy - y^2 = 0$

This is a homogeneous equation of degree 2 in $x$ and $y$ (of the form $ax^2 + 2hxy + by^2 = 0$), which represents a pair of straight lines passing through the origin.

Answer: Pair of straight Lines

</details>

---

### Q7. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the differential equation $(x^2 + y^2)\,dy = xy\,dx$, it is given that $y(1) = 1$ and $y(x_0) = e$, then the value of $x_0$ is _____

**Options:**

- **(A)** $e$
- **(B)** $\pm\sqrt{3}\,e$
- **(C)** $3e^2$
- **(D)** $e^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pm\sqrt{3}\,e$**

**Detailed Solution:**

The given differential equation is $(x^2 + y^2)dy = xy dx$.

This can be rewritten as $\dfrac{dx}{dy} = \dfrac{x^2 + y^2}{xy} = \dfrac{x}{y} + \dfrac{y}{x}$.

Let $x = vy$, then $\dfrac{dx}{dy} = v + y\dfrac{dv}{dy}$.

Substituting this into the differential equation, we get:

$v + y\dfrac{dv}{dy} = v + \dfrac{1}{v}$

$y\dfrac{dv}{dy} = \dfrac{1}{v}$

$v dv = \dfrac{dy}{y}$

Integrating both sides, we get:

$\dfrac{v^2}{2} = \ln|y| + C$

Substituting $v = \dfrac{x}{y}$:

$\dfrac{x^2}{2y^2} = \ln|y| + C$

Given $y(1) = 1$, substituting $x = 1$ and $y = 1$:

$\dfrac{1}{2} = \ln(1) + C \Rightarrow C = \dfrac{1}{2}$

The particular solution is:

$\dfrac{x^2}{2y^2} = \ln|y| + \dfrac{1}{2}$

We are given $y(x_0) = e$, so substituting $x = x_0$ and $y = e$:

$\dfrac{x_0^2}{2e^2} = \ln(e) + \dfrac{1}{2}$

$\dfrac{x_0^2}{2e^2} = 1 + \dfrac{1}{2} = \dfrac{3}{2}$

$x_0^2 = 3e^2$

$x_0 = \pm\sqrt{3}e$

Answer: $\pm\sqrt{3}\,e$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through the point (0, 1) and having a slope of the tangent at point $P(x, y)$ is equal to $\dfrac{y}{x + y}$, is

**Options:**

- **(A)** $x = e^{-\frac{y}{x}}$
- **(B)** $y = e^{-\frac{y}{x}} + 1$
- **(C)** $x = e^{\frac{x}{y}} - 1$
- **(D)** $y = e^{\frac{x}{y}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y = e^{\frac{x}{y}}$**

**Detailed Solution:**

Given the slope of the tangent is $\dfrac{dy}{dx} = \dfrac{y}{x + y}$

Taking the reciprocal, we get:

$\dfrac{dx}{dy} = \dfrac{x + y}{y}$

$\Rightarrow \dfrac{dx}{dy} - \dfrac{x}{y} = 1$

This is a linear differential equation of the form $\dfrac{dx}{dy} + Px = Q$, where $P = -\dfrac{1}{y}$ and $Q = 1$.

Integrating Factor (IF) $= e^{\int -\dfrac{1}{y} dy} = e^{-\ln y} = \dfrac{1}{y}$

The solution is given by:

$x \cdot (\text{IF}) = \int Q \cdot (\text{IF}) dy + C$

$\Rightarrow x \left(\dfrac{1}{y}\right) = \int \dfrac{1}{y} dy + C$

$\Rightarrow \dfrac{x}{y} = \ln y + C$

Since the curve passes through the point $(0, 1)$, substitute $x = 0$ and $y = 1$:

$\dfrac{0}{1} = \ln 1 + C \Rightarrow C = 0$

Therefore, the equation of the curve is:

$\dfrac{x}{y} = \ln y$

$\Rightarrow y = e^{\dfrac{x}{y}}$

Answer: $y = e^{\frac{x}{y}}$

</details>

---

### Q9. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} = \dfrac{x+y}{x-y}$ is

**Options:**

- **(A)** $c(x^2 + y^2)^{\frac{1}{2}} + e^{\tan^{-1}\left(\frac{y^2}{x}\right)} = 0$, where c is an arbitrary constant
- **(B)** $c(x^2 + y^2)^{\frac{1}{2}} = e^{\tan^{-1}\left(\frac{y}{x}\right)}$, where c is an arbitrary constant
- **(C)** $c(x^2 - y^2) = e^{\tan^{-1}\left(\frac{y}{x}\right)}$, where c is an arbitrary constant
- **(D)** $c(x^2 + y^2) = e^{\tan^{-1}\left(\frac{y}{x}\right)}$, where c is an arbitrary constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $c(x^2 + y^2)^{\frac{1}{2}} = e^{\tan^{-1}\left(\frac{y}{x}\right)}$, where c is an arbitrary constant**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{x+y}{x-y}$.

Substituting $y = vx$, we get $\dfrac{dy}{dx} = v + x\dfrac{dv}{dx}$.

$v + x\dfrac{dv}{dx} = \dfrac{x+vx}{x-vx} = \dfrac{1+v}{1-v}$

$x\dfrac{dv}{dx} = \dfrac{1+v}{1-v} - v = \dfrac{1+v-v+v^2}{1-v} = \dfrac{1+v^2}{1-v}$

Separating the variables, we get:

$\dfrac{1-v}{1+v^2} dv = \dfrac{dx}{x}$

Integrating both sides:

$\int \dfrac{1}{1+v^2} dv - \int \dfrac{v}{1+v^2} dv = \int \dfrac{dx}{x}$

$\tan^{-1}v - \dfrac{1}{2}\ln(1+v^2) = \ln|x| + C$

Substituting $v = \dfrac{y}{x}$:

$\tan^{-1}\left(\dfrac{y}{x}\right) - \dfrac{1}{2}\ln\left(1+\dfrac{y^2}{x^2}\right) = \ln|x| + C$

$\tan^{-1}\left(\dfrac{y}{x}\right) - \dfrac{1}{2}\ln\left(\dfrac{x^2+y^2}{x^2}\right) = \ln|x| + C$

$\tan^{-1}\left(\dfrac{y}{x}\right) - \dfrac{1}{2}\ln(x^2+y^2) + \ln|x| = \ln|x| + C$

$\tan^{-1}\left(\dfrac{y}{x}\right) - \dfrac{1}{2}\ln(x^2+y^2) = C$

$\ln(x^2+y^2)^{\dfrac{1}{2}} = \tan^{-1}\left(\dfrac{y}{x}\right) - C$

$(x^2+y^2)^{\dfrac{1}{2}} = e^{\tan^{-1}\left(\dfrac{y}{x}\right) - C}$

$e^C (x^2+y^2)^{\dfrac{1}{2}} = e^{\tan^{-1}\left(\dfrac{y}{x}\right)}$

Letting $c = e^C$, we obtain:

$c(x^2+y^2)^{\dfrac{1}{2}} = e^{\tan^{-1}\left(\dfrac{y}{x}\right)}$

Answer: $c(x^2 + y^2)^{\frac{1}{2}} = e^{\tan^{-1}\left(\frac{y}{x}\right)}$, where c is an arbitrary constant

</details>

---

### Q10. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The slope of the tangent at $(x, y)$ to the curve passing through $(2,1)$ is $\frac{x^2+y^2}{2 x y}$, then the equation of the curve is

**Options:**

- **(A)** $2(x^2-y^2)=3x$
- **(B)** $2(x^2+y^2)=3x$
- **(C)** $x^2-y^2=3x$
- **(D)** $x^2+y^2=3x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2(x^2-y^2)=3x$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{x^2+y^2}{2xy}$.

Rearranging the terms:

$2xy \, dy = (x^2+y^2) \, dx$

$2xy \, dy - y^2 \, dx = x^2 \, dx$

Dividing both sides by $x^2$:

$\dfrac{x(2y \, dy) - y^2 \, dx}{x^2} = dx$

$d\left(\dfrac{y^2}{x}\right) = dx$

Integrating both sides:

$\dfrac{y^2}{x} = x + C$

$y^2 = x^2 + Cx$

$x^2 - y^2 = -Cx$

Since the curve passes through $(2,1)$, substitute $x=2$ and $y=1$:

$2^2 - 1^2 = -C(2)$

$3 = -2C \Rightarrow -C = \dfrac{3}{2}$

Therefore, the equation of the curve is $x^2 - y^2 = \dfrac{3}{2}x$, which simplifies to $2(x^2 - y^2) = 3x$.

Answer: $2(x^2-y^2)=3x$

</details>

---

### Q11. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of differential equation $\left(y^2-x^2\right) \mathrm{d} x=x y$ dy $(x \neq 0)$ is

**Options:**

- **(A)** $2 x^2 \log x+\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration
- **(B)** $2 x^2 \log x-\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration
- **(C)** $x^2 \log x+\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration
- **(D)** $x^2 \log x-\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 x^2 \log x+\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration**

**Detailed Solution:**

The given differential equation is $(y^2 - x^2) \mathrm{d}x = xy \mathrm{d}y$.

Rearranging the terms, we get:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{y^2 - x^2}{xy}$

This is a homogeneous differential equation. Substitute $y = vx$, which gives $\dfrac{\mathrm{d}y}{\mathrm{d}x} = v + x \dfrac{\mathrm{d}v}{\mathrm{d}x}$.

Substituting these into the differential equation:

$v + x \dfrac{\mathrm{d}v}{\mathrm{d}x} = \dfrac{v^2 x^2 - x^2}{vx^2}$

$v + x \dfrac{\mathrm{d}v}{\mathrm{d}x} = \dfrac{v^2 - 1}{v}$

$x \dfrac{\mathrm{d}v}{\mathrm{d}x} = \dfrac{v^2 - 1}{v} - v$

$x \dfrac{\mathrm{d}v}{\mathrm{d}x} = \dfrac{v^2 - 1 - v^2}{v}$

$x \dfrac{\mathrm{d}v}{\mathrm{d}x} = -\dfrac{1}{v}$

Separating the variables:

$v \mathrm{d}v = -\dfrac{\mathrm{d}x}{x}$

Integrating both sides:

$\int v \mathrm{d}v = -\int \dfrac{1}{x} \mathrm{d}x$

$\dfrac{v^2}{2} = -\log x - c$

Substituting back $v = \dfrac{y}{x}$:

$\dfrac{y^2}{2x^2} = -\log x - c$

Multiplying the entire equation by $2x^2$:

$y^2 = -2x^2 \log x - 2cx^2$

$2x^2 \log x + y^2 + 2cx^2 = 0$

Answer: $2 x^2 \log x+\mathrm{y}^2+2 \mathrm{c} x^2=0$, where c is the constant of integration

</details>

---

### Q12. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x \frac{\mathrm{dy}}{\mathrm{d} x}=\mathrm{y}(\log \mathrm{y}-\log x+1)$, then the solution of the equation is

**Options:**

- **(A)** $\log \frac{x}{\mathrm{y}}=\mathrm{cy}$, where c is the constant of integration
- **(B)** $\log \frac{\mathrm{y}}{x}=\mathrm{cy}$, where c is the constant of integration
- **(C)** $\log \frac{x}{\mathrm{y}}=\mathrm{c} x$, where c is the constant of integration
- **(D)** $\log \frac{\mathrm{y}}{x}=\mathrm{c} x$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \frac{\mathrm{y}}{x}=\mathrm{c} x$, where c is the constant of integration**

**Detailed Solution:**

The given differential equation is:

$x \dfrac{\mathrm{dy}}{\mathrm{d} x} = \mathrm{y}(\log \mathrm{y} - \log x + 1)$

Dividing both sides by $x$, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{\mathrm{y}}{x} \left( \log \left( \dfrac{\mathrm{y}}{x} \right) + 1 \right)$

This is a homogeneous differential equation. Substitute $\mathrm{y} = v x$, which gives $\dfrac{\mathrm{dy}}{\mathrm{d} x} = v + x \dfrac{\mathrm{dv}}{\mathrm{d} x}$.

Substituting these into the equation:

$v + x \dfrac{\mathrm{dv}}{\mathrm{d} x} = v (\log v + 1)$

$v + x \dfrac{\mathrm{dv}}{\mathrm{d} x} = v \log v + v$

$x \dfrac{\mathrm{dv}}{\mathrm{d} x} = v \log v$

Separating the variables:

$\dfrac{\mathrm{dv}}{v \log v} = \dfrac{\mathrm{d} x}{x}$

Integrating both sides:

$\int \dfrac{1}{v \log v} \mathrm{dv} = \int \dfrac{1}{x} \mathrm{d} x$

$\log(\log v) = \log x + \log \mathrm{c}$

$\log(\log v) = \log(\mathrm{c} x)$

$\log v = \mathrm{c} x$

Substituting back $v = \dfrac{\mathrm{y}}{x}$:

$\log \left( \dfrac{\mathrm{y}}{x} \right) = \mathrm{c} x$

Answer: $\log \frac{\mathrm{y}}{x}=\mathrm{c} x$, where c is the constant of integration

</details>

---

### Q13. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $x=\sec \theta-\cos \theta, y=\sec ^{10} \theta-\cos ^{10} \theta$ and $\left(x^2+4\right)\left(\dfrac{\mathrm{d} y}{\mathrm{~d} x}\right)^2=\mathrm{k}\left(y^2+4\right)$, then the value of k is

**Options:**

- **(A)** $\dfrac{1}{100}$
- **(B)** 1
- **(C)** 10
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 100**

**Detailed Solution:**

Given $x = \sec \theta - \cos \theta$ and $y = \sec^{10} \theta - \cos^{10} \theta$.

Squaring and adding $4$ to both expressions:

$x^2 + 4 = (\sec \theta - \cos \theta)^2 + 4 = \sec^2 \theta + \cos^2 \theta - 2 + 4 = \sec^2 \theta + \cos^2 \theta + 2 = (\sec \theta + \cos \theta)^2$

$y^2 + 4 = (\sec^{10} \theta - \cos^{10} \theta)^2 + 4 = \sec^{20} \theta + \cos^{20} \theta - 2 + 4 = \sec^{20} \theta + \cos^{20} \theta + 2 = (\sec^{10} \theta + \cos^{10} \theta)^2$

Differentiating $x$ and $y$ with respect to $\theta$:

$\dfrac{\mathrm{d}x}{\mathrm{d}\theta} = \sec \theta \tan \theta + \sin \theta = \tan \theta (\sec \theta + \cos \theta)$

$\dfrac{\mathrm{d}y}{\mathrm{d}\theta} = 10 \sec^9 \theta (\sec \theta \tan \theta) - 10 \cos^9 \theta (-\sin \theta) = 10 \sec^{10} \theta \tan \theta + 10 \cos^9 \theta \sin \theta = 10 \tan \theta (\sec^{10} \theta + \cos^{10} \theta)$

Dividing the two derivatives to find $\dfrac{\mathrm{d}y}{\mathrm{d}x}$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{d}y}{\mathrm{d}\theta}}{\dfrac{\mathrm{d}x}{\mathrm{d}\theta}} = \dfrac{10 \tan \theta (\sec^{10} \theta + \cos^{10} \theta)}{\tan \theta (\sec \theta + \cos \theta)} = \dfrac{10 (\sec^{10} \theta + \cos^{10} \theta)}{\sec \theta + \cos \theta}$

Squaring both sides and multiplying by $x^2 + 4$:

$(x^2 + 4) \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^2 = (\sec \theta + \cos \theta)^2 \times \dfrac{100 (\sec^{10} \theta + \cos^{10} \theta)^2}{(\sec \theta + \cos \theta)^2}$

$(x^2 + 4) \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^2 = 100 (\sec^{10} \theta + \cos^{10} \theta)^2$

Substituting $y^2 + 4 = (\sec^{10} \theta + \cos^{10} \theta)^2$:

$(x^2 + 4) \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^2 = 100 (y^2 + 4)$

Comparing this with the given equation $(x^2 + 4) \left(\dfrac{\mathrm{d}y}{\mathrm{d}x}\right)^2 = \mathrm{k}(y^2 + 4)$, we get $\mathrm{k} = 100$.

Answer: 100

</details>

---

### Q14. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $(2 x-2 y+3) \mathrm{d} x-(x-y+1) \mathrm{d} y=0$ when $x=0, y=1$ is

**Options:**

- **(A)** $x-2 y-\log (x-y+2)+2=0$
- **(B)** $x-y-\log (x-y+2)+1=0$
- **(C)** $2 x+y-\log (x-y+2)-1=0$
- **(D)** $2 x-y-\log (x-y+2)+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 x-y-\log (x-y+2)+1=0$**

**Detailed Solution:**

Let $x-y+1=v$
$\begin{aligned}
& \Rightarrow 1-\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\mathrm{d} v}{\mathrm{~d} x} \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=1-\frac{\mathrm{d} v}{\mathrm{~d} x} \\
& \text { now } \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{2 x-2 y+3}{x-y+1} \\
& \Rightarrow 1-\frac{\mathrm{d} v}{\mathrm{~d} x}=\frac{2 v+1}{v} \\
& \Rightarrow \frac{\mathrm{d} v}{\mathrm{~d} x}=1-\frac{2 v+1}{v}=\frac{-(v+1)}{v} \\
& \Rightarrow \frac{v}{v+1} \mathrm{~d} v=-\mathrm{d} x \\
& \Rightarrow \int\left(1-\frac{1}{v+1}\right) \mathrm{d} v=-\int \mathrm{d} x \\
& \Rightarrow n-\log |n+1|=-x+c \\
& \Rightarrow(x-y+1)-\log (x-y+1+1)=-x+c \\
& \Rightarrow 2 x-y+1+\log (x-y+2)=c
\end{aligned}$
$\begin{aligned} & \text { for } x=0, y=1 ; c=0 \\ & \Rightarrow 2 x-y-\log (x-y+2)+1=0\end{aligned}$

</details>

---

### Q15. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation $y^{\prime}=\frac{y}{x+\sqrt{x y}}$ has general solution given by (Where $C$ is a constant of integration.)

**Options:**

- **(A)** $y=C e^{2 \sqrt{x y}}$
- **(B)** $y=C e^{2\left(\sqrt{\frac{y}{x}}\right)}$
- **(C)** $y=C e^{2\left(\sqrt{\frac{x}{y}}\right)}$
- **(D)** $y=C e^{-2 \sqrt{x y}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=C e^{2\left(\sqrt{\frac{x}{y}}\right)}$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{y}{x+\sqrt{x y}} \text { let } y=v x \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=v+x \cdot \frac{\mathrm{d} v}{\mathrm{~d} x} \\ & \Rightarrow v+x \cdot \frac{\mathrm{d} v}{\mathrm{~d} x}=\frac{v x}{x+\sqrt{x \cdot v x}}=\frac{v}{1+\sqrt{v}} \\ & \Rightarrow x \cdot \frac{\mathrm{d} v}{\mathrm{~d} x}=\frac{v}{1+\sqrt{v}}-v=\frac{-v \sqrt{v}}{1+\sqrt{v}} \\ & \Rightarrow-\frac{1+\sqrt{v}}{v \sqrt{v}} \mathrm{~d} v=\frac{\mathrm{d} x}{x} \\ & \Rightarrow-\int\left(v^{\frac{-3}{2}}+v^{-1}\right) \mathrm{d} v=\int \frac{\mathrm{d} x}{x} \\ & \Rightarrow 2 v \frac{-1}{2}-\log v=\log x+\log c^{\prime} \\ & \Rightarrow \frac{2 \sqrt{x}}{\sqrt{y}}-\log \frac{y}{x}=\log c^{\prime} x\end{aligned}$
$\begin{aligned} & \Rightarrow \frac{2 \sqrt{x}}{\sqrt{y}}=\log \left(c^{\prime} x \cdot \frac{y}{x}\right) \\ & \Rightarrow c \cdot e^{\frac{2 \sqrt{x}}{\sqrt{y}}}\end{aligned}$

</details>

---

### Q16. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of differential equation $e^{\frac{1}{2}\left(\frac{d y}{d x}\right)}=3^x$ is (where $C$ is a constant of integration.)

**Options:**

- **(A)** $y=x \log 3+C$
- **(B)** $y=x^2 \log 3+C$
- **(C)** $y=2 x \log 3+C$
- **(D)** $x=(\log 3) y^2+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y=x^2 \log 3+C$**

**Detailed Solution:**

$\begin{aligned} & e^{\frac{1}{2}\left(\frac{d y}{d x}\right)}=3^x \Rightarrow \frac{1}{2} \frac{d y}{d x}=\log _e 3^x=x \log _e 3 \\ & \Rightarrow \frac{d y}{d x}=\left(2 \log _e 3\right) x \\ & \Rightarrow y=2 \log _e 3 \times \frac{x^2}{2}+c \\ & \Rightarrow y=x^2 \log _e 3+c\end{aligned}$

</details>

---

### Q17. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $x^2+y^2-2 x y \frac{d y}{d x}=0$ is (where $C$ is a constant of integration.)

**Options:**

- **(A)** $2\left(x^2-y^2\right)+x=C$
- **(B)** $x^2+y^2=C x$
- **(C)** $x^2-y^2=C x$
- **(D)** $x^2+y^2=C y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2-y^2=C x$**

**Detailed Solution:**

$\begin{aligned} & x^2+y^2-2 x y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x^2+y^2}{2 x y} \Rightarrow v+x \cdot \frac{d v}{d x}=\frac{1+v^2}{2 v} \\ & \text { [Let } y=n x] \\ & \Rightarrow \int \frac{2 v d v}{1-v^2}=\int \frac{d x}{x} \\ & \Rightarrow-\log \left|1-v^2\right|+\log |c|=\log |x| \\ & \Rightarrow \log \left|\frac{c}{1-v^2}\right|=\log |x| \\ & \Rightarrow \frac{c}{1-\frac{y^2}{x^2}}=x \\ & \Rightarrow c x=x^2-y^2\end{aligned}$

</details>

---

### Q18. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{d y}{d x}=\frac{3 x+y}{x-y}$ is (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{y}{x \sqrt{3}}\right)-\log \left(\frac{y^2+3 x^2}{x^2}\right)^{\frac{1}{2}}=\log (x)+C$
- **(B)** $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{y}{x \sqrt{3}}\right)+\log \left(\frac{y^2+3 x^2}{x^2}\right)^{\frac{1}{2}}=\log (x)+C$
- **(C)** $\tan ^{-1}\left(\frac{y}{x}\right)+\log \left(\frac{y^2+3 x^2}{x^2}\right)=\log (x)+C$
- **(D)** $\tan ^{-1}\left(\frac{x}{y}\right)+\log \left(\frac{y^2+3 x^2}{x^2}\right)=\log (x)+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\sqrt{3}} \tan ^{-1}\left(\frac{y}{x \sqrt{3}}\right)-\log \left(\frac{y^2+3 x^2}{x^2}\right)^{\frac{1}{2}}=\log (x)+C$**

**Detailed Solution:**

$\frac{d y}{d x}=\frac{3 x+y}{x-y}$
$\begin{aligned} & \Rightarrow v=x \cdot \frac{d v}{d x}=\frac{3+v}{1-v} \quad[\text { let } y=v x] \\ & \Rightarrow x \cdot \frac{d v}{d x}=\frac{3+v}{1-v}-v \\ & \Rightarrow x \frac{d v}{d x}=\frac{3+v^2}{1-v} \\ & \Rightarrow \int \frac{1-v}{3+v^2} d v=\int \frac{d x}{x} \\ & \Rightarrow \int \frac{d v}{3+v^2}-\frac{1}{2} \int \frac{2 v d v}{3+v^2}=\int \frac{d x}{x} \\ & \Rightarrow \frac{1}{\sqrt{3}} \tan ^{-1} \frac{v}{\sqrt{3}}-\frac{1}{2} \log \left(3+v^2\right)=\log x+C\end{aligned}$
$\begin{aligned} & \Rightarrow \frac{1}{\sqrt{3}} \tan ^{-1} \frac{y}{x \sqrt{3}}-\frac{1}{2} \log \left(\frac{3 x^2+y^2}{x^2}\right)=\log x+C \\ & \Rightarrow \frac{1}{\sqrt{3}} \tan ^{-1} \frac{y}{x \sqrt{3}}-\log \left(\frac{y^2+3 x^2}{x^2}\right)^{\frac{1}{2}}=\log x+C\end{aligned}$

</details>

---

### Q19. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A curve passes through the point $\left(1, \frac{\pi}{6}\right)$. Let the slope of the curve at each point $(x, y)$ be given by $\frac{y}{x}+\sec \left(\frac{y}{x}\right), x>0$, then the equation of the curve is

**Options:**

- **(A)** $\sin \left(\frac{y}{x}\right)=\log x+\frac{1}{2}$
- **(B)** $\operatorname{cosec}\left(\frac{y}{x}\right)=\log e+2$
- **(C)** $\cos \left(\frac{2 y}{x}\right)=\log x+\frac{1}{2}$
- **(D)** $\sec \left(\frac{2 y}{x}\right)=\log x+2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin \left(\frac{y}{x}\right)=\log x+\frac{1}{2}$**

**Detailed Solution:**

Here $\frac{\mathrm{dy}}{\mathrm{dx}}=\frac{\mathrm{y}}{\mathrm{x}}+\sec \left(\frac{\mathrm{y}}{\mathrm{x}}\right)$
Let $\frac{y}{x}=v \Rightarrow y=v x \Rightarrow \frac{d y}{d x}=v+x \cdot \frac{d v}{d x}$
$\begin{aligned} & \Rightarrow v+x \cdot \frac{d v}{d x}=v+\sec v \\ & \Rightarrow x \cdot \frac{d v}{d x}=\operatorname{secv} \\ & \Rightarrow \int \cos v \cdot d v=\int \frac{d x}{x} \\ & \Rightarrow \operatorname{sinv}=\log _e x+C\end{aligned}$
$\Rightarrow \sin \left(\frac{y}{x}\right)=\log _e x+C$
Putting $\mathrm{x}=1, \mathrm{y}=\frac{\pi}{6} \Rightarrow \mathrm{c}=\frac{1}{2}$
$\Rightarrow \sin \left(\frac{y}{x}\right)=\log _e^x+\frac{1}{2}$

</details>

---

### Q20. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of $\frac{d y}{d x}=\frac{x+y}{x-y}$ is

**Options:**

- **(A)** $\tan ^{-1} \frac{x}{y}+\frac{1}{2} \log \left|x^2+y^2\right|=c$
- **(B)** $\tan ^{-1} \frac{\mathrm{y}}{\mathrm{x}}+\frac{1}{2} \log \left|\mathrm{x}^2+\mathrm{y}^2\right|=\mathrm{c}$
- **(C)** $\tan ^{-1} \frac{y}{x}-\frac{1}{2} \log \left|x^2+y^2\right|=c$
- **(D)** $\tan ^{-1} \frac{x}{y}-\frac{1}{2} \log \left|x^2+y^2\right|=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan ^{-1} \frac{y}{x}-\frac{1}{2} \log \left|x^2+y^2\right|=c$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{x+y}{x-y} \\ & \text { Put } y=v x \\ & \therefore \frac{d y}{d x}=v+x \frac{d v}{d x} \\ & \therefore v+x \frac{d v}{d x}=\frac{x+v x}{x-v x}=\frac{1+v}{1-v} \\ & \therefore x \frac{d v}{d x}=\frac{1+v}{1-v}-v=\frac{1+v-v+v^2}{1-v}=\frac{1+v^2}{1-v} \\ & \therefore \int \frac{(1-v)}{1+v^2} d v=\int \frac{d x}{x} \\ & \therefore \int \frac{1}{1+v^2} d v-\frac{1}{2} \int \frac{2 v}{1+v^2} d v=\int \frac{d x}{x} \\ & \therefore \tan ^{-1}(v)-\frac{1}{2} \log \left|1+v^2\right|=\log |x|+c \\ & \therefore \tan ^{-1}\left(\frac{y}{x}\right)-\frac{1}{2} \log \left|1+\frac{y^2}{x^2}\right|-\frac{1}{2} \log \left|x^2\right|=c\end{aligned}$
$\begin{aligned} & \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)-\frac{1}{2}\left[\log \left|\frac{\mathrm{x}^2+\mathrm{y}^2}{\mathrm{x}^2}\right|+\log \left|\mathrm{x}^2\right|\right]=\mathrm{c} \\ & \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)-\frac{1}{2} \log \left|\mathrm{x}^2+\mathrm{y}^2\right|=\mathrm{c}\end{aligned}$

</details>

---

### Q21. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Solution of the differential equation $y^{\prime}=\frac{\left(x^2+y^2\right)}{x y}$, where $y(1)=-2$ is given by

**Options:**

- **(A)** $y^2=4 x^2 \log x^2+x^2$
- **(B)** $y^2=x^2 \log x-x^2$
- **(C)** $y^2=x \log x^2+4 x^2$
- **(D)** $y^2=x^2 \log x^2+4 x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y^2=x^2 \log x^2+4 x^2$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{x^2+y^2}{x y}=\frac{x}{y}+\frac{y}{x} \\ & \text { Let } \frac{x}{y}=v \Rightarrow y=\frac{v}{x} \\ & \therefore \frac{d y}{d x}=\frac{v-x\left(\frac{d v}{d x}\right)}{v^2} \\ & \therefore \frac{v-x\left(\frac{d v}{d x}\right)}{v^2}=v+\frac{1}{v} \Rightarrow \frac{1}{v}-\left(\frac{x}{v^2}\right) \frac{d v}{d x}=v+\frac{1}{v} \\ & \therefore \int \frac{d v}{v^3}=-\int \frac{d x}{x} \\ & \therefore \frac{-1}{2 v^2}=-\log x-c \quad \Rightarrow \frac{1}{2 v^2}=\log x+c \\ & \therefore \frac{y^2}{2 x^2}=\log \mathrm{x}+\mathrm{c} \quad \Rightarrow \mathrm{y}^2=\mathrm{x}^2 \log \mathrm{x}^2+2 \mathrm{x}^2 \mathrm{c} \\ & \text { We have } \mathrm{y}(1)=-2 \\ & \therefore 4=0+2 c \Rightarrow c=2 \\ & \therefore \mathrm{y}^2=\mathrm{x}^2 \log \mathrm{x}^2+4 \mathrm{x}^2 \\ & \end{aligned}$

</details>

---

### Q22. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
I: y^{\prime}=\frac{y+x}{x} ; \quad \text { II }: y^{\prime}=\frac{x^2+y}{x^3} ; \quad \text { III }: y^{\prime}=\frac{2 x y}{y^2-x^2}
$$
S1: Differential equations given by I and II are homogeneous differential equations.

S2: Differential equations given by II and III are homogeneous differential equations.

S3: Differential equations given by I and III are homogeneous differential equations.

**Options:**

- **(A)** only $\mathrm{S} 1$ is valid
- **(B)** both S1 and S2 are valid
- **(C)** only S3 is valid
- **(D)** only S2 is valid

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) only S3 is valid**

**Detailed Solution:**

We will check all 3 equations.
I : $\frac{d y}{d x}=\frac{y+x}{x} \Rightarrow$ All terms have same degree equal to 1 .
II : $\frac{d y}{d x}=\frac{x^2+y}{y^3} \Rightarrow$ Here all terms have different degrees.,
III : $\frac{d y}{d x}=\frac{2 x y}{y^2-x^2} \Rightarrow$ All terms have same degree equal to 2 .

</details>

---

### Q23. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation $\left(3 x y+y^2\right) d x$ $+\left(x^2+x y\right) d y=0$ is

**Options:**

- **(A)** $x^2\left(2 x y-y^2\right)=c$
- **(B)** $x^2\left(y^2-2 x y\right)=c$
- **(C)** $x\left(2 x y+y^2\right)=c$
- **(D)** $\mathrm{x}^2\left(2 \mathrm{xy}+\mathrm{y}^2\right)=\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{x}^2\left(2 \mathrm{xy}+\mathrm{y}^2\right)=\mathrm{c}$**

**Detailed Solution:**

$$
\begin{aligned}
& \left(3 x y+y^2\right) d x+\left(x^2+x y\right) d y=0 \\
& \therefore \frac{d y}{d x}=-\frac{\left(3 x y+y^2\right)}{\left(x^2+x y\right)}
\end{aligned}
$$
Put $y=v x \Rightarrow \frac{d y}{d x}=v+x \frac{d v}{d x}$


$$
\begin{aligned}
& \therefore v+x \frac{d v}{d x}=-\frac{\left(3 v x^2+v^2 x^2\right)}{\left(x^2+v x^2\right)}=-\frac{3 v+v^2}{1+v} \\
& \therefore x \frac{d v}{d x}=-\frac{3 v+v^2}{1+v}-v=-\frac{\left(2 v^2+4 v\right)}{1+v}
\end{aligned}
$$


$$
\begin{aligned}
& \therefore \int \frac{1+v}{\left(2 v^2+4 v\right)} d v=\int \frac{-1}{x} d x \\
& \therefore \frac{1}{2} \int \frac{v+1}{v^2+2 v} d v=-\int \frac{d x}{x} \Rightarrow \frac{1}{4} \int \frac{2(v+1)}{v^2+2 v} d v=-\log x+\log c_1
\end{aligned}
$$


$$
\begin{aligned}
& \therefore \frac{1}{4} \log \left(\mathrm{v}^2+2 \mathrm{v}\right)+\log \mathrm{x}=\log \mathrm{c}_1 \Rightarrow \frac{1}{4} \log \left(\frac{\mathrm{y}^2}{\mathrm{x}^2}+\frac{2 \mathrm{y}}{\mathrm{x}}\right)+\log \mathrm{x}=\log \mathrm{c}_1 \\
& \therefore \frac{1}{4} \log \left(\frac{\mathrm{y}^2+2 \mathrm{xy}}{\mathrm{x}^2}\right)+\log \mathrm{x}=\log \mathrm{c}_1 \Rightarrow \log \left(\frac{\mathrm{y}^2+2 \mathrm{xy}}{\mathrm{x}^2}\right)+\log \mathrm{x}^4=4 \log \mathrm{c}_1 \\
& \therefore \log \left[\left(\frac{\mathrm{y}^2+2 \mathrm{xy}}{\mathrm{x}^2}\right)\left(\mathrm{x}^4\right)\right]=\log \mathrm{c}_1^4 \Rightarrow \log \left[\mathrm{x}^2\left(\mathrm{y}^2+2 \mathrm{xy}\right)\right]=\log \mathrm{c}_1^4 \\
& \therefore \mathrm{x}^2\left(\mathrm{y}^2+2 \mathrm{xy}\right)=\mathrm{c}
\end{aligned}
$$

</details>

---

### Q24. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation $\frac{d y}{d x}=\frac{x+2 y-1}{x+2 y+1}$ is

**Options:**

- **(A)** $3(x+y)+4 \log |3 x+6 y-1|=K$
- **(B)** $3(\mathrm{x}-\mathrm{y})+4 \log |3 \mathrm{x}+6 \mathrm{y}-1|=\mathrm{K}$
- **(C)** $6(-x+y)+4 \log |3 x+6 y-1|=K$
- **(D)** $6(\mathrm{x}+\mathrm{y})+4 \log |3 \mathrm{x}+6 \mathrm{y}-1|=\mathrm{K}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6(-x+y)+4 \log |3 x+6 y-1|=K$**

**Detailed Solution:**

$$
\frac{d y}{d x}=\frac{x+2 y-1}{x+2 y+1}
$$
Put $x+2 y=t \Rightarrow x+2 y=t \Rightarrow 1+2 \frac{d y}{d x}=\frac{d t}{d x} \Rightarrow \frac{d y}{d x}=\frac{\left(\frac{d t}{d x}-1\right)}{2}$
$$
\begin{aligned}
& \therefore \frac{\left(\frac{d t}{d x}-1\right)}{2}=\frac{t-1}{t+1} \Rightarrow \frac{d t}{d x}-1=\frac{2 t-2}{t+1} \\
& \therefore \frac{d t}{d x}=\frac{2 t-2}{t+1}+1=\frac{3 t-1}{t+1}
\end{aligned}
$$


$$
\begin{aligned}
& \therefore \int \frac{t+1}{3 t-1} d t=\int d x \\
& \therefore \frac{1}{3} \int \frac{3(t+1)}{3 t-1} d t=\int d x \Rightarrow \frac{1}{3} \int \frac{3 t-1+4}{3 t-1} d t=\int d x \\
& \therefore \frac{1}{3} \int d t+\frac{4}{3} \int \frac{d t}{3 t-1}=\int d x \\
& \therefore \frac{t}{3}+\frac{4}{3} \frac{\log |3 t-1|}{3}=x+c_1 \\
& \therefore \frac{x+2 y}{3}+\frac{4}{3} \frac{\log |3(x+2 y)-1|}{3}=x+c_1 \\
& \therefore 3 x+6 y+4 \log |3 x+6 y-1|=9 x+9 c_1 \\
& \therefore 6(-x+y)+4 \log |3 x+6 y-1|=K
\end{aligned}
$$

</details>

---

### Q25. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\cos x \cdot \sin y d x$ $+\sin x \cdot \cos y d y=0$ is

**Options:**

- **(A)** $\sin x+\sin y=c$
- **(B)** $\cos x+\cos y=c$
- **(C)** $\sin x \cdot \sin y=c$
- **(D)** $\cos x \cdot \cos y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sin x \cdot \sin y=c$**

**Detailed Solution:**

$$
\begin{aligned}
& \cos \mathrm{x} \sin \mathrm{ydx}+\sin \mathrm{x} \cos \mathrm{y} d \mathrm{y}=0 \\
& \therefore \cos \mathrm{x} \sin \mathrm{ydx}=-\sin \mathrm{x} \cos \mathrm{ydy} \\
& \therefore \int \frac{\cos \mathrm{x}}{\sin \mathrm{x}} \mathrm{dx}=-\int \frac{\cos \mathrm{y}}{\sin \mathrm{y}} \mathrm{dy} \\
& \therefore \log |\sin \mathrm{x}|=-\log |\sin \mathrm{y}|+\mathrm{c}_1 \\
& \therefore \log |\sin \mathrm{x}|+\log |\sin \mathrm{y}|=\mathrm{c}_1 \Rightarrow \log [\sin \mathrm{x} \sin \mathrm{y}]=\mathrm{c}_1 \\
& \therefore \sin \mathrm{x} \sin \mathrm{y}=\mathrm{e}^{c_1}=\mathrm{c}
\end{aligned}
$$

</details>

---

### Q26. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $x \cdot \sin \left(\frac{y}{x}\right) d y=\left[y \cdot \sin \left(\frac{y}{x}\right)-x\right] d x$ is

**Options:**

- **(A)** $\cos \left(\frac{x}{y}\right)=\log |x|+c$
- **(B)** $\cos \left(\frac{y}{x}\right)=\log |y|+c$
- **(C)** $\cos \left(\frac{y}{x}\right)=\log |x|+c$
- **(D)** $\cos \left(\frac{x}{y}\right)=\log |y|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos \left(\frac{y}{x}\right)=\log |x|+c$**

**Detailed Solution:**

We have $x \cdot \sin \left(\frac{y}{x}\right) d y=\left[y \cdot \sin \left(\frac{y}{x}\right)-x\right] d x$
$\therefore \frac{d y}{d x}=\frac{y \cdot \sin \left(\frac{y}{x}\right)-x}{x \sin \left(\frac{y}{x}\right)}=\left(\frac{y}{x}\right)-\frac{1}{\sin \left(\frac{y}{x}\right)}$
$\therefore \frac{d y}{d x}-\left(\frac{1}{x}\right) y=-\operatorname{cosec}\left(\frac{y}{x}\right)$
Put $\frac{y}{x}=v \Rightarrow y=v x \Rightarrow \frac{d y}{d x}=v+x \frac{d v}{d x}$
$\therefore\left(\mathrm{v}+\frac{\mathrm{xdv}}{\mathrm{dx}}\right)-\mathrm{v}=-\operatorname{cosec} \mathrm{v} \Rightarrow \mathrm{x} \frac{\mathrm{dv}}{\mathrm{dx}}=-\operatorname{cosec} \mathrm{v}$
$\therefore \int \frac{\mathrm{dv}}{\operatorname{cosec} \mathrm{v}}=-\int \frac{\mathrm{d} \mathrm{x}}{\mathrm{x}} \Rightarrow \int \sin \mathrm{v} \mathrm{dv}=-\log |\mathrm{x}|$
$-\cos v=-\log |x|+c_{1} \Rightarrow \log x+c=\cos v$
$\therefore \cos \left(\frac{y}{x}\right)=\log |x|+c$

</details>

---

### Q27. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$y=c^{2}+\frac{c}{x}$ is the solution of the differential equation

**Options:**

- **(A)** $x^{4}\left(\frac{d y}{d x}\right)^{2}+x\left(\frac{d y}{d x}\right)-y=0$
- **(B)** $x^{4}\left(\frac{d y}{d x}\right)^{2}-x\left(\frac{d y}{d x}\right)-y=0$
- **(C)** $x^{4}\left(\frac{d y}{d x}\right)^{2}-x\left(\frac{d y}{d x}\right)+y=0$
- **(D)** $x^{4}\left(\frac{d y}{d x}\right)^{2}+x\left(\frac{d y}{d x}\right)+y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^{4}\left(\frac{d y}{d x}\right)^{2}-x\left(\frac{d y}{d x}\right)-y=0$**

**Detailed Solution:**

Given $y=c^{2}+\frac{c}{x}$
Differentiating w.r.t. $x$
$$
\frac{d y}{d x}=0-\frac{c}{x^{2}}=-\frac{c}{x^{2}} \Rightarrow c=\left(-x^{2}\right)\left(\frac{d y}{d x}\right)
$$
Substituting value of $\mathrm{c}$ in given equation, We get
$$
\begin{aligned}
y &=\left[\left(-x^{2}\right)\left(\frac{d y}{d x}\right)\right]^{2}+\frac{\left(-x^{2}\right)\left(\frac{d y}{d x}\right)}{x} \\
&=x^{4}\left(\frac{d y}{d x}\right)^{2}-x \frac{d y}{d x} \\
\therefore & x^{4}\left(\frac{d y}{d x}\right)^{2}-x \frac{d y}{d x}-y=0
\end{aligned}
$$

</details>

---

### Q28. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The equation of the curve which passes through point $(1,0)$ and has tangent with
slope $1+\frac{y}{x}+\left(\frac{y}{x}\right)^{2}$ is

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{x}{y}\right)=\log |x|$
- **(B)** $\tan ^{-1}\left(\frac{x}{y}\right)=\log |y|$
- **(C)** $\tan ^{-1}\left(\frac{y}{x}\right)=\log |y|$
- **(D)** $\tan ^{-1}\left(\frac{y}{x}\right)=\log |x|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan ^{-1}\left(\frac{y}{x}\right)=\log |x|$**

**Detailed Solution:**

We have siope of tangent $=\frac{d y}{d x}=1+\frac{y}{x}+\left(\frac{y}{x}\right)^{2}$
$\therefore \frac{d y}{d x}=1+\frac{y}{x}+\frac{y^{2}}{x^{2}} \Rightarrow \frac{d y}{d x}=\frac{x^{2}+x y+y^{2}}{x^{2}}$ ...(1)
Put $y=u x \Rightarrow \frac{d y}{d x}=u+x \frac{d u}{d x}$
$\therefore \quad u+x \frac{d u}{d x}=\frac{x^{2}+u x^{2}+u^{2} x^{2}}{x^{2}}$
$\therefore \quad u+x \frac{d u}{d x}=1+u+u^{2} \Rightarrow x \frac{d u}{d x}=1+u^{2} \Rightarrow \int \frac{d u}{1+u^{2}}=\int \frac{d x}{x}$
$\therefore \tan ^{-1} u=\log |x|+c \Rightarrow \tan ^{-1}\left(\frac{y}{x}\right)=\log |x|+c$
At $(1,0)$, we write $\tan ^{-1}(0)=\log |1|+c \Rightarrow c=0$
$\therefore \tan ^{-1}\left(\frac{y}{x}\right)=\log |x|$

</details>

---

### Q29. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of differential equation $x^{2} \frac{d y}{d x}=y^{2}+x y$ is

**Options:**

- **(A)** $\frac{x}{y}+\log |x|=c$
- **(B)** $\frac{y}{x}+\log |x|=c$
- **(C)** $\frac{x}{y}-\log |x|=c$
- **(D)** $\frac{y}{x}-\log |x|=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{x}{y}+\log |x|=c$**

**Detailed Solution:**

We have $x^{2} \frac{d y}{d x}=y^{2}+x y$
$\begin{array}{l}
\therefore \frac{d y}{d x}=\frac{y^{2}+x y}{x^{2}} ...(1) \\
\therefore \text { Put } y=u x \\
\therefore \frac{d y}{d x}=u+x \frac{d u}{d x}
\end{array}$
$\therefore$ Equation (1) becomes
$u+x \frac{d u}{d x}=\frac{u^{2} x^{2}+x(u x)}{x^{2}} \Rightarrow u+x \frac{d u}{d x}=u^{2}+u$
$\begin{array}{l}
\therefore \mathrm{x} \frac{\mathrm{du}}{\mathrm{dx}}=\mathrm{u}^{2} \\
\therefore \int \frac{\mathrm{du}}{\mathrm{u}^{2}}=\int \frac{\mathrm{dx}}{\mathrm{x}} \\
\therefore \frac{-1}{\mathrm{u}}=\log |\mathrm{x}|+\mathrm{c}_{1} \Rightarrow \quad \frac{-\mathrm{x}}{\mathrm{y}}=\log |\mathrm{x}|+\mathrm{c}_{1} \\
\therefore \frac{\mathrm{x}}{\mathrm{y}}+\log |\mathrm{x}|=\mathrm{c}
\end{array}$

</details>

---

### Q30. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $\frac{d y}{d x}=\frac{x+y+1}{x+y-1}$ is given by

**Options:**

- **(A)** $x+y=\log |x+y|+c$
- **(B)** $x-y=\log |x+y|+c$
- **(C)** $y=x+\log |x+y|+c$
- **(D)** $y=x \log |x+y|+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=x+\log |x+y|+c$**

**Detailed Solution:**

$\frac{d y}{d x}=\frac{x+y+1}{x+y-1}$
Put $\quad x+y=t$
$\Rightarrow \quad 1+\frac{d y}{d x}=\frac{d t}{d x}$
$$
\begin{array}{lc}
\Rightarrow & \frac{d y}{d x}=\frac{d t}{d x}-1 \\
\therefore & \frac{d t}{d x}-1=\frac{t+1}{t-1} \\
\Rightarrow & \frac{d t}{d x}=\frac{t+1+t-1}{t-1} \\
\Rightarrow & \frac{d t}{d x}=\frac{2 t}{t-1} \\
\Rightarrow & \left(\frac{t-1}{2 t}\right) d t=d x \\
\Rightarrow & \left(\frac{1}{2}-\frac{1}{2 t}\right) d t=d x
\end{array}
$$
On integrating, we get
$$
\frac{1}{2} t-\frac{1}{2} \log t=x+c_{1}
$$
$\begin{array}{lrl}\Rightarrow & t-\log t & =2 x+2 c_{1} \\ \Rightarrow & x+y-\log (x+y) & =2 x+2 c_{1} \\ \Rightarrow & y & =x+\log (x+y)+c\end{array}$

</details>

---

### Q31. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\left(3 x y+y^{2}\right) d x+\left(x^{2}+x y\right) d y=0$ is

**Options:**

- **(A)** $x^{2}\left(2 x y+y^{2}\right)=c^{2}$
- **(B)** $x^{2}\left(2 x y-y^{2}\right)=c^{2}$
- **(C)** $x^{2}\left(y^{2}-2 x y\right)=c^{2}$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x^{2}\left(2 x y+y^{2}\right)=c^{2}$**

**Detailed Solution:**

Homogeneous equation can be written in the form of
Put
$$
\begin{aligned}
\frac{d y}{d x} &=-\frac{3 x y+y^{2}}{x^{2}+x y} \\
y=& v x \text { and } \frac{d y}{d x}=v+x \frac{d v}{d x}, \text { we get }
\end{aligned}
$$
$$
v+x \frac{d v}{d x}=-\frac{3 x^{2} v+x^{2} v^{2}}{x^{2}+x^{2} v}
$$
$$
\Rightarrow \quad x \frac{d v}{d x}=\frac{-2 v(v+2)}{v+1}
$$
$$
\begin{array}{ll}
\Rightarrow \quad & \frac{1}{x} d x=-\frac{(v+1)}{2 v(v+2)} d v \\
\Rightarrow \quad & -\frac{2}{x}=-\left[\frac{1}{2(v+2)}+\frac{1}{2 v}\right] d v
\end{array}
$$
On integrating, we get
$$
\begin{aligned}
&-2 \log _{e} x=\frac{1}{2} \log (v+2)+\frac{1}{2} \log v-\log c \\
\Rightarrow & v(v+2) x^{4}=c^{2} \\
\Rightarrow & \frac{y}{x}\left(\frac{y}{x}+2\right) x^{4}=c^{2} &\left(\because v=\frac{y}{x}\right)
\end{aligned}
$$
Hence, required solution is $\left(y^{2}+2 x y\right) x^{2}=c^{2}$

</details>

---

### Q32. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\frac{d y}{d x}=\frac{x-y+3}{2(x-y)+5}$ is

**Options:**

- **(A)** $2(x-y)+\log (x-y)=x+c$
- **(B)** $2(x-y)-\log (x-y+2)=x+c$
- **(C)** $2(x-y)+\log (x-y+2)=x+c$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2(x-y)+\log (x-y+2)=x+c$**

**Detailed Solution:**

Given differential equation is
$$
\frac{d y}{d x}=\frac{x-y+3}{2(x-y)+5}
$$
Let $\quad x-y=v \Rightarrow \frac{d y}{d x}=1-\frac{d v}{d x}$
$\therefore$
$$
\frac{d v}{d x}=\frac{v+2}{2 v+5}
$$
$$
\begin{array}{l}
\Rightarrow \quad \int \frac{2 v+5}{v+2} d v=\int d x \\
\Rightarrow \quad \int\left(2+\frac{1}{v+2}\right) d v=\int d x
\end{array}
$$
$\Rightarrow \quad 2 v+\log (v+2)=x+c$
$\Rightarrow 2(x-y)+\log (x-y+2)=x+c$

</details>

---

