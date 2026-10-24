# MHT CET Mathematics - Differentiation

## Topic 2: Differentiation of implicit functions

**Total Questions:** 48

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y^{1/n} + y^{-1/n} = 2x$, then $(x^2 - 1)\dfrac{d^2y}{dx^2} + x\dfrac{dy}{dx} = \ldots$

**Options:**

- **(A)** $n^2 y$
- **(B)** $-n^2 y$
- **(C)** $0$
- **(D)** $y$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $n^2 y$**

**Detailed Solution:**

Given $y^{1/n} + y^{-1/n} = 2x$

Differentiating with respect to $x$:

$\dfrac{1}{n} y^{1/n - 1} \dfrac{dy}{dx} - \dfrac{1}{n} y^{-1/n - 1} \dfrac{dy}{dx} = 2$

$\dfrac{dy}{dx} \left( \dfrac{y^{1/n} - y^{-1/n}}{n y} \right) = 2$

$\dfrac{dy}{dx} (y^{1/n} - y^{-1/n}) = 2n y$

Squaring both sides:

$\left(\dfrac{dy}{dx}\right)^2 (y^{1/n} - y^{-1/n})^2 = 4n^2 y^2$

Using the identity $(a - b)^2 = (a + b)^2 - 4ab$:

$(y^{1/n} - y^{-1/n})^2 = (y^{1/n} + y^{-1/n})^2 - 4 = 4x^2 - 4 = 4(x^2 - 1)$

Substituting this back:

$\left(\dfrac{dy}{dx}\right)^2 4(x^2 - 1) = 4n^2 y^2$

$(x^2 - 1)\left(\dfrac{dy}{dx}\right)^2 = n^2 y^2$

Differentiating again with respect to $x$:

$(x^2 - 1) 2\dfrac{dy}{dx} \dfrac{d^2y}{dx^2} + 2x \left(\dfrac{dy}{dx}\right)^2 = 2n^2 y \dfrac{dy}{dx}$

Dividing by $2\dfrac{dy}{dx}$:

$(x^2 - 1)\dfrac{d^2y}{dx^2} + x\dfrac{dy}{dx} = n^2 y$

Answer: $n^2 y$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{1 - x^6} + \sqrt{1 - y^6} = a^3(x^3 - y^3)$, then $\dfrac{dy}{dx} = \ldots$

**Options:**

- **(A)** $\dfrac{x^2}{y^2}\sqrt{\dfrac{1 - x^6}{1 - y^6}}$
- **(B)** $\dfrac{y^2}{x^2}\sqrt{\dfrac{1 - y^6}{1 - x^6}}$
- **(C)** $\dfrac{x^2}{y^2}\sqrt{\dfrac{1 - y^6}{1 - x^6}}$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x^2}{y^2}\sqrt{\dfrac{1 - y^6}{1 - x^6}}$**

**Detailed Solution:**

Substitute $x^3 = \sin \alpha$ and $y^3 = \sin \beta$.

The given equation becomes:

$\sqrt{1 - \sin^2 \alpha} + \sqrt{1 - \sin^2 \beta} = a^3(\sin \alpha - \sin \beta)$

$\cos \alpha + \cos \beta = a^3(\sin \alpha - \sin \beta)$

Using sum-to-product formulas:

$2 \cos \left( \dfrac{\alpha + \beta}{2} \right) \cos \left( \dfrac{\alpha - \beta}{2} \right) = a^3 \left( 2 \sin \left( \dfrac{\alpha - \beta}{2} \right) \cos \left( \dfrac{\alpha + \beta}{2} \right) \right)$

$\cot \left( \dfrac{\alpha - \beta}{2} \right) = a^3$

$\alpha - \beta = 2 \cot^{-1}(a^3)$

Substituting back $\alpha = \sin^{-1}(x^3)$ and $\beta = \sin^{-1}(y^3)$:

$\sin^{-1}(x^3) - \sin^{-1}(y^3) = 2 \cot^{-1}(a^3)$

Differentiating both sides with respect to $x$:

$\dfrac{1}{\sqrt{1 - (x^3)^2}} \cdot 3x^2 - \dfrac{1}{\sqrt{1 - (y^3)^2}} \cdot 3y^2 \dfrac{dy}{dx} = 0$

$\dfrac{3x^2}{\sqrt{1 - x^6}} = \dfrac{3y^2}{\sqrt{1 - y^6}} \dfrac{dy}{dx}$

$\dfrac{dy}{dx} = \dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$

Answer: $\dfrac{x^2}{y^2}\sqrt{\dfrac{1 - y^6}{1 - x^6}}$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $3x^2 + 4xy + 5y^2 = 0$, then $\dfrac{dy}{dx} = \ldots$

**Options:**

- **(A)** $\dfrac{x}{y}$
- **(B)** $\dfrac{y}{x}$
- **(C)** $\dfrac{2x}{y}$
- **(D)** $\dfrac{x}{2y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{y}{x}$**

**Detailed Solution:**

Given equation is $3x^2 + 4xy + 5y^2 = 0$.

Differentiating both sides with respect to $x$, we get:

$6x + 4\left(y + x\dfrac{dy}{dx}\right) + 10y\dfrac{dy}{dx} = 0$

$6x + 4y + (4x + 10y)\dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} = -\dfrac{6x + 4y}{4x + 10y} = -\dfrac{3x + 2y}{2x + 5y}$

To simplify this expression, consider the difference between $\dfrac{y}{x}$ and $\dfrac{dy}{dx}$:

$\dfrac{y}{x} - \left( -\dfrac{3x + 2y}{2x + 5y} \right) = \dfrac{y(2x + 5y) + x(3x + 2y)}{x(2x + 5y)}$

$\Rightarrow \dfrac{y}{x} + \dfrac{3x + 2y}{2x + 5y} = \dfrac{2xy + 5y^2 + 3x^2 + 2xy}{x(2x + 5y)} = \dfrac{3x^2 + 4xy + 5y^2}{x(2x + 5y)}$

Since it is given that $3x^2 + 4xy + 5y^2 = 0$, the numerator is zero.

$\Rightarrow \dfrac{y}{x} - \dfrac{dy}{dx} = 0$

$\Rightarrow \dfrac{dy}{dx} = \dfrac{y}{x}$

(Alternatively, for any homogeneous equation of degree $n$ in $x$ and $y$ representing straight lines through the origin, $\dfrac{dy}{dx} = \dfrac{y}{x}$ always holds true.)

Answer: $\dfrac{y}{x}$

</details>

---

### Q4. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{1 - x^6} + \sqrt{1 - y^6} = a^3(x^3 - y^3)$, then $\dfrac{dy}{dx} = $ ...

**Options:**

- **(A)** $-\dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$
- **(B)** $\dfrac{y^2}{x^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$
- **(C)** $\dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$
- **(D)** $-\dfrac{y^2}{x^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$**

**Detailed Solution:**

Let $x^3 = \sin \alpha$ and $y^3 = \sin \beta$.

The given equation becomes:

$\sqrt{1 - \sin^2 \alpha} + \sqrt{1 - \sin^2 \beta} = a^3(\sin \alpha - \sin \beta)$

$\cos \alpha + \cos \beta = a^3(\sin \alpha - \sin \beta)$

Using trigonometric sum-to-product identities:

$2 \cos\left(\dfrac{\alpha + \beta}{2}\right) \cos\left(\dfrac{\alpha - \beta}{2}\right) = a^3 \left[ 2 \cos\left(\dfrac{\alpha + \beta}{2}\right) \sin\left(\dfrac{\alpha - \beta}{2}\right) \right]$

$\cot\left(\dfrac{\alpha - \beta}{2}\right) = a^3$

$\alpha - \beta = 2 \cot^{-1}(a^3)$

Substituting back $\alpha = \sin^{-1}(x^3)$ and $\beta = \sin^{-1}(y^3)$:

$\sin^{-1}(x^3) - \sin^{-1}(y^3) = 2 \cot^{-1}(a^3)$

Differentiating both sides with respect to $x$:

$\dfrac{1}{\sqrt{1 - (x^3)^2}} \cdot 3x^2 - \dfrac{1}{\sqrt{1 - (y^3)^2}} \cdot 3y^2 \dfrac{dy}{dx} = 0$

$\dfrac{3x^2}{\sqrt{1 - x^6}} - \dfrac{3y^2}{\sqrt{1 - y^6}} \dfrac{dy}{dx} = 0$

$\dfrac{dy}{dx} = \dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$

Answer: $\dfrac{x^2}{y^2} \sqrt{\dfrac{1 - y^6}{1 - x^6}}$

</details>

---

### Q5. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{\dfrac{x}{y}} + \sqrt{\dfrac{y}{x}} = 6$, then $\dfrac{dy}{dx} =$

**Options:**

- **(A)** $\dfrac{x + 17y}{17x - y}$
- **(B)** $\dfrac{x - 17y}{17x - y}$
- **(C)** $\dfrac{x - 17y}{17x + y}$
- **(D)** $\dfrac{x + 17y}{17x + y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{x - 17y}{17x - y}$**

**Detailed Solution:**

Given $\sqrt{\dfrac{x}{y}} + \sqrt{\dfrac{y}{x}} = 6$

Squaring both sides, we get:

$\dfrac{x}{y} + \dfrac{y}{x} + 2 = 36$

$\dfrac{x}{y} + \dfrac{y}{x} = 34$

$x^2 + y^2 = 34xy$

Differentiating both sides with respect to $x$:

$2x + 2y \dfrac{dy}{dx} = 34 \left( y + x \dfrac{dy}{dx} \right)$

Dividing by $2$:

$x + y \dfrac{dy}{dx} = 17y + 17x \dfrac{dy}{dx}$

Rearranging the terms to solve for $\dfrac{dy}{dx}$:

$x - 17y = (17x - y) \dfrac{dy}{dx}$

$\dfrac{dy}{dx} = \dfrac{x - 17y}{17x - y}$

Answer: $\dfrac{x - 17y}{17x - y}$

</details>

---

### Q6. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{y + x} + \sqrt{y - x} = c$ and $\dfrac{dy}{dx} = K - \sqrt{\dfrac{y^2}{x^2} - 1}$ , then the value of $K$ is

**Options:**

- **(A)** $\dfrac{-x}{y}$
- **(B)** $\dfrac{-y}{x}$
- **(C)** $\dfrac{x}{y}$
- **(D)** $\dfrac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{y}{x}$**

**Detailed Solution:**

Given equation is $\sqrt{y + x} + \sqrt{y - x} = c$

Squaring both sides, we get:

$(\sqrt{y + x} + \sqrt{y - x})^2 = c^2$

$(y + x) + (y - x) + 2\sqrt{(y + x)(y - x)} = c^2$

$2y + 2\sqrt{y^2 - x^2} = c^2$

$y + \sqrt{y^2 - x^2} = \dfrac{c^2}{2}$

Differentiating both sides with respect to $x$:

$\dfrac{dy}{dx} + \dfrac{1}{2\sqrt{y^2 - x^2}} \left( 2y \dfrac{dy}{dx} - 2x \right) = 0$

$\dfrac{dy}{dx} + \dfrac{y}{\sqrt{y^2 - x^2}} \dfrac{dy}{dx} - \dfrac{x}{\sqrt{y^2 - x^2}} = 0$

$\dfrac{dy}{dx} \left( 1 + \dfrac{y}{\sqrt{y^2 - x^2}} \right) = \dfrac{x}{\sqrt{y^2 - x^2}}$

$\dfrac{dy}{dx} \left( \dfrac{\sqrt{y^2 - x^2} + y}{\sqrt{y^2 - x^2}} \right) = \dfrac{x}{\sqrt{y^2 - x^2}}$

$\dfrac{dy}{dx} = \dfrac{x}{y + \sqrt{y^2 - x^2}}$

Rationalizing the denominator by multiplying the numerator and denominator by $y - \sqrt{y^2 - x^2}$:

$\dfrac{dy}{dx} = \dfrac{x(y - \sqrt{y^2 - x^2})}{(y + \sqrt{y^2 - x^2})(y - \sqrt{y^2 - x^2})}$

$\dfrac{dy}{dx} = \dfrac{x(y - \sqrt{y^2 - x^2})}{y^2 - (y^2 - x^2)}$

$\dfrac{dy}{dx} = \dfrac{x(y - \sqrt{y^2 - x^2})}{x^2}$

$\dfrac{dy}{dx} = \dfrac{y - \sqrt{y^2 - x^2}}{x}$

$\dfrac{dy}{dx} = \dfrac{y}{x} - \sqrt{\dfrac{y^2 - x^2}{x^2}}$

$\dfrac{dy}{dx} = \dfrac{y}{x} - \sqrt{\dfrac{y^2}{x^2} - 1}$

Comparing this with the given expression $\dfrac{dy}{dx} = K - \sqrt{\dfrac{y^2}{x^2} - 1}$, we get:

$K = \dfrac{y}{x}$

Answer: $\dfrac{y}{x}$

</details>

---

### Q7. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $x^m + y^m = k, (m \neq 1)$ and $y'' = \dfrac{ax^b}{y^c}$ such that $a + b + c = 0$, then the value of k is...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $m$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Differentiating $x^m + y^m = k$ with respect to $x$:

$m x^{m-1} + m y^{m-1} y' = 0$

$y' = -x^{m-1} y^{1-m}$

Differentiating again with respect to $x$:

$y'' = -(m-1) x^{m-2} y^{1-m} - x^{m-1} (1-m) y^{-m} y'$

Substituting $y' = -x^{m-1} y^{1-m}$:

$y'' = (1-m) x^{m-2} y^{1-m} - (1-m) x^{m-1} y^{-m} (-x^{m-1} y^{1-m})$

$y'' = (1-m) x^{m-2} y^{1-m} + (1-m) x^{2m-2} y^{1-2m}$

Factoring out $(1-m) x^{m-2} y^{1-2m}$:

$y'' = (1-m) x^{m-2} y^{1-2m} (y^m + x^m)$

Since $x^m + y^m = k$, we get:

$y'' = \dfrac{k(1-m) x^{m-2}}{y^{2m-1}}$

Comparing this with $y'' = \dfrac{ax^b}{y^c}$, we obtain:

$a = k(1-m)$

$b = m-2$

$c = 2m-1$

Given $a + b + c = 0$, we have:

$k(1-m) + (m-2) + (2m-1) = 0$

$k(1-m) + 3m - 3 = 0$

$k(1-m) - 3(1-m) = 0$

$(k - 3)(1 - m) = 0$

Since $m \neq 1$, it follows that $k = 3$.

Answer: $3$

</details>

---

### Q8. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $3y^2 - 2xy - x = 0$, then the value of $\dfrac{dy}{dx}$ at $y = 2$ is...

**Options:**

- **(A)** $\dfrac{5}{36}$
- **(B)** $\dfrac{35}{36}$
- **(C)** $\dfrac{25}{36}$
- **(D)** $\dfrac{36}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{25}{36}$**

**Detailed Solution:**

Given equation is $3y^2 - 2xy - x = 0$.

Substituting $y = 2$ in the equation:

$3(2)^2 - 2x(2) - x = 0$

$12 - 4x - x = 0$

$5x = 12 \Rightarrow x = \dfrac{12}{5}$

Differentiating the given equation with respect to $x$:

$\dfrac{d}{dx}(3y^2 - 2xy - x) = 0$

$6y \dfrac{dy}{dx} - 2\left(y + x \dfrac{dy}{dx}\right) - 1 = 0$

$(6y - 2x) \dfrac{dy}{dx} = 2y + 1$

$\dfrac{dy}{dx} = \dfrac{2y + 1}{6y - 2x}$

Substituting $x = \dfrac{12}{5}$ and $y = 2$:

$\dfrac{dy}{dx} = \dfrac{2(2) + 1}{6(2) - 2\left(\dfrac{12}{5}\right)}$

$\dfrac{dy}{dx} = \dfrac{5}{12 - \dfrac{24}{5}}$

$\dfrac{dy}{dx} = \dfrac{5}{\dfrac{36}{5}} = \dfrac{25}{36}$

Answer: $\dfrac{25}{36}$

</details>

---

### Q9. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $y = \sqrt[p]{x^3 y}$. If $\dfrac{dy}{dx} = \dfrac{3}{2}$ when $y = 1$, then the value of $p$ is equal to $\ldots$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

Given $y = \sqrt[p]{x^3 y}$

Raising both sides to the power $p$:

$y^p = x^3 y$

$y^{p-1} = x^3$

Differentiating both sides with respect to $x$:

$(p-1) y^{p-2} \dfrac{dy}{dx} = 3x^2$

When $y = 1$, from $y^{p-1} = x^3$, we get $x^3 = 1 \Rightarrow x = 1$.

Substituting $x = 1$, $y = 1$, and $\dfrac{dy}{dx} = \dfrac{3}{2}$ into the differentiated equation:

$(p-1) (1)^{p-2} \left(\dfrac{3}{2}\right) = 3(1)^2$

$(p-1) \dfrac{3}{2} = 3$

$p - 1 = 2$

$p = 3$

Answer: $3$

</details>

---

### Q10. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x\,e^{xy} = y + \sin^2 x$, then the value of $\dfrac{dy}{dx}$ at $x = 0$ is equal to

**Options:**

- **(A)** $-1$
- **(B)** $1$
- **(C)** $-2$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

Given equation is $x e^{xy} = y + \sin^2 x$.

Substituting $x = 0$ to find the corresponding value of $y$:

$0 \cdot e^0 = y + \sin^2 0 \Rightarrow y = 0$

Differentiating the given equation with respect to $x$:

$\dfrac{d}{dx}(x e^{xy}) = \dfrac{d}{dx}(y + \sin^2 x)$

$e^{xy} + x e^{xy} \left(y + x \dfrac{dy}{dx}\right) = \dfrac{dy}{dx} + 2 \sin x \cos x$

Substituting $x = 0$ and $y = 0$ into the differentiated equation:

$e^0 + 0 \cdot e^0 \left(0 + 0 \cdot \dfrac{dy}{dx}\right) = \dfrac{dy}{dx} + 2 \sin 0 \cos 0$

$1 + 0 = \dfrac{dy}{dx} + 0$

$\dfrac{dy}{dx} = 1$

Answer: $1$

</details>

---

### Q11. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y^{\frac{1}{m}} + y^{\frac{-1}{m}} = 2x$ , then $(x^2 - 1)y_1^{\ 2} =$

**Options:**

- **(A)** $my^2$
- **(B)** $m^2 y^2$
- **(C)** $m^2 y$
- **(D)** $my$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $m^2 y^2$**

**Detailed Solution:**

Given $y^{\dfrac{1}{m}} + y^{-\dfrac{1}{m}} = 2x$

Differentiating both sides with respect to $x$:

$\dfrac{1}{m} y^{\dfrac{1}{m} - 1} y_1 - \dfrac{1}{m} y^{-\dfrac{1}{m} - 1} y_1 = 2$

$\dfrac{y_1}{m y} \left( y^{\dfrac{1}{m}} - y^{-\dfrac{1}{m}} \right) = 2$

$y_1 \left( y^{\dfrac{1}{m}} - y^{-\dfrac{1}{m}} \right) = 2my$

Squaring both sides:

$y_1^2 \left( y^{\dfrac{1}{m}} - y^{-\dfrac{1}{m}} \right)^2 = 4m^2 y^2$

Using the identity $(a - b)^2 = (a + b)^2 - 4ab$:

$y_1^2 \left[ \left( y^{\dfrac{1}{m}} + y^{-\dfrac{1}{m}} \right)^2 - 4 \right] = 4m^2 y^2$

Substituting $y^{\dfrac{1}{m}} + y^{-\dfrac{1}{m}} = 2x$:

$y_1^2 \left[ (2x)^2 - 4 \right] = 4m^2 y^2$

$y_1^2 (4x^2 - 4) = 4m^2 y^2$

$4(x^2 - 1)y_1^2 = 4m^2 y^2$

$(x^2 - 1)y_1^2 = m^2 y^2$

Answer: $m^2 y^2$

</details>

---

### Q12. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $e^y + xy = e$, then the ordered pair $\left(\dfrac{\text{d}y}{\text{d}x}, \dfrac{\text{d}^2 y}{\text{d}x^2}\right)$ at $x = 0$ is equal to

**Options:**

- **(A)** $\left(\dfrac{1}{e}, \dfrac{-1}{e^2}\right)$
- **(B)** $\left(\dfrac{-1}{e}, \dfrac{1}{e^2}\right)$
- **(C)** $\left(\dfrac{1}{e}, \dfrac{1}{e^2}\right)$
- **(D)** $\left(\dfrac{-1}{e}, \dfrac{-1}{e^2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\dfrac{-1}{e}, \dfrac{1}{e^2}\right)$**

**Detailed Solution:**

Given equation is $e^y + xy = e$.

Substituting $x = 0$ in the given equation:
$e^y + 0 = e \Rightarrow y = 1$

Differentiating the given equation with respect to $x$:
$e^y \dfrac{\text{d}y}{\text{d}x} + y + x \dfrac{\text{d}y}{\text{d}x} = 0$

Substituting $x = 0$ and $y = 1$:
$e^1 \dfrac{\text{d}y}{\text{d}x} + 1 + 0 = 0 \Rightarrow \dfrac{\text{d}y}{\text{d}x} = \dfrac{-1}{e}$

Differentiating again with respect to $x$:
$e^y \left(\dfrac{\text{d}y}{\text{d}x}\right)^2 + e^y \dfrac{\text{d}^2 y}{\text{d}x^2} + \dfrac{\text{d}y}{\text{d}x} + \dfrac{\text{d}y}{\text{d}x} + x \dfrac{\text{d}^2 y}{\text{d}x^2} = 0$

$e^y \left(\dfrac{\text{d}y}{\text{d}x}\right)^2 + 2\dfrac{\text{d}y}{\text{d}x} + (e^y + x) \dfrac{\text{d}^2 y}{\text{d}x^2} = 0$

Substituting $x = 0$, $y = 1$, and $\dfrac{\text{d}y}{\text{d}x} = \dfrac{-1}{e}$:
$e \left(\dfrac{-1}{e}\right)^2 + 2\left(\dfrac{-1}{e}\right) + (e + 0) \dfrac{\text{d}^2 y}{\text{d}x^2} = 0$

$\dfrac{1}{e} - \dfrac{2}{e} + e \dfrac{\text{d}^2 y}{\text{d}x^2} = 0$

$-\dfrac{1}{e} + e \dfrac{\text{d}^2 y}{\text{d}x^2} = 0 \Rightarrow \dfrac{\text{d}^2 y}{\text{d}x^2} = \dfrac{1}{e^2}$

Therefore, the ordered pair $\left(\dfrac{\text{d}y}{\text{d}x}, \dfrac{\text{d}^2 y}{\text{d}x^2}\right)$ is $\left(\dfrac{-1}{e}, \dfrac{1}{e^2}\right)$.

Answer: $\left(\dfrac{-1}{e}, \dfrac{1}{e^2}\right)$

</details>

---

### Q13. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{y+x} + \sqrt{y-x} = c$ such that $\dfrac{dy}{dx} = f(x) - \sqrt{[f(x)]^2 - 1}$, then $f(x) =$ ____

**Options:**

- **(A)** $\dfrac{y}{x}$
- **(B)** $-\dfrac{x}{y}$
- **(C)** $-\dfrac{y}{x}$
- **(D)** $\dfrac{x}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{y}{x}$**

**Detailed Solution:**

Given equation: $\sqrt{y+x} + \sqrt{y-x} = c$

Differentiating both sides with respect to $x$:

$\dfrac{1}{2\sqrt{y+x}} \left(\dfrac{dy}{dx} + 1\right) + \dfrac{1}{2\sqrt{y-x}} \left(\dfrac{dy}{dx} - 1\right) = 0$

$\dfrac{dy}{dx} \left( \dfrac{1}{\sqrt{y+x}} + \dfrac{1}{\sqrt{y-x}} \right) = \dfrac{1}{\sqrt{y-x}} - \dfrac{1}{\sqrt{y+x}}$

$\dfrac{dy}{dx} \left( \dfrac{\sqrt{y-x} + \sqrt{y+x}}{\sqrt{y^2-x^2}} \right) = \dfrac{\sqrt{y+x} - \sqrt{y-x}}{\sqrt{y^2-x^2}}$

$\dfrac{dy}{dx} = \dfrac{\sqrt{y+x} - \sqrt{y-x}}{\sqrt{y+x} + \sqrt{y-x}}$

Rationalizing the denominator by multiplying the numerator and denominator by $\sqrt{y+x} - \sqrt{y-x}$:

$\dfrac{dy}{dx} = \dfrac{(\sqrt{y+x} - \sqrt{y-x})^2}{(\sqrt{y+x})^2 - (\sqrt{y-x})^2}$

$\dfrac{dy}{dx} = \dfrac{(y+x) + (y-x) - 2\sqrt{y^2-x^2}}{(y+x) - (y-x)}$

$\dfrac{dy}{dx} = \dfrac{2y - 2\sqrt{y^2-x^2}}{2x}$

$\dfrac{dy}{dx} = \dfrac{y}{x} - \dfrac{\sqrt{y^2-x^2}}{x}$

$\dfrac{dy}{dx} = \dfrac{y}{x} - \sqrt{\left(\dfrac{y}{x}\right)^2 - 1}$

Comparing this with the given equation $\dfrac{dy}{dx} = f(x) - \sqrt{[f(x)]^2 - 1}$, we get:

$f(x) = \dfrac{y}{x}$

Answer: $\dfrac{y}{x}$

</details>

---

### Q14. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^3 + y^3 = 6$ and $\dfrac{d^2y}{dx^2} \cdot \dfrac{d^2x}{dy^2} = \dfrac{m}{(xy)^n}$, where $m, n \in R$ then $\dfrac{m}{n} = $

**Options:**

- **(A)** $36$
- **(B)** $9$
- **(C)** $6$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $36$**

**Detailed Solution:**

Given $x^3 + y^3 = 6$.

Differentiating with respect to $x$, we get:

$3x^2 + 3y^2 \dfrac{dy}{dx} = 0 \Rightarrow \dfrac{dy}{dx} = -\dfrac{x^2}{y^2}$

Differentiating again with respect to $x$:

$\dfrac{d^2y}{dx^2} = -\dfrac{d}{dx}\left(\dfrac{x^2}{y^2}\right) = -\dfrac{y^2(2x) - x^2\left(2y \dfrac{dy}{dx}\right)}{y^4}$

Substituting $\dfrac{dy}{dx} = -\dfrac{x^2}{y^2}$:

$\dfrac{d^2y}{dx^2} = -\dfrac{2xy^2 - 2x^2y\left(-\dfrac{x^2}{y^2}\right)}{y^4} = -\dfrac{2xy^2 + \dfrac{2x^4}{y}}{y^4} = -\dfrac{2x(y^3 + x^3)}{y^5}$

Since $x^3 + y^3 = 6$:

$\dfrac{d^2y}{dx^2} = -\dfrac{12x}{y^5}$

By symmetry, differentiating $x^3 + y^3 = 6$ with respect to $y$ twice gives:

$\dfrac{d^2x}{dy^2} = -\dfrac{12y}{x^5}$

Multiplying the two second derivatives:

$\dfrac{d^2y}{dx^2} \cdot \dfrac{d^2x}{dy^2} = \left(-\dfrac{12x}{y^5}\right) \left(-\dfrac{12y}{x^5}\right) = \dfrac{144xy}{x^5y^5} = \dfrac{144}{(xy)^4}$

Comparing with $\dfrac{m}{(xy)^n}$, we get $m = 144$ and $n = 4$.

Therefore, $\dfrac{m}{n} = \dfrac{144}{4} = 36$.

Answer: $36$

</details>

---

### Q15. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $y = \sqrt{\tan x + \sqrt{\tan x + \sqrt{\tan x + \cdots \cdots \cdots \infty}}}$, then $\left(\dfrac{dy}{dx}\right)^2$ at $x = \dfrac{\pi}{4}$ is

**Options:**

- **(A)** $\dfrac{5}{4}$
- **(B)** $\dfrac{-5}{4}$
- **(C)** $\dfrac{4}{5}$
- **(D)** $\dfrac{-4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{4}{5}$**

**Detailed Solution:**

Given $y = \sqrt{\tan x + \sqrt{\tan x + \sqrt{\tan x + \cdots \infty}}}$

Squaring both sides, we get:

$y^2 = \tan x + y$

Differentiating both sides with respect to $x$:

$2y \dfrac{dy}{dx} = \sec^2 x + \dfrac{dy}{dx}$

$\dfrac{dy}{dx} (2y - 1) = \sec^2 x$

$\dfrac{dy}{dx} = \dfrac{\sec^2 x}{2y - 1}$

At $x = \dfrac{\pi}{4}$, $\tan x = 1$. Substituting this into the equation for $y$:

$y^2 - y - 1 = 0$

Solving for $y$, we get $y = \dfrac{1 \pm \sqrt{5}}{2}$. Since $y$ represents a principal square root, $y > 0$, so $y = \dfrac{1 + \sqrt{5}}{2}$.

Substituting $y = \dfrac{1 + \sqrt{5}}{2}$ and $x = \dfrac{\pi}{4}$ into the derivative:

$2y - 1 = 2\left(\dfrac{1 + \sqrt{5}}{2}\right) - 1 = \sqrt{5}$

$\sec^2\left(\dfrac{\pi}{4}\right) = (\sqrt{2})^2 = 2$

$\dfrac{dy}{dx} = \dfrac{2}{\sqrt{5}}$

Squaring both sides:

$\left(\dfrac{dy}{dx}\right)^2 = \dfrac{4}{5}$

Answer: $\dfrac{4}{5}$

</details>

---

### Q16. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x \cdot \log _{\mathrm{e}}\left(\log _{\mathrm{e}} x\right)-x^2+\mathrm{y}^2=4(\mathrm{y}>0)$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=\mathrm{e}$ is

**Options:**

- **(A)** $\frac{\mathrm{e}}{\sqrt{4+\mathrm{e}^2}}$
- **(B)** $\frac{2 e-1}{2 \sqrt{4+e^2}}$
- **(C)** $\frac{1+2 \mathrm{e}}{\sqrt{4+\mathrm{e}^2}}$
- **(D)** $\frac{1+2 e}{2 \sqrt{4+e^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 e-1}{2 \sqrt{4+e^2}}$**

**Detailed Solution:**

Given equation is $x \cdot \log_{\mathrm{e}}(\log_{\mathrm{e}} x) - x^2 + \mathrm{y}^2 = 4$.

Substitute $x = \mathrm{e}$ to find $\mathrm{y}$:

$\mathrm{e} \cdot \log_{\mathrm{e}}(\log_{\mathrm{e}} \mathrm{e}) - \mathrm{e}^2 + \mathrm{y}^2 = 4$

Since $\log_{\mathrm{e}} \mathrm{e} = 1$ and $\log_{\mathrm{e}} 1 = 0$, we get:

$0 - \mathrm{e}^2 + \mathrm{y}^2 = 4 \Rightarrow \mathrm{y}^2 = 4 + \mathrm{e}^2$

Since $\mathrm{y} > 0$, $\mathrm{y} = \sqrt{4 + \mathrm{e}^2}$.

Differentiating the given equation with respect to $x$:

$\log_{\mathrm{e}}(\log_{\mathrm{e}} x) \cdot 1 + x \cdot \dfrac{1}{\log_{\mathrm{e}} x} \cdot \dfrac{1}{x} - 2x + 2\mathrm{y} \dfrac{\mathrm{dy}}{\mathrm{d}x} = 0$

$\log_{\mathrm{e}}(\log_{\mathrm{e}} x) + \dfrac{1}{\log_{\mathrm{e}} x} - 2x + 2\mathrm{y} \dfrac{\mathrm{dy}}{\mathrm{d}x} = 0$

Substitute $x = \mathrm{e}$ and $\mathrm{y} = \sqrt{4 + \mathrm{e}^2}$:

$\log_{\mathrm{e}}(1) + \dfrac{1}{1} - 2\mathrm{e} + 2\sqrt{4 + \mathrm{e}^2} \dfrac{\mathrm{dy}}{\mathrm{d}x} = 0$

$0 + 1 - 2\mathrm{e} + 2\sqrt{4 + \mathrm{e}^2} \dfrac{\mathrm{dy}}{\mathrm{d}x} = 0$

$2\sqrt{4 + \mathrm{e}^2} \dfrac{\mathrm{dy}}{\mathrm{d}x} = 2\mathrm{e} - 1$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = \dfrac{2\mathrm{e} - 1}{2\sqrt{4 + \mathrm{e}^2}}$

Answer: $\frac{2 e-1}{2 \sqrt{4+e^2}}$

</details>

---

### Q17. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Derivative of
$\mathrm{y}=\sqrt{\sin x+\sqrt{\sin x+\sqrt{\sin x+\ldots \ldots \ldots \ldots \ldots}} \infty}$ is

**Options:**

- **(A)** $\frac{\sin x}{1-2 y}$
- **(B)** $\frac{\cos x}{1-2 y}$
- **(C)** $\frac{\sin x}{1+2 y}$
- **(D)** $\frac{\cos x}{2 y-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\cos x}{2 y-1}$**

**Detailed Solution:**

Given $y = \sqrt{\sin x + \sqrt{\sin x + \sqrt{\sin x + \dots \infty}}}$

Squaring both sides, we get:

$y^2 = \sin x + y$

Differentiating both sides with respect to $x$:

$2y \dfrac{dy}{dx} = \cos x + \dfrac{dy}{dx}$

$2y \dfrac{dy}{dx} - \dfrac{dy}{dx} = \cos x$

$(2y - 1) \dfrac{dy}{dx} = \cos x$

$\dfrac{dy}{dx} = \dfrac{\cos x}{2y - 1}$

Answer: $\frac{\cos x}{2 y-1}$

</details>

---

### Q18. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{e}^{\mathrm{y}}+x \mathrm{y}=\mathrm{e}$, then the ordered pair $\left(\frac{\mathrm{dy}}{\mathrm{d} x}, \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}\right)$ at $x=0$ is equal to

**Options:**

- **(A)** $\left(-\frac{1}{e}, \frac{1}{e^2} \right)$
- **(B)** $\left(\frac{1}{e}, \frac{1}{e^2} \right)$
- **(C)** $\left(-\frac{1}{e}, -\frac{1}{e^2} \right)$
- **(D)** $\left(\frac{1}{e}, -\frac{1}{e^2} \right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(-\frac{1}{e}, \frac{1}{e^2} \right)$**

**Detailed Solution:**

Given equation: $\mathrm{e}^{\mathrm{y}} + x\mathrm{y} = \mathrm{e}$

Substitute $x = 0$ into the equation:

$\mathrm{e}^{\mathrm{y}} + 0 = \mathrm{e} \Rightarrow \mathrm{y} = 1$

Differentiating the given equation with respect to $x$:

$\mathrm{e}^{\mathrm{y}} \dfrac{\mathrm{dy}}{\mathrm{d}x} + \mathrm{y} + x \dfrac{\mathrm{dy}}{\mathrm{d}x} = 0$

Substitute $x = 0$ and $\mathrm{y} = 1$:

$\mathrm{e} \dfrac{\mathrm{dy}}{\mathrm{d}x} + 1 + 0 = 0 \Rightarrow \dfrac{\mathrm{dy}}{\mathrm{d}x} = -\dfrac{1}{\mathrm{e}}$

Differentiating again with respect to $x$:

$\mathrm{e}^{\mathrm{y}} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} + \mathrm{e}^{\mathrm{y}} \left(\dfrac{\mathrm{dy}}{\mathrm{d}x}\right)^2 + \dfrac{\mathrm{dy}}{\mathrm{d}x} + \dfrac{\mathrm{dy}}{\mathrm{d}x} + x \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = 0$

$\mathrm{e}^{\mathrm{y}} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} + \mathrm{e}^{\mathrm{y}} \left(\dfrac{\mathrm{dy}}{\mathrm{d}x}\right)^2 + 2\dfrac{\mathrm{dy}}{\mathrm{d}x} + x \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = 0$

Substitute $x = 0$, $\mathrm{y} = 1$, and $\dfrac{\mathrm{dy}}{\mathrm{d}x} = -\dfrac{1}{\mathrm{e}}$:

$\mathrm{e} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} + \mathrm{e} \left(-\dfrac{1}{\mathrm{e}}\right)^2 + 2\left(-\dfrac{1}{\mathrm{e}}\right) + 0 = 0$

$\mathrm{e} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} + \dfrac{1}{\mathrm{e}} - \dfrac{2}{\mathrm{e}} = 0$

$\mathrm{e} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} - \dfrac{1}{\mathrm{e}} = 0$

$\mathrm{e} \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \dfrac{1}{\mathrm{e}} \Rightarrow \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \dfrac{1}{\mathrm{e}^2}$

Therefore, the ordered pair $\left(\dfrac{\mathrm{dy}}{\mathrm{d}x}, \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2}\right)$ at $x = 0$ is $\left(-\dfrac{1}{\mathrm{e}}, \dfrac{1}{\mathrm{e}^2}\right)$.

Answer: $\left(-\frac{1}{e}, \frac{1}{e^2} \right)$

</details>

---

### Q19. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{y-\sqrt{y-\sqrt{y-\ldots \ldots \ldots \ldots \ldots \ldots \infty}}}=\sqrt{x+\sqrt{x+\sqrt{x+\ldots \ldots \ldots \ldots \ldots \ldots \ldots \infty}}}$ , then $\frac{\mathrm{dy}}{\mathrm{d} x}=$

**Options:**

- **(A)** $\frac{y+x+1}{y-x+1}$
- **(B)** $\frac{y-x-1}{y-x+1}$
- **(C)** $\frac{y-x+1}{y-x-1}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{y-x+1}{y-x-1}$**

**Detailed Solution:**

Let $u = \sqrt{y-\sqrt{y-\sqrt{y-\ldots \infty}}}$.

Then $u = \sqrt{y - u} \Rightarrow u^2 = y - u \Rightarrow y = u^2 + u$

Let $v = \sqrt{x+\sqrt{x+\sqrt{x+\ldots \infty}}}$.

Then $v = \sqrt{x + v} \Rightarrow v^2 = x + v \Rightarrow x = v^2 - v$

Given that the two expressions are equal, we have $u = v$.

Thus, $y = u^2 + u$ and $x = u^2 - u$.

Subtracting the two equations, we get:

$y - x = (u^2 + u) - (u^2 - u) = 2u$

Differentiating $y$ and $x$ with respect to $u$:

$\dfrac{\mathrm{d}y}{\mathrm{d}u} = 2u + 1$

$\dfrac{\mathrm{d}x}{\mathrm{d}u} = 2u - 1$

Now, finding $\dfrac{\mathrm{d}y}{\mathrm{d}x}$ using the parametric differentiation:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{\dfrac{\mathrm{d}y}{\mathrm{d}u}}{\dfrac{\mathrm{d}x}{\mathrm{d}u}} = \dfrac{2u + 1}{2u - 1}$

Substituting $2u = y - x$ into the above expression:

$\dfrac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{y - x + 1}{y - x - 1}$

Answer: $\frac{y-x+1}{y-x-1}$

</details>

---

### Q20. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{y}=\sqrt{x+\sqrt{\mathrm{y}+\sqrt{x+\sqrt{\mathrm{y}+\ldots \ldots \ldots \ldots \ldots \ldots \ldots \infty}}}}$, then $\frac{\mathrm{dy}}{\mathrm{d} x}=$

**Options:**

- **(A)** $2 y-1$
- **(B)** $\frac{1}{2 y-1}$
- **(C)** $\frac{y^2-x}{2 y^3-2 x y-1}$
- **(D)** ${ }^{14} C_6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{y^2-x}{2 y^3-2 x y-1}$**

**Detailed Solution:**

Given equation is $y = \sqrt{x + \sqrt{y + \sqrt{x + \sqrt{y + \dots \infty}}}}$

Squaring both sides, we get:

$y^2 = x + \sqrt{y + \sqrt{x + \sqrt{y + \dots \infty}}}$

$y^2 - x = \sqrt{y + \sqrt{x + \sqrt{y + \dots \infty}}}$

Squaring both sides again, we get:

$(y^2 - x)^2 = y + \sqrt{x + \sqrt{y + \dots \infty}}$

Since the infinite nested radical repeats itself, the term $\sqrt{x + \sqrt{y + \dots \infty}}$ is exactly equal to $y$. Substituting this back, we get:

$(y^2 - x)^2 = y + y$

$(y^2 - x)^2 = 2y$

Differentiating both sides with respect to $x$:

$2(y^2 - x) \dfrac{d}{dx}(y^2 - x) = 2 \dfrac{dy}{dx}$

$2(y^2 - x) \left(2y \dfrac{dy}{dx} - 1\right) = 2 \dfrac{dy}{dx}$

Dividing by $2$ on both sides:

$(y^2 - x) \left(2y \dfrac{dy}{dx} - 1\right) = \dfrac{dy}{dx}$

$2y(y^2 - x) \dfrac{dy}{dx} - (y^2 - x) = \dfrac{dy}{dx}$

$(2y^3 - 2xy) \dfrac{dy}{dx} - \dfrac{dy}{dx} = y^2 - x$

$\dfrac{dy}{dx} (2y^3 - 2xy - 1) = y^2 - x$

$\dfrac{dy}{dx} = \dfrac{y^2 - x}{2y^3 - 2xy - 1}$

Answer: $\frac{y^2-x}{2 y^3-2 x y-1}$

</details>

---

### Q21. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $(\mathrm{a}+\mathrm{b} x) \mathrm{e}^{\frac{\mathrm{y}}{x}}=x$, then $x^3 \frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}$ is equal to

**Options:**

- **(A)** $\left(\mathrm{y} \frac{\mathrm{dy}}{\mathrm{d} x}-x\right)^2$
- **(B)** $\left(x \frac{\mathrm{dy}}{\mathrm{d} x}-\mathrm{y}\right)^2$
- **(C)** $\left(x \frac{\mathrm{dy}}{\mathrm{d} x}+\mathrm{y}\right)^2$
- **(D)** $\left(\mathrm{y} \frac{\mathrm{dy}}{\mathrm{d} x}+x\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(x \frac{\mathrm{dy}}{\mathrm{d} x}-\mathrm{y}\right)^2$**

**Detailed Solution:**

Given equation: $(\mathrm{a}+\mathrm{b}x)\mathrm{e}^{\dfrac{\mathrm{y}}{x}} = x$

Taking the natural logarithm on both sides:

$\ln(\mathrm{a}+\mathrm{b}x) + \dfrac{\mathrm{y}}{x} = \ln x$

$\dfrac{\mathrm{y}}{x} = \ln x - \ln(\mathrm{a}+\mathrm{b}x)$

Differentiating both sides with respect to $x$:

$\dfrac{x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y}}{x^2} = \dfrac{1}{x} - \dfrac{\mathrm{b}}{\mathrm{a}+\mathrm{b}x}$

$\dfrac{x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y}}{x^2} = \dfrac{\mathrm{a}+\mathrm{b}x - \mathrm{b}x}{x(\mathrm{a}+\mathrm{b}x)}$

$\dfrac{x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y}}{x^2} = \dfrac{\mathrm{a}}{x(\mathrm{a}+\mathrm{b}x)}$

Multiplying by $x^2$ on both sides:

$x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y} = \dfrac{\mathrm{a}x}{\mathrm{a}+\mathrm{b}x}$

Differentiating again with respect to $x$:

$\dfrac{\mathrm{dy}}{\mathrm{d}x} + x \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} - \dfrac{\mathrm{dy}}{\mathrm{d}x} = \dfrac{\mathrm{a}(\mathrm{a}+\mathrm{b}x) - \mathrm{a}x(\mathrm{b})}{(\mathrm{a}+\mathrm{b}x)^2}$

$x \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \dfrac{\mathrm{a}^2 + \mathrm{ab}x - \mathrm{ab}x}{(\mathrm{a}+\mathrm{b}x)^2}$

$x \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \dfrac{\mathrm{a}^2}{(\mathrm{a}+\mathrm{b}x)^2}$

Multiplying both sides by $x^2$:

$x^3 \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \dfrac{\mathrm{a}^2 x^2}{(\mathrm{a}+\mathrm{b}x)^2} = \left(\dfrac{\mathrm{a}x}{\mathrm{a}+\mathrm{b}x}\right)^2$

Substituting $\dfrac{\mathrm{a}x}{\mathrm{a}+\mathrm{b}x} = x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y}$ into the equation:

$x^3 \dfrac{\mathrm{d}^2\mathrm{y}}{\mathrm{d}x^2} = \left(x \dfrac{\mathrm{dy}}{\mathrm{d}x} - \mathrm{y}\right)^2$

Answer: $\left(x \frac{\mathrm{dy}}{\mathrm{d} x}-\mathrm{y}\right)^2$

</details>

---

### Q22. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x^{\mathrm{y}}+\mathrm{y}^x=\mathrm{a}^{\mathrm{b}}$, then $\frac{\mathrm{dy}}{\mathrm{d} x}$ at $x=1, \mathrm{y}=2$ is

**Options:**

- **(A)** $-2(1+\log 2)$
- **(B)** $2(1+\log 2)$
- **(C)** $2+\log 2$
- **(D)** $1+\log 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-2(1+\log 2)$**

**Detailed Solution:**

Given $x^{\mathrm{y}} + \mathrm{y}^x = \mathrm{a}^{\mathrm{b}}$

Differentiating both sides with respect to $x$:

$\dfrac{\mathrm{d}}{\mathrm{d}x}(x^{\mathrm{y}}) + \dfrac{\mathrm{d}}{\mathrm{d}x}(\mathrm{y}^x) = 0$

Using the formula $\dfrac{\mathrm{d}}{\mathrm{d}x}(u^v) = u^v \left( \dfrac{v}{u} \dfrac{\mathrm{d}u}{\mathrm{d}x} + \log u \dfrac{\mathrm{d}v}{\mathrm{d}x} \right)$:

$x^{\mathrm{y}} \left( \dfrac{\mathrm{y}}{x} + \log x \dfrac{\mathrm{dy}}{\mathrm{d}x} \right) + \mathrm{y}^x \left( \dfrac{x}{\mathrm{y}} \dfrac{\mathrm{dy}}{\mathrm{d}x} + \log \mathrm{y} \right) = 0$

Substituting $x = 1$ and $\mathrm{y} = 2$:

$1^2 \left( \dfrac{2}{1} + \log 1 \dfrac{\mathrm{dy}}{\mathrm{d}x} \right) + 2^1 \left( \dfrac{1}{2} \dfrac{\mathrm{dy}}{\mathrm{d}x} + \log 2 \right) = 0$

Since $\log 1 = 0$, we get:

$1(2 + 0) + 2 \left( \dfrac{1}{2} \dfrac{\mathrm{dy}}{\mathrm{d}x} + \log 2 \right) = 0$

$2 + \dfrac{\mathrm{dy}}{\mathrm{d}x} + 2\log 2 = 0$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = -2 - 2\log 2$

$\dfrac{\mathrm{dy}}{\mathrm{d}x} = -2(1 + \log 2)$

Answer: $-2(1+\log 2)$

</details>

---

### Q23. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x^{\frac{2}{5}}+\mathrm{y}^{\frac{2}{5}}=a^{\frac{2}{5}}$ then $\frac{\mathrm{dy}}{\mathrm{d} x}=$

**Options:**

- **(A)** $\sqrt[5]{\left(\frac{\mathrm{y}}{x}\right)^3}$
- **(B)** $-\sqrt[5]{\left(\frac{x}{y}\right)^3}$
- **(C)** $\sqrt[5]{\left(\frac{x}{y}\right)^3}$
- **(D)** $-\sqrt[5]{\left(\frac{y}{x}\right)^3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\sqrt[5]{\left(\frac{y}{x}\right)^3}$**

**Detailed Solution:**

Given equation is $x^{\dfrac{2}{5}} + y^{\dfrac{2}{5}} = a^{\dfrac{2}{5}}$

Differentiating both sides with respect to $x$, we get

$\dfrac{2}{5} x^{\dfrac{2}{5}-1} + \dfrac{2}{5} y^{\dfrac{2}{5}-1} \dfrac{dy}{dx} = 0$

$x^{-\dfrac{3}{5}} + y^{-\dfrac{3}{5}} \dfrac{dy}{dx} = 0$

$y^{-\dfrac{3}{5}} \dfrac{dy}{dx} = -x^{-\dfrac{3}{5}}$

$\dfrac{dy}{dx} = -\dfrac{x^{-\dfrac{3}{5}}}{y^{-\dfrac{3}{5}}}$

$\dfrac{dy}{dx} = -\dfrac{y^{\dfrac{3}{5}}}{x^{\dfrac{3}{5}}}$

$\dfrac{dy}{dx} = -\left(\dfrac{y}{x}\right)^{\dfrac{3}{5}}$

$\dfrac{dy}{dx} = -\sqrt[5]{\left(\dfrac{y}{x}\right)^3}$

Answer: $-\sqrt[5]{\left(\frac{y}{x}\right)^3}$

</details>

---

### Q24. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=\sqrt{\dfrac{1-\sin ^{-1} x}{1+\sin ^{-1} x}}$, then $\left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)$ at $x=0$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** -2
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

Given $y = \sqrt{\dfrac{1 - \sin^{-1} x}{1 + \sin^{-1} x}}$

Taking natural logarithm on both sides:

$\ln y = \dfrac{1}{2} \left[ \ln(1 - \sin^{-1} x) - \ln(1 + \sin^{-1} x) \right]$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{dy}{dx} = \dfrac{1}{2} \left[ \dfrac{-1}{1 - \sin^{-1} x} \cdot \dfrac{1}{\sqrt{1 - x^2}} - \dfrac{1}{1 + \sin^{-1} x} \cdot \dfrac{1}{\sqrt{1 - x^2}} \right]$

At $x = 0$, $y = \sqrt{\dfrac{1 - 0}{1 + 0}} = 1$ and $\sin^{-1} 0 = 0$.

Substituting these values into the derivative equation:

$\dfrac{1}{1} \left(\dfrac{dy}{dx}\right)_{x=0} = \dfrac{1}{2} \left[ \dfrac{-1}{1 - 0} \cdot \dfrac{1}{\sqrt{1 - 0}} - \dfrac{1}{1 + 0} \cdot \dfrac{1}{\sqrt{1 - 0}} \right]$

$\left(\dfrac{dy}{dx}\right)_{x=0} = \dfrac{1}{2} ( -1 - 1 ) = -1$

</details>

---

### Q25. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $x>1$, if $(2 x)^{2 y}=4 \mathrm{e}^{2 x-2 y}$, then $\left(1+\log _e 2 x\right)^2 \frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $\frac{x \log _{\mathrm{e}} 2 x+\log _{\mathrm{e}} 2}{x}$
- **(B)** $\frac{x \log _e 2 x-\log _e 2}{x}$
- **(C)** $x \log _e 2 x+\frac{\log _e 2}{x}$
- **(D)** $x \log _{\mathrm{e}} 2 x-\frac{\log _{\mathrm{e}} 2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{x \log _e 2 x-\log _e 2}{x}$**

**Detailed Solution:**

$$
(2 x)^{2 y}=4 \mathrm{e}^{2 x-2 y}
$$

Taking ' $\log _{\mathrm{e}}$ ' on both sides, we get
$$
2 y \log _{\mathrm{e}}(2 x)=\log _{\mathrm{e}} 4+(2 x-2 y) \log _{\mathrm{e}} \mathrm{e}
$$
$$
\therefore \quad y \log _{\mathrm{e}}(2 x)=\log _{\mathrm{e}} 2+x-y
$$
Differentiating w.r.t. $x$, we get
$$
\begin{array}{ll} 
& {\left[\log _{\mathrm{e}} 2 x\right] \frac{\mathrm{d} y}{\mathrm{~d} x}+\frac{2 y}{2 x}=0+1-\frac{\mathrm{d} y}{\mathrm{~d} x}} \\
& {\left[1+\log _{\mathrm{e}} 2 x\right] \frac{\mathrm{d} y}{\mathrm{~d} x}=1-\frac{y}{x}} \\
& \text { Now, (i) } \Rightarrow y=\frac{\log _{\mathrm{e}} 2+x}{1+\log _{\mathrm{e}} 2 x} \\
\therefore \quad \ldots \text { (ii) } & \left(\text { ii) } \Rightarrow\left(1+\log _{\mathrm{e}} 2 x\right) \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x \log _{\mathrm{e}} 2 x-\log _{\mathrm{e}} 2}{x\left(1+\log _e 2 x\right)}\right. \\
\therefore \quad & \left(1+\log _{\mathrm{e}} 2 x\right)^2 \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{x \log _{\mathrm{e}} 2 x-\log _{\mathrm{e}} 2}{x}
\end{array}
$$

</details>

---

### Q26. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y$ is a function of $x$ and $\log (x+y)=2 x y$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** $0$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

$\log (x+y)=2 x y...(i)$
Differentiating both sides w.r.t. $x$, we get
$\begin{aligned}
& \left(\frac{1}{x+y}\right)\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)=2\left(x \frac{\mathrm{d} y}{\mathrm{~d} x}+y\right) \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{1-2 x y-2 y^2}{2 x^2+2 x y-1}
\end{aligned}$
Putting $x=0$ in (i), we get
$\begin{aligned}
& y=1 \\
\therefore \quad & \left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{x=0}=\frac{1-0-2}{0+0-1}=1
\end{aligned}$

</details>

---

### Q27. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x^y \cdot y^x=16$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $(2,2)$ is

**Options:**

- **(A)** -2
- **(B)** 2
- **(C)** 1
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -1**

**Detailed Solution:**

$x^y \cdot y^x=16$
$\Rightarrow y \log x+x \log y=\log 16$ [Taking log both sides]
Differentiating we get
$\frac{\mathrm{d} y}{\mathrm{~d} x} \cdot \log x+y \cdot \frac{1}{x}+\log y+x \cdot \frac{1}{y} \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}=0$
Putting $x=2$ and $y=0$
$\begin{aligned}
& \frac{\mathrm{d} y}{\mathrm{~d} x}(1+\log 2)=-(1+\log 2) \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-1
\end{aligned}$

</details>

---

### Q28. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\log (x+y)=\log (x y)+a$, where a is constant, then $\frac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=2$ and $y=4$ is

**Options:**

- **(A)** $-4$
- **(B)** $-8$
- **(C)** 4
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4$**

**Detailed Solution:**

$\begin{aligned} & \log (x+y)=\log (x y)+a \\ & \Rightarrow \log \left(\frac{x+y}{x y}\right)=a \\ & \Rightarrow \frac{x+y}{x y}=e^a \\ & \Rightarrow \frac{1}{y}+\frac{1}{x}=e^a \\ & \Rightarrow-\frac{1}{y^2} \frac{\mathrm{d} y}{\mathrm{~d} x}-\frac{1}{x^2}=0 \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-\frac{y^2}{x^2} \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x} \quad=-\frac{4^2}{2^2}=-4\end{aligned}$

</details>

---

### Q29. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x y=\tan ^{-1}(x y)+\cot ^{-1}(x y)$, then $\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)_{(4,2)}=($ where $x, y \in I R)$

**Options:**

- **(A)** $\frac{-1}{2}$
- **(B)** -2
- **(C)** 2
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{-1}{2}$**

**Detailed Solution:**

$\begin{aligned}
& x y=\tan ^{-1}(x y)+\cot ^{-1}(x y) \\
& \Rightarrow x y=\frac{\pi}{2}
\end{aligned}$
diff. we get $1 \cdot y+x \cdot \frac{d y}{d x}=0$
$\begin{aligned}
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=\frac{-y}{x} \\
& \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x} \text { at, }(4,2)=\frac{-2}{4}=\frac{-1}{2}
\end{aligned}$

</details>

---

### Q30. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\log (x+y)=\log x y+3$, then $\frac{\mathrm{d} y}{\mathrm{~d} x}=$

**Options:**

- **(A)** $\left(\frac{y}{x}\right)^2$
- **(B)** $-\left(\frac{x}{y}\right)^2$
- **(C)** $-\left(\frac{y}{x}\right)^2$
- **(D)** $\left(\frac{x}{y}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-\left(\frac{y}{x}\right)^2$**

**Detailed Solution:**

$\begin{aligned} & \log (x+y)=\log x y+3 \\ & \Rightarrow \log \left(\frac{x+y}{x y}\right)=3 \\ & \Rightarrow \frac{x+y}{x y}=e^3 \\ & \Rightarrow \frac{1}{y}+\frac{1}{x}=e^3 \\ & \text { Diff } \frac{-1}{y^2} \frac{\mathrm{d} y}{\mathrm{~d} x}-\frac{1}{x^2}=0 \\ & \Rightarrow \frac{\mathrm{d} y}{\mathrm{~d} x}=-\frac{y^2}{x^2}\end{aligned}$

</details>

---

### Q31. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $e^x+e^y=e^{x+y}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $-e^{y-x}$
- **(B)** $e^{x-y}$
- **(C)** $-e^{x-y}$
- **(D)** $e^{y-x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-e^{y-x}$**

**Detailed Solution:**

$e^x+e^y=e^{x+y} \Rightarrow e^x+e^y \cdot \frac{d y}{d x}=e^{x+y}\left(1+\frac{d y}{d x}\right)$
$\Rightarrow \frac{d y}{d x}=\frac{e^x-e^{x+y}}{e^{x+y}-e^y}=\frac{e^x-e^x-e^y}{e^x+e^y-e^y}=-\frac{e^y}{e^x}=-e^{y-x}$

</details>

---

### Q32. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $x^y=e^{x-y}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{\log x}{1+\log x}$
- **(B)** $\frac{\log x}{x(1+\log x)^2}$
- **(C)** $\frac{\log x}{(1+\log x)^2}$
- **(D)** $\frac{x \log x}{(1+\log x)^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\log x}{(1+\log x)^2}$**

**Detailed Solution:**

$x^y=e^{x-y}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wx_miTJKgt6qxPRSyXA5qLcBKbzJYp6nGZJFftbL_7I.original.fullsize.png">
$\begin{aligned} & \Rightarrow \frac{d y}{d x} \log x+y \cdot \frac{1}{x}=1-\frac{d y}{d x} \\ & \Rightarrow \frac{d y}{d x}=\frac{x-y}{x(1+\log x)} \\ & \Rightarrow \frac{d y}{d x}=\frac{\log x}{(1+\log x)^2} \quad\left[\text { Putting } y=\frac{x}{1+\log x} \text { from (i)] }\right.\end{aligned}$

</details>

---

### Q33. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $y^{\frac{1}{m}}+y^{\frac{-1}{m}}=2 x, x^1 1$, then $\left(x^2-1\right)\left(\frac{d y}{d x}\right)^2$ is equal to

**Options:**

- **(A)** $m^2 y$
- **(B)** $m^2 y^2$
- **(C)** $m y^2$
- **(D)** $\frac{m y^2}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $m^2 y^2$**

**Detailed Solution:**

$y^{\frac{1}{m}}+y^{-\frac{1}{m}}=2 x \Rightarrow y^{\frac{2}{m}}+y^{-\frac{2}{m}}+2=4 x^2 \ldots .$. (1) 
$\begin{aligned} & \frac{1}{m}\left(y^{\frac{1}{m}-1}-y^{-\frac{1}{m}-1}\right) \frac{d x}{d y}=2 \\ & \Rightarrow\left(y^{\frac{1}{m}}-y^{-\frac{1}{m}}\right)=\frac{2 m y}{\frac{d y}{d x}} \\ & \Rightarrow y^{\frac{2}{m}}+y^{-\frac{2}{m}}-2=\frac{4 m^2 y^2}{\left(\frac{d y}{d x}\right)^2} \ldots \ldots .(2) \text { [squaring both sides] }\end{aligned}$
from (1)-(2)
$\begin{aligned} & 4=4 x^2-\frac{4 m^2 y^2}{\left(\frac{d y}{d x}\right)^2} \Rightarrow 4\left(\frac{d y}{d x}\right)^2=4 x^2\left(\frac{d y}{d x}\right)^2-4 m^2 y^2 \\ & \Rightarrow\left(x^2-1\right)\left(\frac{d y}{d x}\right)^2=m^2 y^2\end{aligned}$

</details>

---

### Q34. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If
$\sqrt{y-\sqrt{y-\sqrt{y-\ldots \ldots \ldots \infty}}}=\sqrt{x+\sqrt{x+\sqrt{x+\ldots \ldots \ldots \infty}}}$ then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{y-x-1}{y-x+1}$
- **(B)** $\frac{y+x+1}{y+x+1}$
- **(C)** $\frac{y-x+1}{x+x+1}$
- **(D)** $\frac{y-x+1}{y-x-1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{y-x+1}{y-x-1}$**

**Detailed Solution:**

$\begin{aligned} & \text { Let } \sqrt{y-\sqrt{y-\sqrt{y-\ldots \ldots \infty}}}=\sqrt{x+\sqrt{x+\sqrt{x+\ldots \ldots \infty}}}=\mathrm{z} \\ & \Rightarrow \mathrm{y}-\mathrm{z}=\mathrm{z}^2 \text { and } \mathrm{x}+\mathrm{z}=\mathrm{z}^2 \\ & \Rightarrow \mathrm{y}=\mathrm{z}^2+\mathrm{z} \text { and } \mathrm{x}=\mathrm{z}^2-\mathrm{z} \\ & \Rightarrow \frac{\mathrm{dy}}{\mathrm{dz}}=2 \mathrm{z}+1 \text { and } \frac{\mathrm{dx}}{\mathrm{dz}}=2 \mathrm{z}-1 \text { also } 2 \mathrm{z}=\mathrm{y}-\mathrm{x} \\ & \Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{2 \mathrm{z}+1}{2 \mathrm{z}-1}=\frac{\mathrm{y}-\mathrm{x}+1}{\mathrm{y}-\mathrm{x}-1}\end{aligned}$

</details>

---

### Q35. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=1+x e^y$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{\mathrm{e}^{\mathrm{y}}}{2-\mathrm{y}}$
- **(B)** $\frac{e^y}{2+y}$
- **(C)** $\frac{\mathrm{e}^{\mathrm{y}}}{1-\mathrm{e}^{\mathrm{y}}}$
- **(D)** $\frac{\mathrm{e}^{\mathrm{y}}}{1+\mathrm{e}^{\mathrm{y}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{e}^{\mathrm{y}}}{2-\mathrm{y}}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{y}=1+\mathrm{xe}^{\mathrm{y}} \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=0+\mathrm{xe}^{\mathrm{y}} \frac{\mathrm{dy}}{\mathrm{dx}}+\mathrm{e}^{\mathrm{y}} \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}\left(\mathrm{xe}^{\mathrm{y}}-1\right)=-\mathrm{e}^{\mathrm{y}} \Rightarrow \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{-\mathrm{e}^{\mathrm{y}}}{\mathrm{xe}^{\mathrm{y}}-1} \\ & \therefore \frac{\mathrm{dy}}{\mathrm{dx}}=\frac{-\mathrm{e}^{\mathrm{y}}}{\left(1+\mathrm{xe}^{\mathrm{y}}\right)-2}=\frac{-\mathrm{e}^{\mathrm{y}}}{\mathrm{y}-2}=\frac{\mathrm{e}^{\mathrm{y}}}{2-\mathrm{y}}\end{aligned}$

</details>

---

### Q36. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin ^2 x+\cos ^2 y=1$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{\sin ^2 x}{\sin ^2 y}$
- **(B)** $\frac{\sin ^2 y}{\sin ^2 x}$
- **(C)** $\frac{\sin 2 x}{\sin 2 y}$
- **(D)** $\frac{-\sin ^2 y}{\sin ^2 x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\sin 2 x}{\sin 2 y}$**

**Detailed Solution:**

$\begin{aligned} & \sin ^2 x+\cos ^2 y=1 \\ & \therefore 2 \sin x \cos x-2 \cos y \sin y \frac{d y}{d x}=0 \\ & \therefore \frac{d y}{d x}=\frac{2 \sin x \cos x}{2 \sin y \cos y}=\frac{\sin 2 x}{\sin 2 y}\end{aligned}$

</details>

---

### Q37. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y=x \tan y$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{\tan x}{x-y^2}$
- **(B)** $\frac{y}{x-x^2-y^2}$
- **(C)** $\frac{\tan x}{x-x^2-y^2}$
- **(D)** $\frac{\tan y}{y-x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{y}{x-x^2-y^2}$**

**Detailed Solution:**

$\begin{aligned} & y=x \tan y \\ & \therefore \quad \frac{d y}{d x}=x \sec ^2 y \frac{d y}{d x}+\tan y \\ & \therefore \quad\left(x \sec ^2 y-1\right) \frac{d y}{d x}=-\tan y \\ & \therefore \quad \frac{d y}{d x}=\frac{-\tan y}{x \sec ^2 y-1}=\frac{-x \tan y}{x^2 \sec ^2 y-x} \\ & =\frac{-x \tan y}{x^2\left(1+\tan ^2 y\right)-x}=\frac{-x \tan y}{x^2+x^2 \tan ^2 y-x} \\ & \therefore \quad \frac{d y}{d x}=\frac{-y}{x^2+y^2-x}=\frac{y}{x-x^2-y^2} \cdot \cdots[\because y=x \tan y, \text { given }]\end{aligned}$

</details>

---

### Q38. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $e^{-y} \cdot y=x$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $\frac{y}{1-y}$
- **(B)** $\frac{1}{x y(1-y)}$
- **(C)** $\frac{1}{x(1-y)}$
- **(D)** $\frac{\mathrm{y}}{\mathrm{x}(1-\mathrm{y})}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{y}}{\mathrm{x}(1-\mathrm{y})}$**

**Detailed Solution:**

$$
\begin{aligned}
& e^{-y} \cdot y=x \\
& \therefore \frac{y}{e^y}=x \Rightarrow y=x e^y \ldots
\end{aligned}
$$
and
$$
\mathrm{e}^{\mathrm{y}}=\frac{\mathrm{y}}{\mathrm{x}}
$$
Now $y=\mathrm{xe}^{\mathrm{y}}$
$$
\begin{aligned}
& \therefore \frac{d y}{d x}=x e^y \frac{d y}{d x}+e^y \\
& \therefore \frac{d y}{d x}\left(x e^y-1\right)=-e^y \Rightarrow \frac{d y}{d x}=\frac{-e^y}{x e^y-1}
\end{aligned}
$$


From (1) and (2), we write
$$
\frac{d y}{d x}=-\left(\frac{y}{x}\right) \times \frac{1}{y-1}=\frac{-y}{x(y-1)}=\frac{y}{x(1-y)}
$$

</details>

---

### Q39. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{x}{\sqrt{1+x}}+\frac{y}{\sqrt{1+y}}=0, x \neq y$, then $\frac{d y}{d x}=0$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 0
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -1**

**Detailed Solution:**

(B)
$\begin{array}{l}
\frac{x}{\sqrt{1+x}}+\frac{y}{\sqrt{1+y}}=0 \\
x \cdot(\sqrt{1+y})+y(\sqrt{1+x})=0 \quad \Rightarrow x \cdot \sqrt{1+y}=-y \sqrt{1+x}
\end{array}$
Squaring both sides we get,
$\begin{array}{l}
x^{2}(1+y)=y^{2}(1+x) \Rightarrow x^{2}+x^{2} y=y^{2}+x y^{2} \\
x^{2}-y^{2}=x y^{2}-x^{2} y \Rightarrow(x-y)(x+y)=-x y(x-y) \\
x+y=-x y \Rightarrow(1+x) y=-x \Rightarrow y=\frac{-x}{1+x}
\end{array}$
Differentiating both sides w.r.t. $x$, we get
$\begin{aligned}
& \frac{d y}{d x}=-\frac{(1+x)(1)-(x)(1)}{(1+x)^{2}}=\frac{-1}{(1+x)^{2}} \\
\therefore &(1+x)^{2} \frac{d y}{d x}=-1
\end{aligned}$

</details>

---

### Q40. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{\frac{x}{y}}+\sqrt{\frac{y}{x}}=4$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{y-7 x}{7 x-y}$
- **(B)** $\frac{7 y-7 x}{y-7 x}$
- **(C)** $\frac{7 x+y}{x-7 y}$
- **(D)** $\frac{y+7 x}{7y-x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7 y-7 x}{y-7 x}$**

**Detailed Solution:**

(B)
Given : $\sqrt{\frac{x}{y}}+\sqrt{\frac{y}{x}}=4$
$\therefore \frac{x+y}{\sqrt{x y}}=4 \Rightarrow x+y=4 \sqrt{x y}$
Squaring both sides, we get,
$(x+y)^{2}=16 x y \Rightarrow x^{2}+y^{2}=14 x y$
Differentiating both sides w.r.t. $x$
$\begin{array}{l}
2 x+2 y \frac{d y}{d x}=14\left[x \frac{d y}{d x}+y\right] \Rightarrow x+y \frac{d y}{d x}=7 x \cdot \frac{d y}{d x}+7 y \\
(y-7 x) \frac{d y}{d x}=7 y-x \Rightarrow \frac{d y}{d x}=\frac{7 y-x}{y-7 x}
\end{array}$

</details>

---

### Q41. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $y \sqrt{1-x^{2}}+x \sqrt{1-y^{2}}=1, \quad$ then $\frac{d y}{d x}=$

**Options:**

- **(A)** $-\sqrt{\frac{1-y^{2}}{1-x^{2}}}$
- **(B)** $-\sqrt{\frac{1-x^{2}}{1-y^{2}}}$
- **(C)** $\sqrt{\frac{1+y^{2}}{1+x^{2}}}$
- **(D)** $\sqrt{\frac{1-x^{2}}{1-y^{2}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\sqrt{\frac{1-y^{2}}{1-x^{2}}}$**

**Detailed Solution:**

Given $y \sqrt{1-x^{2}}+x \sqrt{1-y^{2}}=1$
Put $x=\sin \alpha$ and $y=\sin \beta$
Given equation becomes
$\sin \beta \cos \alpha+\sin \alpha \cos \beta=1 \Rightarrow \sin (\alpha+\beta)=1 \Rightarrow \alpha+\beta=\sin ^{-1}(1)$
$\therefore \sin ^{-1} x+\sin ^{-1} y=\frac{\pi}{2}$
Differentiating w.r.t. $x$
$$
\begin{aligned}
& \frac{1}{\sqrt{1-x^{2}}}+\frac{1}{\sqrt{1-y^{2}} \frac{d y}{d x}}=0 \\
\therefore & \frac{1}{\sqrt{1-y^{2}}} \frac{d y}{d x}=-\frac{1}{\sqrt{1-x^{2}}} \Rightarrow \frac{d y}{d x}=-\sqrt{\frac{1-y^{2}}{1-x^{2}}}
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{x}+\sqrt{y}=\sqrt{x y}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $-\left(\frac{y}{x}\right)^{\frac{3}{2}}$
- **(B)** $\left(\frac{x}{y}\right)^{\frac{3}{2}}$
- **(C)** $-\left(\frac{x}{y}\right)^{\frac{3}{2}}$
- **(D)** $\left(\frac{y}{x}\right)^{\frac{3}{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\left(\frac{y}{x}\right)^{\frac{3}{2}}$**

**Detailed Solution:**

We have $\sqrt{x}+\sqrt{y}=\sqrt{x y}$
Dividing both sides by $\sqrt{x y}$, we get
$\frac{1}{\sqrt{y}}+\frac{1}{\sqrt{x}}=1$
Differentiating both sides w.r.t. $x$, we get
$\begin{aligned}
&\left(\frac{-1}{2}\right)\left(\frac{1}{y^{3 / 2}}\right)\left(\frac{d y}{d x}\right)-\left(\frac{1}{2}\right)\left(\frac{1}{x^{3 / 2}}\right)=0 \\
\therefore & \frac{d y}{d x}=-\left(\frac{y}{x}\right)^{3 / 2}
\end{aligned}$

</details>

---

### Q43. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sin \left(\frac{x+y}{x-y}\right)=\tan \frac{\pi}{5}$, then $\frac{d y}{d x}=$

**Options:**

- **(A)** $\frac{x}{y}$
- **(B)** $\frac{y}{x}$
- **(C)** $-\frac{y}{x}$
- **(D)** $-\frac{x}{y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{y}{x}$**

**Detailed Solution:**

Given $\sin \left(\frac{x+y}{x-y}\right)=\tan \frac{\pi}{5}$ 
$\therefore \frac{x+y}{x-y}=\sin ^{-1}\left(\tan \frac{\pi}{5}\right) \Rightarrow \frac{x+y}{x-y}=K \quad \ldots$ say ...(1)
$\therefore x+y=K(x-y)$ 
$\quad 1+\frac{d y}{d x}=K\left(1-\frac{d y}{d x}\right) \Rightarrow 1+\frac{d y}{d x}=K-K \frac{d y}{d x}$ 
$(1+K) \frac{d y}{d x}=K-1 \Rightarrow \frac{d y}{d x}=\frac{K-1}{K+1}$ 
$\begin{aligned} \frac{d y}{d x} &=\frac{\frac{x+y}{x-y}-1}{\frac{x+y}{x-y}+1} \quad[\ldots \text { From (1) }] \\ &=\frac{x+y-x+y}{x+y+x-y}=\frac{2 y}{2 x}=\frac{y}{x} \end{aligned}$
This problem can also be solved as follow:
$\frac{x+y}{x-y}=\sin ^{-1}\left(\tan \frac{\pi}{5}\right)$
Differentiating w.r.t. $\mathrm{x}$, we get
$\begin{aligned}
& \frac{(x-y)\left(1+\frac{d y}{d x}\right)-(x+y)\left(1-\frac{d y}{d x}\right)}{(x-y)^{2}}=0 \\
\therefore &\left(x-y+x \frac{d y}{d x}-y \frac{d y}{d x}\right)-\left(x+y-x \frac{d y}{d x}-y \frac{d y}{d x}\right)=0 \\
\therefore &-2 y+2 x \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{y}{x}
\end{aligned}$

</details>

---

### Q44. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If then <math><mi mathvariant="normal"></mi><msup><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup><mo>,</mo></math> then <math><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math> at x =1 is ….

**Options:**

- **(A)** e
- **(B)** 1
- **(C)** 0
- **(D)** -1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

Given have, <math><msup><mrow><mi>x</mi></mrow><mrow><mi>y</mi></mrow></msup><mo>=</mo><msup><mrow><mi>e</mi></mrow><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></msup></math>  
taking log on both sides, we get 
<math><mi>y</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>e</mi><mo>=</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></math> ….(i) 
when <math><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>t</mi><mi>h</mi><mi>e</mi><mi>n</mi><mi></mi><mi>y</mi><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mn>1</mn></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math>  
On differentiating both sides, 
<math><mi>y</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>.</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mrow><mi>x</mi></mrow></mfrac></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></mrow><mrow><mi>x</mi><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math>  
when x = 1, then 
<math><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>1</mn><mfenced separators="|"><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi><mn>1</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>0</mn></math>

</details>

---

### Q45. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If $x^{p}+y^{q}=(x+y)^{p+q}$, then $\frac{d y}{d x}$ is

**Options:**

- **(A)** $-\frac{x}{y}$
- **(B)** $\frac{x}{y}$
- **(C)** $-\frac{y}{x}$
- **(D)** $\frac{y}{x}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{y}{x}$**

**Detailed Solution:**

If $x^{p}+y^{q}=(x+y)^{p+q}$
Taking log on both sides, $p \log x+q \log y=(p+q) \log (x+y)$
On differentiating w.r.t $x$, we get $\frac{p}{x}+\frac{q}{y} \cdot \frac{d y}{d x}=\frac{(p+q)}{(x+y)}\left(1+\frac{d y}{d x}\right)$
$$
\left\{\frac{p}{x}-\frac{p+q}{x+y}\right\}=\left\{\frac{p+q}{x+y}-\frac{q}{y}\right\} \frac{d y}{d x}
$$
$\left\{\frac{p x+p y-p x-q x}{x(x+y)}\right\}=\left\{\frac{p y+q y-q x-q y}{y(x+y)}\right\} \frac{d y}{d x}$
$\Rightarrow \frac{(p y-q x)}{x}=\frac{(p y-q x)}{y} \cdot \frac{d y}{d x}$
$\Rightarrow \quad \frac{d y}{d x}=\frac{y}{x}$

</details>

---

### Q46. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

If $x^{p} y^{q}=(x+y)^{p+q}$, then $\frac{d y}{d x}$ is equal to

**Options:**

- **(A)** $y / x$
- **(B)** $p y / q x$
- **(C)** $x / y$
- **(D)** $q y / p x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y / x$**

**Detailed Solution:**

Given, $x^{p} y^{q}=(x+y)^{p+q}$
Taking log on both sides, we get
$$
\begin{array}{l}
\quad p \log x+q \log y=(p+q) \log (x+y) \\
\Rightarrow \quad \frac{p}{x}+\frac{q}{y} \frac{d y}{d x}=\frac{(p+q)}{(x+y)}\left(1+\frac{d y}{d x}\right) \\
\Rightarrow \quad\left(\frac{p}{x}-\frac{p+q}{x+y}\right)=\left(\frac{p+q}{x+y}-\frac{q}{y}\right) \frac{d y}{d x} \\
\Rightarrow \quad \frac{d y}{d x}=\frac{y}{x}
\end{array}
$$

</details>

---

### Q47. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `3`

If $x^{2} y^{5}=(x+y)^{7}$, then $\frac{d^{2} y}{d x^{2}}$ is equal to

**Options:**

- **(A)** $y / x^{2}$
- **(B)** $x / y$
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

Given, $x^{2} y^{5}=(x+y)^{7}$
Taking log on both sides, we get
$$
2 \log x+5 \log y=7 \log (x+y)
$$
On differentiating, we get
$$
\begin{aligned}
\frac{2}{x}+\frac{5}{y} \frac{d y}{d x} &=\frac{7}{x+y}\left(1+\frac{d y}{d x}\right) \\
\Rightarrow \quad & \frac{d y}{d x}\left(\frac{7}{x+y}-\frac{5}{y}\right)=\frac{2}{x}-\frac{7}{x+y}
\end{aligned}
$$
$$
\Rightarrow \quad \frac{d y}{d x}=\frac{y}{x}
$$
Again, differentiating, we get
$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} &=\frac{x \frac{d y}{d x}-y}{x^{2}} \\
&=\frac{x \cdot(y / x)-y}{x^{2}}[\text { from Eq. (i)] }\\
&=0
\end{aligned}
$$

</details>

---

### Q48. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

The value of $\left(\frac{\Delta^{2}}{E}\right) x^{3}$ at $h=1$ is

**Options:**

- **(A)** $8 x$
- **(B)** $6 x$
- **(C)** $5 x^{2}$
- **(D)** $6 x^{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6 x$**

**Detailed Solution:**

$\begin{aligned} &\left(\frac{\Delta^{2}}{E}\right) x^{3}=\left(\frac{(E-1)^{2}}{E}\right) x^{3} \\ &=\left(\frac{E^{2}-2 E+1}{E}\right) x^{3} \\ &=E\left(x^{3}\right)-2 x^{3}+E^{-1}\left(x^{3}\right) \\ &=(x+1)^{3}-2 x^{3}+(x-1)^{3} \\ &=x^{3}+1+3 x^{2}+3 x-2 x^{3}+x^{3}-1-3 x^{2}+3 x \\ &=6 x \end{aligned}$

</details>

---

