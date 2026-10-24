# MHT CET Mathematics - Complex Number

## Topic 7: Cube Root of Unity

**Total Questions:** 18

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are complex cube roots of unity, then the difference between the values of $\alpha^2 + \beta^2 + \alpha\beta$ and $\alpha^4 + \beta^4 + \alpha^{-1}\beta^{-1}$ is

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $4$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0$**

**Detailed Solution:**

Let $\alpha = \omega$ and $\beta = \omega^2$, where $\omega$ is a complex cube root of unity.

We know that $\omega^3 = 1$ and $1 + \omega + \omega^2 = 0$.

The first expression is $\alpha^2 + \beta^2 + \alpha\beta$.

Substituting the values, we get $\omega^2 + (\omega^2)^2 + \omega(\omega^2) = \omega^2 + \omega^4 + \omega^3$.

Since $\omega^4 = \omega$ and $\omega^3 = 1$, this becomes $\omega^2 + \omega + 1 = 0$.

The second expression is $\alpha^4 + \beta^4 + \alpha^{-1}\beta^{-1}$.

Substituting the values, we get $\omega^4 + (\omega^2)^4 + (\omega)^{-1}(\omega^2)^{-1} = \omega^4 + \omega^8 + \omega^{-3}$.

Since $\omega^4 = \omega$, $\omega^8 = \omega^2$, and $\omega^{-3} = 1$, this becomes $\omega + \omega^2 + 1 = 0$.

The difference between the two expressions is $0 - 0 = 0$.

Answer: $0$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $w = -\dfrac{1}{2} + \dfrac{i\sqrt{3}}{2}$, then the value of $\begin{vmatrix} 1 & 1 & 1 \\ 1 & -1-w^2 & w^2 \\ 1 & w^2 & w^4 \end{vmatrix}$ is...

**Options:**

- **(A)** $3w(w+1)$
- **(B)** $3w(w-1)$
- **(C)** $-3w(w-1)$
- **(D)** $-3w(w+1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3w(w-1)$**

**Detailed Solution:**

Given $w = -\dfrac{1}{2} + \dfrac{i\sqrt{3}}{2}$, $w$ is a complex cube root of unity.

Thus, $w^3 = 1$ and $1 + w + w^2 = 0$.

From this, we have $-1 - w^2 = w$ and $w^4 = w^3 \cdot w = w$.

Substituting these into the given determinant:

$\Delta = \begin{vmatrix} 1 & 1 & 1 \\\\ 1 & w & w^2 \\\\ 1 & w^2 & w \end{vmatrix}$

Applying the column operation $C_1 \rightarrow C_1 + C_2 + C_3$, we get:

$\Delta = \begin{vmatrix} 3 & 1 & 1 \\\\ 1+w+w^2 & w & w^2 \\\\ 1+w^2+w & w^2 & w \end{vmatrix}$

Since $1 + w + w^2 = 0$, this simplifies to:

$\Delta = \begin{vmatrix} 3 & 1 & 1 \\\\ 0 & w & w^2 \\\\ 0 & w^2 & w \end{vmatrix}$

Expanding along the first column:

$\Delta = 3(w^2 - w^4)$

Since $w^4 = w$, we get:

$\Delta = 3(w^2 - w) = 3w(w - 1)$

Answer: $3w(w-1)$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\omega$ is a complex cube root of unity, then the value of the expression $(1 - \omega + \omega^2)^7 + (1 + \omega - \omega^2)^7$ is equal to...

**Options:**

- **(A)** $128$
- **(B)** $-128$
- **(C)** $128\omega$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $128$**

**Detailed Solution:**

Since $\omega$ is a complex cube root of unity, $1 + \omega + \omega^2 = 0$ and $\omega^3 = 1$.

From this, we have $1 + \omega^2 = -\omega$ and $1 + \omega = -\omega^2$.

Substituting these into the given expression:

$(1 - \omega + \omega^2)^7 + (1 + \omega - \omega^2)^7 = (-\omega - \omega)^7 + (-\omega^2 - \omega^2)^7$

$= (-2\omega)^7 + (-2\omega^2)^7$

$= -128\omega^7 - 128\omega^{14}$

Using $\omega^3 = 1$, we get $\omega^7 = (\omega^3)^2 \cdot \omega = \omega$ and $\omega^{14} = (\omega^3)^4 \cdot \omega^2 = \omega^2$.

The expression becomes:

$= -128\omega - 128\omega^2$

$= -128(\omega + \omega^2)$

Since $\omega + \omega^2 = -1$, we get:

$= -128(-1) = 128$

Answer: $128$

</details>

---

### Q4. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $w$ is a complex cube root of unity , then the value of $w^{10} - w^7 + w^5 - w^2 + 1$ is.

**Options:**

- **(A)** $0$
- **(B)** $-1$
- **(C)** $1$
- **(D)** $w$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

Since $w$ is a complex cube root of unity, $w^3 = 1$ and $1 + w + w^2 = 0$.

Simplifying each term using $w^3 = 1$:

$w^{10} = (w^3)^3 \cdot w = 1 \cdot w = w$

$w^7 = (w^3)^2 \cdot w = 1 \cdot w = w$

$w^5 = w^3 \cdot w^2 = 1 \cdot w^2 = w^2$

Substituting these values into the given expression:

$w^{10} - w^7 + w^5 - w^2 + 1 = w - w + w^2 - w^2 + 1$

$= 0 + 0 + 1 = 1$

Answer: $1$

</details>

---

### Q5. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The value of $\left(\dfrac{-1+i\sqrt{3}}{2}\right)^{18} + \left(\dfrac{-1-i\sqrt{3}}{2}\right)^{18}$ is

**Options:**

- **(A)** $2$
- **(B)** $35$
- **(C)** $\sqrt{3}$
- **(D)** $\dfrac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Let $\omega = \dfrac{-1+i\sqrt{3}}{2}$ and $\omega^2 = \dfrac{-1-i\sqrt{3}}{2}$ be the complex cube roots of unity.

The given expression can be written as $\omega^{18} + (\omega^2)^{18}$.

Since $\omega^3 = 1$, we have $\omega^{18} = (\omega^3)^6 = 1^6 = 1$.

Similarly, $(\omega^2)^{18} = \omega^{36} = (\omega^3)^{12} = 1^{12} = 1$.

Therefore, the value of the expression is $1 + 1 = 2$.

Answer: $2$

</details>

---

### Q6. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\alpha$ and $\beta$ are the distinct roots of the equation $x^2 - x + 1 = 0$, then the value of $\alpha^{200} + \beta^{206} + 2$ is equal to

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $0$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

Given equation: $x^2 - x + 1 = 0$

Multiplying both sides by $(x + 1)$, we get:

$(x + 1)(x^2 - x + 1) = 0$

$x^3 + 1 = 0 \Rightarrow x^3 = -1$

Since $\alpha$ and $\beta$ are roots of $x^2 - x + 1 = 0$, they satisfy the equation $x^3 = -1$.

Therefore, $\alpha^3 = -1$ and $\beta^3 = -1$.

Now, evaluating the given expression $\alpha^{200} + \beta^{206} + 2$ :

$\alpha^{200} = (\alpha^3)^{66} \cdot \alpha^2 = (-1)^{66} \cdot \alpha^2 = \alpha^2$

$\beta^{206} = (\beta^3)^{68} \cdot \beta^2 = (-1)^{68} \cdot \beta^2 = \beta^2$

Substituting these values, the expression becomes $\alpha^2 + \beta^2 + 2$.

From the given quadratic equation, the sum of roots $\alpha + \beta = 1$ and the product of roots $\alpha \beta = 1$.

Using the identity $\alpha^2 + \beta^2 = (\alpha + \beta)^2 - 2\alpha\beta$ :

$\alpha^2 + \beta^2 = (1)^2 - 2(1) = -1$

Therefore, $\alpha^{200} + \beta^{206} + 2 = -1 + 2 = 1$.

</details>

---

### Q7. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\omega$ is a complex cube root of unity, then the value of $\sin\left[\pi(\omega^{10} + \omega^{23}) - \dfrac{\pi}{4}\right] =$

**Options:**

- **(A)** $-\dfrac{\sqrt{3}}{2}$
- **(B)** $-\dfrac{1}{\sqrt{2}}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $\dfrac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{\sqrt{2}}$**

**Detailed Solution:**

Since $\omega$ is a complex cube root of unity, $\omega^3 = 1$ and $1 + \omega + \omega^2 = 0$.

$\omega^{10} = (\omega^3)^3 \cdot \omega = \omega$

$\omega^{23} = (\omega^3)^7 \cdot \omega^2 = \omega^2$

$\omega^{10} + \omega^{23} = \omega + \omega^2 = -1$

Substituting this into the given expression:

$\sin\left[\pi(\omega^{10} + \omega^{23}) - \dfrac{\pi}{4}\right] = \sin\left(-\pi - \dfrac{\pi}{4}\right)$

$= \sin\left(-\dfrac{5\pi}{4}\right)$

$= -\sin\left(\pi + \dfrac{\pi}{4}\right)$

$= -\left(-\sin\dfrac{\pi}{4}\right)$

$= \dfrac{1}{\sqrt{2}}$

Answer: $\dfrac{1}{\sqrt{2}}$

</details>

---

### Q8. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\omega$ is a complex cube root of unity, then the value of the expression $2\left(1+\dfrac{1}{\omega}\right)\left(1+\dfrac{1}{\omega^2}\right) + 3\left(2+\dfrac{1}{\omega}\right)\left(2+\dfrac{1}{\omega^2}\right) + \ldots + (n+1)\left(n+\dfrac{1}{\omega}\right)\left(n+\dfrac{1}{\omega^2}\right)$ is...

**Options:**

- **(A)** $\left[\dfrac{n(n+1)}{2}\right]^2 + n$
- **(B)** $\left[\dfrac{n(n+1)}{2}\right]^2 - n$
- **(C)** $\left[\dfrac{n(n+1)}{2}\right]^2$
- **(D)** $\left[\dfrac{n(n-1)}{2}\right]^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\dfrac{n(n+1)}{2}\right]^2 + n$**

**Detailed Solution:**

The general term of the given series is $T_k = (k+1)\left(k+\dfrac{1}{\omega}\right)\left(k+\dfrac{1}{\omega^2}\right)$.

Since $\omega^3 = 1$, we have $\dfrac{1}{\omega} = \omega^2$ and $\dfrac{1}{\omega^2} = \omega$.

$T_k = (k+1)(k+\omega^2)(k+\omega)$

$T_k = (k+1)(k^2 + k(\omega+\omega^2) + \omega^3)$

Using $1+\omega+\omega^2 = 0 \Rightarrow \omega+\omega^2 = -1$ and $\omega^3 = 1$, we get:

$T_k = (k+1)(k^2 - k + 1)$

$T_k = k^3 + 1$

The sum of the series up to $n$ terms is:

$S_n = \sum_{k=1}^n T_k = \sum_{k=1}^n (k^3 + 1)$

$S_n = \sum_{k=1}^n k^3 + \sum_{k=1}^n 1$

$S_n = \left[\dfrac{n(n+1)}{2}\right]^2 + n$

</details>

---

### Q9. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x = \sqrt{-1-\sqrt{-1-\sqrt{-1-\ldots\infty}}}$, where $\omega$ is a non-real complex cube root of unity, then the value of $x$ is...

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $-\omega$
- **(D)** $\omega^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\omega^2$**

**Detailed Solution:**

Given $x = \sqrt{-1-\sqrt{-1-\sqrt{-1-\ldots\infty}}}$

Squaring both sides, we get:

$x^2 = -1 - \sqrt{-1-\sqrt{-1-\ldots\infty}}$

$x^2 = -1 - x$

$x^2 + x + 1 = 0$

Solving this quadratic equation, we get:

$x = \dfrac{-1 \pm \sqrt{1 - 4}}{2} = \dfrac{-1 \pm i\sqrt{3}}{2}$

Thus, $x = \omega$ or $x = \omega^2$, where $\omega$ is a non-real complex cube root of unity.

Among the given options, $\omega^2$ is the correct choice.

Answer: $\omega^2$

</details>

---

### Q10. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are the roots of the equation $x^2 + x + 1 = 0$ then $\alpha^{2026} + \beta^{2026} = $

**Options:**

- **(A)** $-1$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-1$**

**Detailed Solution:**

The roots of the equation $x^2 + x + 1 = 0$ are the complex cube roots of unity, $\omega$ and $\omega^2$.

Let $\alpha = \omega$ and $\beta = \omega^2$.

Substituting the values of $\alpha$ and $\beta$ into the given expression gives $\omega^{2026} + (\omega^2)^{2026} = \omega^{2026} + \omega^{4052}$.

Since $\omega^3 = 1$, dividing the exponents by $3$ yields the remainders.

$2026 = 3 \times 675 + 1 \Rightarrow \omega^{2026} = \omega$

$4052 = 3 \times 1350 + 2 \Rightarrow \omega^{4052} = \omega^2$

Therefore, $\alpha^{2026} + \beta^{2026} = \omega + \omega^2$.

Using the property $1 + \omega + \omega^2 = 0$, we get $\omega + \omega^2 = -1$.

Thus, $\alpha^{2026} + \beta^{2026} = -1$.

</details>

---

### Q11. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The area of the triangle whose vertices are $i, \omega$ and $\omega^2$ is (Where $\omega$ is a complex cube root of unity other than $1, \mathrm{i}$ is an imaginary number) ______ sq.units

**Options:**

- **(A)** $\frac{3 \sqrt{3}}{4}$
- **(B)** $\frac{\sqrt{3}}{2}$
- **(C)** $\frac{3 \sqrt{3}}{2}$
- **(D)** $\frac{\sqrt{3}}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\sqrt{3}}{4}$**

**Detailed Solution:**

The vertices of the triangle in the complex plane are $z_1 = i$, $z_2 = \omega$, and $z_3 = \omega^2$.

The coordinates of these vertices are:
$z_1 = (0, 1)$
$z_2 = \left(-\dfrac{1}{2}, \dfrac{\sqrt{3}}{2}\right)$
$z_3 = \left(-\dfrac{1}{2}, -\dfrac{\sqrt{3}}{2}\right)$

The base of the triangle is the distance between $z_2$ and $z_3$:
$\text{Base} = |z_2 - z_3| = |\omega - \omega^2| = \left| i\sqrt{3} \right| = \sqrt{3}$

The line joining $z_2$ and $z_3$ is vertical and has the equation $x = -\dfrac{1}{2}$.

The height of the triangle is the perpendicular distance from $z_1(0, 1)$ to the line $x = -\dfrac{1}{2}$:
$\text{Height} = \left| 0 - \left(-\dfrac{1}{2}\right) \right| = \dfrac{1}{2}$

The area of the triangle is:
$\text{Area} = \dfrac{1}{2} \times \text{Base} \times \text{Height} = \dfrac{1}{2} \times \sqrt{3} \times \dfrac{1}{2} = \dfrac{\sqrt{3}}{4}$ sq. units.

Answer: $\frac{\sqrt{3}}{4}$

</details>

---

### Q12. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{w}=\dfrac{-1+\mathrm{i} \sqrt{3}}{2}$, where $\mathrm{i}=\sqrt{-1}$, then the value of $\left(3+w+3 w^2\right)^4$ is

**Options:**

- **(A)** 16
- **(B)** -16
- **(C)** 16 w
- **(D)** $16 w^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 16 w**

**Detailed Solution:**

Given $w = \dfrac{-1+\mathrm{i} \sqrt{3}}{2}$, which is the complex cube root of unity.

We know the properties of the cube root of unity: $1 + w + w^2 = 0$ and $w^3 = 1$.

Consider the expression $(3 + w + 3w^2)^4$.

Rearranging the terms inside the bracket:

$3 + w + 3w^2 = 3(1 + w^2) + w$

Using $1 + w^2 = -w$, we get:

$3(-w) + w = -3w + w = -2w$

Now, substitute this back into the given expression:

$(-2w)^4 = 16w^4$

Since $w^3 = 1$, we have $w^4 = w^3 \cdot w = 1 \cdot w = w$.

Therefore, the value is $16w$.

Answer: 16 w

</details>

---

### Q13. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $z^2+z+1=0$ then $\left(z^3+\dfrac{1}{z^3}\right)^2+\left(z^4+\dfrac{1}{z^4}\right)^2=$ where $\mathrm{z}=\mathrm{w}=$ complex cube root of unity

**Options:**

- **(A)** 4
- **(B)** 1
- **(C)** 5
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Given $z^2+z+1=0$, the roots are the complex cube roots of unity, so $z = \omega$ or $z = \omega^2$.

We know that $\omega^3 = 1$ and $1 + \omega + \omega^2 = 0$.

For $z = \omega$, the first term is $z^3 + \dfrac{1}{z^3} = \omega^3 + \dfrac{1}{\omega^3} = 1 + 1 = 2$.

The second term is $z^4 + \dfrac{1}{z^4} = \omega^4 + \dfrac{1}{\omega^4}$.

Since $\omega^3 = 1$, we have $\omega^4 = \omega$.

Thus, $\omega^4 + \dfrac{1}{\omega^4} = \omega + \dfrac{1}{\omega} = \omega + \omega^2$.

Using $1 + \omega + \omega^2 = 0$, we get $\omega + \omega^2 = -1$.

Substituting these values into the given expression:

$\left(z^3+\dfrac{1}{z^3}\right)^2+\left(z^4+\dfrac{1}{z^4}\right)^2 = (2)^2 + (-1)^2 = 4 + 1 = 5$.

Answer: 5

</details>

---

### Q14. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\omega \neq 1$ be a cube root of unity and $S$ be the set of all non-singular matrices of the form $\left[\begin{array}{ccc}1 & a & b \\ \omega & 1 & c \\ \omega^2 & \omega & 1\end{array}\right]$ where each of $a, b$ and $c$ is either $\omega$ or $\omega^2$, then the number of distinct matrices in the set $\mathrm{S}$ is

**Options:**

- **(A)** $2$
- **(B)** $6$
- **(C)** $4$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2$**

**Detailed Solution:**

Let $A=\left[\begin{array}{ccc}1 & a & b \\ \omega & 1 & c \\ \omega^2 & \omega & 1\end{array}\right]$ For non-singular matrix
$$
\begin{aligned}
& |\mathrm{A}| \neq 0 \\
& \Rightarrow\left|\begin{array}{ccc}
1 & \mathrm{a} & \mathrm{b} \\
\omega & 1 & \mathrm{c} \\
\omega^2 & \omega & 1
\end{array}\right| \neq 0
\end{aligned}
$$
$$
\begin{aligned}
& \Rightarrow 1(1-\omega c)-a\left(\omega-\omega^2 c\right)+b(0) \neq 0 \\
& \Rightarrow 1(1-\omega c)-a \omega(1-\omega c) \neq 0 \\
& \Rightarrow(1-\omega c)(1-a \omega) \neq 0 \\
& \Rightarrow c \neq \frac{1}{\omega} \text { and } a \neq \frac{1}{\omega} \\
& \Rightarrow c \neq \omega^2 \text { and } a \neq \omega^2 \quad \ldots\left[\because \omega^3=1\right]
\end{aligned}
$$

So possible value of a and $\mathrm{c}$ is $\omega$ only and $\mathrm{b}$ can take values $\omega$ or $\omega^2$.
$\therefore \quad$ The possible number of distinct matrices $=2$.

</details>

---

### Q15. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are the complex cube roots of unity, then $\alpha^3+\beta^3+\alpha^{-2} \times \beta^{-2}$ is equal to

**Options:**

- **(A)** $1$
- **(B)** $-3$
- **(C)** $3$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

$\begin{aligned} & \alpha^3+\beta^3+\alpha^{-2} \cdot \beta^{-2}=\alpha^3+\beta^3+\frac{1}{\alpha^2 \beta^2} \\ & =\omega^3+\omega^6+\frac{1}{\omega^2 \omega^4}=1+1+1=3\end{aligned}$

</details>

---

### Q16. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\alpha$ and $\beta$ are imaginary cube roots of units then value of $\alpha^4+\beta^{28}+\frac{1}{\alpha \beta}$ is

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $-1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

Let $\alpha=\omega, \beta=\omega^2$
Now $\alpha^4+\beta^{28}+\frac{1}{\alpha \beta}$
$\begin{aligned} & =\omega^4+\left(\omega^2\right)^{28}+\frac{1}{\omega \omega^2} \\ & =\omega^4+\omega^{56}+\frac{1}{\omega^3} \\ & =\omega+\omega^2+\frac{1}{1} \\ & \left.=0 \quad \quad \quad \text { [as } \omega^3=1\right]\end{aligned}$

</details>

---

### Q17. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\omega$ is the complex cube root of unity, the
$$
\left(3+5 \omega+3 \omega^2\right)^2+\left(3+3 \omega+5 \omega^2\right)^2=
$$

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 4
- **(D)** -4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -4**

**Detailed Solution:**

$\begin{aligned} & \left(3+5 \omega+3 \omega^2\right)^2+\left(3+3 \omega+5 \omega^2\right)^2 \\ & =\left(3+3 \omega+3 \omega^2+2 \omega\right)^2+\left(3+3 \omega+3 \omega^2+2 \omega^2\right)^2 \\ & =\left[3\left(1+\omega+\omega^2\right)+2 \omega\right]^2+\left[3\left(1+\omega+\omega^2\right)+2 \omega^2\right]^2 \\ & =(3(0)+2 \omega)^2+\left[3(0)+2 \omega^2\right]^2=4 \omega^2+4 \omega^4 \\ & =4 \omega^2\left(1+\omega^2\right)=4 \omega^2(-\omega) \\ & =-4 \omega^2=-4\end{aligned}$

</details>

---

### Q18. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $\omega$ is complex cube root of unity and $(1+\omega)^7=\mathrm{A}+\mathrm{B} \omega$, then values of A and B are, respectively.

**Options:**

- **(A)** 0,1
- **(B)** 1,0
- **(C)** 1,1
- **(D)** $-1,1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1,1**

**Detailed Solution:**

$\begin{aligned} & (1+\omega)^7=\mathrm{A}+\mathrm{B} \omega \\ & \therefore \mathrm{A}+\mathrm{B} \omega=\left(-\omega^2\right)^7 \quad \ldots\left(\because 1+\omega+\omega^2=0\right] \\ & =(-1) \omega^{14}=-\omega^{12} \omega^2=-\omega^2=(1+\omega) \\ & \therefore A=1, B=1\end{aligned}$

</details>

---

