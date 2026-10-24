# JEE Main Mathematics - Complex Number

## Topic 7: De Moivres Theorem

**Total Questions:** 2

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $S = \{z \in \mathbb{C} : z^2 + \sqrt{6}\,iz - 3 = 0\}$. Then $\sum\limits_{z \in S} z^8$ is equal to :

**Options:**

- **(A)** $162$
- **(B)** $184$
- **(C)** $262$
- **(D)** $324$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $162$**

**Detailed Solution:**

Given equation is $z^2 + \sqrt{6}iz - 3 = 0$.

Rearranging the terms, we get $z^2 - 3 = -\sqrt{6}iz$.

Squaring both sides, we obtain:

$(z^2 - 3)^2 = (-\sqrt{6}iz)^2$

$z^4 - 6z^2 + 9 = -6z^2$

$z^4 + 9 = 0$

$z^4 = -9$

Squaring again, we get:

$(z^4)^2 = (-9)^2$

$z^8 = 81$

Since the given equation is a quadratic in $z$, it has two roots, say $z_1$ and $z_2$.

The discriminant of the quadratic equation is $\Delta = (\sqrt{6}i)^2 - 4(1)(-3) = -6 + 12 = 6 \neq 0$, which means the roots are distinct.

Thus, the set $S$ contains two distinct elements $z_1$ and $z_2$.

For each root, $z^8 = 81$.

Therefore, $\sum\limits_{z \in S} z^8 = z_1^8 + z_2^8 = 81 + 81 = 162$.

Answer: $162$

</details>

---

### Q2. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $z=\frac{\sqrt{3}}{2}+\frac{i}{2}, i=\sqrt{-1}$, then $\left(z^{201}-i\right)^{8}$ is equal to

**Options:**

- **(A)** 1
- **(B)** 256
- **(C)** -1
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 256**

**Detailed Solution:**

$z = \frac{\sqrt{3}}{2} + \frac{i}{2} = e^{i\pi/6}$.
$z^{201} = e^{i \cdot 201\pi/6} = e^{i \cdot 33.5\pi} = e^{i(33\pi + \pi/2)}$.
Since $e^{i \cdot 33\pi} = e^{i\pi} = -1$, we get $z^{201} = -1 \cdot e^{i\pi/2} = -i$.
$z^{201} - i = -i - i = -2i$.
$(z^{201} - i)^8 = (-2i)^8 = 2^8 \cdot i^8 = 256 \cdot 1 = 256$.

</details>

---

