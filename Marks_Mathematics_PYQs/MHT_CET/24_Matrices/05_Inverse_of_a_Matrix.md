# MHT CET Mathematics - Matrices

## Topic 5: Inverse of a Matrix

**Total Questions:** 104

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the matrix $\begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix}$ and its multiplicative inverse is

**Options:**

- **(A)** $\begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix}$
- **(B)** $\begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix}$
- **(C)** $\begin{bmatrix} -5 & 0 \\ 0 & -5 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\begin{bmatrix} -5 & 0 \\ 0 & -5 \end{bmatrix}$**

**Detailed Solution:**

Let $A = \begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix}$

The determinant of $A$ is $|A| = (2)(-7) - (-3)(5) = -14 + 15 = 1$

The multiplicative inverse of $A$ is $A^{-1} = \dfrac{1}{|A|} \text{adj}(A) = \begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix}$

The sum of the matrix and its inverse is $A + A^{-1} = \begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix} + \begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix} = \begin{bmatrix} -5 & 0 \\ 0 & -5 \end{bmatrix}$

Answer: $\begin{bmatrix} -5 & 0 \\ 0 & -5 \end{bmatrix}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 1 & 2 \\ -5 & 1 \end{bmatrix}$ and $A^{-1} = xA + yI$, then the pair $(x,y) = \cdots$

**Options:**

- **(A)** $\left(\dfrac{1}{11}, \dfrac{2}{11}\right)$
- **(B)** $\left(\dfrac{1}{11}, -\dfrac{2}{11}\right)$
- **(C)** $\left(-\dfrac{1}{11}, -\dfrac{2}{11}\right)$
- **(D)** $\left(-\dfrac{1}{11}, \dfrac{2}{11}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(-\dfrac{1}{11}, \dfrac{2}{11}\right)$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\begin{vmatrix} 1 - \lambda & 2 \\ -5 & 1 - \lambda \end{vmatrix} = 0$

$(1 - \lambda)^2 + 10 = 0$

$\lambda^2 - 2\lambda + 11 = 0$

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation. Thus,

$A^2 - 2A + 11I = 0$

Multiplying both sides by $A^{-1}$, we get:

$A - 2I + 11A^{-1} = 0$

$11A^{-1} = -A + 2I$

$A^{-1} = -\dfrac{1}{11}A + \dfrac{2}{11}I$

Comparing this with the given equation $A^{-1} = xA + yI$, we obtain:

$x = -\dfrac{1}{11}, y = \dfrac{2}{11}$

The pair $(x,y)$ is $\left(-\dfrac{1}{11}, \dfrac{2}{11}\right)$.

Answer: $\left(-\dfrac{1}{11}, \dfrac{2}{11}\right)$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A = \begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix}$, then $A - A^{-1} =$

**Options:**

- **(A)** $\begin{bmatrix} -9 & 6 \\ -10 & 9 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 9 & -6 \\ 10 & -9 \end{bmatrix}$
- **(C)** $\begin{bmatrix} -9 & 10 \\ -6 & 9 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 9 & -10 \\ 6 & -9 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{bmatrix} 9 & -6 \\ 10 & -9 \end{bmatrix}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix}$

The determinant of $A$ is $|A| = (2)(-7) - (-3)(5) = -14 + 15 = 1$

The inverse of $A$ is $A^{-1} = \dfrac{1}{|A|} \begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix} = \begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix}$

Now, $A - A^{-1} = \begin{bmatrix} 2 & -3 \\ 5 & -7 \end{bmatrix} - \begin{bmatrix} -7 & 3 \\ -5 & 2 \end{bmatrix}$

$A - A^{-1} = \begin{bmatrix} 2 - (-7) & -3 - 3 \\ 5 - (-5) & -7 - 2 \end{bmatrix} = \begin{bmatrix} 9 & -6 \\ 10 & -9 \end{bmatrix}$

Answer: $\begin{bmatrix} 9 & -6 \\ 10 & -9 \end{bmatrix}$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A^{-1} = \begin{bmatrix} 1 & 0 & -4 \\ 0 & -1 & 2 \\ -1 & 2 & 1 \end{bmatrix} = \dfrac{\text{adj}(A)}{k}$, then $k$ is a root of the equation...

**Options:**

- **(A)** $x^2 + 1 = 0$
- **(B)** $x^2 - 1 = 0$
- **(C)** $x^2 - 2 = 0$
- **(D)** $x^2 - x + 1 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2 - 1 = 0$**

**Detailed Solution:**

We know that $A^{-1} = \dfrac{\text{adj}(A)}{|A|}$.

Given $A^{-1} = \dfrac{\text{adj}(A)}{k}$, we get $k = |A|$.

The determinant of $A^{-1}$ is given by:

$|A^{-1}| = \begin{vmatrix} 1 & 0 & -4 \\ 0 & -1 & 2 \\ -1 & 2 & 1 \end{vmatrix}$

$|A^{-1}| = 1(-1 - 4) - 0 + (-4)(0 - 1)$

$|A^{-1}| = -5 + 4 = -1$

Since $|A| = \dfrac{1}{|A^{-1}|}$, we have:

$k = |A| = \dfrac{1}{-1} = -1$

Now, substituting $x = -1$ in the given options, we find that it satisfies the equation $x^2 - 1 = 0$.

Answer: $x^2 - 1 = 0$

</details>

---

### Q5. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the matrix $A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 1 & 5 \\ 2 & 4 & 7 \end{bmatrix}$ and its inverse is $A^{-1} = \begin{bmatrix} a & c & -7 \\ b & -1 & c \\ -2 & 0 & 1 \end{bmatrix}$, then ....

**Options:**

- **(A)** $a = 13,\ b = -3,\ c = 0$
- **(B)** $a = 13,\ b = 3,\ c = -2$
- **(C)** $a = 13,\ b = -7,\ c = 2$
- **(D)** $a = 13,\ b = -3,\ c = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a = 13,\ b = -3,\ c = 2$**

**Detailed Solution:**

Since $A A^{-1} = I$, we can multiply the matrices and equate the corresponding elements to the identity matrix.

$A A^{-1} = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 1 & 5 \\ 2 & 4 & 7 \end{bmatrix} \begin{bmatrix} a & c & -7 \\ b & -1 & c \\ -2 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

Multiplying the first row of $A$ with the second column of $A^{-1}$:
$1(c) + 2(-1) + 3(0) = 0 \Rightarrow c - 2 = 0 \Rightarrow c = 2$

Multiplying the second row of $A$ with the first column of $A^{-1}$:
$1(a) + 1(b) + 5(-2) = 0 \Rightarrow a + b = 10$

Multiplying the first row of $A$ with the first column of $A^{-1}$:
$1(a) + 2(b) + 3(-2) = 1 \Rightarrow a + 2b = 7$

Subtracting the equation $a + b = 10$ from $a + 2b = 7$:
$(a + 2b) - (a + b) = 7 - 10 \Rightarrow b = -3$

Substituting $b = -3$ into $a + b = 10$:
$a - 3 = 10 \Rightarrow a = 13$

Therefore, $a = 13$, $b = -3$, and $c = 2$.

Answer: $a = 13,\ b = -3,\ c = 2$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$, then $A^{-1} =$

**Options:**

- **(A)** $\dfrac{1}{6}(A - 4I)$
- **(B)** $\dfrac{1}{6}(A + 5I)$
- **(C)** $\dfrac{1}{6}(A + 4I)$
- **(D)** $\dfrac{1}{6}(A - 5I)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{6}(A - 5I)$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$(4 - \lambda)(1 - \lambda) - 10 = 0$

$\lambda^2 - 5\lambda - 6 = 0$

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation. Substituting $A$ for $\lambda$, we get:

$A^2 - 5A - 6I = 0$

Multiplying both sides by $A^{-1}$, we obtain:

$A - 5I - 6A^{-1} = 0$

$6A^{-1} = A - 5I$

$A^{-1} = \dfrac{1}{6}(A - 5I)$

Answer: $\dfrac{1}{6}(A - 5I)$

</details>

---

### Q7. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A^{-1} = \begin{bmatrix} 3 & -1 & 1 \\ -15 & 6 & -5 \\ 5 & -2 & 2 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1 \end{bmatrix}$, then $(AB)^{-1} =$

**Options:**

- **(A)** $\begin{bmatrix} 9 & -3 & 5 \\ -2 & 1 & 0 \\ 1 & 0 & 2 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 9 & 3 & -5 \\ -2 & -1 & 0 \\ 1 & 0 & 2 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 9 & -3 & 5 \\ -2 & -1 & 0 \\ 1 & 0 & -2 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 9 & -3 & 5 \\ -2 & 1 & 0 \\ 1 & 0 & -2 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} 9 & -3 & 5 \\ -2 & 1 & 0 \\ 1 & 0 & 2 \end{bmatrix}$**

**Detailed Solution:**

Using the property of the inverse of a product of matrices, $(AB)^{-1} = B^{-1} A^{-1}$.

First, we find $B^{-1}$. The determinant of $B$ is:
$|B| = 1(3 - 0) - 2(-1 - 0) - 2(2 - 0) = 3 + 2 - 4 = 1$

The cofactor matrix of $B$ is calculated as follows:
$C_{11} = 3, C_{12} = 1, C_{13} = 2$
$C_{21} = 2, C_{22} = 1, C_{23} = 2$
$C_{31} = 6, C_{32} = 2, C_{33} = 5$

The adjoint of $B$ is the transpose of the cofactor matrix:
$\text{adj}(B) = \begin{bmatrix} 3 & 2 & 6 \ 1 & 1 & 2 \ 2 & 2 & 5 \end{bmatrix}$

Since $|B| = 1$, $B^{-1} = \dfrac{1}{|B|} \text{adj}(B) = \begin{bmatrix} 3 & 2 & 6 \ 1 & 1 & 2 \ 2 & 2 & 5 \end{bmatrix}$.

Now, substituting $B^{-1}$ and $A^{-1}$ into the formula:
$(AB)^{-1} = B^{-1} A^{-1} = \begin{bmatrix} 3 & 2 & 6 \ 1 & 1 & 2 \ 2 & 2 & 5 \end{bmatrix} \begin{bmatrix} 3 & -1 & 1 \ -15 & 6 & -5 \ 5 & -2 & 2 \end{bmatrix}$

Multiplying the two matrices:
$(AB)^{-1} = \begin{bmatrix} 3(3) + 2(-15) + 6(5) & 3(-1) + 2(6) + 6(-2) & 3(1) + 2(-5) + 6(2) \ 1(3) + 1(-15) + 2(5) & 1(-1) + 1(6) + 2(-2) & 1(1) + 1(-5) + 2(2) \ 2(3) + 2(-15) + 5(5) & 2(-1) + 2(6) + 5(-2) & 2(1) + 2(-5) + 5(2) \end{bmatrix}$

$(AB)^{-1} = \begin{bmatrix} 9 - 30 + 30 & -3 + 12 - 12 & 3 - 10 + 12 \ 3 - 15 + 10 & -1 + 6 - 4 & 1 - 5 + 4 \ 6 - 30 + 25 & -2 + 12 - 10 & 2 - 10 + 10 \end{bmatrix}$

$(AB)^{-1} = \begin{bmatrix} 9 & -3 & 5 \ -2 & 1 & 0 \ 1 & 0 & 2 \end{bmatrix}$

Answer: $\begin{bmatrix} 9 & -3 & 5 \\ -2 & 1 & 0 \\ 1 & 0 & 2 \end{bmatrix}$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 2 & 1 \\ 3 & 2 \end{bmatrix}$ and $B = \begin{bmatrix} -1 & -1 \\ 1 & 1 \end{bmatrix}$. If the variables $x$ and $y$ satisfy the matrix equation $(A^{-1} + B)\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix}$, then the value of $x + 3y$ is......

**Options:**

- **(A)** $8$
- **(B)** $10$
- **(C)** $12$
- **(D)** $14$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 2 & 1 \\ 3 & 2 \end{bmatrix}$, the determinant is $|A| = 2(2) - 1(3) = 1$.

The inverse of $A$ is $A^{-1} = \begin{bmatrix} 2 & -1 \\ -3 & 2 \end{bmatrix}$.

Adding $B = \begin{bmatrix} -1 & -1 \\ 1 & 1 \end{bmatrix}$ to $A^{-1}$ gives:

$A^{-1} + B = \begin{bmatrix} 2 & -1 \\ -3 & 2 \end{bmatrix} + \begin{bmatrix} -1 & -1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -2 \\ -2 & 3 \end{bmatrix}$

The given matrix equation is $(A^{-1} + B)\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix}$.

Substituting the matrix $A^{-1} + B$ yields:

$\begin{bmatrix} 1 & -2 \\ -2 & 3 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ -2 \end{bmatrix}$

This results in the system of linear equations:

$x - 2y = 0 \Rightarrow x = 2y$

$-2x + 3y = -2$

Substituting $x = 2y$ into the second equation gives:

$-2(2y) + 3y = -2$

$-4y + 3y = -2 \Rightarrow -y = -2 \Rightarrow y = 2$

Using $y = 2$, we get $x = 2(2) = 4$.

The value of $x + 3y$ is $4 + 3(2) = 10$.

Answer: $10$

</details>

---

### Q9. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If matrix $\begin{pmatrix} x & 1 & 2 \\ 2 & 4 & x \\ -3 & 3 & 2 \end{pmatrix}$ is non-invertible matrix and distinct values of $x$ are $a$ and $b$ then $9(a^2 + b^2) = \cdots\cdots\cdots$

**Options:**

- **(A)** $271$
- **(B)** $721$
- **(C)** $217$
- **(D)** $-278$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $217$**

**Detailed Solution:**

For a matrix to be non-invertible, its determinant must be zero.

$\begin{vmatrix} x & 1 & 2 \\ 2 & 4 & x \\ -3 & 3 & 2 \end{vmatrix} = 0$

Expanding along the first row:

$x(4 \times 2 - 3 \times x) - 1(2 \times 2 - (-3) \times x) + 2(2 \times 3 - (-3) \times 4) = 0$

$x(8 - 3x) - 1(4 + 3x) + 2(6 + 12) = 0$

$8x - 3x^2 - 4 - 3x + 36 = 0$

$-3x^2 + 5x + 32 = 0$

$3x^2 - 5x - 32 = 0$

Since $a$ and $b$ are the distinct roots of this quadratic equation, using the sum and product of roots:

$a + b = \dfrac{5}{3}$

$ab = -\dfrac{32}{3}$

We need to find the value of $9(a^2 + b^2)$:

$9(a^2 + b^2) = 9((a + b)^2 - 2ab)$

$9(a^2 + b^2) = 9\left(\left(\dfrac{5}{3}\right)^2 - 2\left(-\dfrac{32}{3}\right)\right)$

$9(a^2 + b^2) = 9\left(\dfrac{25}{9} + \dfrac{64}{3}\right)$

$9(a^2 + b^2) = 25 + 3 \times 64$

$9(a^2 + b^2) = 25 + 192 = 217$

Answer: $217$

</details>

---

### Q10. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 1 & 3 \\ 2 & 1 \end{bmatrix}$, then the determinant of $(A^2 - 2A)^{-1}$ is...

**Options:**

- **(A)** $\dfrac{1}{5}$
- **(B)** $25$
- **(C)** $\dfrac{1}{25}$
- **(D)** $-25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{25}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 1 & 3 \\ 2 & 1 \end{bmatrix}$

The characteristic equation of matrix $A$ is given by $\lambda^2 - (\text{Tr}(A))\lambda + |A| = 0$

Here, $\text{Tr}(A) = 1 + 1 = 2$ and $|A| = 1(1) - 3(2) = -5$

So, the characteristic equation is $\lambda^2 - 2\lambda - 5 = 0$

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation. Thus:

$A^2 - 2A - 5I = 0$

$A^2 - 2A = 5I$

Taking the determinant on both sides for a $2 \times 2$ matrix:

$|A^2 - 2A| = |5I| = 5^2 |I| = 25$

We need to find the determinant of $(A^2 - 2A)^{-1}$:

$|(A^2 - 2A)^{-1}| = \dfrac{1}{|A^2 - 2A|} = \dfrac{1}{25}$

Answer: $\dfrac{1}{25}$

</details>

---

### Q11. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1 \end{bmatrix}$ and $A^{-1} = xA + yI$, then the values of $x$ and $y$ are...

**Options:**

- **(A)** $x = \dfrac{1}{5}, y = \dfrac{-4}{5}$
- **(B)** $x = \dfrac{-1}{5}, y = \dfrac{4}{5}$
- **(C)** $x = \dfrac{1}{5}, y = \dfrac{4}{5}$
- **(D)** $x = 1, y = -4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x = \dfrac{1}{5}, y = \dfrac{-4}{5}$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\begin{vmatrix} 1-\lambda & 2 & 2 \\ 2 & 1-\lambda & 2 \\ 2 & 2 & 1-\lambda \end{vmatrix} = 0$

Expanding the determinant, we get:

$(1-\lambda)[(1-\lambda)^2 - 4] - 2[2(1-\lambda) - 4] + 2[4 - 2(1-\lambda)] = 0$

$(1-\lambda)(\lambda^2 - 2\lambda - 3) + 4\lambda + 4 + 4\lambda + 4 = 0$

$(1-\lambda)(\lambda - 3)(\lambda + 1) + 8(\lambda + 1) = 0$

$(\lambda + 1)[-\lambda^2 + 4\lambda - 3 + 8] = 0$

$-(\lambda + 1)(\lambda^2 - 4\lambda - 5) = 0$

$-(\lambda + 1)^2(\lambda - 5) = 0$

The minimal polynomial of the symmetric matrix $A$ is the product of distinct linear factors corresponding to its eigenvalues, which is $(\lambda + 1)(\lambda - 5) = \lambda^2 - 4\lambda - 5 = 0$.

By the Cayley-Hamilton theorem, $A$ satisfies its minimal polynomial:

$A^2 - 4A - 5I = 0$

Multiplying the entire equation by $A^{-1}$, we get:

$A - 4I - 5A^{-1} = 0$

$5A^{-1} = A - 4I$

$A^{-1} = \dfrac{1}{5}A - \dfrac{4}{5}I$

Comparing this with the given equation $A^{-1} = xA + yI$, we obtain:

$x = \dfrac{1}{5}, y = \dfrac{-4}{5}$

Answer: $x = \dfrac{1}{5}, y = \dfrac{-4}{5}$

</details>

---

### Q12. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the matrix $A = \begin{bmatrix} 3 & -5 \\ 4 & -7 \end{bmatrix}$ and $A^{-1} = \begin{bmatrix} 7 & -5 \\ 4 & a \end{bmatrix}$, then the value of $a$ is...

**Options:**

- **(A)** $-3$
- **(B)** $3$
- **(C)** $5$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-3$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 3 & -5 \\\\ 4 & -7 \end{bmatrix}$

The determinant of $A$ is $|A| = (3)(-7) - (-5)(4) = -21 + 20 = -1$

The inverse of a $2 \times 2$ matrix $\begin{bmatrix} p & q \\\\ r & s \end{bmatrix}$ is $\dfrac{1}{ps - qr} \begin{bmatrix} s & -q \\\\ -r & p \end{bmatrix}$

$A^{-1} = \dfrac{1}{-1} \begin{bmatrix} -7 & 5 \\\\ -4 & 3 \end{bmatrix} = \begin{bmatrix} 7 & -5 \\\\ 4 & -3 \end{bmatrix}$

Comparing this with the given $A^{-1} = \begin{bmatrix} 7 & -5 \\\\ 4 & a \end{bmatrix}$, we get $a = -3$

Answer: $-3$

</details>

---

### Q13. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\begin{bmatrix}\sin\alpha & -\cos\alpha\\\cos\alpha & \sin\alpha\end{bmatrix}$ and $S=\left\{\alpha:\alpha\in\left(\dfrac{\pi}{2},\dfrac{3\pi}{2}\right), A+A^{-1}=I\right\}$, then $\alpha=$ ...

**Options:**

- **(A)** $\dfrac{2\pi}{3}$
- **(B)** $\dfrac{3\pi}{4}$
- **(C)** $\dfrac{5\pi}{6}$
- **(D)** $\pi$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{5\pi}{6}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} \sin\alpha & -\cos\alpha \\ \cos\alpha & \sin\alpha \end{bmatrix}$

The determinant of $A$ is $|A| = \sin^2\alpha - (-\cos^2\alpha) = \sin^2\alpha + \cos^2\alpha = 1$.

The inverse of $A$ is given by:

$A^{-1} = \dfrac{1}{|A|} \text{adj}(A) = \begin{bmatrix} \sin\alpha & \cos\alpha \\ -\cos\alpha & \sin\alpha \end{bmatrix}$

We are given that $A + A^{-1} = I$. Substituting the matrices, we get:

$\begin{bmatrix} \sin\alpha & -\cos\alpha \\ \cos\alpha & \sin\alpha \end{bmatrix} + \begin{bmatrix} \sin\alpha & \cos\alpha \\ -\cos\alpha & \sin\alpha \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

$\begin{bmatrix} 2\sin\alpha & 0 \\ 0 & 2\sin\alpha \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

Equating the corresponding elements, we obtain:

$2\sin\alpha = 1 \Rightarrow \sin\alpha = \dfrac{1}{2}$

Since $\alpha \in \left( \dfrac{\pi}{2}, \dfrac{3\pi}{2} \right)$, the angle must lie in the second or third quadrant. The sine function is positive in the second quadrant, so:

$\alpha = \pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}$

Answer: $\dfrac{5\pi}{6}$

</details>

---

### Q14. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A = \begin{bmatrix} 1 & -5 \\ -2 & 4 \end{bmatrix}$, then $A^{-1} =$

**Options:**

- **(A)** $-\dfrac{1}{6}\begin{bmatrix} -4 & 5 \\ 2 & -1 \end{bmatrix}$
- **(B)** $\dfrac{1}{14}\begin{bmatrix} -1 & 5 \\ 2 & -4 \end{bmatrix}$
- **(C)** $\dfrac{1}{14}\begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$
- **(D)** $-\dfrac{1}{6}\begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{6}\begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 1 & -5 \\ -2 & 4 \end{bmatrix}$

The determinant of $A$ is $|A| = (1)(4) - (-5)(-2) = 4 - 10 = -6$

The adjoint of $A$ is obtained by interchanging the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(A) = \begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$

The inverse of the matrix is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$

$A^{-1} = -\dfrac{1}{6} \begin{bmatrix} 4 & 5 \\ 2 & 1 \end{bmatrix}$

</details>

---

### Q15. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} a & 1 \\ 1 & b \end{bmatrix}$, where $a$ and $b$ are the roots of the equation $x^2 - 4x + 2 = 0$. If $A + A^{-1} = kI_2$, then the value of $k$ is ____

**Options:**

- **(A)** $2$
- **(B)** $2\sqrt{2}$
- **(C)** $4$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4$**

**Detailed Solution:**

Given $A = \begin{bmatrix} a & 1 \\ 1 & b \end{bmatrix}$

Since $a$ and $b$ are roots of $x^2 - 4x + 2 = 0$, we have $a + b = 4$ and $ab = 2$.

The determinant of $A$ is $|A| = ab - 1 = 2 - 1 = 1$.

The inverse of $A$ is $A^{-1} = \dfrac{1}{|A|} \begin{bmatrix} b & -1 \\ -1 & a \end{bmatrix} = \begin{bmatrix} b & -1 \\ -1 & a \end{bmatrix}$.

Now, $A + A^{-1} = \begin{bmatrix} a & 1 \\ 1 & b \end{bmatrix} + \begin{bmatrix} b & -1 \\ -1 & a \end{bmatrix} = \begin{bmatrix} a+b & 0 \\ 0 & a+b \end{bmatrix}$.

Substituting $a + b = 4$, we get $A + A^{-1} = \begin{bmatrix} 4 & 0 \\ 0 & 4 \end{bmatrix} = 4I_2$.

Comparing with $A + A^{-1} = kI_2$, we get $k = 4$.

</details>

---

### Q16. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The inverse of the matrix $A = \begin{bmatrix} 2 & -1 & 4 \\ 4 & -3 & 1 \\ 1 & 2 & 1 \end{bmatrix}$ is $B = \dfrac{1}{37}\begin{bmatrix} -5 & 9 & 11 \\ -3 & -2 & 14 \\ 11 & -5 & k \end{bmatrix}$, then the value of $k$ is...

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $2$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-2$**

**Detailed Solution:**

Since $B$ is the inverse of $A$, we have $AB = I$, which implies $A(37B) = 37I$.

The element in the first row and third column of the matrix $37I$ is $0$.

Multiplying the first row of $A$ with the third column of $37B$, we get:

$2(11) + (-1)(14) + 4(k) = 0$

$22 - 14 + 4k = 0$

$8 + 4k = 0$

$k = -2$

Alternatively, multiplying the third row of $A$ with the third column of $37B$ gives the element in the third row and third column of $37I$, which is $37$:

$1(11) + 2(14) + 1(k) = 37$

$11 + 28 + k = 37$

$39 + k = 37$

$k = -2$

Answer: $-2$

</details>

---

### Q17. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The inverse of matrix $\begin{bmatrix} 1+pq & p & 0 \\ q & 1+pq & p \\ 0 & q & 1 \end{bmatrix}$ is ...

**Options:**

- **(A)** $\begin{bmatrix} 1+pq & p & 0 \\ q & 1+pq & p \\ 0 & q & 1 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 1 & p & p^2 \\ q & 1+pq & p+p^2q \\ q^2 & q+pq^2 & 1+pq+p^2q^2 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 1 & -p & p^2 \\ -q & 1+pq & -(p+p^2q) \\ q^2 & -(q+pq^2) & 1+pq+p^2q^2 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 1 & -p & p^2 \\ -q & 1+pq & p+p^2q \\ q^2 & q+pq^2 & 1+pq+p^2q^2 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\begin{bmatrix} 1 & -p & p^2 \\ -q & 1+pq & -(p+p^2q) \\ q^2 & -(q+pq^2) & 1+pq+p^2q^2 \end{bmatrix}$**

**Detailed Solution:**

Let the given matrix be $A = \begin{bmatrix} 1+pq & p & 0 \\ q & 1+pq & p \\ 0 & q & 1 \end{bmatrix}$.

The inverse of matrix $A$ is given by $A^{-1} = \dfrac{1}{|A|}\text{adj}(A)$.

First, evaluate the determinant of $A$:

$|A| = (1+pq)[(1+pq)(1) - (p)(q)] - p[q(1) - (p)(0)] + 0$

$|A| = (1+pq)[1 + pq - pq] - p[q]$

$|A| = (1+pq)(1) - pq = 1 + pq - pq = 1$

Since $|A| = 1$, the inverse matrix is $A^{-1} = \text{adj}(A)$.

To find the adjoint of $A$, we calculate the cofactors of each element:

$C_{11} = (1+pq)(1) - pq = 1$

$C_{12} = -(q(1) - 0) = -q$

$C_{13} = q(q) - 0 = q^2$

$C_{21} = -(p(1) - 0) = -p$

$C_{22} = (1+pq)(1) - 0 = 1+pq$

$C_{23} = -((1+pq)q - 0) = -(q + pq^2)$

$C_{31} = p(p) - 0 = p^2$

$C_{32} = -((1+pq)p - 0) = -(p + p^2q)$

$C_{33} = (1+pq)^2 - pq = 1 + 2pq + p^2q^2 - pq = 1 + pq + p^2q^2$

The adjoint matrix is the transpose of the cofactor matrix:

$\text{adj}(A) = \begin{bmatrix} C_{11} & C_{21} & C_{31} \\ C_{12} & C_{22} & C_{32} \\ C_{13} & C_{23} & C_{33} \end{bmatrix} = \begin{bmatrix} 1 & -p & p^2 \\ -q & 1+pq & -(p+p^2q) \\ q^2 & -(q+pq^2) & 1+pq+p^2q^2 \end{bmatrix}$

Therefore, $A^{-1} = \begin{bmatrix} 1 & -p & p^2 \\ -q & 1+pq & -(p+p^2q) \\ q^2 & -(q+pq^2) & 1+pq+p^2q^2 \end{bmatrix}$.

</details>

---

### Q18. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If matrix A and its inverse $A^{-1}$ are given by $A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & x & 1 \end{bmatrix}$ and $A^{-1} = \begin{bmatrix} \dfrac{1}{2} & -\dfrac{1}{2} & \dfrac{1}{2} \\ -4 & 3 & y \\ \dfrac{5}{2} & -\dfrac{3}{2} & \dfrac{1}{2} \end{bmatrix}$, then the polar co-ordinates of the points whose Cartesian co-ordinates are $(x, y)$ are $\ldots$

**Options:**

- **(A)** $\left(2, \dfrac{7\pi}{4}\right)$
- **(B)** $\left(\sqrt{2}, \dfrac{\pi}{4}\right)$
- **(C)** $\left(\sqrt{2}, \dfrac{7\pi}{4}\right)$
- **(D)** $\left(2, \dfrac{\pi}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left(\sqrt{2}, \dfrac{7\pi}{4}\right)$**

**Detailed Solution:**

Since $A A^{-1} = I$, the product of the first row of $A$ and the third column of $A^{-1}$ must be $0$.

$0 \times \dfrac{1}{2} + 1 \times y + 2 \times \dfrac{1}{2} = 0 \Rightarrow y + 1 = 0 \Rightarrow y = -1$

Similarly, the product of the third row of $A$ and the first column of $A^{-1}$ must be $0$.

$3 \times \dfrac{1}{2} + x \times (-4) + 1 \times \dfrac{5}{2} = 0 \Rightarrow 4 - 4x = 0 \Rightarrow x = 1$

The Cartesian coordinates are $(x, y) = (1, -1)$.

The polar coordinates $(r, \theta)$ are given by $r = \sqrt{x^2 + y^2}$ and $\tan \theta = \dfrac{y}{x}$.

$r = \sqrt{1^2 + (-1)^2} = \sqrt{2}$

Since the point $(1, -1)$ lies in the fourth quadrant, $\theta = 2\pi - \dfrac{\pi}{4} = \dfrac{7\pi}{4}$.

Thus, the polar coordinates are $\left(\sqrt{2}, \dfrac{7\pi}{4}\right)$.

</details>

---

### Q19. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 3 & -4 \\ 1 & -1 \end{bmatrix}$ and $B = \begin{bmatrix} 6 & -13 \\ 5 & -10 \end{bmatrix}$ be two matrices. If the variables $x$ and $y$ satisfy the matrix equation $((A^{-1})^2 + B)\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$, then the ordered pair $(x, y) = $

**Options:**

- **(A)** $(3, 5)$
- **(B)** $(10, 7)$
- **(C)** $(4, 6)$
- **(D)** $(5, 3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(5, 3)$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 3 & -4 \\ 1 & -1 \end{bmatrix}$

Determinant of $A$ is $|A| = (3)(-1) - (-4)(1) = 1$

The inverse of $A$ is $A^{-1} = \dfrac{1}{|A|} \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix}$

Now, $(A^{-1})^2 = \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} -1 & 4 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 1 - 4 & -4 + 12 \\ 1 - 3 & -4 + 9 \end{bmatrix} = \begin{bmatrix} -3 & 8 \\ -2 & 5 \end{bmatrix}$

Adding matrix $B$:

$(A^{-1})^2 + B = \begin{bmatrix} -3 & 8 \\ -2 & 5 \end{bmatrix} + \begin{bmatrix} 6 & -13 \\ 5 & -10 \end{bmatrix} = \begin{bmatrix} 3 & -5 \\ 3 & -5 \end{bmatrix}$

The given matrix equation is $((A^{-1})^2 + B)\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

$\begin{bmatrix} 3 & -5 \\ 3 & -5 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$

This gives the equation $3x - 5y = 0 \Rightarrow 3x = 5y$

Checking the given options, the ordered pair $(5, 3)$ satisfies this equation since $3(5) - 5(3) = 0$.

Answer: $(5, 3)$

</details>

---

### Q20. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 1 & -\tan\dfrac{\theta}{2} \\ \tan\dfrac{\theta}{2} & 1 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & \tan\dfrac{\theta}{2} \\ -\tan\dfrac{\theta}{2} & 1 \end{bmatrix}$ then $A^{-1}B$ is equal to

**Options:**

- **(A)** $\begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$
- **(B)** $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$
- **(C)** $\begin{bmatrix} \sin\theta & -\cos\theta \\ \cos\theta & \sin\theta \end{bmatrix}$
- **(D)** $\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$**

**Detailed Solution:**

Let $t = \tan\dfrac{\theta}{2}$.

The given matrices can be written as:
$A = \begin{bmatrix} 1 & -t \\ t & 1 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & t \\ -t & 1 \end{bmatrix}$

The determinant of $A$ is $|A| = 1(1) - (-t)(t) = 1 + t^2$.

The adjugate of $A$ is $\text{adj}(A) = \begin{bmatrix} 1 & t \\ -t & 1 \end{bmatrix}$.

Therefore, the inverse of $A$ is:
$A^{-1} = \dfrac{1}{|A|} \text{adj}(A) = \dfrac{1}{1+t^2} \begin{bmatrix} 1 & t \\ -t & 1 \end{bmatrix}$

Now, multiply $A^{-1}$ and $B$:
$A^{-1}B = \dfrac{1}{1+t^2} \begin{bmatrix} 1 & t \\ -t & 1 \end{bmatrix} \begin{bmatrix} 1 & t \\ -t & 1 \end{bmatrix}$

$A^{-1}B = \dfrac{1}{1+t^2} \begin{bmatrix} 1(1) + t(-t) & 1(t) + t(1) \\ -t(1) + 1(-t) & -t(t) + 1(1) \end{bmatrix}$

$A^{-1}B = \dfrac{1}{1+t^2} \begin{bmatrix} 1 - t^2 & 2t \\ -2t & 1 - t^2 \end{bmatrix}$

$A^{-1}B = \begin{bmatrix} \dfrac{1-t^2}{1+t^2} & \dfrac{2t}{1+t^2} \\ \dfrac{-2t}{1+t^2} & \dfrac{1-t^2}{1+t^2} \end{bmatrix}$

Using the half-angle trigonometric identities $\cos\theta = \dfrac{1 - \tan^2\dfrac{\theta}{2}}{1 + \tan^2\dfrac{\theta}{2}}$ and $\sin\theta = \dfrac{2\tan\dfrac{\theta}{2}}{1 + \tan^2\dfrac{\theta}{2}}$, we get:

$A^{-1}B = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$

Answer: $\begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$

</details>

---

### Q21. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A$ is a non-singular matrix and $A^2 - A + I = 0$, then $A^{-1} = \ldots$

**Options:**

- **(A)** $A$
- **(B)** $A - I$
- **(C)** $I - A$
- **(D)** $A + I$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $I - A$**

**Detailed Solution:**

Given $A^2 - A + I = 0$

Multiplying both sides by $A^{-1}$, we get

$A^{-1}(A^2 - A + I) = 0$

$A - I + A^{-1} = 0$

$A^{-1} = I - A$

Answer: $I - A$

</details>

---

### Q22. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Inverse of $\begin{bmatrix} 3 & -2 \\ 1 & 4 \end{bmatrix}$ is

**Options:**

- **(A)** $\begin{bmatrix} \dfrac{2}{7} & \dfrac{1}{7} \\ -\dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix}$
- **(B)** $\begin{bmatrix} \dfrac{3}{14} & -\dfrac{1}{7} \\ \dfrac{1}{14} & \dfrac{2}{7} \end{bmatrix}$
- **(C)** $\begin{bmatrix} \dfrac{2}{7} & -\dfrac{1}{7} \\ \dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix}$
- **(D)** $\begin{bmatrix} -\dfrac{3}{14} & \dfrac{1}{7} \\ \dfrac{1}{14} & \dfrac{2}{7} \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} \dfrac{2}{7} & \dfrac{1}{7} \\ -\dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix}$**

**Detailed Solution:**

Let $A = \begin{bmatrix} 3 & -2 \\ 1 & 4 \end{bmatrix}$

The determinant of $A$ is $|A| = (3)(4) - (-2)(1) = 12 + 2 = 14$

The adjugate of $A$ is $\text{adj}(A) = \begin{bmatrix} 4 & 2 \\ -1 & 3 \end{bmatrix}$

The inverse of $A$ is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$

$A^{-1} = \dfrac{1}{14} \begin{bmatrix} 4 & 2 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} \dfrac{4}{14} & \dfrac{2}{14} \\ -\dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix} = \begin{bmatrix} \dfrac{2}{7} & \dfrac{1}{7} \\ -\dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix}$

Answer: $\begin{bmatrix} \dfrac{2}{7} & \dfrac{1}{7} \\ -\dfrac{1}{14} & \dfrac{3}{14} \end{bmatrix}$

</details>

---

### Q23. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The element in the third row and the second column in the inverse matrix of a matrix $\begin{bmatrix} 1 & 3 & 3 \\ 3 & 1 & 3 \\ 3 & 3 & 4 \end{bmatrix}$ is

**Options:**

- **(A)** $\dfrac{3}{2}$
- **(B)** $\dfrac{2}{3}$
- **(C)** $\dfrac{-3}{2}$
- **(D)** $\dfrac{-2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{3}{2}$**

**Detailed Solution:**

Let $A = \begin{bmatrix} 1 & 3 & 3 \\ 3 & 1 & 3 \\ 3 & 3 & 4 \end{bmatrix}$.

The element in the third row and second column of $A^{-1}$ is given by $\dfrac{C_{23}}{|A|}$, where $C_{23}$ is the cofactor of the element $a_{23}$ in $A$.

First, we calculate the determinant of $A$:

$|A| = 1(1 \times 4 - 3 \times 3) - 3(3 \times 4 - 3 \times 3) + 3(3 \times 3 - 1 \times 3)$

$|A| = 1(-5) - 3(3) + 3(6) = -5 - 9 + 18 = 4$

Next, we find the cofactor $C_{23}$:

$C_{23} = (-1)^{2+3} \begin{vmatrix} 1 & 3 \\ 3 & 3 \end{vmatrix} = -(1 \times 3 - 3 \times 3) = -(3 - 9) = 6$

Therefore, the required element is $\dfrac{C_{23}}{|A|} = \dfrac{6}{4} = \dfrac{3}{2}$.

Answer: $\dfrac{3}{2}$

</details>

---

### Q24. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The element in 1st row and 2nd column of the inverse of the matrix $\begin{bmatrix} 1 & 3 & -2 \\ -3 & 0 & -5 \\ 2 & 5 & 0 \end{bmatrix}$ is ...

**Options:**

- **(A)** $-\dfrac{2}{5}$
- **(B)** $-\dfrac{10}{3}$
- **(C)** $-\dfrac{2}{25}$
- **(D)** $\dfrac{1}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-\dfrac{2}{5}$**

**Detailed Solution:**

Let $A = \begin{bmatrix} 1 & 3 & -2 \\ -3 & 0 & -5 \\ 2 & 5 & 0 \end{bmatrix}$

The determinant of $A$ is given by:

$|A| = 1(0 - (-25)) - 3(0 - (-10)) - 2(-15 - 0)$

$|A| = 25 - 30 + 30 = 25$

The inverse of matrix $A$ is $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$.

The element in the 1st row and 2nd column of $A^{-1}$ is $\dfrac{1}{|A|} C_{21}$, where $C_{21}$ is the cofactor of the element $a_{21}$ in $A$.

$C_{21} = (-1)^{2+1} \begin{vmatrix} 3 & -2 \\ 5 & 0 \end{vmatrix} = -(0 - (-10)) = -10$

Therefore, the required element is $\dfrac{-10}{25} = -\dfrac{2}{5}$.

</details>

---

### Q25. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 2 & 0 & -1 \\ 5 & 1 & 0 \\ 0 & 1 & 3 \end{bmatrix}_{3 \times 3}$, and $A^{-1} = \begin{bmatrix} \gamma & -1 & 1 \\ \alpha & 6 & -5 \\ \beta & -2 & 2 \end{bmatrix}_{3 \times 3}$, then $|\alpha \cdot \beta \cdot \gamma| = $ _____ (where $|\cdot|$ denotes the absolute value)

**Options:**

- **(A)** $125$
- **(B)** $220$
- **(C)** $225$
- **(D)** $-225$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $225$**

**Detailed Solution:**

The determinant of matrix $A$ is:

$|A| = 2(1 \times 3 - 0 \times 1) - 0 + (-1)(5 \times 1 - 1 \times 0) = 6 - 5 = 1$

Since $|A| = 1$, the inverse of $A$ is simply its adjugate matrix, $A^{-1} = \text{adj}(A)$.

The elements $\gamma, \alpha, \beta$ form the first column of $A^{-1}$, which corresponds to the cofactors $C_{11}, C_{12}, C_{13}$ of the first row of matrix $A$.

Calculating these cofactors:

$C_{11} = (1)(3) - (0)(1) = 3 \Rightarrow \gamma = 3$

$C_{12} = -((5)(3) - (0)(0)) = -15 \Rightarrow \alpha = -15$

$C_{13} = (5)(1) - (1)(0) = 5 \Rightarrow \beta = 5$

The product of these values is:

$\alpha \cdot \beta \cdot \gamma = (-15) \cdot 5 \cdot 3 = -225$

Taking the absolute value:

$|\alpha \cdot \beta \cdot \gamma| = |-225| = 225$

Answer: $225$

</details>

---

### Q26. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{bmatrix}$ then which of the following is true ?

**Options:**

- **(A)** $A^2 = A^{-1}$
- **(B)** $A = -(\text{adj} A)$
- **(C)** $A^{-1} = A$
- **(D)** $A^{-1} = -A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $A^{-1} = A$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{bmatrix}$

Let us calculate $A^2$:

$A^2 = A \cdot A = \begin{bmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{bmatrix}$

$A^2 = \begin{bmatrix} 0(0) + 0(0) + (-1)(-1) & 0(0) + 0(-1) + (-1)(0) & 0(-1) + 0(0) + (-1)(0) \\ 0(0) + (-1)(0) + 0(-1) & 0(0) + (-1)(-1) + 0(0) & 0(-1) + (-1)(0) + 0(0) \\ (-1)(0) + 0(0) + 0(-1) & (-1)(0) + 0(-1) + 0(0) & (-1)(-1) + 0(0) + 0(0) \end{bmatrix}$

$A^2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$

Since $A^2 = I$, multiplying both sides by $A^{-1}$ gives:

$A^2 \cdot A^{-1} = I \cdot A^{-1}$

$A = A^{-1}$

Answer: $A^{-1} = A$

</details>

---

### Q27. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \dfrac{1}{2}\begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & -1 \end{bmatrix}$ then $A^{-1} - A^2$ is not

**Options:**

- **(A)** a null-matrix
- **(B)** a unit matrix
- **(C)** a diagonal matrix
- **(D)** a scalar matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a unit matrix**

**Detailed Solution:**

Given $A = \dfrac{1}{2}\begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & -1 \end{bmatrix}$

Calculating $A^2$:

$A^2 = \dfrac{1}{4}\begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & -1 \end{bmatrix} \begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & -1 \end{bmatrix} = \dfrac{1}{4}\begin{bmatrix} 1-3 & \sqrt{3}+\sqrt{3} \\ -\sqrt{3}-\sqrt{3} & -3+1 \end{bmatrix} = \dfrac{1}{4}\begin{bmatrix} -2 & 2\sqrt{3} \\ -2\sqrt{3} & -2 \end{bmatrix} = \dfrac{1}{2}\begin{bmatrix} -1 & \sqrt{3} \\ -\sqrt{3} & -1 \end{bmatrix}$

Now, finding the determinant of $A$:

$|A| = \left(\dfrac{1}{2}\right)^2 ((-1)(-1) - (-\sqrt{3})(\sqrt{3})) = \dfrac{1}{4} (1 + 3) = 1$

The inverse of $A$ is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$:

$A^{-1} = \dfrac{1}{2}\begin{bmatrix} -1 & \sqrt{3} \\ -\sqrt{3} & -1 \end{bmatrix}$

Thus, $A^{-1} - A^2 = \dfrac{1}{2}\begin{bmatrix} -1 & \sqrt{3} \\ -\sqrt{3} & -1 \end{bmatrix} - \dfrac{1}{2}\begin{bmatrix} -1 & \sqrt{3} \\ -\sqrt{3} & -1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = O$

The result is a null matrix. A null matrix is also a diagonal matrix (all non-diagonal elements are zero) and a scalar matrix (all diagonal elements are equal). However, it is not a unit matrix since its diagonal elements are zero, not $1$.

Answer: a unit matrix

</details>

---

### Q28. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 2i & i^3 \\ i^2 & 1 \end{bmatrix}$, then $A^{-1}$ is equal to

**Options:**

- **(A)** $\begin{bmatrix} -i & 1 \\ -i & 2 \end{bmatrix}$
- **(B)** $\begin{bmatrix} i & 1 \\ i & -2 \end{bmatrix}$
- **(C)** $\begin{bmatrix} -i & -1 \\ i & -2 \end{bmatrix}$
- **(D)** $\begin{bmatrix} i & -1 \\ -i & 2 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} -i & 1 \\ -i & 2 \end{bmatrix}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 2i & i^3 \\ i^2 & 1 \end{bmatrix}$

Substituting $i^2 = -1$ and $i^3 = -i$, we get:

$A = \begin{bmatrix} 2i & -i \\ -1 & 1 \end{bmatrix}$

The determinant of $A$ is:

$|A| = (2i)(1) - (-i)(-1) = 2i - i = i$

The adjugate of $A$ is:

$\text{adj}(A) = \begin{bmatrix} 1 & i \\ 1 & 2i \end{bmatrix}$

The inverse of $A$ is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$

$A^{-1} = \dfrac{1}{i} \begin{bmatrix} 1 & i \\ 1 & 2i \end{bmatrix}$

Since $\dfrac{1}{i} = -i$, we have:

$A^{-1} = -i \begin{bmatrix} 1 & i \\ 1 & 2i \end{bmatrix} = \begin{bmatrix} -i & -i^2 \\ -i & -2i^2 \end{bmatrix}$

Substituting $i^2 = -1$:

$A^{-1} = \begin{bmatrix} -i & 1 \\ -i & 2 \end{bmatrix}$

Answer: $\begin{bmatrix} -i & 1 \\ -i & 2 \end{bmatrix}$

</details>

---

### Q29. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ is a matrix of order 2 and $I$ is the identity matrix of order 2 such that $\mathrm{A}^2-4 \mathrm{~A}+3 \mathrm{I}=0$ then $(\mathrm{A}+3 \mathrm{I})^{-1}=$

**Options:**

- **(A)** $\frac{\mathrm{A}}{24}-\frac{7}{24} \mathrm{I}$
- **(B)** $\frac{\mathrm{A}}{21}-\frac{7}{21} \mathrm{I}$
- **(C)** $\frac{7 \mathrm{I}}{24}-\frac{1}{24} \mathrm{~A}$
- **(D)** A-3 I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7 \mathrm{I}}{24}-\frac{1}{24} \mathrm{~A}$**

**Detailed Solution:**

Given $A^2 - 4A + 3I = 0$

Let $(A + 3I)^{-1} = xA + yI$

$(A + 3I)(xA + yI) = I$

$xA^2 + (3x + y)A + 3yI = I$

Substituting $A^2 = 4A - 3I$:

$x(4A - 3I) + (3x + y)A + 3yI = I$

$4xA - 3xI + 3xA + yA + 3yI = I$

$(7x + y)A + (3y - 3x)I = I$

Comparing the coefficients of $A$ and $I$ on both sides:

$7x + y = 0 \Rightarrow y = -7x$

$3y - 3x = 1$

Substituting $y = -7x$ in the second equation:

$3(-7x) - 3x = 1$

$-24x = 1 \Rightarrow x = -\dfrac{1}{24}$

$y = -7\left(-\dfrac{1}{24}\right) = \dfrac{7}{24}$

Therefore, $(A + 3I)^{-1} = -\dfrac{1}{24}A + \dfrac{7}{24}I = \dfrac{7I}{24} - \dfrac{1}{24}A$

Answer: $\frac{7 \mathrm{I}}{24}-\frac{1}{24} \mathrm{~A}$

</details>

---

### Q30. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Matrix $A$ is non-singular matrix and $(A-3 I)(A-5 I)=0$, then $\frac{15}{8} A^{-1}=$ _________

**Options:**

- **(A)** $\mathrm{I}-8 \mathrm{~A}$
- **(B)** $2 \mathrm{I}-\frac{1}{15} \mathrm{~A}$
- **(C)** $\mathrm{I}-\frac{1}{8} \mathrm{~A}$
- **(D)** $8 \mathrm{I}-15 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{I}-\frac{1}{8} \mathrm{~A}$**

**Detailed Solution:**

Given $(A-3I)(A-5I)=0$

$A^2 - 5A - 3A + 15I = 0$

$A^2 - 8A + 15I = 0$

Multiplying by $A^{-1}$ on both sides:

$A - 8I + 15A^{-1} = 0$

$15A^{-1} = 8I - A$

Dividing by $8$ on both sides:

$\dfrac{15}{8}A^{-1} = I - \dfrac{1}{8}A$

Answer: $\mathrm{I}-\frac{1}{8} \mathrm{~A}$

</details>

---

### Q31. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{lll}3 & -3 & 4 \\ 2 & -3 & 4 \\ 0 & -1 & 1\end{array}\right]_{3 \times 3}$, then $A^{-1}=$

**Options:**

- **(A)** $A$
- **(B)** $\mathrm{A}^2$
- **(C)** $\mathrm{A}^3$
- **(D)** $\mathrm{A}^4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A}^3$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\lambda^3 - S_1 \lambda^2 + S_2 \lambda - |A| = 0$

where $S_1$ is the trace of $A$, $S_2$ is the sum of the principal minors, and $|A|$ is the determinant of $A$.

$S_1 = 3 + (-3) + 1 = 1$

$S_2 = \begin{vmatrix}-3 & 4 \\ -1 & 1\end{vmatrix} + \begin{vmatrix}3 & 4 \\ 0 & 1\end{vmatrix} + \begin{vmatrix}3 & -3 \\ 2 & -3\end{vmatrix}$

$S_2 = (-3 + 4) + (3 - 0) + (-9 + 6) = 1 + 3 - 3 = 1$

$|A| = 3(-3 + 4) - (-3)(2 - 0) + 4(-2 - 0) = 3(1) + 3(2) - 8 = 1$

Substituting these values, the characteristic equation is:

$\lambda^3 - \lambda^2 + \lambda - 1 = 0$

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation:

$A^3 - A^2 + A - I = 0$

Multiplying both sides by $(A + I)$:

$(A + I)(A^3 - A^2 + A - I) = 0$

$A^4 - I = 0$

$A^4 = I$

Multiplying both sides by $A^{-1}$:

$A^3 = A^{-1}$

Answer: $\mathrm{A}^3$

</details>

---

### Q32. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ and $B$ are non-singular matrices of order 2 such that $(\mathrm{AB})^{-1}=\frac{1}{6}\left[\begin{array}{cc}-7 & -3 \\ 2 & 3\end{array}\right]$ and $\mathrm{A}^{-1}=\frac{1}{3}\left[\begin{array}{cc}4 & 3 \\ -1 & 0\end{array}\right]$ then $\mathrm{B}^{-1}=$

**Options:**

- **(A)** $\frac{1}{2}\left[\begin{array}{cc}2 & 3 \\ 1 & -1\end{array}\right]$
- **(B)** $\frac{1}{2}\left[\begin{array}{ll}3 & 1 \\ 2 & 4\end{array}\right]$
- **(C)** $\frac{1}{2}\left[\begin{array}{cc}-1 & 3 \\ 1 & 2\end{array}\right]$
- **(D)** $\frac{1}{6}\left[\begin{array}{ll}1 & 1 \\ 2 & 3\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}\left[\begin{array}{cc}-1 & 3 \\ 1 & 2\end{array}\right]$**

**Detailed Solution:**

We know that $(AB)^{-1} = B^{-1}A^{-1}$.

Given:
$(AB)^{-1} = \dfrac{1}{6}\left[\begin{array}{cc}-7 & -3 \\ 2 & 3\end{array}\right]$

$A^{-1} = \dfrac{1}{3}\left[\begin{array}{cc}4 & 3 \\ -1 & 0\end{array}\right]$

To find $B^{-1}$, we can post-multiply $(AB)^{-1}$ by $A$:
$B^{-1} = (AB)^{-1}A$

First, we find $A = (A^{-1})^{-1}$.
Let $M = \left[\begin{array}{cc}4 & 3 \\ -1 & 0\end{array}\right]$. Then $A^{-1} = \dfrac{1}{3}M$.
The determinant of $M$ is $|M| = (4)(0) - (3)(-1) = 3$.
The inverse of $M$ is $M^{-1} = \dfrac{1}{3}\left[\begin{array}{cc}0 & -3 \\ 1 & 4\end{array}\right]$.

Since $A^{-1} = \dfrac{1}{3}M$, we have:
$A = (A^{-1})^{-1} = \left(\dfrac{1}{3}M\right)^{-1} = 3M^{-1} = 3 \times \dfrac{1}{3}\left[\begin{array}{cc}0 & -3 \\ 1 & 4\end{array}\right] = \left[\begin{array}{cc}0 & -3 \\ 1 & 4\end{array}\right]$

Now, substitute $A$ into the equation for $B^{-1}$:
$B^{-1} = \dfrac{1}{6}\left[\begin{array}{cc}-7 & -3 \\ 2 & 3\end{array}\right] \left[\begin{array}{cc}0 & -3 \\ 1 & 4\end{array}\right]$

Multiplying the two matrices:
$B^{-1} = \dfrac{1}{6}\left[\begin{array}{cc}(-7)(0) + (-3)(1) & (-7)(-3) + (-3)(4) \\ (2)(0) + (3)(1) & (2)(-3) + (3)(4)\end{array}\right]$

$B^{-1} = \dfrac{1}{6}\left[\begin{array}{cc}-3 & 21 - 12 \\ 3 & -6 + 12\end{array}\right]$

$B^{-1} = \dfrac{1}{6}\left[\begin{array}{cc}-3 & 9 \\ 3 & 6\end{array}\right]$

Taking $\dfrac{3}{6}$ common from the matrix:
$B^{-1} = \dfrac{1}{2}\left[\begin{array}{cc}-1 & 3 \\ 1 & 2\end{array}\right]$

Answer: $\frac{1}{2}\left[\begin{array}{cc}-1 & 3 \\ 1 & 2\end{array}\right]$

</details>

---

### Q33. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If matrix $A=\frac{1}{11}\left[\begin{array}{rrr}-1 & 7 & -24 \\ 2 & a & 4 \\ 2 & -3 & 15\end{array}\right]$ and $A^{-1}=\left[\begin{array}{rrr}3 & 3 & 4 \\ 2 & -3 & 4 \\ b & -1 & c\end{array}\right]$, then the values of $a, b, c$ respectively are ......

**Options:**

- **(A)** $3,1,0$
- **(B)** $\frac{-6}{11}, 0, \frac{1}{11}$
- **(C)** $-3,0,1$
- **(D)** $\frac{-3}{11}, 0, \frac{1}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-3,0,1$**

**Detailed Solution:**

We know that $A A^{-1} = I$.

$\dfrac{1}{11} \left[\begin{array}{rrr}-1 & 7 & -24 \\ 2 & a & 4 \\ 2 & -3 & 15\end{array}\right] \left[\begin{array}{rrr}3 & 3 & 4 \\ 2 & -3 & 4 \\ b & -1 & c\end{array}\right] = \left[\begin{array}{rrr}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$

$\left[\begin{array}{rrr}-1 & 7 & -24 \\ 2 & a & 4 \\ 2 & -3 & 15\end{array}\right] \left[\begin{array}{rrr}3 & 3 & 4 \\ 2 & -3 & 4 \\ b & -1 & c\end{array}\right] = \left[\begin{array}{rrr}11 & 0 & 0 \\ 0 & 11 & 0 \\ 0 & 0 & 11\end{array}\right]$

Equating the element in the first row and first column:
$(-1)(3) + (7)(2) + (-24)(b) = 11$
$-3 + 14 - 24b = 11$
$11 - 24b = 11 \Rightarrow b = 0$

Equating the element in the first row and third column:
$(-1)(4) + (7)(4) + (-24)(c) = 0$
$-4 + 28 - 24c = 0$
$24 - 24c = 0 \Rightarrow c = 1$

Equating the element in the second row and first column:
$(2)(3) + (a)(2) + (4)(b) = 0$
$6 + 2a + 4(0) = 0$
$2a = -6 \Rightarrow a = -3$

Therefore, the values of $a, b, c$ are $-3, 0, 1$ respectively.

Answer: $-3,0,1$

</details>

---

### Q34. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}1 & \cot \frac{\theta}{2} \\ -\cot \frac{\theta}{2} & 1\end{array}\right]$ then $A^{-1}=$

**Options:**

- **(A)** $\operatorname{cosec}^2 \frac{\theta}{2} \quad A^T$
- **(B)** $\frac{-\sin ^2 \theta}{2} \quad A^T$
- **(C)** $\left(\frac{1+\cos \theta}{2}\right) \quad \mathrm{A}^{\mathrm{T}}$
- **(D)** $\left(\frac{1-\cos \theta}{2}\right) \quad A^T$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{1-\cos \theta}{2}\right) \quad A^T$**

**Detailed Solution:**

Given $A = \left[\begin{array}{cc}1 & \cot \dfrac{\theta}{2} \\ -\cot \dfrac{\theta}{2} & 1\end{array}\right]$

The determinant of $A$ is:

$|A| = (1)(1) - \left(\cot \dfrac{\theta}{2}\right)\left(-\cot \dfrac{\theta}{2}\right) = 1 + \cot^2 \dfrac{\theta}{2} = \operatorname{cosec}^2 \dfrac{\theta}{2}$

The adjoint of $A$ is obtained by interchanging the diagonal elements and changing the signs of the off-diagonal elements:

$\operatorname{adj}(A) = \left[\begin{array}{cc}1 & -\cot \dfrac{\theta}{2} \\ \cot \dfrac{\theta}{2} & 1\end{array}\right]$

The transpose of $A$ is:

$A^T = \left[\begin{array}{cc}1 & -\cot \dfrac{\theta}{2} \\ \cot \dfrac{\theta}{2} & 1\end{array}\right]$

Thus, $\operatorname{adj}(A) = A^T$.

The inverse of $A$ is given by:

$A^{-1} = \dfrac{1}{|A|} \operatorname{adj}(A)$

$A^{-1} = \dfrac{1}{\operatorname{cosec}^2 \dfrac{\theta}{2}} A^T$

$A^{-1} = \sin^2 \dfrac{\theta}{2} A^T$

Using the half-angle formula $\sin^2 \dfrac{\theta}{2} = \dfrac{1 - \cos \theta}{2}$, we get:

$A^{-1} = \left(\dfrac{1 - \cos \theta}{2}\right) A^T$

Answer: $\left(\frac{1-\cos \theta}{2}\right) \quad A^T$

</details>

---

### Q35. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{cc}1 & \tan x \\ -\tan x & 1\end{array}\right]$, then $\mathrm{A}^{\mathrm{T}} \mathrm{A}^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}\cos 2 x & -\sin 2 x \\ -\sin 2 x & \cos 2 x\end{array}\right]$
- **(B)** $\left[\begin{array}{lr}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}-\cos 2 x & \sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}-\cos 2 x & \sin 2 x \\ -\sin 2 x & \cos 2 x\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{lr}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$**

**Detailed Solution:**

Given $A = \left[\begin{array}{cc}1 & \tan x \\ -\tan x & 1\end{array}\right]$

The transpose of $A$ is:
$A^T = \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right]$

The determinant of $A$ is:
$|A| = (1)(1) - (\tan x)(-\tan x) = 1 + \tan^2 x = \sec^2 x$

The inverse of $A$ is:
$A^{-1} = \dfrac{1}{|A|} \text{adj}(A) = \dfrac{1}{\sec^2 x} \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right] = \cos^2 x \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right]$

Now, multiplying $A^T$ and $A^{-1}$:
$A^T A^{-1} = \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right] \left( \cos^2 x \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right] \right)$

$A^T A^{-1} = \cos^2 x \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right] \left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right]$

$A^T A^{-1} = \cos^2 x \left[\begin{array}{cc}1 - \tan^2 x & -2\tan x \\ 2\tan x & 1 - \tan^2 x\end{array}\right]$

Multiplying $\cos^2 x$ inside the matrix:
$A^T A^{-1} = \left[\begin{array}{cc}\cos^2 x (1 - \tan^2 x) & \cos^2 x (-2\tan x) \\ \cos^2 x (2\tan x) & \cos^2 x (1 - \tan^2 x)\end{array}\right]$

Using $\tan x = \dfrac{\sin x}{\cos x}$:
$A^T A^{-1} = \left[\begin{array}{cc}\cos^2 x - \sin^2 x & -2\sin x \cos x \\ 2\sin x \cos x & \cos^2 x - \sin^2 x\end{array}\right]$

Using the double angle formulas $\cos 2x = \cos^2 x - \sin^2 x$ and $\sin 2x = 2\sin x \cos x$:
$A^T A^{-1} = \left[\begin{array}{cc}\cos 2x & -\sin 2x \\ \sin 2x & \cos 2x\end{array}\right]$

Answer: $\left[\begin{array}{lr}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$

</details>

---

### Q36. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{rr}1 & 2 \\ -1 & 4\end{array}\right]$ and $\mathrm{A}^{-1}=\alpha \mathrm{I}+\beta \mathrm{A}$
$\alpha, \beta \in \mathrm{R}$ where I is the identity matrix of order 2 , then $4(\alpha+\beta)=$

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{10}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8}{3}$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$

$\lambda^2 - (\text{Tr}(A))\lambda + |A| = 0$

Here, $\text{Tr}(A) = 1 + 4 = 5$ and $|A| = (1)(4) - (2)(-1) = 6$

$\lambda^2 - 5\lambda + 6 = 0$

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation:

$A^2 - 5A + 6I = 0$

Multiplying both sides by $A^{-1}$:

$A - 5I + 6A^{-1} = 0$

$6A^{-1} = 5I - A$

$A^{-1} = \dfrac{5}{6}I - \dfrac{1}{6}A$

Comparing this with the given equation $A^{-1} = \alpha I + \beta A$, we get:

$\alpha = \dfrac{5}{6}$ and $\beta = -\dfrac{1}{6}$

$\alpha + \beta = \dfrac{5}{6} - \dfrac{1}{6} = \dfrac{4}{6} = \dfrac{2}{3}$

$4(\alpha + \beta) = 4 \left(\dfrac{2}{3}\right) = \dfrac{8}{3}$

Answer: $\frac{8}{3}$

</details>

---

### Q37. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{A}=\left[\begin{array}{cc}1 & 2 \\ -1 & 4\end{array}\right]$ and $\mathrm{A}^{-1}=\alpha \mathrm{I}+\beta \mathrm{A}, \alpha, \beta \in \mathbb{R}$, I is the identity matrix of order 2 , then $4(\alpha-\beta)$ is

**Options:**

- **(A)** $\frac{8}{3}$
- **(B)** 4
- **(C)** 2
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\lambda^2 - \text{Tr}(A)\lambda + |A| = 0$

The trace of $A$ is $1 + 4 = 5$ and the determinant is $|A| = (1)(4) - (2)(-1) = 6$.

$\lambda^2 - 5\lambda + 6 = 0$

By Cayley-Hamilton theorem, matrix $A$ satisfies its own characteristic equation:

$A^2 - 5A + 6I = 0$

Multiplying by $A^{-1}$:

$A - 5I + 6A^{-1} = 0$

$6A^{-1} = 5I - A$

$A^{-1} = \dfrac{5}{6}I - \dfrac{1}{6}A$

Comparing with $A^{-1} = \alpha I + \beta A$:

$\alpha = \dfrac{5}{6}, \beta = -\dfrac{1}{6}$

The value of $4(\alpha - \beta)$ is:

$4(\alpha - \beta) = 4\left(\dfrac{5}{6} - \left(-\dfrac{1}{6}\right)\right) = 4\left(\dfrac{6}{6}\right) = 4$

Answer: 4

</details>

---

### Q38. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}\left[\begin{array}{ll}2 & 1 \\ 7 & 4\end{array}\right]$ then $\left(\mathrm{A}^2-5 \mathrm{~A}\right)^{-1}$ is

**Options:**

- **(A)** $\left(-\frac{1}{4}\right)\left[\begin{array}{cc}-3 & 1 \\ 7 & -1\end{array}\right]$
- **(B)** $\left(\frac{1}{4}\right)\left[\begin{array}{cc}-3 & 1 \\ 7 & -1\end{array}\right]$
- **(C)** $\left(\frac{1}{4}\right)\left[\begin{array}{ll}3 & 1 \\ 7 & 1\end{array}\right]$
- **(D)** $\left(\frac{1}{-4}\right)\left[\begin{array}{ll}3 & -1 \\ 7 & -1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{1}{4}\right)\left[\begin{array}{cc}-3 & 1 \\ 7 & -1\end{array}\right]$**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\lambda^2 - \text{Tr}(A)\lambda + |A| = 0$

Here, $\text{Tr}(A) = 2 + 4 = 6$ and $|A| = (2)(4) - (1)(7) = 1$.

So, the characteristic equation is $\lambda^2 - 6\lambda + 1 = 0$.

By the Cayley-Hamilton theorem, every square matrix satisfies its own characteristic equation:

$A^2 - 6A + I = 0$

We can rewrite this to find $A^2 - 5A$:

$A^2 - 5A = A - I$

Now, we calculate $A - I$:

$A - I = \begin{bmatrix} 2 & 1 \\ 7 & 4 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 7 & 3 \end{bmatrix}$

Let $B = A^2 - 5A = \begin{bmatrix} 1 & 1 \\ 7 & 3 \end{bmatrix}$. We need to find $B^{-1}$.

The determinant of $B$ is $|B| = (1)(3) - (1)(7) = -4$.

The adjugate of $B$ is obtained by swapping the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(B) = \begin{bmatrix} 3 & -1 \\ -7 & 1 \end{bmatrix}$

The inverse of $B$ is given by:

$B^{-1} = \dfrac{1}{|B|} \text{adj}(B) = \dfrac{1}{-4} \begin{bmatrix} 3 & -1 \\ -7 & 1 \end{bmatrix}$

Multiplying the scalar by $-1$ inside the matrix, we get:

$B^{-1} = \dfrac{1}{4} \begin{bmatrix} -3 & 1 \\ 7 & -1 \end{bmatrix}$

Answer: $\left(\frac{1}{4}\right)\left[\begin{array}{cc}-3 & 1 \\ 7 & -1\end{array}\right]$

</details>

---

### Q39. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Inverse of the matrix $\left[\begin{array}{cc}0.8 & -0.6 \\ 0.6 & 0.8\end{array}\right]$ is

**Options:**

- **(A)** $\left[\begin{array}{cc}0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}-0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}-0.8 & -0.6 \\ 0.6 & 0.8\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}8 & -6 \\ 6 & 8\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right]$**

**Detailed Solution:**

Let $A = \left[\begin{array}{cc}0.8 & -0.6 \\ 0.6 & 0.8\end{array}\right]$

The determinant of $A$ is $|A| = (0.8)(0.8) - (-0.6)(0.6) = 0.64 + 0.36 = 1$

The inverse of a $2 \times 2$ matrix $\left[\begin{array}{cc}a & b \\ c & d\end{array}\right]$ is $\dfrac{1}{ad-bc} \left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right]$

$A^{-1} = \dfrac{1}{1} \left[\begin{array}{cc}0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right] = \left[\begin{array}{cc}0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right]$

Answer: $\left[\begin{array}{cc}0.8 & 0.6 \\ -0.6 & 0.8\end{array}\right]$

</details>

---

### Q40. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{lll}1 & 1 & 1 \\ 1 & \mathrm{a} & 3 \\ 3 & 2 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}-2 & 0 & \mathrm{~b} \\ 7 & -1 & -2 \\ \mathrm{c} & 1 & 1\end{array}\right]$ and if matrix $B$ is the inverse of matrix $A$, then value of $4 a+2 b-c$ is

**Options:**

- **(A)** 6
- **(B)** 14
- **(C)** -14
- **(D)** -6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 14**

**Detailed Solution:**

Since $B$ is the inverse of $A$, we must have $AB = I$.

$\begin{bmatrix} 1 & 1 & 1 \\ 1 & a & 3 \\ 3 & 2 & 2 \end{bmatrix} \begin{bmatrix} -2 & 0 & b \\ 7 & -1 & -2 \\ c & 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

Equating the corresponding elements of the product to the identity matrix:

For the $(1,1)$ element:
$1(-2) + 1(7) + 1(c) = 1$
$5 + c = 1 \Rightarrow c = -4$

For the $(1,3)$ element:
$1(b) + 1(-2) + 1(1) = 0$
$b - 1 = 0 \Rightarrow b = 1$

For the $(2,2)$ element:
$1(0) + a(-1) + 3(1) = 1$
$-a + 3 = 1 \Rightarrow a = 2$

Now, substituting the values of $a$, $b$, and $c$ into the given expression:
$4a + 2b - c = 4(2) + 2(1) - (-4)$
$= 8 + 2 + 4 = 14$

Answer: 14

</details>

---

### Q41. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}=\left[\begin{array}{cc}1 & 2 \\ -5 & 1\end{array}\right]$ and $\mathrm{A}^{-1}=x \mathrm{~A}+y \mathrm{I}_2$, (where $\mathrm{I}_2$ is unit matrix of order 2), then

**Options:**

- **(A)** $x=\dfrac{-1}{11}, y=\dfrac{2}{11}$.
- **(B)** $x=\dfrac{1}{11}, y=\dfrac{-2}{11}$
- **(C)** $x=\dfrac{-1}{11}, y=\dfrac{-2}{11}$
- **(D)** $x=\dfrac{1}{11}, y=\dfrac{2}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $x=\dfrac{-1}{11}, y=\dfrac{2}{11}$.**

**Detailed Solution:**

The characteristic equation of matrix $A$ is given by $|A - \lambda I| = 0$.

$\begin{vmatrix} 1 - \lambda & 2 \\ -5 & 1 - \lambda \end{vmatrix} = 0$

$(1 - \lambda)^2 + 10 = 0$

$\lambda^2 - 2\lambda + 11 = 0$

By Cayley-Hamilton theorem, matrix $A$ satisfies its characteristic equation:

$A^2 - 2A + 11I_2 = 0$

Multiplying by $A^{-1}$ on both sides:

$A - 2I_2 + 11A^{-1} = 0$

$11A^{-1} = -A + 2I_2$

$A^{-1} = \dfrac{-1}{11}A + \dfrac{2}{11}I_2$

Comparing with $A^{-1} = xA + yI_2$, we get $x = \dfrac{-1}{11}$ and $y = \dfrac{2}{11}$.

Answer: $x=\dfrac{-1}{11}, y=\dfrac{2}{11}$.

</details>

---

### Q42. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\left[\begin{array}{cc}2 & -2 \\ 4 & 3\end{array}\right]$, then $\mathrm{A}^{-1}=$

**Options:**

- **(A)** $\quad-\dfrac{1}{2}\left[\begin{array}{cc}3 & 2 \\ -4 & 2\end{array}\right]$
- **(B)** $\dfrac{1}{14}\left[\begin{array}{cc}3 & 2 \\ -4 & 2\end{array}\right]$
- **(C)** $\dfrac{1}{14}\left[\begin{array}{cc}-3 & -2 \\ 4 & -2\end{array}\right]$
- **(D)** $\quad-\dfrac{1}{14}\left[\begin{array}{ll}3 & -2 \\ 4 & -2\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{14}\left[\begin{array}{cc}3 & 2 \\ -4 & 2\end{array}\right]$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 2 & -2 \\ 4 & 3 \end{bmatrix}$

The determinant of $A$ is $|A| = (2)(3) - (-2)(4) = 6 + 8 = 14$

The adjugate of $A$ is obtained by swapping the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(A) = \begin{bmatrix} 3 & 2 \\ -4 & 2 \end{bmatrix}$

The inverse of the matrix is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$

$A^{-1} = \dfrac{1}{14} \begin{bmatrix} 3 & 2 \\ -4 & 2 \end{bmatrix}$

Answer: $\dfrac{1}{14}\left[\begin{array}{cc}3 & 2 \\ -4 & 2\end{array}\right]$

</details>

---

### Q43. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}3 & -1 \\ -4 & 2\end{array}\right]$, then $A^{-1}$ is

**Options:**

- **(A)** $\left[\begin{array}{cc}1 & -\dfrac{1}{2} \\ 2 & \dfrac{3}{2}\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}1 & \dfrac{1}{2} \\ -2 & \dfrac{3}{2}\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}1 & -\dfrac{1}{2} \\ -2 & \dfrac{3}{2}\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}1 & \dfrac{1}{2} \\ 2 & \dfrac{3}{2}\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{ll}1 & \dfrac{1}{2} \\ 2 & \dfrac{3}{2}\end{array}\right]$**

**Detailed Solution:**

Given $A = \left[\begin{array}{cc}3 & -1 \\ -4 & 2\end{array}\right]$

The determinant of $A$ is $|A| = (3)(2) - (-1)(-4) = 6 - 4 = 2$

The adjugate of $A$ is $\text{adj}(A) = \left[\begin{array}{cc}2 & 1 \\ 4 & 3\end{array}\right]$

The inverse of $A$ is given by $A^{-1} = \dfrac{1}{|A|} \text{adj}(A)$

$A^{-1} = \dfrac{1}{2} \left[\begin{array}{cc}2 & 1 \\ 4 & 3\end{array}\right] = \left[\begin{array}{cc}1 & \dfrac{1}{2} \\ 2 & \dfrac{3}{2}\end{array}\right]$

Answer: $\left[\begin{array}{ll}1 & \dfrac{1}{2} \\ 2 & \dfrac{3}{2}\end{array}\right]$

</details>

---

### Q44. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}1 & -1 \\ 2 & -1\end{array}\right], B=\left[\begin{array}{cc}1 & 1 \\ 4 & -1\end{array}\right]$, then $(A+B)^{-1}$ is

**Options:**

- **(A)** $\left[\begin{array}{cc}\frac{-1}{2} & 0 \\ \frac{-3}{2} & \frac{1}{2}\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}\frac{1}{2} & 0 \\ \frac{3}{2} & \frac{-1}{2}\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}\frac{1}{2} & 0 \\ \frac{-3}{2} & \frac{1}{2}\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}\frac{1}{2} & 0 \\ \frac{3}{2} & \frac{1}{2}\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{cc}\frac{1}{2} & 0 \\ \frac{3}{2} & \frac{-1}{2}\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} A+B & =\left[\begin{array}{cc}1 & -1 \\ 2 & -1\end{array}\right]+\left[\begin{array}{cc}1 & 1 \\ 4 & -1\end{array}\right]=\left[\begin{array}{cc}2 & 0 \\ 6 & -2\end{array}\right] \\ \therefore \quad|A+B| & =\left|\begin{array}{cc}2 & 0 \\ 6 & -2\end{array}\right|=-4 \neq 0 \\ \text { If } A & =\left[\begin{array}{ll}a & b \\ c & d\end{array}\right] \text { and ad }-\mathrm{bc} \neq 0, \\ \text { then } A^{-1} & =\frac{1}{(a d-b c)}\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right] \\ (A+B)^{-1} & =\frac{1}{-4}\left[\begin{array}{cc}-2 & 0 \\ -6 & 2\end{array}\right] \\ \therefore \quad & =\left[\begin{array}{cc}\frac{1}{2} & 0 \\ \frac{3}{2} & -\frac{1}{2}\end{array}\right]\end{aligned}$

</details>

---

### Q45. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}1 & \tan x \\ -\tan x & 1\end{array}\right]$, then $A^T \cdot A^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{ll}-\cos 2 x & \sin 2 x \\ -\sin 2 x & \cos 2 x\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}\cos 2 x & \sin 2 x \\ -\sin 2 x & \cos 2 x\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}\cos 2 x & -\sin 2 x \\ -\sin 2 x & \cos 2 x\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{cc}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \begin{aligned}|A| & =\left|\begin{array}{cc}1 & \tan x \\ -\tan x & 1\end{array}\right| \\ & =1+\tan ^2 x \neq 0\end{aligned} \\ & \text { If } A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right] \text { and ad }-b c \neq 0, \\ & \text { then } A^{-1}=\frac{1}{(a d-b c)}\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right]\end{aligned}$
$\begin{aligned} & \therefore \quad \mathrm{A}^{-1}=\frac{1}{1+\tan ^2 x}\left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right] \\ & \therefore \quad \mathrm{A}^{\mathrm{T}} \mathrm{A}^{-1}=\left[\begin{array}{cc}1 & -\tan x \\ \tan x & 1\end{array}\right]\left[\begin{array}{cc}\frac{1}{1+\tan ^2 x} & \frac{-\tan x}{1+\tan ^2 x} \\ \frac{\tan x}{1+\tan ^2 x} & \frac{1}{1+\tan ^2 x}\end{array}\right]\end{aligned}$
$\begin{aligned} & =\left[\begin{array}{ll}\frac{1-\tan ^2 x}{1+\tan ^2 x} & \frac{-2 \tan x}{1+\tan ^2 x} \\ \frac{2 \tan x}{1+\tan ^2 x} & \frac{1-\tan ^2 x}{1+\tan ^2 x}\end{array}\right] \\ & =\left[\begin{array}{ll}\cos 2 x & -\sin 2 x \\ \sin 2 x & \cos 2 x\end{array}\right]\end{aligned}$

</details>

---

### Q46. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the matrix $\mathrm{A}=\left[\begin{array}{cc}1 & 2 \\ -5 & 1\end{array}\right]$ and $\mathrm{A}^{-1}=x \mathrm{~A}+y \mathrm{I}$, when $I$ is a unit matrix of order 2 , then the value of $2 x+3 y$ is

**Options:**

- **(A)** $\frac{8}{11}$
- **(B)** $\frac{4}{11}$
- **(C)** $\frac{-8}{11}$
- **(D)** $\frac{-4}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{11}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}=\left[\begin{array}{cc}1 & 2 \\ -5 & 1\end{array}\right] \\ \therefore \quad & \mathrm{A} \mid=11 \\ & \mathrm{~A}^{-1}=\frac{1}{|\mathrm{~A}|}\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right]=\frac{1}{11}\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right] \\ & \mathrm{A}^{-1}=x \mathrm{~A}+y \mathrm{I}, \text { we get } \\ & {\left[\begin{array}{cc}\frac{1}{11} & \frac{-2}{11} \\ \frac{5}{11} & \frac{1}{11}\end{array}\right]=\left[\begin{array}{cc}x & 2 x \\ -5 x & x\end{array}\right]+\left[\begin{array}{ll}y & 0 \\ 0 & y\end{array}\right] }\end{aligned}$
$\begin{array}{ll}\therefore & {\left[\begin{array}{cc}\frac{1}{11} & \frac{-2}{11} \\ \frac{5}{11} & \frac{1}{11}\end{array}\right]=\left[\begin{array}{cc}x+y & 2 x \\ -5 x & x+y\end{array}\right]} \\ \Rightarrow & x=\frac{-1}{11} \text { and } y=\frac{2}{11} \\ \therefore & 2 x+3 y=2\left(\frac{-1}{11}\right)+3\left(\frac{2}{11}\right)=\frac{4}{11}\end{array}$

</details>

---

### Q47. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\left[\begin{array}{ll}\mathrm{i} & 1 \\ 1 & 0\end{array}\right]$ where $\mathrm{i}=\sqrt{-1}$ and $\mathrm{B}=\mathrm{A}^{2029}$, then $\mathrm{B}^{-1}=$

**Options:**

- **(A)** $-\mathrm{A}$
- **(B)** $\operatorname{adj} \mathrm{A}$
- **(C)** $-I$
- **(D)** $-\operatorname{adj} \mathrm{A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\operatorname{adj} \mathrm{A}$**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{ll}i & 1 \\ 1 & 0\end{array}\right] \\ & \therefore \quad A^2=\left[\begin{array}{ll}i & 1 \\ 1 & 0\end{array}\right] \times\left[\begin{array}{ll}i & 1 \\ 1 & 0\end{array}\right]=\left[\begin{array}{ll}0 & i \\ i & 1\end{array}\right] \\ & \therefore \quad A^3=\left[\begin{array}{ll}0 & i \\ i & 1\end{array}\right]\left[\begin{array}{ll}i & 1 \\ 1 & 0\end{array}\right]=\left[\begin{array}{ll}i & 0 \\ 0 & i\end{array}\right] \\ & \therefore \quad \mathrm{A}^6=\mathrm{A}^3 \times \mathrm{A}^3 \\ & =\left[\begin{array}{ll}\mathrm{i} & 0 \\ 0 & \mathrm{i}\end{array}\right] \times\left[\begin{array}{ll}\mathrm{i} & 0 \\ 0 & \mathrm{i}\end{array}\right] \\ & =\left[\begin{array}{cc}-1 & 0 \\ 0 & -1\end{array}\right]=(-1) I_2 \\ & \text { Now, } B=A^{2029}=A^{(6 \times 338+1)} \\ & \therefore \quad \mathrm{B}=\left(\mathrm{A}^6\right)^{338} \times \mathrm{A} \\ & =\left((-1) \mathrm{I}_2\right)^{338} \times \mathrm{A} \\ & =\mathrm{I}_2 \times \mathrm{A} \\ & \therefore \quad \mathrm{B}=\mathrm{A} \\ & \text { Now, }|A|=-1 \\ & \therefore \quad B^{-1}=A^{-1}=\frac{1}{|A|} \operatorname{adj} A \\ & \therefore \quad \mathrm{B}^{-1}=-\operatorname{adj} \mathrm{A} \\ & \end{aligned}$

</details>

---

### Q48. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}2 & -1 \\ -1 & 3\end{array}\right]$, then the inverse of $\left(2 A^2+5 A\right)$ is

**Options:**

- **(A)** $\frac{1}{95}\left[\begin{array}{ll}7 & 3 \\ 3 & 4\end{array}\right]$
- **(B)** $\frac{1}{95}\left[\begin{array}{ll}-7 & 3 \\ 3 & -4\end{array}\right]$
- **(C)** $\frac{1}{95}\left[\begin{array}{ll}-7 & -3 \\ 3 & 4\end{array}\right]$
- **(D)** $\frac{1}{95}\left[\begin{array}{ll}4 & 3 \\ 3 & 7\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{95}\left[\begin{array}{ll}7 & 3 \\ 3 & 4\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} A & =\left[\begin{array}{cc}2 & -1 \\ -1 & 3\end{array}\right] \\ & A^2=\left[\begin{array}{cc}2 & -1 \\ -1 & 3\end{array}\right]\left[\begin{array}{cc}2 & -1 \\ -1 & 3\end{array}\right] \\ \therefore \quad A^2 & =\left[\begin{array}{cc}5 & -5 \\ -5 & 10\end{array}\right] \\ \text { Now, } 2 A^2+5 A & =2\left[\begin{array}{cc}5 & -5 \\ -5 & 10\end{array}\right]+5\left[\begin{array}{cc}2 & -1 \\ -1 & 3\end{array}\right] \\ & =\left[\begin{array}{cc}20 & -15 \\ -15 & 35\end{array}\right] \\ \text { If } A & =\left[\begin{array}{ll}a & b \\ c & d\end{array}\right], \operatorname{then~} A^{-1}=\frac{1}{a d-b c}\left[\begin{array}{cc}d & -b \\ -c & a\end{array}\right] \\ \therefore \quad\left(2 A^2+5 A\right)^{-1} & =\frac{1}{475}\left[\begin{array}{cc}35 & 15 \\ 15 & 20\end{array}\right] \\ & =\frac{1}{95}\left[\begin{array}{ll}7 & 3 \\ 3 & 4\end{array}\right]\end{aligned}$

</details>

---

### Q49. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $(B A)^{-1}=C$ where $B=\left[\begin{array}{ccc}2 & 6 & 4 \\ 1 & 0 & 1 \\ -1 & 1 & -1\end{array}\right]$ and $C=\left[\begin{array}{ccc}-1 & 0 & 1 \\ 1 & 1 & 3 \\ 2 & 0 & 2\end{array}\right]$, then $A^{-1}$ is given by

**Options:**

- **(A)** $\left[\begin{array}{ccc}-3 & -3 & 5 \\ 0 & 9 & 2 \\ 2 & 14 & 6\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}-3 & -5 & -5 \\ 0 & 9 & 2 \\ 2 & 14 & 6\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}-3 & -5 & 5 \\ 0 & 9 & 14 \\ 2 & 2 & 6\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}-3 & 5 & 5 \\ 0 & 9 & 2 \\ 2 & 14 & 6\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{ccc}-3 & -5 & -5 \\ 0 & 9 & 2 \\ 2 & 14 & 6\end{array}\right]$**

**Detailed Solution:**

$(B A)^{-1}=C$
$\begin{aligned} & \Rightarrow A^{-1} B^{-1}=C \\ & \Rightarrow A^{-1} B^{-1} B=C B \\ & \Rightarrow A^{-1}=C B \\ & \Rightarrow A^{-1}=\left[\begin{array}{ccc}-1 & 0 & 1 \\ 1 & 1 & 3 \\ 2 & 0 & 2\end{array}\right]\left[\begin{array}{ccc}2 & 6 & 4 \\ 1 & 0 & 1 \\ -1 & 1 & -1\end{array}\right]=\left[\begin{array}{ccc}-3 & -5 & -5 \\ 0 & 9 & 2 \\ 2 & 14 & 6\end{array}\right]\end{aligned}$

</details>

---

### Q50. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If matrix $A=\left[\begin{array}{ll}1 & 2 \\ 3 & 5\end{array}\right]$ and $A^{-1}=\alpha I+\beta A$ where $I$ is a unit matrix of order 2 and $\alpha, \beta$ are constants, then the value of $\alpha+\beta+\alpha \beta$ is

**Options:**

- **(A)** $11$
- **(B)** $-7$
- **(C)** $7$
- **(D)** $-11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-11$**

**Detailed Solution:**

$\begin{aligned} & A^{-1}=\alpha I+\beta A \\ & \Rightarrow\left[\begin{array}{ll}1 & 2 \\ 3 & 5\end{array}\right]^{-1}=\alpha\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]+\beta\left[\begin{array}{ll}1 & 2 \\ 3 & 5\end{array}\right] \\ & \Rightarrow\left[\begin{array}{cc}-5 & 2 \\ 3 & -1\end{array}\right]=\left[\begin{array}{cc}\alpha+\beta & 2 \beta \\ 3 \beta & \alpha+5 \beta\end{array}\right] \\ & \Rightarrow \alpha=-6, \beta=1\end{aligned}$
Now $\alpha+\beta+\alpha \beta=-6+1+(-6) \times 1=-11$

</details>

---

### Q51. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right]$, then $A-A^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}-5 & 0 \\ 0 & -5\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}3 & 2 \\ 10 & 3\end{array}\right]$
- **(C)** $3\left[\begin{array}{cc}3 & -2 \\ \frac{10}{3} & -3\end{array}\right]$
- **(D)** $5\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3\left[\begin{array}{cc}3 & -2 \\ \frac{10}{3} & -3\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & A-A^{-1}=\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right]-\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right]^{-1}=\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right]-\left[\begin{array}{ll}-7 & 3 \\ -5 & 2\end{array}\right] \\ & =\left[\begin{array}{cc}9 & -6 \\ 10 & -9\end{array}\right]=3\left[\begin{array}{cc}3 & -2 \\ \frac{10}{3} & -3\end{array}\right]\end{aligned}$

</details>

---

### Q52. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$ such that $A^2-4 A+3 I=0$, where $\mathrm{I}$ is a unit matrix of order 2 , then $A^{-1}$ is

**Options:**

- **(A)** $\frac{1}{3}\left[\begin{array}{cc}-2 & 1 \\ 1 & -2\end{array}\right]$
- **(B)** $\frac{1}{3}\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$
- **(C)** $\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$
- **(D)** $\frac{1}{3}\left[\begin{array}{cc}-1 & 2 \\ 2 & -1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & A^2-4 A+3 I=0 \Rightarrow A(4 I-A)=3 I \Rightarrow A\left(\frac{4 I-A}{3}\right)=I \\ & \Rightarrow A^{-1}=\frac{4 I-A}{3}=\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]\left[\text { as } A A^{-1}=I\right]\end{aligned}$

</details>

---

### Q53. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}3 & 2 \\ 0 & 1\end{array}\right]$, then $\left(A^{-1}\right)^3=$

**Options:**

- **(A)** $\frac{1}{27}\left[\begin{array}{cc}-1 & 26 \\ 0 & 27\end{array}\right]$
- **(B)** $\frac{1}{27}\left[\begin{array}{ll}1 & -26 \\ 0 & -27\end{array}\right]$
- **(C)** $\frac{1}{27}\left[\begin{array}{cc}1 & -26 \\ 0 & 27\end{array}\right]$
- **(D)** $\frac{1}{27}\left[\begin{array}{cc}1 & 26 \\ 0 & -27\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{27}\left[\begin{array}{cc}1 & -26 \\ 0 & 27\end{array}\right]$**

**Detailed Solution:**

$\left(A^{-1}\right)^3=\left(A^3\right)^{-1}=\left\{\left[\begin{array}{ll}3 & 2 \\ 0 & 1\end{array}\right]^3\right\}^{-1}=\left[\begin{array}{cc}27 & 26 \\ 0 & 1\end{array}\right]^{-1}=\frac{1}{27}\left[\begin{array}{cc}1 & -26 \\ 0 & 27\end{array}\right]$

</details>

---

### Q54. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{lll}1 & 2 & 1 \\ 3 & 1 & 3\end{array}\right]$ and $B=\left[\begin{array}{ll}2 & 3 \\ 1 & 2 \\ 1 & 2\end{array}\right]$, then $(A B)^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}\frac{-17}{5} & \frac{9}{5} \\ 2 & -1\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}\frac{17}{5} & \frac{9}{5} \\ 2 & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}\frac{-17}{5} & 2 \\ \frac{-9}{5} & -1\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}\frac{-17}{5} & 2 \\ \frac{9}{5} & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}\frac{-17}{5} & \frac{9}{5} \\ 2 & -1\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & A B=\left[\begin{array}{ll}2+1+1 & 3+4+2 \\ 6+1+3 & 9+2+6\end{array}\right] \\ & =\left[\begin{array}{cc}5 & 9 \\ 10 & 17\end{array}\right] \\ & (A B)-1=\frac{1}{-5}\left[\begin{array}{cc}17 & -9 \\ -10 & 5\end{array}\right]=\left[\begin{array}{cc}-\frac{17}{5} & \frac{9}{5} \\ 2 & -1\end{array}\right]\end{aligned}$

</details>

---

### Q55. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}1 & a & 3 \\ 1 & 1 & 5 \\ 2 & 4 & 7\end{array}\right]$ and $A^{-1}=\left[\begin{array}{ccc}13 & 2 & -7 \\ -3 & b & 2 \\ -2 & 0 & 1\end{array}\right]$, then the values of $a$ and $b$ are respectively

**Options:**

- **(A)** $2,-1$
- **(B)** 1,2
- **(C)** 2,1
- **(D)** $-1,2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2,-1$**

**Detailed Solution:**

$$
|A|=1 \times(7-20)-a(10-7)+3(4-2)=3 a-7
$$
Now $-3=-\left\{\frac{-3}{3 a-7}\right\} \Rightarrow a=2$
Also $\mathrm{b}=\frac{7-6}{3 \mathrm{a}-7}=\frac{1}{3 \times 2-7}=-1$
Hence $\mathrm{a}=2$ and $\mathrm{b}=-1$

</details>

---

### Q56. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 3 & 4 \\ 3 & 4 & 3\end{array}\right]$, then $A^{-1}=$

**Options:**

- **(A)** $-\frac{1}{4}\left[\begin{array}{ccc}-7 & -6 & -1 \\ 9 & 6 & -1 \\ -5 & -2 & 1\end{array}\right]$
- **(B)** $\frac{1}{4}\left[\begin{array}{ccc}-7 & 6 & -1 \\ 9 & -6 & -1 \\ -5 & 2 & 1\end{array}\right]$
- **(C)** $-\frac{1}{4}\left[\begin{array}{ccc}-7 & 6 & 1 \\ 9 & -1 & 1 \\ -5 & 2 & 1\end{array}\right]$
- **(D)** $-\frac{1}{4}\left[\begin{array}{ccc}-7 & 6 & -1 \\ 9 & -6 & -1 \\ -5 & 2 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\frac{1}{4}\left[\begin{array}{ccc}-7 & 6 & -1 \\ 9 & -6 & -1 \\ -5 & 2 & 1\end{array}\right]$**

**Detailed Solution:**

$\because A^{-1}=\frac{\operatorname{adj}(A)}{|A|}=-\frac{1}{4}\left[\begin{array}{ccc}-7 & 6 & -1 \\ 9 & -6 & -1 \\ -5 & 2 & 1\end{array}\right]$

</details>

---

### Q57. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}0 & 1+2 i & i-2 \\ -1-2 i & 0 & K \\ 2-1 & 7 & 0\end{array}\right]$ and $A^{-1}$ does not exists, then $K=$ (where $\mathrm{i}=\sqrt{-1}$ )

**Options:**

- **(A)** $1+2 i$
- **(B)** $-7$
- **(C)** $7$
- **(D)** $1-2 i$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-7$**

**Detailed Solution:**

The inverse of an order skew-symmetric does not exist Hence, $\mathrm{K}=-7$

</details>

---

### Q58. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The element in the third row and second column of the inverse of the $\operatorname{matrix}\left[\begin{array}{ccc}3 & 2 & 6 \\ 1 & 1 & 2 \\ 2 & 2 & 5\end{array}\right]$ is

**Options:**

- **(A)** $1$
- **(B)** $-2$
- **(C)** $2$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-2$**

**Detailed Solution:**

The element of third row and second column of inverse of a matrix
$$
=\frac{\text { Cofactor of second row and third column of the matrix }}{\text { Determinant of the matrix }}
$$
$$
\begin{aligned}
& =\frac{-(3 \times 2-2 \times 2)}{3(1 \times 5-2 \times 2)+2(2 \times 2-1 \times 5)+6(1 \times 2-2 \times 1)} \\
& =\frac{-2}{3-2+0} \\
& =-2
\end{aligned}
$$

</details>

---

### Q59. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}\lambda & i \\ i & -\lambda\end{array}\right]$ and $A^{-1}$ does not exist, then $\lambda=($ where $I=\sqrt{-1})$

**Options:**

- **(A)** $\pm 2$
- **(B)** $\pm 1$
- **(C)** 0
- **(D)** $\pm 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pm 1$**

**Detailed Solution:**

$A=\left[\begin{array}{cc}
\lambda & \mathrm{i} \\
\mathrm{i} & -\lambda
\end{array}\right] \Rightarrow|\mathrm{A}|=\left|\begin{array}{cc}
\lambda & \mathrm{i} \\
\mathrm{i} & -\lambda
\end{array}\right|$
Since $\mathrm{A}^{-1}$ does not exist, we write $|\mathrm{A}|=0$
$\therefore\left(-\lambda^2\right)-\left(\mathrm{i}^2\right)=0 \quad \Rightarrow \lambda^2=1 \Rightarrow \lambda= \pm 1$

</details>

---

### Q60. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following matrices are invertible?
$$
\mathrm{A}=\left[\begin{array}{cc}
2 & 3 \\
10 & 15
\end{array}\right], \mathrm{B}=\left[\begin{array}{ccc}
1 & 2 & 3 \\
2 & -1 & 3 \\
1 & 2 & 3
\end{array}\right], \mathrm{C}=\left[\begin{array}{lll}
1 & 2 & 3 \\
3 & 4 & 5 \\
4 & 6 & 8
\end{array}\right], \mathrm{D}=\left[\begin{array}{lll}
2 & 4 & 2 \\
1 & 1 & 0 \\
1 & 4 & 5
\end{array}\right]
$$

**Options:**

- **(A)** both A and B
- **(B)** only C
- **(C)** only A
- **(D)** only D

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) only D**

**Detailed Solution:**

$\begin{aligned} & |A|=\left[\begin{array}{cc}2 & 3 \\ 10 & 15\end{array}\right]=30-30=0 \mid \\ & |B|=\left[\begin{array}{ccc}1 & 2 & 3 \\ 2 & -1 & 3 \\ 1 & 2 & 3\end{array}\right]=0 \quad \ldots\left[\mathrm{R}_1 \text { and } \mathrm{R}_2 \text { are identical }\right] \\ & |\mathrm{C}|=\left[\begin{array}{lll}1 & 2 & 3 \\ 3 & 4 & 5 \\ 4 & 6 & 8\end{array}\right]=1(2)-2(4)+3(2)=0 \\ & |\mathrm{D}|=\left[\begin{array}{lll}2 & 4 & 2 \\ 1 & 1 & 0 \\ 1 & 4 & 5\end{array}\right]=2(5)-4(5)+2(3)=-4 \neq 0\end{aligned}$

</details>

---

### Q61. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\left[\begin{array}{cc}2 & 3 \\ 5 & -2\end{array}\right]$ and $\mathrm{A}^{-1}=\mathrm{KA}$, then $\mathrm{K}$ is

**Options:**

- **(A)** 19
- **(B)** $\frac{-1}{19}$
- **(C)** $-19$
- **(D)** $\frac{1}{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{19}$**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{cc}2 & 3 \\ 5 & -2\end{array}\right] \\ & |A|-4-15=-19 \text { and adj } A=\left[\begin{array}{cc}-2 & -3 \\ -5 & 2\end{array}\right] \\ & \therefore A^{-1}=\frac{-1}{19}\left[\begin{array}{cc}-2 & -3 \\ -5 & 2\end{array}\right]=\frac{1}{19}\left[\begin{array}{cc}2 & 3 \\ 5 & -2\end{array}\right] \Rightarrow \mathrm{k}=\frac{1}{19}\end{aligned}$

</details>

---

### Q62. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}2 & -2 \\ 2 & -3\end{array}\right], B=\left[\begin{array}{cc}0 & -1 \\ 1 & 0\end{array}\right]$, then $\left(B^{-1} A^{-1}\right)^{-1}=$ ?

**Options:**

- **(A)** $A=\left[\begin{array}{ll}-2 & -2 \\ -3 & -2\end{array}\right]$
- **(B)** $A=\left[\begin{array}{cc}2 & 2 \\ -2 & -3\end{array}\right]$
- **(C)** $A=\left[\begin{array}{cc}3 & -2 \\ 2 & 2\end{array}\right]$
- **(D)** $A=\left[\begin{array}{cc}1 & -1 \\ -2 & 3\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $A=\left[\begin{array}{ll}-2 & -2 \\ -3 & -2\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \left(B^{-1} A^{-1}\right)^{-1}=\left(A^{-1}\right)^{-1}\left(B^{-1}\right)^{-1}=A B \\ & \therefore\left(B^{-1} A^{-1}\right)^{-1}=\left[\begin{array}{ll}2 & -2 \\ 2 & -3\end{array}\right]\left[\begin{array}{cc}0 & -1 \\ 1 & 0\end{array}\right]=\left[\begin{array}{ll}-2 & -2 \\ -3 & -2\end{array}\right]\end{aligned}$

</details>

---

### Q63. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $A=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 1 & a \\ 2 & 4 & 7\end{array}\right]$ and $B=\left[\begin{array}{ccc}13 & 2 & b \\ -3 & -1 & 2 \\ -2 & 0 & 1\end{array}\right]$ where matrix $B$ is inverse of matrix $a$, then the value of $a$ and $b$ are

**Options:**

- **(A)** $\mathrm{a}=-5, \mathrm{~b}=7$
- **(B)** $a=7, b=-5$
- **(C)** $a=-7, b=5$
- **(D)** $a=5, b=-7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=5, b=-7$**

**Detailed Solution:**

$$
A=\left|\begin{array}{lll}
1 & 2 & 3 \\
1 & 1 & a \\
2 & 4 & 7
\end{array}\right|=(7-4 a)-2(7-2 a)+3(2)=-1
$$
matrix B is inverse of matrix A. ' $b$ ' is element $(1 \times 3)$ in matrix B. Here element $(3 \times 1)$ in matrix $A$ is 2 .
Cofactor of $2==(-1)^{3+1}\left|\begin{array}{ll}2 & 3 \\ 1 & \mathrm{a}\end{array}\right|=2 \mathrm{a}-3$
Now $\frac{2 \mathrm{a}-3}{-1}=\mathrm{b} \Rightarrow 2 \mathrm{a}+\mathrm{b}=3$
For element $(1 \times 2)$ in matrix A i.e. 2
Now cofactor of 2 is $(-1)^{1+2}\left|\begin{array}{ll}1 & a \\ 2 & 7\end{array}\right|=-(7-2 a)$ and
$$
\frac{-(7-2 \mathrm{a})}{-1}=7-2 \mathrm{a}
$$
Here element $(2 \times 1)$ in matrix B is -3
$$
\therefore 7-2 \mathrm{a}=-3
$$
Solving eq. (1) and (2), we get $\mathrm{a}=5, \mathrm{~b}=-7$

</details>

---

### Q64. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 2 & 1 \\ -1 & 1 & 3\end{array}\right]$ and $B=\left[\begin{array}{cc}1 & 2 \\ -3 & 1 \\ 0 & 2\end{array}\right]$, then $(A B)^{-1}$

**Options:**

- **(A)** $\left[\begin{array}{cc}5 & -6 \\ -4 & 5\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}5 & 6 \\ 4 & 5\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}-5 & 6 \\ -4 & 5\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}-5 & -6 \\ -4 & -5\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{ll}-5 & 6 \\ -4 & 5\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{AB}=\left[\begin{array}{ccc}1 & 2 & 1 \\ -1 & 1 & 3\end{array}\right]\left[\begin{array}{cc}1 & 2 \\ -3 & 1 \\ 0 & 2\end{array}\right] \\ & =\left[\begin{array}{cc}1-6+0 & 2+2+2 \\ -1-3+0 & -2+1+6\end{array}\right]=\left[\begin{array}{ll}-5 & 6 \\ -4 & 5\end{array}\right] \\ & \therefore|\mathrm{AB}|=\left[\begin{array}{cc}5 & -6 \\ 4 & -5\end{array}\right] \\ & \therefore(\mathrm{AB})^{-1}=\frac{\left[\begin{array}{cc}5 & -6 \\ 4 & -5\end{array}\right]}{(-1)}=\left[\begin{array}{ll}-5 & 6 \\ -4 & 5\end{array}\right]\end{aligned}$

</details>

---

### Q65. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}1 & 0 & 1 \\ 0 & 2 & 3 \\ 1 & 2 & 1\end{array}\right]$, then the value of determinant of $A^{-1}$ is

**Options:**

- **(A)** $-6$
- **(B)** $\frac{-1}{6}$
- **(C)** $\frac{1}{36}$
- **(D)** 36

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{6}$**

**Detailed Solution:**

$$
\begin{aligned}
& \text { We have } A=\left[\begin{array}{lll}
1 & 0 & 1 \\
0 & 2 & 3 \\
1 & 2 & 1
\end{array}\right] \\
& \therefore|A|=(2-6)+(0-2)=-6
\end{aligned}
$$
We know that $\left|\mathrm{A}^{-1}\right|=\frac{1}{|\mathrm{~A}|}$
$$
\therefore\left|\mathrm{A}^{-1}\right|=\frac{1}{-6}
$$

</details>

---

### Q66. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}\mathrm{k} & 2 \\ -2 & -\mathrm{k}\end{array}\right]$, then $\mathrm{A}^{-1}$ does not exists if $\mathrm{k}=$

**Options:**

- **(A)** $3$
- **(B)** $\pm 2$
- **(C)** $0$
- **(D)** $\pm 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\pm 2$**

**Detailed Solution:**

$$
\begin{aligned}
& A=\left[\begin{array}{cc}
\mathrm{k} & 2 \\
-2 & -\mathrm{k}
\end{array}\right] \\
& \therefore|\mathrm{A}|=\left[\begin{array}{cc}
\mathrm{k} & 2 \\
-2 & -\mathrm{k}
\end{array}\right]=-\mathrm{k}^2+4
\end{aligned}
$$
When $-\mathrm{k}^2+4=0$, we get $\mathrm{k}= \pm 2$

</details>

---

### Q67. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 1 & 1\end{array}\right]$, then $A^{-1}=$

**Options:**

- **(A)** $\left(\frac{1}{2}\right)\left[\begin{array}{lll}0 & 1 & 2 \\ 3 & 2 & 1 \\ 4 & 2 & 3\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}\frac{1}{2} & \frac{-1}{2} & \frac{1}{2} \\ -4 & 3 & -1 \\ \frac{5}{2} & \frac{-3}{2} & \frac{1}{2}\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}\frac{1}{2} & -1 & \frac{5}{2} \\ 1 & -6 & 3 \\ 1 & 2 & -1\end{array}\right]$
- **(D)** $\left(\frac{1}{2}\right)\left[\begin{array}{ccc}1 & -1 & -1 \\ -8 & 6 & -2 \\ 5 & -3 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{ccc}\frac{1}{2} & \frac{-1}{2} & \frac{1}{2} \\ -4 & 3 & -1 \\ \frac{5}{2} & \frac{-3}{2} & \frac{1}{2}\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & {\left[\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 1 & 1\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]} \\ & \mathrm{R}_1 \rightarrow \mathrm{R}_1+\mathrm{R}_2 \text { and } \mathrm{R}_3 \rightarrow \mathrm{R}_3-3 \mathrm{R}_2 \\ & {\left[\begin{array}{ccc}1 & 3 & 5 \\ 1 & 2 & 3 \\ 0 & -5 & -8\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{ccc}1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1\end{array}\right]} \\ & \mathrm{R}_2 \rightarrow \mathrm{R}_2-\mathrm{R}_1 \\ & {\left[\begin{array}{ccc}1 & 3 & 5 \\ 0 & -1 & -2 \\ 0 & -5 & -8\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{ccc}1 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & -3 & 1\end{array}\right]} \\ & \mathrm{R}_1 \rightarrow \mathrm{R}_1+3 \mathrm{R}_2 \text { and } \mathrm{R}_3 \rightarrow \mathrm{R}_3-5 \mathrm{R}_2 \\ & {\left[\begin{array}{ccc}1 & 0 & -1 \\ 0 & -1 & -2 \\ 0 & 0 & 2\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{ccc}-2 & 1 & 0 \\ -1 & 0 & 0 \\ 5 & -3 & 1\end{array}\right]}\end{aligned}$
$\mathrm{R}_2 \rightarrow \mathrm{R}_2+\mathrm{R}_3$ and $\mathrm{R}_1 \rightarrow 2 \mathrm{R}_1+\mathrm{R}_3$
$\begin{aligned} & {\left[\begin{array}{ccc}2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{ccc}1 & -1 & 1 \\ 4 & -3 & 1 \\ 5 & -3 & 1\end{array}\right]} \\ & \mathrm{R}_1=\frac{1}{2} \mathrm{R}_1, \mathrm{R}_2 \rightarrow-\mathrm{R}_2, \mathrm{R}_3 \rightarrow \frac{1}{2} \mathrm{R}_3 \\ & {\left[\begin{array}{ccc}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right] \mathrm{A}^{-1}=\left[\begin{array}{ccc}\frac{1}{2} & \frac{-1}{2} & \frac{1}{2} \\ -4 & 3 & -1 \\ \frac{5}{2} & \frac{-3}{2} & \frac{1}{2}\end{array}\right]}\end{aligned}$

</details>

---

### Q68. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$A=\left[\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & a & 1\end{array}\right]$ and $A^{-1}=\frac{1}{2}\left[\begin{array}{ccc}1 & -1 & 1 \\ -8 & 6 & 2 c \\ 5 & -3 & 1\end{array}\right]$, then values of $a$ and $\mathrm{c}$ are respectively

**Options:**

- **(A)** $\frac{1}{2}, \frac{1}{2}$
- **(B)** -1,1
- **(C)** $2, \frac{-1}{2}$
- **(D)** 1,-1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1,-1**

**Detailed Solution:**

We know that $\mathrm{AA}^{-1}=1$
$$
\begin{aligned}
& \therefore\left[\begin{array}{lll}
0 & 1 & 2 \\
1 & 2 & 3 \\
3 & \mathrm{a} & 1
\end{array}\right]\left[\begin{array}{ccc}
\frac{1}{2} & \frac{-1}{2} & \frac{1}{2} \\
-4 & 3 & \mathrm{c} \\
\frac{5}{2} & \frac{-3}{2} & \frac{1}{2}
\end{array}\right]=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& \therefore\left[\begin{array}{ccc}
1 & 0 & \mathrm{c}+1 \\
0 & 1 & 2+2 \mathrm{c} \\
4-4 \mathrm{a} & 3 \mathrm{a}-3 & 2+\mathrm{ac}
\end{array}\right]=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]
\end{aligned}
$$
Thus $\mathrm{c}+1 \Rightarrow \mathrm{c}=-1$ and $4-4 \mathrm{a}=0 \Rightarrow \mathrm{a}=1$

</details>

---

### Q69. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A^{-1}=\frac{-1}{2}\left[\begin{array}{cc}5 & 8 \\ -1 & 2\end{array}\right]$, then $2 A+I_2=$, where $I_2$ is a unit matrix of order 2

**Options:**

- **(A)** $\left[\begin{array}{ll}5 & 8 \\ 1 & 2\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}5 & 8 \\ 2 & 2\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}2 & 4 \\ 1 & 1\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}5 & 8 \\ 2 & 3\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{ll}5 & 8 \\ 2 & 3\end{array}\right]$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{A}^{-1}=\frac{-1}{2}\left[\begin{array}{cc}
1 & -4 \\
-1 & 2
\end{array}\right]=\left[\begin{array}{cc}
\frac{-1}{2} & 2 \\
\frac{1}{2} & -1
\end{array}\right] \\
& \mathrm{AA}^{-1}=\mathrm{I} \Rightarrow \mathrm{A}\left[\begin{array}{cc}
\frac{-1}{2} & 2 \\
\frac{1}{2} & -1
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]
\end{aligned}
$$


$$
\begin{aligned}
& \mathrm{R}_2 \rightarrow \mathrm{R}_1+\mathrm{R}_2 \\
& \mathrm{~A}\left[\begin{array}{ll}
\frac{-1}{2} & 2 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right] \\
& \mathrm{R}_1 \rightarrow \mathrm{R}_1+2 \mathrm{R}_2 \\
& \mathrm{~A}\left[\begin{array}{cc}
\frac{-1}{2} & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{cc}
-1 & -2 \\
1 & 1
\end{array}\right] \\
& \mathrm{R}_1 \rightarrow-2 \mathrm{R}_1 \\
& \mathrm{~A}\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
2 & 4 \\
1 & 1
\end{array}\right] \Rightarrow \mathrm{A}=\left[\begin{array}{ll}
2 & 4 \\
1 & 1
\end{array}\right] \\
& \therefore 2 \mathrm{~A}+\mathrm{I}_2=\left[\begin{array}{ll}
4 & 8 \\
2 & 2
\end{array}\right]+\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{ll}
5 & 8 \\
2 & 3
\end{array}\right]
\end{aligned}
$$

</details>

---

### Q70. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $F(\propto)=\left[\begin{array}{ccc}\cos \propto & -\sin \propto & 0 \\ \sin \propto & \cos \propto & 0 \\ 0 & 0 & 1\end{array}\right]$, where $\propto \in R$, then $[F(\propto)]^{-1}$

**Options:**

- **(A)** $\mathrm{F}(-\propto)$
- **(B)** $F(2 \propto)$
- **(C)** $F(\propto)$
- **(D)** $\mathrm{F}(3 \propto)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{F}(-\propto)$**

**Detailed Solution:**

$$
\begin{aligned}
& F(\propto)=\left[\begin{array}{ccc}
\cos \propto & -\sin \propto & 0 \\
\sin \propto & \cos \propto & 0 \\
0 & 0 & 1
\end{array}\right] \\
& \therefore|F(\alpha)|=\cos \alpha(\cos \alpha)+\sin \alpha(\sin \alpha)=\cos ^2 \alpha+\sin ^2 \alpha=1 \\
& \therefore \operatorname{adj}[F(\alpha)]=\left[\begin{array}{ccc}
\cos \alpha & -\sin \alpha & 0 \\
\sin \alpha & \cos \alpha & 0 \\
0 & 0 & 1
\end{array}\right]^{\mathrm{T}}
\end{aligned}
$$


$$
\begin{aligned}
& =\left[\begin{array}{ccc}
\cos \alpha & \sin \alpha & 0 \\
-\sin \alpha & \cos \alpha & 0 \\
0 & 0 & 1
\end{array}\right]=\left[\begin{array}{ccc}
\cos (-\alpha)
& -\sin (-\alpha) 
& 0 \\
\sin (-\alpha) 
& \cos (-\alpha) 
& 0 \\
0 & 0 & 1
\end{array}\right] \\
& {[F(\alpha)]^{-1}=\frac{\operatorname{adj}[F(\alpha)]}{|F(\alpha)|}=F(-\alpha)}
\end{aligned}
$$

</details>

---

### Q71. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A^{-1}=\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right]$ and $B^{-1}=\left[\begin{array}{cc}1 & 0 \\ -3 & 1\end{array}\right]$, then $(A B)^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}2 & 7 \\ 3 & -1\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}2 & -7 \\ -3 & 11\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}2 & 3 \\ 7 & -11\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$**

**Detailed Solution:**

$$
\begin{aligned}
& (\mathrm{AB})^{-1}=\mathrm{B}^{-1} \mathrm{~A}^{-1} \\
& =\left[\begin{array}{cc}
1 & 0 \\
-3 & 1
\end{array}\right]\left[\begin{array}{cc}
2 & -3 \\
-1 & 2
\end{array}\right] \\
& =\left[\begin{array}{cc}
2+0 & -3+0 \\
-6-1 & 9+2
\end{array}\right]=\left[\begin{array}{cc}
2 & -3 \\
-7 & 11
\end{array}\right]
\end{aligned}
$$

</details>

---

### Q72. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If inverse of $\left[\begin{array}{ccc}1 & 2 & x \\ 4 & -1 & 7 \\ 2 & 4 & -6\end{array}\right]$ does not exist, then $x=$

**Options:**

- **(A)** -3
- **(B)** 2
- **(C)** 3
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -3**

**Detailed Solution:**

$\begin{aligned} & \text { Here }\left[\begin{array}{ccc}1 & 2 & x \\ 4 & -1 & 7 \\ 2 & 4 & -6\end{array}\right]=0 \\ & \therefore(6-28)-2(-24-14)+x(16+20)=0 \\ & \therefore-22+76+18 x=\Rightarrow x=-3\end{aligned}$

</details>

---

### Q73. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$ and $X$ is a $2 \times 2$ matrix such that $A X=1$, then $X=$

**Options:**

- **(A)** $\left[\begin{array}{cc}-2 & 1 \\ \frac{3}{2} & \frac{1}{2}\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}2 & 1 \\ \frac{3}{2} & -\frac{1}{2}\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}-2 & 1 \\ -\frac{3}{2} & -\frac{1}{2}\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}-2 & 1 \\ \frac{3}{2} & -\frac{1}{2}\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}-2 & 1 \\ \frac{3}{2} & -\frac{1}{2}\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} A=\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right] & \text { and } A X=I \\ \therefore X=A^{-1} \Rightarrow A^{-1} &=\frac{1}{4-6}\left[\begin{array}{cc}4 & -2 \\ -3 & 1\end{array}\right] \\ &=\frac{1}{-2}\left[\begin{array}{cc}4 & -2 \\ -3 & 1\end{array}\right]=\left[\begin{array}{cc}-2 & 1 \\ \frac{3}{2} & \frac{-1}{2}\end{array}\right] \end{aligned}$

</details>

---

### Q74. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right]$, then $2 A-3 A^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}25 & 15 \\ 25 & 20\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}25 & 25 \\ -15 & -20\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}25 & -15 \\ 25 & -20\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}25 & -25 \\ -15 & -20\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{cc}25 & -15 \\ 25 & -20\end{array}\right]$**

**Detailed Solution:**

$A=\left[\begin{array}{ll}2 & -3 \\ 5 & -7\end{array}\right] \Rightarrow|A|=-14+15=1$
$\therefore A^{-1}=\left[\begin{array}{cc}-7 & 3 \\ -5 & 2\end{array}\right] \quad$ and $\quad 2 A=\left[\begin{array}{cc}4 & -6 \\ 10 & -14\end{array}\right]$
$\therefore 2 A-3 A^{-1}=\left[\begin{array}{cc}4-(-21) & -6-9 \\ 10-(-15) & -14-6\end{array}\right]=\left[\begin{array}{cc}25 & -15 \\ 25 & -20\end{array}\right]$

</details>

---

### Q75. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}1 & 2 \\ -5 & 1\end{array}\right]$ and $A^{-1}=x A+y I$, where $I$ is unit matrix of order 2 , then the values of $x$ and $y$ are respectively

**Options:**

- **(A)** $\frac{1}{11}, \frac{2}{11}$
- **(B)** $\frac{-1}{11}, \frac{2}{11}$
- **(C)** $\frac{1}{11}, \frac{-2}{11}$
- **(D)** $\frac{-1}{11}, \frac{-2}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{-1}{11}, \frac{2}{11}$**

**Detailed Solution:**

$|\mathrm{A}|=\left|\begin{array}{cc}1 & 2 \\ -5 & 1\end{array}\right|=1+10=11$ and adj $\mathrm{A}=\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right]$
$\therefore \mathrm{A}^{-1}=\frac{1}{11}\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right]$
Given $\mathrm{A}^{-1}=\mathrm{x} \mathrm{A}+\mathrm{yI}$
$$
\frac{1}{11}\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right]=\left[\begin{array}{cc}\mathrm{x} & 2 \mathrm{x} \\ -5 \mathrm{x} & \mathrm{x}\end{array}\right]+\left[\begin{array}{ll}\mathrm{y} & 0 \\ 0 & \mathrm{y}\end{array}\right]
$$
$\therefore \frac{1}{11}\left[\begin{array}{cc}1 & -2 \\ 5 & 1\end{array}\right] \quad=\left[\begin{array}{cc}\mathrm{x}+\mathrm{y} & 2 \mathrm{x} \\ -5 \mathrm{x} & \mathrm{x}+\mathrm{y}\end{array}\right]$
$\therefore 2 \mathrm{x}=\frac{-2}{11} \Rightarrow \mathrm{x}=\frac{-1}{11}$ and $\mathrm{x}+\mathrm{y}=\frac{1}{11} \Rightarrow \mathrm{y}=\frac{2}{11}$

</details>

---

### Q76. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The element in the third row and first column of the inverse of the matrix $\left[\begin{array}{ccc}1 & -3 & 2 \\ -3 & 3 & -1 \\ 2 & -1 & 0\end{array}\right]$ is

**Options:**

- **(A)** $-3$
- **(B)** $x=4$
- **(C)** $3$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$**

**Detailed Solution:**

We have $A=\left[\begin{array}{ccc}-1 & -3 & 2 \\ -3 & 3 & -1 \\ 2 & -1 & 0\end{array}\right] \Rightarrow \begin{aligned}|A| &=\left|\begin{array}{ccc}-1 & -3 & 2 \\ -3 & 3 & -1 \\ 2 & -1 & 0\end{array}\right| \\ &=-(-1)+3(2)+2(3-6)=1+6-6=1 \end{aligned}$
We have to find $a_{31}$ in $A^{-1}$. So we will find $A_{13}$ in $A$.
Cofactor of $2=(-1)^{1+3}\left|\begin{array}{cc}-3 & 3 \\ 2 & -1\end{array}\right|=3-6=-3$
Hence $a_{31}$ in $A^{-1}=\frac{-3}{|A|}=\frac{-3}{1}=-3$

</details>

---

### Q77. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}4 & 5 \\ 2 & 1\end{array}\right]$ and $A^{2}-5 A-6 I=0$, then $A^{-1}=$

**Options:**

- **(A)** $\frac{1}{6}\left[\begin{array}{cc}-1 & 5 \\ 2 & 4\end{array}\right]$
- **(B)** $\frac{1}{6}\left[\begin{array}{cc}-1 & 5 \\ -2 & -4\end{array}\right]$
- **(C)** $\frac{1}{6}\left[\begin{array}{cc}-1 & 5 \\ 2 & -4\end{array}\right]$
- **(D)** $\frac{1}{6}\left[\begin{array}{cc}1 & 5 \\ 2 & -4\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{6}\left[\begin{array}{cc}-1 & 5 \\ 2 & -4\end{array}\right]$**

**Detailed Solution:**

(D)
$\begin{array}{l}
A=\left[\begin{array}{cc}
4 & 5 \\
2 & 1
\end{array}\right] \Rightarrow|A|=4-10--6 \text { and }(\operatorname{adj} A)-\left[\begin{array}{cc}
1 & 5 \\
-2 & 4
\end{array}\right] \\
\therefore A^{-1}=-\frac{1}{6}\left[\begin{array}{cc}
1 & -5 \\
-2 & 4
\end{array}\right]=\frac{1}{6}\left[\begin{array}{cc}
-1 & 5 \\
2 & -4
\end{array}\right]
\end{array}$

</details>

---

### Q78. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\omega$ is a complex cube root of unity and $A=\left[\begin{array}{cc}\omega & 0 \\ 0 & \omega\end{array}\right]$, then $A^{-1}=$

**Options:**

- **(A)** $\mathrm{A}^{2}$
- **(B)** $2 \mathrm{~A}$
- **(C)** $-\mathrm{A}$
- **(D)** $\mathrm{A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{A}^{2}$**

**Detailed Solution:**

(C)
Given $A=\left[\begin{array}{ll}\omega & 0 \\ 0 & \omega\end{array}\right] \Rightarrow|A|=\left(\omega^{2}-0\right)=\omega^{2}$ and adj $A=\left[\begin{array}{cc}\omega & 0 \\ 0 & \omega\end{array}\right]$
$\therefore A^{-1}=\frac{1}{\omega^{2}}\left[\begin{array}{ll}\omega & 0 \\ 0 & \omega\end{array}\right]=\left[\begin{array}{cc}\frac{1}{\omega} & 0 \\ 0 & \frac{1}{\omega}\end{array}\right]=\left[\begin{array}{cc}\omega^{2} & 0 \\ 0 & \omega^{2}\end{array}\right] \quad \ldots\left[\because \omega^{3}=1\right]$
$\therefore A^{2}=\left[\begin{array}{ll}\omega & 0 \\ 0 & \omega\end{array}\right]\left[\begin{array}{ll}\omega & 0 \\ 0 & \omega\end{array}\right]=\left[\begin{array}{cc}\omega^{2} & 0 \\ 0 & \omega^{2}\end{array}\right]$

</details>

---

### Q79. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right], B=\left[\begin{array}{ll}1 & 0 \\ 3 & 1\end{array}\right]$, then $\mathrm{B}^{-1} \mathrm{~A}^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$
- **(B)** $\left[\begin{array}{lc}2 & 3 \\ 7 & 11\end{array}\right]$
- **(C)** $\left[\begin{array}{lc}-2 & -3 \\ -7 & 11\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}-2 & -3 \\ -7 & -11\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$**

**Detailed Solution:**

(A)
We have $A=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right] \Rightarrow|A|=4-3=1 \Rightarrow A^{-1}$ exists.
$B=\left[\begin{array}{ll}
1 & 0 \\
3 & 1
\end{array}\right] \Rightarrow|B|=1 \Rightarrow B^{-1} \text { exists }$
$\begin{aligned} A^{-1} &=\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right] \text { and } B^{-1}=\left[\begin{array}{cc}1 & 0 \\ -3 & 1\end{array}\right] \\ \therefore B^{-1} A^{-1} &=\left[\begin{array}{cc}1 & 0 \\ -3 & 1\end{array}\right]\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right] \\ &=\left[\begin{array}{cc}2+0 & -3+0 \\ -6-1 & 9+2\end{array}\right]=\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right] \end{aligned}$

</details>

---

### Q80. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The matrix $A=\left[\begin{array}{ccc}a & -1 & 4 \\ -3 & 0 & 1 \\ -1 & 1 & 2\end{array}\right]$ is not invertible only if a =

**Options:**

- **(A)** -17
- **(B)** -16
- **(C)** 16
- **(D)** 17

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -17**

**Detailed Solution:**

(D)
Since $\mathrm{A}$ is not invertible, $|\mathrm{A}|=0$
$\begin{aligned} \therefore &\left|\begin{array}{ccc}a & -1 & 4 \\ -3 & 0 & 1 \\ -1 & 1 & 2\end{array}\right|=0 \\ & \mathrm{a}(0-1)-(-1)(-6+1)+4(-3-0)=0 \Rightarrow-\mathrm{a}-5-12=0 \Rightarrow \mathrm{a}=-17 \end{aligned}$

</details>

---

### Q81. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}2 & 0 & -1 \\ 5 & 1 & 0 \\ 0 & 1 & 3\end{array}\right]$ and $A^{-1}=\left[\begin{array}{ccc}3 & -1 & 1 \\ \alpha & 6 & -5 \\ \beta & -2 & 2\end{array}\right]$, then the values of $\alpha$ and $\beta$ are. respectively

**Options:**

- **(A)** 15, 5
- **(B)** -15,5
- **(C)** 15,-5
- **(D)** -15,-5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) -15,5**

**Detailed Solution:**

(B)
We know,
$\begin{array}{l}
\mathrm{A} \cdot \mathrm{A}^{-1}=\mathrm{I} \\
{\left[\begin{array}{ccc}
2 & 0 & -1 \\
5 & 1 & 0 \\
0 & 1 & 3
\end{array}\right]\left[\begin{array}{ccc}
3 & -1 & 1 \\
\alpha & 6 & -5 \\
\beta & -2 & 2
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]} \\
{\left[\begin{array}{ccc}
6+0-\beta & -2+0+2 & 2+0-2 \\
15+\alpha+0 & -5+6+0 & 5-5+0 \\
0+\alpha+3 \beta & 0+6-6 & 0-5+6
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]} \\
{\left[\begin{array}{ccc}
6-\beta & 0 & 0 \\
15+\alpha & 1 & 0 \\
\alpha+3 \beta & 0 & 1
\end{array}\right]=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]} \\
6-\beta=1 \Rightarrow \beta=5 \text { and } 15+\alpha=0 \Rightarrow \alpha=-15
\end{array}$
This problem can also be solved as follows :
We have $A=\left[\begin{array}{ccc}2 & 0 & -1 \\ 5 & 1 & 0 \\ 0 & 1 & 3\end{array}\right] \Rightarrow|A|=2(3)-(5)=1$ $\alpha$ is $a_{21}$ in $A^{-1}$. So we will find cofactor of $a_{12}$ in $A$.

</details>

---

### Q82. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}1 & 2 & 1 \\ 2 & 1 & 0\end{array}\right], B=\left[\begin{array}{ll}1 & 2 \\ 2 & 1 \\ 0 & 1\end{array}\right]$, then $(\mathrm{AB})^{-1}$ is

**Options:**

- **(A)** $\left(\frac{1}{5}\right)\left[\begin{array}{ll}5 & -5 \\ 4 & -5\end{array}\right]$
- **(B)** $\left(\frac{1}{5}\right)\left[\begin{array}{cc}5 & -5 \\ -4 & 5\end{array}\right]$
- **(C)** $\left(\frac{1}{5}\right)\left[\begin{array}{cc}5 & -5 \\ 4 & 5\end{array}\right]$
- **(D)** $\left(\frac{1}{5}\right)\left[\begin{array}{cc}5 & -5 \\ -4 & -5\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\frac{1}{5}\right)\left[\begin{array}{cc}5 & -5 \\ -4 & 5\end{array}\right]$**

**Detailed Solution:**

$A=\left[\begin{array}{lll}1 & 2 & 1 \\ 2 & 1 & 0\end{array}\right]$ and $B=\left[\begin{array}{ll}1 & 2 \\ 2 & 1 \\ 0 & 1\end{array}\right]$
$\therefore A B$
$$
\begin{array}{l}(A B)^{-1} \\ =\frac{1}{|A B|}\left[\begin{array}{cc}1+4+0 & 2+2+1 \\ 2+2+0 & 4+1+0\end{array}\right]=\left[\begin{array}{ll}5 & 5 \\ 4 & 5\end{array}\right]\end{array}
$$

</details>

---

### Q83. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}1 & 1 \\ 1 & 2\end{array}\right], \quad B=\left[\begin{array}{ll}4 & 1 \\ 3 & 1\end{array}\right], \quad$ then $(A+B)^{-1}=$

**Options:**

- **(A)** $\frac{1}{7}\left[\begin{array}{ll}3 & 2 \\ 4 & 5\end{array}\right]$
- **(B)** $7\left[\begin{array}{cc}3 & 2 \\ 4 & 5\end{array}\right]$
- **(C)** $\frac{1}{7}\left[\begin{array}{cc}3 & -2 \\ -4 & 5\end{array}\right]$
- **(D)** $7\left[\begin{array}{cc}3 & -2 \\ -4 & 5\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{7}\left[\begin{array}{cc}3 & -2 \\ -4 & 5\end{array}\right]$**

**Detailed Solution:**

$A+B=\left[\begin{array}{ll}1 & 1 \\ 1 & 2\end{array}\right]+\left[\begin{array}{ll}4 & 1 \\ 3 & 1\end{array}\right]=\left[\begin{array}{ll}5 & 2 \\ 4 & 3\end{array}\right]$
$|A+B|=15-8=7$ and adj $(A+B)=\left[\begin{array}{cc}3 & -2 \\ -4 & 5\end{array}\right]$
$\therefore(A+B)^{-1}=\frac{1}{7}\left[\begin{array}{cc}3 & -2 \\ -4 & 5\end{array}\right]$

</details>

---

### Q84. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0\end{array}\right]$, then

**Options:**

- **(A)** $A$ is not invertible
- **(B)** $A=A^{-1}$
- **(C)** $A^{-1}=2 A$
- **(D)** $A^{-1}=I$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $A=A^{-1}$**

**Detailed Solution:**

Here $|\mathrm{A}|=-1(-1)=1$
and $\quad A^{-1}=\left[\begin{array}{ccc}0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0\end{array}\right]=A$

</details>

---

### Q85. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The value of $x$ such that the matrix $\left[\begin{array}{lll}x & 2 & 3 \\ 4 & 5 & 6 \\ 2 & 3 & 5\end{array}\right]$ is not invertible is

**Options:**

- **(A)** $\frac{-10}{7}$
- **(B)** $\frac{7}{10}$
- **(C)** $\frac{-7}{10}$
- **(D)** $\frac{10}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{10}{7}$**

**Detailed Solution:**

For given matrix to be invertible, we write
$$
\begin{array}{l}
\left|\begin{array}{lll}
x & 2 & 3 \\
4 & 5 & 6 \\
2 & 3 & 5
\end{array}\right|=0 \\
x(25-18)-2(20-12)+3(12-10)=0 \Rightarrow 7 x-16+6=0 \Rightarrow x=\frac{10}{7}
\end{array}
$$

</details>

---

### Q86. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the elements of matrix A are the reciprocals of elements of matrix $\left[\begin{array}{ccc}1 & \omega & \omega^{2} \\ \omega & \omega^{2} & 1 \\ \omega^{2} & 1 & \omega\end{array}\right]$,
where $\omega$ is complex cube root of unity, then

**Options:**

- **(A)** $A^{-1}=I$
- **(B)** $A^{-1}=A^{2}$
- **(C)** $A^{-1}=A$
- **(D)** $A^{-1} $does not exits

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $A^{-1} $does not exits**

**Detailed Solution:**

$\begin{aligned} \text { We have, } \mathrm{A} &=\left[\begin{array}{ccc}1 & \frac{1}{\omega} & \frac{1}{\omega^{2}} \\ \frac{1}{\omega} & \frac{1}{\omega^{2}} & 1 \\ \frac{1}{\omega^{2}} & 1 & \frac{1}{\omega}\end{array}\right] \\|\mathrm{A}| &=1\left\{\frac{1}{\omega^{3}}-1\right\}-\frac{1}{\omega}\left(\frac{1}{\omega^{2}}-\frac{1}{\omega^{2}}\right)+\frac{1}{\omega^{2}}\left(\frac{1}{\omega}-\frac{1}{\omega^{4}}\right) \\ &=1(1-1)-0+\frac{1}{\omega^{2}}\left(\frac{1}{\omega}-\frac{1}{\omega}\right) \quad\left[\because \omega^{3}=1 \text { and } \because \omega^{4}=\omega\right] \\|\mathrm{A}| &=0 \Rightarrow \mathrm{A}^{-1} \text { does not exist } \end{aligned}$

</details>

---

### Q87. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -1\end{array}\right]$, then $A^{4} A^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{ccc}8 & 0 & 0 \\ 0 & -8 & 0 \\ 0 & 0 & -1\end{array}\right]$
- **(B)** $\left[\begin{array}{lll}8 & 0 & 0 \\ 0 & 8 & 0 \\ 0 & 0 & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}\frac{1}{2} & 0 & 0 \\ 0 & \frac{-1}{2} & 0 \\ 0 & 0 & -1\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}-4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & -1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{ccc}8 & 0 & 0 \\ 0 & -8 & 0 \\ 0 & 0 & -1\end{array}\right]$**

**Detailed Solution:**

Understand that $\mathrm{A}$ is a diagonal matrix
$\therefore A^{n}=\left[\begin{array}{ccc}
a_{11}^{n} & 0 & 0 \\
0 & a_{22}^{n} & 0 \\
0 & 0 & a_{33}^{n}
\end{array}\right] \Rightarrow A^{4}=\left[\begin{array}{ccc}
16 & 0 & 0 \\
0 & 16 & 0 \\
0 & 0 & 1
\end{array}\right]$
$\begin{aligned} \text { Here }|A| &=\left[\begin{array}{ccc}2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -1\end{array} \mid=2(2)=4\right.\\ \operatorname{adj} A &=\left[\begin{array}{ccc}2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -4\end{array}\right] \Rightarrow A^{-1}=\frac{1}{4}\left[\begin{array}{ccc}2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -4\end{array}\right]=\left[\begin{array}{ccc}\frac{1}{2} & 0 & 0 \\ 0 & \frac{-1}{2} & 0 \\ 0 & 0 & -1\end{array}\right] \\ A^{4} A^{-1} &=\left[\begin{array}{ccc}16 & 0 & 0 \\ 0 & 16 & 0 \\ 0 & 0 & 1\end{array}\right]\left[\begin{array}{ccc}\frac{1}{2} & 0 & 0 \\ 0 & \frac{-1}{2} & 0 \\ 0 & 0 & -1\end{array}\right] \\ &=\left[\begin{array}{ccc}8 & 0 & 0 \\ 0 & -8 & 0 \\ 0 & 0 & -1\end{array}\right] \end{aligned}$

</details>

---

### Q88. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]$ and $B=\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right]$, then $\left(B^{-1} A^{-1}\right)^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}2 & 3 \\ 1 & -2\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}1 & 2 \\ 3 & 4\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$**

**Detailed Solution:**

$\left(\mathrm{B}^{-1} \mathrm{~A}^{-1}\right)^{-1}=\left(\mathrm{A}^{-1}\right)^{-1}\left(\mathrm{~B}^{-1}\right)^{-1}=\mathrm{AB}$
$\therefore \quad \mathrm{AB}=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{cc}2 & -3 \\ -1 & 2\end{array}\right]=\left[\begin{array}{cc}4-3 & -6+6 \\ 2-2 & -3+4\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$

</details>

---

### Q89. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$, then $A^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}-\sin \theta & -\cos \theta \\ -\cos \theta & \sin \theta\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}\sin \theta & -\cos \theta \\ \cos \theta & -\sin \theta\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}-\cos \theta & \sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$**

**Detailed Solution:**

We have $A=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right] \Rightarrow \operatorname{adj} A=\left[\begin{array}{cc}-\cos \theta & \sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
$|A|=\left|\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right|=-\cos ^{2} \theta-\sin ^{2} \theta=-\left(\cos ^{2} \theta+\sin ^{2} \theta\right)=-1$
$\therefore A^{-1}=\frac{1}{(-1)}\left[\begin{array}{cc}-\cos \theta & \sin \theta \\ \sin \theta & \cos \theta\end{array}\right]=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$

</details>

---

### Q90. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right], B=\left[\begin{array}{ll}1 & 0 \\ 3 & 1\end{array}\right]$, then $(A B)^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}2 & -3 \\ 7 & 11\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}2 & -3 \\ -7 & -11\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}-2 & -3 \\ -7 & 11\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} A B &=\left[\begin{array}{ll}2 & 3 \\ 1 & 2\end{array}\right]\left[\begin{array}{ll}1 & 0 \\ 3 & 1\end{array}\right]=\left[\begin{array}{cc}11 & 3 \\ 7 & 2\end{array}\right] \Rightarrow|A B|=\left|\begin{array}{cc}11 & 3 \\ 7 & 2\end{array}\right|=22-21=1 \\ \operatorname{adj}(A B) &=\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right] \Rightarrow(A B)^{-1}=\left[\begin{array}{cc}2 & -3 \\ -7 & 11\end{array}\right] \end{aligned}$

</details>

---

### Q91. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following matrix is invertible?
$A_{1}=\left[\begin{array}{ll}4 & 2 \\ 2 & 1\end{array}\right]$
$A_{2}=\left[\begin{array}{ccc}-1 & -2 & 3 \\ 4 & 5 & 7 \\ 2 & 4 & -6\end{array}\right]$
$A_{3}=\left[\begin{array}{lll}1 & 0 & 0 \\ 5 & 2 & 1 \\ 7 & 2 & 1\end{array}\right]$
$A_{4}=\left[\begin{array}{lll}1 & 0 & 1 \\ 0 & 2 & 3 \\ 1 & 2 & 1\end{array}\right]$

**Options:**

- **(A)** $A_{1}$
- **(B)** $A_{3}$
- **(C)** $A_{4}$
- **(D)** $A_{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $A_{4}$**

**Detailed Solution:**

Any Matrix is said to be invertiable only if $|\mathrm{A}| \neq 0$ 
Here
$\left|A_{4}\right|=\left|\begin{array}{lll}
1 & 0 & 1 \\
0 & 2 & 3 \\
1 & 2 & 1
\end{array}\right| \quad=(-4)+1(-2)=-6 \neq 0$

</details>

---

### Q92. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$, such that $A^{2}-4 A+3 I=0$, then $A^{-1}=$

**Options:**

- **(A)** $\frac{-1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$
- **(B)** $\frac{-1}{3}\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right]$
- **(C)** $\frac{1}{3}\left[\begin{array}{cc}-2 & -1 \\ 1 & -2\end{array}\right]$
- **(D)** $\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$**

**Detailed Solution:**

$A=\left[\begin{array}{cc}2 & -1 \\ -1 & 2\end{array}\right] \quad \Rightarrow|A|=4-1=3 \quad$ and $(\operatorname{adj} A)=\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$
$\therefore A^{-1} \quad=\frac{1}{3}\left[\begin{array}{ll}2 & 1 \\ 1 & 2\end{array}\right]$

</details>

---

### Q93. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>A</mi></math> is non-singular matrix such that <math><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>2</mn><mi>I</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>4</mn><mi>I</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> , then <math><mi>A</mi><mo>+</mo><mn>8</mn><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mi>I</mi></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mn>3</mn><mi>I</mi></math>
- **(D)** <math><mn>6</mn><mi>I</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>6</mn><mi>I</mi></math>**

**Detailed Solution:**

Given: <math><mi>A</mi></math> is non-singular matrix then <math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>≠</mo><mn>0</mn></math>  
Also <math><mi></mi><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>2</mn><mi>I</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>4</mn><mi>I</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>6</mn><mi>A</mi><mo>+</mo><mn>8</mn><mi>I</mi><mo>=</mo><mn>0</mn><mo> </mo><mo> </mo><mo> </mo><mo> </mo><mi mathvariant="normal">m</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal"></mi><mi mathvariant="normal">b</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal"></mi><msup><mrow><mi>A</mi></mrow><mrow><mo>–</mo><mn>1</mn></mrow></msup></math> both the side 
<math><mi mathvariant="normal">W</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal"></mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">v</mi><mi mathvariant="normal">e</mi><mi></mi><mi>A</mi><mo>+</mo><mn>8</mn><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>6</mn><mi>I</mi></math>

</details>

---

### Q94. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> and <math><mi>A</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>,</mo></math> then <math><mi>x</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0</mn></math>**

**Detailed Solution:**

Given <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>  
Then <math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>x</mi></mtd></mtr></mtable></mrow></mfenced><mo> </mo></math>  
Given <math><mi>A</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn></math>

</details>

---

### Q95. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If is non-singular matrix and <math><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>l</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mi>l</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> then <math><mi>A</mi><mo>+</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mo>…</mo><mo>…</mo></math>

**Options:**

- **(A)** 2A
- **(B)** 0
- **(C)** <math><mi>l</mi></math>
- **(D)** 3 <math><mi>l</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2A**

**Detailed Solution:**

We have, A is non-singular matrix 
<math><mo>∴</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
and <math><mfenced separators="|"><mrow><mi>A</mi><mo>+</mo><mi>l</mi></mrow></mfenced><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mi>l</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>0</mn></math>  
<math><mo>&#8658;</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>l</mi></math>  
<math><mo>&#8658;</mo><mi>A</mi><mo>.</mo><mi>A</mi><mo>=</mo><mi>l</mi><mo>&#8658;</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>A</mi></math>  
<math><mo>∴</mo><mi>A</mi><mo>+</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>A</mi><mo>+</mo><mi>A</mi><mo>=</mo><mn>2</mn><mi>A</mi></math>

</details>

---

### Q96. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>ω</mi></math> is a complex cube root of unity and <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> then <math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

Given, <math><mi>ω</mi></math> is a complex cube root of unity
<math><mo>∴</mo><mtext>  </mtext><msup><mrow><mi>ω</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mn>1</mn></math>
Given matrix A can be written as <math><mi>A</mi><mo>=</mo><mi>l</mi><mi>A</mi></math>
<math><mo>⇒</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mi>A</mi></math>
On apply <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>→</mo><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>→</mo><mi>ω</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> , we get
<math><mo>⇒</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>3</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>3</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mi>A</mi></math>
<math><mo>⇒</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mi>A</mi></math>
<math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><msup><mrow><mi>ω</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>ω</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q97. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced></math> then <math><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>A</mi></mrow></mfenced><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo></math>

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<math> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>A</mi> <mn>2</mn> </msup> <mo>−</mo><mn>5</mn><mi>A</mi></mrow> <mo>)</mo></mrow><msup> <mi>A</mi> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> </mrow> </math>
<math> <mrow> <mo>=</mo><msup> <mi>A</mi> <mn>2</mn> </msup> <mo>⋅</mo><msup> <mi>A</mi> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> <mo>−</mo><mn>5</mn><mi>A</mi><msup> <mi>A</mi> <mrow> <mo>−</mo><mn>1</mn></mrow> </msup> </mrow> </math>
<math> <mrow> <mo>=</mo><mi>A</mi><mo>−</mo><mn>5</mn><mi>I</mi></mrow> </math>
<math> <mrow> <mo>=</mo><mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mn>3</mn> </mtd> </mtr> <mtr> <mtd> <mrow> <mo>−</mo><mn>1</mn></mrow> </mtd> <mtd> <mn>1</mn> </mtd> <mtd> <mn>2</mn> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mn>4</mn> </mtd> </mtr> </mtable></mrow> <mo>]</mo></mrow><mo>−</mo><mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mn>5</mn> </mtd> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>5</mn> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mn>0</mn> </mtd> <mtd> <mn>5</mn> </mtd> </mtr> </mtable></mrow> <mo>]</mo></mrow></mrow> </math>
<math> <mrow> <mo>=</mo><mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mrow> <mo>−</mo><mn>4</mn></mrow> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mn>3</mn> </mtd> </mtr> <mtr> <mtd> <mrow> <mo>−</mo><mn>1</mn></mrow> </mtd> <mtd> <mrow> <mo>−</mo><mn>4</mn></mrow> </mtd> <mtd> <mn>2</mn> </mtd> </mtr> <mtr> <mtd> <mn>1</mn> </mtd> <mtd> <mn>2</mn> </mtd> <mtd> <mrow> <mo>−</mo><mn>1</mn></mrow> </mtd> </mtr> </mtable></mrow> <mo>]</mo></mrow></mrow> </math>

</details>

---

### Q98. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

If the inverse of the matrix <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>α</mi></mtd><mtd><mn>14</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math> does not exist then the value of <math><mi>α</mi></math> is

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mo>-</mo><mn>1</mn></math>
- **(C)** <math><mn>0</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>2</mn></math>**

**Detailed Solution:**

<math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>α</mi></mtd><mtd><mn>14</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math> 
 <math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>7</mn><mi>α</mi><mo>+</mo><mn>14</mn></math> 
 <math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>  does not exists if  <math><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mi> </mi><mn>0</mn></math> 
 <math><mo>⇒</mo><mi> </mi><mn>7</mn><mi>α</mi><mo>+</mo><mn>14</mn><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>α</mi><mo>=</mo><mo>-</mo><mn>2</mn></math>

</details>

---

### Q99. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

The inverse of the matrix <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> is

**Options:**

- **(A)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

For <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> <math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math>
Now<math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mo>|</mo><mi> </mi><mi>A</mi><mi> </mi><mo>|</mo></mrow></mfrac><mi>A</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q100. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If Matrix <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math> such that <math><mi>A</mi><mi>X</mi><mo>=</mo><mi>I</mi><mo>,</mo></math> then <math><mi>X</mi><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

Given <math><mi>A</mi><mi> </mi><mi>X</mi><mo>=</mo><mi>I</mi></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>X</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math><math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mfenced close="|" open="|" separators=","> <mrow> <mtext>A</mtext> </mrow> </mfenced> </mrow> </mfrac> <mtext>adj A</mtext> </mrow> </math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>X</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi>X</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q101. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mi>,</mi><mi> </mi><mi>B</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> then <math> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <msup> <mi>B</mi> <mrow> <mo>−</mo><mn>1</mn> </mrow> </msup> <msup> <mi>A</mi> <mrow> <mo>−</mo><mn>1</mn> </mrow> </msup> </mrow> <mo>)</mo></mrow> </mrow> <mrow> <mo>−</mo><mn>1</mn> </mrow> </msup> <mo>=</mo> </mrow> </math>

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<math><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>B</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
<math><mo>=</mo><mi>A</mi><mi>B</mi></math>
<math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q102. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

The multiplicative inverse of $A=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
is

**Options:**

- **(A)** $\left[\begin{array}{cc}-\cos \theta & \sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}-\cos \theta & -\sin \theta \\ \sin \theta & -\cos \theta\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}\cos \theta & \sin \theta \\ \sin \theta & -\cos \theta\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{cc}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$**

**Detailed Solution:**

$|A|=\cos ^{2} \theta+\sin ^{2} \theta=1$
$$
\begin{array}{l}
\operatorname{adj}(A)=\left[\begin{array}{ll}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right] \\
A^{-1}=\frac{\operatorname{adj}(A)}{|A|}=\left[\begin{array}{ll}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{array}\right]
\end{array}
$$

</details>

---

### Q103. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$, then the inverse of $A$
is

**Options:**

- **(A)** $\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}-\cos \theta & \sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}\sin \theta & -\cos \theta \\ \cos \theta & -\sin \theta\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}-\sin \theta & -\cos \theta \\ -\cos \theta & \sin \theta\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ -\sin \theta & -\cos \theta\end{array}\right]$**

**Detailed Solution:**

$$
\begin{array}{l}
\quad|A|=\left|\begin{array}{cc}
\cos \theta & -\sin \theta \\
-\sin \theta & -\cos \theta
\end{array}\right|=-1 \\
\operatorname{adj}(A)=\left[\begin{array}{cc}
-\cos \theta & \sin \theta \\
\sin \theta & \cos \theta
\end{array}\right] \\
\therefore \quad A^{-1}=\left|\begin{array}{cc}
\cos \theta & -\sin \theta \\
-\sin \theta & -\cos \theta
\end{array}\right|=A
\end{array}
$$

</details>

---

### Q104. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The inverse matrix of $\left[\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 1 & 1\end{array}\right]$ is

**Options:**

- **(A)** $\left[\begin{array}{rrr}\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ -4 & 3 & -1 \\ \frac{5}{2} & -\frac{3}{2} & \frac{1}{2}\end{array}\right]$
- **(B)** $\left[\begin{array}{rrr}\frac{1}{2} & -4 & \frac{5}{2} \\ 1 & -6 & 3 \\ 1 & 2 & -1\end{array}\right]$
- **(C)** $\frac{1}{2}\left[\begin{array}{lll}1 & 2 & 3 \\ 3 & 2 & 1 \\ 4 & 2 & 3\end{array}\right]$
- **(D)** $\frac{1}{2}\left[\begin{array}{rrr}1 & -1 & -1 \\ -8 & 6 & -2 \\ 5 & -3 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{rrr}\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ -4 & 3 & -1 \\ \frac{5}{2} & -\frac{3}{2} & \frac{1}{2}\end{array}\right]$**

**Detailed Solution:**

Let 
$\begin{aligned} A &=\left[\begin{array}{lll}0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & 1 & 1\end{array}\right] \\ \therefore \begin{aligned}|A| &=0-1(1-9)+2(1-6) \\ &=8-10=-2 \neq 0 \\ \operatorname{adj}(A) &=\left[\begin{array}{rrr}-1 & 1 & -1 \\ 8 & -6 & 2 \\ -5 & 3 & -1\end{array}\right] \\ \therefore A^{-1} &=\frac{\operatorname{adj}(A)}{|A|} \\ &=\frac{1}{-2}\left[\begin{array}{rrr}-1 & 1 & -1 \\ 8 & -6 & 2 \\ -5 & 3 & -1\end{array}\right] \\ &=\left[\begin{array}{rrrr}1 / 2 & -1 / 2 & 1 / 2 \\ -4 & 3 & -1 \\ 5 / 2 & -3 / 2 & 1 / 2\end{array}\right] \end{aligned} \end{aligned}$

</details>

---

