# MHT CET Mathematics - Differential Equations

## Topic 3: Variable Separable Form

**Total Questions:** 123

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation $\dfrac{dy}{dx} = \dfrac{\sqrt{1 - y^2}}{y}$ determines a family of circles with

**Options:**

- **(A)** variable radii and fixed center at $(0, 1)$
- **(B)** fixed radius of $1$ and variable centers on X-axis
- **(C)** variable radii and fixed center at $(0, -1)$
- **(D)** fixed radius of $1$ and variable centers on Y-axis

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) fixed radius of $1$ and variable centers on X-axis**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{\sqrt{1 - y^2}}{y}$

Separating the variables, we get:

$\dfrac{y}{\sqrt{1 - y^2}} dy = dx$

Integrating both sides:

$\int \dfrac{y}{\sqrt{1 - y^2}} dy = \int dx$

Let $1 - y^2 = t$, then $-2y dy = dt \Rightarrow y dy = -\dfrac{dt}{2}$

$\int -\dfrac{1}{2\sqrt{t}} dt = \int dx$

$-\sqrt{t} = x + C$

$-\sqrt{1 - y^2} = x + C$

Squaring both sides, we obtain:

$1 - y^2 = (x + C)^2$

$(x + C)^2 + y^2 = 1$

This equation represents a family of circles with center $(-C, 0)$ and radius $1$.

Since $C$ is an arbitrary constant, the centers lie on the X-axis and vary, while the radius is fixed at $1$.

Answer: fixed radius of $1$ and variable centers on X-axis

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of $e^{\frac{dy}{dx}} = x$ is

**Options:**

- **(A)** $y = x\log x - x + c$
- **(B)** $y = x\log x + c$
- **(C)** $y = 1/x + c$
- **(D)** $y = x.\log x + x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y = x\log x - x + c$**

**Detailed Solution:**

Given differential equation is $e^{\dfrac{dy}{dx}} = x$

Taking natural logarithm on both sides, we get

$\dfrac{dy}{dx} = \log x$

Separating the variables, we get

$dy = \log x \, dx$

Integrating both sides, we get

$\int dy = \int \log x \cdot 1 \, dx$

Using integration by parts, taking $\log x$ as the first function and $1$ as the second function:

$y = \log x \int 1 \, dx - \int \left( \dfrac{d}{dx}(\log x) \int 1 \, dx \right) dx$

$y = x \log x - \int \left( \dfrac{1}{x} \cdot x \right) dx$

$y = x \log x - \int 1 \, dx$

$y = x \log x - x + c$

Answer: $y = x\log x - x + c$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the general solution of the differential equation $\dfrac{dy}{dx} = \cos(2x - 3y) - \cos(2x + 3y)$ is $\cos 2x = g(y) + c$, then $g(y) = \ldots$

**Options:**

- **(A)** $\cos 2x + \cos 2y$
- **(B)** $\sec y + \tan y$
- **(C)** $-\dfrac{1}{3}\log\left|\tan\left(\dfrac{3y}{2}\right)\right|$
- **(D)** $2\log|\text{cosec} 3y - \cot 3y|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\dfrac{1}{3}\log\left|\tan\left(\dfrac{3y}{2}\right)\right|$**

**Detailed Solution:**

The given differential equation is:

$\dfrac{dy}{dx} = \cos(2x - 3y) - \cos(2x + 3y)$

Using the trigonometric identity $\cos(A - B) - \cos(A + B) = 2 \sin A \sin B$:

$\dfrac{dy}{dx} = 2 \sin 2x \sin 3y$

Separating the variables:

$\dfrac{dy}{\sin 3y} = 2 \sin 2x dx$

$\csc 3y dy = 2 \sin 2x dx$

Integrating both sides:

$\int \csc 3y dy = \int 2 \sin 2x dx$

$\dfrac{1}{3} \log \left| \tan \left( \dfrac{3y}{2} \right) \right| = -\cos 2x + c_1$

Rearranging to match the form $\cos 2x = g(y) + c$:

$\cos 2x = -\dfrac{1}{3} \log \left| \tan \left( \dfrac{3y}{2} \right) \right| + c_1$

From this equation, we get:

$g(y) = -\dfrac{1}{3} \log \left| \tan \left( \dfrac{3y}{2} \right) \right|$

</details>

---

### Q4. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\dfrac{dy}{dx} = \dfrac{xy + y}{xy + x}$ is

**Options:**

- **(A)** $y - x = \log\left(\dfrac{x}{y}\right) + c$
- **(B)** $x - y = \log\left(\dfrac{x}{y}\right) + c$
- **(C)** $y + x = \log\left(\dfrac{x}{y}\right) + c$
- **(D)** $y + x = \log\left(\dfrac{y}{x}\right) + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y - x = \log\left(\dfrac{x}{y}\right) + c$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{xy + y}{xy + x}$

Factoring the numerator and the denominator, we get:

$\dfrac{dy}{dx} = \dfrac{y(x + 1)}{x(y + 1)}$

Separating the variables $x$ and $y$:

$\dfrac{y + 1}{y} dy = \dfrac{x + 1}{x} dx$

$\left(1 + \dfrac{1}{y}\right) dy = \left(1 + \dfrac{1}{x}\right) dx$

Integrating both sides:

$\int \left(1 + \dfrac{1}{y}\right) dy = \int \left(1 + \dfrac{1}{x}\right) dx$

$y + \log y = x + \log x + c$

Rearranging the terms:

$y - x = \log x - \log y + c$

$y - x = \log\left(\dfrac{x}{y}\right) + c$

Answer: $y - x = \log\left(\dfrac{x}{y}\right) + c$

</details>

---

### Q5. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An ice ball melts. The rate at which it melts is proportional to the amount of the ice at that time. If half quantity of ice melts in $20$ minutes, then the time when $(1/8)^{th}$ part of original amount of the ice is left is:

**Options:**

- **(A)** $60\ \text{minutes}$
- **(B)** $30\ \text{minutes}$
- **(C)** $20\ \text{minutes}$
- **(D)** $40\ \text{minutes}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $60\ \text{minutes}$**

**Detailed Solution:**

Let $V$ be the amount of ice at time $t$.

Given that the rate of melting is proportional to the amount of ice present:

$\dfrac{dV}{dt} = -kV$

Integrating both sides, we get:

$V = V_0 e^{-kt}$

where $V_0$ is the initial amount of ice.

It is given that half the quantity of ice melts in $20\ \text{minutes}$. Thus, at $t = 20$, $V = \dfrac{V_0}{2}$.

$\dfrac{V_0}{2} = V_0 e^{-20k}$

$e^{-20k} = \dfrac{1}{2}$

Taking natural logarithm on both sides:

$20k = \ln 2 \Rightarrow k = \dfrac{\ln 2}{20}$

We need to find the time $t$ when $\dfrac{1}{8}$ of the original amount of ice is left. So, $V = \dfrac{V_0}{8}$.

$\dfrac{V_0}{8} = V_0 e^{-kt}$

$e^{-kt} = \dfrac{1}{8}$

$kt = \ln 8 = 3 \ln 2$

Substituting the value of $k$:

$\left(\dfrac{\ln 2}{20}\right) t = 3 \ln 2$

$t = 60\ \text{minutes}$

Answer: $60\ \text{minutes}$

</details>

---

### Q6. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} + 1 = e^{x+y}$ is

**Options:**

- **(A)** $(x + y + C)e^{x+y} = 0$
- **(B)** $(x + C)e^{x+y} = 0$
- **(C)** $(x - C)e^{x+y} = 0$
- **(D)** $(x + C)e^{x+y} + 1 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(x + C)e^{x+y} + 1 = 0$**

**Detailed Solution:**

Let $x + y = v$.

Differentiating with respect to $x$, we get $1 + \dfrac{dy}{dx} = \dfrac{dv}{dx}$.

Substituting this into the given differential equation, we obtain:

$\dfrac{dv}{dx} = e^v$

Separating the variables, we get:

$e^{-v} dv = dx$

Integrating both sides, we have:

$\int e^{-v} dv = \int dx$

$-e^{-v} = x + C$

Substituting $v = x + y$, we get:

$-e^{-(x+y)} = x + C$

Multiplying the entire equation by $e^{x+y}$, we obtain:

$-1 = (x + C)e^{x+y}$

Rearranging the terms, we get:

$(x + C)e^{x+y} + 1 = 0$

Answer: $(x + C)e^{x+y} + 1 = 0$

</details>

---

### Q7. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A person's assets start reducing in such a way that the rate of reduction of assets is proportional to the square root of the assets existing at that moment. If the assets at the beginning are $\rupee 40$ lakhs and they dwindle down to $\rupee 40000$ after $2$ years. Then the person will be bankrupt in k years from the start. Then $k = $

**Options:**

- **(A)** $2\dfrac{2}{9}$
- **(B)** $2\dfrac{2}{7}$
- **(C)** $2\dfrac{2}{5}$
- **(D)** $2\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2\dfrac{2}{9}$**

**Detailed Solution:**

Let $A$ be the assets at time $t$ in years.

$\dfrac{dA}{dt} = -c \sqrt{A}$

$\int \dfrac{dA}{\sqrt{A}} = \int -c dt$

$2\sqrt{A} = -ct + C$

At $t = 0$, $A = 40,00,000$

$2\sqrt{4000000} = -c(0) + C \Rightarrow C = 4000$

At $t = 2$, $A = 40,000$

$2\sqrt{40000} = -2c + 4000$

$400 = -2c + 4000 \Rightarrow 2c = 3600 \Rightarrow c = 1800$

For bankruptcy, $A = 0$

$0 = -1800t + 4000$

$t = \dfrac{4000}{1800} = \dfrac{20}{9} = 2\dfrac{2}{9}$ years.

Answer: $2\dfrac{2}{9}$

</details>

---

### Q8. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} + 1 = e^{x+y}$ is

**Options:**

- **(A)** $e^{x+y} = x + c$, where $c$ is integral constant
- **(B)** $(x + c)e^{x+y} - 1 = 0$, where $c$ is integral constant
- **(C)** $(x + c)e^{x+y} + 1 = 0$, where $c$ is integral constant
- **(D)** $e^{x+y} = x + y + c$, where $c$ is integral constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(x + c)e^{x+y} + 1 = 0$, where $c$ is integral constant**

**Detailed Solution:**

Let $x + y = v$

Differentiating with respect to $x$, we get $1 + \dfrac{dy}{dx} = \dfrac{dv}{dx}$

Substituting this into the given differential equation, we get:

$\dfrac{dv}{dx} = e^v$

Separating the variables:

$e^{-v} dv = dx$

Integrating both sides:

$\int e^{-v} dv = \int dx$

$-e^{-v} = x + c$

Substituting $v = x + y$:

$-e^{-(x+y)} = x + c$

Multiplying both sides by $e^{x+y}$:

$-1 = (x + c)e^{x+y}$

$(x + c)e^{x+y} + 1 = 0$

Answer: $(x + c)e^{x+y} + 1 = 0$, where $c$ is integral constant

</details>

---

### Q9. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of disintegration of a radioactive element at any time t is proportional to its mass at that time. Then the time during which the original mass of $4.5$ gm will disintegrate to a mass of $1.5$ gm. is...(where $k$ is proportionality constant)

**Options:**

- **(A)** $\dfrac{1}{k} \log 3$
- **(B)** $-\dfrac{1}{k} \log 3$
- **(C)** $k \log\left(\dfrac{1}{3}\right)$
- **(D)** $\dfrac{1}{k} \log\left(\dfrac{3}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{k} \log 3$**

**Detailed Solution:**

Let $m$ be the mass of the radioactive element at time $t$.

The rate of disintegration is proportional to its mass, which can be written as:

$-\dfrac{dm}{dt} = km$

$\dfrac{dm}{m} = -k dt$

Integrating both sides with the given limits (from initial mass $4.5$ gm at $t = 0$ to final mass $1.5$ gm at time $t$):

$\int_{4.5}^{1.5} \dfrac{dm}{m} = -k \int_{0}^{t} dt$

$[\log m]_{4.5}^{1.5} = -kt$

$\log(1.5) - \log(4.5) = -kt$

$\log\left(\dfrac{1.5}{4.5}\right) = -kt$

$\log\left(\dfrac{1}{3}\right) = -kt$

$-\log 3 = -kt$

$t = \dfrac{1}{k} \log 3$

Answer: $\dfrac{1}{k} \log 3$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\dfrac{dy}{dx} = y + 3$, where $y + 3 > 0$ and $y(0) = 2$, then $y(\log 2)$ is equal to...

**Options:**

- **(A)** $5$
- **(B)** $7$
- **(C)** $10$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = y + 3$

$\Rightarrow \dfrac{dy}{y + 3} = dx$

Integrating both sides,

$\int \dfrac{dy}{y + 3} = \int dx$

$\ln(y + 3) = x + C$

Given $y(0) = 2$, substituting $x = 0$ and $y = 2$,

$\ln(2 + 3) = 0 + C \Rightarrow C = \ln 5$

Substituting $C$ back into the equation,

$\ln(y + 3) = x + \ln 5$

$\Rightarrow \ln\left(\dfrac{y + 3}{5}\right) = x$

$\Rightarrow \dfrac{y + 3}{5} = e^x$

$\Rightarrow y = 5e^x - 3$

Substituting $x = \log 2$,

$y(\log 2) = 5e^{\log 2} - 3$

$y(\log 2) = 5(2) - 3 = 7$

Answer: $7$

</details>

---

### Q11. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $y=f(x)$ satisfies the differential equation $x\dfrac{dy}{dx}=xy+y$ and $y(1)=e$, then which of the following is true?

**Options:**

- **(A)** $f(x)$ is not continuous at $x=0$
- **(B)** $f(x)$ is decreasing in $(-1,\infty)$
- **(C)** $f(x)$ is increasing in $(-1,\infty)$
- **(D)** $f(x)$ has maxima at $x=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x)$ is increasing in $(-1,\infty)$**

**Detailed Solution:**

Given differential equation is $x\dfrac{dy}{dx} = xy + y$

Separating the variables, we get:

$\dfrac{dy}{y} = \left(\dfrac{x+1}{x}\right) dx$

$\dfrac{dy}{y} = \left(1 + \dfrac{1}{x}\right) dx$

Integrating both sides:

$\int \dfrac{dy}{y} = \int \left(1 + \dfrac{1}{x}\right) dx$

$\ln|y| = x + \ln|x| + C$

$y = A x e^x$

Given $y(1) = e$, we substitute $x = 1$ and $y = e$:

$e = A(1)e^1 \Rightarrow A = 1$

Thus, the function is $f(x) = x e^x$.

Differentiating with respect to $x$:

$f'(x) = e^x + x e^x = e^x(x+1)$

For $x \in (-1, \infty)$, $x+1 > 0$ and $e^x > 0$, which implies $f'(x) > 0$.

Therefore, $f(x)$ is increasing in $(-1, \infty)$.

Also, $f(x)$ is continuous for all $x \in \mathbb{R}$ and has a local minimum at $x = -1$.

Answer: $f(x)$ is increasing in $(-1,\infty)$

</details>

---

### Q12. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = f(x)$ is a monotonically increasing function such that $\left(\dfrac{dy}{dx}\right)^2 = 6 - \dfrac{dy}{dx}$ and $y(0) = 5$, then $y(3) = \cdots$

**Options:**

- **(A)** $23$
- **(B)** $14$
- **(C)** $13$
- **(D)** $11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $11$**

**Detailed Solution:**

Let $\dfrac{dy}{dx} = p$

The given differential equation is $p^2 + p - 6 = 0$

$(p+3)(p-2) = 0$

$p = -3$ or $p = 2$

Since $y = f(x)$ is a monotonically increasing function, $\dfrac{dy}{dx} > 0$

Therefore, $\dfrac{dy}{dx} = 2$

Integrating both sides, we get $y = 2x + C$

Given $y(0) = 5$, we have $5 = 2(0) + C \Rightarrow C = 5$

Thus, $y = 2x + 5$

Substituting $x = 3$, we get $y(3) = 2(3) + 5 = 11$

Answer: $11$

</details>

---

### Q13. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{dy}{dx} = \cos(x + y)$ is...

**Options:**

- **(A)** $\cot\left(\dfrac{x + y}{2}\right) = x + c$
- **(B)** $\tan\left(\dfrac{x + y}{2}\right) = x + c$
- **(C)** $-\sin(x + y) = x + c$
- **(D)** $\sec(x - y) + x = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan\left(\dfrac{x + y}{2}\right) = x + c$**

**Detailed Solution:**

Let $x + y = v$

Differentiating with respect to $x$, we get $1 + \dfrac{dy}{dx} = \dfrac{dv}{dx}$

$\dfrac{dy}{dx} = \dfrac{dv}{dx} - 1$

Substituting this in the given differential equation:

$\dfrac{dv}{dx} - 1 = \cos v$

$\dfrac{dv}{dx} = 1 + \cos v$

$\dfrac{dv}{1 + \cos v} = dx$

Integrating both sides:

$\int \dfrac{dv}{2 \cos^2\left(\dfrac{v}{2}\right)} = \int dx$

$\dfrac{1}{2} \int \sec^2\left(\dfrac{v}{2}\right) dv = \int dx$

$\tan\left(\dfrac{v}{2}\right) = x + c$

Substituting $v = x + y$:

$\tan\left(\dfrac{x + y}{2}\right) = x + c$

</details>

---

### Q14. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The rate of disintegration of a radioactive element at any time is proportional to its mass at that time, where $k$ $(k>0)$ is the constant of proportionality. The time during which an original mass of 1.5 gm will disintegrate to a mass of 0.5 gm is $\ldots$

**Options:**

- **(A)** $k\log 3$
- **(B)** $\dfrac{1}{k}\log 3$
- **(C)** $k\log 5$
- **(D)** $\dfrac{1}{k}\log 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{k}\log 3$**

**Detailed Solution:**

Let $m$ be the mass of the radioactive element at time $t$.

The rate of disintegration is given by $\dfrac{dm}{dt} = -km$

$\dfrac{dm}{m} = -k dt$

Integrating both sides with appropriate limits:

$\int_{1.5}^{0.5} \dfrac{dm}{m} = -k \int_{0}^{t} dt$

$[\log m]_{1.5}^{0.5} = -kt$

$\log 0.5 - \log 1.5 = -kt$

$\log \left(\dfrac{0.5}{1.5}\right) = -kt$

$\log \left(\dfrac{1}{3}\right) = -kt$

$-\log 3 = -kt$

$t = \dfrac{1}{k} \log 3$

Answer: $\dfrac{1}{k}\log 3$

</details>

---

### Q15. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve whose slope is $\dfrac{y-1}{x^2+x}$ and which passes through the point $(1, 0)$ is

**Options:**

- **(A)** $xy - x - y - 1 = 0$
- **(B)** $(y-1)(x+1) = 2x$
- **(C)** $xy + x + y - 1 = 0$
- **(D)** $y(x+1) - x + 1 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $xy + x + y - 1 = 0$**

**Detailed Solution:**

The slope of the curve is given by $\dfrac{dy}{dx}$.

$\dfrac{dy}{dx} = \dfrac{y-1}{x^2+x}$

Separating the variables, we get:

$\dfrac{dy}{y-1} = \dfrac{dx}{x(x+1)}$

Integrating both sides:

$\int \dfrac{dy}{y-1} = \int \left( \dfrac{1}{x} - \dfrac{1}{x+1} \right) dx$

$\ln|y-1| = \ln|x| - \ln|x+1| + \ln|C|$

$\ln|y-1| = \ln\left|\dfrac{Cx}{x+1}\right|$

$y-1 = \dfrac{Cx}{x+1}$

Since the curve passes through the point $(1, 0)$, we substitute $x = 1$ and $y = 0$:

$0 - 1 = \dfrac{C(1)}{1+1}$

$-1 = \dfrac{C}{2} \Rightarrow C = -2$

Substituting $C = -2$ back into the equation:

$y-1 = \dfrac{-2x}{x+1}$

$(y-1)(x+1) = -2x$

$xy + y - x - 1 = -2x$

$xy + x + y - 1 = 0$

Answer: $xy + x + y - 1 = 0$

</details>

---

### Q16. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equations $\dfrac{dy}{dx} = (9x + y + 5)^2$ is...

**Options:**

- **(A)** $\tan^{-1}\left(\dfrac{9x + y + 5}{2}\right) = -2x + c$
- **(B)** $\tan^{-1}\left(\dfrac{9x + y + 5}{2}\right) = 2x + c$
- **(C)** $\tan^{-1}\left(\dfrac{9x + y + 5}{3}\right) = -3x + c$
- **(D)** $\tan^{-1}\left(\dfrac{9x + y + 5}{3}\right) = 3x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan^{-1}\left(\dfrac{9x + y + 5}{3}\right) = 3x + c$**

**Detailed Solution:**

Let $9x + y + 5 = v$

Differentiating with respect to $x$:

$9 + \dfrac{dy}{dx} = \dfrac{dv}{dx}$

$\dfrac{dy}{dx} = \dfrac{dv}{dx} - 9$

Substituting this in the given differential equation:

$\dfrac{dv}{dx} - 9 = v^2$

$\dfrac{dv}{dx} = v^2 + 9$

$\dfrac{dv}{v^2 + 9} = dx$

Integrating both sides:

$\int \dfrac{dv}{v^2 + 3^2} = \int dx$

$\dfrac{1}{3} \tan^{-1}\left(\dfrac{v}{3}\right) = x + c_1$

$\tan^{-1}\left(\dfrac{v}{3}\right) = 3x + 3c_1$

Substituting $v = 9x + y + 5$ and letting $3c_1 = c$:

$\tan^{-1}\left(\dfrac{9x + y + 5}{3}\right) = 3x + c$

Answer: $\tan^{-1}\left(\dfrac{9x + y + 5}{3}\right) = 3x + c$

</details>

---

### Q17. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)$ is a polynomial such that $f(x) = [f'(x)]^2$ and $f(2) = 0$, then $f(-2) = \ldots$

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $4$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4$**

**Detailed Solution:**

Let the degree of the polynomial $f(x)$ be $n$.

The degree of $f'(x)$ is $n-1$, so the degree of $[f'(x)]^2$ is $2(n-1)$.

Equating the degrees, $n = 2n - 2 \Rightarrow n = 2$.

Let $f(x) = ax^2 + bx + c$, where $a \neq 0$.

Then $f'(x) = 2ax + b$.

Substituting into the given equation $f(x) = [f'(x)]^2$:

$ax^2 + bx + c = (2ax + b)^2$

$ax^2 + bx + c = 4a^2x^2 + 4abx + b^2$

Comparing the coefficients of like powers of $x$:

$a = 4a^2 \Rightarrow a = \dfrac{1}{4}$ (since $a \neq 0$)

$b = 4ab \Rightarrow b = b$

$c = b^2$

Thus, the polynomial is $f(x) = \dfrac{1}{4}x^2 + bx + b^2$.

Given $f(2) = 0$:

$\dfrac{1}{4}(2)^2 + 2b + b^2 = 0$

$b^2 + 2b + 1 = 0$

$(b+1)^2 = 0 \Rightarrow b = -1$

Substituting $b = -1$ into $f(x)$:

$f(x) = \dfrac{1}{4}x^2 - x + 1$

Now, evaluating $f(-2)$:

$f(-2) = \dfrac{1}{4}(-2)^2 - (-2) + 1$

$f(-2) = 1 + 2 + 1 = 4$

Answer: $4$

</details>

---

### Q18. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The rate of reduction is proportional to the square root of a persons existing assets at that moment. If his assets at the beginning are 10000 and they dwindle down to 5625 in 2 years, then the person will be bankrupt in

**Options:**

- **(A)** 4 years
- **(B)** 6 years
- **(C)** 8 years
- **(D)** 10 years

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8 years**

**Detailed Solution:**

Let $A$ be the assets at time $t$. The rate of reduction is proportional to the square root of the existing assets.

$\dfrac{dA}{dt} = -k\sqrt{A}$

Separating the variables and integrating:

$\int \dfrac{dA}{\sqrt{A}} = \int -k dt$

$2\sqrt{A} = -kt + C$

At $t = 0$, $A = 10000$

$2\sqrt{10000} = -k(0) + C \Rightarrow C = 200$

At $t = 2$ years, $A = 5625$

$2\sqrt{5625} = -k(2) + 200$

$2(75) = -2k + 200$

$150 = -2k + 200 \Rightarrow 2k = 50 \Rightarrow k = 25$

The equation for the assets at time $t$ becomes:

$2\sqrt{A} = -25t + 200$

For the person to be bankrupt, the assets $A$ must be $0$.

$2\sqrt{0} = -25t + 200$

$25t = 200 \Rightarrow t = 8$ years

Answer: 8 years

</details>

---

### Q19. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $\dfrac{\text{d}y}{\text{d}x} = \sin(x + y) + \cos(x + y)$ is

**Options:**

- **(A)** $\log\left[1 + \tan\left(\dfrac{x+y}{2}\right)\right] = y + c$, where c is the constant of integration
- **(B)** $\log\left[1 - \tan\left(\dfrac{x+y}{2}\right)\right] = y + c$, where c is the constant of integration
- **(C)** $\log\left[1 + \tan\left(\dfrac{x+y}{2}\right)\right] = x + c$, where c is the constant of integration
- **(D)** $\log\left[1 - \tan\left(\dfrac{x+y}{2}\right)\right] = x + c$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log\left[1 + \tan\left(\dfrac{x+y}{2}\right)\right] = x + c$, where c is the constant of integration**

**Detailed Solution:**

Let $x + y = v$

Differentiating with respect to $x$, we get $1 + \dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}v}{\text{d}x}$

$\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}v}{\text{d}x} - 1$

Substituting in the given differential equation:

$\dfrac{\text{d}v}{\text{d}x} - 1 = \sin v + \cos v$

$\dfrac{\text{d}v}{\text{d}x} = 1 + \sin v + \cos v$

$\dfrac{\text{d}v}{1 + \sin v + \cos v} = \text{d}x$

Using the half-angle formulas $\sin v = \dfrac{2\tan(v/2)}{1+\tan^2(v/2)}$ and $\cos v = \dfrac{1-\tan^2(v/2)}{1+\tan^2(v/2)}$:

$\dfrac{\text{d}v}{1 + \dfrac{2\tan(v/2)}{1+\tan^2(v/2)} + \dfrac{1-\tan^2(v/2)}{1+\tan^2(v/2)}} = \text{d}x$

$\dfrac{(1+\tan^2(v/2))\text{d}v}{1+\tan^2(v/2) + 2\tan(v/2) + 1-\tan^2(v/2)} = \text{d}x$

$\dfrac{\sec^2(v/2)\text{d}v}{2(1+\tan(v/2))} = \text{d}x$

Integrating both sides:

$\int \dfrac{\sec^2(v/2)}{2(1+\tan(v/2))} \text{d}v = \int \text{d}x$

Let $1 + \tan(v/2) = t$, then $\dfrac{1}{2}\sec^2(v/2)\text{d}v = \text{d}t$

$\int \dfrac{\text{d}t}{t} = \int \text{d}x$

$\log t = x + c$

$\log\left[1 + \tan\left(\dfrac{v}{2}\right)\right] = x + c$

Substituting $v = x + y$:

$\log\left[1 + \tan\left(\dfrac{x+y}{2}\right)\right] = x + c$

Answer: $\log\left[1 + \tan\left(\dfrac{x+y}{2}\right)\right] = x + c$, where c is the constant of integration

</details>

---

### Q20. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $e^{-x}(y+1)\text{d}y + (\cos^2 x - \sin 2x)y\, \text{d}x = 0$, given that $y = 1$ when $x = 0$ is

**Options:**

- **(A)** $\log y + \dfrac{1}{y} + e^x \cos^2 x = 1$
- **(B)** $\log y + y + e^x\cos^2 x = 2$
- **(C)** $(y+1) + e^x\cos^2 x = 2$
- **(D)** $\log\left(y + \dfrac{1}{y}\right) + e^x\cos^2 x = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log y + y + e^x\cos^2 x = 2$**

**Detailed Solution:**

The given differential equation is $e^{-x}(y+1)\text{d}y + (\cos^2 x - \sin 2x)y\, \text{d}x = 0$

Separating the variables, we get:

$\dfrac{y+1}{y}\text{d}y + e^x(\cos^2 x - \sin 2x)\text{d}x = 0$

$\left(1 + \dfrac{1}{y}\right)\text{d}y + e^x(\cos^2 x - \sin 2x)\text{d}x = 0$

Integrating both sides:

$\int \left(1 + \dfrac{1}{y}\right)\text{d}y + \int e^x(\cos^2 x - \sin 2x)\text{d}x = C$

Using the standard integral $\int e^x(f(x) + f'(x))\text{d}x = e^x f(x)$, where $f(x) = \cos^2 x$ and $f'(x) = -\sin 2x$, we get:

$y + \log y + e^x \cos^2 x = C$

Given that $y = 1$ when $x = 0$, substituting these values:

$1 + \log 1 + e^0 \cos^2 0 = C$

$1 + 0 + 1 = C \Rightarrow C = 2$

Therefore, the solution is:

$\log y + y + e^x \cos^2 x = 2$

</details>

---

### Q21. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\dfrac{dy}{dx} = e^{x-y} + x^2 e^{-y}$ is...

**Options:**

- **(A)** $y = e^x + c$
- **(B)** $e^y = e^x + x^3 + c$
- **(C)** $e^y = e^x + \dfrac{x^3}{3} + c$
- **(D)** $e^y = e^x + 2x + c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $e^y = e^x + \dfrac{x^3}{3} + c$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = e^{x-y} + x^2 e^{-y}$

This can be rewritten by factoring out $e^{-y}$ as $\dfrac{dy}{dx} = e^{-y}(e^x + x^2)$

Separating the variables, we get $e^y dy = (e^x + x^2) dx$

Integrating both sides, we get $\int e^y dy = \int (e^x + x^2) dx$

$e^y = e^x + \dfrac{x^3}{3} + c$

Answer: $e^y = e^x + \dfrac{x^3}{3} + c$

</details>

---

### Q22. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the differential equation $\begin{vmatrix} f(x) & f'(x) \\ f'(x) & f''(x) \end{vmatrix} = 0$ for all $x$ and $f(0) = 1, f'(0) = 2$, then...

**Options:**

- **(A)** $f'(x) = -f(x)$
- **(B)** $f'(x) = f(x)$
- **(C)** $f'(x) = 2f(x)$
- **(D)** $f'(x) = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f'(x) = 2f(x)$**

**Detailed Solution:**

The given differential equation is $\begin{vmatrix} f(x) & f'(x) \\ f'(x) & f''(x) \end{vmatrix} = 0$

Expanding the determinant, we get $f(x)f''(x) - (f'(x))^2 = 0$

Dividing both sides by $(f(x))^2$, we get $\dfrac{f(x)f''(x) - (f'(x))^2}{(f(x))^2} = 0$

This can be written as $\dfrac{d}{dx} \left( \dfrac{f'(x)}{f(x)} \right) = 0$

Integrating both sides with respect to $x$, we get $\dfrac{f'(x)}{f(x)} = c$

Given $f(0) = 1$ and $f'(0) = 2$

Substituting $x = 0$, we get $c = \dfrac{f'(0)}{f(0)} = \dfrac{2}{1} = 2$

Therefore, $\dfrac{f'(x)}{f(x)} = 2 \Rightarrow f'(x) = 2f(x)$

Answer: $f'(x) = 2f(x)$

</details>

---

### Q23. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\dfrac{dy}{dx} = y + 5$ and $y(0) = 4$ then $y(\log 2)$ is equal to

**Options:**

- **(A)** $2$
- **(B)** $5$
- **(C)** $7$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $13$**

**Detailed Solution:**

Given differential equation is $\dfrac{dy}{dx} = y + 5$

Separating the variables gives

$\dfrac{dy}{y + 5} = dx$

Integrating both sides gives

$\int \dfrac{dy}{y + 5} = \int dx$

$\log|y + 5| = x + C$

Using the initial condition $y(0) = 4$ gives

$\log(4 + 5) = 0 + C \Rightarrow C = \log 9$

Substituting $C$ back into the equation gives

$\log(y + 5) = x + \log 9$

$y + 5 = e^{x + \log 9} = 9e^x$

$y = 9e^x - 5$

Substituting $x = \log 2$ gives

$y(\log 2) = 9e^{\log 2} - 5$

$y(\log 2) = 9(2) - 5 = 13$

Answer: $13$

</details>

---

### Q24. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A spherical balloon expands at a rate proportional to its surface area. Initially its radius is 2 cm and 5 minutes later it increases upto 7 cm, then surface area of spherical balloon after 12 minutes will be

**Options:**

- **(A)** $2480$ sq.cm.
- **(B)** $2460$ sq.cm.
- **(C)** $2464$ sq.cm.
- **(D)** $2400$ sq.cm.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2464$ sq.cm.**

**Detailed Solution:**

Let $V$ be the volume and $S$ be the surface area of the spherical balloon.

Given that the balloon expands at a rate proportional to its surface area:

$\dfrac{dV}{dt} \propto S$

$\dfrac{dV}{dt} = kS$

Using $V = \dfrac{4}{3}\pi r^3$ and $S = 4\pi r^2$, differentiating $V$ with respect to $t$ gives:

$\dfrac{dV}{dt} = 4\pi r^2 \dfrac{dr}{dt} = S \dfrac{dr}{dt}$

Equating the two expressions for $\dfrac{dV}{dt}$:

$S \dfrac{dr}{dt} = kS \Rightarrow \dfrac{dr}{dt} = k$

Integrating both sides with respect to $t$:

$r = kt + C$

Initially, at $t = 0$, $r = 2$ cm:

$2 = k(0) + C \Rightarrow C = 2$

At $t = 5$ minutes, $r = 7$ cm:

$7 = 5k + 2 \Rightarrow 5k = 5 \Rightarrow k = 1$

Thus, the radius at any time $t$ is given by:

$r = t + 2$

After $12$ minutes ($t = 12$):

$r = 12 + 2 = 14$ cm

The surface area of the balloon at $t = 12$ minutes is:

$S = 4\pi r^2 = 4 \times \dfrac{22}{7} \times (14)^2$

$S = 4 \times \dfrac{22}{7} \times 196 = 4 \times 22 \times 28 = 2464$ sq.cm.

Answer: $2464$ sq.cm.

</details>

---

### Q25. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation $xdy + 2ydx = 0$, when $x = 2$ and $y = 1$ is

**Options:**

- **(A)** $x\sqrt{y} = 2$
- **(B)** $x\sqrt{y} = -2$
- **(C)** $\sqrt{x} y = 2$
- **(D)** $x\sqrt{y} = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x\sqrt{y} = 2$**

**Detailed Solution:**

The given differential equation is $xdy + 2ydx = 0$

Separating the variables, we get:

$\dfrac{dy}{y} + \dfrac{2dx}{x} = 0$

Integrating both sides:

$\int \dfrac{dy}{y} + 2 \int \dfrac{dx}{x} = 0$

$\ln y + 2 \ln x = \ln C$

$\ln(y x^2) = \ln C$

$x^2 y = C$

Substituting $x = 2$ and $y = 1$:

$(2)^2(1) = C \Rightarrow C = 4$

The particular solution is $x^2 y = 4$

Taking the square root on both sides:

$x\sqrt{y} = \pm 2$

Since $x = 2$ and $y = 1$ satisfies the positive root, we get:

$x\sqrt{y} = 2$

Answer: $x\sqrt{y} = 2$

</details>

---

### Q26. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $\log \left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)=2 \mathrm{x}-5 \mathrm{y}, \mathrm{y}(0)=0$ is

**Options:**

- **(A)** $2 e^{2 x}+5 e^{5 y}=6$
- **(B)** $5 e^{2 x}-2 e^{5 y}=3$
- **(C)** $2 e^{2 x}-5 e^{5 y}=6$
- **(D)** $5 e^{2 x}+2 e^{5 y}=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 e^{2 x}-2 e^{5 y}=3$**

**Detailed Solution:**

Given $\log \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right) = 2x - 5y$

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = e^{2x - 5y} = e^{2x} \cdot e^{-5y}$

Separating the variables:

$e^{5y} \mathrm{dy} = e^{2x} \mathrm{dx}$

Integrating both sides:

$\int e^{5y} \mathrm{dy} = \int e^{2x} \mathrm{dx}$

$\dfrac{e^{5y}}{5} = \dfrac{e^{2x}}{2} + C$

Using the initial condition $y(0) = 0$, substitute $x = 0$ and $y = 0$:

$\dfrac{e^{0}}{5} = \dfrac{e^{0}}{2} + C$

$\dfrac{1}{5} = \dfrac{1}{2} + C \Rightarrow C = \dfrac{1}{5} - \dfrac{1}{2} = -\dfrac{3}{10}$

Substituting the value of $C$ back into the equation:

$\dfrac{e^{5y}}{5} = \dfrac{e^{2x}}{2} - \dfrac{3}{10}$

Multiplying the entire equation by $10$:

$2e^{5y} = 5e^{2x} - 3$

$5e^{2x} - 2e^{5y} = 3$

Answer: $5 e^{2 x}-2 e^{5 y}=3$

</details>

---

### Q27. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the equation $\frac{\mathrm{dy}}{\mathrm{d} x}=\frac{1}{x+\mathrm{y}+1}$ is

**Options:**

- **(A)** $x=\log (x+\mathrm{y}+2)+\mathrm{c}$, where c is the constant of integration
- **(B)** $x=\log (x+\mathrm{y}-2)+\mathrm{c}$, where c is the constant of integration
- **(C)** $\mathrm{y}=\log (x+\mathrm{y}+2)+\mathrm{c}$, where c is the constant of integration
- **(D)** $\mathrm{y}=\log (x+\mathrm{y}-2)+\mathrm{c}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{y}=\log (x+\mathrm{y}+2)+\mathrm{c}$, where c is the constant of integration**

**Detailed Solution:**

Given differential equation is $\dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{1}{x+y+1}$

Let $x+y+1 = v$

Differentiating with respect to $x$, we get:

$1 + \dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{\mathrm{dv}}{\mathrm{d} x}$

$\Rightarrow \dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{\mathrm{dv}}{\mathrm{d} x} - 1$

Substituting this in the given equation:

$\dfrac{\mathrm{dv}}{\mathrm{d} x} - 1 = \dfrac{1}{v}$

$\Rightarrow \dfrac{\mathrm{dv}}{\mathrm{d} x} = 1 + \dfrac{1}{v} = \dfrac{v+1}{v}$

Separating the variables:

$\dfrac{v}{v+1} \mathrm{dv} = \mathrm{d} x$

$\Rightarrow \left(1 - \dfrac{1}{v+1}\right) \mathrm{dv} = \mathrm{d} x$

Integrating both sides:

$\int \left(1 - \dfrac{1}{v+1}\right) \mathrm{dv} = \int \mathrm{d} x$

$\Rightarrow v - \log(v+1) = x + c_1$

Substituting $v = x+y+1$:

$\Rightarrow x + y + 1 - \log(x+y+1+1) = x + c_1$

$\Rightarrow y + 1 - \log(x+y+2) = c_1$

$\Rightarrow y = \log(x+y+2) + c_1 - 1$

Let $c = c_1 - 1$, then:

$y = \log(x+y+2) + c$

Answer: $\mathrm{y}=\log (x+\mathrm{y}+2)+\mathrm{c}$, where c is the constant of integration

</details>

---

### Q28. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The population $p$ of the city at time $t$ is given by $\frac{d p}{d t}=\frac{p}{2}-100$.
If initial population is 100 then $\mathrm{p}=$

**Options:**

- **(A)** $200+100 e^{\frac{t}{2}}$
- **(B)** $200-100 \mathrm{e}^{\frac{\mathrm{t}}{2}}$
- **(C)** $300-100 \mathrm{e}^{\frac{\mathrm{t}}{2}}$
- **(D)** $300+100 \mathrm{e}^{\frac{t}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $200-100 \mathrm{e}^{\frac{\mathrm{t}}{2}}$**

**Detailed Solution:**

The given differential equation is $\dfrac{dp}{dt} = \dfrac{p}{2} - 100$

$\dfrac{dp}{dt} = \dfrac{p - 200}{2}$

$\dfrac{dp}{p - 200} = \dfrac{dt}{2}$

Integrating both sides, we get:

$\int \dfrac{dp}{p - 200} = \int \dfrac{dt}{2}$

$\ln |p - 200| = \dfrac{t}{2} + C$

Given that the initial population is $100$, at $t = 0$, $p = 100$.

$\ln |100 - 200| = 0 + C \Rightarrow C = \ln 100$

Substituting $C$ back into the equation:

$\ln |p - 200| = \dfrac{t}{2} + \ln 100$

$\ln \left| \dfrac{p - 200}{100} \right| = \dfrac{t}{2}$

$\left| \dfrac{p - 200}{100} \right| = e^{\dfrac{t}{2}}$

Since $p(0) = 100$, $p - 200$ is initially negative, so $|p - 200| = 200 - p$.

$\dfrac{200 - p}{100} = e^{\dfrac{t}{2}}$

$200 - p = 100 e^{\dfrac{t}{2}}$

$p = 200 - 100 e^{\dfrac{t}{2}}$

Answer: $200-100 \mathrm{e}^{\frac{\mathrm{t}}{2}}$

</details>

---

### Q29. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The equation of a curve passing through $(1,0)$ and having slope of tangent at any point $(\mathrm{x}, \mathrm{y})$ of the curve as $\frac{\mathrm{y}-1}{x^2+x}$ is

**Options:**

- **(A)** $2(\mathrm{y}-1)+x(x+1)=0$
- **(B)** $2 x-(y-1)(x+1)=0$
- **(C)** $2 x+(x+1)(y-1)=0$
- **(D)** $2 x(y-1)+(x+1)=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 x+(x+1)(y-1)=0$**

**Detailed Solution:**

The slope of the tangent at any point $(x, y)$ is given by $\dfrac{dy}{dx}$.

$\dfrac{dy}{dx} = \dfrac{y-1}{x^2+x}$

Separating the variables, we get:

$\dfrac{dy}{y-1} = \dfrac{dx}{x(x+1)}$

Using partial fractions on the right side:

$\dfrac{dy}{y-1} = \left(\dfrac{1}{x} - \dfrac{1}{x+1}\right) dx$

Integrating both sides:

$\int \dfrac{dy}{y-1} = \int \left(\dfrac{1}{x} - \dfrac{1}{x+1}\right) dx$

$\ln |y-1| = \ln |x| - \ln |x+1| + \ln |C|$

$\ln |y-1| = \ln \left| \dfrac{Cx}{x+1} \right|$

$y-1 = \dfrac{Cx}{x+1}$

Since the curve passes through $(1,0)$, substitute $x=1$ and $y=0$:

$0-1 = \dfrac{C(1)}{1+1}$

$-1 = \dfrac{C}{2} \Rightarrow C = -2$

Substituting $C = -2$ back into the equation:

$y-1 = \dfrac{-2x}{x+1}$

$(y-1)(x+1) = -2x$

$2x + (x+1)(y-1) = 0$

Answer: $2 x+(x+1)(y-1)=0$

</details>

---

### Q30. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation $\frac{\mathrm{dy}}{\mathrm{d} x}=\cot x \cdot \cot \mathrm{y}$ is

**Options:**

- **(A)** $\cos x=\mathrm{c} \operatorname{cosec} \mathrm{y}$, where c is the constant of integration.
- **(B)** $\sin x=\mathrm{c~sec~} \mathrm{y}, \quad$ where c is the constant of integration.
- **(C)** $\sin x=x \cos \mathrm{y}, \quad$ where c is the constant of integration.
- **(D)** $\cos x=\mathrm{c} \sin \mathrm{y}, \quad$ where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sin x=\mathrm{c~sec~} \mathrm{y}, \quad$ where c is the constant of integration.**

**Detailed Solution:**

Given differential equation:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \cot x \cdot \cot y$

Separating the variables, we get:

$\dfrac{\mathrm{dy}}{\cot y} = \cot x \, \mathrm{d}x$

$\tan y \, \mathrm{dy} = \cot x \, \mathrm{d}x$

Integrating both sides:

$\int \tan y \, \mathrm{dy} = \int \cot x \, \mathrm{d}x$

$\log|\sec y| = \log|\sin x| + \log|C_1|$

$\log|\sec y| = \log|C_1 \sin x|$

$\sec y = C_1 \sin x$

$\sin x = \dfrac{1}{C_1} \sec y$

$\sin x = \mathrm{c} \sec y$

where $\mathrm{c} = \dfrac{1}{C_1}$ is the constant of integration.

Answer: $\sin x=\mathrm{c~sec~} \mathrm{y}, \quad$ where c is the constant of integration.

</details>

---

### Q31. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through origin and satisfying $\left(1+x^2\right) \frac{\mathrm{dy}}{\mathrm{d} x}+2 x y=4 x^2$ is

**Options:**

- **(A)** $y\left(1+x^2\right)=4 x^3$
- **(B)** $4\left(1+x^2\right)=4+y^2$
- **(C)** $3 \mathrm{y}\left(1+x^2\right)=4 x^3$
- **(D)** $1+\mathrm{y}^2=4 x^3+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3 \mathrm{y}\left(1+x^2\right)=4 x^3$**

**Detailed Solution:**

The given differential equation is $(1+x^2) \dfrac{dy}{dx} + 2xy = 4x^2$.

This can be rewritten as the exact derivative of a product:

$\dfrac{d}{dx}[y(1+x^2)] = 4x^2$

Integrating both sides with respect to $x$, we get:

$\int \dfrac{d}{dx}[y(1+x^2)] dx = \int 4x^2 dx + C$

$y(1+x^2) = \dfrac{4x^3}{3} + C$

Since the curve passes through the origin $(0,0)$, we substitute $x=0$ and $y=0$ into the equation:

$0(1+0^2) = \dfrac{4(0)^3}{3} + C \Rightarrow C = 0$

Substituting $C = 0$ back into the equation, we get:

$y(1+x^2) = \dfrac{4x^3}{3}$

$3y(1+x^2) = 4x^3$

Answer: $3 \mathrm{y}\left(1+x^2\right)=4 x^3$

</details>

---

### Q32. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the equation $x^2 \mathrm{y}-x^3 \frac{\mathrm{dy}}{\mathrm{d} x}=\mathrm{y}^4 \cos x$, where $\mathrm{y}(0)=1$, is

**Options:**

- **(A)** $\mathrm{y}^3=3 x^2 \sin x$
- **(B)** $x^3=3 y^3 \sin x$
- **(C)** $x^3=y^3 \sin x$
- **(D)** $\mathrm{y}^3=4 x^3 \sin x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^3=3 y^3 \sin x$**

**Detailed Solution:**

The given differential equation is $x^2 y - x^3 \dfrac{dy}{dx} = y^4 \cos x$.

Dividing the entire equation by $x^3 y^4$, we get:

$\dfrac{1}{x y^3} - \dfrac{1}{y^4} \dfrac{dy}{dx} = \dfrac{\cos x}{x^3}$

Let $v = \dfrac{1}{y^3}$. Differentiating with respect to $x$, we get:

$\dfrac{dv}{dx} = -\dfrac{3}{y^4} \dfrac{dy}{dx} \Rightarrow -\dfrac{1}{y^4} \dfrac{dy}{dx} = \dfrac{1}{3} \dfrac{dv}{dx}$

Substituting this into the differential equation:

$\dfrac{1}{3} \dfrac{dv}{dx} + \dfrac{1}{x} v = \dfrac{\cos x}{x^3}$

$\dfrac{dv}{dx} + \dfrac{3}{x} v = \dfrac{3 \cos x}{x^3}$

This is a linear differential equation of the form $\dfrac{dv}{dx} + P v = Q$, where $P = \dfrac{3}{x}$ and $Q = \dfrac{3 \cos x}{x^3}$.

Integrating factor (IF) = $e^{\int \dfrac{3}{x} dx} = e^{3 \ln x} = x^3$.

The general solution is given by:

$v x^3 = \int \left( \dfrac{3 \cos x}{x^3} x^3 \right) dx + C$

$\dfrac{x^3}{y^3} = \int 3 \cos x dx + C$

$\dfrac{x^3}{y^3} = 3 \sin x + C$

$x^3 = y^3 (3 \sin x + C)$

Given the initial condition $y(0) = 1$, substituting $x = 0$ and $y = 1$ yields:

$0^3 = 1^3 (3 \sin 0 + C) \Rightarrow C = 0$

Substituting $C = 0$ back into the equation, we get:

$x^3 = 3 y^3 \sin x$

Answer: $x^3=3 y^3 \sin x$

</details>

---

### Q33. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation $x \frac{\mathrm{dy}}{\mathrm{d} x}=2 \mathrm{y}$ represents ....

**Options:**

- **(A)** a family of circles with radius $c$.
- **(B)** a family of parabolas with vertex at the origin and axis along the Y-axis
- **(C)** a family of parabolas with vertex at the origin and axis along the X-axis
- **(D)** a family of ellipses

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a family of parabolas with vertex at the origin and axis along the Y-axis**

**Detailed Solution:**

The given differential equation is $x \dfrac{\mathrm{dy}}{\mathrm{d}x} = 2y$.

Separating the variables, we get:

$\dfrac{\mathrm{dy}}{y} = 2 \dfrac{\mathrm{dx}}{x}$

Integrating both sides:

$\int \dfrac{\mathrm{dy}}{y} = 2 \int \dfrac{\mathrm{dx}}{x}$

$\ln |y| = 2 \ln |x| + \ln |c|$

$\ln |y| = \ln (cx^2)$

$y = cx^2$

This equation represents a family of parabolas with vertex at the origin and axis along the Y-axis.

Answer: a family of parabolas with vertex at the origin and axis along the Y-axis

</details>

---

### Q34. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Solution of $(2 y-x) \frac{d y}{d x}=1$ is

**Options:**

- **(A)** $x=2(y-1)+c \mathrm{e}^{-\mathrm{y}}$, where c is the constant of integration
- **(B)** $x=2(y-1)+\mathrm{ce}^{-x}$, where c is the constant of integration
- **(C)** $\mathrm{y}=2(x-1)+\mathrm{ce}^{-x}$, where c is the constant of integration
- **(D)** $\mathrm{y}=2(x-1)+\mathrm{ce}^{-\mathrm{y}}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x=2(y-1)+c \mathrm{e}^{-\mathrm{y}}$, where c is the constant of integration**

**Detailed Solution:**

Given differential equation is $(2y - x) \dfrac{dy}{dx} = 1$

This can be written as $\dfrac{dx}{dy} = 2y - x$

$\Rightarrow \dfrac{dx}{dy} + x = 2y$

This is a linear differential equation of the form $\dfrac{dx}{dy} + Px = Q$, where $P = 1$ and $Q = 2y$.

Integrating Factor (I.F.) $= e^{\int P dy} = e^{\int 1 dy} = e^y$

The general solution is given by:

$x \cdot (\text{I.F.}) = \int Q \cdot (\text{I.F.}) dy + c$

$x e^y = \int 2y e^y dy + c$

Using integration by parts:

$x e^y = 2 \left( y e^y - \int 1 \cdot e^y dy \right) + c$

$x e^y = 2(y e^y - e^y) + c$

$x e^y = 2e^y(y - 1) + c$

Dividing both sides by $e^y$:

$x = 2(y - 1) + c e^{-y}$

Answer: $x=2(y-1)+c \mathrm{e}^{-\mathrm{y}}$, where c is the constant of integration

</details>

---

### Q35. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through $\left(2, \frac{9}{2}\right)$ and having the slope $\left(1-\frac{1}{x^2}\right)$ at $(\mathrm{x}, \mathrm{y})$ is

**Options:**

- **(A)** $x y=x^2+2 x+1$
- **(B)** $x y=x^2+x+2$
- **(C)** $x y=x^2+x+5$
- **(D)** $x y=x^2+2 x+5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x y=x^2+2 x+1$**

**Detailed Solution:**

The slope of the curve at any point $(x, y)$ is given by $\dfrac{dy}{dx}$.

$\dfrac{dy}{dx} = 1 - \dfrac{1}{x^2}$

Integrating both sides with respect to $x$:

$y = \int \left(1 - \dfrac{1}{x^2}\right) dx$

$y = x + \dfrac{1}{x} + C$

Since the curve passes through the point $\left(2, \dfrac{9}{2}\right)$, substitute $x = 2$ and $y = \dfrac{9}{2}$ into the equation:

$\dfrac{9}{2} = 2 + \dfrac{1}{2} + C$

$\dfrac{9}{2} = \dfrac{5}{2} + C$

$C = \dfrac{9}{2} - \dfrac{5}{2} = 2$

Substituting $C = 2$ back into the equation of the curve:

$y = x + \dfrac{1}{x} + 2$

Multiplying the entire equation by $x$:

$xy = x^2 + 1 + 2x$

$xy = x^2 + 2x + 1$

Answer: $x y=x^2+2 x+1$

</details>

---

### Q36. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation. $\frac{\mathrm{dy}}{\mathrm{d} x}+\sin \left(\frac{x+\mathrm{y}}{2}\right)=\sin \left(\frac{x-\mathrm{y}}{2}\right)$ is

**Options:**

- **(A)** $\log \tan \left(\frac{y}{2}\right)=c-2 \sin \frac{x}{2}$, where $c$ is the constant of integration
- **(B)** $\log \tan \left(\frac{\mathrm{y}}{4}\right)=\mathrm{c}-2 \sin \left(\frac{x}{2}\right)$, where c is the constant of integration
- **(C)** $\log \left[\tan \left(\frac{\mathrm{y}}{2}+\frac{\pi}{4}\right)\right]=\mathrm{c}-2 \sin x$, where c is the constant of integration
- **(D)** $\log \left[\tan \left(\frac{\mathrm{y}}{4}+\frac{\pi}{4}\right)\right]=\mathrm{c}-2 \sin \frac{x}{2}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \tan \left(\frac{\mathrm{y}}{4}\right)=\mathrm{c}-2 \sin \left(\frac{x}{2}\right)$, where c is the constant of integration**

**Detailed Solution:**

The given differential equation is:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} + \sin \left(\dfrac{x+\mathrm{y}}{2}\right) = \sin \left(\dfrac{x-\mathrm{y}}{2}\right)$

Rearranging the terms, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \sin \left(\dfrac{x-\mathrm{y}}{2}\right) - \sin \left(\dfrac{x+\mathrm{y}}{2}\right)$

Using the trigonometric identity $\sin A - \sin B = 2 \cos\left(\dfrac{A+B}{2}\right) \sin\left(\dfrac{A-B}{2}\right)$, we have:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = 2 \cos\left(\dfrac{\dfrac{x-\mathrm{y}}{2} + \dfrac{x+\mathrm{y}}{2}}{2}\right) \sin\left(\dfrac{\dfrac{x-\mathrm{y}}{2} - \dfrac{x+\mathrm{y}}{2}}{2}\right)$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = 2 \cos\left(\dfrac{x}{2}\right) \sin\left(\dfrac{-\mathrm{y}}{2}\right)$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = -2 \cos\left(\dfrac{x}{2}\right) \sin\left(\dfrac{\mathrm{y}}{2}\right)$

Separating the variables, we get:

$\dfrac{\mathrm{dy}}{\sin\left(\dfrac{\mathrm{y}}{2}\right)} = -2 \cos\left(\dfrac{x}{2}\right) \mathrm{d}x$

$\csc\left(\dfrac{\mathrm{y}}{2}\right) \mathrm{dy} = -2 \cos\left(\dfrac{x}{2}\right) \mathrm{d}x$

Integrating both sides:

$\int \csc\left(\dfrac{\mathrm{y}}{2}\right) \mathrm{dy} = -2 \int \cos\left(\dfrac{x}{2}\right) \mathrm{d}x$

$\dfrac{\log \tan\left(\dfrac{\mathrm{y}}{4}\right)}{\dfrac{1}{2}} = -2 \dfrac{\sin\left(\dfrac{x}{2}\right)}{\dfrac{1}{2}} + \mathrm{c}'$

$2 \log \tan\left(\dfrac{\mathrm{y}}{4}\right) = -4 \sin\left(\dfrac{x}{2}\right) + \mathrm{c}'$

Dividing the entire equation by $2$:

$\log \tan\left(\dfrac{\mathrm{y}}{4}\right) = -2 \sin\left(\dfrac{x}{2}\right) + \mathrm{c}$

where $\mathrm{c} = \dfrac{\mathrm{c}'}{2}$ is the constant of integration.

Answer: $\log \tan \left(\frac{\mathrm{y}}{4}\right)=\mathrm{c}-2 \sin \left(\frac{x}{2}\right)$, where c is the constant of integration

</details>

---

### Q37. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A wet substance in the open air loses its moisture at a rate proportional to the moisture content. If a sheet, hung in the open air, loses half its moisture during the first hour, then $90 \%$ of the moisture will be lost in ...... hours.

**Options:**

- **(A)** $2 \log _2 10$
- **(B)** $\frac{4 \log 10}{\log 2}$
- **(C)** $\log _2 10$
- **(D)** $\frac{3 \log 10}{\log 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\log _2 10$**

**Detailed Solution:**

Let $M$ be the moisture content at time $t$.

Given that the rate of loss of moisture is proportional to the moisture content:

$\dfrac{dM}{dt} = -kM$

$\int \dfrac{dM}{M} = -k \int dt$

$\log M = -kt + C$

At $t = 0$, $M = M_0 \Rightarrow C = \log M_0$

$\log \left(\dfrac{M}{M_0}\right) = -kt$

At $t = 1$, half the moisture is lost, so $M = \dfrac{M_0}{2}$

$\log \left(\dfrac{1}{2}\right) = -k(1) \Rightarrow k = \log 2$

When $90 \%$ of the moisture is lost, the remaining moisture is $10 \%$ of $M_0$, so $M = \dfrac{M_0}{10}$

$\log \left(\dfrac{1}{10}\right) = -kt$

$-\log 10 = -t \log 2$

$t = \dfrac{\log 10}{\log 2} = \log_2 10$

Answer: $\log _2 10$

</details>

---

### Q38. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\mathrm{y}(x)$ and $\left(\frac{2+\sin x}{\mathrm{y}+1}\right) \frac{\mathrm{dy}}{\mathrm{d} x}=-\cos x$, $y(0)=1$, then $y\left(\frac{\pi}{2}\right)=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $-\frac{1}{3}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

Given differential equation is $\left(\dfrac{2+\sin x}{y+1}\right) \dfrac{dy}{dx} = -\cos x$

Separating the variables, we get:

$\dfrac{dy}{y+1} = -\dfrac{\cos x}{2+\sin x} dx$

Integrating both sides:

$\int \dfrac{1}{y+1} dy = -\int \dfrac{\cos x}{2+\sin x} dx$

$\ln|y+1| = -\ln|2+\sin x| + C$

$\ln|(y+1)(2+\sin x)| = C$

$(y+1)(2+\sin x) = e^C = K$

Given $y(0) = 1$, substitute $x = 0$ and $y = 1$:

$(1+1)(2+\sin 0) = K$

$2 \times 2 = K \Rightarrow K = 4$

The particular solution is:

$(y+1)(2+\sin x) = 4$

To find $y\left(\dfrac{\pi}{2}\right)$, substitute $x = \dfrac{\pi}{2}$:

$\left(y + 1\right)\left(2 + \sin\dfrac{\pi}{2}\right) = 4$

$(y + 1)(2 + 1) = 4$

$3(y + 1) = 4$

$y + 1 = \dfrac{4}{3}$

$y = \dfrac{4}{3} - 1 = \dfrac{1}{3}$

Answer: $\frac{1}{3}$

</details>

---

### Q39. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A particular solution of $3 \mathrm{e}^x \tan \mathrm{y} \mathrm{d} x+\left(1-\mathrm{e}^x\right) \sec ^2 \mathrm{y} \mathrm{dy}=0$ with $y(1)=\frac{\pi}{4} \quad$ is

**Options:**

- **(A)** $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}^3}{1-\mathrm{e}^x}\right)^3$
- **(B)** $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}^2}{1-\mathrm{e}^x}\right)^3$
- **(C)** $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}}{1-\mathrm{e}^x}\right)^3$
- **(D)** $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}^x}{1-\mathrm{e}}\right)^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}^x}{1-\mathrm{e}}\right)^3$**

**Detailed Solution:**

Given differential equation:

$3 \mathrm{e}^x \tan \mathrm{y} \, \mathrm{d}x + \left(1 - \mathrm{e}^x\right) \sec^2 \mathrm{y} \, \mathrm{dy} = 0$

Rearranging the terms to separate the variables:

$\left(1 - \mathrm{e}^x\right) \sec^2 \mathrm{y} \, \mathrm{dy} = -3 \mathrm{e}^x \tan \mathrm{y} \, \mathrm{d}x$

$\dfrac{\sec^2 \mathrm{y}}{\tan \mathrm{y}} \, \mathrm{dy} = \dfrac{-3 \mathrm{e}^x}{1 - \mathrm{e}^x} \, \mathrm{d}x$

Integrating both sides:

$\int \dfrac{\sec^2 \mathrm{y}}{\tan \mathrm{y}} \, \mathrm{dy} = 3 \int \dfrac{-\mathrm{e}^x}{1 - \mathrm{e}^x} \, \mathrm{d}x$

$\ln |\tan \mathrm{y}| = 3 \ln |1 - \mathrm{e}^x| + \ln C$

$\ln |\tan \mathrm{y}| = \ln \left|C(1 - \mathrm{e}^x)^3\right|$

$\tan \mathrm{y} = C(1 - \mathrm{e}^x)^3$

Using the initial condition $y(1) = \dfrac{\pi}{4}$, substitute $x = 1$ and $y = \dfrac{\pi}{4}$:

$\tan\left(\dfrac{\pi}{4}\right) = C(1 - \mathrm{e}^1)^3$

$1 = C(1 - \mathrm{e})^3$

$C = \dfrac{1}{(1 - \mathrm{e})^3}$

Substituting the value of $C$ back into the general solution:

$\tan \mathrm{y} = \dfrac{1}{(1 - \mathrm{e})^3} (1 - \mathrm{e}^x)^3$

$\tan \mathrm{y} = \left(\dfrac{1 - \mathrm{e}^x}{1 - \mathrm{e}}\right)^3$

Answer: $\tan \mathrm{y}=\left(\frac{1-\mathrm{e}^x}{1-\mathrm{e}}\right)^3$

</details>

---

### Q40. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of $\frac{\mathrm{dy}}{\mathrm{d} x}=2 x \mathrm{ye}^{x^2}$ is

**Options:**

- **(A)** $y=e^{-e^{x^2}} c, \quad$ where $c$ is the constant of integration
- **(B)** $y=e^{-x^2} c, \quad$ where $c$ is the constant of integration
- **(C)** $\mathrm{y}=\mathrm{e}^{\mathrm{e}^{x^2}} \mathrm{c}, \quad$ where c is the constant of integration
- **(D)** $\mathrm{y}=\mathrm{e}^{x^2} \mathrm{c}, \quad$ where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{y}=\mathrm{e}^{\mathrm{e}^{x^2}} \mathrm{c}, \quad$ where c is the constant of integration**

**Detailed Solution:**

The given differential equation is $\dfrac{\mathrm{dy}}{\mathrm{d} x} = 2 x y \mathrm{e}^{x^2}$

Separating the variables, we get:

$\dfrac{\mathrm{dy}}{y} = 2 x \mathrm{e}^{x^2} \mathrm{d} x$

Integrating both sides:

$\int \dfrac{1}{y} \mathrm{dy} = \int 2 x \mathrm{e}^{x^2} \mathrm{d} x$

Substitute $x^2 = t \Rightarrow 2x \mathrm{d} x = \mathrm{d} t$

$\int \dfrac{1}{y} \mathrm{dy} = \int \mathrm{e}^t \mathrm{d} t$

$\ln y = \mathrm{e}^t + c_1$

$\ln y = \mathrm{e}^{x^2} + c_1$

$y = \mathrm{e}^{\mathrm{e}^{x^2} + c_1}$

$y = \mathrm{e}^{\mathrm{e}^{x^2}} \cdot \mathrm{e}^{c_1}$

Let $\mathrm{e}^{c_1} = c$, where $c$ is the constant of integration.

$y = \mathrm{e}^{\mathrm{e}^{x^2}} c$

Answer: $\mathrm{y}=\mathrm{e}^{\mathrm{e}^{x^2}} \mathrm{c}, \quad$ where c is the constant of integration

</details>

---

### Q41. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A particular solution of $\frac{\mathrm{dy}}{\mathrm{d} x}=(x+9 \mathrm{y})^2$, when $x=0, \mathrm{y}=\frac{1}{27}$ is

**Options:**

- **(A)** $3 x+27 y=\tan \left[3\left(x+\frac{\pi}{12}\right)\right]$
- **(B)** $3 x+27 y=\tan \left(x+\frac{\pi}{4}\right)$
- **(C)** $3 x+27 y=\tan \left(x+\frac{\pi}{12}\right)$
- **(D)** $3 x+27 y=\tan \left[3\left(x+\frac{\pi}{4}\right)\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3 x+27 y=\tan \left[3\left(x+\frac{\pi}{12}\right)\right]$**

**Detailed Solution:**

Given $\dfrac{\mathrm{dy}}{\mathrm{d} x}=(x+9 \mathrm{y})^2$

Let $v = x + 9y$

Differentiating with respect to $x$:

$\dfrac{\mathrm{dv}}{\mathrm{d} x} = 1 + 9\dfrac{\mathrm{dy}}{\mathrm{d} x}$

Substituting $\dfrac{\mathrm{dy}}{\mathrm{d} x} = v^2$:

$\dfrac{\mathrm{dv}}{\mathrm{d} x} = 1 + 9v^2$

Separating the variables:

$\dfrac{\mathrm{dv}}{1 + 9v^2} = \mathrm{d} x$

Integrating both sides:

$\int \dfrac{\mathrm{dv}}{1 + (3v)^2} = \int \mathrm{d} x$

$\dfrac{1}{3} \tan^{-1}(3v) = x + C$

$\tan^{-1}(3v) = 3x + 3C$

Substituting $v = x + 9y$:

$\tan^{-1}(3x + 27y) = 3x + 3C$

Given $x = 0$ and $y = \dfrac{1}{27}$:

$\tan^{-1}\left(3(0) + 27\left(\dfrac{1}{27}\right)\right) = 3(0) + 3C$

$\tan^{-1}(1) = 3C$

$3C = \dfrac{\pi}{4}$

Substituting $3C$ back into the equation:

$\tan^{-1}(3x + 27y) = 3x + \dfrac{\pi}{4}$

$3x + 27y = \tan\left(3x + \dfrac{\pi}{4}\right)$

$3x + 27y = \tan\left[3\left(x + \dfrac{\pi}{12}\right)\right]$

Answer: $3 x+27 y=\tan \left[3\left(x+\frac{\pi}{12}\right)\right]$

</details>

---

### Q42. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\cos \left(\frac{\mathrm{dy}}{\mathrm{dx}}\right)=0.5, \mathrm{y}=1$ at $x=0$ is

**Options:**

- **(A)** $\cos \left(\frac{2}{x}\right)=1$
- **(B)** $\cos \left(\frac{y}{x-1}\right)=0.5$
- **(C)** $\cos \left(\frac{y-1}{x}\right)=0.5$
- **(D)** $\cos \left(\frac{y}{x}\right)=0.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\cos \left(\frac{y-1}{x}\right)=0.5$**

**Detailed Solution:**

Given differential equation is $\cos \left(\dfrac{\mathrm{dy}}{\mathrm{dx}}\right)=0.5$

$\dfrac{\mathrm{dy}}{\mathrm{dx}} = \cos^{-1}(0.5)$

Integrating both sides with respect to $x$, we get:

$y = x \cos^{-1}(0.5) + c$

Given $y=1$ when $x=0$, substituting these values:

$1 = 0 + c \Rightarrow c = 1$

Substituting $c=1$ in the general solution:

$y = x \cos^{-1}(0.5) + 1$

$\dfrac{y-1}{x} = \cos^{-1}(0.5)$

$\cos \left(\dfrac{y-1}{x}\right) = 0.5$

Answer: $\cos \left(\frac{y-1}{x}\right)=0.5$

</details>

---

### Q43. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the differential equation $\frac{d y}{d x}+\frac{x}{y}=\frac{a}{y}$ where $a$ is constant, represents a family of circles then the radius of the circle is ......

**Options:**

- **(A)** $a+2 \mathrm{c} \quad$, where c is the constant of integration
- **(B)** $\sqrt{a^2+2 c}$, where $c$ is the constant of integration
- **(C)** $a^2+2 c \quad$, where $c$ is the constant of integration
- **(D)** $\sqrt{a+c} \quad$, where $c$ is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{a^2+2 c}$, where $c$ is the constant of integration**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} + \dfrac{x}{y} = \dfrac{a}{y}$

Multiplying by $y$, we get:

$y \dfrac{dy}{dx} + x = a$

$y \, dy + x \, dx = a \, dx$

Integrating both sides, we get:

$\int y \, dy + \int x \, dx = \int a \, dx$

$\dfrac{y^2}{2} + \dfrac{x^2}{2} = ax + c$

$x^2 + y^2 - 2ax = 2c$

Adding $a^2$ to both sides to complete the square:

$x^2 - 2ax + a^2 + y^2 = a^2 + 2c$

$(x - a)^2 + y^2 = a^2 + 2c$

Comparing with the standard equation of a circle $(x - h)^2 + (y - k)^2 = r^2$, we get:

$r^2 = a^2 + 2c$

$r = \sqrt{a^2 + 2c}$

Answer: $\sqrt{a^2+2 c}$, where $c$ is the constant of integration

</details>

---

### Q44. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $\frac{\mathrm{dy}}{\mathrm{d} x}=(x+\mathrm{y})^2$ is

**Options:**

- **(A)** $\tan ^{-1}(x+y)=x+c, \quad$ where $c$ is the constant of integration
- **(B)** $x+\mathrm{y}=\tan x+\mathrm{c}, \quad$ where c is the constant of integration
- **(C)** $x+\mathrm{y}=\cot ^{-1} x+\mathrm{c}, \quad$ where c is the constant of integration
- **(D)** $x+\mathrm{y}=\sin ^{-1}(x+\mathrm{y})+\mathrm{c}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan ^{-1}(x+y)=x+c, \quad$ where $c$ is the constant of integration**

**Detailed Solution:**

Let $x+y = v$

Differentiating with respect to $x$, we get:

$1 + \dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{\mathrm{dv}}{\mathrm{d} x}$

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = \dfrac{\mathrm{dv}}{\mathrm{d} x} - 1$

Substituting this in the given differential equation, we get:

$\dfrac{\mathrm{dv}}{\mathrm{d} x} - 1 = v^2$

$\dfrac{\mathrm{dv}}{\mathrm{d} x} = 1 + v^2$

Separating the variables:

$\dfrac{\mathrm{dv}}{1 + v^2} = \mathrm{d} x$

Integrating both sides, we get:

$\int \dfrac{1}{1 + v^2} \mathrm{dv} = \int \mathrm{d} x$

$\tan^{-1} v = x + c$

Substituting $v = x+y$, we get:

$\tan^{-1}(x+y) = x + c$

Answer: $\tan ^{-1}(x+y)=x+c, \quad$ where $c$ is the constant of integration

</details>

---

### Q45. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation
$x \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}=1 \quad$ at $\quad x=\mathrm{y}=1$ with $\frac{\mathrm{dy}}{\mathrm{d} x}=0$ at $x=1$, is

**Options:**

- **(A)** $\mathrm{y}=x \log x+x+2$
- **(B)** $\mathrm{y}=x \log x-x+2$
- **(C)** $\mathrm{y}=x \log x+2$
- **(D)** $x \log x-x=\mathrm{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{y}=x \log x-x+2$**

**Detailed Solution:**

Given differential equation is $x \dfrac{d^2y}{dx^2} = 1$

$\dfrac{d^2y}{dx^2} = \dfrac{1}{x}$

Integrating with respect to $x$, we get:

$\dfrac{dy}{dx} = \log x + C_1$

Given that $\dfrac{dy}{dx} = 0$ at $x = 1$:

$0 = \log 1 + C_1 \Rightarrow C_1 = 0$

So, $\dfrac{dy}{dx} = \log x$

Integrating again with respect to $x$ using integration by parts:

$y = \int (\log x \cdot 1) dx$

$y = x \log x - \int \left(x \cdot \dfrac{1}{x}\right) dx$

$y = x \log x - x + C_2$

Given that $y = 1$ at $x = 1$:

$1 = 1 \log 1 - 1 + C_2$

$1 = -1 + C_2 \Rightarrow C_2 = 2$

Therefore, the solution is $y = x \log x - x + 2$.

Answer: $\mathrm{y}=x \log x-x+2$

</details>

---

### Q46. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\mathrm{y}(x)$ satisfies $\left(\frac{2+\sin x}{1+y}\right) \frac{\mathrm{dy}}{\mathrm{d} x}=-\cos x$. such that $y(0)=2$, then $y\left(\frac{\pi}{2}\right)$ is equal to

**Options:**

- **(A)** $4$
- **(B)** $3$
- **(C)** $2$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

The given differential equation is:

$\left(\dfrac{2+\sin x}{1+y}\right) \dfrac{\mathrm{dy}}{\mathrm{d} x} = -\cos x$

Separating the variables, we get:

$\dfrac{1}{1+y} \mathrm{dy} = -\dfrac{\cos x}{2+\sin x} \mathrm{d} x$

Integrating both sides:

$\int \dfrac{1}{1+y} \mathrm{dy} = -\int \dfrac{\cos x}{2+\sin x} \mathrm{d} x$

$\ln |1+y| = -\ln |2+\sin x| + C$

Given the initial condition $y(0) = 2$, substitute $x = 0$ and $y = 2$:

$\ln |1+2| = -\ln |2+\sin 0| + C$

$\ln 3 = -\ln 2 + C$

$C = \ln 3 + \ln 2 = \ln 6$

Substituting the value of $C$ back into the equation:

$\ln |1+y| = -\ln |2+\sin x| + \ln 6$

$\ln |1+y| = \ln \left( \dfrac{6}{2+\sin x} \right)$

Since $1+y > 0$ and $2+\sin x > 0$, we can remove the absolute value:

$1+y = \dfrac{6}{2+\sin x}$

To find $y\left(\dfrac{\pi}{2}\right)$, substitute $x = \dfrac{\pi}{2}$:

$1 + y = \dfrac{6}{2+\sin\left(\dfrac{\pi}{2}\right)}$

$1 + y = \dfrac{6}{2+1}$

$1 + y = 2$

$y = 1$

Answer: $1$

</details>

---

### Q47. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The rate of growth of bacteria in a culture is proportional to the number of bacteria present and the bacteria count is 1000 at $\mathrm{t}=0$. The number of bacteria is increased by $20 \%$ in 2 hours. If the population of bacteria is 2000 after $\frac{\mathrm{k}}{\log \left(\frac{6}{5}\right)}$ hours, then $\left(\frac{\mathrm{k}}{\log 2}\right)^2$ is

**Options:**

- **(A)** 16
- **(B)** 8
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Let $N$ be the number of bacteria at time $t$.

$\dfrac{dN}{dt} \propto N \Rightarrow \dfrac{dN}{dt} = \lambda N \Rightarrow N = c e^{\lambda t}$

At $t = 0$, $N = 1000 \Rightarrow c = 1000$

At $t = 2$, the number of bacteria increases by $20\%$, so $N = 1000 + \dfrac{20}{100} \times 1000 = 1200$

$1200 = 1000 e^{2\lambda} \Rightarrow e^{2\lambda} = \dfrac{6}{5} \Rightarrow 2\lambda = \log\left(\dfrac{6}{5}\right) \Rightarrow \lambda = \dfrac{1}{2}\log\left(\dfrac{6}{5}\right)$

Let the population be 2000 at time $t$.

$2000 = 1000 e^{\lambda t} \Rightarrow e^{\lambda t} = 2 \Rightarrow \lambda t = \log 2$

$t = \dfrac{\log 2}{\lambda} = \dfrac{2\log 2}{\log\left(\dfrac{6}{5}\right)}$

Given $t = \dfrac{k}{\log\left(\dfrac{6}{5}\right)}$, comparing gives $k = 2\log 2$.

$\left(\dfrac{k}{\log 2}\right)^2 = \left(\dfrac{2\log 2}{\log 2}\right)^2 = 2^2 = 4$

Answer: 4

</details>

---

### Q48. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The slope of tangent at $(x, y)$ to a curve passing through $\left(1, \frac{\pi}{4}\right)$ is $\frac{y}{x}-\cos ^2 \frac{y}{x}$, then the equation of curve is

**Options:**

- **(A)** $y=\tan ^{-1}\left(\log \left(\frac{\mathrm{e}}{x}\right)\right)$
- **(B)** $y=x^2\left(\tan ^{-1}\left(\log \frac{\mathrm{e}}{x}\right)\right)$
- **(C)** $y=x\left(\tan ^{-1}\left(\log \frac{\mathrm{e}}{x}\right)\right)$
- **(D)** $y=\frac{1}{x}\left(\tan ^{-1}\left(\log \frac{\mathrm{e}}{x}\right)\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=x\left(\tan ^{-1}\left(\log \frac{\mathrm{e}}{x}\right)\right)$**

**Detailed Solution:**

The given differential equation is

$\dfrac{dy}{dx} = \dfrac{y}{x} - \cos^2 \left(\dfrac{y}{x}\right)$

This is a homogeneous differential equation. Substituting $y = vx$, we get

$\dfrac{dy}{dx} = v + x\dfrac{dv}{dx}$

Substituting this in the differential equation:

$v + x\dfrac{dv}{dx} = v - \cos^2 v$

$x\dfrac{dv}{dx} = -\cos^2 v$

Separating the variables:

$\dfrac{dv}{\cos^2 v} = -\dfrac{dx}{x}$

$\sec^2 v \, dv = -\dfrac{dx}{x}$

Integrating both sides:

$\int \sec^2 v \, dv = -\int \dfrac{dx}{x}$

$\tan v = -\log x + C$

Substituting $v = \dfrac{y}{x}$:

$\tan \left(\dfrac{y}{x}\right) = -\log x + C$

Since the curve passes through $\left(1, \dfrac{\pi}{4}\right)$, substituting $x = 1$ and $y = \dfrac{\pi}{4}$:

$\tan \left(\dfrac{\pi}{4}\right) = -\log 1 + C$

$1 = 0 + C \Rightarrow C = 1$

The equation of the curve becomes:

$\tan \left(\dfrac{y}{x}\right) = 1 - \log x$

$\tan \left(\dfrac{y}{x}\right) = \log \mathrm{e} - \log x$

$\tan \left(\dfrac{y}{x}\right) = \log \left(\dfrac{\mathrm{e}}{x}\right)$

$\dfrac{y}{x} = \tan^{-1} \left(\log \left(\dfrac{\mathrm{e}}{x}\right)\right)$

$y = x \left(\tan^{-1} \left(\log \dfrac{\mathrm{e}}{x}\right)\right)$

Answer: $y=x\left(\tan ^{-1}\left(\log \frac{\mathrm{e}}{x}\right)\right)$

</details>

---

### Q49. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{d y}{d x}=\frac{3 e^{2 x}+3 e^{4 x}}{. e^x+e^{-x}}$ is

**Options:**

- **(A)** $y=\mathrm{e}^{-3 x}+\mathrm{c}$, where c is a constant of integration.
- **(B)** $y=\mathrm{e}^x+\mathrm{c}$, where c is a constant of integration.
- **(C)** $y=\mathrm{e}^{3 x}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $y=\mathrm{e}^{-x}+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=\mathrm{e}^{3 x}+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Given the differential equation:

$\dfrac{d y}{d x} = \dfrac{3 e^{2 x} + 3 e^{4 x}}{e^x + e^{-x}}$

Factor out $3 e^{2 x}$ from the numerator and $e^{-x}$ from the denominator:

$\dfrac{d y}{d x} = \dfrac{3 e^{2 x} (1 + e^{2 x})}{e^{-x} (e^{2 x} + 1)}$

Canceling the common term $(1 + e^{2 x})$ from the numerator and denominator:

$\dfrac{d y}{d x} = \dfrac{3 e^{2 x}}{e^{-x}}$

$\dfrac{d y}{d x} = 3 e^{2 x} \cdot e^x = 3 e^{3 x}$

Separating the variables:

$d y = 3 e^{3 x} d x$

Integrating both sides:

$\int d y = \int 3 e^{3 x} d x$

$y = \dfrac{3 e^{3 x}}{3} + c$

$y = e^{3 x} + c$

where $c$ is a constant of integration.

Answer: $y=\mathrm{e}^{3 x}+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q50. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y(x)$ is the solution of the differential equation $(x+2) \frac{\mathrm{d} y}{\mathrm{~d} x}=x^2+4 x-9, x \neq-2$ and $y(0)=0$, then $y(-4)$ (assuming the same constant of integration for $x < -2$) is equal to

**Options:**

- **(A)** 0
- **(B)** 1
- **(C)** -1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given the differential equation:

$(x+2) \dfrac{\mathrm{d} y}{\mathrm{d} x} = x^2+4 x-9$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{x^2+4 x+4-13}{x+2}$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{(x+2)^2-13}{x+2}$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = x+2 - \dfrac{13}{x+2}$

Integrating both sides with respect to $x$:

$y(x) = \dfrac{(x+2)^2}{2} - 13 \ln |x+2| + C$

Using the initial condition $y(0) = 0$:

$0 = \dfrac{(0+2)^2}{2} - 13 \ln |0+2| + C$

$0 = 2 - 13 \ln 2 + C$

$C = 13 \ln 2 - 2$

Substituting $C$ back into the equation for $y(x)$:

$y(x) = \dfrac{(x+2)^2}{2} - 13 \ln |x+2| + 13 \ln 2 - 2$

To find $y(-4)$, substitute $x = -4$ into the equation:

$y(-4) = \dfrac{(-4+2)^2}{2} - 13 \ln |-4+2| + 13 \ln 2 - 2$

$y(-4) = \dfrac{(-2)^2}{2} - 13 \ln |-2| + 13 \ln 2 - 2$

$y(-4) = \dfrac{4}{2} - 13 \ln 2 + 13 \ln 2 - 2$

$y(-4) = 2 - 2 = 0$

Answer: 0

</details>

---

### Q51. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The particular solution of the differential equation, $x y \frac{\mathrm{~d} y}{\mathrm{~d} x}=x^2+2 y^2$ when $y(1)=0$ is

**Options:**

- **(A)** $\frac{x^2+y^2}{x^3}=1$
- **(B)** $x^2+y^2=x$
- **(C)** $x^2+y^2=x^4$
- **(D)** $x^2+2 y^2=x^4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2+y^2=x^4$**

**Detailed Solution:**

The given differential equation is $x y \dfrac{\mathrm{d} y}{\mathrm{d} x} = x^2 + 2 y^2$.

Dividing by $xy$, we get:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{x}{y} + \dfrac{2y}{x}$

This is a homogeneous differential equation. Substituting $y = vx$, we get $\dfrac{\mathrm{d} y}{\mathrm{d} x} = v + x \dfrac{\mathrm{d} v}{\mathrm{d} x}$.

Substituting these into the equation:

$v + x \dfrac{\mathrm{d} v}{\mathrm{d} x} = \dfrac{1}{v} + 2v$

$x \dfrac{\mathrm{d} v}{\mathrm{d} x} = \dfrac{1}{v} + v = \dfrac{1 + v^2}{v}$

Separating the variables:

$\dfrac{v}{1 + v^2} \mathrm{d} v = \dfrac{\mathrm{d} x}{x}$

Integrating both sides:

$\dfrac{1}{2} \int \dfrac{2v}{1 + v^2} \mathrm{d} v = \int \dfrac{1}{x} \mathrm{d} x$

$\dfrac{1}{2} \ln(1 + v^2) = \ln x + c$

$\ln(1 + v^2) = 2 \ln x + 2c$

$\ln\left(1 + \dfrac{y^2}{x^2}\right) = \ln x^2 + \ln C$

$\ln\left(\dfrac{x^2 + y^2}{x^2}\right) = \ln(C x^2)$

$\dfrac{x^2 + y^2}{x^2} = C x^2$

$x^2 + y^2 = C x^4$

Using the initial condition $y(1) = 0$, substitute $x = 1$ and $y = 0$:

$1^2 + 0^2 = C(1)^4 \Rightarrow C = 1$

Therefore, the particular solution is $x^2 + y^2 = x^4$.

Answer: $x^2+y^2=x^4$

</details>

---

### Q52. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of $\frac{\mathrm{d} y}{\mathrm{~d} x}+\sin \left(\frac{x+y}{2}\right)=\sin \left(\frac{x-y}{2}\right)$ is

**Options:**

- **(A)** $\log \tan \left(\frac{y}{2}\right)=\mathrm{C}-2 \sin x$
- **(B)** $\log \tan \left(\frac{y}{4}\right)=\mathrm{C}-2 \sin \left(\frac{x}{2}\right)$
- **(C)** $\log \tan \left(\frac{y}{2}+\frac{\pi}{4}\right)=\mathrm{C}-2 \sin x$
- **(D)** $\quad \log \tan \left(\frac{y}{2}+\frac{\pi}{4}\right)=\mathrm{C}-2 \sin \left(\frac{x}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \tan \left(\frac{y}{4}\right)=\mathrm{C}-2 \sin \left(\frac{x}{2}\right)$**

**Detailed Solution:**

The given differential equation is:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} + \sin \left(\dfrac{x+y}{2}\right) = \sin \left(\dfrac{x-y}{2}\right)$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \sin \left(\dfrac{x-y}{2}\right) - \sin \left(\dfrac{x+y}{2}\right)$

Using the trigonometric identity $\sin A - \sin B = 2 \cos \left(\dfrac{A+B}{2}\right) \sin \left(\dfrac{A-B}{2}\right)$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = 2 \cos \left(\dfrac{x}{2}\right) \sin \left(\dfrac{-y}{2}\right)$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = -2 \cos \left(\dfrac{x}{2}\right) \sin \left(\dfrac{y}{2}\right)$

Separating the variables:

$\dfrac{\mathrm{d} y}{\sin \left(\dfrac{y}{2}\right)} = -2 \cos \left(\dfrac{x}{2}\right) \mathrm{d} x$

$\operatorname{cosec} \left(\dfrac{y}{2}\right) \mathrm{d} y = -2 \cos \left(\dfrac{x}{2}\right) \mathrm{d} x$

Integrating both sides:

$\int \operatorname{cosec} \left(\dfrac{y}{2}\right) \mathrm{d} y = -2 \int \cos \left(\dfrac{x}{2}\right) \mathrm{d} x$

$\dfrac{\log \tan \left(\dfrac{y}{4}\right)}{1/2} = -2 \dfrac{\sin \left(\dfrac{x}{2}\right)}{1/2} + \mathrm{C}_1$

$2 \log \tan \left(\dfrac{y}{4}\right) = -4 \sin \left(\dfrac{x}{2}\right) + \mathrm{C}_1$

Dividing the entire equation by $2$:

$\log \tan \left(\dfrac{y}{4}\right) = \mathrm{C} - 2 \sin \left(\dfrac{x}{2}\right)$

where $\mathrm{C} = \dfrac{\mathrm{C}_1}{2}$.

Answer: $\log \tan \left(\frac{y}{4}\right)=\mathrm{C}-2 \sin \left(\frac{x}{2}\right)$

</details>

---

### Q53. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\mathrm{e}^{y-x} \dfrac{\mathrm{~d} y}{\mathrm{~d} x}=y\left(\dfrac{\sin x+\cos x}{1+y \log y}\right)$. is

**Options:**

- **(A)** $\mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\mathrm{e}^y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.
- **(C)** $\log y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.
- **(D)** $y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

The given differential equation is:

$\mathrm{e}^{y-x} \dfrac{\mathrm{d} y}{\mathrm{d} x} = y \left( \dfrac{\sin x + \cos x}{1 + y \log y} \right)$

Rewriting the equation by separating the variables $x$ and $y$:

$\mathrm{e}^y \mathrm{e}^{-x} \dfrac{\mathrm{d} y}{\mathrm{d} x} = y \left( \dfrac{\sin x + \cos x}{1 + y \log y} \right)$

$\dfrac{\mathrm{e}^y (1 + y \log y)}{y} \mathrm{d} y = \mathrm{e}^x (\sin x + \cos x) \mathrm{d} x$

$\left( \dfrac{\mathrm{e}^y}{y} + \mathrm{e}^y \log y \right) \mathrm{d} y = \mathrm{e}^x (\sin x + \cos x) \mathrm{d} x$

Integrating both sides:

$\int \left( \mathrm{e}^y \log y + \mathrm{e}^y \dfrac{1}{y} \right) \mathrm{d} y = \int \mathrm{e}^x (\sin x + \cos x) \mathrm{d} x$

Using the standard integral formula $\int \mathrm{e}^t (f(t) + f'(t)) \mathrm{d} t = \mathrm{e}^t f(t) + \mathrm{c}$ on both sides:

For the left side, $f(y) = \log y$ and $f'(y) = \dfrac{1}{y}$.

For the right side, $f(x) = \sin x$ and $f'(x) = \cos x$.

Substituting these into the formula, we get:

$\mathrm{e}^y \log y = \mathrm{e}^x \sin x + \mathrm{c}$

Answer: $\mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q54. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=\dfrac{x+y+1}{x+y-1}$ is

**Options:**

- **(A)** $y=x+\log (x+y)+\mathrm{c}$, where c is a constant of integration.
- **(B)** $y=x-\log (x+y)+\mathrm{c}$, where c is a constant of integration.
- **(C)** $y=x-\log (2 x+y)+\mathrm{c}$, where c is a constant of integration.
- **(D)** $y=x^2+\log (x+y)+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y=x+\log (x+y)+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Let $x+y = v$. Differentiating with respect to $x$, we get:

$1 + \dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d} v}{\mathrm{d} x}$

$\Rightarrow \dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d} v}{\mathrm{d} x} - 1$

Substituting this into the given differential equation:

$\dfrac{\mathrm{d} v}{\mathrm{d} x} - 1 = \dfrac{v+1}{v-1}$

$\dfrac{\mathrm{d} v}{\mathrm{d} x} = \dfrac{v+1}{v-1} + 1$

$\dfrac{\mathrm{d} v}{\mathrm{d} x} = \dfrac{v+1+v-1}{v-1} = \dfrac{2v}{v-1}$

Separating the variables:

$\dfrac{v-1}{v} \mathrm{d} v = 2 \mathrm{d} x$

$\left(1 - \dfrac{1}{v}\right) \mathrm{d} v = 2 \mathrm{d} x$

Integrating both sides:

$\int \left(1 - \dfrac{1}{v}\right) \mathrm{d} v = \int 2 \mathrm{d} x$

$v - \log (v) = 2x + \mathrm{c}_1$

Substituting back $v = x+y$:

$x+y - \log (x+y) = 2x + \mathrm{c}_1$

$y = x + \log (x+y) + \mathrm{c}_1$

Replacing $\mathrm{c}_1$ with $\mathrm{c}$, we get:

$y = x + \log (x+y) + \mathrm{c}$

Answer: $y=x+\log (x+y)+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q55. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=\dfrac{y+\sqrt{x^2-y^2}}{x}$ is

**Options:**

- **(A)** $\sin ^{-1} y=\log x+\mathrm{c}$, where c is a constant of integration.
- **(B)** $\dfrac{y}{x}=\sin ^{-1} x+\mathrm{c}$, where c is a constant of integration.'
- **(C)** $\dfrac{y}{x}=\sqrt{x^2-y^2}+\mathrm{c}$, where c is a constant of integration.
- **(D)** $\sin ^{-1}\left(\dfrac{y}{x}\right)=\log x+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sin ^{-1}\left(\dfrac{y}{x}\right)=\log x+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

The given differential equation is $\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{y+\sqrt{x^2-y^2}}{x}$

Dividing the numerator by $x$, we get:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{y}{x} + \sqrt{1 - \left(\dfrac{y}{x}\right)^2}$

This is a homogeneous differential equation. Substituting $y = vx$, we have $\dfrac{\mathrm{d} y}{\mathrm{d} x} = v + x \dfrac{\mathrm{d} v}{\mathrm{d} x}$

$v + x \dfrac{\mathrm{d} v}{\mathrm{d} x} = v + \sqrt{1 - v^2}$

$x \dfrac{\mathrm{d} v}{\mathrm{d} x} = \sqrt{1 - v^2}$

Separating the variables:

$\dfrac{\mathrm{d} v}{\sqrt{1 - v^2}} = \dfrac{\mathrm{d} x}{x}$

Integrating both sides:

$\int \dfrac{\mathrm{d} v}{\sqrt{1 - v^2}} = \int \dfrac{\mathrm{d} x}{x}$

$\sin^{-1} v = \log x + \mathrm{c}$

Substituting back $v = \dfrac{y}{x}$:

$\sin^{-1}\left(\dfrac{y}{x}\right) = \log x + \mathrm{c}$

Answer: $\sin ^{-1}\left(\dfrac{y}{x}\right)=\log x+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q56. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of differential equation $\left(1+y^2\right)(1+\log x) \mathrm{d} x+x \mathrm{~d} y=0$ at $x=1, y=1$ is

**Options:**

- **(A)** $\log x-\dfrac{1}{2}(\log x)^2-\tan ^{-1} y=-\dfrac{\pi}{4}$
- **(B)** $\quad \log x+\dfrac{1}{2}(\log x)^2+\tan ^{-1} y=\dfrac{\pi}{4}$
- **(C)** $\log x-\dfrac{1}{2}(\log x)^2+\tan ^{-1} y=\dfrac{\pi}{4}$
- **(D)** $\log x+\dfrac{1}{2}(\log x)^2-\tan ^{-1} y=\dfrac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\quad \log x+\dfrac{1}{2}(\log x)^2+\tan ^{-1} y=\dfrac{\pi}{4}$**

**Detailed Solution:**

The given differential equation is:

$(1+y^2)(1+\log x) \mathrm{d} x + x \mathrm{~d} y = 0$

Separating the variables, we get:

$\dfrac{1+\log x}{x} \mathrm{d} x + \dfrac{1}{1+y^2} \mathrm{d} y = 0$

Integrating both sides:

$\int \dfrac{1+\log x}{x} \mathrm{d} x + \int \dfrac{1}{1+y^2} \mathrm{d} y = C$

For the first integral, substitute $t = \log x \Rightarrow \mathrm{d}t = \dfrac{1}{x} \mathrm{d}x$:

$\int (1+t) \mathrm{d} t + \tan^{-1} y = C$

$t + \dfrac{t^2}{2} + \tan^{-1} y = C$

Substituting back $t = \log x$:

$\log x + \dfrac{1}{2}(\log x)^2 + \tan^{-1} y = C$

To find the particular solution, apply the given condition $x=1, y=1$:

$\log 1 + \dfrac{1}{2}(\log 1)^2 + \tan^{-1} 1 = C$

$0 + 0 + \dfrac{\pi}{4} = C \Rightarrow C = \dfrac{\pi}{4}$

Therefore, the particular solution is:

$\log x + \dfrac{1}{2}(\log x)^2 + \tan^{-1} y = \dfrac{\pi}{4}$

Answer: $\quad \log x+\dfrac{1}{2}(\log x)^2+\tan ^{-1} y=\dfrac{\pi}{4}$

</details>

---

### Q57. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\dfrac{1}{x} \dfrac{\mathrm{~d} y}{\mathrm{~d} x}=\tan ^{-1} x$ is

**Options:**

- **(A)** $y+\dfrac{x^2 \tan ^{-1} x}{2}+\mathrm{c}=0$, where c is a constant of integration.
- **(B)** $y+x \tan ^{-1} x+\mathrm{c}=0$, where c is a constant integration.
- **(C)** $y-x-\tan ^{-1} x+\mathrm{c}=0$, where is a constant of integration.
- **(D)** $y=\dfrac{x^2 \tan ^{-1} x}{2}-\dfrac{1}{2}\left(x-\tan ^{-1} x\right)+\mathrm{c}$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=\dfrac{x^2 \tan ^{-1} x}{2}-\dfrac{1}{2}\left(x-\tan ^{-1} x\right)+\mathrm{c}$, where c is constant of integration.**

**Detailed Solution:**

The given differential equation is $\dfrac{1}{x} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \tan^{-1} x$

Rearranging the terms, we get:

$\mathrm{d}y = x \tan^{-1} x \, \mathrm{d}x$

Integrating both sides:

$\int \mathrm{d}y = \int x \tan^{-1} x \, \mathrm{d}x$

Using integration by parts on the right-hand side, taking $\tan^{-1} x$ as the first function and $x$ as the second function:

$y = \tan^{-1} x \int x \, \mathrm{d}x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d}x} (\tan^{-1} x) \int x \, \mathrm{d}x \right) \mathrm{d}x$

$y = \dfrac{x^2}{2} \tan^{-1} x - \int \dfrac{1}{1+x^2} \cdot \dfrac{x^2}{2} \, \mathrm{d}x$

$y = \dfrac{x^2}{2} \tan^{-1} x - \dfrac{1}{2} \int \dfrac{x^2 + 1 - 1}{1+x^2} \, \mathrm{d}x$

$y = \dfrac{x^2}{2} \tan^{-1} x - \dfrac{1}{2} \int \left( 1 - \dfrac{1}{1+x^2} \right) \mathrm{d}x$

$y = \dfrac{x^2}{2} \tan^{-1} x - \dfrac{1}{2} \left( x - \tan^{-1} x \right) + \mathrm{c}$

where $\mathrm{c}$ is the constant of integration.

Answer: $y=\dfrac{x^2 \tan ^{-1} x}{2}-\dfrac{1}{2}\left(x-\tan ^{-1} x\right)+\mathrm{c}$, where c is constant of integration.

</details>

---

### Q58. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Given that the slope of the tangent to a curve $y=y(x)$ at any point $(x, y)$ is $\dfrac{2 y}{x^2}$. If the curve passes through the centre of the circle $x^2+y^2-2 x-2 y=0$, then its equation is

**Options:**

- **(A)** $\quad x \log |y|=x-1$
- **(B)** $x \log |y|=-2(x-1)$
- **(C)** $\quad x \log |y|=2(x-1)$
- **(D)** $x^2 \log |y|=-2(x-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad x \log |y|=2(x-1)$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} = \dfrac{2y}{x^2}$

Separating the variables, we get:

$\dfrac{dy}{y} = \dfrac{2}{x^2} dx$

Integrating both sides:

$\int \dfrac{dy}{y} = \int \dfrac{2}{x^2} dx$

$\log |y| = -\dfrac{2}{x} + C$

The curve passes through the centre of the circle $x^2+y^2-2x-2y=0$.

The centre of the given circle is $(1, 1)$.

Substituting $x=1$ and $y=1$ in the equation of the curve:

$\log |1| = -\dfrac{2}{1} + C$

$0 = -2 + C \Rightarrow C = 2$

Substituting the value of $C$ back into the equation:

$\log |y| = -\dfrac{2}{x} + 2$

Multiplying by $x$ on both sides:

$x \log |y| = -2 + 2x$

$x \log |y| = 2(x - 1)$

Answer: $\quad x \log |y|=2(x-1)$

</details>

---

### Q59. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $(2+\sin x) \dfrac{\mathrm{d} y}{\mathrm{~d} x}+(y+1) \cos x=0$ and $y(0)=1$, then $y\left(\dfrac{\pi}{2}\right)$ is equal to

**Options:**

- **(A)** $-\dfrac{2}{3}$
- **(B)** $-\dfrac{1}{3}$
- **(C)** $\dfrac{4}{3}$
- **(D)** $\dfrac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{3}$**

**Detailed Solution:**

The given differential equation is $(2+\sin x) \dfrac{\mathrm{d} y}{\mathrm{d} x}+(y+1) \cos x=0$

This can be rewritten as:

$\dfrac{\mathrm{d}}{\mathrm{d} x} [(y+1)(2+\sin x)] = 0$

Integrating both sides with respect to $x$, we get:

$(y+1)(2+\sin x) = C$

Given $y(0)=1$, substitute $x=0$ and $y=1$:

$(1+1)(2+\sin 0) = C$

$2 \times 2 = C \Rightarrow C = 4$

So, the equation of the curve is:

$(y+1)(2+\sin x) = 4$

To find $y\left(\dfrac{\pi}{2}\right)$, substitute $x = \dfrac{\pi}{2}$:

$\left(y\left(\dfrac{\pi}{2}\right)+1\right)\left(2+\sin \dfrac{\pi}{2}\right) = 4$

$\left(y\left(\dfrac{\pi}{2}\right)+1\right)(2+1) = 4$

$3\left(y\left(\dfrac{\pi}{2}\right)+1\right) = 4$

$y\left(\dfrac{\pi}{2}\right)+1 = \dfrac{4}{3}$

$y\left(\dfrac{\pi}{2}\right) = \dfrac{4}{3} - 1 = \dfrac{1}{3}$

Answer: $\dfrac{1}{3}$

</details>

---

### Q60. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=y(x)$ is the solution of the differential equation $\left(\dfrac{5+\mathrm{e}^x}{2+y}\right) \dfrac{\mathrm{d} y}{\mathrm{~d} x}+\mathrm{e}^x=0$ satisfying $y(0)=1$, then a value of $y(\log 13)$ is

**Options:**

- **(A)** $\quad-1$
- **(B)** 0
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\quad-1$**

**Detailed Solution:**

Given differential equation is $\left(\dfrac{5+\mathrm{e}^x}{2+y}\right) \dfrac{\mathrm{d} y}{\mathrm{d} x}+\mathrm{e}^x=0$

Separating the variables, we get:

$\dfrac{\mathrm{d} y}{2+y} = -\dfrac{\mathrm{e}^x}{5+\mathrm{e}^x} \mathrm{d} x$

Integrating both sides:

$\int \dfrac{\mathrm{d} y}{2+y} = -\int \dfrac{\mathrm{e}^x}{5+\mathrm{e}^x} \mathrm{d} x$

$\ln |2+y| = -\ln (5+\mathrm{e}^x) + C$

Using the initial condition $y(0)=1$:

$\ln |2+1| = -\ln (5+\mathrm{e}^0) + C$

$\ln 3 = -\ln 6 + C \Rightarrow C = \ln 18$

Substituting $C$ back into the equation:

$\ln |2+y| = -\ln (5+\mathrm{e}^x) + \ln 18$

$\ln |2+y| = \ln \left(\dfrac{18}{5+\mathrm{e}^x}\right)$

Since $y(0)=1$, $2+y > 0$, so we can remove the absolute value:

$2+y = \dfrac{18}{5+\mathrm{e}^x}$

$y = \dfrac{18}{5+\mathrm{e}^x} - 2$

To find $y(\log 13)$, substitute $x = \log 13$ (which means $\ln 13$):

$y(\log 13) = \dfrac{18}{5+\mathrm{e}^{\ln 13}} - 2$

$y(\log 13) = \dfrac{18}{5+13} - 2$

$y(\log 13) = \dfrac{18}{18} - 2 = 1 - 2 = -1$

Answer: $\quad-1$

</details>

---

### Q61. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x \dfrac{\mathrm{~d} y}{\mathrm{~d} x}=y(\log y-\log x+1)$, then general solution of this equation is

**Options:**

- **(A)** $\log \left(\dfrac{x}{y}\right)=\mathrm{c} y$, where c is a constant of integration.
- **(B)** $\log \left(\dfrac{x}{y}\right)=c x$, where c is a constant of integration.
- **(C)** $\log \left(\dfrac{y}{x}\right)=\mathrm{cy}$, where c is a constant of integration.
- **(D)** $\log \left(\dfrac{y}{x}\right)=\mathrm{c} x$, where c is a constant of integration:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log \left(\dfrac{y}{x}\right)=\mathrm{c} x$, where c is a constant of integration:**

**Detailed Solution:**

The given differential equation is $x \dfrac{\mathrm{d}y}{\mathrm{d}x} = y(\log y - \log x + 1)$

Dividing by $x$, we get:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{y}{x} \left( \log\left(\dfrac{y}{x}\right) + 1 \right)$

This is a homogeneous differential equation. Let $y = vx$, then $\dfrac{\mathrm{d}y}{\mathrm{d}x} = v + x \dfrac{\mathrm{d}v}{\mathrm{d}x}$

Substituting these values into the equation, we get:

$v + x \dfrac{\mathrm{d}v}{\mathrm{d}x} = v (\log v + 1)$

$v + x \dfrac{\mathrm{d}v}{\mathrm{d}x} = v \log v + v$

$x \dfrac{\mathrm{d}v}{\mathrm{d}x} = v \log v$

Separating the variables, we get:

$\dfrac{\mathrm{d}v}{v \log v} = \dfrac{\mathrm{d}x}{x}$

Integrating both sides:

$\int \dfrac{\mathrm{d}v}{v \log v} = \int \dfrac{\mathrm{d}x}{x}$

$\log(\log v) = \log x + \log c$

$\log(\log v) = \log(cx)$

$\log v = cx$

Substituting $v = \dfrac{y}{x}$, we get:

$\log\left(\dfrac{y}{x}\right) = cx$

Answer: $\log \left(\dfrac{y}{x}\right)=\mathrm{c} x$, where c is a constant of integration:

</details>

---

### Q62. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\dfrac{\mathrm{d} y}{\mathrm{~d} x}=(x-y)^2$ when $y(1)=1$ is

**Options:**

- **(A)** $\quad \log \left|\dfrac{2-y}{2-x}\right|=2(y-1)$
- **(B)** $\quad-\log \left|\dfrac{1+x-y}{1-x+y}\right|=x+y-2$
- **(C)** $\quad \log \left|\dfrac{2-x}{2-y}\right|=x-y$
- **(D)** $\quad-\log \left|\dfrac{1-x+y}{1+x-y}\right|=2(x-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad-\log \left|\dfrac{1-x+y}{1+x-y}\right|=2(x-1)$**

**Detailed Solution:**

Given the differential equation:

$\dfrac{\mathrm{d} y}{\mathrm{~d} x}=(x-y)^2$

Let $x-y=v$. Differentiating with respect to $x$, we get:

$1-\dfrac{\mathrm{d} y}{\mathrm{~d} x}=\dfrac{\mathrm{d} v}{\mathrm{~d} x} \Rightarrow \dfrac{\mathrm{d} y}{\mathrm{~d} x}=1-\dfrac{\mathrm{d} v}{\mathrm{~d} x}$

Substituting this into the differential equation:

$1-\dfrac{\mathrm{d} v}{\mathrm{~d} x}=v^2$

$\dfrac{\mathrm{d} v}{\mathrm{~d} x}=1-v^2$

Separating the variables and integrating both sides:

$\int \dfrac{\mathrm{d} v}{1-v^2}=\int \mathrm{d} x$

$\dfrac{1}{2} \log \left|\dfrac{1+v}{1-v}\right|=x+C$

Substituting back $v=x-y$:

$\dfrac{1}{2} \log \left|\dfrac{1+x-y}{1-x+y}\right|=x+C$

Using the initial condition $y(1)=1$, substitute $x=1$ and $y=1$:

$\dfrac{1}{2} \log \left|\dfrac{1+1-1}{1-1+1}\right|=1+C$

$\dfrac{1}{2} \log (1)=1+C \Rightarrow 0=1+C \Rightarrow C=-1$

Substituting $C=-1$ back into the equation:

$\dfrac{1}{2} \log \left|\dfrac{1+x-y}{1-x+y}\right|=x-1$

$\log \left|\dfrac{1+x-y}{1-x+y}\right|=2(x-1)$

Using the property $\log \left(\dfrac{a}{b}\right) = -\log \left(\dfrac{b}{a}\right)$, we get:

$-\log \left|\dfrac{1-x+y}{1+x-y}\right|=2(x-1)$

Answer: $\quad-\log \left|\dfrac{1-x+y}{1+x-y}\right|=2(x-1)$

</details>

---

### Q63. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $\cos x(1+\cos y) \mathrm{d} x-\sin y(1+\sin x) \mathrm{d} y=0$ is

**Options:**

- **(A)** $(1+\cos x)(1+\sin y)=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $1+\sin x+\cos y=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $(1+\sin x)(1+\cos y)=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $1+\sin x \cos y=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1+\sin x)(1+\cos y)=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$$
\begin{aligned}
& \cos x(1+\cos y) \mathrm{d} x-\sin y(1+\sin x) \mathrm{d} y=0 \\
& \Rightarrow \frac{\cos x}{1+\sin x} \mathrm{~d} x-\frac{\sin y}{1+\cos y} \mathrm{~d} y=0
\end{aligned}
$$

Integrating on both sides, we get
$$
\begin{aligned}
& \log |1+\sin x|+\log |1+\cos y|=\log |c| \\
& \Rightarrow \log |(1+\sin x)(1+\cos y)|=\log |c| \\
& \Rightarrow(1+\sin x)(1+\cos y)=c
\end{aligned}
$$

</details>

---

### Q64. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $(1+x y) y \mathrm{~d} x+(1-x y) x \mathrm{~d} y=0$ is.

**Options:**

- **(A)** $\log \left(\frac{x}{y}\right)+\frac{1}{x y}=\mathrm{k}$, where $\mathrm{k}$ is constant of integration.
- **(B)** $\log \left(\frac{x}{y}\right)=\frac{1}{x y}+\mathrm{k}$, where $\mathrm{k}$ is constant of integration.
- **(C)** $\log \left(\frac{x}{y}\right)+x y=\mathrm{k}$, where $\mathrm{k}$ is constant of integration.
- **(D)** $\log \left(\frac{x}{y}\right)=x y+\mathrm{k}$, where $\mathrm{k}$ is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left(\frac{x}{y}\right)=\frac{1}{x y}+\mathrm{k}$, where $\mathrm{k}$ is constant of integration.**

**Detailed Solution:**

$(1+x y) y \mathrm{~d} x+(1-x y) x \mathrm{~d} y=0$
$\Rightarrow y \mathrm{~d} x+x \mathrm{~d} y+x y^2 \mathrm{~d} x-x^2 y \mathrm{~d} y=0$
$\Rightarrow \frac{y \mathrm{~d} x+x \mathrm{~d} y}{x^2 y^2}+\frac{\mathrm{d} x}{x}-\frac{\mathrm{d} y}{y}=0$
$\Rightarrow \frac{\mathrm{d}(x y)}{x^2 y^2}+\frac{\mathrm{d} x}{x}-\frac{\mathrm{d} y}{y}=0$
Integrating on both sides, we get
$-\frac{1}{x y}+\log x-\log y=\mathrm{k}$
$\Rightarrow \log \left(\frac{x}{y}\right)=\frac{1}{x y}+\mathrm{k}$

</details>

---

### Q65. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of differential equation $\mathrm{e}^{\frac{d y}{d x}}=(x+1), y(0)=3$ is

**Options:**

- **(A)** $y=x \log x-x+2$
- **(B)** $y=(x+1) \log (x+1)-x+3$
- **(C)** $y=(x+1) \log (x+1)+x-3$
- **(D)** $y=x \log x+x-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y=(x+1) \log (x+1)-x+3$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{e}^{\frac{\mathrm{d}}{\mathrm{d} x}}=(x+1) \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\log (x+1)
\end{aligned}
$$
Integrating on both sides, we get
$$
\begin{aligned}
\int \mathrm{d} y & =\int \log (x+1) \mathrm{d} x+\mathrm{c} \\
\Rightarrow y & =x \log (x+1)-\int \frac{x}{x+1} \mathrm{~d} x+\mathrm{c} \\
& =x \log (x+1)-\int \frac{x+1-1}{x+1} \mathrm{~d} x+\mathrm{c} \\
& =x \log (x+1)-\int\left(1-\frac{1}{x+1}\right) \mathrm{d} x+\mathrm{c} \\
y & =x \log (x+1)-x+\log (x+1)+\mathrm{c} .
\end{aligned}
$$
Since $y(0)=3$, i.e., $y=3$ when $x=0$
$$
\begin{aligned}
& 3=0+\mathrm{c} \Rightarrow \mathrm{c}=3 \\
& y=x \log (x+1)+\log (x+1)-x+3 \\
& y=(x+1) \log (x+1)-x+3
\end{aligned}
$$

</details>

---

### Q66. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\mathrm{e}^{-x}(y+1) \mathrm{d} y+\left(\cos ^2 x-\sin 2 x\right) y \mathrm{~d} x=0$ at $x=0$, $y=1$ is

**Options:**

- **(A)** $(y+1)+\mathrm{e}^x \cos ^2 x=2$
- **(B)** $y+\log y=\mathrm{e}^x \cos ^2 x$
- **(C)** $\log (y+1)+\mathrm{e}^x \cos ^2 x=1$
- **(D)** $y+\log y+\mathrm{e}^x \cos ^2 x=2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y+\log y+\mathrm{e}^x \cos ^2 x=2$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{e}^{-x}(y+1) \mathrm{d} y+\left(\cos ^2 x-\sin 2 x\right) y \mathrm{~d} x=0 \\
& \Rightarrow \frac{y+1}{y} \mathrm{~d} y+\mathrm{e}^x\left(\cos ^2 x-\sin 2 x\right) \mathrm{d} x=0
\end{aligned}
$$
Integrating on both sides, we get
$$
\begin{aligned}
& \int\left(1+\frac{1}{y}\right) \mathrm{d} y+\int \mathrm{e}^x\left(\cos ^2 x-2 \sin x \cos x\right) \mathrm{d} x=\mathrm{c} \\
& \Rightarrow y+\log |y|+\mathrm{e}^x \cos ^2 x=\mathrm{c} \\
& \text { At } x=0, y=1 \\
\therefore \quad & 1+\log 1+\mathrm{e}^0 \cos ^2 0=\mathrm{c} \\
& \Rightarrow \mathrm{c}=2 \\
\therefore \quad & y+\log |y|+\mathrm{e}^x \cos ^2 x=2
\end{aligned}
$$

</details>

---

### Q67. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $(2+\sin x) \frac{\mathrm{d} y}{\mathrm{~d} x}+(y+1) \cos x=0$ and $y(0)=1$, then $y\left(\frac{\pi}{2}\right)$ is

**Options:**

- **(A)** $\frac{-2}{3}$
- **(B)** $\frac{-1}{3}$
- **(C)** $\frac{4}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{array}{ll} & (2+\sin x) \frac{\mathrm{d} y}{\mathrm{~d} x}+(y+1) \cos x=0 \\ \therefore \quad & \frac{1}{y+1} \mathrm{~d} y=\frac{-\cos x}{2+\sin x} \mathrm{~d} x \\ \therefore \quad & \text { Integrating both sides, we get } \\ & \log (y+1)=-\log (2+\sin x)+\mathrm{c} \ldots \text { (i) } \\ & \text { when } x=0, y=1 \\ & \Rightarrow \mathrm{c}=2 \log 2 \\ \therefore \quad & (\mathrm{i}) \Rightarrow \log (y+1)=-\log (2+\sin x)+\log 4 \\ & \Rightarrow \log (y+1)=\log \left(\frac{4}{2+\sin x}\right) \\ & \Rightarrow y+1=\frac{4}{2+\sin x} \\ & \quad \text { When } x=\frac{\pi}{2}, \text { (ii) } \Rightarrow y=\frac{4}{3}-1=\frac{1}{3}\end{array}$

</details>

---

### Q68. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The solution of $\mathrm{e}^{y-x} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{y(\sin x+\cos x)}{(1+y \log y)}$ is

**Options:**

- **(A)** $\frac{\mathrm{e}^y}{y}=\mathrm{e}^x \sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\mathrm{e}^y \log y=\mathrm{e}^x \cos x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\mathrm{e}^y y=\mathrm{e}^x \sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\begin{array}{ll} & \mathrm{e}^{y-x} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{y(\sin x+\cos x)}{(1+y \log y)} \\ \therefore \quad & \mathrm{e}^y \frac{(1+y \log y)}{y} \mathrm{~d} y=\mathrm{e}^x(\sin x+\cos x) \mathrm{d} x \\ \therefore \quad & \int \mathrm{e}^y\left(\log y+\frac{1}{y}\right) \mathrm{d} y=\int \mathrm{e}^x(\sin x+\cos x) \mathrm{d} x \\ & \Rightarrow \mathrm{e}^y \log y=\mathrm{e}^x \sin x+\mathrm{c} \\ & \ldots\left[\because \int \mathrm{e}^x\left(\mathrm{f}(x)+\mathrm{f}^{\prime}(x)\right) \mathrm{d} x=\mathrm{e}^x \mathrm{f}(x)+\mathrm{c}\right]\end{array}$

</details>

---

### Q69. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\log (x+y)=2 x y$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** 1
- **(B)** -1
- **(C)** 2
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$$
\log (x+y)=2 x y
$$
Differentiating w.r.t. $x$, we get
$$
\begin{array}{ll} 
& \frac{1}{x+y}\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)=2 y+2 x \frac{\mathrm{d} y}{\mathrm{~d} x} \\
\therefore \quad & \frac{1}{x+y}+\frac{1}{x+y} \frac{\mathrm{d} y}{\mathrm{~d} x}=2 y+2 x \frac{\mathrm{d} y}{\mathrm{~d} x} \\
& \text { At } x=0,(\mathrm{i}) \Rightarrow y=1 \\
\therefore \quad & \text { (ii) }\left.\Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}\right|_{x=0}=1
\end{array}
$$

</details>

---

### Q70. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\frac{\mathrm{d} y}{\mathrm{~d} x}=y+3$ and $y(0)=2$, then $y(\log 2)=$

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** 13
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 7**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{\mathrm{d} y}{\mathrm{~d} x}=y+3 \\
& \Rightarrow \frac{\mathrm{d} y}{y+3}=\mathrm{d} x
\end{aligned}
$$
Integrating on both sides, we get
$$
\begin{array}{ll} 
& \int \frac{\mathrm{d} y}{y+3}=\int \mathrm{d} x+\mathrm{c} \\
\Rightarrow & \log (y+3)=x+\mathrm{c} \\
& y=2 \text { when } x=0 \\
\therefore \quad & \log (2+3)=0+\mathrm{c} \Rightarrow \mathrm{c}=\log 5 \\
\therefore \quad & \log (y+3)=x+\log 5 \\
& \Rightarrow y+3=5 \mathrm{e}^x \\
\Rightarrow y=5 \mathrm{e}^x-3 & \\
\therefore \quad & y(\log 2)=5 \mathrm{e}^{\log 2}-3=10-3 \\
& =7
\end{array}
$$

</details>

---

### Q71. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation $\cos (x+y) \mathrm{d} y=\mathrm{d} x$ has the general solution given by

**Options:**

- **(A)** $y=\sin (x+y)+\mathrm{c}$, where $\mathrm{c}$ is a constant.
- **(B)** $y=\tan (x+y)+\mathrm{c}$, where c is a constant
- **(C)** $y=\tan \left(\frac{x+y}{2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant
- **(D)** $y=\frac{1}{2} \tan (x+y)+\mathrm{c}$, where $\mathrm{c}$ is a constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=\tan \left(\frac{x+y}{2}\right)+\mathrm{c}$, where $\mathrm{c}$ is a constant**

**Detailed Solution:**

$$
\begin{aligned}
& \cos (x+y) \mathrm{d} y=\mathrm{d} x \\
\therefore \quad & \frac{\mathrm{d} x}{\mathrm{~d} y}=\cos (x+y)
\end{aligned}
$$
Put $x+y=\mathrm{u}$ Differentiating w.r.t. $y$, we get $\frac{\mathrm{d} x}{\mathrm{~d} y}+1=\frac{\mathrm{du}}{\mathrm{d} y}$
$$
\therefore \quad \frac{\mathrm{d} x}{\mathrm{~d} y}=\frac{\mathrm{du}}{\mathrm{d} y}-1
$$

Substituting (ii) and (iii) in (i), we get
$$
\begin{aligned}
& \frac{\mathrm{du}}{\mathrm{d} y}-1=\cos \mathrm{u} \\
& \therefore \quad \frac{\mathrm{du}}{1+\operatorname{cosu}}=\mathrm{d} y \\
& \therefore \quad \frac{\mathrm{du}}{2 \cos ^2\left(\frac{\mathrm{u}}{2}\right)}=\mathrm{d} y
\end{aligned}
$$
Integrating on both sides, we get
$$
\begin{aligned}
& \quad \frac{1}{2} \int \sec ^2\left(\frac{\mathrm{u}}{2}\right) \mathrm{du}=\int \mathrm{d} y \\
& \therefore \quad y=\tan \left(\frac{x+y}{2}\right)+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q72. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+y^2}{1+x^2}$ is

**Options:**

- **(A)** $x+y=\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $x-y=\mathrm{c}(x y)$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $x+y=\mathrm{c}(1+x y)$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $y-x=\mathrm{c}(1+x y)$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y-x=\mathrm{c}(1+x y)$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

No Solution Available

</details>

---

### Q73. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $\cos x(1+\cos y) \mathrm{d} x-\sin y(1+\sin x) \mathrm{d} y=0$ is

**Options:**

- **(A)** $(1+\cos x)(1+\sin y)=\mathrm{c}$
- **(B)** $1+\sin x+\cos y=c$
- **(C)** $(1+\sin x)(1+\cos y)=c$
- **(D)** $1+\sin x \cdot \cos y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1+\sin x)(1+\cos y)=c$**

**Detailed Solution:**

Given differential equation is
$\begin{aligned}
& \cos x(1+\cos y) \mathrm{d} x-\sin y(1+\sin x) \mathrm{d} y=0 \\
& \Rightarrow \cos x(1+\cos y) \mathrm{d} x=\sin y(1+\sin x) \mathrm{d} y \\
& \Rightarrow \frac{\cos x}{1+\sin x} \mathrm{~d} x=\frac{\sin y}{1+\cos y} \mathrm{~d} y
\end{aligned}$
Integrating on both sides, we get
$\begin{aligned}
& \int \frac{\cos x}{1+\sin x} \mathrm{~d} x=\frac{\sin y}{1+\cos y} \mathrm{~d} y+\log |\mathrm{c}| \\
& \Rightarrow \log |1+\sin x|=-\log |1+\cos y|+\log |\mathrm{c}| \\
& \Rightarrow \log |1+\sin x|+\log |1+\cos y|=\log |\mathrm{c}| \\
& \Rightarrow \log |(1+\sin x)(1+\cos y)|=\log |\mathrm{c}| \\
& \Rightarrow(1+\sin x)(1+\cos y)=\mathrm{c}
\end{aligned}$

</details>

---

### Q74. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\sqrt{1-y^2}}{y}$ determines a family of circles with

**Options:**

- **(A)** variable radii and fixed centre at $(0,1)$.
- **(B)** variable radii and fixed centre at $(0,-1)$.
- **(C)** fixed radius of 1 unit and variable centre along the $\mathrm{Y}$-axis.
- **(D)** fixed radius of 1 unit and variable centre along the $\mathrm{X}$-axis.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) fixed radius of 1 unit and variable centre along the $\mathrm{X}$-axis.**

**Detailed Solution:**

$\begin{array}{ll} & \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{\sqrt{1-y^2}}{y} \\ \therefore \quad & \int \frac{y}{\sqrt{1-y^2}} \mathrm{~d} y=\int 1 \mathrm{~d} x \\ \therefore \quad & -\sqrt{1-y^2}=x+\mathrm{c} \\ \therefore \quad & (x+\mathrm{c})^2=1-y^2\end{array}$
$\therefore \quad(x+\mathrm{c})^2+y^2=1$
$\therefore \quad$ Radius is fixed, which is 1 and the centre is $(-c, 0)$ which is a variable centre on the $\mathrm{X}$-axis.

</details>

---

### Q75. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $\log \left(\frac{d y}{d x}\right)=a x+b y$ is

**Options:**

- **(A)** $a e^{b y}+b e^{a x}=c_1$, where $c_1$ is a constant.
- **(B)** $a e^{-b y}+b^{-a x}=c_1$, where $c_1$ is a constant.
- **(C)** $a e^{-b y}+b e^{a x}=c_1$, where $c_1$ is a constant.
- **(D)** $a e^{b y}+b e^{-a x}=c_1$, where $c_1$ is a constant.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a e^{-b y}+b e^{a x}=c_1$, where $c_1$ is a constant.**

**Detailed Solution:**

Given differential equation is
$\begin{array}{ll} 
& \log \left(\frac{d y}{d x}\right)=a x+b y \\
\therefore \quad & \frac{d y}{d x}=e^{a x+b y} \\
\therefore \quad & \frac{d y}{d x}=e^{a x} \cdot e^{b y}
\end{array}$
$\begin{aligned} & \therefore \quad \frac{\mathrm{d} y}{\mathrm{e}^{\mathrm{by}}}=\mathrm{e}^{\mathrm{ax}} \cdot \mathrm{d} x \\ & \mathrm{e}^{-\mathrm{by}} \mathrm{d} y-\mathrm{e}^{\mathrm{ax}} \mathrm{d} x=0 \\ & \text { Integrating both sides, we get } \\ & \int \mathrm{e}^{-\mathrm{by}} \mathrm{d} y-\int \mathrm{e}^{\mathrm{ax}} \mathrm{d} x=0 \\ & \frac{e^{-b y}}{-b}-\frac{e^{a x}}{a}+c=0 \\ & \text { i.e., } \frac{e^{-b y}}{b}+\frac{e^{x x}}{a}=c \\ & a e^{-b y}+b e^{a x}=a b c \\ & a e^{-b y}+b e^{a x}=c_1 \text {, where } c_1=a b c \\ & \end{aligned}$

</details>

---

### Q76. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{f}^{\prime}(x)=x-\frac{5}{x^5}$ and $\mathrm{f}(1)=4$, then $\mathrm{f}(x)$ is

**Options:**

- **(A)** $\frac{x^2}{2}+\frac{9}{4} \frac{1}{x^4}+\frac{5}{4}$
- **(B)** $\frac{x^2}{2}-\frac{5}{4} \frac{1}{x^4}+\frac{9}{4}$
- **(C)** $\frac{x^2}{2}+\frac{5}{4} \frac{1}{x^4}+\frac{9}{4}$
- **(D)** $\frac{x^2}{2}-\frac{9}{4} \frac{1}{x^4}+\frac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{x^2}{2}+\frac{5}{4} \frac{1}{x^4}+\frac{9}{4}$**

**Detailed Solution:**

Given $\mathrm{f}^{\prime}(x)=x-\frac{5}{x^5}$
$\therefore \quad$ Integrating both sides, we get
$\begin{array}{ll} 
& \mathrm{f}(x)=\int\left(x-\frac{5}{x^5}\right) \mathrm{d} x \\
& \mathrm{f}(x)=\frac{x^2}{2}+\frac{5}{4} \times \frac{1}{x^4}+\mathrm{c} \\
\therefore \quad & \text { But } \mathrm{f}(1)=4 \\
\therefore \quad & \frac{1}{2}+\frac{5}{4}+\mathrm{c}=4 \\
\therefore \quad & \mathrm{c}=\frac{9}{4} \\
\therefore \quad & \mathrm{f}(x)=\frac{x^2}{2}+\frac{5}{4} \frac{1}{x^4}+\frac{9}{4}
\end{array}$

</details>

---

### Q77. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\left(1+y^2\right) \mathrm{d} x-x y \mathrm{~d} y=0$ at $x=1, y=0$, represents

**Options:**

- **(A)** circle
- **(B)** pair of straight lines
- **(C)** hyperbola
- **(D)** ellipse

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) hyperbola**

**Detailed Solution:**

$\begin{array}{ll} 
& \left(1+y^2\right) \mathrm{d} x-x y \mathrm{~d} y=0 \\
\therefore \quad & \left(1+y^2\right) \mathrm{d} x=x y \mathrm{~d} y \\
\therefore \quad & \frac{1}{x} \mathrm{~d} x=\frac{y \mathrm{~d} y}{1+y^2}
\end{array}$
Integrating both sides, we get
$\begin{aligned}
& \int \frac{1}{x} \mathrm{~d} x=\int \frac{y}{1+y^2} \mathrm{~d} y \\
& \log x=\frac{1}{2} \log \left(1+y^2\right)+\mathrm{c}
\end{aligned}$
$\text { At } x=1, y=0...[Given]$
$\begin{array}{ll}
\therefore & 0=\frac{1}{2} \log (1+0)+\mathrm{c} \\
\therefore & \quad \mathrm{c}=0 \\
\therefore & \log x=\frac{1}{2} \log \left(1+y^2\right) \\
\therefore & x^2=1+y^2 \\
\therefore & x^2-y^2=1,
\end{array}$
Which is a rectangular hyperbola.

</details>

---

### Q78. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $(1+x) y \mathrm{~d} x+(1-y) x \mathrm{~d} y=0$ is

**Options:**

- **(A)** $\log x y-x+y=C$
- **(B)** $\log \left(\frac{x}{y}\right)-x+y=C$
- **(C)** $\log x y-x-y=C$
- **(D)** $\log (x y)+x-y=C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log (x y)+x-y=C$**

**Detailed Solution:**

$\begin{aligned} & (1+x) y \mathrm{~d} x+(1-y) x \mathrm{~d} y=0 \\ & \Rightarrow \int \frac{1+x}{x} \mathrm{~d} x=\int \frac{y-1}{y} \mathrm{~d} y \\ & \Rightarrow \log |x|+x=y-\log |y|+C \\ & \Rightarrow \log (x y)+x-y=C\end{aligned}$

</details>

---

### Q79. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of $\frac{y}{x} \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+y^2}{1+x^2}$ when $x=2, y=1$ is

**Options:**

- **(A)** $\left(1+y^2\right)=2\left(1+x^2\right)$
- **(B)** $2\left(1+y^2\right)=5\left(1+x^2\right)$
- **(C)** $2\left(1+y^2\right)=\left(1+x^2\right)$
- **(D)** $5\left(1+y^2\right)=2\left(1+x^2\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5\left(1+y^2\right)=2\left(1+x^2\right)$**

**Detailed Solution:**

$\begin{aligned} & \frac{y}{x} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1+y^2}{1+x^2} \\ & \Rightarrow \frac{y}{1+y^2} \mathrm{~d} y=\frac{x}{1+x^2} \mathrm{~d} x \\ & \Rightarrow \frac{1}{2} \int \frac{2 y \mathrm{~d} y}{1+y^2}=\frac{1}{2} \int \frac{2 x}{1+x^2} \mathrm{~d} x \\ & \Rightarrow \frac{1}{2} \log \left|1+y^2\right|=\frac{1}{2} \log \left|1+x^2\right|+\frac{1}{2} \log c \\ & \Rightarrow \log \frac{1+y^2}{1+x^2}=\log c \\ & \Rightarrow \frac{1+y^2}{1+x^2}=C\end{aligned}$
Putting $x=2, y=1$ we get $C=\frac{2}{5}$
$$
\begin{aligned}
& \Rightarrow \frac{1+y^2}{1+x^2}=\frac{2}{5} \\
& \Rightarrow 5\left(1+y^2\right)=2\left(1+x^2\right)
\end{aligned}
$$

</details>

---

### Q80. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $x \cos y \mathrm{~d} y=\left(x \mathrm{e}^x \log x+\mathrm{e}^x\right) \mathrm{d} x$ is (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\sin y=\mathrm{e}^x \log x+C$
- **(B)** $\sin y=\mathrm{e}^x+C \log x$
- **(C)** $\sin y=C \mathrm{e}^x+\log x$
- **(D)** $\mathrm{e}^x \sin y=\log x+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin y=\mathrm{e}^x \log x+C$**

**Detailed Solution:**

$\begin{aligned} & x \cos y \mathrm{~d} y=\left(x \mathrm{e}^x \log x+\mathrm{e}^x\right) \mathrm{d} x \\ & \Rightarrow \int \cos y \mathrm{~d} y=\int \mathrm{e}^x\left\{\log x+\frac{1}{x}\right\} \mathrm{d} x \\ & \Rightarrow \sin y=\mathrm{e}^x \log x+C\left[\because \int \mathrm{e}^x\left\{f(x)+f^{\prime}(x)\right\} \mathrm{d} x=\mathrm{e}^x f(x)+C\right]\end{aligned}$

</details>

---

### Q81. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\mathrm{e}^{\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)}=x+1 ; y(0)=5$, $x \in(-1, \infty)$

**Options:**

- **(A)** $(x-1) \log (x+1)-x-5=y$
- **(B)** $(x+1) \log (x+1)+x+5=y$
- **(C)** $(x-1) \log (x+1)+x-5=y$
- **(D)** $(x+1) \log (x+1)-x+5=y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(x+1) \log (x+1)-x+5=y$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{e}^{\frac{\mathrm{d} y}{\mathrm{~d} x}}=x+1 \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\log _{\mathrm{e}}(x+1) \\ & \Rightarrow \int \mathrm{d} y=\int \log _{\mathrm{e}}(x+1) \mathrm{d} x \\ & \Rightarrow y=(x+1) \log _{\mathrm{e}}(x+1)-(x+1)+C \text { [integrating by parts] } \\ & \text { putting } x=0 \text { and } y=5 \text { we get } C=6 \\ & \Rightarrow y=(x+1) \log _{\mathrm{e}}(x+1)-x+5\end{aligned}$

</details>

---

### Q82. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=1-x+y-x y$ is (where $C$ is a constant of integration)

**Options:**

- **(A)** $\log (1+y)=x+\frac{x^2}{2}+C$
- **(B)** $\log (1-x)=\log (1+y)+y+C$
- **(C)** $\log (1+y)=y-\frac{x^2}{2}+C$
- **(D)** $\log (1+y)=x-\frac{x^2}{2}+C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log (1+y)=x-\frac{x^2}{2}+C$**

**Detailed Solution:**

$\begin{aligned} & \frac{\mathrm{d} y}{\mathrm{~d} x}=1-x+y-x y=(1-x)(1+y) \\ & \Rightarrow \int \frac{\mathrm{d} y}{1+y}=\int(1-x) \mathrm{d} x \\ & \Rightarrow \log (1+y)=x-\frac{x^2}{2}+C\end{aligned}$

</details>

---

### Q83. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation $x^2(y+1) d x+y^2(x-1) d y=0$ has the general solution given by (where $C$ is a constant of integration.)

**Options:**

- **(A)** $(x-1)^2+(y-1)^2+2 \log [(x+1)(y+1)]=C$
- **(B)** $(x-1)^2+(y+1)^2+2 \log [(x+1)(y-1)]=C$
- **(C)** $(x+1)^2+(y+1)^2+2 \log [(x-1)(y+1)]=C$
- **(D)** $(x+1)^2+(y-1)^2+2 \log [(x-1)(y+1)]=C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(x+1)^2+(y-1)^2+2 \log [(x-1)(y+1)]=C$**

**Detailed Solution:**

$\begin{aligned} & x^2(y+1) d x+y^2(x-1) d y=0 \\ & \Rightarrow \int \frac{x^2}{1-x} d x=\int \frac{y^2}{y-1} d y \\ & \Rightarrow \int\left(-x-1+\frac{1}{1+x}\right) d x=\int\left(y-1+\frac{1}{y+1}\right) d y \\ & \Rightarrow-\frac{x^2}{2}-x-\log \left|1-x+C^1=\frac{y^2}{2}-y+\log \right| y+1 \mid \\ & \Rightarrow C^1=+x+-y+\log |1-x|+\log |y+1| \\ & \Rightarrow 2 C^1=x^2+2 x+y^2-2 y+2 \log |(1-x)(y+1)| \\ & \Rightarrow 2 C^1+2=(x+1)^2+(y-1)^2+2 \log |(1-x)(y+1)|\end{aligned}$
$\Rightarrow(x+1)^2+(y-1)^2+2 \log |(x-1)(y+1)|=C$

</details>

---

### Q84. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of $\frac{d y}{d x}=1+x+y^2+x y^2$, when $y(0)=0$. is

**Options:**

- **(A)** $y=\log \left(1+\frac{x^2}{2}\right)$
- **(B)** $y^3=\log \left(1+\frac{x^2}{2}\right)$
- **(C)** $y^2=\tan \left(1+\frac{x^2}{2}\right)$
- **(D)** $y=\tan \left(x+\frac{x^2}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=\tan \left(x+\frac{x^2}{2}\right)$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=1+x+y^2+x y^2=(1+x)\left(1+y^2\right) \\ & \Rightarrow \int \frac{d y}{1+y^2}=\int(1+x) d x \\ & \Rightarrow \tan ^{-1} y=x+\frac{x^2}{2}+c \\ & \because y(0)=0 \Rightarrow c=0 \\ & \Rightarrow \tan ^{-1} y=x+\frac{x^2}{2} \\ & \Rightarrow y=\tan \left(x+\frac{x^2}{2}\right)\end{aligned}$

</details>

---

### Q85. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of $\log \left(\frac{d y}{d x}\right)=3 x+4 y$ at $x=y=0$ is

**Options:**

- **(A)** $3 e^{-4 y}-4 e^{3 x}=7$
- **(B)** $3 e^{-4 y}+4 e^{3 x}=7$
- **(C)** $4 e^{-4 y}-3 e^{3 x}=7$
- **(D)** $4 e^{-4 y}+3 e^{3 x}=7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 e^{-4 y}+4 e^{3 x}=7$**

**Detailed Solution:**

$\begin{aligned} & \log \left(\frac{d y}{d x}\right)=3 x+4 y \text { and } x=y=0 \\ & \Rightarrow \frac{d y}{d x}=e^{3 x+4 y} \\ & \Rightarrow \int e^{-4 y} d y=\int e^{3 x} d x \\ & \Rightarrow \frac{e^{-4 y}}{-4}=\frac{e^{3 x}}{3}+C\end{aligned}$
Putting $x=0$ and $y=0$ we get $C=\frac{-7}{12}$
$\begin{aligned} & \frac{e^{-4 y}}{-4}=\frac{e^{3 x}}{3}-\frac{7}{12} \\ & \Rightarrow 3 e^{-4 y}=-4 e^{3 x}+7 \\ & \Rightarrow 3 e^{-4 y}+4 e^{3 x}=7\end{aligned}$

</details>

---

### Q86. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\left(1+e^{-x}\right)\left(1+y^2\right) \frac{d y}{d x}=y^2$ which passes through the point $(0,1)$ is

**Options:**

- **(A)** $y^2+1=y\left(\log \left(\frac{1+e^x}{2}\right)+2\right)$
- **(B)** $y^2+1=y\left(\log \left(\left(\frac{1+e^{-x}}{2}\right)+2\right)\right)$
- **(C)** $y^2=1+y \log \left(\frac{1+e^{-x}}{2}\right)$
- **(D)** $y^2=1+y \log \left(\frac{1+e^x}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y^2=1+y \log \left(\frac{1+e^x}{2}\right)$**

**Detailed Solution:**

$\begin{aligned} & \left(1+e^{-x}\right)\left(1+y^2\right) \frac{d y}{d x}=y^2 \\ & \Rightarrow \int \frac{1+y^2}{y^2} d y=\int \frac{e^x}{1+e^x} d x \\ & \Rightarrow-\frac{1}{y}+y=\log \left(1+e^x\right)+\log C \\ & \Rightarrow-1+y^2=y \log c\left(1+e^x\right)\end{aligned}$
Putting $x=0$ and $y=1$ we get $c=\frac{1}{2}$
$\begin{aligned} & \Rightarrow-1+y^2=y \log \left(\frac{1+e^x}{2}\right) \\ & \Rightarrow y^2=1+y \log \left(\frac{1+e^x}{2}\right)\end{aligned}$

</details>

---

### Q87. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of differential equation $\frac{d y}{d x}=e^{x+y}+x^2 e^{x^3+y}$ is (where $\mathrm{C}$ is a constant of integration.)

**Options:**

- **(A)** $\mathrm{e}^{\mathrm{x}}+\mathrm{e}^{-\mathrm{y}}+\frac{1}{3} \mathrm{e}^{\mathrm{x}^3}=\mathrm{C}$
- **(B)** $e^x-e^{-y}-\frac{1}{3} e^{x^3}=C$
- **(C)** $e^x-e^{-y}+\frac{1}{3} e^{x^3}=C$
- **(D)** $e^x-e^{-y}+\frac{1}{3} e^{x^3}=C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{\mathrm{x}}+\mathrm{e}^{-\mathrm{y}}+\frac{1}{3} \mathrm{e}^{\mathrm{x}^3}=\mathrm{C}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=e^{x+y}+x^2 e^{x^3+y} \\ & \Rightarrow \frac{d y}{d x}=e^y\left(e^x+x^2 e^{x^3}\right) \\ & \Rightarrow \int e^{-y} d y=\int\left(e^x+x^2 e^{x^3}\right) d x \\ & \Rightarrow-e^{-y}+c=e^x+\frac{1}{3} e^{x^3} \\ & \Rightarrow e^x+e^{-y}+\frac{1}{3} e^{x^3}=c\end{aligned}$

</details>

---

### Q88. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation $\frac{d y}{d x}=e^{2 y} \cos x$, when $y\left(\frac{\pi}{6}\right)=0$ is

**Options:**

- **(A)** $\sin \mathrm{x}-\frac{\mathrm{e}^{2 \mathrm{y}}}{2}=0$
- **(B)** $4 \sin x-e^{-2 y}-1=0$
- **(C)** $\sin x+e^{-2 y}-2=0$
- **(D)** $2 \sin x+e^{-2 y}-2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \sin x+e^{-2 y}-2=0$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=e^{2 y} \cos x \Rightarrow \int e^{2 y} d y=\int \cos d x \\ & \Rightarrow \frac{e^{2 y}}{-2}=\sin x+c\end{aligned}$
Putting $\mathrm{x}=\frac{\pi}{6}$ and $\mathrm{y}=0$ we get $\mathrm{c}=-1$
$\begin{aligned} & \Rightarrow \frac{e^{-2 y}}{-2}=\sin x-1 \\ & \Rightarrow e^{-2 y}=-2 \sin x+2 \\ & \Rightarrow 2 \sin x+e^{-2 y}-2=0\end{aligned}$

</details>

---

### Q89. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

General solution of the differential equation $\left(y^3+y\right)\left(x^2+1\right) d y=\left(x y^4+2 y^2 x\right) d x$ is (where $C$ is a constant of integration.)

**Options:**

- **(A)** $\mathrm{y}^2\left(\mathrm{y}^2+1\right)=\mathrm{C}\left(\mathrm{x}^2+1\right)^2$
- **(B)** $\mathrm{y}^2\left(\mathrm{y}^2+2\right)=\mathrm{C}\left(\mathrm{x}^2+1\right)$
- **(C)** $\mathrm{y}^2\left(\mathrm{y}^2+2\right)=\mathrm{C}\left(\mathrm{x}^2+1\right)^2$
- **(D)** $y^2\left(y^2+1\right)=C\left(x^2+2\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{y}^2\left(\mathrm{y}^2+2\right)=\mathrm{C}\left(\mathrm{x}^2+1\right)^2$**

**Detailed Solution:**

$\begin{aligned} & \left(y^3+y\right)\left(x^2+1\right) d y=\left(x y^4+2 y^2 x\right) d x \\ & \Rightarrow \int \frac{y^3+y}{y^4+2 y^2} d y=\int \frac{x}{x^2+1} d x \\ & \Rightarrow \frac{1}{4} \log _e\left(y^4+2 y^2\right)=\frac{1}{2} \log _e\left(x^2+1\right)+\log C^1 \\ & \Rightarrow \log _e\left(y^4+2 y^2\right)=2 \log _e\left(C^1\right)^2\left(x^2+1\right) \\ & \Rightarrow y^4+2 y^2=\left(c^1\right)^4\left(x^2+1\right)^2 \\ & \Rightarrow y^2\left(y^2+2\right)=C\left(x^2+1\right)^2\end{aligned}$

</details>

---

### Q90. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

General solution of the differential equation $\sin ^3 \mathrm{x} \frac{\mathrm{dx}}{\mathrm{dy}}=\sin \mathrm{y}$ is given by

**Options:**

- **(A)** $\cos y-\frac{3}{4} \cos x-\frac{1}{12} \cos 3 x=C$
- **(B)** $\cos y-\frac{3}{4} \cos x+\frac{1}{12} \cos 3 x=C$
- **(C)** $\cos y+\frac{3}{4} \cos x-\frac{1}{12} \cos 3 x=C$
- **(D)** $\cos y+\frac{3}{4} \cos x-\frac{1}{12} \cos 3 x=C$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\cos y-\frac{3}{4} \cos x+\frac{1}{12} \cos 3 x=C$**

**Detailed Solution:**

$\begin{aligned} & \sin ^3 x \frac{d x}{d y}=\sin y \Rightarrow \int \sin ^3 x d x=\int \sin y d y \\ & \Rightarrow \int \frac{3 \sin x-\sin 3 x}{4} d x=\int \sin y d y \\ & \Rightarrow \frac{-3}{4} \cos x+\frac{1}{4} \cdot \frac{\cos 3 x}{3}=-\cos y+C \\ & \Rightarrow \cos y-\frac{3}{4} \cos x+\frac{1}{12} \cos 3 x=C\end{aligned}$

</details>

---

### Q91. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=y(x)$ and $\frac{2+\sin x}{y+1}\left(\frac{d y}{d x}\right)=-\cos x, y(0)=1$, then $y\left(\frac{\pi}{2}\right)$ is equal to

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{3}$
- **(C)** $-\frac{1}{3}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & \frac{2+\sin x}{y+1} \frac{d y}{d x}=-\cos x \\ & \Rightarrow \int \frac{d y}{y+1}=\int \frac{-\cos x d x}{2+\sin x} \\ & \Rightarrow \log _{\mathrm{e}}|y+1|=-\log _{\mathrm{e}}|2+\sin x|+\log _{\mathrm{e}} C \\ & \Rightarrow \log _e|y+1|+\log _e|2+\sin x|=\log _e C \\ & \Rightarrow \log _e|(y+1)(2+\sin x)|=\log _e C \\ & \Rightarrow(y+1)(2+\sin x)=C \\ & \text { Putting } x=0 \text { and } y=1 \text { we get } c=4 \\ & \Rightarrow(y+1)(2+\sin x)=4 \\ & \end{aligned}$
Now putting $x=\frac{\pi}{2}$ we get $y=\frac{1}{3}$

</details>

---

### Q92. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\left(1+e^{2 x}\right) d y+e^x\left(1+y^2\right) d x=0$ at $x=0$ and $y=1$ is

**Options:**

- **(A)** $\tan ^{-1} \mathrm{e}^{\mathrm{x}}-\tan ^{-1} \mathrm{y}=0$
- **(B)** $\tan ^{-1} \mathrm{e}^{\mathrm{x}}+\tan ^{-1} \mathrm{y}=\frac{\pi}{2}$
- **(C)** $\tan ^{-1} \mathrm{e}^{\mathrm{x}}+\tan ^{-1} \mathrm{y}=\frac{3 \pi}{4}$
- **(D)** $\tan ^{-1} e^x-\tan ^{-1} y=\frac{3 \pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan ^{-1} \mathrm{e}^{\mathrm{x}}+\tan ^{-1} \mathrm{y}=\frac{\pi}{2}$**

**Detailed Solution:**

$\begin{aligned}
& \left(1+\mathrm{e}^{2 \mathrm{x}}\right) \mathrm{dy}+\mathrm{e}^{\mathrm{x}}\left(1+\mathrm{y}^2\right) \mathrm{dx}=0 \\
& \therefore \frac{\mathrm{dy}}{1+\mathrm{y}^2}+\frac{\mathrm{e}^{\mathrm{x}}}{\left(1+\mathrm{e}^{2 \mathrm{x}}\right)} \mathrm{dx}=0 \\
& \therefore \int \frac{\mathrm{dy}}{1+\mathrm{y}^2}=-\int \frac{\mathrm{e}^{\mathrm{x}}}{1+\mathrm{e}^{2 \mathrm{x}}} d \mathrm{x}
\end{aligned}$
Put $\mathrm{e}^{\mathrm{x}}=\mathrm{t} \Rightarrow \mathrm{e}^{\mathrm{x}} \mathrm{dx}=\mathrm{dt}$
$\therefore \int \frac{\mathrm{dy}}{1+\mathrm{y}^2}=-\int \frac{\mathrm{dt}}{1+\mathrm{t}^2} \Rightarrow \tan ^{-1}(\mathrm{y})=-\tan ^{-1}(\mathrm{t})+\mathrm{c}$
$\therefore \tan ^{-1}(\mathrm{y})+\tan ^{-1}\left(\mathrm{e}^{\mathrm{x}}\right)=\mathrm{c}$
We have $\mathrm{x}=0, \mathrm{y}=1$
$\therefore \tan ^{-1}(1)+\tan ^{-1}\left(\mathrm{e}^{\circ}\right)=\mathrm{c} \Rightarrow \mathrm{c}=2 \tan ^{-1}(1)=\frac{\pi}{2}$
$\therefore \tan ^{-1} \mathrm{y}+\tan ^{-1} \mathrm{e}^{\mathrm{x}}=\frac{\pi}{2}$

</details>

---

### Q93. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{\mathrm{dy}}{\mathrm{dx}}=\tan \left(\frac{\mathrm{y}}{\mathrm{x}}\right)+\frac{\mathrm{y}}{\mathrm{x}}$ is

**Options:**

- **(A)** $\sin \left(\frac{y}{x}\right)=c y$
- **(B)** $\cos \left(\frac{y}{x}\right)=c y$
- **(C)** $\cos \left(\frac{y}{x}\right)=c x$
- **(D)** $\sin \left(\frac{y}{x}\right)=c x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sin \left(\frac{y}{x}\right)=c x$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\tan \left(\frac{y}{x}\right)+\frac{y}{x} \\ & \text { Put } \frac{y}{x}=v \Rightarrow y=x v \Rightarrow \frac{d y}{d x}=x \frac{d v}{d x}+v \\ & \therefore \quad v+x \frac{d v}{d x}=\tan v+v \Rightarrow x \frac{d v}{d x}=\tan v \\ & \therefore \quad \int \frac{d v}{\tan v}=\int \frac{d x}{x} \\ & \therefore \quad \log |\sin v|=\log |x|+\log |c| \Rightarrow \sin v=x c \\ & \therefore \quad \sin \left(\frac{y}{x}\right)=x c\end{aligned}$

</details>

---

### Q94. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $y(1+\log x) \frac{d x}{d y}-x \log x=0$ when $x=e, y=e^2$ is

**Options:**

- **(A)** $y^2=e^4 \log x$
- **(B)** $y=e^2 \log x$
- **(C)** $y=x^2 \log x$
- **(D)** $y=e x \log x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=e x \log x$**

**Detailed Solution:**

$\begin{aligned} & y(1+\log x) \frac{d y}{d x}-x \log x=0 \\ & \therefore y(1+\log x) \frac{d y}{d x}=x \log x \Rightarrow \frac{d y}{d x}=\frac{y(1+\log x)}{x \log x} \\ & \therefore \int \frac{d y}{d x}=\int \frac{1+\log x}{x \log x} d x \\ & \therefore \log |y|+\log |x \log x|+\log c \\ & \text { We have } x=e, y=e^2 \\ & \therefore \log |e|^2=\log |e \log e|+\log c \\ & 2=1+\log c \Rightarrow \log c=1=\log e \\ & \therefore \log |y|=\log |x \log x|+\log e \\ & y=e x \log x\end{aligned}$

</details>

---

### Q95. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation $\cos (x+y) \frac{d y}{d x}=1$ is

**Options:**

- **(A)** $y=\tan (x+y)+c$
- **(B)** $y=\sec (x+y)+c$
- **(C)** $y=\tan \left(\frac{x+y}{2}\right)+c$
- **(D)** $y=\cot \left(\frac{x+y}{2}\right)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y=\tan \left(\frac{x+y}{2}\right)+c$**

**Detailed Solution:**

$$
\cos (x+y) \frac{d y}{d x}=1
$$
Put $x+y=V \Rightarrow 1+\frac{d y}{d x}=\frac{d V}{d x}$
$$
\begin{aligned}
& \therefore \cos \mathrm{V}\left(\frac{\mathrm{dV}}{\mathrm{dx}}-1\right)=1 \Rightarrow \cos \mathrm{V}\left(\frac{\mathrm{dV}}{\mathrm{dx}}\right)=1+\cos \mathrm{V} \\
& \therefore \int \frac{\cos \mathrm{V}}{1+\cos \mathrm{V}} \mathrm{dV}=\int \mathrm{dx} \\
& \therefore \int\left[\frac{1+\cos \mathrm{V}}{1+\cos \mathrm{V}}-\frac{1}{1+\cos \mathrm{V}}\right] \mathrm{dV} \\
& =\int \mathrm{dx} \Rightarrow \int \mathrm{dV}-\frac{1}{2} \int \sec ^2 \frac{\mathrm{V}}{2} \mathrm{dV}=\int \mathrm{dx}
\end{aligned}
$$
$$
\begin{aligned}
& \therefore \mathrm{V}-\frac{1}{2} \frac{\tan \left(\frac{\mathrm{V}}{2}\right)}{\left(\frac{1}{2}\right)}=\mathrm{x}+\mathrm{c} \Rightarrow \mathrm{V}-\tan \left(\frac{\mathrm{V}}{2}\right)=\mathrm{x}+\mathrm{c} \\
& \Rightarrow \mathrm{x}+\mathrm{y}-\tan \left(\frac{\mathrm{x}+\mathrm{y}}{2}\right)=\mathrm{x}+\mathrm{c} \\
& \mathrm{y}=\tan \left(\frac{\mathrm{x}+\mathrm{y}}{2}\right)+\mathrm{c}
\end{aligned}
$$

</details>

---

### Q96. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The particular solution of differential equation $(\mathrm{x}+\mathrm{y}) \mathrm{dy}+(\mathrm{x}-\mathrm{y}) \mathrm{d} \mathrm{x}=0$ at $\mathrm{x}=\mathrm{y}=1$ is

**Options:**

- **(A)** $\log \left|\frac{\mathrm{x}^2+\mathrm{y}^2}{2}\right|=\frac{\pi}{2}-2 \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)$
- **(B)** $\log \left|\mathrm{x}^2+\mathrm{y}^2\right|=\frac{\pi}{2}-2 \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)$
- **(C)** $\log \left|\frac{\mathrm{x}^2+\mathrm{y}^2}{2}\right|=\frac{\pi}{4}-\tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)$
- **(D)** $\log \left|\mathrm{x}^2+\mathrm{y}^2\right|=\frac{\pi}{4}-2 \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log \left|\frac{\mathrm{x}^2+\mathrm{y}^2}{2}\right|=\frac{\pi}{2}-2 \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)$**

**Detailed Solution:**

$$
(x+y) d y+(x-y) d x=0
$$
We have $\frac{d y}{d x}=-\frac{(x-y)}{x+y}$
Put $y=v x \Rightarrow \frac{d y}{d x}=v+x \frac{d v}{d x}$
$$
\therefore v+x \frac{d v}{d x}=\frac{-(x-v x)}{x+v x}=\frac{-x(1-v)}{x(1+v)}=\frac{-(1-v)}{1+v}
$$
$\therefore x \frac{d v}{d x}=\frac{-1+v}{1+v}-v=\frac{-1+v-v-v^2}{1+v} \Rightarrow x \frac{d v}{d x}=\frac{-\left(1+v^2\right)}{1+v}$
$$
\therefore \int \frac{(1+v)}{1+v^2} d v=-\int \frac{d x}{x} \Rightarrow \int \frac{d v}{1+v^2}+\frac{1}{2} \int \frac{2 v}{1+v^2} d v=-\int \frac{d x}{x}
$$
$$
\begin{aligned}
& \therefore \tan ^{-1}(\mathrm{v})+\frac{1}{2} \log \left|1+\mathrm{v}^2\right|=-\log \mathrm{x}+\log \mathrm{c}_1 \\
& \quad \Rightarrow \tan ^{-1}\left(\frac{\mathrm{y}}{\mathrm{x}}\right)+\frac{1}{2} \log \left|1+\frac{\mathrm{y}^2}{\mathrm{x}^2}\right|=-\log \mathrm{x}+\log \mathrm{c}_1
\end{aligned}
$$
$$
2 \tan ^{-1}\left(\frac{y}{x}\right)+\log \left|\frac{x^2+y^2}{x^2}\right|+2 \log x=\log c \ldots\left[\because \log c=2 \log c_1\right]
$$
$$
\therefore 2 \tan ^{-1}\left(\frac{y}{x}\right)+\log \left|\frac{x^2+y^2}{x^2} \times x^2\right|=\log c
$$

</details>

---

### Q97. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation $\frac{d y}{d x}+\frac{y^2+y+1}{x^2+x+1}=0$ is

**Options:**

- **(A)** $x+y+1=c(1+x+y+2 x y)$
- **(B)** $x+y+1=c(2+x+y+2 x y)$
- **(C)** $x+y+1=c(1-x-y-2 x y$
- **(D)** $x+y+2=c(2-x-y-2 x y)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x+y+1=c(1-x-y-2 x y$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}+\frac{y^2+y+1}{x^2+x+1}=0 \\ & \therefore \frac{d y}{d x}=-\left(\frac{y^2+y+1}{x^2+x-1}\right) \\ & \therefore \int \frac{d y}{y^2+y+1}=-\int \frac{d x}{x^2+x+1} \\ & \Rightarrow \int \frac{d y}{y^2+y+\frac{1}{4}+\frac{3}{4}}=-\int \frac{d x}{x^2+x+\frac{1}{4}+\frac{3}{4}} \\ & \int \frac{d y}{\left(y+\frac{1}{2}\right)^2+\left(\frac{\sqrt{3}}{2}\right)^2}=-\int \frac{d x}{\left(x+\frac{1}{2}\right)^2+\left(\frac{\sqrt{3}}{2}\right)^2} \\ & \Rightarrow \frac{1}{\left(\frac{\sqrt{3}}{2}\right)^2} \tan ^{-1}\left[\frac{y+\frac{1}{2}}{\left(\frac{\sqrt{3}}{2}\right)}\right]=\frac{-1}{\left(\frac{\sqrt{3}}{2}\right)^{-1} \tan ^{-1}}\left[\frac{x+\frac{1}{2}}{\left(\frac{\sqrt{3}}{2}\right)}\right]+C_1\end{aligned}$
$\begin{aligned} & \therefore \frac{2}{\sqrt{3}} \tan ^{-1}\left(\frac{2 \mathrm{y}+1}{\sqrt{3}}\right)=\frac{-2}{\sqrt{3}} \tan ^{-1}\left(\frac{2 \mathrm{x}+1}{\sqrt{3}}\right)+\mathrm{C}_1 \\ & \therefore \frac{2}{\sqrt{3}} \tan ^{-1}\left[\frac{\frac{(2 \mathrm{y}+1)}{\sqrt{3}}+\left(\frac{2 \mathrm{x}+1}{\sqrt{3}}\right)}{1-\left(\frac{2 \mathrm{y}+1}{\sqrt{3}}\right)\left(\frac{2 \mathrm{x}+1}{\sqrt{3}}\right)}\right]=\mathrm{C}_1 \\ & \Rightarrow \frac{2}{\sqrt{3}} \tan ^{-1}\left[\frac{\frac{2(x+y+1)}{\sqrt{3}}}{\frac{3-(4 x y+2 x+2 y+1)}{3}}\right]=C_1 \\ & \therefore \frac{2}{\sqrt{3}} \tan ^{-1}\left[\frac{2(x+y+1)}{\sqrt{3}} \times \frac{3}{2(1-2 x y-x-y)}\right]=C_1 \\ & \end{aligned}$
$\begin{aligned} & \therefore \frac{2}{\sqrt{3}} \tan ^{-1}\left[\frac{\sqrt{3}(x+y+1)}{1-2 x y-x-y}\right]=C_1 \\ & \Rightarrow \tan ^{-1}\left[\frac{\sqrt{3}(x+y+1)}{1-x-y-2 x y}\right]=C_2 \\ & \ldots\left[\text { where } \mathrm{C}_2=\frac{\sqrt{3} \mathrm{C}_1}{2}\right] \\ & \therefore \frac{\sqrt{3}(x+y+1)}{1-x-y-2 x y}=\tan C_2 \Rightarrow \frac{x+y+1}{1-x-y-2 x y}=\frac{\tan C_2}{\sqrt{3}}=c \\ & \text {... (say) } \\ & \therefore \mathrm{x}+\mathrm{y}+1=\mathrm{c}(1-\mathrm{x}-\mathrm{y}-2 \mathrm{xy}) \\ & \end{aligned}$

</details>

---

### Q98. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation $\frac{d x}{d t}=\frac{x \log x}{t}$ is

**Options:**

- **(A)** lot $x-x=c$
- **(B)** $\mathrm{e}^{\mathrm{ct}}+\mathrm{x}=0$
- **(C)** $\log \mathrm{t}=\mathrm{x}+\mathrm{c}$
- **(D)** $\mathrm{e}^{\mathrm{ct}}=\mathrm{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{e}^{\mathrm{ct}}=\mathrm{x}$**

**Detailed Solution:**

$\begin{aligned} & \frac{d x}{d t}=\frac{x \log x}{t} \\ & \therefore \int \frac{d x}{x \log x}=\int \frac{d t}{t} \\ & \therefore \log |\log x|=\log |t|+\log c \\ & \therefore \log x=t c \Rightarrow x=e^{t c}\end{aligned}$

</details>

---

### Q99. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{d y}{d x}=2^{y-x}$ is

**Options:**

- **(A)** $2^x-2^y=c$
- **(B)** $\frac{1}{2^x}-\frac{1}{2^y}=c$
- **(C)** $\frac{1}{2^x}+\frac{1}{2^y}=c$
- **(D)** $2^x+2^y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2^x}-\frac{1}{2^y}=c$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=2^{y-x} \\ & \therefore \frac{d y}{d x}=\frac{2^y}{2^x} \Rightarrow \int \frac{d y}{2^y}=\int \frac{d x}{2^x} \\ & \therefore \int 2^{-y} d y=\int 2^{-x} d x \Rightarrow \frac{2^{-y}}{-\ell n 2}=\frac{2^{-x}}{-\ln 2}+c_1 \Rightarrow \frac{2^{-y}}{\ln 2}=\frac{2^{-x}}{\ln 2}-c_1 \\ & \therefore \frac{1}{\ln 2}\left[2^{-x}-2^{-y}\right]=c_1 \\ & \therefore \frac{1}{2^x}-\frac{1}{2^y}=c, \text { where } c=\left(c_1\right)(\ln 2)\end{aligned}$

</details>

---

### Q100. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $(2 y-1) d x-(2 x+3) d y=0$ is

**Options:**

- **(A)** $(2 x+3)^2=c(2 y-1)$
- **(B)** $\frac{2 x+3}{2 y-1}=c$
- **(C)** $(2 x+3)(2 y-1)=c$
- **(D)** $(2 x+3)(2 y-1)^2=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 x+3}{2 y-1}=c$**

**Detailed Solution:**

$\begin{aligned} & (2 y-1) d x-(2 x+3) d y=0 \Rightarrow \frac{d y}{d x}=\frac{(2 y-1)}{(2 x+3)} \\ & \therefore \int \frac{d y}{2 y-1}=\int \frac{d x}{2 x+3} \\ & \frac{\log |2 y-1|}{2}=\frac{\log |2 x+3|}{2}+\log c_1 \Rightarrow \log \left|\frac{2 x+3}{2 y-1}\right|=-\log c_1=\log c \\ & \therefore \frac{2 x+3}{2 y-1}=c\end{aligned}$

</details>

---

### Q101. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $\frac{d y}{d x}=\frac{y+1}{x^2-x}$, when $\mathrm{x}=2$ and $\mathrm{y}=1$ is

**Options:**

- **(A)** $x y=4 x-6$
- **(B)** xy $=2 x-2$
- **(C)** $x y=x-2$
- **(D)** $x y=-x+4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x y=x-2$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}=\frac{y+1}{x^2-x} \\ & \therefore \int \frac{d y}{y+1}=\int \frac{d x}{x(x-1)} \\ & \therefore \int \frac{d y}{y+1}=\int\left[\frac{1}{x-1}-\frac{1}{x}\right] d x \Rightarrow \log |y+1|=\log |x-1|-\log |x|+ \\ & \log c \\ & \text { We have } x=2 \text { and } y=1 \\ & \therefore \log |2|=\log |1|-\log |1|+\log c \Rightarrow c=2 \\ & \therefore \log |y+1|=\log |x-1|-\log |x|+\log |2| \\ & \log |y+1|=\log \left|\frac{2(x-1)}{x}\right| \\ & \therefore y+1=\frac{2(x-1)}{x} \Rightarrow x y+x=2 x-2 \Rightarrow x y=x-2\end{aligned}$

</details>

---

### Q102. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of $\sin ^{-1}\left(\frac{d y}{d x}\right)=x+y$ is

**Options:**

- **(A)** $\tan (x+y)-\sec (x+y)=x^2+c$
- **(B)** $\tan (x+y)+\sec (x+y)=x^2+c$
- **(C)** $\tan (x+y)+\sec (x+y)=x+c$
- **(D)** $\tan (x+y)-\sec (x+y)=x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\tan (x+y)-\sec (x+y)=x+c$**

**Detailed Solution:**

$\begin{aligned} & \sin ^{-1}\left(\frac{d y}{d x}\right)=x+y \\ & \therefore \frac{d y}{d x}=\sin (x+y) \\ & \text { Put } x+y=t \quad \Rightarrow 1+\frac{d y}{d x}=\frac{d t}{d x} \\ & \therefore \frac{d t}{d x}-1=\sin t \Rightarrow \frac{d t}{d x}=1+\sin t \\ & \therefore \int \frac{d t}{1+\sin t}=\int d x \\ & \therefore \int \frac{(1-\sin t) d t}{1-\sin } t=\int d x \Rightarrow \int \frac{1-\sin t}{\cos ^2 t} d t=\int d x \\ & \Rightarrow \int\left(\sec ^2 t-\operatorname{sect} \tan t\right) d t=\int d x \\ & \therefore \tan t-\sec t=x+c \\ & \therefore \tan (x+y)-\sec (x+y)=x+c\end{aligned}$

</details>

---

### Q103. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $y(1+\log x)=\left(\log x^x\right) \frac{d y}{d x}$, when $y(e)=e^2$ is

**Options:**

- **(A)** 2 ex $\log x-y=e^2$
- **(B)** $3 e x \log y x-y=2 e^2$
- **(C)** $e x \log x+y=2 e^2$
- **(D)** $e x \log x-y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $e x \log x-y=0$**

**Detailed Solution:**

$$
\begin{aligned}
& y(1+\log x)=\left(\log x^x\right) \frac{d y}{d x} \\
& \therefore \int \frac{(1+\log x)}{\left(\log x^x\right)}=\int \frac{d y}{y}
\end{aligned}
$$
We know that $\frac{d}{d x}\left(\log x^x\right)=(1+\log x) d x$
$$
\begin{aligned}
& \therefore \log \left|\log \mathrm{x}^{\mathrm{x}}\right|=\log |\mathrm{y}|+\log \mathrm{c} \\
& \text { We have } \mathrm{y}(\mathrm{e})=\mathrm{e}^2 \\
& \therefore \log \left|\log \mathrm{e}^{\mathrm{e}}\right|=\log \left|\mathrm{e}^2\right|+\log \mathrm{c} \\
& \therefore \log |\mathrm{e} \log \mathrm{e}|=2 \log |\mathrm{e}|+\log \mathrm{c} \\
& \therefore 1=2+\log \mathrm{c} \Rightarrow \log \mathrm{c}=-1 \\
& \therefore \log \left|\log \mathrm{x}^{\mathrm{x}}\right|=\log |\mathrm{y}|-\log \mathrm{e} \\
& \therefore \log |\mathrm{x} \log \mathrm{x}|+\log \mathrm{e}=\log |\mathrm{y}| \\
& \therefore \mathrm{ex} \log \mathrm{x}-\mathrm{y}=0
\end{aligned}
$$

</details>

---

### Q104. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation.
$$
\left(\frac{y}{x}\right) \cos \left(\frac{y}{x}\right) d x-\left[\left(\frac{x}{y}\right) \sin \left(\frac{y}{x}\right)+\cos \left(\frac{y}{x}\right)\right] d y=0 \text { is }
$$

**Options:**

- **(A)** $\mathrm{y}^2 \sin \left(\frac{\mathrm{y}}{\mathrm{x}}\right)=\mathrm{k}$
- **(B)** $\mathrm{x} \sin \left(\frac{\mathrm{y}}{\mathrm{x}}\right)=\mathrm{k}$
- **(C)** $\sin \left(\frac{\mathrm{y}}{\mathrm{x}}\right)=\mathrm{k}$
- **(D)** $y \sin \left(\frac{y}{x}\right)=k$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y \sin \left(\frac{y}{x}\right)=k$**

**Detailed Solution:**

We have $\left(\frac{y}{x}\right) \cos \left(\frac{y}{x}\right) d x-\left[\left(\frac{x}{y}\right) \sin \left(\frac{y}{x}\right)+\cos \left(\frac{y}{x}\right)\right] d y=0$
$$
\therefore \frac{d y}{d x}=\frac{\left(\frac{y}{x}\right) \cos \left(\frac{y}{x}\right)}{\left(\frac{x}{y}\right) \sin \left(\frac{y}{x}\right)+\cos \left(\frac{y}{x}\right)}
$$
Put $\frac{y}{x}=v \Rightarrow y=v x \Rightarrow \frac{d y}{d x}=v+x \frac{d v}{d x}$
$$
\begin{aligned}
& \therefore \mathrm{v}+\mathrm{x} \frac{\mathrm{dv}}{\mathrm{dx}}=\frac{\mathrm{v} \cos \mathrm{v}}{\frac{1}{\mathrm{v}} \sin \mathrm{v}+\cos \mathrm{v}}=\frac{\mathrm{v}^2 \cos \mathrm{v}}{\sin \mathrm{v}+\mathrm{v} \cos \mathrm{v}} \Rightarrow \mathrm{x} \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{-\mathrm{v} \sin \mathrm{v}}{\sin \mathrm{v}+\mathrm{v} \cos \mathrm{v}} \\
& \therefore \int \frac{\sin \mathrm{v}+\mathrm{v} \cos \mathrm{v}}{\mathrm{v} \sin \mathrm{v}} \mathrm{dv}=\int \frac{-\mathrm{dx}}{\mathrm{x}} \Rightarrow \int \frac{1}{\mathrm{v}} \mathrm{dv}+\int \cot \mathrm{v} d \mathrm{v}=-\int \frac{\mathrm{dx}}{\mathrm{x}} \\
& \therefore \log |\mathrm{v}|+\log |+\sin \mathrm{x}|=-\log |\mathrm{x}|+\log \mathrm{k} \Rightarrow \log |(\mathrm{v})(\sin \mathrm{v})(\mathrm{x})| \\
& =\log \mathrm{k}
\end{aligned}
$$
$\therefore y \sin \left(\frac{y}{x}\right)=k$

</details>

---

### Q105. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation
$$
y(1+\log x)\left(\frac{d x}{d y}\right)
$$
$-x \log x=0$ is

**Options:**

- **(A)** $\mathrm{y}(1+\log \mathrm{x})=\mathrm{c}$
- **(B)** $\mathrm{x} \log \mathrm{x}=\mathrm{yc}$
- **(C)** $x \log x=y+c$
- **(D)** $\log \mathrm{x}-\mathrm{y}=\mathrm{c}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{x} \log \mathrm{x}=\mathrm{yc}$**

**Detailed Solution:**

$$
\begin{aligned}
& y(1+\log x)\left(\frac{d y}{d x}\right)-x \log x=0 \\
& \therefore \int \frac{(1+\log x)}{x \log x} d x=\int \frac{d y}{y} \\
& \int \frac{d x}{x \log x}+\int \frac{d x}{x}=\int \frac{d y}{y} \\
& \therefore \log (\log x)+\log x=\log y+\log c \\
& \therefore \log [x \log x]=\log (y, c)
\Rightarrow x \log x=y c
\end{aligned}
$$

</details>

---

### Q106. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $x+y \frac{d y}{d x}=\sec \left(x^2+y^2\right)$ is

**Options:**

- **(A)** $\sin \left(x^2+y^2\right)=2 x+c$
- **(B)** $\sin \left(x^2+y^2\right)+2 x=c$
- **(C)** $\sin \left(x^2+y^2\right)+x=c$
- **(D)** $\cos \left(x^2+y^2\right)=2 x+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sin \left(x^2+y^2\right)=2 x+c$**

**Detailed Solution:**

$\begin{aligned} & \text { We have, } x+y \frac{d y}{d x}=\sec \left(x^2+y^2\right) \\ & \text { Put } x^2+y^2=u \Rightarrow 2 x+2 y \frac{d y}{d x}=\frac{d u}{d x} \\ & \therefore x+y \frac{d y}{d x}=\frac{1}{2} \frac{d u}{d x} \\ & \therefore \frac{1}{2} \frac{d u}{d x}=\sec u \\ & \therefore \int \frac{d u}{\sec u}=\int 2 d x \\ & \therefore \sin u=2 x+c \\ & \Rightarrow \sin \left(x^2+y^2\right)=2 x+c\end{aligned}$

</details>

---

### Q107. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A differential equation for the temperature ' $\mathrm{T}$ ' of a hot body as a function of time, when it is placed in a both which is held at a constant temperature of $32^{\circ} \mathrm{F}$, is given by (where $\mathrm{k}$ is a constant of proportionality)

**Options:**

- **(A)** $\frac{\mathrm{dT}}{\mathrm{dt}}=\mathrm{kT}-32$
- **(B)** $\frac{\mathrm{dT}}{\mathrm{dt}}=\mathrm{kT}+32$
- **(C)** $\frac{\mathrm{dT}}{\mathrm{dt}}=\mathrm{k}(\mathrm{T}-32)$
- **(D)** $\frac{\mathrm{dT}}{\mathrm{dt}}=32 \mathrm{kT}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{dT}}{\mathrm{dt}}=\mathrm{k}(\mathrm{T}-32)$**

**Detailed Solution:**

The temperature $\mathrm{T}$ of the body will decrease with time. The body is kept in a bath of temperature $32^{\circ} \mathrm{F}$.
$$
\begin{aligned}
& \therefore \frac{\mathrm{dT}}{\mathrm{dt}} \alpha-(\mathrm{T}-32) \\
& \Rightarrow \frac{\mathrm{dT}}{\mathrm{dt}}=-\mathrm{k}(\mathrm{T}-32)
\end{aligned}
$$

</details>

---

### Q108. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{d y}{d x}=\frac{x+y+1}{x+y-1}$ is given by

**Options:**

- **(A)** $y=x \log (x+y)+c$
- **(B)** $x-y=\log (x+y)+c$
- **(C)** $x+y=\log (x+y)+c$
- **(D)** $y=x+\log (x+y)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y=x+\log (x+y)+c$**

**Detailed Solution:**

$$
\frac{d y}{d x}=\frac{x+y+1}{x+y-1}
$$
Put $x+y=u \Rightarrow 1+\frac{d y}{d x}=\frac{d u}{d x}$
$$
\begin{aligned}
& \therefore \frac{\mathrm{du}}{\mathrm{dx}}-1=\frac{\mathrm{u}+1}{\mathrm{u}-1} \Rightarrow \frac{\mathrm{du}}{\mathrm{dx}}=\frac{\mathrm{du}+1}{\mathrm{dx}-1}+1=\frac{2 \mathrm{u}}{\mathrm{u}-1} \\
& \therefore\left(\frac{\mathrm{u}-1}{\mathrm{u}}\right) \mathrm{du}=2 \mathrm{dx}
\end{aligned}
$$
Integrating both sides, we get
$$
\begin{aligned}
& \int d u-\int \frac{d u}{u}=\int 2 d x \\
& \therefore u-\log u=2 x+c \\
& \therefore x+y-\log (x+y)=2 x+c \Rightarrow y=x+\log (x+y)+c
\end{aligned}
$$

</details>

---

### Q109. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\sin ^{-1}\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)=x+\mathrm{y}$ is

**Options:**

- **(A)** $x=\tan (x+y) \cdot \sec (x+y)+c$
- **(B)** $x=\tan (x+y)-\sec (x+y)+c$
- **(C)** $x=\tan (x+y)+\sec (x+y)+c$
- **(D)** $x=\tan x \cdot \tan y+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=\tan (x+y)-\sec (x+y)+c$**

**Detailed Solution:**

We have $\sin ^{-1}\left(\frac{d y}{d x}\right)=x+y$
$$
\therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\sin (\mathrm{x}+\mathrm{y})
$$
Put $\quad x+y=t \Rightarrow y=t-x \Rightarrow \frac{d y}{d x}=\frac{d t}{d x}-1$
$$
\therefore \frac{\mathrm{dt}}{\mathrm{dx}}=1+\sin \mathrm{t} \Rightarrow \int \frac{\mathrm{dt}}{1+\sin \mathrm{t}}=\int \mathrm{dx}
$$
$\int \frac{(1-\sin t)}{(1+\sin t)(1-\sin t)} d t=\int d x \Rightarrow x=\int \frac{1-\sin t}{1-\sin ^{2} t} d t$
$x=\int \frac{1-\sin t}{\cos ^{2} t} d t=\int\left(\sec ^{2} t-\sec t \tan t\right) d t$
$x=\tan t-\sec t+c$
$x=\tan (x+y)-\sec (x+y)+c$

</details>

---

### Q110. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\left(1+y^{2}\right)+\left(x-e^{\tan ^{-1} y}\right) \frac{d y}{d x}=0$ is

**Options:**

- **(A)** $x \cdot e^{\tan ^{-1} y}=\frac{\left(e^{\tan ^{-1} x}\right)^{2}}{2}+c$
- **(B)** $e^{\tan ^{-1} y}=\left(e^{\tan ^{-1} x}\right)^{2}+c$
- **(C)** $x \cdot e^{\tan ^{-1} y}=\frac{\left(e^{t a n^{-1} y}\right)^{2}}{2}+c$
- **(D)** $e^{\tan ^{-1} y}=\left(e^{\tan ^{-1} y}\right)^{2}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x \cdot e^{\tan ^{-1} y}=\frac{\left(e^{t a n^{-1} y}\right)^{2}}{2}+c$**

**Detailed Solution:**

(A)
$\begin{array}{l}
\left(1+y^{2}\right)+\left(x-e^{\tan ^{-1} y}\right) \frac{d y}{d x}=0 \\
\therefore \quad\left(x-e^{\tan ^{-1} y}\right) \frac{d y}{d x}=-\left(1+y^{2}\right) \Rightarrow \frac{d y}{d x}=\frac{-\left(1+y^{2}\right)}{x-e^{\tan ^{-1} y}} \\
\therefore \frac{d x}{d y}=\frac{\left(x-e^{\tan ^{-1} y}\right)}{-\left(1+y^{2}\right)} \Rightarrow \frac{d x}{d y}=\frac{-x}{\left(1+y^{2}\right)}+\frac{e^{\tan ^{-1} y}}{1+y^{2}} \\
\therefore \frac{d x}{d y}+\frac{x}{1+y^{2}}=\frac{e^{\tan ^{-1} y}}{1+y^{2}} \\
\quad \text { I.F. }=e^{\int \frac{1}{1+y^{2}} d y}=e^{\tan ^{-1} y}
\end{array}$
So, the general solution is
$\begin{array}{l}
x \cdot e^{\tan ^{-1} y}=\int \frac{e^{\tan ^{-1} y}}{1+y^{2}} \cdot e^{\tan ^{-1} y} d x \\
\text { Put } e^{\tan ^{-1} y}=t \Rightarrow \frac{e^{\tan ^{-1} y}}{1+y^{2}} d y=d t \\
\therefore x \cdot e^{\tan ^{-1} y}=\int t d t \\
\therefore x \cdot e^{\tan ^{-1} y}=\frac{t^{2}}{2}+c \Rightarrow x \cdot e^{\tan ^{-1} y}=\frac{\left(e^{\tan ^{-1} y}\right)^{2}}{2}+c
\end{array}$

</details>

---

### Q111. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The particular solution of the differential equation $y\left(\frac{\mathrm{d} x}{\mathrm{~d} y}\right)=x \log x$ at $x=\mathrm{e}$ and $\mathrm{y}=1$ is

**Options:**

- **(A)** $\mathrm{e}^{x y}=2$
- **(B)** $x=\mathrm{e}^{\mathrm{y}}$
- **(C)** $x\mathrm{y}=2$
- **(D)** $\log x=2 y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x=\mathrm{e}^{\mathrm{y}}$**

**Detailed Solution:**

(D)
$y\left(\frac{d x}{d y}\right)=x \cdot \log x$
$\therefore \int \frac{1}{x \cdot \log x} d x=\int \frac{1}{y} d y$
$\therefore \log |\log x|=\log y+\log c$
We have $x=e$ and $y=1$
$\therefore \log |\log e|=\log 1+\log c \Rightarrow \log c=0$
$\therefore \log |\log x|=\log y \Rightarrow \log x=y \Rightarrow x=e^{y}$

</details>

---

### Q112. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\log \left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)=9 x-6 \mathrm{y}+6$ is
(given that $\mathrm{y}=1$ when $x=0$ )

**Options:**

- **(A)** $3 e^{6 y}=2 e^{9 x-6}+e^{6}$
- **(B)** $3 e^{6 y}=2 e^{9 x+6}+e^{6}$
- **(C)** $3 e^{6 y}=2 e^{9 x+6}-e^{6}$
- **(D)** $3 e^{6 y}=2 e^{9 x-6}-e^{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 e^{6 y}=2 e^{9 x+6}+e^{6}$**

**Detailed Solution:**

$\log \left(\frac{d y}{d x}\right)=9 x-6 y+6 \Rightarrow \frac{d y}{d x}=e^{9 x-6 y+6}$
$\therefore \frac{d y}{d x}=e^{9 x+6} \cdot e^{-6 y} \Rightarrow \frac{d y}{e^{-6 y}}=e^{9 x} \cdot e^{6} d x$
$\therefore \int e^{6 y} d y=e^{6} \int e^{9 x} d x$
$\frac{e^{6 y}}{6}=\frac{e^{6} e^{9 x}}{9}+C$
We have $x=0, y=1$
$\therefore \frac{e^{6}}{6}=\frac{e^{6}}{9}+C \Rightarrow C=\frac{e^{6}}{18}$
$\therefore \frac{e^{6 y}}{6}=\frac{e^{6} e^{9 x}}{9}+\frac{e^{6}}{18} \Rightarrow 3 e^{6 y}=2 e^{6+9 x}+e^{6}$

</details>

---

### Q113. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation $\frac{d y}{d x}+\frac{1}{\sqrt{1-x^{2}}}=0$ is

**Options:**

- **(A)** $y^{2}+2 \sin ^{-1} x=c$
- **(B)** $x+\sin ^{-1} y=c$
- **(C)** $y+\sin ^{-1} x=c$
- **(D)** $x^{2}+2 \sin ^{2} y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y+\sin ^{-1} x=c$**

**Detailed Solution:**

$\frac{d y}{d x}+\frac{1}{\sqrt{1-x^{2}}}=0$
$\therefore \frac{d y}{d x}=\frac{-1}{\sqrt{1-x^{2}}} \Rightarrow d y=\frac{-d x}{\sqrt{1-x^{2}}} \Rightarrow \int d y=-\int \frac{d x}{\sqrt{1-x^{2}}}$
$\therefore y=-\sin ^{-1} x+c$

</details>

---

### Q114. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation $x d y+2 y d x=0$, when $x=2$
and $y=1$ is

**Options:**

- **(A)** $x y^{2}=4$
- **(B)** $x^{2} y=4$
- **(C)** $x^{2} y=-4$
- **(D)** $x y^{2}=-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^{2} y=4$**

**Detailed Solution:**

Given D.E. is $x d y+2 y d x=0$
$\therefore x d y=-2 y d x \Rightarrow \int \frac{d y}{y}=\int-\frac{2 d x}{x}$
$\log y=-2 \log x+\log c \Rightarrow \log y+2 \log x=\log c$
$\therefore \quad \log y+\log x^{2}=\log c \Rightarrow x^{2} y=c$
when $x=2, y=1, c=4$
$\therefore$ Particular solution is $\mathrm{x}^{2} \mathrm{y}=4$

</details>

---

### Q115. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The general solution of the differential equation $\sec ^{2} x$ tany $d x+\sec ^{2} y \tan x d y=0$
is

**Options:**

- **(A)** $\tan x \tan y=c$
- **(B)** $\sec x \tan y=c$
- **(C)** $\sec x \sec y=c$
- **(D)** $\tan x \sec y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\tan x \tan y=c$**

**Detailed Solution:**

$\begin{aligned} & \sec ^{2} x \tan y d x+\sec ^{2} y \tan x d y=0 \\ \therefore & \sec ^{2} x \tan y d x=-\sec ^{2} y \tan x d y \\ & \frac{\sec ^{2} x}{\tan x} d x=-\frac{\sec ^{2} y}{\tan y} d y \Rightarrow \int \frac{\sec ^{2} x}{\tan x} d x=-\int \frac{\sec ^{2} y}{\tan y} d y \\ & \log (\tan x)=-\log (\tan y)+\log c \\ \therefore & \log (\tan x \tan y)=\log c \\ & \tan x \tan y=c \end{aligned}$

</details>

---

### Q116. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of <math><mi>x</mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>y</mi><mo>-</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow></math> is ________

**Options:**

- **(A)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi></mrow></mrow></math>
- **(B)** <math><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Given equation is 
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>  
is Homogeneous equation, then 
Put <math><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math>   and <math><mi mathvariant="normal"></mi><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>  
Then, 
<math><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>-</mo><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>v</mi></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi>v</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math> (integrate both sides) 
<math><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>v</mi></mrow></mrow></mrow></mrow><mo>=</mo><mi></mi><mo>–</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mi>c</mi></mrow></mrow></math>  
<math><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mfenced separators="|"><mrow><mi>x</mi><mo>⋅</mo><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mi>c</mi></mrow></mrow><mo>&#8658;</mo><mi>x</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>c</mi></math>

</details>

---

### Q117. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation <math><mi mathvariant="normal"></mi><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mi>k</mi><mfenced separators="|"><mrow><mi>θ</mi><mo>-</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></math>, where k is constant, is ……

**Options:**

- **(A)** <math><mi>θ</mi><mo>=</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>k</mi><mi>t</mi></mrow></msup></math>
- **(B)** <math><mi>θ</mi><mo>=</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup></math>
- **(C)** <math><mi>θ</mi><mo>=</mo><mn>2</mn><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup></math>
- **(D)** <math><mi>θ</mi><mo>=</mo><mn>2</mn><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>k</mi><mi>t</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>θ</mi><mo>=</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>k</mi><mi>t</mi></mrow></msup></math>**

**Detailed Solution:**

We have differential equation 
<math><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mi>k</mi><mfenced separators="|"><mrow><mi>θ</mi><mo>-</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced><mo>,</mo></math> where k is constant 
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>θ</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><mi>k</mi><mi>θ</mi><mo>=</mo><mi>k</mi><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub></math>  
Which is linear differential equation in form of 
<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi></math>  
<math><mo>∴</mo><mi>I</mi><mi>F</mi><msub><mrow><mo>=</mo></mrow><mrow><mi>e</mi></mrow></msub><mo>∫</mo><mi>k</mi><mi>d</mi><mi>t</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup></math>  
Therefore, required solution, 
<math><mfenced separators="|"><mrow><mi>θ</mi></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup></mrow></mfenced><mo>=</mo><mo>∫</mo><mfenced separators="|"><mrow><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup><mo>×</mo><mi>k</mi><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced><mi>d</mi><mi>t</mi></math>  
<math><mo>&#8658;</mo><msup><mrow><mi>θ</mi></mrow><mrow><mi>e</mi><mi>k</mi><mi>t</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>k</mi><mi>t</mi></mrow></msup><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>a</mi></math>  
<math><mo>&#8658;</mo><mi>θ</mi><mo>=</mo><msub><mrow><mi>θ</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mi>a</mi><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mi>k</mi><mi>t</mi></mrow></msup></math>

</details>

---

### Q118. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation log <math><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi></math> , when x =0, y = 1 is …..

**Options:**

- **(A)** <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></math>
- **(B)** <math><mi>y</mi><mo>=</mo><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>
- **(C)** <math><mi>y</mi><mo>=</mo><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><mn>2</mn></math>
- **(D)** <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>**

**Detailed Solution:**

We have, differential equations, 
<math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>x</mi><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>  
<math><mo>&#8658;</mo><mi>d</mi><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math>  
Integrating on both sides, we get 
<math><mo>∫</mo><mi>d</mi><mi>y</mi><mo>=</mo><mo>∫</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mi>d</mi><mi>x</mi></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup><mo>+</mo><mi>C</mi></math> … (i) 
On putting x = 0, y = 1 is Eq. (i), we get 
<math><mn>1</mn><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>+</mo><mi>C</mi><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>0</mn></math>  
Now, particular solution of the given differential is <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi></mrow></msup></math>

</details>

---

### Q119. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of differential equation <math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math> is….

**Options:**

- **(A)** <math><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>c</mi></math>
- **(B)** <math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>c</mi></math>
- **(C)** <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>c</mi></math>
- **(D)** <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>c</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>c</mi></math>**

**Detailed Solution:**

We have, differential equation 
<math><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math>  
<em>On the integrating both sides, we get</em> 
<math><mo>∫</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math>  
<math><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>=</mo><mo>-</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>+</mo><mi>C</mi></math>  
<math><mo>&#8658;</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>x</mi><mo>+</mo><msup><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>y</mi><mo>=</mo><mi>C</mi></math>

</details>

---

### Q120. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `3`

The general solution of differential equation <math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi> </mrow> <mrow> <mi>d</mi><mi>x</mi> </mrow> </mfrac> <mo>=</mo><mi>cos</mi><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>+</mo><mi>y</mi> </mrow> <mo>)</mo></mrow> </mrow> </math> is

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>y</mi><mo>+</mo><mi>c</mi></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>y</mi><mo>+</mo><mi>c</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></mrow></mrow></math>**

**Detailed Solution:**

Let <math> <mrow> <mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mi>v</mi></mrow> </math>
<math> <mrow> <mn>1</mn><mo>+</mo><mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>−</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mo>∴</mo><mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>−</mo><mn>1</mn><mo>=</mo><mi>cos</mi><mi>v</mi></mrow> </math>
<math> <mo>⇒</mo><mrow> <mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mn>1</mn><mo>+</mo><mi>cos</mi><mi>v</mi></mrow> </math>
<math> <mo>⇒</mo><mrow> <mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> <mo>=</mo><mn>2</mn><msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mfrac> <mi>v</mi> <mn>2</mn> </mfrac> </mrow> </math>
<math> <mo>⇒</mo><mrow>  <mrow><mo>∫</mo> <mrow> <mfrac> <mrow> <mi>d</mi><mi>v</mi></mrow> <mrow> <msup> <mrow> <mi>cos</mi></mrow> <mn>2</mn> </msup> <mfrac> <mi>v</mi> <mn>2</mn> </mfrac> </mrow> </mfrac> <mo>=</mo><mn>2</mn> <mrow><mo>∫</mo> <mrow> <mi>d</mi><mi>x</mi></mrow> </mrow> </mstyle></mrow> </mrow> </mstyle></mrow> </math>
<math> <mo>⇒</mo><mrow>  <mrow><mo>∫</mo> <mrow> <msup> <mrow> <mi>sec</mi></mrow> <mn>2</mn> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mi>v</mi> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow></mrow> </mrow> </mstyle><mtext> </mtext><mi>d</mi><mi>v</mi><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></mrow> </math>
<math> <mo>⇒</mo><mrow> <mn>2</mn><mi>tan</mi><mrow><mo>(</mo> <mrow> <mfrac> <mi>v</mi> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></mrow> </math>
<math> <mo>⇒</mo><mrow><mn>2</mn><mi>tan</mi><mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mi>x</mi><mo>+</mo><mi>y</mi></mrow> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>c</mi></mrow> </math>
<math><mrow><mo>⇒</mo><mi>tan</mi><mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mi>x</mi><mo>+</mo><mi>y</mi></mrow> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mi>x</mi><mo>+</mo><mfrac> <mi>c</mi> <mn>2</mn> </mfrac> </mrow> </math>
<math> <mrow> <mo>⇒</mo><mi>tan</mi><mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mi>x</mi><mo>+</mo><mi>y</mi></mrow> <mn>2</mn> </mfrac> </mrow> <mo>)</mo></mrow><mo>=</mo><mi>x</mi><mo>+</mo><mi>c</mi></mrow> </math>

</details>

---

### Q121. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow></math> is

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi><mi>x</mi></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi><mi>x</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>c</mi><mi>y</mi></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>c</mi><mi>y</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>c</mi><mi>x</mi></mrow></mrow></math>**

**Detailed Solution:**

<math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></math> 
 <math><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi></math> 
 <math><mi>y</mi><mo>=</mo><mi>v</mi><mi>x</mi></math> 
 <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> 
 <math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi></math>   the given equation becomes
 <math><mi>v</mi><mo>+</mo><mi>x</mi><mfrac><mrow><mi>d</mi><mi>v</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>v</mi><mo>+</mo><mi>v</mi></mrow></mrow></math> 
 <math><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>v</mi></mrow></mrow></mrow></mfrac><mi>d</mi><mi>v</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mi> </mi><mi>d</mi><mi>x</mi></math> 
 <math><mrow><mo stretchy="false">∫</mo><mrow><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>v</mi></mrow></mrow></mrow></mrow><mi> </mi><mi>d</mi><mi>v</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mrow><mi>d</mi><mi>x</mi></math> 
 <math><mrow><mrow><mi mathvariant="normal">log </mi></mrow><mo>⁡</mo><mrow><mfenced close="|" open="|" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>v</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>c</mi></mrow></mrow></math> 
 <math><mo>=</mo><mrow><mrow><mi mathvariant="normal">log </mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi>x</mi><mi>c</mi></mrow></mfenced></mrow></mrow></math> 
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>v</mi></mrow></mrow><mo>=</mo><mi>x</mi><mi>c</mi></math> 
 <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mrow><mo>=</mo><mi>x</mi><mi>c</mi></math>

</details>

---

### Q122. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $y(1+\log x) \frac{d x}{d y}-x \log x=0$ is

**Options:**

- **(A)** $x \log x=y+c$
- **(B)** $x \log x=y c$
- **(C)** $y(1+\log x)=c$
- **(D)** $\log x-y=c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x \log x=y c$**

**Detailed Solution:**

Given differential equation is
$$
y(1+\log x) \frac{d x}{d y}-x \log x=0
$$
$$
\begin{array}{ll}
\Rightarrow & \int \frac{1+\log x}{x \log x} d x=\int \frac{d y}{y} \\
\Rightarrow & \int \frac{1}{x \log x} d x+\int \frac{1}{x} d x=\int \frac{1}{y} d y \\
\Rightarrow & \log (\log x)+\log x=\log y+\log c \\
\Rightarrow & x \log x=y c
\end{array}
$$

</details>

---

### Q123. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

If $x y=\tan ^{-1}(x y)+\cot ^{-1}(x y)$, then $\frac{d y}{d x}$ is equal
to

**Options:**

- **(A)** $\frac{y}{x}$
- **(B)** $-\frac{y}{x}$
- **(C)** $\frac{x}{y}$
- **(D)** $-\frac{x}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{y}{x}$**

**Detailed Solution:**

$x y=\tan ^{-1}(x y)+\cot ^{-1}(x y)=\frac{\pi}{2}$
$\Rightarrow \quad x y=\frac{\pi}{2}$
$\therefore \quad x \frac{d y}{d x}+y=0$
$\Rightarrow \quad \frac{d y}{d x}=\frac{-y}{x}$

</details>

---

