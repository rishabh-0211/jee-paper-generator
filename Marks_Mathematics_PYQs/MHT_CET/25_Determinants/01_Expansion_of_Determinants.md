# MHT CET Mathematics - Determinants

## Topic 1: Expansion of Determinants

**Total Questions:** 15

---

### Q1. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{vmatrix} \sin x + \sin 2x + \sin 3x & \sin 2x & \sin 3x \\ 3 + 4\sin x & 3 & 4\sin x \\ 1 + \sin x & \sin x & 1 \end{vmatrix}$, then $\displaystyle\int_{0}^{\frac{\pi}{2}} f(x)\,dx =$

**Options:**

- **(A)** $1$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{3}$**

**Detailed Solution:**

Applying the column operation $C_1 \rightarrow C_1 - C_2 - C_3$, we get:

$f(x) = \begin{vmatrix} \sin x & \sin 2x & \sin 3x \\ 0 & 3 & 4\sin x \\ 0 & \sin x & 1 \end{vmatrix}$

Expanding the determinant along the first column:

$f(x) = \sin x (3 \times 1 - 4\sin x \times \sin x)$

$f(x) = \sin x (3 - 4\sin^2 x)$

$f(x) = 3\sin x - 4\sin^3 x = \sin 3x$

Now, evaluating the integral:

$\displaystyle\int_{0}^{\dfrac{\pi}{2}} f(x)\,dx = \displaystyle\int_{0}^{\dfrac{\pi}{2}} \sin 3x \,dx$

$= \left[ -\dfrac{\cos 3x}{3} \right]_{0}^{\dfrac{\pi}{2}}$

$= -\dfrac{1}{3} \left( \cos\left(\dfrac{3\pi}{2}\right) - \cos(0) \right)$

$= -\dfrac{1}{3} (0 - 1) = \dfrac{1}{3}$

Answer: $\dfrac{1}{3}$

</details>

---

### Q2. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A = \begin{bmatrix} 3 & 1 & 2 \\ 1 & 2 & 0 \\ 1 & 1 & 4 \end{bmatrix}$ and $pC_{11} + 4C_{21} - 5C_{32} = -2$, where $C_{ij}$ denotes the cofactor of an element $a_{ij}$ of matrix $A$, then the value of $p$ is :

**Options:**

- **(A)** $-2$
- **(B)** $2$
- **(C)** $4$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Given matrix $A = \begin{bmatrix} 3 & 1 & 2 \\ 1 & 2 & 0 \\ 1 & 1 & 4 \end{bmatrix}$

The cofactor $C_{ij}$ is given by $(-1)^{i+j} M_{ij}$, where $M_{ij}$ is the minor of the element $a_{ij}$.

Calculating the required cofactors:

$C_{11} = (-1)^{1+1} \begin{vmatrix} 2 & 0 \\ 1 & 4 \end{vmatrix} = 1 \times (8 - 0) = 8$

$C_{21} = (-1)^{2+1} \begin{vmatrix} 1 & 2 \\ 1 & 4 \end{vmatrix} = -1 \times (4 - 2) = -2$

$C_{32} = (-1)^{3+2} \begin{vmatrix} 3 & 2 \\ 1 & 0 \end{vmatrix} = -1 \times (0 - 2) = 2$

Substituting these values into the given equation $pC_{11} + 4C_{21} - 5C_{32} = -2$:

$p(8) + 4(-2) - 5(2) = -2$

$8p - 8 - 10 = -2$

$8p - 18 = -2$

$8p = 16$

$p = 2$

Answer: $2$

</details>

---

### Q3. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The lines $x+2 a y+a=0, x+3 b y+b=0, x+4 c y+c=0$ are concurrent then $a, \mathrm{~b}, \mathrm{c}$ are in

**Options:**

- **(A)** Harmonic progression
- **(B)** Geometric progression
- **(C)** Arithmetic progression
- **(D)** Arithmetico geometric progression

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Harmonic progression**

**Detailed Solution:**

The condition for the given three lines to be concurrent is that the determinant of their coefficients must be zero.

$\begin{vmatrix} 1 & 2a & a \\ 1 & 3b & b \\ 1 & 4c & c \end{vmatrix} = 0$

Expanding the determinant along the first column:

$1(3bc - 4bc) - 1(2ac - 4ac) + 1(2ab - 3ab) = 0$

$-bc - (-2ac) + (-ab) = 0$

$2ac - bc - ab = 0$

$2ac = ab + bc$

Dividing the entire equation by $abc$:

$\dfrac{2ac}{abc} = \dfrac{ab}{abc} + \dfrac{bc}{abc}$

$\dfrac{2}{b} = \dfrac{1}{c} + \dfrac{1}{a}$

This implies that $\dfrac{1}{a}, \dfrac{1}{b}, \dfrac{1}{c}$ are in Arithmetic Progression.

Therefore, $a, b, c$ are in Harmonic Progression.

Answer: Harmonic progression

</details>

---

### Q4. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}\cos \theta & \sin \theta & 0 \\ -\sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$,
where $A_{21}, A_{22}, A_{23}$ are cofactors of $a_{21}, a_{22}, a_{23}$ respectively, then the value of $a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23}=$

**Options:**

- **(A)** $1$
- **(B)** $-1$
- **(C)** $0$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

The sum of the products of the elements of any row with their corresponding cofactors is equal to the determinant of the matrix.

Therefore, $a_{21} A_{21} + a_{22} A_{22} + a_{23} A_{23} = |A|$

Calculating the determinant of $A$:

$|A| = \cos \theta (\cos \theta \cdot 1 - 0) - \sin \theta (-\sin \theta \cdot 1 - 0) + 0$

$|A| = \cos^2 \theta + \sin^2 \theta = 1$

Thus, $a_{21} A_{21} + a_{22} A_{22} + a_{23} A_{23} = 1$

Answer: $1$

</details>

---

### Q5. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If \([2 \overline{\mathrm{p}}-3 \overline{\mathrm{r}} ~\overline{\mathrm{q}} ~\overline{\mathrm{s}}]+[3 \overline{\mathrm{p}}+2 \overline{\mathrm{q}} ~\overline{\mathrm{r}} ~\overline{\mathrm{s}}]=\mathrm{m}[\overline{\mathrm{p}} ~\overline{\mathrm{r}} ~\overline{\mathrm{s}}]+\mathrm{n}[\overline{\mathrm{q}} ~\overline{\mathrm{r}} ~\overline{\mathrm{s}}]+\mathrm{t}[\overline{\mathrm{p}} ~\overline{\mathrm{q}} ~\overline{\mathrm{s}}]\),, then the values of $m, n, t$ respectively are ....

**Options:**

- **(A)** $2,3,3$
- **(B)** $3,4,5$
- **(C)** $1,2,3$
- **(D)** $3,5,2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3,5,2$**

**Detailed Solution:**

Using the properties of scalar triple product:

$[2\bar{p} - 3\bar{r} \quad \bar{q} \quad \bar{s}] = [2\bar{p} \quad \bar{q} \quad \bar{s}] - [3\bar{r} \quad \bar{q} \quad \bar{s}]$

$= 2[\bar{p} \quad \bar{q} \quad \bar{s}] - 3[\bar{r} \quad \bar{q} \quad \bar{s}]$

Since $[\bar{r} \quad \bar{q} \quad \bar{s}] = -[\bar{q} \quad \bar{r} \quad \bar{s}]$, we get:

$[2\bar{p} - 3\bar{r} \quad \bar{q} \quad \bar{s}] = 2[\bar{p} \quad \bar{q} \quad \bar{s}] + 3[\bar{q} \quad \bar{r} \quad \bar{s}]$

Similarly, for the second term:

$[3\bar{p} + 2\bar{q} \quad \bar{r} \quad \bar{s}] = [3\bar{p} \quad \bar{r} \quad \bar{s}] + [2\bar{q} \quad \bar{r} \quad \bar{s}]$

$= 3[\bar{p} \quad \bar{r} \quad \bar{s}] + 2[\bar{q} \quad \bar{r} \quad \bar{s}]$

Adding the two expressions:

$[2\bar{p} - 3\bar{r} \quad \bar{q} \quad \bar{s}] + [3\bar{p} + 2\bar{q} \quad \bar{r} \quad \bar{s}] = 2[\bar{p} \quad \bar{q} \quad \bar{s}] + 3[\bar{q} \quad \bar{r} \quad \bar{s}] + 3[\bar{p} \quad \bar{r} \quad \bar{s}] + 2[\bar{q} \quad \bar{r} \quad \bar{s}]$

$= 3[\bar{p} \quad \bar{r} \quad \bar{s}] + 5[\bar{q} \quad \bar{r} \quad \bar{s}] + 2[\bar{p} \quad \bar{q} \quad \bar{s}]$

Comparing this with $m[\bar{p} \quad \bar{r} \quad \bar{s}] + n[\bar{q} \quad \bar{r} \quad \bar{s}] + t[\bar{p} \quad \bar{q} \quad \bar{s}]$, we get:

$m = 3$, $n = 5$, $t = 2$

Answer: $3,5,2$

</details>

---

### Q6. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $w=\dfrac{-1-i \sqrt{3}}{2}$ where $i=\sqrt{-1}$, then the value of $\left|\begin{array}{ccc}1 & w & w^2 \\ w & w^2 & 1 \\ w^2 & 1 & w\end{array}\right|$ is

**Options:**

- **(A)** -1
- **(B)** 0
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

Given $w = \dfrac{-1 - i\sqrt{3}}{2}$, which is a complex cube root of unity.

Therefore, $w^3 = 1$ and $1 + w + w^2 = 0$.

The given determinant is $\Delta = \left|\begin{array}{ccc}1 & w & w^2 \\ w & w^2 & 1 \\ w^2 & 1 & w\end{array}\right|$.

Applying the column operation $C_1 \rightarrow C_1 + C_2 + C_3$, we get:

$\Delta = \left|\begin{array}{ccc}1 + w + w^2 & w & w^2 \\ 1 + w + w^2 & w^2 & 1 \\ 1 + w + w^2 & 1 & w\end{array}\right|$

Substituting $1 + w + w^2 = 0$:

$\Delta = \left|\begin{array}{ccc}0 & w & w^2 \\ 0 & w^2 & 1 \\ 0 & 1 & w\end{array}\right|$

Since all elements of the first column are zero, the value of the determinant is $0$.

Answer: 0

</details>

---

### Q7. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the matrix $\mathrm{A}=\left[\begin{array}{ccc}2 & 0 & -1 \\ 3 & 1 & 2 \\ -1 & 1 & 2\end{array}\right]$, the matrix of cofactors is

**Options:**

- **(A)** $\left[\begin{array}{ccc}0 & 8 & -4 \\ -1 & 3 & 2 \\ 1 & -7 & 2\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}0 & -8 & 4 \\ -1 & 3 & -2 \\ 1 & -7 & 2\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}0 & 8 & -4 \\ 1 & -3 & 2 \\ -1 & 7 & -2\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}0 & -8 & 4 \\ -1 & 3 & 2 \\ -1 & -7 & 2\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{ccc}0 & -8 & 4 \\ -1 & 3 & -2 \\ 1 & -7 & 2\end{array}\right]$**

**Detailed Solution:**

Let $C_{ij}$ be the cofactor of the element $a_{ij}$ in the given matrix $A$.

$C_{11} = (-1)^{1+1} \begin{vmatrix} 1 & 2 \\ 1 & 2 \end{vmatrix} = 2 - 2 = 0$

$C_{12} = (-1)^{1+2} \begin{vmatrix} 3 & 2 \\ -1 & 2 \end{vmatrix} = -(6 - (-2)) = -8$

$C_{13} = (-1)^{1+3} \begin{vmatrix} 3 & 1 \\ -1 & 1 \end{vmatrix} = 3 - (-1) = 4$

$C_{21} = (-1)^{2+1} \begin{vmatrix} 0 & -1 \\ 1 & 2 \end{vmatrix} = -(0 - (-1)) = -1$

$C_{22} = (-1)^{2+2} \begin{vmatrix} 2 & -1 \\ -1 & 2 \end{vmatrix} = 4 - 1 = 3$

$C_{23} = (-1)^{2+3} \begin{vmatrix} 2 & 0 \\ -1 & 1 \end{vmatrix} = -(2 - 0) = -2$

$C_{31} = (-1)^{3+1} \begin{vmatrix} 0 & -1 \\ 1 & 2 \end{vmatrix} = 0 - (-1) = 1$

$C_{32} = (-1)^{3+2} \begin{vmatrix} 2 & -1 \\ 3 & 2 \end{vmatrix} = -(4 - (-3)) = -7$

$C_{33} = (-1)^{3+3} \begin{vmatrix} 2 & 0 \\ 3 & 1 \end{vmatrix} = 2 - 0 = 2$

The matrix of cofactors is $\left[\begin{array}{ccc}0 & -8 & 4 \\ -1 & 3 & -2 \\ 1 & -7 & 2\end{array}\right]$.

Answer: $\left[\begin{array}{ccc}0 & -8 & 4 \\ -1 & 3 & -2 \\ 1 & -7 & 2\end{array}\right]$

</details>

---

### Q8. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\left|\begin{array}{ccc}\cos (A+B) & -\sin (A+B) & \cos (2 B) \\ \sin A & \cos A & \sin B \\ -\cos A & \sin A & \cos B\end{array}\right|=0$, then the value of $\mathrm{B}$ is

**Options:**

- **(A)** $\mathrm{n} \pi, \mathrm{n} \in \mathbb{Z}$
- **(B)** $(2 \mathrm{n}+1) \frac{\pi}{2}, \mathrm{n} \in \mathrm{Z}$
- **(C)** $(2 n+1) \frac{\pi}{4}, n \in \mathbb{Z}$
- **(D)** $2 \mathrm{n} \frac{\pi}{3}, \mathrm{n} \in \mathbb{Z}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(2 \mathrm{n}+1) \frac{\pi}{2}, \mathrm{n} \in \mathrm{Z}$**

**Detailed Solution:**

$\begin{aligned} & \left|\begin{array}{ccc}\cos (A+B) & -\sin (A+B) & \cos (2 B) \\ \sin A & \cos A & \sin B \\ -\cos A & \sin A & \cos B\end{array}\right|=0 \\ & \therefore \quad \cos (\mathrm{A}+\mathrm{B})[(\cos \mathrm{A} \cos \mathrm{B}-\sin \mathrm{A} \sin \mathrm{B})] \\ & +\sin (A+B)[\sin A \cos B+\sin B \cos A] \\ & +\cos 2 \mathrm{~B}\left[\sin ^2 \mathrm{~A}+\cos ^2 \mathrm{~A}\right]=0 \\ & \therefore \quad \cos (\mathrm{A}+\mathrm{B}) \cdot \cos (\mathrm{A}+\mathrm{B}) \\ & +\sin (A+B) \cdot \sin (A+B)+\cos 2 B=0 \\ & \cos ^2(A+B)+\sin ^2(A+B)+\cos 2 B=0 \\ & 1+\cos 2 B=0 \\ & 2 \cos ^2 \mathrm{~B}=0 \\ & \therefore \quad \cos \mathrm{B}=0 \\ & \therefore \quad B=(2 n+1) \frac{\pi}{2} \text { for }(n \in Z) \\ & \end{aligned}$

</details>

---

### Q9. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[a_{i j}\right]_{3 \times 3}=\left[\begin{array}{ccc}1 & 3 & 3 \\ -1 & 2 & 2 \\ 1 & 1 & 4\end{array}\right]$ and $A_{i j}$ is a cofactor of $a_{i j}$ then the value of $a_{31} A_{31}+a_{32} A_{32}+a_{33} A_{33}$ is equal to

**Options:**

- **(A)** 5
- **(B)** 15
- **(C)** 20
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 15**

**Detailed Solution:**

$\begin{aligned} & a_{31} A_{31}+a_{32} A_{32}+a_{33} A_{33}=|A| \\ & =1 \times(8-2)-3(-4-2)+3(-1-2)=6+18-9=15\end{aligned}$

</details>

---

### Q10. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[a_{i j}\right]_{3 \times 3}=\left[\begin{array}{lll}3 & 2 & 4 \\ 1 & 4 & 1 \\ 2 & 6 & 3\end{array}\right]$ and $A_{i j}$ is a cofactor of $a_{i j}$, then the value of $a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23}$ is equal to

**Options:**

- **(A)** 18
- **(B)** 8
- **(C)** -8
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

$a_{21} A_{21}, a_{22} A_{22}+a_{23} A_{23}=|A|=3 \times(12-6)-2(3-2)+4(6-8)=8$

</details>

---

### Q11. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\left[\mathrm{a}_{\mathrm{ij}}\right]_{3 \times 3}=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 1 & 5 \\ 2 & 4 & 7\end{array}\right]$ and $\mathrm{Aij}$ is a cofactor of $\mathrm{a}_{\mathrm{ij}}$, then $a_{11} A_{21}+a_{12} A_{22}+a_{13} A_{23}$ is equal to

**Options:**

- **(A)** $-1$
- **(B)** $2$
- **(C)** $0$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

If we multiply elements of one row to the corresponding cofactors of another row and add them then we get zero hence,
$a_{11} A_{21}+a_{12} A_{22}+a_{13} A_{23}=0$

</details>

---

### Q12. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}5 & 6 & 3 \\ -4 & 3 & 2 \\ -4 & -7 & 3\end{array}\right]$, then cofactors of all elements of second row are respectively.

**Options:**

- **(A)** $-39,3,11$
- **(B)** $-39,27,11$
- **(C)** $39,-3-11$
- **(D)** $-39,-27,11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-39,27,11$**

**Detailed Solution:**

$$
A=\left[\begin{array}{ccc}
5 & 6 & 3 \\
-4 & 3 & 2 \\
-4 & -7 & 3
\end{array}\right]
$$
Cofactors of elements in second row are
Cofactor of -4
Cofactor of 3
$$
\begin{aligned}
& =(-1)^{2+1}\left|\begin{array}{cc}
6 & 3 \\
-7 & 3
\end{array}\right|=-(18+21)=-39 \\
& =(-1)^{2+2}\left|\begin{array}{cc}
5 & 3 \\
-4 & 3
\end{array}\right|=15+12=27 \\
& =(-1)^{2+3}\left|\begin{array}{cc}
5 & 6 \\
-4 & -7
\end{array}\right|=-(-35+24)=11
\end{aligned}
$$

</details>

---

### Q13. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The co-factors of the elements of second column of $\left[\begin{array}{ccc}1 & -1 & 2 \\ 3 & 2 & 1 \\ -1 & 3 & 4\end{array}\right]$ are

**Options:**

- **(A)** $-13,6,5$
- **(B)** $13,5,6$
- **(C)** $13,-6,-5$
- **(D)** $-13,-6,5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-13,6,5$**

**Detailed Solution:**

Required cofactors are as follows:
$$
\begin{aligned}
& \mathrm{A}_{12}=(-1)^{1+2}\left|\begin{array}{cc}
3 & 1 \\
-1 & 4
\end{array}\right|=-(12+1)=-13 \\
& \mathrm{~A}_{22}=(-1)^{2+2}\left|\begin{array}{cc}
1 & 2 \\
-1 & 4
\end{array}\right|=(4+2)=6 \\
& \mathrm{~A}_{32}=(-1)^{3+2}\left|\begin{array}{cc}
1 & 2 \\
3 & 1
\end{array}\right|=-(-1-6)=5
\end{aligned}
$$

</details>

---

### Q14. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A\left[\begin{array}{lll}3 & 2 & 4 \\ 1 & 2 & 1 \\ 3 & 2 & 6\end{array}\right]$ and $\mathrm{A}_{\mathrm{ij}}$ are cofactors of the elements $\mathrm{a}_{\mathrm{ij}}$ of $\mathrm{A}$, then $a_{11} A_{11}+a_{12} A_{12}+a_{13} A_{13}$ is equal to

**Options:**

- **(A)** 8
- **(B)** 6
- **(C)** 4
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

$\begin{aligned} & a_{11} A_{11}+a_{12} A_{12}+a_{13} A_{13}=|A| \\ & \therefore|A|=\left|\begin{array}{lll}3 & 2 & 4 \\ 1 & 2 & 1 \\ 3 & 2 & 6\end{array}\right| \\ & =3(12-2)-2(6-3)+4(2-6)=30-6-16=8\end{aligned}$

</details>

---

### Q15. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ccc}1 & 0 & 2 \\ 2 & 1 & 3 \\ 0 & 3 & -5\end{array}\right]$, where $A_{\text {ij }}$ is the cofactor of the element $a_{\text {ij }}$ of matrix $A$, then
$a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23}=$

**Options:**

- **(A)** $-26$
- **(B)** 0
- **(C)** $-2$
- **(D)** 26

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $-2$**

**Detailed Solution:**

$\begin{aligned} a_{21} & A_{21}+a_{22} A_{22}+a_{23} A_{23} \\ &=-2(0-6)+1(-5-0)-3(3-0) \\ &=12-5-9=-2 \end{aligned}$

</details>

---

