# JEE Advanced Physics - Mechanical Properties of Fluids

## Topic 2: Efflux of liquid

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> A container of height $2$ m, length $2$ m and breadth $1$ m is made of insulating vertical walls and two large area horizontal metal plates ($M_1$ and $M_2$) which extend far beyond the vertical walls in all directions. The container is partitioned into two equal chambers with a thin insulating vertical wall. The partition wall contains a small hole of cross-sectional area $\sqrt{10}$ cm$^2$ near its bottom edge. Initially the hole is closed and the left chamber of the container is completely filled with a liquid of dielectric constant $\epsilon_r = 15$ and the right chamber is empty ($\epsilon_r = 1$). At time $t = 0$, the hole is opened and the liquid flows from the left chamber to the right chamber. In both the chambers, the space above the liquid has $\epsilon_r = 1$ and is maintained at atmospheric pressure. The schematic of the container at a time $t > 0$ is shown in the figure.
[Given: acceleration due to gravity is $10$ ms$^{-2}$.]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q33_d1.png" />

<strong>Question:</strong> The height (in m) of the liquid in left chamber at $t = 500$ s is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.25**

**Detailed Solution:**

Let $A$ be the cross-sectional area of each chamber and $a$ be the cross-sectional area of the hole.
From the given dimensions, the area of each chamber is $A = 1 \text{ m} \times 1 \text{ m} = 1 \text{ m}^2$.
The area of the hole is $a = \sqrt{10} \text{ cm}^2 = \sqrt{10} \times 10^{-4} \text{ m}^2$.
Let $h_1$ and $h_2$ be the heights of the liquid in the left and right chambers at time $t$, respectively.
By conservation of volume, $A h_1 + A h_2 = A H$, where $H = 2$ m is the initial height of the liquid in the left chamber.
$\Rightarrow h_1 + h_2 = 2$

The velocity of efflux through the hole is given by Torricelli's law:
$v = \sqrt{2g(h_1 - h_2)}$

The rate of flow of the liquid is:
$-A \dfrac{dh_1}{dt} = a \sqrt{2g(h_1 - h_2)}$

Substitute $h_2 = 2 - h_1$ into the equation:
$-A \dfrac{dh_1}{dt} = a \sqrt{2g(2h_1 - 2)}$

Let $y = 2h_1 - 2$. Then $dy = 2 dh_1$, which gives $dh_1 = \dfrac{dy}{2}$.
The differential equation becomes:
$-\dfrac{A}{2} \dfrac{dy}{dt} = a \sqrt{2gy}$
$\Rightarrow \dfrac{dy}{\sqrt{y}} = -\dfrac{2a\sqrt{2g}}{A} dt$

Integrating both sides from $t = 0$ to $t = 500$ s. At $t = 0$, $h_1 = 2$ m, so $y(0) = 2(2) - 2 = 2$ m.
$\int_{2}^{y} y^{-1/2} dy = -\dfrac{2a\sqrt{2g}}{A} \int_{0}^{500} dt$
$[2\sqrt{y}]_{2}^{y} = -\dfrac{2 \times (\sqrt{10} \times 10^{-4}) \times \sqrt{20}}{1} \times 500$
$2\sqrt{y} - 2\sqrt{2} = -1000 \times 10^{-4} \times \sqrt{200}$
$2\sqrt{y} - 2\sqrt{2} = -0.1 \times 10\sqrt{2}$
$2\sqrt{y} - 2\sqrt{2} = -\sqrt{2}$
$2\sqrt{y} = \sqrt{2}$
$\sqrt{y} = \dfrac{\sqrt{2}}{2}$

Squaring both sides, we get:
$y = 0.5$

Since $y = 2h_1 - 2$, we have:
$2h_1 - 2 = 0.5$
$2h_1 = 2.5$
$h_1 = 1.25 \text{ m}$

Answer: $1.25$

</details>

---

