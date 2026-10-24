# JEE Main Mathematics - Matrices

## Topic 6: Types of Matrices

**Total Questions:** 1

---

### Q1. JEE Main 2026 (23 January Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $A=\left[\begin{array}{ccc}0 & 2 & -3 \\ -2 & 0 & 1 \\ 3 & -1 & 0\end{array}\right]$ and $B$ be a matrix such that $B(I-A)=I+A$. Then the sum of the diagonal elements of $\mathrm{B}^{\mathrm{T}} \mathrm{B}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

$A$ is skew-symmetric ($A^T = -A$).
From $B(I-A) = I+A$:
$B = (I+A)(I-A)^{-1}$.
$B^T = ((I-A)^T)^{-1}(I+A)^T = (I+A)^{-1}(I-A)$.
Since $A$ is skew-symmetric, $(I-A)$ and $(I+A)$ commute:
$(I-A)(I+A) = I - A^2 = (I+A)(I-A)$.
$B^TB = (I+A)^{-1}(I-A)(I+A)(I-A)^{-1} = (I+A)^{-1}(I+A)(I-A)(I-A)^{-1} = I$.
Trace of $B^TB = \text{tr}(I) = 3$.

</details>

---

