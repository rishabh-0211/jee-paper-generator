# MHT CET Mathematics - Differential Equations

## Topic 1: Order and Degree

**Total Questions:** 43

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The order and degree of the differential equation $e^{\frac{dy}{dx}} + \dfrac{dy}{dx} = x$ is

**Options:**

- **(A)** order = 1 and degree = 1
- **(B)** order = 1 and degree = 2
- **(C)** order = 1 and degree = not defined
- **(D)** order = not defined and degree = 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) order = 1 and degree = not defined**

**Detailed Solution:**

The given differential equation is $e^{\dfrac{dy}{dx}} + \dfrac{dy}{dx} = x$.

The highest order derivative present in the equation is $\dfrac{dy}{dx}$. Thus, the order of the differential equation is $1$.

The degree of a differential equation is defined only when it can be expressed as a polynomial equation in its derivatives. Since the given equation contains the term $e^{\dfrac{dy}{dx}}$, it cannot be expressed as a polynomial in $\dfrac{dy}{dx}$.

Therefore, the degree of the differential equation is not defined.

Answer: order = 1 and degree = not defined

</details>

---

### Q2. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Degree of differential equation $\sqrt[3]{\left(\dfrac{dy}{dx}\right)^2 + 5} = \dfrac{1 + \left(\dfrac{dx}{dy}\right)^3}{\sqrt{4 + \left(\dfrac{dy}{dx}\right)^5}}$ is

**Options:**

- **(A)** $37$
- **(B)** $19$
- **(C)** $10$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $37$**

**Detailed Solution:**

Let $\dfrac{dy}{dx} = p$. Then $\dfrac{dx}{dy} = \dfrac{1}{p}$.

The given differential equation can be written as:

$(p^2 + 5)^{1/3} = \dfrac{1 + \dfrac{1}{p^3}}{(4 + p^5)^{1/2}}$

$(p^2 + 5)^{1/3} = \dfrac{p^3 + 1}{p^3 (4 + p^5)^{1/2}}$

Raising both sides to the power of $6$ (the least common multiple of $3$ and $2$) to eliminate fractional exponents:

$(p^2 + 5)^2 = \dfrac{(p^3 + 1)^6}{p^{18} (4 + p^5)^3}$

Cross-multiplying to express it as a polynomial in $p$:

$p^{18} (p^2 + 5)^2 (4 + p^5)^3 = (p^3 + 1)^6$

The highest power of $p$ on the left hand side is $18 + (2 \times 2) + (5 \times 3) = 18 + 4 + 15 = 37$.

The highest power of $p$ on the right hand side is $3 \times 6 = 18$.

Since the differential equation is a polynomial in $p$ (which is $\dfrac{dy}{dx}$) and the highest power of $p$ is $37$, the degree of the differential equation is $37$.

Answer: $37$

</details>

---

### Q3. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The order and degree of the differential equation $\sqrt{1 + \dfrac{1}{\left(\frac{dy}{dx}\right)^2}} = \left(\dfrac{d^2y}{dx^2}\right)^{\frac{3}{2}}$, respectively are

**Options:**

- **(A)** $2, 1$
- **(B)** $2, 3$
- **(C)** $1, 2$
- **(D)** $3, 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2, 3$**

**Detailed Solution:**

The given differential equation is $\sqrt{1 + \dfrac{1}{\left(\dfrac{dy}{dx}\right)^2}} = \left(\dfrac{d^2y}{dx^2}\right)^{\dfrac{3}{2}}$

Squaring both sides to remove the fractional powers, we get:

$1 + \dfrac{1}{\left(\dfrac{dy}{dx}\right)^2} = \left(\dfrac{d^2y}{dx^2}\right)^3$

Multiplying the entire equation by $\left(\dfrac{dy}{dx}\right)^2$ to express it as a polynomial in derivatives:

$\left(\dfrac{dy}{dx}\right)^2 + 1 = \left(\dfrac{dy}{dx}\right)^2 \left(\dfrac{d^2y}{dx^2}\right)^3$

The highest order derivative present in the equation is $\dfrac{d^2y}{dx^2}$, which means the order of the differential equation is $2$.

The power of the highest order derivative in this polynomial form is $3$, which means the degree of the differential equation is $3$.

Therefore, the order and degree are $2$ and $3$, respectively.

Answer: $2, 3$

</details>

---

### Q4. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\left(\dfrac{d^3 y}{dx^3}\right)^{\frac{2}{3}} - 3\dfrac{d^2 y}{dx^2} + 5\dfrac{dy}{dx} + 4 = 0$ are respectively

**Options:**

- **(A)** $2, 3$
- **(B)** $3, 2$
- **(C)** $3$, not defined
- **(D)** not defined, $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3, 2$**

**Detailed Solution:**

The given differential equation is $\left(\dfrac{d^3 y}{dx^3}\right)^{\dfrac{2}{3}} - 3\dfrac{d^2 y}{dx^2} + 5\dfrac{dy}{dx} + 4 = 0$.

The order of a differential equation is the order of the highest derivative present in the equation. The highest derivative is $\dfrac{d^3 y}{dx^3}$, so the order is $3$.

To find the degree, the differential equation must be expressed as a polynomial in its derivatives. Isolating the term with the fractional power, we get:

$\left(\dfrac{d^3 y}{dx^3}\right)^{\dfrac{2}{3}} = 3\dfrac{d^2 y}{dx^2} - 5\dfrac{dy}{dx} - 4$

Cubing both sides to remove the fractional power, we obtain:

$\left(\dfrac{d^3 y}{dx^3}\right)^2 = \left(3\dfrac{d^2 y}{dx^2} - 5\dfrac{dy}{dx} - 4\right)^3$

The degree of a differential equation is the power of the highest order derivative when the equation is a polynomial in derivatives. The power of the highest order derivative $\dfrac{d^3 y}{dx^3}$ is $2$.

Thus, the order is $3$ and the degree is $2$.

Answer: $3, 2$

</details>

---

### Q5. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\sqrt{1 + \dfrac{1}{\left(\dfrac{dy}{dx}\right)^2}} = \left(\dfrac{d^2y}{dx^2}\right)^{\frac{3}{2}}$ are $\ldots$

**Options:**

- **(A)** Order 2, Degree 3
- **(B)** Order 2, Degree 2
- **(C)** Order 3, Degree 3
- **(D)** Order 3, Degree 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Order 2, Degree 3**

**Detailed Solution:**

The given differential equation is $\sqrt{1 + \dfrac{1}{\left(\dfrac{dy}{dx}\right)^2}} = \left(\dfrac{d^2y}{dx^2}\right)^{\dfrac{3}{2}}$

Squaring both sides to remove the fractional powers, we get:

$1 + \dfrac{1}{\left(\dfrac{dy}{dx}\right)^2} = \left(\dfrac{d^2y}{dx^2}\right)^3$

Multiplying the entire equation by $\left(\dfrac{dy}{dx}\right)^2$ to express it as a polynomial in derivatives:

$\left(\dfrac{dy}{dx}\right)^2 + 1 = \left(\dfrac{dy}{dx}\right)^2 \left(\dfrac{d^2y}{dx^2}\right)^3$

The highest order derivative present in the equation is $\dfrac{d^2y}{dx^2}$, which means the order of the differential equation is $2$.

The highest power of this highest order derivative is $3$, which means the degree of the differential equation is $3$.

Answer: Order 2, Degree 3

</details>

---

### Q6. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the differential equation $\dfrac{d^3y}{dx^3} + \cos\left(\dfrac{d^2y}{dx^2}\right) = 0$, which of the following is true ?

**Options:**

- **(A)** Order = 3, degree = 1
- **(B)** Order = 3, degree = 2
- **(C)** Order = 3, degree is not defined
- **(D)** Order = 2, degree is not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Order = 3, degree is not defined**

**Detailed Solution:**

The given differential equation is $\dfrac{d^3y}{dx^3} + \cos\left(\dfrac{d^2y}{dx^2}\right) = 0$.

The order of a differential equation is the order of the highest derivative appearing in it. The highest order derivative present is $\dfrac{d^3y}{dx^3}$, so the order is $3$.

The degree of a differential equation is defined only when it can be expressed as a polynomial equation in its derivatives. Since the equation contains the term $\cos\left(\dfrac{d^2y}{dx^2}\right)$, it cannot be expressed as a polynomial in terms of the derivatives.

Therefore, the degree of the given differential equation is not defined.

Answer: Order = 3, degree is not defined

</details>

---

### Q7. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The order and degree of the differential equation $3 - \left(\dfrac{\text{d}^3 y}{\text{d}x^3}\right)^{\frac{7}{3}} = \left(\dfrac{\text{d}y}{\text{d}x}\right)^5$ are respectively

**Options:**

- **(A)** $3, 7$
- **(B)** $7, 3$
- **(C)** $5, 7$
- **(D)** $3, 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3, 7$**

**Detailed Solution:**

The given differential equation is $3 - \left(\dfrac{\text{d}^3 y}{\text{d}x^3}\right)^{\dfrac{7}{3}} = \left(\dfrac{\text{d}y}{\text{d}x}\right)^5$.

Rearranging the terms to isolate the fractional power, we get:

$\left(\dfrac{\text{d}^3 y}{\text{d}x^3}\right)^{\dfrac{7}{3}} = 3 - \left(\dfrac{\text{d}y}{\text{d}x}\right)^5$

Cubing both sides to remove the fractional power, we obtain:

$\left(\dfrac{\text{d}^3 y}{\text{d}x^3}\right)^7 = \left[3 - \left(\dfrac{\text{d}y}{\text{d}x}\right)^5\right]^3$

The highest order derivative present in the equation is $\dfrac{\text{d}^3 y}{\text{d}x^3}$, so the order is $3$.

The power of the highest order derivative is $7$, so the degree is $7$.

Answer: $3, 7$

</details>

---

### Q8. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The order and degree of the differential equation $\sqrt{2 + \left(\dfrac{d^2 y}{dx^2}\right)^3} = \left(\dfrac{d^3 y}{dx^3}\right)^{5/2}$ respectively are

**Options:**

- **(A)** $2, 3$
- **(B)** $3, 5$
- **(C)** $3, 2$
- **(D)** $5, 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3, 5$**

**Detailed Solution:**

The given differential equation is $\sqrt{2 + \left(\dfrac{d^2 y}{dx^2}\right)^3} = \left(\dfrac{d^3 y}{dx^3}\right)^{5/2}$

Squaring both sides to remove fractional powers, we get:

$2 + \left(\dfrac{d^2 y}{dx^2}\right)^3 = \left(\dfrac{d^3 y}{dx^3}\right)^5$

The highest order derivative present in the equation is $\dfrac{d^3 y}{dx^3}$, so the order of the differential equation is $3$.

The power of the highest order derivative is $5$, so the degree of the differential equation is $5$.

Therefore, the order and degree are $3$ and $5$ respectively.

Answer: $3, 5$

</details>

---

### Q9. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $3-\left(\frac{\mathrm{d}^3 \mathrm{y}}{\mathrm{d} x^3}\right)^{\frac{7}{3}}=\left(\frac{\mathrm{dy}}{\mathrm{d} x}\right)^5$ are respectively

**Options:**

- **(A)** $3, 7$
- **(B)** $7, 3$
- **(C)** $3, 5$
- **(D)** $5, 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3, 7$**

**Detailed Solution:**

The given differential equation is $3-\left(\dfrac{\mathrm{d}^3 \mathrm{y}}{\mathrm{d} x^3}\right)^{\dfrac{7}{3}}=\left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)^5$.

Rearranging the terms, we get:

$\left(\dfrac{\mathrm{d}^3 \mathrm{y}}{\mathrm{d} x^3}\right)^{\dfrac{7}{3}} = 3 - \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)^5$

Cubing both sides to remove the fractional power:

$\left(\dfrac{\mathrm{d}^3 \mathrm{y}}{\mathrm{d} x^3}\right)^7 = \left[3 - \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)^5\right]^3$

The highest order derivative is $\dfrac{\mathrm{d}^3 \mathrm{y}}{\mathrm{d} x^3}$, so the order is $3$.

The power of the highest order derivative is $7$, so the degree is $7$.

The order and degree are $3$ and $7$ respectively.

Answer: $3, 7$

</details>

---

### Q10. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The order of the differential equation whose general solution is given by $\mathrm{y}=\left(\mathrm{C}_1+\mathrm{C}_2\right) \sin \left(\mathrm{x}+\mathrm{C}_3\right)-\mathrm{C}_4 \mathrm{e}^{x+\mathrm{C}_5}$ is (where $\mathrm{C}_1, \mathrm{C}_2, \mathrm{C}_3, \mathrm{C}_4, \mathrm{C}_5$ are arbitrary constants)

**Options:**

- **(A)** 5
- **(B)** 4
- **(C)** 2
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

Given the general solution of the differential equation:

$\mathrm{y}=\left(\mathrm{C}_1+\mathrm{C}_2\right) \sin \left(\mathrm{x}+\mathrm{C}_3\right)-\mathrm{C}_4 \mathrm{e}^{x+\mathrm{C}_5}$

We can rewrite the equation by expanding the terms:

$\mathrm{y}=\left(\mathrm{C}_1+\mathrm{C}_2\right)\left(\sin \mathrm{x} \cos \mathrm{C}_3+\cos \mathrm{x} \sin \mathrm{C}_3\right)-\mathrm{C}_4 \mathrm{e}^{\mathrm{C}_5} \mathrm{e}^x$

$\mathrm{y}=\left(\left(\mathrm{C}_1+\mathrm{C}_2\right) \cos \mathrm{C}_3\right) \sin \mathrm{x}+\left(\left(\mathrm{C}_1+\mathrm{C}_2\right) \sin \mathrm{C}_3\right) \cos \mathrm{x}-\left(\mathrm{C}_4 \mathrm{e}^{\mathrm{C}_5}\right) \mathrm{e}^x$

Let $\mathrm{A}=\left(\mathrm{C}_1+\mathrm{C}_2\right) \cos \mathrm{C}_3$, $\mathrm{B}=\left(\mathrm{C}_1+\mathrm{C}_2\right) \sin \mathrm{C}_3$, and $\mathrm{C}=-\mathrm{C}_4 \mathrm{e}^{\mathrm{C}_5}$.

Substituting these new constants into the equation, we get:

$\mathrm{y}=\mathrm{A} \sin \mathrm{x}+\mathrm{B} \cos \mathrm{x}+\mathrm{C} \mathrm{e}^x$

The equation now contains exactly $3$ essential arbitrary constants ($\mathrm{A}$, $\mathrm{B}$, and $\mathrm{C}$).

Since the order of a differential equation is equal to the number of essential arbitrary constants in its general solution, the order of this differential equation is $3$.

Answer: 3

</details>

---

### Q11. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The differential equation whose solution is $\mathrm{A} x^2+\mathrm{By}^2=1$ where $A$ and $B$ are arbitrary constants is of

**Options:**

- **(A)** degree 1 and order 2
- **(B)** degree 2 and order 1
- **(C)** degree 3 and order 2
- **(D)** degree 1 and order 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) degree 1 and order 2**

**Detailed Solution:**

The given equation is $Ax^2 + By^2 = 1$.

Differentiating with respect to $x$, we get:

$2Ax + 2By \dfrac{dy}{dx} = 0$

$Ax + By \dfrac{dy}{dx} = 0$

$\dfrac{A}{B} = -\dfrac{y}{x} \dfrac{dy}{dx}$

Differentiating again with respect to $x$, we get:

$A + B \left( y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 \right) = 0$

$\dfrac{A}{B} = - \left( y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 \right)$

Equating the values of $\dfrac{A}{B}$:

$-\dfrac{y}{x} \dfrac{dy}{dx} = - \left( y \dfrac{d^2y}{dx^2} + \left(\dfrac{dy}{dx}\right)^2 \right)$

$xy \dfrac{d^2y}{dx^2} + x \left(\dfrac{dy}{dx}\right)^2 - y \dfrac{dy}{dx} = 0$

The highest order derivative is $\dfrac{d^2y}{dx^2}$, so the order is $2$.

The power of the highest order derivative is $1$, so the degree is $1$.

Answer: degree 1 and order 2

</details>

---

### Q12. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\sqrt{\frac{\mathrm{dy}}{\mathrm{d} x}}-4 \frac{\mathrm{dy}}{\mathrm{d} x}-7 x=0$ is respectively

**Options:**

- **(A)** 1,2
- **(B)** 2,1
- **(C)** 2,2
- **(D)** 3,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1,2**

**Detailed Solution:**

The given differential equation is $\sqrt{\dfrac{\mathrm{dy}}{\mathrm{d} x}}-4 \dfrac{\mathrm{dy}}{\mathrm{d} x}-7 x=0$.

Rearranging the terms, we get:

$\sqrt{\dfrac{\mathrm{dy}}{\mathrm{d} x}} = 4 \dfrac{\mathrm{dy}}{\mathrm{d} x} + 7 x$

Squaring both sides to make the equation a polynomial in its derivatives:

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = \left(4 \dfrac{\mathrm{dy}}{\mathrm{d} x} + 7 x\right)^2$

$\dfrac{\mathrm{dy}}{\mathrm{d} x} = 16 \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)^2 + 56 x \dfrac{\mathrm{dy}}{\mathrm{d} x} + 49 x^2$

$16 \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}\right)^2 + (56 x - 1) \dfrac{\mathrm{dy}}{\mathrm{d} x} + 49 x^2 = 0$

The highest order derivative present in the equation is $\dfrac{\mathrm{dy}}{\mathrm{d} x}$, so the order is $1$.

The highest power of the highest order derivative is $2$, so the degree is $2$.

Answer: 1,2

</details>

---

### Q13. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The degree of the differential equation $\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}+3\left(\frac{\mathrm{~d} y}{\mathrm{~d} x}\right)^2=x^2 \log \left(\frac{\mathrm{~d}^2 \mathrm{y}}{\mathrm{d} x^2}\right)$ is

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** Not defined

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Not defined**

**Detailed Solution:**

The given differential equation is $\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2} + 3\left(\dfrac{\mathrm{d} y}{\mathrm{d} x}\right)^2 = x^2 \log \left(\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}\right)$.

The highest order derivative present in the equation is $\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}$, so the order of the differential equation is $2$.

For the degree of a differential equation to be defined, the equation must be a polynomial in its derivatives.

Since the equation contains the term $\log \left(\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}\right)$, it cannot be expressed as a polynomial equation in terms of its derivatives.

Therefore, the degree of the given differential equation is not defined.

Answer: Not defined

</details>

---

### Q14. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the degree and order of the differential equation $\sqrt{\frac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}}=\sqrt[5]{\frac{\mathrm{dy}}{\mathrm{d} x}-5}$ is

**Options:**

- **(A)** $1$
- **(B)** $3$
- **(C)** $5$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $7$**

**Detailed Solution:**

The given differential equation is $\sqrt{\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}}=\sqrt[5]{\dfrac{\mathrm{dy}}{\mathrm{d} x}-5}$.

To eliminate the fractional powers, we raise both sides to the power of $10$ (the LCM of $2$ and $5$):

$\left(\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}\right)^5 = \left(\dfrac{\mathrm{dy}}{\mathrm{d} x}-5\right)^2$

The highest order derivative present in the equation is $\dfrac{\mathrm{d}^2 \mathrm{y}}{\mathrm{d} x^2}$, so the order of the differential equation is $2$.

The power of the highest order derivative is $5$, so the degree of the differential equation is $5$.

The sum of the degree and order is $5 + 2 = 7$.

Answer: $7$

</details>

---

### Q15. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The order and degree of differential equation of all tangent lines to the parabola $x^2=4 \mathrm{y}$ is respectively.

**Options:**

- **(A)** 1,2
- **(B)** 2,2
- **(C)** 3,1
- **(D)** 4,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1,2**

**Detailed Solution:**

The equation of the parabola is $x^2 = 4y$.

The equation of any tangent to the parabola $x^2 = 4ay$ in terms of its slope $m$ is given by $y = mx - am^2$.

Here, $4a = 4 \Rightarrow a = 1$.

So, the equation of the family of tangent lines is:
$y = mx - m^2$

Since there is only one arbitrary constant $m$, we differentiate the equation once with respect to $x$:
$\dfrac{dy}{dx} = m$

Substituting $m = \dfrac{dy}{dx}$ back into the equation of the tangent to eliminate the arbitrary constant, we get the differential equation:
$y = x \left(\dfrac{dy}{dx}\right) - \left(\dfrac{dy}{dx}\right)^2$

In this differential equation, the highest order derivative is $\dfrac{dy}{dx}$, which means the order is $1$.

The highest power of the highest order derivative is $2$, which means the degree is $2$.

Therefore, the order and degree are $1$ and $2$ respectively.

Answer: 1,2

</details>

---

### Q16. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation, whose general solution is given by
$y=\left(\mathrm{c}_1+\mathrm{c}_2\right) \cos \left(x+\mathrm{c}_3\right)-\mathrm{c}_4 \mathrm{e}^{x+\mathrm{c}^5}$
where $c_1, c_2, c_3, c_4$ and $c_5$ are arbitrary constant, is

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** 4
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

The given general solution is:

$y = (c_1 + c_2) \cos(x + c_3) - c_4 e^{x + c_5}$

Substituting $c_1 + c_2 = A$, the equation becomes:

$y = A \cos(x + c_3) - c_4 e^{c_5} e^x$

Substituting $c_4 e^{c_5} = B$, the equation simplifies to:

$y = A \cos(x + c_3) - B e^x$

Expanding the cosine term gives:

$y = A (\cos x \cos c_3 - \sin x \sin c_3) - B e^x$

$y = (A \cos c_3) \cos x - (A \sin c_3) \sin x - B e^x$

Substituting $A \cos c_3 = C_1$ and $-A \sin c_3 = C_2$, the equation can be written as:

$y = C_1 \cos x + C_2 \sin x - B e^x$

This equation contains exactly 3 independent arbitrary constants ($C_1$, $C_2$, and $B$).

Since the order of a differential equation is equal to the number of independent arbitrary constants in its general solution, the order of the differential equation is 3.

Answer: 3

</details>

---

### Q17. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If order and degree of the differential equation $\left(\dfrac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)^5+4 \dfrac{\left(\dfrac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}\right)^5}{\left(\dfrac{\mathrm{~d}^3 y}{\mathrm{~d} x^3}\right)}+\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}=\sin x$, are m and n respectively, then the value of $\left(m^2+n^2\right)$ is equal to

**Options:**

- **(A)** 29
- **(B)** 13
- **(C)** 5
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 13**

**Detailed Solution:**

The given differential equation is:

$\left(\dfrac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)^5+4 \dfrac{\left(\dfrac{\mathrm{~d}^2 y}{\mathrm{~d} x^2}\right)^5}{\left(\dfrac{\mathrm{~d}^3 y}{\mathrm{~d} x^3}\right)}+\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}=\sin x$

To find the degree, the differential equation must be expressed as a polynomial in its derivatives. Multiplying both sides by $\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}$, we get:

$\left(\dfrac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)^5 \left(\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}\right) + 4 \left(\dfrac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)^5 + \left(\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}\right)^2 = \sin x \left(\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}\right)$

The highest order derivative present in the equation is $\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}$. Thus, the order of the differential equation is $m = 3$.

The highest power of the highest order derivative $\dfrac{\mathrm{d}^3 y}{\mathrm{~d} x^3}$ is $2$. Thus, the degree of the differential equation is $n = 2$.

We need to find the value of $m^2 + n^2$:

$m^2 + n^2 = 3^2 + 2^2 = 9 + 4 = 13$

Answer: 13

</details>

---

### Q18. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation $\left[\dfrac{1+\left(\dfrac{d y}{d x}\right)^2}{\left(\dfrac{d^2 y}{d x^2}\right)^{\dfrac{3}{2}}}\right]^2=\mathrm{k} x$ is of

**Options:**

- **(A)** order $=2$, degree $=3$
- **(B)** order $=3$, degree $=2$
- **(C)** order $=2$, degree $=2$
- **(D)** order $=3$, degree $=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) order $=2$, degree $=3$**

**Detailed Solution:**

The given differential equation is:

$\left[\dfrac{1+\left(\dfrac{d y}{d x}\right)^2}{\left(\dfrac{d^2 y}{d x^2}\right)^{\dfrac{3}{2}}}\right]^2=\mathrm{k} x$

Squaring the terms inside the bracket, we get:

$\dfrac{\left[1+\left(\dfrac{d y}{d x}\right)^2\right]^2}{\left(\dfrac{d^2 y}{d x^2}\right)^3} = \mathrm{k} x$

Multiplying both sides by $\left(\dfrac{d^2 y}{d x^2}\right)^3$ to express the equation as a polynomial in derivatives:

$\left[1+\left(\dfrac{d y}{d x}\right)^2\right]^2 = \mathrm{k} x \left(\dfrac{d^2 y}{d x^2}\right)^3$

The highest order derivative present in the equation is $\dfrac{d^2 y}{d x^2}$, so the order of the differential equation is $2$.

The power of the highest order derivative in this polynomial form is $3$, so the degree of the differential equation is $3$.

Answer: order $=2$, degree $=3$

</details>

---

### Q19. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The differential equation representing the family of curves $y^2=2 \mathrm{c}(x+\sqrt{\mathrm{c}})$, where $\mathrm{c}$ is a positive parameter, is of

**Options:**

- **(A)** order 1, degree 4
- **(B)** order 2, degree 3
- **(C)** order 2, degree 4
- **(D)** order 1, degree 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) order 1, degree 3**

**Detailed Solution:**

$y^2=2 \mathrm{c}(x+\sqrt{\mathrm{c}})... (i)$
Differentiating w.r.t. $x$, we get
$2 y \frac{\mathrm{d} y}{\mathrm{~d} x}=2 \mathrm{c}... (ii)$
Substituting (ii) in (i), we get
$\begin{aligned}
& y^2=2 y \frac{\mathrm{d} y}{\mathrm{~d} x}\left(x+\sqrt{y \frac{\mathrm{d} y}{\mathrm{~d} x}}\right) \\
& \Rightarrow y=2 x \frac{\mathrm{d} y}{\mathrm{~d} x}+2 \frac{\mathrm{d} y}{\mathrm{~d} x} \sqrt{y \frac{\mathrm{d} y}{\mathrm{~d} x}} \\
& \Rightarrow\left(y-2 x \frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2=4 y\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^3
\end{aligned}$
This is a differential equation of order 1 and degree 3 .

</details>

---

### Q20. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of a differential equation obtained by eliminating arbitrary constant $C$ from the family of curves $y^2=2 C(x+\sqrt{C})$ are respectively

**Options:**

- **(A)** 1,3
- **(B)** 1,4
- **(C)** 1,1
- **(D)** 1,2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1,3**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/02Xkbp7nVvXIv9_PGL6zgnvEUNB1Vj5iZaYif04Kphg.original.fullsize.png">
from (i) and (ii)
$\begin{aligned} & y^2=2 y \frac{\mathrm{d} y}{\mathrm{~d} x}\left(x+\sqrt{y \frac{\mathrm{d} y}{\mathrm{~d} x}}\right) \\ & \Rightarrow y-2 x \frac{\mathrm{d} y}{\mathrm{~d} x}=2 \frac{\mathrm{d} y}{\mathrm{~d} x} \cdot \sqrt{y \cdot \frac{\mathrm{d} y}{\mathrm{~d} x}} \\ & \Rightarrow\left(y-2 x \frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2=4 y\left(\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^3 \text { order }=1, \text { degree }=3\end{aligned}$

</details>

---

### Q21. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation
$\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^{\frac{1}{3}}=\sqrt{\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}}$ are respectively.

**Options:**

- **(A)** 3,1
- **(B)** 3,2
- **(C)** 2,3
- **(D)** 2,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2,3**

**Detailed Solution:**

$\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^{\frac{1}{3}}=\sqrt{\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}} \Rightarrow\left(1+\frac{\mathrm{d} y}{\mathrm{~d} x}\right)^2=\left(\frac{\mathrm{d}^2 y}{\mathrm{~d} x^2}\right)^3$
order $=2$ and degree $=3$.

</details>

---

### Q22. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the differential equation $\left[1-\left(\frac{d y}{d x}\right)^2\right]^{5 / 2}=8 \frac{d^2 y}{d x^2}$ has the order and degree

**Options:**

- **(A)** 2 and 1
- **(B)** 2 and 3
- **(C)** 2 and 6
- **(D)** 2 and 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2 and 3**

**Detailed Solution:**

$\begin{aligned} & \left\{1-\left(\frac{d y}{d x}\right)^2\right\}^{\frac{5}{3}}=8 \frac{d x y}{d x^2} \\ & \Rightarrow\left\{1-\left(\frac{d y}{d x}\right)^2\right\}^5=8^3\left(\frac{d x y}{d x^2}\right)^3 \\ & \text { order }=2 \text { and degree }=3\end{aligned}$

</details>

---

### Q23. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\sqrt{\frac{d y}{d x}}-4 \frac{d y}{d x}-7 x=0$ are respectively.

**Options:**

- **(A)** 2 and 2
- **(B)** 1 and 2
- **(C)** 1 and 1
- **(D)** 2 and 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1 and 2**

**Detailed Solution:**

$\begin{aligned} & \sqrt{\frac{d y}{d x}}-4 \frac{d y}{d x}-7 x=0 \\ & \therefore \sqrt{\frac{d y}{d x}}=4 \frac{d y}{d x}+7 x \text { and squaring both sides, we get } \\ & \frac{d y}{d x}=16\left(\frac{d y}{d x}\right)^2+56 x\left(\frac{d y}{d x}\right)+49 x^2 \\ & \therefore \text { Order }=1, \text { degree }=2\end{aligned}$

</details>

---

### Q24. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\frac{d^2 y}{d x^2}=\sqrt{\frac{d y}{d x}}$ are respectively

**Options:**

- **(A)** 2,3
- **(B)** 3,3
- **(C)** 2,2
- **(D)** 1,3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2,2**

**Detailed Solution:**

$\begin{aligned} & \frac{d^2 y}{d x^2}=\sqrt{\frac{d y}{d x}} \\ & \therefore \quad\left(\frac{d^2 y}{d x^2}\right)=\frac{d y}{d x} \\ & \therefore \text { order }=2 \text { and degree }=2\end{aligned}$

</details>

---

### Q25. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation whose solution is $\mathrm{y}=\mathrm{a} \cos \mathrm{x}+\mathrm{b} \sin \mathrm{x}+\mathrm{c} \mathrm{e}^{-\mathrm{x}}$ is

**Options:**

- **(A)** 3
- **(B)** 4
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

$\mathrm{y}=\mathrm{a} \cos \mathrm{x}+\mathrm{b} \sin \mathrm{x}+\mathrm{c} \mathrm{e}^{-\mathrm{x}}$ Since the equation has 3 arbitrary constants, the order of differential equation is 3 .

</details>

---

### Q26. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The degree of the differential equation whose solution is $y^2=8 a(x+a)$, is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

We have $y^2=8 a x+8 a^2$
Differentiating w.r.t. $\mathrm{x}$, we get
$$
2 y \frac{d y}{d x}=8 a \quad \Rightarrow \quad a=\left(\frac{y}{4}\right) \frac{d y}{d x}
$$
Substituting value of ' $a$ ' in eq. (1), we get
$$
\begin{aligned}
& y^2=8\left(\frac{y}{4}\right) \frac{d y}{d x}(x)+8\left[\left(\frac{y}{4}\right)\left(\frac{d y}{d x}\right)\right]^2=2 x y \frac{d y}{d x}+\left(\frac{y^2}{2}\right)\left(\frac{d y}{d x}\right)^2 \\
& \therefore 2 y^2=4 x y\left(\frac{d y}{d x}\right)+y^2\left(\frac{d y}{d x}\right)^2
\end{aligned}
$$
Hence order $=1$, degree $=2$

</details>

---

### Q27. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{m}$ is order and $\mathrm{n}$ is degree of the differential equation $\left(\frac{d^2 y}{d x^2}\right)^5+4 \frac{\left(\frac{d^2 y}{d x^2}\right)}{\left(\frac{d^3 y}{d x^3}\right)}+\left(\frac{d^3 y}{d x^3}\right)=x^2-1$, then

**Options:**

- **(A)** m=3, n=1
- **(B)** m=3, n=2
- **(C)** m=3, n=3
- **(D)** m=3, n=5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) m=3, n=2**

**Detailed Solution:**

$\begin{aligned} & \text { We have }\left(\frac{d^2 y}{d x^2}\right)^5+\frac{4\left(\frac{d^2 y}{d x^2}\right)}{\left(\frac{d^3 y}{d x^3}\right)}+\left(\frac{d^3 y}{d x^3}\right)=x^2-1 \\ & \therefore\left(\frac{d^3 y}{d x^3}\right)\left(\frac{d^2 y}{d x^2}\right)^5+4\left(\frac{d^2 y}{d x^2}\right)\left(\frac{d^3 y}{d x^3}\right)^2=\left(x^2-1\right)\left(\frac{d^3 y}{d x^3}\right) \\ & \therefore \text { order }=3 \text {, degree }=2\end{aligned}$

</details>

---

### Q28. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{m}$ is order and $\mathrm{n}$ is degree of the differential equation $\mathrm{y}=\frac{\mathrm{dp}}{\mathrm{dx}}+\sqrt{\mathrm{a}^2 \mathrm{p}^2-\mathrm{b}^2}$, where $\mathrm{p}=\frac{\mathrm{dp}}{\mathrm{dx}}$, then the value of $\mathrm{m}+\mathrm{n}$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

$$
\begin{aligned}
& y=\frac{d p}{d x}+\sqrt{a^2 p^2-b^2}=\frac{d}{d x}\left(\frac{d y}{d x}\right)+\sqrt{a^2\left(\frac{d y}{d x}\right)^2-b^2} \\
& \therefore y-\frac{d^2 y}{d x^2}=\sqrt{a^2\left(\frac{d y}{d x}\right)^2-b^2}
\end{aligned}
$$
Squaring both sides, we write
$$
\begin{aligned}
& y^2+\left(\frac{d^2 y}{d x}\right)^2-2 y \frac{d^2 y}{d x^2}=a^2\left(\frac{d y}{d x}\right)^2-b^2 \\
& \therefore \text { order }=2 \text { and degree }=2
\end{aligned}
$$

</details>

---

### Q29. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and the degree of the differential equation $\left[1+\left(\frac{d y}{d x}\right)^{3}\right]^{\frac{7}{3}}=7\left(\frac{d^{2} y}{d x^{2}}\right)$ are respectively

**Options:**

- **(A)** 2,3
- **(B)** 3,3
- **(C)** 2,2
- **(D)** 3,2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2,3**

**Detailed Solution:**

We have $\left[1+\left(\frac{d y}{d x}\right)^{3}\right]^{\frac{7}{3}}=7\left(\frac{d^{2} y}{d x^{2}}\right)$ Raising both sides to power of 3 , we get
$$
\left[1+\left(\frac{d y}{d x}\right)^{3}\right]^{7}=(7)^{3}\left(\frac{d^{2} y}{d x^{2}}\right)^{3}
$$
Hence order $=2$, degree $=3$

</details>

---

### Q30. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $y=p x+\sqrt{a^{2} \mathbf{p}^{2}+b^{2}}$, where $\mathrm{p}=\frac{\mathrm{d} y}{\mathrm{~d} x}$ are respectively

**Options:**

- **(A)** $1, 2$
- **(B)** $3,1$
- **(C)** 2,1
- **(D)** $1,3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1, 2$**

**Detailed Solution:**

Given
$$
\begin{array}{r}
y=p x+\sqrt{a^{2} p^{2}+b^{2}} \\
\therefore y-p x=\sqrt{a^{2} p^{2}+b^{2}}
\end{array}
$$
On squaring both side we get
$$
y^{2}-2 p x y+p^{2} x^{2}=a^{2} p^{2}+b^{2}
$$
$$
\mathrm{y}^{2}-2 \mathrm{xy} \frac{\mathrm{dy}}{\mathrm{dx}}+\left(\frac{\mathrm{dy}}{\mathrm{dx}}\right)^{2} \mathrm{x}^{2}=\mathrm{a}^{2}\left(\frac{\mathrm{dy}}{\mathrm{dx}}\right)^{2}+\mathrm{b}^{2} \quad \ldots\left[\mathrm{p}=\frac{\mathrm{dy}}{\mathrm{dx}}, \text { given }\right]
$$
Thus order is 1 and degree is 2 .

</details>

---

### Q31. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\left[1+\frac{1}{\left(\frac{d y}{d x}\right)^{2}}\right]^{\frac{5}{3}}=5 \frac{d^{2} y}{d x^{2}}$ are
respectively

**Options:**

- **(A)** 2,3
- **(B)** 3,2
- **(C)** 5,2
- **(D)** 2,5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2,3**

**Detailed Solution:**

(D)
Raising both sides of differential equation to degree 3 , we get
$\begin{array}{l}
{\left[1+\frac{1}{\left(\frac{d y}{d x}\right)^{2}}\right]^{5}=125\left(\frac{d^{2} y}{d x^{2}}\right)^{3}} \\
{\left[\left(\frac{d y}{d x}\right)^{2}+1\right]^{5}=125 \cdot\left(\frac{d^{2} y}{d x^{2}}\right)^{3}\left[\left(\frac{d y}{d x}\right)^{2}\right]^{5}}
\end{array}$
$\therefore$ Its order is 2 and degree is $3 .$

</details>

---

### Q32. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\sqrt{1+\frac{1}{\left(\frac{d y}{d x}\right)^{2}}}=\left(\frac{d^{2} y}{d x^{2}}\right)^{\frac{3}{2}}$ are respectively

**Options:**

- **(A)** 3,2
- **(B)** 2,3
- **(C)** 2,2
- **(D)** 3,3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2,3**

**Detailed Solution:**

(A)
By raising the given equation to the power of 2 , we get
$\begin{aligned}
& 1+\frac{1}{\left(\frac{d y}{d x}\right)^{2}}=\left(\frac{d^{2} y}{d x^{2}}\right)^{3} \\
\therefore &\left(\frac{d y}{d x}\right)^{2}+1=\left(\frac{d^{2} y}{d x^{2}}\right)^{3}\left(\frac{d y}{d x}\right)^{2}
\end{aligned}$
It's order is 2 and degree is 3 .

</details>

---

### Q33. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\left[1+\left[\frac{d y}{d x}\right]^{3}\right]^{\frac{7}{3}}=7 \frac{d^{2} y}{d x^{2}}$ are respectively.

**Options:**

- **(A)** 2,1
- **(B)** 2,3
- **(C)** 1,2
- **(D)** 3,2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1,2**

**Detailed Solution:**

(D)
We have $\left[1+\left[\frac{d y}{d x}\right]^{3}\right]^{\frac{7}{3}}=7 \cdot \frac{d^{2} y}{d x^{2}}$
Cubing both sides, we get
$\left[1+\left[\frac{d y}{d x}\right]^{3}\right]^{7}=7\left[\frac{d^{2} y}{d x^{2}}\right]^{3}$
Hence order is 2 and degree is $3 .$

</details>

---

### Q34. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Degree of the differential equation $e^{\frac{d y}{d x}}+\left(\frac{d y}{d x}\right)^{3}=x$ is

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** not defined
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) not defined**

**Detailed Solution:**

The degree of differential equation is the power of the highest ordered derivative when te: derivatives are made free from fractional or negative indices if any.
So here degree is not defined.

</details>

---

### Q35. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The order of the differential equation of all circles whose radius is <math><mn>4</mn><mo>,</mo></math> is ________

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn></math>**

**Detailed Solution:**

Let general equation of circle is 
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>g</mi><mi>x</mi><mo>+</mo><mn>2</mn><mi>f</mi><mi>y</mi><mo>+</mo><mi>c</mi><mo>=</mo><mi>o</mi></math>  
Its radius, <math><msqrt><msup><mrow><mi>g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>c</mi></msqrt><mo>=</mo><mn>4</mn></math>  
Then, <math><mi>c</mi><mo>=</mo><msup><mrow><mi>g</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>f</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>16</mn></math>  
Hence, we have 2 necessary arbitrary constants g and f. Then, order of differential equation is 2.

</details>

---

### Q36. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation of all circles which lie in the first quadrant and touch both the axes is…

**Options:**

- **(A)** Two
- **(B)** Three
- **(C)** One
- **(D)** Four

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) One**

**Detailed Solution:**

Equation of the circle touching both axes is <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>x</mi><mo>-</mo><mn>2</mn><mi>a</mi><mi>y</mi><mo>+</mo><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>  
Here, number of arbitrary constant is one which is equal to the order of its differential equation.

</details>

---

### Q37. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation of all parabolas, whose latus rectum is <math><mn>4</mn><mi>a</mi></math> and axis parallel to the <math><mi>x</mi><mo>-</mo><mi>a</mi><mi>x</mi><mi>i</mi><mi>s</mi></math> , is

**Options:**

- **(A)** One
- **(B)** Four
- **(C)** Three
- **(D)** Two

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Two**

**Detailed Solution:**

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/332751.png" style="width: 362px; height: 176px;" />
Since general equation of such parabola <math> <semantics> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>y</mi><mo>−</mo><mi>k</mi></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> <mo>=</mo><mn>4</mn><mi>a</mi><mrow><mo>(</mo> <mrow> <mi>x</mi><mo>−</mo><mi>h</mi></mrow> <mo>)</mo></mrow></mrow> </semantics></math> have two arbitrary constants h and k
<math> <mo>∴</mo> </math> order <math> <mrow> <mo>=</mo><mn>2</mn></mrow> </math>

</details>

---

### Q38. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

The degree and order of the differential equation <math><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>7</mn><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>y</mi></mrow><mrow><mi>d</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></math> respectively are

**Options:**

- **(A)** <math > <mn>3</mn></math> and <math > <mn>7</mn></math>
- **(B)** <math > <mn>3</mn></math> and <math > <mn>2</mn></math>
- **(C)** <math > <mn>7</mn></math> and <math > <mn>3</mn></math>
- **(D)** <math > <mn>2</mn></math> and <math > <mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math > <mn>3</mn></math> and <math > <mn>2</mn></math>**

**Detailed Solution:**

The given differential equation can be written as
<math> <mrow> <msup> <mrow> <mrow><mo>[</mo> <mrow> <mn>1</mn><mo>+</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <mi>d</mi><mi>y</mi></mrow> <mrow> <mi>d</mi><mi>x</mi></mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> <mn>3</mn> </msup> </mrow> <mo>]</mo></mrow></mrow> <mn>7</mn> </msup> <mo>=</mo><msup> <mn>7</mn> <mn>3</mn> </msup> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mi>d</mi> <mn>2</mn> </msup> <mi>y</mi></mrow> <mrow> <mi>d</mi><msup> <mi>x</mi> <mn>2</mn> </msup> </mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> <mn>3</mn> </msup> </mrow> </math>
<math> <mrow> <mo>⇒</mo> </mrow> </math> order = 2, degree = 3

</details>

---

### Q39. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $m$ and $n$ are order and degree of the equation $\left(\frac{d^{2} y}{d x^{2}}\right)^{5}+4 \cdot \frac{\left(\frac{d^{2} y}{d x^{2}}\right)^{3}}{\left(\frac{d^{3} y}{d x^{3}}\right)}+\left(\frac{d^{3} y}{d x^{3}}\right)=x^{2}-1$, then

**Options:**

- **(A)** $m=3, n=3$
- **(B)** $m=3, n=2$
- **(C)** $m=3, n=5$
- **(D)** $m=3, n=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $m=3, n=2$**

**Detailed Solution:**

The given differential equation can be rewritten as
$$
\begin{array}{l}
\left(\frac{d^{2} y}{d x^{2}}\right)^{5} \cdot \frac{d^{3} y}{d x^{3}}+4\left(\frac{d^{2} y}{d x^{2}}\right)^{3}+\left(\frac{d^{3} y}{d x^{3}}\right)^{2} \\
=\left(x^{2}-1\right) \frac{d^{3} y}{d x^{3}} \Rightarrow \text { order }(m)=3
\end{array}
$$
and $\quad$ degree $(n)=2$

</details>

---

### Q40. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation whose solution is $a e^{x}+b e^{2 x}+c e^{3 x}+d=0$, is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Since, this equation has 4 arbitrary constants $a, b, c, d$ therefore, order of this differential equation is $4 .$

</details>

---

### Q41. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\frac{d^{2} y}{d x^{2}}=\sqrt[3]{1-\left(\frac{d y}{d x}\right)^{4}}$ are respectively

**Options:**

- **(A)** 2,3
- **(B)** 3,2
- **(C)** 2,4
- **(D)** 2,2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2,3**

**Detailed Solution:**

Given differential equation is
$$
\begin{aligned}
& \frac{d^{2} y}{d x^{2}} &=\sqrt[3]{1-\left(\frac{d y}{d x}\right)^{4}} \\
\Rightarrow &\left(\frac{d^{2} y}{d x^{2}}\right)^{3} &=1-\left(\frac{d y}{d x}\right)^{4} \\
\therefore & \quad \text { Order } &=2, \text { degree }=3
\end{aligned}
$$

</details>

---

### Q42. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The order and degree of the differential equation $\sqrt{\frac{d y}{d x}}-4 \frac{d y}{d x}-7 x=0$ are

**Options:**

- **(A)** 1 and $1 / 2$
- **(B)** 2 and 1
- **(C)** 1 and 1
- **(D)** 1 and 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1 and 2**

**Detailed Solution:**

Given equation is $\sqrt{\frac{d y}{d x}}-4 \frac{d y}{d x}-7 x=0$
$$
\Rightarrow \frac{d y}{d x}=16\left(\frac{d y}{d x}\right)^{2}+49 x^{2}+56 x \frac{d y}{d x}
$$
Obviously, it is first order and second degree differential equation.

</details>

---

### Q43. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

The order of the differential equation whose solution is $y=a \cos x+b \sin x+c e^{-x}$, is

**Options:**

- **(A)** 3
- **(B)** 1
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

In given equation their are three parameters, so its differential equation is third order differential equation.

</details>

---

