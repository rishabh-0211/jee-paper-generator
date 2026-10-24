# MHT CET Mathematics - Inverse Trigonometric Functions

## Topic 7: Infinite Series

**Total Questions:** 2

---

### Q1. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\cot ^{-1}\left(2 \cdot 1^2\right)+\cot ^{-1}\left(2 \cdot 2^2\right)+\cot ^{-1}\left(2 \cdot 3^2\right)+\ldots \ldots \ldots \ldots \ldots \ldots \ldots \infty =$

**Options:**

- **(A)** $\frac{\pi}{2}$
- **(B)** $\frac{\pi}{3}$
- **(C)** $\frac{\pi}{4}$
- **(D)** $\frac{\pi}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\pi}{4}$**

**Detailed Solution:**

The $n^{\text{th}}$ term of the given series is $T_n = \cot^{-1}(2n^2)$.

$T_n = \tan^{-1}\left(\dfrac{1}{2n^2}\right) = \tan^{-1}\left(\dfrac{2}{4n^2}\right)$

$T_n = \tan^{-1}\left(\dfrac{(2n+1) - (2n-1)}{1 + (2n+1)(2n-1)}\right)$

Using the formula $\tan^{-1}\left(\dfrac{x-y}{1+xy}\right) = \tan^{-1}(x) - \tan^{-1}(y)$, we get:

$T_n = \tan^{-1}(2n+1) - \tan^{-1}(2n-1)$

Writing the first few terms:

$T_1 = \tan^{-1}(3) - \tan^{-1}(1)$

$T_2 = \tan^{-1}(5) - \tan^{-1}(3)$

$T_3 = \tan^{-1}(7) - \tan^{-1}(5)$

$\dots$

$T_n = \tan^{-1}(2n+1) - \tan^{-1}(2n-1)$

Adding these terms, the sum of the first $n$ terms is:

$S_n = \tan^{-1}(2n+1) - \tan^{-1}(1)$

For the sum to infinity, we take the limit as $n \to \infty$:

$S_{\infty} = \lim_{n \to \infty} [\tan^{-1}(2n+1) - \tan^{-1}(1)]$

$S_{\infty} = \dfrac{\pi}{2} - \dfrac{\pi}{4} = \dfrac{\pi}{4}$

Answer: $\frac{\pi}{4}$

</details>

---

### Q2. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\cot \left(\sum_{n=1}^{23} \cot ^{-1}\left(1+\sum_{k=1}^n 2 k\right)\right)$ is

**Options:**

- **(A)** $\frac{23}{25}$
- **(B)** $\frac{25}{23}$
- **(C)** $\frac{23}{24}$
- **(D)** $\frac{24}{23}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{25}{23}$**

**Detailed Solution:**

$\begin{aligned} & \cot \left(\sum_{n=1}^{23} \cot ^{-1}\left(1+\sum_{k=1}^n 2 k\right)\right) \\ & =\cot \left(\sum_{n=1}^{23} \cot ^{-1}\left(1+2 \times \frac{n(n+1)}{2}\right)\right) \\ & =\cot \left(\sum_{n=1}^{23} \cot ^{-1}(1+n(n+1))\right)\end{aligned}$
$\begin{aligned} & =\cot \left(\sum_{n=1}^{23} \tan ^{-1}\left(\frac{1}{1+\mathrm{n}(\mathrm{n}+1)}\right)\right) \\ & =\cot \left(\sum_{\mathrm{n}=1}^{23} \tan ^{-1}\left(\frac{\mathrm{n}+1-\mathrm{n}}{1+\mathrm{n}(\mathrm{n}+1)}\right)\right) \\ & =\cot \left(\sum_{\mathrm{n}=1}^{23} \tan ^{-1}(\mathrm{n}+1)-\sum_{\mathrm{n}-1}^{23} \tan ^{-1} \mathrm{n}\right) \\ & =\cot \left[\left(\tan ^{-1}(2)+\tan ^{-1}(3)+\ldots+\tan ^{-1}(24)\right)\right. \\ & =\cot \left(\tan ^{-1}(24)-\tan ^{-1}(1)\right) \\ & =\cot \left(\tan ^{-1}\left(\frac{24-1}{1+24(1)}\right)\right) \\ & =\cot \left(\tan ^{-1}\left(\frac{23}{25}\right)\right) \\ & =\cot \left(\cot ^{-1}\left(\frac{25}{23}\right)\right) \\ & =\frac{25}{23}\end{aligned}$

</details>

---

