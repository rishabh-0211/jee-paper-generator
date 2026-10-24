# JEE Main Physics - Semiconductors

## Topic 3: Diodes

**Total Questions:** 85

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum rated power of the LED is $2$ mW and it is used in the circuit with input voltage of $5$ V as shown in the figure below. The current through resistance $R_S$ is $0.5$ mA. The minimum value of the resistance of $R_S$, to ensure that the LED is not damaged is _______ k$\Omega$.
<img style="width: 400px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/06APRS1__q39_d1.png" />

**Options:**

- **(A)** $6$
- **(B)** $2$
- **(C)** $4$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$**

**Detailed Solution:**

Since the reverse-biased diode branch acts as an open circuit, the entire current through the series resistor $R_S$ flows through the LED:
$I_{\text{LED}} = I_{R_S} = 0.5\text{ mA}$

At the boundary condition where the LED dissipates its maximum rated power of $2\text{ mW}$:
$P_{\text{LED}} = V_{\text{LED}} \cdot I_{\text{LED}}$

$V_{\text{LED}} = \dfrac{P_{\text{LED}}}{I_{\text{LED}}} = \dfrac{2\text{ mW}}{0.5\text{ mA}} = 4\text{ V}$

Applying Kirchhoff's voltage law to the loop:
$V_{\text{input}} - V_{R_S} - V_{\text{LED}} = 0$

$5 - (I_{R_S} \cdot R_S) - 4 = 0$

$I_{R_S} \cdot R_S = 1\text{ V}$

$R_S = \dfrac{1\text{ V}}{0.5 \times 10^{-3}\text{ A}} = 2000\ \Omega = 2\text{ k}\Omega$

Hence, the correct option is $(2)\ 2$.

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a semiconductor p-n diode, the doping concentrations on p-side and n-side are $10^{15}\text{ atoms/cm}^3$ and $10^{18}\text{ atoms/cm}^3$, respectively. Which one of the following statements is true ?

**Options:**

- **(A)** Widths of depletion region on either side of the interface are equal
- **(B)** The depletion region width is more on p-side compared to that in n-side
- **(C)** The depletion region width is more on n-side compared to that in p-side
- **(D)** No depletion region forms because of unequal doping concentrations on p and n-sides

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The depletion region width is more on p-side compared to that in n-side**

**Detailed Solution:**

In a p-n junction diode, the total charge on both sides of the depletion region must be equal to maintain charge neutrality.

Let $x_p$ and $x_n$ be the widths of the depletion region on the p-side and n-side, respectively. Let $N_A$ and $N_D$ be the doping concentrations on the p-side and n-side.

The charge neutrality condition is given by:
$N_A x_p = N_D x_n$

Given $N_A = 10^{15} \text{ atoms/cm}^3$ and $N_D = 10^{18} \text{ atoms/cm}^3$.

Substituting the values, we get:
$10^{15} x_p = 10^{18} x_n$

$x_p = 10^3 x_n$

Since $x_p > x_n$, the depletion region penetrates more into the lightly doped side. Therefore, the depletion region width is more on the p-side compared to that in the n-side.

Answer: The depletion region width is more on p-side compared to that in n-side

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `numerical` | *Level:* `1`

A diode has Zener voltage of $10$ V and maximum power dissipation of $0.5$ W, then the minimum resistance to be used in series with this diode for safety when it is connected to a $25$ V power supply is ______ $\Omega$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **300**

**Detailed Solution:**

Given Zener voltage $V_Z = 10$ V and maximum power dissipation $P_{max} = 0.5$ W.

The maximum safe current through the Zener diode is given by $I_{max} = \dfrac{P_{max}}{V_Z} = \dfrac{0.5}{10} = 0.05$ A.

The voltage drop across the series resistor is $V_R = V_S - V_Z = 25 - 10 = 15$ V.

For safety, the current through the circuit should not exceed $I_{max}$. Thus, the minimum resistance $R$ is $R = \dfrac{V_R}{I_{max}} = \dfrac{15}{0.05} = 300$ $\Omega$.

Answer: $300$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R

Assertion A: A diode under reverse-biased condition provides very small current which is nearly independent of voltage until a critical limit at which the current increases drastically.

Reason R: Below the critical voltage limit, only majority charge carriers flow which increases drastically above critical voltage.

Choose the correct answer from the options given below

**Options:**

- **(A)** Both A and R are true and R is the correct explanation of A
- **(B)** Both A and R are true but R is NOT the correct explanation of A
- **(C)** A is true but R is false
- **(D)** A is false but R is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A is true but R is false**

**Detailed Solution:**

In a reverse-biased diode, the current is very small and remains almost constant (known as reverse saturation current) until the breakdown voltage is reached. At the breakdown voltage (critical limit), the current increases drastically. Thus, Assertion A is true.

The small current in reverse bias is due to the flow of minority charge carriers, not majority charge carriers. The drastic increase in current at breakdown is due to the generation of a large number of electron-hole pairs (avalanche or Zener breakdown). Thus, Reason R is false.

Answer: A is true but R is false

</details>

---

### Q5. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the given circuit (shown in part (A)) the time dependent input voltage $v_{in}(t)$ and corresponding output $v_o(t)$ are shown in part (B) and part (C), respectively. Identify the components that are used in the circuit between points X and Y.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d1.png" />

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d2.png" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d3.png" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d4.png" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d5.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS1__q37_d3.png" />**

**Detailed Solution:**

Given: Input is an alternating voltage with peak values $+20$ V and $-20$ V. Output is clipped at $+5$ V and $-5$ V.

The existing branch (given in circuit) contains an ideal diode (anode down) in series with a Zener diode ($V_z = 5$ V).

During negative half cycle: The ideal diode is forward-biased, and the Zener diode is reverse-biased. When $|v_{in}| > 5$ V, the Zener breaks down, clipping the output at $-5$ V. So the existing branch handles the negative half cycle.

During positive half cycle: The ideal diode in the existing branch is reverse-biased, so that branch is open. The branch between X and Y must clip the output at $+5$ V.

For clipping at $+5$ V during the positive half cycle, the XY branch must have an ideal diode (anode towards X) in series with a Zener diode (cathode towards X, $V_z = 5$ V).

When $v_{in} > +5$ V: ideal diode is forward-biased, Zener is reverse-biased and clamps at $5$ V $\Rightarrow$ output clipped at $+5$ V.
When $v_{in}$ is negative: ideal diode is reverse-biased $\Rightarrow$ branch is open, leaving the existing branch to handle clipping.

This matches Option B.

</details>

---

### Q6. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Assuming in forward bias condition there is a voltage drop of 0.7 V across a silicon diode, the current through diode $D_{1}$ in the circuit is $\_\_\_\_$ mA. 
 (Assume all diodes in the given circuit are identical) 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S1_q_28_1.png">

**Options:**

- **(A)** 17.6
- **(B)** 18.8
- **(C)** 11.7
- **(D)** 20.15

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 18.8**

**Detailed Solution:**

$12 - 0.3 \times 10^3 I - 0.7 = 0$
$\dfrac{11.3}{0.3 \times 10^3} = I$
$37.66 \times 10^{-3} \text{ A} = I$
Current through diode $D_1$, $I_1 = I/2$
$I_1 = 18.83 \text{ mA}$

</details>

---

### Q7. JEE Main 2026 (24 January Shift 1)

*Type:* `numerical` | *Level:* `2`

A voltage regulating circuit consisting of Zener diode, having break-down voltage of 10 V and maximum power dissipation of 0.4 W, is operated at 15 V. The approximate value of protective resistance in this circuit is $\_\_\_\_$ $\Omega$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **125**

**Detailed Solution:**

The maximum current through the Zener diode is determined by its maximum power dissipation: $I_{Z,max} = \frac{P_{max}}{V_Z} = \frac{0.4}{10} = 0.04$ A.
The protective series resistance must limit the current such that the Zener operates safely. Using Ohm's law across the series resistance and Zener when the Zener carries maximum current:
$R_s = \frac{V_{in} - V_Z}{I_{Z,max}} = \frac{15 - 10}{0.04} = \frac{5}{0.04} = 125$ Ω

</details>

---

### Q8. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The following diagram shows a Zener diode as a voltage regulator. The Zener diode is rated at $V_{z}=5 \mathrm{~V}$ and the desired current in load is 5 mA. The unregulated voltage source can supply upto 25 V. Considering the Zener diode can withstand four times of the load current, the value of resistor $R_{S}$ (shown in circuit) should be $\_\_\_\_$ $\Omega$. <img style="width:400px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_q_30_1.png">

**Options:**

- **(A)** $100$
- **(B)** $1000$
- **(C)** $10$
- **(D)** None of the above

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of the above**

**Detailed Solution:**

This question has been dropped by NTA.

</details>

---

### Q9. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The output voltage in the following circuit is (Consider ideal diode case)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZKsOqC-gowCiBF4TaJ-89oqNcovTgj6QZDztv14gnbw.original.fullsize.png"/>

**Options:**

- **(A)** 10 V
- **(B)** 0 V
- **(C)** $+5 \mathrm{~V}$
- **(D)** $-5 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0 V**

**Detailed Solution:**

Here $D_1$ is reverse biased and $D_2$ is forward biased. Therefore current flow through $\mathrm{D}_{\mathrm{Q}}$ and 5 V drop on resistor.
So, $V_{\text {out }}=0$

</details>

---

### Q10. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the following circuit, the reading of the ammeter will be (Take Zener breakdown voltage $=4 \mathrm{~V})$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/sGxv5FrnhkvpyW0OSXU3y1vSAJybQ7hjewCTyPRPURA.original.fullsize.png"/>

**Options:**

- **(A)** 24 mA
- **(B)** 80 mA
- **(C)** 10 mA
- **(D)** 60 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 10 mA**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/RaxUT7pm499Pkoq5Vn3-Re6vWq3Q_DL1MZwjMgG3qHI.original.fullsize.png"/>
$\mathrm{V}_1=\frac{400}{100+400} \times 12 \mathrm{~V}=\frac{4}{5} \times 12=\frac{48}{5} \mathrm{~V}$
here, $\mathrm{V}_1 \gt \mathrm{V}_{\mathrm{z}},\left(\mathrm{V}_{\mathrm{z}}=\right.$ Zener Voltage $)$ So, Zener breakdown will be take place So, voltage across $400 \Omega$ will be 4 V
$\mathrm{I}=\frac{4}{400} \mathrm{~A}=\frac{1}{100 \mathrm{~A}}=10 \mathrm{~mA}$

</details>

---

### Q11. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A zener diode with 5 V zener voltage is used to regulate an unregulated dc voltage input of 25 V. For a $400 \Omega$ resistor connected in series, the zener current is found to be 4 times load current. The load current $\left(I_L\right)$ and load resistance $\left(R_{\mathrm{L}}\right)$ are :

**Options:**

- **(A)** $\mathrm{I}_{\mathrm{L}}=20 \mathrm{~mA} ; \mathrm{R}_{\mathrm{L}}=250 \Omega$
- **(B)** $\mathrm{I}_{\mathrm{L}}=10 \mathrm{~A} ; \mathrm{R}_{\mathrm{L}}=0.5 \Omega$
- **(C)** $\mathrm{I}_{\mathrm{L}}=0.02 \mathrm{~mA} ; \mathrm{R}_{\mathrm{L}}=250 \Omega$
- **(D)** $\mathrm{I}_{\mathrm{L}}=10 \mathrm{~mA} ; \mathrm{R}_{\mathrm{L}}=500 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{I}_{\mathrm{L}}=10 \mathrm{~mA} ; \mathrm{R}_{\mathrm{L}}=500 \Omega$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/E1DaBwaY9RYop0gfVIxQTMjj9dK_lflcbja14DhX6as.original.fullsize.png"/>
From the circuit diagram,
$\begin{aligned}
& 5 \mathrm{i}=\frac{20}{400}=\frac{1}{20} \mathrm{~A} \\
& \therefore \mathrm{i}=\frac{1}{100} \mathrm{~A}=10 \mathrm{~mA}=\text { Load current }
\end{aligned}$
Also, $\mathrm{V}_{\mathrm{L}}=5 \mathrm{~V}$
$\therefore \mathrm{R}_{\mathrm{L}}=\frac{5}{10 \times 10^{-3}} \Omega=500 \Omega$

</details>

---

### Q12. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jmq1V0CPY2x14ini5fEh85Olp0qrYB_QPZ6_USp6tF4.original.fullsize.png"/>


In the circuit shown here, assuming threshold voltage of diode is negligibly small, then voltage $V_{A B}$ is correctly represented by :

**Options:**

- **(A)** $\mathrm{V}_{\mathrm{AB}}$ would be zero at all times
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/nfgosFWrTC5JlgymP4pgm61Na-jKLdMwJW8WKLPbSCo.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/psVBiWklYsuLMjVeozLus4ezpIHpl4M7o6jOQUy9yjw.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/m3w26ehAWUDQ1tz-7r8GdDSyGOlSDqzZVX5nVkqgYHc.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/m3w26ehAWUDQ1tz-7r8GdDSyGOlSDqzZVX5nVkqgYHc.original.fullsize.png"/>**

**Detailed Solution:**

$\mathrm{V}=\mathrm{V}_0 \sin \omega \mathrm{t}$


<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NW1F5kttZbDyex6FTbHA8l8TX1EDYD2LBf7WDBeCCx0.original.fullsize.png">

</details>

---

### Q13. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Refer to the circuit diagram given in the figure. which of the following observations are correct?
A. Total resistance of circuit is $6 \Omega$
B. Current in Ammeter is 1 A
C. Potential across $A B$ is 4 Volts.
D. Potential across CD is 4 Volts
E. Total resistance of the circuit is $8 \Omega$.

Choose the correct answer from the options given below:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/B_NrMfkxxosqTaVE7_gmT0JGEy5nZC3XdzT1S9fucsY.original.fullsize.png"/>

**Options:**

- **(A)** A, B and D Only
- **(B)** A, B and C Only
- **(C)** A, C and D Only
- **(D)** B, C and E Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A, B and D Only**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qn3ddbVvHjeXY2VeOJLj5XLrgfAmSZrCnWqMYpIgFIU.original.fullsize.png">




Current through ammeter $=1 \mathrm{~A}$
$\mathrm{R}_{\mathrm{net}}=6 \Omega$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Q2S2VlVEdxNTLTKQt0VZGFgiF9jzT_bbdr9ZKCjIx6w.original.fullsize.png">


$\begin{aligned}
& \mathrm{V}_{\mathrm{AB}}=0.5 \times 4=2 \mathrm{volt} \\
& \mathrm{~V}_{\mathrm{CD}}=1 \times 4=4 \mathrm{volt}
\end{aligned}$

A, B & D are correct

</details>

---

### Q14. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following circuits represents a forward biased diode?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/AMRRk4NBqCMXikFrDC9Br7IKgq2nLw1GJvLyb_xX-g0.original.fullsize.png"/>

Choose the correct answer from the options given below :

**Options:**

- **(A)** (A) and (D) only
- **(B)** (B), (D) and (E) only
- **(C)** (C) and (E) only
- **(D)** (B), (C) and (E) only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (B), (C) and (E) only**

**Detailed Solution:**

For forward bias potential of $p$ side should be higher than $n$ side.

</details>

---

### Q15. JEE Main 2024 (08 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

A potential divider circuit is connected with a dc source of $20 \mathrm{~V}$, a light emitting diode of glow in voltage $1.8 \mathrm{~V}$ and a zener diode of breakdown voltage of $3.2 \mathrm{~V}$. The length (PR) of the resistive wire is $20 \mathrm{~cm}$. The minimum length of PQ to just glow the LED is _____$\mathrm{cm}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Gs54MkZHGs-Hmq-BGuX7Sa_pekl5WoGjbt1SfdsTIGk.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cu0yMLKAe8WiY5oZTuqwakkXoS62JacOiWClBcXmLtw.original.fullsize.png">
$\begin{aligned} & \mathrm{PR}=20 \mathrm{~cm} \\ & \mathrm{~V}_{\mathrm{PQ}}=\frac{1}{4} \times \mathrm{R}_{\mathrm{PR}} \\ & \ell_{\min }(\mathrm{PQ})=\frac{1}{4} \times 20 \\ & =5 \mathrm{~cm}\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Which of the diode circuit shows correct biasing used for the measurement of dynamic resistance of p-n junction diode :

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-y2ZguBDcpN3-WLAiuNZyZMYYO3ya8CQ4I0t65scmSE.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b86B4UBPR4I5Pu1ZHloz35XrZUCoxM2gWN_hFCkbLI8.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qlFGog0jcuY4OghkphKfJuZu7cRWgebn7U8_bBxKXEg.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d6I8a8kKdG-44W8wvxOxbGsvc5rpLeG1-LVZN9dy7YE.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qlFGog0jcuY4OghkphKfJuZu7cRWgebn7U8_bBxKXEg.original.fullsize.png"/>**

**Detailed Solution:**

Diode should be in forward biased to calculate dynamic resistance.

</details>

---

### Q17. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of net resistance of the network as shown in the given figure is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dPFlpDL1gaVTjhnh3WmsaAQ8425FRvppm1-Iw13A6Ms.original.fullsize.png">

**Options:**

- **(A)** $6 \Omega$
- **(B)** $(5 / 2) \Omega$
- **(C)** $(15 / 4) \Omega$
- **(D)** $(30 / 11) \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6 \Omega$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yBOlssAOZoI28FJtkwlk0QgzgWMhmhPZC4So51uWQG0.original.fullsize.png">
Diode 2 is in reverse bias
So current will not flow in branch of $2^{\text {nd }}$ diode, So we can assume it to be broken wire.
Diode 1 is in forward bias
So it will behave like conducting wire. So new circuit will be<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Lia0N2rSLP84bAbXzbn0MdeewAQxK_Lj9SsVczbTn8M.original.fullsize.png">

</details>

---

### Q18. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the given circuit if the power rating of Zener diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>mW</mi></math>, the value of series resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub></math> to regulate the input unregulated supply is:</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b28eaad7-4dfa-4b5a-bcc0-7bb64182811c.png" style="width: 400px; height: 173px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac><mo> </mo><mi>k</mi><mi>Ω</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>Ω</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi>k</mi><mi>Ω</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>k</mi><mi>Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac><mo> </mo><mi>k</mi><mi>Ω</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d25c5b36-e00f-48f8-aefd-2b3d6d6e3bfc.png" style="width: 350px; height: 150px;"/></p><p>Potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>=</mo><mn>8</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">V</mi></math></p><p>Current through the load resistor</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>5</mn><mrow><mn>1</mn><mo>×</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>5</mn><mo> </mo><mi>mA</mi></math></p><p>Maximum current through Zener diode</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>Z</mi><mo>,</mo><mo> </mo><mi>max</mi></mrow></msub><mo>=</mo><mfrac><mn>10</mn><mn>5</mn></mfrac><mo>=</mo><mn>2</mn><mo> </mo><mi>mA</mi></math></p><p>And minimum current through Zener diode</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>Z</mi><mo>,</mo><mo> </mo><mi>min</mi></mrow></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo> </mo><msub><mi>I</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>max</mi></mrow></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>2</mn><mo>=</mo><mn>7</mn><mi>m</mi><mi>A</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>min</mi></mrow></msub><mo>=</mo><mfrac><msub><mi>V</mi><mn>1</mn></msub><msub><mi>I</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>max</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mi>k</mi><mi>Ω</mi></math></p><p>Similarly,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>min</mi></mrow></msub><mo>=</mo><mn>5</mn><mo> </mo><mi>mA</mi></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>max</mi></mrow></msub><mo>=</mo><mfrac><msub><mi>V</mi><mn>1</mn></msub><msub><mi>I</mi><mrow><mi>S</mi><mo>,</mo><mo> </mo><mi>min</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo> </mo><mi>k</mi><mi>Ω</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∴</mo><mo> </mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mi>k</mi><mi>Ω</mi><mo>&lt;</mo><msub><mi>R</mi><mi>s</mi></msub><mo>&lt;</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mi>k</mi><mi>Ω</mi></math></p>

</details>

---

### Q19. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the given circuit, the voltage across load resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msub><mi>R</mi><mi>L</mi></msub><mo>)</mo></math> is:</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2f96fae3-9f04-4396-8891-8e5c304b0f9d.png" style="width: 350px; height: 161px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>75</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mn>9</mn><mo>.</mo><mn>00</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>50</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.</mo><mn>00</mn><mo> </mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>75</mn><mo> </mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6359c29b-4b03-4bca-8c6d-7bf1bcb624ec.png" style="width: 350px; height: 176px;"/></p><p>Both diodes are in forward bias. In forward bias, potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>e</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mi>i</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">V</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mn>0</mn><mo>.</mo><mn>7</mn><mo> </mo><mi mathvariant="normal">V</mi></math> respectively.</p><p>Therefore, current in the circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mrow><mn>15</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>7</mn></mrow><mrow><mn>4</mn><mo>×</mo><mn>1000</mn></mrow></mfrac><mo>=</mo><mn>3</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>mA</mi></math></p><p>Required potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub></math>, 
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mi>i</mi><msub><mi>R</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mfenced><mrow><mn>3</mn><mo>.</mo><mn>5</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mo>×</mo><mfenced><mrow><mn>2</mn><mo>.</mo><mn>5</mn><mo>×</mo><mn>1000</mn></mrow></mfenced><mo> </mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>.</mo><mn>75</mn><mo> </mo><mi mathvariant="normal">V</mi><mo> </mo></math></p></blockquote>

</details>

---

### Q20. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A Zener diode of breakdown voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi mathvariant="normal">V</mi></math> is used as a voltage regulator as shown in the figure. The current through the Zener diode is</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/35e1f014-096a-4084-ad44-f50e45a4999c.png" style="width: 300px; height: 185px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo> </mo><mi>mA</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo> </mo><mi>mA</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo> </mo><mi>mA</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo> </mo><mi>mA</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/955e162a-ed23-4ea4-a99d-7fb69927fbd4.png" style="width: 250px; height: 154px;"/></p><p>As Zener is in breakdown region, therefore potential drop across it would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi mathvariant="normal">V</mi></math>. Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>10</mn><mn>500</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>50</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>10</mn><mn>200</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><msub><mi>I</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>20</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>50</mn></mfrac></mrow></mfenced><mo>=</mo><mfenced><mfrac><mn>3</mn><mn>100</mn></mfrac></mfenced><mo> </mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>30</mn><mo> </mo><mi>mA</mi></math></p>

</details>

---

### Q21. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the given circuit, the breakdown voltage of the Zener diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo> </mo><mi mathvariant="normal">V</mi></math>. What is the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>z</mi></msub></math> ?</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5186ad56-edfe-4ba3-a227-401a943696b5.png" style="width: 350px; height: 235px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>3</mn><mo> </mo><mi>mA</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>mA</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>mA</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo> </mo><mi>mA</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>mA</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b363b48-3941-41b4-9005-f38115f9ef53.png" style="width: 350px; height: 233px;"/></p><p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>z</mi></msub><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">V</mi></math></p><p>Let potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
Potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mfenced><msub><mi>V</mi><mi>E</mi></msub></mfenced><mo>=</mo><mn>10</mn><mo> </mo><mi mathvariant="normal">V</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>C</mi></msub><mo>=</mo><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">V</mi></math> and,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>z</mi></msub><mo>+</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mi>I</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>The current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo> </mo><mi>kΩ</mi></math> resistor is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>I</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>10</mn><mo>-</mo><mn>3</mn></mrow><mn>1000</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>7</mn><mn>1000</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></mtd></mtr></mtable></math></p><p>From the diagram, it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>2000</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></math></p><p>Therefore, from equation (1), it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mi>z</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>7</mn><mo>-</mo><mn>1</mn><mo>.</mo><mn>5</mn></mrow><mn>1000</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>5</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>mA</mi></mtd></mtr></mtable></math></p>

</details>

---

### Q22. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which of the following circuits is reverse - biased ?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/763e317a-39cf-46e1-a4c2-e1c3f2c5e846.png" style="width: 220px; height: 85px;"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1dc8f7bb-bed2-4638-a8f2-05d0524b278c.png" style="width: 190px; height: 208px;"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/74c01d41-a461-445a-a2d5-3cd4f2eade94.png" style="width: 190px; height: 179px;"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cfe98b54-2f84-4ac1-9729-0f2201cb97db.png" style="width: 263px; height: 81px;"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cfe98b54-2f84-4ac1-9729-0f2201cb97db.png" style="width: 263px; height: 81px;"/>**

**Detailed Solution:**

<p>Reverse biasing in a PN-junction occurs when an external voltage is applied in such a way that the positive terminal of the voltage source is connected to the N-type semiconductor, and the negative terminal is connected to the P-type semiconductor.</p><p>In other words, if the potential of the P-side is less than that of the N-side of the junction, the diode is said to be in the reverse bias condition.</p><p>Amongst the given configurations, this is the correct one which indicates the reverse biasing of the diode.</p>

</details>

---

### Q23. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>If each diode has a forward bias resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mi mathvariant="normal">&#937;</mi></math>  in the below circuit,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/93440fc5-27b1-40a8-9900-c97083042a6b.png" style="width: 300px; height: 240px;" /></p><p>Which of the following options is correct?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><msub><mi mathvariant="normal">I</mi><mn>3</mn></msub></mfrac><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>3</mn></msub><msub><mi mathvariant="normal">I</mi><mn>4</mn></msub></mfrac><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>As the diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mn>2</mn></msub></math> is connected in reverse order, there is no current through it.</p><p>The effective resistances of the circuit can, then, be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>R</mi><mrow><mi>e</mi><mi>f</mi><mi>f</mi></mrow></msub></mtd><mtd><mo>=</mo></mtd><mtd><mn>25</mn><mo>+</mo><mfrac><msup><mfenced><mrow><mn>25</mn><mo>+</mo><mn>125</mn></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mn>25</mn><mo>+</mo><mn>125</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>25</mn><mo>+</mo><mn>125</mn></mrow></mfenced></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mtd></mtr></mtable></math></p><p>Each current through the diodes can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>1</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfenced><mfrac><mrow><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mtd></mtr></mtable></math></p><p>As the diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mn>2</mn></msub></math> is non-conducting, the current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> will be divided equally among the other two diodes <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">D</mi><mn>3</mn></msub></math>.</p><p>Hence, the currents in the diodes can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>I</mi><mn>2</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mn>2</mn></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>025</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mtd></mtr><mtr><mtd><msub><mi>I</mi><mn>4</mn></msub></mtd><mtd><mo>=</mo></mtd><mtd><mn>0</mn><mo>.</mo><mn>025</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mtd></mtr></mtable></math></p><p>Thus,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><msub><mi>I</mi><mn>1</mn></msub><msub><mi>I</mi><mn>2</mn></msub></mfrac></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow><mrow><mn>0</mn><mo>.</mo><mn>025</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mn>2</mn></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q24. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A zener diode of power rating <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math> is to be used as voltage regulator. If the zener diode has a breakdown of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and it has to regulate voltage fluctuating between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> The value of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub></math> for safe operation of diode will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/539c014a-1ecc-4a04-8177-48b40e89cf0b.png" style="width: 250px; height: 126px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/24198823-94f8-4eb6-8900-a3e104982ec8.png" style="width: 250px; height: 171px;" /></p><p>Power rating of zener diode <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p><p>From the diagram above,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>V</mi><mi>B</mi></msub><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Power is given by</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>V</mi><mi>i</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>i</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></mrow><mrow><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>C</mi></msub><mo>-</mo><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>-</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Thus, using Ohm&#39;s law,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q25. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Choose the correct statement about Zener diode:

**Options:**

- **(A)** It works as a voltage regulator in reverse bias and behaves like simple p-n junction diode in forward bias
- **(B)** It works as a voltage regulator in both forward and reverse bias
- **(C)** It works a voltage regulator only in forward bias
- **(D)** It works as a voltage regulator in forward bias and behaves like simple p-n junction diode in reverse bias

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) It works as a voltage regulator in reverse bias and behaves like simple p-n junction diode in forward bias**

**Detailed Solution:**

<p>Zener diode is a special type of p-n junction diode.</p><p>In a p-n junction diode, the majority carriers in p-side are the holes and that in n-side are the electrons. When a p-n junction diode is connected in such a way that the p-side is connected to the positive terminal and the n-side is connected to the negative terminal of a battery, there is a flow of current through the circuit. This condition is known as the forward bias condition of the junction.</p><p>If the connections are made in the opposite order, there is very less current that can pass through the p-n junction diode. This is called the reverse bias condition.</p><p>A Zener diode works in a reverse bias condition. It works in breakdown region of the applied voltage as a voltage regulator. Hence, it can act as simple p-n junction in forward bias</p>

</details>

---

### Q26. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi mathvariant="normal">V</mi></math> Zener diode along with a series resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is connected across a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> supply (as shown in the figure). If the maximum Zener current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math>, then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/21f9da59-2641-4db6-9b82-354f5b5df9cb-image.png" style="width: 200px; height: 113px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **480**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> be the current through Zener diode and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub></math> through load resistor.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ef504f92-3f59-4766-9a84-88bdc675e581-image.png" style="width: 330px; height: 180px;" />​​​​​​​</p><p>As maximum current flows through Zener diode, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&there4;</mo></math>Maximum current, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mn>25</mn><mo> </mo><mi>mA</mi><mo>+</mo><mn>0</mn><mo>=</mo><mn>25</mn><mo> </mo><mi>mA</mi></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>o</mi></msub></math> is voltage drop across Zener <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo> </mo><mi mathvariant="normal">V</mi></math>. 
Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is maximum, hence minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><msub><mi>V</mi><mi>i</mi></msub><mo>-</mo></mrow><mrow><msub><mi>V</mi><mi>o</mi></msub></mrow><mi>I</mi></mfrac><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mn>8</mn></mrow><mrow><mn>25</mn><mo>&times;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>480</mn><mo> </mo><mi mathvariant="normal">&Omega;</mi></math></p></blockquote>

</details>

---

### Q27. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the potential barrier across a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. Then the electric field intensity, in the depletion region having the width of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></math>, will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c2ebe4af-6607-4b24-b43e-127e15fc0295-image.png" style="width: 220px; height: 138px;" /></p><p>Electric field intensity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mi>V</mi><mi>d</mi></mfrac><mo>=</mo><mfrac><mrow><mi>Potential</mi><mo>&#160;</mo><mi>barrier</mi><mo>&#160;</mo><mi>across</mi><mo>&#160;</mo><mi>junction</mi></mrow><mrow><mi>width</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><mi>depletion</mi><mo>&#160;</mo><mi>region</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">N</mi><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q28. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>In the circuit shown below, maximum Zener diode current will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8442604a-603c-487b-8d83-64ed57722a78-image.png" style="width: 300px; height: 126px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<blockquote><p><meta charset="utf-8" /><meta charset="utf-8" /><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3842b7f0-258b-4c55-87b8-6a30988fe1aa-image.png" style="width: 350px; height: 143px;" /><b>​​​​​​​</b></p><p>Current through load resistor is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>L</mi></msub><mo>=</mo><mfrac><mrow><mn>60</mn><mo> </mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>10000</mn><mo> </mo><mi mathvariant="normal">&Omega;</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>006</mn><mo> </mo><mi mathvariant="normal">A</mi></math> and current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4000</mn><mo> </mo><mi mathvariant="normal">&Omega;</mi></math> resistor is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>120</mn><mo>-</mo><mn>60</mn></mrow></mfenced><mo> </mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>4000</mn><mo> </mo><mi mathvariant="normal">&Omega;</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>015</mn><mo> </mo><mi mathvariant="normal">A</mi></math></p><p>Thus, maximum current through Zener diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>Z</mi></msub><mo>=</mo><mi>I</mi><mo>-</mo><msub><mi>I</mi><mi>L</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>015</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>006</mn><mo>=</mo><mn>0</mn><mo>.</mo><mn>009</mn><mo> </mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>9</mn><mo> </mo><mi>mA</mi></math></p></blockquote>

</details>

---

### Q29. JEE Main 2022 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>Two ideal diodes are connected in the network as shown in figure. The equivalent resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#937;</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/88936a04-311c-4f66-bd90-57e9192bb2f8-1.jpg" style="width: 307px; height: 172px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<blockquote><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is connected to a higher potential compared to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>, then left diode will be in forward bias and hence will not offer any resistance also the right diode will be in reverse bias and hence it will behave as open key. Therefore, the modified circuit will be as given below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1bbf1f27-410c-4c1d-bed2-0b24ab7552ed-2.jpg" style="width: 311px; height: 173px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Equivalent resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>20</mn><mn>2</mn></mfrac><mo>+</mo><mn>15</mn><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q30. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

A potential barrier of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> exists across a p-n junction. An electron enters the junction from the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-side with a speed of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>0</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The speed with which electron enters the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> side will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>x</mi><mn>3</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><msup><mrow><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____.: (Given mass of electron <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi></math>, charge on electron <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">C</mi></math>.)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f2dc0f8b-694a-4466-82e3-15f4bcc6683a-image.png" style="width: 220px; height: 156px;" /></p><p>Applying conservation of energy</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>e</mi><msub><mi>V</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msubsup><mi>v</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mo>-</mo><mi>e</mi><msub><mi>V</mi><mi>p</mi></msub><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup></math></p><p>We know, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>n</mi></msub><mo>-</mo><msub><mi>V</mi><mi>p</mi></msub><mo>=</mo></math>potential barrier<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Then, we have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>e</mi><mfenced><mrow><msub><mi>V</mi><mi>n</mi></msub><mo>-</mo><msub><mi>V</mi><mi>p</mi></msub></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msubsup><mi>v</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>m</mi><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>1</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><mo>&#215;</mo><mn>36</mn><mo>&#215;</mo><msup><mn>10</mn><mn>10</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><msubsup><mrow><mo>&#160;</mo><mi mathvariant="normal">v</mi></mrow><mi>f</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>64</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>+</mo><mn>1</mn><mo>.</mo><mn>62</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>98</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>19</mn></mrow></msup><mo>=</mo><mn>4</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>31</mn></mrow></msup><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>v</mi><mi>f</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>98</mn><mo>&#215;</mo><msup><mn>10</mn><mn>12</mn></msup></mrow><mrow><mn>4</mn><mo>.</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>v</mi><mi>f</mi></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>466666</mn><mo>&#215;</mo><msup><mn>10</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>.</mo><mn>6666</mn><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mfrac><mn>14</mn><mn>3</mn></mfrac><mo>&#215;</mo><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi mathvariant="normal">m</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q31. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A Zener of breakdown voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>Z</mi></msub><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and maximum Zener current, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>ZM</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>mA</mi></math> is subjected to an input voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>i</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> with series resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. In the given circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi mathvariant="normal">L</mi></msub></math> represents the variable load resistance. The ratio of maximum and minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub></math> is _____ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e4e916d1-1489-4802-9b5b-fbb0a93297a8-image.png" style="width: 400px; height: 170px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>Minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub></math> for which the diode is shorted is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mi>L</mi></msub><mrow><msub><mi>R</mi><mi>L</mi></msub><mo>+</mo><mn>100</mn></mrow></mfrac><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>8</mn><mo>&#8658;</mo><msub><mi>R</mi><mi>L</mi></msub><mo>=</mo><mn>400</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>For maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub></math>, current through diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi mathvariant="normal">R</mi></msub><mo>=</mo><msub><mi>i</mi><msub><mi mathvariant="normal">R</mi><mi mathvariant="normal">L</mi></msub></msub><mo>+</mo><msub><mi>I</mi><mi>ZM</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>100</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><msub><mi>R</mi><mi mathvariant="normal">L</mi></msub></mfrac><mo>+</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>=</mo><mfrac><mn>8</mn><msub><mi>R</mi><mi mathvariant="normal">L</mi></msub></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>R</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mn>800</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mi>Lmax</mi></msub><msub><mi>R</mi><mi>Lmin</mi></msub></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q32. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>In the given circuit the input voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>in</mi><mo>&#160;</mo></mrow></msub></math> is shown in figure. The cut-in voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction diode (<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math>) is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. Which of the following output voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>V</mi><mn>0</mn></msub></mfenced></math> waveform across the diode is correct?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5d75a0e0-485c-4ea1-972d-5e4d5fa8257f-image.png" style="width: 560px; height: 142px;" /></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70a53c50-18fb-4f37-9359-3dbc92da8e46-image.png" style="width: 180px; height: 102px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/28885ab6-65bf-4bb7-8b75-e860075a04c0-image.png" style="width: 180px; height: 103px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/267cea6a-e040-48b4-b672-d278ff042f0a-image.png" style="width: 210px; height: 113px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/200f306b-f17a-4240-8f7e-0caf63d3fafc-image.png" style="width: 210px; height: 112px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/200f306b-f17a-4240-8f7e-0caf63d3fafc-image.png" style="width: 210px; height: 112px;" />**

**Detailed Solution:**

<p>During the positive half cycle of the input waveform, diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> is forward biased and diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> is reverse biased. Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> appears across the output as the diode is conducting. During negative half cycle the diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> is reverse biased and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> is forward biased, so, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> appears across the output as the diode is conducting in negative direction. This circuit can be used as a voltage limiter. This circuit will not allow any voltage above <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>and below <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p>Hence, the output waveform is </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/200f306b-f17a-4240-8f7e-0caf63d3fafc-image.png" style="width: 210px; height: 112px;" /></p>

</details>

---

### Q33. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For using a multimeter to identify diode from electrical components, choose the correct statement out of the following about the diode

**Options:**

- **(A)** It is two terminal device which conducts current in both directions.
- **(B)** It is two terminal device which conducts current in one direction only
- **(C)** It does not conduct current gives an initial deflection which decays to zero.
- **(D)** It is three terminal device which conducts current in one direction only between central terminal and either of the remaining two terminals

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) It is two terminal device which conducts current in one direction only**

**Detailed Solution:**

A diode is a two-terminal device that conducts current in forward bias and does not conduct current in reverse bias i.e. it conducts current in one direction only.

</details>

---

### Q34. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>The cut-off voltage of the diodes (shown in figure) in forward bias is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The current through the resister of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mi mathvariant="normal">&#937;</mi></math> is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c75faf00-65b9-40c2-923e-46d06cab17a6-image.png" style="width: 250px; height: 154px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Here diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> is forward biased and diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> is reverse biased.</p><p>So, no current will flow through diode <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> resistor.</p><p>Current through the resistor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>6</mn></mrow><mrow><mn>60</mn><mo>+</mo><mn>40</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>4</mn></mrow><mn>100</mn></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q35. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>As per the given circuit, the value of current through the battery will be _____ A.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9518db1d-9c7e-494a-ab9a-77517b6ea6ee-image.png" style="width: 220px; height: 142px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9518db1d-9c7e-494a-ab9a-77517b6ea6ee-image.png" style="width: 220px; height: 142px;" /></p><p>In the given circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> will be reverse biased and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>D</mi><mn>3</mn></msub></math> will be forward biased. Therefore,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cdc8d630-c06d-4e87-aa0c-5dbc2f3682b5-image.png" style="width: 160px; height: 126px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>16</mn><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>10</mn><mn>10</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q36. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>-</mo><mi mathvariant="normal">V</mi></math> characteristics of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction diode in forward bias is shown in the figure. The ratio of dynamic resistance, corresponding to forward bias voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> respective is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41e3a4ad-f94b-4662-a6a4-de8085e81d64-image.png" style="width: 260px; height: 166px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>40</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>:</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Dynamic resistance of a diode is defined as, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mo>&#8710;</mo><mi>V</mi></mrow><mrow><mo>&#8710;</mo><mi>i</mi></mrow></mfrac></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41e3a4ad-f94b-4662-a6a4-de8085e81d64-image.png" style="width: 250px; height: 159px;" /></p><p>At forward bias voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mo>&#8710;</mo><mi>V</mi></mrow><mrow><mo>&#8710;</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>.</mo><mn>1</mn><mo>-</mo><mn>2</mn></mrow><mrow><mfenced><mrow><mn>10</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>At forward bias voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mo>&#8710;</mo><mi>V</mi></mrow><mrow><mo>&#8710;</mo><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>.</mo><mn>2</mn><mo>-</mo><mn>4</mn></mrow><mrow><mfenced><mrow><mn>250</mn><mo>-</mo><mn>200</mn></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.</p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mn>20</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>1</mn></mfrac></math></p>

</details>

---

### Q37. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>In the given circuit, the value of current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>L</mi></msub></math> will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi><mo>.</mo></math> (When <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>k&#937;</mi></math>)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1425653d-60d7-47c8-9206-b982f09de4cf-image.png" style="width: 270px; height: 115px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a33da0a9-a0a7-4486-93be-1eef8459638c-image.png" style="width: 300px; height: 121px;" /></p><p>Potential drop across the branch containing load resistance will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> due to Zener diode. Therefore, potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>800</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>-</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p>Now, current through battery will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>5</mn><mn>800</mn></mfrac><mo>&#215;</mo><mn>1000</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>Current through load will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>L</mi></msub><mo>=</mo><mfrac><mn>5</mn><mn>1000</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q38. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>In the given figure, each diode has a forward bias resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and infinite resistance in reverse bias. The current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> will be :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dec4f262-5c6a-4db6-91b3-14f9fab8b74c-image.png" style="width: 275px; height: 373px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>75</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>73</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>35</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c9554d63-cbdc-40f0-91b2-00e92923a8ec-image.png" style="width: 274px; height: 373px;" /></p><p>We know that in reverse bias ideal diode does not pass current it only works in forward bias so, the current in the third branch is zero, it means the net resistance of the upper two branch is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>160</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>160</mn></mfrac><mo>&#8658;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><msub><mo>'</mo><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mn>80</mn><mo>+</mo><mn>20</mn><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>i</mi><mo>=</mo><mfrac><mn>200</mn><mn>100</mn></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q39. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>B</mi></msub></math> are the input voltages (either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>) and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>0</mn></msub></math> is the output voltage then the two gates represented in the following circuits <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> are :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/980f5d53-99af-4390-8533-f958bc16d3db-image.png" style="width: 680px; height: 325px;" />

**Options:**

- **(A)** OR and NOT Gate
- **(B)** AND and NOT Gate
- **(C)** AND and OR Gate
- **(D)** NAND and NOR Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR and NOT Gate**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fa9cf094-f106-4cca-abaa-eb938d76a6c2-image.png" style="width: 232px; height: 156px;" />
In the above circuit is we are applying high voltage in any one of the diodes or in both diodes simultaneously then we get a high out due to forward biasing of diode while we are applied low voltage in both the diode then we get low voltage so this is like OR gate. </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/807b9505-21fc-4a56-9268-f3e59f252d57-image.png" style="width: 321px; height: 278px;" /></p><p>In the above circuit which is an NPN transistor in a common emitter configuration having a phase difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn><mo>&#176;</mo></math> between input voltage and output voltage, when we are applied high voltage then we get low voltage vice-versa so, the circuit is the same as NOT gate.</p>

</details>

---

### Q40. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Choose the correct waveform that can represent the voltage across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> of the following circuit, assuming the diode is ideal one:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73fb6064-ee17-442d-b27e-5837b9b1e678-image.png" style="width: 300px; height: 161px;" />

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f2ea40b-8432-4841-b444-07862a879c1a-image.png" style="width: 250px; height: 145px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dee2a58b-f906-4eb8-90bd-90e246e59ab3-image.png" style="width: 250px; height: 143px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/460a87f4-4939-4447-bba2-52fdff8cf3e4-image.png" style="width: 250px; height: 150px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3e3e9dc5-e085-4b11-a91b-94add380c97a-image.png" style="width: 250px; height: 141px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f2ea40b-8432-4841-b444-07862a879c1a-image.png" style="width: 250px; height: 145px;" />**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8b573908-3674-4149-b5b8-e95f043c0b94-image.png" style="width: 360px; height: 167px;" /></p><p>Current will flow from the diode when diode is in forward biased.
Thus <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>V</mi><mo>=</mo><mo>(</mo><mn>10</mn><mi>sin</mi><mi>&#969;</mi><mi>t</mi><mo>-</mo><mn>3</mn><mo>)</mo><mi>V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>V</mi></math> will be &#39;zero&#39;, when diode is reverse biased.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/97122452-6d13-4c9a-ae23-4e7e65b55c2d-image.png" style="width: 300px; height: 156px;" /></p>

</details>

---

### Q41. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A zener diode of power rating <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math> is to be used as a voltage regulator. If the zener diode has a breakdown of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and it has to regulate voltage fluctuated between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub></math> for safe operation should be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#937;</mi></math> .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8433487d-7b09-455a-a663-d2fd4ae913eb-16de8932-8de0-400a-8197-5cbe63710257-image.png" style="width: 300px; height: 138px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p>For diode <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>V</mi><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mo>=</mo><mfrac><mi mathvariant="normal">P</mi><mi mathvariant="normal">V</mi></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>10</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">s</mi></msub><mo>=</mo><mn>14</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Voltage drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mi>s</mi></msub><mo>=</mo><mn>14</mn><mo>-</mo><mn>10</mn><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi><mo>=</mo><msub><mi>iR</mi><mi mathvariant="normal">s</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mi>s</mi></msub><mo>=</mo><mfrac><mn>4</mn><mrow><mn>0</mn><mo>.</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi>&#937;</mi></math></p>

</details>

---

### Q42. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>A circuit is arranged as shown in figure. The output voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>o</mi></msub></math> is equal to __________ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3a282190-1fa9-40f3-b758-2986aa08e50a-image.png" style="width: 343px; height: 196px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6d8624fe-55db-40dd-b01a-9b7f98cf326a-image.png" style="width: 342px; height: 193px;" /></p><p>Diodes are forward biased, so they act as wire so input current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> as input source is short circuited output current is also zero, as input current is zero</p><p>Now, output voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q43. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>For the given circuit, the power across zener diode is _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mW</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7bdb8802-e4d9-4f1e-bfc1-c36a8dc98be1-image.png" style="width: 400px; height: 148px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **120**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e8199f33-f588-4cdc-96dd-dbf4a87f3bf1-image.png" style="width: 380px; height: 166px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>14</mn><mrow><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>14</mn><mo>&#160;</mo><mi>mA</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>10</mn><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi>mA</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>-</mo><msub><mi mathvariant="normal">i</mi><mn>3</mn></msub><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>Power consumed in zener diode</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi mathvariant="normal">V</mi><mo>&#215;</mo><mi mathvariant="normal">i</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>=</mo><mn>120</mn><mo>&#160;</mo><mi>mW</mi></math></p>

</details>

---

### Q44. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>In a given circuit diagram, a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> zener diode along with a series resistance is connected across a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> power supply. The minimum value of the resistance required, if the maximum zener current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#160;</mo><mi>mA</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="bottom"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></menclose></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#937;.</mtext></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b91cb447-5427-4cd7-851a-3be7e131d972-image.png" style="width: 433px; height: 192px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **500**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b91cb447-5427-4cd7-851a-3be7e131d972-image.png" style="width: 433px; height: 192px;" /></p><p>Voltage across, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>5</mn><msub><mi>R</mi><mi mathvariant="italic">L</mi></msub></mfrac></math></p><p>Also, voltage across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>50</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>45</mn></math> volt</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>v</mi><mo>=</mo><mi>i</mi><mi>R</mi><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><mi>v</mi><mi>i</mi></mfrac><mo>=</mo><mfrac><mn>45</mn><mrow><msub><mi>i</mi><mi mathvariant="italic">i</mi></msub><mo>+</mo><msub><mi>i</mi><mn>2</mn></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mn>45</mn><mrow><mn>90</mn><mi>m</mi><mi>A</mi><mo>+</mo><mfrac><mn>5</mn><msub><mi>R</mi><mi>L</mi></msub></mfrac></mrow></mfrac></math></p><p>Current in zener diode is maximum when <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>L</mi></msub><mo>&#8594;</mo><mo>&#8734;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close=""><mrow><msub><mi>i</mi><mn>2</mn></msub><mo>&#8594;</mo><mn>0</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open=""><mrow><msub><mi>i</mi><mi>i</mi></msub><mo>=</mo><mi>i</mi></mrow></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mn>45</mn><mrow><mn>90</mn><mo>&#160;</mo><mi>mA</mi></mrow></mfrac><mo>=</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q45. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>For the forward biased diode characteristics shown in the figure, the dynamic resistance at <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi>D</mi></msub><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>mA</mi></math> will be ________<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e1fcf718-3c47-468d-893f-3e71e7965e5f-image.png" style="width: 400px; height: 306px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>d</mi></msub><mo>=</mo><mfrac><mrow><mi>d</mi><mi>V</mi></mrow><mrow><mi>d</mi><mi>i</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mfenced><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>v</mi></mrow></mfrac></mfenced></mfrac><mo>=</mo><mfrac><mn>1</mn><mfenced><mfrac><mrow><mn>5</mn><mo>-</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow><mrow><mn>0</mn><mo>.</mo><mn>75</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>65</mn></mrow></mfrac></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>100</mn><mn>4</mn></mfrac><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q46. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A zener diode having zener voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi>V</mi></math> and power dissipation rating of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>W</mi></math> is connected across a potential divider arranged with maximum potential drop across zener diode is as shown in the diagram. The value of protective resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>p</mi></msub></math> is _____<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a152405f-d08f-40c7-b1da-6433f0171521-image.png" style="width: 230px; height: 235px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **192**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>V</mi><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>=</mo><mn>8</mn><mi>i</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>&#160;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mn>20</mn><mo>=</mo><mn>8</mn><mo>+</mo><mi>i</mi><msub><mi>R</mi><mi>P</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>P</mi></msub><mo>=</mo><mn>12</mn><mo>&#215;</mo><mn>16</mn><mo>=</mo><mn>192</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q47. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>For the circuit shown below, calculate the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi mathvariant="normal">z</mi></msub><mo>:</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e0424a4d-c94c-4639-be48-428cfe0a02e8-image.png" style="width: 382px; height: 167px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>50</mn><mn>1000</mn></mfrac><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi>mA</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/356804ad-ef7c-4587-a284-47a6258ac3b4-image.png" style="width: 434px; height: 168px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>50</mn><mn>2000</mn></mfrac><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mi mathvariant="normal">Z</mi></msub><mo>=</mo><msub><mi>I</mi><mn>1000</mn></msub><mo>-</mo><msub><mi>I</mi><mn>2000</mn></msub></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>50</mn><mo>-</mo><mn>25</mn><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q48. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>The value of power dissipated across the zener diode <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>V</mi><mi mathvariant="italic">z</mi></msub><mo>=</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow></mfenced></math> connected in the circuit as shown in the figure is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40a2000b-749c-416a-b750-94cbb14554fa-image.png" style="width: 298px; height: 125px;" /></p><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> to the nearest integer is _______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f645cd68-5f6d-4e9f-bb65-2855abcd97ee-image.png" style="width: 298px; height: 125px;" /></p><p>Voltage across <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>S</mi></msub><mo>=</mo><mn>22</mn><mo>-</mo><mn>15</mn><mo>=</mo><mn>7</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Current through <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi mathvariant="italic">S</mi></msub><mo>=</mo><mi>I</mi><mo>=</mo><mfrac><mn>7</mn><mn>35</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Current through  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mi mathvariant="normal">&#937;</mi><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>15</mn><mn>90</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Current through zener <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>30</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Power through zener diode</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>V</mi><mi>I</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>15</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>30</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn></math> watt</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> watt</p>

</details>

---

### Q49. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `3`

<p>The zener diode has a <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>z</mi></msub><mo>=</mo><mn>30</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The current passing through the diode for the following circuit is___<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/847abeea-4ea7-4bd8-bb7d-4dcff560654a-image.png" style="width: 301px; height: 140px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/18446a82-9b18-45e1-bb7e-9e334d63ca19-image.png" style="width: 359px; height: 191px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>60</mn><mn>4000</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>30</mn><mn>5000</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>-</mo><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>60</mn><mn>4000</mn></mfrac><mo>-</mo><mfrac><mn>30</mn><mn>5000</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>1000</mn></mfrac><mi mathvariant="normal">A</mi></math> </p><p>current from zener diode</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>2</mn></msub><mo>=</mo><mi>i</mi><mo>-</mo><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mn>9</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q50. JEE Main 2021 (26 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The circuit contains two diodes each with a forward resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and with infinite reverse resistance. If the battery voltage is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, the current through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance is _______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi></math><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdf73a7a-e3b7-4811-b5f7-3482f83faf1d-image.png" style="width: 179px; height: 170px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/89638f73-fc91-4eb5-953c-57112b742e01-image.png" style="width: 206px; height: 169px;" /></p><p>In this circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> will be forward bias and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> will be revers bias.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> There will be no current through <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math></p><p>Apply KVL in circuit we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>6</mn><mo>-</mo><mn>50</mn><mi>i</mi><mo>-</mo><mn>130</mn><mi>i</mi><mo>-</mo><mn>120</mn><mi>i</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>6</mn><mn>300</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>6</mn><mn>300</mn></mfrac><mo>&#215;</mo><mn>1000</mn><mo>&#160;</mo><mi>mA</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>20</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q51. JEE Main 2021 (25 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery is connected across the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math>. Assume <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> to be normal silicon diodes. Find the current supplied by the battery if the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mi>v</mi><mi>e</mi></math> terminal of the battery is connected to point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2c13b553-8586-4136-93ee-34c570f7224e-image.png" style="width: 220px; height: 188px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>~</mo><mn>0</mn><mo>.</mo><mn>86</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>~</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>~</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>~</mo><mn>0</mn><mo>.</mo><mn>43</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>~</mo><mn>0</mn><mo>.</mo><mn>43</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b06873b4-4fcf-4135-a6f3-70fec01715ad-image.png" style="width: 200px; height: 188px;" /></p><p>Here only <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> will work and we know for silicon diode, potential drop on <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>7</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>7</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>43</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q52. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Given below are two statements:</p><p><strong>Statement I</strong> : <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction diodes can be used to function as a transistor, simply by connecting two diodes, back to back, which acts as the base terminal</p><p><strong>Statement II</strong>: In the study of transistors, the amplification factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> indicates ratio of the collector current to the base current.</p><p>In the light of the above statements, choose the correct answer from the options given below.</p>

**Options:**

- **(A)** Both Statement I and Statement II are false
- **(B)** Statement I is true but Statement II is false
- **(C)** Statement I is false but Statement II is true
- **(D)** Both Statement I and Statement II are true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Statement I is false but Statement II is true**

**Detailed Solution:**

S-1 Statement 1 is false because in case of two discrete back to back connected diodes, there are four doped regions instead of three and there is nothing that resembles a thin base region between an emitter and a collector.
S-2 Statement-2 is true, as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><msub><mi>I</mi><mi>C</mi></msub><msub><mi>I</mi><mi>B</mi></msub></mfrac></math>

</details>

---

### Q53. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Zener breakdown occurs in a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction having <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> both:

**Options:**

- **(A)** lightly doped and have narrow depletion layer.
- **(B)** heavily doped and have wide depletion layer.
- **(C)** lightly doped and have wide depletion layer.
- **(D)** heavily doped and have narrow depletion layer.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) heavily doped and have narrow depletion layer.**

**Detailed Solution:**

<p>Zener breakdown occurs in a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo><mi>n</mi></math> junction having <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> both because , zener breakdown occurs in the heavily doped p-n junction diode. Heavily doped <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>-</mo><mi mathvariant="normal">n</mi></math> junction diodes have narrow depletion region.</p>

</details>

---

### Q54. JEE Main 2021 (24 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>In connection with the circuit drawn below, the value of current flowing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>k&#937;</mi></math> resistor is______<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>.</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/618a50ab-64e2-4155-a472-d5b8fea492f9-image.png" style="width: 280px; height: 154px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p>Current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k&#937;</mi></math> resistance</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>5</mn><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q55. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Two Zener diodes (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>) having breakdown voltages of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> respectively, are connected as shown in the circuit below. The output voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub></math> variation with input voltage linearly increasing with time, is given by (<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>i</mi><mi>n</mi><mi>p</mi><mi>u</mi><mi>t</mi></mrow></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mi>V</mi><mo>&#160;</mo><mi>a</mi><mi>t</mi><mo>&#160;</mo><mi>t</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math>)</p><p></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e9a88c77-ddcd-4cfc-b557-40ad5104036d-image.png" style="width: 250px; height: 114px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0fa39f17-a52c-4f06-9e1b-6b37c6ee91c1-image.png" style="width: 247px; height: 112px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ddeed1c0-53a5-429a-bc1a-15b36715c24c-image.png" style="width: 237px; height: 111px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c48560ea-2869-442d-a2cb-5d3e250ee90b-image.png" style="width: 250px; height: 116px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ddeed1c0-53a5-429a-bc1a-15b36715c24c-image.png" style="width: 237px; height: 111px;" />**

**Detailed Solution:**

<p>At time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn><mo>,</mo></math> voltage across the first zener diode is increases linearly till it reaches it&#39;s breakdown voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, after that voltage increases linearly till it reaches the breakdown voltage of second zener diode,</p><p>As soon as voltage across the zener diode reaches the breakdown voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> of second zener diode, volatge becomes constant and doesn&#39;t change with time.</p>

</details>

---

### Q56. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Take the breakdown voltage of the zener diode used in the given circuit as <math><mrow><mn>6</mn><mtext>V</mtext></mrow></math>. For the input voltage shown in the figure below, the time variation of the output voltage is: (Graphs drawn are schematic and not to the scale)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f4bb1330-f2df-47da-9ed3-5385aa53e6fd-image.png" style="width: 667px; height: 198px;" /> </p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/920f44a9-0b33-4f94-8774-17a2b8eb0631-image.png" style="width: 465px; height: 191px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/023742f2-fb4e-4f9c-9c56-9a43988fabe0-image.png" style="width: 465px; height: 191px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a751f833-be2a-47e5-9134-4aee58e2d995-image.png" style="width: 465px; height: 187px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f84010e-7e79-4d02-bf50-1daeb9e89bbf-image.png" style="width: 465px; height: 187px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a751f833-be2a-47e5-9134-4aee58e2d995-image.png" style="width: 465px; height: 187px;" />**

**Detailed Solution:**

<p>A diode in forward biased acts as short circuit, since current can smoothly pass in such case. The potential difference across this is negligible.</p><p>In reverse biased, initially, a negligible current can pass through it. When a voltage greater than the breakdown voltage<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>V</mi><mo>&#8728;</mo></msub></mfenced></math> applied across this, the potential difference remains at the breakdown voltage.</p><p>In this question, two diodes are connected in opposite polarity. At a time, one diode is in forward biased and other is reversed biased. For solution, we can ignore the forward-biased diode as its voltage is negligible. If the applied potential difference(input) across the reversed biased diode becomes greater than the breakdown voltage<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>V</mi><mo>&#8728;</mo></msub></mfenced></math>, the potential difference across it will not increase and maintains at breakdown voltage.</p><p>In this question, the potential difference is changing direction and there will be one diode in reverse biased always. Hence, every peak will have a cut section and the range of the output graph will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><msub><mi>V</mi><mo>&#8728;</mo></msub><mo>,</mo><mo>&#160;</mo><mo>+</mo><msub><mi>V</mi><mo>&#8728;</mo></msub></mrow></mfenced></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ee41c4ec-ce10-43df-b2d5-ae1f0c112446-image.png" style="width: 465px; height: 189px;" /></p>

</details>

---

### Q57. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

When a diode is forward biased, it has a voltage drop of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> . the safe limit of current through the diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>mA</mi></math>. If a battery of emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is used in the circuit, the value of minimum resistance to be connected in series with the diode so that the current does not exceed the safe limit is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/48c2301f-bb8f-45dc-b783-e33d7ba23cd1-image.png" style="width: 285px; height: 168px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>d</mi><mi>i</mi><mi>o</mi><mi>d</mi><mi>e</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>volt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">R</mi></msub><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>volt</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>iR</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mn>1</mn><mi mathvariant="normal">i</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfrac><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q58. JEE Main 2020 (09 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

In the circuit shown below, is working as a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>&#160;</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal">c</mi></math> regulated voltage source. When <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is used as an input, the power dissipated (in <math><mi mathvariant="normal">m</mi><mi mathvariant="normal">W</mi></math> ) in each diode is (Considering both zener diodes are identical) 

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1de57253-1fc8-4839-8d04-0ab43549efcb-image.png" style="width: 290px; height: 251px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **40**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mfenced separators="|"><mrow><mn>12</mn><mo>-</mo><mn>8</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>200</mn><mo>+</mo><mn>200</mn></mrow></mfenced></mfrac><mi mathvariant="normal">A</mi><mo>=</mo><mfrac><mn>4</mn><mn>400</mn></mfrac><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
Power loss in each diode<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mn>4</mn></mfenced><mfenced separators="|"><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi>mW</mi></math>

</details>

---

### Q59. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The current <math><mi>i</mi></math> in the network is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/669ae281-c4e7-43c1-932e-868e5af1dd99-image.png" style="width: 215px; height: 218px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.3</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.3</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

Both the diodes are in reverse biased.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7bfc05f1-2353-464d-9ead-f9c23382916c-image.png" style="width: 250px; height: 184px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>9</mn><mn>30</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>10</mn></mfrac><mi mathvariant="normal">A</mi><mo>=</mo><mn>0.3</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

</details>

---

### Q60. JEE Main 2020 (09 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Both the diodes used in the circuit shown are assumed to be ideal and have negligible resistance when these are forward biased. Built in potential in each diode is <math><mn>0.7</mn><mi></mi><mi>V</mi></math>. For the input voltages shown in the figure, the voltage (in Volts) at point A is ________
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41edeab1-5373-435f-afff-bd8219540e21-image.png" style="width: 300px; height: 155px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63a648da-0b22-4080-a038-f0c40c19cca7-image.png" style="width: 300px; height: 146px;" />
Let <math><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>=</mo><mn>0</mn></math>
Right diode is reversed baised and left diode is forward biased
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><mn>12.7</mn><mo>-</mo><mn>0.7</mn></math>
<math><mo>=</mo><mn>12</mn></math> Volt

</details>

---

### Q61. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Figure shows a <math><mi mathvariant="normal">D</mi><mi mathvariant="normal">C</mi></math> voltage regulator circuit, with a Zener diode of breakdown voltage <math><mo>=</mo><mn>6</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></math> . If the unregulated input voltage varies between <math><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></math> to <math><mn>16</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi><mo>,</mo></math> then what is the maximum Zener current?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/358a11b0-81ef-4675-9ed0-3b367ec603dd-image.png" style="width: 300px; height: 264px;" />

**Options:**

- **(A)** <math><mn>1.5</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math> <mrow>  <mn>3.5</mn><mtext>&#x2009;</mtext><mtext>mA</mtext></mrow></math>
- **(C)** <math><mn>7.5</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(D)** <math><mn>2.5</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow>  <mn>3.5</mn><mtext>&#x2009;</mtext><mtext>mA</mtext></mrow></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/590801f4-2621-4452-b0d1-8023d9951d54-image.png" style="width: 300px; height: 285px;" />
Current through <math><mn>2</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">K</mi><mi mathvariant="normal">&#937;</mi></math> is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mi mathvariant="normal">&#160;</mi><mo>=</mo><mi mathvariant="normal">&#160;</mi><mfrac><mn>10</mn><mn>2000</mn></mfrac><mi mathvariant="normal">&#160;</mi><mo>=</mo><mi mathvariant="normal">&#160;</mi><mn>5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
Current through 4 <math><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">K</mi><mi mathvariant="normal">&#937;</mi></math> 
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mi mathvariant="normal">L</mi></msub><mo>=</mo><mi mathvariant="normal">i</mi><mo>-</mo><msub><mi mathvariant="normal">i</mi><mi mathvariant="normal">z</mi></msub><mo>=</mo><mfrac><mn>6</mn><mn>4000</mn></mfrac><mo>&#8201;</mo><mo>=</mo><mn>1.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">&#160;</mi><msub><mi mathvariant="normal">i</mi><mi mathvariant="normal">z</mi></msub><mo>=</mo><mi mathvariant="normal">i</mi><mo>-</mo><mn>1.5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#160;</mi><mo>&#8756;</mo><msub><mi mathvariant="normal">i</mi><mi mathvariant="normal">z</mi></msub><mo>=</mo><mn>5</mn><mo>-</mo><mn>1</mn><mo>.5</mo><mo>=</mo><mn>3</mn><mo>.5</mo><mi mathvariant="normal">&#160;</mi><mi>mA</mi></math></p>

</details>

---

### Q62. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The figure represents a voltage regulator circuit using a Zener diode. The breakdown voltage of the Zener diode is <math><mn>6</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math> and the load resistance is, <math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">L</mi></mrow></msub><mo>=</mo><mn>4</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">k</mi><mi mathvariant="normal">&#937;</mi></math> . The series resistance of the circuit is <math><mi>&#160;</mi><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">i</mi></mrow></msub><mo>=</mo><mn>1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">k</mi><mi mathvariant="normal">&#937;</mi></math> . If the battery voltage <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">B</mi></mrow></msub></math> varies from <math><mn>8</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi><mi mathvariant="normal">&#160;</mi></math> to <math><mi mathvariant="normal">&#160;</mi><mn>16</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math> , what are the minimum and maximum values of the current through Zener diode?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/02d4a28e-c453-4769-9701-db0d02a487bb-image.png" style="width: 314px; height: 204px;" />

**Options:**

- **(A)** <math><mn>0.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>;</mo><mi mathvariant="normal"> </mi><mn>6</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math><mn>1</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>;</mo><mi mathvariant="normal"> </mi><mn>8.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(C)** <math><mn>0.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>;</mo><mi mathvariant="normal"> </mi><mn>8.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(D)** <math><mn>1.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>;</mo><mi mathvariant="normal"> </mi><mn>8.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>;</mo><mi mathvariant="normal"> </mi><mn>8.5</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

For <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>8</mn><mi mathvariant="normal">V</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f20e9ad9-ac93-4720-bde9-ca0f2b1ac0a1-image.png" style="width: 360px; height: 201px;" />
<math><mn>8</mn><mi mathvariant="normal">&#160;</mi><mi>V</mi><mo>-</mo><mn>1000</mn><mi mathvariant="normal">&#160;</mi><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>6</mn><mi mathvariant="normal">&#160;</mi><mi>V</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>4000</mn></mrow></mfrac><mo>=</mo><mn>1.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
For <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>16</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">V</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f0092670-1463-46c7-8fab-206ff51424de-image.png" style="width: 362px; height: 198px;" />
<math><mn>16</mn><mi mathvariant="normal">&#160;</mi><mi>V</mi><mo>-</mo><mn>1000</mn><msub><mrow><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>6</mn><mi mathvariant="normal">&#160;</mi><mi>V</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>4000</mn></mrow></mfrac><mo>=</mo><mn>1.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>8.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

</details>

---

### Q63. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The reverse break down voltage of a Zener diode is <math><mn>5.6</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></math> in the given circuit.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2f0d43af-5654-4e27-898f-2898c8c61476-image.png" style="width: 270px; height: 119px;" />
The current <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi>z</mi></mrow></msub></math> through the Zener is:

**Options:**

- **(A)** <math><mi> </mi><mn>10</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math><mi> </mi><mn>7</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(C)** <math><mn>17</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
- **(D)** <math><mn>15</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi> </mi><mn>10</mn><mi> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5ee187a8-d2e6-42a3-b5ae-dddc3363db3c-image.png" style="width: 270px; height: 134px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>-</mo><msub><mi mathvariant="normal">i</mi><mi>z</mi></msub><mo>=</mo><mfrac><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">z</mi></msub><mn>800</mn></mfrac><mo>=</mo><mfrac><mn>5.6</mn><mn>800</mn></mfrac><mo>=</mo><mn>7</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
For loop ABCF,
<math><mn>9</mn><mo>-</mo><mn>200</mn><mi mathvariant="normal">&#160;</mi><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">z</mi></mrow></msub><mo>=</mo><mn>0</mn></math>
<math><msub><mrow><mi mathvariant="normal">i</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>0.017</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">&#160;</mi><mn>17</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mtext>z</mtext></msub><mo>=</mo><mfenced separators="|"><mrow><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>-</mo><mn>7</mn></mrow></mfenced><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi></math>

</details>

---

### Q64. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The circuit shown below contains two ideal diodes, each with a forward resistance of $50 \Omega$. If the battery voltage is $6 \mathrm{~V},$ the current through the $100 \Omega$ resistance (in Amperes) is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/81YotldGrsYQ52emafYDzohLgdJbl0BxJYWxrE-HJlU.original.fullsize.png">

**Options:**

- **(A)** 0.036
- **(B)** 0.02
- **(C)** 0.027
- **(D)** 0.03

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.02**

**Detailed Solution:**

As $D_{2}$ is reversed biased, so no current through $75 \Omega$ resistor.

now $R_{e q}=150+50+100$

$=300 \Omega$

So, required current $I=\frac{\text { BatteryVoltage }}{300}$ $\mathrm{I}=\frac{6}{300}=0.02$

</details>

---

### Q65. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit the current through Zener Diode is close to:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xs8EATWKrwPcXPpnn33fMrwL7_F2gu8bO8wZY_Tmcdw.original.fullsize.png">

**Options:**

- **(A)** $0.0 \mathrm{~mA}$
- **(B)** $6.7 \mathrm{~mA}$
- **(C)** $4.0 \mathrm{~mA}$
- **(D)** $6.0 \mathrm{~mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.0 \mathrm{~mA}$**

**Detailed Solution:**

Since voltage across zener diode does not reach to breakdown voltage therefore its resistance will be infinite \& current through it is $0 .$

</details>

---

### Q66. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the circuit shown below, the current through the Zener diode is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/79ba39f8-afc4-4b4d-b23b-f8336e6dc1a4-image.png" style="width: 400px; height: 163px;" />

**Options:**

- **(A)** zero.
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>&#160;</mi><mi>mA</mi></math>.
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#160;</mi><mi>mA</mi></math>.
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mi>&#160;</mi><mi>mA</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#160;</mi><mi>mA</mi></math>.**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e62103ca-d107-4be6-b073-a54a0710e059-image.png" />

Current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>k&#937;</mi></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>70</mn><mn>5000</mn></mfrac><mo>=</mo><mn>14</mn><mo>&#160;</mo><mi>mA</mi></math>

Current through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>k&#937;</mi></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi>l</mi></msub><mo>=</mo><mfrac><mn>50</mn><mn>10000</mn></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math>

Current through the Zener diode, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mi>mA</mi></math>

</details>

---

### Q67. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<math><mi>G</mi><mi>e</mi></math> and <math><mi>S</mi><mi>i</mi></math> diodes start conducting at <math><mn>0.3</mn><mi>&#160;</mi><mi>V</mi></math> and <math><mn>0.7</mn><mi>&#160;</mi><mi>V</mi></math> respectively. In the following figure if <math><mi>G</mi><mi>e</mi></math> diode connection are reversed, the value of <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub></math> changes by: (assume that the Ge diode has large breakdown voltage)

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yecoopdsbyfuiqfdljbnvxpllnbdupttfeelnpuqixtnfbvxxq.png" />

**Options:**

- **(A)** <math><mn>0.8</mn><mi> </mi><mi>V</mi></math>
- **(B)** <math><mn>0.4</mn><mi> </mi><mi>V</mi></math>
- **(C)** <math><mn>0.2</mn><mi> </mi><mi>V</mi></math>
- **(D)** <math><mn>0.6</mn><mi> </mi><mi>V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>0.4</mn><mi> </mi><mi>V</mi></math>**

**Detailed Solution:**

In first case, <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mn>12</mn><mo>-</mo><mn>0.3</mn></mrow></mfenced><mi>V</mi><mo>=</mo><mn>11.7</mn><mi> </mi><mi>V</mi></math> 

In second case, <math><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mn>12</mn><mo>-</mo><mn>0.7</mn></mrow></mfenced><mi>V</mi><mo>=</mo><mn>11.3</mn><mi> </mi><mi>V</mi></math> 

 <math><mo>∆</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>0.4</mn><mi> </mi><mi>V</mi></math>

</details>

---

### Q68. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit the current through zener diode is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f0555cca-8c2a-40e1-bab5-e646d6b4232b-image.png" style="width: 320px; height: 230px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>7</mn><mo>&#160;</mo><mi>mA</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi>mA</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>AB</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>V</mi><mi>BC</mi></msub><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, the current in <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi>&#160;</mi><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>500</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>mA</mi></math>. Current in <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi>&#160;</mi><msub><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>1500</mn></mrow></mfrac></math><math><mo>&#8658;</mo><mi>&#160;</mi><msub><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>20</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>m</mi><mi>A</mi></math>

Current in zener diode = <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>-</mo><mi>&#160;</mi><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfenced separators="|"><mrow><mn>10</mn><mo>-</mo><mfrac><mn>20</mn><mn>3</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mi>mA</mi><mo>=</mo><mfrac><mn>10</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>mA</mi><mi mathvariant="normal">&#160;</mi></math>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/bd2c17c7-4057-4c66-a198-831ea05f218d-image.png" style="width: 320px; height: 225px;" />

</details>

---

### Q69. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The reading of the ammeter for a silicon diode in the given circuit is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0f0f3a05-5f32-4fb6-9d78-977ab8fd4053-image.png" style="width: 250px; height: 163px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>.5</mo><mi mathvariant="normal">&#160;</mi><mi>mA</mi></math>
- **(B)** <math><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mi mathvariant="normal">&#160;</mi><mi>mA</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.5</mo><mi mathvariant="normal">&#160;</mi><mi>mA</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.5</mo><mi mathvariant="normal">&#160;</mi><mi>mA</mi></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>200</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. We have to calculate the current. We know that, a potential barrier across silicon diode <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0.7</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d21cdd39-d3fb-4891-82b1-43ecf2e12439-image.png" style="width: 240px; height: 182px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>I</mi><mi>R</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>0.7</mn></mrow><mn>200</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>0115</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>11</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>So, the current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math>.</p>

</details>

---

### Q70. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>-</mo><mi>I</mi></math> characteristic of a diode is shown in the figure. The ratio of forward to reverse bias resistance is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3d82a9c8-e27c-4257-914f-de848b46a13d-7afa2803-7ed4-4f01-9b12-a456b05ff0ba-image.png" style="width: 250px; height: 222px;" /></p>

**Options:**

- **(A)** <math><mn>100</mn></math>
- **(B)** <math><msup><mrow><mn>10</mn></mrow><mrow><mn>6</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup></math>
- **(D)** <math><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup></math>**

**Detailed Solution:**

Forward bias resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>0.8</mn><mo>-</mo><mn>0.7</mn></mrow><mrow><mfenced separators="|"><mrow><mn>20</mn><mo>-</mo><mn>10</mn></mrow></mfenced><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mn>0.1</mn><mrow><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.

Reverse bias resistance<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>10</mn><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mfrac><mo>=</mo><msup><mn>10</mn><mn>7</mn></msup><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.

<math><mfrac><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup></math>.

</details>

---

### Q71. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A Zener diode with a breakdown voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is connected in series with a resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to a battery of emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>. The maximum power dissipation rating for the Zener diode is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> to ensure maximum power dissipation across the diode is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#xA0;</mo><mi mathvariant="normal">&#x3A9;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>&#xA0;</mo><mi mathvariant="normal">&#x3A9;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mo>&#xA0;</mo><mi mathvariant="normal">&#x3A9;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#xA0;</mo><mi mathvariant="normal">&#x3A9;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>&#xA0;</mo><mi mathvariant="normal">&#x3A9;</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM01355481.jpg" style="width: 250px; height: 153px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mtext mathvariant="italic">P</mtext><mtext mathvariant="italic">zener</mtext></msub><mo>=</mo><mn>4</mn><mi>i</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>i</mi><mo>=</mo><mfrac bevelled="true"><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>6</mn><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q72. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the semiconductor devices whose characteristics are given below, in the order <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">a</mi></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mfenced><mi mathvariant="normal">b</mi></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mfenced><mi mathvariant="normal">c</mi></mfenced><mo>,</mo><mi mathvariant="normal">&#160;</mi><mfenced><mi mathvariant="normal">d</mi></mfenced></math>:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f7899f02-c166-414e-9d1b-09ce66929ccf-image.png" style="width: 450px; height: 207px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/737296f6-6ec7-4934-908d-be58192ac508-image.png" style="width: 450px; height: 187px;" /></p>

**Options:**

- **(A)** Solar cell, Light dependent resistance, Zener diode, Simple diode
- **(B)** Zener diode, Solar cell, Simple diode, Light dependent resistance
- **(C)** Simple diode, Zener diode, Solar cell, Light dependent resistance
- **(D)** Zener diode, Simple diode, Light dependent resistance, Solar cell

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Simple diode, Zener diode, Solar cell, Light dependent resistance**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/587582d2-4d72-40cf-9093-7aa70a82aeef-image.png" style="width: 230px; height: 195px;" />
Graph represents V-I characteristics of simple diode.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5d6749a4-9c7e-49c6-8556-e5402959cf86-image.png" style="width: 240px; height: 201px;" />
Graph represents V-I characteristic of Zener diode.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73190b6a-6512-4739-9dbb-824a25d81105-image.png" style="width: 250px; height: 193px;" />
Graph represents V-I characteristics of Solar cell 

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/85d8722f-15c1-4ec5-9d08-d21f4c930363-image.png" style="width: 300px; height: 181px;" />
Graph represents V-I characteristics of light dependence resistance. </p>

</details>

---

### Q73. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#8201;</mo><mi mathvariant="normal">V</mi></math> battery is connected across <math> <mrow> <mi>A</mi><mi>B</mi></mrow> </math> as shown in the figure. The value of the current supplied by the battery when in first case battery&#39;s positive terminal is connected to <math> <mi>A</mi> </math> and in second case when positive terminal of battery is connected to <math> <mi>B</mi> </math> will respectively be:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e07e81c4-657d-456f-b035-2d67a077b81c-image.png" style="width: 180px; height: 164px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2&#160;</mn><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.1&#160;</mn><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.1&#160;</mn><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2&#160;</mn><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2&#160;</mn><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.4&#160;</mn><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.4&#160;</mn><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2&#160;</mn><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.4&#160;</mn><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.2&#160;</mn><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

When <math xmlns="http://www.w3.org/1998/Math/MathML"> <mrow> <mo>+</mo><mtext>ve</mtext></mrow> </math> polarity is connected to <math> <mtext>A</mtext> </math>

Then <math><msub><mrow><mi>D</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is forward biased and <math><msub><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is reversed biased i.e.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e407a9e1-6f04-4610-bd03-711e216d304f-image.png" style="width: 180px; height: 136px;" />

<math><mo>&#8756;</mo></math> <math><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub></math> current through <math><msub><mrow><mi>D</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>0.4</mn><mi>&#160;</mi><mn>A</mn></math>

When <math xmlns="http://www.w3.org/1998/Math/MathML"> <mrow> <mo>+</mo><mtext>ve</mtext></mrow> </math> polarity is connected to <math> <mtext>B</mtext> </math> then <math><msub><mrow><mi>D</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is forward biased and <math><msub><mrow><mi>D</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is reversed biased then

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6f2e266c-7796-45ea-99bc-3d1bc7b16a2b-image.png" style="width: 180px; height: 131px;" />

<math><mo>&#8658;</mo><msub><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mn>0.2&#160; </mn><mn>A</mn></math>

</details>

---

### Q74. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p>The value of the resistor, <math><msub><mrow><mi>R</mi></mrow><mrow><mi>S</mi></mrow></msub></math>, needed in the DC voltage regulator circuit shown here, equals:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2b0fbfea-1b92-4764-bad5-2740a41de210-image.png" style="width: 300px; height: 159px;" /></p>

**Options:**

- **(A)** <math><mfrac><mrow><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>+</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>n</mi><mi> </mi><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>+</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>n</mi><mi> </mi><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0c9aaa07-c6d7-4a99-8cb3-f9b113b6a12c-image.png" style="width: 280px; height: 285px;" />

Across zener diode <math><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub><mo>=</mo><mi>c</mi><mi>o</mi><mi>n</mi><mi>s</mi><mi>t</mi><mi>a</mi><mi>n</mi><mi>t</mi></math>

<math><mo>&#8757;</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mi>S</mi></mrow></msub></math>

<math><mo>&#8658;</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mi>S</mi></mrow></msub></math>

<math><mo>&#8658;</mo><msub><mrow><mi>R</mi></mrow><mrow><mi>S</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msub><mrow><mi>I</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfrac></math>

</details>

---

### Q75. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

In an unbiased p - n junction electrons diffuse from n-region to p-region because:

**Options:**

- **(A)** electrons travel across the junction due to potential difference
- **(B)** only electrons move from n to p region and not the vice - versa
- **(C)** electron concentration in n - region is more as compared to that in p - region
- **(D)** holes in p - region attract them

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) electron concentration in n - region is more as compared to that in p - region**

**Detailed Solution:**

In a <math><mi>p</mi><mo>-</mo><mi>n</mi></math> junction diffusion occurs due to spontaneous movement of majority charge carrier from the region of high concentration to low concentration.

</details>

---

### Q76. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A Zener diode is connected to a battery and a load as show below:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/NIuELh--7Oh-1UgOL0_2Kuet91As4yfoBB99Szg5bM4.original.fullsize.png">

The currents, $\mathrm{I}, \mathrm{I}_{\mathrm{Z}}$ and $\mathrm{I}_{\mathrm{L}}$ are respectively.

**Options:**

- **(A)** $15 \mathrm{~mA}, 5 \mathrm{~mA}, 10 \mathrm{~mA}$
- **(B)** $15 \mathrm{~mA}, 7.5 \mathrm{~mA}, 7.5 \mathrm{~mA}$
- **(C)** $12.5 \mathrm{~mA}, 5 \mathrm{~mA}, 7.5 \mathrm{~mA}$
- **(D)** $12.5 \mathrm{~mA}, 7.5 \mathrm{~mA}, 5 \mathrm{~mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12.5 \mathrm{~mA}, 7.5 \mathrm{~mA}, 5 \mathrm{~mA}$**

**Detailed Solution:**

Here, $R=4 \mathrm{k} \Omega=4 \times 10^3 \Omega$
$$
V_i=60 \mathrm{~V}
$$
Zener voltage $V_z=10 \mathrm{~V}$ $R_L=2 \mathrm{k} \Omega=2 \times 10^3 \Omega$
Load current, $I_{\mathrm{L}}=\frac{V_Z}{R_L}=\frac{10}{2 \times 10^3}=5 \mathrm{~mA}$
Current through $R, I=\frac{V_i-V_Z}{R}$ $=\frac{60-10}{4 \times 10^3}=\frac{50}{4 \times 10^3}=12.5 \mathrm{~mA}$
Fom circuit diagram,
$$
\begin{aligned}
& I=I_Z+I_L \\
\Rightarrow & 12.5=I_Z+5 \\
\Rightarrow & I_7=12.5-5=7.5 \mathrm{~mA}
\end{aligned}
$$

</details>

---

### Q77. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The forward biased diode connection is :

**Options:**

- **(A)** <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025748Opt_1.jpg" style="width: 311px; height: 63px;" /></strong></u>
- **(B)** <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025748Opt_2.jpg" /></strong></u>
- **(C)** <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025748Opt_3.jpg" style="width: 311px; height: 58px;" /></strong></u>
- **(D)** <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025748Opt_4.jpg" style="width: 311px; height: 56px;" /></strong></u>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/EM0025748Opt_1.jpg" style="width: 311px; height: 63px;" /></strong></u>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d13bd334-d826-46ba-a070-88edddcd996a-image.png" style="width: 300px; height: 254px;" /></p><p>A junction diode is said to be forward-biased when the positive terminal of the external battery is connected to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo></math>region and the negative terminal to the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo></math>region of the diode.</p><p>The potential of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>-</mo></math>side is more positive that of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo></math>side, hence diode is in forward biasing. In forward biasing it acts as short circuit, hence current flows.</p><p>In case of forward biased circuit P-junction should be at higher potential. 

<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Q_28_AnsExp_1.jpg" style="width: 311px; height: 63px;" /></p>

</details>

---

### Q78. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Figure shows a circuit in which three identical diodes are used. Each diode has forward resistance of $20 \Omega$ and infinite backward resistance. Resistors $\mathrm{R}_1=\mathrm{R}_2=\mathrm{R}_3=50 \Omega$. Battery voltage is $6 \mathrm{~V}$. The current through $\mathrm{R}_3$ is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZafraJVC-sUpiKskEG5mrBZZzcjM-TTjfDO5ltIJczc.original.fullsize.png">

**Options:**

- **(A)** $50 \mathrm{~mA}$
- **(B)** $100 \mathrm{~mA}$
- **(C)** $60 \mathrm{~mA}$
- **(D)** $25 \mathrm{~mA}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $50 \mathrm{~mA}$**

**Detailed Solution:**

Here, diodes $D_1$ and $D_2$ are forward biased and $\mathrm{D}_3$ is reverse biased. Therefore current through $\mathrm{R}_3$
$$
\mathrm{i}=\frac{\mathrm{V}}{\mathrm{R}^{\prime}}=\frac{6}{120}=\frac{1}{20} \mathrm{~A}=50 \mathrm{~mA}
$$

</details>

---

### Q79. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The <math> <mrow> <mtext>I</mtext> <mo>-</mo> <mtext>V</mtext> </mrow> </math> characteristics of an <math> <mrow> <mtext>LED</mtext> </mrow> </math> is:

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cf0f8103-7ba9-49e1-a8c0-8c65af65c846-image.png" style="width: 200px; height: 143px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e4c72c25-9d6a-4142-a63b-991a8cd9f928-image.png" style="width: 200px; height: 148px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6e54574f-2f73-4878-819f-59372b45e18a-image.png" style="width: 200px; height: 175px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f9469edf-69d0-43dd-91ab-0159bfc01764-image.png" style="width: 200px; height: 156px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6e54574f-2f73-4878-819f-59372b45e18a-image.png" style="width: 200px; height: 175px;" />**

**Detailed Solution:**

For same value of current higher value of voltage is required for higher frequency hence,

<math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">T</mi><mi mathvariant="normal">h</mi></mrow></msub><mo>∝</mo><mi mathvariant="normal">Δ</mi><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mi mathvariant="normal">g</mi></mrow></msub><mo>∝</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">λ</mi></mrow></mfrac></math>

LED works in forward Bias. This graph is correct.

</details>

---

### Q80. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `3`

<p>A diode detector is used to detect an amplitude modulated wave of 60% modulation  by using a condenser of capacity 250 pico farad in parallel with a load resistance of 100 kilo ohm. Find the maximum modulated frequency which could be detected by it.</p>

**Options:**

- **(A)** <math> <mrow> <mtext>5.31 MHz</mtext> </mrow> </math>
- **(B)** <math> <mrow> <mtext>5.31 kHz</mtext> </mrow> </math>
- **(C)** <math> <mrow> <mtext>10.62 MHz</mtext> </mrow> </math>
- **(D)** <math> <mrow> <mtext>10.62 kHz</mtext> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mtext>10.62 kHz</mtext> </mrow> </math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/00cc7448-cf4e-4241-ba9f-c604f8372f92-image.png" style="width: 362px; height: 181px;" />

<math> <mrow> <mi>&#964;</mi> <mo>=</mo> <mtext>RC</mtext> <mo>=</mo> <mn>1</mn> <mn>0</mn> <mn>0</mn> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mn>3</mn> </msup> <mo>&#215;</mo> <mn>2</mn> <mn>5</mn> <mn>0</mn> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>1</mn> <mn>2</mn> </mrow> </msup> <mtext>&#160;sec</mtext> </mrow> </math>

           <math><mrow> <mo>=</mo> <mtext>2.5</mtext> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mn>7</mn> </msup> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mn>-1</mn> <mn>2</mn> </mrow> </msup> <mtext>&#160;sec</mtext> </mrow> </math>
 
           <math> <mrow> <mo>=</mo> <mtext>2.5</mtext> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>5</mn> </mrow> </msup> <mtext>&#160;sec</mtext> </mrow> </math>

The higher frequency which can be detected with tolerable distortion is

<math> <mrow> <mtext>f</mtext> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> <mi>&#960;</mi> <msub> <mtext>m</mtext> <mtext>a</mtext> </msub> <mtext>RC</mtext> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> <mi>&#960;</mi> <mo>&#215;</mo> <mtext>0.6</mtext> <mo>&#215;</mo> <mtext>2.5</mtext> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>5</mn> </mrow> </msup> </mrow> </mfrac> <mtext>&#160;Hz</mtext> </mrow> </math>

  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mn>0</mn><mn>0</mn><mo>&#215;</mo><mn>1</mn><msup><mn>0</mn><mn>4</mn></msup></mrow><mrow><mn>2</mn><mn>5</mn><mo>&#215;</mo><mtext>1.2</mtext><mi>&#960;</mi></mrow></mfrac><mo>&#160;</mo><mtext>&#160;Hz</mtext></math>

  <math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>4</mn> </mrow> <mrow> <mtext>1.2</mtext> <mi>&#960;</mi> </mrow> </mfrac> <mo>&#215;</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mn>4</mn> </mrow> </msup> <mtext>&#160;Hz</mtext> </mrow> </math>

  <math><mrow><mo> =&#160;</mo> <mtext>10.61 kHz</mtext> </mrow> </math>

This condition is obtained by applying the condition that rate of decay of capacitor voltage must be equal or less then the rate of decay modulated signal voltage for proper detection of modulated signal.

</details>

---

### Q81. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

If in a $\mathrm{p-n}$ junction diode, a square input signal of $10 \mathrm{~V}$ is applied as shown
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mvsRBugXngvjwjErsx5SpGfK0Dkydu19hto4gyJyvvk.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/89f7MZSLREuIuXu-EIL3P69oGMtZByVY_8EAWtBfaGQ.original.fullsize.png">

Then the output signal across $R_{\mathrm{L}}$ will be

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/y6WH-EKQcXRKAXL-EqchyMT6eJ4jlo2u4QfLit8sIbQ.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZIsrOGTTHIsY2X7kB7n6T7UM_3hFOnhf_9FhImUusMg.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/umgu0YDK5tUUcAxZKPmxhWRUOiMzxH5rJuCmd7zKKyk.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qMyhRzBeiGSYuM1P_dK99FdPh2lcyedBWLblCfb8jY4.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qMyhRzBeiGSYuM1P_dK99FdPh2lcyedBWLblCfb8jY4.original.fullsize.png">**

**Detailed Solution:**

No Solution Available

</details>

---

### Q82. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The circuit has two oppositely connect ideal diodes in parallel. What is the current following in the circuit?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HIA1M0Xj1mXyZ9UwHjpL5-p6cheuIq2RBV7MYOlFvKY.original.fullsize.png">

**Options:**

- **(A)** $1.33 \mathrm{~A}$
- **(B)** $1.71 \mathrm{~A}$
- **(C)** $2.00 \mathrm{~A}$
- **(D)** $2.31 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2.00 \mathrm{~A}$**

**Detailed Solution:**

$D_1$ is reverse biased therefore it will act like an open circuit.
$$
\mathrm{i}=\frac{12}{6}=2.00 \mathrm{~A}
$$

</details>

---

### Q83. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

In the following, which one of the diodes is reverse biased?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IBDUzBmKCxGfO-lR8g-nPI5yIkwigJLDpashGk8wrwA.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jY-8Zd7e1skSn6nfaQPcx_sHytuvz0kZ35CgXawL4zY.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/u21WJVJ9f6-vUYGLxpmhXFMurwvCM7gs8huNUk8o6C4.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3MHvoV5W9eie-6uEuBb2seNELDpWwApUA0SYFovz_SM.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/IBDUzBmKCxGfO-lR8g-nPI5yIkwigJLDpashGk8wrwA.original.fullsize.png">**

**Detailed Solution:**

No Solution Available

</details>

---

### Q84. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

When p-n junction diode is forward biased

**Options:**

- **(A)** the depletion region is reduced and barrier height is increased
- **(B)** the depletion region is widened and barrier height is reduced
- **(C)** both the depletion region and barrier height reduced
- **(D)** both the depletion region and barrier height increased.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) both the depletion region and barrier height reduced**

**Detailed Solution:**

No Solution Available

</details>

---

### Q85. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

In the middle of the depletion layer of a reverse biased p-n junction, the

**Options:**

- **(A)** electric field is zero
- **(B)** potential is maximum
- **(C)** electric field is maximum
- **(D)** potential is zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) electric field is maximum**

**Detailed Solution:**

No Solution Available

</details>

---

