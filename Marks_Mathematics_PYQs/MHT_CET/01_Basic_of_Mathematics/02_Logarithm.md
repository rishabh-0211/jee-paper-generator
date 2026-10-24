# MHT CET Mathematics - Basic of Mathematics

## Topic 2: Logarithm

**Total Questions:** 8

---

### Q1. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given $\log_{10} 2 = 0.3010$. Then the number of digits in the number $20^{10}$ is...

**Options:**

- **(A)** $11$
- **(B)** $12$
- **(C)** $13$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $14$**

**Detailed Solution:**

Let $N = 20^{10}$

Taking logarithm to the base $10$, we get

$\log_{10} N = \log_{10} (20^{10})$

$\log_{10} N = 10 \log_{10} (2 \times 10)$

$\log_{10} N = 10 (\log_{10} 2 + \log_{10} 10)$

Substituting the value of $\log_{10} 2 = 0.3010$, we get

$\log_{10} N = 10 (0.3010 + 1)$

$\log_{10} N = 10 (1.3010) = 13.010$

The characteristic of the logarithm is $13$.

The number of digits in $N$ is given by characteristic $+ 1$.

Number of digits $= 13 + 1 = 14$.

Answer: $14$

</details>

---

### Q2. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $x$, y, z are the sides of a right angled triangle, where z is the largest side, then $\dfrac{1}{\log_{x+z} y} + \dfrac{1}{\log_{z-x} y} =$

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $3$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Since $x, y, z$ are the sides of a right-angled triangle and $z$ is the largest side, $z$ is the hypotenuse.

By Pythagoras theorem, $x^2 + y^2 = z^2$, which gives $y^2 = z^2 - x^2$.

The given expression is $\dfrac{1}{\log_{x+z} y} + \dfrac{1}{\log_{z-x} y}$.

Using the property $\dfrac{1}{\log_a b} = \log_b a$, the expression can be written as:

$\log_y (x+z) + \log_y (z-x)$

Using the property $\log_a m + \log_a n = \log_a (mn)$, we get:

$\log_y ((x+z)(z-x))$

$\Rightarrow \log_y (z^2 - x^2)$

Substituting $z^2 - x^2 = y^2$, we get:

$\log_y (y^2) = 2 \log_y y = 2$

Answer: $2$

</details>

---

### Q3. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $p^3=q^4=r^6=t^7=s^2$, then $\log _t(p q r s)=\ldots$.

**Options:**

- **(A)** $\frac{168}{5}$
- **(B)** 28
- **(C)** $\frac{31}{4}$
- **(D)** $\frac{35}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{35}{4}$**

**Detailed Solution:**

Let $p^3 = q^4 = r^6 = t^7 = s^2 = k$

Expressing $p, q, r, s$ and $t$ in terms of $k$:

$p = k^{1/3}$, $q = k^{1/4}$, $r = k^{1/6}$, $s = k^{1/2}$, $t = k^{1/7}$

Finding the product $pqrs$:

$pqrs = k^{1/3} \cdot k^{1/4} \cdot k^{1/6} \cdot k^{1/2}$

$pqrs = k^{1/3 + 1/4 + 1/6 + 1/2}$

$pqrs = k^{\dfrac{4 + 3 + 2 + 6}{12}} = k^{\dfrac{15}{12}} = k^{\dfrac{5}{4}}$

Substituting the values in terms of $k$ into the logarithm:

$\log_t(pqrs) = \log_{k^{1/7}}(k^{5/4})$

Using the property $\log_{a^m}(a^n) = \dfrac{n}{m}$:

$\log_t(pqrs) = \dfrac{\dfrac{5}{4}}{\dfrac{1}{7}} = \dfrac{5}{4} \times 7 = \dfrac{35}{4}$

Answer: $\frac{35}{4}$

</details>

---

### Q4. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\sqrt{\log _3 x^{16}}+9 \log _{27} \sqrt[3]{\frac{3}{x}}=5$
then $x=\ldots$.

**Options:**

- **(A)** $81$
- **(B)** $\frac{1}{405}$
- **(C)** $27$
- **(D)** $405$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $81$**

**Detailed Solution:**

Given equation: $\sqrt{\log _3 x^{16}}+9 \log _{27} \sqrt[3]{\dfrac{3}{x}}=5$

Simplify the first term:
$\sqrt{\log _3 x^{16}} = \sqrt{16 \log _3 x} = 4 \sqrt{\log _3 x}$

Simplify the second term:
$9 \log _{27} \sqrt[3]{\dfrac{3}{x}} = 9 \log _{3^3} \left(\dfrac{3}{x}\right)^{\dfrac{1}{3}}$

Using the property $\log_{a^m} b^n = \dfrac{n}{m} \log_a b$:
$9 \times \dfrac{\dfrac{1}{3}}{3} \log _3 \left(\dfrac{3}{x}\right) = 9 \times \dfrac{1}{9} \log _3 \left(\dfrac{3}{x}\right) = \log _3 \left(\dfrac{3}{x}\right)$

Using the quotient rule for logarithms:
$\log _3 \left(\dfrac{3}{x}\right) = \log _3 3 - \log _3 x = 1 - \log _3 x$

Substitute these back into the original equation:
$4 \sqrt{\log _3 x} + 1 - \log _3 x = 5$

Let $t = \sqrt{\log _3 x}$. Then $\log _3 x = t^2$. The equation becomes:
$4t + 1 - t^2 = 5$

$t^2 - 4t + 4 = 0$

$(t - 2)^2 = 0$

$t = 2$

Substituting back $t = \sqrt{\log _3 x}$:
$\sqrt{\log _3 x} = 2$

$\log _3 x = 4$

$x = 3^4 = 81$

Answer: $81$

</details>

---

### Q5. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $x+\log _{15}\left(5+3^x\right)=x \log _{15} 5+\log _{15} 24$, then $x=\ldots .$.

**Options:**

- **(A)** $1$
- **(B)** $5$
- **(C)** $2$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

The given equation is:

$x + \log_{15}(5 + 3^x) = x \log_{15} 5 + \log_{15} 24$

Rearranging the terms, we get:

$x - x \log_{15} 5 + \log_{15}(5 + 3^x) = \log_{15} 24$

$x(1 - \log_{15} 5) + \log_{15}(5 + 3^x) = \log_{15} 24$

Using $1 = \log_{15} 15$, we have:

$x(\log_{15} 15 - \log_{15} 5) + \log_{15}(5 + 3^x) = \log_{15} 24$

$x \log_{15} \left(\dfrac{15}{5}\right) + \log_{15}(5 + 3^x) = \log_{15} 24$

$x \log_{15} 3 + \log_{15}(5 + 3^x) = \log_{15} 24$

$\log_{15}(3^x) + \log_{15}(5 + 3^x) = \log_{15} 24$

Using the property $\log a + \log b = \log(ab)$:

$\log_{15}(3^x(5 + 3^x)) = \log_{15} 24$

Equating the arguments:

$3^x(5 + 3^x) = 24$

Let $3^x = y$. Then the equation becomes:

$y(5 + y) = 24$

$y^2 + 5y - 24 = 0$

$(y + 8)(y - 3) = 0$

$y = -8$ or $y = 3$

Since $3^x > 0$ for all real $x$, we must have $y = 3$.

$3^x = 3$

$x = 1$

Answer: $1$

</details>

---

### Q6. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The approximate value of $\log _{10} 1002$ is (Given $\log _{10} \mathrm{e}=0.4343$ )

**Options:**

- **(A)** 3.0117
- **(B)** 3.0009
- **(C)** 2.9999
- **(D)** 3.1119

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3.0009**

**Detailed Solution:**

Let $y = \log_{10} x$

Differentiating with respect to $x$, we get $\dfrac{dy}{dx} = \dfrac{1}{x} \log_{10} e$

Let $x = 1000$ and $\Delta x = 2$

$\Delta y \approx \dfrac{dy}{dx} \Delta x = \dfrac{1}{1000} \times 0.4343 \times 2 = 0.0008686$

The approximate value is $y + \Delta y = \log_{10} 1000 + 0.0008686 = 3 + 0.0008686 = 3.0008686$

Rounding off to four decimal places, we get $3.0009$

Answer: 3.0009

</details>

---

### Q7. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $y=[(x+1)(2 x+1)(3 x+1) \ldots \ldots \ldots \ldots(\mathrm{n} x+1)]^4$ then $\dfrac{\mathrm{d} y}{\mathrm{~d} x}$ at $x=0$ is

**Options:**

- **(A)** $\dfrac{\mathrm{n}(\mathrm{n}+1)}{2}$
- **(B)** $4 \mathrm{n}(\mathrm{n}+1)$
- **(C)** $\left(\dfrac{\mathrm{n}(\mathrm{n}+1)}{2}\right)^2$
- **(D)** $2 \mathrm{n}(\mathrm{n}+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 \mathrm{n}(\mathrm{n}+1)$**

**Detailed Solution:**

Given $y = [(x+1)(2x+1)(3x+1) \dots (nx+1)]^4$

Taking natural logarithm on both sides:

$\ln y = 4 [\ln(x+1) + \ln(2x+1) + \ln(3x+1) + \dots + \ln(nx+1)]$

Differentiating with respect to $x$:

$\dfrac{1}{y} \dfrac{\mathrm{d}y}{\mathrm{d}x} = 4 \left[ \dfrac{1}{x+1} + \dfrac{2}{2x+1} + \dfrac{3}{3x+1} + \dots + \dfrac{\mathrm{n}}{\mathrm{n}x+1} \right]$

Substituting $x = 0$, we get $y = [(0+1)(0+1)(0+1) \dots (0+1)]^4 = 1$

$\dfrac{1}{1} \left( \dfrac{\mathrm{d}y}{\mathrm{d}x} \right)_{x=0} = 4 \left[ \dfrac{1}{0+1} + \dfrac{2}{0+1} + \dfrac{3}{0+1} + \dots + \dfrac{\mathrm{n}}{0+1} \right]$

$\left( \dfrac{\mathrm{d}y}{\mathrm{d}x} \right)_{x=0} = 4 [1 + 2 + 3 + \dots + \mathrm{n}]$

$\left( \dfrac{\mathrm{d}y}{\mathrm{d}x} \right)_{x=0} = 4 \left( \dfrac{\mathrm{n}(\mathrm{n}+1)}{2} \right) = 2\mathrm{n}(\mathrm{n}+1)$

Answer: $2 \mathrm{n}(\mathrm{n}+1)$

</details>

---

### Q8. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\log _2 x+\log _4 x+\log _y x+\log _{16} x-\frac{25}{36}$ and $x=2^k$, then $k$ is

**Options:**

- **(A)** 1
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned}
& \log _2 x+\log _4 x+\log _8 x+\log _{16} x=\frac{25}{36} \\
& \frac{\log x}{\log 2}+\frac{\log x}{\log 4}+\frac{\log x}{\log 8}+\frac{\log x}{\log 16}=\frac{25}{36} \\
& \frac{\log x}{\log 2}+\frac{\log x}{2 \log 2}+\frac{\log x}{3 \log 2}+\frac{\log x}{4 \log 2}=\frac{25}{36} \\
& \frac{\log x}{\log 2}\left[1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}\right]=\frac{25}{36} \\
& \frac{\log x}{\log 2}\left[\frac{25}{12}\right]=\frac{25}{36} \\
& \frac{25}{12} \log _2 x=\frac{25}{36} \\
& \log _2 x=\frac{1}{3} \\
& \therefore \quad x=2^{\frac{1}{3}} \\
&
\end{aligned}$
But $x=2^{\mathrm{k}}$ ... [Given]
$\therefore \quad \mathrm{k}=\frac{1}{3}$

</details>

---

