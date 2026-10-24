# MHT CET Mathematics - Matrices

## Topic 7: Symmetric & Skew Symmetric Matrices

**Total Questions:** 2

---

### Q1. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the matrix $A = \begin{bmatrix} 4 & 1 \\ 3 & 2 \end{bmatrix}$ is expressed as the sum of a symmetric matrix B and a skew symmetric matrix C then which of the following relations is correct?

**Options:**

- **(A)** $|A| = |B| \times |C|$
- **(B)** $|A| = |B| + |C|$
- **(C)** $|C| = 0$
- **(D)** $|A| = |B|$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $|A| = |B| + |C|$**

**Detailed Solution:**

Given $A = \begin{bmatrix} 4 & 1 \\ 3 & 2 \end{bmatrix}$

The transpose of matrix $A$ is $A^T = \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}$

Any square matrix can be expressed as the sum of a symmetric matrix $B$ and a skew-symmetric matrix $C$, where $B = \dfrac{1}{2}(A + A^T)$ and $C = \dfrac{1}{2}(A - A^T)$

$B = \dfrac{1}{2} \left( \begin{bmatrix} 4 & 1 \\ 3 & 2 \end{bmatrix} + \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix} \right) = \begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix}$

$C = \dfrac{1}{2} \left( \begin{bmatrix} 4 & 1 \\ 3 & 2 \end{bmatrix} - \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix} \right) = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$

Calculating the determinants of $A$, $B$, and $C$:

$|A| = (4)(2) - (1)(3) = 5$

$|B| = (4)(2) - (2)(2) = 4$

$|C| = (0)(0) - (-1)(1) = 1$

Checking the given relations, we find that $|B| + |C| = 4 + 1 = 5$

Therefore, $|A| = |B| + |C|$

Answer: $|A| = |B| + |C|$

</details>

---

### Q2. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\mathrm{A}+\mathrm{B}=\left[\begin{array}{cr}1 & \tan \dfrac{\theta}{2} \\ -\tan \dfrac{\theta}{2} & 1\end{array}\right]$ where A is symmetric and B is skew-symmetric matrix, then the matrix $\left(A^{-1} B+A B^{-1}\right)$ at $\theta=\dfrac{\pi}{6}$ is given by

**Options:**

- **(A)** $\left[\begin{array}{cc}1 & 2 \sqrt{3} \\ 2 \sqrt{3} & 1\end{array}\right]$
- **(B)** $\left[\begin{array}{cc}-1 & -2 \sqrt{3} \\ 2 \sqrt{3} & 1\end{array}\right]$
- **(C)** $\left[\begin{array}{cc}0 & 2 \sqrt{3} \\ 2 \sqrt{3} & 0\end{array}\right]$
- **(D)** $\left[\begin{array}{cc}0 & -2 \sqrt{3} \\ 2 \sqrt{3} & 0\end{array}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left[\begin{array}{cc}0 & -2 \sqrt{3} \\ 2 \sqrt{3} & 0\end{array}\right]$**

**Detailed Solution:**

Let $M = A + B = \left[\begin{array}{cr}1 & \tan \dfrac{\theta}{2} \\ -\tan \dfrac{\theta}{2} & 1\end{array}\right]$.

Since $A$ is a symmetric matrix and $B$ is a skew-symmetric matrix, they can be uniquely determined by:

$A = \dfrac{M + M^T}{2}$ and $B = \dfrac{M - M^T}{2}$

Calculating $A$ and $B$:

$A = \dfrac{1}{2} \left( \left[\begin{array}{cr}1 & \tan \dfrac{\theta}{2} \\ -\tan \dfrac{\theta}{2} & 1\end{array}\right] + \left[\begin{array}{cr}1 & -\tan \dfrac{\theta}{2} \\ \tan \dfrac{\theta}{2} & 1\end{array}\right] \right) = \left[\begin{array}{cr}1 & 0 \\ 0 & 1\end{array}\right] = I$

$B = \dfrac{1}{2} \left( \left[\begin{array}{cr}1 & \tan \dfrac{\theta}{2} \\ -\tan \dfrac{\theta}{2} & 1\end{array}\right] - \left[\begin{array}{cr}1 & -\tan \dfrac{\theta}{2} \\ \tan \dfrac{\theta}{2} & 1\end{array}\right] \right) = \left[\begin{array}{cr}0 & \tan \dfrac{\theta}{2} \\ -\tan \dfrac{\theta}{2} & 0\end{array}\right]$

We need to find the value of $A^{-1} B + A B^{-1}$. Since $A = I$, we have $A^{-1} = I$.

$A^{-1} B + A B^{-1} = I B + I B^{-1} = B + B^{-1}$

At $\theta = \dfrac{\pi}{6}$, let $t = \tan \dfrac{\pi}{12} = 2 - \sqrt{3}$.

$B = \left[\begin{array}{cr}0 & t \\ -t & 0\end{array}\right]$

The inverse of $B$ is given by:

$B^{-1} = \dfrac{1}{t^2} \left[\begin{array}{cr}0 & -t \\ t & 0\end{array}\right] = \left[\begin{array}{cr}0 & -\dfrac{1}{t} \\ \dfrac{1}{t} & 0\end{array}\right]$

Since $t = 2 - \sqrt{3}$, we have $\dfrac{1}{t} = \dfrac{1}{2 - \sqrt{3}} = 2 + \sqrt{3}$.

Now, adding $B$ and $B^{-1}$:

$B + B^{-1} = \left[\begin{array}{cr}0 & t \\ -t & 0\end{array}\right] + \left[\begin{array}{cr}0 & -\dfrac{1}{t} \\ \dfrac{1}{t} & 0\end{array}\right] = \left[\begin{array}{cc}0 & t - \dfrac{1}{t} \\ -t + \dfrac{1}{t} & 0\end{array}\right]$

Evaluating the terms:

$t - \dfrac{1}{t} = (2 - \sqrt{3}) - (2 + \sqrt{3}) = -2\sqrt{3}$

$-t + \dfrac{1}{t} = -(2 - \sqrt{3}) + (2 + \sqrt{3}) = 2\sqrt{3}$

Therefore, the required matrix is:

$A^{-1} B + A B^{-1} = \left[\begin{array}{cc}0 & -2 \sqrt{3} \\ 2 \sqrt{3} & 0\end{array}\right]$

Answer: $\left[\begin{array}{cc}0 & -2 \sqrt{3} \\ 2 \sqrt{3} & 0\end{array}\right]$

</details>

---

