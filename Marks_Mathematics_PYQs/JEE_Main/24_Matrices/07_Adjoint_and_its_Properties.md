# JEE Main Mathematics - Matrices

## Topic 7: Adjoint and its Properties

**Total Questions:** 57

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} \alpha & 1 & 2 \\ 2 & 3 & 0 \\ 0 & 4 & 5 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -5\alpha & 0 \\ 0 & 4\alpha & -2\alpha \end{bmatrix} + \text{adj}(A)$. If $\det(B)=66$, then $\det(\text{adj}(A))$ equals:

**Options:**

- **(A)** $289$
- **(B)** $361$
- **(C)** $441$
- **(D)** $529$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $441$**

**Detailed Solution:**

The cofactor matrix of $A$ is calculated as follows:

$C_{11} = 15$, $C_{12} = -10$, $C_{13} = 8$

$C_{21} = 3$, $C_{22} = 5\alpha$, $C_{23} = -4\alpha$

$C_{31} = -6$, $C_{32} = 4$, $C_{33} = 3\alpha - 2$

The adjoint of $A$ is the transpose of the cofactor matrix:

$\text{adj}(A) = \begin{bmatrix} 15 & 3 & -6 \\ -10 & 5\alpha & 4 \\ 8 & -4\alpha & 3\alpha - 2 \end{bmatrix}$

The matrix $B$ is given by:

$B = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -5\alpha & 0 \\ 0 & 4\alpha & -2\alpha \end{bmatrix} + \begin{bmatrix} 15 & 3 & -6 \\ -10 & 5\alpha & 4 \\ 8 & -4\alpha & 3\alpha - 2 \end{bmatrix} = \begin{bmatrix} 16 & 3 & -6 \\ -10 & 0 & 4 \\ 8 & 0 & \alpha - 2 \end{bmatrix}$

Expanding the determinant of $B$ along the second column:

$\det(B) = -3 \begin{vmatrix} -10 & 4 \\ 8 & \alpha - 2 \end{vmatrix} = -3(-10(\alpha - 2) - 32) = -3(-10\alpha - 12) = 30\alpha + 36$

Given $\det(B) = 66$, we get:

$30\alpha + 36 = 66 \Rightarrow 30\alpha = 30 \Rightarrow \alpha = 1$

The determinant of $A$ is:

$\det(A) = \alpha(15 - 0) - 1(10 - 0) + 2(8 - 0) = 15\alpha + 6$

Substituting $\alpha = 1$:

$\det(A) = 15(1) + 6 = 21$

Using the property $\det(\text{adj}(A)) = (\det(A))^{n-1}$ for a $3 \times 3$ matrix:

$\det(\text{adj}(A)) = (\det(A))^2 = (21)^2 = 441$

Answer: $441$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $A = \begin{bmatrix} -1 & 1 & -1 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ satisfy $A^2 + \alpha(adj(adj(A))) + \beta(adj(A)(adj(adj(A)))) = \begin{bmatrix} 2 & -2 & 2 \\ -2 & 0 & -1 \\ 0 & 0 & -1 \end{bmatrix}$ for some $\alpha, \beta \in \mathbb{R}$. Then $(\alpha - \beta)^2$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

The determinant of matrix $A$ is:

$|A| = -1(0 - 0) - 1(1 - 0) - 1(0 - 0) = -1$

Using the properties of the adjoint of a $3 \times 3$ matrix:

$adj(adj(A)) = |A|^{3-2}A = -A$

$adj(A)(adj(adj(A))) = adj(A)(-A) = -|A|I = -(-1)I = I$

The given equation simplifies to:

$A^2 - \alpha A + \beta I = \begin{bmatrix} 2 & -2 & 2 \\ -2 & 0 & -1 \\ 0 & 0 & -1 \end{bmatrix}$

Calculating $A^2$:

$A^2 = \begin{bmatrix} -1 & 1 & -1 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} -1 & 1 & -1 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -1 & 1 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

Substituting $A^2$, $A$, and $I$ into the simplified equation:

$\begin{bmatrix} 2 & -1 & 1 \\ -1 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} - \alpha \begin{bmatrix} -1 & 1 & -1 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{bmatrix} + \beta \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -2 & 2 \\ -2 & 0 & -1 \\ 0 & 0 & -1 \end{bmatrix}$

Comparing the corresponding elements on both sides:

From the $(1,2)$ element:

$-1 - \alpha = -2 \Rightarrow \alpha = 1$

From the $(2,2)$ element:

$1 + \beta = 0 \Rightarrow \beta = -1$

Therefore, the value of $(\alpha - \beta)^2$ is:

$(1 - (-1))^2 = 2^2 = 4$

Answer: $4$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $A$ be a $3 \times 3$ matrix such that $A^T \begin{bmatrix}1\\0\\1\end{bmatrix} = \begin{bmatrix}5\\2\\2\end{bmatrix}$, $A^T \begin{bmatrix}0\\0\\1\end{bmatrix} = \begin{bmatrix}3\\1\\1\end{bmatrix}$, $A \begin{bmatrix}1\\0\\1\end{bmatrix} = \begin{bmatrix}3\\4\\4\end{bmatrix}$ and $A \begin{bmatrix}0\\0\\1\end{bmatrix} = \begin{bmatrix}1\\3\\1\end{bmatrix}$. If $\det(A) = 1$, then $\det(\operatorname{adj}(A^2 + A))$ is equal to:

**Options:**

- **(A)** $16$
- **(B)** $25$
- **(C)** $49$
- **(D)** $64$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $64$**

**Detailed Solution:**

Let $C_1, C_2, C_3$ be the columns of $A$ and $R_1, R_2, R_3$ be the rows of $A$.

From the given equations, we have:
$A \begin{bmatrix}0\\0\\1\end{bmatrix} = C_3 = \begin{bmatrix}1\\3\\1\end{bmatrix}$

$A \begin{bmatrix}1\\0\\1\end{bmatrix} = C_1 + C_3 = \begin{bmatrix}3\\4\\4\end{bmatrix} \Rightarrow C_1 = \begin{bmatrix}2\\1\\3\end{bmatrix}$

Similarly, for the transpose $A^T$, the columns correspond to the rows of $A$:
$A^T \begin{bmatrix}0\\0\\1\end{bmatrix} = R_3^T = \begin{bmatrix}3\\1\\1\end{bmatrix} \Rightarrow R_3 = \begin{bmatrix}3 & 1 & 1\end{bmatrix}$

$A^T \begin{bmatrix}1\\0\\1\end{bmatrix} = R_1^T + R_3^T = \begin{bmatrix}5\\2\\2\end{bmatrix} \Rightarrow R_1^T = \begin{bmatrix}2\\1\\1\end{bmatrix} \Rightarrow R_1 = \begin{bmatrix}2 & 1 & 1\end{bmatrix}$

Using the elements of $C_1, C_3, R_1,$ and $R_3$, we can construct the matrix $A$ with an unknown central element $b$:
$A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & b & 3 \\ 3 & 1 & 1 \end{bmatrix}$

We are given that $\det(A) = 1$. Expanding along the first row:
$\det(A) = 2(b - 3) - 1(1 - 9) + 1(1 - 3b) = 1$

$2b - 6 + 8 + 1 - 3b = 1$

$3 - b = 1 \Rightarrow b = 2$

Thus, the matrix $A$ is:
$A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 2 & 3 \\ 3 & 1 & 1 \end{bmatrix}$

We need to find $\det(\operatorname{adj}(A^2 + A))$. Using the properties of determinants and adjoints:
$\det(\operatorname{adj}(A^2 + A)) = (\det(A^2 + A))^2 = (\det(A) \cdot \det(A + I))^2$

First, find $A + I$:
$A + I = \begin{bmatrix} 3 & 1 & 1 \\ 1 & 3 & 3 \\ 3 & 1 & 2 \end{bmatrix}$

Now, calculate $\det(A + I)$:
$\det(A + I) = 3(6 - 3) - 1(2 - 9) + 1(1 - 9)$

$\det(A + I) = 3(3) - 1(-7) + 1(-8) = 9 + 7 - 8 = 8$

Since $\det(A) = 1$, we have:
$\det(A^2 + A) = 1 \times 8 = 8$

Finally, for a $3 \times 3$ matrix:
$\det(\operatorname{adj}(A^2 + A)) = 8^{3-1} = 8^2 = 64$

Answer: $64$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $A = \begin{bmatrix} 1 & 1 & 2 \\ -2 & 0 & 1 \\ 1 & 3 & 5 \end{bmatrix}$. Then the sum of all elements of the matrix $\text{adj}(\text{adj}(2(\text{adj}A)^{-1}))$ is equal to:

**Options:**

- **(A)** $3$
- **(B)** $4$
- **(C)** $-4$
- **(D)** $-3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-3$**

**Detailed Solution:**

The determinant of matrix $A$ is given by:

$|A| = 1(0 - 3) - 1(-10 - 1) + 2(-6 - 0)$

$|A| = -3 + 11 - 12 = -4$

We know the property $A(\text{adj}A) = |A|I$, which gives $\text{adj}A = |A|A^{-1}$.

Taking the inverse on both sides:

$(\text{adj}A)^{-1} = \dfrac{A}{|A|} = \dfrac{A}{-4}$

Let $B = 2(\text{adj}A)^{-1}$. Substituting the above expression, we get:

$B = 2\left(\dfrac{A}{-4}\right) = -\dfrac{1}{2}A$

We need to find the matrix $\text{adj}(\text{adj}B)$. For a square matrix of order $n$, we have $\text{adj}(\text{adj}B) = |B|^{n-2}B$. Since the order is $n = 3$:

$\text{adj}(\text{adj}B) = |B|^{3-2}B = |B|B$

Now, we calculate the determinant of $B$:

$|B| = \left|-\dfrac{1}{2}A\right| = \left(-\dfrac{1}{2}\right)^3|A| = -\dfrac{1}{8}(-4) = \dfrac{1}{2}$

Substituting $|B|$ back into the expression for $\text{adj}(\text{adj}B)$:

$\text{adj}(\text{adj}B) = \dfrac{1}{2}B = \dfrac{1}{2}\left(-\dfrac{1}{2}A\right) = -\dfrac{1}{4}A$

The sum of all elements of matrix $A$ is:

$1 + 1 + 2 - 2 + 0 + 1 + 1 + 3 + 5 = 12$

Therefore, the sum of all elements of the matrix $-\dfrac{1}{4}A$ is:

$-\dfrac{1}{4} \times 12 = -3$

Answer: $-3$

</details>

---

### Q5. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $P=\left[p_{i j}\right]$ and $Q=\left[q_{i j}\right]$ be two square matrices of order 3 such that $q_{\mathrm{ij}}=2^{(\mathrm{i}+\mathrm{j}-1)} \mathrm{p}_{\mathrm{ij}}$ and $\operatorname{det}(\mathrm{Q})=2^{10}$. Then the value of $\operatorname{det}(\operatorname{adj}(\operatorname{adj} \mathrm{P}))$ is:

**Options:**

- **(A)** 81
- **(B)** 16
- **(C)** 124
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 16**

**Detailed Solution:**

$\begin{vmatrix} 2p_{11} & 2^2p_{12} & 2^3p_{13} \\ 2^2p_{21} & 2^3p_{22} & 2^4p_{23} \\ 2^3p_{31} & 2^4p_{32} & 2^5p_{33} \end{vmatrix} = 2^{10}$
$2^2 \cdot 2 \cdot 2^3 \begin{vmatrix} p_{11} & p_{12} & p_{13} \\ 2p_{21} & 2p_{22} & 2p_{23} \\ 2^2p_{31} & 2^2p_{32} & 2^2p_{33} \end{vmatrix} = 2^{10}$
$2^9 \begin{vmatrix} p_{11} & p_{12} & p_{13} \\ p_{21} & p_{22} & p_{23} \\ p_{31} & p_{32} & p_{33} \end{vmatrix} = 2^{10} \Rightarrow |P| = 2$
$|\text{adj}(\text{adj}(P))| = |P|^{(n-1)^2} = |P|^4 = 2^4 = 16$

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $f(x)=\int \frac{7 x^{10}+9 x^{8}}{\left(1+x^{2}+2 x^{9}\right)^{2}} d x, x>0, \lim _{x \rightarrow 0} f(x)=0$ and $f(1)=\frac{1}{4}$. If $\mathrm{A}=\left[\begin{array}{ccc}0 & 0 & 1 \\ \frac{1}{4} & f^{\prime}(1) & 1 \\ \alpha^{2} & 4 & 1\end{array}\right]$ and $\mathrm{B}=\operatorname{adj}(\operatorname{adj} \mathrm{A})$ be such that $|\mathrm{B}|=81$, then $\alpha^{2}$ is equal to

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

Divide numerator and denominator by $x^{18}$, let $t = x^{-9} + x^{-7} + 2$, then $dt = -(9x^{-10}+7x^{-8})dx$.
$f(x) = \frac{1}{t} + C = \frac{x^9}{1+x^2+2x^9} + C$.
$\lim_{x \to 0} f(x) = 0 \Rightarrow C = 0$. $f(1) = \frac{1}{4}$ (verified).
$f'(x) = \frac{9x^8(1+x^2+2x^9) - x^9(2x+18x^8)}{(1+x^2+2x^9)^2}$.
$f'(1) = \frac{36-20}{16} = 1$.
$|A| = \begin{vmatrix} 0 & 0 & 1 \\ 1/4 & 1 & 1 \\ \alpha^2 & 4 & 1 \end{vmatrix} = 1 - \alpha^2$.
$|B| = |\text{adj}(\text{adj } A)| = |A|^{(3-1)^2} = (1-\alpha^2)^4 = 81 = 3^4$.
$|1-\alpha^2| = 3 \Rightarrow \alpha^2 = 4$.

</details>

---

### Q7. JEE Main 2026 (23 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $|\mathrm{A}|=6$, where A is a $3 \times 3$ matrix. If $\left|\operatorname{adj}\left(3 \operatorname{adj}\left(\mathrm{~A}^{2} \cdot \operatorname{adj}(2 \mathrm{~A})\right)\right)\right|=2^{\mathrm{m}} \cdot 3^{\mathrm{n}}, \mathrm{m}, \mathrm{n} \in \mathbf{N}$, then $\mathrm{m}+\mathrm{n}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **62**

**Detailed Solution:**

For $3 \times 3$ matrix: $|\text{adj}(M)| = |M|^2$, $|kM| = k^3|M|$.
$|2A| = 8 \cdot 6 = 48$, $|\text{adj}(2A)| = 48^2 = 2^8 \cdot 3^2$.
$|A^2 \cdot \text{adj}(2A)| = |A|^2 \cdot |\text{adj}(2A)| = 2^2 \cdot 3^2 \cdot 2^8 \cdot 3^2 = 2^{10} \cdot 3^4$.
Let $B = A^2 \cdot \text{adj}(2A)$. $|\text{adj}(B)| = |B|^2 = 2^{20} \cdot 3^8$.
$|3\,\text{adj}(B)| = 3^3 \cdot 2^{20} \cdot 3^8 = 2^{20} \cdot 3^{11}$.
$|\text{adj}(3\,\text{adj}(B))| = (2^{20} \cdot 3^{11})^2 = 2^{40} \cdot 3^{22}$.
$m = 40, n = 22 \Rightarrow m + n = 62$.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$ is a solution of the system of equations $A X=B$, where $\operatorname{adj} A=\left[\begin{array}{ccc}4 & 2 & 2 \\ -5 & 0 & 5 \\ 1 & -2 & 3\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{l}4 \\ 0 \\ 2\end{array}\right]$, then $|x+y+z|$ is equal to :

**Options:**

- **(A)** 2
- **(B)** $\frac{3}{2}$
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

$X = \frac{1}{|A|}\text{adj}(A)\cdot B$.
$|\text{adj}(A)| = 4(10)-2(-20)+2(10) = 100$, so $|A|^2=100 \Rightarrow |A|=\pm10$.
$\text{adj}(A)\cdot B = \begin{pmatrix}16+0+4\\-20+0+10\\4+0+6\end{pmatrix}=\begin{pmatrix}20\\-10\\10\end{pmatrix}$
$x+y+z = \frac{20-10+10}{|A|}=\frac{20}{\pm10}=\pm2$
$|x+y+z|=2$

</details>

---

### Q9. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let A be a $3 \times 3$ matrix such that $\mathrm{A}+\mathrm{A}^{\mathrm{T}}=\mathrm{O}$. If $\mathrm{A}\left[\begin{array}{c}1 \\ -1 \\ 0\end{array}\right]=\left[\begin{array}{l}3 \\ 3 \\ 2\end{array}\right], \mathrm{A}^{2}\left[\begin{array}{c}1 \\ -1 \\ 0\end{array}\right]=\left[\begin{array}{c}-3 \\ 19 \\ -24\end{array}\right]$ and $\operatorname{det}(\operatorname{adj}(2 \operatorname{adj}(\mathrm{~A}+\mathrm{I})))=(2)^{\alpha} \cdot(3)^{\beta} \cdot(11)^{\gamma}, \alpha, \beta, \gamma$ are non-negative integers, then $\alpha+\beta+\gamma$ is equal to $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

$A$ is skew-symmetric: $A = \begin{bmatrix}0 & -c & b\\c & 0 & -a\\-b & a & 0\end{bmatrix}$.
From $A\begin{bmatrix}1\\-1\\0\end{bmatrix} = \begin{bmatrix}3\\3\\2\end{bmatrix}$: $c = 3$, $a+b = -2$.
From $A^2\begin{bmatrix}1\\-1\\0\end{bmatrix} = \begin{bmatrix}-3\\19\\-24\end{bmatrix}$: $b = 3$, $a = -5$.
$A+I = \begin{bmatrix}1&-3&3\\3&1&5\\-3&-5&1\end{bmatrix}$, $\det(A+I) = 44$.
For $3 \times 3$ matrix: $\det(\text{adj}(M)) = (\det M)^2$.
$\det(2\,\text{adj}(A+I)) = 8 \cdot 44^2 = 8 \cdot 1936 = 15488 = 2^7 \cdot 11^2$.
$\det(\text{adj}(2\,\text{adj}(A+I))) = 15488^2 = 2^{14} \cdot 11^4$.
$\alpha = 14,\ \beta = 0,\ \gamma = 4$. $\alpha+\beta+\gamma = 18$.

</details>

---

### Q10. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{ccc}2 & 2+p & 2+p+q \\ 4 & 6+2 p & 8+3 p+2 q \\ 6 & 12+3 p & 20+6 p+3 q\end{array}\right]$.
If $\operatorname{det}(\operatorname{adj}(\operatorname{adj}(3 \mathrm{~A})))=2^{\mathrm{m}} \cdot 3^{\mathrm{n}}, \mathrm{m}, \mathrm{n} \in \mathrm{N}$, then $\mathrm{m}+\mathrm{n}$ is equal to

**Options:**

- **(A)** 22
- **(B)** 24
- **(C)** 26
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 24**

**Detailed Solution:**

$|A|=\left|\begin{array}{ccc}2 & 2+p & 2+p+q \\ 4 & 6+2 p & 8+3 p+2 q \\ 6 & 12+3 p & 20+6 p+3 q\end{array}\right|$
$\mathrm{C}_3 \rightarrow \mathrm{C}_3-\mathrm{C}_2-\mathrm{C}_1 \times \frac{\mathrm{q}}{2}$
Then $\mathrm{C}_3 \rightarrow \mathrm{C}_2-\mathrm{C}_1 \mathrm{X}\left(1+\frac{\mathrm{p}}{2}\right)$
$\begin{aligned}
& \Rightarrow|\mathrm{A}|=\left|\begin{array}{ccc}
2 & 0 & 0 \\
4 & 2 & 2+\mathrm{p} \\
6 & 6 & 8+3 \mathrm{p}
\end{array}\right| \\
& \Rightarrow|\mathrm{A}|=2(16+6 \mathrm{p}-12-6 \mathrm{p})=8=2^3 \\
& |\operatorname{adj}(\operatorname{adj}(3 \mathrm{~A}))|=|3 \mathrm{~A}|^{(3-1)^2}=|3 \mathrm{~A}|^4 \\
& =\left(3^3|\mathrm{~A}|\right)^4=\left(3^3 \times 2^3\right)^4=2^{12} \times 3^{12} \\
& \Rightarrow \mathrm{~m}+\mathrm{n}=24
\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be a $3 \times 3$ matrix such that
$\begin{aligned}
& |\operatorname{adj}(\operatorname{adj}(\operatorname{adj} \mathrm{A}))|=81 . \text { If } \\
& \mathrm{S}=\left\{\mathrm{n} \in \mathbb{Z}:(|\operatorname{adj}(\operatorname{adj} A)|)^{\frac{(n-1)^2}{2}}=|A|^{\left(3 n^2-5 n-4\right)}\right\}
\end{aligned}$
, then $\sum_{n \in S}\left|A^{\left(n^2+n\right)}\right|$ is equal to

**Options:**

- **(A)** 866
- **(B)** 750
- **(C)** 820
- **(D)** 732

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 732**

**Detailed Solution:**

$\begin{aligned} & |\operatorname{adj}(\operatorname{adj})(\operatorname{adjA})|=81 \\ & \Rightarrow|\operatorname{adjA}|^4=81 \\ & \Rightarrow|\operatorname{adjA}|=3 \\ & \Rightarrow|\mathrm{~A}|^2=3 \\ & \Rightarrow|\mathrm{~A}|=\sqrt{3} \\ & \left(|\mathrm{~A}|^4\right)^{\frac{(\mathrm{n}-1)^2}{2}}=|\mathrm{A}|^{\mathrm{n}^2-5 \mathrm{n}-4} \\ & \Rightarrow 2(\mathrm{n}-1)^2=3 \mathrm{n}^2-5 \mathrm{n}-4 \\ & \Rightarrow 2 \mathrm{n}^2-4 \mathrm{n}+2=3 \mathrm{n}^2-5 \mathrm{n}-4 \\ & \Rightarrow \mathrm{n}^2-\mathrm{n}-6=0 \\ & \Rightarrow(\mathrm{n}-3)(\mathrm{n}+2)=0 \\ & \Rightarrow \mathrm{n}=3,-2 \\ & \sum_{\mathrm{n} \in \mathrm{s}}\left|\mathrm{A}^{\mathrm{n}^2+\mathrm{n}}\right| \\ & =\left|\mathrm{A}^2\right|+\left|\mathrm{A}^{12}\right| \\ & =3+36=3+729=732\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (3 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $I$ be the identity matrix of order $3 \times 3$ and for the matrix $\mathrm{A}=\left[\begin{array}{ccc}\lambda & 2 & 3 \\ 4 & 5 & 6 \\ 7 & -1 & 2\end{array}\right],|\mathrm{A}|=-1$. Let B be the inverse of the matrix $\operatorname{adj}\left(\mathrm{A} \operatorname{adj}\left(\mathrm{A}^2\right)\right)$. Then $|(\lambda B+1)|$ is equal to _____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **38**

**Detailed Solution:**

$\begin{aligned}
& |A|=\left|\begin{array}{ccc}
\lambda & 2 & 3 \\
4 & 5 & 6 \\
7 & -1 & 2
\end{array}\right|=-1 \\
& \lambda(16)-2(-34)+3(-39)=-1 \\
& 16 \lambda=48 \Rightarrow \lambda=3 \\
& \mathrm{~B}^{-1}=\operatorname{adj}\left(\mathrm{A} \cdot \operatorname{adj}\left(\mathrm{~A}^2\right)\right) \\
& \text { Let } \mathrm{C}=\mathrm{A} \cdot \operatorname{adj}\left(\mathrm{~A}^2\right) \\
& A C=A^2 \operatorname{adj}\left(A^2\right)=|A|^2 \cdot I=I \Rightarrow C=A^{-1} \\
& \text { Now } B^{-1}=\operatorname{adj}\left(A^{-1}\right)=B=\operatorname{adj}(A) \\
& \text { Now } \lambda \mathrm{B}+\mathrm{I} \Rightarrow 3 \mathrm{~B}+\mathrm{I} \\
& \text { Let } \mathrm{P}=3 \mathrm{~B}+\mathrm{I} \\
& \text { P }=3 \operatorname{adj}(\mathrm{~A})+\mathrm{I} \\
& \mathrm{AP}=3 \operatorname{Aadj}(\mathrm{~A})+\mathrm{A} \\
& \mathrm{AP}=3|\mathrm{~A}| \cdot \mathrm{I}+\mathrm{A} \\
& \mathrm{AP}=\mathrm{A}-3 \mathrm{I} \\
& |\mathrm{AP}|=|\mathrm{A}-3 \mathrm{I}| \\
& |\mathrm{A}| \cdot|\mathrm{P}|=\left|\begin{array}{ccc}
0 & 2 & 3 \\
4 & 2 & 6 \\
7 & -1 & -1
\end{array}\right|=38 \\
& |\mathrm{P}|=-38
\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be a matrix of order $3 \times 3$ and $|A|=5$. If $|2 \operatorname{adj}(3 \mathrm{~A} \operatorname{adj}(2 \mathrm{~A}))|=2^\alpha \cdot 3^\beta \cdot 5^\gamma \alpha, \beta, \gamma \in \mathrm{N}$ then $\alpha+\beta+\gamma$ is equal to

**Options:**

- **(A)** $25$
- **(B)** $26$
- **(C)** $27$
- **(D)** $28$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $27$**

**Detailed Solution:**

$\begin{aligned} & |2 \operatorname{adj}(3 \mathrm{~A} \operatorname{adj}(2 \mathrm{~A}))| \\ & 2^3 \cdot|3 \mathrm{~A} \operatorname{adj}(2 \mathrm{~A})|^2 \\ & 2^3 \cdot\left(3^3\right)^2 \cdot|\mathrm{~A}|^2 \cdot|\operatorname{adj}(2 \mathrm{~A})|^2 \\ & 2^3 \cdot 3^6 \cdot|\mathrm{~A}|^2 \cdot\left(|2 \mathrm{~A}|^2\right)^2 \\ & 2^3 \cdot 3^6 \cdot|\mathrm{~A}|^2\left[\left(2^3\right)^2 \cdot|\mathrm{~A}|^2\right]^2 \\ & 2^3 \cdot 3^6 \cdot|\mathrm{~A}|^2 \cdot 2^{12} \cdot|\mathrm{~A}|^4 \\ & 2^{15} \cdot 3^6 \cdot|\mathrm{~A}|^6 \\ & 2^{15} \cdot 3^6 \cdot 5^6=2^\alpha \cdot 3^\beta \cdot 5^\gamma \\ & \alpha=15, \quad \beta=6, \quad \gamma=6 \\ & \alpha+\beta+\gamma=27\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{a} \in \mathbf{R}$ and A be a matrix of order $3 \times 3$ such that $\operatorname{det}(A)=-4$ and $A+I=\left[\begin{array}{lll}1 & a & 1 \\ 2 & 1 & 0 \\ a & 1 & 2\end{array}\right]$, where $I$ is the identity matrix of order $3 \times 3$.
If $\operatorname{det}((a+1) \operatorname{adj}((a-1) A))$ is $2^m 3^n, m, n \in$ $\{0,1,2, \ldots .20\}$, then $\mathrm{m}+\mathrm{n}$ is equal to :

**Options:**

- **(A)** 14
- **(B)** 17
- **(C)** 15
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 16**

**Detailed Solution:**

$\mathrm{A}=\left[\begin{array}{lll}1 & \mathrm{a} & 1 \\ 2 & 1 & 0 \\ \mathrm{a} & 1 & 2\end{array}\right]-\mathrm{I}=\left[\begin{array}{lll}0 & \mathrm{a} & 1 \\ 2 & 0 & 0 \\ \mathrm{a} & 1 & 1\end{array}\right]$
$\begin{aligned} & |\mathrm{A}|=-4 \Rightarrow 2-2 \mathrm{a}=-4 \Rightarrow \mathrm{a}=3 \\ & |(\mathrm{a}+1) \operatorname{adj}(\mathrm{a}-1) \mathrm{A}|=|4 \operatorname{adj} 3 \mathrm{~A}| \\ & =4^3|\operatorname{adj} 3 \mathrm{~A}| \\ & =4^3 \times|3 \mathrm{~A}|^{3-1}=64|3 \mathrm{~A}|^2 \\ & =64 \times\left(3^3\right)^2|\mathrm{~A}|^2 \\ & =2^6 \times 3^6 \times 16 \\ & 2^{\mathrm{m}} \times 3^{\mathrm{n}}=2^{10} \times 3^6 \\ & \therefore \mathrm{~m}=10, \mathrm{n}=6 \\ & \Rightarrow \mathrm{~m}+\mathrm{n}=16\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let \(\mathrm{A}=\left[\mathrm{a}_{i j}\right]=\left[\begin{array}{cc}\log _5 128 & \log _4 5 \\ \log _5 8 & \log _4 25\end{array}\right]\).
If \(\mathrm{A}_{i j}\) is the cofactor of \(\mathrm{a}_{i j}, \mathrm{C}_{i j}=\sum_{\mathrm{k}=1}^2 \mathrm{a}_{i \mathrm{k}} \mathrm{A}_{j \mathrm{k}}, 1 \leq i, j \leq 2\), and \(\mathrm{C}=\left[\mathrm{C}_{i j}\right]\), then \(8|\mathrm{C}|\) is equal to :

**Options:**

- **(A)** 288
- **(B)** 222
- **(C)** 242
- **(D)** 262

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 242**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{A}|=\frac{11}{2} \\ & \mathrm{C}_{11}=\sum_{\mathrm{k}=1}^2 \mathrm{a}_{1 \mathrm{k}} \cdot \mathrm{A}_{1 \mathrm{k}}=\mathrm{a}_{11} \mathrm{~A}_{11}+\mathrm{a}_{12} \mathrm{~A}_{12}=|\mathrm{A}|=\frac{11}{2} \\ & \mathrm{C}_{12}=\sum_{\mathrm{k}=1}^2 \mathrm{a}_{1 \mathrm{k}} \cdot \mathrm{A}_{2 \mathrm{k}}=0 \\ & \mathrm{C}_{21}=\sum_{\mathrm{k}=1}^2 \mathrm{a}_{2 \mathrm{k}} \cdot \mathrm{A}_{1 \mathrm{k}}=0 \\ & \mathrm{C}_{22}=\sum_{\mathrm{k}=1}^2 \mathrm{a}_{2 \mathrm{k}} \cdot \mathrm{A}_{2 \mathrm{k}}=|\mathrm{A}|=\frac{11}{2} \\ & \mathrm{C}=\left[\begin{array}{cc}11 / 2 & 0 \\ 0 & 11 / 2\end{array}\right] \\ & |\mathrm{C}|=\frac{121}{4} \\ & 8|\mathrm{C}|=242\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $A$ be a $3 \times 3$ matrix such that $X^T A X=O$ for all nonzero $3 \times 1$ matrices $X=\left[\begin{array}{l}x \\ y \\ z\end{array}\right]$. If $\mathbf{A}\left[\begin{array}{l}1 \\ 1 \\ 1\end{array}\right]=\left[\begin{array}{c}1 \\ 4 \\ -5\end{array}\right], \mathbf{A}\left[\begin{array}{l}1 \\ 2 \\ 1\end{array}\right]=\left[\begin{array}{c}0 \\ 4 \\ -8\end{array}\right]$, and $\operatorname{det}(\operatorname{adj}(2(\mathbf{A}+\mathbf{1})))-2^\alpha 3^\beta 5^\gamma, \alpha, \beta, \gamma \in N$, then $\alpha^2+\beta^2+\gamma^2$ is_____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

$\begin{aligned}
& X^{\top} A X=0 \\
& (x y z)\left[\begin{array}{lll}
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3 \\
c_1 & c_2 & c_3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
z
\end{array}\right]=0 \\
& (x y z)\left[\begin{array}{l}
a_1 x+a_2 y+a_3 z \\
b_1 x+b_2 y+b_3 z \\
c_1 x+c_2 y+c_3 z
\end{array}\right]=0 \\
& x\left(a_1 x+a_2 y+a_3 z\right)+y\left(b_1 x+b_2 y+b_3 z\right) \\
& +z\left(c_1 x+c_2 y+c_3 z\right) \\
& a_1=0, b_2=0, c_3=0 \\
& a_2+b_1=0, a_3+c_1=0, b_3+c_2=0 \\
& A=\text { skew symmetric matrix } \\
& A=\left[\begin{array}{ccc}
0 & x & y \\
-x & 0 & z \\
-y & -z & 0
\end{array}\right] ; A\left[\begin{array}{l}
1 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{c}
1 \\
4 \\
-5
\end{array}\right] \\
& \Rightarrow\left[\begin{array}{ccc}
0 & x & y \\
-x & 0 & z \\
-y & -z & 0
\end{array}\right]\left[\begin{array}{l}
1 \\
1 \\
1
\end{array}\right]=\left[\begin{array}{c}
1 \\
4 \\
-5
\end{array}\right] \\
& x+y=1 \\
& -x+z=4 \\
& y+z=5 \\
& {\left[\begin{array}{ccc}
0 & x & y \\
-x & 0 & z \\
-y & -z & 0
\end{array}\right]\left[\begin{array}{l}
1 \\
2 \\
1
\end{array}\right]=\left[\begin{array}{c}
1 \\
4 \\
-8
\end{array}\right]} \\
& 2 x+y=0 \quad x=-1 \\
& -x+z=4 \quad y=2 \\
& -y-2 z=-8 \quad z=3
\end{aligned}$
$\begin{aligned} & A=\left[\begin{array}{ccc}0 & -1 & 2 \\ 1 & 0 & 3 \\ -2 & -3 & 0\end{array}\right] \\ & 2(A+l)=\left[\begin{array}{ccc}2 & -2 & 4 \\ 2 & 2 & 6 \\ -2 & -6 & 2\end{array}\right] \\ & 2(A+l)=120 \\ & \Rightarrow \operatorname{det}(\operatorname{adj}(2 A+l)) \\ & \quad=120^2=2^6 \cdot 3^2 \cdot 5^2 \\ & \therefore \quad \alpha=6, \beta=2, \gamma=2 \\ & \text { Hence } \alpha^2+\beta^2+\gamma^2=6^2+2^2+2^2=44\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For a $3 \times 3$ matrix $M$, let trace $(M)$ denote the sum of all the diagonal elements of $M$. Let $A$ be a $3 \times 3$ matrix such that $|A|=\frac{1}{2}$ and trace $(A)=3$. If $B=\operatorname{adj}(\operatorname{adj}(2 A))$, then the value of $|B|+$ trace (B) equals :

**Options:**

- **(A)** 56
- **(B)** 132
- **(C)** 174
- **(D)** 280

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 280**

**Detailed Solution:**

$\because \operatorname{tr}(A)=3 \text { and }|A|=\frac{1}{2}$
Now, $B=\operatorname{adj}(\operatorname{adj}(2 A))=|2 A|^{3-2} \cdot(2 A)$
$=2^3|A| \cdot 2 A=8 A$
$\begin{aligned} & \therefore \operatorname{tr}(B)=8 \operatorname{tr}(A)=24 \\ & \text { and }|B|=|8 A|=8^3 \cdot \frac{1}{2}=256 \\ & \therefore \quad \operatorname{trace}(B)+|B|=24+256\end{aligned}$
$=280$

</details>

---

### Q18. JEE Main 2025 (22 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A$ be a square matrix of order 3 such that $\operatorname{det}(A)=-2$ and $\operatorname{det}(3 \operatorname{adj}(-6 \operatorname{adj}(3 A)))=2^{\mathrm{m}+\mathrm{n}} \cdot 3^{\mathrm{mn}}, \mathrm{m}\gt\mathrm{n}$. Then $4 \mathrm{~m}+2 \mathrm{n}$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **34**

**Detailed Solution:**

$\begin{aligned}
& \text { As } A \operatorname{adj} A=|A| l, \operatorname{det}(\lambda A)=\lambda^n \operatorname{det} A \\
& \operatorname{det}(3 \operatorname{adj}(-6 \operatorname{adj}(3 A)))=3^3 \operatorname{det}(\operatorname{adj}(-6 \operatorname{adj}(3 A))) \\
& =3^3(-6 \operatorname{adj}(3 A))^2 \\
& =3^3(-6)^6|3 A|^4 \\
& =3^9 2^6 \cdot 3^{12} \cdot(-2)^4 \\
& =3^{21} \cdot 2^{10}
\end{aligned}$

Now comparing with given condition
$\begin{aligned}
& 2^{m+n} 3^{m n}=2^{10} \cdot 3^{21} \\
& m+n=10, m n=21 \\
& \Rightarrow \quad m=7, n=3(m>n) \\
& \therefore \quad 4 m+2 n=28+6=34
\end{aligned}$

</details>

---

### Q19. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let $A$ be a non-singular matrix of order 3 . If $\operatorname{det}(3 \operatorname{adj}(2 \operatorname{adj}((\operatorname{det} A) A)))=3^{-13} \cdot 2^{-10}$ and $\operatorname{det}(3 \operatorname{adj}(2 \mathrm{~A}))=2^{\mathrm{m}} \cdot 3^{\mathrm{n}}$, then $|3 \mathrm{~m}+2 \mathrm{n}|$ is equal to $\qquad$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

$\begin{aligned} & |3 \operatorname{adj}(2 \operatorname{adj}(|A| A))|=\mid 3 \operatorname{adj}\left(2|A|^2 \operatorname{adj}(A) \mid\right. \\ & =\left.\left|3.2^2\right| A\right|^4 \operatorname{adj}\left(\left.\operatorname{adj}(A)\left|=2^6 3^3\right| A\right|^{12}|A|^4\right. \\ & =2^6 3^3|A|^{16}=2^{-10} 3^{-13} \\ & \Rightarrow|A|^{16}=2^{-16} 3^{-16} \Rightarrow|A|=2^{-1} 3^{-1}\end{aligned}$
$\begin{aligned} & \text { Now }|3 \operatorname{adj}(2 \mathrm{~A})|=\left|3.2^2 \operatorname{adj}(\mathrm{A})\right| \\ & =2^6 3^3|\mathrm{~A}|^2=2^{-\mathrm{m}} 3^{-\mathrm{n}} \\ & \Rightarrow 2^6 3^3 2^{-2} 3^{-2}=2^{-\mathrm{m}} 3^{-\mathrm{n}} \\ & \Rightarrow 2^{-\mathrm{m}} 3^{-\mathrm{n}}=2^4 3^1 \\ & \Rightarrow \mathrm{m}=-4, \mathrm{n}=-1 \\ & \Rightarrow|3 \mathrm{~m}+2 \mathrm{n}|=|-12-2|=14\end{aligned}$

</details>

---

### Q20. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ is a square matrix of order 3 such that $\operatorname{det}(A)=3$ and $\operatorname{det}\left(\operatorname{adj}\left(-4 \operatorname{adj}\left(-3 \operatorname{adj}\left(3 \operatorname{adj}\left((2 \mathrm{~A})^{-1}\right)\right)\right)\right)\right)=2^{\mathrm{m}} 3^{\mathrm{n}}$, then $\mathrm{m}+2 \mathrm{n}$ is equal to :

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 6
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 4**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{A}|=3 \\ & \mid \operatorname{adj}\left(-4 \operatorname{adj}\left(-3 \operatorname{adj}\left(3 \operatorname{adj}\left((2 \mathrm{~A})^{-1}\right)\right)\right) \mid\right. \\ & \mid-4 \operatorname{adj}\left(-\left.3 \operatorname{adj}\left(3 \operatorname{adj}(2 \mathrm{~A})^{-1}\right)\right|^2\right. \\ & 4^6\left|\operatorname{adj}\left(-3 \operatorname{adj}\left(3 \operatorname{adj}(2 \mathrm{~A})^{-1}\right)\right)\right|^2 \\ & 2^{12} \cdot 3^{12}\left|3 \operatorname{adj}(2 \mathrm{~A})^{-1}\right|^8 \\ & 2^{12} \cdot 3^{12} \cdot 3^{24}\left|\operatorname{adj}(2 \mathrm{~A})^{-1}\right|^8\end{aligned}$
$\begin{aligned} & 2^{12} \cdot 3^{36}\left|(2 \mathrm{~A})^{-1}\right|^{16} \\ & 2^{12} \cdot 3^{36} \frac{1}{|2 \mathrm{~A}|^{16}} \\ & 2^{12} \cdot 3^{36} \frac{1}{2^{48}|\mathrm{~A}|^{16}} \\ & 2^{12} \cdot 3^{36} \frac{1}{2^{48} \cdot 3^{16}} \\ & \frac{3^{20}}{2^{36}}=2^{-36} \cdot 3^{20} \\ & \mathrm{~m}=-36 \quad \mathrm{n}=20 \\ & \mathrm{~m}+2 \mathrm{n}=4\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ and $B$ be two square matrices of order 3 such that $|A|=3$ and $|B|=2$. Then $\left|\mathrm{A}^{\mathrm{T}} \mathrm{A}(\operatorname{adj}(2 \mathrm{~A}))^{-1}(\operatorname{adj}(4 \mathrm{~B}))(\operatorname{adj}(\mathrm{AB}))^{-1} \mathrm{AA}^{\mathrm{T}}\right|$ is equal to :

**Options:**

- **(A)** 108
- **(B)** 32
- **(C)** 81
- **(D)** 64

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 64**

**Detailed Solution:**

$\begin{aligned} & |\mathrm{A}|=3,|\mathrm{~B}|=2 \\ & \left|\mathrm{~A}^{\mathrm{T}} \mathrm{A}(\operatorname{adj}(2 \mathrm{~A}))^{-1}(\operatorname{adj}(4 \mathrm{~B}))(\operatorname{adj}(\mathrm{AB}))^{-1} \mathrm{AA}^{\mathrm{T}}\right|\end{aligned}$
\(\begin{array}{ccc} =3 \times 3 \times \mid \left(\operatorname{adj}(2 \mathrm{~A})^{-1}|\times| \operatorname{adj}(4 \mathrm{~B})| \times|(\operatorname{adj}(\mathrm{AB}))^{-1}\mid \times 3 \times 3\right. \\ \downarrow \qquad\qquad \downarrow \qquad\qquad \downarrow \\ \frac{1}{|\operatorname{adj}(2 \mathrm{~A})|} \qquad 2^{12} \times 2^2 \qquad \frac{1}{|\operatorname{adj}(\mathrm{AB})|} \end{array}\)
$\begin{aligned} & =\frac{1}{2^6|\operatorname{adj} \mathrm{A}|} \quad=\frac{1}{|\operatorname{adj} \mathrm{B} \cdot \operatorname{adj} \mathrm{A}|} \\ & =\frac{1}{2^6 \cdot 3^2} \quad=\frac{1}{2^2 \cdot 3^2} \\ & =3^4 \cdot \frac{1}{2^6 \cdot 3^2} \cdot 2^{12} \cdot 2^2 \cdot \frac{1}{2^2 \cdot 3^2}=64 \\ & \end{aligned}$

</details>

---

### Q22. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{ll}1 & 2 \\ 0 & 1\end{array}\right]$ and $B=I+\operatorname{adj}(A)+(\operatorname{adj} A)^2+\ldots+(\operatorname{adj} A)^{10}$. Then, the sum of all the elements of the matrix $B$ is:

**Options:**

- **(A)** -124
- **(B)** 22
- **(C)** -88
- **(D)** -110

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -88**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fbG0MMzJtpqy_TdtGRi9QlCuwj46EamGZHTzZCps1Hg.original.fullsize.png">
$\begin{aligned} & \mathrm{B}=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right]+\left[\begin{array}{cc}1 & -2 \\ 0 & 1\end{array}\right]+\left[\begin{array}{cc}1 & -4 \\ 0 & 1\end{array}\right]+\ldots+\left[\begin{array}{cc}1 & -20 \\ 0 & 1\end{array}\right] \\ & \mathrm{B}=\left[\begin{array}{cc}11 & -110 \\ 0 & 11\end{array}\right] \Rightarrow \text { sum of elements of } \mathrm{B} \\ & =-88\end{aligned}$

</details>

---

### Q23. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\alpha \in(0, \infty)$ and $A=\left[\begin{array}{lll}1 & 2 & \alpha \\ 1 & 0 & 1 \\ 0 & 1 & 2\end{array}\right]$. If $\operatorname{det}\left(\operatorname{adj}\left(2 A-A^T\right) \cdot \operatorname{adj}\left(A-2 A^T\right)\right)=2^8$, then $(\operatorname{det}(A))^2$ is equal to:

**Options:**

- **(A)** 36
- **(B)** 16
- **(C)** 1
- **(D)** 49

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 16**

**Detailed Solution:**

$\begin{aligned} & \left|\operatorname{adj}\left(\mathrm{A}-2 \mathrm{~A}^{\mathrm{T}}\right)\left(2 \mathrm{~A}-\mathrm{A}^{\mathrm{T}}\right)\right|=28 \\ & \left|\left(\mathrm{~A}-2 \mathrm{~A}^{\mathrm{T}}\right)\left(2 \mathrm{~A}-\mathrm{A}^{\mathrm{T}}\right)\right|=24 \\ & \left|\mathrm{~A}-2 \mathrm{~A}^{\mathrm{T}}\right|\left|2 \mathrm{~A}-\mathrm{A}^{\mathrm{T}}\right|= \pm 16 \\ & \left(\mathrm{~A}-2 \mathrm{~A}^{\mathrm{T}}\right)^{\mathrm{T}}=\mathrm{A}^{\mathrm{T}}-2 \mathrm{~A} \\ & \left|\mathrm{~A}-2 \mathrm{~A}^{\mathrm{T}}\right|=\left|\mathrm{A}^{\mathrm{T}}-2 \mathrm{~A}\right| \\ & \Rightarrow\left|\mathrm{A}-2 \mathrm{~A}^{\mathrm{T}}\right|^2=16 \\ & \left|\mathrm{~A}-2 \mathrm{~A}^{\mathrm{T}}\right|= \pm 4 \\ & {\left[\begin{array}{ccc}1 & 2 & \alpha \\ 1 & 0 & 1 \\ 0 & 1 & 2\end{array}\right]-\left[\begin{array}{ccc}2 & 2 & 0 \\ 4 & 0 & 2 \\ 2 \alpha & 2 & 4\end{array}\right]} \\ & \left|\begin{array}{lll}-1 & 0 & \alpha \\ -3 & 0 & -1 \\ -2 \alpha & -1 & -2\end{array}\right| \\ & 1+3 \alpha=4 \\ & 3 \alpha=3 \\ & \alpha=1 \\ & |\mathrm{~A}|=\left|\begin{array}{lll}1 & 2 & 1 \\ 1 & 0 & 1 \\ 0 & 1 & 2\end{array}\right|=-1-3=-4 \\ & |\mathrm{~A}|^2=16\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>×</mo><mn>3</mn></math> matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math>. If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mi>det</mi><mfenced><munder><munder><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mo>.</mo><mo>...</mo><mfenced><mfenced open=""><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></mfenced></mrow></mfenced></mrow></mfenced></mrow><mo>⏟</mo></munder><mrow><mn>2024</mn><mo>−</mo><mi>times</mi></mrow></munder></mfenced></math>, then the remainder when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is divided by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> is equal to __________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mi>det</mi><mfenced><munder><munder><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mo>..</mo><mfenced><mi>A</mi></mfenced></mrow></mfenced></mrow></mfenced></mrow><mo>⏟</mo></munder><mrow><mn>2024</mn><mo> </mo><mi>times</mi></mrow></munder></mfenced></math></p><p>Now, using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><munder><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mo>..</mo><mfenced><mi>A</mi></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>⏟</mo></munder><mrow><mi>r</mi><mo> </mo><mi>times</mi></mrow></munder><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mfenced close="|" open="|"><munder><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mo>..</mo><mfenced><mi>A</mi></mfenced></mrow></mfenced></mrow></mfenced></mrow><mo>⏟</mo></munder></mfenced><mrow><mn>2024</mn><mo> </mo><mi>times</mi></mrow></munder><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></mfenced><mn>2024</mn></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mn>2</mn><mn>2024</mn></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>2024</mn></msup><mo>=</mo><msup><mn>4</mn><mn>1012</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mn>1012</mn></msup><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><msup><mn>2</mn><mrow><mn>3</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><mn>2</mn><mo>·</mo><msup><mn>2</mn><mrow><mn>3</mn><mi>k</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><mn>2</mn><mo>·</mo><msup><mfenced><mrow><mn>9</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>k</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><mn>9</mn><mi>m</mi><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><mn>9</mn><mi>t</mi><mo>-</mo><mn>2</mn><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><msup><mn>2</mn><mn>2024</mn></msup></msup><mo>=</mo><mn>9</mn><mi>m</mi><mo>+</mo><mn>7</mn></math></p><p>Hence, the remainder is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></p>

</details>

---

### Q25. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mi>x</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>y</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>z</mi></mtd></mtr></mtable></mfenced></math> be a non-zero <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>×</mo><mn>3</mn></math> matrix, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>sin</mi><mi>θ</mi><mo>=</mo><mi>y</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>z</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>≠</mo><mn>0</mn><mo>,</mo><mi>θ</mi><mo>∈</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mi>π</mi><mo>)</mo></math>. For a square matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>, let Trace<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>M</mi></mfenced></math> denote the sum of all the diagonal entries of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>.</mo></math> Then, among the statements:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math> Trace<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>R</mi><mo>)</mo><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>II</mi><mo>)</mo></math> If Trace<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>adj</mo><mo>(</mo><mo>adj</mo><mo>(</mo><mi>R</mi><mo>)</mo><mo>)</mo><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> has exactly one non-zero entry.

**Options:**

- **(A)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">I</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>II</mi><mo>)</mo></math> are true
- **(B)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>II</mi><mo>)</mo></math> is true
- **(C)** Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">I</mi><mo>)</mo></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>II</mi><mo>)</mo></math> is true
- **(D)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">I</mi><mo>)</mo></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">I</mi><mo>)</mo></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>II</mi><mo>)</mo></math> is true**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>sin</mi><mi>θ</mi><mo>=</mo><mi>y</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mi>z</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>≠</mo><mn>0</mn></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>θ</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac><mo>,</mo><mo> </mo><mi>z</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>θ</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p>Now, finding the trace of matrix we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>θ</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mi>θ</mi></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mstyle></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>x</mi><mi>sin</mi><mi>θ</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>x</mi><mi>sin</mi><mi>θ</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>x</mi><mi>sin</mi><mi>θ</mi><mfenced><mrow><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac></mstyle><mo>·</mo><mn>2</mn><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mi>x</mi><mi>sin</mi><mi>θ</mi><mfenced><mrow><mn>2</mn><mi>sin</mi><mfenced><mrow><mi mathvariant="normal">θ</mi><mo>+</mo><mi mathvariant="normal">π</mi></mrow></mfenced><mi>cos</mi><mfenced><mfrac><mi mathvariant="normal">π</mi><mn>3</mn></mfrac></mfenced></mrow></mfenced></mrow><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>·</mo><mfenced><mrow><mi>cos</mi><mfenced><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mfenced><mo>-</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>θ</mi><mo>+</mo><mn>2</mn><mi>π</mi></mrow></mfenced></mrow></mfenced><mo>+</mo><mi>x</mi><mi>sin</mi><mi>θ</mi><mfenced><mrow><mo>-</mo><mn>2</mn><mi>sin</mi><mi>θ</mi><mo>·</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mstyle><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi>π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mi>x</mi><mn>2</mn></mfrac><mo>·</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mi>cos</mi><mn>2</mn><mi>θ</mi></mrow></mfenced><mo>-</mo><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mstyle><mrow><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mi>cos</mi><mn>2</mn><mi>θ</mi><mo>-</mo><mn>4</mn><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mstyle><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mo>-</mo><mi>x</mi><mo>-</mo><mn>2</mn><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mrow></mfenced><mo>-</mo><mn>4</mn><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mstyle><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>4</mn><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi><mo>-</mo><mn>4</mn><mi>x</mi><msup><mi>sin</mi><mn>2</mn></msup><mi>θ</mi></mstyle><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mfrac><mstyle displaystyle="true"><mo>-</mo><mn>3</mn><mi>x</mi></mstyle><mrow><mn>4</mn><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mi>sin</mi><mfenced><mrow><mi>θ</mi><mo>+</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">π</mi></mrow><mn>3</mn></mfrac></mrow></mfenced></mrow></mfrac><mo>≠</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math> Trace <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">R</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>≠</mo><mn>0</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo></math> Statement (i) is False</p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mi>R</mi><mo>)</mo><mo>)</mo></math></p><p>Now, using the property <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mi>R</mi><mo>)</mo><mo>)</mo><mo>=</mo><mi>R</mi><mo>|</mo><mi>R</mi><mo>|</mo></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Trace</mi><mo> </mo><mo>(</mo><mi>Adj</mi><mo>(</mo><mi>Adj</mi><mo>(</mo><mi>R</mi><mo>)</mo><mo>)</mo><mo>)</mo><mo>=</mo><mi>x</mi><mi>y</mi><mi>z</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>)</mo><mo>≠</mo><mn>0</mn></math></p><p>{As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>≠</mo><mn>0</mn></math> proved above and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mi>z</mi></math> are non zero}</p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Trace</mi><mo>(</mo><mo>adj</mo><mo>(</mo><mo>adj</mo><mo>(</mo><mi>R</mi><mo>)</mo><mo>)</mo><mo>=</mo><mn>0</mn></math> is a false statement,</p><p>So, neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>II</mi></mfenced></math> are true</p></blockquote>

</details>

---

### Q26. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the determinant of a square matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>-</mo><mi>n</mi></math>, where m and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> satisfy <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>22</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mi>m</mi><mo>+</mo><mn>4</mn><mi>n</mi><mo>=</mo><mn>93</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>e</mi><mi>t</mi><mfenced><mrow><mi>n</mi><mo>&#160;</mo><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>m</mi><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mi>a</mi></msup><msup><mn>5</mn><mi>b</mi></msup><msup><mn>6</mn><mi>c</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>109</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>**

**Detailed Solution:**

<blockquote><p>We have been given that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mi>m</mi><mo>-</mo><mi>n</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>22</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mi>m</mi><mo>+</mo><mn>4</mn><mi>n</mi><mo>=</mo><mn>93</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>2</mn></math></p><p>Order <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>w</mi><mo>-</mo><mn>1</mn></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>w</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msup><mo>&#160;</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>&#215;</mo><mi>w</mi></math> is the order of the matrix.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>d</mi><mi>e</mi><mi>t</mi><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>&#160;</mo><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>m</mi><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><msup><mfenced close="|" open="|"><mrow><mn>5</mn><mi>A</mi></mrow></mfenced><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><mo>&#160;</mo><msup><mn>5</mn><mn>80</mn></msup><mo>&#160;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>16</mn></msup><mo>=</mo><msup><mn>2</mn><mn>5</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>16</mn></msup><mo>&#183;</mo><msup><mn>5</mn><mn>80</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>11</mn></msup><mo>&#160;</mo><msup><mn>5</mn><mn>80</mn></msup><mo>&#160;</mo><msup><mn>6</mn><mn>5</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>96</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q27. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mo>adj</mo><mo>(</mo><mn>2</mn><mo>adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>32</mn><mi>n</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>n</mi><mo>+</mo><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mfenced><mrow><mn>6</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mn>2</mn><mo>adj</mo><mo>(</mo><mn>2</mn><mo>adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>32</mn><mi>n</mi></msup></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mi>n</mi></msup><mfenced close="|" open="|"><mi>A</mi></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>adj</mo><mo>(</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>)</mo><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>adj</mi><mfenced><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo mathvariant="italic">=</mo><msup><mi>k</mi><mrow><mi>n</mi><mo mathvariant="italic">-</mo><mn mathvariant="italic">1</mn></mrow></msup><mi>adj</mi><mfenced><mi>A</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>|</mo><mo>adj</mo><mo>(</mo><mn>2</mn><mo>adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>|</mo><msup><mn>2</mn><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msup><mo>adj</mo><mo>(</mo><mo>adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>3</mn></msup><mo>&#183;</mo><mo>(</mo><mn>4</mn><msup><mo>)</mo><mn>3</mn></msup><mo>|</mo><mo>adj</mo><mo>(</mo><mo>adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>|</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>|</mo><mn>2</mn><mi>A</mi><msup><mo>|</mo><mrow><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><mo>|</mo><mn>2</mn><mi>A</mi><msup><mo>|</mo><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>12</mn></msup><mo>|</mo><mi>A</mi><msup><mo>|</mo><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>21</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>4</mn></msup><mo>=</mo><msup><mn>2</mn><mn>25</mn></msup><mo>=</mo><mo>(</mo><mn>32</mn><msup><mo>)</mo><mi>n</mi></msup><mo>=</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mrow><mn>5</mn><mi>n</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>n</mi><mo>+</mo><mi>&#945;</mi><mo>=</mo><mn>15</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>11</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q28. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>2</mn></math> be the adjoint of a matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mi>B</mi><mfenced open="[" close="]"><mtable><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>16</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>16</mn></math>**

**Detailed Solution:**

<blockquote><p>We have been given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>&#945;</mi><mo>&#62;</mo><mn>2</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mi>B</mi><mo>,</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>|</mo><mo>=</mo><mo>|</mo><mi>B</mi><mo>|</mo></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>=</mo><mo>(</mo><mn>8</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>)</mo><mo>-</mo><mn>3</mn><mo>(</mo><mn>4</mn><mo>-</mo><mn>3</mn><mi>&#945;</mi><mo>)</mo><mo>+</mo><mi>&#945;</mi><mo>(</mo><mo>-</mo><mi>&#945;</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>&#945;</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>(</mo><mi>&#945;</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>4</mn><mo>,</mo><mn>2</mn></math> but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>2</mn></math> so <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="box"><mi>&#945;</mi><mo>=</mo><mn>4</mn></menclose></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mi>B</mi><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mo>&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>8</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>8</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>12</mn></mtd><mtd><mn>12</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>8</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>48</mn><mo>-</mo><mn>96</mn><mo>+</mo><mn>32</mn><mo>=</mo><mo>-</mo><mn>16</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q29. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo><mn>6</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>5</mn><mo>!</mo></mtd><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd><mtd><mn>9</mn><mo>!</mo></mtd></mtr></mtable></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math>  is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>20</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>12</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>16</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>16</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo><mn>6</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>5</mn><mo>!</mo></mtd><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd><mtd><mn>9</mn><mo>!</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo><mn>6</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>5</mn><mo>!</mo></mtd><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>6</mn><mo>!</mo></mtd><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd></mtr><mtr><mtd><mn>7</mn><mo>!</mo></mtd><mtd><mn>8</mn><mo>!</mo></mtd><mtd><mn>9</mn><mo>!</mo></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo><mn>6</mn><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mn>5</mn><mo>!</mo><mo>&#215;</mo><mn>6</mn><mo>!</mo><mo>&#215;</mo><mn>7</mn><mo>!</mo><mfenced close="|" open="|"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>42</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>7</mn></mtd><mtd><mn>56</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p><p>Now using the property of adjoint of matrix we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mi>A</mi></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mi>n</mi></msup><mfenced close="|" open="|"><mi>A</mi></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is order of square matrix,</p><p>Now using the above two formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mn>4</mn></msup><mo>=</mo><msup><mn>2</mn><mn>12</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>12</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>16</mn></msup></math></p></blockquote>

</details>

---

### Q30. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mn>3</mn><mo mathvariant="italic">adj</mo><mfenced><mrow><mfenced open="|" close="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>12</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>11</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>12</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>10</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>11</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>10</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>10</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>We need to find the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>3</mn><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mfenced close="|" open="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mi>n</mi></msup><mfenced close="|" open="|"><mi>A</mi></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the order of the matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is a constant.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mfenced close="|" open="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mfenced><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><mn>2</mn></mrow></mfenced><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mi>A</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced close="|" open="|"><mrow><msup><mfenced><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><msup><mi>A</mi><mn>2</mn></msup></mfenced></mrow></mfenced></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><msup><mfenced><msup><mfenced><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mfenced><mn>3</mn></msup><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><msup><mi>A</mi><mn>2</mn></msup></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><msup><mfenced><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><mn>2</mn></mrow></mfenced><mn>6</mn></msup><msup><mfenced close="|" open="|"><msup><mi>A</mi><mn>2</mn></msup></mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><msup><mfenced><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><mn>2</mn></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mn>2</mn></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>21</mn></msup></math></p><p>Hence, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>21</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>6</mn><mn>10</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>11</mn></msup></math></p></blockquote>

</details>

---

### Q31. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mtable><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mtd><mtd><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mtd><mtd><mtable><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>(</mo><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mn>2</mn><mi>A</mi><mo>)</mo></mrow></mfenced></mrow></mfenced><mo>=</mo><mo>(</mo><mn>16</mn><msup><mo>)</mo><mi>n</mi></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>16</mn><mi>n</mi></msup></math>.</p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msup></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the order of the square matrix.</p><p>Let us find <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>-</mo><mn>0</mn><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mn>0</mn><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>0</mn><mo>&#215;</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mn>3</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced><mo>+</mo><mn>0</mn><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></msup><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mn>8</mn></msup><mo>=</mo><msup><mfenced><msup><mn>2</mn><mn>8</mn></msup></mfenced><mn>3</mn></msup><msup><mfenced open="|" close="|"><mi>A</mi></mfenced><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>24</mn></msup><mo>&#215;</mo><msup><mn>4</mn><mn>8</mn></msup><mo>=</mo><msup><mn>16</mn><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>16</mn><mn>6</mn></msup><mo>&#215;</mo><msup><mn>16</mn><mn>4</mn></msup><mo>=</mo><msup><mn>16</mn><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>16</mn><mn>10</mn></msup><mo>=</mo><msup><mn>16</mn><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>10</mn></math></p><p>Therefore, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>.</p></blockquote>

</details>

---

### Q32. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math>. If the determinant of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Adj</mo><mfenced><mrow><mn>2</mn><mo>.</mo><mo>Adj</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>84</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now simplifying,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mo>.</mo><mo>Adj</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mn>2</mn><mo>&#183;</mo><mo>Adj</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mfenced close="|" open="|"><mrow><mo>Adj</mo><mfenced><mrow><mn>2</mn><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><msup><mfenced close="|" open="|"><mrow><mn>2</mn><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup><msup><mfenced><msup><mfenced><mrow><msup><mn>2</mn><mi>n</mi></msup><mfenced close="|" open="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced close="|" open="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>A</mi></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></msup><msup><mfenced><msup><mfenced><msup><mn>2</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></msup><mo>=</mo><msup><mn>2</mn><mn>84</mn></msup></math></p><p>Now comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mn>84</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>84</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>21</mn></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math> now checking <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>25</mn><mo>-</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>21</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q33. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>T</mi></msup><mo>=</mo><mi>a</mi><mi>P</mi><mo>+</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">I</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>1</mn></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is a singular matrix
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>Adj</mo><mi>P</mi><mo>|</mo><mo>&#62;</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>Adj</mo><mi>P</mi><mo>|</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>Adj</mo><mi>P</mi><mo>|</mo><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>Adj</mo><mi>P</mi><mo>|</mo><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>T</mi></msup><mo>=</mo><mi>a</mi><mi>P</mi><mo>+</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">I</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Taking transpose on both sides we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msup><mi>P</mi><mi>T</mi></msup></mfenced><mi>T</mi></msup><mo>=</mo><msup><mfenced><mrow><mi>aP</mi><mo>+</mo><mo>(</mo><mi mathvariant="normal">a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">I</mi></mrow></mfenced><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><mi>a</mi><msup><mi>P</mi><mi mathvariant="normal">T</mi></msup><mo>+</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">I</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Subtract equation (1) and (2),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mi>T</mi></msup><mo>-</mo><mi>P</mi><mo>=</mo><mi>a</mi><mfenced><mrow><mi>P</mi><mo>-</mo><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><msup><mi>P</mi><mi mathvariant="italic">T</mi></msup></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8800;</mo><mo>-</mo><mn>1</mn></math></p><p>From equation (1),</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>a</mi><mi>P</mi><mo>+</mo><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><mo>-</mo><mi>I</mi></math></p><p>Taking adjoint on both sides,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Adj</mi><mo>&#160;</mo><mi>P</mi><mo>=</mo><mi>Adj</mi><mo>(</mo><mo>-</mo><mi>I</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mi>Adj</mi><mo>&#160;</mo><mi>P</mi></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mrow><mi>Adj</mi><mo>&#160;</mo><mo>(</mo><mo>-</mo><mi>I</mi><mo>)</mo></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mo>-</mo><mi>I</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>Adj</mo><mi>P</mi><mo>|</mo><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q34. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>m</mi></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>A</mi><mo>-</mo><mi mathvariant="normal">d</mi><mfenced><mrow><mo>Adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>m</mi></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;&#160;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>d</mi><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mo>-</mo><mi>d</mi><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mfenced close="]" open="["><mtable><mtr><mtd><mi>m</mi></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr></mtable></mfenced><mo>-</mo><mi>d</mi><mfenced close="]" open="["><mtable><mtr><mtd><mi>q</mi></mtd><mtd><mo>-</mo><mi>n</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>p</mi></mtd><mtd><mi>m</mi></mtd></mtr></mtable></mfenced></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>m</mi><mo>-</mo><mi>q</mi><mi>d</mi></mtd><mtd><mi>n</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced></mtd></mtr><mtr><mtd><mi>p</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced></mtd><mtd><mi>q</mi><mo>-</mo><mi>m</mi><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mi>q</mi><mi>d</mi></mrow></mfenced><mfenced><mrow><mi>q</mi><mo>-</mo><mi>m</mi><mi>d</mi></mrow></mfenced><mo>-</mo><mi>n</mi><mi>p</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mi>q</mi><mo>-</mo><msup><mi>m</mi><mn>2</mn></msup><mi>d</mi><mo>-</mo><msup><mi>q</mi><mn>2</mn></msup><mi>d</mi><mo>+</mo><mi>m</mi><mi>q</mi><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mi>p</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mi>q</mi><mo>-</mo><msup><mi>m</mi><mn>2</mn></msup><mi>d</mi><mo>-</mo><msup><mi>q</mi><mn>2</mn></msup><mi>d</mi><mo>+</mo><mi>m</mi><mi>q</mi><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mi>p</mi><mo>-</mo><mn>2</mn><mi>n</mi><mi>p</mi><mi>d</mi><mo>-</mo><mi>n</mi><mi>p</mi><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi></mrow></mfenced><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mfenced><mrow><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi></mrow></mfenced><mo>-</mo><mi>d</mi><mfenced><mrow><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mi>p</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>)</mo><mo>-</mo><mi>d</mi><mo>(</mo><mi>m</mi><mo>+</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>d</mi><mo>(</mo><mi>m</mi><mo>+</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>(</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi><mo>)</mo><mo>(</mo><mi>m</mi><mo>+</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mo>(</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi><mo>)</mo></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mi>m</mi><mi>q</mi><mo>-</mo><mi>n</mi><mi>p</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>m</mi><mo>+</mo><mi>q</mi></mrow></mfenced><mn>2</mn></msup></math></p><p>Hence, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is correct.</p>

</details>

---

### Q35. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi><mo>&#62;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><msub><mi>log</mi><mi>x</mi></msub><mi>y</mi></mtd><mtd><msub><mi>log</mi><mi>x</mi></msub><mi>z</mi></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>y</mi></msub><mi>x</mi></mtd><mtd><mn>2</mn></mtd><mtd><msub><mi>log</mi><mi>y</mi></msub><mi>z</mi></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>z</mi></msub><mi>x</mi></mtd><mtd><msub><mi>log</mi><mi>z</mi></msub><mi>y</mi></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mn>4</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mn>8</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>4</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><msub><mi>log</mi><mi>x</mi></msub><mi>y</mi></mtd><mtd><msub><mi>log</mi><mi>x</mi></msub><mi>z</mi></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>y</mi></msub><mi>x</mi></mtd><mtd><mn>2</mn></mtd><mtd><msub><mi>log</mi><mi>y</mi></msub><mi>z</mi></mtd></mtr><mtr><mtd><msub><mi>log</mi><mi>z</mi></msub><mi>x</mi></mtd><mtd><msub><mi>log</mi><mi>z</mi></msub><mi>y</mi></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mrow><mi>log</mi><mi>y</mi></mrow><mrow><mi>log</mi><mi>x</mi></mrow></mfrac></mtd><mtd><mfrac><mrow><mi>log</mi><mi>z</mi></mrow><mrow><mi>log</mi><mi>x</mi></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mi>log</mi><mi>x</mi></mrow><mrow><mi>log</mi><mi>y</mi></mrow></mfrac></mtd><mtd><mn>2</mn></mtd><mtd><mfrac><mrow><mi>log</mi><mi>z</mi></mrow><mrow><mi>log</mi><mi>y</mi></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mi>log</mi><mi>x</mi></mrow><mrow><mi>log</mi><mi>z</mi></mrow></mfrac></mtd><mtd><mfrac><mrow><mi>log</mi><mi>y</mi></mrow><mrow><mi>log</mi><mi>z</mi></mrow></mfrac></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>log</mi><mi>x</mi><mi>log</mi><mi>y</mi><mi>log</mi><mi>z</mi></mrow></mfrac><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mi>log</mi><mi>y</mi></mtd><mtd><mi>log</mi><mi>z</mi></mtd></mtr><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mn>2</mn><mi>log</mi><mi>y</mi></mtd><mtd><mi>log</mi><mi>z</mi></mtd></mtr><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mi>log</mi><mi>y</mi></mtd><mtd><mn>3</mn><mi>log</mi><mi>z</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>log</mi><mi>x</mi><mo>&#183;</mo><mi>log</mi><mi>y</mi><mo>&#183;</mo><mi>log</mi><mi>z</mi></mrow></mfrac><mfenced open="|" close="|"><mtable columnalign="left"><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mi>log</mi><mi>y</mi></mtd><mtd><mi>log</mi><mi>z</mi></mtd></mtr><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mn>2</mn><mi>log</mi><mi>y</mi></mtd><mtd><mi>log</mi><mi>z</mi></mtd></mtr><mtr><mtd><mi>log</mi><mi>x</mi></mtd><mtd><mi>log</mi><mi>y</mi></mtd><mtd><mn>3</mn><mi>log</mi><mi>z</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mrow><mi>log</mi><mi>x</mi><mo>&#183;</mo><mi>log</mi><mi>y</mi><mo>&#183;</mo><mi>log</mi><mi>z</mi></mrow><mrow><mi>log</mi><mi>x</mi><mo>&#183;</mo><mi>log</mi><mi>y</mi><mo>&#183;</mo><mi>log</mi><mi>z</mi></mrow></mfrac><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mo>adj</mo><msup><mi>A</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><msup><mi>A</mi><mn>2</mn></msup></mfenced><mn>4</mn></msup><mo>=</mo><msup><mfenced open="|" close="|"><mi>A</mi></mfenced><mn>8</mn></msup><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup></math></p>

</details>

---

### Q36. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>12</mn><mn>4</mn></msup></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<p>Given equation is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>.</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>12</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>3</mn></msup></mrow></msup><mo>=</mo><msup><mn>12</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mo>(</mo><mn>3</mn><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>3</mn></msup></mrow></msup><mo>=</mo><msup><mn>12</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>8</mn></msup><mo>=</mo><msup><mn>12</mn><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>.</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>A</mi></mfenced></mfrac><mo>&#215;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p>

</details>

---

### Q37. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>0</mn></msub><mo>=</mo><msup><mi>A</mi><mn>49</mn></msup><mo>+</mo><mn>2</mn><msup><mi>A</mi><mn>98</mn></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mi mathvariant="italic">n</mi></msub><mo>=</mo><mi>Adj</mi><mfenced><msub><mi>B</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mfenced></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><msub><mi>B</mi><mn>4</mn></msub></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>28</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>30</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>32</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>36</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>32</mn></msup></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>98</mn></msup><mo>=</mo><mi>I</mi><mo>;</mo><msup><mi>A</mi><mn>49</mn></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>B</mi><mn>0</mn></msub><mo>=</mo><msup><mi>A</mi><mn>98</mn></msup><mo>+</mo><mn>2</mn><msup><mi>A</mi><mn>49</mn></msup><mo>=</mo><mi>I</mi><mo>+</mo><mn>2</mn><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mi>n</mi></msub><mo>=</mo><mo>adj</mo><mfenced><msub><mi>B</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>B</mi><mn>4</mn></msub><mo>=</mo><mo>adj</mo><mfenced><msub><mi>B</mi><mn>3</mn></msub></mfenced><mo>=</mo><mo>adj</mo><mfenced><mrow><mo>adj</mo><msub><mi>B</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><msub><mi>B</mi><mn>1</mn></msub></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><msub><mi>B</mi><mn>0</mn></msub></mrow></mfenced></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><msub><mi>B</mi><mn>4</mn></msub></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><msub><mi>B</mi><mn>0</mn></msub></mfenced><msup><mn>2</mn><mn>4</mn></msup></msup><mo>=</mo><msup><mfenced close="|" open="|"><msub><mi>B</mi><mn>0</mn></msub></mfenced><mn>16</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>B</mi><mn>0</mn></msub></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mn>9</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi>B</mi><mn>4</mn></msub></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><msub><mi>B</mi><mn>0</mn></msub></mfenced><mn>16</mn></msup><mo>=</mo><msup><mn>9</mn><mn>16</mn></msup><mo>=</mo><msup><mn>3</mn><mn>32</mn></msup></math></p></blockquote>

</details>

---

### Q38. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Consider a matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#946;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#947;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mtd><mtd><mi>&#947;</mi><mo>+</mo><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></math> are three distinct natural numbers.
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>det</mo><mfenced><mrow><mo>adj</mo><mo>(</mo><mo>adj</mo><mfenced><mrow><mi>adj</mi><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>16</mn></msup></mrow></mfrac><mo>=</mo><msup><mn>2</mn><mn>32</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>16</mn></msup></math>, then the number of such <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>- tuples <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **42**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#946;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#947;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mtd><mtd><mi>&#947;</mi><mo>+</mo><mi>&#945;</mi></mtd><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub><mo>&#8594;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>+</mo><msub><mi>R</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#946;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#947;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mtd><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mtd><mtd><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mfenced close="|" open="|"><mtable><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#946;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#947;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></mrow></mfenced><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced></math></p><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></msup></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><msup><mn>2</mn><mn>4</mn></msup></msup><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>16</mn></msup></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|"><mfenced><mrow><mo>adj</mo><mo>(</mo><mo>adj</mo><mfenced><mrow><mi>adj</mi><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></mfenced><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>16</mn></msup></mrow></mfrac><mo>=</mo><msup><mn>2</mn><mn>32</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>16</mn></msup></mrow><mrow><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><msup><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>16</mn></msup></mrow></mfrac><mo>=</mo><msup><mn>2</mn><mn>32</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><mo>=</mo><msup><mn>2</mn><mn>32</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>16</mn></msup><mo>=</mo><msup><mfenced><mn>12</mn></mfenced><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>=</mo><mn>12</mn></math></p></blockquote><blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>&#8712;</mo><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>9</mn></math></p><p>Possible number all tuples <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>=</mo><mn>55</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> case for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>=</mo><mi>&#947;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> case when any two of these are equal are also included here but <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8800;</mo><mi>&#946;</mi><mo>&#8800;</mo><mi>&#947;</mi></math></p><p>Hence, number of distinct tuples <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>55</mn><mo>-</mo><mn>13</mn><mo>=</mo><mn>42</mn></math></p></blockquote>

</details>

---

### Q39. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $A$ be a $2 \times 2$ matrix with $\operatorname{det}(A)=-1$ and $\operatorname{det}((A+I)(\operatorname{Adj}(A)+I))=4$. Then the sum of the diagonal elements of $A$ can be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p>Now given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>+</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>+</mo><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mfenced close="|" open="|"><mi>A</mi></mfenced><mi>I</mi><mo>+</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>+</mo><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mo>-</mo><mi>I</mi><mo>+</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>+</mo><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>+</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mi>d</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>a</mi><mo>+</mo><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math> </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>I</mi><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mfenced><mrow><mo>adj</mo><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>(</mo><mo>adj</mo><mo>&#160;</mo><mi>A</mi><msup><mo>)</mo><mn>2</mn></msup><mo mathvariant="italic">-</mo><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">-</mo><mo mathvariant="italic">&#160;</mo><mmultiscripts><mi>C</mi><mn mathvariant="italic">5</mn><none></none><mprescripts></mprescripts><none></none><mn mathvariant="italic">5</mn></mmultiscripts><msup><mstyle mathvariant="italic"><mrow><mo>(</mo><mi mathvariant="normal">adj</mi><mo>&#160;</mo><mi>A</mi><mo>)</mo></mrow></mstyle><mn mathvariant="italic">5</mn></msup></math>, then the sum of all elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>**

**Detailed Solution:**

<p>Simplifying the given expression we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>I</mi><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>(</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>(</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>(</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>4</mn></msup><mo>-</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>(</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mo>(</mo><mi>I</mi><mo>-</mo><mo>adj</mo><mo>(</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>5</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>&#8658;</mo><mo>adj</mo><mfenced><mi>A</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>B</mi><mo>=</mo><msup><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>-</mo><mi>B</mi><mo>=</mo><msup><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mn>5</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, sum of elements of matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1</mn><mo>-</mo><mn>5</mn><mo>-</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>7</mn></math></p>

</details>

---

### Q41. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>2</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced close=""><mrow><mo>det</mo><mo>(</mo><mi>A</mi><mo>)</mo><mo>adj</mo><mfenced><mrow><mn>5</mn><mo>adj</mo><mfenced><msup><mi>A</mi><mn>3</mn></msup></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to _____.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1024</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>256</mn><mo>&#215;</mo><msup><mn>10</mn><mn>11</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math>**

**Detailed Solution:**

\(|(\operatorname{det}(\mathrm{A})) \operatorname{adj}(5 \operatorname{adj}(\mathrm{A}))|\)
\(=\left|2 \operatorname{adj}\left(5 \operatorname{adj}\left(\mathrm{A}^3\right)\right)\right|\)
\(=2^3 \mid \operatorname{adj}\left(5 \operatorname{adj}\left(\mathrm{A}^3\right) \|\right.\)
\(=2^3 \cdot\left|5 \operatorname{adj}\left(\mathrm{A}^3\right)\right|^2\)
\(=2^3\left(5^3 \cdot\left|\operatorname{adj}\left(\mathrm{A}^3\right)\right|\right)^2\)
\(=2^3 \cdot 5^6 \cdot\left|\operatorname{adj} \mathrm{A}^3\right|^2\)
\(=2^3 \cdot 5^6\left(\left(|\mathrm{~A}|^3\right)^2\right)^2\)
\(=2^3 \cdot 5^6 \cdot 2^{12}=2^{15} \times 5^6\)
\(=2^9 \times 10^6\)
\(=512 \times 10^6\)

</details>

---

### Q42. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>I</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>B</mi><mi>a</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>128</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>I</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p>Now by using property <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>adj</mi><mfenced><mrow><mi>P</mi><mi>Q</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mo>adj</mo><mi>Q</mi></mrow></mfenced><mfenced><mrow><mo>adj</mo><mi>P</mi></mrow></mfenced></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mi>B</mi><mo>&#183;</mo><mo>adj</mo><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>B</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>adj</mi><mfenced><mrow><mi>adj</mi><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mi>adj</mi><mn>2</mn><mi>A</mi></mrow></mfenced><mn>2</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="|" open="|"><msup><mn>2</mn><mn>3</mn></msup></mfenced><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><msup><mfenced><msup><mn>2</mn><mn>3</mn></msup></mfenced><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>{Property used <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>k</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mi>n</mi></msup><mfenced close="|" open="|"><mi>A</mi></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is order of matrix}</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>B</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>B</mi></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mi>i</mi><mi>i</mi><mi>i</mi><mo>)</mo></math></p><p>Now putting the value of equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>iii</mi></mfenced></math> in eq <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mi>B</mi><mo>&#183;</mo><mo>adj</mo><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>B</mi></mfenced><mn>2</mn></msup></math> </p><p>Now using<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>B</mi></mfenced></mfrac></math>as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>I</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mi>B</mi><mo>&#183;</mo><mo>adj</mo><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><mo>&#215;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><msup><mn>8</mn><mn>2</mn></msup></mfrac><mo>=</mo><mn>64</mn></math></p>

</details>

---

### Q43. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The positive value of the determinant of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, whose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>d</mi><mi>j</mi><mfenced><mrow><mi>A</mi><mi>d</mi><mi>j</mi><mfenced><mi>A</mi></mfenced></mrow></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd></mtr><mtr><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd></mtr></mtable></mfenced></math>, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd></mtr><mtr><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup></math> if it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd><mtd><mn>28</mn></mtd></mtr><mtr><mtd><mn>28</mn></mtd><mtd><mo>-</mo><mn>14</mn></mtd><mtd><mn>14</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><msup><mn>14</mn><mn>3</mn></msup><mo>&#160;</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><msup><mn>14</mn><mn>3</mn></msup><mo>&#215;</mo><mfenced><mn>14</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>4</mn></msup><mo>=</mo><msup><mfenced><mn>14</mn></mfenced><mn>4</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q44. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> invertible matrix. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>adj</mi><mfenced><mrow><mn>24</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>adj</mo><mfenced><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><mi mathvariant="normal">A</mi></mrow></mfenced></mrow></mfenced><mo>|</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>12</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>512</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mn>6</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>K</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mi>K</mi><mi>n</mi></msup><mfenced close="|" open="|"><mi>A</mi></mfenced></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is order of matrix</p><p>Given </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>adj</mi><mfenced><mrow><mn>24</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>adj</mi><mn>3</mn><mfenced><mrow><mi>adj</mi><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><mn>24</mn><mi>A</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>24</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>24</mn><mn>3</mn></msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced close="|" open="|"><mrow><mo>adj</mo><mn>2</mn><mi>A</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>24</mn><mn>3</mn></msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>24</mn><mn>3</mn></msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><msup><mn>2</mn><mn>3</mn></msup><msup><mn>2</mn><mn>3</mn></msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mfenced close="|" open="|"><mi>A</mi></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><msup><mn>24</mn><mn>3</mn></msup><mrow><msup><mn>2</mn><mn>3</mn></msup><msup><mn>2</mn><mn>3</mn></msup><msup><mn>3</mn><mn>3</mn></msup></mrow></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced><mrow><msup><mn>2</mn><mn>3</mn></msup><mo>&#183;</mo><mn>3</mn></mrow></mfenced><mn>3</mn></msup><mrow><msup><mn>2</mn><mn>6</mn></msup><msup><mn>3</mn><mn>3</mn></msup></mrow></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>64</mn></math></p>

</details>

---

### Q45. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo></math>{<math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>n</mi></msqrt><mo>:</mo><mn>1</mn><mo>&#10877;</mo><mi>n</mi><mo>&#10877;</mo><mn>50</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is odd}. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>S</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="right"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>&#931;</mi><mrow><mi>a</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mo>det</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mn>100</mn><mi>&#955;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>218</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>221</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>663</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1717</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>221</mn></math>**

**Detailed Solution:**

<p>We know that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mi>A</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced open="|" close="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix</p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup></math></p><p>Now find <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>A</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup></math></p><p>Now </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mi>&#931;</mi><mrow><mi>a</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mo>det</mo><mfenced><mrow><mo>adj</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mi>&#931;</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>48</mn><mn>2</mn></msup><mo>+</mo><msup><mn>50</mn><mn>2</mn></msup><mo>=</mo><mn>100</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>25</mn><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>100</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>&#215;</mo><mfrac><mrow><mn>25</mn><mo>&#215;</mo><mn>26</mn><mo>&#215;</mo><mn>51</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>100</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>221</mn><mo>=</mo><mi>&#955;</mi></math></p>

</details>

---

### Q46. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> real matrix. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mo>(</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>)</mo><mo>)</mo><mo>=</mo><msup><mn>2</mn><mn>41</mn></msup><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup></mfenced></math> equals ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>|</mo><mi>K</mi><mi>A</mi><mo>|</mo><mo>=</mo><msup><mi>K</mi><mi>n</mi></msup><mo>|</mo><mi>A</mi><mo>|</mo><mo>,</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> matrix</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mo>Adj</mo><mi mathvariant="normal">A</mi><mo>|</mo><mo>=</mo><mo>|</mo><mi mathvariant="normal">A</mi><msup><mo>|</mo><mrow><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> matrix</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mi>A</mi><mo>)</mo><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>41</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>3</mn></msup><mo>|</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>41</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>38</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mo>|</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>|</mo><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>38</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mn>2</mn><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>19</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>3</mn></msup><mo>|</mo><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>19</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>Adj</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>16</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mo>|</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>|</mo><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>16</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><msup><mo>|</mo><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>)</mo><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>4</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>3</mn></msup><mo>|</mo><mo>&#160;</mo><mi>A</mi><mo>|</mo><mo>=</mo><msup><mn>2</mn><mn>4</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msup><mi>A</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q47. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mfenced open="{" close=""><mtable><mtr><mtd><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>j</mi><mo>-</mo><mi>i</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><mi>j</mi></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>i</mi><mo>+</mo><mi>j</mi></mrow></msup><mo>&#160;</mo><mo>&#160;&#160;&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>&#62;</mo><mi>j</mi></mtd></mtr></mtable></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced><mrow><mn>3</mn><mo>Adj</mo><mfenced><mrow><mn>2</mn><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **108**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><mfenced close="" open="{"><mtable><mtr><mtd><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>j</mi><mo>-</mo><mi>i</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>&#160;&#160;</mo><mo>&#160;</mo><mo>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>=</mo><mi>j</mi></mtd></mtr><mtr><mtd><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mi>i</mi><mo>+</mo><mi>j</mi></mrow></msup><mo>&#160;</mo><mo>&#160;&#160;&#160;</mo><mi>if</mi><mo>&#160;</mo><mi>i</mi><mo>&#62;</mo><mi>j</mi></mtd></mtr></mtable></mfenced></math></p><p>The,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="right"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>4</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><mrow><mn>2</mn><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mfenced close="|" open="|"><mrow><mi>k</mi><mo>adj</mo><mfenced><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfenced><mo>=</mo><msup><mi>k</mi><mi>n</mi></msup><mfenced close="|" open="|"><mrow><mo>adj</mo><mfenced><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>6</mn></msup><msup><mfenced close="|" open="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><mrow><mi>k</mi><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced><msup><mi>k</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfenced><mi>n</mi></msup><mfenced open="|" close="|"><mrow><mo>adj</mo><mfenced><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced></mrow></mfenced><mo>=</mo><msup><mfenced><msup><mi>k</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfenced><mi>n</mi></msup><msup><mfenced open="|" close="|"><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mn>3</mn><mo>adj</mo><mfenced><mrow><mn>2</mn><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mn>12</mn><mn>3</mn></msup><msup><mfenced close="|" open="|"><msup><mrow><mo mathvariant="italic">&#160;</mo><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><msup><mn>12</mn><mn>3</mn></msup><mrow><mo>|</mo><mo>&#160;</mo><mi>A</mi><msup><mo>|</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><msup><mn>12</mn><mn>3</mn></msup><mn>16</mn></mfrac><mo>=</mo><mn>108</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>det</mo><mfenced><msup><mi>A</mi><mn>4</mn></msup></mfenced><mo>+</mo><mo>det</mo><mfenced><mrow><msup><mi>A</mi><mn>10</mn></msup><mo>-</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>10</mn></msup></mrow></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mn>15</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mn>15</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>32</mn></mtd><mtd><mn>33</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>10</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>32</mn></mtd><mtd><mn>33</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>32</mn></mtd><mtd><mn>33</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1024</mn></mtd><mtd><mn>1023</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>6</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>16</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>16</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>16</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mo>-</mo><mn>240</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>256</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>5</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mo>-</mo><mn>240</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>256</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>32</mn></mtd><mtd><mo>-</mo><mn>1056</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1024</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>10</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>32</mn></mtd><mtd><mo>-</mo><mn>1056</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1024</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>32</mn></mtd><mtd><mo>-</mo><mn>1056</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1024</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1024</mn></mtd><mtd><mo>-</mo><mn>1047552</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1048576</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>10</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>10</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1024</mn></mtd><mtd><mn>1023</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1024</mn></mtd><mtd><mo>-</mo><mn>1047552</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1048576</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1048575</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1048575</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>det</mi><mfenced><mrow><msup><mi>A</mi><mn>10</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>Adj</mi><mfenced><mrow><mn>2</mn><mi>A</mi></mrow></mfenced></mrow></mfenced><mn>10</mn></msup></mrow></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1048575</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1048575</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mo>det</mo><mfenced><msup><mi>A</mi><mn>4</mn></msup></mfenced><mo>+</mo><mo>det</mo><mfenced><mrow><msup><mi>A</mi><mn>10</mn></msup><mo>-</mo><mo>(</mo><mo>Adj</mo><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>A</mi><mo>)</mo><msup><mo>)</mo><mn>10</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><msup><mfenced><mrow><mo>det</mo><mfenced><mi>A</mi></mfenced></mrow></mfenced><mn>4</mn></msup><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q49. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="right"><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced close="]" open="["><msub><mi>q</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math> is a matrix satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mi>k</mi><msub><mi>I</mi><mn>3</mn></msub></math> for
some non-zero <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>23</mn></msub><mo>=</mo><mo>-</mo><mfrac><mi>k</mi><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>Q</mi></mfenced><mo>=</mo><mfrac><msup><mi>k</mi><mn>2</mn></msup><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></math> is equal to_________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mo>=</mo><mi>k</mi><mi>I</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>P</mi></mfenced><mo>.</mo><mfenced close="|" open="|"><mi>Q</mi></mfenced><mo>=</mo><msup><mi>k</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>P</mi></mfenced><mo>=</mo><mn>2</mn><mi>k</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>P</mi></math> is an invertible matrix</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>P</mi><mi>Q</mi><mo>=</mo><mi>k</mi><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>k</mi><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mfrac><mrow><mo>&#160;</mo><mi>adj</mi><mo>.</mo><mi>P</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><msub><mi>q</mi><mn>23</mn></msub><mo>=</mo><mo>-</mo><mfrac><mi>k</mi><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mo>-</mo><mfenced><mrow><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mi>k</mi><mn>8</mn></mfrac><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mi>P</mi></mfenced><mo>=</mo><mn>2</mn><mi>k</mi><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>10</mn><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Put value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>.. we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>17</mn></math></p>

</details>

---

### Q50. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let A be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>adj</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mo>adj</mo><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mi>&#955;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msup><mfenced><msup><mi>B</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>&#8868;</mo></msup></mfenced><mo>=</mo><mi>&#956;</mi></math>, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>81</mn></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>9</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>81</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>9</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>81</mn></mfrac></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>81</mn></mfrac></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mo>&#177;</mo><mn>3</mn><mo>=</mo><mi>&#955;</mi><mo>&#8658;</mo><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mo>&#160;</mo><mi>A</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><msup><mfenced><msup><mi>B</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mi>T</mi></msup></mfenced><mo>=</mo><mfenced close="|" open="|"><msup><mi>B</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>B</mi></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mfenced close="|" open="|"><mi>B</mi></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>81</mn></mfrac><mo>=</mo><mi>&#956;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced><mrow><mfenced close="|" open="|"><mi>&#955;</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>&#956;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>81</mn></mfrac></mrow></mfenced></math>.</p>

</details>

---

### Q51. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo> </mo><mi>B</mi><mo>=</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></math> and <math><mi>C</mi><mo>=</mo><mn>3</mn><mi>A</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>B</mi></mrow></mfenced><mfenced close="|" open="|" separators="|"><mi>C</mi></mfenced></mfrac></math> is equal to

**Options:**

- **(A)** <math><mn>8</mn></math>
- **(B)** <math><mn>16</mn></math>
- **(C)** <math><mn>72</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>8</mn></math>**

**Detailed Solution:**

<math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mfenced separators="|"><mrow><mn>9</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>13</mn><mo>+</mo><mn>1</mn><mo>-</mo><mn>8</mn><mo>=</mo><mn>6</mn></math>
<math><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi></mi><mi>B</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi></mi><mi>a</mi><mi>d</mi><mi>j</mi><mi></mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></msup><mo>=</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>36</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>C</mi></mfenced><mo>=</mo><mfenced open="|" close="|" separators="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mn>3</mn><mn>3</mn></msup><mo>&#215;</mo><mn>6</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mfenced open="|" close="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>B</mi></mrow></mfenced><mfenced open="|" close="|" separators="|"><mi>C</mi></mfenced></mfrac><mo>=</mo><mfrac><mrow><mn>36</mn><mo>&#215;</mo><mn>36</mn></mrow><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>&#215;</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mn>8</mn></math>

</details>

---

### Q52. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be any <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> invertible matrix. Then which one of the following is not always true?

**Options:**

- **(A)** <math><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced><mo>=</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>.</mo><mi> </mi><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>.</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(C)** <math><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j (A)</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mi> </mi><mo>.</mo><mi> </mi><mi>A</mi></math>
- **(D)** <math><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>.</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>.</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> (A)</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<math><mo>∵</mo><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow></mfrac><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow></mfenced></math>

<math><mo>∴</mo><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>…</mo><mo>…</mo><mfenced separators="|"><mrow><mn>i</mn></mrow></mfenced></math>

<math><mo>∵</mo><mi>A</mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mi mathvariant="normal">I</mi></math>

<math><mo>∴</mo><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<math><mo>∴</mo><msup><mrow><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow></mfrac><mi>A</mi></math>

<math><mo>∴</mo></math><math><mi>  from (i)</mi> </math></br></br><math><mi>a</mi><mi>d</mi><mi>j</mi><mfenced separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi> </mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>.</mo><mi>A</mi></math>

</details>

---

### Q53. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Adj</mi><mfenced separators="|"><mrow><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>A</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>72</mn></mtd><mtd><mo>-</mo><mn>84</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>63</mn></mtd><mtd><mn>51</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>51</mn></mtd><mtd><mn>63</mn></mtd></mtr><mtr><mtd><mn>84</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>51</mn></mtd><mtd><mn>84</mn></mtd></mtr><mtr><mtd><mn>63</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>72</mn></mtd><mtd><mo>-</mo><mn>63</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>84</mn></mtd><mtd><mn>51</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>51</mn></mtd><mtd><mn>63</mn></mtd></mtr><mtr><mtd><mn>84</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>4</mn><mo>+</mo><mn>12</mn></mtd><mtd><mo>-</mo><mn>6</mn><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>8</mn><mo>-</mo><mn>4</mn></mtd><mtd><mn>12</mn><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mo>-</mo><mn>9</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>12</mn></mtd><mtd><mn>13</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>48</mn></mtd><mtd><mo>-</mo><mn>27</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>36</mn></mtd><mtd><mn>39</mn></mtd></mtr></mtable></mfenced></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>A</mi><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>24</mn></mtd><mtd><mo>-</mo><mn>36</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>48</mn></mtd><mtd><mn>12</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;&#160;&#160;</mo><mfenced separators="|"><mrow><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>72</mn></mtd><mtd><mo>-</mo><mn>63</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>84</mn></mtd><mtd><mn>51</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Adj</mi><mfenced separators="|"><mrow><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>51</mn></mtd><mtd><mn>84</mn></mtd></mtr><mtr><mtd><mn>63</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mfenced><mi>T</mi></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>51</mn></mtd><mtd><mn>63</mn></mtd></mtr><mtr><mtd><mn>84</mn></mtd><mtd><mn>72</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q54. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn><mi>a</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>=</mo><mi>A</mi><mi>&#160;</mi><msup><mi>A</mi><mi>T</mi></msup></math> , then <math><mn>5</mn><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>13</mn></math>
- **(C)** <math><mo>-</mo><mn>1</mn></math>
- **(D)** <math><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>5</mn></math>**

**Detailed Solution:**

<math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn><mi>a</mi></mtd><mtd><mo>-</mo><mi>b</mi></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math> and <math><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>5</mn><mi>a</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>b</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mi>A</mi><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>25</mn><msup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>b</mi></mrow><mrow><mn>2</mn></mrow></msup></mtd><mtd><mn>15</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mtd></mtr><mtr><mtd><mn>15</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi></mtd><mtd><mn>13</mn></mtd></mtr></mtable></mrow></mfenced></math>

Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi><mo>=</mo><mfenced open="|" close="|" separators="|"><mi>A</mi></mfenced><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>10</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>10</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></mtd></mtr></mtable></mfenced></math>

Given <math><mi>A</mi><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>=</mo><mi>A</mi><mo>.</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>&#160;</mi><mi>A</mi></math>

<math><mn>15</mn><mi>a</mi><mo>-</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></math> ......(i)

<math><mn>10</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>13</mn></math> .......(ii)

Solving we get

<math><mn>5</mn><mi>a</mi><mo>=</mo><mn>2</mn></math> and <math><mi>b</mi><mo>=</mo><mi>&#160;</mi><mn>3</mn></math>

<math><mo>&#8756;</mo></math> <math><mn>5</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>5</mn></math>

</details>

---

### Q55. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mrow><mn>5</mn><mi>&#160;</mi><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi>A</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math><mo>±</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>
- **(B)** <math><mo>±</mo><mn>5</mn></math>
- **(C)** <math><mo>±</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mo>±</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>±</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math><mfenced close="|" open="|" separators="|"><mrow><mn>5</mn><mi>&#160;</mi><mi>A</mi><mi>d</mi><mi>j</mi><mi>&#160;</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math>

<math><mn>125</mn><mi>&#160;</mi><mo>|</mo><mi>a</mi><mi>d</mi><mi>j</mi><mi>&#160;</mi><mi>A</mi><mo>|</mo><mo>=</mo><mn>5</mn></math>

Since <math><mo>[</mo><mi>A</mi><mo>]</mo></math> is <math><mn>3</mn><mo>&#215;</mo><mn>3</mn></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>&#160;</mi><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<math><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mo>&#177;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>.</mo></math></p>

</details>

---

### Q56. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math> is the adjoint of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>A</mi></mfenced><mo>=</mo><mn>4</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>P</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced close="|" open="|"><mrow><mi>a</mi><mi>d</mi><mi>j</mi><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>where</mi><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>P</mi></mfenced><mo>=</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"/><mo>=</mo><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mn>12</mn><mo>&#8722;</mo><mn>12</mn></mrow></mfenced><mo>&#8722;</mo><mi>&#945;</mi><mo>&#215;</mo><mfenced><mrow><mn>4</mn><mo>&#8722;</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mo>&#215;</mo><mfenced><mrow><mn>4</mn><mo>&#8722;</mo><mn>6</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mi>6</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>1</mn><mn>6</mn></math></p><p><math><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>11</mn></math></p>

</details>

---

### Q57. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

Let A be a $2 \times 2$ matrix
Statement-1 $: \operatorname{adj}(\operatorname{adj} A)=A$
Statement-2 : $|\operatorname{adj} \mathrm{A}|=|\mathrm{A}|$

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation for Statement-1
- **(C)** Statement-1 is true, Statement-2 is false
- **(D)** Statement-1 is false, Statement-2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation for Statement-1**

**Detailed Solution:**

$$
\begin{aligned}
& |\operatorname{adj} A|=|A|^{n-1}=|A|^{2-1}=|A| \\
& \operatorname{adj}(\operatorname{adj} A)=|A|^{n-2} A=|A|^0 A=A
\end{aligned}
$$

</details>

---

