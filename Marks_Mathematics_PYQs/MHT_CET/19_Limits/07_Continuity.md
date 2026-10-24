# MHT CET Mathematics - Limits

## Topic 7: Continuity

**Total Questions:** 1

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x) = \dfrac{10^x + 7^x - 14^x - 5^x}{1 - \cos x}$, for $x \neq 0$ and $f(0) = k$ is continuous at $x = 0$, then the value of $k$ is _____

**Options:**

- **(A)** $\log 4\, \log \dfrac{7}{5}$
- **(B)** $\log 4\, \log \dfrac{5}{7}$
- **(C)** $\log \dfrac{5}{7}$
- **(D)** $\log 2\, \log \dfrac{5}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\log 4\, \log \dfrac{5}{7}$**

**Detailed Solution:**

Given $f(x) = \dfrac{10^x + 7^x - 14^x - 5^x}{1 - \cos x}$

Factorizing the numerator:

$10^x + 7^x - 14^x - 5^x = 5^x(2^x - 1) - 7^x(2^x - 1) = (5^x - 7^x)(2^x - 1)$

Since $f(x)$ is continuous at $x = 0$, $f(0) = \lim_{x \rightarrow 0} f(x)$.

$k = \lim_{x \rightarrow 0} \dfrac{(5^x - 7^x)(2^x - 1)}{1 - \cos x}$

Dividing the numerator and the denominator by $x^2$:

$k = \lim_{x \rightarrow 0} \dfrac{\dfrac{5^x - 7^x}{x} \cdot \dfrac{2^x - 1}{x}}{\dfrac{1 - \cos x}{x^2}}$

Using the standard limits $\lim_{x \rightarrow 0} \dfrac{a^x - b^x}{x} = \log \dfrac{a}{b}$, $\lim_{x \rightarrow 0} \dfrac{a^x - 1}{x} = \log a$, and $\lim_{x \rightarrow 0} \dfrac{1 - \cos x}{x^2} = \dfrac{1}{2}$:

$k = \dfrac{\log \left(\dfrac{5}{7}\right) \cdot \log 2}{\dfrac{1}{2}}$

$k = 2 \log 2 \cdot \log \dfrac{5}{7}$

$k = \log 4 \cdot \log \dfrac{5}{7}$

Answer: $\log 4\, \log \dfrac{5}{7}$

</details>

---

