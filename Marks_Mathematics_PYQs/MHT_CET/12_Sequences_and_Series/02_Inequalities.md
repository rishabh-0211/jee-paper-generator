# MHT CET Mathematics - Sequences and Series

## Topic 2: Inequalities

**Total Questions:** 2

---

### Q1. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The minimum value of $e^{2x} + e^{-2x}$ is .......

**Options:**

- **(A)** $-2$
- **(B)** $0$
- **(C)** $1$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2$**

**Detailed Solution:**

Using the AM-GM inequality for positive real numbers $e^{2x}$ and $e^{-2x}$:

$\dfrac{e^{2x} + e^{-2x}}{2} \ge \sqrt{e^{2x} \cdot e^{-2x}}$

$\dfrac{e^{2x} + e^{-2x}}{2} \ge 1$

$e^{2x} + e^{-2x} \ge 2$

The equality holds when $e^{2x} = e^{-2x}$, which gives $x = 0$.

The minimum value is $2$.

Answer: $2$

</details>

---

### Q2. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

With usual notations, if the perimeter of a triangle is $2s$, then its maximum area is:

**Options:**

- **(A)** $\dfrac{s^2}{3}$
- **(B)** $\dfrac{\sqrt{3} s^2}{4}$
- **(C)** $\dfrac{s^2}{\sqrt{3}}$
- **(D)** $\dfrac{s^2}{3\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{s^2}{3\sqrt{3}}$**

**Detailed Solution:**

Using Heron's formula, the area of a triangle is given by $\Delta = \sqrt{s(s-a)(s-b)(s-c)}$.

To maximize $\Delta$, we need to maximize the product $(s-a)(s-b)(s-c)$.

Applying the AM-GM inequality to the positive numbers $(s-a)$, $(s-b)$, and $(s-c)$:

$\dfrac{(s-a) + (s-b) + (s-c)}{3} \ge \sqrt[3]{(s-a)(s-b)(s-c)}$

Since $a+b+c = 2s$, the sum in the numerator is $3s - (a+b+c) = 3s - 2s = s$.

$\dfrac{s}{3} \ge \sqrt[3]{(s-a)(s-b)(s-c)}$

Cubing both sides, we get:

$(s-a)(s-b)(s-c) \le \dfrac{s^3}{27}$

Substituting this maximum value back into Heron's formula:

$\Delta_{max} = \sqrt{s \left(\dfrac{s^3}{27}\right)} = \sqrt{\dfrac{s^4}{27}} = \dfrac{s^2}{3\sqrt{3}}$

Equality holds when $s-a = s-b = s-c$, which implies $a = b = c = \dfrac{2s}{3}$ (an equilateral triangle).

Answer: $\dfrac{s^2}{3\sqrt{3}}$

</details>

---

