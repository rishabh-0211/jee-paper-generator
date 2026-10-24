# MHT CET Mathematics - Binomial Theorem

## Topic 5: Sum of Series

**Total Questions:** 1

---

### Q1. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If ${ }^{\mathrm{n}} \mathrm{C}_0+\frac{1}{2}{ }^{\mathrm{n}} \mathrm{C}_1+\frac{1}{3}{ }^{\mathrm{n}} \mathrm{C}_2+\ldots \ldots \ldots \ldots . . \cdot \frac{1}{\mathrm{n}}{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{n}-1}+\frac{1}{\mathrm{n}+1}{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{n}}=\frac{1023}{10}$ then $\mathrm{n}=$

**Options:**

- **(A)** 7
- **(B)** 8
- **(C)** 9
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 9**

**Detailed Solution:**

Consider the binomial expansion:

$(1+x)^n = ^{n}C_0 + ^{n}C_1 x + ^{n}C_2 x^2 + \dots + ^{n}C_n x^n$

Integrating both sides with respect to $x$ from $0$ to $1$:

$\int_{0}^{1} (1+x)^n dx = \int_{0}^{1} (^{n}C_0 + ^{n}C_1 x + ^{n}C_2 x^2 + \dots + ^{n}C_n x^n) dx$

$\left[ \dfrac{(1+x)^{n+1}}{n+1} \right]_0^1 = \left[ ^{n}C_0 x + ^{n}C_1 \dfrac{x^2}{2} + ^{n}C_2 \dfrac{x^3}{3} + \dots + ^{n}C_n \dfrac{x^{n+1}}{n+1} \right]_0^1$

$\dfrac{2^{n+1}-1}{n+1} = ^{n}C_0 + \dfrac{1}{2} ^{n}C_1 + \dfrac{1}{3} ^{n}C_2 + \dots + \dfrac{1}{n+1} ^{n}C_n$

Given that the sum is equal to $\dfrac{1023}{10}$, we have:

$\dfrac{2^{n+1}-1}{n+1} = \dfrac{1023}{10}$

Comparing the denominators, we can check $n+1 = 10 \Rightarrow n = 9$.

Checking the numerator for $n = 9$:

$2^{9+1}-1 = 2^{10}-1 = 1024-1 = 1023$

This satisfies the equation perfectly.

Therefore, $n = 9$.

Answer: 9

</details>

---

