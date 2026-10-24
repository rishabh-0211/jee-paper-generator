# MHT CET Physics - Semiconductors

## Topic 3: Diodes

**Total Questions:** 81

---

### Q1. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

To use Zener diode of maximum power rating $1.0$ W as a $4.0$ V stabilized power supply, the maximum current flowing through Zener diode will

**Options:**

- **(A)** $0.25$ mA
- **(B)** $25$ mA
- **(C)** $250$ mA
- **(D)** $2500$ mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $250$ mA**

**Detailed Solution:**

Given maximum power rating $P_{max} = 1.0$ W and Zener voltage $V_Z = 4.0$ V.

The maximum current $I_{max}$ flowing through the Zener diode is given by the relation:

$P_{max} = V_Z \times I_{max}$

$I_{max} = \dfrac{P_{max}}{V_Z}$

$I_{max} = \dfrac{1.0}{4.0} = 0.25$ A

$I_{max} = 0.25 \times 1000$ mA $= 250$ mA

Answer: $250$ mA

</details>

---

### Q2. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the following circuit, the current through the Zener diode is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/19_may_shift_1__q50_d1.png" />

**Options:**

- **(A)** $5.00 \text{ mA}$
- **(B)** $6.25 \text{ mA}$
- **(C)** $11.25 \text{ mA}$
- **(D)** $16.25 \text{ mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6.25 \text{ mA}$**

**Detailed Solution:**

First, we check if the Zener diode is in the breakdown region. The voltage across $R_2$ without the Zener diode is:

$V' = \dfrac{R_2}{R_1 + R_2} \times V = \dfrac{1800}{800 + 1800} \times 18 = \dfrac{1800}{2600} \times 18 \approx 12.46 \text{ V}$

Since $V' > V_Z$ ($12.46 \text{ V} > 9 \text{ V}$), the Zener diode is in the breakdown region and the voltage across it is fixed at $V_Z = 9 \text{ V}$.

The voltage across resistor $R_1$ is:

$V_{R1} = V - V_Z = 18 \text{ V} - 9 \text{ V} = 9 \text{ V}$

The total current $I$ flowing through $R_1$ is:

$I = \dfrac{V_{R1}}{R_1} = \dfrac{9}{800} \text{ A} = 11.25 \text{ mA}$

The current flowing through resistor $R_2$ is:

$I_{R2} = \dfrac{V_Z}{R_2} = \dfrac{9}{1800} \text{ A} = 5 \text{ mA}$

By Kirchhoff's current law, the current through the Zener diode $I_Z$ is:

$I_Z = I - I_{R2} = 11.25 \text{ mA} - 5 \text{ mA} = 6.25 \text{ mA}$

Answer: $6.25 \text{ mA}$

</details>

---

### Q3. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The Zener diode has reverse breakdown voltage $V_Z$. The current through the load resistance $R_L$ is $I_L$. The current through Zener diode is
($V_0$ = Input voltage , $R_S$ = Series resistance)

**Options:**

- **(A)** $\dfrac{(V_0 - V_Z)}{R_S}$
- **(B)** $\dfrac{(V_0 - V_Z)}{R_L}$
- **(C)** $\dfrac{V_Z}{R_L}$
- **(D)** $\left(\dfrac{V_0 - V_Z}{R_S}\right) - I_L$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\dfrac{V_0 - V_Z}{R_S}\right) - I_L$**

**Detailed Solution:**

The voltage across the Zener diode in breakdown region is $V_Z$.

The voltage drop across the series resistor $R_S$ is $V_0 - V_Z$.

The current through the series resistor is $I_S = \dfrac{V_0 - V_Z}{R_S}$.

Applying Kirchhoff's current law at the junction, the total current $I_S$ is the sum of the Zener current $I_Z$ and the load current $I_L$.

$I_S = I_Z + I_L$

$I_Z = I_S - I_L$

$I_Z = \left(\dfrac{V_0 - V_Z}{R_S}\right) - I_L$

Answer: $\left(\dfrac{V_0 - V_Z}{R_S}\right) - I_L$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If an alternating voltage is applied across a diode in series with a load resistance then

**Options:**

- **(A)** a d.c. voltage appears across load
- **(B)** an a.c. voltage appears across load
- **(C)** a pulsating voltage appears across load
- **(D)** no voltage appears across load

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a pulsating voltage appears across load**

**Detailed Solution:**

When an alternating voltage is applied across a diode in series with a load resistance, the circuit acts as a half-wave rectifier.

During the positive half-cycle of the input a.c. voltage, the diode is forward-biased and conducts current.

During the negative half-cycle, the diode is reverse-biased and does not conduct current.

As a result, the current flows through the load resistance in only one direction, but its magnitude varies with time.

Thus, the voltage across the load resistance is unidirectional and pulsating in nature. Therefore, a pulsating voltage appears across the load.

Answer: a pulsating voltage appears across load

</details>

---

### Q5. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the middle of the depletion region of reversed biased p-n junction the

**Options:**

- **(A)** electric field is zero
- **(B)** potential is infinite
- **(C)** electric field is maximum
- **(D)** potential is zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) electric field is maximum**

**Detailed Solution:**

In a p-n junction, the depletion region contains immobile positive donor ions on the n-side and negative acceptor ions on the p-side.

According to Gauss's law, $\dfrac{dE}{dx} = \dfrac{\rho}{\varepsilon}$. The electric field is directed from the n-side to the p-side.

The magnitude of the electric field increases as we move from the edges of the depletion region towards the junction, reaching its maximum value exactly at the metallurgical junction (the middle of the depletion region).

Therefore, the electric field is maximum in the middle of the depletion region.

Answer: electric field is maximum

</details>

---

### Q6. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The forward biased diode connection is

**Options:**

- **(A)** <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d1.png" />
- **(B)** <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d2.png" />
- **(C)** <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d3.png" />
- **(D)** <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d4.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d1.png" />**

**Detailed Solution:**

A p-n junction diode is forward biased when its p-side (anode) is at a higher potential than its n-side (cathode), i.e., $V_p > V_n$.

Let us check the potential difference for each given option:

For the first circuit:
$V_p = +2\text{ V}$ and $V_n = -2\text{ V}$
Since $V_p > V_n$, the diode is forward biased.

For the second circuit:
$V_p = +2\text{ V}$ and $V_n = +4\text{ V}$
Since $V_p < V_n$, the diode is reverse biased.

For the third circuit:
$V_p = -3\text{ V}$ and $V_n = -3\text{ V}$
Since $V_p = V_n$, the diode is unbiased.

For the fourth circuit:
$V_p = -2\text{ V}$ and $V_n = +2\text{ V}$
Since $V_p < V_n$, the diode is reverse biased.

Therefore, only the first circuit represents a forward biased diode.

Answer: <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q10_d1.png" />

</details>

---

### Q7. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The circuit shown contains two ideal diodes $D_1$ and $D_2$. If a cell of e.m.f. $3$V and negligible internal resistance is connected, then the current through $70\,\Omega$ resistance in ampere is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/12_may_shift_2__q45_d1_v2.png" />

**Options:**

- **(A)** $0.01$
- **(B)** $0.02$
- **(C)** $0.03$
- **(D)** $0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.03$**

**Detailed Solution:**

From the circuit diagram, the positive terminal of the $3\text{ V}$ battery is on the left.

Diode $D_1$ is reverse-biased (n-side connected to the positive terminal) and acts as an open circuit.

Diode $D_2$ is forward-biased (p-side connected to the positive terminal) and acts as a closed circuit since it is an ideal diode.

Current flows only through the branch containing $D_2$. The circuit simplifies to the $30\ \Omega$ and $70\ \Omega$ resistors connected in series.

The equivalent resistance of the circuit is $R_{eq} = 30 + 70 = 100\ \Omega$.

Using Ohm's law, the current through the $70\ \Omega$ resistance is:

$I = \dfrac{V}{R_{eq}} = \dfrac{3}{100} = 0.03\text{ A}$

</details>

---

### Q8. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In one branch, $40\,\Omega$ resistance and a p-n junction diode are connected in series and in another branch, $40\,\Omega$ resistance is connected. Both the branches are connected in parallel to each other. The total resistance of the circuit when a) diode is forward biased and when b) diode is reverse biased respectively are {consider the p-n junction diode as an ideal diode}

**Options:**

- **(A)** $40\,\Omega$ and $20\,\Omega$
- **(B)** $60\,\Omega$ and $30\,\Omega$
- **(C)** $20\,\Omega$ and $40\,\Omega$
- **(D)** $30\,\Omega$ and $60\,\Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $20\,\Omega$ and $40\,\Omega$**

**Detailed Solution:**

When the ideal p-n junction diode is forward biased, it offers zero resistance. The resistance of the first branch is $40\,\Omega$.

Since the two branches are in parallel, the equivalent resistance $R_{eq}$ is given by:

$R_{eq} = \dfrac{40 \times 40}{40 + 40} = 20\,\Omega$

When the ideal p-n junction diode is reverse biased, it offers infinite resistance. The first branch acts as an open circuit and no current flows through it.

The equivalent resistance of the circuit is simply the resistance of the second branch:

$R_{eq} = 40\,\Omega$

The total resistance of the circuit in forward and reverse bias respectively are $20\,\Omega$ and $40\,\Omega$.

Answer: $20\,\Omega$ and $40\,\Omega$

</details>

---

### Q9. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The depletion region of p-n junction

**Options:**

- **(A)** increases if reverse biased.
- **(B)** increases if forward biased.
- **(C)** decreases if reverse biased.
- **(D)** remains same in reverse and forward biasing.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increases if reverse biased.**

**Detailed Solution:**

In a p-n junction, when it is reverse biased, the positive terminal of the battery is connected to the n-type region and the negative terminal to the p-type region.

The applied reverse voltage is in the same direction as the built-in potential barrier. This increases the effective potential barrier across the junction.

As a result, the majority charge carriers are pulled away from the junction, which causes the width of the depletion region to increase.

Conversely, during forward biasing, the applied voltage opposes the built-in potential, causing the depletion region to decrease.

Answer: increases if reverse biased.

</details>

---

### Q10. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the following electrical circuit, the reading in the milliammeter is
(Take knee voltage of silicon diode $= 0.7$ V)
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_2__q10_d1.png" />

**Options:**

- **(A)** $25.5$ mA
- **(B)** $21.5$ mA
- **(C)** $18.5$ mA
- **(D)** $15.8$ mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $21.5$ mA**

**Detailed Solution:**

In the given circuit, the p-side of the silicon diode is connected to the positive terminal of the battery, so it is forward-biased.

The effective voltage across the resistor is the battery voltage minus the knee voltage of the diode:
$V_{\text{eff}} = V - V_k$
$V_{\text{eff}} = 5 - 0.7 = 4.3\text{ V}$

The current in the circuit is given by Ohm's law:
$I = \dfrac{V_{\text{eff}}}{R}$
$I = \dfrac{4.3}{200}\text{ A}$
$I = 0.0215\text{ A}$

Converting to milliamperes:
$I = 21.5\text{ mA}$

Answer: $21.5$ mA

</details>

---

### Q11. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A diode and resistance are connected as shown in figures.
<img style="width: 250px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_1__q13_d1.png" />
Out of the following statements, which one is true?
Diode in
A) fig (1) and fig (2) are both forward biased.
B) fig (1) and fig (2) are both reverse biased.
C) fig (1) is forward biased and in fig (2) is reverse biased.
D) fig (1) is reverse biased and in fig (2) is forward biased.

**Options:**

- **(A)** D
- **(B)** B
- **(C)** A
- **(D)** C

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) D**

**Detailed Solution:**

A diode is said to be forward biased if the potential at its p-side is greater than the potential at its n-side ($V_p > V_n$). It is reverse biased if the potential at its p-side is less than the potential at its n-side ($V_p < V_n$).

In Figure 1:
The p-side of diode $D_1$ is connected to $-5\text{ V}$ and the n-side is connected to $-3\text{ V}$ through resistor $R_1$.
Since $-5\text{ V} < -3\text{ V}$, the p-side is at a lower potential than the n-side.
Therefore, diode $D_1$ is reverse biased.

In Figure 2:
The p-side of diode $D_2$ is connected to $0\text{ V}$ and the n-side is connected to $-4\text{ V}$ through resistor $R_2$.
Since $0\text{ V} > -4\text{ V}$, the p-side is at a higher potential than the n-side.
Therefore, diode $D_2$ is forward biased.

Thus, the diode in fig (1) is reverse biased and in fig (2) is forward biased.

Answer: D

</details>

---

### Q12. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

When the Zener diode is used as a voltage regulator, it is connected in

**Options:**

- **(A)** forward bias and in parallel with load.
- **(B)** reverse bias and in series with load.
- **(C)** forward bias and in series with load.
- **(D)** reverse bias and in parallel with load.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) reverse bias and in parallel with load.**

**Detailed Solution:**

A Zener diode is used as a voltage regulator to provide a constant voltage across a load.

To operate in the Zener breakdown region, the diode must be connected in reverse bias.

To ensure the voltage across the load remains constant and equal to the Zener voltage, it is connected in parallel with the load.

Answer: reverse bias and in parallel with load.

</details>

---

### Q13. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown in figure all the three diodes D1, D2, D3 have forward resistance $50\ \Omega$ each and infinite backward resistance. If the battery voltage is 5V, the current through $100\ \Omega$ resistance is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q6_d1.png" />

**Options:**

- **(A)** $60$ mA
- **(B)** $30$ mA
- **(C)** $20$ mA
- **(D)** $10$ mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $30$ mA**

**Detailed Solution:**

The positive terminal of the $5 \text{ V}$ battery is connected to the left side of the circuit, making diodes D1 and D2 forward-biased and diode D3 reverse-biased.

Since D3 has infinite backward resistance, it acts as an open circuit and no current flows through its branch.

The forward resistance of D1 and D2 is $50 \Omega$ each. The resistance of the top branch is $R_1 = 50 + 150 = 200 \Omega$.

The resistance of the middle branch is $R_2 = 50 + 50 = 100 \Omega$.

These two branches are in parallel, so their equivalent resistance $R_p$ is:

$R_p = \dfrac{R_1 R_2}{R_1 + R_2} = \dfrac{200 \times 100}{200 + 100} = \dfrac{20000}{300} = \dfrac{200}{3} \Omega$

The $100 \Omega$ resistor is in series with this parallel combination. The total equivalent resistance of the circuit is:

$R_{eq} = R_p + 100 = \dfrac{200}{3} + 100 = \dfrac{500}{3} \Omega$

The total current $I$ from the battery, which is the current flowing through the $100 \Omega$ resistor, is:

$I = \dfrac{V}{R_{eq}} = \dfrac{5}{\dfrac{500}{3}} = \dfrac{15}{500} \text{ A}$

$I = 0.03 \text{ A} = 30 \text{ mA}$

</details>

---

### Q14. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the diagram shown, the resistance between points A and B is '$R_1$' when an ideal diode D is forward biased and is '$R_2$' when ideal diode D is reverse biased. The ratio $R_1 / R_2$ is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/14_april_shift_2__q23_d1.png" />

**Options:**

- **(A)** $2$
- **(B)** $1$
- **(C)** $\dfrac{1}{2}$
- **(D)** $\dfrac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}$**

**Detailed Solution:**

When the ideal diode D is forward biased, it acts as a short circuit with zero resistance.

The circuit then consists of two $30\ \Omega$ resistors connected in parallel between points A and B.

The equivalent resistance $R_1$ is given by:

$R_1 = \dfrac{30 \times 30}{30 + 30} = 15\ \Omega$

When the ideal diode D is reverse biased, it acts as an open circuit with infinite resistance.

No current flows through the top branch, so the equivalent resistance $R_2$ is simply the resistance of the bottom branch.

$R_2 = 30\ \Omega$

The ratio $\dfrac{R_1}{R_2}$ is:

$\dfrac{R_1}{R_2} = \dfrac{15}{30} = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q15. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a p-n junction diode, breakdown voltage occurs when

**Options:**

- **(A)** reverse bias is decreased
- **(B)** reverse bias is not changed
- **(C)** reverse-bias is increased
- **(D)** forward bias is increased

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) reverse-bias is increased**

**Detailed Solution:**

In a p-n junction diode, when the reverse bias voltage is increased, the width of the depletion region and the electric field across it increase.

At a sufficiently high reverse bias voltage, the electric field becomes strong enough to break covalent bonds (Zener breakdown) or accelerate minority carriers to cause impact ionization (avalanche breakdown).

This leads to a sudden and sharp increase in the reverse current, which is known as the breakdown voltage. Therefore, breakdown occurs when the reverse bias is increased.

Answer: reverse-bias is increased

</details>

---

### Q16. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If p-n junction diode is forward biased then

**Options:**

- **(A)** width of depletion layer decreases.
- **(B)** width of depletion layer increases.
- **(C)** barrier voltage increases
- **(D)** electric conduction is not possible

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) width of depletion layer decreases.**

**Detailed Solution:**

When a p-n junction diode is forward biased, the positive terminal of the external voltage source is connected to the p-side and the negative terminal to the n-side.

The applied forward voltage opposes the built-in potential barrier, reducing the effective barrier voltage.

This external electric field pushes the majority charge carriers (holes in the p-region and electrons in the n-region) towards the junction.

As the carriers move towards the junction, they neutralize some of the immobile ions, which causes the width of the depletion layer to decrease.

This allows majority carriers to cross the junction easily, facilitating electric conduction.

Answer: width of depletion layer decreases.

</details>

---

### Q17. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Choose the correct statement about Zener diode:

**Options:**

- **(A)** It works as a voltage regulator in reverse bias and behaves like simple pn junction diode in forward bias.
- **(B)** It works as a voltage regulator in both forward and reverse bias.
- **(C)** It works a voltage regulator only in forward bias.
- **(D)** It works as a voltage regulator in forward bias and behaves like simple pn junction diode in reverse bias.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) It works as a voltage regulator in reverse bias and behaves like simple pn junction diode in forward bias.**

**Detailed Solution:**

A Zener diode is a heavily doped p-n junction diode designed to operate in the reverse breakdown region.

In reverse bias, when the applied voltage reaches the Zener breakdown voltage, the voltage across the diode remains constant for a wide range of currents. This property allows it to be used as a voltage regulator.

In forward bias, a Zener diode behaves exactly like a standard p-n junction diode, allowing current to flow when the forward voltage exceeds the barrier potential.

Answer: It works as a voltage regulator in reverse bias and behaves like simple pn junction diode in forward bias.

</details>

---

### Q18. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following figure represents forward bias diode?

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/hzbtnzihjGwCLy-eFwktZjJ_APQmx8TnjKfKwZPs90Y.original.fullsize.png">

**Options:**

- **(A)** A
- **(B)** C
- **(C)** D
- **(D)** B

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A**

**Detailed Solution:**

A p-n junction diode is said to be forward-biased when its p-side (anode) is at a higher potential than its n-side (cathode), i.e., $V_p > V_n$.

Let us check the potentials for each given figure:
In figure (A), $V_p = 0\text{ V}$ and $V_n = -4\text{ V}$. Since $0\text{ V} > -4\text{ V}$, the diode is forward-biased.
In figure (B), $V_p = -4\text{ V}$ and $V_n = -3\text{ V}$. Since $-4\text{ V} < -3\text{ V}$, the diode is reverse-biased.
In figure (C), $V_p = -2\text{ V}$ and $V_n = +2\text{ V}$. Since $-2\text{ V} < +2\text{ V}$, the diode is reverse-biased.
In figure (D), $V_p = 3\text{ V}$ and $V_n = 5\text{ V}$. Since $3\text{ V} < 5\text{ V}$, the diode is reverse-biased.

Therefore, only figure (A) represents a forward-biased diode.

Answer: A

</details>

---

### Q19. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

When the zener diode is used as voltage regulator, it is connected in

**Options:**

- **(A)** reverse bias and in parallel with load.
- **(B)** reverse bias and in series with load.
- **(C)** forward bias and in series with load.
- **(D)** forward bias and in parallel with load.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) reverse bias and in parallel with load.**

**Detailed Solution:**

A Zener diode is used as a voltage regulator to provide a constant voltage across a load. To achieve this, it is operated in the breakdown region, which requires it to be connected in reverse bias.

To maintain a constant voltage across the load, the Zener diode must be connected in parallel with the load resistance.

Answer: reverse bias and in parallel with load.

</details>

---

### Q20. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If p-n junction diode is forward biased, then

**Options:**

- **(A)** electric conduction is not possible.
- **(B)** width of depletion layer decreases.
- **(C)** width of depletion layer increases.
- **(D)** barrier voltage increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) width of depletion layer decreases.**

**Detailed Solution:**

When a p-n junction diode is forward biased, the positive terminal of the external voltage source is connected to the p-region and the negative terminal to the n-region.

The applied forward voltage opposes the built-in potential barrier, which reduces the effective barrier voltage.

As a result of the decreased potential barrier, the width of the depletion layer decreases, allowing majority charge carriers to easily cross the junction and conduct electricity.

Answer: width of depletion layer decreases.

</details>

---

### Q21. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Applying forward bias to p-n junction, the potential barrier

**Options:**

- **(A)** increases
- **(B)** decreases
- **(C)** remains unchanged
- **(D)** becomes zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) decreases**

**Detailed Solution:**

When a p-n junction is forward biased, the positive terminal of the external voltage source is connected to the p-region and the negative terminal to the n-region.

The applied external voltage opposes the built-in potential barrier of the junction. As a result, the effective potential barrier across the junction decreases, which reduces the width of the depletion layer and allows majority charge carriers to flow across the junction easily.

Answer: decreases

</details>

---

### Q22. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In which of the following figures, the p. n. junction diode is reverse biased?
<img style="width:700px;" src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/7GMGiNAfAGpEVGTq2N1cvnyQlm4c8a00381tC4HjiFU.original.fullsize.png">

**Options:**

- **(A)** (c)
- **(B)** (d)
- **(C)** (b)
- **(D)** (a)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) (b)**

**Detailed Solution:**

A p-n junction diode is reverse biased when the potential at the p-side is lower than the potential at the n-side ($V_p < V_n$).

For figure (a): $V_p = +6\text{ V}$, $V_n = -2\text{ V} \Rightarrow V_p > V_n$ (Forward biased).

For figure (b): $V_p = -5\text{ V}$, $V_n = +3\text{ V} \Rightarrow V_p < V_n$ (Reverse biased).

For figure (c): $V_p = 0\text{ V}$, $V_n = -10\text{ V} \Rightarrow V_p > V_n$ (Forward biased).

For figure (d): $V_p = +6\text{ V}$, $V_n = 0\text{ V} \Rightarrow V_p > V_n$ (Forward biased).

Therefore, the diode in figure (b) is reverse biased.

Answer: (b)

</details>

---

### Q23. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

I-V characteristics of LED is shown correctly by graph
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/JguW6hC3aDvX9aOcvWU91vlY_0-FOZnIos_ysxCyfYE.original.fullsize.png">

**Options:**

- **(A)** d
- **(B)** b
- **(C)** a
- **(D)** c

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) b**

**Detailed Solution:**

An LED (Light Emitting Diode) is a heavily doped p-n junction diode that operates in forward bias.

In forward bias, the current remains very small until the applied voltage exceeds the threshold (cut-in) voltage of the diode. Beyond this threshold voltage, the forward current increases rapidly with the applied voltage.

This behavior is correctly depicted in graph (b), which shows the forward bias I-V characteristics in the first quadrant.

For context:
- Graph (a) represents a typical p-n junction diode or Zener diode showing both forward and reverse characteristics.
- Graph (c) represents a solar cell (operating in the fourth quadrant).
- Graph (d) represents the magnitude of a photodiode's reverse bias characteristics.

Answer: b

</details>

---

### Q24. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

I - V characteristics of photodiode for different illumination intensities $\mathrm{I}_1, \mathrm{I}_2, \mathrm{I}_3$ and $\mathrm{I}_4$ are drawn as follows. Then the maximum intensity among them is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/58b8l5375saVonUdNa-GyZDcAGZHBBfrm_2xuoisuLg.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{I}_1$
- **(B)** $\mathrm{I}_2$
- **(C)** $\mathrm{I}_3$
- **(D)** $\mathrm{I}_4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{I}_4$**

**Detailed Solution:**

In a photodiode, the magnitude of the reverse saturation current (photocurrent) is directly proportional to the intensity of incident light.

The given graph shows the I-V characteristics in reverse bias for different illumination intensities. The magnitude of the reverse current is represented by the downward displacement from the horizontal axis.

From the graph, the magnitude of the reverse current is maximum for the curve labeled $\mathrm{I}_4$.

Therefore, the intensity of illumination is maximum for $\mathrm{I}_4$, which means $\mathrm{I}_4 > \mathrm{I}_3 > \mathrm{I}_2 > \mathrm{I}_1$.

Answer: $\mathrm{I}_4$

</details>

---

### Q25. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The graph given below represents I - V characteristics of zener diode. The part of the characteristics curve that is most relevant for its operation as a voltage regulator is
<img width=300px src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/L9vbmjHOuf68DSDth0OhbhgaSlA09eaVbwVYNuiVlj0.original.fullsize.png">

**Options:**

- **(A)** ab
- **(B)** bc
- **(C)** cd
- **(D)** de

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) de**

**Detailed Solution:**

A Zener diode is used as a voltage regulator when it is operated in the reverse breakdown region.

In the given I-V characteristics graph, the reverse bias operation is shown in the third quadrant.

The region 'cd' represents the reverse leakage current before the breakdown occurs.

The region 'de' represents the reverse breakdown region (Zener breakdown), where the voltage across the diode remains almost constant even for large changes in the reverse current.

Therefore, the part 'de' of the characteristics curve is most relevant for its operation as a voltage regulator.

Answer: de

</details>

---

### Q26. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If an alternating voltage is applied across a p-n junction diode in series with a load then

**Options:**

- **(A)** no voltage appears across load.
- **(B)** a pulsating voltage appears across load.
- **(C)** an a.c. voltage appears across load.
- **(D)** a d.c. voltage appears across load which is not pulsating.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a pulsating voltage appears across load.**

**Detailed Solution:**

When an alternating voltage is applied across a p-n junction diode in series with a load, the circuit acts as a half-wave rectifier.

During the positive half-cycle of the a.c. input, the diode is forward-biased and conducts current through the load.

During the negative half-cycle, the diode is reverse-biased and does not conduct current.

As a result, current flows through the load in only one direction and only during half of each cycle. This produces a unidirectional but varying voltage across the load, which is known as a pulsating voltage.

Answer: a pulsating voltage appears across load.

</details>

---

### Q27. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the internal resistance of cell is negligible then current flowing through the circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/OYcKUB_eRueiYfwomS8cyc45GNetArJ0VHunGvbKuTU.original.fullsize.png">

**Options:**

- **(A)** 0.04 A
- **(B)** 0.06 A
- **(C)** 0.08 A
- **(D)** 0.10 A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.10 A**

**Detailed Solution:**

From the given circuit, the positive terminal of the $5\text{ V}$ battery is on the left. Thus, current flows from left to right through the parallel branches.

Diode $D_1$ is forward-biased as its p-side is connected to the higher potential (left side).

Diode $D_2$ is reverse-biased as its n-side is connected to the higher potential. No current flows through the top branch.

The effective circuit is a series combination of the $20 \Omega$ resistor, the forward-biased diode $D_1$, the $30 \Omega$ resistor, and the $5\text{ V}$ battery.

Total resistance, $R = 20 \Omega + 30 \Omega = 50 \Omega$.

Current, $I = \dfrac{V}{R} = \dfrac{5}{50} = 0.10\text{ A}$.

Answer: 0.10 A

</details>

---

### Q28. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the following circuit shown in figure, three diodes are connected each with forward resistance $40 \Omega$ and infinite backward resistance. The current through $100 \Omega$ resistance is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/-iyeBtLRt17RPDWdc6vQ1fdrWBqGXIzxQe5uUiJzwrM.original.fullsize.png">

**Options:**

- **(A)** 18 mA
- **(B)** 36 mA
- **(C)** 9 mA
- **(D)** 27 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 36 mA**

**Detailed Solution:**

From the given circuit diagram, the positive terminal of the $6\text{ V}$ battery is connected to the top wire and the negative terminal is connected to the bottom wire through the $100\ \Omega$ resistor. Therefore, the top wire is at a higher potential than the bottom wire.

Based on this polarity:
Diode $D_1$ has its n-side connected to the higher potential, so it is reverse-biased. Its resistance is infinite, and no current flows through this branch.
Diodes $D_2$ and $D_3$ have their p-sides connected to the higher potential, so they are forward-biased. Each offers a forward resistance of $40\ \Omega$.

The resistance of the branch containing $D_2$ is:
$R_2 = 40\ \Omega + 60\ \Omega = 100\ \Omega$

The resistance of the branch containing $D_3$ is:
$R_3 = 40\ \Omega + 160\ \Omega = 200\ \Omega$

These two branches are in parallel. Their equivalent resistance $R_p$ is:
$\dfrac{1}{R_p} = \dfrac{1}{R_2} + \dfrac{1}{R_3} = \dfrac{1}{100} + \dfrac{1}{200} = \dfrac{3}{200}\ \Omega^{-1}$
$R_p = \dfrac{200}{3}\ \Omega$

This parallel combination is in series with the $100\ \Omega$ resistor and the $6\text{ V}$ battery. The total equivalent resistance of the circuit is:
$R_{eq} = 100 + R_p = 100 + \dfrac{200}{3} = \dfrac{500}{3}\ \Omega$

The current through the $100\ \Omega$ resistor is the total current $I$ drawn from the battery:
$I = \dfrac{V}{R_{eq}} = \dfrac{6}{\dfrac{500}{3}} = \dfrac{18}{500}\text{ A}$

Converting the current to milliamperes (mA):
$I = \dfrac{18}{500} \times 1000\text{ mA} = 18 \times 2\text{ mA} = 36\text{ mA}$

Answer: 36 mA

</details>

---

### Q29. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For an ideal diode, in forward and reverse biased condition the resistance is respectively

**Options:**

- **(A)** infinite, zero.
- **(B)** infinite, infinite.
- **(C)** zero, zero.
- **(D)** zero, infinite.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) zero, infinite.**

**Detailed Solution:**

An ideal diode acts as a perfect conductor when it is forward biased, meaning it offers zero resistance to the flow of current.

When it is reverse biased, it acts as a perfect insulator, meaning it offers infinite resistance and blocks the current completely.

Therefore, the resistance in forward and reverse biased conditions is zero and infinite, respectively.

Answer: zero, infinite.

</details>

---

### Q30. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In unbiased p-n junction diode

**Options:**

- **(A)** the potential is same everywhere.
- **(B)** there is an electric field at the junction directed from the p-type side to the n-type side.
- **(C)** there is an electric field at the junction directed from the n-type side to p-type side.
- **(D)** the p-type side is at higher potential than the n-type side.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) there is an electric field at the junction directed from the n-type side to p-type side.**

**Detailed Solution:**

In an unbiased p-n junction, due to the concentration gradient, electrons diffuse from the n-region to the p-region and holes diffuse from the p-region to the n-region.

This diffusion process leaves behind positively charged immobile donor ions in the n-region and negatively charged immobile acceptor ions in the p-region near the junction.

These immobile ions form a depletion layer. The accumulation of positive charges on the n-side and negative charges on the p-side creates an internal electric field.

The direction of this electric field is from the positive charges to the negative charges, which is from the n-type side to the p-type side.

Answer: there is an electric field at the junction directed from the n-type side to p-type side.

</details>

---

### Q31. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the depletion layer of reverse biased p-n junction, the

**Options:**

- **(A)** electric field is maximum.
- **(B)** electric field is very small.
- **(C)** potential is maximum.
- **(D)** potential is zero.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) electric field is maximum.**

**Detailed Solution:**

In a reverse-biased p-n junction, the applied reverse voltage adds to the built-in potential barrier, increasing the total potential difference across the junction.

The electric field is zero in the neutral p and n regions outside the depletion layer. Within the depletion layer, the electric field is directed from the n-side to the p-side and is given by the potential gradient $E = -\dfrac{dV}{dx}$.

Because the potential changes significantly over the very small width of the depletion layer, the electric field is very high and reaches its maximum value at the metallurgical junction. Therefore, in the depletion layer, the electric field is maximum.

Answer: electric field is maximum.

</details>

---

### Q32. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the $\mathrm{p}-\mathrm{n}$ junction diode is unbiased,

**Options:**

- **(A)** n-type side has lower potential than p-type side.
- **(B)** n-type side has same potential as p-type side.
- **(C)** An electric field is established at the junction such that n side is at positive voltage relative to p -side.
- **(D)** The potential across the junction is such that $p$-side is at positive voltage relative to n -side

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) An electric field is established at the junction such that n side is at positive voltage relative to p -side.**

**Detailed Solution:**

In an unbiased p-n junction, due to the concentration gradient, electrons diffuse from the n-side to the p-side and holes diffuse from the p-side to the n-side.

This diffusion leaves behind uncompensated positive donor ions on the n-side and negative acceptor ions on the p-side near the junction.

As a result, a depletion region is formed with a built-in electric field directed from the positive ions on the n-side to the negative ions on the p-side.

This electric field creates a potential barrier where the n-side is at a higher (positive) potential relative to the p-side.

Answer: An electric field is established at the junction such that n side is at positive voltage relative to p -side.

</details>

---

### Q33. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

What is the current in the following junction diode circuit?
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/NTHk7XgojxXEq8-CVTZhfc0Hkh_dtzGF0-349OI2LnI.original.fullsize.png"/>

**Options:**

- **(A)** $10^{-1} \mathrm{~A}$
- **(B)** zero
- **(C)** $10^{-2} \mathrm{~A}$
- **(D)** $5 \times 10^{-3} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) zero**

**Detailed Solution:**

From the given circuit diagram, the potential at the P-side of the diode is $V_P = -5 \text{ V}$.

The N-side of the diode is connected to a potential of $-2 \text{ V}$ through a $500 \ \Omega$ resistor.

For a diode to be forward-biased and conduct current, the potential at the P-side must be greater than the potential at the N-side ($V_P > V_N$).

Here, $V_P = -5 \text{ V}$ and the potential applied to the N-side is $-2 \text{ V}$. Since $-5 \text{ V} < -2 \text{ V}$, the P-side is at a lower potential than the N-side.

Therefore, the diode is reverse-biased.

An ideal reverse-biased diode acts as an open circuit, offering infinite resistance.

Hence, the current flowing through the circuit is zero.

Answer: zero

</details>

---

### Q34. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Assuming that junction diode is ideal, the current in arrangement shown in figure
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/XdCq1_exFRfYR9RJ-oe65xAZPxBcDdqLqbw05z9SXYM.original.fullsize.png"/>

**Options:**

- **(A)** 2 mA
- **(B)** 20 mA
- **(C)** 30 mA
- **(D)** 10 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 20 mA**

**Detailed Solution:**

The potential at the p-side of the diode is $3\text{ V}$ and the potential at the n-side (through the resistor) is $1\text{ V}$.

Since the p-side is at a higher potential than the n-side, the diode is forward-biased.

An ideal diode in forward bias acts as a short circuit with zero resistance and zero voltage drop.

The potential difference across the resistor is:
$\Delta V = 3\text{ V} - 1\text{ V} = 2\text{ V}$

Using Ohm's law, the current $I$ in the circuit is:
$I = \dfrac{\Delta V}{R} = \dfrac{2}{100}\text{ A}$

$I = 0.02\text{ A} = 20\text{ mA}$

Answer: 20 mA

</details>

---

### Q35. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A p-n junction diode cannot be used

**Options:**

- **(A)** as a rectifier.
- **(B)** for converting light energy to electrical energy.
- **(C)** for getting light radiation.
- **(D)** for increasing the amplitude of an a.c. signal.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) for increasing the amplitude of an a.c. signal.**

**Detailed Solution:**

A p-n junction diode allows current to flow in only one direction, so it is used as a rectifier.

A photodiode and a solar cell are p-n junction diodes that convert light energy into electrical energy.

A light-emitting diode (LED) is a p-n junction diode that emits light radiation when forward biased.

A p-n junction diode cannot amplify a signal. Amplification (increasing the amplitude of an a.c. signal) requires a transistor, which consists of two p-n junctions.

Answer: for increasing the amplitude of an a.c. signal.

</details>

---

### Q36. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit, Zener breakdown voltage is 8 V. If power of Zener diode is 1.6 W . The value of $R$ is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Kw63Q8QZnP7WG595PPEOeO4ot33pTsBhuM12lpJlIAU.original.fullsize.png"/>

**Options:**

- **(A)** $2 \Omega$
- **(B)** $4 \Omega$
- **(C)** $6 \Omega$
- **(D)** $10 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10 \Omega$**

**Detailed Solution:**

Given, input voltage $V_{in} = 10\text{ V}$
Zener breakdown voltage $V_Z = 8\text{ V}$
Power of Zener diode $P_Z = 1.6\text{ W}$

The current through the Zener diode is given by:
$I_Z = \dfrac{P_Z}{V_Z} = \dfrac{1.6}{8} = 0.2\text{ A}$

Since there is no load resistor, the entire current flows through the series resistor $R$.
Therefore, current through the resistor $I_R = I_Z = 0.2\text{ A}$

The voltage drop across the resistor $R$ is:
$V_R = V_{in} - V_Z = 10\text{ V} - 8\text{ V} = 2\text{ V}$

Using Ohm's law, the value of resistance $R$ is:
$R = \dfrac{V_R}{I_R} = \dfrac{2}{0.2} = 10\text{ }\Omega$

Answer: $10 \Omega$

</details>

---

### Q37. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two ideal diodes are connected to a battery as shown in the circuit. The current supplied by the battery is
<img width=200px src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/OBvhegryd-ggioiito.png"/>

**Options:**

- **(A)** zero
- **(B)** 0.50 A
- **(C)** 0.25 A
- **(D)** $\quad 0.75 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.50 A**

**Detailed Solution:**

In the given circuit, the positive terminal of the $10\text{ V}$ battery is on the left and the negative terminal is on the right.

Diode $D_1$ has its p-side connected to the higher potential (positive terminal), so it is forward-biased. Being an ideal diode, it acts as a short circuit (zero resistance).

Diode $D_2$ has its n-side connected to the higher potential, so it is reverse-biased. It acts as an open circuit (infinite resistance).

Because $D_2$ is reverse-biased, no current flows through the lower branch. The entire current from the battery flows through the upper branch containing the $20\ \Omega$ resistor.

Using Ohm's law, the current supplied by the battery is:
$I = \dfrac{V}{R} = \dfrac{10}{20} = 0.5\text{ A}$

Answer: 0.50 A

</details>

---

### Q38. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the following circuit, the reading in the ammeter is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Sy91YWBzB0LTrMGsRxv4qZGu3iJCSTA_KlqUEDgUzKk.original.fullsize.png"/>

**Options:**

- **(A)** 25.1 mA
- **(B)** 22.5 mA
- **(C)** 21.5 mA
- **(D)** 21.25 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 21.5 mA**

**Detailed Solution:**

In the given circuit, the positive terminal of the $5\text{ V}$ battery is connected to the p-side of the Silicon diode, so the diode is forward-biased.

The forward voltage drop across a Silicon diode is typically $V_D = 0.7\text{ V}$.

Applying Kirchhoff's Voltage Law to the loop, we get:

$V - V_D - I R = 0$

$5 - 0.7 - I \times 200 = 0$

$4.3 = 200 I$

$I = \dfrac{4.3}{200}\text{ A}$

$I = \dfrac{4.3}{200} \times 1000\text{ mA}$

$I = 21.5\text{ mA}$

The reading in the ammeter is $21.5\text{ mA}$.

Answer: 21.5 mA

</details>

---

### Q39. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the diagram shown, the resistance between points A and B when the ideal diode ' $D$ ' is forward biased is ' $R_1$ ' and that when reverse biased is ' $R_2$ '. The ratio $\dfrac{R_1}{R_2}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_vj1ocGYkQIEtT-Zlf8n0TvGhGmngDCWnMQeYhhnTfE.original.fullsize.png"/>

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{2}{5}$
- **(C)** $\dfrac{3}{2}$
- **(D)** $\dfrac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2}{5}$**

**Detailed Solution:**

When the ideal diode is forward biased, it acts as a short circuit (zero resistance). The $40\ \Omega$ and $60\ \Omega$ resistors are in parallel.

$R_1 = \dfrac{40 \times 60}{40 + 60} = \dfrac{2400}{100} = 24\ \Omega$

When the ideal diode is reverse biased, it acts as an open circuit (infinite resistance). No current flows through the top branch, so the equivalent resistance is simply the resistance of the bottom branch.

$R_2 = 60\ \Omega$

The required ratio is:

$\dfrac{R_1}{R_2} = \dfrac{24}{60} = \dfrac{2}{5}$

Answer: $\dfrac{2}{5}$

</details>

---

### Q40. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The depletion layer in $\mathrm{p}-\mathrm{n}$ junction region is caused by

**Options:**

- **(A)** drift of electrons.
- **(B)** migration of impurity ions.
- **(C)** diffusion of charge carries.
- **(D)** drift of holes.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) diffusion of charge carries.**

**Detailed Solution:**

In a p-n junction, there is a higher concentration of holes in the p-region and a higher concentration of electrons in the n-region.

Due to this concentration gradient, holes diffuse from the p-side to the n-side, and electrons diffuse from the n-side to the p-side.

As these charge carriers diffuse across the junction, they leave behind immobile ionized dopant atoms (negative ions on the p-side and positive ions on the n-side).

This creates a region near the junction that is depleted of mobile charge carriers, which is known as the depletion layer.

Therefore, the depletion layer is caused by the diffusion of charge carriers.

Answer: diffusion of charge carries.

</details>

---

### Q41. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In the circuit diagram shown in figure, the current through the zener diode is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/i-soXw5tQnJPE3X47LsE7zsqkyynHVAHiFhfcSDfCWI.original.fullsize.png"/>

**Options:**

- **(A)** 30 mA
- **(B)** 17.5 mA
- **(C)** 15 mA
- **(D)** $\quad 12.5 \mathrm{~mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 17.5 mA**

**Detailed Solution:**

Given:
Input voltage, $V_{in} = 24 \text{ V}$
Zener voltage, $V_Z = 15 \text{ V}$
Series resistance, $R_S = 300 \text{ } \Omega$
Load resistance, $R_L = 1200 \text{ } \Omega$

First, check if the Zener diode is in the breakdown region. The voltage across the load without the Zener diode is:
$V = V_{in} \times \dfrac{R_L}{R_S + R_L} = 24 \times \dfrac{1200}{300 + 1200} = 24 \times \dfrac{1200}{1500} = 19.2 \text{ V}$

Since $19.2 \text{ V} > 15 \text{ V}$, the Zener diode is in breakdown and regulates the voltage across the load to $V_Z = 15 \text{ V}$.

The voltage drop across the series resistor $R_S$ is:
$V_S = V_{in} - V_Z = 24 - 15 = 9 \text{ V}$

The current through the series resistor $R_S$ is:
$I_S = \dfrac{V_S}{R_S} = \dfrac{9}{300} \text{ A} = 30 \text{ mA}$

The current through the load resistor $R_L$ is:
$I_L = \dfrac{V_Z}{R_L} = \dfrac{15}{1200} \text{ A} = 12.5 \text{ mA}$

Applying Kirchhoff's current law, the current through the Zener diode $I_Z$ is:
$I_Z = I_S - I_L = 30 \text{ mA} - 12.5 \text{ mA} = 17.5 \text{ mA}$

Answer: 17.5 mA

</details>

---

### Q42. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A semiconductor device $X$ is connected in series with a battery and a resistor. The current of 10 mA is found to pass through the circuit. If the terminals of X are connected in reverse manner, the current drops to almost zero. $X$ may be

**Options:**

- **(A)** a zener diode
- **(B)** a p-n junction diode
- **(C)** an intrinsic semiconductor
- **(D)** an extrinsic semiconductor

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a p-n junction diode**

**Detailed Solution:**

The device allows a significant current of $10\text{ mA}$ to flow when connected in one direction, indicating it is in forward bias.

When the terminals are reversed, the current drops to almost zero, indicating it offers very high resistance in the reverse direction (reverse bias).

This unidirectional conduction property is the characteristic of a p-n junction diode.

Intrinsic and extrinsic semiconductors conduct current equally in both directions, acting like simple resistors.

A Zener diode can also conduct in reverse bias if the applied voltage exceeds its breakdown voltage, but a standard p-n junction diode is specifically designed to block current in reverse bias.

Answer: a p-n junction diode

</details>

---

### Q43. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A zener diode, having breakdown voltage 15 V is used in a voltage regulator circuit as shown. The current through the zener diode is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/yYishGlKrJ4sghLsljNduq9GTNZdLmM2xsnXKOjO_0c.original.fullsize.png"/>

**Options:**

- **(A)** 20 mA
- **(B)** 5 mA
- **(C)** 10 mA
- **(D)** 15 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5 mA**

**Detailed Solution:**

Given:
Input voltage, $V_{in} = 20\text{ V}$
Zener voltage, $V_Z = 15\text{ V}$
Series resistance, $R_s = 250\ \Omega$
Load resistance, $R_L = 1\text{ k}\Omega = 1000\ \Omega$

Since the Zener diode is in parallel with the load resistor, the voltage across the load is regulated at $V_L = V_Z = 15\text{ V}$.

The voltage drop across the series resistor is:
$V_s = V_{in} - V_Z = 20\text{ V} - 15\text{ V} = 5\text{ V}$

The total current from the source (through $R_s$) is:
$I_s = \dfrac{V_s}{R_s} = \dfrac{5}{250}\text{ A} = 20\text{ mA}$

The current through the load resistor is:
$I_L = \dfrac{V_L}{R_L} = \dfrac{15}{1000}\text{ A} = 15\text{ mA}$

Applying Kirchhoff's current law, the current through the Zener diode is:
$I_Z = I_s - I_L = 20\text{ mA} - 15\text{ mA} = 5\text{ mA}$

Answer: 5 mA

</details>

---

### Q44. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Find the magnitude of current in the given circuit.
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/fb0BdQzwqqF0tLVVd_mFizzhsnUNJXdx0tvf8CRITzs.original.fullsize.png"/>

**Options:**

- **(A)** zero ampere
- **(B)** 1 ampere
- **(C)** 0.1 ampere
- **(D)** 0.2 ampere

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) zero ampere**

**Detailed Solution:**

Let us analyze the potentials at the two ends of the given circuit branch.

From the circuit diagram, the left terminal is connected to a battery which provides a potential of $-4\text{V}$ at the p-side of the diode. Thus, the potential at the p-side is $V_p = -4\text{V}$.

The right terminal is connected to a battery which provides a potential of $-1\text{V}$ at the other end of the $3\,\Omega$ resistor. Thus, the potential at the n-side of the diode (if it were conducting) would be pulled towards $V_n = -1\text{V}$.

For a p-n junction diode to be forward biased and conduct current, the potential at the p-side must be greater than the potential at the n-side ($V_p > V_n$).

In this circuit, we have:
$V_p = -4\text{V}$
$V_n = -1\text{V}$

Comparing the two potentials, we see that $-4\text{V} < -1\text{V}$, which means $V_p < V_n$.

Since the p-side is at a lower potential than the n-side, the diode is reverse biased.

An ideal diode in reverse bias acts as an open circuit, offering infinite resistance. Therefore, it blocks the flow of current.

As a result, the current in the circuit is zero.

Answer: zero ampere

</details>

---

### Q45. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In the following circuit, the current flowing through zener diode is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/tTAbfpfM8sF4YUnGgvyHbiA4ZOsdqHaLN4CePV29OCU.original.fullsize.png"/>

**Options:**

- **(A)** 35 mA
- **(B)** 25 mA
- **(C)** 15 mA
- **(D)** 5 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 25 mA**

**Detailed Solution:**

Given:
Input voltage, $V = 20\text{ V}$
Zener voltage, $V_Z = 8\text{ V}$
Series resistance, $R_1 = 400\text{ }\Omega$
Load resistance, $R_2 = 1600\text{ }\Omega$

First, check if the Zener diode is in the breakdown region. The voltage across $R_2$ without the Zener diode is:
$V' = \dfrac{R_2}{R_1 + R_2} \times V = \dfrac{1600}{400 + 1600} \times 20 = 16\text{ V}$

Since $V' > V_Z$ ($16\text{ V} > 8\text{ V}$), the Zener diode is in the breakdown region and the voltage across it will be maintained at $8\text{ V}$.

The voltage across $R_1$ is:
$V_{R_1} = V - V_Z = 20 - 8 = 12\text{ V}$

The current through $R_1$ is:
$I_{R_1} = \dfrac{V_{R_1}}{R_1} = \dfrac{12}{400} = 0.03\text{ A} = 30\text{ mA}$

The current through $R_2$ is:
$I_{R_2} = \dfrac{V_Z}{R_2} = \dfrac{8}{1600} = 0.005\text{ A} = 5\text{ mA}$

Applying Kirchhoff's current law, the current through the Zener diode is:
$I_Z = I_{R_1} - I_{R_2} = 30\text{ mA} - 5\text{ mA} = 25\text{ mA}$

Answer: 25 mA

</details>

---

### Q46. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The potential barrier in $\mathrm{p}-\mathrm{n}$ junction diode is due to

**Options:**

- **(A)** depletion of positive charges near the junction.
- **(B)** accumulation of positive charges near the junction.
- **(C)** depletion of negative charges near the junction.
- **(D)** accumulation of positive and negative charges near the junction.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) accumulation of positive and negative charges near the junction.**

**Detailed Solution:**

When a p-n junction is formed, electrons from the n-region diffuse into the p-region and holes from the p-region diffuse into the n-region.

This diffusion of majority charge carriers leaves behind immobile positive donor ions on the n-side and immobile negative acceptor ions on the p-side near the junction.

The accumulation of these positive and negative charges near the junction creates an electric field directed from the n-side to the p-side, which gives rise to the potential barrier.

Answer: accumulation of positive and negative charges near the junction.

</details>

---

### Q47. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

On increasing the reverse bias to a large value in a P-N junction diode, current

**Options:**

- **(A)** increase slowly.
- **(B)** remains fixed.
- **(C)** suddenly increases.
- **(D)** decreases slowly.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) suddenly increases.**

**Detailed Solution:**

When the reverse voltage increases beyond the breakdown voltage, the current suddenly increases.

</details>

---

### Q48. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The following graph represents
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/t2QFKmr7MRdNo0R0qgIOLVJ-n63lWzavKTdWZkGY4h0.original.fullsize.png">

**Options:**

- **(A)** forward bias characteristics of a solar cell
- **(B)** reverse bias characteristics of a Zener diode
- **(C)** reverse bias characteristics of a photodiode
- **(D)** forward bias characteristics of a LED

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) forward bias characteristics of a LED**

**Detailed Solution:**

With increasing voltage, the LED's current rises, leading to light emission due to charge carrier recombination.

</details>

---

### Q49. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In which figure, the junction diode is forward biased?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/v7zBYSYpzvqnhGaeUodJ9pwVwc8ZZTuwu1XHu0QQ5AA.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/FRCQf50ctPkn4SFhia78vLjgIkp5C1_YXIv1JPVuAMI.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ChN6a1nVxiaW52L2hDDLfVht3JDyZaGC6sgvSQX73iI.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/W5_oq1JGLcp0Aaq_nF_NWrrBA71zuhJZz7zksZoPqG4.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/FRCQf50ctPkn4SFhia78vLjgIkp5C1_YXIv1JPVuAMI.original.fullsize.png">**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WLQweI_X2uBejgJUsvv0ipHevpKW7sQEQ_023uaJWSo.original.fullsize.png">

</details>

---

### Q50. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

When forward bias is applied to a p-n junction, then what happens to the potential barrier $\left(\mathrm{V}_{\mathrm{B}}\right)$ and the width $(\mathrm{X})$ of the depletion region?

**Options:**

- **(A)** $V_B$ increase, $X$ decreases
- **(B)** $\mathrm{V}_{\mathrm{B}}$ decreases, $\mathrm{X}$ increase
- **(C)** $\mathrm{V}_{\mathrm{B}}$ increase, $\mathrm{X}$ increase
- **(D)** $\quad V_B$ decreases, $\mathrm{X}$ decreases

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\quad V_B$ decreases, $\mathrm{X}$ decreases**

**Detailed Solution:**

\begin{array}{|l|l|l|} \hline Std.11 & Ch-14 & Subtopic-14.6 \\ \hline \end{array}

</details>

---

### Q51. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}-\mathrm{n}$ junction diode is in forward bias then

**Options:**

- **(A)** width of depletion layer increases
- **(B)** electric conduction is not possible at all
- **(C)** barrier voltage increases
- **(D)** width of depletion layer decreases

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) width of depletion layer decreases**

**Detailed Solution:**

Std.11|Ch-14 | Subtopic-14.7

</details>

---

### Q52. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Identify the correct circuit diagrams for the normal operation from the following.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/8v-ecfYkQQDxSJKHAEtpEhKgSrIUkTnWEleH8y6pjnM.original.fullsize.png">

**Options:**

- **(A)** (A), (B)
- **(B)** (B), (C)
- **(C)** $(\mathrm{A}),(\mathrm{C})$
- **(D)** (B), (D)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (B), (D)**

**Detailed Solution:**

Option (B) is photodiode and option (D) is LED with reverse and forward biasing respectively. Therefore both will operate properly.

</details>

---

### Q53. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the diagram shown, the resistances between points $\mathrm{A}$ and $\mathrm{B}$ when ideal diode $\mathrm{D}$ is forward biased is ' $R_1$ ' and that when reverse biased is ' $R_2$ '. The ratio $R_1: R_2$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4u7JSn17qoFxKfAy_l_QTwtuQNDKzKAq8gbNb5C0TiM.original.fullsize.png">

**Options:**

- **(A)** $2: 1$
- **(B)** $1: 1$
- **(C)** $1: 2$
- **(D)** $1: 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 2$**

**Detailed Solution:**

When the diode is forward biased, current will flow through both the arms.
$\therefore \quad$ The effective resistance is
$\mathrm{R}_1=\frac{40 \times 40}{80}=\frac{1600}{80}=20 \Omega$
When the diode is reverse biased, current will flow through the bottom arm only
$\therefore \quad$ The effective resistance $\mathrm{R}_2$ is $40 \Omega$.
$\therefore \quad \frac{\mathrm{R}_1}{\mathrm{R}_2}=\frac{20}{40}=\frac{1}{2}$

</details>

---

### Q54. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Identify the mismatch out of the following.

**Options:**

- **(A)** Zener diode - voltage regulator.
- **(B)** Photodiode-optocouplers.
- **(C)** Solar cell-Electrical energy into light.
- **(D)** Light emitting diode - optical communication.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Solar cell-Electrical energy into light.**

**Detailed Solution:**

Solar cell converts light energy into electrical energy.

</details>

---

### Q55. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the reverse biasing of a p-n junction diode

**Options:**

- **(A)** the width of the depletion layer decreases.
- **(B)** the width of the depletion layer increases.
- **(C)** the number of minority charge carriers increase.
- **(D)** the number of majority charge carriers increase.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) the width of the depletion layer increases.**

**Detailed Solution:**

Std.11 | Ch-14 | Subtopic-14.6

</details>

---

### Q56. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A $5.0 \mathrm{~V}$ stabilized power supply is required to be designed using a $12 \mathrm{~V} \mathrm{DC}$ power supply as input source. The maximum power rating of zener diode is $2.0 \mathrm{~W}$. The minimum value of resistance $\mathrm{R}_{\mathrm{s}}$ in $\Omega$ connected in series with zener diode will be

**Options:**

- **(A)** $16.5$
- **(B)** $17.5$
- **(C)** $18.5$
- **(D)** $15.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $17.5$**

**Detailed Solution:**

Using the series resistance formula for a zener diode
$\begin{aligned}
\mathrm{R}_{\mathrm{S}} & =\frac{\left(\mathrm{V}_{\mathrm{S}}-\mathrm{V}_{\mathrm{Z}}\right)}{\mathrm{I}_{\mathrm{Z}_{\max }}} \\
\mathrm{I}_{\mathrm{Z} \max } & =\frac{\mathrm{P}_{\mathrm{Z}}}{\mathrm{V}_{\mathrm{Z}}}=\frac{2}{5}=400 \mathrm{~mA} \\
\therefore \quad \mathrm{R}_{\mathrm{S}} & =\frac{(12-5)}{400 \times 10^{-3}}=\frac{7}{400} \times 10^3 \\
& =17.5 \Omega
\end{aligned}$

</details>

---

### Q57. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Reverse bias applied to a $p-n$ junction diode

**Options:**

- **(A)** increases the minority charge carriers.
- **(B)** lowers the potential barrier.
- **(C)** decreases the majority charge carriers.
- **(D)** raises the potential barrier.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) raises the potential barrier.**

**Detailed Solution:**

In reverse bias a $p-n$ junction diode has raised potential barrier.

</details>

---

### Q58. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The given circuit has two ideal diodes $D_1$ and $D_2$ connected as shown in the figure. The current flowing through the resistance $R_1$ will be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/x2HaLltfVVM6gT498JVV694zav9juAdHCLJgd3fuPz4.original.fullsize.png">

**Options:**

- **(A)** $2 \mathrm{~A}$
- **(B)** $3.3 \mathrm{~A}$
- **(C)** $2.5 \mathrm{~A}$
- **(D)** $7 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2.5 \mathrm{~A}$**

**Detailed Solution:**

The ideal diode $D_1$ is reversed biased whereas ideal diode $D_2$ is forward biased. Thus, $D_1$ acts as an open switch while $D_2$ as a closed switch as shown in the circuit.
Thus, current flowing through $R_1, I=\frac{V}{R_1+R_3}=\frac{10}{2+2}=2.5 \mathrm{~A}$

</details>

---

### Q59. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Which one of the following graph represents forward bias characteristic of a diode?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/57eeKNtMlneZ8Wuk1JsBPwVv1u8ui5qwql5JWQburiA.original.fullsize.png">

**Options:**

- **(A)** C
- **(B)** B
- **(C)** D
- **(D)** A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) D**

**Detailed Solution:**

Conceptual problem. Theory based.
Graph D has exponential characteristic, which is similar to ideal diode.

The current-voltage function (also called the " $i-v$ characteristic") for an ideal diode is
$i(v)=I_S\left[\exp \left(\frac{v}{\eta V_T}\right)-1\right], v>V_Z$
where $I_S$ is the reverse saturation current, $v$ is the applied voltage (reverse bias is negative), $V_T$ is constant dependent on temperature, and $\eta$ is the emission coefficient, which is 1 for germanium devices and 2 for silicon devices.
$V_Z$ is the reverse bias break done voltage.

</details>

---

### Q60. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a forward bias arrangement of a p-n junction diode, the

**Options:**

- **(A)** p-region is connected to the positive terminal of battery.
- **(B)** n-region is connected to the positive terminal of battery.
- **(C)** p-region is connected to negative terminal of battery.
- **(D)** p-region is connected to negative terminal of the battery.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) p-region is connected to the positive terminal of battery.**

**Detailed Solution:**

Concept based.

</details>

---

### Q61. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

What are the values of the currents flowing in each of the following diode circuits $\mathrm{X}$ and $\mathrm{Y}$ respectively? (Assume that the diodes are ideal)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wgg_qJFx6HxOebfhioA958tWp0KjzpvPaVs13kFmQSk.original.fullsize.png">

**Options:**

- **(A)** $1 \mathrm{~A}, 2 \mathrm{~A}$
- **(B)** $2 \mathrm{~A}, 1 \mathrm{~A}$
- **(C)** $4 \mathrm{~A}, 2 \mathrm{~A}$
- **(D)** $2 \mathrm{~A}, 4 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \mathrm{~A}, 2 \mathrm{~A}$**

**Detailed Solution:**

In circuit $\mathrm{X}$, both the diodes are forward biased and hence both will conduct.

The two resistances of $4 \Omega$ each are in parallel. Their equivalent resistance is $2 \Omega$. Hence the current $\mathrm{I}=\frac{\mathrm{v}}{\mathrm{R}}=\frac{8}{2}=4 \mathrm{~A}$

In the circuit $Y$, the diode $D_1$ is forward biased but diode $D_2$ is reverse biased. Hence only diode $\mathrm{D}_1$ will conduct. The resistance is $4 \Omega$.
Hence, $\mathrm{I}=\frac{8}{4}=2 \mathrm{~A}$

</details>

---

### Q62. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A p-n junction photodiode is fabricated from semiconductor with a band gap of $2.5 \mathrm{eV}$. It can detect a signal of wavelength
[Planck's constant $=6.6 \times 10^{-34} \mathrm{Js}, \mathrm{c}=3 \times 10^8 \mathrm{~m} / \mathrm{s}, \mathrm{e}=1.6 \times 10^{-}$ $\left.{ }^{19} \mathrm{C}\right]$

**Options:**

- **(A)** $6000 \mathrm{~nm}$
- **(B)** $6000 Å$
- **(C)** $5000 Å$
- **(D)** $4000 \mathrm{~nm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5000 Å$**

**Detailed Solution:**

The wavelength corresponding to $2.5 \mathrm{eV}$ is given by Energy $(\mathrm{eV})=\frac{12400}{\lambda(Å)}$
$$
\therefore \lambda=\frac{12400}{2.5}=5000 Å
$$
To get detected, the signal should have energy greater than $2.5 \mathrm{eV}$ or wavelength less than $5000 Å$.

</details>

---

### Q63. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two identical ideal diodes are connected to an ammeter and a d.c source (1 volt) as shown. In which one of the following circuits, ammeter will not show any defection?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/F3vXOGHPw9t9Mas3Rsw-t8QOZN9GojElynZ_cpyIH-k.original.fullsize.png">

**Options:**

- **(A)** (d)
- **(B)** (a)
- **(C)** (b)
- **(D)** (c)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (a)**

**Detailed Solution:**

In circuit (a) the two diodes are in series and one of the diodes is reverse biased. Hence no current will flow in the circuit and ammeter will not show any deflection.

</details>

---

### Q64. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an ideal junction diode, the current flowing through $\mathrm{PQ}$ is (resistance is 2 kilo-ohms)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BXjNn9mYdxlLE-5glEY8tRp1kcSZY-1VJ4VcOnr9p5E.original.fullsize.png">

**Options:**

- **(A)** $2 \times 10^{-3} \mathrm{~A}$
- **(B)** $2 \times 10^{-2} \mathrm{~A}$
- **(C)** $4 \times 10^{-3} \mathrm{~A}$
- **(D)** $10^{-3} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 \times 10^{-3} \mathrm{~A}$**

**Detailed Solution:**

The diode is forward biased. The potential difference between $\mathrm{P}$ and $\mathrm{Q}$ is $(3-(-5))=8 \mathrm{~V}$.
$$
\mathrm{I}=\frac{\mathrm{V}}{\mathrm{R}}=\frac{8}{2 \times 10^3}=4 \times 10^{-3} \mathrm{~A}
$$

</details>

---

### Q65. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$$
\text { The current in the following circuit is }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/U2TxD3ERBcriew4CVx-is6SMri3yuYqtj6ZWOXXwGmY.original.fullsize.png">

**Options:**

- **(A)** $10 \mathrm{~A}$
- **(B)** zero
- **(C)** 0.025
- **(D)** $10^{-2} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10^{-2} \mathrm{~A}$**

**Detailed Solution:**

The diode is forward biased.
Potential difference $=5-3=2 \mathrm{~V}$
$$
\mathrm{I}=\frac{\mathrm{V}}{\mathrm{R}}=\frac{2}{200}=10^{-2} \mathrm{~A}
$$

</details>

---

### Q66. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

When $\mathrm{p}-\mathrm{n}$ junction diode is reverse biased, then the width of the barrier potential will

**Options:**

- **(A)** increase and it will offer more resistance.
- **(B)** decrease and it will offer zero resistance.
- **(C)** remain constant and it will not offer resistance.
- **(D)** decrease and it will offer more resistance.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increase and it will offer more resistance.**

**Detailed Solution:**

No Solution.

</details>

---

### Q67. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{p}-\mathrm{n}$ junction diode is reverse biased then

**Options:**

- **(A)** potential barrier decreases.
- **(B)** width of the depletion layer decreases.
- **(C)** electrical conduction is possible.
- **(D)** width of the depletion layer increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) width of the depletion layer increases.**

**Detailed Solution:**

(B)
When p-n junction is reverse biased, the depletion region is increased i.e., the potential barrier increased.

</details>

---

### Q68. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

I-V characteristics for a junction diode is shown. The device is

**Options:**

- **(A)** LED.
- **(B)** solar cell.
- **(C)** photo cell.
- **(D)** zener diode.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) solar cell.**

**Detailed Solution:**

(C)
Theory question

</details>

---

### Q69. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The width of depletion layer of a p-n junction diode, when it is (i) forward biased
and (ii) reverse biased respectively

**Options:**

- **(A)** increases and increases.
- **(B)** decreases and decreases.
- **(C)** increases and decreases
- **(D)** decreases and increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreases and increases.**

**Detailed Solution:**

(i) The width of depletion layer of a p-n junction decreases when the junction is forward biased.
(ii) The width of depletion layer of a p-n junction increases when the junction is reverse biased.

</details>

---

### Q70. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For an ideal diode, the current in the following arrangement is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ymOW0tCDbpMkNVnIiqu490kmHwz5UmfPUOJHF9jerr8.original.fullsize.png">

**Options:**

- **(A)** $10 A$
- **(B)** $10 \mathrm{~mA}$
- **(C)** $20 \mathrm{~mA}$
- **(D)** $1 \mathrm{~mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $10 \mathrm{~mA}$**

**Detailed Solution:**

This general configuration, emitter is forward biased and collector is reverse biased w.r.t the base.

</details>

---

### Q71. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The figure shows two diagrams in which diode and resistance are connected. Out of the following statements which one is TRUE?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/KyguMRihoTBwCY-3J-GvvFY2m-YkObOj1Ot2Lg1PXM8.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Pmki1crcLQ8mIJ4JC9q7aV4r-PZYWoLpr53ahxFFwt4.original.fullsize.png">

**Options:**

- **(A)** diagram (A) and diagram (B) both are forward biased.
- **(B)** diagram (A) forward biased and diagram (B) reverse biased.
- **(C)** diagram (A) and diagram (B) both are reverse biased.
- **(D)** diagram (A) reverse biased and diagram (B) forward biased.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) diagram (A) reverse biased and diagram (B) forward biased.**

**Detailed Solution:**

The anode in diagram (a) has a lower voltage than the cathode. as a result it is skewed in the opposite direction .the anode in diagram(b) has a higher potential than the cathodes. as a result it is in forward biased

</details>

---

### Q72. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The non-zero potential difference across diode $\mathrm{D}_{1}$ and that across diode $\mathrm{D}_{2}$ are
equal in the circuit shown in the figure (both the diodes are identical in
characteristics)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/jOE5TG3lnnpYb9HtUu8s4LymTipvnfZwmZLrCAdj1SY.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RMaqynnWLy4S-LcOT0FGxvhe3LQHqSa84b4dXUjVcWc.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/HBcD3Qt6CIEKe7oacTyfICxKhxQFKyGyiFdeF-DDk5c.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/pfTtriWTuf7Vu4IUyudplBuqepnHfmeSPKuI0isDBuw.original.fullsize.png">

**Options:**

- **(A)** (A)
- **(B)** (B)
- **(C)** (C)
- **(D)** (D)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (D)**

**Detailed Solution:**

In diagram (a) anode is at a lower potential compared to cathode. Hence it is reverse biased. In diagram (b) anode is at a higher potential compared to cathode. Hence it is forward biased.

</details>

---

### Q73. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The region near the junction of an unbiased $\mathrm{p}-\mathrm{n}$ junction diode is known as
depletion layer. The layer is depleted of

**Options:**

- **(A)** only negative ions.
- **(B)** electrons and holes.
- **(C)** both positive and negative ions.
- **(D)** only positive ions.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) electrons and holes.**

**Detailed Solution:**

Theoretical question

</details>

---

### Q74. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Assuming that the junction diode is ideal, the current in the arrangement shown in figure is

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f7e41561-d834-4c36-84b4-83b519ecf52a.png" style="height: 44px; width: 280px;" />

**Options:**

- **(A)** <math><mn>30</mn><mi></mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math><mn>40</mn><mi></mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(C)** <math><mn>20</mn><mi></mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(D)** <math><mn>10</mn><mi></mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>20</mn><mi></mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<math><mi>L</mi><mi>'</mi><mo>=</mo><mfrac><mrow><mi>V</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo> </mo><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>100</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>100</mn></mrow></mfrac><mi>A</mi></math>  
<math><msup><mrow><mi>L</mi></mrow><mrow><mi>'</mi></mrow></msup><mo>=</mo><mn>20</mn><mi></mi><mi>m</mi><mi>A</mi></math>

</details>

---

### Q75. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In case of p-n junction diode, the width of depletion region is

**Options:**

- **(A)** Decreased with heavy doping
- **(B)** Increased by reserve biasing
- **(C)** Decreased with light doping
- **(D)** Increased by forward biasing

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Increased by reserve biasing**

**Detailed Solution:**

In case of p – n junction diode, when it is reserved biased, the reserve voltage supports the barrier potential and hence the width of the depletion layer increases. 
In forward biasing, the width decreases as the forward voltage opposes the potential barrier. 
The width of the depletion region increases, if the diode is further doped heavily as the movement of charge carrier decrease.

</details>

---

### Q76. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

V-I characteristics of LED is shown correctly by graph

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3be06787-7fe5-43ad-a96b-5b3c4a2cfca0.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/d189a4d7-fa47-4c26-9d0b-24f39bfd2f23.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/f7e0e8c7-6bb8-4b32-909f-1e39ef405035.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/49106ab3-55fd-4c99-b306-ad73ce0a32da.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/d189a4d7-fa47-4c26-9d0b-24f39bfd2f23.png">**

**Detailed Solution:**

Since, an LED is forward biased diode, so its characteristics are those of forward bias, i.e., 
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/d0e95541-66c3-4b2f-97e8-6dae2e29474a.png"> 
Here, option (a) is characteristics of a diode in forward and reverse bias. Option (c) <math><mo>→</mo></math> characteristics of solar cell. 
Option (d) <math><mo>→</mo></math> reverse bias characteristics 1 drawn in first quadrant can be photodiode or Zener diode.

</details>

---

### Q77. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `1`

With forward bias mode, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>-</mo><mi mathvariant="normal">n</mi></math> junction diode

**Options:**

- **(A)** is one in which width of depletion layer increases
- **(B)** is one in which potential barrier increases
- **(C)** acts as closed switch
- **(D)** acts as open switch

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) acts as closed switch**

**Detailed Solution:**

​When a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>-</mo><mi mathvariant="normal">n</mi></math> junction is in forward bias, it allows current to flow through it with minimal resistance.
Hence we can say, it acts like a closed switch

</details>

---

### Q78. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

In reverse bias $p n$ -junction diode depletion layer width

**Options:**

- **(A)** decreases
- **(B)** increases
- **(C)** remain same
- **(D)** Can't predicted

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) increases**

**Detailed Solution:**

In reverse bias $p n$ -junction diode depletion layer width increases.

</details>

---

### Q79. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

A $p-n$ photodiode is made of a material with a band gap of $2.0$ eV. The minimum frequency of the radiation that can be absorbed by the material is nearly

**Options:**

- **(A)** $10 \times 10^{14} \mathrm{~Hz}$
- **(B)** $5 \times 10^{14} \mathrm{~Hz}$
- **(C)** $1 \times 10^{14} \mathrm{~Hz}$
- **(D)** $20 \times 10^{14} \mathrm{~Hz}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \times 10^{14} \mathrm{~Hz}$**

**Detailed Solution:**

$p-n$ photodiode is a semiconductor diode that produces a significant current when illuminated. It is reversed biased but is operated below the breakdown voltage. Energy of radiation $=$ band gap energy ie, $h v=2.0 \mathrm{eV}$
or $v=\frac{2.0 \times 1.6 \times 10^{-19}}{6.6 \times 10^{-34}} \approx 5 \times 10^{14} \mathrm{~Hz}$

</details>

---

### Q80. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

A photoelectric cell is illuminated by a point source of light $1 \mathrm{~m}$ away. When the source is shifted to $2 \mathrm{~m}$ then

**Options:**

- **(A)** each emitted electron carries half the initial energy
- **(B)** number of electrons emitted is a quarter of the initial number
- **(C)** each emitted electron carries one quarter of the initial energy
- **(D)** number of electrons emitted is half the initial number

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) number of electrons emitted is a quarter of the initial number**

**Detailed Solution:**

Key Idea Number of photoelectrons emitted per second is directly proportional to intensity of light. Intensity of light source is
$$
I \propto \frac{1}{d^{2}}
$$
When distance is doubled, intensity becomes one-fourth.
As number of photoelectrons $\propto$ intensity, so number of photoelectrons is quarter of the initial number.

</details>

---

### Q81. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

The thermal conductivity of a rod is $2 .$ What is its thermal resistivity?

**Options:**

- **(A)** $0.5$
- **(B)** 1
- **(C)** $0.25$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.5$**

**Detailed Solution:**

Key Idea Thermal resistivity is reciprocal of thermal conductivity.
$$
\begin{aligned}
\text { Thermal resistivity } &=\frac{1}{\text { Thermal conductivity }} \\
&=\frac{1}{2} \\
&=0.5
\end{aligned}
$$

</details>

---

