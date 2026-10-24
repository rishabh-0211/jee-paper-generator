# BITSAT Mathematics - Matrices

## Topic 1: Basic Algebra of Matrices

**Total Questions:** 3

---

### Q1. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ and $B$ are symmetric matrices of same order such that $A B+B A=X$ and $A B-B A=Y$, then $(X Y)^{\mathrm{T}}=$

**Options:**

- **(A)** $X Y$
- **(B)** $X^{\top} Y^{\top}$
- **(C)** -YX
- **(D)** $-Y^{\top} X^{\top}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) -YX**

**Detailed Solution:**

Since $X Y=(A B+B A)(A B-B A)$
$=(\mathrm{AB}) \mathrm{AB}+(\mathrm{BA})(\mathrm{AB})-(\mathrm{AB})(\mathrm{BA})-(\mathrm{BA})(\mathrm{BA})$
Now $(X Y)^{\mathrm{T}}=((\mathrm{AB}) \cdot(\mathrm{AB}))^{\mathrm{T}}+(\mathrm{BA} \cdot \mathrm{AB})^{\mathrm{T}}-$ $(\mathrm{AB} \cdot \mathrm{BA})^{\mathrm{T}}$
$\begin{array}{r}=(\mathrm{AB})^{\mathrm{T}} \cdot(\mathrm{AB})^{\mathrm{T}}+(\mathrm{AB})^{\mathrm{T}} \cdot(\mathrm{BA})^{\mathrm{T}}-(\mathrm{BA})^{\mathrm{T}}(\mathrm{AB})^{\mathrm{T}} \\ -(\mathrm{BA})^{\mathrm{T}}(\mathrm{BA})^{\mathrm{T}}\end{array}$
$=\left(B^{\top} \cdot A^{\top}\right)\left(B^{\top} \cdot A^{\top}\right)+\left(B^{\top} \cdot A^{\top}\right) \cdot\left(A^{\top} B^{\top}\right)$
$-\left(\mathrm{A}^{\top} \mathrm{B}^{\top}\right)\left(\mathrm{B}^{\top} \mathrm{A}^{\top}\right)-\left(\mathrm{A}^{\top} \mathrm{B}^{\top}\right)\left(\mathrm{A}^{\top} \mathrm{B}^{\top}\right)$
Since, A & B are symmetric matrix.
$=(\mathrm{BA})(\mathrm{BA})+(\mathrm{BA})(\mathrm{AB})-(\mathrm{AB})(\mathrm{BA})$
$-(\mathrm{AB})(\mathrm{AB})$
$=(\mathrm{BA}-\mathrm{AB})(\mathrm{BA}+\mathrm{AB})=-\mathrm{YX}$

</details>

---

### Q2. BITSAT 2023 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}=\left[\begin{array}{cc}0 & 2 \\ 3 & -4\end{array}\right]$ and $k \mathrm{~A}=\left[\begin{array}{cc}0 & 3 a \\ 2 b & 24\end{array}\right]$, then the values of $k, a$ and $b$ respectively are:

**Options:**

- **(A)** $-6,-12,-18$
- **(B)** $-6,-4,-9$
- **(C)** $-6,4,9$
- **(D)** $-6,12,18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-6,-4,-9$**

**Detailed Solution:**

$k A=\left[\begin{array}{cc}0 & 2 k \\ 3 k & -4 k\end{array}\right]=\left[\begin{array}{cc}0 & 3 a \\ 2 b & 24\end{array}\right]$
$\Rightarrow \quad k=-6, a=-4$ and $b=-9$

</details>

---

### Q3. BITSAT 2010

*Type:* `singleCorrect` | *Level:* `1`

The value of \(\cos ^{-1} x+\cos ^{-1}\left(\frac{x}{2}+\frac{1}{2} \sqrt{3-3 x^2}\right)\); \(\frac{1}{2} \leq x \leq 1\) is

**Options:**

- **(A)** \(-\frac{\pi}{3}\)
- **(B)** \(\frac{\pi}{3}\)
- **(C)** \(\frac{3}{\pi}\)
- **(D)** \(-\frac{3}{\pi}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(\frac{\pi}{3}\)**

**Detailed Solution:**

Let \(\cos ^{-1} x=y\)
\(\Rightarrow x=\cos y\), so that \(\frac{1}{2} \leq x \leq 1\) or \(\quad 0 \leq y \leq \frac{\pi}{3}\)
and \(\frac{x}{2}+\frac{1}{2} \sqrt{3-3 x^2}=\frac{1}{2} \cos y+\frac{\sqrt{3}}{2} \sin y\)
\(=\cos \frac{\pi}{3} \cos y+\sin \frac{\pi}{3} \sin y=\cos \left(\frac{\pi}{3}-y\right)\)
\(\Rightarrow \cos ^{-1}\left(\frac{x}{2}+\frac{1}{2} \sqrt{3-3 x^2}\right)=\frac{\pi}{3}-y\)
\(\therefore\) the given expression is equal to
\(y+\frac{\pi}{3}-y, \text { i.e., } \frac{\pi}{3}\)

</details>

---

