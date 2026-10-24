# JEE Advanced Physics - Alternating Current

## Topic 2: AC Circuits

**Total Questions:** 22

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider a circuit consisting of a capacitor of capacitance $C$ and a coil with $N$ turns per unit length, cross sectional area $S$ and length $d$, where $d^2 \gg S$. There is another coil of length $d/2$, cross sectional area $S/2$ and $2N$ turns per unit length completely inside the larger coil, as shown in the figure. The ends of this smaller coil are connected with each other by an insulated conducting wire. The self-inductance of the larger coil is $L$. Neglecting edge effects and all the Ohmic resistances, the resonant frequency of the circuit is:

<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q18_d1.png" />

**Options:**

- **(A)** $\dfrac{4}{\sqrt{15\, LC}}$
- **(B)** $\dfrac{6}{\sqrt{5\, LC}}$
- **(C)** $\dfrac{2}{\sqrt{3\, LC}}$
- **(D)** $\sqrt{\dfrac{2}{3\, LC}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{\sqrt{3\, LC}}$**

**Detailed Solution:**

Let the larger coil be coil 1 and the smaller coil be coil 2.

The self-inductance of the larger coil is given by:
$L_1 = \mu_0 n_1^2 A_1 l_1 = \mu_0 N^2 S d = L$

The self-inductance of the smaller coil is:
$L_2 = \mu_0 n_2^2 A_2 l_2 = \mu_0 (2N)^2 \left(\dfrac{S}{2}\right) \left(\dfrac{d}{2}\right) = \mu_0 (4N^2) \left(\dfrac{Sd}{4}\right) = \mu_0 N^2 S d = L$

The mutual inductance between the two coils is:
$M = \mu_0 n_1 n_2 A_{\text{common}} l_{\text{common}}$
Since the smaller coil is completely inside the larger coil, the common area is $S/2$ and the common length is $d/2$.
$M = \mu_0 (N) (2N) \left(\dfrac{S}{2}\right) \left(\dfrac{d}{2}\right) = \dfrac{1}{2} \mu_0 N^2 S d = \dfrac{L}{2}$

Let $i_1$ be the current in the larger coil and $i_2$ be the current in the smaller coil. The voltage across the larger coil is:
$V = L_1 \dfrac{di_1}{dt} + M \dfrac{di_2}{dt}$

Since the smaller coil is short-circuited, the net voltage across it is zero:
$0 = L_2 \dfrac{di_2}{dt} + M \dfrac{di_1}{dt} \Rightarrow \dfrac{di_2}{dt} = -\dfrac{M}{L_2} \dfrac{di_1}{dt}$

Substituting this into the first equation, we get the effective inductance $L_{\text{eq}}$:
$V = L_1 \dfrac{di_1}{dt} - \dfrac{M^2}{L_2} \dfrac{di_1}{dt} = \left( L_1 - \dfrac{M^2}{L_2} \right) \dfrac{di_1}{dt}$
$L_{\text{eq}} = L_1 - \dfrac{M^2}{L_2} = L - \dfrac{(L/2)^2}{L} = L - \dfrac{L}{4} = \dfrac{3L}{4}$

The resonant angular frequency of the circuit is:
$\omega = \dfrac{1}{\sqrt{L_{\text{eq}} C}} = \dfrac{1}{\sqrt{\dfrac{3L}{4} C}} = \dfrac{2}{\sqrt{3LC}}$

Answer: $\dfrac{2}{\sqrt{3\, LC}}$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

A circuit with an electrical load having impedance $Z$ is connected with an AC source as shown in the diagram. The source voltage varies in time as $V(t)=300 \sin (400 t) \mathrm{V}$, where $t$ is time in s. List-I shows various options for the load. The possible currents $i(t)$ in the circuit as a function of time are given in List-II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/HDUZdrDxzk0suEBf1flYa78p7ZDAnnvgDPsFfWde2nc.original.fullsize.png">
Choose the option that describes the correct match between the entries in List-I to those in List-II. <table> <thead> <tr> <th> </th> <th>List-I </th> <th> </th> <th>List-II </th> </tr> </thead> <tbody> <tr> <td>$(P)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/I83fmicNtdnD2Hb5phAqSDl3gMW732c8271HLfmgXWw.original.fullsize.png">
 </td> <td>$(1)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Tc0Fei75EHkgdj1XojIFmbGhwG88Z3rNuKe4y-0jFyM.original.fullsize.png">
 </td> </tr> <tr> <td>$(Q)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/arVVeux1NEMwmJDsErmRmD-0sxVY8mZATIpZoXJKnPo.original.fullsize.png">
 </td> <td>$(2)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/2Scs4ImbkzkTYShb-rXtQJIwVO2plxuvp-NhbsbF9A4.original.fullsize.png">
 </td> </tr> <tr> <td>$(R)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/kr9j3P2pQ0a19PkvwzjgwUullMa1jyFgw5NgNa_0NjY.original.fullsize.png">
 </td> <td>$(3)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/M-w-CMXo8zBeO_ElCMjz5TGEwbMd_S_UqF3JcmU2Thc.original.fullsize.png">
 </td> </tr> <tr> <td>$(S)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/AvDITlICDu25QzCbM8St5RdIMVdHvKzpBeo9TGSI_08.original.fullsize.png">
 </td> <td>$(4)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/THrBOzfn5U0LUuIujrH3RFg_0r4zsOLmsp41D7g_3No.original.fullsize.png">
 </td> </tr> <tr> <td> </td> <td> </td> <td>$(5)$ </td> <td><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/23x2obyz27dVb3-DmHeg8pVo_1nQdwu70I8B-PbS6qA.original.fullsize.png">
 </td> </tr> </tbody> </table>

**Options:**

- **(A)** $\mathrm{P} \rightarrow 3, \mathrm{Q} \rightarrow 5, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 1$
- **(B)** $\mathrm{P} \rightarrow 1, \mathrm{Q} \rightarrow 5, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 3$
- **(C)** $\mathrm{P} \rightarrow 3, \mathrm{Q} \rightarrow 4, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 1$
- **(D)** $\mathrm{P} \rightarrow 1, \mathrm{Q} \rightarrow 4, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{P} \rightarrow 3, \mathrm{Q} \rightarrow 5, \mathrm{R} \rightarrow 2, \mathrm{~S} \rightarrow 1$**

**Detailed Solution:**

For P
$i=\frac{V}{R}=10 \sin 400 t \Rightarrow(3)$
For Q
$\begin{aligned} & X_L=\omega L=400 \times 100 \times 10^{-3}=40 \Omega \\ & \therefore Z=50 \Omega \\ & \left.\therefore i=\frac{300}{50} \sin \left(400 t-53^{\circ}\right) \text { [current will lag by } \tan ^{-1} \frac{X_L}{R}\right] \Rightarrow(5)\end{aligned}$
For R
$\begin{aligned} & \mathrm{X}_{\mathrm{C}}=\frac{10^6}{400 \times 50} \Omega=50 \Omega \text { and } \mathrm{X}_{\mathrm{L}}=400 \times 25 \times 10^{-3}=10 \Omega \\ & \therefore \mathrm{Z}=50 \Omega \\ & \therefore \mathrm{i}=\frac{300}{50} \sin \left(400 \mathrm{t}+53^{\circ}\right) \quad\left[\text { Current will lead by } \tan ^{-1} \frac{\mathrm{X}_{\mathrm{C}}-\mathrm{X}_{\mathrm{L}}}{\mathrm{R}}\right] \Rightarrow(2)\end{aligned}$
For $S$
$\therefore \mathrm{i}=\frac{300}{60} \sin (400 \mathrm{t}) \quad \mathrm{X}_{\mathrm{L}}=\mathrm{X}_{\mathrm{C}} \Rightarrow$ Resonance $\Rightarrow(1)$

</details>

---

### Q3. JEE Advanced 2024 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

The circuit shown in the figure contains an inductor $L$, a capacitor $C_0$, a resistor $R_0$ and an ideal battery. The circuit also contains two keys $\mathrm{K}_1$ and $\mathrm{K}_2$. Initially, both the keys are open and there is no charge on the capacitor. At an instant, key $K_1$ is closed and immediately after this the current in $R_0$ is found to be $I_1$. After a long time, the current attains a steady state value $I_2$. Thereafter, $\mathrm{K}_2$ is closed and simultaneously $\mathrm{K}_1$ is opened and the voltage across $C_0$ oscillates with amplitude $V_0$ and angular frequency $\omega_0$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/gtCywhCB2kjRD3T_mrEaL97CXA1OOKKNkrEgYLTfF7I.original.fullsize.png">
Match the quantities mentioned in List-I with their values in List-II and choose the correct option.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YN0t29dyBmgcnZUvZRB5083-KtYXTXnB1ZVkG2E2ik8.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{P} \rightarrow 1 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 2 ; \mathrm{S} \rightarrow 5$
- **(B)** $\mathrm{P} \rightarrow 1 ; \mathrm{Q} \rightarrow 2 ; \mathrm{R} \rightarrow 3 ; \mathrm{S} \rightarrow 5$
- **(C)** $\mathrm{P} \rightarrow 1 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 2 ; \mathrm{S} \rightarrow 4$
- **(D)** $\mathrm{P} \rightarrow 2 ; \mathrm{Q} \rightarrow 5 ; \mathrm{R} \rightarrow 3 ; \mathrm{S} \rightarrow 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{P} \rightarrow 1 ; \mathrm{Q} \rightarrow 3 ; \mathrm{R} \rightarrow 2 ; \mathrm{S} \rightarrow 5$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/XHjQssUUXUlsMCQagX0R6gIUIU-2xPpQkXmO2H6DRgc.original.fullsize.png">
(P) When $K_1$ is closed current in $R_0$ is $I_1$ At $\mathrm{t}=0$; circuit will be
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YZE2pTaLg3nl-u4oITH6ixf6BdffN2KsofdFkqYlZxo.original.fullsize.png">
$\begin{aligned} & \mathrm{I}_1=0 \\ & \mathrm{P} \rightarrow(1)\end{aligned}$
(Q) After long time inductor behave as a wire so $\mathrm{I}_2$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8SIuHNdha2KuCuSaP7q57Jy_UAsvr89eybPYkeRhgTc.original.fullsize.png">
$\begin{aligned} & \mathrm{I}_2=\frac{20}{5}=4 \mathrm{~A} \\ & \mathrm{Q} \rightarrow(3)\end{aligned}$
(R) When $\mathrm{K}_2$ is closed and $\mathrm{K}_1$ open
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1ohb7ytp-oJ5PQ4BEr_m6m8D71B6cLlJ-lGa775AtAw.original.fullsize.png">
$\begin{aligned} & \omega_0=\frac{1}{\sqrt{\mathrm{LC}}} \\ & \omega_0=\frac{1}{\sqrt{25 \times 10^{-3} \times 10 \times 10^{-6}}}=\frac{1}{5 \times 10^{-4}} \\ & \omega_0=2 \times 10^3 \mathrm{rad} / \mathrm{s} \\ & \omega_0=2 \text { kilo-radian } / \mathrm{s} \\ & \mathrm{R} \rightarrow(2)\end{aligned}$
(S) Now $\mathrm{K}_2$ is closed and $\mathrm{K}_1$ open
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/kKePUTI_G2IYk3uB6WOgj5NzIFndmEnehqGmxMGweTw.original.fullsize.png">
$\begin{aligned} & \frac{1}{2} \mathrm{LI}_2^2=\frac{1}{2} \mathrm{CV}_0^2 \\ & 25 \times 10^{-3} \times(4)^2=10 \times 10^{-6} \times \mathrm{V}_0^2 \\ & \mathrm{~V}_0^2=2500 \times 16 \\ & \mathrm{~V}_0=50 \times 4=200 \mathrm{~V} \\ & \mathrm{~S} \rightarrow(5)\end{aligned}$

</details>

---

### Q4. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A series LCR circuit is connected to a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#160;</mo><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>)</mo></math> Volt source. The resonant angular frequency of the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>5</mn></msup><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></math> and current amplitude at resonance is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math>. When the angular frequency of the source is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#969;</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></math>, the current amplitude in the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><msub><mi>I</mi><mn>0</mn></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi>mH</mi></math>, match each entry in List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> with an appropriate value from List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> and choose the correct option.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td style="text-align: center;">List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math></td>			<td style="text-align: center;"> </td>			<td style="text-align: center;">List-<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>mA</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn><mo>.</mo><mn>4</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Q</mi></math></td>			<td>The quality factor of the circuit</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math></td>			<td>The bandwidth of the circuit in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math></td>			<td>The peak power dissipated at resonance in Watt</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2250</mn></math></td>		</tr>		<tr>			<td> </td>			<td> </td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math></td>		</tr>	</tbody></table>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>2</mn></math>**

**Detailed Solution:**

<blockquote><p>Resonant angular frequency is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mi>L</mi><mi>C</mi></msqrt></mfrac><mo>=</mo><msup><mn>10</mn><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msqrt><mfenced><mrow><mn>50</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mi>C</mi></msqrt></mfrac><mo>=</mo><msup><mn>10</mn><mn>5</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">F</mi></math></p><p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>45</mn><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi></mrow></mfenced></math>. Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub><mo>=</mo><mn>45</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><msub><mi>V</mi><mn>0</mn></msub><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>45</mn><mi>R</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Inductive reactance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>L</mi></msub><mo>=</mo><mi>&#969;</mi><mi>L</mi><mo>=</mo><mfenced><mrow><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>50</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>4000</mn><mo>&#160;</mo><mi>&#937;</mi></math>.</p><p>and capacitive reactance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>C</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mi>&#969;</mi><mi>C</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>8</mn><mo>&#215;</mo><msup><mn>10</mn><mn>4</mn></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>9</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>6250</mn><mo>&#160;</mo><mi>&#937;</mi></math>.</p><p>For new current amplitude, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>05</mn><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>45</mn><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><msub><mi>X</mi><mi>L</mi></msub><mo>-</mo><msub><mi>X</mi><mi>C</mi></msub></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>05</mn><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>45</mn><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6250</mn><mo>-</mo><mn>4000</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>05</mn><mo>&#215;</mo><mfrac><mn>45</mn><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>45</mn><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6250</mn><mo>-</mo><mn>4000</mn></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>6250</mn><mo>-</mo><mn>4000</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><msup><mi>R</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>0</mn><mo>.</mo><mn>05</mn></mrow></mfenced><mn>2</mn></msup></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>2250</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>400</mn><msup><mi>R</mi><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><mn>2250</mn><msqrt><mn>399</mn></msqrt></mfrac><mo>=</mo><mn>112</mn><mo>.</mo><mn>67</mn><mo>&#160;</mo><mi>&#937;</mi></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><msub><mi>L</mi><mn>0</mn></msub></msub><mo>=</mo><msub><mi>X</mi><msub><mi>C</mi><mn>0</mn></msub></msub></math> are at resonant frequencies</p><p>On solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>0</mn></msub><mo>=</mo><mfrac><mn>45</mn><mi>R</mi></mfrac><mo>&#8771;</mo><mn>400</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>Quality factor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><msub><mi>X</mi><mi>L</mi></msub><mi>R</mi></mfrac><mo>&#8771;</mo><mn>44</mn><mo>.</mo><mn>44</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mfrac><msub><mi>&#969;</mi><mn>0</mn></msub><mrow><mo>&#8710;</mo><mi>&#969;</mi></mrow></mfrac><mo>&#8658;</mo><mo>&#8710;</mo><mi>&#969;</mi><mo>&#8771;</mo><mn>2250</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>.</p><p>Peak power <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>45</mn><mo>&#215;</mo><mfrac><mn>400</mn><mn>1000</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">W</mi><mo>=</mo><mn>18</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>&#8594;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>&#8594;</mo><mn>2</mn></math>.</p></blockquote>

</details>

---

### Q5. JEE Advanced 2023 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>In a circuit shown in the figure, the capacitor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is initially uncharged and the key <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math> is open. In this condition, a current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> flows through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>&#937;</mi></math> resistor. The key is closed at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msub><mi>t</mi><mn>0</mn></msub></math>. Which of the following statement(s) is(are) correct?</p><p>[Given : <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mo>&#8211;</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>36</mn></math>]</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ab0a548c-0db2-4253-b388-be88dde718f8.png" style="width: 400px; height: 379px;" /></p>

**Options:**

- **(A)** The value of the resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>&#937;</mi></math>
- **(B)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#60;</mo><msub><mi>t</mi><mn>0</mn></msub></math>, the value of current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">A</mi></math>
- **(C)** At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msub><mi>t</mi><mn>0</mn></msub><mo>+</mo><mn>7</mn><mo>.</mo><mn>2</mn><mi>&#956;</mi><mi mathvariant="normal">s</mi></math>, the current in the capacitor is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mi mathvariant="normal">A</mi></math>
- **(D)** For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></math>, the charge on the capacitor is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>&#8594;</mo><mo>&#8734;</mo></math>, the charge on the capacitor is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/95ff5d1a-e107-4cf1-a985-291f5f000c53.png" style="width: 300px; height: 309px;" /></p><p>From second branch, we can see the potential drop across the branch is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>&#215;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p>Now for the first branch, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>-</mo><mi>I</mi><mi>R</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> and from third branch, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Now from Kirchoff&#39;s junction rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p><p>Now, from equation(1), we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>-</mo><mn>3</mn><mi>R</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>3</mn><mi>&#937;</mi></math></p><p>All three branches are in parallel, therefore we can write equivalent resistance as:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>R</mi><mi>eq</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi>&#937;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi>&#937;</mi></math></p><p>As all branches are in parallel with the capacitor branch, potential drop across all three branches will be the same. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mi>eq</mi></msub><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/09e2376b-8e36-476a-a72e-1a04966c0430.png" style="width: 300px; height: 204px;" /></p><p> </p><p>Now, current variation in the circuit due to charging will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>+</mo><mn>3</mn></mstyle></mfenced></mfrac><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mfenced><mrow><mi>t</mi><mo>-</mo><msub><mi>t</mi><mn>0</mn></msub></mrow></mfenced></mrow><mrow><mi>C</mi><mi>R</mi></mrow></mfrac></msup></math></p><p>At, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msub><mi>t</mi><mn>0</mn></msub><mo>+</mo><mn>7</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi>&#956;s</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn></mrow><mn>18</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mfenced><mrow><mn>7</mn><mo>.</mo><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfenced><mrow><mfenced><mrow><mn>2</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mo>.</mo><mn>6</mn></mrow></mfenced></mrow></mfrac></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>30</mn><mn>18</mn></mfrac><mo>&#215;</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>30</mn><mn>18</mn></mfrac><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>At steady state, voltage across capacitor <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>12</mn><mi>&#956;</mi><mi mathvariant="normal">C</mi></math>.</p>

</details>

---

### Q6. JEE Advanced 2022 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Consider an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LC</mi></math> circuit, with inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">H</mi></math> and capacitance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">F</mi></math>, kept on a plane. The area of the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></math>. It is placed in a constant magnetic field of strength <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>0</mn></msub></math> which is perpendicular to the plane of the circuit. At time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>, the magnetic field strength starts increasing linearly as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msub><mi>B</mi><mn>0</mn></msub><mo>+</mo><mi>&#946;</mi><mi mathvariant="normal">t</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>04</mn><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math>. The maximum magnitude of the current in the circuit is____<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Emf induced in the circuit is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>E</mi></mfenced><mo>=</mo><mfenced close="|" open="|"><mfrac><mrow><mi>d</mi><mi>&#981;</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><msub><mi>B</mi><mn>0</mn></msub><mo>+</mo><mi>&#946;</mi><mi>t</mi></mrow></mfenced><mi>A</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#946;</mi><mo>&#215;</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>04</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>So the circuit can be rearranged as</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cdfabb06-6d55-4bef-a38a-c61bb4952fbc-image.png" style="width: 220px; height: 174px;" /></p><p>Using Kirchhoff&#39;s law we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>+</mo><mfrac><mi>q</mi><mi>C</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mfrac><mrow><mi>d</mi><mi>i</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>E</mi><mo>-</mo><mfrac><mi>q</mi><mi>C</mi></mfrac></math></p><p>For maximum current, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>d</mo><mi>i</mi></mrow><mrow><mo>d</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math>, </p><p>Or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mi>C</mi><mi>E</mi></math></p></blockquote><blockquote><p>Using work energy theorem,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><msup><mi>i</mi><mn>2</mn></msup><mo>+</mo><mfrac><msup><mi>q</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>C</mi></mrow></mfrac></math></p><p>At <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi>max</mi></msub></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>E</mi><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><msubsup><mi>i</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow><mn>2</mn></msubsup><mo>+</mo><mfrac><mrow><msup><mi>E</mi><mn>2</mn></msup><msup><mi>C</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>C</mi></mrow></mfrac></math></p><p>Or, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi>max</mi></msub><mo>=</mo><msqrt><mfrac><mi>C</mi><mi>L</mi></mfrac></msqrt><mi>E</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi>max</mi></msub><mo>=</mo><msqrt><mfrac><mrow><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>04</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></msqrt></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>mA</mi></math></p></blockquote>

</details>

---

### Q7. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

In a circuit, a metal filament lamp is connected in series with a capacitor of capacitance $\mathrm{C} \mu F$ across a $200 \mathrm{~V}, 50 \mathrm{~Hz}$ supply. The power consumed by the lamp is $500 \mathrm{~W}$ while the voltage drop across it is $100 \mathrm{~V}$. Assume that there is no inductive load in the circuit. Take $r m s$ values of the voltages. The magnitude of the phaseangle (in degrees) between the current and the supply voltage is $\varphi$. Assume, $\pi \sqrt{3} \approx 5$.
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>R</mi></msub><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi>Hz</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>=</mo><mn>200</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a9534dee-8bf1-4528-9e41-ca0b7e175386-image.png" style="width: 250px; height: 172px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mi>R</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mi>P</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><msup><mfenced><mn>100</mn></mfenced><mn>2</mn></msup><mn>500</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>R</mi><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Now current in the circuit,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msub><mi>i</mi><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>voltage</mi><mo>&#160;</mo><mi>across</mi><mo>&#160;</mo><mi>resistor</mi></mrow><mi>resistance</mi></mfrac><mspace linebreak="newline"/><mi>i</mi><mo>=</mo><mfrac><mn>100</mn><mn>20</mn></mfrac><mspace linebreak="newline"/><mi>i</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Phasor diagram of the given circuit for voltage,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/74da4edb-8ed0-4431-8111-49c799cec0a8-image.png" style="width: 274px; height: 174px;" /> </p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><msup><msub><mi>V</mi><mi>C</mi></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mn>200</mn><mn>2</mn></msup><mo>=</mo><msup><msub><mi>V</mi><mi>C</mi></msub><mn>2</mn></msup><mo>+</mo><msup><mn>100</mn><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>V</mi><mi>C</mi></msub><mo>=</mo><mn>100</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>C</mi></msub><mo>=</mo><mn>100</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mi>I</mi><msub><mi>X</mi><mi>C</mi></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>X</mi><mi>C</mi></msub><mo>=</mo><mfrac><mrow><mn>100</mn><msqrt><mn>3</mn></msqrt></mrow><mn>5</mn></mfrac><mo>=</mo><mn>20</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>C</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>f</mi></mrow></mfenced><mi>C</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>20</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>&#215;</mo><mn>100</mn></mrow></mfenced><mi>C</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi>&#956;F</mi></math></p><p>From the phasor diagram,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mi>&#981;</mi></mfenced><mo>=</mo><mfrac><msub><mi>X</mi><mi>C</mi></msub><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mn>20</mn><msqrt><mn>3</mn></msqrt></mrow><mn>20</mn></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#981;</mi><mo>=</mo><mn>60</mn><mo>&#176;</mo></math></p>

</details>

---

### Q8. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

In a circuit, a metal filament lamp is connected in series with a capacitor of capacitance $\mathrm{C} \mu F$ across a $200 \mathrm{~V}, 50 \mathrm{~Hz}$ supply. The power consumed by the lamp is $500 \mathrm{~W}$ while the voltage drop across it is $100 \mathrm{~V}$. Assume that there is no inductive load in the circuit. Take $r m s$ values of the voltages. The magnitude of the phaseangle (in degrees) between the current and the supply voltage is $\varphi$. Assume, $\pi \sqrt{3} \approx 5$.
The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is ____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>R</mi></msub><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>=</mo><mn>50</mn><mo>&#160;</mo><mi>Hz</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>=</mo><mn>200</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/a9534dee-8bf1-4528-9e41-ca0b7e175386-image.png" style="width: 250px; height: 172px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mi>R</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mi>P</mi></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><msup><mfenced><mn>100</mn></mfenced><mn>2</mn></msup><mn>500</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>R</mi><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Now current in the circuit,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><msub><mi>i</mi><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>voltage</mi><mo>&#160;</mo><mi>across</mi><mo>&#160;</mo><mi>resistor</mi></mrow><mi>resistance</mi></mfrac><mspace linebreak="newline"/><mi>i</mi><mo>=</mo><mfrac><mn>100</mn><mn>20</mn></mfrac><mspace linebreak="newline"/><mi>i</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Phasor diagram of the given circuit for voltage,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/74da4edb-8ed0-4431-8111-49c799cec0a8-image.png" style="width: 274px; height: 174px;" /> </p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>V</mi><mn>2</mn></msup><mo>=</mo><msup><msub><mi>V</mi><mi>C</mi></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>V</mi><mi>R</mi></msub><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msup><mn>200</mn><mn>2</mn></msup><mo>=</mo><msup><msub><mi>V</mi><mi>C</mi></msub><mn>2</mn></msup><mo>+</mo><msup><mn>100</mn><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>V</mi><mi>C</mi></msub><mo>=</mo><mn>100</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Now, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>C</mi></msub><mo>=</mo><mn>100</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mi>I</mi><msub><mi>X</mi><mi>C</mi></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>X</mi><mi>C</mi></msub><mo>=</mo><mfrac><mrow><mn>100</mn><msqrt><mn>3</mn></msqrt></mrow><mn>5</mn></mfrac><mo>=</mo><mn>20</mn><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>C</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mi>f</mi></mrow></mfenced><mi>C</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mn>20</mn><msqrt><mn>3</mn></msqrt><mo>=</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>&#960;</mi><mo>&#215;</mo><mn>100</mn></mrow></mfenced><mi>C</mi></mrow></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>C</mi><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi>&#956;F</mi></math></p><p>From the phasor diagram,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mi>&#981;</mi></mfenced><mo>=</mo><mfrac><msub><mi>X</mi><mi>C</mi></msub><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mn>20</mn><msqrt><mn>3</mn></msqrt></mrow><mn>20</mn></mfrac><mo>=</mo><msqrt><mn>3</mn></msqrt><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>&#981;</mi><mo>=</mo><mn>60</mn><mo>&#176;</mo></math></p>

</details>

---

### Q9. JEE Advanced 2019 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>In the circuit shown, initially there is no charge on capacitors and keys <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>2</mn></mrow></msub></math> are open. The values of the capacitors are <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>10</mn><mtext> </mtext><mi mathvariant="normal">μ</mi><mi mathvariant="normal">F</mi><mo>,</mo><mtext> </mtext><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>30</mn><mtext> </mtext><mi mathvariant="normal">μ</mi><mi mathvariant="normal">F</mi></math> and <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mtext> </mtext><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>80</mn><mtext> </mtext><mi mathvariant="normal">μ</mi><mi mathvariant="normal">F</mi><mo>.</mo></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/uiykwvzukdqxzdodvjfobioubfkbhodselzzfkrfpaqkrtdibg.png"/>
Which of the statement(s) is/are correct?</p>

**Options:**

- **(A)** If key  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is kept closed for long time such that capacitors are fully charged, the voltage difference between points  <math><mi mathvariant="normal">P</mi></math>  and  <math><mi mathvariant="normal">Q</mi></math>  will be  <math><mn>10</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">V</mi><mo>.</mo></math>
- **(B)** The keys  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is kept closed for long time such that capacitors are fully charged. Now key  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  is closed, at this time, the instantaneous current across  <math><mn>30</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">Ω</mi></math>  resistor (between points  <math><mi mathvariant="normal">P</mi></math>  and  <math><mi mathvariant="normal">Q</mi></math> ) will be  <math><mn>0.2</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">A</mi></math>  (round off to  <math><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math>  decimal place).
- **(C)** At time  <math><mi mathvariant="normal">t</mi><mo>=</mo><mn>0</mn><mo>,</mo></math>  the key  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is closed, the instantaneous current in the closed circuit will be  <math><mn>25</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">A</mi><mo>.</mo></math>
- **(D)** If key  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is kept closed for long time such that capacitors are fully charged, the voltage across the capacitors  <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  will be  <math><mn>4</mn><mi mathvariant="normal">V</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) If key  <math><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is kept closed for long time such that capacitors are fully charged, the voltage across the capacitors  <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  will be  <math><mn>4</mn><mi mathvariant="normal">V</mi><mo>.</mo></math>**

**Detailed Solution:**

<p>For option  <math><mo>(</mo><mi mathvariant="normal">C</mi><mo>)</mo></math> , refer circuit diagram below
 <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/fyklfizxiaegqlppnkxyrqchuvtqagqqjtnyoqxouwxrhxdlkr.png"/> 
Just after closing of switch charge on all the capacitors  <math><mfenced separators="|"><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext> </mtext><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mtext> </mtext><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mtext> </mtext><msub><mrow><mi>C</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math> 
 <math><mo>∴</mo></math>  Replace all capacitors with wire, then circuit will get reduced as shown below.
 <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/exrypamauszhrcnwmuplndfezwbiawxfxprfoqwacviwhjccll.png"/> 
 <math><mi>i</mi><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>70</mn><mo>+</mo><mn>100</mn><mo>+</mo><mn>30</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>200</mn></mrow></mfrac><mo>=</mo><mn>25</mn><mtext> </mtext><mi>m</mi><mi>A</mi><mo>⇒</mo><mo>(</mo><mi mathvariant="normal">C</mi><mo>)</mo></math>  is correct
Now  <math><msub><mrow><mi>S</mi></mrow><mrow><mn>1</mn></mrow></msub></math>  is kept closed for long time circuit is in steady state
 <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/qhwxogwfbkulyfnapmvnzbgnfnuoabuycckruicsjinfidvolo.png"/> 
 <math><mo>⇒</mo></math>  Apply KVL in loop, start from battery
 <math><mo>+</mo><mn>5</mn><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>80</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>80</mn></mrow></mfrac><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mfrac><mrow><mn>10.2</mn></mrow><mrow><mn>80</mn></mrow></mfrac><mo>=</mo><mn>5</mn></math> 
 <math><mo>⇒</mo><mn>2</mn><mo>=</mo><mn>40</mn><mtext> </mtext><mi>μ</mi><mi>C</mi></math> 
 <math><mo>⇒</mo></math>  Potential difference across  <math><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><mi>Δ</mi><msub><mrow><mi>V</mi></mrow><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mtext> </mtext><mi mathvariant="normal">v</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">t</mi></math> 
 <math><mo>⇒</mo><mo>(</mo><mi mathvariant="normal">D</mi><mo>)</mo></math>  is correct.
For option  <math><mo>(</mo><mi mathvariant="normal">B</mi><mo>)</mo><mo>⇒</mo></math>  Now just after closing of  <math><msub><mrow><mi>S</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  charge on each capacitor remain same,
Refer circuit below -
 <img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/pcpbogoxnqcgwwtqonhjziesloeabuzsqhpjbqpkkmdtgdcfsv.png"/> 
KVL in left loop, starting from battery of  <math><mn>10</mn></math>  volts,
 <math><mn>10</mn><mo>-</mo><mn>30</mn><mi>x</mi><mo>-</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>-</mo><mn>70</mn><mi>y</mi><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mn>30</mn><mi>x</mi><mo>+</mo><mn>70</mn><mi>y</mi><mo>=</mo><mn>6</mn></math>  ...(i)
Now, apply KVL in right loop starting from  <math><mn>80</mn><mtext> </mtext><mi>μ</mi><mi>F</mi></math>  capacitor
 <math><mo>⇒</mo><mo>-</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>80</mn></mrow></mfrac><mo>+</mo><mn>5</mn><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mn>30</mn><mo>-</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>80</mn></mrow></mfrac><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>×</mo><mn>100</mn><mo>-</mo><mn>10</mn><mo>+</mo><mi>x</mi><mo>×</mo><mn>30</mn><mo>=</mo><mn>0</mn></math> 
 <math><mo>⇒</mo><mn>160</mn><mi>x</mi><mo>-</mo><mn>130</mn><mi>y</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>  ...(ii)
Now, solving equation (i) and (ii) we get,
 <math><mi>y</mi><mo>=</mo><mfrac><mrow><mn>96</mn></mrow><mrow><mn>1510</mn></mrow></mfrac></math> 
and  <math><mi>x</mi><mo>=</mo><mn>0.05</mn><mtext> </mtext><mi>a</mi><mi>m</mi><mi>p</mi><mo>.</mo></math> <math><mo>⇒</mo><mo>(</mo><mi>B</mi><mo>)</mo></math>  is incorrect.</p>

</details>

---

### Q10. JEE Advanced 2017 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>In the circuit shown, <math><mi>L</mi><mtext> </mtext><mo>=</mo><mtext> </mtext><mn>1</mn><mtext> </mtext><mtext>μ</mtext><mi>H</mi><mo>,</mo><mtext> </mtext><mi>C</mi><mo>=</mo><mn>1</mn><mtext> </mtext><mtext>μ</mtext><mi>F</mi><mtext> </mtext><mi>a</mi><mi>n</mi><mi>d</mi><mtext> </mtext><mi>R</mi><mo>=</mo><mn>1</mn><mtext> </mtext><mi>k</mi><mi mathvariant="normal">Ω</mi><mo>.</mo><mtext> </mtext></math> They are connected in series with an a.c. source <math><mi>V</mi><mo>=</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>0</mn></mrow></msub><mtext> </mtext><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>⁡</mo><mrow><mtext>ω</mtext><mi>t</mi></mrow></mrow></math> as shown. Which of the following options is/are correct?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/skflzdeounqrjeglmncmnzywmskplktgavkdxirnucfvacbvku.jpeg"/></p>

**Options:**

- **(A)** At  <math><mi>ω</mi><mo>≫</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>6</mn></mrow></msup><mi> </mi><mi>r</mi><mi>a</mi><mi>d</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi></mrow></mrow></math> the circuit behaves as a capacitor
- **(B)** The frequency at which the current will be in phase with the voltage is independent of <math><mi>R</mi></math>
- **(C)** The current will be in phase with the voltage if  <math><mi>ω</mi><mo>=</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>4</mn></mrow></msup><mi> </mi><mi>r</mi><mi>a</mi><mi>d</mi><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mo>⁡</mo><mrow><mi> </mi></mrow></mrow></math>
- **(D)** At <math><mi>&omega;</mi><mo>~</mo><mn>0</mn><mi> </mi></math> the current flowing through the circuit becomes nearly zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) At <math><mi>&omega;</mi><mo>~</mo><mn>0</mn><mi> </mi></math> the current flowing through the circuit becomes nearly zero**

**Detailed Solution:**

<p>The current will be in phase with voltage when phase angle is zero, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>tan</mi><mo>&#8289;</mo><mtext>&#981;</mtext><mo>=</mo><mfrac><mrow><mtext>&#969;</mtext><mi>L</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mtext>&#969;</mtext><mi>C</mi></mrow></mfrac></mrow><mi>R</mi></mfrac><mo>=</mo><mn>0</mn></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#969;</mtext><mo>,</mo><mo>&#160;</mo><mi>L</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>R</mi></math> are the angular frequency, inductance, capacitance and resistance respectively.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>&#969;</mtext><mo>=</mo><msub><mtext>&#969;</mtext><mn>0</mn></msub><mo>=</mo><mfrac><mn>1</mn><msqrt><mi>L</mi><mi>C</mi></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mtext>&#969;</mtext><mtext>&#959;</mtext></msub></math>is independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>r</mi><mi>e</mi><mi>s</mi><mi>o</mi><mi>n</mi><mi>a</mi><mi>n</mi><mi>t</mi><mo>&#160;</mo><mi>f</mi><mi>r</mi><mi>e</mi><mi>q</mi><mi>u</mi><mi>e</mi><mi>n</mi><mi>c</mi><mi>y</mi><mo>)</mo><mo>&#160;</mo><msub><mtext>&#969;</mtext><mn>0</mn></msub><mo>=</mo><msup><mn>10</mn><mn>6</mn></msup><mtext>&#160;</mtext><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi><mo>/</mo><mi mathvariant="normal">s</mi></math></p><p>Current in the circuit is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>0</mn></msub><mo>=</mo><mfrac><msub><mi>V</mi><mn>0</mn></msub><msqrt><msup><mi>R</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mtext>&#969;</mtext><mi>L</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mtext>&#969;</mtext><mi>C</mi></mrow></mfrac></mrow></mfenced><mn>2</mn></msup></msqrt></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#969;</mtext><mo>&#8594;</mo><mn>0</mn><mo>,</mo><mtext>&#160;</mtext><mspace linebreak="newline"></mspace><msub><mi>i</mi><mn>0</mn></msub><mo>&#8594;</mo><mn>0</mn></math></p><p>For  <math><mtext>&#969;</mtext><mo>&#8811;</mo><msub><mrow><mtext>&#969;</mtext></mrow><mrow><mn>0</mn></mrow></msub></math> circuit behaves as inductor.</p>

</details>

---

### Q11. JEE Advanced 2016 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>In the circuit shown below, the key is pressed at time t = 0. Which of the following statement(s) is(are) true?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_13.jpg"/></p>

**Options:**

- **(A)** The voltmeter displays -5V as soon as the key is pressed, and displays +5V after a long time
- **(B)** The voltmeter will display 0 V at time t = ln 2 seconds
- **(C)** The current in the ammeter becomes 1/e of the initial value after 1 second
- **(D)** The current in the ammeter becomes zero after a long time

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The current in the ammeter becomes zero after a long time**

**Detailed Solution:**

<p>(i) At t = 0, capacitor acts as short - circuit
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_13_Ans_a_.jpg"/></p><p>The the reading of voltmeter will be -5 V
At <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">t</mi><mo>→</mo><mi mathvariant="normal">∞</mi><mo>,</mo></math> capacitor acts as open circuit and no current flows through voltmeter.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_13_Ans_b_.jpg"/>
If it is ideal voltmeter then its resistance is infinite & therefore it will read +5V
(ii)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_Papr2_13_Ans_c_.jpg"/></p><p>The Charge on the capacitor is given by
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi><mo>=</mo><msub><mi mathvariant="normal">q</mi><mn>0</mn></msub><mo>(</mo><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mi mathvariant="normal">t</mi><mo>/</mo><mi>RC</mi></mrow></msup><mo>)</mo></math>
as q<sub>0</sub> = RC is the max charge stored</p><p>For C<span style="font-size: 10.8333px;">1</span>=2C=40 <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi></math>F, R<span style="font-size: 10.8333px;">1</span>=R=25 k<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mi mathvariant="normal">x</mi></msub><mo>=</mo><mn>2</mn><mi>CV</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">e</mi><mfrac><mrow><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><mi>CR</mi></mrow></mfrac></msup></mrow></mfenced><mo>  </mo><mi mathvariant="normal"> </mi></math></p><p>The current through resistance of R=25 k is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal"> </mi><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mi mathvariant="normal">V</mi><mi mathvariant="normal">R</mi></mfrac><mi mathvariant="normal"> </mi><msup><mi mathvariant="normal">e</mi><mfrac><mrow><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><mi>CR</mi></mrow></mfrac></msup></math></p><p>For C<sub>2</sub>=C=20 <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi></math>F, R<sub>2</sub>=2R=50 k
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mi mathvariant="normal">y</mi></msub><mo>=</mo><mi>CV</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">e</mi><mfrac><mrow><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><mi>CR</mi></mrow></mfrac></msup></mrow></mfenced><mi mathvariant="normal"> </mi></math></p><p>The current through resistance of 2R=50k is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mfrac><mi mathvariant="normal">V</mi><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow></mfrac><msup><mi mathvariant="normal">e</mi><mfrac><mrow><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><mi>CR</mi></mrow></mfrac></msup></math></p><p>Reading of voltmeter (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo></math>V) = Voltage across 2C - Voltage across 2R</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∆</mo><mi mathvariant="normal">V</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">q</mi><mi mathvariant="normal">x</mi></msub><mrow><mn>2</mn><mi mathvariant="normal">C</mi></mrow></mfrac><mo>-</mo><mi mathvariant="normal">y</mi><mo>(</mo><mn>2</mn><mi mathvariant="normal">R</mi><mo>)</mo><mspace linebreak="newline"></mspace><mo>=</mo><mi mathvariant="normal">V</mi><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mi mathvariant="normal">e</mi><mfrac><mrow><mo>-</mo><mi mathvariant="normal">t</mi></mrow><mrow><mn>2</mn><mi>CR</mi></mrow></mfrac></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>
(iii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">τ</mi><mo>=</mo><mn>2</mn><mi>RC</mi><mspace linebreak="newline"></mspace><mo>=</mo><mn>2</mn><mo>×</mo><mn>25</mn><mo>×</mo><msup><mn>10</mn><mn>3</mn></msup><mo>×</mo><mn>40</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup><mspace linebreak="newline"></mspace><mo>=</mo><mn>1</mn><mo> </mo><mi>sec</mi></math>
Now Current is given by<math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi mathvariant="normal">i</mi><mo>=</mo><msub><mi mathvariant="normal">i</mi><mn>0</mn></msub><msup><mi mathvariant="normal">e</mi><mrow><mfenced><mrow><mo>-</mo><mfrac><mi mathvariant="normal">t</mi><mi mathvariant="normal">τ</mi></mfrac></mrow></mfenced><mi mathvariant="normal"> </mi></mrow></msup></math></p><p>at t= 1 sec, Current <math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi mathvariant="normal">i</mi><mo>=</mo><mfrac><msub><mi mathvariant="normal">i</mi><mi mathvariant="normal">o</mi></msub><mi mathvariant="normal">e</mi></mfrac></math></p><p>
(iv) After long time no current flows since capacitor act as a open circuit and voltmeter acts as an ideal it's resistance is infinite, therefore current does not allow.</p>

</details>

---

### Q12. JEE Advanced 2016 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Two inductors <math><msub><mrow><mi>L</mi></mrow><mrow><mi>i</mi></mrow></msub></math> (inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>mH</mi></math>, internal resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> ) and <math><msub><mrow><mi>L</mi></mrow><mrow><mn>2</mn></mrow></msub></math> (inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>mH</mi></math>, internal resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> ), and a resistor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>(resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> ) are all connected in parallel across a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery. The circuit is switched on at time <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mn>0</mn></math>. The ratio of the maximum current <math><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub></mrow><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub></mrow></mfrac></mrow></mfenced></math> drawn from the battery is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/Phy_15_Ans_.jpg"/>
Initally, the inductances will offer infinite resistance and the current will be maximum.</p><p><math><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>ε</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mi>A</mi></math> (Initially at t = 0)</p><p>Upon reaching steady state, the inductances will act as pure resistors and hence the current will be minimum.
<math><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>ε</mi></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mi>e</mi><mi>q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mi> </mi><mi>ε</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>R</mi></mrow></mfrac></mrow></mfenced></math> (Finally in steady state)
<math><mo>=</mo><mn>5</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>A</mi></math>
<math><mfrac><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub></mrow><mrow><msub><mrow><mi>I</mi></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub></mrow></mfrac><mo>=</mo><mn>8</mn></math></p>

</details>

---

### Q13. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>At time t = 0, terminal A in the circuit shown in the figure is connected to B by a key and an alternating current <math><mi mathvariant="normal">I</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">ω</mi><mi mathvariant="normal">t</mi></mrow></mfenced></mrow></mrow></math> , with <math><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><mn>1</mn><mi mathvariant="normal">A</mi></math> and <math><mi mathvariant="normal">ω</mi><mo>=</mo><mn>500</mn><mi mathvariant="normal"> </mi></math> rad/s starts flowing in it with the initial direction shown in the figure. At <math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">π</mi></mrow><mrow><mn>6</mn><mi mathvariant="normal">ω</mi></mrow></mfrac></math> , the key is switched from B to D. Now onwards only A and D are connected. A total charge Q flows from the battery to charge the capacitor fully. If <math><mi mathvariant="normal">C</mi><mo>=</mo><mn>20</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">F</mi><mo>,</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">R</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">Ω</mi></math> and the battery is ideal with of 50V, identify the correct statement(s).

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image1-a89efa1a-9cfb-473f-9eb2-e89c46373e8c.png"/></p>

**Options:**

- **(A)** Magnitude of the maximum charge on the capacitor before  <math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">π</mi></mrow><mrow><mn>6</mn><mi mathvariant="normal">ω</mi></mrow></mfrac></math>  is  <math><mn>1</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal"> </mi><mi mathvariant="normal">C</mi></math> .
- **(B)** The current in the left part of the circuit just before  <math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">π</mi></mrow><mrow><mn>6</mn><mi mathvariant="normal">ω</mi></mrow></mfrac></math>  is clockwise.
- **(C)** Immediately after A is connected to D, the current in R is 10 A.
- **(D)** <math><mi mathvariant="normal">Q</mi><mo>=</mo><mn>2</mn><mo>&times;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal"> </mi><mi mathvariant="normal">C</mi></math> .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi mathvariant="normal">Q</mi><mo>=</mo><mn>2</mn><mo>&times;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal"> </mi><mi mathvariant="normal">C</mi></math> .**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>i</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>,</mo><mi mathvariant="normal">I</mi><mo>=</mo><msub><mi mathvariant="normal">I</mi><mn>0</mn></msub><mi>cos</mi><mfenced><mi>&#969;t</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>P</mi><mi>e</mi><mi>a</mi><mi>k</mi><mo>&#160;</mo><mi>o</mi><mi>r</mi><mo>&#160;</mo><mi>m</mi><mi>a</mi><mi>x</mi><mi>i</mi><mi>m</mi><mi>u</mi><mi>m</mi><mo>&#160;</mo><mi>c</mi><mi>u</mi><mi>r</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mo>&#160;</mo><msub><mi mathvariant="normal">I</mi><mn>0</mn></msub><mo>=</mo><mn>1</mn><mi mathvariant="normal">A</mi><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>g</mi><mi>u</mi><mi>l</mi><mi>a</mi><mi>r</mi><mo>&#160;</mo><mi>f</mi><mi>r</mi><mi>e</mi><mi>q</mi><mi>u</mi><mi>e</mi><mi>n</mi><mi>c</mi><mi>y</mi><mo>,</mo><mi mathvariant="normal">&#969;</mi><mo>=</mo><mn>500</mn><mo>&#160;</mo><mi>rad</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>c</mi><mi>a</mi><mi>p</mi><mi>a</mi><mi>c</mi><mi>i</mi><mi>tan</mi><mi>c</mi><mi>e</mi><mo>&#160;</mo><mi mathvariant="normal">C</mi><mo>=</mo><mn>20</mn><mi>&#956;F</mi><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>r</mi><mi>e</mi><mi>s</mi><mi>i</mi><mi>s</mi><mi>tan</mi><mi>c</mi><mi>e</mi><mo>&#8201;</mo><mi>R</mi><mo>=</mo><mn>10</mn><mi mathvariant="normal">&#937;</mi><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>b</mi><mi>a</mi><mi>t</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>y</mi><mo>&#160;</mo><mi>v</mi><mi>o</mi><mi>l</mi><mi>t</mi><mi>a</mi><mi>g</mi><mi>e</mi><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>=</mo><mn>50</mn><mi mathvariant="normal">V</mi></math>If q represent the charge on capacitor&rsquo;s upper plate:
<math><mi mathvariant="normal">I</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mo>(</mo><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">t</mi></mrow></mrow><mo>)</mo><mi mathvariant="normal">&#160;</mi></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">q</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">&#969;</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">&#969;</mi><mi mathvariant="normal">t</mi></mrow></mfenced></mrow></mrow></math>
<math><mo>&#8756;</mo></math> Max charge <math><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">m</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">x</mi></mrow></msub></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mi mathvariant="normal">A</mi></mrow><mrow><mn>500</mn><mfrac><mrow><mi mathvariant="normal">R</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></mrow><mrow><mi mathvariant="normal">s</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
Charge of upper plate at <math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>6</mn><mi mathvariant="normal">&#969;</mi></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">&#969;</mi></mrow></mfrac><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>7</mn><mi mathvariant="normal">&#960;</mi></mrow><mrow><mi mathvariant="normal">&#969;</mi></mrow></mfrac></mrow></mfenced><mi mathvariant="normal">&#160;</mi></mrow></mrow><mo>=</mo><mo>-</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn><mi mathvariant="normal">&#969;</mi></mrow></mfrac></math>
When capacitor is fully charged then charge on upper plate <math><mo>=</mo><mn>50</mn><mi mathvariant="normal">v</mi><mo>&#215;</mo><mn>20</mn><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">f</mi></math>
<math><mo>=</mo><mn>10</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
<math><mo>&#8658;</mo><mi mathvariant="normal">Q</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mn>2</mn><mi mathvariant="normal">&#969;</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal">C</mi></math>
Voltage across capacitor when A and D are connected <math><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>3</mn></mrow></msup><mi mathvariant="normal">C</mi></mrow><mrow><mn>20</mn><mo>&#215;</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">f</mi></mrow></mfrac><mo>=</mo><mn>50</mn><mi mathvariant="normal">V</mi></math>
Total voltage across <math><mi mathvariant="normal">R</mi><mo>=</mo><mn>100</mn><mi mathvariant="normal">V</mi></math>
Current is anticlockwise

</details>

---

### Q14. JEE Advanced 2011 (Paper 2)

*Type:* `numerical` | *Level:* `1`

A series $R-C$ combination is connected to an $\mathrm{AC}$ voltage of angular frequency $\omega=500 \mathrm{rad} / \mathrm{s}$. If the impedance of the $R-C$ circuit is $R \sqrt{1.25}$, the time constant (in millisecond) of the circuit is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

$Z=\sqrt{R^2+X_C^2}=R \sqrt{1.25}$
$$
\therefore \quad R^2+X_C^2=1.25 R^2
$$
or $\quad X_C=\frac{R}{2}$
or $\quad \frac{1}{\omega C}=\frac{R}{2}$
$\begin{aligned} \therefore \text { Time constant } & =C R=\frac{2}{\omega} \\ & =\frac{2}{500} \mathrm{~s}=4 \mathrm{~ms}\end{aligned}$
$\therefore$ Answer is 4 .
Analysis of Question
(i) Question is very simple.
(ii) I think this is one of the simplest formula based question of this paper.

</details>

---

### Q15. JEE Advanced 2011 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `1`

A series $R$ - $C$ circuit is connected to $A C$ voltage source. Consider two cases; $(A)$ when $C$ is without a dielectric medium and $(B)$ when $C$ is filled with dielectric of constant 4. The current $I_R$ through the resistor and voltage $V_C$ across the capacitor are compared in the two cases. Which of the following is/are true?

**Options:**

- **(A)** $I_R^A>I_R^B$
- **(B)** $I_R^A < I_R^B$
- **(C)** $V_C^A>V_C^B$
- **(D)** $V_C^A < V_C^B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $V_C^A>V_C^B$**

**Detailed Solution:**

$Z=\sqrt{R^2+X_C^2}=\sqrt{R^2+\left(\frac{1}{\omega C}\right)^2}$
In case (b) capacitance $C$ will be more.
Therefore, impedance $Z$ will be less.
Hence, current will be more.
$\therefore$ Option (b) is correct.
Further, $\quad \begin{aligned} V_C & =\sqrt{V^2-V_R^2} \\ & =\sqrt{V^2-(I R)^2}\end{aligned}$
In case (b), since current $I$ is more.
Therefore, $V_C$ will be less.
$\therefore$ Option (c) is correct.
$\therefore$ Correct options are (b) and (c).
Analysis of Question
(i) Question is moderately difficult.
(ii) In my opinion problems of alternating currents are not very difficult.
(iii) Topic of $A C$ is small. One can feel comfortable in this topic by putting less efforts.

</details>

---

### Q16. JEE Advanced 2010 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

You are given many resistances, capacitors and inductors. These are connected to a variable DC voltage source (the first two circuits) or an AC voltage source of $50 \mathrm{~Hz}$ frequency (the next three circuits) in different ways as shown in Column II. When a current $I$ (steady state for DC or rms for $A C$ ) flows through the circuit, the corresponding voltage $V_1$ and $V_2$ (indicated in circuits) are related as shown in Column I. Match the two
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/kkECDVG_QlKf7IOiWse0mZXry5Mwmeoal-mAQ0RPmpQ.original.fullsize.png">

**Options:**

- **(A)** (A) R,S,T, (B) Q,R,T, (C) P, (D) Q,R,S
- **(B)** (A) R,S,T, (B) Q,R,S,T, (C) P,Q, (D) Q,R,S,T
- **(C)** (A) S,T, (B) Q,R,T, (C) P,Q, (D) Q,R,S,T
- **(D)** (A) S,T, (B) Q,R,S,T, (C) P, (D) Q,R,S

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (A) R,S,T, (B) Q,R,S,T, (C) P,Q, (D) Q,R,S,T**

**Detailed Solution:**

In circuit (P), I can't be non zero in steady state.
In circuit (Q) :
$V_1=0$ and $V_2=2 I=V$ (also)
$$
\begin{aligned}
& \text { In circuit (R): } V_1=X_L I=(2 \pi f \mathrm{~L}) I \\
& \quad=\left(2 \pi \times 50 \times 6 \times 10^{-3}\right) I \\
& \quad=1.88 I \\
& V_2=2 I
\end{aligned}
$$
In circuit (S): $V_1=X_L I=1.88 I$
$$
\begin{array}{r}
V_2=X_C I=\left(\frac{1}{2 \pi f C}\right) I \\
=\left(\frac{1}{2 \pi \times 50 \times 3 \times 10^{-6}}\right) I=(1061) I
\end{array}
$$
In circuit (T):
$$
\begin{aligned}
& V_1=I R=(1000) I \\
& V_2=X_C I=(1061) I
\end{aligned}
$$
Therefore the correct options are as under
(A) $\rightarrow$ R, S, T $\quad$ (B) $\rightarrow$ Q, R, S, T
(C) $\rightarrow$ Q or $P, Q \quad$ (D) $\rightarrow$ Q, R, S, T

</details>

---

### Q17. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `2`

At time $t=0$, a battery of $10 \mathrm{~V}$ is connected across points $A$ and $B$ in the given circuit. If the capacitors have no charge initially, at what time (in second) does the voltage across them become $4 \mathrm{~V}$ ?
[Take $: \ln 5=1.6, \ln 3=1.1]$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/rfEriRiK0xFSvAhxaL1qn9GOEaZY3xS3ePfpc2E2LMM.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Voltage across the capacitors will increase from 0 to $10 \mathrm{~V}$ exponentially. The voltage at time $t$ will be given by
$$
\begin{aligned}
& V=10\left(1-e^{-t / \tau} \mathrm{C}\right) \\
& \text { Here } \tau_c=C_{\text {net }} R_{\text {net }} \\
& =\left(1 \times 10^6\right)\left(4 \times 10^{-6}\right)=4 \mathrm{~s} \\
& \therefore \quad V=10\left(1-e^{-t / 4}\right) \\
&
\end{aligned}
$$
Substituting $V=4$ volt we have,
$$
4=10\left(1-e^{-t / 4}\right)
$$
Substituting $V=4$ volt we have,
$$
4=10\left(1-e^{-t / 4}\right)
$$
or $e^{-t / 4}=0.6=\frac{3}{5}$
Taking $\log$ both sides we have,
$$
-\frac{t}{4}=\ln 3-\ln 5
$$
or $\quad t=4(\ln 5-\ln 3)=2 \mathrm{~s}$.
Hence, the answer is 2 .

</details>

---

### Q18. JEE Advanced 2010 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

An AC voltage source of variable angular frequency $\omega$ and fixed amplitude $V_0$ is connected in series with a capacitance $C$ and an electric bulb of resistance $R$ (inductance zero). When $\omega$ is increased

**Options:**

- **(A)** the bulb glows dimmer
- **(B)** the bulb glows brighter
- **(C)** total impedance of the circuit is unchanged
- **(D)** total impedance of the circuit increases

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) the bulb glows brighter**

**Detailed Solution:**

$Z=\sqrt{R^2+X_C^2}: I_{\mathrm{rms}}=\frac{V_{\mathrm{rms}}}{Z}: P=I_{\mathrm{rms}}^2 R$ where, $\quad X_C=\frac{1}{\omega C}$
As $\omega$ is increased, $X_C$ will decrease or $Z$ will decrease. Hence $I_{\mathrm{mms}}$ or $P$ will increase. Therefore, bulb glows brighter.
Hence the correct option is (b).

</details>

---

### Q19. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `3`

<strong>Paragraph:</strong>
The capacitor of capacitance $C$ can be charged (with the help of a resistance $R$ ) by a voltage source $V$, by closing switch $S_1$ while keeping switch $S_2$ open. The capacitor can be connected in series with an inductor $L$ by closing switch $S_2$ and opening $S_1$.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/0Y1I8mvhYVnowTpUifCLeg2xPE10yRn1Ap7tEzxaL24.original.fullsize.png">
<strong>Question:</strong>
If the total charge stored in the $L C$ circuit is $Q_0$, then for $t \geq 0$

**Options:**

- **(A)** the charge on the capacitor is $Q=Q_0 \cos \left(\frac{\pi}{2}+\frac{t}{\sqrt{L C}}\right)$
- **(B)** the charge on the capacitor is $Q=Q_0 \cos \left(\frac{\pi}{2}-\frac{t}{\sqrt{L C}}\right)$
- **(C)** the charge on the capacitor is $Q=-L C \frac{d^2 Q}{d t^2}$
- **(D)** the charge on the capacitor is $Q=-\frac{1}{\sqrt{L C}} \frac{d^2 Q}{d t^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) the charge on the capacitor is $Q=-L C \frac{d^2 Q}{d t^2}$**

**Detailed Solution:**

Comparing the LC oscillations with normal SHM, we get
$$
\frac{d^2 Q}{d t^2}=-\omega^2 Q
$$
Here,
$$
\begin{aligned}
\omega^2 & =\frac{1}{L C} \\
Q & =-L C \frac{d^2 Q}{d t^2}
\end{aligned}
$$
$$
\therefore \quad Q=-L C \frac{d^2 Q}{d t^2}
$$

</details>

---

### Q20. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

<strong>Paragraph:</strong>
The capacitor of capacitance $C$ can be charged (with the help of a resistance $R$ ) by a voltage source $V$, by closing switch $S_1$ while keeping switch $S_2$ open. The capacitor can be connected in series with an inductor $L$ by closing switch $S_2$ and opening $S_1$.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/0Y1I8mvhYVnowTpUifCLeg2xPE10yRn1Ap7tEzxaL24.original.fullsize.png">
<strong>Question:</strong>
After the capacitor gets fully charged, $S_1$ is opened and $S_2$ is closed so that the inductor is connected in series with the capacitor. Then,

**Options:**

- **(A)** at $t=0$, energy stored in the circuit is purely in the form of magnetic energy
- **(B)** at any time $t>0$, current in the circuit is in the same direction
- **(C)** at $t>0$, there is no exchange of energy between the inductor and capacitor
- **(D)** at any time $t>0$, maximum instantaneous current in the circuit may $V \sqrt{\frac{C}{L}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) at any time $t>0$, maximum instantaneous current in the circuit may $V \sqrt{\frac{C}{L}}$**

**Detailed Solution:**

From conservation of energy, $\frac{1}{2} L I_{\max }^2=\frac{1}{2} C V^2$
$$
\therefore \quad I_{\max }=V \sqrt{\frac{C}{L}}
$$

</details>

---

### Q21. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
The capacitor of capacitance $C$ can be charged (with the help of a resistance $R$ ) by a voltage source $V$, by closing switch $S_1$ while keeping switch $S_2$ open. The capacitor can be connected in series with an inductor $L$ by closing switch $S_2$ and opening $S_1$.<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/0Y1I8mvhYVnowTpUifCLeg2xPE10yRn1Ap7tEzxaL24.original.fullsize.png">
<strong>Question:</strong>
Initially, the capacitor was uncharged. Now, switch $S_1$ is closed and $S_2$ is kept open. If time constant of this circuit is $\tau$, then

**Options:**

- **(A)** after time interval $\tau$, charge on the capacitor is $C V / 2$
- **(B)** after time interval $2 \tau$, charge on the capacitor is $C V /\left(1-e^{-2}\right)$
- **(C)** the work done by the voltage source will be half on the heat dissipated when the capacitor is fully charged
- **(D)** after time interval $2 \tau$, charge on the capacitor is $C V\left(1-e^{-1}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) after time interval $2 \tau$, charge on the capacitor is $C V /\left(1-e^{-2}\right)$**

**Detailed Solution:**

Charge on capacitor at time $t$ is $q=q_0\left(1-e^{-t / \tau}\right)$
$\begin{array}{ll}\text { Here, } & q_0=C V \text { and } t=2 \tau \\ \therefore & q=C V\left(1-e^{-2 \tau / \tau}\right)=C V\left(1-e^{-2}\right)\end{array}$

</details>

---

### Q22. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

$$
\text { Find the time constant for the given } R C \text { circuits in correct order. }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/7aU5aAIeBz3ebRc4ZXsLteRMyxFnx6QQ53YxU94qFDo.original.fullsize.png">

$R_1=1 \Omega, R_2=2 \Omega, C_1=4 \mu \mathrm{F}, C_2=2 \mu \mathrm{F}$

**Options:**

- **(A)** $18,4,8 / 9$
- **(B)** $18,8 / 9,4$
- **(C)** $4,18,8 / 9$
- **(D)** $4,8 / 9,18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $18,8 / 9,4$**

**Detailed Solution:**

$$
\begin{aligned}
\tau & =C R \\
\tau_1 & =\left(C_1+C_2\right)\left(R_1+R_2\right)=18 \mu \mathrm{s} \\
\tau_2 & =\left(\frac{C_1 C_2}{C_1+C_2}\right)\left(\frac{R_1 R_2}{R_1+R_2}\right)=\frac{8}{6} \times \frac{2}{3}=\frac{8}{9} \mu \mathrm{s} \\
\tau_2 & =\left(C_1+C_2\right)\left(\frac{R_1 R_2}{R_1+R_2}\right)=(6)\left(\frac{2}{3}\right)=4 \mu \mathrm{s}
\end{aligned}
$$

</details>

---

