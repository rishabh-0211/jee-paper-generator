# MHT CET Mathematics - Matrices

## Topic 4: Adjoint and its Properties

**Total Questions:** 44

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 1 & -1 & 1 \\ 0 & 2 & -3 \\ 2 & 1 & 0 \end{bmatrix}$, $B = \text{adj}\ A$ and $C = 5A$, then the value of $\dfrac{|\text{adj}\ B|}{|C|}$ is:

**Options:**

- **(A)** $25$
- **(B)** $2$
- **(C)** $1$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

The determinant of matrix $A$ is calculated as:

$|A| = 1(0 - (-3)) - (-1)(0 - (-6)) + 1(0 - 4)$

$|A| = 3 + 6 - 4 = 5$

Given $B = \text{adj}\ A$, we need to find $|\text{adj}\ B|$, which is $|\text{adj}(\text{adj}\ A)|$. For a matrix of order $n$, the property is $|\text{adj}(\text{adj}\ A)| = |A|^{(n-1)^2}$.

Since the order of matrix $A$ is $n = 3$:

$|\text{adj}\ B| = |A|^{(3-1)^2} = |A|^4$

$|\text{adj}\ B| = 5^4 = 625$

Given $C = 5A$, the determinant of $C$ is found using the property $|kA| = k^n |A|$:

$|C| = |5A| = 5^3 |A|$

$|C| = 125 \times 5 = 625$

The required ratio is:

$\dfrac{|\text{adj}\ B|}{|C|} = \dfrac{625}{625} = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be an invertible matrix. Identify the correct statement(s) from the following.
(I) $A(\text{adj }A^{-1})=\dfrac{1}{|A|}A^2$ (II) $(\text{adj }A^{-1})^{-1}=\dfrac{1}{|A|}A^{-1}$ (III) $(\text{adj }A)=\dfrac{1}{|A|}A^{-1}$

**Options:**

- **(A)** only (I)
- **(B)** only (I) and (II)
- **(C)** only (III)
- **(D)** only (II) and (III)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) only (I)**

**Detailed Solution:**

For any invertible matrix $M$, we have $\text{adj } M = |M| M^{-1}$.

Replacing $M$ with $A^{-1}$, we get $\text{adj } A^{-1} = |A^{-1}| (A^{-1})^{-1} = \dfrac{1}{|A|} A$.

Checking statement (I):
$A(\text{adj } A^{-1}) = A \left( \dfrac{1}{|A|} A \right) = \dfrac{1}{|A|} A^2$.
Thus, statement (I) is correct.

Checking statement (II):
$(\text{adj } A^{-1})^{-1} = \left( \dfrac{1}{|A|} A \right)^{-1} = |A| A^{-1}$.
Thus, statement (II) is incorrect.

Checking statement (III):
$\text{adj } A = |A| A^{-1}$.
Thus, statement (III) is incorrect.

Therefore, only statement (I) is correct.

Answer: only (I)

</details>

---

### Q3. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If matrix $A = \begin{bmatrix} -1 & 2025 & 2026 \\ 0 & 2 & 2027 \\ 0 & 0 & -1 \end{bmatrix}$, then the sum of all elements in $\text{adj}(A^{-1})$ is equal to...

**Options:**

- **(A)** $1013$
- **(B)** $2026$
- **(C)** $3039$
- **(D)** $6078$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3039$**

**Detailed Solution:**

For any invertible matrix $M$, we have the property $\text{adj}(M) = |M| M^{-1}$.

Substituting $M = A^{-1}$, we get:

$\text{adj}(A^{-1}) = |A^{-1}| (A^{-1})^{-1} = \dfrac{1}{|A|} A$

Since $A$ is an upper triangular matrix, its determinant is the product of its diagonal elements:

$|A| = (-1) \times 2 \times (-1) = 2$

Thus, $\text{adj}(A^{-1}) = \dfrac{1}{2} A$.

The sum of all elements in $\text{adj}(A^{-1})$ will be $\dfrac{1}{2}$ times the sum of all elements in $A$.

Sum of all elements in $A = -1 + 2025 + 2026 + 0 + 2 + 2027 + 0 + 0 + (-1)$

Sum $= 2025 + 2026 + 2027 = 6078$

Therefore, the sum of all elements in $\text{adj}(A^{-1})$ is:

$\dfrac{1}{2} \times 6078 = 3039$

</details>

---

### Q4. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = [a_{ij}]_{3\times3}$, where $a_{ij} = \begin{cases} 1, & \text{if } i+j \text{ is even} \\ 0, & \text{if } i+j \text{ is odd} \end{cases}$, then $\text{adj}(A) = \ldots$ ..

**Options:**

- **(A)** $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$
- **(B)** $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{bmatrix}$
- **(C)** $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$
- **(D)** $\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{bmatrix}$**

**Detailed Solution:**

Given $A = [a_{ij}]_{3\times3}$ where $a_{ij} = 1$ if $i+j$ is even, and $0$ if $i+j$ is odd.

Constructing the matrix $A$:

$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$

The adjoint of $A$ is the transpose of the cofactor matrix $C$. Calculating the cofactors $C_{ij} = (-1)^{i+j} M_{ij}$:

$C_{11} = 1, C_{12} = 0, C_{13} = -1$

$C_{21} = 0, C_{22} = 0, C_{23} = 0$

$C_{31} = -1, C_{32} = 0, C_{33} = 1$

The cofactor matrix is $C = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{bmatrix}$.

Taking the transpose of $C$ gives the adjoint matrix:

$\text{adj}(A) = C^T = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{bmatrix}$

Answer: $\begin{bmatrix} 1 & 0 & -1 \\ 0 & 0 & 0 \\ -1 & 0 & 1 \end{bmatrix}$

</details>

---

### Q5. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} \cos\alpha & -\sin\alpha & 0 \\ \sin\alpha & \cos\alpha & 0 \\ 0 & 0 & 1 \end{bmatrix}$. If $B = \text{adj}\,A$, then the matrix $B^{-1}$ is equal to...

**Options:**

- **(A)** $I$
- **(B)** $A^{-1}$
- **(C)** $-A$
- **(D)** $A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $A$**

**Detailed Solution:**

The determinant of matrix $A$ is given by

$|A| = \cos\alpha(\cos\alpha - 0) - (-\sin\alpha)(\sin\alpha - 0) + 0$

$|A| = \cos^2\alpha + \sin^2\alpha = 1$

We know the property of adjoint of a matrix:

$A(\text{adj}\,A) = |A|I$

Substituting $|A| = 1$, we get

$A(\text{adj}\,A) = I$

$\Rightarrow \text{adj}\,A = A^{-1}$

It is given that $B = \text{adj}\,A$, so

$B = A^{-1}$

Taking the inverse on both sides, we obtain

$B^{-1} = (A^{-1})^{-1} = A$

Answer: $A$

</details>

---

### Q6. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix}$ and $A\,(\text{adj }A) = AA^T$, Then $5a + b =$

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $5$
- **(D)** $\dfrac{15}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix}$.

Using the property $A(\text{adj } A) = |A|I$, the given equation becomes $AA^T = |A|I$.

$|A| = (5a)(2) - (-b)(3) = 10a + 3b$

$AA^T = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix} \begin{bmatrix} 5a & 3 \\ -b & 2 \end{bmatrix} = \begin{bmatrix} 25a^2 + b^2 & 15a - 2b \\ 15a - 2b & 13 \end{bmatrix}$

Equating $AA^T$ to $|A|I$:

$\begin{bmatrix} 25a^2 + b^2 & 15a - 2b \\ 15a - 2b & 13 \end{bmatrix} = \begin{bmatrix} 10a + 3b & 0 \\ 0 & 10a + 3b \end{bmatrix}$

From the off-diagonal elements:

$15a - 2b = 0 \Rightarrow b = \dfrac{15a}{2}$

From the bottom-right elements:

$10a + 3b = 13$

Substituting $b = \dfrac{15a}{2}$ into the equation:

$10a + 3\left(\dfrac{15a}{2}\right) = 13$

$\dfrac{20a + 45a}{2} = 13$

$\dfrac{65a}{2} = 13 \Rightarrow a = \dfrac{26}{65} = \dfrac{2}{5}$

Substituting $a = \dfrac{2}{5}$ to find $b$:

$b = \dfrac{15}{2} \left(\dfrac{2}{5}\right) = 3$

$5a + b = 5\left(\dfrac{2}{5}\right) + 3 = 2 + 3 = 5$

Answer: $5$

</details>

---

### Q7. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 2k-1 & 1 & 1 \\ 0 & 2k-1 & 1 \\ 0 & 0 & 2k-1 \end{bmatrix}$ and $B = \begin{bmatrix} 0 & 2k-1 & 1 \\ 1-2k & 0 & k \\ -1 & -k & 0 \end{bmatrix}$ where k is a real number. If $\det(\text{adj} A) + \det(\text{adj} B) = 11^6$, then the value of $k - 5$ is equal to...

**Options:**

- **(A)** $1$
- **(B)** $2$
- **(C)** $4$
- **(D)** $6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

The determinant of the upper triangular matrix $A$ is the product of its diagonal elements:

$|A| = (2k-1)^3$

The matrix $B$ is a skew-symmetric matrix of odd order ($3 \times 3$), so its determinant is zero:

$|B| = 0$

Using the property $|\text{adj} M| = |M|^{n-1}$ for a matrix of order $n$, we have:

$|\text{adj} A| = |A|^2 = ((2k-1)^3)^2 = (2k-1)^6$

$|\text{adj} B| = |B|^2 = 0$

Given $|\text{adj} A| + |\text{adj} B| = 11^6$, we get:

$(2k-1)^6 + 0 = 11^6$

$2k-1 = \pm 11$

$2k = 12 \Rightarrow k = 6$

$2k = -10 \Rightarrow k = -5$

Checking the given options for the value of $k - 5$:

If $k = 6$, $k - 5 = 6 - 5 = 1$

If $k = -5$, $k - 5 = -5 - 5 = -10$

Since $-10$ is not among the options, we take $k = 6$, which gives $1$.

Answer: $1$

</details>

---

### Q8. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = \begin{bmatrix} \sec\theta & -\tan\theta \\ -\tan\theta & \sec\theta \end{bmatrix}$, $\theta \in \left(0, \dfrac{\pi}{2}\right)$ such that $A + adj\,A = 4I$, then $\theta =$

**Options:**

- **(A)** $\dfrac{\pi}{12}$
- **(B)** $\dfrac{\pi}{6}$
- **(C)** $\dfrac{\pi}{3}$
- **(D)** $\dfrac{\pi}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\pi}{3}$**

**Detailed Solution:**

Given $A = \begin{bmatrix} \sec\theta & -\tan\theta \\ -\tan\theta & \sec\theta \end{bmatrix}$

The adjoint of a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is $\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.

$adj\,A = \begin{bmatrix} \sec\theta & \tan\theta \\ \tan\theta & \sec\theta \end{bmatrix}$

$A + adj\,A = \begin{bmatrix} \sec\theta & -\tan\theta \\ -\tan\theta & \sec\theta \end{bmatrix} + \begin{bmatrix} \sec\theta & \tan\theta \\ \tan\theta & \sec\theta \end{bmatrix} = \begin{bmatrix} 2\sec\theta & 0 \\ 0 & 2\sec\theta \end{bmatrix}$

Given $A + adj\,A = 4I$, we have:

$\begin{bmatrix} 2\sec\theta & 0 \\ 0 & 2\sec\theta \end{bmatrix} = \begin{bmatrix} 4 & 0 \\ 0 & 4 \end{bmatrix}$

$2\sec\theta = 4 \Rightarrow \sec\theta = 2$

Since $\theta \in \left(0, \dfrac{\pi}{2}\right)$, $\theta = \dfrac{\pi}{3}$

</details>

---

### Q9. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{rrr}1 & -2 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right]$ then $A(I+\operatorname{adj} A)=$

**Options:**

- **(A)** $\left[\begin{array}{rrr}9 & -2 & 2 \\ 0 & 10 & -3 \\ 3 & -2 & 11\end{array}\right]$
- **(B)** $\left[\begin{array}{ccr}8 & -2 & 2 \\ 0 & 9 & -3 \\ 3 & -2 & 10\end{array}\right]$
- **(C)** $\left[\begin{array}{rrr}9 & -2 & 2 \\ 0 & 10 & -3 \\ 3 & -2 & 12\end{array}\right]$
- **(D)** $\left[\begin{array}{crr}3 & 2 & -2 \\ 0 & 10 & 3 \\ -3 & 2 & 12\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{rrr}9 & -2 & 2 \\ 0 & 10 & -3 \\ 3 & -2 & 12\end{array}\right]$**

**Detailed Solution:**

The determinant of matrix $A$ is given by:

$|A| = 1(8 - 6) - (-2)(0 - (-9)) + 2(0 - 6)$

$|A| = 1(2) + 2(9) + 2(-6) = 2 + 18 - 12 = 8$

Using the property of matrices, $A(\operatorname{adj} A) = |A|I$.

We need to find the value of $A(I + \operatorname{adj} A)$:

$A(I + \operatorname{adj} A) = AI + A(\operatorname{adj} A)$

$A(I + \operatorname{adj} A) = A + |A|I$

Substituting $|A| = 8$, we get:

$A + 8I = \left[\begin{array}{rrr}1 & -2 & 2 \\ 0 & 2 & -3 \\ 3 & -2 & 4\end{array}\right] + \left[\begin{array}{rrr}8 & 0 & 0 \\ 0 & 8 & 0 \\ 0 & 0 & 8\end{array}\right]$

$A + 8I = \left[\begin{array}{rrr}9 & -2 & 2 \\ 0 & 10 & -3 \\ 3 & -2 & 12\end{array}\right]$

Answer: $\left[\begin{array}{rrr}9 & -2 & 2 \\ 0 & 10 & -3 \\ 3 & -2 & 12\end{array}\right]$

</details>

---

### Q10. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}=\left[\begin{array}{cc}5 a & -\mathrm{b} \\ 3 & 2\end{array}\right]$ and A.adj $\mathrm{A}=\mathrm{AA}^{\mathrm{T}}$, then $5 a+\mathrm{b}=$

**Options:**

- **(A)** 7
- **(B)** 9
- **(C)** 13
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

Given $\mathrm{A} = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix}$

We know that $\mathrm{A} \cdot \text{adj}(\mathrm{A}) = |\mathrm{A}| \mathrm{I}$

$|\mathrm{A}| = (5a)(2) - (-b)(3) = 10a + 3b$

$\mathrm{A} \cdot \text{adj}(\mathrm{A}) = \begin{bmatrix} 10a + 3b & 0 \\ 0 & 10a + 3b \end{bmatrix}$

Now, calculate $\mathrm{A}\mathrm{A}^{\mathrm{T}}$:

$\mathrm{A}\mathrm{A}^{\mathrm{T}} = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix} \begin{bmatrix} 5a & 3 \\ -b & 2 \end{bmatrix} = \begin{bmatrix} 25a^2 + b^2 & 15a - 2b \\ 15a - 2b & 9 + 4 \end{bmatrix} = \begin{bmatrix} 25a^2 + b^2 & 15a - 2b \\ 15a - 2b & 13 \end{bmatrix}$

Since $\mathrm{A} \cdot \text{adj}(\mathrm{A}) = \mathrm{A}\mathrm{A}^{\mathrm{T}}$, we equate the corresponding elements:

$15a - 2b = 0 \Rightarrow b = \dfrac{15a}{2}$

$10a + 3b = 13$

Substituting $b = \dfrac{15a}{2}$ into the second equation:

$10a + 3\left(\dfrac{15a}{2}\right) = 13$

$\dfrac{20a + 45a}{2} = 13$

$\dfrac{65a}{2} = 13 \Rightarrow 65a = 26 \Rightarrow a = \dfrac{26}{65} = \dfrac{2}{5}$

Now, find $b$:

$b = \dfrac{15}{2} \times \dfrac{2}{5} = 3$

Therefore, $5a + b = 5\left(\dfrac{2}{5}\right) + 3 = 2 + 3 = 5$

Answer: 5

</details>

---

### Q11. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $A=\left[\begin{array}{rrr}1 & -1 & 1 \\ 0 & 2 & -3 \\ 2 & 1 & 0\end{array}\right], B=\operatorname{adj} A$ and $C=5 A$, then $\frac{|\operatorname{adj} B|}{|C|}=$

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** 1
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

The determinant of matrix $A$ is calculated as:

$|A| = 1(2 \times 0 - (-3) \times 1) - (-1)(0 \times 0 - (-3) \times 2) + 1(0 \times 1 - 2 \times 2)$

$|A| = 1(3) + 1(6) + 1(-4) = 3 + 6 - 4 = 5$

We are given $B = \operatorname{adj} A$. Using the property of determinants, $|\operatorname{adj} A| = |A|^{n-1}$, where $n$ is the order of the matrix. Here, $n = 3$.

$|B| = |\operatorname{adj} A| = |A|^{3-1} = |A|^2$

Now, we need to find $|\operatorname{adj} B|$:

$|\operatorname{adj} B| = |B|^{n-1} = |B|^2$

Substituting $|B| = |A|^2$, we get:

$|\operatorname{adj} B| = (|A|^2)^2 = |A|^4 = 5^4$

We are also given $C = 5A$. Using the property $|kA| = k^n|A|$:

$|C| = |5A| = 5^3|A| = 5^3 \times 5 = 5^4$

Finally, the required ratio is:

$\dfrac{|\operatorname{adj} B|}{|C|} = \dfrac{5^4}{5^4} = 1$

Answer: 1

</details>

---

### Q12. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be a non-singular matrix of order $n$ and $|A|=k$, then $(\operatorname{adj} A)^{-1}$ is

**Options:**

- **(A)** $\frac{\mathrm{A}}{\mathrm{k}}$
- **(B)** $\mathrm{k}^{\mathrm{n}-1}(\operatorname{adj} \mathrm{~A})$
- **(C)** $\mathrm{k}^{\mathrm{n}-2} \mathrm{~A}$
- **(D)** kA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{A}}{\mathrm{k}}$**

**Detailed Solution:**

We know that for a non-singular matrix $A$,

$A(\operatorname{adj} A) = |A|I$

Post-multiplying both sides by $(\operatorname{adj} A)^{-1}$, we get

$A(\operatorname{adj} A)(\operatorname{adj} A)^{-1} = |A|I(\operatorname{adj} A)^{-1}$

$A = |A|(\operatorname{adj} A)^{-1}$

Given $|A| = k$, substituting this value yields

$A = k(\operatorname{adj} A)^{-1}$

$(\operatorname{adj} A)^{-1} = \dfrac{A}{k}$

Answer: $\frac{\mathrm{A}}{\mathrm{k}}$

</details>

---

### Q13. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The third element in the second row of adjoint of a matrix $\mathrm{A}=\left[\mathrm{a}_{\mathrm{ij}}\right]_{3 \times 3}\left(\right.$ where $\left.\mathrm{a}_{\mathrm{ij}}=2 \mathrm{i}+\mathrm{j}\right)$ is

**Options:**

- **(A)** $2$
- **(B)** $-2$
- **(C)** $4$
- **(D)** $-4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4$**

**Detailed Solution:**

The elements of the matrix $A = [a_{ij}]_{3 \times 3}$ are given by $a_{ij} = 2i + j$.

Constructing the matrix $A$:
$a_{11} = 2(1) + 1 = 3$, $a_{12} = 2(1) + 2 = 4$, $a_{13} = 2(1) + 3 = 5$
$a_{21} = 2(2) + 1 = 5$, $a_{22} = 2(2) + 2 = 6$, $a_{23} = 2(2) + 3 = 7$
$a_{31} = 2(3) + 1 = 7$, $a_{32} = 2(3) + 2 = 8$, $a_{33} = 2(3) + 3 = 9$

Thus, $A = \begin{bmatrix} 3 & 4 & 5 \\ 5 & 6 & 7 \\ 7 & 8 & 9 \end{bmatrix}$.

The adjoint of matrix $A$, denoted as $\text{adj}(A)$, is the transpose of the cofactor matrix $C$.
The third element in the second row of $\text{adj}(A)$ corresponds to the element at position $(2, 3)$ in $\text{adj}(A)$.
Since $\text{adj}(A) = C^T$, the element at position $(2, 3)$ in $\text{adj}(A)$ is the element at position $(3, 2)$ in the cofactor matrix $C$, which is $C_{32}$.

The cofactor $C_{32}$ is given by $(-1)^{3+2} M_{32}$, where $M_{32}$ is the minor of $a_{32}$.
Deleting the third row and second column of $A$, we get the minor $M_{32}$:
$M_{32} = \begin{vmatrix} 3 & 5 \\ 5 & 7 \end{vmatrix} = (3 \times 7) - (5 \times 5) = 21 - 25 = -4$

Therefore, the cofactor is:
$C_{32} = -(-4) = 4$

Answer: $4$

</details>

---

### Q14. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}5 a & -b \\ 3 & 2\end{array}\right]$ and $A \cdot \operatorname{adj} A=AA^T$, then $5 \mathrm{a}+\mathrm{b}$ is equal to

**Options:**

- **(A)** -1
- **(B)** 5
- **(C)** 3
- **(D)** 13

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Given $A = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix}$.

We know that $A \cdot \operatorname{adj} A = |A| I$.

$|A| = (5a)(2) - (-b)(3) = 10a + 3b$

So, $A \cdot \operatorname{adj} A = \begin{bmatrix} 10a + 3b & 0 \\ 0 & 10a + 3b \end{bmatrix}$

Now, calculate $A A^T$:

$A A^T = \begin{bmatrix} 5a & -b \\ 3 & 2 \end{bmatrix} \begin{bmatrix} 5a & 3 \\ -b & 2 \end{bmatrix} = \begin{bmatrix} 25a^2 + b^2 & 15a - 2b \\ 15a - 2b & 13 \end{bmatrix}$

Since $A \cdot \operatorname{adj} A = A A^T$, we equate the corresponding elements:

$15a - 2b = 0 \Rightarrow b = \dfrac{15a}{2}$

$10a + 3b = 13$

Substituting the value of $b$ into the second equation:

$10a + 3\left(\dfrac{15a}{2}\right) = 13$

$10a + \dfrac{45a}{2} = 13$

$\dfrac{65a}{2} = 13 \Rightarrow a = \dfrac{26}{65} = \dfrac{2}{5}$

Now, find $b$:

$b = \dfrac{15}{2} \times \dfrac{2}{5} = 3$

Therefore, the value of $5a + b$ is:

$5a + b = 5\left(\dfrac{2}{5}\right) + 3 = 2 + 3 = 5$

Answer: 5

</details>

---

### Q15. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{cc}2 & -1 \\ 0 & 2\end{array}\right]$.
If $\mathrm{B}=\mathrm{I}-{ }^3 \mathrm{C}_1(\operatorname{adj} \mathrm{A})+{ }^3 \mathrm{C}_2(\operatorname{adj} \mathrm{A})^2-{ }^3 \mathrm{C}_3(\operatorname{adj} \mathrm{A})^3$, then the sum of all elements of the matrix $B$ is

**Options:**

- **(A)** $-1$
- **(B)** $-3$
- **(C)** $-4$
- **(D)** $-5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-5$**

**Detailed Solution:**

$$
\begin{aligned}
\mathrm{B} & =\mathrm{I}-{ }^3 \mathrm{C}_1(\operatorname{adj} \mathrm{A})+{ }^3 \mathrm{C}_2(\operatorname{adj} \mathrm{A})^2-{ }^3 \mathrm{C}_3(\operatorname{adj} \mathrm{A})^3 \\
& =\mathrm{I}-3 \operatorname{adj} \mathrm{A}+3(\operatorname{adj} \mathrm{A})^2-1(\operatorname{adj} \mathrm{A})^3 \\
& =(\mathrm{I}-\operatorname{adj} \mathrm{A})^3 \\
\operatorname{adj} \mathrm{A} & =\left[\begin{array}{ll}
2 & 1 \\
0 & 2
\end{array}\right] \\
\therefore \quad \mathrm{B} & =\left(\left[\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right]-\left[\begin{array}{ll}
2 & 1 \\
0 & 2
\end{array}\right]\right)^3 \\
& =\left[\begin{array}{rr}
-1 & -1 \\
0 & -1
\end{array}\right] \\
& =\left[\begin{array}{rr}
-1 & -1 \\
0 & -1
\end{array}\right]\left[\begin{array}{rr}
-1 & -1 \\
0 & -1
\end{array}\right]\left[\begin{array}{cc}
-1 & -1 \\
0 & -1
\end{array}\right] \\
& =\left[\begin{array}{rr}
1 & 2 \\
0 & 1
\end{array}\right]\left[\begin{array}{rr}
-1 & -1 \\
0 & -1
\end{array}\right] \\
& =\left[\begin{array}{rr}
-1 & -3 \\
0 & -1
\end{array}\right]
\end{aligned}
$$

Sum of all elements of the matrix B $=-1-3-1=-5$

</details>

---

### Q16. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 2 & 3 \\ -1 & 1 & 2 \\ 1 & 2 & 4\end{array}\right]$ and $A_{i j}$ is a cofactor of $a_{i j}$, then the value of $a_{21} A_{21}+a_{22} A_{22}+a_{23} A_{23}$ is

**Options:**

- **(A)** 0
- **(B)** -2
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} & \mathrm{a}_{21}=-1, \mathrm{a}_{22}=1, \mathrm{a}_{23}=2 \\ & \mathrm{~A}_{21}=(-1)^{2+1}\left|\begin{array}{ll}2 & 3 \\ 2 & 4\end{array}\right|=(-1)(2)=-2 \\ & \mathrm{~A}_{22}=(-1)^{2+2}\left|\begin{array}{ll}1 & 3 \\ 1 & 4\end{array}\right|=1(1)=1 \\ & \quad \mathrm{~A}_{23}=(-1)^{2+3}\left|\begin{array}{ll}1 & 2 \\ 1 & 2\end{array}\right|=(-1)(0)=0 \\ & \therefore \quad \mathrm{a}_{21} \mathrm{~A}_{21}+\mathrm{a}_{22} \mathrm{~A}_{22}+\mathrm{a}_{23} \mathrm{~A}_{23}=(-1)(-2)+1(1)+2(0) \\ &=3\end{aligned}$

</details>

---

### Q17. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $P=\left[\begin{array}{lll}1 & \alpha & 3 \\ 1 & 3 & 3 \\ 2 & 4 & 4\end{array}\right]$ is the adjoint of a $3 \times 3$ matrix A and $|A|=4$, then value of $\alpha$ is

**Options:**

- **(A)** $4$
- **(B)** $11$
- **(C)** $5$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $11$**

**Detailed Solution:**

$\begin{aligned} & P=\operatorname{adj} A \\ \therefore \quad & |\mathrm{P}|=|\mathrm{A}|^2 \\ & \Rightarrow\left|\begin{array}{lll}1 & \alpha & 3 \\ 1 & 3 & 3 \\ 2 & 4 & 4\end{array}\right|=4^2 \\ & \Rightarrow 2 \alpha-6=16 \\ & \Rightarrow \alpha=11\end{aligned}$

</details>

---

### Q18. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $B=\left[\begin{array}{ccc}3 & \alpha & -1 \\ 1 & 3 & 1 \\ -1 & 1 & 3\end{array}\right]$ is the adjoint of $a$ $3 \times 3$ matrix $\mathrm{A}$ and $|\mathrm{A}|=4$, then $\alpha$ is equal to8

**Options:**

- **(A)** $1$
- **(B)** $0$
- **(C)** $-1$
- **(D)** $-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

$\begin{aligned}
& \quad \text { Using }|\operatorname{adj} A|=|A|^{\mathrm{n}-1} \\
& \quad \text { But } \mathrm{B}=\operatorname{Adj}(\mathrm{A}) ...[Given]\\
& \therefore \quad|\mathrm{B}|=|\mathrm{A}|^2 \\
& \Rightarrow\left|\begin{array}{ccc}
3 & \alpha & -1 \\
1 & 3 & 1 \\
-1 & 1 & 3
\end{array}\right|=|\mathrm{A}|^2 \\
& \Rightarrow 24-4 \alpha-4=4^2 \\
& \Rightarrow 20-4 \alpha=16 \\
& \Rightarrow \alpha=1
\end{aligned}$

</details>

---

### Q19. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $B=\left[\begin{array}{lll}1 & \alpha & 2 \\ 1 & 2 & 2 \\ 2 & 3 & 3\end{array}\right]$ is the adjoint of a $3 \times 3$ matrix $\mathrm{A}$ and $|\mathrm{A}|=5$, then $\alpha$ is equal to

**Options:**

- **(A)** 25
- **(B)** 27
- **(C)** $3 \sqrt{3}$
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 27**

**Detailed Solution:**

Using $|\operatorname{Adj} A|=|A|^{n-1}$
But $\mathrm{B}=\operatorname{Adj}(\mathrm{A})$...['Given]
$\therefore \quad|\mathrm{B}|=|\mathrm{A}|^2$
$\begin{aligned} & \Rightarrow\left|\begin{array}{lll}1 & \alpha & 2 \\ 1 & 2 & 2 \\ 2 & 3 & 3\end{array}\right|=|\mathrm{A}|^2 \\ & \Rightarrow \alpha-2=5^2 \\ & \Rightarrow \alpha-2=25 \\ & \Rightarrow \alpha=27\end{aligned}$

</details>

---

### Q20. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{cc}2 & -3 \\ 4 & 1\end{array}\right]$, then $A+\operatorname{adj} A$ is

**Options:**

- **(A)** $\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}1 & 3 \\ -4 & 2\end{array}\right]$
- **(C)** $\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}1 & -3 \\ 4 & 2\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$**

**Detailed Solution:**

$A+\operatorname{adj}(A)=\left[\begin{array}{cc}2 & -3 \\ 4 & 1\end{array}\right]+\left[\begin{array}{cc}1 & 3 \\ -4 & 2\end{array}\right]=\left[\begin{array}{ll}3 & 0 \\ 0 & 3\end{array}\right]$

</details>

---

### Q21. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $|A|=-3$ and $A^{-1}=\left[\begin{array}{ccc}1 & 0 & 0 \\ -1 & \frac{1}{3} & 0 \\ 3 & \frac{2}{3} & -1\end{array}\right]$, then $(\operatorname{adj} A)$ is

**Options:**

- **(A)** $\left[\begin{array}{ccc}-3 & 0 & 0 \\ 3 & -1 & 0 \\ -9 & -2 & 3\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}-\frac{1}{3} & 0 & 0 \\ \frac{1}{3} & -\frac{1}{9} & 0 \\ 1 & -\frac{2}{9} & \frac{1}{3}\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}3 & 0 & 0 \\ -3 & 1 & 0 \\ 9 & 2 & -3\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}\frac{1}{3} & 0 & 0 \\ -\frac{1}{3} & \frac{1}{9} & 0 \\ -1 & \frac{2}{9} & -\frac{1}{3}\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{ccc}-3 & 0 & 0 \\ 3 & -1 & 0 \\ -9 & -2 & 3\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \because A^{-1}=\frac{\operatorname{adj}(A)}{|A|} \\ & \Rightarrow \operatorname{adj}(A)=|A| A^{-1}=\left[\begin{array}{ccc}-3 & 0 & 0 \\ 3 & -1 & 0 \\ -9 & -2 & 3\end{array}\right]\end{aligned}$

</details>

---

### Q22. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}2 & 3 \\ -4 & 1\end{array}\right]$, then adj $\left(3 A^2+12 A\right)$ is equal to

**Options:**

- **(A)** $\left[\begin{array}{cc}-21 & 63 \\ 84 & 0\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}21 & 63 \\ 84 & 0\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}21 & -63 \\ 84 & 0\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}-21 & -63 \\ 84 & 0\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}-21 & -63 \\ 84 & 0\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & 3 A^2+12 A=3\left[\begin{array}{cc}2 & 3 \\ -4 & 1\end{array}\right]^2+12 \\ & =3\left[\begin{array}{cc}-8 & 9 \\ -12 & -11\end{array}\right]+12\left[\begin{array}{cc}2 & 3 \\ -4 & 1\end{array}\right] \\ & =\left[\begin{array}{cc}-24+24 & 27+36 \\ -36-48 & -33+12\end{array}\right] \\ & =\left[\begin{array}{cc}0 & 63 \\ -84 & -21\end{array}\right] \\ & \Rightarrow \operatorname{adj}\left(3 A^2+12 A\right)=\left[\begin{array}{cc}-21 & -63 \\ 84 & 0\end{array}\right]\end{aligned}$

</details>

---

### Q23. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 0 & 2 & -3 \\ 2 & 1 & 3\end{array}\right]$ and $B=\operatorname{adj} A, C=54$, then $\frac{|\operatorname{adj} B|}{|C|}=$

**Options:**

- **(A)** 5
- **(B)** 25
- **(C)** -1
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$\begin{aligned} & A=\left|\begin{array}{ccc}1 & -1 & 1 \\ 0 & 2 & -3 \\ 2 & 1 & 0\end{array}\right| \\ & \Rightarrow|A|=1 \times(0+3)+1 \times(0+6)+1 \times(0-4)=5 \\ & \because B=\operatorname{adj} A \\ & \Rightarrow|B|=|\operatorname{adj} A|=|A|^2=25 \\ & \Rightarrow|\operatorname{adj} B|=|B|^2=625 \\ & \because C=5 A \\ & \Rightarrow|C|=|5 A|=5^3|A|=125 \times 5=625 \\ & \text { now } \frac{|\operatorname{adj} B|}{|C|}=\frac{625}{625}=1\end{aligned}$

</details>

---

### Q24. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right]$, adj $A=\left[\begin{array}{ccc}4 & -1 & 1 \\ 8 & -7 & a \\ 9 & -6 & b\end{array}\right]$, then

**Options:**

- **(A)** $a=2, b=-1$
- **(B)** $a=2, b=1$
- **(C)** $a=-2, b=1$
- **(D)** $a=1, b=-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $a=2, b=1$**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right], \operatorname{adj} A=\left[\begin{array}{lll}4 & -1 & 1 \\ 8 & -7 & a \\ 9 & -6 & b\end{array}\right] \\ & \text { now, } A \cdot \operatorname{adj} A=\left[\begin{array}{ccc}5 & 0 & 1-a+b \\ 0 & 5 & 2-a \\ 0 & 0 & 3+3 a-4 b\end{array}\right]=|A| . \mathrm{I} \\ & \Rightarrow 1-a+b=0 \text { and } 2-a=0 \\ & \Rightarrow a=2 \text { and } b=1\end{aligned}$

</details>

---

### Q25. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given $\mathrm{A}=\left[\begin{array}{lll}x & 3 & 2 \\ 1 & y & 4 \\ 2 & 2 & z\end{array}\right], x y z=60$ and $8 x+4 y+3 z=20$, then $\mathrm{A} \cdot(\operatorname{adjA})$ is equal to

**Options:**

- **(A)** $\left[\begin{array}{ccc}60 & 0 & 0 \\ 0 & 60 & 0 \\ 0 & 0 & 60\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}20 & 0 & 0 \\ 0 & 20 & 0 \\ 0 & 0 & 20\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}68 & 0 & 0 \\ 0 & 68 & 0 \\ 0 & 0 & 68\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}108 & 0 & 0 \\ 0 & 108 & 0 \\ 0 & 0 & 108\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{ccc}68 & 0 & 0 \\ 0 & 68 & 0 \\ 0 & 0 & 68\end{array}\right]$**

**Detailed Solution:**

$$
\begin{aligned}
& |A|=x(y z-8)+3(8-z)+2(2-2 y) \\
& =x y z-8 x+24-3 z+4-4 y \\
& =x y z-(8 x+4 y+3 z)+28 \\
& =60-20+28 \\
& =68
\end{aligned}
$$
we have, $A \cdot \operatorname{adj}(A)=|A| I=\left[\begin{array}{ccc}68 & 0 & 0 \\ 0 & 68 & 0 \\ 0 & 0 & 68\end{array}\right]$

</details>

---

### Q26. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{cc}2 & -3 \\ -4 & 1\end{array}\right]$, then adj $\left(3 A^2+12 A\right)$ is equal to

**Options:**

- **(A)** $\left[\begin{array}{cc}72 & -63 \\ -84 & 51\end{array}\right]$
- **(B)** $\left[\begin{array}{ll}51 & 63 \\ 84 & 72\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}72 & -84 \\ -63 & 51\end{array}\right]$
- **(D)** $\left[\begin{array}{ll}51 & 84 \\ 63 & 72\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{ll}51 & 63 \\ 84 & 72\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \operatorname{adj}\left(3 \mathrm{~A}^2+12 \mathrm{~A}\right)=\operatorname{adj}\{3 \mathrm{~A}(\mathrm{~A}+4 \mathrm{I})\} \\ & =\operatorname{adj}(\mathrm{A}+4 \mathrm{I}) \cdot \operatorname{adj}(3 \mathrm{~A}) \\ & =\operatorname{adj}\left(\left[\begin{array}{cc}6 & -3 \\ -4 & 5\end{array}\right]\right) \cdot \operatorname{adj}\left(\left[\begin{array}{cc}6 & -9 \\ -12 & 3\end{array}\right]\right) \\ & =\left[\begin{array}{ll}5 & 3 \\ 4 & 6\end{array}\right]\left[\begin{array}{cc}3 & 9 \\ 12 & 6\end{array}\right] \\ & =\left[\begin{array}{ll}51 & 63 \\ 84 & 72\end{array}\right]\end{aligned}$

</details>

---

### Q27. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 3 & -2 \\ -3 & 0 & -5 \\ 2 & 5 & 0\end{array}\right]$ and $A(\operatorname{adj} A)=K I$, then the value of $K$ is (where $I$ is unit matrix of order 3)

**Options:**

- **(A)** $-25$
- **(B)** $25$
- **(C)** $85$
- **(D)** $-85$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $25$**

**Detailed Solution:**

$$
\because A(\operatorname{adj} A)=|A| . I
$$
Hence $\mathrm{K}=|\mathrm{A}|=25$

</details>

---

### Q28. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 2 & 3 \\ -1 & 1 & 2 \\ 1 & 2 & 4\end{array}\right]$, and $A(\operatorname{adj} A)=k I$, then the value of $(k+1)^4$ is

**Options:**

- **(A)** 256
- **(B)** 81
- **(C)** 16
- **(D)** 625

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 256**

**Detailed Solution:**

$|A|=\left|\begin{array}{ccc}
1 & 2 & 3 \\
-1 & 1 & 2 \\
1 & 2 & 4
\end{array}\right|=1(0)-2(-6)+3(-3)=3$
We know that $\mathrm{A}(\operatorname{adj} \mathrm{A})=|\mathrm{A}| \mathrm{I}$
$\begin{aligned}
& \therefore \mathrm{A}(\operatorname{adj} \mathrm{A})=3 \mathrm{I} \Rightarrow \mathrm{k}=3 \\
& (\mathrm{k}+1)^4=(3+1)^4=256
\end{aligned}$

</details>

---

### Q29. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ccc}1 & 2 & 3 \\ -1 & 1 & 2 \\ 1 & 2 & 4\end{array}\right]$, then $A(\operatorname{adj} A)=$

**Options:**

- **(A)** $\left[\begin{array}{ccc}-1 / 3 & 0 & 0 \\ 0 & -1 / 3 & 0 \\ 0 & & -1 / 3\end{array}\right]$
- **(B)** $\left[\begin{array}{lll}3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}1 & 2 & 3 \\ -1 & 1 & 2 \\ 1 & 2 & 4\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & 1 & 2 \\ 3 & 2 & 4\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[\begin{array}{lll}3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3\end{array}\right]$**

**Detailed Solution:**

$$
\begin{aligned}
& A=\left[\begin{array}{ccc}
1 & 2 & 3 \\
-1 & 1 & 2 \\
1 & 2 & 4
\end{array}\right] \\
& \therefore|A|=1(4,-4)-2(-4-2)+3(-2-1)=12-9=3
\end{aligned}
$$
We know that $\mathrm{A}(\operatorname{adj} \mathrm{A})=|\mathrm{A}| \mathrm{I}$
$$
\therefore A(\operatorname{adj} A)=3\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]=\left[\begin{array}{lll}
3 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 3
\end{array}\right]
$$

</details>

---

### Q30. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a $3 \times 3$ matrix A, if $\mathrm{A}(\operatorname{adj} \mathrm{A})=\left[\begin{array}{ccc}-10 & 0 & 0 \\ 0 & -10 & 2 \\ 0 & 0 & -10\end{array}\right]$, then the value of determinant of $\mathrm{A}$ is

**Options:**

- **(A)** 100
- **(B)** -1000
- **(C)** -10
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -10**

**Detailed Solution:**

$\begin{aligned} & \text { We have }|\mathrm{A}(\operatorname{adj} \mathrm{A})|=\left[\begin{array}{ccc}-10 & 0 & 0 \\ 0 & -10 & 2 \\ 0 & 0 & -10\end{array}\right] \\ & \therefore|\mathrm{A}||\operatorname{adj} \mathrm{A}|=(-10)(100)=-1000 \\ & \therefore|\mathrm{A}||\mathrm{A}|^{3-1}=-1000 \Rightarrow|\mathrm{A}|^3=-1000 \Rightarrow|\mathrm{A}|=-10\end{aligned}$

</details>

---

### Q31. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{A}\left[\begin{array}{cc}5 \mathrm{a} & -\mathrm{b} \\ 3 & 2\end{array}\right]$ and $\mathrm{A}$ adj $\mathrm{A}=\mathrm{AA}^{\mathrm{T}}$, then $5 \mathrm{a}+\mathrm{b}=$

**Options:**

- **(A)** 13
- **(B)** 4
- **(C)** -1
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$$
\begin{aligned}
& \text { We have } \mathrm{A}\left[\begin{array}{cc}
5 \mathrm{a} & -\mathrm{b} \\
3 & 2
\end{array}\right] \text { and } \mathrm{A} \operatorname{adj} \mathrm{A}=\mathrm{AA}^{\mathrm{T}} \\
& \therefore\left[\begin{array}{cc}
5 \mathrm{a} & -\mathrm{b} \\
3 & 2
\end{array}\right]\left[\begin{array}{cc}
2 & \mathrm{~b} \\
-3 & 5 \mathrm{a}
\end{array}\right]=\left[\begin{array}{cc}
5 \mathrm{a} & -\mathrm{b} \\
3 & 2
\end{array}\right]\left[\begin{array}{cc}
5 \mathrm{a} & 3 \\
-\mathrm{b} & 2
\end{array}\right] \\
& {\left[\begin{array}{cc}
10 \mathrm{a}+3 \mathrm{~b} & 0 \\
0 & 10 \mathrm{a}+3 \mathrm{~b}
\end{array}\right]=\left[\begin{array}{cc}
25 \mathrm{a}^2+\mathrm{b}^2 & 15 \mathrm{a}-2 \mathrm{~b} \\
15 \mathrm{a}-2 \mathrm{~b} & 9+4
\end{array}\right]} \\
& \therefore 10 \mathrm{a}+3 \mathrm{~b}=13 \text { and } 15 \mathrm{a}-2 \mathrm{~b}=0
\end{aligned}
$$
Solving these equations, we get $a=\frac{2}{5}$ and $b=3$
$$
\therefore 5 a+b=2+3=5
$$

</details>

---

### Q32. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For an invertible matrix $A$, if $A(\operatorname{adj} A)=\left[\begin{array}{cc}20 & 0 \\ 0 & 20\end{array}\right]$, then $|A|=$

**Options:**

- **(A)** -200
- **(B)** 200
- **(C)** -2
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 20**

**Detailed Solution:**

$\begin{aligned} & \text { We have } \mathrm{A}(\operatorname{adj} \mathrm{A})=\left[\begin{array}{cc}20 & 0 \\ 0 & 20\end{array}\right] \\ & \therefore|\mathrm{A}||\operatorname{adj} \mathrm{A}|=\left[\begin{array}{cc}20 & 0 \\ 0 & 20\end{array}\right] \Rightarrow|\mathrm{A}|\left(|\mathrm{A}|^{2-1}\right)=400 \Rightarrow(|\mathrm{A}|)^2=(20)^2 \\ & \Rightarrow|\mathrm{A}|=20\end{aligned}$

</details>

---

### Q33. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}\cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$, then $\operatorname{adj} A=$

**Options:**

- **(A)** $\left[\begin{array}{ccc}-\cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$
- **(B)** $\left[\begin{array}{ccc}\cos \theta & \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{ccc}\cos \theta & \sin \theta & 0 \\ -\sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$
- **(D)** $\left[\begin{array}{ccc}\cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\begin{array}{ccc}\cos \theta & \sin \theta & 0 \\ -\sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{ccc}\cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right] \\ & \therefore \operatorname{adj} A=\left[\begin{array}{ccc}\cos \theta & -\sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]=\left[\begin{array}{ccc}\cos \theta & \sin \theta & 0 \\ -\sin \theta & \cos \theta & 0 \\ 0 & 0 & 1\end{array}\right]\end{aligned}$

</details>

---

### Q34. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 0 & 2 \\ -1 & 1 & -2 \\ 0 & 2 & 1\end{array}\right]$, adj $A=\left[\begin{array}{ccc}5 & x & -2 \\ 1 & 1 & 0 \\ -2 & -2 & y\end{array}\right]$, then value of $\mathrm{x}+\mathrm{y}$ is

**Options:**

- **(A)** 6
- **(B)** 3
- **(C)** 4
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5**

**Detailed Solution:**

$x$ is element $a_{12}$ in adj (A)
$\therefore \mathrm{x}=$ cofactor of $\mathrm{a}_{21}=(-1)^{2+1}\left|\begin{array}{ll}0 & 2 \\ 2 & 1\end{array}\right|=-(-4)=4$
Similarly, $y=(-1)^{3+3}\left|\begin{array}{cc}1 & 0 \\ -1 & 1\end{array}\right|=1 \Rightarrow x+y=5$

</details>

---

### Q35. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$A(\propto)\left[\begin{array}{cc}\cos \propto & \sin \propto \\ -\sin \propto & \cos \propto\end{array}\right]$, then $\left[A^2(\propto)\right]^{-1}=$

**Options:**

- **(A)** $A(\propto)$
- **(B)** $\mathrm{A}^2(\propto)$
- **(C)** $A(-2 \propto)$
- **(D)** $A(2 \propto c)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $A(-2 \propto)$**

**Detailed Solution:**

$\begin{aligned} & A(\alpha)=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right] \Rightarrow|\mathrm{A}(\alpha)|=\cos ^2 \alpha+\sin ^2 \alpha=1 \\ & \mathrm{~A}^2(\alpha)=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right] \\ & {\left[\begin{array}{cc}\cos ^2 \alpha-\sin ^2 \alpha & 2 \sin \alpha \cos \alpha \\ -\sin \alpha \cos \alpha & \cos ^2 \alpha-\sin ^2 \alpha\end{array}\right]=\left[\begin{array}{cc}\cos \alpha & \sin \alpha \\ -\sin \alpha & \cos \alpha\end{array}\right]} \\ & \therefore \operatorname{adj}\left[\mathrm{A}^2(\alpha)\right]\left[\begin{array}{cc}\cos 2 \alpha & -\sin 2 \alpha \\ \sin 2 \alpha & \cos 2 \alpha\end{array}\right] \\ & \therefore\left[\mathrm{A}^2(\alpha)\right]^{-1}=\left[\begin{array}{cc}\cos 2 \alpha & -\sin 2 \alpha \\ \sin 2 \alpha & \cos 2 \alpha\end{array}\right] \quad \ldots\left[\because\left|\mathrm{A}^2\right|=|\mathrm{A}|^2=1\right] \\ & \therefore\left[\mathrm{A}^2(\alpha)\right]^{-1}=\left[\begin{array}{cc}\cos (-2 \alpha) & \sin (-2 \alpha) \\ -\sin (-2 \alpha) & \cos (-2 \alpha)\end{array}\right]=\mathrm{A}(-2 \alpha)\end{aligned}$

</details>

---

### Q36. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The cofactors of the elements of the first column of the matrix $A=\left[\begin{array}{ccc}2 & 0 & -1 \\ 3 & 1 & 2 \\ -1 & 1 & 2\end{array}\right]$
are

**Options:**

- **(A)** $0,-7,2$
- **(B)** $0,-1,1$
- **(C)** $0,-8,4$
- **(D)** $-1,3,-2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0,-1,1$**

**Detailed Solution:**

(B)
We know,
$\begin{array}{l}
C_{i j}=(-1)^{i+j} \times M_{i j} \\
C_{11}=(-1)^{111} \times\left|\begin{array}{ll}
1 & 2 \\
1 & 2
\end{array}\right|=(-1)^{2} \times 0=0 \\
C_{21}=(-1)^{2+1} \times\left|\begin{array}{cc}
0 & -1 \\
1 & 2
\end{array}\right|=(-1)^{3} \times(1)=-1 \\
C_{31}=(-1)^{3+1} \times\left|\begin{array}{cc}
0 & -1 \\
1 & 2
\end{array}\right|=(-1)^{4} \times(1)=1
\end{array}$

</details>

---

### Q37. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the cofactors of the elements of second row of the matrix $\left[\begin{array}{ccc}1 & 3 & 2 \\ -2 & 0 & 1 \\ 5 & 2 &1\end{array}\right]$ is

**Options:**

- **(A)** 23
- **(B)** 3
- **(C)** 5
- **(D)** -23

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

(B)
Co-factors of second row of matrix are
$\begin{array}{l}
A_{21}=(-1)^{2+1}\left|\begin{array}{ll}
3 & 2 \\
2 & 1
\end{array}\right|=(-1)^{3}(-1)=1 \\
A_{22}=(-1)^{2+2}\left|\begin{array}{ll}
1 & 2 \\
5 & 1
\end{array}\right|=(-1)^{4}(-9)=-9 \\
A_{23}=(-1)^{2+3}\left[\begin{array}{ll}
1 & 3 \\
5 & 2
\end{array}\right]=(-1)^{5}(-13)=13 \\
\text { Their sum }=A_{21}+A_{12}+A_{23}=1-9+13=5
\end{array}$

</details>

---

### Q38. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The adjoint of the matrix $A=\left[\begin{array}{cc}2 & -3 \\ 3 & 5\end{array}\right]$ is

**Options:**

- **(A)** $\left[\begin{array}{cc}5 & 3 \\ -3 & 2\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}5 & -3 \\ 3 & 2\end{array}\right]$
- **(C)** $\frac{1}{19}\left[\begin{array}{cc}5 & 3 \\ -3 & 2\end{array}\right]$
- **(D)** $\frac{1}{19}\left[\begin{array}{cc}5 & -3 \\ 3 & 2\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left[\begin{array}{cc}5 & 3 \\ -3 & 2\end{array}\right]$**

**Detailed Solution:**

Given $A=\left[\begin{array}{cc}2 & -3 \\ 3 & 5\end{array}\right] \Rightarrow \operatorname{Adj} A=\left[\begin{array}{cc}5 & 3 \\ -3 & 2\end{array}\right]$

</details>

---

### Q39. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{lll}1 & 2 & i \\ 1 & 1 & 1 \\ 1 & 1 & 0\end{array}\right]$, then $[\operatorname{adj}(\operatorname{adj} A)]^{-1}=$

**Options:**

- **(A)** $A^{2}$
- **(B)** $2 \mathrm{~A}$
- **(C)** $\mathrm{A}^{-1}$
- **(D)** I

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A}^{-1}$**

**Detailed Solution:**

We have $|A|=\left[\begin{array}{lll}1 & 2 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 0\end{array}\right]$
$\quad=1(0-1)-2(0-1)+i(0)$
$\quad=-1+2=1$
$\begin{aligned} \text { Adj(Adj A) } &=|A|^{n-2} A \\ \text { Now [adj (adj A)] }^{-1} &=\left[|A|^{p-2} A\right]^{-1} \\ &=\left[(1)^{3-2} A\right]^{-1}=A^{-1} \end{aligned}$

</details>

---

### Q40. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mtd></mtr></mtable></mrow></mfenced></math> where <math><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math> , then A (adj A) = ….

**Options:**

- **(A)** -2 <math><mi></mi><mi>l</mi></math>
- **(B)** 2 <math><mi></mi><mi>l</mi></math>
- **(C)** 5 <math><mi>l</mi></math>
- **(D)** 4 <math><mi>l</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4 <math><mi>l</mi></math>**

**Detailed Solution:**

<math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mtd></mtr></mtable></mrow></mfenced></math>  
<math><mo>∴</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>i</mi></mrow></mfenced><mo>+</mo><msup><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>=</mo><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>i</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn></math>  
<math><mo>∴</mo><mi>A</mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mfenced close="|" open="|" separators="|"><mrow><mo>=</mo><mn>4</mn></mrow></mfenced></math>

</details>

---

### Q41. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

Matrix <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>7</mn></mtd></mtr></mtable></mrow></mfenced></math> then the value of <math><msub><mrow><mi>a</mi></mrow><mrow><mn>31</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>31</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>32</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>32</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>33</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>33</mn></mrow></msub></math> is

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>13</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mo>-</mo><mn>13</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>1</mn></math>**

**Detailed Solution:**

We know that <math> <mrow> <msub> <mi>a</mi> <mrow> <mn>31</mn></mrow> </msub> <msub> <mi>A</mi> <mrow> <mn>31</mn></mrow> </msub> <mo>+</mo><msub> <mi>a</mi> <mrow> <mn>32</mn></mrow> </msub> <msub> <mi>A</mi> <mrow> <mn>32</mn></mrow> </msub> <mo>+</mo><msub> <mi>a</mi> <mrow> <mn>33</mn></mrow> </msub> <msub> <mi>A</mi> <mrow> <mn>33</mn></mrow> </msub> <mo>=</mo><mrow><mo>|</mo> <mi>A</mi> <mo>|</mo></mrow></mrow> </math>
Now <math> <mrow> <mrow><mo>|</mo> <mi>A</mi> <mo>|</mo></mrow><mo>=</mo><mn>1</mn><mrow><mo>(</mo> <mrow> <mn>7</mn><mo>−</mo><mn>20</mn></mrow> <mo>)</mo></mrow><mo>−</mo><mn>2</mn><mrow><mo>(</mo> <mrow> <mn>7</mn><mo>−</mo><mn>10</mn></mrow> <mo>)</mo></mrow><mo>+</mo><mn>3</mn><mrow><mo>(</mo> <mrow> <mn>4</mn><mo>−</mo><mn>2</mn></mrow> <mo>)</mo></mrow></mrow> </math>
<math> <mrow> <mo>=</mo><mo>−</mo><mn>13</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>6</mn></mrow> </math>
<math> <mrow> <mo>=</mo><mo>−</mo><mn>1</mn></mrow> </math>

</details>

---

### Q42. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

For a invertible matrix <math> <mi>A</mi> </math> if <math> <mi>A</mi> </math> <math> <mrow> <mrow><mo>(</mo> <mrow> <mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi> </mrow> <mo>)</mo></mrow><mo>=</mo><mrow><mo>[</mo> <mrow> <mtable> <mtr> <mtd> <mrow> <mn>10</mn> </mrow> </mtd> <mtd> <mn>0</mn> </mtd> </mtr> <mtr> <mtd> <mn>0</mn> </mtd> <mtd> <mrow> <mn>10</mn> </mrow> </mtd> </mtr> </mtable> </mrow> <mo>]</mo></mrow> </mrow><mo>,</mo> </math> then <math> <mrow> <mrow><mo>|</mo> <mi>A</mi> <mo>|</mo></mrow><mo>=</mo> </mrow> </math>

**Options:**

- **(A)** <math > <mrow>  <mn>100</mn> </mrow></math>
- **(B)** <math > <mrow> <mo>-</mo> <mn>100</mn> </mrow></math>
- **(C)** <math > <mrow>  <mn>10</mn> </mrow></math>
- **(D)** <math > <mrow> <mo>-</mo> <mn>10</mn> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math > <mrow>  <mn>10</mn> </mrow></math>**

**Detailed Solution:**

Given that <math> <mrow> <mi>A</mi><mrow><mo>(</mo> <mrow> <mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi> </mrow> <mo>)</mo></mrow> </mrow> </math> <math><mo>=</mo></math> <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>10</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>10</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>10</mn><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>10</mn><mi> </mi><mi>I</mi></math>
We know that <math > <mrow>  <mi>A</mi><mrow><mo>(</mo>   <mrow>    <mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi>   </mrow>  <mo>)</mo></mrow> </mrow></math> <math><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mi> </mi><mi>I</mi></math>
<math><mo>⇒</mo><mi> </mi><mi> </mi><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mn>10</mn></math>

</details>

---

### Q43. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>,</mo></math> then <math><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>21</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>12</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>22</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>23</mn></mrow></msub><mo>=</mo></math> _______

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>0</mn></math>**

**Detailed Solution:**

Here,
<math><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></math>  stands for element of matrix <math><mi>A</mi></math> in <math><msup><mrow><mi>i</mi></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> row and <math><msup><mrow><mi>j</mi></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> column, and <math><msub><mrow><mi>A</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></math> stands for co-factor of element <math><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></math> of matrix <math><mi>A</mi></math> .
<math><mo>∴</mo><mi> </mi><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><msub><mrow><mi>a</mi></mrow><mrow><mn>12</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow></msub><mo>=</mo><mn>0</mn></math>
And
<math><msub><mrow><mi>A</mi></mrow><mrow><mn>21</mn></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></msup><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
<math><msub><mrow><mi>A</mi></mrow><mrow><mn>22</mn></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>2</mn></mrow></msup><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>1</mn></math>
<math><msub><mrow><mi>A</mi></mrow><mrow><mn>23</mn></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow></msup><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math>
Therefore
<math><msub><mrow><mi>a</mi></mrow><mrow><mn>11</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>21</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>12</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>22</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>13</mn></mrow></msub><msub><mrow><mi>A</mi></mrow><mrow><mn>23</mn></mrow></msub><mo>=</mo><mn>1</mn><mo>×</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>×</mo><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced><mo>+</mo><mn>0</mn><mo>×</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

</details>

---

### Q44. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

If $A$ is a square matrix of order $n \times n$, then $\operatorname{adj}(\operatorname{adj} A)$ is equal to

**Options:**

- **(A)** | $\left.A\right|^{n} A$
- **(B)** $|A|^{n-1} A$
- **(C)** $|A|^{n-2} A$
- **(D)** $|A|^{n-3} A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $|A|^{n-2} A$**

**Detailed Solution:**

For any square matrix $B$, we have $B(\operatorname{adj} B)=|B| I_{n}$
On taking $B=\operatorname{adj} A$, we get $(\operatorname{adj} A)[\operatorname{adj}(\operatorname{adj} A)]=|\operatorname{adj} A| I_{n}$
$$
\Rightarrow \quad \operatorname{adj} A[\operatorname{adj}(\operatorname{adj} A)]=|A|^{n-1} I_{n}
$$
$\left(\because|\operatorname{adj} A|=|A|^{n-1}\right)$
$\Rightarrow(A \operatorname{adj} A)[\operatorname{adj}(\operatorname{adj} A)]=|A|^{n-1} A$
$\Rightarrow\left(|A| I_{n}\right)[\operatorname{adj}(\operatorname{adj} A)]=|A|^{n-1} A$
$\Rightarrow$
$(\operatorname{adj} A)=|A|^{n-2} A$

</details>

---

