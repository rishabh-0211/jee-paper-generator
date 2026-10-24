# JEE Advanced Mathematics - Matrices

## Topic 8: Types of Matrices

**Total Questions:** 2

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

For real numbers $\alpha, \beta, \gamma, \delta$ and $\mu$, consider the matrix

$M = \begin{bmatrix} \alpha & \dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}} \\ \dfrac{1}{\sqrt{3}} & \beta & \dfrac{1}{\sqrt{3}} \\ \gamma & \delta & \mu \end{bmatrix}$.

Suppose that $MM^T = I$, where $M^T$ is the transpose of the matrix $M$, and $I$ is the $3 \times 3$ identity matrix. Let
$\vec{u} = \alpha\,\hat{i} + \dfrac{1}{\sqrt{3}}\,\hat{j} + \gamma\,\hat{k}$, $\vec{v} = \dfrac{1}{\sqrt{2}}\,\hat{i} + \beta\,\hat{j} + \delta\,\hat{k}$ and $\vec{w} = -\dfrac{1}{\sqrt{2}}\,\hat{i} + \dfrac{1}{\sqrt{3}}\,\hat{j} + \mu\,\hat{k}$.

Match each entry in List-I to the correct entry in List-II and choose the correct option.
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 10px;">List-I</th><th style="border: 1px solid black; padding: 10px;">List-II</th></tr><tr><td style="border: 1px solid black; padding: 10px;">(P) The value of $\gamma^2 + \delta^2$ is</td><td style="border: 1px solid black; padding: 10px;">(1) $0$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(Q) If $x\vec{u} + y\vec{v} + z\vec{w} = \hat{j}$ for some real numbers $x, y$ and $z$, then the value of $x$ is</td><td style="border: 1px solid black; padding: 10px;">(2) $1$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(R) The value of $|\vec{u} \cdot (\vec{v} \times \vec{w})|$ is</td><td style="border: 1px solid black; padding: 10px;">(3) $\dfrac{1}{\sqrt{2}}$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">(S) The value of $|\vec{u} \times (\vec{v} \times \vec{w})|$ is</td><td style="border: 1px solid black; padding: 10px;">(4) $\dfrac{1}{\sqrt{3}}$</td></tr><tr><td style="border: 1px solid black; padding: 10px;"></td><td style="border: 1px solid black; padding: 10px;">(5) $\dfrac{5}{6}$</td></tr></table>

**Options:**

- **(A)** (P) $\rightarrow$ (5), (Q) $\rightarrow$ (4), (R) $\rightarrow$ (2), (S) $\rightarrow$ (1)
- **(B)** (P) $\rightarrow$ (4), (Q) $\rightarrow$ (5), (R) $\rightarrow$ (1), (S) $\rightarrow$ (2)
- **(C)** (P) $\rightarrow$ (5), (Q) $\rightarrow$ (3), (R) $\rightarrow$ (2), (S) $\rightarrow$ (1)
- **(D)** (P) $\rightarrow$ (5), (Q) $\rightarrow$ (4), (R) $\rightarrow$ (1), (S) $\rightarrow$ (2)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (P) $\rightarrow$ (5), (Q) $\rightarrow$ (4), (R) $\rightarrow$ (2), (S) $\rightarrow$ (1)**

**Detailed Solution:**

Since $MM^T = I$, $M$ is an orthogonal matrix.

The columns of an orthogonal matrix form an orthonormal basis for $\mathbb{R}^3$. The given vectors $\vec{u}, \vec{v}, \vec{w}$ are exactly the columns of $M$. Therefore, $\vec{u}, \vec{v}, \vec{w}$ are mutually orthogonal unit vectors.

For (P): The rows of $M$ are also orthonormal. The third row is $\begin{bmatrix} \gamma & \delta & \mu \end{bmatrix}$, so $\gamma^2 + \delta^2 + \mu^2 = 1$.

The third column $\vec{w}$ is a unit vector, so $|\vec{w}|^2 = \left(-\dfrac{1}{\sqrt{2}}\right)^2 + \left(\dfrac{1}{\sqrt{3}}\right)^2 + \mu^2 = 1$.

$\dfrac{1}{2} + \dfrac{1}{3} + \mu^2 = 1 \Rightarrow \mu^2 = \dfrac{1}{6}$

Substituting $\mu^2$ into the row equation gives $\gamma^2 + \delta^2 = 1 - \dfrac{1}{6} = \dfrac{5}{6}$. Thus, (P) $\rightarrow$ (5).

For (Q): Given $x\vec{u} + y\vec{v} + z\vec{w} = \hat{j}$. Taking the dot product with $\vec{u}$ on both sides gives $x(\vec{u} \cdot \vec{u}) + y(\vec{v} \cdot \vec{u}) + z(\vec{w} \cdot \vec{u}) = \hat{j} \cdot \vec{u}$.

Since the vectors are orthonormal, $\vec{u} \cdot \vec{u} = 1$ and $\vec{v} \cdot \vec{u} = \vec{w} \cdot \vec{u} = 0$.

Thus, $x = \hat{j} \cdot \vec{u}$. From the definition of $\vec{u}$, the $\hat{j}$ component is $\dfrac{1}{\sqrt{3}}$, so $x = \dfrac{1}{\sqrt{3}}$. Thus, (Q) $\rightarrow$ (4).

For (R): The scalar triple product $\vec{u} \cdot (\vec{v} \times \vec{w})$ represents the determinant of the matrix formed by these column vectors, which is $M$.

Since $M$ is orthogonal, $\det(M) = \pm 1$. Thus, $|\vec{u} \cdot (\vec{v} \times \vec{w})| = |\det(M)| = 1$. Thus, (R) $\rightarrow$ (2).

For (S): Using the vector triple product expansion, $\vec{u} \times (\vec{v} \times \vec{w}) = (\vec{u} \cdot \vec{w})\vec{v} - (\vec{u} \cdot \vec{v})\vec{w}$.

Since $\vec{u}, \vec{v}, \vec{w}$ are mutually orthogonal, $\vec{u} \cdot \vec{w} = 0$ and $\vec{u} \cdot \vec{v} = 0$.

Thus, $\vec{u} \times (\vec{v} \times \vec{w}) = \vec{0}$, and its magnitude is $0$. Thus, (S) $\rightarrow$ (1).

Answer: (P) $\rightarrow$ (5), (Q) $\rightarrow$ (4), (R) $\rightarrow$ (2), (S) $\rightarrow$ (1)

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider the matrix, $P=\left(\begin{array}{lll}2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3\end{array}\right)$
Let the transpose of a matrix $X$ be denoted by $\mathrm{X}^T$. Then the number of $3 \times 3$ invertible matrices Q with integer entries, such that $Q^{-1}=Q^T$ and $P Q=Q P$ is

**Options:**

- **(A)** 32
- **(B)** 8
- **(C)** 16
- **(D)** 24

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 16**

**Detailed Solution:**

\(\begin{aligned}
& \mathrm{PQ}=\mathrm{QP} \Rightarrow\left[\begin{array}{ccc}
2 \mathrm{a}_1 & 2 \mathrm{~b}_1 & 2 \mathrm{c}_1 \\
2 \mathrm{a}_2 & 2 \mathrm{~b}_2 & 2 \mathrm{c}_2 \\
3 \mathrm{a}_3 & 3 \mathrm{~b}_3 & 3 \mathrm{c}_3
\end{array}\right]=\left[\begin{array}{ccc}
2 \mathrm{a}_1 & 2 \mathrm{~b}_1 & 3 \mathrm{c}_1 \\
2 \mathrm{a}_2 & 2 \mathrm{~b}_2 & 3 \mathrm{c}_2 \\
2 \mathrm{a}_3 & 2 \mathrm{~b}_3 & 3 \mathrm{c}_3
\end{array}\right] \\
& \mathrm{c}_1=0, \mathrm{c}_2=0, \mathrm{a}_3=0, \mathrm{~b}_3=0 \\
& \mathrm{Q}=\left[\begin{array}{ccc}
\mathrm{a}_1 & \mathrm{~b}_1 & 0 \\
\mathrm{a}_2 & \mathrm{~b}_2 & 0 \\
0 & 0 & \mathrm{c}_3
\end{array}\right] \\
& \mathrm{a}_1 \mathrm{a}_2+\mathrm{b}_1 \mathrm{~b}_2=0 \\
& \mathrm{a}_1^2+\mathrm{b}_1^2=1, \mathrm{a}_2^2+\mathrm{b}_2^2=1, \mathrm{c}_3^2=1
\end{aligned}\)
\(\begin{array}{lllll}
a_1 & b_1 & a_2 & b_2 & c_3 \\
1 & 0 & 0 & 1,-1 & +1,-1 \\
-1 & 0 & 0 & 1,-1 & 1,-1 \\
0 & 1 & 1,-1 & 0 & 1,-1 \\
0 & -1 & 1,-1 & 0 & 1,-1
\end{array}\)
Total 16 matrices

</details>

---

