# JEE Advanced Mathematics - Statistics

## Topic 2: Mean

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `2`

Consider a data consisting of $10$ observations $x_1, x_2, \ldots, x_{10}$, whose mean is $5$ and variance is $7$. If the mean and the variance of the first $8$ observations $x_1, x_2, \ldots, x_8$ are $4$ and $3.5$, respectively, and $x_9 < x_{10}$, then the value of $3x_9 + 2x_{10}$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **44**

**Detailed Solution:**

Given $\dfrac{\sum_{i=1}^{10} x_i}{10} = 5 \Rightarrow \sum_{i=1}^{10} x_i = 50$

$\dfrac{\sum_{i=1}^{10} x_i^2}{10} - 5^2 = 7 \Rightarrow \sum_{i=1}^{10} x_i^2 = 320$

For the first $8$ observations:

$\dfrac{\sum_{i=1}^{8} x_i}{8} = 4 \Rightarrow \sum_{i=1}^{8} x_i = 32$

$\dfrac{\sum_{i=1}^{8} x_i^2}{8} - 4^2 = 3.5 \Rightarrow \sum_{i=1}^{8} x_i^2 = 8(3.5 + 16) = 156$

Subtracting the sums, we get:

$x_9 + x_{10} = 50 - 32 = 18$

$x_9^2 + x_{10}^2 = 320 - 156 = 164$

Using $(x_9 + x_{10})^2 = x_9^2 + x_{10}^2 + 2x_9 x_{10}$:

$18^2 = 164 + 2x_9 x_{10} \Rightarrow 2x_9 x_{10} = 324 - 164 = 160 \Rightarrow x_9 x_{10} = 80$

The numbers $x_9$ and $x_{10}$ are roots of the equation $t^2 - 18t + 80 = 0$.

$(t - 8)(t - 10) = 0 \Rightarrow t = 8, 10$

Since $x_9 < x_{10}$, we have $x_9 = 8$ and $x_{10} = 10$.

Therefore, $3x_9 + 2x_{10} = 3(8) + 2(10) = 24 + 20 = 44$.

Answer: $44$

</details>

---

