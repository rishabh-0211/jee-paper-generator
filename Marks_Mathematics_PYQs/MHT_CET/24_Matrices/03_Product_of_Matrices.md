# MHT CET Mathematics - Matrices

## Topic 3: Product of Matrices

**Total Questions:** 20

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $X = \begin{bmatrix} 4 & 2 \\ -1 & 3 \end{bmatrix}$, $Y = \begin{bmatrix} -1 & 2 \\ 1 & -3 \end{bmatrix}$, then $(XY)^{-1}$ is equal to

**Options:**

- **(A)** $\begin{bmatrix} \dfrac{11}{14} & \dfrac{-2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$
- **(B)** $\begin{bmatrix} \dfrac{-11}{14} & \dfrac{2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$
- **(C)** $\begin{bmatrix} \dfrac{-11}{14} & \dfrac{-2}{14} \\ \dfrac{4}{14} & \dfrac{-2}{14} \end{bmatrix}$
- **(D)** $\begin{bmatrix} \dfrac{-11}{14} & \dfrac{-2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\begin{bmatrix} \dfrac{-11}{14} & \dfrac{-2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$**

**Detailed Solution:**

First, we find the product of matrices $X$ and $Y$:

$XY = \begin{bmatrix} 4 & 2 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} -1 & 2 \\ 1 & -3 \end{bmatrix}$

$XY = \begin{bmatrix} 4(-1) + 2(1) & 4(2) + 2(-3) \\ -1(-1) + 3(1) & -1(2) + 3(-3) \end{bmatrix}$

$XY = \begin{bmatrix} -2 & 2 \\ 4 & -11 \end{bmatrix}$

Next, we find the determinant of $XY$:

$|XY| = (-2)(-11) - (2)(4) = 22 - 8 = 14$

The adjugate of $XY$ is obtained by interchanging the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(XY) = \begin{bmatrix} -11 & -2 \\ -4 & -2 \end{bmatrix}$

The inverse of $XY$ is given by $(XY)^{-1} = \dfrac{1}{|XY|} \text{adj}(XY)$:

$(XY)^{-1} = \dfrac{1}{14} \begin{bmatrix} -11 & -2 \\ -4 & -2 \end{bmatrix} = \begin{bmatrix} \dfrac{-11}{14} & \dfrac{-2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$

Answer: $\begin{bmatrix} \dfrac{-11}{14} & \dfrac{-2}{14} \\ \dfrac{-4}{14} & \dfrac{-2}{14} \end{bmatrix}$

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$, then which of the following is not true?

**Options:**

- **(A)** $A^{-1} = A^2$
- **(B)** $A^2$ is a triangular matrix.
- **(C)** $A$ is a non-singular matrix.
- **(D)** $A^3$ is an identity matrix.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $A^2$ is a triangular matrix.**

**Detailed Solution:**

Evaluating the determinant of $A$:

$|A| = 1(0 - 0) - (-1)(0 - 0) + 1(0 - (-1)) = 1$

Since $|A| \neq 0$, $A$ is a non-singular matrix.

Evaluating $A^2$:

$A^2 = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -1 & 2 \\ 1 & -1 & 1 \end{bmatrix}$

Since elements both above and below the principal diagonal are non-zero, $A^2$ is not a triangular matrix.

Evaluating $A^3$:

$A^3 = A^2 A = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -1 & 2 \\ 1 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$

Since $A^3 = I$, multiplying both sides by $A^{-1}$ gives $A^2 = A^{-1}$.

Therefore, the only incorrect statement is that $A^2$ is a triangular matrix.

Answer: $A^2$ is a triangular matrix.

</details>

---

### Q3. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} -\dfrac{1}{2} & -\dfrac{\sqrt{3}}{2} \\ \dfrac{\sqrt{3}}{2} & -\dfrac{1}{2} \end{bmatrix}$, the value of $|\text{Adj}(A^{2026})|$ is equal to:

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $-\dfrac{1}{2}$
- **(D)** $\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

The determinant of matrix $A$ is given by:

$|A| = \begin{vmatrix} -\dfrac{1}{2} & -\dfrac{\sqrt{3}}{2} \\ \dfrac{\sqrt{3}}{2} & -\dfrac{1}{2} \end{vmatrix} = \left(-\dfrac{1}{2}\right)\left(-\dfrac{1}{2}\right) - \left(-\dfrac{\sqrt{3}}{2}\right)\left(\dfrac{\sqrt{3}}{2}\right)$

$|A| = \dfrac{1}{4} + \dfrac{3}{4} = 1$

Using the property of determinants, $|A^k| = |A|^k$

$|A^{2026}| = (1)^{2026} = 1$

For a matrix $M$ of order $n$, the determinant of its adjoint is given by $|\text{Adj}(M)| = |M|^{n-1}$

Since $A$ is a $2 \times 2$ matrix, $n = 2$

$|\text{Adj}(A^{2026})| = |A^{2026}|^{2-1} = |A^{2026}| = 1$

Answer: $1$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 2 & 3 \\ 3 & a & 1 \end{bmatrix}$ and $A^{-1} = \begin{bmatrix} \dfrac{1}{2} & -\dfrac{1}{2} & \dfrac{1}{2} \\ -4 & 3 & c \\ \dfrac{5}{2} & -\dfrac{3}{2} & \dfrac{1}{2} \end{bmatrix}$, then ...

**Options:**

- **(A)** $a = 1,\,c = 1$
- **(B)** $a = 1,\,c = -1$
- **(C)** $a = 1,\,c = 2$
- **(D)** $a = -1,\,c = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a = 1,\,c = -1$**

**Detailed Solution:**

Using the property $A A^{-1} = I$, the product of the matrix $A$ and its inverse $A^{-1}$ must yield the identity matrix.

Equating the element in the first row and third column of $A A^{-1}$ to $0$:

$0 \times \dfrac{1}{2} + 1 \times c + 2 \times \dfrac{1}{2} = 0$

$c + 1 = 0 \Rightarrow c = -1$

Equating the element in the third row and first column of $A A^{-1}$ to $0$:

$3 \times \dfrac{1}{2} + a \times (-4) + 1 \times \dfrac{5}{2} = 0$

$\dfrac{3}{2} - 4a + \dfrac{5}{2} = 0$

$4 - 4a = 0 \Rightarrow a = 1$

Therefore, $a = 1$ and $c = -1$.

Answer: $a = 1,\,c = -1$

</details>

---

### Q5. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 3 & 2 & 6 \\ 1 & 1 & 2 \\ 2 & 2 & 5 \end{bmatrix}$, $B = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$ such that $XA = B^T$ and $A^{-1}Y = B$, then $XY = $

**Options:**

- **(A)** $[-1]$
- **(B)** $[1]$
- **(C)** $[-2]$
- **(D)** $[2]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $[2]$**

**Detailed Solution:**

Given $XA = B^T$

Post-multiplying by $A^{-1}$, we get $X = B^T A^{-1}$

Given $A^{-1}Y = B$

Pre-multiplying by $A$, we get $Y = AB$

Now, $XY = (B^T A^{-1})(AB)$

Using the associative property of matrix multiplication, $XY = B^T (A^{-1}A) B$

$XY = B^T I B = B^T B$

Substituting the given matrix $B$, we get:

$XY = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$

$XY = [1 \times 1 + 0 \times 0 + 1 \times 1] = [2]$

Answer: $[2]$

</details>

---

### Q6. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 2 & 3 \\ 5 & -2 \end{bmatrix}$, $B^{-1} = \begin{bmatrix} \dfrac{1}{5} & \dfrac{2}{5} \\ \dfrac{2}{5} & -\dfrac{1}{5} \end{bmatrix}$, then $(AB)^{-1} = $

**Options:**

- **(A)** $\dfrac{1}{95}\begin{bmatrix} 8 & -1 \\ -1 & 12 \end{bmatrix}$
- **(B)** $\dfrac{1}{95}\begin{bmatrix} 12 & -1 \\ -1 & 8 \end{bmatrix}$
- **(C)** $\dfrac{1}{95}\begin{bmatrix} -12 & 1 \\ 1 & -8 \end{bmatrix}$
- **(D)** $\dfrac{1}{95}\begin{bmatrix} -8 & 1 \\ 1 & -12 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{95}\begin{bmatrix} 12 & -1 \\ -1 & 8 \end{bmatrix}$**

**Detailed Solution:**

Using the reversal law for the inverse of a product of matrices, we have:

$(AB)^{-1} = B^{-1}A^{-1}$

First, we find the inverse of matrix $A$. The determinant of $A$ is:

$|A| = (2)(-2) - (3)(5) = -4 - 15 = -19$

The adjugate of $A$ is obtained by swapping the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(A) = \begin{bmatrix} -2 & -3 \\ -5 & 2 \end{bmatrix}$

Thus, $A^{-1}$ is given by:

$A^{-1} = \dfrac{1}{|A|} \text{adj}(A) = \dfrac{1}{-19} \begin{bmatrix} -2 & -3 \\ -5 & 2 \end{bmatrix} = \dfrac{1}{19} \begin{bmatrix} 2 & 3 \\ 5 & -2 \end{bmatrix}$

We are given $B^{-1} = \begin{bmatrix} \dfrac{1}{5} & \dfrac{2}{5} \\ \dfrac{2}{5} & -\dfrac{1}{5} \end{bmatrix} = \dfrac{1}{5} \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix}$.

Now, we compute $(AB)^{-1}$ by multiplying $B^{-1}$ and $A^{-1}$:

$(AB)^{-1} = B^{-1}A^{-1} = \left( \dfrac{1}{5} \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix} \right) \left( \dfrac{1}{19} \begin{bmatrix} 2 & 3 \\ 5 & -2 \end{bmatrix} \right)$

$(AB)^{-1} = \dfrac{1}{95} \begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 5 & -2 \end{bmatrix}$

Performing the matrix multiplication:

$(AB)^{-1} = \dfrac{1}{95} \begin{bmatrix} (1)(2) + (2)(5) & (1)(3) + (2)(-2) \\ (2)(2) + (-1)(5) & (2)(3) + (-1)(-2) \end{bmatrix}$

$(AB)^{-1} = \dfrac{1}{95} \begin{bmatrix} 2 + 10 & 3 - 4 \\ 4 - 5 & 6 + 2 \end{bmatrix} = \dfrac{1}{95} \begin{bmatrix} 12 & -1 \\ -1 & 8 \end{bmatrix}$

Answer: $\dfrac{1}{95}\begin{bmatrix} 12 & -1 \\ -1 & 8 \end{bmatrix}$

</details>

---

### Q7. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 3 & 1 \\ -1 & 2 \end{bmatrix}$, $C = \begin{bmatrix} 7 & 3 \\ 0 & 6 \end{bmatrix}$ and $AB = C$, then the inverse of matrix B is

**Options:**

- **(A)** $\dfrac{1}{42}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix}$
- **(B)** $\dfrac{1}{6}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix}$
- **(C)** $\dfrac{1}{42}\begin{bmatrix} 6 & 3 \\ -1 & 2 \end{bmatrix}$
- **(D)** $\dfrac{1}{6}\begin{bmatrix} 7 & 3 \\ -1 & 3 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{6}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix}$**

**Detailed Solution:**

Given $AB = C$

Taking inverse on both sides, we get $(AB)^{-1} = C^{-1}$

$B^{-1}A^{-1} = C^{-1}$

Multiplying both sides by $A$ on the right, we get $B^{-1} = C^{-1}A$

We have $C = \begin{bmatrix} 7 & 3 \\ 0 & 6 \end{bmatrix}$

$|C| = 7(6) - 3(0) = 42$

$C^{-1} = \dfrac{1}{42}\begin{bmatrix} 6 & -3 \\ 0 & 7 \end{bmatrix}$

Now, $B^{-1} = \dfrac{1}{42}\begin{bmatrix} 6 & -3 \\ 0 & 7 \end{bmatrix}\begin{bmatrix} 3 & 1 \\ -1 & 2 \end{bmatrix}$

$B^{-1} = \dfrac{1}{42}\begin{bmatrix} 18+3 & 6-6 \\ 0-7 & 0+14 \end{bmatrix}$

$B^{-1} = \dfrac{1}{42}\begin{bmatrix} 21 & 0 \\ -7 & 14 \end{bmatrix}$

$B^{-1} = \dfrac{7}{42}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix} = \dfrac{1}{6}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix}$

Answer: $\dfrac{1}{6}\begin{bmatrix} 3 & 0 \\ -1 & 2 \end{bmatrix}$

</details>

---

### Q8. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$, then the matrix $A^{-3}$ when $\theta = \dfrac{\pi}{6}$ is equal to...

**Options:**

- **(A)** $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$

Using the property of rotation matrices, $A^n = \begin{bmatrix} \cos n\theta & -\sin n\theta \\ \sin n\theta & \cos n\theta \end{bmatrix}$ for any integer $n$.

For $n = -3$, we have:

$A^{-3} = \begin{bmatrix} \cos(-3\theta) & -\sin(-3\theta) \\ \sin(-3\theta) & \cos(-3\theta) \end{bmatrix}$

Since $\cos(-x) = \cos x$ and $\sin(-x) = -\sin x$, this simplifies to:

$A^{-3} = \begin{bmatrix} \cos 3\theta & \sin 3\theta \\ -\sin 3\theta & \cos 3\theta \end{bmatrix}$

Substituting $\theta = \dfrac{\pi}{6}$, we get $3\theta = \dfrac{\pi}{2}$:

$A^{-3} = \begin{bmatrix} \cos\dfrac{\pi}{2} & \sin\dfrac{\pi}{2} \\ -\sin\dfrac{\pi}{2} & \cos\dfrac{\pi}{2} \end{bmatrix}$

$A^{-3} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$

Answer: $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$

</details>

---

### Q9. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\left[\begin{array}{ll}x & 1 \\ 1 & 0\end{array}\right], x \in \mathbb{R}^{+}$and $\mathrm{A}^4=\left[\mathrm{a}_{\mathrm{ij}}\right]_2$.
If $\mathrm{a}_{11}=109$, then $\left(\mathrm{A}^4\right)^{-1}=$

**Options:**

- **(A)** $\left[\begin{array}{ll}109 & 33 \\ 33 & 10\end{array}\right]$.
- **(B)** $\left[\begin{array}{ll}10 & 33 \\ 33 & 10\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}10 & 33 \\ 33 & 109\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}10 & -33 \\ -33 & 109\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}10 & -33 \\ -33 & 109\end{array}\right]$**

**Detailed Solution:**

Given $A = \begin{bmatrix} x & 1 \\ 1 & 0 \end{bmatrix}$.

First, we find $A^2$:
$A^2 = \begin{bmatrix} x & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} x^2+1 & x \\ x & 1 \end{bmatrix}$

Next, we find $A^4 = (A^2)^2$:
$A^4 = \begin{bmatrix} x^2+1 & x \\ x & 1 \end{bmatrix} \begin{bmatrix} x^2+1 & x \\ x & 1 \end{bmatrix} = \begin{bmatrix} (x^2+1)^2 + x^2 & x(x^2+1) + x \\ x(x^2+1) + x & x^2 + 1 \end{bmatrix}$

We are given that the first element of $A^4$ is $a_{11} = 109$.
$(x^2+1)^2 + x^2 = 109$
$x^4 + 2x^2 + 1 + x^2 = 109$
$x^4 + 3x^2 - 108 = 0$
$(x^2 + 12)(x^2 - 9) = 0$

Since $x \in \mathbb{R}^{+}$, $x^2$ must be positive, so $x^2 = 9$, which gives $x = 3$.

Now, substituting $x = 3$ into the elements of $A^4$:
$a_{11} = 109$
$a_{12} = 3(9+1) + 3 = 33$
$a_{21} = 33$
$a_{22} = 9 + 1 = 10$

Thus, $A^4 = \begin{bmatrix} 109 & 33 \\ 33 & 10 \end{bmatrix}$.

The determinant of $A^4$ is $|A^4| = (109)(10) - (33)(33) = 1090 - 1089 = 1$.

The inverse of a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is $\dfrac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.

Therefore, $(A^4)^{-1} = \dfrac{1}{1} \begin{bmatrix} 10 & -33 \\ -33 & 109 \end{bmatrix} = \begin{bmatrix} 10 & -33 \\ -33 & 109 \end{bmatrix}$.

Answer: $\left[\begin{array}{cc}10 & -33 \\ -33 & 109\end{array}\right]$

</details>

---

### Q10. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let A and B be $3 \times 3$ real matrices such that A is symmetric matrix and $B$ is skew-symmetric matrix. Then the system of linear equations $\left(A^2 B^2-B^2 A^2\right) X=0$. where $X$ is $3 \times 1$ column matrix of unknown variables and O is a $3 \times 1$ null matrix, has

**Options:**

- **(A)** a unique solution
- **(B)** exactly two solutions
- **(C)** no solution
- **(D)** infinitely many solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) infinitely many solutions**

**Detailed Solution:**

Let $M = A^2 B^2 - B^2 A^2$.

Taking the transpose of $M$, we get:

$M^T = (A^2 B^2 - B^2 A^2)^T$

$M^T = (A^2 B^2)^T - (B^2 A^2)^T$

$M^T = (B^2)^T (A^2)^T - (A^2)^T (B^2)^T$

Since $A$ is a symmetric matrix, $A^T = A$, which implies $(A^2)^T = A^2$.

Since $B$ is a skew-symmetric matrix, $B^T = -B$, which implies $(B^2)^T = (-B)^2 = B^2$.

Substituting these into the equation for $M^T$:

$M^T = B^2 A^2 - A^2 B^2 = -(A^2 B^2 - B^2 A^2) = -M$

This shows that $M$ is a skew-symmetric matrix. The order of $M$ is $3 \times 3$, which is an odd order.

The determinant of a skew-symmetric matrix of odd order is always zero. Therefore, $|M| = 0$.

The given system of equations is $MX = 0$, which is a homogeneous system of linear equations. Since the determinant of the coefficient matrix $M$ is zero, the system has non-trivial solutions.

A homogeneous system of linear equations with non-trivial solutions always has infinitely many solutions.

Answer: infinitely many solutions

</details>

---

### Q11. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Suppose A is any $3 \times 3$ non-singular matrix and $(\mathrm{A}-3 \mathrm{I})(\mathrm{A}-5 \mathrm{I})=0$ where $\mathrm{I}=\mathrm{I}_3$ and $\mathrm{O}=\mathrm{O}_3$. Here $\mathrm{O}_3$ represent zero matrix of order 3 and $\mathrm{I}_3$ is an identity matrix of order 3 . If $\alpha \mathrm{A}+\beta \mathrm{A}^{-1}=4 \mathrm{I}$, then $\alpha+\beta$ is equal to

**Options:**

- **(A)** 13
- **(B)** 7
- **(C)** 12
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8**

**Detailed Solution:**

Given the equation $(A - 3I)(A - 5I) = O$

Expanding the product, we get:

$A^2 - 5A - 3A + 15I = O$

$A^2 - 8A + 15I = O$

Since $A$ is a non-singular matrix, its inverse $A^{-1}$ exists. Multiplying the entire equation by $A^{-1}$, we obtain:

$A - 8I + 15A^{-1} = O$

$A + 15A^{-1} = 8I$

To match the given form $\alpha A + \beta A^{-1} = 4I$, we divide the equation by $2$:

$\dfrac{1}{2}A + \dfrac{15}{2}A^{-1} = 4I$

Comparing this with $\alpha A + \beta A^{-1} = 4I$, we find:

$\alpha = \dfrac{1}{2}$ and $\beta = \dfrac{15}{2}$

Therefore, the sum $\alpha + \beta$ is:

$\alpha + \beta = \dfrac{1}{2} + \dfrac{15}{2} = \dfrac{16}{2} = 8$

Answer: 8

</details>

---

### Q12. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the system $x-y+z=4,2 x+y-3 z=0$, $x+y+z=2$, the values of $x, y, z$ respectively are given by

**Options:**

- **(A)** $2,1,1$
- **(B)** $2,-1,1$
- **(C)** $2,1,-1$
- **(D)** $-2,1,1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2,-1,1$**

**Detailed Solution:**

The given system of equations is:
$x - y + z = 4$
$2x + y - 3z = 0$
$x + y + z = 2$

Subtracting the first equation from the third equation:
$(x + y + z) - (x - y + z) = 2 - 4$
$2y = -2$
$y = -1$

Substituting $y = -1$ into the first equation:
$x - (-1) + z = 4$
$x + z = 3$

Substituting $y = -1$ into the second equation:
$2x + (-1) - 3z = 0$
$2x - 3z = 1$

Multiplying $x + z = 3$ by $3$ and adding to $2x - 3z = 1$:
$3(x + z) + (2x - 3z) = 3(3) + 1$
$3x + 3z + 2x - 3z = 9 + 1$
$5x = 10$
$x = 2$

Substituting $x = 2$ into $x + z = 3$:
$2 + z = 3$
$z = 1$

The values of $x, y, z$ are $2, -1, 1$ respectively.

Answer: $2,-1,1$

</details>

---

### Q13. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{cc}2 \mathrm{a} & -3 \mathrm{~b} \\ 3 & 2\end{array}\right]$ and $\mathrm{A} \cdot \operatorname{adj} \mathrm{A}=\mathrm{AA}^{\mathrm{T}}$, then $2 a+3 b$ is

**Options:**

- **(A)** $-1$
- **(B)** $1$
- **(C)** $5$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{cc}2 a & -3 b \\ 3 & 2\end{array}\right] \\ & A \cdot \operatorname{adj} A=\left[\begin{array}{cc}2 a & -3 b \\ 3 & 2\end{array}\right]\left[\begin{array}{cc}2 & 3 b \\ -3 & 2 a\end{array}\right] \\ & =\left[\begin{array}{cc}4 a+9 b & 0 \\ 0 & 9 b+4 a\end{array}\right] \\ & A \cdot A^T=\left[\begin{array}{cc}2 a & -3 b \\ 3 & 2\end{array}\right]\left[\begin{array}{cc}2 a & 3 \\ -3 b & 2\end{array}\right] \\ & =\left[\begin{array}{cc}4 a^2+9 b^2 & 6 a-6 b \\ 6 a-6 b & 13\end{array}\right] \\ & \therefore \quad \mathrm{A} \cdot \operatorname{adj} \mathrm{A}=\mathrm{A} \cdot \mathrm{A}^{\mathrm{T}} \\ & \Rightarrow\left[\begin{array}{cc}4 a+9 b & 0 \\ 0 & 4 a+9 b\end{array}\right]=\left[\begin{array}{cc}4 a^2+9 b^2 & 6 a-6 b \\ 6 a-6 b & 13\end{array}\right] \\ & \Rightarrow \mathrm{a}=\mathrm{b} \text { and } 4 \mathrm{a}+9 \mathrm{~b}=13 \\ & \Rightarrow \mathrm{a}=\mathrm{b}=1 \\ & \Rightarrow 2 a+3 b=5 \\ & \end{aligned}$

</details>

---

### Q14. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}=\left[\begin{array}{ccc}1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & -2 & 1\end{array}\right], \mathrm{B}=\left[\begin{array}{c}6 \\ 11 \\ 0\end{array}\right]$ and $\mathrm{X}-\left[\begin{array}{l}\mathrm{a} \\ \mathrm{b} \\ \mathrm{c}\end{array}\right]$, if $\mathrm{AX}=\mathrm{B}$, then the value of $2 \mathrm{a}+\mathrm{b}+2 \mathrm{c}$ is

**Options:**

- **(A)** 10
- **(B)** 8
- **(C)** 6
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 10**

**Detailed Solution:**

$\begin{aligned} & \mathrm{AX}=\mathrm{B} \\ & {\left[\begin{array}{ccc}1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & -2 & 1\end{array}\right]\left[\begin{array}{l}a \\ b \\ c\end{array}\right]=\left[\begin{array}{c}6 \\ 11 \\ 0\end{array}\right]} \\ & \therefore \quad a+b+c=6 ...(i)\\ & \mathrm{~b}+3 \mathrm{c}=11 ...(ii)\\ & a-2 b+c=0 \\ & \text { i.e., } a+c=2 b ...(iii)\\ & \text { From (i) and (ii), we get } b=2 \\ & \text { From (ii), } c=3 \\ & \text { From (i), } a=1 \\ & \therefore \quad 2 \mathrm{a}+\mathrm{b}+2 \mathrm{c}=2(1)+2+2(3)=10 \\ & \end{aligned}$

</details>

---

### Q15. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}$ is non-singular matrix of order 3 such that $(A-2 \mathrm{I})(A-4 \mathrm{I})=0$, then $\frac{1}{6} A+\frac{4}{3} A^{-1}$ is (where I is a unit matrix of order 3 and 0 is a null matrix of order 3)

**Options:**

- **(A)** 6I
- **(B)** I
- **(C)** 0
- **(D)** 2I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) I**

**Detailed Solution:**

$\begin{aligned} & (A-2 \mathrm{I})(A-4 \mathrm{I})=0 \\ & \Rightarrow A^2-6 A+8 \mathrm{I}=0 \\ & \Rightarrow A^2+8 \mathrm{I}=6 A \\ & \Rightarrow A^2 A^{-1}+8 \mathrm{I} A^{-1}=6 A A^{-1} \\ & \Rightarrow A+8 A^{-1}=6 \mathrm{I} \\ & \Rightarrow \frac{1}{6} A+\frac{4}{3} A^{-1}=\mathrm{I}\end{aligned}$

</details>

---

### Q16. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If matrix $\mathrm{A}=\left[\begin{array}{ll}1 & 2 \\ 4 & 3\end{array}\right]$ is such that $\mathrm{AX}=\mathrm{I}$, where $\mathrm{I}$ is $2 \times 2$ unit matrix, then $X=$

**Options:**

- **(A)** $\frac{1}{5}\left[\begin{array}{ll}-3 & -2 \\ -4 & -1\end{array}\right]$
- **(B)** $\frac{1}{5}\left[\begin{array}{cc}-3 & 2 \\ 4 & -1\end{array}\right]$
- **(C)** $\frac{1}{5}\left[\begin{array}{ll}3 & 2 \\ 4 & 1\end{array}\right]$
- **(D)** $\frac{1}{5}\left[\begin{array}{cc}3 & -2 \\ -4 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{5}\left[\begin{array}{cc}-3 & 2 \\ 4 & -1\end{array}\right]$**

**Detailed Solution:**

$\mathrm{AX}=\mathrm{I} \Rightarrow \mathrm{X}=\mathrm{A}^{-1}=\mathrm{A}^{-1}$
$\Rightarrow X=\left[\begin{array}{ll}1 & 2 \\ 4 & 3\end{array}\right]^{-1}=\frac{-1}{5}\left[\begin{array}{cc}3 & -2 \\ -4 & 1\end{array}\right]=\frac{1}{5}\left[\begin{array}{cc}-3 & 2 \\ 4 & -1\end{array}\right]$

</details>

---

### Q17. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{AX}=\mathrm{B}$, where $\mathrm{A}=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 2 & 1\end{array}\right], \mathrm{X}=\left[\begin{array}{l}\mathrm{x} \\ \mathrm{y} \\ \mathrm{z}\end{array}\right], \mathrm{B}=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]$, then $2 x+y-z=0$

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 4
- **(D)** -2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$\begin{aligned} & {\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & -3 \\ 1 & 2 & 1\end{array}\right]\left[\begin{array}{l}\mathrm{x} \\ \mathrm{y} \\ \mathrm{z}\end{array}\right]=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]} \\ & \mathrm{R}_3 \rightarrow \mathrm{R}_3-\mathrm{R}_1 \text { and } \mathrm{R}_2 \rightarrow \mathrm{R}_2-2 \mathrm{R}_1 \\ & {\left[\begin{array}{ccc}1 & -1 & 1 \\ 0 & 3 & -5 \\ 0 & 2 & 0\end{array}\right]\left[\begin{array}{l}\mathrm{x} \\ \mathrm{y} \\ \mathrm{z}\end{array}\right]=\left[\begin{array}{c}4 \\ -8 \\ -2\end{array}\right]}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/O4ecgd3-ULY6eiCaH94oZ33Cnk-34QF5duC6OBDx0-E.original.fullsize.png">

$\begin{array}{lll}\therefore & y=-1 & \ldots[\operatorname{from}(3)] \\ \therefore & -3-5 z=-8 \quad \Rightarrow z=1 & \ldots[\operatorname{from}(2)] \\ \therefore & x-(-1)+1=4 \Rightarrow x=2 & \ldots[\operatorname{from}(1)] \\ \therefore & 2 x+y-z=2(2)-1-1=2 & \end{array}$

</details>

---

### Q18. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}1 & 0 \\ -1 & 7\end{array}\right], I=\left[\begin{array}{cc}1 & 0 \\ 0 & 1\end{array}\right]$ and $A^{2}=8 A+k I$, then the value of $K$ is

**Options:**

- **(A)** $\frac{1}{7}$
- **(B)** $\frac{-1}{7}$
- **(C)** $-7$
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-7$**

**Detailed Solution:**

$$
A^{2}=A \times A=\left[\begin{array}{cc}
1 & 0 \\
-1 & 7
\end{array}\right]\left[\begin{array}{cc}
1 & 0 \\
-1 & 7
\end{array}\right]=\left[\begin{array}{cc}
1 & 0 \\
-8 & 49
\end{array}\right]
$$
Given $A^{2}=8 A+K I$
$$
\begin{aligned}
&=8\left[\begin{array}{cc}
1 & 0 \\
-1 & 7
\end{array}\right]+\mathrm{k}\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]=\left[\begin{array}{cc}
8 & 0 \\
-8 & 56
\end{array}\right]+\left[\begin{array}{cc}
\mathrm{k} & 0 \\
0 & \mathrm{k}
\end{array}\right] \\
\therefore \quad\left[\begin{array}{cc}
1 & 0 \\
-8 & 49
\end{array}\right] &=\left[\begin{array}{cc}
8+\mathrm{k} & 0 \\
-8 & 56+\mathrm{k}
\end{array}\right] \Rightarrow 8+\mathrm{k}=1 \Rightarrow \mathrm{k}=-7
\end{aligned}
$$

</details>

---

### Q19. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

$A=\left[\begin{array}{rr}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$ and $A B=B A=I$, then $B$ is
equal to

**Options:**

- **(A)** $\left[\begin{array}{rr}-\cos \theta & \sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
- **(B)** $\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$
- **(C)** $\left[\begin{array}{rr}-\sin \theta & \cos \theta \\ \cos \theta & \sin \theta\end{array}\right]$
- **(D)** $\left[\begin{array}{rr}\sin \theta & -\cos \theta \\ -\cos \theta & \sin \theta\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$**

**Detailed Solution:**

Given, $A=\left[\begin{array}{rr}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right]$
and $\quad A B=B A=I$
$\Rightarrow B=A^{-1} I=A^{-1}$
$=\frac{1}{\cos ^{2} \theta+\sin ^{2} \theta}\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$
$\Rightarrow B=\left[\begin{array}{rr}\cos \theta & \sin \theta \\ -\sin \theta & \cos \theta\end{array}\right]$

</details>

---

### Q20. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}\cos ^{2} \alpha & \cos \alpha \sin \alpha \\ \cos \alpha \sin \alpha & \sin ^{2} \alpha\end{array}\right]$
and
$B=\left[\begin{array}{cc}\cos ^{2} \beta & \cos \beta \sin \beta \\ \cos \beta \sin \beta & \sin ^{2} \beta\end{array}\right]$ are two matrices
such that the product $A B$ is null matrix, then $\alpha-\beta$ is

**Options:**

- **(A)** 0
- **(B)** multiple of $\pi$
- **(C)** an odd multiple of $\pi / 2$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Given, $A B=O$
$\Rightarrow \alpha-\beta$ is an odd multiple of $\pi / 2$.

</details>

---

