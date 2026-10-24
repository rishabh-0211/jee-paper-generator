# MHT CET Physics - Electromagnetic Induction

## Topic 6: LR Circuit

**Total Questions:** 7

---

### Q1. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown, when the current '$i$' is $3\text{A}$ and increasing at the rate of $1\text{A/s}$ the measurement of the potential difference between A and B is $12\ \text{V}$. But when the same current $3\text{A}$ is decreasing at the rate of $1\text{A/s}$, the measured potential difference $V_{AB}$ between A and B is $6\text{V}$. The value of 'R' in the circuit is
<img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_1__q41_d1.png" />

**Options:**

- **(A)** $3\ \Omega$
- **(B)** $4\ \Omega$
- **(C)** $6\ \Omega$
- **(D)** $8\ \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3\ \Omega$**

**Detailed Solution:**

The potential difference between points A and B can be written using Kirchhoff's Voltage Law as:
$V_A - iR - L \dfrac{di}{dt} = V_B$
$\Rightarrow V_{AB} = V_A - V_B = iR + L \dfrac{di}{dt}$

Case 1: When the current is $3\text{ A}$ and increasing at $1\text{ A/s}$, we have $i = 3\text{ A}$ and $\dfrac{di}{dt} = 1\text{ A/s}$.
Given $V_{AB} = 12\text{ V}$, substituting the values:
$12 = 3R + L(1)$
$3R + L = 12$  ... (i)

Case 2: When the current is $3\text{ A}$ and decreasing at $1\text{ A/s}$, we have $i = 3\text{ A}$ and $\dfrac{di}{dt} = -1\text{ A/s}$.
Given $V_{AB} = 6\text{ V}$, substituting the values:
$6 = 3R + L(-1)$
$3R - L = 6$  ... (ii)

Adding equations (i) and (ii), we get:
$(3R + L) + (3R - L) = 12 + 6$
$6R = 18$
$R = 3\ \Omega$

Answer: $3\ \Omega$

</details>

---

### Q2. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit, if $dI/dt = -1\ \text{A/s}$ then the value of $V_{AB}$ at this instant will be
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_2__q15_d1.png" />

**Options:**

- **(A)** $30\text{V}$
- **(B)** $20\text{V}$
- **(C)** $10\text{V}$
- **(D)** $15\text{V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $15\text{V}$**

**Detailed Solution:**

Applying Kirchhoff's Voltage Law (KVL) from point A to point B:

$V_A - IR - L \dfrac{dI}{dt} - V_{\text{battery}} = V_B$

Given:
$I = 2\ \text{A}$
$R = 6\ \Omega$
$L = 3\ \text{H}$
$\dfrac{dI}{dt} = -1\ \text{A/s}$
$V_{\text{battery}} = 6\ \text{V}$ (Moving from left to right along the bottom wire, the path goes from the positive to the negative terminal, so it is a potential drop)

Substituting the values into the KVL equation:

$V_A - (2)(6) - (3)(-1) - 6 = V_B$

$V_A - 12 + 3 - 6 = V_B$

$V_A - 15 = V_B$

$V_{AB} = V_A - V_B = 15\ \text{V}$

Answer: $15\text{V}$

</details>

---

### Q3. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The following figure represents two bulbs $B_1$ and $B_2$, resistor R and an inductor L. When the switch S is turned off, which of the following statement is true?
<img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/11_april_shift_1__q13_d1.png" />

**Options:**

- **(A)** $B_1$ becomes off promptly but $B_2$ with some delay
- **(B)** $B_2$ becomes off promptly but $B_1$ with some delay
- **(C)** Both $B_1$ and $B_2$ becomes off with same delay
- **(D)** Both $B_1$ and $B_2$ becomes off promptly

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Both $B_1$ and $B_2$ becomes off with same delay**

**Detailed Solution:**

When the switch S is turned off, the main voltage source is disconnected from the circuit.

The inductor L has stored energy in its magnetic field. According to Faraday's and Lenz's laws, it opposes the sudden drop in current and acts as a source of emf.

A closed loop is formed containing the inductor L, bulb $B_2$, bulb $B_1$, and resistor R in series.

The induced current from the inductor flows through this series loop, meaning the same decaying current passes through both bulbs $B_1$ and $B_2$.

Since the current through both bulbs is identical at any instant after the switch is opened, both $B_1$ and $B_2$ become off with the same delay.

</details>

---

### Q4. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $L$ is the inductance and $R$ is the resistance then the SI unit of $\frac{L}{R}$ is

**Options:**

- **(A)** second
- **(B)** volt
- **(C)** ampere
- **(D)** per second

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) second**

**Detailed Solution:**

The time constant of an $L-R$ circuit is given by $\tau = \dfrac{L}{R}$.

Since $\tau$ represents time, the SI unit of $\dfrac{L}{R}$ is second.

Alternatively, using dimensional analysis:

The unit of inductance $L$ is Henry, which can be written as $\dfrac{\text{Volt} \cdot \text{second}}{\text{Ampere}}$.

The unit of resistance $R$ is Ohm, which is $\dfrac{\text{Volt}}{\text{Ampere}}$.

Therefore, the unit of $\dfrac{L}{R}$ is $\dfrac{\text{Volt} \cdot \text{second} / \text{Ampere}}{\text{Volt} / \text{Ampere}} = \text{second}$.

Answer: second

</details>

---

### Q5. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In the given circuit, when $S_1$ is closed, the capacitor $C$ gets full charged. Then $S_1$ is kept open and $S_2$ is closed. Hence
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BrkFXjdFYC9tTTHXDq9rNQ10aQqfPWeFjUxthtwhNDY.original.fullsize.png">

**Options:**

- **(A)** The current in the circuit is in the same direction.
- **(B)** The instantaneous current in the circuit may be $V \sqrt{\frac{C}{L}}$.
- **(C)** The energy stored in the circuit is purely in the form of magnetic energy.
- **(D)** There is no exchange of energy between inductor $L$ and capacitor $C$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The instantaneous current in the circuit may be $V \sqrt{\frac{C}{L}}$.**

**Detailed Solution:**

When $S_1$ is closed, potential difference across capacitor is $V$.
Direction of current gets reversed when $S_2$ is closed.
When $S_1$ is opened and $S_2$ is closed,
$\begin{aligned}
& \frac{1}{2} C V^2=\frac{1}{2} L I^2 \\
& \Rightarrow I=V \sqrt{\frac{C}{L}}
\end{aligned}$
Total energy oscillates between capacitor and inductor.

</details>

---

### Q6. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The network shown in the figure is part of complete circuit. If at a certain instant the current $i$ is $5 \mathrm{~A}$ and is decreasing at the rate of $10^3 \mathrm{~A} / \mathrm{s}$, then $\mathrm{V}_{\mathrm{B}}-\mathrm{V}_{\mathrm{A}}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mKUQKq7spUW7nrAHGpcfzlkt8CWUGUEWQ02WZuNYYgI.original.fullsize.png">

**Options:**

- **(A)** 15V
- **(B)** 10V
- **(C)** 5V
- **(D)** 20V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 15V**

**Detailed Solution:**

Consider the diagram below:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/a4EJrQWoq27sPsEA94nBa5rhUhS5stDKaeWYlyrylKw.original.fullsize.png">

Given, $=5 \mathrm{~A}, \mathrm{R}=1 \Omega, \mathrm{L}=5 \mathrm{mH}, \frac{\mathrm{di}}{\mathrm{dt}}=10^3 \mathrm{~A} / \mathrm{s}$
$\begin{aligned}
& V_A-i R+E-L\left(\frac{d i}{d t}\right)=V_B \\
& \Rightarrow V_A-V_B=\left(i R+L\left(\frac{d i}{d t}\right)-E\right)
\end{aligned}$
$\begin{aligned}
& \mathrm{V}_{\mathrm{A}}-\mathrm{V}_{\mathrm{B}}=5 \mathrm{~A} \times 1 \Omega+5 \times 10^{-3} \mathrm{H} \times 10^{-3} \frac{\mathrm{A}}{\mathrm{s}}-15 \mathrm{~V} \\
& \mathrm{~V}_{\mathrm{B}}-\mathrm{V}_{\mathrm{A}}=-(5+5-15) \mathrm{V}=5 \mathrm{~V}
\end{aligned}$

</details>

---

### Q7. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A circuit has self-inductance ' $L$ ' and carries a current ' $\mathrm{I}$ '. To prevent sparking when the circuit is switched off, a capacitor which can withstand potential difference ' $\mathrm{V}$ ' is used. The least capacitance is

**Options:**

- **(A)** $\frac{\mathrm{IV}}{\mathrm{L}}$
- **(B)** $\mathrm{L}\left(\frac{\mathrm{V}}{\mathrm{L}}\right)^2$
- **(C)** $\mathrm{L}\left(\frac{\mathrm{I}}{\mathrm{V}}\right)^2$
- **(D)** $\frac{\mathrm{LI}}{\mathrm{V}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{L}\left(\frac{\mathrm{I}}{\mathrm{V}}\right)^2$**

**Detailed Solution:**

The energy stored in the inductance is given by $\mathrm{U}=\frac{1}{2} \mathrm{LI}^2$ Energy stored by the capacitor is given by $\mathrm{W}=\frac{1}{2} \mathrm{CV}^2$ This energy must be transferred to the capacitor.
$$
\begin{aligned}
& \therefore \frac{1}{2} \mathrm{CV}^2=\frac{1}{2} \mathrm{LI}^2 \\
& \mathrm{C}=\mathrm{L}\left(\frac{\mathrm{I}}{\mathrm{V}}\right)^2
\end{aligned}
$$

</details>

---

