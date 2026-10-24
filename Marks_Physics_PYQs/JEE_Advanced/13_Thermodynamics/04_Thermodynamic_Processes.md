# JEE Advanced Physics - Thermodynamics

## Topic 4: Thermodynamic Processes

**Total Questions:** 26

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

Ten moles of an ideal monoatomic gas, initially in state $\boldsymbol{a}$ at atmospheric pressure and temperature $T_a = 27^\circ$C, is enclosed in a metal cylinder of volume $V_0$ fitted with a frictionless piston. The gas is suddenly compressed to state $\boldsymbol{b}$ with volume $V_0/3$. Now, keeping the piston stationary, the cylinder is submerged in a water bath of temperature $11^\circ$C until the gas reaches the temperature of the water bath, which is denoted as state $\boldsymbol{c}$. Finally, while still in the water bath, the piston is brought slowly to its initial position, which is denoted as state $\boldsymbol{f}$. If $R$ is universal gas constant, then the correct option(s) is/are:
[Given: $9^{1/3} = 2.08$]

**Options:**

- **(A)** The schematic P-V diagram of the processes described above is: <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q27_d1.png" />
- **(B)** The change in internal energy in going from state $\boldsymbol{a}$ to $\boldsymbol{b}$ is $4860R$.
- **(C)** The net change in the internal energy in the whole process is $-240R$.
- **(D)** The pressure and temperature of the state $\boldsymbol{b}$ are $2.08$ times the atmospheric pressure and $624$ K, respectively.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) The net change in the internal energy in the whole process is $-240R$.**

**Detailed Solution:**

For state $a$: $n = 10$, $T_a = 27^{\circ}\text{C} = 300\text{ K}$, $P_a = 1\text{ atm}$, $V_a = V_0$.
For a monoatomic gas, $C_v = \dfrac{3}{2}R$ and $\gamma = \dfrac{5}{3}$.

Process $a \rightarrow b$ is a sudden compression, which is an adiabatic process.
$V_b = \dfrac{V_0}{3}$
Using $T_a V_a^{\gamma-1} = T_b V_b^{\gamma-1}$:
$T_b = T_a \left(\dfrac{V_a}{V_b}\right)^{\gamma-1} = 300 \times (3)^{5/3 - 1} = 300 \times 3^{2/3} = 300 \times (9)^{1/3}$
Given $9^{1/3} = 2.08$, we get $T_b = 300 \times 2.08 = 624\text{ K}$.
Using $P_a V_a^\gamma = P_b V_b^\gamma$:
$P_b = P_a \left(\dfrac{V_a}{V_b}\right)^\gamma = 1 \times (3)^{5/3} = 3 \times 3^{2/3} = 3 \times 2.08 = 6.24\text{ atm}$.
Thus, the pressure at state $b$ is $6.24$ times the atmospheric pressure. Option (D) is incorrect.

The change in internal energy for process $a \rightarrow b$ is:
$\Delta U_{ab} = n C_v (T_b - T_a) = 10 \times \dfrac{3}{2}R \times (624 - 300) = 15R \times 324 = 4860R$.
Option (B) is correct.

Process $b \rightarrow c$ is isochoric (stationary piston), so $V_c = \dfrac{V_0}{3}$.
The gas cools to the water bath temperature, $T_c = 11^{\circ}\text{C} = 284\text{ K}$.

Process $c \rightarrow f$ is isothermal (slow expansion in water bath), so $T_f = T_c = 284\text{ K}$ and $V_f = V_0$.
The net change in internal energy for the entire process $a \rightarrow f$ depends only on the initial and final temperatures:
$\Delta U_{net} = n C_v (T_f - T_a) = 10 \times \dfrac{3}{2}R \times (284 - 300) = 15R \times (-16) = -240R$.
Option (C) is correct.

For the P-V diagram:
Process $a \rightarrow b$ is an adiabatic compression (curve upwards and to the left).
Process $b \rightarrow c$ is an isochoric cooling (vertical line downwards).
Process $c \rightarrow f$ is an isothermal expansion (curve downwards and to the right).
Comparing pressures at volume $V_0$:
$P_a = \dfrac{nR(300)}{V_0}$ and $P_f = \dfrac{nR(284)}{V_0}$
Since $P_a > P_f$, point $a$ lies above point $f$. The given schematic diagram correctly represents all these features. Option (A) is correct.

Answer: The schematic P-V diagram of the processes described above is: <img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q27_d1.png" />; The change in internal energy in going from state $\boldsymbol{a}$ to $\boldsymbol{b}$ is $4860R$.; The net change in the internal energy in the whole process is $-240R$.

</details>

---

### Q2. JEE Advanced 2026 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

A quasi-static cycle of a monoatomic ideal gas contains an isothermal process $(\boldsymbol{ab})$, followed by an isochoric process $(\boldsymbol{bc})$ and an adiabatic process $(\boldsymbol{ca})$ as shown in the figure. The volumes of the gas are $V_1$ and $V_2$ at $\boldsymbol{a}$ and $\boldsymbol{b}$, respectively. If the cycle has heat input $Q_{\text{in}}$ and output $Q_{\text{out}}$, then the efficiency of the cycle is defined as $\eta = \dfrac{Q_{\text{in}} - Q_{\text{out}}}{Q_{\text{in}}}$. The correct statement(s) is/are:
[Given: $\ln 2 \approx 0.7$]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q23_d1.png" />

**Options:**

- **(A)** If $V_2/V_1 = 8$, the heat released in the process $\boldsymbol{bc}$ is smaller than the heat absorbed in the process $\boldsymbol{ab}$.
- **(B)** For a given value of $V_2/V_1$, $\eta$ does not depend on the temperature of the isothermal process.
- **(C)** If $V_2/V_1 = 8$, then the temperature of the gas at $\boldsymbol{a}$ is $4$ times the temperature of the gas at $\boldsymbol{c}$.
- **(D)** If $V_2/V_1 = 8$, then the pressure of the gas at $\boldsymbol{a}$ is $4$ times the pressure of the gas at $\boldsymbol{b}$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) If $V_2/V_1 = 8$, then the temperature of the gas at $\boldsymbol{a}$ is $4$ times the temperature of the gas at $\boldsymbol{c}$.**

**Detailed Solution:**

For the monoatomic ideal gas, $\gamma = \dfrac{5}{3}$.

Process $ab$ is isothermal, so $T_a = T_b$ and $V_a = V_1$, $V_b = V_2$.

Process $bc$ is isochoric, so $V_b = V_c = V_2$.

Process $ca$ is adiabatic, so $T_c V_c^{\gamma-1} = T_a V_a^{\gamma-1}$.

$T_c V_2^{2/3} = T_a V_1^{2/3} \Rightarrow T_c = T_a \left(\dfrac{V_1}{V_2}\right)^{2/3}$.

If $\dfrac{V_2}{V_1} = 8$, $T_c = T_a \left(\dfrac{1}{8}\right)^{2/3} = \dfrac{T_a}{4} \Rightarrow T_a = 4 T_c$. Thus, statement (C) is correct.

Heat absorbed in isothermal process $ab$ is $Q_{ab} = nRT_a \ln\left(\dfrac{V_2}{V_1}\right)$.

For $\dfrac{V_2}{V_1} = 8$, $Q_{ab} = nRT_a \ln(8) = 3nRT_a \ln 2 \approx 3 \times 0.7 nRT_a = 2.1 nRT_a$.

Heat released in isochoric process $bc$ is $Q_{bc} = nC_v(T_b - T_c) = n\left(\dfrac{3}{2}R\right)\left(T_a - \dfrac{T_a}{4}\right) = \dfrac{9}{8}nRT_a = 1.125 nRT_a$.

Since $1.125 nRT_a < 2.1 nRT_a$, the heat released in $bc$ is smaller than the heat absorbed in $ab$. Thus, statement (A) is correct.

The efficiency of the cycle is $\eta = 1 - \dfrac{Q_{\text{out}}}{Q_{\text{in}}} = 1 - \dfrac{Q_{bc}}{Q_{ab}}$.

$\eta = 1 - \dfrac{n \left(\dfrac{3}{2} R\right) T_a \left(1 - \left(\dfrac{V_1}{V_2}\right)^{2/3}\right)}{nRT_a \ln\left(\dfrac{V_2}{V_1}\right)} = 1 - \dfrac{3 \left(1 - \left(\dfrac{V_1}{V_2}\right)^{2/3}\right)}{2 \ln\left(\dfrac{V_2}{V_1}\right)}$.

This expression depends only on the volume ratio $\dfrac{V_2}{V_1}$ and is independent of the temperature $T_a$. Thus, statement (B) is correct.

For the isothermal process $ab$, $P_a V_a = P_b V_b \Rightarrow P_a V_1 = P_b V_2 \Rightarrow P_a = 8 P_b$. Thus, statement (D) is incorrect.

Answer: If $V_2/V_1 = 8$, the heat released in the process $\boldsymbol{bc}$ is smaller than the heat absorbed in the process $\boldsymbol{ab}$.; For a given value of $V_2/V_1$, $\eta$ does not depend on the temperature of the isothermal process.; If $V_2/V_1 = 8$, then the temperature of the gas at $\boldsymbol{a}$ is $4$ times the temperature of the gas at $\boldsymbol{c}$.

</details>

---

### Q3. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `2`

The left and right compartments of a thermally isolated container of length $L$ are separated by a thermally conducting, movable piston of area $A$. The left and right compartments are filled with $\frac{3}{2}$ and 1 moles of an ideal gas, respectively. In the left compartment the piston is attached by a spring with spring constant k and natural length $\frac{2 L}{5}$. In thermodynamic equilibrium, the piston is at a distance $\frac{L}{2}$ from the left and right edges of the container as shown in the figure. Under the above conditions, if the pressure in the right compartment is $P=\frac{\mathrm{k} L}{\mathrm{~A}} \alpha$, then the value of $\alpha$ is $\qquad$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/wMInrVg1OTZkbtXrGf3EZwEJGOIKcJuT1zP5pb9ZVMM.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.2**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/fYTmIqDtDmRWWQMvN7h9iaoWO0AbGQegqwMqlS0SuHg.original.fullsize.png">
Extension in spring
$\begin{aligned}
& x=0.5 \mathrm{~L}-0.4 \mathrm{~L} \\
& =0.1 \mathrm{~L}
\end{aligned}$
FBD of piston<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/2AOzx9o_ODs7ZjgkWwVbaWUw1knqraBcgAXcOfqPJLM.original.fullsize.png">
$\begin{aligned} & \mathrm{kx}+\mathrm{P}_2 \mathrm{~A}=\mathrm{P}_1 \mathrm{~A} \\ & \mathrm{P}_2 \mathrm{~A}=\mathrm{P}_1 \mathrm{~A}-\mathrm{kx}\end{aligned}$
$P_2=P_1-\frac{k L}{A(10)} \qquad ....(i)$
$\begin{aligned} & \mathrm{P}_1 \mathrm{~V}=\mathrm{n}_1 \mathrm{RT} \\ & \mathrm{P}_2 \mathrm{~V}=\mathrm{n}_2 \mathrm{RT} \\ & \frac{\mathrm{P}_1}{\mathrm{P}_2}=\frac{\mathrm{n}_1}{\mathrm{n}_2}=\frac{3}{2}\end{aligned}$
$\mathrm{P}_1=\frac{3}{2} \mathrm{P}_2 \qquad ....(ii)$
$\begin{aligned} & P_2=\frac{3}{2} P_2-\frac{k L}{10 A} \\ & \frac{P_2}{2}=\frac{k L}{10 A} \\ & P_2=\frac{k L}{5 A}=\frac{k L}{A} \alpha \\ & \alpha=\frac{1}{5}=0.2\end{aligned}$

</details>

---

### Q4. JEE Advanced 2025 (Paper 2)

*Type:* `numerical` | *Level:* `3`

An ideal monatomic gas of n moles is taken through a cycle $W X Y Z W$ consisting of consecutive adiabatic and isobaric quasi-static processes, as shown in the schematic $V-T$ diagram. The volume of the gas at $W, X$ and $Y$ points are, $64 \mathrm{~cm}^3, 125 \mathrm{~cm}^3$ and $250 \mathrm{~cm}^3$, respectively. If the absolute temperature of the gas $T_W$ at the point $W$ is such that $n R T_W=1 \mathrm{~J}$ ( R is the universal gas constant), then the amount of heat absorbed (in J ) by the gas along the path $X Y$ is $\qquad$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/siWmsSNAccov_QYDBNEnKz6EZalFaDZQ6wG-qcTJiWo.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.6**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Kw9HCUXp8MJCJT2XZ07liQ3hA5LUxnZKBt7KlVvAPJI.original.fullsize.png">
$\begin{aligned}
& \mathrm{nRT}_{\mathrm{W}}=\mathrm{P}_{\mathrm{W}} \mathrm{~V}_{\mathrm{W}}=1 \mathrm{~J} \\
& \mathrm{P}_{\mathrm{W}}=\frac{1}{64} \times 10^6 \mathrm{~Pa}
\end{aligned}$
For WX process
$\begin{aligned}
& P_X V_X^Y=P_W V_W^y \\
& \Rightarrow P_X=P_W\left(\frac{V_W}{V_X}\right)^y
\end{aligned}$
amount of heat absorbed in XY process
$\begin{aligned} \mathrm{Q} & =\mathrm{nCP} \Delta \mathrm{T}=\mathrm{n} \times \frac{5}{2} \mathrm{R} \times\left[\mathrm{T}_{\mathrm{Y}}-\mathrm{T}_{\mathrm{X}}\right] \quad\left[\text { For monoatomic gas } \mathrm{C}_{\mathrm{P}}=\frac{5 \mathrm{R}}{2}\right] \\ \mathrm{Q} & =\frac{5}{2}\left[\mathrm{nRT}_{\mathrm{Y}}-\mathrm{nRT} \mathrm{T}_{\mathrm{X}}\right] \\ & =\frac{5}{2}\left[\mathrm{P}_{\mathrm{Y}} \mathrm{V}_{\mathrm{Y}}-\mathrm{P}_{\mathrm{X}} \mathrm{V}_{\mathrm{X}}\right] \\ & =\frac{5}{2} \mathrm{P}_{\mathrm{X}}\left[\mathrm{V}_{\mathrm{Y}}-\mathrm{V}_{\mathrm{X}}\right] \quad\left[\because \quad \mathrm{P}_{\mathrm{X}}=\mathrm{P}_{\mathrm{Y}} ; \text { Isobaric process }\right] \\ & =\frac{5}{2} \times \mathrm{P}_{\mathrm{W}} \times\left[\frac{\mathrm{V}_{\mathrm{W}}}{\mathrm{V}_{\mathrm{X}}}\right]^{\mathrm{y}}\left[\mathrm{V}_{\mathrm{Y}}-\mathrm{V}_{\mathrm{X}}\right]\end{aligned}$
Putting values :
$Q=1.6$ Joule

</details>

---

### Q5. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

One mole of a monatomic ideal gas undergoes the cyclic process $\mathrm{J} \rightarrow \mathrm{K} \rightarrow \mathrm{L} \rightarrow \mathrm{M} \rightarrow \mathrm{J}$, as shown in the P-T diagram.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/A-EbJMeFTqnbL7W1l5-jIy2mDZEDRvXRUDq5I7gpTsQ.original.fullsize.png">
Match the quantities mentioned in List-I with their values in List-II and choose the correct option.
[$\mathcal{R}$ is the gas constant.]
\(\begin{array}{l|l}
\text{List-I} & \text{List-II} \\
\hline \text{(P) Work done in the complete cyclic process} & (1) \mathcal{R} T_0-4 \mathcal{R} T_0 \ln 2 \\
\text{(Q) Change in the internal energy of the gas in the process JK} & (2) 0 \\
\text{(R) Heat given to the gas in the process KL} & (3) 3 \mathcal{R} T_0 \\
\text{(S) Change in the internal energy of the gas in the process MJ} & (4) -2 \mathcal{R} T_0 \ln 2 \\
& (5) -3 \mathcal{R} T_0 \ln 2
\end{array}\)

**Options:**

- **(A)** $\mathrm{P} \rightarrow 1 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 5 ; \mathrm{S} \rightarrow 4$
- **(B)** $\mathrm{P} \rightarrow 4 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 5 ; \mathrm{S} \rightarrow 2$
- **(C)** $\mathrm{P} \rightarrow 4$; $\mathrm{Q} \rightarrow 1 ; \mathrm{R} \rightarrow 2 ; \mathrm{S} \rightarrow 2$
- **(D)** $\mathrm{P} \rightarrow 2 ; \mathrm{Q} \rightarrow 5 ; \mathrm{R} \rightarrow 3 ; \mathrm{S} \rightarrow 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{P} \rightarrow 4 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 5 ; \mathrm{S} \rightarrow 2$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{J}\left(\mathrm{P}_0, \mathrm{~V}_0, \mathrm{~T}_0\right) \\ & \mathrm{K}\left(\mathrm{P}_0, 3 \mathrm{~V}_0, 3 \mathrm{~T}_0\right) \\ & \mathrm{M}\left(2 \mathrm{P}_0, \frac{\mathrm{V}_0}{2}, \mathrm{~T}_0\right) \\ & \mathrm{L}\left(2 \mathrm{P}_0, \frac{3 \mathrm{~V}_0}{2}, 3 \mathrm{~T}_0\right) \\ & \mathrm{P}_0 \mathrm{~V}_0=\mathrm{nRT}_0 \\ & \mathrm{JK} \rightarrow \text { isobaric } \Rightarrow \mathrm{W}=\mathrm{P}_0\left(2 \mathrm{~V}_0\right)=2 \mathrm{nRT}_0 \\ & \Delta \mathrm{U}=\frac{3}{2} \mathrm{nR}\left(2 \mathrm{~T}_0\right)=3 \mathrm{nRT}_0 \\ & \mathrm{KL} \rightarrow \text { isothermal } \rightarrow \mathrm{W}=\mathrm{nR}(3 \mathrm{~T}) \ln \left(\frac{1}{2}\right)=-3 \mathrm{nRT}_0 \ell \mathrm{n} 2 \\ & \Delta \mathrm{U}=0 \Rightarrow \mathrm{Q}=-3 \mathrm{nRT}{ }_0 \ln 2 \\ & \mathrm{LM} \rightarrow \text { isobaric }=2 \mathrm{P}_0\left(-\mathrm{V}_0\right)=-2 \mathrm{nRT} \mathrm{e}_0 \\ & \mathrm{MJ} \rightarrow \text { isothermal } \Rightarrow \mathrm{nRT} \mathrm{n}_0 \ln 2 ; \Delta \mathrm{U}=0 \\ & \mathrm{WD} \text { net }=-2 \mathrm{nRT} \mathrm{e}_0 \ln 2 \\ & \mathrm{P} \rightarrow 4, \mathrm{Q} \rightarrow 3, \mathrm{R} \rightarrow 5, \mathrm{~S} \rightarrow 2\end{aligned}$

</details>

---

### Q6. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<p>One mole of an ideal gas undergoes two different cyclic processes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math>, as shown in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>-</mo><mi>V</mi></math> diagrams below. In cycle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math>, processes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> are isobaric, isothermal, isobaric and isochoric, respectively. In cycle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math>, processes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#39;</mo><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#39;</mo><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#39;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>&#39;</mo></math> are isothermal, isochoric, isobaric and isochoric, respectively. The total work done during cycle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mi mathvariant="normal">I</mi></msub></math> and that during cycle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mi>II</mi></msub></math>. The ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>W</mi><mi mathvariant="normal">I</mi></msub><msub><mi>W</mi><mi>II</mi></msub></mfrac></math> is _____.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/fbe35803-daf5-4533-8eda-8e7dcbfa6ee3.png" style="width: 300px; height: 206px;" />           <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/29ba4b2a-e2c7-4092-ad9d-a45acad68e00.png" style="width: 350px; height: 193px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/214c76d6-9a42-4853-9424-09c3f4f8b4f5.png" style="width: 300px; height: 204px;" />           <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ab7f5f9e-c113-4fe9-852b-55522eea943f.png" style="width: 350px; height: 222px;" /></p><p>For first case:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mi mathvariant="normal">I</mi></msub><mo>=</mo><msub><mi>W</mi><mi>a</mi></msub><mo>+</mo><msub><mi>W</mi><mi>b</mi></msub><mo>+</mo><msub><mi>W</mi><mi>c</mi></msub><mo>+</mo><msub><mi>W</mi><mi>d</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msub><mi>P</mi><mn>0</mn></msub><mfenced><mrow><mn>2</mn><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><msub><mi>V</mi><mn>0</mn></msub></mrow></mfenced><mo>+</mo><mi>n</mi><mi>R</mi><mi>T</mi><mo>&#160;</mo><mi>ln</mi><mfenced><mfrac><mrow><mn>4</mn><msub><mi>V</mi><mn>0</mn></msub></mrow><mrow><mn>2</mn><msub><mi>V</mi><mn>0</mn></msub></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn><msub><mi>P</mi><mn>0</mn></msub><mfenced><mrow><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>4</mn><msub><mi>V</mi><mn>0</mn></msub></mrow></mfenced><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub><mo>+</mo><mi>n</mi><mi>R</mi><mfenced><mfrac><mrow><mn>8</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></mrow><mrow><mi>n</mi><mi>R</mi></mrow></mfrac></mfenced><mi>ln</mi><mn>2</mn><mo>-</mo><mn>6</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub><mo>&#160;</mo><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></math></p><p>For second case: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mi>II</mi></msub><mo>=</mo><mi>W</mi><msub><mo>&#39;</mo><mi>a</mi></msub><mo>+</mo><mi>W</mi><msub><mo>&#39;</mo><mi>b</mi></msub><mo>+</mo><mi>W</mi><msub><mo>&#39;</mo><mi>c</mi></msub><mo>+</mo><mi>W</mi><msub><mo>&#39;</mo><mi>d</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>R</mi><mi>T</mi><mo>&#160;</mo><mi>ln</mi><mfenced><mfrac><mrow><mn>2</mn><msub><mi>V</mi><mn>0</mn></msub></mrow><msub><mi>V</mi><mn>0</mn></msub></mfrac></mfenced><mo>+</mo><mn>0</mn><mo>+</mo><msub><mi>P</mi><mn>0</mn></msub><mfenced><mrow><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>2</mn><msub><mi>V</mi><mn>0</mn></msub></mrow></mfenced><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>R</mi><mfenced><mfrac><mrow><mn>4</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></mrow><mrow><mi>n</mi><mi>R</mi></mrow></mfrac></mfenced><mi>ln</mi><mn>2</mn><mo>-</mo><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub><mo>&#160;</mo><mi>ln</mi><mn>2</mn><mo>-</mo><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></math></p><p>Therefore, required ratio is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>W</mi><mi mathvariant="normal">I</mi></msub><msub><mi>W</mi><mi>II</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub><mi>ln</mi><mn>2</mn><mo>-</mo><mn>2</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></mrow><mrow><mn>4</mn><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub><mi>ln</mi><mn>2</mn><mo>-</mo><msub><mi>P</mi><mn>0</mn></msub><msub><mi>V</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q7. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>One mole of an ideal gas expands adiabatically from an initial state <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msub><mi>T</mi><mi>A</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi>V</mi><mn>0</mn></msub><mo>)</mo></math> to final state <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msub><mi>T</mi><mi>f</mi></msub><mo>,</mo><mo>&#160;</mo><mn>5</mn><msub><mi>V</mi><mn>0</mn></msub><mo>)</mo></math>. Another mole of the same gas expands isothermally from a different initial state <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msub><mi>T</mi><mi>B</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi>V</mi><mn>0</mn></msub><mo>)</mo></math> to the same final state <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><msub><mi>T</mi><mi>f</mi></msub><mo>,</mo><mo>&#160;</mo><mn>5</mn><msub><mi>V</mi><mn>0</mn></msub><mo>)</mo></math>. The ratio of the specific heats at constant pressure and constant volume of this ideal gas is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi></math>. What is the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mi>A</mi></msub><msub><mi>T</mi><mi>B</mi></msub></mfrac></math>?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mrow><mn>1</mn><mo>-</mo><mi>&#947;</mi></mrow></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mi>&#947;</mi></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mrow><mn>1</mn><mo>+</mo><mi>&#947;</mi></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup></math>**

**Detailed Solution:**

<blockquote><p>As we know for an Adiabatic process</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><msup><mi>V</mi><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mtext>Constant</mtext></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/bbe9d799-1e12-4ca5-b1d8-b2ed2f71dd83.png" style="width: 300px; height: 294px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>A</mi></msub><msup><msub><mi>V</mi><mn>0</mn></msub><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msub><mi>T</mi><mi>f</mi></msub><msup><mfenced><mrow><mn>5</mn><msub><mi>V</mi><mn>0</mn></msub></mrow></mfenced><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>For Isothermal process</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>B</mi></msub><mo>=</mo><msub><mi>T</mi><mi>f</mi></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Dividing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> by equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>T</mi><mi>A</mi></msub><msub><mi>T</mi><mi>B</mi></msub></mfrac><mo>=</mo><msup><mn>5</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p></blockquote>

</details>

---

### Q8. JEE Advanced 2022 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>In the given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>-</mo><mi>V</mi></math> diagram, a monoatomic gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#947;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></math> is first compressed adiabatically from state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. Then it expands isothermally from state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> to state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>. [Given : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mrow><mn>0</mn><mo>.</mo><mn>6</mn></mrow></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>,</mo><mi>ln</mi><mn>2</mn><mo>&#8776;</mo><mn>0</mn><mo>.</mo><mn>7</mn></math>].</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/db612306-c4da-45a1-8ecc-e2c81f99f0fe-1.jpg" style="width: 320px; height: 201px;" /></p><p>Which of the following statement(s) is(are) correct?</p>

**Options:**

- **(A)** The magnitude of the total work done in the process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8594;</mo><mi>B</mi><mo>&#8594;</mo><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>144</mn><mo>&#160;</mo><mi>kJ</mi></math>
- **(B)** The magnitude of the work done in the process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>&#8594;</mo><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn><mi>kJ</mi></math>.
- **(C)** The magnitude of the work done in the process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#8594;</mo><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mi>kJ</mi></math>.
- **(D)** The magnitude of the work done in the process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8594;</mo><mi>A</mi></math> is zero.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The magnitude of the work done in the process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8594;</mo><mi>A</mi></math> is zero.**

**Detailed Solution:**

<p>For adiabatic process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><msup><mi>V</mi><mi>&#947;</mi></msup><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>100</mn><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>8</mn></mrow></mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></msup><mo>=</mo><mn>300</mn><msup><mfenced><msub><mi>V</mi><mi>B</mi></msub></mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>V</mi><mi>B</mi></msub><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>8</mn></mrow><msup><mn>3</mn><mrow><mn>3</mn><mo>/</mo><mn>5</mn></mrow></msup></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>3</mn></msup></math></p><p>Work done in an adiabatic process is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mn>1</mn></msub><msub><mi>V</mi><mn>1</mn></msub><mo>-</mo><msub><mi>P</mi><mn>2</mn></msub><msub><mi>V</mi><mn>2</mn></msub></mrow><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>W</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mi>A</mi></msub><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>P</mi><mi>B</mi></msub><msub><mi>V</mi><mi>B</mi></msub></mrow><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>80</mn><mo>-</mo><mn>300</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></mfrac><mo>&#160;</mo><mi>kJ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>W</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>60</mn><mi>kJ</mi></math></p><p>Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> is correct.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#8594;</mo><mi>A</mi></math> is isochoric <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mi>D</mi></mfenced></math> is correct.</p><p>For process <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mi>n</mi><mi>R</mi><mi>T</mi><mi>ln</mi><mfrac><msub><mi>V</mi><mn>2</mn></msub><msub><mi>V</mi><mn>1</mn></msub></mfrac><mo>=</mo><mi>P</mi><mi>V</mi><mi>ln</mi><mfrac><msub><mi>V</mi><mn>2</mn></msub><msub><mi>V</mi><mn>1</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>W</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mn>300</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>4</mn><mi>ln</mi><mfenced close="]" open="["><mfrac><mrow><mn>0</mn><mo>.</mo><mn>8</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>4</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>W</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mn>120</mn><mo>&#215;</mo><mi>ln</mi><mn>2</mn><mo>&#160;</mo><mi>kJ</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>W</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mn>84</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is correct.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>+</mo><msub><mi>W</mi><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>-</mo><mn>60</mn><mo>+</mo><mn>84</mn><mo>=</mo><mn>24</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is incorrect.</p>

</details>

---

### Q9. JEE Advanced 2022 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

A bubble has surface tension <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>. The ideal gas inside the bubble has ratio of specific heats <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math>. The bubble is exposed to the atmosphere and it always retains its spherical shape. When the atmospheric pressure is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub></math>, the radius of the bubble is found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub></math> and the temperature of the enclosed gas is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math>. When the atmospheric pressure is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mrow><mi mathvariant="normal">a</mi><mn>2</mn></mrow></msub></math>, the radius of the bubble and the temperature of the enclosed gas are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>2</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math>, respectively. Which of the following statement(s) is(are) correct?

**Options:**

- **(A)** If the surface of the bubble is a perfect heat insulator, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced><mn>5</mn></msup><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>2</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>2</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfrac></math>
- **(B)** If the surface of the bubble is a perfect heat insulator, then the total internal energy of the bubble including its surface energy does not change with the external atmospheric pressure.
- **(C)** If the surface of the bubble is a perfect heat conductor and the change in atmospheric temperature is negligible, the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfrac></math>
- **(D)** If the surface of the bubble is a perfect heat insulator, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>T</mi><mn>2</mn></msub><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If the surface of the bubble is a perfect heat insulator, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>T</mi><mn>2</mn></msub><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>=</mo><mfrac><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>S</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/498c5902-043c-45a5-a88a-33c1fe621612-image.png" style="width: 204px; height: 200px;" /></p><p>When, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>Pressure</mi></mtd><mtd></mtd><mtd><mi>Radius</mi></mtd><mtd></mtd><mtd><mi>Temperature</mi></mtd></mtr><mtr><mtd><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub></mtd><mtd><mo>&#8594;</mo></mtd><mtd><msub><mi>r</mi><mn>1</mn></msub></mtd><mtd><mo>&#8594;</mo></mtd><mtd><msub><mi>T</mi><mn>1</mn></msub></mtd></mtr><mtr><mtd><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub></mtd><mtd><mo>&#8594;</mo></mtd><mtd><msub><mi>r</mi><mn>2</mn></msub></mtd><mtd><mo>&#8594;</mo></mtd><mtd><msub><mi>T</mi><mn>2</mn></msub></mtd></mtr></mtable></math></p><p>For adiabatic process</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><msubsup><mi>V</mi><mn>1</mn><mi>&#947;</mi></msubsup><mo>=</mo><msub><mi>P</mi><mn>2</mn></msub><msubsup><mi>V</mi><mn>2</mn><mi>&#947;</mi></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfenced><msup><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>r</mi><mn>1</mn><mn>3</mn></msubsup></mrow></mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></msup><mo>=</mo><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow></mfenced><msup><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>r</mi><mn>2</mn><mn>3</mn></msubsup></mrow></mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced><mn>5</mn></msup><mo>=</mo><mfrac><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow></mfenced><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfenced></mfrac></math></p><p>Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> is incorrect.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><msubsup><mi>V</mi><mn>1</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi>T</mi><mn>2</mn></msub><msubsup><mi>V</mi><mn>2</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mn>2</mn></msub><msub><mi>T</mi><mn>1</mn></msub></mfrac><mo>=</mo><msup><mfenced><mfrac><msub><mi>V</mi><mn>1</mn></msub><msub><mi>V</mi><mn>2</mn></msub></mfrac></mfenced><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mfenced><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced><mrow><mn>3</mn><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><msub><mi>T</mi><mn>2</mn></msub><msub><mi>T</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><msup><mfenced><mfrac><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfrac></mfenced><mfrac><mn>2</mn><mn>5</mn></mfrac></msup></math></p><p>Therefore, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>D</mi></mfenced></math> is correct.</p><p>For option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> Total internal energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math> surface energy will not be same as work done by gas will be there. Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> is incorrect.</p><p>For option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> change in temperature is negligible. Therefore, the process is isothermal.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><msub><mi>V</mi><mn>1</mn></msub><mo>=</mo><msub><mi>P</mi><mn>2</mn></msub><msub><mi>V</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfenced><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>r</mi><mn>1</mn><mn>3</mn></msubsup></mrow></mfenced><mo>=</mo><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow></mfenced><mfenced><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>&#960;</mi><msubsup><mi>r</mi><mn>2</mn><mn>3</mn></msubsup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>2</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>2</mn></msub></mfrac></mrow></mfenced><mfenced><mrow><msub><mi>P</mi><mrow><mi>a</mi><mn>1</mn></mrow></msub><mo>+</mo><mfrac><mrow><mn>4</mn><mi>T</mi></mrow><msub><mi>r</mi><mn>1</mn></msub></mfrac></mrow></mfenced></mfrac></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>C</mi></mfenced></math> is correct.</p>

</details>

---

### Q10. JEE Advanced 2022 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>List I describes thermodynamic processes in four different systems. List II gives the magnitudes (either exactly or as a close approximation) of possible changes in the internal energy of the system due to the process.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"> </td>			<td style="text-align: center;"><strong>List-I</strong></td>			<td style="text-align: center;"> </td>			<td style="text-align: center;"><strong>List-II</strong></td>		</tr>		<tr>			<td>(I)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi>kg</mi></math> of water <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mo>&#176;</mo><mi mathvariant="normal">C</mi></math> is converted to steam at the same temperature, at a pressure of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup><mi>Pa</mi></math>. The volume of the system changes from <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><msup><mi mathvariant="normal">m</mi><mn>3</mn></msup></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mi mathvariant="normal">m</mi><mn>3</mn></msup></math> in the process. Latent heat of water <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2250</mn><mo>&#160;</mo><mi>kJ</mi><mo>&#160;</mo><msup><mi>kg</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></td>			<td>(P)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>kJ</mi></math></td>		</tr>		<tr>			<td>(II)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn></math> moles of a rigid diatomic ideal gas with volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> at temperature <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> undergoes an isobaric expansion to volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>V</mi></math>. Assume <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi>mol</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">K</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup></math></td>			<td>(Q)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mi>kJ</mi></math></td>		</tr>		<tr>			<td>(III)</td>			<td>One mole of a monoatomic ideal gas is compressed adiabatically from volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi mathvariant="normal">m</mi><mn>3</mn></msup></math> and pressure <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>kPa</mi></math> to volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>V</mi><mn>8</mn></mfrac></math>.</td>			<td>(R)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi>kJ</mi></math></td>		</tr>		<tr>			<td>(IV)</td>			<td>Three moles of a diatomic ideal gas whose molecules can vibrate, is given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi>kJ</mi></math> of heat and undergoes isobaric expansion.</td>			<td>(S)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>kJ</mi></math></td>		</tr>		<tr>			<td> </td>			<td> </td>			<td>(T)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>kJ</mi></math></td>		</tr>	</tbody></table><p>Which one of the following options is correct?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mi>II</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mi>III</mi><mo>&#8594;</mo><mi mathvariant="normal">S</mi><mo>,</mo><mi>IV</mi><mo>&#8594;</mo><mi mathvariant="normal">Q</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi mathvariant="normal">S</mi><mo>,</mo><mi>II</mi><mo>&#8594;</mo><mi mathvariant="normal">P</mi><mo>,</mo><mi>III</mi><mo>&#8594;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mi>IV</mi><mo>&#8594;</mo><mi mathvariant="normal">P</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi mathvariant="normal">P</mi><mo>,</mo><mi>II</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mi>III</mi><mo>&#8594;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mi>IV</mi><mo>&#8594;</mo><mi mathvariant="normal">Q</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi mathvariant="normal">Q</mi><mo>,</mo><mi>II</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mi>III</mi><mo>&#8594;</mo><mi mathvariant="normal">S</mi><mo>,</mo><mi>IV</mi><mo>&#8594;</mo><mi mathvariant="normal">T</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi mathvariant="normal">P</mi><mo>,</mo><mi>II</mi><mo>&#8594;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mi>III</mi><mo>&#8594;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mi>IV</mi><mo>&#8594;</mo><mi mathvariant="normal">Q</mi></math>**

**Detailed Solution:**

<blockquote><p>(I)</p><p>According to the first law of thermodynamics,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>Q</mi><mo>=</mo><mo>&#8710;</mo><mi>U</mi><mo>+</mo><mi>W</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#8710;</mo><mi>U</mi><mo>=</mo><mo>&#8710;</mo><mi>Q</mi><mo>-</mo><mi>W</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>U</mi><mo>=</mo><mi>M</mi><mi>L</mi><mo>-</mo><mi>P</mi><mi>&#916;</mi><mi>V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>2250</mn><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup><mi>kP</mi><mo>&#215;</mo><mfenced><mrow><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfenced><msup><mi mathvariant="normal">m</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi>kJ</mi><mo>-</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, <strong>I-P</strong></p><p>(II)</p><p>For isobaric process,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>V</mi><mn>1</mn></msub><msub><mi>V</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>T</mi><mn>1</mn></msub><msub><mi>T</mi><mn>2</mn></msub></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>500</mn><mo>=</mo><mn>1500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math></p><p>Now the change in the internal energy will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>U</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>V</mi></msub><mo>&#8710;</mo><mi>T</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>1000</mn><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, <strong>II-R</strong></p><p>(III) </p><p>For adiabatic expansion of monoatomic gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#947;</mi><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><msubsup><mi>V</mi><mn>1</mn><mi>&#947;</mi></msubsup><mo>=</mo><msub><mi>P</mi><mn>2</mn></msub><msubsup><mi>V</mi><mn>2</mn><mi>&#947;</mi></msubsup><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>kPa</mi></mrow></mfenced><mo>&#215;</mo><msubsup><mi>V</mi><mn>0</mn><mfrac><mn>5</mn><mn>3</mn></mfrac></msubsup><mo>=</mo><msub><mi>P</mi><mn>2</mn></msub><mo>&#215;</mo><msup><mfenced><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>8</mn></mfrac></mfenced><mfrac><mn>5</mn><mn>3</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>P</mi><mn>2</mn></msub><mo>=</mo><mn>64</mn><mo>&#160;</mo><mi>kPa</mi></math></p><p>Now the change in the internal energy will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>U</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>v</mi></msub><mi>&#916;</mi><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mi>n</mi><mi>R</mi><mi>&#916;</mi><mi>T</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mfenced><mrow><msub><mi>P</mi><mn>2</mn></msub><msub><mi>V</mi><mn>2</mn></msub><mo>-</mo><msub><mi>P</mi><mn>1</mn></msub><msub><mi>V</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mn>64</mn><mo>&#215;</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#215;</mo><mn>8</mn></mrow></mfrac><mo>-</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, <strong>III-T</strong></p><p>(IV)</p><p>For diatomic gas whose molecules vibrate,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>V</mi></msub><mo>=</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mi>R</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>P</mi></msub><mo>=</mo><mfrac><mn>8</mn><mn>2</mn></mfrac><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#916;</mi><mi>U</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>V</mi></msub><mi>&#916;</mi><mi>T</mi><mo>=</mo><mn>3</mn><mi>n</mi><mi>R</mi><mi>&#916;</mi><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>Q</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>p</mi></msub><mi>&#916;</mi><mi>T</mi><mo>=</mo><mn>4</mn><mi>n</mi><mi>R</mi><mi>&#916;</mi><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#916;</mi><mi>U</mi></mrow><mrow><mi>&#916;</mi><mi>Q</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>U</mi><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#215;</mo><mn>9</mn><mo>=</mo><mn>6</mn><mo>.</mo><mn>75</mn><mo>&#8771;</mo><mn>7</mn><mo>&#160;</mo><mi>kJ</mi></math></p><p>Therefore, <strong>IV-Q</strong></p></blockquote>

</details>

---

### Q11. JEE Advanced 2021 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

<strong>Paragraph</strong>
A thermally insulating cylinder has a thermally insulating and frictionless movable partition in the middle, as shown in the figure below. On each side of the partition, there is one mole of an ideal gas, with specific heat at constant volume, $C_{V}=2 R$. Here, $R$ is the gas constant. Initially, each side has a volume $V_{0}$ and temperature $T_{0}$. The left side has an electric heater, which is turned on at very low power to transfer heat $Q$ to the gas on the left side. As a result the partition moves slowly towards the right reducing the right side volume to $V_{0} / 2$. Consequently, the gas temperatures on the left and the right sides become $T_{L}$ and $T_{R}$, respectively. Ignore the changes in the temperatures of the cylinder, heater and the partition.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/p8IneHxu3YaUNuVY3QLUlwxRAGZWGt2P9beHpCJB0rY.original.fullsize.png" />
<strong>Question</strong>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></mrow></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ea3f1fe0-bb61-483d-8a3a-d01ce55c4578-9fc8c270-5260-45ad-b7f4-8153967f381c-image.png" style="width: 300px; height: 406px;" /></p><p>Writing <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>V</mi></msub></math> in terms of degree of freedom of the gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>V</mi></msub><mo>=</mo><mfrac><mi>f</mi><mn>2</mn></mfrac><mi>R</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">R</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>f</mi><mo>=</mo><mn>4</mn><mo>,</mo></math></p><p>Therefore,​ adiabatic index of gas will be given by,​​​​​​<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mi>f</mi></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>The gas of the right portion has undergone through an adiabatic process so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>i</mi></msub><msubsup><mi>V</mi><mi>i</mi><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi>T</mi><mi>f</mi></msub><msubsup><mi>V</mi><mi>f</mi><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>T</mi><mn>0</mn></msub><msubsup><mrow><mo>&#160;</mo><mi>V</mi></mrow><mn>0</mn><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi>T</mi><mi>R</mi></msub><msup><mfenced><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></mfrac></mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>R</mi></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msub><mi>T</mi><mn>0</mn></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><msub><mi>T</mi><mi>R</mi></msub><msub><mi>T</mi><mn>0</mn></msub></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p><p>Work done by the gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mo>&#8710;</mo><mi>U</mi><mo>=</mo><mo>-</mo><mi>n</mi><msub><mi>C</mi><mi>V</mi></msub><mfenced><mrow><msub><mi>T</mi><mi>f</mi></msub><mo>-</mo><msub><mi>T</mi><mi>i</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mn>1</mn></mfenced><mfenced><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfenced><mfenced><mrow><msqrt><mn>2</mn></msqrt><msub><mi>T</mi><mn>0</mn></msub><mo>-</mo><msub><mi>T</mi><mn>0</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></math></p><p>So work done by the gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>+</mo><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>V</mi><mo>=</mo><mi>n</mi><mi>R</mi><mi>T</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>P</mi><mo>&#8733;</mo><mfrac><mi>T</mi><mi>V</mi></mfrac></math></p><p>For gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8594;</mo><msqrt><mn>2</mn></msqrt></math> times of initial value, Volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> times of initial value</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8733;</mo><mfrac><msqrt><mn>2</mn></msqrt><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt></math> times of initial value<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>P</mi><mi>f</mi></msub><mo>=</mo><mn>2</mn><msqrt><mn>2</mn></msqrt><msub><mi>P</mi><mn>0</mn></msub></math></p><p>So pressure of the gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> will also be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math> times and volume of gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> becomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math> times</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>&#8733;</mo><mi>P</mi><mi>V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>T</mi><mo>&#8733;</mo><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt></math> times of initial value</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>L</mi></msub><mo>=</mo><mn>3</mn><msqrt><mn>2</mn></msqrt><msub><mrow><mo>&#160;</mo><mi>T</mi></mrow><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>U</mi></math> for the left gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>V</mi></msub><mfenced><mrow><msub><mi>T</mi><mi>f</mi></msub><mo>-</mo><msub><mi>T</mi><mi>i</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mn>1</mn></mfenced><mfenced><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfenced><mfenced><mrow><mn>3</mn><msqrt><mn>2</mn></msqrt><msub><mi>T</mi><mn>0</mn></msub><mo>-</mo><msub><mi>T</mi><mn>0</mn></msub></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></math></p><p>Heat given to gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math>,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mi>W</mi><mo>+</mo><mo>&#8710;</mo><mi>U</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub><mo>+</mo><mfenced><mrow><mn>6</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>2</mn></mrow></mfenced><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msub><mi>RT</mi><mn>0</mn></msub><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>Q</mi><mrow><mi>R</mi><msub><mi>T</mi><mn>0</mn></msub></mrow></mfrac><mo>=</mo><mn>4</mn><mfenced><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></math></p>

</details>

---

### Q12. JEE Advanced 2021 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph</strong>
A thermally insulating cylinder has a thermally insulating and frictionless movable partition in the middle, as shown in the figure below. On each side of the partition, there is one mole of an ideal gas, with specific heat at constant volume, $C_{V}=2 R$. Here, $R$ is the gas constant. Initially, each side has a volume $V_{0}$ and temperature $T_{0}$. The left side has an electric heater, which is turned on at very low power to transfer heat $Q$ to the gas on the left side. As a result the partition moves slowly towards the right reducing the right side volume to $V_{0} / 2$. Consequently, the gas temperatures on the left and the right sides become $T_{L}$ and $T_{R}$, respectively. Ignore the changes in the temperatures of the cylinder, heater and the partition.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/p8IneHxu3YaUNuVY3QLUlwxRAGZWGt2P9beHpCJB0rY.original.fullsize.png" />
<strong>Question</strong>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mi>R</mi></msub><msub><mi>T</mi><mn>0</mn></msub></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>2</mn></msqrt></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ea3f1fe0-bb61-483d-8a3a-d01ce55c4578-9fc8c270-5260-45ad-b7f4-8153967f381c-image.png" style="width: 300px; height: 406px;" /></p><p>Writing <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>V</mi></msub></math> in terms of degree of freedom of the gas <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math>, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>V</mi></msub><mo>=</mo><mfrac><mi>f</mi><mn>2</mn></mfrac><mi>R</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">R</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>f</mi><mo>=</mo><mn>4</mn><mo>,</mo></math></p><p>Therefore,​ adiabatic index of gas will be given by,​​​​​​<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#947;</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mi>f</mi></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>The gas of the right portion has undergone through an adiabatic process so,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>i</mi></msub><msubsup><mi>V</mi><mi>i</mi><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi>T</mi><mi>f</mi></msub><msubsup><mi>V</mi><mi>f</mi><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>T</mi><mn>0</mn></msub><msubsup><mrow><mo>&#160;</mo><mi>V</mi></mrow><mn>0</mn><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi>T</mi><mi>R</mi></msub><msup><mfenced><mfrac><msub><mi>V</mi><mn>0</mn></msub><mn>2</mn></mfrac></mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>R</mi></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msub><mi>T</mi><mn>0</mn></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><msub><mi>T</mi><mi>R</mi></msub><msub><mi>T</mi><mn>0</mn></msub></mfrac><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q13. JEE Advanced 2021 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

An ideal gas undergoes a four step cycle as shown in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>-</mo><mi>V</mi></math> diagram below. During this cycle, heat is absorbed by the gas in:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/4d18554e-7e8e-4c08-957f-347a7804e825-image.png" style="width: 280px; height: 190px;" />

**Options:**

- **(A)** steps <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** steps <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** steps <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** steps <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) steps <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>P</mi><mi>V</mi><mo>=</mo><mi>n</mi><mi>R</mi><mi>T</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>In Step <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo></math>constant</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo></math> increasing</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> also will be increase (From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>)</p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>p</mi></msub><mo>&#8710;</mo><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mi>T</mi><mo>&#160;</mo><mo>&#8593;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8710;</mo><mi>T</mi><mo>=</mo></math> Positive</p><p>So,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mo>+</mo><mi>v</mi><mi>e</mi><mo>=</mo></math>absorbed</p><p>Now In step <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mo>&#8593;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo></math> constant</p><p>So from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math> will also be increasing.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>v</mi></msub><mo>&#8710;</mo><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>T</mi><mo>&#8593;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8710;</mo><mi>T</mi><mo>=</mo></math>Positive</p><p>So, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mo>+</mo><mi>v</mi><mi>e</mi><mo>=</mo></math>absorbed</p><p>correct option is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math>.</p>

</details>

---

### Q14. JEE Advanced 2018 (Paper 2)

*Type:* `numerical` | *Level:* `1`

One mole of an ideal monatomic gas undergoes an adiabatic expansion in which its volume becomes eight times its initial value. If the initial temperature of the gas is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#8201;</mo><mi mathvariant="normal">K</mi></math> and the universal gas constant <math><mi>R</mi><mo>=</mo><mn>8.0</mn><mi>&#160;J</mi><mi>&#160;</mi><mn>mo</mn><msup><mrow><mn>l</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><msup><mrow><mn>&#160;K</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>, then how much is the decrease in its internal energy (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">J</mi></math>) ?

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **900**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>i</mi></msub><mo>=</mo><mi>V</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>f</mi></msub><mo>=</mo><mn>8</mn><mi>V</mi></math>
For adiabatic process <math><mo>{</mo><mrow><mi>&#947;</mi><mo>=</mo><mrow><mn>5/</mn></mrow><mrow><mn>3</mn></mrow></mrow></math> for monoatomic gas<math><mo>}</mo></math>
<math> <mrow> <msub> <mi>T</mi> <mn>1</mn> </msub> <mo>&#8901;</mo><msubsup> <mi>V</mi> <mn>1</mn> <mrow> <mi>&#947;</mi><mo>&#8722;</mo><mn>1</mn></mrow> </msubsup> <mo>=</mo><msub> <mi>T</mi> <mn>2</mn> </msub> <mo>&#8901;</mo><msubsup> <mi>V</mi> <mn>2</mn> <mrow> <mi>&#947;</mi><mo>&#8722;</mo><mn>1</mn></mrow> </msubsup> </mrow> </math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msup><mfenced separators="|"><mi>V</mi></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>=</mo><msub><mi>T</mi><mn>2</mn></msub><msup><mfenced separators="|"><mrow><mn>8</mn><mi>V</mi></mrow></mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></math>
<math><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>25</mn><mi>&#160;</mi><mn>K</mn></math>
Loss in internal energy <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>U</mi><mo>=</mo><mi>n</mi><msub><mi>C</mi><mi>v</mi></msub><mo>&#8710;</mo><mi>T</mi><mo>=</mo><mn>1</mn><mfenced separators="|"><mfrac><mrow><mi>f</mi><mi>R</mi></mrow><mn>2</mn></mfrac></mfenced><mfenced open="[" close="]" separators="|"><mrow><mn>100</mn><mo>-</mo><mn>25</mn></mrow></mfenced><mo>=</mo><mn>12</mn><mo>&#215;</mo><mn>75</mn><mo>=</mo><mn>900</mn><mi>&#160;</mi><mi mathvariant="normal">J</mi></math>

</details>

---

### Q15. JEE Advanced 2018 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>One mole of a monatomic ideal gas undergoes a cyclic process as shown in the figure (where V is the volume and T is the temperature). Which of the statements below is (are) true?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/uieuqvzzvewinicdbyzpenrltlqfiarsyaepiqsqnhnpwrhdya.jpeg"/></p>

**Options:**

- **(A)** Process  <math><mi>I</mi></math>  is an isochoric process
- **(B)** In process <math><mi>I</mi><mi>I</mi></math> , gas absorbs heat
- **(C)** In process <math><mi>I</mi><mi>V</mi></math> , gas releases heat
- **(D)** Processes <math><mi> </mi><mi>I</mi><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>I</mi><mi>I</mi><mi>I</mi></math> are not isobaric

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Processes <math><mi> </mi><mi>I</mi><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>I</mi><mi>I</mi><mi>I</mi></math> are not isobaric**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/uieuqvzzvewinicdbyzpenrltlqfiarsyaepiqsqnhnpwrhdya.jpeg"/>
<math><mo>(</mo><mi>A</mi><mo>)</mo></math> Process- <math><mi>I</mi></math> is not isochoric, V is decreasing
<math><mo>(</mo><mi>B</mi><mo>)</mo></math> Process- <math><mi>I</mi><mi>I</mi></math> is isothermal expansion
<math><mo>∆</mo><mi>U</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>W</mi><mo>></mo><mn>0</mn></math>
<math><mo>∆</mo><mi>Q</mi><mo>></mo><mn>0</mn></math>
<math><mo>(</mo><mi>C</mi><mo>)</mo></math> Process- <math><mi>I</mi><mi>V</mi></math> is isothermal compression
<math><mo>∆</mo><mi>U</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>W</mi><mo><</mo><mn>0</mn></math>
<math><mo>∆</mo><mi>Q</mi><mo><</mo><mn>0</mn></math>
<math><mo>(</mo><mi>D</mi><mo>)</mo></math> Process- <math><mi>I</mi><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>I</mi><mi>I</mi><mi>I</mi></math> are NOT isobaric because in isobaric process <math><mi>T</mi><mi> </mi><mo>∝</mo><mi> </mi><mi>V</mi></math> hence isobaric <math><mi>T</mi><mo>–</mo><mi>V</mi></math> graph will be linear

</details>

---

### Q16. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>An ideal gas is undergoing a cyclic thermodynamic process in different ways as shown in the corresponding P-V diagrams in column 3 of the table. Consider only the path from state 1 to state 2. W denotes the corresponding work done on the system. The equations and plots in the table have standard notations as used in thermodynamic process. Here <math><mi>γ</mi></math> is the ratio of heat capacities at constant pressure and constant volume. The number of moles in the gas is <em>n.</em>
 </p><table border="1"><tbody><tr><td>Column – 1</td><td>Column – 2</td><td>Column – 3</td></tr><tr><td>(I) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>γ</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mfenced separators="|"><mrow><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math></td><td>(i) Isothermal</td><td>(P) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/lmyvdpttsrpqwdvdnxdvvcfbkrknvccejymdxqeejxsxjsotmy.jpeg"/></td></tr><tr><td>(II) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></math></td><td>(ii) Isochoric</td><td>(Q) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/nzfxfleovwlhxkjymqdefzstwzpxdzstjpxiutuqkvybauqfgs.jpeg"/></td></tr><tr><td>(III) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math></td><td>(iii) Isobaric</td><td>(R) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/mkbiobegecrigtxewqjbjrearleyzigzeedhwsgyucvwjqjuff.jpeg"/></td></tr><tr><td>(IV) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>n</mi><mi>R</mi><mi>T</mi><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mrow></math></td><td>(iv) Adiabatic</td><td>(S) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ndzhvngdlioiwvoruyzkbhwwwkgnjkqnvsqtnrsjbzwubzdxth.jpeg"/></td></tr></tbody></table>Which of the following options is the only correct representation of the process <math><mo>∆</mo><mi>U</mi><mo>=</mo><mo>∆</mo><mi>Q</mi><mo>-</mo><mi>P</mi><mo>∆</mo><mi>V</mi></math> ?

**Options:**

- **(A)** <math><mo>(</mo><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>Q</mi><mo>)</mo></math>
- **(B)** <math><mo>(</mo><mi>I</mi><mi>V</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>R</mi><mo>)</mo></math>
- **(C)** <math><mo>(</mo><mi>II</mi><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>) </mo><mo>(</mo><mi>R</mi><mo>)</mo></math>
- **(D)** <math><mo>(</mo><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>) </mo><mo>(</mo><mi>Q</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>(</mo><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>) </mo><mo>(</mo><mi>Q</mi><mo>)</mo></math>**

**Detailed Solution:**

The correct match is (I) (iv) (Q)

</details>

---

### Q17. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>An ideal gas is undergoing a cyclic thermodynamic process in different ways as shown in the corresponding P-V diagrams in column 3 of the table. Consider only the path from state 1 to state 2. W denotes the corresponding work done on the system. The equations and plots in the table have standard notations as used in thermodynamic process. Here <math><mi>γ</mi></math> is the ratio of heat capacities at constant pressure and constant volume. The number of moles in the gas is n.
 </p><table border="1"><tbody><tr><td>Column – 1</td><td>Column – 2</td><td>Column – 3</td></tr><tr><td>(I) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>γ</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mfenced separators="|"><mrow><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math></td><td>(i) Isothermal</td><td>(P) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/aaf7f771-5d26-42be-a1dc-b924c98ca07b-image.png"/></td></tr><tr><td>(II) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></math></td><td>(ii) Isochoric</td><td>(Q) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/9e4d8f91-f184-49c2-8a4b-b7c17ddd3d55-image.png"/></td></tr><tr><td>(III) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math></td><td>(iii) Isobaric</td><td>(R) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/011b3ca9-05cf-446d-b15b-55a09c5c59c3-image.png"/></td></tr><tr><td>(IV) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>n</mi><mi>R</mi><mi>T</mi><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mrow></math></td><td>(iv) Adiabatic</td><td>(S) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/c8d42344-5fa3-428e-afe5-c4182b4ff048-image.png"/></td></tr></tbody></table>Which one of the following options is the correct combination?

**Options:**

- **(A)** <math><mo>(</mo><mi>I</mi><mi>V</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>S</mi><mo>)</mo></math>
- **(B)** <math><mo>(</mo><mi>III</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>S</mi><mo>)</mo></math>
- **(C)** <math><mo>(</mo><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>Q</mi><mo>)</mo></math>
- **(D)** <math><mo>(</mo><mi>I</mi><mi>I</mi><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>) </mo><mo>(</mo><mi>R</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mo>(</mo><mi>III</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>) </mo><mo>(</mo><mi>S</mi><mo>)</mo></math>**

**Detailed Solution:**

The correct match is (III) (ii) (S)

</details>

---

### Q18. JEE Advanced 2017 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>An ideal gas is undergoing a cyclic thermodynamic process in different ways as shown in the corresponding P-V diagrams in column 3 of the table. Consider only the path from state 1 to state 2. W denotes the corresponding work done on the system. The equations and plots in the table have standard notations as used in thermodynamic process. Here <math><mi>γ</mi></math> is the ratio of heat capacities at constant pressure and constant volume. The number of moles in the gas in n.</p><table border="1"><tbody><tr><td>Column – 1</td><td>Column – 2</td><td>Column – 3</td></tr><tr><td>(I) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>γ</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mfenced separators="|"><mrow><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math></td><td>(i) Isothermal</td><td>(P) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/lmyvdpttsrpqwdvdnxdvvcfbkrknvccejymdxqeejxsxjsotmy.jpeg"/></td></tr><tr><td>(II) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mi>P</mi><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></math></td><td>(ii) Isochoric</td><td>(Q) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/nzfxfleovwlhxkjymqdefzstwzpxdzstjpxiutuqkvybauqfgs.jpeg"/></td></tr><tr><td>(III) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>0</mn></math></td><td>(iii) Isobaric</td><td>(R) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/mkbiobegecrigtxewqjbjrearleyzigzeedhwsgyucvwjqjuff.jpeg"/></td></tr><tr><td>(IV) <math><msub><mrow><mi>W</mi></mrow><mrow><mn>1</mn><mo>→</mo><mn>2</mn></mrow></msub><mo>=</mo><mi> </mi><mo>-</mo><mi>n</mi><mi>R</mi><mi>T</mi><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mrow></math></td><td>(iv) Adiabatic</td><td>(S) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ndzhvngdlioiwvoruyzkbhwwwkgnjkqnvsqtnrsjbzwubzdxth.jpeg"/></td></tr></tbody></table>Which one of the following options correctly represents a thermodynamic process that is used as a correction in the determination of the speed of sound in ideal gas?

**Options:**

- **(A)** <math><mo>(</mo><mi>I</mi><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>v</mi><mo>) </mo><mo>(</mo><mi>R</mi><mo>)</mo></math>
- **(B)** <math><mo>(</mo><mi>III</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>ii</mi><mo>) </mo><mo>(</mo><mi>P</mi><mo>)</mo></math>
- **(C)** <math><mo>(</mo><mi>II</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>ii</mi><mo>) </mo><mo>(</mo><mi>S</mi><mo>)</mo></math>
- **(D)** <math><mo>(</mo><mi>I</mi><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>ii</mi><mo>) </mo><mo>(</mo><mi>P</mi><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>(</mo><mi>I</mi><mi>I</mi><mo>) </mo><mo>(</mo><mi>i</mi><mi>ii</mi><mo>) </mo><mo>(</mo><mi>P</mi><mo>)</mo></math>**

**Detailed Solution:**

It is for an adiabatic process. The correct match is (II) (iii) (P).

</details>

---

### Q19. JEE Advanced 2016 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

A gas is enclosed in a cylinder with a movable frictionless piston. Its initial thermodynamic state at pressure <math><msub><mrow><mi>P</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></msup><mi>&#160;</mi><mi>P</mi><mi>a</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><mi>v</mi><mi>o</mi><mi>l</mi><mi>u</mi><mi>m</mi><mi>e</mi><mi>&#160;</mi><msub><mrow><mi>V</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>3</mn></mrow></msup></math> changes to a final state at <math><msub><mrow><mi>P</mi></mrow><mrow><mi>f</mi></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>32</mn></mrow></mfrac></mrow></mfenced><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>5</mn></mrow></msup><mi>&#160;</mi><mi>P</mi><mi>a</mi><mi>&#160;</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>&#160;</mi><msub><mrow><mi>V</mi></mrow><mrow><mi>f</mi></mrow></msub><mo>=</mo><mn>8</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi>&#160;</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>3</mn></mrow></msup></math> in an adiabatic quasi - static process, such that <math><msup><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>V</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>=</mo></math> constant. Consider another thermodynamic process that brings the system from the same initial state to the same final state in two steps: an isobaric expansion at <math><msub><mrow><mi>P</mi></mrow><mrow><mi>i</mi></mrow></msub></math> followed by an isochoric (isovolumetric) process at volumes <math><msub><mrow><mi>V</mi></mrow><mrow><mi>f</mi></mrow></msub></math> . The amount of heat supplied to the system in the two step process is approximately

**Options:**

- **(A)** 112 J
- **(B)** 294 J
- **(C)** 588 J
- **(D)** 813 J

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 588 J**

**Detailed Solution:**

<p>In adiabatic process
<math><msup><mrow><mi>P</mi></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mi>V</mi></mrow><mrow><mn>5</mn></mrow></msup><mo>=</mo></math> constant
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>P</mi><msup><mrow><mi>V</mi></mrow><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>=</mo></math> constant
<math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>γ</mi><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>⇒</mo><mi> </mi><mi> </mi><msub><mrow><mi>C</mi></mrow><mrow><mi>V</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>R</mi><mi> </mi><mi> </mi><mi>a</mi><mi>n</mi><mi>d</mi><mi> </mi><msub><mrow><mi>C</mi></mrow><mrow><mi>P</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>R</mi></math>
In another process
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_5.jpg"/>
<math><mo>∆</mo><mi>Q</mi><mo>=</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>P</mi></mrow></msub><mo>∆</mo><mi>T</mi><mo>+</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>v</mi></mrow></msub><mo>∆</mo><mi>T</mi></math>
<math><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi>n</mi><mi>R</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>n</mi><mi>R</mi><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mi>C</mi></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow></mfenced></math>
<math><mo>∆</mo><mi>Q</mi><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><msub><mrow><mi>P</mi></mrow><mrow><mi>B</mi></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mi>A</mi></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mi>A</mi></mrow></msub></mrow></mfenced><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mfenced separators="|"><mrow><msub><mrow><mi>P</mi></mrow><mrow><mi>C</mi></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mi>C</mi></mrow></msub><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mi>B</mi></mrow></msub><msub><mrow><mi>V</mi></mrow><mrow><mi>B</mi></mrow></msub></mrow></mfenced></math>
Putting values
<math><mo>∆</mo><mi>Q</mi><mo>=</mo><mn>587.5</mn><mi> </mi><mi>J</mi><mi> </mi><mo>≈</mo><mn>588</mn><mi>J</mi></math></p>

</details>

---

### Q20. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>One mole of a monatomic ideal gas is taken along two cyclic processes <math> <mrow> <mtext>E</mtext> <mo>&#8594;</mo> <mtext>F</mtext> <mo>&#8594;</mo> <mtext>G</mtext> <mo>&#8594;</mo> <mtext>E</mtext> <mo>&#160;and&#160;</mo> <mtext>E</mtext> <mo>&#8594;</mo> <mtext>F</mtext> <mo>&#8594;</mo> <mtext>H</mtext> <mo>&#8594;</mo> <mtext>E</mtext> </mrow> </math> as shown in the PV diagram. The processes involved are purely isochoric, isobaric, isothermal or adiabatic.
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012664.jpg" style="line-height: 1.6em; width: 344px; height: 252px;" />
Match the paths in List I with the magnitudes of the work done in List II and select the correct answer using the codes given below the lists.
<math> <mrow> <mtable> <mtr> <mtd> </mtd> <mtd> <mtext>List I</mtext> </mtd> <mtd> </mtd> <mtd> </mtd> <mtd> <mtext>List II</mtext> </mtd> </mtr> <mtr> <mtd> <mtext>A.</mtext> </mtd> <mtd> <mtext>G</mtext> <mn>&#8594;</mn> <mtext>E&#160;&#160;</mtext> </mtd> <mtd> </mtd> <mtd> <mn>P</mn> <mtext>.</mtext> </mtd> <mtd> <mn>1</mn> <mn>6</mn> <mn>0&#160;</mn> <msub> <mtext>P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> <mtext>&#160;ln</mtext> <mn>2</mn> </mtd> </mtr> <mtr> <mtd> <mtext>B.</mtext> </mtd> <mtd> <mtext>G</mtext> <mn>&#8594;</mn> <mtext>H&#160;&#160;</mtext> </mtd> <mtd> </mtd> <mtd> <mn>Q</mn> <mtext>.</mtext> </mtd> <mtd> <mn>3</mn> <mn>6</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mtd> </mtr> <mtr> <mtd> <mtext>C.</mtext> </mtd> <mtd> <mtext>F</mtext> <mn>&#8594;</mn> <mtext>H&#160;&#160;</mtext> </mtd> <mtd> </mtd> <mtd> <mn>R</mn> <mtext>.</mtext> </mtd> <mtd> <mn>2</mn> <mn>4</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mtd> </mtr> <mtr> <mtd> <mtext>D.</mtext> </mtd> <mtd> <mtext>F</mtext> <mn>&#8594;</mn> <mtext>G&#160;&#160;</mtext> </mtd> <mtd> </mtd> <mtd> <mn>S</mn> <mtext>.</mtext> </mtd> <mtd> <mn>3</mn> <mn>1</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mtd> </mtr> </mtable> </mrow> </math></p>

**Options:**

- **(A)** a-q;b-s;c-r;d-p;
- **(B)** a-s;b-r;c-q;d-p;
- **(C)** a-q;b-s;c-r;d-p;
- **(D)** a-q;b-r;c-s;d-p;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) a-s;b-r;c-q;d-p;**

**Detailed Solution:**

<u><strong><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012664_AnsExp1_1.jpg" style="width: 450px; height: 294px;" /></strong></u>
<math> <mrow> <mtext>F</mtext> <mo>&#8594;</mo> <mtext>G</mtext> <mn>&#160;work done in isothermal process is nRT ln </mn> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <msub> <mtext>V</mtext> <mtext>f</mtext> </msub> </mrow> <mrow> <msub> <mtext>V</mtext> <mtext>i</mtext> </msub> </mrow> </mfrac> </mrow> </mfenced> <mo>=</mo> <mn>3</mn> <mn>2</mn> <msub> <mtext>P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> <mtext>ln</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>3</mn> <mn>2</mn> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> <mrow> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
<math> <mrow> <mo>=</mo> <mn>3</mn> <mn>2</mn> <msub> <mtext>P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> <mtext>ln</mtext> <msup> <mn>2</mn> <mn>5</mn> </msup> <mo>=</mo> <mn>1</mn> <mn>0</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> <mtext>ln 2</mtext> </mrow> </math>
<math> <mrow> <mtext>ln</mtext> <mtext>&#160;G</mtext> <mo>&#10230;</mo> <mtext>E</mtext> <mtext>,</mtext> <mspace width="0.5em"></mspace> <mo>&#916;</mo> <mtext>W</mtext> <mo>=</mo> <msub> <mtext>P</mtext> <mn>0</mn> </msub> <mfenced close=")" open="(" separators=","> <mrow> <mn>3</mn> <mn>1</mn> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </mfenced> <mo>=</mo> <mn>3</mn> <mn>1</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </math>
<math> <mrow> <mtext>ln</mtext> <mtext>&#160;G</mtext> <mo>&#10230;</mo> <mtext>H</mtext> </mrow> </math> work done is less than <math> <mrow> <mn>3</mn> <mn>1</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </math> i.e., <math> <mrow> <mn>2</mn> <mn>4</mn> <msub> <mtext>P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </math>
<math> <mrow> <mtext>ln</mtext> <mtext>&#160;F</mtext> <mo>&#10230;</mo> <mtext>H</mtext> </mrow> </math> work done is <math> <mrow> <mn>3</mn> <mn>6</mn> <msub> <mtext>&#160;P</mtext> <mn>0</mn> </msub> <msub> <mtext>V</mtext> <mn>0</mn> </msub> </mrow> </math>

</details>

---

### Q21. JEE Advanced 2011 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

$5.6 \mathrm{~L}$ of helium gas at STP is adiabatically compressed to $0.7 \mathrm{~L}$. Taking the initial temperature to be $T_1$, the work done in the process is

**Options:**

- **(A)** $\frac{9}{8} R T_1$
- **(B)** $\frac{3}{2} R T_1$
- **(C)** $\frac{15}{8} R T_1$
- **(D)** $\frac{9}{2} R T_1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{9}{8} R T_1$**

**Detailed Solution:**

At STP, 22.4 L of any gas is 1 mole.
$$
\therefore \quad 5.6 \mathrm{~L}=\frac{5.6}{22.4}=\frac{1}{4} \text { moles }=n
$$

In adiabatic process,
$$
\begin{array}{rlrl} 
& T V^{\gamma-1} & =\text { constant } \\
& \therefore & T_2 V_2^{\gamma-1} & =T_1 V_1^{\gamma-1} \\
& \text { or } & T_2 & =T_1\left(\frac{V_1}{V_2}\right)^{\gamma-1}
\end{array}
$$

$$
\begin{aligned}
& \gamma=\frac{C_p}{C_V}=\frac{5}{3} \text { for monoatomic He gas. } \\
& \therefore \quad T_2=T_1\left(\frac{5.6}{0.7}\right)^{\frac{5}{3}-1}=4 T_1 \\
& \because \text { Further in adiabatic process, } \\
& Q=0 \\
& \therefore \quad W+\Delta U=0 \\
& \text { or } \quad W=-\Delta U \\
& =-n C_V \Delta T \\
& =-n\left(\frac{R}{\gamma-1}\right)\left(T_2-T_1\right) \\
& =-\frac{1}{4}\left(\frac{R}{\frac{5}{3}-1}\right)\left(4 T_1-T_1\right) \\
& =-\frac{9}{8} R T_1 \\
&
\end{aligned}
$$

$\therefore$ Correct option is (a).
Analysis of Question
(i) From calculation point of view question is moderately tough.
(ii) Volume of gas is decreasing. Therefore, work done by the gas should be negative.

</details>

---

### Q22. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `1`

A diatomic ideal gas is compressed adiabatically to $\frac{1}{32}$ of its initial volume. If the initial temperature of the gas is $T_i$ $T_i$ (in kelvin) and the final temperature is $a T_i$, the value of $a$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

In adiabatic process,
$$
\begin{aligned}
& T V^{\gamma-1}=\text { constant } \\
& \therefore T_i V_i^{0.4}=T_f V_f^{0.4} \\
& \text { (as } \gamma=1.4 \text { for diatomic gas) } \\
& \text { or } \quad T_i V_i^{0.4}=\left(\alpha T_i\right)\left(\frac{V_i}{32}\right)^{0.4} \\
& \text { or } \quad \alpha(32)^{0.4}=4 \\
&
\end{aligned}
$$
$\therefore$ The correct answer is 4 .

</details>

---

### Q23. JEE Advanced 2010 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

One mole of an ideal gas in initial state A undergoes a cyclic process $A B C A$, as shown in the figure. Its pressure at $A$ is $p_0$. Choose the correct option(s) from the following
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YOIwtV0RRE5ULb6-11MzP9TjZOlhttuirHvaljEJBUY.original.fullsize.png">

**Options:**

- **(A)** Internal energies at $A$ and $B$ are the same
- **(B)** Work done by the gas in process $A B$ is $p_0 V_0 \ln 4$
- **(C)** Pressure at $C$ is $\frac{p_0}{4}$
- **(D)** Temperature at $C$ is $\frac{T_0}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Work done by the gas in process $A B$ is $p_0 V_0 \ln 4$**

**Detailed Solution:**

$$
\begin{aligned}
& T_A=T_B \quad \therefore U_A=U_B \\
& W_{A B}=(1)(R) T_0 \ln \left(\frac{V_f}{V_i}\right) \\
& =R T_0 \ln \left(\frac{4 V_0}{V_0}\right) \\
& =p_0 V_0 \ln (4)
\end{aligned}
$$
Information regarding $p$ and $T$ at $C$ can not be obtained from the given graph. Unless it is mentioned that line $B C$ passes through origin or not.
Hence, the correct options are (a) and (b).

</details>

---

### Q24. JEE Advanced 2009 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Two soap bubbles $A$ and $B$ are kept in a closed chamber where the air is maintained at pressure $8 \mathrm{Nm}^{-2}$. The radii of bubbles $A$ and $B$ are $2 \mathrm{~cm}$, respectively. Surface tension of the soap-water used to make bubbles is $0.04$ $\mathrm{Nm}^{-1}$. Find the ratio $\frac{n_B}{n_A}$, where $n_A$ and $n_B$ are the number of moles of air in bubbles $A$ and $B$, respectively. [Neglect the effect of gravity]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Although not given in the question but we will have to assume that temperatures of $A$ and $B$ are same.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/R_nXQKXsgRU_Yf6edoVvo3Mol9x3Nj68X29tjGHUZ_Q.original.fullsize.png">


$$
\begin{aligned}
& \frac{n_B}{n_A}=\frac{p_B V_B / R T}{p_A V_A / R T}=\frac{p_B V_B}{p_A V_A} \\
&= \frac{p+4 s / r_A \times 4 / 3 \pi\left(r_A\right)^3}{\left(p+4 s / r_B\right) \times 4 / 3 \pi\left(r_B\right)^3} \\
&(s=\text { surface tension) }
\end{aligned}
$$

</details>

---

### Q25. JEE Advanced 2009 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

The figure shows the $p-V$ plot of an ideal gas taken through a cycle $A B C D A$. The part $A B C$ is a semi-circle and $C D A$ is half of an ellipse. Then,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8ZOM6QJfZljyoG_Z3IXKXCQGTFnt5TyhRv-MeUNK0Pw.original.fullsize.png">

**Options:**

- **(A)** the process during the path $A \rightarrow B$ is isothermal
- **(B)** heat flows out of the gas during the path $B \rightarrow C \rightarrow D$
- **(C)** work done during the path $A \rightarrow B \rightarrow C$ is zero
- **(D)** positive work is done by the gas in the cycle $A B C D A$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) positive work is done by the gas in the cycle $A B C D A$.**

**Detailed Solution:**

(A) $p-V$ graph is not rectangular hyperbola. Therefore, process $A-B$ is not isothermal.
(B) In process $B C D$, product of $p V$ (therefore temperature and intemal energy) is decreasing. Further, volume is decreasing. Hence, work done is also negative. Hence, $Q$ will be negative or heat will flow out of the gas.
(C) $W_{A B C}=$ positive
(D) For clockwise cycle on $p-V$ diagram with $P$ on $y$-axis, net work done is positive.

</details>

---

### Q26. JEE Advanced 2008 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

An ideal gas is expanding such that $p T^2=$ constant. The coefficient of volume expansion of the gas is

**Options:**

- **(A)** $\frac{1}{T}$
- **(B)** $\frac{2}{T}$
- **(C)** $\frac{3}{T}$
- **(D)** $\frac{4}{T}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{T}$**

**Detailed Solution:**

$p T^2=$ constant
$\begin{array}{ll}\therefore \quad & \left(\frac{n R T}{V}\right) T^2=\text { constant } \\ \text { or } \quad T^3 V^{-1}=\text { constant }\end{array}$
Differentiating the equation, we get
$$
\frac{3 T^2}{V} \cdot d T-\frac{T^3}{V^2} \cdot d V=0
$$
or
$$
3 \cdot d T=\frac{T}{V} \cdot d V
$$
From the equation, $d V=V \gamma \cdot d T$
$\gamma$ = coefficient of volume expansion of gas $=\frac{d V}{V \cdot d T}$
From Eq. (i) $\gamma=\frac{d V}{V \cdot d T}=\frac{3}{T}$
$\therefore$ correct answer is (c).

</details>

---

