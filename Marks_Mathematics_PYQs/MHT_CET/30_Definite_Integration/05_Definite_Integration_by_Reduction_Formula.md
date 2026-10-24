# MHT CET Mathematics - Definite Integration

## Topic 5: Definite Integration by Reduction Formula

**Total Questions:** 2

---

### Q1. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $I_n = \int\limits_0^{\pi/4}\tan^n x\ dx, n \in N$ then $I_{n+2} + I_n$ is equal to

**Options:**

- **(A)** $\dfrac{1}{n}$
- **(B)** $\dfrac{1}{n + 1}$
- **(C)** $\dfrac{1}{n - 1}$
- **(D)** $\dfrac{1}{n - 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{n + 1}$**

**Detailed Solution:**

$I_{n+2} + I_n = \int\limits_0^{\pi/4} \tan^{n+2} x\ dx + \int\limits_0^{\pi/4} \tan^n x\ dx$

$I_{n+2} + I_n = \int\limits_0^{\pi/4} \tan^n x (\tan^2 x + 1)\ dx$

$I_{n+2} + I_n = \int\limits_0^{\pi/4} \tan^n x \sec^2 x\ dx$

Substituting $t = \tan x$, we get $dt = \sec^2 x\ dx$.

When $x = 0$, $t = 0$ and when $x = \pi/4$, $t = 1$.

$I_{n+2} + I_n = \int\limits_0^1 t^n\ dt$

$I_{n+2} + I_n = \left[ \dfrac{t^{n+1}}{n+1} \right]_0^1$

$I_{n+2} + I_n = \dfrac{1}{n+1}$

Answer: $\dfrac{1}{n + 1}$

</details>

---

### Q2. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\int_{0}^{1} x(1-x)^{5} d x=$

**Options:**

- **(A)** $\frac{1}{7}$
- **(B)** $-\frac{1}{42}$
- **(C)** $\frac{1}{42}$
- **(D)** $\frac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{42}$**

**Detailed Solution:**

(C)
$\begin{aligned} \text { Let } I &=\int_{0}^{1} x(1-x)^{5} d x \\ \therefore I &=\int_{0}^{1}(1-x)(1-(1-x))^{5} d x=\int_{0}^{1}(1-x) x^{5} d x=\int\left(x^{5}-x^{6}\right) d x \\ &=\left[\frac{x^{6}}{6}-\frac{x^{7}}{7}\right]_{0}^{1}=\frac{1}{6}-\frac{1}{7}=\frac{1}{42} \end{aligned}$

</details>

---

