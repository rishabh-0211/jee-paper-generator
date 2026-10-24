# JEE Advanced Physics - Thermodynamics

## Topic 3: Heat Engine, Refrigerator andSecond Law of Thermodynamics

**Total Questions:** 1

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `2`

As shown in the figure, five Carnot engines, each with efficiency $\eta$ and same number of cycles per unit time, are operating between six heat reservoirs. The amount of heat released per cycle by one engine is completely absorbed by the next engine. Consider $Q_0$ to be the amount of heat absorbed per cycle by the first engine and $W$ as the amount of total work done by all the engines per cycle, then the net efficiency of the system is found to be $\eta_{\text{net}} = \dfrac{W}{Q_0} = \dfrac{211}{243}$. The value of $\eta$ is:
<img style="width: 200px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q26_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.33**

**Detailed Solution:**

Let $Q_0$ be the heat absorbed by the first engine and $Q_1$ be the heat rejected.

The efficiency of the first engine is $\eta = 1 - \dfrac{Q_1}{Q_0} \Rightarrow Q_1 = Q_0(1 - \eta)$

Similarly, for the second engine, the heat rejected is $Q_2 = Q_1(1 - \eta) = Q_0(1 - \eta)^2$

Following this pattern, for the $5^{\text{th}}$ engine, the heat rejected is $Q_5 = Q_0(1 - \eta)^5$

The total work done by all five engines is $W = W_1 + W_2 + W_3 + W_4 + W_5 = (Q_0 - Q_1) + (Q_1 - Q_2) + \dots + (Q_4 - Q_5) = Q_0 - Q_5$

The net efficiency of the system is $\eta_{\text{net}} = \dfrac{W}{Q_0} = \dfrac{Q_0 - Q_5}{Q_0} = 1 - \dfrac{Q_5}{Q_0}$

Substituting the value of $Q_5$, we get $\eta_{\text{net}} = 1 - (1 - \eta)^5$

Given $\eta_{\text{net}} = \dfrac{211}{243}$

$1 - (1 - \eta)^5 = \dfrac{211}{243}$

$(1 - \eta)^5 = 1 - \dfrac{211}{243} = \dfrac{32}{243}$

$(1 - \eta)^5 = \left(\dfrac{2}{3}\right)^5$

$1 - \eta = \dfrac{2}{3}$

$\eta = \dfrac{1}{3}$

Answer: $0.33$

</details>

---

