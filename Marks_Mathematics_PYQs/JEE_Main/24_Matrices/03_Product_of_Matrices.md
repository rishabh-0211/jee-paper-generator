# JEE Main Mathematics - Matrices

## Topic 3: Product of Matrices

**Total Questions:** 83

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 9 & 3 & 1 \end{bmatrix}$ and $B = [b_{ij}]$, $1 \leq i, j \leq 3$. If $B = A^{99} - I$, then the value of $\dfrac{b_{31} - b_{21}}{b_{32}}$ is :

**Options:**

- **(A)** $99$
- **(B)** $199$
- **(C)** $149$
- **(D)** $159$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $149$**

**Detailed Solution:**

Let $A = I + C$, where $I$ is the identity matrix and $C = \begin{bmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 9 & 3 & 0 \end{bmatrix}$.

Calculating the powers of $C$, we get:

$C^2 = \begin{bmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 9 & 3 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 9 & 3 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 9 & 0 & 0 \end{bmatrix}$

$C^3 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 9 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 9 & 3 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$

Since $C^3 = 0$, all higher powers of $C$ are also zero matrices. Using the binomial expansion for $A^{99}$:

$A^{99} = (I + C)^{99} = I + 99C + ^{99}C_{2}C^2$

Given $B = A^{99} - I$, we have:

$B = 99C + 4851C^2$

Substituting the matrices $C$ and $C^2$:

$B = 99 \begin{bmatrix} 0 & 0 & 0 \\ 3 & 0 & 0 \\ 9 & 3 & 0 \end{bmatrix} + 4851 \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 9 & 0 & 0 \end{bmatrix}$

From this, we can extract the required elements of $B$:

$b_{31} = 99 \times 9 + 4851 \times 9 = 9(99 + 4851) = 9 \times 4950 = 44550$

$b_{21} = 99 \times 3 = 297$

$b_{32} = 99 \times 3 = 297$

Now, substituting these values into the given expression:

$\dfrac{b_{31} - b_{21}}{b_{32}} = \dfrac{44550 - 297}{297} = \dfrac{44550}{297} - 1$

$\dfrac{b_{31} - b_{21}}{b_{32}} = 150 - 1 = 149$

Answer: $149$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $S = \left\{A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} : a, b, c, d \in \{0, 1, 2, 3, 4\} \text{ and } A^2 - 4A + 3I = 0\right\}$ be a set of $2 \times 2$ matrices. Then the number of matrices in $S$, for which the sum of the diagonal elements is equal to $4$, is:

**Options:**

- **(A)** $20$
- **(B)** $17$
- **(C)** $21$
- **(D)** $19$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $19$**

**Detailed Solution:**

The characteristic equation of a $2 \times 2$ matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is given by:

$A^2 - \text{Tr}(A)A + \det(A)I = 0$

We are given that the sum of the diagonal elements is $4$, so $\text{Tr}(A) = a + d = 4$. Substituting this into the characteristic equation, we get:

$A^2 - 4A + (ad - bc)I = 0$

We are also given that the matrix satisfies:

$A^2 - 4A + 3I = 0$

Comparing the two equations, we must have:

$ad - bc = 3$

We need to find the number of quadruples $(a, b, c, d)$ with elements from the set $\{0, 1, 2, 3, 4\}$ such that $a + d = 4$ and $ad - bc = 3$. Let us analyze the possible values for $a$ and $d$:

Case 1: $a = 0, d = 4$
$ad - bc = 3 \implies 0 - bc = 3 \implies bc = -3$
Since $b, c \in \{0, 1, 2, 3, 4\}$, $bc \ge 0$. Thus, there are no solutions.

Case 2: $a = 1, d = 3$
$ad - bc = 3 \implies 3 - bc = 3 \implies bc = 0$
For $bc = 0$, either $b = 0$ or $c = 0$.
If $b = 0$, $c$ can take any of the $5$ values from the set.
If $c = 0$, $b$ can take any of the $5$ values from the set.
The pair $(0, 0)$ is counted twice, so the number of pairs $(b, c)$ is $5 + 5 - 1 = 9$.

Case 3: $a = 2, d = 2$
$ad - bc = 3 \implies 4 - bc = 3 \implies bc = 1$
The only possible pair from the given set is $b = 1, c = 1$. This gives $1$ solution.

Case 4: $a = 3, d = 1$
$ad - bc = 3 \implies 3 - bc = 3 \implies bc = 0$
Similar to Case 2, there are $9$ possible pairs for $(b, c)$.

Case 5: $a = 4, d = 0$
$ad - bc = 3 \implies 0 - bc = 3 \implies bc = -3$
Again, there are no solutions.

Adding the valid matrices from all cases, the total number of matrices is $9 + 1 + 9 = 19$.

Answer: $19$

</details>

---

### Q3. JEE Main 2026 (28 January Shift 2)

*Type:* `numerical` | *Level:* `2`

Let $A=\left[\begin{array}{ll}3 & -4 \\ 1 & -1\end{array}\right]$ and $B$ be two matrices such that $A^{100}=100 B+I$. Then the sum of all the elements of $\mathrm{B}^{100}$ is $\_\_\_\_$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

$A = I + \begin{bmatrix} 2 & -4 \\ 1 & -2 \end{bmatrix}$, let $M = \begin{bmatrix} 2 & -4 \\ 1 & -2 \end{bmatrix}$
$M^2 = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = M^3 = M^4 = \ldots = M^{100}$
$A^{100} = (I + M)^{100} = \sum_{r=0}^{100} \binom{100}{r} M^r \cdot I$
$A^{100} = I + 100M = I + 100B$
$\therefore M = B \Rightarrow M^{100} = B^{100} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of $3 \times 2$ matrices A, which can be formed using the elements of the set $\{-2,-1,0,1,2\}$ such that the sum of all the diagonal elements of $\mathrm{A}^{\mathrm{T}} \mathrm{A}$ is 5, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **312**

**Detailed Solution:**

For a 3×2 matrix A, the diagonal sum of $A^T A$ equals the sum of squares of all 6 elements of A. We need:
$a_{11}^2 + a_{21}^2 + a_{31}^2 + a_{12}^2 + a_{22}^2 + a_{32}^2 = 5$ where each element is from $\{-2, -1, 0, 1, 2\}$.
Possible squares: $0^2=0$, $(\pm 1)^2=1$, $(\pm 2)^2=4$.
Case 1:
Distribution $4+1+0+0+0+0$ (one ±2, one ±1, four 0's). 
Arrangements: $\binom{6}{1} \times \binom{5}{1} = 30$.
Sign choices: $2 \times 2 = 4$. Total: $30 \times 4 = 120$.
Case 2:
Distribution $1+1+1+1+1+0$ (five ±1, one 0). 
Arrangements: $\binom{6}{1} = 6$ ways to place the 0.
Sign choices for five ±1: $2^5 = 32$. Total: $6 \times 32 = 192$.
Total matrices: $120 + 192 = 312$

</details>

---

### Q5. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the matrices $\mathrm{A}=\left[\begin{array}{ll}3 & -4 \\ 1 & -1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}-29 & 49 \\ -13 & 18\end{array}\right]$, if $\left(\mathrm{A}^{15}+\mathrm{B}\right)\left[\begin{array}{l}x \\ y\end{array}\right]=\left[\begin{array}{l}0 \\ 0\end{array}\right]$, then among the following which one is true?

**Options:**

- **(A)** $x=5, y=7$
- **(B)** $x=18, y=11$
- **(C)** $x=11, y=2$
- **(D)** $x=16, y=3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x=11, y=2$**

**Detailed Solution:**

Here $A^n = \begin{bmatrix} 2n+1 & -4n \\ n & -2n+1 \end{bmatrix}$
$\Rightarrow A^{15} = \begin{bmatrix} 31 & -60 \\ 15 & -29 \end{bmatrix}$
$\Rightarrow A^{15} + B = \begin{bmatrix} 2 & -11 \\ 2 & -11 \end{bmatrix}$
Now $(A^{15} + B) \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
$\Rightarrow \begin{bmatrix} 2 & -11 \\ 2 & -11 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
$\Rightarrow 2x - 11y = 0 \Rightarrow x = \frac{11y}{2}$.
For $y = 2$, $x = 11$.

</details>

---

### Q6. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `3`

For some $\alpha, \beta \in \mathbf{R}$, let $A=\left[\begin{array}{ll}\alpha & 2 \\ 1 & 2\end{array}\right]$ and $B=\left[\begin{array}{ll}1 & 1 \\ 1 & \beta\end{array}\right]$ be such that $A^{2}-4 A+2 I=B^{2}-3 B+I=O$. Then $\left(\operatorname{det}\left(\operatorname{adj}\left(A^{3}-B^{3}\right)\right)\right)^{2}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **225**

**Detailed Solution:**

From $A^2 - 4A + 2I = O$: characteristic equation is $\lambda^2 - 4\lambda + 2 = 0$.
For $A$: $\alpha + 2 = 4 \Rightarrow \alpha = 2$.
From $B^2 - 3B + I = O$: characteristic equation is $\lambda^2 - 3\lambda + 1 = 0$.
For $B$: $\beta + 1 = 3 \Rightarrow \beta = 2$.
$A^3 = 14A - 8I$, $B^3 = 8B - 3I$.
$A^3 - B^3 = 14A - 8B - 5I = \begin{bmatrix} 15 & 20 \\ 6 & 7 \end{bmatrix}$.
$\det(A^3 - B^3) = 105 - 120 = -15$.
For 2×2 matrix: $\det(\text{adj}(M)) = \det(M)$.
$(\det(\text{adj}(A^3 - B^3)))^2 = 225$.

</details>

---

### Q7. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the matrix $A=\left[\begin{array}{lll}1 & 0 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{array}\right]$ satisfy $A^n=A^{n-2}+A^2-I$ for $\mathrm{n} \geq 3$. Then the sum of all the elements of $\mathrm{A}^{50}$ is :-

**Options:**

- **(A)** $53$
- **(B)** $52$
- **(C)** $39$
- **(D)** $44$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $53$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}^{50}=\mathrm{A}^{48}+\mathrm{A}^2-\mathrm{I} \\ & =\mathrm{A}^{46}+2\left(\mathrm{~A}^2-\mathrm{I}\right) \\ & =\mathrm{A}^{44}+3\left(\mathrm{~A}^2-\mathrm{I}\right) \\ & =\mathrm{A}^2+24\left(\mathrm{~A}^2-\mathrm{I}\right) \\ & =25 \mathrm{~A}^2-24 \mathrm{I}\end{aligned}$
$\begin{aligned}
& =25\left[\begin{array}{lll}
1 & 0 & 0 \\
1 & 1 & 0 \\
1 & 0 & 1
\end{array}\right]-24\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] \\
& =\left[\begin{array}{ccc}
1 & 0 & 0 \\
25 & 1 & 0 \\
25 & 0 & 1
\end{array}\right]
\end{aligned}$
Sum $=53$
option (1)

</details>

---

### Q8. JEE Main 2025 (4 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let $A=\left[\begin{array}{ccc}\cos \theta & 0 & -\sin \theta \\ 0 & 1 & 0 \\ \sin \theta & 0 & \cos \theta\end{array}\right]$. If for some $\theta \in(0, \pi)$, $A^2=A^T$, then the sum of the diagonal elements of the matrix $(\mathrm{A}+\mathrm{I})^3+(\mathrm{A}-\mathrm{I})^3-6 \mathrm{~A}$ is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\because \mathrm{A}$ is orthogonal matrix
$\begin{aligned}
& \therefore A^T=A^{-1} \\
& \Rightarrow A^2=A^{-1} \left(\because \mathrm{A}^2=\mathrm{A}^{\mathrm{T}}\right) \\
& \Rightarrow A^3=I \\
& \text { let } B=(A+I)^3+(A-I)^3-6 A \\
& =2\left(A^3+3 A\right)-6 A \\
& =2 A^3 \\
& B=2 I=\left[\begin{array}{lll}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{array}\right]
\end{aligned}$
Now sum of diagonal elements $=2+2+2=6$

</details>

---

### Q9. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ be a $3 \times 3$ real matrix such that $A^2(A-2 I)-$ $4(\mathrm{~A}-\mathrm{I})=\mathrm{O}$, where I and O are the identity and null matrices, respectively. If $A^5=\alpha A^2+\beta A+\gamma I$, where $\alpha, \beta$ and $\gamma$ are real constants, then $\alpha+\beta+\gamma$ is equal to:

**Options:**

- **(A)** $12$
- **(B)** $20$
- **(C)** $76$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $12$**

**Detailed Solution:**

$\begin{aligned} & A^3-2 A^2-4 A+4 I=0 \\ & A^3=2 A^2+4 A-4 I \\ & A^4=2 A^3+4 A^2-4 A \\ & =2\left(2 A^2+4 A-4 I\right)+4 A^2-4 A \\ & A^4=8 A^2+4 A-8 I \\ & A^5=8 A^3+4 A^2-8 A \\ & =8\left(2 A^2+4 A-4 I\right)+4 A^2-8 A \\ & A^5=20 A^2+24 A-32 I \\ & \therefore \alpha=20, \beta=24, \gamma=-32 \\ & \therefore \alpha+\beta+\gamma=12\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left[a_{i j}\right]$ be a matrix of order $3 \times 3$, with $a_{i j}=(\sqrt{2})^{i+j}$. If the sum of all the elements in the third row of $A^2$ is $\alpha+\beta \sqrt{2}, \alpha, \beta \in \mathbf{Z}$, then $\alpha+\beta$ is equal to :

**Options:**

- **(A)** 280
- **(B)** 224
- **(C)** 210
- **(D)** 168

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 224**

**Detailed Solution:**

$\begin{aligned} & A=\left[\begin{array}{lll}(\sqrt{2})^2 & (\sqrt{2})^3 & (\sqrt{2})^4 \\ (\sqrt{2})^3 & (\sqrt{2})^4 & (\sqrt{2})^5 \\ (\sqrt{2})^4 & (\sqrt{2})^5 & (\sqrt{2})^6\end{array}\right] \\ & A=\left[\begin{array}{ccc}2 & 2 \sqrt{2} & 4 \\ 2 \sqrt{2} & 4 & 4 \sqrt{2} \\ 4 & 4 \sqrt{2} & 8\end{array}\right] \\ & A^2=2^2\left[\begin{array}{ccc}1 & \sqrt{2} & 2 \\ \sqrt{2} & 2 & 2 \sqrt{2} \\ 2 & 2 \sqrt{2} & 4\end{array}\right]\left[\begin{array}{ccc}1 & \sqrt{2} & 2 \\ \sqrt{2} & 2 & 2 \sqrt{2} \\ 2 & 2 \sqrt{2} & 4\end{array}\right]\end{aligned}$

$=4\left[\begin{array}{ccc}- & - & - \\ - & - & - \\ (2+4+8) & (2 \sqrt{2}+4 \sqrt{2}+8 \sqrt{2}) & (4+8+16)\end{array}\right]$




Sum of elements of $3^{\text {nd }}$ row $=4(14+14 \sqrt{2}+28)$
$\begin{aligned}
& =4(42+14 \sqrt{2}) \\
& =168+56 \sqrt{2} \\
& \alpha+\beta \sqrt{2} \\
\therefore & \alpha+\beta=168+56=224
\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let \(\mathrm{S}=\left\{\mathrm{m} \in \mathbf{Z}: \mathrm{A}^{\mathrm{m}^2}+\mathrm{A}^{\mathrm{m}}=3 \mathrm{I}-\mathrm{A}^{-6}\right\}\), where \(\mathrm{A}=\left[\begin{array}{cc}2 & -1 \\ 1 & 0\end{array}\right]\). Then \(\mathrm{n}(\mathrm{S})\) is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

$A=\left[\begin{array}{cc}
2 & -1 \\
1 & 0
\end{array}\right]$
Now finding characteristic equation
$\begin{aligned}
& \left|\begin{array}{cc}
2-\lambda & -1 \\
1 & -\lambda
\end{array}\right|=0 \\
& \Rightarrow(2-\lambda)(-\lambda)-(-1)(1)=-2 \lambda+\lambda^2+1=0 \\
& \Rightarrow \lambda^2-2 \lambda+1=0 \\
& \Rightarrow(\lambda-1)^2=0 \\
& \Rightarrow \lambda=1
\end{aligned}$
Since $A$ satisfies $(A-I)^2=0$
$\begin{aligned}
& \therefore \quad A=I+N \text { where } \\
& N=A-I \\
& N=\left[\begin{array}{ll}
1 & -1 \\
1 & -1
\end{array}\right] \\
& N^2=0 \\
& A^m=(I+N)^m=I+m N \\
& A^m \cdot A^m=(I+m N)(I+m N)=I+2 m N+m^2 N^2
\end{aligned}$
$\text { Since } N^2=0$
$\Rightarrow \quad A^{m^2}=I+2 m N$
Now putting in given condition
$\begin{aligned}
& I+m^2 N+I+m N=3 I-A^{-6} \\
& A^{-1}=\left[\begin{array}{cc}
0 & 1 \\
-1 & 2
\end{array}\right] \\
& A^{-6}=\left(A^{-1}\right)^6=I+(-6) N
\end{aligned}$
$\therefore \quad$ Putting in (i)
$\begin{aligned}
& \left(m^2+m\right) N=I-(I-6 N) \\
& \left(m^2+m\right) N=6 N
\end{aligned}$

Since $N \neq 0$
$\begin{aligned}
& \Rightarrow m^2+m=6 \\
& \Rightarrow m^2+m-6=0 \\
& \Rightarrow(m-2)(m+3)=0 \\
& \Rightarrow m=2,-3
\end{aligned}$
$\therefore \quad$ Number of elements in $S$ is 2

</details>

---

### Q12. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $A=\left[\begin{array}{cc}\frac{1}{\sqrt{2}} & -2 \\ 0 & 1\end{array}\right]$ and $P=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{array}\right], \theta\gt0$. If $\mathrm{B}=\mathrm{PAP}^{\mathrm{T}}, \mathrm{C}=\mathrm{P}^{\mathrm{T}} \mathrm{B}^{10} \mathrm{P}$ and the sum of the diagonal elements of $C$ is $\frac{\mathrm{m}}{\mathrm{n}}$, where $\operatorname{gcd}(\mathrm{m}, \mathrm{n})=1$, then $\mathrm{m}+\mathrm{n}$ is :

**Options:**

- **(A)** $127$
- **(B)** $258$
- **(C)** $65$
- **(D)** $2049$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $65$**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{P}=\left[\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array}\right] \\
& \because \mathrm{P}^{\mathrm{T}} \mathrm{P}=\mathrm{I} \\
& \mathrm{~B}=\mathrm{PAPT}
\end{aligned}$

Pre multiply by $\mathrm{P}^{\mathrm{T}}$ ( Given)
$\mathrm{P}^{\mathrm{T}} \mathrm{~B}=\mathrm{P}^{\mathrm{T}} \mathrm{P} \mathrm{AP}^{\mathrm{T}}=\mathrm{AP}^{\mathrm{T}}$

Now post multiply by P
$\mathrm{P}^{\mathrm{T}} \mathrm{BP}=\mathrm{AP}^{\mathrm{T}} \mathrm{P}=\mathrm{A}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZbUzE9WwTQf-vGun3peGo50mOgS9MiWPEl_yf7YGT5Y.original.fullsize.png">




$\mathrm{A}^2=\mathrm{P}^{\mathrm{T}} \mathrm{~B}^2 \mathrm{P}$

Similarly $A^{10}=P^T B^{10} P=C$
$\begin{aligned}
& A=\left[\begin{array}{cc}
\frac{1}{\sqrt{2}} & -2 \\
0 & 1
\end{array}\right] \text { (Given) } \\
& \Rightarrow A^2=\left[\begin{array}{cc}
\frac{1}{2} & -\sqrt{2}-2 \\
0 & 1
\end{array}\right]
\end{aligned}$

Similarly check $A^3$ and so on since $C=A^{10}$ $\Rightarrow$ Sum of diagonal elements of C is $\left(\frac{1}{\sqrt{2}}\right)^{10}+1$

$\begin{aligned} & =\frac{1}{32}+1=\frac{33}{32}=\frac{\mathrm{m}}{\mathrm{n}} \\ & \operatorname{g~cd}(\mathrm{m}, \mathrm{n})=1(\text { Given }) \\ & \Rightarrow \mathrm{m}+\mathrm{n}=65\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let $A=\left[a_{i j}\right]$ be $3 \times 3$ matrix such that $A\left[\begin{array}{l}0 \\ 1 \\ 0\end{array}\right]=\left[\begin{array}{l}0 \\ 0 \\ 1\end{array}\right], A\left[\begin{array}{l}4 \\ 1 \\ 3\end{array}\right]=\left[\begin{array}{l}0 \\ 1 \\ 0\end{array}\right]$ and $A\left[\begin{array}{l}2 \\ 1 \\ 2\end{array}\right]=\left[\begin{array}{l}1 \\ 0 \\ 0\end{array}\right]$, then $a_{23}$ equals :

**Options:**

- **(A)** -1
- **(B)** 2
- **(C)** 1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) -1**

**Detailed Solution:**

$\begin{aligned}
& \text { Let } A=\left[\begin{array}{lll}
a & b & c \\
d & e & f \\
g & h & i
\end{array}\right] \\
& \therefore\left[\begin{array}{lll}
a & b & c \\
d & e & f \\
g & h & i
\end{array}\right]\left[\begin{array}{l}
0 \\
1 \\
0
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\
1
\end{array}\right] \\
& \therefore \quad b=0, e=0, h=1 \\
& \text { and }\left[\begin{array}{lll}
a & 0 & c \\
d & 0 & f \\
g & 1 & i
\end{array}\right]\left[\begin{array}{l}
4 \\
1 \\
3
\end{array}\right]=\left[\begin{array}{l}
0 \\
1 \\
0
\end{array}\right] \\
& \left.\therefore \begin{array}{l}
4 a+3 c=0 \\
4 d+3 f=1 \\
4 g+1+3 i=0
\end{array}\right\} ....(1)
\end{aligned}$
$\begin{aligned} & \text { and }\left[\begin{array}{ccc}a & 0 & c \\ d & 0 & f \\ g & 1 & i\end{array}\right]\left[\begin{array}{l}2 \\ 1 \\ 2\end{array}\right]=\left[\begin{array}{l}1 \\ 0 \\ 0\end{array}\right] \\ & \left.\begin{array}{c}2 a+2 c=1 \\ \therefore 2 d+2 f=0 \\ 2 g+1+2 i=0\end{array}\right\}...(2)\end{aligned}$
From equation (1) and (2) we get
$\begin{aligned}
& d=1, f=-1 \\
& \therefore \quad a_{23}=-1
\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is real matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>1</mn></math> such that the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mi>T</mi></msup><mi>M</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub></math> holds. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is a real number such that the relation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mi>λ</mi><mi>X</mi></math> holds for some non-zero real matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>1</mn><mo>,</mo></math> then the sum of squares of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup></mrow></mfenced><mfenced><mrow><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup><mo>−</mo><mn>2</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup><mo>+</mo><mn>4</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>−</mo><mn>4</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup><mo>+</mo><mn>4</mn><mi>M</mi><msup><mi>M</mi><mi>T</mi></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mi>M</mi><mi>T</mi></msup><mi>M</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mi>λ</mi><mi>X</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>A</mi><mn>2</mn></msup><mi>X</mi><mo>=</mo><mi>λ</mi><mi>A</mi><mi>X</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>X</mi><mo>=</mo><mi>λ</mi><mfenced><mrow><mi>λ</mi><mi>X</mi></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as</mtext><mo> </mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo> </mo><mo>&amp;</mo><mo> </mo><mi>A</mi><mi>X</mi><mo>=</mo><mi>λ</mi><mi>X</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>X</mi><mo>=</mo><msup><mi>λ</mi><mn>2</mn></msup><mi>X</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>X</mi><mfenced><mrow><msup><mi>λ</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>λ</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>λ</mi><mo>=</mo><mo>±</mo><mn>1</mn></math></p><p>So, sum of square of all possible values <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q15. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msqrt><mn>2</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>−</mo><mn>1</mn></mtd><mtd><msqrt><mn>2</mn></msqrt></mtd></mtr></mtable></mfenced><mo>,</mo><mi>B</mi><mfenced close="]" open="["><mtable equalcolumns="true" equalrows="true"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>C</mi><mo>=</mo><mi>A</mi><mi>B</mi><msup><mi>A</mi><mi>T</mi></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><msup><mi>A</mi><mi>T</mi></msup><msup><mi>C</mi><mn>2</mn></msup><mi>A</mi></math>, then det <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>891</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msqrt><mn>2</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><msqrt><mn>2</mn></msqrt></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>⇒</mo><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mi>A</mi><mi>B</mi><msup><mi>A</mi><mi>T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>C</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mi>B</mi><msup><mi>A</mi><mi>T</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>C</mi></mfenced><mo>=</mo><msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mn>2</mn></msup><mfenced close="|" open="|"><mi>B</mi></mfenced><mo> </mo><mfenced close="}" open="{"><mrow><mtext>as </mtext><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><msup><mi>A</mi><mi>T</mi></msup></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>C</mi></mfenced><mo>=</mo><mn>9</mn></math></p><p> Now, solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mi>A</mi><msup><mi>C</mi><mn>2</mn></msup><msup><mi>A</mi><mi>T</mi></msup></math></p><p>.<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>X</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mfenced close="|" open="|"><msup><mi>C</mi><mn>2</mn></msup></mfenced><mfenced close="|" open="|"><msup><mi>A</mi><mi>T</mi></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>X</mi></mfenced><mo>=</mo><mn>3</mn><mo>×</mo><msup><mn>9</mn><mn>2</mn></msup><mo>×</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>X</mi></mfenced><mo>=</mo><mn>729</mn></math></p>

</details>

---

### Q16. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> be a square matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>=</mo><mi mathvariant="normal">I</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mo> </mo><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>-</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">I</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><mi mathvariant="normal">I</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><mo>=</mo><msup><mi mathvariant="normal">A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Now, solving </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>-</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mo>×</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mfenced><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>-</mo><mn>2</mn><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>-</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mo>×</mo><mn>2</mn><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>-</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><mi mathvariant="normal">A</mi><msup><mfenced><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mfenced><mn>2</mn></msup></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>=</mo><mn>1</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">A</mi><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi mathvariant="normal">A</mi><mo>-</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>=</mo><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></math></p>

</details>

---

### Q17. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>α</mi></mtd><mtd><mi>β</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>β</mi></mtd><mtd><mi>α</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mn>2</mn><mi>A</mi><msup><mo>|</mo><mn>3</mn></msup><mo>=</mo><msup><mn>2</mn><mn>21</mn></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo>∈</mo><mi>Z</mi></math>, Then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>α</mi></mtd><mtd><mi>β</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>β</mi></mtd><mtd><mi>α</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><msup><mn>2</mn><mn>21</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><msup><mn>2</mn><mn>21</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mi>A</mi></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mn>2</mn><mn>3</mn></msup><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>2</mn></msup><mo>-</mo><msup><mi>β</mi><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p>Now, taking value from the option we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>5</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi><mo> </mo><mo>∈</mo><mi>Z</mi></math>, so for other value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math> is not a integer.</p>

</details>

---

### Q18. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo> </mo><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub></mtd><mtd><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub></mtd><mtd><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub></math> are column matrices, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>AB</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>AB</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><msub><mi>AB</mi><mn>3</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mo>|</mo><mi mathvariant="normal">B</mi><mo>|</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math> is the sum of all the diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>3</mn></msup><mo>+</mo><msup><mi>β</mi><mn>3</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub></mtd><mtd><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub></mtd><mtd><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mtd></mtr></mtable></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">B</mi><mn>3</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>AB</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><mn>0</mn><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>1</mn></msub><mo>+</mo><mn>0</mn></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><mn>0</mn><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi mathvariant="normal">y</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><msub><mi mathvariant="normal">z</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>AB</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>AB</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi mathvariant="normal">y</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi mathvariant="normal">z</mi><mn>2</mn></msub><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>AB</mi><mn>3</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">y</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>AB</mi><mn>2</mn></msub><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>3</mn></msub></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">y</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>+</mo><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">x</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mi mathvariant="normal">y</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi mathvariant="normal">z</mi><mn>3</mn></msub><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mo>|</mo><mi mathvariant="normal">B</mi><mo>|</mo><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>β</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>α</mi><mn>3</mn></msup><mo>+</mo><msup><mi>β</mi><mn>3</mn></msup><mo>=</mo><mn>27</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>28</mn></math></p>

</details>

---

### Q19. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mi>A</mi><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>, then the sum of all the elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><msup><mi>B</mi><mi>n</mi></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mi>A</mi><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>M</mi><mi>A</mi><mi>N</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>N</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced><mi>M</mi></mfenced></mover><mo>&#160;</mo><mover><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced><mi>N</mi></mfenced></mover><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>M</mi><mi>N</mi><mo>=</mo><mi>I</mi><mo>=</mo><mi>N</mi><mi>M</mi></math></p><p>Now using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>M</mi><mi>A</mi><mi>N</mi></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mi>M</mi><mi>A</mi><mi>N</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mfenced><mrow><mi>M</mi><mi>A</mi><mi>N</mi></mrow></mfenced><mo>&#160;</mo><mfenced><mrow><mi>M</mi><mi>A</mi><mi>N</mi></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>M</mi><mi>A</mi><mi>N</mi></mrow></mfenced><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mi>M</mi><mi>A</mi><munder><munder><mrow><mi>N</mi><mi>M</mi></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mi>A</mi><munder><munder><mrow><mi>N</mi><mi>M</mi></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><munder><munder><mrow><mi>N</mi><mi>M</mi></mrow><mo>&#9183;</mo></munder><mi>I</mi></munder><mi>A</mi><mi>N</mi><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mi>M</mi><munder><munder><mrow><mi>A</mi><mi>A</mi><mi>A</mi><mi>A</mi><mi>A</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>A</mi></mrow><mo>&#9183;</mo></munder><mrow><mi>n</mi><mo>&#160;</mo><mtext>times</mtext></mrow></munder><mi>N</mi><mo>&#160;</mo><mo>=</mo><mi>M</mi><msup><mi>A</mi><mi>n</mi></msup><mi>N</mi></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi><mo>+</mo><mi>E</mi></math></p><p>Now finding, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>E</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>E</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>, so all higher power will also be zero,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mi>I</mi><mo>+</mo><mi>E</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mi>I</mi><mo>+</mo><mi>n</mi><mi>E</mi><mo>+</mo><munder><munder><mrow><msup><mrow></mrow><mi>n</mi></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mi>E</mi><mn>2</mn></msup></mrow><mo>&#9181;</mo></munder><mn>0</mn></munder><mo>+</mo><munder><munder><mrow><msup><mrow></mrow><mi>n</mi></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mi>E</mi><mn>3</mn></msup></mrow><mo>&#9183;</mo></munder><mn>0</mn></munder><mo>+</mo><munder><munder><mrow><msup><mrow></mrow><mi>n</mi></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mi>E</mi><mn>4</mn></msup></mrow><mo>&#9183;</mo></munder><mn>0</mn></munder><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mi>I</mi><mo>+</mo><mi>n</mi><mi>E</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8658;</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mi>n</mi><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mi>M</mi><msup><mi>A</mi><mi>n</mi></msup><mi>N</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mi>n</mi><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mo>&#160;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mfrac><mi>n</mi><mn>51</mn></mfrac><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mfrac><mrow><mo>-</mo><mi>n</mi></mrow><mn>51</mn></mfrac><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mfrac><mi>n</mi><mn>51</mn></mfrac></mtd><mtd><mfrac><mi>n</mi><mn>51</mn></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mi>n</mi></mrow><mn>51</mn></mfrac></mtd><mtd><mn>1</mn><mo>-</mo><mfrac><mi>n</mi><mn>51</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><msup><mi>B</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>50</mn><mo>+</mo><mfrac><mrow><mn>50</mn><mo>&#183;</mo><mn>51</mn></mrow><mrow><mn>2</mn><mo>&#183;</mo><mn>51</mn></mrow></mfrac></mtd><mtd><mfrac><mstyle displaystyle="true"><mn>50</mn><mo>&#183;</mo><mn>51</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><mo>&#183;</mo><mn>51</mn></mstyle></mfrac></mtd></mtr><mtr><mtd><mfrac><mstyle displaystyle="true"><mo>-</mo><mn>50</mn><mo>&#183;</mo><mn>51</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><mo>&#183;</mo><mn>51</mn></mstyle></mfrac></mtd><mtd><mn>50</mn><mo>-</mo><mfrac><mstyle displaystyle="true"><mn>50</mn><mo>&#183;</mo><mn>51</mn></mstyle><mstyle displaystyle="true"><mn>2</mn><mo>&#183;</mo><mn>51</mn></mstyle></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>75</mn></mtd><mtd><mn>25</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>25</mn></mtd><mtd><mn>25</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>100</mn></math></p>

</details>

---

### Q20. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> matrix with real entries such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mn>1</mn><mo>,</mo></math>  where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi><mo>-</mo><mfenced open="{" close="}"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math>., If det <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math>, the sum of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> matrix with real entries such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mn>1</mn><mo>,</mo></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p>Now putting the value in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mi>I</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#945;</mi><mi>a</mi><mo>+</mo><mn>1</mn></mtd><mtd><mi>&#945;</mi><mi>b</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi><mi>c</mi></mtd><mtd><mi>&#945;</mi><mi>d</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now equating both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>&#945;</mi><mi>a</mi><mo>+</mo><mn>1</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>&#945;</mi><mi>c</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mi>&#945;</mi><mi>b</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math> (not possible as mentioned in question)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>0</mn></math>
Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mi>&#945;</mi><mi>d</mi><mo>+</mo><mn>1</mn><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>|</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>|</mo><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mi>t</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><msup><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>t</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mn>2</mn></math></p><p>So, sum of all possible value will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mi>A</mi></math> and the positive value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> belongs to the interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>]</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>2</mn><mi>c</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi></mtd><mtd><mn>2</mn><mi>a</mi></mtd></mtr><mtr><mtd><mi>c</mi><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mo>+</mo><mn>3</mn><mi>c</mi></mtd></mtr></mtable></mfenced></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi><mo>+</mo><mn>2</mn></mtd><mtd><mn>2</mn><mi>c</mi></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>3</mn><mi>c</mi></mtd><mtd><mn>2</mn><mi>a</mi></mtd></mtr><mtr><mtd><mi>c</mi><mi>a</mi></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn><mo>+</mo><mn>3</mn><mi>c</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>c</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi>c</mi><mi>a</mi><mo>+</mo><mn>3</mn></mtd><mtd><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>c</mi></mtd><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mi>c</mi></mtd></mtr><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>c</mi><mi>a</mi><mo>+</mo><mn>2</mn><mi>a</mi></mtd><mtd><mn>3</mn><mo>+</mo><mn>2</mn><mi>a</mi><mi>c</mi></mtd><mtd><mn>6</mn><mo>+</mo><mn>3</mn><mi>a</mi><mo>+</mo><mn>9</mn><mi>c</mi></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>c</mi></mtd><mtd><mi>c</mi><mi>a</mi><mo>+</mo><mn>2</mn><mi>c</mi><mo>+</mo><mn>3</mn><msup><mi>c</mi><mn>2</mn></msup></mtd><mtd><mn>2</mn><mi>c</mi><mi>a</mi><mo>+</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>Now equating <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mi>A</mi></math> and comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>c</mi><mi>a</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>c</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mi>c</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mn>9</mn><mrow><mn>2</mn><mi>a</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mo>-</mo><mn>9</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>4</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>2</mn></msqrt></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>+</mo><msqrt><mn>76</mn></msqrt></mrow><mn>4</mn></mfrac><mo>&#8776;</mo><mfrac><mrow><mn>6</mn><mo>.</mo><mn>7</mn></mrow><mn>4</mn></mfrac><mo>&#8776;</mo><mn>1</mn><mo>.</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>]</mo></math></p><p>So, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>,</mo><mi>n</mi><mo>]</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>T</mi></msup><msup><mi>Q</mi><mn>2007</mn></msup><mo>&#160;</mo><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math>then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>-</mo><mn>3</mn><mi>c</mi><mo>-</mo><mn>4</mn><mi>d</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2004</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2005</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2007</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2006</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2005</mn></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><msup><mi>P</mi><mi>T</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd><mtd><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mfrac><msqrt><mn>3</mn></msqrt><mn>2</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><msup><mi>P</mi><mi>T</mi></msup><mo>=</mo><mi>I</mi></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>T</mi></msup><msup><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mn>2007</mn></msup><mi>P</mi><mo>=</mo><msup><mi>P</mi><mi>T</mi></msup><munder><munder><mrow><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced></mrow><mo>&#9183;</mo></munder><mrow><mn>2007</mn><mo>&#160;</mo><mi>times</mi></mrow></munder><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mi>T</mi></msup><msup><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mn>2007</mn></msup><mi>P</mi><mo>=</mo><msup><mi>A</mi><mn>2007</mn></msup></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"></mspace><msup><mi>A</mi><mn>2007</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2007</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mi>T</mi></msup><msup><mfenced><mrow><mi>P</mi><mi>A</mi><msup><mi>P</mi><mi>T</mi></msup></mrow></mfenced><mn>2007</mn></msup><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2007</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mi>T</mi></msup><mi>Q</mi><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2007</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>2007</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>3</mn><mi>c</mi><mo>-</mo><mn>4</mn><mi>d</mi><mo>=</mo><mn>2</mn><mo>+</mo><mn>2007</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>2005</mn></math></p></blockquote>

</details>

---

### Q23. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be a square matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><mi>P</mi></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>,</mo><mo>&#160;</mo><mi>&#948;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>&#945;</mi></msup><mo>+</mo><msup><mi>P</mi><mi>&#946;</mi></msup><mo>=</mo><mi>&#947;</mi><mi>l</mi><mo>-</mo><mn>29</mn><mi>P</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>&#945;</mi></msup><mo>-</mo><msup><mi>P</mi><mi>&#946;</mi></msup><mo>=</mo><mi>&#948;</mi><mi>l</mi><mo>-</mo><mn>13</mn><mi>P</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>-</mo><mi>&#948;</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> be a square matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><mi>P</mi></math>,</p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><mi>P</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>4</mn></msup><mo>=</mo><mfenced><mrow><mi>I</mi><mo>-</mo><mi>P</mi></mrow></mfenced><mfenced><mrow><mi>I</mi><mo>-</mo><mi>P</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>4</mn></msup><mo>=</mo><mi>I</mi><mo>+</mo><msup><mi>P</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>4</mn></msup><mo>=</mo><mi>I</mi><mo>+</mo><mi>I</mi><mo>-</mo><mi>P</mi><mo>-</mo><mn>2</mn><mi>P</mi><mo>=</mo><mn>2</mn><mi>I</mi><mo>-</mo><mn>3</mn><mi>P</mi></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>4</mn></msup><mo>&#183;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><msup><mi>P</mi><mn>6</mn></msup><mo>=</mo><mn>2</mn><mi>I</mi><mo>-</mo><mn>5</mn><mi>P</mi><mo>+</mo><mn>3</mn><msup><mi>P</mi><mn>2</mn></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>6</mn></msup><mo>=</mo><mn>2</mn><mi>I</mi><mo>-</mo><mn>5</mn><mi>P</mi><mo>+</mo><mn>3</mn><mfenced><mrow><mi>I</mi><mo>-</mo><mi>P</mi></mrow></mfenced><mo>=</mo><mn>5</mn><mi>I</mi><mo>-</mo><mn>8</mn><mi>P</mi></math>... <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>8</mn></msup><mo>=</mo><mn>13</mn><mi>I</mi><mo>-</mo><mn>21</mn><mi>P</mi></math> ... <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p>Now adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>+</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>8</mn></msup><mo>+</mo><msup><mi>P</mi><mn>6</mn></msup><mo>=</mo><mn>18</mn><mi>I</mi><mo>-</mo><mn>29</mn><mi>P</mi></math></p><p>Now subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced><mo>-</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>8</mn></msup><mo>-</mo><msup><mi>P</mi><mn>6</mn></msup><mo>=</mo><mn>8</mn><mi>I</mi><mo>-</mo><mn>13</mn><mi>P</mi></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>&#945;</mi></msup><mo>-</mo><msup><mi>P</mi><mi>&#946;</mi></msup><mo>=</mo><mi>&#948;</mi><mi>l</mi><mo>-</mo><mn>13</mn><mi>P</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>P</mi><mi>&#945;</mi></msup><mo>+</mo><msup><mi>P</mi><mi>&#946;</mi></msup><mo>=</mo><mi>&#947;</mi><mi>l</mi><mo>-</mo><mn>29</mn><mi>P</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>&#947;</mi><mo>=</mo><mn>18</mn><mo>,</mo><mo>&#160;</mo><mi>&#948;</mi><mo>=</mo><mn>8</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi><mo>-</mo><mi>&#948;</mi><mo>=</mo><mn>8</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>18</mn><mo>-</mo><mn>8</mn><mo>=</mo><mn>24</mn></math></p></blockquote>

</details>

---

### Q24. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn></mrow></msub><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mmultiscripts><mo>&#8800;</mo><mprescripts></mprescripts><mrow><mi>i</mi><mi>j</mi></mrow><none></none></mmultiscripts><mn>0</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi></math>, Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi></math> be the sum of all diagonal elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfenced close="|" open="|"><mi>A</mi></mfenced></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<blockquote><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr><mtr><mtd><mi>r</mi></mtd><mtd><mi>s</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr><mtr><mtd><mi>r</mi></mtd><mtd><mi>s</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>p</mi></mtd><mtd><mi>q</mi></mtd></mtr><mtr><mtd><mi>r</mi></mtd><mtd><mi>s</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>r</mi></mtd><mtd><mi>p</mi><mi>q</mi><mo>+</mo><mi>q</mi><mi>s</mi></mtd></mtr><mtr><mtd><mi>r</mi><mi>p</mi><mo>+</mo><mi>r</mi><mi>s</mi></mtd><mtd><mi>q</mi><mi>r</mi><mo>+</mo><msup><mi>s</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>Now given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>r</mi></mtd><mtd><mi>p</mi><mi>q</mi><mo>+</mo><mi>q</mi><mi>s</mi></mtd></mtr><mtr><mtd><mi>r</mi><mi>p</mi><mo>+</mo><mi>r</mi><mi>s</mi></mtd><mtd><mi>q</mi><mi>r</mi><mo>+</mo><msup><mi>s</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now on comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>+</mo><mi>q</mi><mi>r</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>(</mo><mi>p</mi><mo>+</mo><mi>s</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>r</mi><mo>(</mo><mi>p</mi><mo>+</mo><mi>s</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>q</mi><mi>r</mi><mo>+</mo><msup><mi>s</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Now on solving above relation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>&#8800;</mo><mn>0</mn><mo>&#8658;</mo><mi>p</mi><mo>+</mo><mi>s</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>0</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>|</mo><mi>A</mi><mo>|</mo><mo>=</mo><mi>p</mi><mi>s</mi><mo>-</mo><mi>q</mi><mi>r</mi><mo>=</mo><mo>-</mo><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mi>q</mi><mi>r</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>(</mo><mo>&#8757;</mo><mi>s</mi><mo>=</mo><mo>-</mo><mi>p</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mn>3</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p></blockquote>

</details>

---

### Q25. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> then,

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>30</mn></msup><mo>-</mo><msup><mi mathvariant="normal">A</mi><mn>25</mn></msup><mo>=</mo><mn>2</mn><mi mathvariant="normal">I</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>30</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mn>25</mn></msup><mo>+</mo><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">I</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>30</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mn>25</mn></msup><mo>-</mo><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">I</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>30</mn></msup><mo>=</mo><msup><mi mathvariant="normal">A</mi><mn>25</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>30</mn></msup><mo>+</mo><msup><mi mathvariant="normal">A</mi><mn>25</mn></msup><mo>-</mo><mi mathvariant="normal">A</mi><mo>=</mo><mi mathvariant="normal">I</mi></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></mtd><mtd><mo>-</mo><mn>3</mn><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><msqrt><mn>3</mn></msqrt></mtd></mtr><mtr><mtd><mo>-</mo><msqrt><mn>3</mn></msqrt></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><menclose notation="box"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><mi>I</mi></menclose><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>30</mn></msup><mo>=</mo><mo>(</mo><mo>-</mo><mi>I</mi><msup><mo>)</mo><mn>10</mn></msup><mo>=</mo><mi>I</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Again from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>25</mn></msup><mo>=</mo><msup><mfenced><msup><mi>A</mi><mn>3</mn></msup></mfenced><mn>8</mn></msup><mo>.</mo><mi>A</mi><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mi>I</mi></mrow></mfenced><mn>8</mn></msup><mo>.</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>25</mn></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>25</mn></msup><mo>-</mo><mi>A</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>3</mn><mo>)</mo></math></p><p>On adding equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>30</mn></msup><mo>+</mo><msup><mi>A</mi><mn>25</mn></msup><mo>-</mo><mi>A</mi><mo>=</mo><mi>I</mi></math></p>

</details>

---

### Q26. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math>. Then the sum of the diagonal elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mn>11</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6144</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4094</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4097</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2050</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4097</mn></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mi>A</mi><mo>&#183;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>&#183;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mo>&#160;</mo><msup><mi>A</mi><mn>11</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mo>&#160;</mo><msup><mi>A</mi><mn>10</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>10</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mo>&#160;</mo><mi>A</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>11</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mrow></mfenced><mi>A</mi><mo>+</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mn>2</mn><mn>11</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mi>A</mi><mo>+</mo><mi>I</mi><mo>=</mo><mn>2047</mn><mo>&#160;</mo><mi>A</mi><mo>+</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mn>2047</mn><mi>A</mi><mo>+</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>I</mi></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2047</mn><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn><mo>&#215;</mo><mn>2047</mn><mo>+</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn><mo>&#215;</mo><mn>2047</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>12</mn><mo>&#215;</mo><mn>2047</mn></mtd><mtd><mo>-</mo><mn>3</mn><mo>&#215;</mo><mn>2047</mn><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Sum of diagonal elements</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2047</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4094</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>4097</mn></math></p>

</details>

---

### Q27. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> be real numbers. Consider a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>&#945;</mi><mi>I</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mn>21</mn><mi>A</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi></math>, then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>8</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>&#945;</mi><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>.</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>&#945;</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><mn>3</mn><mi>A</mi><mo>+</mo><mi>&#945;</mi><mi>I</mi></mrow></mfenced><mo>+</mo><mi>&#945;</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mn>9</mn><mi>A</mi><mo>+</mo><mi>&#945;</mi><mi>A</mi><mo>+</mo><mn>3</mn><mi>&#945;</mi><mi>I</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><msup><mi>A</mi><mn>3</mn></msup><mo>.</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced><mrow><mn>9</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>&#945;</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>9</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><mi>A</mi><mo>+</mo><mi>&#945;</mi><mi>I</mi></mrow></mfenced><mo>+</mo><mn>3</mn><mi>&#945;</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">A</mi><mfenced><mrow><mn>27</mn><mo>+</mo><mn>6</mn><mi mathvariant="normal">&#945;</mi></mrow></mfenced><mo>+</mo><mi>&#945;</mi><mfenced><mrow><mn>9</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mn>21</mn><mi>A</mi><mo>+</mo><mi>&#946;</mi><mi>I</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>On comparing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>27</mn><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>=</mo><mn>21</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mi>&#945;</mi><mfenced><mrow><mn>9</mn><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>8</mn></math></p>

</details>

---

### Q28. JEE Main 2023 (25 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>3</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="right"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>=</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><mi>BA</mi></math>, then the inverse of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AM</mi><mn>2023</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2023</mn><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2023</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2023</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2023</mn><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2023</mn><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>3</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>3</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>10</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">B</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">B</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>3</mn><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">B</mi><mn>2023</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2023</mn><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>=</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><mi>BA</mi></math>        (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>=</mo><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mi mathvariant="normal">B</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">M</mi><mo>&#183;</mo><mi mathvariant="normal">M</mi><mo>=</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><msup><mi>BAA</mi><mi mathvariant="normal">T</mi></msup><mi>BA</mi><mo>=</mo><mi>A</mi><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><mo>.</mo><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><mo>.</mo><msup><mi mathvariant="normal">B</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><msup><mi mathvariant="normal">B</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>3</mn></msup><mo>=</mo><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><msup><mi mathvariant="normal">B</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">M</mi><mn>2023</mn></msup><mo>=</mo><msup><mi>AA</mi><mi mathvariant="normal">T</mi></msup><msup><mi mathvariant="normal">B</mi><mn>2023</mn></msup><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>2023</mn></msup></math>                (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup></math> is an identity matrix)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi mathvariant="normal">M</mi><mn>2023</mn></msup><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>2023</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2023</mn><mi>i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>AM</mi><mn>2023</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2023</mn><mi mathvariant="normal">i</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q29. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are two non-zero <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#215;</mo><mi>n</mi></math> matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>,</mo></math> then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>I</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><mi>I</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mi>B</mi><mo>=</mo><mi>I</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><mi>B</mi><msup><mi>A</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><mi>B</mi><msup><mi>A</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>-</mo><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>B</mi><mo>+</mo><mi>I</mi><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>I</mi><msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mo>=</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>B</mi><msup><mfenced><mrow><mi>B</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>B</mi><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>I</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>B</mi><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mi>B</mi><mo>=</mo><mi>B</mi><msup><mi>A</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><mi>B</mi><msup><mi>A</mi><mn>2</mn></msup></math></p>

</details>

---

### Q30. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8469;</mi></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mo>'</mo></msup><msup><mi>A</mi><mi>k</mi></msup><mi>X</mi><mo>=</mo><mn>33</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mi>T</mi></msup><msup><mi>A</mi><mi>K</mi></msup><mi>X</mi><mo>=</mo><mn>33</mn></math></p><p>Now putting the value of matrices in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mi>T</mi></msup><msup><mi>A</mi><mi>K</mi></msup><mi>X</mi><mo>=</mo><mn>33</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><msup><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mi mathvariant="normal">k</mi></msup><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>33</mn></math></p><p>Now finding   <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>12</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Similary <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>8</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>24</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>10</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>24</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>30</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>&#8594;</mo></math> Even <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>K</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn><mi>K</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now again putting the value in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mi>T</mi></msup><msup><mi>A</mi><mi>K</mi></msup><mi>X</mi><mo>=</mo><mn>33</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn><mo>&#160;</mo><mi>K</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn><mo>&#160;</mo><mi>K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mn>3</mn><mo>&#160;</mo><mi>K</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>33</mn></math></p><p>Now assuming <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mn>33</mn></mfenced></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>K</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>33</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>K</mi><mo>=</mo><mn>10</mn></math></p><p>Now, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is odd <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mi>T</mi></msup><msup><mi>A</mi><mi>K</mi></msup><mi>X</mi><mo>=</mo><mn>33</mn></math></p><p>We can rewrite above expression as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mi>T</mi></msup><mi>A</mi><msup><mi>A</mi><mrow><mi>K</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>X</mi><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn><mi>k</mi><mo>-</mo><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>3</mn><mi>k</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mn>33</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><mo>-</mo><mn>3</mn><mi mathvariant="normal">k</mi><mo>+</mo><mn>13</mn></mrow></mfenced><mo>=</mo><mfenced close="]" open="["><mn>33</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">k</mi><mo>=</mo><mn>20</mn><mo>/</mo><mn>3</mn></math> (not possible)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>10</mn></math> is the required answer.</p></blockquote>

</details>

---

### Q31. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> non-zero real matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> is a zero matrix. Then

**Options:**

- **(A)** The system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mn>0</mn></math> has a unique solution
- **(B)** The system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mn>0</mn></math> has infinitely many solutions
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is an invertible matrix
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>adj</mi><mfenced><mi>A</mi></mfenced></math> is an invertible matrix

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>X</mi><mo>=</mo><mn>0</mn></math> has infinitely many solutions**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>A</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/16510b7f-8907-47de-a9c5-a72f93c83932-image.png" style="width: 158px; height: 90px;" /></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>0</mn></math> (not possible)</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>0</mn></math>  (not possible)</p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>A</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>B</mi></math> are non-invertible matrix,</p><p>So, <mo> </mo><mi>A</mi><mi>X</mi><mo>=</mo><mn>0</mn> has infinitely many solutions</p></blockquote>

</details>

---

### Q32. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>1</mn></msub></math> be the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> which satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#945;</mi><mn>2</mn></msub></math> be the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> which satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>B</mi><mn>2</mn></msup></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>&#945;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>2</mn></msub></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>R</mi></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#946;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#946;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>&#946;</mi><mo>+</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>&#945;</mi></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mn>2</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>4</mn></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>Now on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn><mo>=</mo><msub><mi>&#945;</mi><mn>1</mn></msub></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>B</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>&#945;</mi></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>Again on comparing both side we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>=</mo><msub><mi>&#945;</mi><mn>2</mn></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msub><mi>&#945;</mi><mn>1</mn></msub><mo>-</mo><msub><mi>&#945;</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q33. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mn>9</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup></mtd><mtd><msup><mn>11</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><msup><mn>12</mn><mn>2</mn></msup></mtd><mtd><msup><mn>13</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>14</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup></mtd><mtd><msup><mn>16</mn><mn>2</mn></msup></mtd><mtd><msup><mn>17</mn><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mi>B</mi><mi>A</mi></math> is;

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1224</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1042</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>540</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>539</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>539</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mn>9</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup></mtd><mtd><msup><mn>11</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><msup><mn>12</mn><mn>2</mn></msup></mtd><mtd><msup><mn>13</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>14</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup></mtd><mtd><msup><mn>16</mn><mn>2</mn></msup></mtd><mtd><msup><mn>17</mn><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math> </p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left center center"><mtr><mtd><msup><mn>9</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup></mtd><mtd><msup><mn>11</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><msup><mn>12</mn><mn>2</mn></msup></mtd><mtd><msup><mn>13</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>14</mn><mn>2</mn></msup></mtd></mtr><mtr><mtd><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup></mtd><mtd><msup><mn>16</mn><mn>2</mn></msup></mtd><mtd><msup><mn>17</mn><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>12</mn><mn>2</mn></msup><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup></mtd><mtd><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>13</mn><mn>2</mn></msup><mo>+</mo><msup><mn>16</mn><mn>2</mn></msup></mtd><mtd><msup><mn>11</mn><mn>2</mn></msup><mo>-</mo><msup><mn>14</mn><mn>2</mn></msup><mo>+</mo><msup><mn>17</mn><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>325</mn></mtd><mtd><mn>214</mn></mtd></mtr></mtable></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>&#39;</mo></msup><mi>B</mi><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>325</mn></mtd><mtd><mn>214</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mrow><mn>325</mn><mo>+</mo><mn>214</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mn>539</mn></mfenced></math></p></blockquote>

</details>

---

### Q34. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>. If for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>48</mn></mtd><mtd><mn>2160</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>96</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Now on rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi><mo>+</mo><mi>B</mi></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>a</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>a</mi><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn></math></p><p>Now by using binomial expansion we get,<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>B</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mi>I</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mi>B</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>B</mi><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>B</mi><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>n</mi><mi>a</mi></mtd><mtd><mi>n</mi><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>n</mi><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mtext>as</mtext><mo>&#160;</mo><msup><mi>B</mi><mn>3</mn></msup><mo>&#160;</mo><mtext>and&#160;higher&#160;power&#160;will&#160;become&#160;zero</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi><mi>a</mi></mtd><mtd><mi>n</mi><mi>a</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>a</mi><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>n</mi><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>48</mn></mtd><mtd><mn>2160</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>96</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>On comparing we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>a</mi><mo>=</mo><mn>48</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mi>b</mi><mo>=</mo><mn>96</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>a</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mi>a</mi><mi>b</mi><mo>=</mo><mn>2160</mn></math></p><p>On solving above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>4</mn><mo>,</mo><mi>n</mi><mo>=</mo><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>8</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>4</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>24</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>A</mi><mo>-</mo><mi>I</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mfrac><mrow><msqrt><mn>3</mn></msqrt><mi mathvariant="normal">i</mi><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math>, then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>100</mn></mrow></mfenced><mo>:</mo><msup><mi>A</mi><mi>n</mi></msup><mo>+</mo><msup><mfenced><mrow><mi>&#969;</mi><mi>B</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mi>A</mi></math> </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8704;</mo><mi>n</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left left right"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left left right"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left left right"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mfenced open="[" close="]"><mtable columnalign="left left right"><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><mi>B</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mn>3</mn></msup><mo>=</mo><mo>-</mo><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mi>B</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>B</mi><mn>5</mn></msup><mo>=</mo><mi>B</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">B</mi><mn>99</mn></msup><mo>=</mo><mi mathvariant="normal">B</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#969;</mi><mrow><mn>3</mn><mi mathvariant="bold-italic">k</mi></mrow></msup><mo>=</mo><mn>1</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo></math> common of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>99</mn></mrow></mfenced></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>99</mn></mrow></mfenced><mo>=</mo><mn>17</mn></math></p></blockquote>

</details>

---

### Q36. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is a non-zero real number and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mn>49</mn></munderover><msup><mi>M</mi><mrow><mn>2</mn><mi>k</mi></mrow></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>I</mi><mo>-</mo><msup><mi>M</mi><mn>2</mn></msup></mrow></mfenced><mi>N</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>I</mi></math>, then the positive integral value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>M</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mi>I</mi></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mn>49</mn></munderover><msup><mi>M</mi><mrow><mn>2</mn><mi>k</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mo>=</mo><msup><mi>M</mi><mn>2</mn></msup><mo>+</mo><msup><mi>M</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mi>M</mi><mn>98</mn></msup><mo>=</mo><mfenced close="]" open="["><mrow><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>-</mo><msup><mi>&#945;</mi><mn>6</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mrow><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mn>49</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfrac><mo>.</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>&#945;</mi><mn>98</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mfenced><mrow><mi>I</mi><mo>-</mo><msup><mi>M</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mfenced><mrow><msup><mi>&#945;</mi><mn>98</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>I</mi><mo>-</mo><msup><mi>M</mi><mn>2</mn></msup></mrow></mfenced><mi>N</mi><mo>=</mo><mo>-</mo><mn>2</mn><mi>I</mi></math></p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>.</p>

</details>

---

### Q37. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math> be a square matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><msup><mn>2</mn><mrow><mi>j</mi><mo>-</mo><mi>i</mi></mrow></msup></math>, for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mo>&#160;</mo><mi>j</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math>. Then, the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>A</mi><mn>10</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mfenced><mi>A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mfenced><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mfenced><mi>A</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msub><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mrow><mn>3</mn><mo>&#215;</mo><mn>3</mn></mrow></msub></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub><mo>=</mo><msup><mn>2</mn><mrow><mi>j</mi><mo>-</mo><mi>i</mi></mrow></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>12</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mn>3</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>4</mn></mfrac></mtd><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>3</mn><mi>A</mi></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>A</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><msup><mi>A</mi><mn>4</mn></msup><mo>+</mo><mo>&#8943;</mo><msup><mi>A</mi><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mi>A</mi><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mi>A</mi><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mi>A</mi><mo>+</mo><mo>&#8943;</mo><msup><mn>3</mn><mn>9</mn></msup><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mi>A</mi><mfenced close="]" open="["><mfrac><mrow><msup><mn>3</mn><mn>9</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><mi>A</mi><mfenced close="]" open="["><mfrac><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mfenced></math></p>

</details>

---

### Q38. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>. Then, the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mi>n</mi><mo>&#8712;</mo><mo>{</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>100</mn><mo>}</mo><mo>:</mo><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mi>A</mi></mrow></mfenced></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><mo>&#183;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi><mo>+</mo><mn>1</mn></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>&#183;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn><mo>-</mo><mi>i</mi></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><msup><mi>A</mi><mn>3</mn></msup><mo>&#183;</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>i</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mi>I</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><msup><mi>A</mi><mn>4</mn></msup><mo>&#183;</mo><mi>A</mi><mo>=</mo><mi>I</mi><mo>&#183;</mo><mi>A</mi><mo>=</mo><mi>A</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>6</mn></msup><mo>=</mo><msup><mi>A</mi><mn>4</mn></msup><mo>&#183;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>&#183;</mo><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup></math> and so on</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msup><mi>A</mi><mn>1</mn></msup><mo>=</mo><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><msup><mi>A</mi><mn>9</mn></msup><mo>=</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>=</mo><msup><mi>A</mi><mn>97</mn></msup><mo>=</mo><mi>A</mi></math></p><p>Hence, possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>9</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>97</mn></mrow></mfenced></math></p><p>Clearly, above sequence is in A.P. where</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>t</mi><mi>n</mi></msub><mo>=</mo><mn>97</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mn>97</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>1</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn><mo>=</mo><mn>97</mn></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>n</mi><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> The number of elements in the given set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>25</mn></math>.</p>

</details>

---

### Q39. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>Y</mi><mo>=</mo><mi>&#945;</mi><mi>l</mi><mo>+</mo><mi>&#946;</mi><mi>X</mi><mo>+</mo><mi>&#947;</mi><msup><mi>X</mi><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mi>I</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mi>X</mi><mo>+</mo><mfenced><mrow><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#947;</mi></mrow></mfenced><msup><mi>X</mi><mn>2</mn></msup><mo>,</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>,</mo><mi>&#947;</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8477;</mi></math>.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">Y</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd></mtr></mtable></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to ______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>, so <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>X</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>Now, finding <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>&#945;</mi><mi>l</mi><mo>+</mo><mi>&#946;</mi><mi>X</mi><mo>+</mo><mi>&#947;</mi><msup><mi>X</mi><mn>2</mn></msup></math> &amp;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mi>I</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mi>X</mi><mo>+</mo><mfenced><mrow><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#947;</mi></mrow></mfenced><msup><mi>X</mi><mn>2</mn></msup></math>  by putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>X</mi><mn>2</mn></msup></math> we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>Z</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mtd><mtd><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#947;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>&#183;</mo><msup><mi>Y</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi mathvariant="normal">I</mi></math>  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd><mtd><mi>&#947;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mn>1</mn><mn>5</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mfrac><mi>&#945;</mi><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#945;</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mn>5</mn></mfrac></mtd><mtd><mfrac><mi>&#945;</mi><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#946;</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mi>&#947;</mi><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mfrac><mi>&#945;</mi><mn>5</mn></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn><mi>&#945;</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mi>&#946;</mi><mn>5</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mfrac><mi>&#945;</mi><mn>5</mn></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mspace linebreak="newline"></mspace></math></p><p>On comparing L.H.S and R.H.S we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>5</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mi>&#945;</mi><mo>+</mo><mfrac><mi>&#946;</mi><mn>5</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#946;</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#945;</mi><mn>5</mn></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn><mi>&#946;</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mi>&#947;</mi><mn>5</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>&#947;</mi><mo>=</mo><mn>15</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>+</mo><mi>&#947;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>5</mn><mo>-</mo><mn>10</mn><mo>+</mo><mn>15</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn></math></p>

</details>

---

### Q40. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math> . Then the number of elements in the set {<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>,</mo><mi>m</mi></mrow></mfenced><mo>:</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mn>10</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><msup><mi>A</mi><mi>n</mi></msup><mo>+</mo><mi>m</mi><msup><mi>B</mi><mi>m</mi></msup><mo>=</mo><mi>I</mi></math>} is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>A</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>B</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi></math></p><p>Therefore the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><msup><mi>A</mi><mi>n</mi></msup><mo>+</mo><mi>m</mi><msup><mi>B</mi><mi>m</mi></msup><mo>=</mo><mi>I</mi></math> is true for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>1</mn></math> so, only one set is possible.</p>

</details>

---

### Q41. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mfenced><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mo>;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#8712;</mo><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mn>100</mn></mrow></mfenced></mrow></mfenced></math> and let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mi>A</mi><mo>&#8712;</mo><mi>S</mi><mo>:</mo><msup><mi>A</mi><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>=</mo><mi>I</mi></mrow></mfenced></math>. Then the number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo largeop="true">&#8745;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msub><mi>T</mi><mi>n</mi></msub></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>b</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfenced open="{" close="}"><mrow><mi>A</mi><mo>&#8712;</mo><mi>S</mi><mo>;</mo><msup><mi>A</mi><mrow><mi>n</mi><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup><mo>=</mo><mi>I</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi></math> must be equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> In this case <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup></math>  will become identity matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> can take any value from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total number of common element will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>.</p>

</details>

---

### Q42. JEE Main 2021 (31 Aug Shift 2)

*Type:* `numerical` | *Level:* `3`

The number of elements in the set {<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>:</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>&#8712;</mo><mo>{</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>}</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>I</mi><mo>-</mo><mi>A</mi><msup><mo>)</mo><mn>3</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><msup><mi>A</mi><mn>3</mn></msup></math>}, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> identity matrix, is <u>                 </u> .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>:</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>I</mi><mo>-</mo><mi>A</mi></mrow></mfenced><mn>3</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><msup><mi>A</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>-</mo><msup><mi>A</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>I</mi><mo>-</mo><msup><mi>A</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>A</mi><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><mo>.</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>d</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>d</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>d</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>d</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p>Comparing on both sides
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mfenced><mrow><mi>d</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>(</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>)</mo><mo>=</mo><mi>b</mi></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>:</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>)</mo><mo>&#8801;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo><mo>&#8594;</mo><mn>4</mn></math> ways</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi><mo>&#160;</mo><mo>:</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>&#160;</mo><mo>(</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>&#8594;</mo><mn>4</mn></math> ways</p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math> ways</p>

</details>

---

### Q43. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>K</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mfenced><mrow><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi>I</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi>I</mi><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mfenced><mrow><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><mi mathvariant="normal">I</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>2</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>2</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">K</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mn>4</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>2</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>2</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>2</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>2</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>-</mo><mn>4</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>4</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">K</mi><mo>&#160;</mo><mo>&#160;</mo></mtd><mtd><mn>2</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn><mi mathvariant="normal">K</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><mi>AI</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>8</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>3</mn><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>8</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>-</mo><mi mathvariant="normal">K</mi></mtd><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>+</mo><mn>3</mn><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi mathvariant="normal">K</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">I</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi mathvariant="normal">K</mi></mtd><mtd><mn>6</mn><mo>-</mo><mn>8</mn><mi mathvariant="normal">K</mi><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi mathvariant="normal">K</mi><mo>-</mo><mi mathvariant="normal">K</mi><mo>-</mo><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup></mtd><mtd><mn>4</mn><msup><mi mathvariant="normal">K</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi mathvariant="normal">K</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><mo>-</mo><mn>8</mn><mi mathvariant="normal">K</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q44. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2025</mn></msup><mo>-</mo><msup><mi>A</mi><mn>2020</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>6</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>-</mo><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>A</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>n</mi><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2025</mn></msup><mo>-</mo><msup><mi>A</mi><mn>2020</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2024</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2019</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><msup><mi>A</mi><mn>6</mn></msup><mo>-</mo><mi>A</mi></math></p>

</details>

---

### Q45. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left left"><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mo>,</mo><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><msup><mi>A</mi><mi>T</mi></msup><mi>B</mi><mi>A</mi></math>, then the inverse of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>Q</mi><mn>2021</mn></msup><msup><mi>A</mi><mi mathvariant="normal">T</mi></msup></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnspacing="1em" rowspacing="4pt" columnalign="center center"><mtr><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mn>2021</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2021</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnspacing="1em" rowspacing="4pt" columnalign="center center"><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mo>&#8722;</mo><mn>2021</mn></mtd></mtr><mtr><mtd><mn>2021</mn></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnspacing="1em" rowspacing="4pt" columnalign="center center"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mspace/></mtd></mtr><mtr><mtd><mn>2021</mn></mtd><mtd><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2021</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>AA</mi><mo>&#8868;</mo></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr><mtr><mtd><mfrac><mn>2</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd><mtd><mfrac><mn>1</mn><msqrt><mn>5</mn></msqrt></mfrac></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi mathvariant="normal">I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><msup><mi>A</mi><mo>&#8868;</mo></msup><mi>B</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>Q</mi><mn>2</mn></msup><mo>=</mo><mfenced><mrow><msup><mi>A</mi><mo>&#8868;</mo></msup><mi>B</mi><mi>A</mi></mrow></mfenced><mfenced><mrow><msup><mi>A</mi><mo>&#8868;</mo></msup><mi>B</mi><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mo>&#8868;</mo></msup><mi>B</mi><mfenced><mrow><mi>A</mi><msup><mi>A</mi><mo>&#8868;</mo></msup></mrow></mfenced><mi>B</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mo>&#8868;</mo></msup><mi>B</mi><mfenced><mi>I</mi></mfenced><mi>B</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mo>&#8868;</mo></msup><msup><mi>B</mi><mn>2</mn></msup><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>Q</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mo>&#8868;</mo></msup><msup><mi>B</mi><mn>3</mn></msup><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">Q</mi><mn>2021</mn></msup><mo>=</mo><msup><mi mathvariant="normal">A</mi><mi mathvariant="normal">T</mi></msup><msup><mi mathvariant="normal">B</mi><mn>2021</mn></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>=</mo><msup><mi>AQ</mi><mn>2021</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mi mathvariant="normal">T</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>=</mo><mi mathvariant="normal">A</mi><mfenced><mrow><msup><mi mathvariant="normal">A</mi><mo>&#8868;</mo></msup><msup><mi mathvariant="normal">B</mi><mn>2021</mn></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow></mfenced><msup><mi mathvariant="normal">A</mi><mo>&#8868;</mo></msup></math></p><p>given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mo>&#8868;</mo></msup><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>=</mo><msup><mi mathvariant="normal">B</mi><mn>2021</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">B</mi><mn>2021</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2021</mn><mi mathvariant="normal">i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>inverse of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced><msup><mi>P</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>=</mo><msup><mfenced><msup><mi>B</mi><mn>2021</mn></msup></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2021</mn><mi>i</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q46. JEE Main 2021 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mi>A</mi><mo>+</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>A</mi><mn>20</mn></msup><mo>,</mo></math> then the sum of all the elements of the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2020**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mi>A</mi><mo>+</mo><msup><mi>A</mi><mn>2</mn></msup><mo>+</mo><msup><mi>A</mi><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>A</mi><mn>20</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi>A</mi><mo>.</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mn>2</mn></msup><mo>.</mo><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>n</mi></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>n</mi></mtd><mtd><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mi>n</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So, required sum</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>2</mn><munderover><mrow><mo>&#8721;</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mfrac><mrow><mi>r</mi><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>2</mn><munderover><mrow><mo>&#8721;</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>21</mn><mo>&#215;</mo><mn>41</mn></mrow><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>r</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo>+</mo><mn>5</mn><mfenced><mrow><mn>5</mn><mo>&#215;</mo><mn>21</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>5</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>41</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><mo>+</mo><mn>525</mn><mo>+</mo><mn>1435</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2020</mn></math></p>

</details>

---

### Q47. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>50</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>25</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>50</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>25</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>50</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>25</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>4</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>3</mn><mn>2</mn></mfrac></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>P</mi><mn>50</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>49</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>25</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q48. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo><mo>&#160;</mo><msup><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mi>n</mi></msup><mfenced><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>&#8704;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt><mo>.</mo></math> Then the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo></math> digit numbers in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><msup><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mi>X</mi><mo>=</mo><mi>I</mi><mi>X</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mi>i</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mi>n</mi></msup><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>8</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi></math> is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo></math></p><p>So number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> digit numbers in the set </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>16</mn><mo>,</mo><mn>24</mn><mo>,</mo><mn>32</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>96</mn></mrow></mfenced></math></p><p>Clearly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>,</mo><mn>24</mn><mo>,</mo><mn>32</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>96</mn></math> are in arithmetic progression.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>24</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mn>96</mn></math></p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is the first term, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is the common difference, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is the last term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of terms.</p><p>Consider, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mn>96</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>8</mn><mo>=</mo><mn>96</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>8</mn><mo>=</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>11</mn></math></p><p>Hence, number of two-digit numbers in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>.</p>

</details>

---

### Q49. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math> Then the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with entries from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>}</mo></math> and satisfying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>B</mi><mi>A</mi></math> is ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3125**

**Detailed Solution:**

<p>Let, the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>A</mi><mi>B</mi><mo>=</mo><mi>B</mi><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>d</mi></mtd><mtd><mi>e</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>h</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>b</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>e</mi></mtd><mtd><mi>d</mi></mtd><mtd><mi>f</mi></mtd></mtr><mtr><mtd><mi>h</mi></mtd><mtd><mi>g</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p>On equating the matrices, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>e</mi><mo>=</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>f</mi><mo>=</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>=</mo><mi>h</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>g</mi></mtd><mtd><mi>g</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p>No. of ways of selecting each of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>g</mi><mo>,</mo><mo>&#160;</mo><mi>i</mi></math> from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo></math></p><p>Thus, the total number of ways are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>5</mn><mn>5</mn></msup><mo>=</mo><mn>3125</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> No. of Matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>3125</mn><mo>.</mo></math></p>

</details>

---

### Q50. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>7</mn><msup><mi>A</mi><mn>20</mn></msup><mo>-</mo><mn>20</mn><msup><mi>A</mi><mn>7</mn></msup><mo>+</mo><mn>2</mn><mi>I</mi></math>,
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is an identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><msub><mi>b</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>13</mn></msub></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **910**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mo>=</mo><mi>I</mi><mo>+</mo><mi>C</mi></math></p><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>C</mi><mn>2</mn></msup><mo>=</mo><mtable><mtr><mtd><mfenced close="]" open="["><mtable><mtr><mtd><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced></mtd></mtr></mtable></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>C</mi><mn>3</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mtd></mtr></mtable></mfenced><mo>=</mo><msup><mi>C</mi><mn>4</mn></msup><mo>=</mo><msup><mi>C</mi><mn>5</mn></msup><mo>=</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>7</mn><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>20</mn></msup><mo>-</mo><mn>20</mn><msup><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>7</mn></msup><mo>+</mo><mn>2</mn><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>(</mo><mi>I</mi><mo>+</mo><mi>C</mi><msup><mo>)</mo><mn>20</mn></msup><mo>-</mo><mn>20</mn><mo>(</mo><mi>I</mi><mo>+</mo><mi>C</mi><msup><mo>)</mo><mn>7</mn></msup><mo>+</mo><mn>2</mn><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mfenced><mrow><mi>I</mi><mo>+</mo><mn>20</mn><mi>C</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>20</mn></mmultiscripts><msup><mi>C</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mn>20</mn><mfenced><mrow><mi>I</mi><mo>+</mo><mn>7</mn><mi>C</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>7</mn></mmultiscripts><msup><mi>C</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mn>2</mn><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8211;</mo><mn>11</mn><mi>I</mi><mo>+</mo><mn>910</mn><mo>&#160;</mo><msup><mi>C</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>11</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>910</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>11</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>11</mn></mtd></mtr></mtable></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>13</mn></msub><mo>=</mo><mn>910</mn></math></p>

</details>

---

### Q51. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> be an identity matrix of order <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mi>n</mi></msup><mo>=</mo><mn>5</mn><mi>I</mi><mo>-</mo><mn>8</mn><mi>P</mi></math> is equal to ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>I</mi><mo>-</mo><mn>8</mn><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>5</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mfenced><mo>-</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>16</mn></mtd><mtd><mo>-</mo><mn>8</mn></mtd></mtr><mtr><mtd><mn>40</mn></mtd><mtd><mo>-</mo><mn>24</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mo>-</mo><mn>11</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>40</mn></mtd><mtd><mn>29</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>P</mi><mn>3</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd><mtd><mo>-</mo><mn>3</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>5</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>6</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mo>-</mo><mn>7</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>11</mn></mtd><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>40</mn></mtd><mtd><mn>29</mn></mtd></mtr></mtable></mfenced><mo>=</mo><msup><mi>P</mi><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q52. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>&#8800;</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>d</mi><mo>=2021,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi></math> is equal to ______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2020**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mo>=</mo><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo><mi>B</mi><mo>=</mo><mi>O</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mrow><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo></mrow></mfenced><mo>&#215;</mo><mfenced open="|" close="|"><mi>B</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>|</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>|</mo><mo>=</mo><mn>0</mn><mo>,</mo></math> since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8800;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|"><mtable><mtr><mtd><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mo>(</mo><mi>d</mi><mo>-</mo><mn>1</mn><mo>)</mo></mtd></mtr></mtable></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>d</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>a</mi><mo>-</mo><mi>d</mi><mo>+</mo><mn>1</mn><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mn>2021</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>2020</mn><mo>.</mo></math></p>

</details>

---

### Q53. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mi>sin</mi><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>&#945;</mi></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>det</mi><mfenced><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">I</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>,</mo></math> then a possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mi>I</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mfrac><mi mathvariant="normal">I</mi><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><msup><mi>sin</mi><mn>2</mn></msup><mi>&#945;</mi><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>sin</mi><mi>&#945;</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math> </p>

</details>

---

### Q54. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>b</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced></math> be two <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>1</mn></math>matrices with real entries such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>X</mi><mi>B</mi><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>k</mi></mtd></mtr></mtable></mfenced><mo>,</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>R</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup><mo>&#8800;</mo><mo>-</mo><mn>2</mn><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>X</mi><mi>B</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>k</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>b</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msqrt><mn>3</mn></msqrt><msub><mi>a</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msqrt><mn>3</mn></msqrt><msub><mi>a</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><msub><mi>b</mi><mn>1</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mtd></mtr><mtr><mtd><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>1</mn></msub><mo>+</mo><mi>k</mi><msub><mi>b</mi><mn>2</mn></msub></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><msub><mi>a</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mi>k</mi><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><msqrt><mn>3</mn></msqrt><msub><mi>a</mi><mn>2</mn></msub><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced><mrow><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><mi>k</mi><msub><mi>b</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow></mfenced><mn>3</mn></mfrac><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mi>b</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msubsup><mi>b</mi><mn>2</mn><mn>2</mn></msubsup></math></p><p>On comparing we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>(</mo><mi>k</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>4</mn></mfenced></math></p><p>From both we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q55. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>. Then, the system of linear equations <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>8</mn></msup><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>64</mn></mtd></mtr></mtable></mfenced></math> has :

**Options:**

- **(A)** A unique solution
- **(B)** Infinitely many solutions
- **(C)** No solution
- **(D)** Exactly two solutions

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) No solution**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>i</mi></mtd><mtd><mo>-</mo><mi>i</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>i</mi></mtd><mtd><mi>i</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>8</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>8</mn></msup><mo>=</mo><mn>64</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mn>128</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>8</mn></msup><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi mathvariant="normal">x</mi></mtd></mtr><mtr><mtd><mi mathvariant="normal">y</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>64</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>128</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>64</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>128</mn><mfenced open="[" close="]"><mtable><mtr><mtd><mi>x</mi><mo>-</mo><mi>y</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>8</mn></mtd></mtr><mtr><mtd><mn>64</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> From <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math> : No solution.</p>

</details>

---

### Q56. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

If the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>20</mn></msup><mo>+</mo><mi>&#945;</mi><msup><mi>A</mi><mn>19</mn></msup><mo>+</mo><mi>&#946;</mi><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> for some real numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>8</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>16</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Hence, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>20</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mn>2</mn><mn>20</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><msup><mi>A</mi><mn>19</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mn>2</mn><mn>19</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>20</mn></msup><mo>+</mo><mi>&#945;</mi><msup><mi>A</mi><mn>19</mn></msup><mo>+</mo><mi>&#946;</mi><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mn>2</mn><mn>20</mn></msup><mo>+</mo><mi>&#945;</mi><mo>.</mo><msup><mn>2</mn><mn>19</mn></msup><mo>+</mo><mn>2</mn><mi>&#946;</mi></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn><mo>-</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Therefore <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>20</mn></msup><mo>+</mo><msup><mn>2</mn><mn>19</mn></msup><mi>&#945;</mi><mo>-</mo><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mn>2</mn><mn>18</mn></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mfenced><mrow><msup><mn>2</mn><mn>18</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#946;</mi><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q57. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If for the matrix, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>&#160;&#160;</mo><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>&#945;</mi></mtd><mtd><mi>&#946;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><mi>&#945;</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mtd></mtr><mtr><mtd><mi>&#945;</mi><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>4</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q58. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd></mtr><mtr><mtd><mi>y</mi></mtd><mtd><mi>z</mi></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>z</mi></mtd><mtd><mi>x</mi></mtd><mtd><mi>y</mi></mtd></mtr></mtable></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> are real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mi>z</mi><mo>=</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><msup><mi>z</mi><mn>3</mn></msup></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mi mathvariant="normal">I</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><msup><mi>A</mi><mo>&#39;</mo></msup><mo>=</mo><mi>I</mi></math> (as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mo>'</mo></msup><mo>=</mo><mi>A</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi></math> is orthogonal</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>+</mo><mi>y</mi><mi>z</mi><mo>+</mo><mi>z</mi><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>1</mn></math></p><p>Thus, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><msup><mi>z</mi><mn>3</mn></msup><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>&#215;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>7</mn></math></p>

</details>

---

### Q59. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos&#952;</mi></mtd><mtd><mi>sin&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin&#952;</mi></mtd><mtd><mi>cos&#952;</mi></mtd></mtr></mtable></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>=</mo><mi mathvariant="normal">A</mi><mo>+</mo><msup><mi mathvariant="normal">A</mi><mn>4</mn></msup></math>, then det <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">B</mi></mfenced></math> :

**Options:**

- **(A)** is one
- **(B)** lies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced></math>
- **(C)** is zero
- **(D)** lies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) lies in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mn>4</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mn>4</mn><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mn>4</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mn>4</mn><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mo>+</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mi>sin</mi><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mi>sin</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mo>-</mo><mfenced><mrow><mi>sin</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></mtd><mtd><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>B</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>cos</mi><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>sin</mi><mn>4</mn><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mfenced><mrow><mi>cos</mi><mn>4</mn><mi>&#952;</mi><mo>&#183;</mo><mi>cos</mi><mi>&#952;</mi><mo>+</mo><mi>sin</mi><mn>4</mn><mi>&#952;</mi><mo>&#183;</mo><mi>sin</mi><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mfenced><mrow><mn>4</mn><mi>&#952;</mi><mo>-</mo><mi>&#952;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mn>3</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>B</mi></mfenced><mo>=</mo><mn>2</mn><mo>+</mo><mn>2</mn><mi>cos</mi><mfrac><mrow><mn>3</mn><mi mathvariant="normal">&#960;</mi></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>-</mo><mfenced><mfrac><mrow><msqrt><mn>5</mn></msqrt><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>&#8712;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p>

</details>

---

### Q60. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mi>&#952;</mi></mtd><mtd><mtext>&#160;isin</mtext><mi>&#952;</mi></mtd></mtr><mtr><mtd><mtext>isin</mtext><mi>&#952;</mi></mtd><mtd><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>24</mn></mfrac></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msqrt><mo>-</mo><mn>1</mn></msqrt></math>, then which one of the following is not true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#8722;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>i</mi><mi>sin</mi><mi>&#952;</mi><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><msup><mi>cos</mi><mn>2</mn></msup><mi>&#952;</mi><mo>&#8722;</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mtext>&#8201;</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mn>2</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mn>2</mn><mi>&#952;</mi><mtext>&#8201;&#160;&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mn>2</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mn>3</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mn>3</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mn>3</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>5</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>cos</mi><mn>5</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;</mtext><mi>i</mi><mi>sin</mi><mn>5</mn><mi>&#952;</mi></mtd></mtr><mtr><mtd><mi>i</mi><mi>sin</mi><mn>5</mn><mi>&#952;</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;&#8201;&#8201;</mtext><mi>cos</mi><mn>5</mn><mi>&#952;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi><mo>&#160;</mo><mtext>&#8201;&#8201;&#8201;</mtext><mi>d</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>cos</mi><mn>5</mn><mi>&#952;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>i</mi><mi>sin</mi><mn>5</mn><mi>&#952;</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>=</mo><mi>i</mi><mi>sin</mi><mn>5</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mi>cos</mi><mn>5</mn><mi>&#952;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>5</mn><mi>&#952;</mi><mo>&#8722;</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>5</mn><mi>&#952;</mi><mo>=</mo><mi>cos</mi><mn>10</mn><mi>&#952;</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>cos</mi><mn>2</mn></msup><mn>5</mn><mi>&#952;</mi><mo>+</mo><msup><mi>sin</mi><mn>2</mn></msup><mn>5</mn><mi>&#952;</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>4</mn><mo>)</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#8722;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q61. JEE Main 2020 (03 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mi>&#949;</mi><mo>&#160;</mo><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced close="]" open="["><msub><mi>a</mi><mrow><mi>i</mi><mi>j</mi></mrow></msub></mfenced><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>=</mo><mn>109</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>22</mn></msub></math> is equal to_____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>&#215;</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#215;</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><mi>x</mi></mtd></mtr><mtr><mtd><mi>x</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable equalrows="true" equalcolumns="true"><mtr><mtd><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi></mtd><mtd><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>11</mn></msub><mo>=</mo><mn>109</mn><mo>&#8658;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>109</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>a</mi><mn>22</mn></msub><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q62. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#8712;</mo><mi>R</mi></math> be all non-zero and satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>+</mo><msup><mi>c</mi><mn>3</mn></msup><mo>=</mo><mn>2</mn></math>. If the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mtable columnalign="left"><mtr></mtr><mtr></mtr><mtr></mtr></mtable></math> satisfies <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mi>A</mi><mo>=</mo><mi>I</mi><mo>,</mo></math> then a value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>c</mi></math> can be</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><msup><mi>A</mi><mi>T</mi></msup><mi>A</mi><mo>=</mo><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="[" close="]"><mtable columnalign="left"><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd></mtr><mtr><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd></mtr><mtr><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>a</mi><mi>c</mi></mtd><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>On comparing each element both sides, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>+</mo><msup><mi>c</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>-</mo><mi>a</mi><mi>c</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math> (from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Now, we also know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mrow><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>a</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mfenced><mn>0</mn></mfenced></math> (from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p>Putting it in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mo>&#177;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mn>2</mn><mo>&#8723;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>a</mi><mi>b</mi><mi>c</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q63. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>X</mi><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mi>z</mi></mrow></mfenced><mi>T</mi></msup><mo>:</mo><mi>P</mi><mi>X</mi><mo>=</mo><mn>0</mn><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mo>-</mo><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>9</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math> then the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>

**Options:**

- **(A)** Is a singleton.
- **(B)** Is an empty set.
- **(C)** Contains more than two elements
- **(D)** Contains exactly two elements

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Contains exactly two elements**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>P</mi></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> System of equations </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>2</mn><mo>&#160;</mo><mi>y</mi><mo>+</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>y</mi><mo>+</mo><mn>4</mn><mi>z</mi><mo>=</mo><mn>0</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>9</mn><mi>y</mi><mo>-</mo><mi>z</mi><mo>=</mo><mn>0</mn></math> has infinitely many solutions.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi><mo>=</mo><mi>k</mi><mo>&#8712;</mo><mi>R</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>11</mn><mi mathvariant="normal">k</mi></mrow><mn>7</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">k</mi></mrow><mn>7</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">z</mi><mo>=</mo><mi mathvariant="normal">k</mi></math> </p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>z</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">k</mi><mo>=</mo><mo>&#177;</mo><mfrac><mn>7</mn><msqrt><mn>174</mn></msqrt></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Two solutions are only possible.</p><p>Hence, set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> contains exactly two elements.</p>

</details>

---

### Q64. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>&#945;</mi></math> be a root of the equation <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> and the matrix <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#945;</mi></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>&#945;</mi><mn>2</mn></msup></mtd><mtd><msup><mi>&#945;</mi><mn>4</mn></msup></mtd></mtr></mtable></mfenced><mo>,</mo></math> then the matrix <math><msup><mrow><mi>A</mi></mrow><mrow><mn>31</mn></mrow></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup></math>
- **(B)** <math><msub><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></msub></math>
- **(C)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup></math>**

**Detailed Solution:**

<p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mi>&#969;</mi><mo>,</mo><msup><mi>&#969;</mi><mn>2</mn></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi></math> is complex cube root of unity.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#969;</mi></mtd><mtd><msup><mi>&#969;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>&#969;</mi><mn>2</mn></msup></mtd><mtd><mi>&#969;</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mi>&#969;</mi></mtd><mtd><msup><mi>&#969;</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><msup><mi>&#969;</mi><mn>2</mn></msup></mtd><mtd><mi>&#969;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>31</mn></msup><mo>=</mo><msup><mi>A</mi><mn>28</mn></msup><mo>&#215;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mi>I</mi><mo>&#215;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><msup><mi>A</mi><mn>3</mn></msup></math></p>

</details>

---

### Q65. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The total number of matrices <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mo>-</mo><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mi>y</mi></mrow></mfenced></math> for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mi>T</mi></msup><mi>A</mi><mo>=</mo><mn>3</mn><msub><mi>I</mi><mn>3</mn></msub></math> is:

**Options:**

- **(A)** <math><mn>6</mn></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>4</mn></math>**

**Detailed Solution:**

<p>Given <math><msup><mrow><mi>A</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>A</mi><mo>=</mo><mn>3</mn><msub><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mn>2</mn><mi>x</mi></mtd></mtr><mtr><mtd><mn>2</mn><mi>y</mi></mtd><mtd><mi>y</mi></mtd><mtd><mo>-</mo><mi>y</mi></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mi>y</mi></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>2</mn><mi>x</mi></mtd><mtd><mo>-</mo><mi>y</mi></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced separators="|"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mtable><mtr><mtd><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>6</mn><msup><mi>y</mi><mn>2</mn></msup></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math></p><p>On comparing the two matrices, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn></math> and <math><mn>6</mn><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math> and <math><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mo>&#177;</mo><msqrt><mfrac><mn>3</mn><mn>8</mn></mfrac></msqrt></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>&#177;</mo><msqrt><mfrac><mn>1</mn><mn>2</mn></mfrac></msqrt></math></p><p>For each of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi></math> we have two possible values, hence there are total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>4</mn></math> combinations of values are possible.</p><p>Hence, total <math><mn>4</mn></math> matrices are possible.</p>

</details>

---

### Q66. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mi>cos</mi><mi>&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>&#945;</mi></mtd><mtd><mi>cos</mi><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>a</mi><mo>&#8712;</mo><mi>R</mi></mrow></mfenced><mi>&#160;</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>32</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>.</mo></math> Then, a value of <math><mi>&#945;</mi></math> is:

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>32</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mi>π</mi></mrow><mrow><mn>64</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mi>&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mi>&#945;</mi></mtd><mtd><mi>cos</mi><mi>&#945;</mi></mtd></mtr></mtable></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>&#8658;</mo><mi>A</mi></mrow><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mn>2</mn><mi>&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mtd><mtd><mi>cos</mi><mn>2</mn><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mi mathvariant="normal">&#160;</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mn>3</mn><mi>&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mn>3</mn><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mn>3</mn><mi>&#945;</mi></mtd><mtd><mi>cos</mi><mn>3</mn><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>32</mn></msup><mi mathvariant="normal">&#160;</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mn>32</mn><mi>&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mn>32</mn><mi>&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mn>32</mn><mi>&#945;</mi></mtd><mtd><mi>cos</mi><mn>32</mn><mi>&#945;</mi></mtd></mtr></mtable></mfenced></math>
Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">A</mi><mn>32</mn></msup><mi mathvariant="normal">&#160;</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#160;</mi><mfenced open="[" close="]"><mtable><mtr><mtd><mi>cos</mi><mn>32</mn><mi mathvariant="normal">&#945;</mi></mtd><mtd><mo>-</mo><mi>sin</mi><mn>32</mn><mi mathvariant="normal">&#945;</mi></mtd></mtr><mtr><mtd><mi>sin</mi><mn>32</mn><mi mathvariant="normal">&#945;</mi></mtd><mtd><mi>cos</mi><mn>32</mn><mi mathvariant="normal">&#945;</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p><p>On comparing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>cos</mi><mn>32</mn><mi>&#945;</mi><mo>=</mo><mn>0</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>32</mn><mi>&#945;</mi><mo>=</mo><mn>1</mn></math>, we get,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>64</mn></mfrac></math></p>

</details>

---

### Q67. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math><mi>Q</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><msub><mrow><mi>q</mi></mrow><mrow><mi>i</mi><mi>j</mi></mrow></msub></mrow></mfenced></math> be two <math><mn>3</mn><mo>&#215;</mo><mn>3</mn><mi>&#160;</mi></math> matrices such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>-</mo><msup><mi>P</mi><mn>5</mn></msup><mo>=</mo><msub><mi>I</mi><mn>3</mn></msub></math>. Then <math><mfrac><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>21</mn></mrow></msub><mo>+</mo><msub><mrow><mi>q</mi></mrow><mrow><mn>31</mn></mrow></msub></mrow><mrow><msub><mrow><mi>q</mi></mrow><mrow><mn>32</mn></mrow></msub></mrow></mfrac></math> is equal to :

**Options:**

- **(A)** <math><mn>10</mn></math>
- **(B)** <math><mn>9</mn></math>
- **(C)** <math><mn>15</mn></math>
- **(D)** <math><mn>135</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>10</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>27</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>4</mn></msup><mo>=</mo><msup><mi>P</mi><mn>2</mn></msup><mo>&#215;</mo><msup><mi>P</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>27</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>27</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>90</mn></mtd><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>P</mi><mn>5</mn></msup><mo>=</mo><msup><mi>P</mi><mn>4</mn></msup><mo>&#215;</mo><mi>P</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>90</mn></mtd><mtd><mn>12</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>9</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>15</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>135</mn></mtd><mtd><mn>15</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p>Let,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><msub><mi>q</mi><mn>11</mn></msub></mtd><mtd><msub><mi>q</mi><mn>12</mn></msub></mtd><mtd><msub><mi>q</mi><mn>13</mn></msub></mtd></mtr><mtr><mtd><msub><mi>q</mi><mn>21</mn></msub></mtd><mtd><msub><mi>q</mi><mn>22</mn></msub></mtd><mtd><msub><mi>q</mi><mn>23</mn></msub></mtd></mtr><mtr><mtd><msub><mi>q</mi><mn>31</mn></msub></mtd><mtd><msub><mi>q</mi><mn>31</mn></msub></mtd><mtd><msub><mi>q</mi><mn>33</mn></msub></mtd></mtr></mtable></mfenced></math></p><p>Now, given <math><mi>Q</mi><mo>-</mo><msup><mrow><mi>P</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>=</mo><msub><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>q</mi><mn>21</mn></msub><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn><mo>,</mo><mtext>&#8201;</mtext><msub><mi>q</mi><mn>31</mn></msub><mo>-</mo><mn>135</mn><mo>=</mo><mn>0</mn><mo>,</mo><mtext>&#8201;&#8201;</mtext><msub><mi>q</mi><mn>32</mn></msub><mo>-</mo><mn>15</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>q</mi><mn>21</mn></msub><mo>=</mo><mn>15</mn><mo>,</mo><mtext>&#8201;</mtext><msub><mi>q</mi><mn>31</mn></msub><mo>=</mo><mn>135</mn><mo>,</mo><mtext>&#8201;</mtext><msub><mi>q</mi><mn>32</mn></msub><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mrow><msub><mi>q</mi><mn>21</mn></msub><mo>+</mo><msub><mi>q</mi><mn>31</mn></msub></mrow><msub><mi>q</mi><mn>32</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn><mo>+</mo><mn>135</mn></mrow><mn>15</mn></mfrac><mo>=</mo><mn>10</mn></math>.</p>

</details>

---

### Q68. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left(\begin{array}{ccc}0 & 2 q & r \\ p & q & -r \\ p & -q & r\end{array}\right)$. If $\mathrm{AA}^{\mathrm{T}}=\mathrm{I}_{3},$ then $|\mathrm{p}|$ is:

**Options:**

- **(A)** $\frac{1}{\sqrt{5}}$
- **(B)** $\frac{1}{\sqrt{3}}$
- **(C)** $\frac{1}{\sqrt{2}}$
- **(D)** $\frac{1}{\sqrt{6}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\sqrt{2}}$**

**Detailed Solution:**

$A=\left[\begin{array}{ccc}0 & 2 q & r \\ p & q & -r \\ p & -q & r\end{array}\right]$

$\begin{aligned} \therefore & A \cdot A^{T}=\left[\begin{array}{ccc}0 & 2 q & r \\ p & q & -r \\ p & -q & r\end{array}\right] \times\left[\begin{array}{ccc}0 & p & p \\ 2 q & q & -q \\ r & -r & r\end{array}\right] \\ &=\left[\begin{array}{ccc}4 q^{2}+r^{2} & 2 q^{2}-r^{2} & -2 q^{2}+r^{2} \\ 2 q^{2}-r^{2} & p^{2}+q^{2}+r^{2} & p^{2}-q^{2}-r^{2} \\ -2 q^{2}+r^{2} & p^{2}-q^{2}-r^{2} & p^{2}+q^{2}+r^{2}\end{array}\right] \end{aligned}$

Given, $A A^{T}=I$

$\therefore \quad 4 q^{2}+r^{2}=p^{2}+q^{2}+r^{2}=1$

$\Rightarrow \quad p^{2}-3 q^{2}=0$ and $r^{2}=1-4 q^{2}$

and $2 q^{2}-r^{2}=0 \Rightarrow r^{2}=2 q^{2}$

$\begin{array}{ll}\therefore \quad & p^{2}=\frac{1}{2}, q^{2}=\frac{1}{6} \text { and } r^{2}=\frac{1}{3} \\ \therefore \quad & |p|=\frac{1}{\sqrt{2}}\end{array}$

</details>

---

### Q69. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msup><mi>A</mi><mn>20</mn></msup></math>. Then the sum of the elements of the first column of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>211</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>251</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>231</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>231</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<math><mo>&#8658;</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>6</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>4</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>10</mn></mtd><mtd><mn>4</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>;</mo><mo>&#160;</mo><mo>,</mo><mo>&#8230;</mo><mo>;</mo><mo>&#160;</mo><msup><mi>A</mi><mn>20</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>20</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>210</mn></mtd><mtd><mn>20</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msub><mi>a</mi><mn>31</mn></msub><mo>=</mo><mn>20</mn><mi>th</mi><mo>&#160;</mo><mi>term</mi><mo>&#160;</mo><mi>in</mi><mo>&#160;</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>10</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p>Hence, sum of the elements of first column<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>231</mn></math>.</p>

</details>

---

### Q70. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

Suppose $A$ is any $3 \times 3$ non-singular matrix and $(A-3 I)(A-5 I)=O$, where $I=I_3$ and $O=O_3$. If $\alpha A+$ $\beta A^{-1}=4 I$, then $\alpha+\beta$ is equal to

**Options:**

- **(A)** 8
- **(B)** 12
- **(C)** 13
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 8**

**Detailed Solution:**

We have
$$
\begin{aligned}
&(A-3 I)(A-5 I)=O \\
&\Rightarrow A^2-8 A+15 I=O
\end{aligned}
$$
Multiplying both sides by $A^{-1}$, we get;
$$
\begin{aligned}
A^{-1} A \cdot A-8 A^{-1} A+15 A^{-1} I=A^{-1} O \\
\Rightarrow & A-8 I+15 A^{-1}=O \\
& A+15 A^{-1}=8 I \\
& \frac{A}{2}+\frac{15 A^{-1}}{2}=4 I \\
\therefore & \alpha+\beta=\frac{1}{2}+\frac{15}{2}=\frac{16}{2}=8
\end{aligned}
$$

</details>

---

### Q71. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>A</mi></math> be a matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#183;</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced></math> is a scalar matrix and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|" separators="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mn>108</mn></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup></math> equals :

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>32</mn></mtd><mtd><mn>36</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>36</mn></mtd><mtd><mo>-</mo><mn>32</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>36</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>32</mn></mtd><mtd><mo></mo><mn>4</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mo>-</mo><mn>32</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>36</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mn>36</mn></mtd><mtd><mo>-</mo><mn>32</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p>Let <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></mtd></mtr><mtr><mtd><mi>c</mi></mtd><mtd><mn>2</mn><mi>c</mi><mo>+</mo><mn>3</mn><mi>d</mi></mtd></mtr></mtable></mfenced></math> is a scalar.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>c</mi><mi>&#160;</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>a</mi><mo>=</mo><mn>2</mn><mi>c</mi><mo>+</mo><mn>3</mn><mi>d</mi><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mi>d</mi></math></p><p>Given, <math><mfenced close="|" open="|" separators="|"><mrow><mn>3</mn><mi>A</mi></mrow></mfenced><mo>=</mo><mn>108</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced open="|" close="|" separators="|"><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>108</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>=</mo><mn>12</mn><mo>&#8658;</mo><mi>a</mi><mi>d</mi><mo>-</mo><mi>b</mi><mi>c</mi><mo>=</mo><mi>a</mi><mi>d</mi><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>3</mn><mi>d</mi></mrow></mfenced><mi>d</mi><mo>=</mo><mn>12</mn><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><mi>a</mi><mo>=</mo><mn>3</mn><mi>d</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>3</mn><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>36</mn></math> and</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mi>a</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>6</mn></mrow><mn>3</mn></mfrac><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mi>d</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><msup><mi>a</mi><mn>2</mn></msup></mtd><mtd><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>d</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><msup><mi>d</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>36</mn></mtd><mtd><mo>-</mo><mn>32</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>4</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q72. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $A$ be a matrix such that $A$. $\left[\begin{array}{ll}1 & 2 \\ 0 & 3\end{array}\right]$ is a scalar matrix and $|3 A|=108$. Then $A^2$ equals

**Options:**

- **(A)** $\left[\begin{array}{cc}4 & -32 \\ 0 & 36\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}4 & 0 \\ -32 & 36\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}36 & 0 \\ -32 & 4\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}36 & -32 \\ 0 & 4\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}36 & -32 \\ 0 & 4\end{array}\right]$**

**Detailed Solution:**

A. $\left[\begin{array}{ll}1 & 2 \\ 0 & 3\end{array}\right]$ is a scalar matrix and $|3 \mathrm{~A}|=108$ suppose the scalar matrix is $\left[\begin{array}{ll}k & 0 \\ 0 & k\end{array}\right]$
$$
\begin{aligned}
&\therefore A \cdot\left[\begin{array}{ll}
1 & 2 \\
0 & 3
\end{array}\right]=\left[\begin{array}{ll}
k & 0 \\
0 & k
\end{array}\right] \\
&\Rightarrow A=\left[\begin{array}{ll}
k & 0 \\
0 & k
\end{array}\right]\left[\begin{array}{ll}
1 & 2 \\
0 & 3
\end{array}\right]^{-1} \\
&{\left[\therefore A B=C \Rightarrow A B B^{-1}=C B^{-1} \Rightarrow A=C B^{-1}\right]} \\
&\Rightarrow A=\frac{1}{3}\left[\begin{array}{ll}
k & 0 \\
0 & k
\end{array}\right]\left[\begin{array}{cc}
3 & -2 \\
0 & 1
\end{array}\right] \\
&\Rightarrow A=\left[\begin{array}{ll}
k & 0 \\
0 & k
\end{array}\right]\left[\begin{array}{cc}
1 & -\frac{2}{3} \\
0 & \frac{1}{3}
\end{array}\right]
\end{aligned}
$$
$\Rightarrow A=\left[\begin{array}{cc}k & -\frac{2}{3} k \\ 0 & \frac{k}{3}\end{array}\right]$
$\because|3 \mathrm{~A}|=108$
$\Rightarrow 108=\left|\begin{array}{cc}3 k & -2 k \\ 0 & k\end{array}\right|$
$\Rightarrow 3 k^2=108 \Rightarrow k^2=36 \Rightarrow k=\pm 6$
For $k=6$
$A=\left[\begin{array}{cc}6 & -4 \\ 0 & 2\end{array}\right]$
$\Rightarrow A^2=\left[\begin{array}{cc}36 & -32 \\ 0 & 4\end{array}\right]$
For $k=-6$
$\Rightarrow A=\left[\begin{array}{cc}-6 & 4 \\ 0 & -2\end{array}\right]$
$\Rightarrow A^2=\left[\begin{array}{cc}36 & -32 \\ 0 & 4\end{array}\right]$

</details>

---

### Q73. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> , then the determinant of the matrix <math><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2016</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup><mo>-</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2014</mn></mrow></msup></mrow></mfenced></math> is :

**Options:**

- **(A)** <math><mo>-</mo><mn>175</mn></math>
- **(B)** <math><mn>2014</mn></math>
- **(C)** <math><mn>2016</mn></math>
- **(D)** <math><mo>-</mo><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>25</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>4</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>13</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>9</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced></math></p><p>and <math><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=-</mo><mn>1</mn></math>

Now, <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2016</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup><mo>-</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2014</mn></mrow></msup><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2014</mn></mrow></msup><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|" separators="|"><mrow><msup><mi>A</mi><mn>2016</mn></msup><mo>-</mo><mn>2</mn><msup><mi>A</mi><mn>2015</mn></msup><mo>-</mo><msup><mi>A</mi><mn>2014</mn></msup></mrow></mfenced><mo>=</mo><mfenced close="|" open="|" separators="|"><msup><mi>A</mi><mn>2014</mn></msup></mfenced><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><msup><mi>A</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>A</mi><mo>-</mo><mi>I</mi></mrow></mfenced><mi>&#160;</mi></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>A</mi><mo>-</mo><mi>I</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>20</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>15</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mo>=</mo><msup><mrow><mfenced close="|" open="|" separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mn>2014</mn></mrow></msup><mi>&#160;</mi><mfenced close="|" open="|" separators="|"><mrow><mtable><mtr><mtd><mn>20</mn></mtd><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>15</mn></mtd><mtd><mo>-</mo><mn>5</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mo>=</mo><mo>-</mo><mn>25</mn></math></p>

</details>

---

### Q74. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>, be a <math><mn>3</mn><mi>&#160;</mi><mo>&#215;</mo><mn>3</mn></math> matrix, such that <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>A</mi><mo>+</mo><mn>7</mn><mi>I</mi><mo>=</mo><mi>O</mi><mo>.</mo></math>
Statement - I : <math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mn>5</mn><mi>I</mi><mo>-</mo><mi>A</mi></mrow></mfenced><mo>.</mo></math>
Statement - II : The polynomial <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>I</mi></math>,can be reduced to <math><mn>5</mn><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>4</mn><mi>I</mi></mrow></mfenced><mo>.</mo></math> Then :

**Options:**

- **(A)** Both the statements are true
- **(B)** Both the statements are false
- **(C)** Statement - I is true, but Statement - II is false
- **(D)** Statement - I is false, but Statement - II is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both the statements are true**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><mi>A</mi><mo>-</mo><mn>7</mn><mi>I</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math> 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>A</mi><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>5</mn><mi>A</mi><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>7</mn><mi>I</mi><msup><mi>A</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mi>O</mi></math>

<math><mi>A</mi><mi>I</mi><mo>=</mo><mn>5</mn><mi>I</mi><mo>-</mo><mn>7</mn><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>(</mo><mn>5</mn><mi>I</mi><mo>-</mo><mi>A</mi><mo>)</mo></math>

Hence, the statement I is true.

Now <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>I</mi></math>

<math><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><mn>5</mn><mi>A</mi><mo>-</mo><mn>7</mn><mi>I</mi></mrow></mfenced><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>I</mi></math>       {from<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>} 

<math><mo>=</mo><mn>5</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>7</mn><mi>A</mi><mo>-</mo><mn>2</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>I</mi></math>

<math><mo>=</mo><mn>3</mn><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>10</mn><mi>A</mi><mo>+</mo><mi>I</mi></math></p><p><math><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>5</mn><mi>A</mi><mo>-</mo><mn>7</mn><mi>I</mi></mrow></mfenced><mo>-</mo><mn>10</mn><mi>A</mi><mo>+</mo><mi>I</mi></math>       {from<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>}</p><p><math><mo>=</mo><mn>5</mn><mi>A</mi><mo>-</mo><mn>20</mn><mi>I</mi></math></p><p><math><mo>=</mo><mn>5</mn><mfenced separators="|"><mrow><mi>A</mi><mo>-</mo><mn>4</mn><mi>I</mi></mrow></mfenced></math></p><p>Hence, Statement II is true.</p>

</details>

---

### Q75. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>P</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced><mo>,</mo><mi>&#160;</mi><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> and <math><mi>Q</mi><mo>=</mo><mi>P</mi><mi>A</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>,</mo></math> then <math><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>&#160;</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2015</mn></mrow></msup><mi>&#160;</mi><mi>P</mi></math> is :

**Options:**

- **(A)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2015</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2015</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>2015</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2015</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>2015</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>2015</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2015</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi>P</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mtd><mtd><mfrac><mrow><msqrt><mn>3</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mtd></mtr></mtable></mrow></mfenced></math>

<math><mi>P</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mo>=</mo><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>P</mi><mo>=</mo><mi>I</mi></math>

<math><msup><mrow><mi>Q</mi></mrow><mrow><mn>2015</mn></mrow></msup><mo>=</mo><mfenced separators="|"><mrow><mi>P</mi><mi>A</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>P</mi><mi>A</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup></mrow></mfenced></math> ......(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2015</mn></math> terms)

<math><mo>=</mo><mi>P</mi><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup></math>      ...<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>

<math><mo>&#8756;&#160;&#160;</mo><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>&#160;</mi><msup><mrow><mi>Q</mi></mrow><mrow><mn>2015</mn></mrow></msup><mi>&#160;</mi><mi>P</mi><mo>=</mo><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>P</mi><mi>&#160;</mi><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup><msup><mrow><mi>P</mi></mrow><mrow><mi>T</mi></mrow></msup><mi>P</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup></math>   from..<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>

Given <math><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mo>&#8658;</mo></math> <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>3</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mo>&#8756;</mo></math> <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2015</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2015</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

</details>

---

### Q76. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mi>&#160;</mi><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> , then which one of the following statements is not correct?

**Options:**

- **(A)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>I</mi><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi> </mi><mi>I</mi></mrow></mfenced></math>
- **(B)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mi>I</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>I</mi></math>
- **(C)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>I</mi><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced></math>
- **(D)** <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>I</mi><mo>=</mo><mi>A</mi><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>I</mi><mo>=</mo><mi>A</mi><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced></math>**

**Detailed Solution:**

<math><mi mathvariant="normal">A</mi><mi mathvariant="normal">&#160;</mi><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>  <math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mi>I</mi><mo>=</mo><mi>&#160;</mi><mi>A</mi><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>I</mi></mrow></mfenced></math>

<math><mi>&#160;</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mi>&#160;</mi><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> = <math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable><mi>&#160;</mi><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math> .....Correct

Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> <math><msup><mrow><mi>A</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mi>I</mi><mo>=</mo><msup><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>I</mi></math>

<math><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math> ....Correct

Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mo>&#215;</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math> .....Incorrect

Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math>

<math><msup><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mi>I</mi><mo>=</mo><mi>A</mi><mo>(</mo><mi>A</mi><mo>-</mo><mi>I</mi><mo>)</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mo>&#215;</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mfenced open="[" close="]" separators="|"><mtable><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mo>-</mo><mn>1</mn></mtd><mtd><mo>-</mo><mn>1</mn></mtd></mtr></mtable></mfenced></math>

 ......Correct.

</details>

---

### Q77. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced open="[" close="]"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced></math> is a matrix satisfying the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><msup><mi>A</mi><mi>T</mi></msup><mo>=</mo><mn>9</mn><mi>I</mi></math> , where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#160;</mo></math>is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math> identity matrix, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></mrow></mfenced></math> is equal to </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

Given, <math> <mrow> <mi>A</mi><msup> <mi>A</mi> <mi>T</mi> </msup> <mo>=</mo><mn>9</mn><mi>I</mi></mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mo>&#8722;</mo><mn>2</mn></mtd></mtr><mtr><mtd><mi>a</mi></mtd><mtd><mn>2</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mfenced close="]" open="["><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd><mtd><mi>a</mi></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd><mtd><mo>-</mo><mn>2</mn></mtd><mtd><mi>b</mi></mtd></mtr></mtable></mfenced><mo>=</mo><mn>9</mn><mi>I</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>9</mn></mtd><mtd><mn>0</mn></mtd><mtd><mi>a</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>b</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>9</mn></mtd><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mo>&#8722;</mo><mn>2</mn><mi>b</mi></mtd></mtr><mtr><mtd><mi>a</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>b</mi></mtd><mtd><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mo>&#8722;</mo><mn>2</mn><mi>b</mi></mtd><mtd><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mtd></mtr></mtable></mfenced><mo>=</mo><mfenced close="]" open="["><mtable><mtr><mtd><mn>9</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>9</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>9</mn></mtd></mtr></mtable></mfenced></math>

Equation <math> <mrow> <mi>a</mi><mo>+</mo><mn>4</mn><mo>+</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></mrow> </math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>=</mo><mo>&#8722;</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>

<math> <mrow> <mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mo>&#8722;</mo><mn>2</mn><mi>b</mi><mo>=</mo><mn>0</mn></mrow> </math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>&#8722;</mo><mn>2</mn><mi>b</mi><mo>=</mo><mo>&#8722;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>    

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#38;</mo><mtext>&#8201;</mtext><mtext>&#8201;</mtext><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math>     

On solving, we get <math> <mrow> <mi>a</mi><mo>=</mo><mo>&#8722;</mo><mn>2</mn><mo>,</mo><mtext>&#8201;</mtext><mi>b</mi><mo>=</mo><mo>&#8722;</mo><mn>1</mn></mrow> </math>

</details>

---

### Q78. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ccc}1 & 2 & x \\ 3 & -1 & 2\end{array}\right]$ and $B=\left[\begin{array}{c}y \\ x \\ 1\end{array}\right]$ be such that $\mathrm{AB}=\left[\begin{array}{l}6 \\ 8\end{array}\right]$, then:

**Options:**

- **(A)** $y=2 x$
- **(B)** $y=-2 x$
- **(C)** $y=x$
- **(D)** $y=-x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $y=2 x$**

**Detailed Solution:**

Let $\mathrm{A}=\left[\begin{array}{ccc}1 & 2 & x \\ 3 & -1 & 2\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{l}y \\ x \\ 1\end{array}\right]$

$$
\begin{aligned}
&\mathrm{AB}=\left[\begin{array}{ccc}
1 & 2 & x \\
3 & -1 & 2
\end{array}\right]\left[\begin{array}{l}
y \\
x \\
1
\end{array}\right] \\
&\Rightarrow\left[\begin{array}{l}
6 \\
8
\end{array}\right]=\left[\begin{array}{l}
y+2 x+x \\
3 y-x+2
\end{array}\right] \\
&\Rightarrow\left[\begin{array}{l}
6 \\
8
\end{array}\right]=\left[\begin{array}{l}
y+3 x \\
3 y-x+2
\end{array}\right] \\
&\Rightarrow y+3 x=6 \text { and } 3 y-x=6
\end{aligned}
$$
On solving, we get
$$
\begin{aligned}
&x=\frac{6}{5} \text { and } y=\frac{12}{5} \\
&\Rightarrow y=2 x
\end{aligned}
$$

</details>

---

### Q79. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>3</mn></math>  matrix such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>e</mi><mi>t</mi><mo>.</mo><mo>&#160;</mo><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mi>I</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>50</mn></msup><mo>-</mo><mn>50</mn><mi>B</mi></mrow></mfenced></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>&#8658;</mo><msup><mi>B</mi><mn>4</mn></msup><mo>=</mo><msup><mi>B</mi><mn>6</mn></msup><mo>=</mo><msup><mi>B</mi><mn>8</mn></msup><mo>=</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>=</mo><msup><mi>B</mi><mn>50</mn></msup><mo>=</mo><mn>0</mn></math>  and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>B</mi><mn>3</mn></msup><mo>=</mo><msup><mi>B</mi><mn>2</mn></msup><mi>B</mi><mo>=</mo><mn>0</mn><mi>B</mi><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;&#160;</mo><msup><mfenced><mrow><mi>I</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>50</mn></msup><mo>=</mo><mi>I</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>50</mn></mmultiscripts><mi>B</mi></math> (higher powers are zero)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>e</mi><mi>t</mi><mo>.</mo><mfenced open="[" close="]"><mrow><msup><mfenced><mrow><mi>I</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mn>50</mn></msup><mo>-</mo><mn>50</mn><mi>B</mi></mrow></mfenced><mo>&#160;</mo></math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>d</mi><mi>e</mi><mi>t</mi><mo>.</mo><mo>&#160;</mo><mfenced close="]" open="["><mrow><mi>I</mi><mo>+</mo><msup><mspace></mspace><mrow><mn>5</mn><mn>0</mn></mrow></msup><msub><mi>C</mi><mn>1</mn></msub><mi>B</mi><mo>-</mo><mn>5</mn><mn>0</mn><mi>B</mi></mrow></mfenced></math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>d</mi><mi>e</mi><mi>t</mi><mo>.</mo><mfenced close="]" open="["><mi>I</mi></mfenced></math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math>

</details>

---

### Q80. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The matrix $A^2+4 A-5 I$, where $I$ is identity matrix and $A=\left[\begin{array}{cc}1 & 2 \\ 4 & -3\end{array}\right]$, equals :

**Options:**

- **(A)** $4\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]$
- **(B)** $4\left[\begin{array}{cc}0 & -1 \\ 2 & 2\end{array}\right]$
- **(C)** $32\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]$
- **(D)** $32\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}^2+4 \mathrm{~A}-5 \mathrm{I}=\mathrm{A} \times \mathrm{A}+4 \mathrm{~A}-5 \mathrm{I} \\ = & {\left[\begin{array}{cc}1 & 2 \\ 4 & -3\end{array}\right] \times\left[\begin{array}{cc}1 & 2 \\ 4 & -3\end{array}\right]+4\left[\begin{array}{cc}1 & 2 \\ 4 & -3\end{array}\right]-5\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right] } \\ & =\left[\begin{array}{cc}9 & -4 \\ -8 & 17\end{array}\right]+\left[\begin{array}{cc}4 & 8 \\ 16 & -12\end{array}\right]-\left[\begin{array}{cc}5 & 0 \\ 0 & 5\end{array}\right] \\ & =\left[\begin{array}{cc}9+4-5 & -4+8-0 \\ -8+16-0 & 17-12-5\end{array}\right]=\left[\begin{array}{ll}8 & 4 \\ 8 & 0\end{array}\right] \\ & =4\left[\begin{array}{ll}2 & 1 \\ 2 & 0\end{array}\right]\end{aligned}$

</details>

---

### Q81. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `2`

Let $P$ and $Q$ be $3 \times 3$ matrices with $P \neq Q$. If $P^3=Q^3$ and $P^2 Q=Q^2 P$, then determinant of $\left(P^2+Q^2\right)$ is equal to

**Options:**

- **(A)** $-2$
- **(B)** $1$
- **(C)** $0$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0$**

**Detailed Solution:**

$P^3=Q^3$
$P^3-P^2 Q=Q^3-Q^2 P$
$P^2(P-Q)=Q^2(Q-P)$
$P^2(P-Q)+Q^2(P-Q)=O$
$\left(P^2+Q^2\right)(P-Q)=O \quad \Rightarrow\left|P^2+Q^2\right|=0$

</details>

---

### Q82. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

Let $A=\left[\begin{array}{ccc}5 & 5 \alpha & \alpha \\ 0 & \alpha & 5 \alpha \\ 0 & 0 & 5\end{array}\right]$. If $\left|A^2\right|=25$, then $|\alpha|$ equals

**Options:**

- **(A)** $5^2$
- **(B)** $1$
- **(C)** $1 / 5$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 / 5$**

**Detailed Solution:**

$\mathrm{A}^2=\left[\begin{array}{ccc}5 & 5 \alpha & \alpha \\ 0 & \alpha & 5 \alpha \\ 0 & 0 & 5\end{array}\right]\left[\begin{array}{ccc}5 & 5 \alpha & \alpha \\ 0 & \alpha & 5 \alpha \\ 0 & 0 & 5\end{array}\right]$
$\mathrm{A}^2=\left[\begin{array}{ccc}25 & 25 \alpha+5 \alpha^2 & 5 \alpha+25 \alpha^2+5 \alpha \\ 0 & \alpha^2 & 5 \alpha^2+25 \alpha \\ 0 & 0 & 25\end{array}\right]$
$625 \alpha^2=25$
$\Rightarrow|\alpha|=\frac{1}{5}$.

</details>

---

### Q83. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

If $A=\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]$ and $A_2=\left[\begin{array}{ll}\alpha & \beta \\ \beta & \alpha\end{array}\right]$, then

**Options:**

- **(A)** $\alpha=2 a b, \beta=a^2+b^2$
- **(B)** $\alpha=\mathrm{a}_2+\mathrm{b}_2, \beta=\mathrm{ab}$
- **(C)** $\alpha=a^2+b^2, \beta=2 a b$
- **(D)** $\alpha=a^2+b^2, \beta=a^2-b^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\alpha=a^2+b^2, \beta=2 a b$**

**Detailed Solution:**

$A^2=\left[\begin{array}{ll}\alpha & \beta \\ \beta & \alpha\end{array}\right]=\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]\left[\begin{array}{ll}a & b \\ b & a\end{array}\right]$
$\alpha=a^2+b^2 ; \beta=2 a b$

</details>

---

