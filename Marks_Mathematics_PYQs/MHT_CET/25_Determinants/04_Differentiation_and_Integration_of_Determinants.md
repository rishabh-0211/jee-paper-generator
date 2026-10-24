# MHT CET Mathematics - Determinants

## Topic 4: Differentiation and Integration of Determinants

**Total Questions:** 1

---

### Q1. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \begin{vmatrix} x^2 & \sin x & e^x \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix}$ then $f''(0) = $

**Options:**

- **(A)** $2p^2 - p + 1$
- **(B)** $4p^2 - p + 1$
- **(C)** $4p^2 - p + 2$
- **(D)** $2p^2 - p + 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4p^2 - p + 2$**

**Detailed Solution:**

Given $f(x) = \begin{vmatrix} x^2 & \sin x & e^x \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix}$

Since the second and third rows are independent of $x$, we can differentiate the determinant by differentiating only the first row.

$f'(x) = \begin{vmatrix} \dfrac{d}{dx}(x^2) & \dfrac{d}{dx}(\sin x) & \dfrac{d}{dx}(e^x) \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix} = \begin{vmatrix} 2x & \cos x & e^x \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix}$

Differentiating again with respect to $x$:

$f''(x) = \begin{vmatrix} \dfrac{d}{dx}(2x) & \dfrac{d}{dx}(\cos x) & \dfrac{d}{dx}(e^x) \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix} = \begin{vmatrix} 2 & -\sin x & e^x \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix}$

Substituting $x = 0$:

$f''(0) = \begin{vmatrix} 2 & -\sin 0 & e^0 \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix} = \begin{vmatrix} 2 & 0 & 1 \\ 2 & 1 & -1 \\ p & p^2 & 1 \end{vmatrix}$

Expanding the determinant along the first row:

$f''(0) = 2(1 - (-p^2)) - 0 + 1(2p^2 - p)$

$f''(0) = 2(1 + p^2) + 2p^2 - p$

$f''(0) = 4p^2 - p + 2$

Answer: $4p^2 - p + 2$

</details>

---

