# MHT CET Mathematics - Quadratic Equation

## Topic 4: Range of Quadratic Function

**Total Questions:** 2

---

### Q1. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A ball is thrown in the air. Its height at any time $t$ is given by $h = 3 + 14t - 5t^2$, then the maximum height it can reach

**Options:**

- **(A)** $12.9$
- **(B)** $12.8$
- **(C)** $12.7$
- **(D)** $12.6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12.8$**

**Detailed Solution:**

Given $h = 3 + 14t - 5t^2$

Differentiating with respect to $t$:

$\dfrac{dh}{dt} = 14 - 10t$

For maximum height, $\dfrac{dh}{dt} = 0$:

$14 - 10t = 0 \Rightarrow t = 1.4$

Substituting $t = 1.4$ in the equation for $h$:

$h_{max} = 3 + 14(1.4) - 5(1.4)^2$

$h_{max} = 3 + 19.6 - 5(1.96)$

$h_{max} = 22.6 - 9.8 = 12.8$

Answer: $12.8$

</details>

---

### Q2. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of roots of the equation, $(81)^{\sin ^2 x}+(81)^{\cos ^2 x}=30$ in the interval $[0, \pi]$, is equal to

**Options:**

- **(A)** 4
- **(B)** 8
- **(C)** 3
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

Given equation is $(81)^{\sin^2 x} + (81)^{\cos^2 x} = 30$

Since $\cos^2 x = 1 - \sin^2 x$, the equation can be written as:

$(81)^{\sin^2 x} + (81)^{1 - \sin^2 x} = 30$

$(81)^{\sin^2 x} + \dfrac{81}{(81)^{\sin^2 x}} = 30$

Let $y = (81)^{\sin^2 x}$. Substituting this in the equation:

$y + \dfrac{81}{y} = 30$

$y^2 - 30y + 81 = 0$

$(y - 27)(y - 3) = 0$

$y = 27$ or $y = 3$

Case 1: $y = 27$

$(81)^{\sin^2 x} = 27$

$3^{4\sin^2 x} = 3^3$

$4\sin^2 x = 3 \Rightarrow \sin^2 x = \dfrac{3}{4}$

Since $x \in [0, \pi]$, $\sin x \ge 0$, which gives $\sin x = \dfrac{\sqrt{3}}{2}$

$x = \dfrac{\pi}{3}, \dfrac{2\pi}{3}$

Case 2: $y = 3$

$(81)^{\sin^2 x} = 3$

$3^{4\sin^2 x} = 3^1$

$4\sin^2 x = 1 \Rightarrow \sin^2 x = \dfrac{1}{4}$

Since $x \in [0, \pi]$, $\sin x \ge 0$, which gives $\sin x = \dfrac{1}{2}$

$x = \dfrac{\pi}{6}, \dfrac{5\pi}{6}$

The roots in the interval $[0, \pi]$ are $\dfrac{\pi}{6}, \dfrac{\pi}{3}, \dfrac{2\pi}{3}, \dfrac{5\pi}{6}$.

The number of roots is $4$.

Answer: 4

</details>

---

