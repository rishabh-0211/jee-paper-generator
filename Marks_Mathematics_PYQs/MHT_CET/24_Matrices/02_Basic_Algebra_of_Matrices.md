# MHT CET Mathematics - Matrices

## Topic 2: Basic Algebra of Matrices

**Total Questions:** 11

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A + I = \begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$, then the inverse of the matrix $(A - I)$ is:

**Options:**

- **(A)** $\begin{pmatrix} 1 & -2 \\ 1 & -3 \end{pmatrix}$
- **(B)** $\begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$
- **(C)** $\begin{pmatrix} -3 & 2 \\ -1 & 1 \end{pmatrix}$
- **(D)** $\begin{pmatrix} -3 & 2 \\ -1 & -1 \end{pmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$**

**Detailed Solution:**

Given $A + I = \begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$

Subtracting $2I$ from both sides:

$A - I = \begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix} - \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 1 & -3 \end{pmatrix}$

To find the inverse of $(A - I)$, we first calculate its determinant:

$|A - I| = (1)(-3) - (-2)(1) = -3 + 2 = -1$

The adjugate matrix of $(A - I)$ is obtained by swapping the diagonal elements and changing the signs of the off-diagonal elements:

$\text{adj}(A - I) = \begin{pmatrix} -3 & 2 \\ -1 & 1 \end{pmatrix}$

The inverse is given by:

$(A - I)^{-1} = \dfrac{1}{|A - I|} \text{adj}(A - I) = \dfrac{1}{-1} \begin{pmatrix} -3 & 2 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$

Answer: $\begin{pmatrix} 3 & -2 \\ 1 & -1 \end{pmatrix}$

</details>

---

### Q2. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} -3 & 2 \\ 1 & 4 \end{bmatrix}$ and if $A^2 - 2A + I = \begin{bmatrix} 18 & p \\ q & 11 \end{bmatrix}$, then $\ldots$

**Options:**

- **(A)** $p = -2,\ q = -1$
- **(B)** $p = 2,\ q = 1$
- **(C)** $p = -1,\ q = -2$
- **(D)** $p = 1,\ q = 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p = -2,\ q = -1$**

**Detailed Solution:**

Given $A = \begin{bmatrix} -3 & 2 \\ 1 & 4 \end{bmatrix}$

First, we calculate $A^2$:
$A^2 = \begin{bmatrix} -3 & 2 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} -3 & 2 \\ 1 & 4 \end{bmatrix} = \begin{bmatrix} 9 + 2 & -6 + 8 \\ -3 + 4 & 2 + 16 \end{bmatrix} = \begin{bmatrix} 11 & 2 \\ 1 & 18 \end{bmatrix}$

Next, we calculate $2A$:
$2A = 2 \begin{bmatrix} -3 & 2 \\ 1 & 4 \end{bmatrix} = \begin{bmatrix} -6 & 4 \\ 2 & 8 \end{bmatrix}$

Now, substituting these into $A^2 - 2A + I$:
$A^2 - 2A + I = \begin{bmatrix} 11 & 2 \\ 1 & 18 \end{bmatrix} - \begin{bmatrix} -6 & 4 \\ 2 & 8 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

$= \begin{bmatrix} 11 - (-6) + 1 & 2 - 4 + 0 \\ 1 - 2 + 0 & 18 - 8 + 1 \end{bmatrix}$

$= \begin{bmatrix} 18 & -2 \\ -1 & 11 \end{bmatrix}$

We are given that $A^2 - 2A + I = \begin{bmatrix} 18 & p \\ q & 11 \end{bmatrix}$.

Comparing the corresponding elements of the matrices, we get:
$p = -2$
$q = -1$

Answer: $p = -2,\ q = -1$

</details>

---

### Q3. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A = \begin{bmatrix} 3 & 0 & 0 \\ 0 & -5 & 0 \\ 0 & 0 & 7 \end{bmatrix}$; $B = \begin{bmatrix} -1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 4 \end{bmatrix}$ then, $(2A + 3B)^{-1} =$ _______

**Options:**

- **(A)** $\begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & -\dfrac{1}{4} & 0 \\ 0 & 0 & \dfrac{1}{26} \end{bmatrix}$
- **(B)** $\begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & \dfrac{1}{4} & 0 \\ 0 & 0 & \dfrac{1}{26} \end{bmatrix}$
- **(C)** $\begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & \dfrac{1}{4} & 0 \\ 0 & 0 & -\dfrac{1}{26} \end{bmatrix}$
- **(D)** $\begin{bmatrix} -\dfrac{1}{3} & 0 & 0 \\ 0 & \dfrac{1}{4} & 0 \\ 0 & 0 & -\dfrac{1}{26} \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & -\dfrac{1}{4} & 0 \\ 0 & 0 & \dfrac{1}{26} \end{bmatrix}$**

**Detailed Solution:**

$A = \begin{bmatrix} 3 & 0 & 0 \\ 0 & -5 & 0 \\ 0 & 0 & 7 \end{bmatrix}$

$B = \begin{bmatrix} -1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 4 \end{bmatrix}$

$2A = \begin{bmatrix} 6 & 0 & 0 \\ 0 & -10 & 0 \\ 0 & 0 & 14 \end{bmatrix}$

$3B = \begin{bmatrix} -3 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 12 \end{bmatrix}$

$2A + 3B = \begin{bmatrix} 6 - 3 & 0 & 0 \\ 0 & -10 + 6 & 0 \\ 0 & 0 & 14 + 12 \end{bmatrix} = \begin{bmatrix} 3 & 0 & 0 \\ 0 & -4 & 0 \\ 0 & 0 & 26 \end{bmatrix}$

The inverse of a diagonal matrix is obtained by taking the reciprocal of its diagonal elements.

$(2A + 3B)^{-1} = \begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & -\dfrac{1}{4} & 0 \\ 0 & 0 & \dfrac{1}{26} \end{bmatrix}$

Answer: $\begin{bmatrix} \dfrac{1}{3} & 0 & 0 \\ 0 & -\dfrac{1}{4} & 0 \\ 0 & 0 & \dfrac{1}{26} \end{bmatrix}$

</details>

---

### Q4. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix}$ and $A^2 + xA + yI_2 = O_2$, where $I_2$ and $O_2$ are the identity matrix and null matrix of order 2 respectively, then:

**Options:**

- **(A)** $x = 4,\ y = 4$
- **(B)** $x = -4,\ y = 4$
- **(C)** $x = -4,\ y = -2$
- **(D)** $x = 4,\ y = -4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x = -4,\ y = 4$**

**Detailed Solution:**

$A^2 = \begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 4 & -4 \\ 0 & 4 \end{bmatrix}$

Substituting $A^2$, $A$, and $I_2$ into the given equation $A^2 + xA + yI_2 = O_2$:

$\begin{bmatrix} 4 & -4 \\ 0 & 4 \end{bmatrix} + x \begin{bmatrix} 2 & -1 \\ 0 & 2 \end{bmatrix} + y \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$

$\begin{bmatrix} 4 + 2x + y & -4 - x \\ 0 & 4 + 2x + y \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$

Equating the corresponding elements to zero:

$-4 - x = 0 \Rightarrow x = -4$

$4 + 2x + y = 0$

Substituting $x = -4$ into the second equation:

$4 + 2(-4) + y = 0 \Rightarrow y = 4$

Answer: $x = -4,\ y = 4$

</details>

---

### Q5. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A = \begin{bmatrix} -5 & -3 \\ 2 & 1 \end{bmatrix}$. The Row transformation $R_1 \rightarrow R_1 + 3R_2$ will transform matrix A into

**Options:**

- **(A)** an upper triangular matrix
- **(B)** a lower triangular matrix
- **(C)** an identity matrix
- **(D)** a singular matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a lower triangular matrix**

**Detailed Solution:**

Given $A = \begin{bmatrix} -5 & -3 \\ 2 & 1 \end{bmatrix}$

Applying the row transformation $R_1 \rightarrow R_1 + 3R_2$, the elements of the first row become:

$a_{11} = -5 + 3(2) = 1$

$a_{12} = -3 + 3(1) = 0$

The transformed matrix is $\begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$.

Since all elements above the principal diagonal are zero, it is a lower triangular matrix.

Answer: a lower triangular matrix

</details>

---

### Q6. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\left[\begin{array}{ccc}1 & 1 & 1 \\ 1 & -2 & -2 \\ 1 & 3 & 1\end{array}\right]\left[\begin{array}{l}x \\ y \\ z\end{array}\right]=\left[\begin{array}{l}0 \\ 3 \\ 4\end{array}\right]$, then $2 x-y+z=$

**Options:**

- **(A)** 3
- **(B)** 2
- **(C)** 1
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3$**

**Detailed Solution:**

From the given equation we have
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/F7pPzi9PfWugqXpUbryX54QcaBGoiMbQ-t8-ehG88NQ.original.fullsize.png">
Solving we get $x=1, y=2$ and $z=-3$
Now, $2 x-y+z=2 \times 1-2+(-3)=-3$

</details>

---

### Q7. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\left[\begin{array}{ll}2 & 1 \\ 3 & 2\end{array}\right] A\left[\begin{array}{cc}-3 & 2 \\ 5 & -3\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$, then $A=$

**Options:**

- **(A)** $\left[\begin{array}{ll}1 & 1 \\ 1 & 1\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}1 & 0 \\ 1 & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & {\left[\begin{array}{ll}2 & 1 \\ 3 & 2\end{array}\right] A\left[\begin{array}{cc}-3 & 2 \\ 5 & -3\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]} \\ & \Rightarrow A=\left[\begin{array}{ll}2 & 1 \\ 3 & 2\end{array}\right]^{-1}\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]\left[\begin{array}{ll}3 & 2 \\ 5 & 3\end{array}\right]^{-1} \\ & \Rightarrow A=\left[\begin{array}{cc}2 & -1 \\ -3 & 2\end{array}\right]\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]\left[\begin{array}{ll}3 & 2 \\ 5 & 3\end{array}\right] \\ & \Rightarrow A=\left[\begin{array}{cc}2 & -1 \\ -3 & 2\end{array}\right]\left[\begin{array}{ll}3 & 2 \\ 5 & 3\end{array}\right] \\ & \Rightarrow A=\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]\end{aligned}$

</details>

---

### Q8. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 1 & 1 \\ 2 & 1 & -3 \\ -1 & 2 & 3\end{array}\right]$, then $A_{31}+A_{32}+A_{33}=$ where $A_{i j}$, where $A=\left[a_{i j}\right]_{3 \times 3}$

**Options:**

- **(A)** 10
- **(B)** 1
- **(C)** 0
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

We know that sum of the product of elements of one row of a determinant and cofactor of corresponding element of any other row is zero.
$\begin{aligned} & \Rightarrow a_{11} A_{31}+a_{12} A_{32}+a_{13} A_{33}=0 \\ & \Rightarrow 1 \cdot A_{31}+1 \cdot A_{32}+1 \cdot A_{33}=0 \Rightarrow A_{31}+A_{32}+A_{33}=0\end{aligned}$

</details>

---

### Q9. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A^{-1}=\left[\begin{array}{lll}3 & 2 & 6 \\ 1 & 1 & 2 \\ 2 & 5 & 5\end{array}\right]$, then $A=$

**Options:**

- **(A)** $\left[\begin{array}{ccc}-5 & 20 & -2 \\ -1 & 3 & 0 \\ 3 & -11 & 1\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}-5 & 20 & 2 \\ -1 & 3 & 0 \\ 3 & 11 & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}-5 & 20 & 2 \\ 1 & 3 & 0 \\ 3 & 11 & -1\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}-5 & 20 & -2 \\ 1 & 3 & 0 \\ 3 & 11 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{ccc}-5 & 20 & -2 \\ -1 & 3 & 0 \\ 3 & -11 & 1\end{array}\right]$**

**Detailed Solution:**

Let $\mathrm{A}^{-1} \mathrm{~A}=\mathrm{I}$
$$
\begin{aligned}
& {\left[\begin{array}{lll}
3 & 2 & 6 \\
1 & 1 & 2 \\
2 & 5 & 5
\end{array}\right] A=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]} \\
& R_2 \rightarrow 3 R_2-R_1 \text { and } R_3 \rightarrow 3 R_3-2 R_1 \\
& {\left[\begin{array}{ccc}
3 & 2 & 6 \\
0 & 1 & 0 \\
0 & 11 & 3
\end{array}\right] A=\left[\begin{array}{ccc}
1 & 0 & 0 \\
-1 & 3 & 0 \\
-2 & 0 & 3
\end{array}\right]} \\
& R_1 \rightarrow R_1-2 R_2 \text { and } R_3 \rightarrow R_3-11 R_2
\end{aligned}
$$


$$
\begin{aligned}
& {\left[\begin{array}{lll}
3 & 0 & 6 \\
0 & 1 & 0 \\
0 & 0 & 3
\end{array}\right] A=\left[\begin{array}{ccc}
3 & - & 0 \\
-1 & 3 & 0 \\
9 & -33 & 3
\end{array}\right]} \\
& \mathrm{R}_1 \rightarrow \mathrm{R}_1-2 \mathrm{R}_3 \\
& {\left[\begin{array}{lll}
3 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 3
\end{array}\right] \mathrm{A}=\left[\begin{array}{ccc}
-15 & 60 & -6 \\
-1 & 3 & 0 \\
9 & -33 & 3
\end{array}\right]} \\
& \mathrm{R}_1 \rightarrow \frac{1}{3} \mathrm{R}_1 \text { and } \mathrm{R}_3 \rightarrow \frac{1}{3} \mathrm{R}_3 \\
& {\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \mathrm{A}=\left[\begin{array}{ccc}
-5 & 20 & -2 \\
-1 & 3 & 0 \\
3 & -11 & 1
\end{array}\right]}
\end{aligned}
$$

</details>

---

### Q10. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

If matrix $A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$, then $|A|^{-1}$ is equal to

**Options:**

- **(A)** $a d-b c$
- **(B)** $\frac{1}{a d-b c}$
- **(C)** $\frac{1}{a d-b c}\left[\begin{array}{rr}d & -b \\ -c & a\end{array}\right]$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{a d-b c}$**

**Detailed Solution:**

Given, $\quad A=\left[\begin{array}{ll}a & b \\ c & d\end{array}\right]$
$$
\begin{array}{l}
|A|=a d-b c \\
|A|^{-1}=\frac{1}{a d-b c}
\end{array}
$$

</details>

---

### Q11. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `1`

The solution of the equation
$\left[\begin{array}{rrr}1 & 0 & 1 \\ -1 & 1 & 0 \\ 0 & -1 & 1\end{array}\right]\left[\begin{array}{l}x \\ y \\ z\end{array}\right]=\left[\begin{array}{l}1 \\ 1 \\ 2\end{array}\right]$ is $(x, y, z)=$

**Options:**

- **(A)** $(1,1,1)$
- **(B)** $(0,-1,2)$
- **(C)** $(-1,2,2)$
- **(D)** $(-1,0,2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(-1,0,2)$**

**Detailed Solution:**

$$
\begin{aligned}
\left[\begin{array}{rrr}
1 & 0 & 1 \\
-1 & 1 & 0 \\
0 & -1 & 1
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right] \\
\Rightarrow\left[\begin{array}{r}
x+0 y+z \\
-x+y+0 z \\
0 x-y+z
\end{array}\right]=\left[\begin{array}{l}
1 \\
1 \\
2
\end{array}\right] \\
\Rightarrow \quad x+z=1, \\
-x+y=1
\end{aligned}
$$
and $\quad-y+z=2$
On solving these equations, we get
$$
x=-1, y=0, z=2
$$

</details>

---

