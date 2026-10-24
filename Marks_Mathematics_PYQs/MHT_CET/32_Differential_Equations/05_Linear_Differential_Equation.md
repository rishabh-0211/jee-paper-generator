# MHT CET Mathematics - Differential Equations

## Topic 5: Linear Differential Equation

**Total Questions:** 54

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following is not a correct pair of a linear differential equation and its integrating factor?

**Options:**

- **(A)** Linear differential equation $\dfrac{dy}{dx} - y = 2x$, Integrating factor $= e^{-x}$
- **(B)** Linear differential equation $\dfrac{dy}{dx} + y = e^x$, Integrating factor $= e^x$
- **(C)** Linear differential equation $\dfrac{dy}{dx} = x + xy$, Integrating factor $= e^{\frac{x^2}{2}}$
- **(D)** Linear differential equation $x\dfrac{dy}{dx} + 2y = x^2 \log x$, Integrating factor $= x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Linear differential equation $\dfrac{dy}{dx} = x + xy$, Integrating factor $= e^{\frac{x^2}{2}}$**

**Detailed Solution:**

A linear differential equation is of the form $\dfrac{dy}{dx} + Py = Q$, and its integrating factor is given by $e^{\int P dx}$.

For the first option, the differential equation is $\dfrac{dy}{dx} - y = 2x$. Here $P = -1$.
Integrating factor $= e^{\int -1 dx} = e^{-x}$. This pair is correct.

For the second option, the differential equation is $\dfrac{dy}{dx} + y = e^x$. Here $P = 1$.
Integrating factor $= e^{\int 1 dx} = e^x$. This pair is correct.

For the third option, the differential equation is $\dfrac{dy}{dx} = x + xy \Rightarrow \dfrac{dy}{dx} - xy = x$. Here $P = -x$.
Integrating factor $= e^{\int -x dx} = e^{-\dfrac{x^2}{2}}$. The given integrating factor is $e^{\dfrac{x^2}{2}}$, which is incorrect.

For the fourth option, the differential equation is $x\dfrac{dy}{dx} + 2y = x^2 \log x \Rightarrow \dfrac{dy}{dx} + \dfrac{2}{x}y = x \log x$. Here $P = \dfrac{2}{x}$.
Integrating factor $= e^{\int \dfrac{2}{x} dx} = e^{2\log x} = x^2$. This pair is correct.

Thus, the incorrect pair is the third option.

Answer: Linear differential equation $\dfrac{dy}{dx} = x + xy$, Integrating factor $= e^{\frac{x^2}{2}}$

</details>

---

### Q2. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $(x + 1)\dfrac{dy}{dx} - y = e^x(x + 1)^2$ is given by:

**Options:**

- **(A)** $y = (x + 1)(e^x + c)$
- **(B)** $y = (x + 1)(e^{-x} + c)$
- **(C)** $y = \dfrac{e^x + c}{x + 1}$
- **(D)** $y = e^x + c(x + 1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y = (x + 1)(e^x + c)$**

**Detailed Solution:**

The given differential equation is $(x + 1)\dfrac{dy}{dx} - y = e^x(x + 1)^2$

Dividing the entire equation by $(x + 1)$, we get:

$\dfrac{dy}{dx} - \dfrac{1}{x + 1}y = e^x(x + 1)$

This is a linear differential equation of the form $\dfrac{dy}{dx} + P(x)y = Q(x)$, where $P(x) = -\dfrac{1}{x + 1}$ and $Q(x) = e^x(x + 1)$.

The integrating factor (IF) is given by:

$\text{IF} = e^{\int P(x) dx} = e^{\int -\dfrac{1}{x + 1} dx} = e^{-\ln(x + 1)} = \dfrac{1}{x + 1}$

The general solution is:

$y \cdot (\text{IF}) = \int Q(x) \cdot (\text{IF}) dx + c$

$y \cdot \dfrac{1}{x + 1} = \int e^x(x + 1) \cdot \dfrac{1}{x + 1} dx + c$

$\dfrac{y}{x + 1} = \int e^x dx + c$

$\dfrac{y}{x + 1} = e^x + c$

$y = (x + 1)(e^x + c)$

Answer: $y = (x + 1)(e^x + c)$

</details>

---

### Q3. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the curve $y = f(x)$ passes through the point $(1, 2)$ and satisfies the differential equation $x dy + (y + x^3 y^2)dx = 0$, then the equation of curve is...

**Options:**

- **(A)** $xy = 2$
- **(B)** $y = 2x$
- **(C)** $x^2 y = 2$
- **(D)** $x^3 y = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^3 y = 2$**

**Detailed Solution:**

The given differential equation is:

$x dy + (y + x^3 y^2)dx = 0$

Rearranging the terms, we get:

$x dy + y dx = -x^3 y^2 dx$

Using the product rule of differentiation, $d(xy) = x dy + y dx$. Substituting this into the equation:

$d(xy) = -x^3 y^2 dx$

Dividing both sides by $(xy)^2$:

$\dfrac{d(xy)}{(xy)^2} = -x dx$

Integrating both sides:

$\int \dfrac{d(xy)}{(xy)^2} = -\int x dx$

$-\dfrac{1}{xy} = -\dfrac{x^2}{2} + C$

Since the curve passes through the point $(1, 2)$, we substitute $x = 1$ and $y = 2$ into the equation:

$-\dfrac{1}{1 \times 2} = -\dfrac{1^2}{2} + C$

$-\dfrac{1}{2} = -\dfrac{1}{2} + C \Rightarrow C = 0$

Substituting $C = 0$ back into the integrated equation:

$-\dfrac{1}{xy} = -\dfrac{x^2}{2}$

$\dfrac{1}{xy} = \dfrac{x^2}{2}$

$x^3 y = 2$

Answer: $x^3 y = 2$

</details>

---

### Q4. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $g(x)$ denotes the integrating factor of the differential equation $x \log x \dfrac{dy}{dx} + y = 2 \log x$ and $\int g(x) \, dx = h(x)[g(x) - 1] + c$, then $h(x) = $.........

**Options:**

- **(A)** $1$
- **(B)** $x$
- **(C)** $\log x$
- **(D)** $x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x$**

**Detailed Solution:**

The given differential equation is $x \log x \dfrac{dy}{dx} + y = 2 \log x$.

Dividing the entire equation by $x \log x$, we get:

$\dfrac{dy}{dx} + \dfrac{1}{x \log x} y = \dfrac{2}{x}$

This is a linear differential equation of the form $\dfrac{dy}{dx} + P y = Q$, where $P = \dfrac{1}{x \log x}$.

The integrating factor $g(x)$ is given by:

$g(x) = e^{\int P \, dx} = e^{\int \dfrac{1}{x \log x} \, dx}$

Let $\log x = t$, then $\dfrac{1}{x} dx = dt$.

$\int \dfrac{1}{x \log x} \, dx = \int \dfrac{1}{t} \, dt = \log t = \log(\log x)$

Therefore, $g(x) = e^{\log(\log x)} = \log x$.

Now, we evaluate $\int g(x) \, dx$:

$\int g(x) \, dx = \int \log x \, dx$

Using integration by parts:

$\int \log x \cdot 1 \, dx = x \log x - \int x \cdot \dfrac{1}{x} \, dx = x \log x - x + c = x(\log x - 1) + c$

We are given that $\int g(x) \, dx = h(x)[g(x) - 1] + c$.

Substituting $g(x) = \log x$, we get:

$x(\log x - 1) + c = h(x)[\log x - 1] + c$

Comparing both sides, we obtain:

$h(x) = x$

Answer: $x$

</details>

---

### Q5. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $yf(x)=g(x)+c$ where $c$ is an arbitrary constant such that $\dfrac{dy}{dx}+yg(x)=f(x)$ and $[f(x)]^2-[g(x)]^2=1$, then $\int f(x)\cdot g(x)\,dx=$ ...

**Options:**

- **(A)** $g(x)+c$
- **(B)** $-g(x)+c$
- **(C)** $f(x)+c$
- **(D)** $-f(x)+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(x)+c$**

**Detailed Solution:**

Given the differential equation:

$\dfrac{dy}{dx} + y g(x) = f(x)$

The solution is given as:

$y f(x) = g(x) + c$

Differentiating the solution with respect to $x$, we get:

$\dfrac{dy}{dx} f(x) + y f'(x) = g'(x)$

Substitute $\dfrac{dy}{dx} = f(x) - y g(x)$ from the given differential equation into the differentiated equation:

$(f(x) - y g(x)) f(x) + y f'(x) = g'(x)$

$f(x)^2 - y f(x) g(x) + y f'(x) = g'(x)$

$y (f'(x) - f(x) g(x)) + f(x)^2 - g'(x) = 0$

Since this equation must hold true for any arbitrary constant $c$, it must be an identity in $y$. Therefore, the coefficient of $y$ and the remaining terms must independently be zero:

$f'(x) - f(x) g(x) = 0 \Rightarrow f'(x) = f(x) g(x)$

$f(x)^2 - g'(x) = 0 \Rightarrow g'(x) = f(x)^2$

We can verify this is consistent with the given relation $[f(x)]^2 - [g(x)]^2 = 1$. Differentiating it gives $2f(x)f'(x) - 2g(x)g'(x) = 0$, which holds true upon substituting $f'(x)$ and $g'(x)$.

We need to evaluate the integral $\int f(x) g(x) \,dx$. Using the relation $f'(x) = f(x) g(x)$, we get:

$\int f(x) g(x) \,dx = \int f'(x) \,dx = f(x) + c$

Answer: $f(x)+c$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\dfrac{dy}{dx} + \dfrac{y}{x} = x^2 + 5$ is ....

**Options:**

- **(A)** $\dfrac{x^4}{4} + \dfrac{5x^2}{2} - xy = c$
- **(B)** $\dfrac{x^4}{4} - \dfrac{5x^2}{2} - xy = c$
- **(C)** $\dfrac{x^4}{4} - \dfrac{5x^2}{2} + xy = c$
- **(D)** $\dfrac{x^4}{4} + \dfrac{5x^2}{2} + xy = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{x^4}{4} + \dfrac{5x^2}{2} - xy = c$**

**Detailed Solution:**

The given differential equation is $\dfrac{dy}{dx} + \dfrac{1}{x}y = x^2 + 5$.

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = \dfrac{1}{x}$ and $Q = x^2 + 5$.

The integrating factor is $e^{\int P dx} = e^{\int \dfrac{1}{x} dx} = e^{\ln x} = x$.

Multiplying the equation by the integrating factor, the solution is given by:

$y \cdot x = \int x(x^2 + 5) dx + C$

$xy = \int (x^3 + 5x) dx + C$

$xy = \dfrac{x^4}{4} + \dfrac{5x^2}{2} + C$

Rearranging the terms, we get:

$\dfrac{x^4}{4} + \dfrac{5x^2}{2} - xy = -C$

Taking $-C = c$, the general solution is:

$\dfrac{x^4}{4} + \dfrac{5x^2}{2} - xy = c$

Answer: $\dfrac{x^4}{4} + \dfrac{5x^2}{2} - xy = c$

</details>

---

### Q7. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\tan x$ is an integrating factor of the differential equation $\dfrac{dy}{dx} + Py = Q$, then $P$ can be

**Options:**

- **(A)** $2\sec 2x$
- **(B)** $\tan 2x$
- **(C)** $\sin 2x$
- **(D)** $2\csc 2x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2\csc 2x$**

**Detailed Solution:**

The integrating factor of the linear differential equation $\dfrac{dy}{dx} + Py = Q$ is given by $e^{\int P dx}$.

Given that the integrating factor is $\tan x$, we have:

$e^{\int P dx} = \tan x$

Taking the natural logarithm on both sides:

$\int P dx = \ln(\tan x)$

Differentiating both sides with respect to $x$:

$P = \dfrac{d}{dx} (\ln(\tan x))$

$P = \dfrac{1}{\tan x} \cdot \sec^2 x$

$P = \dfrac{\cos x}{\sin x} \cdot \dfrac{1}{\cos^2 x}$

$P = \dfrac{1}{\sin x \cos x}$

$P = \dfrac{2}{2 \sin x \cos x}$

$P = \dfrac{2}{\sin 2x}$

$P = 2 \csc 2x$

Answer: $2\csc 2x$

</details>

---

### Q8. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the solution of the differential equation $(1 + x^3)\dfrac{dy}{dx} + 6x^2y = 1 + x^2$ is $y = \dfrac{1}{(1 + x^3)^s}\left[x + \dfrac{x^p}{p} + \dfrac{x^q}{q} + \dfrac{x^r}{r} + c\right]$, then the LCM of $p, q, r$ and $s$ is...

**Options:**

- **(A)** $1$
- **(B)** $6$
- **(C)** $4$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12$**

**Detailed Solution:**

The given differential equation is $(1 + x^3)\dfrac{dy}{dx} + 6x^2y = 1 + x^2$.

Dividing by $(1 + x^3)$, we get a linear differential equation of the form $\dfrac{dy}{dx} + P(x)y = Q(x)$:

$\dfrac{dy}{dx} + \dfrac{6x^2}{1 + x^3}y = \dfrac{1 + x^2}{1 + x^3}$

The integrating factor (IF) is given by:

$\text{IF} = e^{\int P(x) dx} = e^{\int \dfrac{6x^2}{1 + x^3} dx}$

Let $1 + x^3 = t$, then $3x^2 dx = dt$, which gives $6x^2 dx = 2 dt$.

$\int \dfrac{6x^2}{1 + x^3} dx = \int \dfrac{2}{t} dt = 2 \ln t = \ln(t^2) = \ln((1 + x^3)^2)$

Thus, $\text{IF} = e^{\ln((1 + x^3)^2)} = (1 + x^3)^2$.

Multiplying the differential equation by the IF, we get:

$\dfrac{d}{dx} \left[ y (1 + x^3)^2 \right] = \dfrac{1 + x^2}{1 + x^3} \times (1 + x^3)^2$

$\dfrac{d}{dx} \left[ y (1 + x^3)^2 \right] = (1 + x^2)(1 + x^3)$

$\dfrac{d}{dx} \left[ y (1 + x^3)^2 \right] = 1 + x^2 + x^3 + x^5$

Integrating both sides with respect to $x$:

$y (1 + x^3)^2 = \int (1 + x^2 + x^3 + x^5) dx$

$y (1 + x^3)^2 = x + \dfrac{x^3}{3} + \dfrac{x^4}{4} + \dfrac{x^6}{6} + c$

$y = \dfrac{1}{(1 + x^3)^2} \left[ x + \dfrac{x^3}{3} + \dfrac{x^4}{4} + \dfrac{x^6}{6} + c \right]$

Comparing this with the given solution $y = \dfrac{1}{(1 + x^3)^s}\left[x + \dfrac{x^p}{p} + \dfrac{x^q}{q} + \dfrac{x^r}{r} + c\right]$, we find:

$s = 2$

The set of values for $\{p, q, r\}$ is $\{3, 4, 6\}$.

We need to find the LCM of $p, q, r$ and $s$, which is the LCM of $3, 4, 6,$ and $2$.

$\text{LCM}(2, 3, 4, 6) = 12$

Answer: $12$

</details>

---

### Q9. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $x\dfrac{dy}{dx} + 2y = x^2 \log x$ is

**Options:**

- **(A)** $x^3$
- **(B)** $x^2$
- **(C)** $\log 2x$
- **(D)** $\log x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2$**

**Detailed Solution:**

The given differential equation is $x\dfrac{dy}{dx} + 2y = x^2 \log x$.

Dividing the entire equation by $x$, we get:

$\dfrac{dy}{dx} + \dfrac{2}{x}y = x \log x$

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = \dfrac{2}{x}$ and $Q = x \log x$.

The integrating factor (IF) is given by $e^{\int P dx}$.

$\text{IF} = e^{\int \dfrac{2}{x} dx}$

$\text{IF} = e^{2 \log x}$

$\text{IF} = e^{\log x^2}$

$\text{IF} = x^2$

Answer: $x^2$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $x\sin x\dfrac{dy}{dx} + (x\cos x + \sin x)y = \sin x$ is

**Options:**

- **(A)** $x\sin x + y\cos x = c$
- **(B)** $y\sin x + x\cos x = c$
- **(C)** $xy\sin x - \cos x = c$
- **(D)** $xy\sin x + \cos x = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $xy\sin x + \cos x = c$**

**Detailed Solution:**

The given differential equation is $x\sin x\dfrac{dy}{dx} + (x\cos x + \sin x)y = \sin x$

Observing the left hand side, it can be rewritten using the product rule of differentiation:

$x\sin x\dfrac{dy}{dx} + y\dfrac{d}{dx}(x\sin x) = \sin x$

$\dfrac{d}{dx}(xy\sin x) = \sin x$

Integrating both sides with respect to $x$:

$\int \dfrac{d}{dx}(xy\sin x) dx = \int \sin x dx$

$xy\sin x = -\cos x + c$

$xy\sin x + \cos x = c$

Answer: $xy\sin x + \cos x = c$

</details>

---

### Q11. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\sec y + (x - e^{\sin y})\dfrac{dy}{dx} = 0$ is...

**Options:**

- **(A)** $e^{\sin y} = x + c$
- **(B)** $xe^{\sin y} = \dfrac{e^{2\sin y}}{2} + c$
- **(C)** $2x\cos y = e^x + c$
- **(D)** $\sin y - e^{\sin y} = c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $xe^{\sin y} = \dfrac{e^{2\sin y}}{2} + c$**

**Detailed Solution:**

The given differential equation is $\sec y + (x - e^{\sin y})\dfrac{dy}{dx} = 0$

Rearranging the terms, we get:

$\sec y \dfrac{dx}{dy} + x - e^{\sin y} = 0$

$\dfrac{dx}{dy} + x \cos y = e^{\sin y} \cos y$

This is a linear differential equation of the form $\dfrac{dx}{dy} + P(y)x = Q(y)$, where $P(y) = \cos y$ and $Q(y) = e^{\sin y} \cos y$.

The integrating factor (IF) is:

$IF = e^{\int \cos y dy} = e^{\sin y}$

Multiplying the equation by the integrating factor and integrating, the solution is given by:

$x \cdot IF = \int Q(y) \cdot IF dy + c$

$x e^{\sin y} = \int e^{\sin y} \cos y \cdot e^{\sin y} dy + c$

$x e^{\sin y} = \int e^{2\sin y} \cos y dy + c$

Let $\sin y = t$, then $\cos y dy = dt$. The integral becomes:

$\int e^{2t} dt = \dfrac{e^{2t}}{2} = \dfrac{e^{2\sin y}}{2}$

Thus, the general solution is:

$x e^{\sin y} = \dfrac{e^{2\sin y}}{2} + c$

Answer: $xe^{\sin y} = \dfrac{e^{2\sin y}}{2} + c$

</details>

---

### Q12. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y = e^{-mx}$ is a solution of the differential equation $\dfrac{d^2y}{dx^2} + 4\dfrac{dy}{dx} + 3y = 0$, then the values of $m$ are

**Options:**

- **(A)** $1, 3$
- **(B)** $-1, 3$
- **(C)** $-1, -3$
- **(D)** $1, -3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1, 3$**

**Detailed Solution:**

Given $y = e^{-mx}$

Differentiating with respect to $x$, we get:

$\dfrac{dy}{dx} = -m e^{-mx}$

$\dfrac{d^2y}{dx^2} = m^2 e^{-mx}$

Substituting these into the given differential equation $\dfrac{d^2y}{dx^2} + 4\dfrac{dy}{dx} + 3y = 0$:

$m^2 e^{-mx} + 4(-m e^{-mx}) + 3(e^{-mx}) = 0$

$e^{-mx}(m^2 - 4m + 3) = 0$

Since $e^{-mx} \neq 0$ for any finite $x$, we have:

$m^2 - 4m + 3 = 0$

$(m - 1)(m - 3) = 0$

$m = 1, 3$

Answer: $1, 3$

</details>

---

### Q13. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $(1 + t^2) + \left(x - e^{\tan^{-1}t}\right)\dfrac{dt}{dx} = 0$ is

**Options:**

- **(A)** $e^{\tan^{-1}t}$
- **(B)** $-e^{\tan^{-1}t}$
- **(C)** $e^{-\tan^{-1}t}$
- **(D)** $-e^{-\tan^{-1}t}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $e^{\tan^{-1}t}$**

**Detailed Solution:**

The given differential equation is $(1 + t^2) + \left(x - e^{\tan^{-1}t}\right)\dfrac{dt}{dx} = 0$

Rearranging the terms, we get:

$(1 + t^2)\dfrac{dx}{dt} + x - e^{\tan^{-1}t} = 0$

$\dfrac{dx}{dt} + \dfrac{1}{1 + t^2}x = \dfrac{e^{\tan^{-1}t}}{1 + t^2}$

This is a linear differential equation of the form $\dfrac{dx}{dt} + Px = Q$, where $P = \dfrac{1}{1 + t^2}$ and $Q = \dfrac{e^{\tan^{-1}t}}{1 + t^2}$

The integrating factor is given by $e^{\int P dt}$

$IF = e^{\int \dfrac{1}{1 + t^2} dt} = e^{\tan^{-1}t}$

Answer: $e^{\tan^{-1}t}$

</details>

---

### Q14. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $\left(x + 2y^3\right)\dfrac{dy}{dx} - y = 0$ is

**Options:**

- **(A)** $x = (c + y^2)y$, where c is the constant of integration
- **(B)** $y = (c + y^2)x$, where c is the constant of integration
- **(C)** $x = (c + y)y$, where c is the constant of integration
- **(D)** $y = (c + x^2)$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x = (c + y^2)y$, where c is the constant of integration**

**Detailed Solution:**

The given differential equation is $(x + 2y^3)\dfrac{dy}{dx} - y = 0$

Rearranging the terms, we get:

$\dfrac{dx}{dy} = \dfrac{x + 2y^3}{y}$

$\dfrac{dx}{dy} - \dfrac{1}{y}x = 2y^2$

This is a linear differential equation of the form $\dfrac{dx}{dy} + P(y)x = Q(y)$, where $P(y) = -\dfrac{1}{y}$ and $Q(y) = 2y^2$.

The integrating factor (IF) is:

$IF = e^{\int -\dfrac{1}{y} dy} = e^{-\ln y} = \dfrac{1}{y}$

Multiplying the differential equation by the integrating factor and integrating, the solution is given by:

$x \cdot (IF) = \int Q(y) \cdot (IF) dy + c$

$x \left(\dfrac{1}{y}\right) = \int 2y^2 \left(\dfrac{1}{y}\right) dy + c$

$\dfrac{x}{y} = \int 2y dy + c$

$\dfrac{x}{y} = y^2 + c$

$x = y(y^2 + c)$

Answer: $x = (c + y^2)y$, where c is the constant of integration

</details>

---

### Q15. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $x^2 \dfrac{dy}{dx} - xy = 1$ is...

**Options:**

- **(A)** $2xy - 2cx^2 - 1 = 0$
- **(B)** $2xy + 2cx^2 + 1 = 0$
- **(C)** $2xy - 2cx^2 + 1 = 0$
- **(D)** $2x^2 y - 2cx + 1 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2xy - 2cx^2 + 1 = 0$**

**Detailed Solution:**

The given differential equation is $x^2 \dfrac{dy}{dx} - xy = 1$

Dividing by $x^2$, we get:

$\dfrac{dy}{dx} - \dfrac{1}{x}y = \dfrac{1}{x^2}$

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = -\dfrac{1}{x}$ and $Q = \dfrac{1}{x^2}$

Integrating Factor (IF) = $e^{\int P dx} = e^{\int -\dfrac{1}{x} dx} = e^{-\ln x} = \dfrac{1}{x}$

The solution is given by:

$y \cdot (\text{IF}) = \int Q \cdot (\text{IF}) dx + c$

$y \left(\dfrac{1}{x}\right) = \int \dfrac{1}{x^2} \left(\dfrac{1}{x}\right) dx + c$

$\dfrac{y}{x} = \int x^{-3} dx + c$

$\dfrac{y}{x} = \dfrac{x^{-2}}{-2} + c$

$\dfrac{y}{x} = -\dfrac{1}{2x^2} + c$

Multiplying the entire equation by $2x^2$, we get:

$2xy = -1 + 2cx^2$

$2xy - 2cx^2 + 1 = 0$

Answer: $2xy - 2cx^2 + 1 = 0$

</details>

---

### Q16. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $(x+y)\dfrac{dy}{dx} = 1$ is

**Options:**

- **(A)** $x + y + 1 = c$, where $c$ is a constant of integration
- **(B)** $x + y + 1 = ce^y$, where $c$ is a constant of integration
- **(C)** $x + y + 1 = ce^{-y}$, where $c$ is a constant of integration
- **(D)** $x + y - 1 = ce^{-y}$, where $c$ is a constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x + y + 1 = ce^y$, where $c$ is a constant of integration**

**Detailed Solution:**

Given differential equation is $(x+y)\dfrac{dy}{dx} = 1$

Rewriting the equation, we get $\dfrac{dx}{dy} = x + y$

$\dfrac{dx}{dy} - x = y$

This is a linear differential equation of the form $\dfrac{dx}{dy} + Px = Q$, where $P = -1$ and $Q = y$.

Integrating Factor (IF) $= e^{\int P dy} = e^{\int -1 dy} = e^{-y}$

The general solution is given by $x \cdot (\text{IF}) = \int Q \cdot (\text{IF}) dy + c$

$x e^{-y} = \int y e^{-y} dy + c$

Using integration by parts,

$x e^{-y} = y(-e^{-y}) - \int 1 \cdot (-e^{-y}) dy + c$

$x e^{-y} = -y e^{-y} - e^{-y} + c$

Multiplying both sides by $e^y$, we get

$x = -y - 1 + c e^y$

$x + y + 1 = c e^y$

Answer: $x + y + 1 = ce^y$, where $c$ is a constant of integration

</details>

---

### Q17. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $2x\dfrac{dy}{dx} - y = 3$ represents a family of

**Options:**

- **(A)** straight lines
- **(B)** circles
- **(C)** parabola
- **(D)** ellipse

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) parabola**

**Detailed Solution:**

The given differential equation is $2x\dfrac{dy}{dx} - y = 3$

Rearranging the terms, we get:

$2x\dfrac{dy}{dx} = y + 3$

Separating the variables:

$\dfrac{dy}{y + 3} = \dfrac{dx}{2x}$

Integrating both sides:

$\int \dfrac{dy}{y + 3} = \int \dfrac{dx}{2x}$

$\ln(y + 3) = \dfrac{1}{2}\ln x + \ln c$

$\ln(y + 3) = \ln(c\sqrt{x})$

$y + 3 = c\sqrt{x}$

Squaring both sides, we get:

$(y + 3)^2 = c^2 x$

This is an equation of the form $Y^2 = 4aX$, which represents a family of parabolas.

Answer: parabola

</details>

---

### Q18. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation $x\dfrac{dy}{dx} + y = x^3 y^6$, is...

**Options:**

- **(A)** $y^5 = \dfrac{5}{2}x^{-3} + cx^5$
- **(B)** $y^5 = \dfrac{5}{2}x^3 + cx^5$
- **(C)** $\dfrac{1}{y^5} = \dfrac{5}{2}x^{-3} + cx^5$
- **(D)** $\dfrac{1}{y^5} = \dfrac{5}{2}x^3 + cx^5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{y^5} = \dfrac{5}{2}x^3 + cx^5$**

**Detailed Solution:**

The given differential equation is:

$x\dfrac{dy}{dx} + y = x^3 y^6$

Dividing the entire equation by $x y^6$:

$\dfrac{1}{y^6} \dfrac{dy}{dx} + \dfrac{1}{x y^5} = x^2$

Let $v = \dfrac{1}{y^5} = y^{-5}$.

Differentiating with respect to $x$:

$\dfrac{dv}{dx} = -5 y^{-6} \dfrac{dy}{dx} \Rightarrow \dfrac{1}{y^6} \dfrac{dy}{dx} = -\dfrac{1}{5} \dfrac{dv}{dx}$

Substituting this into the differential equation:

$-\dfrac{1}{5} \dfrac{dv}{dx} + \dfrac{1}{x} v = x^2$

$\dfrac{dv}{dx} - \dfrac{5}{x} v = -5 x^2$

This is a linear differential equation of the form $\dfrac{dv}{dx} + P v = Q$, where $P = -\dfrac{5}{x}$ and $Q = -5 x^2$.

The Integrating Factor (IF) is:

$IF = e^{\int -\dfrac{5}{x} dx} = e^{-5 \ln x} = x^{-5}$

The solution is given by:

$v \cdot x^{-5} = \int (-5 x^2) \cdot x^{-5} dx + c$

$v x^{-5} = \int -5 x^{-3} dx + c$

$v x^{-5} = -5 \left( \dfrac{x^{-2}}{-2} \right) + c$

$v x^{-5} = \dfrac{5}{2} x^{-2} + c$

Multiplying both sides by $x^5$:

$v = \dfrac{5}{2} x^3 + c x^5$

Substituting back $v = \dfrac{1}{y^5}$:

$\dfrac{1}{y^5} = \dfrac{5}{2} x^3 + c x^5$

Answer: $\dfrac{1}{y^5} = \dfrac{5}{2}x^3 + cx^5$

</details>

---

### Q19. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integrating factor of the differential equation $x \frac{\mathrm{dy}}{\mathrm{d} x}+\mathrm{y} \log x=x \mathrm{e}^x \cdot x^{\frac{-1}{2}} \log x(x>0)$ is

**Options:**

- **(A)** $(\log x)^x$
- **(B)** $x^{\log x}$
- **(C)** $(\sqrt{x})^{\log x}$
- **(D)** $\mathrm{e}^{\sqrt{x} \log x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\sqrt{x})^{\log x}$**

**Detailed Solution:**

The given differential equation is:

$x \dfrac{\mathrm{dy}}{\mathrm{d} x} + y \log x = x \mathrm{e}^x \cdot x^{\dfrac{-1}{2}} \log x$

Dividing the entire equation by $x$, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} + \left(\dfrac{\log x}{x}\right) y = \mathrm{e}^x \cdot x^{\dfrac{-1}{2}} \log x$

This is a linear differential equation of the form $\dfrac{\mathrm{dy}}{\mathrm{d} x} + P y = Q$, where $P = \dfrac{\log x}{x}$.

The integrating factor (I.F.) is given by $\mathrm{e}^{\int P \mathrm{d} x}$.

$\int P \mathrm{d} x = \int \dfrac{\log x}{x} \mathrm{d} x$

Let $\log x = t \Rightarrow \dfrac{1}{x} \mathrm{d} x = \mathrm{d} t$.

$\int t \mathrm{d} t = \dfrac{t^2}{2} = \dfrac{(\log x)^2}{2}$

Therefore, the integrating factor is:

$\text{I.F.} = \mathrm{e}^{\dfrac{(\log x)^2}{2}} = \mathrm{e}^{\dfrac{1}{2} (\log x) (\log x)}$

Using the property $\mathrm{e}^{a \log x} = x^a$, we can write:

$\text{I.F.} = (\mathrm{e}^{\log x})^{\dfrac{1}{2} \log x} = x^{\dfrac{1}{2} \log x} = (x^{\dfrac{1}{2}})^{\log x} = (\sqrt{x})^{\log x}$

Answer: $(\sqrt{x})^{\log x}$

</details>

---

### Q20. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of the differential equation. $(1+x) \frac{\mathrm{dy}}{\mathrm{d} x}-x \mathrm{y}=1-x$ is

**Options:**

- **(A)** $\mathrm{y}(1+x)=x+\mathrm{ce}^x$, where c is the constant of integration
- **(B)** $\mathrm{y}(1+x)=\mathrm{ce}^x$, where c is the constant of integration
- **(C)** $\mathrm{y}(1-x)=x-\mathrm{ce}^x$, where c is the constant of integration
- **(D)** $\mathrm{y}(1+x)=x~ \mathrm{ce}^{-x}$, where c is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{y}(1+x)=x+\mathrm{ce}^x$, where c is the constant of integration**

**Detailed Solution:**

The given differential equation is:

$(1+x) \dfrac{\mathrm{dy}}{\mathrm{d} x} - x \mathrm{y} = 1-x$

Dividing the entire equation by $(1+x)$, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} - \left(\dfrac{x}{1+x}\right) \mathrm{y} = \dfrac{1-x}{1+x}$

This is a linear differential equation of the form $\dfrac{\mathrm{dy}}{\mathrm{d} x} + P\mathrm{y} = Q$, where $P = -\dfrac{x}{1+x}$ and $Q = \dfrac{1-x}{1+x}$.

The integrating factor (IF) is given by:

$\text{IF} = e^{\int P \mathrm{d} x} = e^{-\int \dfrac{x}{1+x} \mathrm{d} x}$

$\int -\dfrac{x}{1+x} \mathrm{d} x = -\int \dfrac{x+1-1}{1+x} \mathrm{d} x = -\int \left(1 - \dfrac{1}{1+x}\right) \mathrm{d} x = -x + \ln(1+x)$

$\text{IF} = e^{-x + \ln(1+x)} = e^{-x} \cdot e^{\ln(1+x)} = (1+x)e^{-x}$

The general solution is given by:

$\mathrm{y} \cdot \text{IF} = \int Q \cdot \text{IF} \mathrm{d} x + \mathrm{c}$

$\mathrm{y}(1+x)e^{-x} = \int \left(\dfrac{1-x}{1+x}\right) (1+x)e^{-x} \mathrm{d} x + \mathrm{c}$

$\mathrm{y}(1+x)e^{-x} = \int (1-x)e^{-x} \mathrm{d} x + \mathrm{c}$

Using integration by parts on the right side:

$\int (1-x)e^{-x} \mathrm{d} x = (1-x)\int e^{-x} \mathrm{d} x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d} x}(1-x) \int e^{-x} \mathrm{d} x \right) \mathrm{d} x$

$= (1-x)(-e^{-x}) - \int (-1)(-e^{-x}) \mathrm{d} x$

$= (x-1)e^{-x} - \int e^{-x} \mathrm{d} x$

$= (x-1)e^{-x} - (-e^{-x})$

$= x e^{-x} - e^{-x} + e^{-x} = x e^{-x}$

Substituting this back into the equation:

$\mathrm{y}(1+x)e^{-x} = x e^{-x} + \mathrm{c}$

Multiplying both sides by $e^x$, we get:

$\mathrm{y}(1+x) = x + \mathrm{c}e^x$

Answer: $\mathrm{y}(1+x)=x+\mathrm{ce}^x$, where c is the constant of integration

</details>

---

### Q21. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integrating factor of $\mathrm{y}+\frac{\mathrm{d}}{\mathrm{d} x}(x \mathrm{y})=x(\sin x+\log x)$ is

**Options:**

- **(A)** $x$
- **(B)** $\log x^2$
- **(C)** $x^2$
- **(D)** $x^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2$**

**Detailed Solution:**

The given differential equation is:

$\mathrm{y} + \dfrac{\mathrm{d}}{\mathrm{d} x}(x \mathrm{y}) = x(\sin x + \log x)$

Expanding the derivative term, we get:

$\mathrm{y} + \mathrm{y} + x \dfrac{\mathrm{d}\mathrm{y}}{\mathrm{d} x} = x(\sin x + \log x)$

$x \dfrac{\mathrm{d}\mathrm{y}}{\mathrm{d} x} + 2\mathrm{y} = x(\sin x + \log x)$

Dividing the entire equation by $x$, we obtain:

$\dfrac{\mathrm{d}\mathrm{y}}{\mathrm{d} x} + \dfrac{2}{x} \mathrm{y} = \sin x + \log x$

This is a linear differential equation of the form $\dfrac{\mathrm{d}\mathrm{y}}{\mathrm{d} x} + P\mathrm{y} = Q$, where $P = \dfrac{2}{x}$.

The integrating factor (I.F.) is given by:

$\text{I.F.} = e^{\int P \mathrm{d}x}$

$\text{I.F.} = e^{\int \dfrac{2}{x} \mathrm{d}x}$

$\text{I.F.} = e^{2 \log x}$

$\text{I.F.} = e^{\log x^2} = x^2$

Answer: $x^2$

</details>

---

### Q22. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}+\frac{\mathrm{d}}{\mathrm{d} x}(x \mathrm{y})=x(\sin x+\log x)$ then

**Options:**

- **(A)** $\mathrm{y}=\cos x+\frac{2 \sin x}{x}+\frac{2}{x^2} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$,
where $c$ is the constant of integration.
- **(B)** $\mathrm{y}=-\cos x-\frac{2}{x} \sin x+\frac{2}{x^2} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$
where $c$ is the constant of integration.
- **(C)** $\mathrm{y}=-\cos x+\frac{2}{x} \sin x+\frac{2}{x^2} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$,
where c is the constant of integration.
- **(D)** $\mathrm{y}=\cos x-\frac{2}{x} \sin x+\frac{2}{x^3} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$,
where c is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{y}=-\cos x+\frac{2}{x} \sin x+\frac{2}{x^2} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$,
where c is the constant of integration.**

**Detailed Solution:**

The given differential equation is:

$y + \dfrac{d}{dx}(xy) = x(\sin x + \log x)$

Expanding the derivative using the product rule:

$y + x\dfrac{dy}{dx} + y = x(\sin x + \log x)$

$x\dfrac{dy}{dx} + 2y = x(\sin x + \log x)$

Dividing the entire equation by $x$:

$\dfrac{dy}{dx} + \dfrac{2}{x}y = \sin x + \log x$

This is a linear differential equation of the form $\dfrac{dy}{dx} + Py = Q$, where $P = \dfrac{2}{x}$ and $Q = \sin x + \log x$.

The integrating factor (IF) is:

$IF = e^{\int P dx} = e^{\int \dfrac{2}{x} dx} = e^{2\log x} = x^2$

Multiplying the differential equation by the integrating factor:

$x^2 \dfrac{dy}{dx} + 2xy = x^2(\sin x + \log x)$

$\dfrac{d}{dx}(x^2 y) = x^2 \sin x + x^2 \log x$

Integrating both sides with respect to $x$:

$x^2 y = \int x^2 \sin x dx + \int x^2 \log x dx + c$

Using integration by parts for the first integral:

$\int x^2 \sin x dx = x^2(-\cos x) - \int 2x(-\cos x) dx$

$= -x^2 \cos x + 2 \int x \cos x dx$

$= -x^2 \cos x + 2\left(x \sin x - \int \sin x dx\right)$

$= -x^2 \cos x + 2x \sin x + 2\cos x$

Using integration by parts for the second integral:

$\int x^2 \log x dx = (\log x)\left(\dfrac{x^3}{3}\right) - \int \dfrac{1}{x} \left(\dfrac{x^3}{3}\right) dx$

$= \dfrac{x^3}{3} \log x - \int \dfrac{x^2}{3} dx$

$= \dfrac{x^3}{3} \log x - \dfrac{x^3}{9}$

Substituting the integrals back into the equation:

$x^2 y = -x^2 \cos x + 2x \sin x + 2\cos x + \dfrac{x^3}{3} \log x - \dfrac{x^3}{9} + c$

Dividing by $x^2$:

$y = -\cos x + \dfrac{2}{x} \sin x + \dfrac{2}{x^2} \cos x + \dfrac{x}{3} \log x - \dfrac{x}{9} + \dfrac{c}{x^2}$

Answer: $\mathrm{y}=-\cos x+\frac{2}{x} \sin x+\frac{2}{x^2} \cos x+\frac{x}{3} \log x-\frac{x}{9}+\frac{\mathrm{c}}{x^2}$,
where c is the constant of integration.

</details>

---

### Q23. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The equation of the curve passing through the origin and satisfying the equation $\left(1+x^2\right) \frac{\mathrm{dy}}{\mathrm{d} x}+2 x y=4 x^2$, is

**Options:**

- **(A)** $3\left(1+x^2\right) \mathrm{y}=4 x^3$
- **(B)** $3\left(1-x^2\right) \mathrm{y}=4 x^3$
- **(C)** $3\left(1+x^2\right)=x^3$
- **(D)** $4\left(1-x^2\right)=x^3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3\left(1+x^2\right) \mathrm{y}=4 x^3$**

**Detailed Solution:**

The given differential equation is $\left(1+x^2\right) \dfrac{\mathrm{dy}}{\mathrm{d} x}+2 x y=4 x^2$.

Notice that the left hand side is the exact derivative of $y(1+x^2)$ with respect to $x$.

$\dfrac{\mathrm{d}}{\mathrm{d}x} \left[ y(1+x^2) \right] = 4x^2$

Integrating both sides with respect to $x$, we get:

$y(1+x^2) = \int 4x^2 \, \mathrm{d}x$

$y(1+x^2) = \dfrac{4x^3}{3} + C$

Since the curve passes through the origin $(0,0)$, we substitute $x = 0$ and $y = 0$ into the equation:

$0(1+0^2) = \dfrac{4(0)^3}{3} + C$

$C = 0$

Substituting $C = 0$ back into the equation, we get:

$y(1+x^2) = \dfrac{4x^3}{3}$

$3y(1+x^2) = 4x^3$

Answer: $3\left(1+x^2\right) \mathrm{y}=4 x^3$

</details>

---

### Q24. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $\left(1+y^2\right)+\left(x-\mathrm{e}^{\tan ^{-1} y}\right) \frac{\mathrm{dy}}{\mathrm{d} x}=0$ is

**Options:**

- **(A)** $2 x \mathrm{e}^{\tan ^{-1} y}=\mathrm{e}^{2 \tan ^{-1} y}+\mathrm{k}$, where k is the constant of integration
- **(B)** $x \cdot \mathrm{e}^{\tan ^{-1} \mathrm{y}}=\mathrm{e}^{\tan ^{-1} \mathrm{y}}+\mathrm{k}$, where k is the constant of integration
- **(C)** $x \cdot \mathrm{e}^{2 \tan ^{-1} \mathrm{y}}=\mathrm{e}^{\tan ^{-1} \mathrm{y}}+\mathrm{k}$, where k is the constant of integration
- **(D)** $x=2+\mathrm{k} \cdot \mathrm{e}^{-\tan ^{-1} \mathrm{y}} \quad$, where k is the constant of integration

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 x \mathrm{e}^{\tan ^{-1} y}=\mathrm{e}^{2 \tan ^{-1} y}+\mathrm{k}$, where k is the constant of integration**

**Detailed Solution:**

The given differential equation is:

$\left(1+y^2\right)+\left(x-\mathrm{e}^{\tan ^{-1} y}\right) \dfrac{\mathrm{dy}}{\mathrm{d} x}=0$

Rearranging the terms, we get:

$\left(x-\mathrm{e}^{\tan ^{-1} y}\right) \dfrac{\mathrm{dy}}{\mathrm{d} x} = -\left(1+y^2\right)$

$\dfrac{\mathrm{d}x}{\mathrm{d}y} = \dfrac{\mathrm{e}^{\tan ^{-1} y} - x}{1+y^2}$

$\dfrac{\mathrm{d}x}{\mathrm{d}y} + \dfrac{1}{1+y^2} x = \dfrac{\mathrm{e}^{\tan ^{-1} y}}{1+y^2}$

This is a linear differential equation of the form $\dfrac{\mathrm{d}x}{\mathrm{d}y} + P(y)x = Q(y)$, where $P(y) = \dfrac{1}{1+y^2}$ and $Q(y) = \dfrac{\mathrm{e}^{\tan ^{-1} y}}{1+y^2}$.

The integrating factor (IF) is:

$\text{IF} = \mathrm{e}^{\int P(y) \mathrm{d}y} = \mathrm{e}^{\int \dfrac{1}{1+y^2} \mathrm{d}y} = \mathrm{e}^{\tan ^{-1} y}$

The general solution is given by:

$x \cdot (\text{IF}) = \int Q(y) \cdot (\text{IF}) \mathrm{d}y + \mathrm{C}$

$x \cdot \mathrm{e}^{\tan ^{-1} y} = \int \dfrac{\mathrm{e}^{\tan ^{-1} y}}{1+y^2} \cdot \mathrm{e}^{\tan ^{-1} y} \mathrm{d}y + \mathrm{C}$

$x \cdot \mathrm{e}^{\tan ^{-1} y} = \int \dfrac{\mathrm{e}^{2 \tan ^{-1} y}}{1+y^2} \mathrm{d}y + \mathrm{C}$

Let $t = \tan ^{-1} y$, then $\mathrm{d}t = \dfrac{1}{1+y^2} \mathrm{d}y$. The integral becomes:

$\int \mathrm{e}^{2t} \mathrm{d}t = \dfrac{1}{2} \mathrm{e}^{2t} = \dfrac{1}{2} \mathrm{e}^{2 \tan ^{-1} y}$

Substituting this back into the solution:

$x \cdot \mathrm{e}^{\tan ^{-1} y} = \dfrac{1}{2} \mathrm{e}^{2 \tan ^{-1} y} + \mathrm{C}$

Multiplying the entire equation by $2$:

$2x \mathrm{e}^{\tan ^{-1} y} = \mathrm{e}^{2 \tan ^{-1} y} + 2\mathrm{C}$

Let $2\mathrm{C} = \mathrm{k}$, where $\mathrm{k}$ is the constant of integration:

$2x \mathrm{e}^{\tan ^{-1} y} = \mathrm{e}^{2 \tan ^{-1} y} + \mathrm{k}$

Answer: $2 x \mathrm{e}^{\tan ^{-1} y}=\mathrm{e}^{2 \tan ^{-1} y}+\mathrm{k}$, where k is the constant of integration

</details>

---

### Q25. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of
$x(x-1) \frac{\mathrm{dy}}{\mathrm{d} x}=x^3(2 x-1)+(x-2) \mathrm{y}$ is

**Options:**

- **(A)** $y(x-1)=x^3+c(x-1)$, where $c$ is the constant of integration.
- **(B)** $\mathrm{y}=x^3(x-1)+\mathrm{c}, \quad$ where c is the constant of integration.
- **(C)** $y(x-1)=x^3(x-1)+c x^2$, where $c$ is the constant of integration.
- **(D)** $y(x-1)=x^3(x-1)+c, \quad$ where $c$ is the constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $y(x-1)=x^3(x-1)+c x^2$, where $c$ is the constant of integration.**

**Detailed Solution:**

The given differential equation is:

$x(x-1) \dfrac{\mathrm{dy}}{\mathrm{d} x} - (x-2) \mathrm{y} = x^3(2 x-1)$

Dividing the entire equation by $x(x-1)$, we get:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} - \dfrac{x-2}{x(x-1)} \mathrm{y} = \dfrac{x^2(2 x-1)}{x-1}$

This is a linear differential equation of the form $\dfrac{\mathrm{dy}}{\mathrm{d} x} + P \mathrm{y} = Q$, where:

$P = -\dfrac{x-2}{x(x-1)}$ and $Q = \dfrac{x^2(2 x-1)}{x-1}$

Using partial fractions for $P$:

$\dfrac{x-2}{x(x-1)} = \dfrac{2}{x} - \dfrac{1}{x-1}$

$\Rightarrow P = \dfrac{1}{x-1} - \dfrac{2}{x}$

The integrating factor (IF) is:

$\text{IF} = e^{\int P \mathrm{d} x} = e^{\int \left(\dfrac{1}{x-1} - \dfrac{2}{x}\right) \mathrm{d} x}$

$\text{IF} = e^{\ln(x-1) - 2\ln x} = e^{\ln\left(\dfrac{x-1}{x^2}\right)} = \dfrac{x-1}{x^2}$

The general solution is given by:

$y \cdot \text{IF} = \int Q \cdot \text{IF} \mathrm{d} x + c$

$y \left(\dfrac{x-1}{x^2}\right) = \int \dfrac{x^2(2 x-1)}{x-1} \cdot \dfrac{x-1}{x^2} \mathrm{d} x + c$

$y \left(\dfrac{x-1}{x^2}\right) = \int (2 x-1) \mathrm{d} x + c$

$y \left(\dfrac{x-1}{x^2}\right) = x^2 - x + c$

$y \left(\dfrac{x-1}{x^2}\right) = x(x-1) + c$

Multiplying both sides by $x^2$, we get:

$y(x-1) = x^3(x-1) + c x^2$

Answer: $y(x-1)=x^3(x-1)+c x^2$, where $c$ is the constant of integration.

</details>

---

### Q26. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The general solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}=y \tan x-y^2 \sec x$ is

**Options:**

- **(A)** $\tan x=(\mathrm{c}+\sec x) y$, where c is constant of integration.
- **(B)** $\sec y=(\mathrm{c}+\tan y) x$, where c is constant of integration.
- **(C)** $\sec x=(\mathrm{c}+\tan x) y$, where c is constant of integration.
- **(D)** $\cos y=(\mathrm{c}+\tan y)$, where c is constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\sec x=(\mathrm{c}+\tan x) y$, where c is constant of integration.**

**Detailed Solution:**

The given differential equation is $\dfrac{\mathrm{d} y}{\mathrm{d} x} - y \tan x = -y^2 \sec x$

Dividing the entire equation by $y^2$, we get:

$\dfrac{1}{y^2} \dfrac{\mathrm{d} y}{\mathrm{d} x} - \dfrac{1}{y} \tan x = -\sec x$

Let $\dfrac{1}{y} = t$, then differentiating with respect to $x$ gives $-\dfrac{1}{y^2} \dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{\mathrm{d} t}{\mathrm{d} x}$

Substituting this into the equation, we get:

$-\dfrac{\mathrm{d} t}{\mathrm{d} x} - t \tan x = -\sec x$

$\dfrac{\mathrm{d} t}{\mathrm{d} x} + t \tan x = \sec x$

This is a linear differential equation of the form $\dfrac{\mathrm{d} t}{\mathrm{d} x} + P t = Q$, where $P = \tan x$ and $Q = \sec x$.

Integrating Factor (IF) $= e^{\int P \mathrm{d} x} = e^{\int \tan x \mathrm{d} x} = e^{\ln(\sec x)} = \sec x$

The general solution is given by:

$t \times \text{IF} = \int (Q \times \text{IF}) \mathrm{d} x + \mathrm{c}$

$t \sec x = \int \sec x \cdot \sec x \mathrm{d} x + \mathrm{c}$

$t \sec x = \int \sec^2 x \mathrm{d} x + \mathrm{c}$

$t \sec x = \tan x + \mathrm{c}$

Substituting back $t = \dfrac{1}{y}$, we get:

$\dfrac{1}{y} \sec x = \tan x + \mathrm{c}$

$\sec x = (\mathrm{c} + \tan x) y$

Answer: $\sec x=(\mathrm{c}+\tan x) y$, where c is constant of integration.

</details>

---

### Q27. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation of $y=\mathrm{e}^x\left(\mathrm{a}+\mathrm{b} x+x^2\right)$ is

**Options:**

- **(A)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+2 \frac{\mathrm{~d} y}{\mathrm{~d} x}-2 y=0$
- **(B)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{~d} y}{\mathrm{~d} x}+y=0$
- **(C)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{~d} y}{\mathrm{~d} x}-2 \mathrm{e}^x+y=0$
- **(D)** $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}+2 \frac{\mathrm{~d} y}{\mathrm{~d} x}-\mathrm{e}^x+2 y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{~d} y}{\mathrm{~d} x}-2 \mathrm{e}^x+y=0$**

**Detailed Solution:**

The given equation is $y = \mathrm{e}^x(a + bx + x^2)$

Multiplying both sides by $\mathrm{e}^{-x}$:

$y \mathrm{e}^{-x} = a + bx + x^2$

Differentiating with respect to $x$:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} \mathrm{e}^{-x} - y \mathrm{e}^{-x} = b + 2x$

$\left( \dfrac{\mathrm{d}y}{\mathrm{d}x} - y \right) \mathrm{e}^{-x} = b + 2x$

Differentiating again with respect to $x$:

$\left( \dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} - \dfrac{\mathrm{d}y}{\mathrm{d}x} \right) \mathrm{e}^{-x} - \left( \dfrac{\mathrm{d}y}{\mathrm{d}x} - y \right) \mathrm{e}^{-x} = 2$

$\left( \dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} - 2\dfrac{\mathrm{d}y}{\mathrm{d}x} + y \right) \mathrm{e}^{-x} = 2$

$\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} - 2\dfrac{\mathrm{d}y}{\mathrm{d}x} + y = 2\mathrm{e}^x$

$\dfrac{\mathrm{d}^2y}{\mathrm{d}x^2} - 2\dfrac{\mathrm{d}y}{\mathrm{d}x} - 2\mathrm{e}^x + y = 0$

Answer: $\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}-2 \frac{\mathrm{~d} y}{\mathrm{~d} x}-2 \mathrm{e}^x+y=0$

</details>

---

### Q28. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $y=y(x)$ be the solution of the differential equation $x \frac{\mathrm{~d} y}{\mathrm{~d} x}+y=x \log x,(x\gt1)$
If $2(y(2))=\log 4-1$ then the value of $y(\mathrm{e})$ is

**Options:**

- **(A)** $\frac{\mathrm{e}^2}{4}$
- **(B)** $\frac{-\mathrm{e}^2}{2}$
- **(C)** $\frac{-\mathrm{e}}{2}$
- **(D)** $\frac{\mathrm{e}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{e}}{4}$**

**Detailed Solution:**

The given differential equation is $x \dfrac{\mathrm{d} y}{\mathrm{d} x} + y = x \log x$.

This can be rewritten as:

$\dfrac{\mathrm{d}}{\mathrm{d} x} (x y) = x \log x$

Integrating both sides with respect to $x$, we get:

$x y = \int x \log x \mathrm{d} x + C$

Using integration by parts:

$x y = \log x \int x \mathrm{d} x - \int \left( \dfrac{\mathrm{d}}{\mathrm{d} x} (\log x) \int x \mathrm{d} x \right) \mathrm{d} x$

$x y = \dfrac{x^2}{2} \log x - \int \dfrac{1}{x} \left( \dfrac{x^2}{2} \right) \mathrm{d} x$

$x y = \dfrac{x^2}{2} \log x - \dfrac{x^2}{4} + C$

We are given that $2 y(2) = \log 4 - 1$. Substituting $x = 2$ into the equation:

$2 y(2) = \dfrac{2^2}{2} \log 2 - \dfrac{2^2}{4} + C$

$2 y(2) = 2 \log 2 - 1 + C$

$2 y(2) = \log 4 - 1 + C$

Since $2 y(2) = \log 4 - 1$, we have $C = 0$.

The particular solution is:

$x y = \dfrac{x^2}{2} \log x - \dfrac{x^2}{4}$

To find $y(\mathrm{e})$, substitute $x = \mathrm{e}$:

$\mathrm{e} y(\mathrm{e}) = \dfrac{\mathrm{e}^2}{2} \log \mathrm{e} - \dfrac{\mathrm{e}^2}{4}$

Since $\log \mathrm{e} = 1$:

$\mathrm{e} y(\mathrm{e}) = \dfrac{\mathrm{e}^2}{2} - \dfrac{\mathrm{e}^2}{4} = \dfrac{\mathrm{e}^2}{4}$

$y(\mathrm{e}) = \dfrac{\mathrm{e}}{4}$

Answer: $\frac{\mathrm{e}}{4}$

</details>

---

### Q29. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\cos x \dfrac{\mathrm{~d} y}{\mathrm{~d} x}-y \sin x=6 x, 0 \lt x \lt \dfrac{\pi}{2}$, then general solution of the differential equation is

**Options:**

- **(A)** $y=\cos x+3 x^2+\mathrm{c}$, where c is a constant of integration.
- **(B)** $y+\cos x=3 x^2+\mathrm{c}$, where c is a constant of integration.
- **(C)** $y=3 x^2 \cos x+\cos x$, where c is a constant of integration.
- **(D)** $y \cdot \cos x=3 x^2+\mathrm{c}$, where c is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y \cdot \cos x=3 x^2+\mathrm{c}$, where c is a constant of integration.**

**Detailed Solution:**

Given differential equation is $\cos x \dfrac{\mathrm{d} y}{\mathrm{d} x} - y \sin x = 6 x$

This can be written as $\dfrac{\mathrm{d}}{\mathrm{d} x}(y \cos x) = 6 x$

Integrating both sides with respect to $x$, we get

$\int \dfrac{\mathrm{d}}{\mathrm{d} x}(y \cos x) \mathrm{d} x = \int 6 x \mathrm{d} x$

$y \cdot \cos x = 3 x^2 + \mathrm{c}$

where $\mathrm{c}$ is a constant of integration.

Answer: $y \cdot \cos x=3 x^2+\mathrm{c}$, where c is a constant of integration.

</details>

---

### Q30. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Integrating factor of the differential equation $\dfrac{\mathrm{d} y}{\mathrm{~d} x}+y=\dfrac{1+y}{x}$ is

**Options:**

- **(A)** $\dfrac{x}{\mathrm{e}^x}$
- **(B)** $x e^x$
- **(C)** $\mathrm{e}^x$
- **(D)** $\dfrac{\mathrm{e}^x}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\mathrm{e}^x}{x}$**

**Detailed Solution:**

The given differential equation is:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} + y = \dfrac{1+y}{x}$

Rearranging the terms, we get:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} + y - \dfrac{y}{x} = \dfrac{1}{x}$

$\dfrac{\mathrm{d} y}{\mathrm{d} x} + \left(1 - \dfrac{1}{x}\right)y = \dfrac{1}{x}$

This is a linear differential equation of the form $\dfrac{\mathrm{d} y}{\mathrm{d} x} + P y = Q$, where $P = 1 - \dfrac{1}{x}$ and $Q = \dfrac{1}{x}$.

The integrating factor (I.F.) is given by $\mathrm{e}^{\int P \mathrm{d} x}$.

$\text{I.F.} = \mathrm{e}^{\int \left(1 - \dfrac{1}{x}\right) \mathrm{d} x}$

$\text{I.F.} = \mathrm{e}^{x - \ln x}$

$\text{I.F.} = \mathrm{e}^x \cdot \mathrm{e}^{-\ln x}$

$\text{I.F.} = \mathrm{e}^x \cdot \dfrac{1}{x} = \dfrac{\mathrm{e}^x}{x}$

Answer: $\dfrac{\mathrm{e}^x}{x}$

</details>

---

### Q31. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The curve satisfying the differential equation $y \mathrm{~d} x-\left(x+3 y^2\right) \mathrm{dy}=0$ and passing through the point $(1,1)$ also passes through the point

**Options:**

- **(A)** $\left(\dfrac{1}{4}, \dfrac{1}{2}\right)$
- **(B)** $\left(\dfrac{1}{4},-\dfrac{1}{2}\right)$
- **(C)** $\left(\dfrac{1}{3},-\dfrac{1}{3}\right)$
- **(D)** $\left(-\dfrac{1}{3}, \dfrac{1}{3}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(-\dfrac{1}{3}, \dfrac{1}{3}\right)$**

**Detailed Solution:**

The given differential equation is $y \mathrm{d}x - (x + 3y^2) \mathrm{dy} = 0$

Rearranging the terms, we get $y \mathrm{d}x - x \mathrm{dy} = 3y^2 \mathrm{dy}$

Dividing both sides by $y^2$, we get $\dfrac{y \mathrm{d}x - x \mathrm{dy}}{y^2} = 3 \mathrm{dy}$

This can be written as $\mathrm{d}\left(\dfrac{x}{y}\right) = 3 \mathrm{dy}$

Integrating both sides, we get $\dfrac{x}{y} = 3y + C$

Since the curve passes through $(1, 1)$, substituting $x = 1$ and $y = 1$ gives $1 = 3 + C \Rightarrow C = -2$

The equation of the curve is $x = 3y^2 - 2y$

Checking the given options, for $y = \dfrac{1}{3}$, we get $x = 3\left(\dfrac{1}{3}\right)^2 - 2\left(\dfrac{1}{3}\right) = \dfrac{1}{3} - \dfrac{2}{3} = -\dfrac{1}{3}$

Thus, the curve passes through $\left(-\dfrac{1}{3}, \dfrac{1}{3}\right)$.

Answer: $\left(-\dfrac{1}{3}, \dfrac{1}{3}\right)$

</details>

---

### Q32. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y=y(x)$ is the solution of the differential equation $x \dfrac{\mathrm{dy}}{\mathrm{d} x}+2 y=x^2$ satisfying $y(1)=1$, then the value of $y\left(\dfrac{1}{2}\right)$ is

**Options:**

- **(A)** $\dfrac{7}{64}$
- **(B)** $\dfrac{1}{4}$
- **(C)** $\dfrac{13}{6}$
- **(D)** $\dfrac{49}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{49}{16}$**

**Detailed Solution:**

The given differential equation is $x \dfrac{\mathrm{dy}}{\mathrm{d} x}+2 y=x^2$

Dividing by $x$, we get $\dfrac{\mathrm{dy}}{\mathrm{d} x}+\dfrac{2}{x} y=x$

This is a linear differential equation of the form $\dfrac{\mathrm{dy}}{\mathrm{d} x} + P y = Q$. The integrating factor is $IF = e^{\int \dfrac{2}{x} \mathrm{d} x} = e^{2 \ln x} = x^2$

Multiplying the equation by the integrating factor, we get $\dfrac{\mathrm{d}}{\mathrm{d} x}(y x^2) = x^3$

Integrating both sides with respect to $x$, we get $y x^2 = \dfrac{x^4}{4} + C$

Given $y(1)=1$, substituting $x=1$ and $y=1$ gives $1 = \dfrac{1}{4} + C \Rightarrow C = \dfrac{3}{4}$

The solution to the differential equation is $y x^2 = \dfrac{x^4}{4} + \dfrac{3}{4}$

Substituting $x = \dfrac{1}{2}$, we get $y\left(\dfrac{1}{2}\right) \left(\dfrac{1}{4}\right) = \dfrac{1}{64} + \dfrac{3}{4}$

$y\left(\dfrac{1}{2}\right) \left(\dfrac{1}{4}\right) = \dfrac{49}{64}$

$y\left(\dfrac{1}{2}\right) = \dfrac{49}{16}$

Answer: $\dfrac{49}{16}$

</details>

---

### Q33. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $y=y(x)$ be the solution of the differential equation $\sin x \dfrac{\mathrm{~d} y}{\mathrm{~d} x}+y \cos x=4 x, x \in(0, \pi)$.
If $y\left(\dfrac{\pi}{2}\right)=0$, then $y\left(\dfrac{\pi}{6}\right)$ is equal to

**Options:**

- **(A)** $-\dfrac{4}{9} \pi^2$
- **(B)** $\dfrac{4}{9 \sqrt{3}} \pi^2$
- **(C)** $\dfrac{-8}{9 \sqrt{3}} \pi^2$
- **(D)** $-\dfrac{8}{9} \pi^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{8}{9} \pi^2$**

**Detailed Solution:**

The given differential equation is $\sin x \dfrac{\mathrm{d} y}{\mathrm{d} x} + y \cos x = 4x$.

This can be rewritten as $\dfrac{\mathrm{d}}{\mathrm{d} x} (y \sin x) = 4x$.

Integrating both sides with respect to $x$, we get:

$\int \dfrac{\mathrm{d}}{\mathrm{d} x} (y \sin x) \mathrm{d} x = \int 4x \, \mathrm{d} x$

$y \sin x = 2x^2 + C$

Given $y\left(\dfrac{\pi}{2}\right) = 0$, substituting $x = \dfrac{\pi}{2}$ and $y = 0$:

$0 \cdot \sin\left(\dfrac{\pi}{2}\right) = 2\left(\dfrac{\pi}{2}\right)^2 + C$

$0 = \dfrac{\pi^2}{2} + C \Rightarrow C = -\dfrac{\pi^2}{2}$

Thus, the solution is $y \sin x = 2x^2 - \dfrac{\pi^2}{2}$.

To find $y\left(\dfrac{\pi}{6}\right)$, substitute $x = \dfrac{\pi}{6}$:

$y\left(\dfrac{\pi}{6}\right) \sin\left(\dfrac{\pi}{6}\right) = 2\left(\dfrac{\pi}{6}\right)^2 - \dfrac{\pi^2}{2}$

$y\left(\dfrac{\pi}{6}\right) \cdot \dfrac{1}{2} = 2\left(\dfrac{\pi^2}{36}\right) - \dfrac{\pi^2}{2}$

$y\left(\dfrac{\pi}{6}\right) \cdot \dfrac{1}{2} = \dfrac{\pi^2}{18} - \dfrac{\pi^2}{2}$

$y\left(\dfrac{\pi}{6}\right) \cdot \dfrac{1}{2} = \dfrac{\pi^2 - 9\pi^2}{18} = -\dfrac{8\pi^2}{18} = -\dfrac{4\pi^2}{9}$

$y\left(\dfrac{\pi}{6}\right) = -\dfrac{8}{9}\pi^2$

Answer: $-\dfrac{8}{9} \pi^2$

</details>

---

### Q34. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x \mathrm{~d} y=y(\mathrm{~d} x+y \mathrm{~d} y), y(1)=1, y(x)>0$, then $y(-3)$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

$x \mathrm{~d} y=y(\mathrm{~d} x+y \mathrm{~d} y)$
$\Rightarrow y \mathrm{~d} x=\left(x-y^2\right) \mathrm{d} y \Rightarrow \frac{\mathrm{d} x}{\mathrm{~d} y}+\left(-\frac{1}{y}\right) x=-y$
$\therefore \quad$ I.F. $=\mathrm{e}^{\int-\frac{1}{d y} y^y}=\mathrm{e}^{-\log y}=\frac{1}{y}$
$\therefore \quad$ Solution of the given equation is
$x \cdot \frac{1}{y}=\int-y \cdot \frac{1}{y} \mathrm{~d} y+\mathrm{c}$
$\Rightarrow \frac{x}{y}=-y+\mathrm{c}$                ....(i)      
Since $y(1)=1$, i.e., $y=1$ when $x=1$
$\therefore \quad 1=-1+c \Rightarrow c=2$
$\therefore \quad \frac{x}{y}=-y+2 \quad \ldots[$ From (i) $]$
Putting $x=-3$, we get
$-\frac{3}{y}=-y+2$
$\begin{aligned} & \Rightarrow y^2-2 y-3=0 \\ & \Rightarrow(y-3)(y+1)=0\end{aligned}$
Since $y(x)>0, y=3$

</details>

---

### Q35. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}+\frac{y}{x}=\sin x$ is

**Options:**

- **(A)** $x y+\cos x=\sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $x(y+\cos x)=\sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $y(x+\cos x)=\sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $x y+\sin x=\cos x+c$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x(y+\cos x)=\sin x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

For given linear differential equation,
$\text { I.F. }=\mathrm{e}^{\int \frac{1}{x} d x}=\mathrm{e}^{\log x}=x$
$\therefore \quad$ The required solution is
$y x=\int x \sin x \frac{\mathrm{d} y}{\mathrm{~d} x}$
$\begin{aligned} & \therefore \quad y x=-x \cos x+\int \cos x \mathrm{~d} x \\ & \therefore \quad y x=-x \cos x+\sin x+\mathrm{c} \\ & \therefore \quad x(y+\cos x)=\sin x+\mathrm{c}\end{aligned}$

</details>

---

### Q36. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The solution of $\frac{\mathrm{d} x}{\mathrm{~d} y}+\frac{x}{y}=x^2$ is

**Options:**

- **(A)** $\frac{1}{y}=\mathrm{c} x-x \log x$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $\frac{1}{x}=\mathrm{c} y-y \log y$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $\frac{1}{x}=\mathrm{c} x-x \log y$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $\frac{1}{y}=\mathrm{c} x-y \log x$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{x}=\mathrm{c} y-y \log y$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

$\frac{\mathrm{d} x}{\mathrm{~d} y}+\frac{x}{y}=x^2$
$\therefore \quad \frac{1}{x^2} \frac{\mathrm{d} x}{\mathrm{~d} y}+\frac{1}{x y}=1.. (i)$
Let $\frac{1}{x}=\mathrm{t}$
Differentiating w.r.t. $y$, we get
$\begin{array}{ll} 
& \frac{-1}{x^2} \frac{\mathrm{d} x}{\mathrm{~d} y}=\frac{\mathrm{dt}}{\mathrm{d} y} \Rightarrow \frac{1}{x^2} \frac{\mathrm{d} x}{\mathrm{~d} y}=\frac{-\mathrm{dt}}{\mathrm{d} y} \\
\therefore \quad & \text { (i) } \Rightarrow \frac{-\mathrm{dt}}{\mathrm{d} y}+\frac{\mathrm{t}}{y}=1 \\
\therefore \quad & \frac{\mathrm{dt}}{\mathrm{d} y}-\frac{\mathrm{t}}{y}=-1 \\
\therefore & \text { I.F. }=\mathrm{e}^{\int \frac{-1}{y} \mathrm{~d}}=\mathrm{e}^{\log \left(\frac{1}{y}\right)}=\frac{1}{y}
\end{array}$
$\therefore \quad$ The solution of the given equation is
$\begin{aligned}
\mathrm{t}(\mathrm{I} . \mathrm{F}) & =\int(-1)(\text { I.F. }) \mathrm{d} y+\mathrm{c} \\
\mathrm{t}\left(\frac{1}{y}\right) & =\int \frac{-1}{y} \mathrm{~d} y+\mathrm{c} \\
\therefore \quad \frac{\mathrm{t}}{y} & =-\log y+\mathrm{c} \\
\therefore \quad \frac{1}{x y} & =-\log y+\mathrm{c} \\
\therefore \quad \frac{1}{x} & =\mathrm{c} y-y \log y
\end{aligned}$

</details>

---

### Q37. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\frac{\mathrm{d} y}{\mathrm{~d} x}+\left(\frac{3 x^2}{1+x^3}\right) y=\frac{1}{x^3+1}$ is

**Options:**

- **(A)** $y\left(1+x^3\right)=x^3+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(B)** $y\left(1+x^3\right)=x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(C)** $y\left(1+x^3\right)=x^2+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.
- **(D)** $y\left(1+x^3\right)=2 x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $y\left(1+x^3\right)=x+\mathrm{c}$, where $\mathrm{c}$ is a constant of integration.**

**Detailed Solution:**

Given differential equation is
$\begin{array}{ll} 
& \frac{\mathrm{d} y}{\mathrm{~d} x}+\left(\frac{3 x^2}{1+x^3}\right) y=\frac{1}{x^3+1} \\
& \text { Here, } \mathrm{P}=\frac{3 x^2}{1+x^3}, \mathrm{Q}=\frac{1}{x^3+1} \\
\therefore \quad & \text { I.F. }=\mathrm{e}^{\int \frac{3 x^2}{1+x^3} \mathrm{~d} x}=\mathrm{e}^{\log \left(1+x^3\right)}=\left(1+x^3\right) \\
\therefore \quad & \text { Solution of the given equation is } \\
& y\left(1+x^3\right)=\int \frac{1}{1+x^3} \cdot\left(1+x^3\right) \mathrm{d} x+\mathrm{c} \\
& \Rightarrow y\left(1+x^3\right)=x+\mathrm{c}
\end{array}$

</details>

---

### Q38. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\left(x^2+y^2\right) \mathrm{d} y=x y \mathrm{~d} x$, with $y\left(x_0\right)=e, y(1)=1$, then $x_0$ has the value

**Options:**

- **(A)** $\sqrt{3} e$
- **(B)** $\sqrt{3} e$
- **(C)** $e$
- **(D)** $\sqrt{3} e^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{3} e$**

**Detailed Solution:**

$\begin{aligned}
& \left.\left(x^2+y^2\right) \mathrm{d} y=x y \mathrm{~d} x \quad \text { [Let } y=v x\right] \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x y}{x^2+y^2} \\
& \Rightarrow v+x \frac{\mathrm{d} v}{\mathrm{~d} x}=\frac{v}{1+v} \\
& \Rightarrow-\int \frac{1+v^2}{v^3} \mathrm{~d} v=\int \frac{\mathrm{d} x}{x} \\
& \Rightarrow \frac{1}{2 v^2}-\log v=\log x+\log c \\
& \Rightarrow c y=e^{\frac{x^2}{2 y^2}}
\end{aligned}$
[Let $y=v x$ ]
Putting $x=1$ and $y=1$ we get $c=e^{-\frac{1}{2}}$
$\Rightarrow y=e^{\frac{x^2-y^2}{2 y^2}}$, now putting $x=x_0$ and $y=e$ we get $x_0=\sqrt{3} e$

</details>

---

### Q39. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation $\frac{d y}{d x}-e^x=y e^x$, when $x=0$ and $y=1$ is

**Options:**

- **(A)** $\log \left(\frac{y+1}{2}\right)=\frac{e^x}{2}-\frac{1}{2}$
- **(B)** $\log \left(\frac{y+1}{2}\right)=e^x-1$
- **(C)** $\log (y-1)=e^x-1$
- **(D)** $\log 2(y-1)=e^x-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log \left(\frac{y+1}{2}\right)=e^x-1$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}-e^x=y e^x \Rightarrow \frac{d y}{d x}=(y+1) e^x \Rightarrow \int \frac{d y}{y+1}=\int e^x d x \\ & \Rightarrow \log (y+1)=e^x+c \\ & \text { for } x=0, y=1 \Rightarrow c=\log 2-1 \\ & \text { Hence, } \log (y+1)=e^x+\log 2-1 \\ & \Rightarrow \log (y+1)-\log 2=e^x-1 \\ & \Rightarrow \log \left(\frac{y+1}{2}\right)=e^x-1\end{aligned}$

</details>

---

### Q40. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of $\left(x \frac{d y}{d x}-y\right) \sin \frac{y}{x}=x^3 e^x$ is

**Options:**

- **(A)** $\mathrm{e}^{\mathrm{x}}(\mathrm{x}-1)+\cos \frac{\mathrm{y}}{\mathrm{x}}+\mathrm{c}=0$
- **(B)** $\mathrm{xe}^{\mathrm{x}}+\cos \frac{\mathrm{y}}{\mathrm{x}}+\mathrm{c}=0$
- **(C)** $\mathrm{e}^{\mathrm{x}}(\mathrm{x}+1)+\cos \frac{\mathrm{y}}{\mathrm{x}}+\mathrm{c}=0$
- **(D)** $\mathrm{ex}^{\mathrm{x}}-\cos \frac{\mathrm{y}}{\mathrm{x}}+\mathrm{c}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{\mathrm{x}}(\mathrm{x}-1)+\cos \frac{\mathrm{y}}{\mathrm{x}}+\mathrm{c}=0$**

**Detailed Solution:**

$$
\begin{aligned}
& \left(x \frac{d y}{d x}-y\right) \sin \frac{y}{x}=x^3 e^x \\
& \text { Put } \frac{y}{x}=t \Rightarrow \frac{x \frac{d y}{d x}-y}{x^2}=\frac{d t}{d x}
\end{aligned}
$$
Put $\frac{y}{x}=t \Rightarrow \frac{x \frac{d y}{d x}-y}{x^2}=\frac{d t}{d x}$
Hence eq. (i) becomes
$$
\begin{aligned}
& \mathrm{x}^2\left(\frac{d t}{d x}\right) \sin t=x^3 e^x \Rightarrow\left(\frac{d t}{d x}\right) \sin t=x e^x \\
& \therefore \int \sin t d t=\int x^x d x \\
& \therefore-\cos t=x e^x-\int e^x d x=x e^4-e^x+c \\
& \therefore-\cos \left(\frac{y}{x}\right)=e^x(x-1)+c
\end{aligned}
$$

</details>

---

### Q41. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $\frac{d y}{d x}(x \log x)+y=4 \log x$ is

**Options:**

- **(A)** $\log (\log x)$
- **(B)** $x$
- **(C)** $e^{x}$
- **(D)** $\log x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\log x$**

**Detailed Solution:**

We have $\frac{d y}{d x}(x \log x)+y \quad=4 \log x$
$\therefore \frac{d y}{d x}+\left(\frac{1}{x \log x}\right) y=\frac{4}{x}$
$\therefore$ I.F. $=e^{\int \frac{d x}{x \log x}}=e^{\log (\log x)}=\log x$

</details>

---

### Q42. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation y $\log _{y}\left(\frac{\mathrm{d} x}{\mathrm{dy}}\right)+x-\log \mathrm{y}=0$
is

**Options:**

- **(A)** $\log (\log y)$
- **(B)** $\log y$
- **(C)** $y$
- **(D)** $e^{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log y$**

**Detailed Solution:**

We have $y \log y\left(\frac{d x}{d y}\right)+x=\log y$
$\therefore \frac{\mathrm{dx}}{\mathrm{dy}}+\frac{\mathrm{x}}{\mathrm{y} \log \mathrm{y}}=\frac{1}{\mathrm{y}}$
$\therefore$ I.F. $=e^{\int \frac{1}{y \log y} d y}=e^{\log (\log y)}=\log y$

</details>

---

### Q43. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integrating factor of the differential equation $x \frac{d y}{d x}+y \log x=x^{2}$ is

**Options:**

- **(A)** $(\log x)^{x}$
- **(B)** $x^{\log x}$
- **(C)** $(\log x)^{2}$
- **(D)** $x^{\log (\sqrt{x})}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $x^{\log (\sqrt{x})}$**

**Detailed Solution:**

(D)
We have $x \frac{d y}{d x}+y \log x=x^{2}$
$\begin{array}{l}
\therefore \frac{\mathrm{dy}}{\mathrm{dx}}+\left(\frac{\log \mathrm{x}}{\mathrm{x}}\right) \mathrm{y}=\mathrm{x} \\
\therefore \text { I.F. }=\mathrm{e}^{\int \frac{\log \mathrm{x}}{\mathrm{x}} \mathrm{dx}}=\mathrm{e}^{\frac{1}{2}(\log \mathrm{x})^{2}}
\end{array}$

</details>

---

### Q44. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The integrating factor of differential equation $\left(1+y+x^{2} y\right) d x+\left(x+x^{3}\right) d y=0$ is

**Options:**

- **(A)** $\frac{1}{x}$
- **(B)** $x$
- **(C)** $\log x$
- **(D)** $e^{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x$**

**Detailed Solution:**

(A)
We have $\left(1+y+x^{2} y\right) d x+\left(x+x^{3}\right) d y=0$
$\therefore \frac{d y}{d x}=\frac{-\left(1+y+x^{2} y\right)}{x\left(1+x^{2}\right)}=\frac{-\left[1+y\left(1+x^{2}\right)\right]}{x\left(1+x^{2}\right)}$
$\therefore \frac{d y}{d x}=\frac{-1}{x\left(1+x^{2}\right)}-\frac{y\left(1+x^{2}\right)}{x\left(1+x^{2}\right)}$
$\therefore \frac{d y}{d x}+\left(\frac{1}{x}\right) y=\frac{-1}{x\left(1+x^{2}\right)}$
$\therefore$ I.F. $=e^{\int \frac{1}{x} d x}=e^{\log x}=x$

</details>

---

### Q45. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The integrating factor of the differential equation siny $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)=\operatorname{cosy}(1-x \cos y)$ is

**Options:**

- **(A)** $\mathrm{e}^{-x}$
- **(B)** $\mathrm{e}^{-\cos y}$
- **(C)** $\mathrm{e}^{-y}$
- **(D)** $\mathrm{e}^{\text {siny }}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{e}^{-x}$**

**Detailed Solution:**

(A)
$\sin y \frac{d y}{d x}=\cos y(1-x \cos y) \Rightarrow \sin y \frac{d y}{d x}=\cos y-x \cos ^{2} y$
Dividing both sides by $\cos ^{2} y$, we get
$\sec y \tan y \frac{d y}{d x}=\sec y-x$
$\sec y \cdot \tan y \frac{d y}{d x}-\sec y=-x$
Put $\sec y=v \Rightarrow \sec y \tan y d y=d x$
$\therefore \frac{\mathrm{dv}}{\mathrm{d} \mathrm{x}}-\mathrm{v}=-\mathrm{x}$...(1)
$\therefore$ I.F. $\quad=\mathrm{e}^{-\int 1 \mathrm{dx}}=\mathrm{e}^{-\mathrm{x}}$

</details>

---

### Q46. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The intearrati the differential equation $\left(1+x^{2}\right) d t=\left(\tan ^{-1} x-t\right) d x$

**Options:**

- **(A)** $-e^{\frac{\left(\tan ^{-1} x\right)^{2}}{2}}$
- **(B)** $-e^{\tan ^{-1} x}$
- **(C)** $e^{\frac{\left(\tan ^{-1} x\right)^{2}}{2}}$
- **(D)** $e^{\tan ^{-1} x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $e^{\tan ^{-1} x}$**

**Detailed Solution:**

(D)
$\begin{aligned}
\frac{\mathrm{dt}}{\mathrm{dx}} &=\frac{\tan ^{-1}-\mathrm{t}}{1+\mathrm{x}^{2}} \\
\therefore \frac{\mathrm{dt}}{\mathrm{dx}}+\frac{\mathrm{t}}{1+\mathrm{x}^{2}} &=\frac{\tan ^{-1} \mathrm{x}}{1+\mathrm{x}^{2}} \\
\text { I.F. }=\mathrm{e}^{\int \frac{1}{1+\mathrm{x}^{2}} \mathrm{dx}} &=\mathrm{e}^{\tan ^{-1} \mathrm{x}}
\end{aligned}$

</details>

---

### Q47. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The general solution of the differential equation $\left(1-x^{2}\right) \frac{d y}{d x}+2 x y=x\left(1-x^{2}\right)^{\frac{1}{2}}$ is

**Options:**

- **(A)** $y=\sqrt{1-x^{2}}+c\left(1-x^{2}\right)$
- **(B)** $y=2 \sqrt{1-x^{2}}+c$
- **(C)** $y=2 \sqrt{1-x^{2}}+c\left(1+x^{2}\right)$
- **(D)** $y \sqrt{1-x^{2}}=c\left(1-x^{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y=\sqrt{1-x^{2}}+c\left(1-x^{2}\right)$**

**Detailed Solution:**

$\begin{aligned} &\left(1-x^{2}\right) \frac{d y}{d x}+2 x y=x\left(1-x^{2}\right)^{\frac{1}{2}} \\ \therefore & \frac{d y}{d x}+\frac{2 x y}{1-x^{2}}=\frac{x}{\left(1-x^{2}\right)^{\frac{1}{2}}} \\ \text { I.F. }=& e^{\int \frac{2 x}{1-x^{2}} d x}=e^{-\int \frac{-2 x}{1-x^{2}} d x}=e^{-\log \left(1-x^{2}\right)}=e^{\log \left(\frac{1}{1-x^{2}}\right)}=\frac{1}{1-x^{2}} \end{aligned}$
$\begin{aligned} \therefore\left(\frac{1}{1-x^{2}}\right) &=\int \frac{x}{\left(1-x^{2}\right)^{\frac{1}{2}}} \times \frac{1}{\left(1-x^{2}\right)} d x \\ &=\frac{-1}{2} \int \frac{-2 x}{\left(1-x^{2}\right)^{3 / 2}} d x=\left(-\frac{1}{2}\right) \frac{\left(1-x^{2}\right)^{-\frac{1}{2}}}{\left(-\frac{1}{2}\right)}+c \\ y\left(\frac{1}{1-x^{2}}\right) &=\frac{1}{\sqrt{1-x^{2}}+c \Rightarrow y}=\sqrt{1-x^{2}}+c\left(1-x^{2}\right) \end{aligned}$

</details>

---

### Q48. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Solution of the differential equation  $\frac{d y}{d x}+2 y=e^{-x}$ is

**Options:**

- **(A)** $y e^{x}=x+c$
- **(B)** $y e^{2 x}=x+c$
- **(C)** $y e^{x}=e^{2 x}+c$
- **(D)** $y e^{2 x}=e^{x}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $y e^{2 x}=e^{x}+c$**

**Detailed Solution:**

$\frac{\mathrm{dy}}{\mathrm{dx}}+2 \mathrm{y}=\mathrm{e}^{-x}$
I.F. $=\mathrm{e}^{2 \int \mathrm{dx}}=\mathrm{e}^{2 \mathrm{x}}$
$\therefore \mathrm{ye}^{2 \mathrm{x}}=\int \mathrm{e}^{2 \mathrm{x}} \cdot \mathrm{e}^{-\mathrm{x}} \mathrm{dx}+\mathrm{c}$
$\therefore \mathrm{y} \mathrm{e}^{2 \mathrm{x}}=\int \mathrm{e}^{\mathrm{x}} \mathrm{dx}+\mathrm{c} \Rightarrow \mathrm{ye}^{2 \mathrm{x}}=\mathrm{e}^{\mathrm{x}}+\mathrm{c}$

</details>

---

### Q49. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The solution of $r d x+\left(x-r^{2}\right) d r=0$ is

**Options:**

- **(A)** $r^{2} x=\frac{r^{3}}{3}+c$
- **(B)** $r x=\frac{r^{2}}{2}+c$
- **(C)** $x=\frac{r^{3}}{3}+c$
- **(D)** $r x=\frac{r^{3}}{3}+c$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $r x=\frac{r^{3}}{3}+c$**

**Detailed Solution:**

Given $\mathrm{rdx}+\left(\mathrm{x}-\mathrm{r}^{2}\right) \mathrm{dr}=0 \Rightarrow \mathrm{rdx}=-\left(\mathrm{x}-\mathrm{r}^{2}\right) \mathrm{dr}$
$\begin{array}{l}
\therefore \mathrm{r} \frac{\mathrm{dx}}{\mathrm{dr}}=\mathrm{r}^{2}-\mathrm{x} \Rightarrow \mathrm{r} \frac{\mathrm{d} \mathrm{x}}{\mathrm{dr}}+\mathrm{x}=\mathrm{r}^{2} \\
\therefore \frac{\mathrm{d} \mathrm{x}}{\mathrm{dr}}+\frac{\mathrm{x}}{\mathrm{r}}=\mathrm{r} \\
\quad \text { I.F. }=\mathrm{e}^{\int \frac{1}{\mathrm{r}} \mathrm{dr}}=\mathrm{e}^{\log \mathrm{r}}=\mathrm{r} \\
\text { Solution is } \mathrm{x} \cdot \mathrm{r}=\int \mathrm{r} \cdot \mathrm{r} \mathrm{dr}+\mathrm{c} \\
\quad \mathrm{xr}=\frac{\mathrm{r}^{3}}{3}+\mathrm{c}
\end{array}$

</details>

---

### Q50. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $\frac{d y}{d x}+\frac{1}{x} y=x^{3}-3$ is

**Options:**

- **(A)** $-y$
- **(B)** $y$
- **(C)** $x$
- **(D)** $-x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x$**

**Detailed Solution:**

$\frac{d y}{d x}+\frac{1}{x} y=x^{3}-3 \quad$ is linear differentiatial equation
$\therefore \text { I.F. }=\mathrm{e}^{\int \frac{1}{x} \mathrm{dx}}=\mathrm{e}^{\log x}=\mathrm{x}$

</details>

---

### Q51. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The particular solution of the differential equation
$\sin ^{2} y \frac{d x}{d y}+x=\cot y$ when $x=0$ and $y=\frac{3 \pi}{4}$ is

**Options:**

- **(A)** $x=1+\cot y$
- **(B)** $x y=\cot (x+y)$
- **(C)** $x y=\cot (x-y)$
- **(D)** $y=1+\cot x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x=1+\cot y$**

**Detailed Solution:**

We have, 
$\sin ^{2} \mathrm{y} \frac{\mathrm{d} x}{\mathrm{dy}}+\mathrm{x}=\cot \mathrm{y}$ 
$\therefore \frac{\mathrm{d} \mathrm{x}}{\mathrm{dy}}+\left(\operatorname{cosec}^{2} \mathrm{y}\right) \mathrm{x}=\cot \mathrm{y} \cdot \operatorname{cosec}^{2} \mathrm{y}$ 
$\therefore$ I.F. $=\mathrm{e}^{\int \operatorname{cosec}^{2} \mathrm{ydy}}=\mathrm{e}^{-\cot y}$ 
$\therefore \mathrm{xe}^{-\cot y}=\int \mathrm{e}^{-\cot y} \cot \mathrm{y} \cos \mathrm{ec}^{2} \mathrm{y} \mathrm{dy}$ 
In RHS, put $-\cot \mathrm{y}=\mathrm{t} \Rightarrow \operatorname{cosec}^{2} \mathrm{y} \mathrm{dy}=\mathrm{dt}$ 
$\therefore \quad \mathrm{xe}^{-\cot y}=\int \mathrm{e}^{t}(-\mathrm{t}) \mathrm{dt}=-\int \mathrm{t} \mathrm{e}^{t} \mathrm{dt}$ 
$=-\left[\mathrm{t} \mathrm{e}^{t}-\int \mathrm{e}^{t} \mathrm{dt}\right]=-\mathrm{t} \mathrm{e}^{t}+\mathrm{e}^{t}=\mathrm{e}^{t}(1-\mathrm{t})$ 
$\quad x \mathrm{e}^{-\cot y}=\mathrm{e}^{-\cot y}(1+\cot y)+C$...(2)
At $x=0, y=\frac{3 \pi}{4}$, we get $0=\mathrm{e}(1-1)+C$
From equation $(2)$, required solution is $x \mathrm{e}^{-\cot y}=\mathrm{e}^{-\cot y}(1+\cot y)$ 
$\quad x \quad=1+\cot y$ $x=1+\cot y$

</details>

---

### Q52. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math> is the integration factor of the linear differential equation <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>P</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mo>,</mo></math> then <math><mi>P</mi></math> is

**Options:**

- **(A)** <math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mrow></math>
- **(B)** <math><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(C)** <math><mrow><mrow><mi mathvariant="normal">tan</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(D)** <math><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>**

**Detailed Solution:**

Given.
I.F of <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>+</mo><mi>p</mi><mi>y</mi><mo>=</mo><mi>Q</mi><mi> </mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><msup><mrow><mi>e</mi></mrow><mrow><mrow><mo stretchy="false">∫</mo><mrow><mi>p</mi><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow></mrow></msup><mo>=</mo><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mi>P</mi><mi> </mi><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></math>
By anti - differentiation method, we will get
<math><mi>P</mi><mo>=</mo><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfrac><mo>.</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
<math><mi>P</mi><mo>=</mo><mrow><mrow><mi mathvariant="normal">cot</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>

</details>

---

### Q53. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `3`

The particular solution of the differential equation <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn><mi> </mi></mrow></mrow></math> when <math>
 <mrow>
  <mi>y</mi><mrow><mo>(</mo>
   <mi>e</mi>
  <mo>)</mo></mrow><mo>=</mo><msup>
   <mi>e</mi>
   <mn>2</mn>
  </msup>
  
 </mrow>
</math>
 is

**Options:**

- **(A)** <math><mi>y</mi><mo>=</mo><mi>e</mi><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(B)** <math><mi>e</mi><mi>y</mi><mo>=</mo><mi>x</mi><mi> </mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(C)** <math><mi>x</mi><mi>y</mi><mo>=</mo><mi>e</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>
- **(D)** <math><mi>y</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow><mo>=</mo><mi>e</mi><mi>x</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>y</mi><mo>=</mo><mi>e</mi><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></math>**

**Detailed Solution:**

<math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi>x</mi></mrow></mrow></mrow></mfenced><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>y</mi></mrow></mfrac><mo>-</mo><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac></math>
Integrating on both side
<math><mi> </mi><mrow><mo stretchy="false">∫</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mrow><mo stretchy="false">∫</mo><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>y</mi></mrow></mfrac></mrow></mrow></mrow></mrow></math>
<math><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>y</mi><mo>+</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>C</mi></mrow></mrow></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></mrow></mfenced></mrow></mrow><mo>=</mo><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mfenced separators="|"><mrow><mi>y</mi><mo>.</mo><mi> </mi><mi>c</mi></mrow></mfenced></mrow></mrow></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>x</mi><mi> </mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mi>y</mi><mo>.</mo><mi>c</mi></mrow></mrow></math> ...... (i)
As <math><mi>x</mi><mo>=</mo><mi>e</mi><mo>,</mo></math> <math><mi>y</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>e</mi><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mn>2</mn></mrow></msup><mi> </mi><mo>.</mo><mi>c</mi></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>c</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math>
Putting <math><mi>c</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>e</mi></mrow></mfrac></math> in equation (i) we get
<math><mi>x</mi><mi> </mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi><mo>=</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>e</mi></mrow></mfrac></mrow></mrow></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi>y</mi><mo>=</mo><mi>e</mi><mi>x</mi><mrow><mrow><mi mathvariant="normal">log</mi></mrow><mo>⁡</mo><mrow><mi> </mi><mi>x</mi></mrow></mrow></math>

</details>

---

### Q54. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

The integrating factor of the differential equation $\frac{d y}{d x}(x \log x)+y=2 \log x$ is given by

**Options:**

- **(A)** $e^{x}$
- **(B)** $\log x$
- **(C)** $\log (\log x)$
- **(D)** $x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log x$**

**Detailed Solution:**

$\begin{aligned} & \frac{d y}{d x}(x \log x)+y=2 \log x \\ & \Rightarrow \quad \frac{d y}{d x}+\frac{y}{x \log x}=\frac{2}{x} \end{aligned}$
Here, $\quad P=\frac{1}{x \log x}, Q=\frac{2}{x}$
IF
$$
=e^{\int P d x}=e^{\int \frac{d x}{x \log x}}
$$
$=\log x$

</details>

---

