# JEE Advanced Mathematics - Permutation Combination

## Topic 2: Division of Identical items

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `2`

The number of ways to distribute $10$ identical red pens and $14$ identical blue pens among four persons such that each person gets $6$ pens, is _____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **206**

**Detailed Solution:**

Let $r_i$ and $b_i$ be the number of red and blue pens given to the $i$-th person, where $i = 1, 2, 3, 4$.

Given that each person receives exactly $6$ pens, we have:
$r_i + b_i = 6 \Rightarrow b_i = 6 - r_i$

Since the number of blue pens must be non-negative ($b_i \ge 0$), we get $r_i \le 6$. Also, $r_i \ge 0$.

The total number of red pens is $10$, so:
$r_1 + r_2 + r_3 + r_4 = 10$

The number of ways to distribute the pens is the number of non-negative integer solutions to this equation subject to $0 \le r_i \le 6$.

This is equivalent to finding the coefficient of $x^{10}$ in the expansion of $(1 + x + x^2 + \dots + x^6)^4$.

$(1 + x + x^2 + \dots + x^6)^4 = \left( \dfrac{1 - x^7}{1 - x} \right)^4 = (1 - x^7)^4 (1 - x)^{-4}$

Expanding both terms:
$(1 - x^7)^4 = 1 - 4x^7 + 6x^{14} - \dots$
$(1 - x)^{-4} = \sum_{k=0}^{\infty} {}^{k+3}C_{3} x^k$

We need the coefficient of $x^{10}$ in the product $(1 - 4x^7 + \dots) \sum_{k=0}^{\infty} {}^{k+3}C_{3} x^k$.

Coefficient of $x^{10} = 1 \times (\text{coefficient of } x^{10} \text{ in } (1-x)^{-4}) - 4 \times (\text{coefficient of } x^3 \text{ in } (1-x)^{-4})$

$= {}^{10+3}C_{3} - 4 \times {}^{3+3}C_{3}$

$= {}^{13}C_{3} - 4 \times {}^{6}C_{3}$

$= \dfrac{13 \times 12 \times 11}{3 \times 2 \times 1} - 4 \times \dfrac{6 \times 5 \times 4}{3 \times 2 \times 1}$

$= 286 - 4 \times 20$

$= 286 - 80 = 206$

Answer: $206$

</details>

---

