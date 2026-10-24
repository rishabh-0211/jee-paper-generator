# MHT CET Mathematics - Matrices

## Topic 1: Formation and Basic of Matrix

**Total Questions:** 2

---

### Q1. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A = [a_{ij}]_{3 \times 3}$ is a matrix such that $a_{ij} = |2i - 5j|$, where $|.|$ denotes the modulus function, then the element in the $2^{\text{nd}}$ row and $3^{\text{rd}}$ column of $A^{-1}$ is ...

**Options:**

- **(A)** $3$
- **(B)** $1$
- **(C)** $0$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-1$**

**Detailed Solution:**

Given $a_{ij} = |2i - 5j|$, we construct the matrix $A$ of order $3 \times 3$:

$A = \begin{bmatrix} |2(1)-5(1)| & |2(1)-5(2)| & |2(1)-5(3)| \\ |2(2)-5(1)| & |2(2)-5(2)| & |2(2)-5(3)| \\ |2(3)-5(1)| & |2(3)-5(2)| & |2(3)-5(3)| \end{bmatrix} = \begin{bmatrix} 3 & 8 & 13 \\ 1 & 6 & 11 \\ 1 & 4 & 9 \end{bmatrix}$

The determinant of matrix $A$ is:

$|A| = 3(54 - 44) - 8(9 - 11) + 13(4 - 6)$

$|A| = 3(10) - 8(-2) + 13(-2) = 30 + 16 - 26 = 20$

The element in the $2^{\text{nd}}$ row and $3^{\text{rd}}$ column of $A^{-1}$ is given by $\dfrac{C_{32}}{|A|}$, where $C_{32}$ is the cofactor of the element $a_{32}$ in matrix $A$.

Calculating the cofactor $C_{32}$:

$C_{32} = (-1)^{3+2} \begin{vmatrix} 3 & 13 \\ 1 & 11 \end{vmatrix} = -(33 - 13) = -20$

Therefore, the required element is:

$\dfrac{C_{32}}{|A|} = \dfrac{-20}{20} = -1$

Answer: $-1$

</details>

---

### Q2. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A=\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right], B=\left[\begin{array}{l}1 \\ 1 \\ 2\end{array}\right]$ and $X=\left[\begin{array}{l}x_1 \\ x_2 \\ x_3\end{array}\right]$ such that $A X=B$, then the value of $x_1+x_2+x_3=$

**Options:**

- **(A)** 4
- **(B)** 5
- **(C)** 6
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 3**

**Detailed Solution:**

$\begin{aligned} & {\left[\begin{array}{ccc}1 & -1 & 1 \\ 2 & -1 & 0 \\ 3 & 3 & -4\end{array}\right]\left[\begin{array}{l}\mathrm{x}_1 \\ \mathrm{x}_2 \\ \mathrm{x}_3\end{array}\right]=\left[\begin{array}{l}1 \\ 1 \\ 2\end{array}\right]} \\ & \mathrm{R}_3 \rightarrow \mathrm{R}_3-3 \mathrm{R}_1 \text { and } \mathrm{R}_2 \rightarrow \mathrm{R}_2-2 \mathrm{R}_1 \\ & {\left[\begin{array}{ccc}1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 6 & -7\end{array}\right]\left[\begin{array}{l}\mathrm{x}_1 \\ \mathrm{x}_2 \\ \mathrm{x}_3\end{array}\right]=\left[\begin{array}{c}1 \\ -1 \\ -1\end{array}\right]} \\ & \mathrm{R}_3 \rightarrow \mathrm{R}_3-6 \mathrm{R}_2 \\ & {\left[\begin{array}{ccc}1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 5\end{array}\right]\left[\begin{array}{l}\mathrm{x}_1 \\ \mathrm{x}_2 \\ \mathrm{x}_3\end{array}\right]=\left[\begin{array}{c}1 \\ -1 \\ 5\end{array}\right]} \\ & \therefore \quad \mathrm{x}_1-\mathrm{x}_2+\mathrm{x}_3=1 \\ & \quad \mathrm{x}_2-2 \mathrm{x}_3=-1 \\ & \quad 5 \mathrm{x}_3=5 \\ & \therefore \mathrm{x}_3=1, \mathrm{x}_2=1, \mathrm{x}_1=1\end{aligned}$

</details>

---

