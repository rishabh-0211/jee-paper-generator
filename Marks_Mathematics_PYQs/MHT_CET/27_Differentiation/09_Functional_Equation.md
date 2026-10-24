# MHT CET Mathematics - Differentiation

## Topic 9: Functional Equation

**Total Questions:** 18

---

### Q1. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $3f(x) - 2f\left(\dfrac{1}{x}\right) = x$ for $x \neq 0$. Then the value of $f'(2)$ is:

**Options:**

- **(A)** $\dfrac{2}{7}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $2$
- **(D)** $\dfrac{7}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Given equation is $3f(x) - 2f\left(\dfrac{1}{x}\right) = x$

Replacing $x$ by $\dfrac{1}{x}$, we get:

$3f\left(\dfrac{1}{x}\right) - 2f(x) = \dfrac{1}{x}$

Multiplying the first equation by $3$ and the second equation by $2$, we obtain:

$9f(x) - 6f\left(\dfrac{1}{x}\right) = 3x$

$-4f(x) + 6f\left(\dfrac{1}{x}\right) = \dfrac{2}{x}$

Adding these two equations gives:

$5f(x) = 3x + \dfrac{2}{x}$

$f(x) = \dfrac{3x}{5} + \dfrac{2}{5x}$

Differentiating with respect to $x$:

$f'(x) = \dfrac{3}{5} - \dfrac{2}{5x^2}$

Substituting $x = 2$:

$f'(2) = \dfrac{3}{5} - \dfrac{2}{5(2)^2} = \dfrac{3}{5} - \dfrac{2}{20} = \dfrac{3}{5} - \dfrac{1}{10} = \dfrac{6 - 1}{10} = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q2. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f : R \to R$ is an even function then

**Options:**

- **(A)** $f'(0) = 1$
- **(B)** $f'(x)$ is an even function
- **(C)** $f(0) = 0$
- **(D)** $f'(x)$ is an odd function

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $f'(x)$ is an odd function**

**Detailed Solution:**

Given that $f(x)$ is an even function, we have:

$f(-x) = f(x)$

Differentiating both sides with respect to $x$, we get:

$-f'(-x) = f'(x)$

$f'(-x) = -f'(x)$

This condition satisfies the definition of an odd function. Therefore, $f'(x)$ is an odd function.

Answer: $f'(x)$ is an odd function

</details>

---

### Q3. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The function $y(x)$ represented by $x=\sin \mathrm{t}$, $y=a e^{\mathrm{t} \sqrt{2}}+b \mathrm{e}^{\mathrm{t} \sqrt{2}}, \mathrm{t} \in\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$ satisfies the equation $\left(1-x^2\right) y^{\prime \prime}-x y^{\prime}=\mathrm{k} y$, then the value of $k$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** -1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Given $x = \sin t$, we have $\dfrac{dx}{dt} = \cos t$.

For $y = a e^{t\sqrt{2}} + b e^{t\sqrt{2}} = (a+b) e^{t\sqrt{2}}$, differentiating with respect to $t$ gives:

$\dfrac{dy}{dt} = \sqrt{2} (a+b) e^{t\sqrt{2}}$

$\dfrac{d^2y}{dt^2} = 2 (a+b) e^{t\sqrt{2}} = 2y$

Finding the first derivative with respect to $x$:

$y' = \dfrac{dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}} = \dfrac{1}{\cos t} \dfrac{dy}{dt}$

Differentiating again with respect to $x$:

$y'' = \dfrac{d}{dx} \left( \dfrac{dy}{dx} \right) = \dfrac{dt}{dx} \dfrac{d}{dt} \left( \dfrac{1}{\cos t} \dfrac{dy}{dt} \right)$

$y'' = \dfrac{1}{\cos t} \left( \dfrac{\cos t \dfrac{d^2y}{dt^2} - (-\sin t) \dfrac{dy}{dt}}{\cos^2 t} \right)$

$y'' = \dfrac{1}{\cos^2 t} \dfrac{d^2y}{dt^2} + \dfrac{\sin t}{\cos^2 t} \left( \dfrac{1}{\cos t} \dfrac{dy}{dt} \right)$

Substituting $\cos^2 t = 1 - \sin^2 t = 1 - x^2$, $\sin t = x$, $\dfrac{d^2y}{dt^2} = 2y$, and $\dfrac{1}{\cos t} \dfrac{dy}{dt} = y'$:

$y'' = \dfrac{2y}{1 - x^2} + \dfrac{x}{1 - x^2} y'$

Multiplying by $(1 - x^2)$:

$(1 - x^2) y'' = 2y + x y'$

$(1 - x^2) y'' - x y' = 2y$

Comparing this with the given equation $(1 - x^2) y'' - x y' = k y$, we get $k = 2$.

Answer: 2

</details>

---

### Q4. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(1)=1, f^{\prime}(1)=5$, then the derivative of $\mathrm{f}(\mathrm{f}(\mathrm{f}(x)))+(\mathrm{f}(x))^2$ at $x=1$ is

**Options:**

- **(A)** 125
- **(B)** 1250
- **(C)** 135
- **(D)** 35

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 135**

**Detailed Solution:**

Let $y = f(f(f(x))) + (f(x))^2$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = f^{\prime}(f(f(x))) \cdot \dfrac{d}{dx}(f(f(x))) + 2f(x) \cdot f^{\prime}(x)$

$\dfrac{dy}{dx} = f^{\prime}(f(f(x))) \cdot f^{\prime}(f(x)) \cdot f^{\prime}(x) + 2f(x)f^{\prime}(x)$

Substituting $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f^{\prime}(f(f(1))) \cdot f^{\prime}(f(1)) \cdot f^{\prime}(1) + 2f(1)f^{\prime}(1)$

Given $f(1) = 1$, we have $f(f(1)) = f(1) = 1$ and $f(f(f(1))) = f(1) = 1$.

$\left. \dfrac{dy}{dx} \right|_{x=1} = f^{\prime}(1) \cdot f^{\prime}(1) \cdot f^{\prime}(1) + 2f(1)f^{\prime}(1)$

Substituting $f(1) = 1$ and $f^{\prime}(1) = 5$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = (5)(5)(5) + 2(1)(5)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = 125 + 10 = 135$

Answer: 135

</details>

---

### Q5. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $f(1)=1$, $f^{\prime}(1)=3$, then the derivative of $\mathrm{f}(\mathrm{f}(\mathrm{f}(x)))+(\mathrm{f}(x))^2$ at $x=1$ is

**Options:**

- **(A)** 12
- **(B)** 15
- **(C)** 9
- **(D)** 33

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 33**

**Detailed Solution:**

Let $y = f(f(f(x))) + (f(x))^2$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = f^{\prime}(f(f(x))) \cdot \dfrac{d}{dx}(f(f(x))) + 2f(x) \cdot f^{\prime}(x)$

$\dfrac{dy}{dx} = f^{\prime}(f(f(x))) \cdot f^{\prime}(f(x)) \cdot f^{\prime}(x) + 2f(x)f^{\prime}(x)$

Substitute $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f^{\prime}(f(f(1))) \cdot f^{\prime}(f(1)) \cdot f^{\prime}(1) + 2f(1)f^{\prime}(1)$

Given $f(1) = 1$, we have $f(f(1)) = f(1) = 1$ and $f(f(f(1))) = f(1) = 1$.

Substituting these values:

$\left. \dfrac{dy}{dx} \right|_{x=1} = f^{\prime}(1) \cdot f^{\prime}(1) \cdot f^{\prime}(1) + 2(1)f^{\prime}(1)$

Given $f^{\prime}(1) = 3$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = (3)(3)(3) + 2(1)(3)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = 27 + 6 = 33$

Answer: 33

</details>

---

### Q6. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{f}(1)=1, \mathrm{f}^{\prime}(1)=3$, then the derivative of $\mathrm{f}(\mathrm{f}(\mathrm{f}(x)))+(\mathrm{f}(x))^2$ at $x=1$ is

**Options:**

- **(A)** 12
- **(B)** 30
- **(C)** 15
- **(D)** 33

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 33**

**Detailed Solution:**

Let $y = \mathrm{f}(\mathrm{f}(\mathrm{f}(x))) + (\mathrm{f}(x))^2$

Differentiating with respect to $x$ using the chain rule:

$\dfrac{dy}{dx} = \mathrm{f}^{\prime}(\mathrm{f}(\mathrm{f}(x))) \cdot \dfrac{d}{dx}(\mathrm{f}(\mathrm{f}(x))) + 2\mathrm{f}(x) \cdot \mathrm{f}^{\prime}(x)$

$\dfrac{dy}{dx} = \mathrm{f}^{\prime}(\mathrm{f}(\mathrm{f}(x))) \cdot \mathrm{f}^{\prime}(\mathrm{f}(x)) \cdot \mathrm{f}^{\prime}(x) + 2\mathrm{f}(x)\mathrm{f}^{\prime}(x)$

Substitute $x = 1$:

$\left. \dfrac{dy}{dx} \right|_{x=1} = \mathrm{f}^{\prime}(\mathrm{f}(\mathrm{f}(1))) \cdot \mathrm{f}^{\prime}(\mathrm{f}(1)) \cdot \mathrm{f}^{\prime}(1) + 2\mathrm{f}(1)\mathrm{f}^{\prime}(1)$

Given $\mathrm{f}(1) = 1$ and $\mathrm{f}^{\prime}(1) = 3$:

$\mathrm{f}(\mathrm{f}(1)) = \mathrm{f}(1) = 1$

$\mathrm{f}(\mathrm{f}(\mathrm{f}(1))) = \mathrm{f}(1) = 1$

Substituting these values into the derivative expression:

$\left. \dfrac{dy}{dx} \right|_{x=1} = \mathrm{f}^{\prime}(1) \cdot \mathrm{f}^{\prime}(1) \cdot \mathrm{f}^{\prime}(1) + 2(1)(3)$

$\left. \dfrac{dy}{dx} \right|_{x=1} = 3 \cdot 3 \cdot 3 + 6 = 27 + 6 = 33$

Answer: 33

</details>

---

### Q7. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $f$ be twice differentiable function such that $\mathrm{f}^{\prime \prime}(x)=-\mathrm{f}(x), \mathrm{f}^{\prime}(x)=\mathrm{g}(x)$ and $\mathrm{h}(x)=(\mathrm{f}(x))^2+(\mathrm{g}(x))^2$. If $\mathrm{h}(5)=1$, then the value of $h(10)$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** $\frac{1}{2}$
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

Given $\mathrm{h}(x) = (\mathrm{f}(x))^2 + (\mathrm{g}(x))^2$

Differentiating with respect to $x$, we get:

$\mathrm{h}^{\prime}(x) = 2\mathrm{f}(x)\mathrm{f}^{\prime}(x) + 2\mathrm{g}(x)\mathrm{g}^{\prime}(x)$

We are given $\mathrm{f}^{\prime}(x) = \mathrm{g}(x)$. Differentiating both sides with respect to $x$ gives $\mathrm{f}^{\prime \prime}(x) = \mathrm{g}^{\prime}(x)$.

Since $\mathrm{f}^{\prime \prime}(x) = -\mathrm{f}(x)$, we have $\mathrm{g}^{\prime}(x) = -\mathrm{f}(x)$.

Substituting $\mathrm{f}^{\prime}(x) = \mathrm{g}(x)$ and $\mathrm{g}^{\prime}(x) = -\mathrm{f}(x)$ into the expression for $\mathrm{h}^{\prime}(x)$:

$\mathrm{h}^{\prime}(x) = 2\mathrm{f}(x)\mathrm{g}(x) + 2\mathrm{g}(x)(-\mathrm{f}(x))$

$\mathrm{h}^{\prime}(x) = 2\mathrm{f}(x)\mathrm{g}(x) - 2\mathrm{f}(x)\mathrm{g}(x) = 0$

Since $\mathrm{h}^{\prime}(x) = 0$ for all $x$, $\mathrm{h}(x)$ is a constant function.

Given $\mathrm{h}(5) = 1$, the constant value is $1$.

Therefore, $\mathrm{h}(10) = 1$.

Answer: 1

</details>

---

### Q8. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $8 \mathrm{f}(x)+6 \mathrm{f}\left(\dfrac{1}{x}\right)=x+5$ and $y=x^2 \mathrm{f}(x)$, then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=-1$ is

**Options:**

- **(A)** 14
- **(B)** -14
- **(C)** $\dfrac{1}{14}$
- **(D)** $-\dfrac{1}{14}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{14}$**

**Detailed Solution:**

Given equation:

$8 \mathrm{f}(x) + 6 \mathrm{f}\left(\dfrac{1}{x}\right) = x + 5$

Replacing $x$ by $\dfrac{1}{x}$, we get:

$8 \mathrm{f}\left(\dfrac{1}{x}\right) + 6 \mathrm{f}(x) = \dfrac{1}{x} + 5$

To eliminate $\mathrm{f}\left(\dfrac{1}{x}\right)$, multiply the first equation by $4$ and the second equation by $3$:

$32 \mathrm{f}(x) + 24 \mathrm{f}\left(\dfrac{1}{x}\right) = 4x + 20$

$18 \mathrm{f}(x) + 24 \mathrm{f}\left(\dfrac{1}{x}\right) = \dfrac{3}{x} + 15$

Subtracting the second equation from the first:

$14 \mathrm{f}(x) = 4x - \dfrac{3}{x} + 5$

$\mathrm{f}(x) = \dfrac{4x - \dfrac{3}{x} + 5}{14}$

We are given $y = x^2 \mathrm{f}(x)$. Substituting $\mathrm{f}(x)$ into this expression:

$y = x^2 \left( \dfrac{4x - \dfrac{3}{x} + 5}{14} \right) = \dfrac{4x^3 + 5x^2 - 3x}{14}$

Differentiating $y$ with respect to $x$:

$\dfrac{\mathrm{d} y}{\mathrm{d} x} = \dfrac{12x^2 + 10x - 3}{14}$

Evaluating the derivative at $x = -1$:

$\left. \dfrac{\mathrm{d} y}{\mathrm{d} x} \right|_{x=-1} = \dfrac{12(-1)^2 + 10(-1) - 3}{14}$

$\left. \dfrac{\mathrm{d} y}{\mathrm{d} x} \right|_{x=-1} = \dfrac{12 - 10 - 3}{14} = -\dfrac{1}{14}$

Answer: $-\dfrac{1}{14}$

</details>

---

### Q9. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $f$ be a twice differentiable function such that $\mathrm{f}^{\prime \prime}(x)=-\mathrm{f}(x), \mathrm{f}^{\prime}(x)=\mathrm{g}(x)$ and $\mathrm{h}(x)=[\mathrm{f}(x)]^2+[\mathrm{g}(x)]^2$. If $\mathrm{h}(5)=1$, then $\mathrm{h}(10)$ is $\qquad$

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

Given $\mathrm{h}(x) = [\mathrm{f}(x)]^2 + [\mathrm{g}(x)]^2$

Differentiating with respect to $x$:

$\mathrm{h}^{\prime}(x) = 2\mathrm{f}(x)\mathrm{f}^{\prime}(x) + 2\mathrm{g}(x)\mathrm{g}^{\prime}(x)$

We are given $\mathrm{f}^{\prime}(x) = \mathrm{g}(x)$. Differentiating this gives $\mathrm{f}^{\prime \prime}(x) = \mathrm{g}^{\prime}(x)$.

Since $\mathrm{f}^{\prime \prime}(x) = -\mathrm{f}(x)$, we have $\mathrm{g}^{\prime}(x) = -\mathrm{f}(x)$.

Substituting these into the derivative of $\mathrm{h}(x)$:

$\mathrm{h}^{\prime}(x) = 2\mathrm{f}(x)\mathrm{g}(x) + 2\mathrm{g}(x)(-\mathrm{f}(x)) = 0$

Since $\mathrm{h}^{\prime}(x) = 0$ for all $x$, $\mathrm{h}(x)$ is a constant function.

Given $\mathrm{h}(5) = 1$, it follows that $\mathrm{h}(x) = 1$ for all $x$.

Therefore, $\mathrm{h}(10) = 1$.

Answer: 1

</details>

---

### Q10. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{F}(x)=\left(\mathrm{f}\left(\dfrac{x}{2}\right)\right)^2+\left(\mathrm{g}\left(\dfrac{x}{2}\right)\right)^2$, where $\mathrm{f}^{\prime \prime}(x)=-\mathrm{f}(x)$ and $g(x)=\mathrm{f}^{\prime}(x)$ and given by $\mathrm{F}(5)=5$, then $\mathrm{F}(10)$ is equal to

**Options:**

- **(A)** 5
- **(B)** 10
- **(C)** 15
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

Given $F(x) = \left(f\left(\dfrac{x}{2}\right)\right)^2 + \left(g\left(\dfrac{x}{2}\right)\right)^2$

Differentiating with respect to $x$:

$F^{\prime}(x) = 2f\left(\dfrac{x}{2}\right)f^{\prime}\left(\dfrac{x}{2}\right) \cdot \dfrac{1}{2} + 2g\left(\dfrac{x}{2}\right)g^{\prime}\left(\dfrac{x}{2}\right) \cdot \dfrac{1}{2}$

$F^{\prime}(x) = f\left(\dfrac{x}{2}\right)f^{\prime}\left(\dfrac{x}{2}\right) + g\left(\dfrac{x}{2}\right)g^{\prime}\left(\dfrac{x}{2}\right)$

We are given $g(x) = f^{\prime}(x)$, which implies $g^{\prime}(x) = f^{\prime \prime}(x)$.

Also given $f^{\prime \prime}(x) = -f(x)$, so $g^{\prime}(x) = -f(x)$.

Substituting these into the derivative:

$F^{\prime}(x) = f\left(\dfrac{x}{2}\right)g\left(\dfrac{x}{2}\right) + g\left(\dfrac{x}{2}\right)\left(-f\left(\dfrac{x}{2}\right)\right) = 0$

Since $F^{\prime}(x) = 0$, $F(x)$ is a constant function.

Given $F(5) = 5$, the constant is $5$.

Therefore, $F(10) = 5$.

Answer: 5

</details>

---

### Q11. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

At present a firm is manufacturing 1000 items. It is estimated that the rate of change of production P w.r.t. additional number of worker $x$ is given by $\frac{\mathrm{dp}}{\mathrm{d} x}=100-12 \sqrt{x}$.
If the firm employees 9 more workers, then the new level of production of items is

**Options:**

- **(A)** $1684$
- **(B)** $1648$
- **(C)** $2116$
- **(D)** $1116$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1684$**

**Detailed Solution:**

$\begin{array}{ll} 
& \frac{\mathrm{dP}}{\mathrm{d} x}=100-12 \sqrt{x} \\
& \text { Integrating both sides, we get } \\
& \int \mathrm{dp}=\int(100-12 \sqrt{x}) \mathrm{d} x \\
\therefore \quad & \mathrm{P}=100 x-8 x \sqrt{x}+\mathrm{c} \\
& \text { Given that } \mathrm{P}=1000, \text { when } x=0 \\
\Rightarrow & 1000=100(0)-8(0)+\mathrm{c} \\
\Rightarrow \mathrm{c}=1000 & \\
\therefore \quad & \mathrm{P}=100 x-8 x \sqrt{x}+1000 \\
& \text { When } x=9, \text { we get } \\
& \mathrm{P}=900-216+1000=1684
\end{array}$
$\therefore \quad$ The new level of production of items is 1684 .

</details>

---

### Q12. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The set of all points, where the derivative of the functions $\mathrm{f}(x)=\frac{x}{1+|x|}$ exists, is

**Options:**

- **(A)** $(-\infty, \infty)$
- **(B)** $[0, \infty)$
- **(C)** $(-\infty, 0) \cup(0, \infty)$
- **(D)** $(0, \infty)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(-\infty, \infty)$**

**Detailed Solution:**

$\mathrm{f}(x)$ can be written as
$\begin{aligned}
& \mathrm{f}(x)=\left\{\begin{array}{l}
\frac{x}{1-x}, x \leq 0 \\
\frac{x}{1+x}, x>0
\end{array}\right. \\
& \mathrm{f}^{\prime}(x)= \begin{cases}\frac{(1-x)+x}{(1+x)^2}, & x \leq 0 \\
\frac{(1+x)-x}{(1+x)^2}, & x>0\end{cases} \\
& \mathrm{f}^{\prime}(x)=\frac{1}{(1+x)^2} \forall x \in(-\infty, \infty)
\end{aligned}$
$\therefore \quad$ Derivative of $\mathrm{f}(x)$ exists $\forall x \in(-\infty, \infty)$

</details>

---

### Q13. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For $x>1$, if $(2 x)^{2 y}=4 \mathrm{e}^{2 x-2 y}$, then $(1+\log 2 x)^2 \frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{x \log 2 x+\log 2}{x}$
- **(B)** $\frac{x \log 2 x-\log 2}{x}$
- **(C)** $x \log 2 x$
- **(D)** $\log 2 x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x \log 2 x-\log 2}{x}$**

**Detailed Solution:**

$(2 x)^{2 y}=4 \mathrm{e}^{2 x-2 y}$
Taking log on both sides, we get
$\begin{aligned}
& 2 y \log 2 x=\log \left(4 \mathrm{e}^{2 x-2 y}\right) \\
& \Rightarrow 2 y \log 2 x=\log 4+\log \mathrm{e}^{2 x-2 y} \\
& \Rightarrow 2 y \log 2 x=\log 4+2 x-2 y \\
& \Rightarrow 2 y \log 2 x+2 y=\log 4+2 x \\
& \Rightarrow 2(y \log 2 x+y)=2 \log 2+2 x \\
& \Rightarrow y \log 2 x+y=\log 2+x \\
& \Rightarrow y(1+\log 2 x)=x+\log 2 \\
& \Rightarrow y=\frac{x+\log 2}{1+\log 2 x}
\end{aligned}$
Differentiating w.r.t. $x$, we get
$\begin{gathered}
\frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{(1+\log 2 x)(1+0)-(x+\log 2)\left(\frac{1}{2 x}\right) \cdot 2}{(1+\log 2 x)^2} \\
\Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{(1+\log 2 x)-\frac{1}{x}(x+\log 2)}{(1+\log 2 x)^2} \\
\Rightarrow(1+\log 2 x)^2 \frac{\mathrm{d} y}{\mathrm{~d} x}=1+\log 2 x-1-\frac{\log 2}{x} \\
\Rightarrow(1+\log 2 x)^2 \frac{\mathrm{d} y}{\mathrm{~d} x}=\log 2 x-\frac{\log 2}{x} \\
=\frac{x \log 2 x-\log 2}{x}
\end{gathered}$

</details>

---

### Q14. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $2 \mathrm{f}(\mathrm{x})=\mathrm{f}^{\prime}(x)$ and $\mathrm{f}(0)=3$, then the value of $\mathrm{f}(2)$ is

**Options:**

- **(A)** $3 e^{2}$
- **(B)** $2 e^{3}$
- **(C)** $4 e^{3}$
- **(D)** $3 e^{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 e^{4}$**

**Detailed Solution:**

We have $f^{\prime}(x)=2 f(x)$
$$
\begin{array}{l}
\therefore \int \frac{\mathrm{f}^{\prime}(\mathrm{x})}{\mathrm{f}(\mathrm{x})} \mathrm{d} \mathrm{x}=\int 2 \mathrm{~d} \mathrm{x} \\
\therefore \log |\mathrm{f}(\mathrm{x})|=2 \mathrm{x}+\mathrm{c}
\end{array}
$$
Now $f(0)=3$
$$
\begin{array}{l}
\therefore|\log 3|=0+c \Rightarrow c=\log 3 \\
\therefore \log |f(x)|=2 x+\log 3
\end{array}
$$
When $x=2$,
$$
\begin{aligned}
& \log |\mathrm{f}(2)|=2(2)+\log 3=4+\log 3 \\
\therefore & \mathrm{f}(2)=\mathrm{e}^{4+\log 3}=\mathrm{e}^{4} \cdot \mathrm{e}^{\log 3}=3 \mathrm{e}^{4}
\end{aligned}
$$

</details>

---

### Q15. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=e^{x} g(x), g(0)=4, g^{\prime}(0)=2$, then $f^{\prime}(0)=$

**Options:**

- **(A)** 4
- **(B)** 6
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6**

**Detailed Solution:**

Given $f(x)=e^{x} g(x)$
$$
\begin{aligned}
\therefore f^{\prime}(x) &=e^{x} g^{\prime}(x)+g(x) \cdot e^{x} \\
\therefore f^{\prime}(0) &=e^{0} g^{\prime}(0)+g(0) \cdot e^{0} \\
&=2+4=6
\end{aligned}
$$

</details>

---

### Q16. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If $u_{0}=8, u_{1}=3, u_{2}=12, u_{3}=51$, then the value of $\Delta^{3} u_{0}$ is

**Options:**

- **(A)** 12
- **(B)** 14
- **(C)** 16
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 16**

**Detailed Solution:**

$\Delta^{3} u_{0}=(E-1)^{3} u_{0}$
$$
\begin{array}{l}
=\left(E^{3}-3 E^{2}+3 E-1\right) u_{0}=u_{3}-3 u_{2}+3 u_{1}-u_{0} \\
=51-3 \times 12+3 \times 3-8=16
\end{array}
$$

</details>

---

### Q17. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

$(1+\Lambda)^{n} f(a)$ is equal to

**Options:**

- **(A)** $f(a+h)$
- **(B)** $f(a+2 h)$
- **(C)** $f(a+n h)$
- **(D)** $f(a+(n-1) h)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $f(a+n h)$**

**Detailed Solution:**

$\begin{aligned}(1+\Delta)^{n} f(a) &=E^{n} f(a) \\ &=f(a+n h) \end{aligned}$

</details>

---

### Q18. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

The valuc of $f(4)-f(3)$ is

**Options:**

- **(A)** $\Delta f(2)+\Delta^{2} f(1)+\Delta^{3} f(1)$
- **(B)** $\Delta f(3)+\Delta^{2} f(2)+\Delta^{3} f(1)$
- **(C)** $\Delta f(2)+\Delta^{2} f(1)+\Delta^{3} f(0)$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\Delta f(2)+\Delta^{2} f(1)+\Delta^{3} f(1)$**

**Detailed Solution:**

$f(4)-f(3)=\Delta f(3)$
$=\Delta[f(2)+\Delta f(2)]$
$[\because \Delta f(2)=f(3)-f(2)]$
$=\Delta f(2)+\Delta^{2} f(2)$
$=\Delta f(2)+\Delta^{2}[f(1)+\Delta f(1)]$
$=\Delta f(2)+\Delta^{2} f(1)+\Delta^{3} f(1)$

</details>

---

