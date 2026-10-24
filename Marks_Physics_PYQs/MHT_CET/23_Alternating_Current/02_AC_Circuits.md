# MHT CET Physics - Alternating Current

## Topic 2: AC Circuits

**Total Questions:** 182

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A resistor of $200\,\Omega$, an inductor of self inductance $\left(\dfrac{2}{\pi^2}\right)$ H and a capacitor of unknown capacity are connected in series to an a.c. source of $100$ V and $50$ Hz. When the current and voltage are in phase the capacitance and the power dissipated is

**Options:**

- **(A)** $2\times 10^{-5}$ F, $25$ W
- **(B)** $4\times 10^{-5}$ F, $100$ W
- **(C)** $5\times 10^{-5}$ F, $50$ W
- **(D)** $3\times 10^{-5}$ F, $200$ W

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5\times 10^{-5}$ F, $50$ W**

**Detailed Solution:**

Given $R = 200\,\Omega$, $L = \dfrac{2}{\pi^2}$ H, $V_{rms} = 100$ V, and $f = 50$ Hz.

Since the current and voltage are in phase, the circuit is in resonance. At resonance, the inductive reactance equals the capacitive reactance ($X_L = X_C$).

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L} = \dfrac{1}{(2\pi f)^2 L}$

Substituting the given values:

$C = \dfrac{1}{(2\pi \times 50)^2 \times \left(\dfrac{2}{\pi^2}\right)} = \dfrac{1}{10000\pi^2 \times \dfrac{2}{\pi^2}} = \dfrac{1}{20000} = 5 \times 10^{-5}$ F

At resonance, the total impedance of the circuit is purely resistive, so $Z = R = 200\,\Omega$.

The power dissipated is given by:

$P = \dfrac{V_{rms}^2}{R} = \dfrac{(100)^2}{200} = \dfrac{10000}{200} = 50$ W

Answer: $5\times 10^{-5}$ F, $50$ W

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A $40$ $\mu$F capacitor is charged to $10$ volts of potential. The battery is disconnected, and a pure $100$ mH coil is connected across the capacitor so that LC oscillations are set up. Then, the maximum current in the coil is:

**Options:**

- **(A)** $0.25$ A
- **(B)** $0.10$ A
- **(C)** $0.30$ A
- **(D)** $0.20$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.20$ A**

**Detailed Solution:**

The maximum energy stored in the capacitor is equal to the maximum energy stored in the inductor during LC oscillations.

$\dfrac{1}{2} C V^2 = \dfrac{1}{2} L I_{max}^2$

$I_{max} = V \sqrt{\dfrac{C}{L}}$

Substituting the given values:

$I_{max} = 10 \sqrt{\dfrac{40 \times 10^{-6}}{100 \times 10^{-3}}}$

$I_{max} = 10 \sqrt{\dfrac{40 \times 10^{-6}}{0.1}}$

$I_{max} = 10 \sqrt{400 \times 10^{-6}}$

$I_{max} = 10 \times 20 \times 10^{-3}$

$I_{max} = 0.20 \text{ A}$

Answer: $0.20$ A

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

To reduce the resonant frequency in an L-C-R series circuit with a generator,

**Options:**

- **(A)** the iron core of the inductor should be removed and the value of the capacitor is kept constant.
- **(B)** the dielectric in the capacitor should be removed and the value of the inductor is kept constant.
- **(C)** the generator frequency should be reduced.
- **(D)** another capacitor should be added in parallel to the first capacitor and the value of the inductor is kept constant.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) another capacitor should be added in parallel to the first capacitor and the value of the inductor is kept constant.**

**Detailed Solution:**

The resonant frequency of an L-C-R series circuit is given by $f_r = \dfrac{1}{2\pi\sqrt{LC}}$.

To reduce the resonant frequency $f_r$, the value of the inductance $L$ or the capacitance $C$ must be increased.

Removing the iron core of the inductor decreases its inductance $L$, which would increase $f_r$.

Removing the dielectric in the capacitor decreases its capacitance $C$, which would also increase $f_r$.

The resonant frequency is a characteristic of the circuit components and is independent of the generator frequency.

Adding another capacitor in parallel to the first capacitor increases the equivalent capacitance of the circuit ($C_{eq} = C_1 + C_2$). An increase in $C$ results in a decrease in the resonant frequency $f_r$.

Answer: another capacitor should be added in parallel to the first capacitor and the value of the inductor is kept constant.

</details>

---

### Q4. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a discharging series L-C-R circuit, $C = 2 \text{ }\mu\text{F}$, $L = 1 \text{ mH}$ and $R = 10 \text{ }\Omega$. The ratio of the energies stored in the inductor and in the capacitor, when the maximum current flows in the circuit, is

**Options:**

- **(A)** $2:1$
- **(B)** $3:1$
- **(C)** $3:2$
- **(D)** $5:1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5:1$**

**Detailed Solution:**

For a discharging series L-C-R circuit, the voltage equation is given by:

$L \dfrac{di}{dt} + iR + \dfrac{q}{C} = 0$

When the current $i$ is maximum, its rate of change is zero, so $\dfrac{di}{dt} = 0$. Substituting this into the equation gives:

$iR + \dfrac{q}{C} = 0 \Rightarrow q = -iRC$

The energy stored in the inductor is:

$U_L = \dfrac{1}{2}Li^2$

The energy stored in the capacitor is:

$U_C = \dfrac{q^2}{2C} = \dfrac{(-iRC)^2}{2C} = \dfrac{1}{2}CR^2i^2$

The ratio of the energy stored in the inductor to that in the capacitor is:

$\dfrac{U_L}{U_C} = \dfrac{\dfrac{1}{2}Li^2}{\dfrac{1}{2}CR^2i^2} = \dfrac{L}{CR^2}$

Given the values:
$L = 1 \text{ mH} = 10^{-3} \text{ H}$
$C = 2 \text{ }\mu\text{F} = 2 \times 10^{-6} \text{ F}$
$R = 10 \text{ }\Omega$

Substituting these values into the ratio:

$\dfrac{U_L}{U_C} = \dfrac{10^{-3}}{2 \times 10^{-6} \times (10)^2} = \dfrac{10^{-3}}{2 \times 10^{-4}} = \dfrac{10}{2} = 5$

Thus, the ratio of the energies is $5:1$.

Answer: $5:1$

</details>

---

### Q5. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An inductor of inductance $L$ and a resistor of resistance $R$ are joined in series and connected to an a.c. source of frequency $\omega$. The power dissipated in the circuit is

**Options:**

- **(A)** $\dfrac{(R^2 + \omega^2 L^2)}{V}$
- **(B)** $\dfrac{V}{(R^2 + \omega^2 L^2)}$
- **(C)** $\dfrac{V^2 R}{(R^2 + \omega^2 L^2)}$
- **(D)** $\sqrt{\dfrac{R^2 + \omega^2 L^2}{V^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{V^2 R}{(R^2 + \omega^2 L^2)}$**

**Detailed Solution:**

The impedance of the series LR circuit is given by $Z = \sqrt{R^2 + \omega^2 L^2}$.

The rms current flowing through the circuit is $I = \dfrac{V}{Z} = \dfrac{V}{\sqrt{R^2 + \omega^2 L^2}}$.

The average power dissipated in the circuit is only due to the resistor, which is given by $P = I^2 R$.

Substituting the value of $I$, we get:

$P = \left( \dfrac{V}{\sqrt{R^2 + \omega^2 L^2}} \right)^2 R = \dfrac{V^2 R}{R^2 + \omega^2 L^2}$.

Answer: $\dfrac{V^2 R}{(R^2 + \omega^2 L^2)}$

</details>

---

### Q6. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Same current is flowing in two AC circuits. First contains only inductance and second contains only capacitance. If frequency of AC is increased for both, the current will

**Options:**

- **(A)** increase in first circuit and decrease in second
- **(B)** increase in both circuits
- **(C)** decrease in both circuits
- **(D)** decrease in first circuit and increase in second

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decrease in first circuit and increase in second**

**Detailed Solution:**

For an AC circuit containing only inductance, the inductive reactance is $X_L = \omega L = 2\pi f L$.

The current in the inductive circuit is $I_L = \dfrac{V}{X_L} = \dfrac{V}{2\pi f L}$.

When the frequency $f$ is increased, $X_L$ increases, so the current $I_L$ decreases.

For an AC circuit containing only capacitance, the capacitive reactance is $X_C = \dfrac{1}{\omega C} = \dfrac{1}{2\pi f C}$.

The current in the capacitive circuit is $I_C = \dfrac{V}{X_C} = V(2\pi f C)$.

When the frequency $f$ is increased, $X_C$ decreases, so the current $I_C$ increases.

Thus, the current decreases in the first circuit and increases in the second circuit.

Answer: decrease in first circuit and increase in second

</details>

---

### Q7. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The natural frequency of L-C circuit is $125000$ Hz. Then the capacitor C is replaced by another capacitor with a dielectric medium of dielectric constant K. Now the frequency decreases by $25$ KHz. The value of K is

**Options:**

- **(A)** $3.0$
- **(B)** $2.1$
- **(C)** $1.56$
- **(D)** $1.7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1.56$**

**Detailed Solution:**

The natural frequency of an L-C circuit is given by $f = \dfrac{1}{2\pi\sqrt{LC}}$.

Initially, $f_1 = 125000$ Hz.

When the capacitor is replaced by one with a dielectric medium of dielectric constant $K$, the new capacitance is $C' = KC$.

The new frequency is $f_2 = \dfrac{1}{2\pi\sqrt{L(KC)}} = \dfrac{f_1}{\sqrt{K}}$.

Given that the frequency decreases by $25$ kHz, $f_2 = 125000 - 25000 = 100000$ Hz.

Substituting the values, $100000 = \dfrac{125000}{\sqrt{K}}$.

$\sqrt{K} = \dfrac{125000}{100000} = \dfrac{5}{4} = 1.25$

$K = (1.25)^2 = 1.5625 \approx 1.56$

Answer: $1.56$

</details>

---

### Q8. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following graph represents the correct variation of inductive reactance ($X_L$) with angular frequency ($\omega$)?
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/15_may_shift_1__q27_d1.png" />

**Options:**

- **(A)** A
- **(B)** B
- **(C)** C
- **(D)** D

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) B**

**Detailed Solution:**

The inductive reactance $X_L$ of an inductor is given by the formula:

$X_L = \omega L$

where $\omega$ is the angular frequency and $L$ is the inductance.

This equation is of the form $y = mx$, which represents a straight line passing through the origin with a positive slope (since $L > 0$).

Looking at the given graphs, graph (B) correctly shows a straight line passing through the origin, representing the direct proportionality between $X_L$ and $\omega$.

Answer: B

</details>

---

### Q9. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An arc lamp requires a direct current of $10$ A at $90$ V to function. If it is connected to $220$ V (rms), $50$ Hz a.c. supply, the series inductor needed for it to work is nearly

**Options:**

- **(A)** $\dfrac{1}{\pi}$ H
- **(B)** $\dfrac{1}{5\pi}$ H
- **(C)** $\dfrac{1}{2\pi}$ H
- **(D)** $\dfrac{1}{4\pi}$ H

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{5\pi}$ H**

**Detailed Solution:**

Resistance of the arc lamp, $R = \dfrac{V}{I} = \dfrac{90}{10} = 9\ \Omega$

In the AC circuit, the required rms current is $I_{rms} = 10$ A.

The impedance of the circuit is $Z = \dfrac{V_{rms}}{I_{rms}} = \dfrac{220}{10} = 22\ \Omega$

The impedance of an LR circuit is given by $Z = \sqrt{R^2 + X_L^2}$

Substituting the values, $22 = \sqrt{9^2 + X_L^2}$

$X_L^2 = 22^2 - 9^2 = 484 - 81 = 403$

$X_L = \sqrt{403} \approx 20\ \Omega$

The inductive reactance is $X_L = \omega L = 2\pi f L$

$20 = 2\pi \times 50 \times L = 100\pi L$

$L = \dfrac{20}{100\pi} = \dfrac{1}{5\pi}$ H

Answer: $\dfrac{1}{5\pi}$ H

</details>

---

### Q10. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A $10\ \mu$F capacitor is charged to $25$ V of potential. The battery is then disconnected and a pure $100$ mH coil is connected across the capacitor so that L-C oscillations are set up. The maximum current in the coil is

**Options:**

- **(A)** $0.25$ A
- **(B)** $0.01$ A
- **(C)** $2.5$ A
- **(D)** $1.6$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.25$ A**

**Detailed Solution:**

By the principle of conservation of energy, the maximum energy stored in the capacitor is equal to the maximum energy stored in the inductor during L-C oscillations.

$\dfrac{1}{2}CV^2 = \dfrac{1}{2}LI_{max}^2$

$I_{max} = V \sqrt{\dfrac{C}{L}}$

Substituting the given values $V = 25$ V, $C = 10 \times 10^{-6}$ F, and $L = 100 \times 10^{-3}$ H:

$I_{max} = 25 \sqrt{\dfrac{10 \times 10^{-6}}{100 \times 10^{-3}}}$

$I_{max} = 25 \sqrt{10^{-4}}$

$I_{max} = 25 \times 10^{-2} = 0.25$ A

Answer: $0.25$ A

</details>

---

### Q11. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A coil of self inductance $L$ is connected in series with a bulb B and an a.c. source. Brightness of the bulb decreases when

**Options:**

- **(A)** frequency of a.c. source is decreased
- **(B)** number of turns in the coil is reduced
- **(C)** an iron rod is inserted in the coil
- **(D)** a capacitance of reactance $X_c$ is included in the same circuit

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) an iron rod is inserted in the coil**

**Detailed Solution:**

The brightness of the bulb depends on the current flowing through it. The current in the AC circuit is given by $I = \dfrac{V}{Z}$, where the impedance $Z = \sqrt{R^2 + X_L^2}$ and $X_L = \omega L = 2\pi f L$.

To decrease the brightness of the bulb, the current $I$ must decrease, which requires the impedance $Z$ to increase.

When an iron rod is inserted into the coil, the magnetic permeability of the core increases, which increases the self-inductance $L$ of the coil. An increase in $L$ leads to an increase in the inductive reactance $X_L$ and the total impedance $Z$. As a result, the current $I$ decreases, and the brightness of the bulb decreases.

Answer: an iron rod is inserted in the coil

</details>

---

### Q12. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An inductance of negligible resistance, whose reactance is $120$ $\Omega$ at $200$ Hz is connected to a $240$ V, $60$ Hz Power line. The current in the inductor is

**Options:**

- **(A)** $6.66$ A
- **(B)** $6.60$ A
- **(C)** $5.45$ A
- **(D)** $54.5$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6.66$ A**

**Detailed Solution:**

The inductive reactance is given by $X_L = 2 \pi f L$.

Since $X_L \propto f$, the reactance at $60$ Hz is

$X_{L2} = X_{L1} \times \dfrac{f_2}{f_1} = 120 \times \dfrac{60}{200} = 36$ $\Omega$

The current in the inductor is

$I = \dfrac{V}{X_{L2}} = \dfrac{240}{36} = \dfrac{20}{3} = 6.66$ A

Answer: $6.66$ A

</details>

---

### Q13. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An alternating voltage $V = 200\sqrt{2} \sin(100t)$ volt is connected to a $1$ $\mu$F capacitor through an a.c. ammeter. The reading of the ammeter will be

**Options:**

- **(A)** $10$ mA
- **(B)** $20$ mA
- **(C)** $40$ mA
- **(D)** $80$ mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $20$ mA**

**Detailed Solution:**

The given alternating voltage is $V = 200\sqrt{2} \sin(100t)$ V.

Comparing this with the standard equation $V = V_0 \sin(\omega t)$, we get:
Peak voltage, $V_0 = 200\sqrt{2}$ V
Angular frequency, $\omega = 100$ rad/s

The rms voltage is given by:
$V_{rms} = \dfrac{V_0}{\sqrt{2}} = \dfrac{200\sqrt{2}}{\sqrt{2}} = 200$ V

The capacitive reactance $X_C$ is:
$X_C = \dfrac{1}{\omega C} = \dfrac{1}{100 \times 10^{-6}} = 10^4 \ \Omega$

The reading of an a.c. ammeter is the rms value of the current. Thus, the rms current $I_{rms}$ is:
$I_{rms} = \dfrac{V_{rms}}{X_C} = \dfrac{200}{10^4} = 20 \times 10^{-3}$ A

$I_{rms} = 20$ mA

Answer: $20$ mA

</details>

---

### Q14. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For series LCR circuit, the current is observed to lead the applied voltage. An additional capacitor $C_1$ when joined with capacitor C, makes the power factor of the circuit unity. The capacitor $C_1$ must be connected in

**Options:**

- **(A)** series with C and has magnitude $\dfrac{C}{(\omega^2 LC - 1)}$
- **(B)** series with C and has magnitude $\dfrac{(1 - \omega^2 LC)}{\omega^2 L}$
- **(C)** parallel with C and has magnitude $\dfrac{(1 - \omega^2 LC)}{\omega^2 L}$
- **(D)** parallel with C and has magnitude $\dfrac{C}{(\omega^2 LC - 1)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) parallel with C and has magnitude $\dfrac{(1 - \omega^2 LC)}{\omega^2 L}$**

**Detailed Solution:**

Since the current leads the applied voltage, the circuit is capacitive, which means $X_C > X_L$.

$\dfrac{1}{\omega C} > \omega L \Rightarrow C < \dfrac{1}{\omega^2 L}$

To make the power factor unity, the circuit must be in resonance. The new equivalent capacitance $C_{eq}$ must satisfy $X_{C_{eq}} = X_L$.

$\dfrac{1}{\omega C_{eq}} = \omega L \Rightarrow C_{eq} = \dfrac{1}{\omega^2 L}$

Since $C_{eq} > C$, the equivalent capacitance must be increased. Therefore, the additional capacitor $C_1$ must be connected in parallel with $C$.

$C_{eq} = C + C_1$

$C_1 = C_{eq} - C = \dfrac{1}{\omega^2 L} - C = \dfrac{1 - \omega^2 LC}{\omega^2 L}$

Answer: parallel with C and has magnitude $\dfrac{(1 - \omega^2 LC)}{\omega^2 L}$

</details>

---

### Q15. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

What is the value of inductance L for which the current is maximum in series LCR circuit with $C = 10$ $\mu$F and $\omega = 1000$/s ?

**Options:**

- **(A)** $100$ mH
- **(B)** $1$ mH
- **(C)** $10$ mH
- **(D)** $1000$ mH

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $100$ mH**

**Detailed Solution:**

In a series LCR circuit, the current is maximum at resonance.

At resonance, the inductive reactance is equal to the capacitive reactance:

$\omega L = \dfrac{1}{\omega C}$

$L = \dfrac{1}{\omega^2 C}$

Substituting the given values, $\omega = 1000 \text{ s}^{-1}$ and $C = 10 \mu\text{F} = 10 \times 10^{-6} \text{ F}$:

$L = \dfrac{1}{(1000)^2 \times 10 \times 10^{-6}}$

$L = \dfrac{1}{10^6 \times 10^{-5}}$

$L = \dfrac{1}{10} \text{ H}$

$L = 0.1 \text{ H} = 100 \text{ mH}$

Answer: $100$ mH

</details>

---

### Q16. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an LCR series circuit, a. c. voltage source is connected in series. When L is removed from the circuit, the phase difference between the voltage and the current is $\pi/3$. If instead C is removed, the phase difference is again $\pi/3$. The power factor of the circuit is $\left(\tan \dfrac{\pi}{3} = \sqrt{3}\right)$

**Options:**

- **(A)** $0.5$
- **(B)** $\dfrac{1}{\sqrt{2}}$
- **(C)** $1$
- **(D)** $\dfrac{\sqrt{3}}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1$**

**Detailed Solution:**

When L is removed, the circuit becomes an RC circuit. The phase difference $\phi_1$ is given by:

$\tan \phi_1 = \dfrac{X_C}{R}$

Given $\phi_1 = \dfrac{\pi}{3}$, we have $\dfrac{X_C}{R} = \tan \dfrac{\pi}{3} = \sqrt{3} \Rightarrow X_C = R\sqrt{3}$

When C is removed, the circuit becomes an RL circuit. The phase difference $\phi_2$ is given by:

$\tan \phi_2 = \dfrac{X_L}{R}$

Given $\phi_2 = \dfrac{\pi}{3}$, we have $\dfrac{X_L}{R} = \tan \dfrac{\pi}{3} = \sqrt{3} \Rightarrow X_L = R\sqrt{3}$

For the LCR series circuit, the net reactance is $X = X_L - X_C$.

Since $X_L = X_C = R\sqrt{3}$, we get $X = 0$.

The impedance of the circuit is $Z = \sqrt{R^2 + (X_L - X_C)^2} = R$.

The power factor of the LCR circuit is $\cos \phi = \dfrac{R}{Z} = \dfrac{R}{R} = 1$.

Answer: $1$

</details>

---

### Q17. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An inductor of self inductance $1$H connected in series with a resistor of $100\,\pi\,\Omega$ and an a.c. supply of $100\,\pi$V, $50$ Hz. Maximum current flowing in the circuit in ampere is

**Options:**

- **(A)** $0.5$
- **(B)** $1$
- **(C)** $1.5$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

The inductive reactance is given by $X_L = \omega L = 2\pi f L$.

Substituting the given values:

$X_L = 2\pi \times 50 \times 1 = 100\pi\,\Omega$

The impedance of the series LR circuit is:

$Z = \sqrt{R^2 + X_L^2}$

$Z = \sqrt{(100\pi)^2 + (100\pi)^2} = 100\pi\sqrt{2}\,\Omega$

The rms current in the circuit is:

$I_{rms} = \dfrac{V_{rms}}{Z} = \dfrac{100\pi}{100\pi\sqrt{2}} = \dfrac{1}{\sqrt{2}}$ A

The maximum (peak) current is:

$I_0 = I_{rms}\sqrt{2} = \dfrac{1}{\sqrt{2}} \times \sqrt{2} = 1$ A

Answer: $1$

</details>

---

### Q18. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit, r.m.s. value of current through the resistor $R$ is
<img style="width: 350px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/12_may_shift_2__q38_d1.png" />

**Options:**

- **(A)** $20$ A
- **(B)** $2$ A
- **(C)** $0.5$ A
- **(D)** $2\sqrt{2}$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2$ A**

**Detailed Solution:**

Given parameters of the series RLC circuit are:
$X_L = 200 \, \Omega$
$X_C = 100 \, \Omega$
$R = 100 \, \Omega$
$V_{rms} = 200\sqrt{2} \, \text{V}$

The total impedance $Z$ of the series circuit is given by:
$Z = \sqrt{R^2 + (X_L - X_C)^2}$

Substituting the given values:
$Z = \sqrt{100^2 + (200 - 100)^2}$
$Z = \sqrt{100^2 + 100^2}$
$Z = 100\sqrt{2} \, \Omega$

The r.m.s. current $I_{rms}$ in the circuit is:
$I_{rms} = \dfrac{V_{rms}}{Z}$

$I_{rms} = \dfrac{200\sqrt{2}}{100\sqrt{2}} = 2 \, \text{A}$

Since the components are in series, the current through the resistor $R$ is the same as the total current in the circuit, which is $2 \, \text{A}$.

Answer: $2$ A

</details>

---

### Q19. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An e.m.f. $e=E_0\cos\omega t$ is applied to a circuit containing L, C and R in series where $X_L=4R$ and $X_C=R$. The average power dissipated in the circuit is

**Options:**

- **(A)** $\dfrac{E_0^2}{20R}$
- **(B)** $\dfrac{E_0^2}{10R}$
- **(C)** $\dfrac{E_0^2}{5R}$
- **(D)** $\dfrac{E_0^2}{2R}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{E_0^2}{20R}$**

**Detailed Solution:**

The impedance of the series LCR circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$

Substituting $X_L = 4R$ and $X_C = R$:

$Z = \sqrt{R^2 + (4R - R)^2} = \sqrt{R^2 + 9R^2} = \sqrt{10}R$

The average power dissipated in the circuit is given by $P_{avg} = I_{rms}^2 R$

Since $I_{rms} = \dfrac{E_{rms}}{Z} = \dfrac{E_0}{\sqrt{2}Z}$, we have:

$P_{avg} = \left(\dfrac{E_0}{\sqrt{2}Z}\right)^2 R = \dfrac{E_0^2}{2Z^2} R$

Substituting $Z^2 = 10R^2$:

$P_{avg} = \dfrac{E_0^2}{2(10R^2)} R = \dfrac{E_0^2}{20R}$

Answer: $\dfrac{E_0^2}{20R}$

</details>

---

### Q20. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a series LCR circuit, the inductance $L=20$ mH, capacitor $C=2\,\mu$F and resistance $R=100$ ohm. The frequency at which resonance occurs is

**Options:**

- **(A)** $\dfrac{(10)^2}{2\pi}$
- **(B)** $\dfrac{(10)^3}{3\pi}$
- **(C)** $\dfrac{(10)^4}{4\pi}$
- **(D)** $\dfrac{10}{\pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{(10)^4}{4\pi}$**

**Detailed Solution:**

The resonant frequency of a series LCR circuit is given by $f = \dfrac{1}{2\pi \sqrt{LC}}$.

Substituting the given values $L = 20 \times 10^{-3}$ H and $C = 2 \times 10^{-6}$ F:

$f = \dfrac{1}{2\pi \sqrt{20 \times 10^{-3} \times 2 \times 10^{-6}}}$

$f = \dfrac{1}{2\pi \sqrt{40 \times 10^{-9}}}$

$f = \dfrac{1}{2\pi \sqrt{4 \times 10^{-8}}}$

$f = \dfrac{1}{2\pi \times 2 \times 10^{-4}}$

$f = \dfrac{10^4}{4\pi}$ Hz.

Answer: $\dfrac{(10)^4}{4\pi}$

</details>

---

### Q21. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an LCR series circuit an alternating voltage source of frequency $F$ is connected. The current leads the voltage by $45^\circ$. The value of $L$ is

**Options:**

- **(A)** $\dfrac{1 + 2\pi FCR}{2\pi FC}$
- **(B)** $\dfrac{1 + 2\pi FCR}{4\pi^2 F^2C}$
- **(C)** $\dfrac{1 - 2\pi FCR}{4\pi^2 F^2C}$
- **(D)** $\dfrac{1 + 2\pi FR}{4\pi^2 F^2C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1 - 2\pi FCR}{4\pi^2 F^2C}$**

**Detailed Solution:**

In an LCR series circuit, the phase difference $\phi$ between the voltage and current when the current leads the voltage is given by $\tan \phi = \dfrac{X_C - X_L}{R}$.

Given that the current leads the voltage by $45^\circ$, we have $\phi = 45^\circ$.

$\tan 45^\circ = \dfrac{X_C - X_L}{R}$

$1 = \dfrac{\dfrac{1}{2\pi FC} - 2\pi FL}{R}$

$R = \dfrac{1}{2\pi FC} - 2\pi FL$

$2\pi FL = \dfrac{1}{2\pi FC} - R$

$2\pi FL = \dfrac{1 - 2\pi FCR}{2\pi FC}$

$L = \dfrac{1 - 2\pi FCR}{4\pi^2 F^2C}$

Answer: $\dfrac{1 - 2\pi FCR}{4\pi^2 F^2C}$

</details>

---

### Q22. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given below are the two circuits, choose the correct option.
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/19_april_shift_2__q38_d1_v2.png" />

**Options:**

- **(A)** At resonance, current in (B) is less than that in (A)
- **(B)** The r.m.s. current in (B) can be larger than that in (A)
- **(C)** The r.m.s. current in (A) is always equal to that in (B)
- **(D)** The r.m.s. current in (B) can never be larger than that in (A)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The r.m.s. current in (B) can never be larger than that in (A)**

**Detailed Solution:**

For circuit (A), the impedance is purely resistive:

$Z_A = R = 30\ \Omega$

The r.m.s. current in circuit (A) is:

$I_A = \dfrac{V_{rms}}{Z_A} = \dfrac{V_{rms}}{R}$

For circuit (B), which is a series LCR circuit, the impedance is given by:

$Z_B = \sqrt{R^2 + (X_L - X_C)^2}$

Since the square of any real number is non-negative, $(X_L - X_C)^2 \ge 0$. Therefore, the impedance of circuit (B) will always be greater than or equal to the resistance $R$:

$Z_B \ge R$

$Z_B \ge Z_A$

The r.m.s. current in circuit (B) is:

$I_B = \dfrac{V_{rms}}{Z_B}$

Since $V_{rms}$ is the same for both circuits ($210\text{ V}$) and $Z_B \ge Z_A$, it follows that:

$I_B \le I_A$

At resonance, $X_L = X_C$, which gives $Z_B = R$ and $I_B = I_A$. For all other conditions, $Z_B > R$ and $I_B < I_A$.

Thus, the r.m.s. current in (B) can never be larger than that in (A).

Answer: The r.m.s. current in (B) can never be larger than that in (A)

</details>

---

### Q23. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a L-R circuit of 4 mH inductance and $3\ \Omega$ resistance, e.m.f. $E = \cos(1000t)$ V is applied. The amplitude of current is

**Options:**

- **(A)** $1.6$ A
- **(B)** $1$ A
- **(C)** $0.2$ A
- **(D)** $0.4$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.2$ A**

**Detailed Solution:**

Given $L = 4 \times 10^{-3}$ H, $R = 3\ \Omega$, and $E = \cos(1000t)$ V.

The peak voltage is $E_0 = 1$ V and the angular frequency is $\omega = 1000$ rad/s.

The inductive reactance is $X_L = \omega L = 1000 \times 4 \times 10^{-3} = 4\ \Omega$.

The impedance of the L-R circuit is $Z = \sqrt{R^2 + X_L^2} = \sqrt{3^2 + 4^2} = 5\ \Omega$.

The amplitude of the current is $I_0 = \dfrac{E_0}{Z} = \dfrac{1}{5} = 0.2$ A.

Answer: $0.2$ A

</details>

---

### Q24. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a series LCR circuit, the voltage across R is $100$ V, $R = 1\,\text{K}\,\Omega$ and $C = 2\,\mu\text{F}$. The angular frequency $\omega$ is $200$ rad s$^{-1}$. At resonance, the voltage across '$L$' is

**Options:**

- **(A)** $150$ V
- **(B)** $200$ V
- **(C)** $250$ V
- **(D)** $300$ V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $250$ V**

**Detailed Solution:**

The current in the series LCR circuit is given by $I = \dfrac{V_R}{R}$.

Substituting the given values:

$I = \dfrac{100}{1000} = 0.1$ A

The capacitive reactance is $X_C = \dfrac{1}{\omega C}$.

$X_C = \dfrac{1}{200 \times 2 \times 10^{-6}} = \dfrac{10^6}{400} = 2500 \, \Omega$

The voltage across the capacitor is $V_C = I X_C$.

$V_C = 0.1 \times 2500 = 250$ V

At resonance, the inductive reactance equals the capacitive reactance ($X_L = X_C$), so the voltage across the inductor equals the voltage across the capacitor.

$V_L = V_C = 250$ V

Answer: $250$ V

</details>

---

### Q25. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Which graph shows the correct variation of r.m.s. current '$i$' with frequency '$f$' of a.c. in case of series resonant circuit ?
<img style="width: 500px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/19_april_shift_1__q43_d1.png" />

**Options:**

- **(A)** $(R)$
- **(B)** $(P)$
- **(C)** $(S)$
- **(D)** $(Q)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(P)$**

**Detailed Solution:**

In a series LCR circuit, the impedance is given by:

$Z = \sqrt{R^2 + \left(X_L - X_C\right)^2} = \sqrt{R^2 + \left(2\pi f L - \dfrac{1}{2\pi f C}\right)^2}$

The r.m.s. current is:

$i = \dfrac{V_{\text{rms}}}{Z}$

At the resonant frequency $f_r = \dfrac{1}{2\pi\sqrt{LC}}$, the inductive reactance equals the capacitive reactance ($X_L = X_C$). At this point, the impedance $Z$ is minimum ($Z = R$) and the current $i$ is maximum.

For frequencies $f < f_r$, $Z$ is large and $i$ is small. As $f$ increases towards $f_r$, $Z$ decreases and $i$ increases.
For frequencies $f > f_r$, $Z$ increases again and $i$ decreases.

Thus, the graph of current $i$ versus frequency $f$ is a bell-shaped curve with a peak at the resonant frequency. Graph (P) correctly represents this variation.

Answer: $(P)$

</details>

---

### Q26. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When an inductance '$L$' and resistor '$R$' are connected in series to $25$V, $50$ Hz supply, a current of $0.5$ A flows in the circuit. The current lags behind in phase from applied voltage by $\left(\dfrac{\pi}{3}\right)$ radian. The value of R is $\left(\cos 60^\circ = \dfrac{1}{2}\right)$

**Options:**

- **(A)** $20\,\Omega$
- **(B)** $25\,\Omega$
- **(C)** $40\,\Omega$
- **(D)** $50\,\Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $25\,\Omega$**

**Detailed Solution:**

The impedance of the LR series circuit is given by:

$Z = \dfrac{V}{I}$

Substituting the given values:

$Z = \dfrac{25}{0.5} = 50 \, \Omega$

The power factor of the circuit is related to the resistance and impedance by:

$\cos \phi = \dfrac{R}{Z}$

Given that the current lags the voltage by $\phi = \dfrac{\pi}{3}$ radian ($60^\circ$):

$R = Z \cos \phi$

$R = 50 \times \cos 60^\circ$

$R = 50 \times \dfrac{1}{2} = 25 \, \Omega$

Answer: $25\,\Omega$

</details>

---

### Q27. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown charge q varies with time t as $q = t^2 - 5$, where q is in coulomb and t is in second. At time $t = 3$ second, voltage $V_{AB}$ in volt will be
<img style="width: 350px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/19_april_shift_1__q41_d1.png" />

**Options:**

- **(A)** $8$
- **(B)** $12$
- **(C)** $14$
- **(D)** $18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $14$**

**Detailed Solution:**

Given charge on the capacitor, $q = t^2 - 5$.

The current $i$ in the circuit is the rate of flow of charge:
$i = \dfrac{dq}{dt} = \dfrac{d}{dt}(t^2 - 5) = 2t$

The rate of change of current is:
$\dfrac{di}{dt} = \dfrac{d}{dt}(2t) = 2 \text{ A/s}$

At time $t = 3 \text{ s}$:
Charge, $q = (3)^2 - 5 = 4 \text{ C}$
Current, $i = 2(3) = 6 \text{ A}$
Rate of change of current, $\dfrac{di}{dt} = 2 \text{ A/s}$

Applying Kirchhoff's Voltage Law from point A to point B:
$V_A - V_C - V_L - V_R = V_B$
$V_A - \dfrac{q}{C} - L\dfrac{di}{dt} - iR = V_B$
$V_A - V_B = \dfrac{q}{C} + L\dfrac{di}{dt} + iR$

Substituting the given values ($C = 4 \text{ F}$, $L = 0.5 \text{ H}$, $R = 2 \ \Omega$):
$V_{AB} = \dfrac{4}{4} + 0.5(2) + 6(2)$
$V_{AB} = 1 + 1 + 12 = 14 \text{ V}$

</details>

---

### Q28. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR circuit $R = 10\,\Omega$ and impedance is $30\,\Omega$. An r.m.s. voltage $210$ V, is applied across the circuit. The true power consumed in AC circuit is

**Options:**

- **(A)** $360$ W
- **(B)** $420$ W
- **(C)** $490$ W
- **(D)** $600$ W

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $490$ W**

**Detailed Solution:**

Given $R = 10 \, \Omega$, $Z = 30 \, \Omega$, and $V_{\text{rms}} = 210$ V.

The rms current in the circuit is given by:

$I_{\text{rms}} = \dfrac{V_{\text{rms}}}{Z} = \dfrac{210}{30} = 7$ A

The true power consumed in the AC circuit is:

$P = I_{\text{rms}}^2 R$

Substituting the values:

$P = (7)^2 \times 10 = 49 \times 10 = 490$ W

Answer: $490$ W

</details>

---

### Q29. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For a series LCR circuit inductive reactance $X_L$ is equal to resistance $R$ and also equal to twice the capacitive reactance $X_C$. The impedance of the circuit and the phase difference between voltage V and current i are respectively

**Options:**

- **(A)** $\sqrt{5}R,\ \tan^{-1}\left(\dfrac{1}{2}\right)$
- **(B)** $\sqrt{5}R,\ \tan^{-1}(2)$
- **(C)** $\dfrac{\sqrt{5}R}{2},\ \tan^{-1}\left(\dfrac{1}{2}\right)$
- **(D)** $\dfrac{\sqrt{5}R}{2},\ \tan^{-1}(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{\sqrt{5}R}{2},\ \tan^{-1}\left(\dfrac{1}{2}\right)$**

**Detailed Solution:**

Given $X_L = R$ and $X_L = 2X_C$.

This gives $X_C = \dfrac{R}{2}$.

The impedance of the series LCR circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

Substituting the values:

$Z = \sqrt{R^2 + \left(R - \dfrac{R}{2}\right)^2} = \sqrt{R^2 + \dfrac{R^2}{4}} = \dfrac{\sqrt{5}R}{2}$.

The phase difference $\phi$ between voltage and current is given by $\tan \phi = \dfrac{X_L - X_C}{R}$.

$\tan \phi = \dfrac{R - \dfrac{R}{2}}{R} = \dfrac{1}{2}$.

$\phi = \tan^{-1}\left(\dfrac{1}{2}\right)$.

Answer: $\dfrac{\sqrt{5}R}{2},\ \tan^{-1}\left(\dfrac{1}{2}\right)$

</details>

---

### Q30. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An alternating voltage $e = 150\sqrt{2}\sin 100t$ volt is applied to a capacitor of capacity $2\ \mu\text{F}$. The root mean square value of current in the circuit is

**Options:**

- **(A)** $300$ mA
- **(B)** $150$ mA
- **(C)** $30$ mA
- **(D)** $15$ mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $30$ mA**

**Detailed Solution:**

Given alternating voltage $e = 150\sqrt{2}\sin(100t)$ V.

Comparing with the standard equation $e = E_0\sin(\omega t)$, we get:

Peak voltage $E_0 = 150\sqrt{2}$ V

Angular frequency $\omega = 100$ rad/s

The root mean square voltage is:

$E_{\text{rms}} = \dfrac{E_0}{\sqrt{2}} = \dfrac{150\sqrt{2}}{\sqrt{2}} = 150$ V

The capacitive reactance is:

$X_C = \dfrac{1}{\omega C} = \dfrac{1}{100 \times 2 \times 10^{-6}} = 5000\ \Omega$

The root mean square current in the circuit is:

$I_{\text{rms}} = \dfrac{E_{\text{rms}}}{X_C} = \dfrac{150}{5000} = 0.03$ A

$I_{\text{rms}} = 30$ mA

Answer: $30$ mA

</details>

---

### Q31. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an LCR circuit at resonance, the a.c. source current is
A) maximum in a series LCR circuit only.
B) maximum in a parallel LCR circuit only.
C) maximum in both series and parallel LCR circuits.
D) minimum in both series and parallel LCR circuits.
The correct answer is

**Options:**

- **(A)** B
- **(B)** D
- **(C)** C
- **(D)** A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) A**

**Detailed Solution:**

In a series LCR circuit, the impedance is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

At resonance, $X_L = X_C$, which makes the impedance minimum ($Z = R$).

Since $I = \dfrac{V}{Z}$, the current is maximum in a series LCR circuit at resonance.

In a parallel LCR circuit, the admittance is given by $Y = \sqrt{\left(\dfrac{1}{R}\right)^2 + \left(\dfrac{1}{X_C} - \dfrac{1}{X_L}\right)^2}$.

At resonance, $X_L = X_C$, which makes the admittance minimum ($Y = \dfrac{1}{R}$) and the impedance maximum.

Since $I = V Y$, the current is minimum in a parallel LCR circuit at resonance.

Thus, the a.c. source current is maximum in a series LCR circuit only.

Answer: A

</details>

---

### Q32. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A series combination of resistor 'R' and capacitor 'C' is connected to an a.c. source of angular frequency '$\omega$'. Keeping the voltage same, if the frequency is changed to $\left(\dfrac{\omega}{3}\right)$ the current becomes half of the original current. Then the ratio of capacitive reactance and resistance is

**Options:**

- **(A)** $\sqrt{6}$
- **(B)** $\sqrt{0.3}$
- **(C)** $\sqrt{3}$
- **(D)** $\sqrt{0.6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{0.6}$**

**Detailed Solution:**

Initial current $I_1 = \dfrac{V}{\sqrt{R^2 + X_C^2}}$ where $X_C = \dfrac{1}{\omega C}$

When frequency is changed to $\dfrac{\omega}{3}$, the new capacitive reactance becomes $X_C' = \dfrac{1}{(\omega/3)C} = 3X_C$

New current $I_2 = \dfrac{V}{\sqrt{R^2 + (3X_C)^2}} = \dfrac{V}{\sqrt{R^2 + 9X_C^2}}$

Given $I_2 = \dfrac{I_1}{2}$

$\dfrac{V}{\sqrt{R^2 + 9X_C^2}} = \dfrac{1}{2} \dfrac{V}{\sqrt{R^2 + X_C^2}}$

Squaring both sides:

$R^2 + 9X_C^2 = 4(R^2 + X_C^2)$

$R^2 + 9X_C^2 = 4R^2 + 4X_C^2$

$5X_C^2 = 3R^2$

$\dfrac{X_C^2}{R^2} = \dfrac{3}{5} = 0.6$

$\dfrac{X_C}{R} = \sqrt{0.6}$

Answer: $\sqrt{0.6}$

</details>

---

### Q33. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the series LCR circuit shown in figure the impedance is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_2__q43_d1.png" />

**Options:**

- **(A)** $300\,\Omega$
- **(B)** $500\,\Omega$
- **(C)** $700\,\Omega$
- **(D)** $900\,\Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $500\,\Omega$**

**Detailed Solution:**

Given parameters from the circuit:
Resistance, $R = 300\ \Omega$
Inductance, $L = 1\text{ H}$
Capacitance, $C = 20\ \mu\text{F} = 20 \times 10^{-6}\text{ F}$
Frequency of the AC source, $f = \dfrac{50}{\pi}\text{ Hz}$

The angular frequency $\omega$ is given by:
$\omega = 2\pi f = 2\pi \left(\dfrac{50}{\pi}\right) = 100\text{ rad/s}$

Inductive reactance, $X_L$:
$X_L = \omega L = 100 \times 1 = 100\ \Omega$

Capacitive reactance, $X_C$:
$X_C = \dfrac{1}{\omega C} = \dfrac{1}{100 \times 20 \times 10^{-6}} = \dfrac{1}{2 \times 10^{-3}} = 500\ \Omega$

The impedance $Z$ of the series LCR circuit is:
$Z = \sqrt{R^2 + (X_C - X_L)^2}$

Substituting the values:
$Z = \sqrt{300^2 + (500 - 100)^2}$
$Z = \sqrt{300^2 + 400^2}$
$Z = \sqrt{90000 + 160000}$
$Z = \sqrt{250000} = 500\ \Omega$

Answer: $500\,\Omega$

</details>

---

### Q34. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an LCR series circuit, the potential difference across the terminals of the inductor, capacitor and resistor is 60 V, 30 V and 40 V respectively. Then supply voltage will be equal to

**Options:**

- **(A)** $10$ V
- **(B)** $50$ V
- **(C)** $70$ V
- **(D)** $130$ V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $50$ V**

**Detailed Solution:**

Given:

$V_L = 60$ V

$V_C = 30$ V

$V_R = 40$ V

The supply voltage $V$ in an LCR series circuit is given by the phasor sum of the voltages:

$V = \sqrt{V_R^2 + (V_L - V_C)^2}$

Substituting the given values:

$V = \sqrt{40^2 + (60 - 30)^2}$

$V = \sqrt{40^2 + 30^2}$

$V = \sqrt{1600 + 900}$

$V = \sqrt{2500} = 50$ V

</details>

---

### Q35. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An a.c. source is applied to a series LR circuit with $X_L = 3R$ and power factor is $X_1$. Now a capacitor with $X_c = R$ is added in series to LR circuit and power factor is $X_2$. The ratio $X_1$ to $X_2$ is

**Options:**

- **(A)** $2 : 1$
- **(B)** $1 : 2$
- **(C)** $\sqrt{2} : 1$
- **(D)** $1 : \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1 : \sqrt{2}$**

**Detailed Solution:**

For the series LR circuit, the impedance is $Z_1 = \sqrt{R^2 + X_L^2}$.

Given $X_L = 3R$, $Z_1 = \sqrt{R^2 + (3R)^2} = \sqrt{10}R$.

The power factor $X_1 = \dfrac{R}{Z_1} = \dfrac{R}{\sqrt{10}R} = \dfrac{1}{\sqrt{10}}$.

When a capacitor with $X_C = R$ is added in series, the new impedance is $Z_2 = \sqrt{R^2 + (X_L - X_C)^2}$.

Substituting the values, $Z_2 = \sqrt{R^2 + (3R - R)^2} = \sqrt{R^2 + 4R^2} = \sqrt{5}R$.

The new power factor $X_2 = \dfrac{R}{Z_2} = \dfrac{R}{\sqrt{5}R} = \dfrac{1}{\sqrt{5}}$.

The ratio $\dfrac{X_1}{X_2} = \dfrac{1/\sqrt{10}}{1/\sqrt{5}} = \dfrac{\sqrt{5}}{\sqrt{10}} = \dfrac{1}{\sqrt{2}}$.

Thus, $X_1 : X_2 = 1 : \sqrt{2}$.

Answer: $1 : \sqrt{2}$

</details>

---

### Q36. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In an a.c. circuit, a resistance R is connected in series with an inductance 'L'. If phase angle between voltage and current is $45^\circ$, the value of inductive reactance will be
($\sin 45^\circ = \dfrac{1}{\sqrt{2}} = \cos 45^\circ$)

**Options:**

- **(A)** $2R$
- **(B)** $R$
- **(C)** $\sqrt{2}R$
- **(D)** $\dfrac{1}{\sqrt{2}}R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $R$**

**Detailed Solution:**

In a series RL circuit, the phase angle $\phi$ between the voltage and the current is given by the relation:

$\tan \phi = \dfrac{X_L}{R}$

Given that the phase angle $\phi = 45^\circ$:

$\tan 45^\circ = \dfrac{X_L}{R}$

Since $\tan 45^\circ = 1$:

$1 = \dfrac{X_L}{R}$

$X_L = R$

The inductive reactance is equal to the resistance $R$.

Answer: $R$

</details>

---

### Q37. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In LCR circuit, at a particular angular frequency the capacitive reactance and inductive reactance is same. If the angular frequency is doubled, the ratio of the reactance of the capacitor to that of the inductor will be

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $1$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{4}$**

**Detailed Solution:**

Let the initial angular frequency be $\omega_0$.

At $\omega_0$, the capacitive reactance $X_C$ and inductive reactance $X_L$ are equal:

$X_C = X_L \Rightarrow \dfrac{1}{\omega_0 C} = \omega_0 L$

When the angular frequency is doubled, the new angular frequency is $\omega = 2\omega_0$.

The new capacitive reactance is:

$X_C' = \dfrac{1}{\omega C} = \dfrac{1}{2\omega_0 C} = \dfrac{X_C}{2}$

The new inductive reactance is:

$X_L' = \omega L = 2\omega_0 L = 2X_L$

The ratio of the new capacitive reactance to the new inductive reactance is:

$\dfrac{X_C'}{X_L'} = \dfrac{\dfrac{X_C}{2}}{2X_L} = \dfrac{1}{4} \left(\dfrac{X_C}{X_L}\right)$

Since $X_C = X_L$, the ratio becomes $\dfrac{1}{4}$.

</details>

---

### Q38. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an a.c. circuit with pure capacitance 'C' and a.c. source $E = E_0\sin\omega t$, the equation of instantaneous current is given by

**Options:**

- **(A)** $I = E_0\,\omega C \cdot \sin(\omega t)$
- **(B)** $I = E_0\omega C\sin\left(\omega t + \dfrac{\pi}{2}\right)$
- **(C)** $I = \dfrac{E_0}{\omega C}\sin(\omega t)$
- **(D)** $I = \dfrac{E_0}{\omega C}\sin\left(\omega t + \dfrac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $I = E_0\omega C\sin\left(\omega t + \dfrac{\pi}{2}\right)$**

**Detailed Solution:**

The instantaneous voltage across the capacitor is given by $E = E_0\sin\omega t$.

The charge on the capacitor at any instant is $q = CE = CE_0\sin\omega t$.

The instantaneous current $I$ is the rate of flow of charge, given by $I = \dfrac{dq}{dt}$.

Differentiating $q$ with respect to $t$, we get:

$I = \dfrac{d}{dt}(CE_0\sin\omega t) = E_0\omega C\cos\omega t$

Using the trigonometric identity $\cos\theta = \sin\left(\theta + \dfrac{\pi}{2}\right)$, the current can be written as:

$I = E_0\omega C\sin\left(\omega t + \dfrac{\pi}{2}\right)$

Answer: $I = E_0\omega C\sin\left(\omega t + \dfrac{\pi}{2}\right)$

</details>

---

### Q39. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The resistor '$R$' inductance '$L$' and capacitance '$C$' are connected in series with an a.c. source. When 'L' is removed from the circuit, the phase difference between voltage and current in the circuit is $\dfrac{\pi}{3}$. If instead, C is removed from the circuit, the phase difference is again $\dfrac{\pi}{3}$. The power factor of the circuit is

**Options:**

- **(A)** $\dfrac{\sqrt{3}}{2}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{\sqrt{2}}$
- **(D)** $1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1$**

**Detailed Solution:**

When $L$ is removed, the circuit becomes an $RC$ circuit. The phase difference is $\phi = \dfrac{\pi}{3}$.

$\tan \phi = \dfrac{X_C}{R} \Rightarrow \tan\left(\dfrac{\pi}{3}\right) = \dfrac{X_C}{R} \Rightarrow X_C = R\sqrt{3}$

When $C$ is removed, the circuit becomes an $RL$ circuit. The phase difference is again $\phi = \dfrac{\pi}{3}$.

$\tan \phi = \dfrac{X_L}{R} \Rightarrow \tan\left(\dfrac{\pi}{3}\right) = \dfrac{X_L}{R} \Rightarrow X_L = R\sqrt{3}$

In the series $RLC$ circuit, the net reactance is $X = X_L - X_C$.

Since $X_L = X_C = R\sqrt{3}$, we have $X = 0$.

The impedance of the circuit is $Z = \sqrt{R^2 + (X_L - X_C)^2} = R$.

The power factor of the circuit is $\cos \phi = \dfrac{R}{Z} = \dfrac{R}{R} = 1$.

Answer: $1$

</details>

---

### Q40. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The LC series resonant circuit produces a resonant frequency '$f$'. If L is tripled and 'C' is increased by 3C, the resonant frequency will be

**Options:**

- **(A)** $\dfrac{f}{3}$
- **(B)** $\dfrac{f}{2\sqrt{3}}$
- **(C)** $6f$
- **(D)** $\dfrac{f}{3\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{f}{2\sqrt{3}}$**

**Detailed Solution:**

The resonant frequency of an LC series circuit is given by $f = \dfrac{1}{2\pi\sqrt{LC}}$.

Given that the inductance $L$ is tripled, the new inductance is $L' = 3L$.

The capacitance $C$ is increased by $3C$, so the new capacitance is $C' = C + 3C = 4C$.

The new resonant frequency $f'$ is given by:

$f' = \dfrac{1}{2\pi\sqrt{L'C'}}$

Substituting the values of $L'$ and $C'$:

$f' = \dfrac{1}{2\pi\sqrt{(3L)(4C)}} = \dfrac{1}{2\pi\sqrt{12LC}}$

$f' = \dfrac{1}{2\sqrt{3}} \left( \dfrac{1}{2\pi\sqrt{LC}} \right)$

$f' = \dfrac{f}{2\sqrt{3}}$

Answer: $\dfrac{f}{2\sqrt{3}}$

</details>

---

### Q41. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In LCR series circuit at resonance

**Options:**

- **(A)** the current is minimum.
- **(B)** the impedance is maximum.
- **(C)** the current leads the voltage by $\dfrac{\pi}{2}$
- **(D)** the current and voltage are in phase.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) the current and voltage are in phase.**

**Detailed Solution:**

In an LCR series circuit, the impedance is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

At resonance, the inductive reactance is equal to the capacitive reactance, i.e., $X_L = X_C$.

Substituting this in the impedance formula, we get $Z = R$. This is the minimum possible impedance, which results in maximum current.

The phase difference $\phi$ between the voltage and current is given by $\tan \phi = \dfrac{X_L - X_C}{R}$.

Since $X_L = X_C$, $\tan \phi = 0 \Rightarrow \phi = 0$.

Thus, the current and voltage are in phase.

Answer: the current and voltage are in phase.

</details>

---

### Q42. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Series LCR circuit containing an a.c. source of 100V has a inductor and a capacitor of reactance $24\ \Omega$ and $16\ \Omega$ respectively. If a resistance of $6\ \Omega$ is connected in series, then the potential difference across the series combination of inductor and capacitor only is

**Options:**

- **(A)** $80\text{V}$
- **(B)** $8\text{V}$
- **(C)** $40\text{V}$
- **(D)** $20\text{V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $80\text{V}$**

**Detailed Solution:**

Given $V = 100\text{V}$, $X_L = 24\ \Omega$, $X_C = 16\ \Omega$, and $R = 6\ \Omega$.

The net reactance of the circuit is $X = X_L - X_C = 24 - 16 = 8\ \Omega$.

The impedance of the series LCR circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

Substituting the values, $Z = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = 10\ \Omega$.

The rms current in the circuit is $I = \dfrac{V}{Z} = \dfrac{100}{10} = 10\text{A}$.

The potential difference across the series combination of the inductor and capacitor is $V_{LC} = I \times |X_L - X_C|$.

$V_{LC} = 10 \times 8 = 80\text{V}$.

</details>

---

### Q43. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An inductor of inductance $2\ \mu\text{H}$ is connected in series with a resistance, a variable capacitor and an a.c. source of 10 kHz. The value of capacitance for which maximum current is drawn in to the circuit is $\dfrac{1}{x}\ \text{F}$, where the value of x is (Take $\pi^2 = 10$)

**Options:**

- **(A)** $8000$
- **(B)** $600$
- **(C)** $400$
- **(D)** $1600$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8000$**

**Detailed Solution:**

Maximum current is drawn in a series LCR circuit at resonance.

At resonance, the inductive reactance equals the capacitive reactance, so $\omega L = \dfrac{1}{\omega C}$.

$C = \dfrac{1}{\omega^2 L} = \dfrac{1}{(2\pi f)^2 L}$

Given $L = 2\ \mu\text{H} = 2 \times 10^{-6}\ \text{H}$ and $f = 10\ \text{kHz} = 10^4\ \text{Hz}$.

$C = \dfrac{1}{4\pi^2 f^2 L}$

Substituting the values and using $\pi^2 = 10$:

$C = \dfrac{1}{4 \times 10 \times (10^4)^2 \times 2 \times 10^{-6}}$

$C = \dfrac{1}{40 \times 10^8 \times 2 \times 10^{-6}}$

$C = \dfrac{1}{80 \times 10^2} = \dfrac{1}{8000}\ \text{F}$

Comparing with $C = \dfrac{1}{x}\ \text{F}$, we get $x = 8000$.

Answer: $8000$

</details>

---

### Q44. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When a capacitor is connected in series LR circuit, the alternating current flowing in the circuit

**Options:**

- **(A)** increases
- **(B)** decreases
- **(C)** remains constant
- **(D)** is zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increases**

**Detailed Solution:**

The impedance of a series LR circuit is given by $Z_1 = \sqrt{R^2 + X_L^2}$.

When a capacitor is connected in series with the LR circuit, it becomes an LCR circuit. The new impedance is given by $Z_2 = \sqrt{R^2 + (X_L - X_C)^2}$.

The net reactance of the circuit changes from $X_L$ to $|X_L - X_C|$. Since the capacitive reactance $X_C$ opposes the inductive reactance $X_L$, the net reactance generally decreases.

As a result, the overall impedance of the circuit decreases ($Z_2 < Z_1$).

Since the alternating current is inversely proportional to the impedance ($I = \dfrac{V}{Z}$), a decrease in impedance leads to an increase in the current flowing through the circuit.

Answer: increases

</details>

---

### Q45. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

With gradual increase in frequency of an a.c. supply, the impedance of an LCR series circuit

**Options:**

- **(A)** increases
- **(B)** decreases
- **(C)** remains constant
- **(D)** first decreases, becomes minimum and then increases

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) first decreases, becomes minimum and then increases**

**Detailed Solution:**

The impedance of an LCR series circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$

where $X_L = 2\pi f L$ and $X_C = \dfrac{1}{2\pi f C}$.

At low frequencies, $X_C > X_L$, so the impedance is high.

As the frequency $f$ increases, $X_C$ decreases and $X_L$ increases, which reduces the magnitude of $(X_L - X_C)$. Thus, the impedance decreases.

At the resonant frequency $f = \dfrac{1}{2\pi\sqrt{LC}}$, $X_L = X_C$, and the impedance becomes minimum, $Z = R$.

With a further increase in frequency, $X_L > X_C$, and the magnitude of $(X_L - X_C)$ increases, causing the impedance to increase.

Therefore, the impedance first decreases, becomes minimum, and then increases.

Answer: first decreases, becomes minimum and then increases

</details>

---

### Q46. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An electric lamp connected in series with a capacitor and an a.c source is glowing with certain brightness. On reducing the frequency of source the brightness of the lamp

**Options:**

- **(A)** is increased
- **(B)** is reduced
- **(C)** remain the same
- **(D)** becomes zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is reduced**

**Detailed Solution:**

The impedance of the series RC circuit is given by $Z = \sqrt{R^2 + X_C^2}$, where $X_C = \dfrac{1}{2\pi f C}$.

When the frequency $f$ of the AC source is reduced, the capacitive reactance $X_C$ increases.

As a result, the total impedance $Z$ of the circuit increases.

The current in the circuit is $I = \dfrac{V}{Z}$. Since $Z$ increases, the current $I$ decreases.

The brightness of the lamp is proportional to the power dissipated, $P = I^2 R$. With a decrease in current, the power dissipated decreases, and hence the brightness of the lamp is reduced.

Answer: is reduced

</details>

---

### Q47. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A series resonant circuit consists of an inductor 'L' and capacitor 'C' which produces resonant frequency 'f'. If 'L' is increased by '2L' and 'C' is changed to '9C' the resonant frequency will be

**Options:**

- **(A)** $\dfrac{f}{3}$
- **(B)** $\dfrac{f}{2}$
- **(C)** $\dfrac{f}{2\sqrt{2}}$
- **(D)** $\dfrac{f}{3\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{f}{3\sqrt{3}}$**

**Detailed Solution:**

The resonant frequency of a series L-C circuit is given by:

$f = \dfrac{1}{2\pi\sqrt{LC}}$

Given that the inductance is increased by $2L$, the new inductance is:

$L' = L + 2L = 3L$

The capacitance is changed to $9C$, so the new capacitance is:

$C' = 9C$

The new resonant frequency $f'$ is:

$f' = \dfrac{1}{2\pi\sqrt{L'C'}}$

Substituting the values of $L'$ and $C'$:

$f' = \dfrac{1}{2\pi\sqrt{(3L)(9C)}}$

$f' = \dfrac{1}{2\pi\sqrt{27LC}}$

$f' = \dfrac{1}{3\sqrt{3}} \left( \dfrac{1}{2\pi\sqrt{LC}} \right)$

$f' = \dfrac{f}{3\sqrt{3}}$

Answer: $\dfrac{f}{3\sqrt{3}}$

</details>

---

### Q48. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an LCR series circuit, at resonance,

**Options:**

- **(A)** the impedance is maximum
- **(B)** the current is minimum
- **(C)** the current leads the voltage by $\dfrac{\pi}{2}$
- **(D)** the current and voltage are in phase

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) the current and voltage are in phase**

**Detailed Solution:**

In an LCR series circuit, the impedance is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

At resonance, the inductive reactance is equal to the capacitive reactance, i.e., $X_L = X_C$.

Substituting this in the impedance formula, we get $Z = R$, which is the minimum impedance.

The phase difference $\phi$ between the voltage and current is given by $\tan \phi = \dfrac{X_L - X_C}{R}$.

Since $X_L = X_C$, $\tan \phi = 0 \Rightarrow \phi = 0$.

Therefore, the current and voltage are in phase.

Answer: the current and voltage are in phase

</details>

---

### Q49. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A series LCR circuit is connected to an a.c. source of $220$ V, $50$ Hz. The circuit contains a resistance $R = 80\,\Omega$, an inductor of inductive reactance $70\,\Omega$ and capacitor of capacitive reactance $130\,\Omega$. The power factor of the circuit is $\dfrac{x}{10}$. The value of x is

**Options:**

- **(A)** $8$
- **(B)** $6$
- **(C)** $4$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $8$**

**Detailed Solution:**

The impedance of the series LCR circuit is given by

$Z = \sqrt{R^2 + (X_C - X_L)^2}$

Substituting the given values:

$Z = \sqrt{80^2 + (130 - 70)^2}$

$Z = \sqrt{80^2 + 60^2}$

$Z = \sqrt{6400 + 3600} = \sqrt{10000} = 100\,\Omega$

The power factor of the circuit is

$\cos \phi = \dfrac{R}{Z}$

$\cos \phi = \dfrac{80}{100} = \dfrac{8}{10}$

Comparing this with $\dfrac{x}{10}$, we get $x = 8$.

Answer: $8$

</details>

---

### Q50. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown, the ratio of the quality factor and the band width is
(Given: band width = R/L)
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/13_april_shift_2__q27_d1_v2.png" />

**Options:**

- **(A)** $\sqrt{\dfrac{1}{LC}}\dfrac{L^2}{R^2}$
- **(B)** $\sqrt{\dfrac{1}{LC}}$
- **(C)** $\sqrt{\dfrac{1}{LC}}\dfrac{L}{R}$
- **(D)** $\sqrt{\dfrac{1}{LC}}\dfrac{R}{L}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{\dfrac{1}{LC}}\dfrac{L^2}{R^2}$**

**Detailed Solution:**

The quality factor $Q$ of a series LCR circuit is given by:

$Q = \dfrac{\omega_0 L}{R}$

where $\omega_0$ is the resonant angular frequency, $\omega_0 = \sqrt{\dfrac{1}{LC}}$.

The bandwidth is given as $\Delta \omega = \dfrac{R}{L}$.

The ratio of the quality factor to the bandwidth is:

$\text{Ratio} = \dfrac{Q}{\Delta \omega} = \dfrac{\dfrac{\omega_0 L}{R}}{\dfrac{R}{L}} = \omega_0 \dfrac{L^2}{R^2}$

Substituting $\omega_0 = \sqrt{\dfrac{1}{LC}}$, we get:

$\text{Ratio} = \sqrt{\dfrac{1}{LC}} \dfrac{L^2}{R^2}$

Answer: $\sqrt{\dfrac{1}{LC}}\dfrac{L^2}{R^2}$

</details>

---

### Q51. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An inductor of $0.5$ mH, a capacitor of $20$ $\mu$F and resistance $20\,\Omega$ are connected in series with a $220$ V ac source. If the current is in phase with the emf, the amplitude of current of the circuit is $[x]^{1/2}$ A. The value of $x$ is

**Options:**

- **(A)** $61$
- **(B)** $121$
- **(C)** $242$
- **(D)** $442$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $242$**

**Detailed Solution:**

Since the current is in phase with the emf, the circuit is in resonance.

At resonance, the impedance of the circuit is equal to its resistance.

$Z = R = 20\,\Omega$

The rms current in the circuit is given by:

$I_{rms} = \dfrac{V_{rms}}{Z} = \dfrac{220}{20} = 11$ A

The amplitude (peak value) of the current is:

$I_{0} = \sqrt{2} I_{rms} = 11\sqrt{2} = \sqrt{242}$ A

Given that the amplitude of the current is $\sqrt{x}$ A, we have:

$\sqrt{x} = \sqrt{242} \Rightarrow x = 242$

Answer: $242$

</details>

---

### Q52. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a series LR circuit with $X_L = R$. Power factor is $P_1$. If a capacitor of capacitance $C$ with $X_c = X_L$ is added to the circuit the power factor becomes $P_2$. The ratio of $P_1$ to $P_2$ will be :

**Options:**

- **(A)** $1:3$
- **(B)** $1:\sqrt{2}$
- **(C)** $1:1$
- **(D)** $1:2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1:\sqrt{2}$**

**Detailed Solution:**

For the initial series LR circuit, the impedance is $Z_1 = \sqrt{R^2 + X_L^2}$.

Given $X_L = R$, we have $Z_1 = \sqrt{R^2 + R^2} = \sqrt{2}R$.

The power factor $P_1 = \dfrac{R}{Z_1} = \dfrac{R}{\sqrt{2}R} = \dfrac{1}{\sqrt{2}}$.

When a capacitor with $X_C = X_L$ is added in series, the new impedance is $Z_2 = \sqrt{R^2 + (X_L - X_C)^2}$.

Since $X_C = X_L$, the circuit is in resonance and $Z_2 = R$.

The new power factor $P_2 = \dfrac{R}{Z_2} = \dfrac{R}{R} = 1$.

The ratio of $P_1$ to $P_2$ is $\dfrac{P_1}{P_2} = \dfrac{1/\sqrt{2}}{1} = \dfrac{1}{\sqrt{2}}$.

Thus, $P_1 : P_2 = 1 : \sqrt{2}$.

</details>

---

### Q53. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR circuit C = 2 uF, L=1 mH and R= 10 $\Omega$. What is the ratio of energies stored in the capacitor and inductor when maximum current flows through circuit?

**Options:**

- **(A)** $0.1 : 1$
- **(B)** $0.4 : 1$
- **(C)** $0.2 : 1$
- **(D)** $0.8 : 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.2 : 1$**

**Detailed Solution:**

For a series LCR circuit undergoing free oscillations, the voltage equation is given by:

$V_L + V_R + V_C = 0$

$L \dfrac{di}{dt} + iR + V_C = 0$

When the current $i$ in the circuit is maximum, its rate of change is zero, i.e., $\dfrac{di}{dt} = 0$.

Substituting this into the voltage equation, we get:

$0 + i_{max}R + V_C = 0 \Rightarrow V_C = -i_{max}R$

The energy stored in the capacitor at this instant is:

$U_C = \dfrac{1}{2} C V_C^2 = \dfrac{1}{2} C (i_{max}R)^2$

The energy stored in the inductor at the same instant is:

$U_L = \dfrac{1}{2} L i_{max}^2$

The ratio of the energy stored in the capacitor to that in the inductor is:

$\dfrac{U_C}{U_L} = \dfrac{\dfrac{1}{2} C i_{max}^2 R^2}{\dfrac{1}{2} L i_{max}^2} = \dfrac{CR^2}{L}$

Given values are:

$C = 2 \times 10^{-6} \text{ F}$

$R = 10 \Omega$

$L = 10^{-3} \text{ H}$

Substituting the given values into the ratio:

$\dfrac{U_C}{U_L} = \dfrac{2 \times 10^{-6} \times (10)^2}{10^{-3}}$

$\dfrac{U_C}{U_L} = \dfrac{2 \times 10^{-4}}{10^{-3}} = 0.2$

Thus, the ratio of energies is $0.2 : 1$.

Answer: $0.2 : 1$

</details>

---

### Q54. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR resonant circuit, R=800 $\Omega$, C = 2 $\mu$F and voltage across resistance is 200 V. The angular frequency is 250 rad/s. At resonance the voltage across the capacitance is

**Options:**

- **(A)** $250$ V
- **(B)** $500$ V
- **(C)** $1000$ V
- **(D)** $750$ V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $500$ V**

**Detailed Solution:**

At resonance, the current in the circuit is determined by the resistance and the voltage across it.

$I = \dfrac{V_R}{R}$

Substituting the given values:

$I = \dfrac{200}{800} = 0.25$ A

The capacitive reactance is given by:

$X_C = \dfrac{1}{\omega C}$

Substituting the given values:

$X_C = \dfrac{1}{250 \times 2 \times 10^{-6}} = \dfrac{10^6}{500} = 2000 \, \Omega$

The voltage across the capacitance is:

$V_C = I X_C$

$V_C = 0.25 \times 2000 = 500$ V

Answer: $500$ V

</details>

---

### Q55. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A resistor of 100 $\Omega$, inductor of self inductance $\left(\dfrac{4}{\pi^2}\right)$ H and a capacitor of unknown capacity are connected in series to an a.c. source of 200 V and 50 Hz. When the current and voltage are in phase, the value of capacity is

**Options:**

- **(A)** $40 \ \mu F$
- **(B)** $50 \ \mu F$
- **(C)** $20 \ \mu F$
- **(D)** $25 \ \mu F$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $25 \ \mu F$**

**Detailed Solution:**

When current and voltage are in phase, the circuit is in resonance.

$X_L = X_C$

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L}$

Given $f = 50$ Hz, $\omega = 2\pi f = 100\pi$ rad/s and $L = \dfrac{4}{\pi^2}$ H.

Substituting the values:

$C = \dfrac{1}{(100\pi)^2 \times \left(\dfrac{4}{\pi^2}\right)}$

$C = \dfrac{1}{10000\pi^2 \times \dfrac{4}{\pi^2}}$

$C = \dfrac{1}{40000}$ F

$C = 25 \times 10^{-6}$ F $= 25 \ \mu F$

Answer: $25 \ \mu F$

</details>

---

### Q56. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A light bulb connected in series with a capacitor and an a.c.source is glowing with certain brightness. On reducing the value of capacitance and frequency respectively, the brightness of the bulb

**Options:**

- **(A)** is reduced, is reduced
- **(B)** is more, is more
- **(C)** is more, is reduced
- **(D)** is reduced, is more

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) is reduced, is reduced**

**Detailed Solution:**

The brightness of the bulb depends on the current flowing through it, which is given by $I = \dfrac{V}{Z}$.

The impedance of the series RC circuit is $Z = \sqrt{R^2 + X_C^2}$, where $X_C = \dfrac{1}{2\pi f C}$.

When the capacitance $C$ is reduced, the capacitive reactance $X_C$ increases. This increases the total impedance $Z$ of the circuit, which in turn reduces the current $I$. Consequently, the brightness of the bulb is reduced.

Similarly, when the frequency $f$ of the AC source is reduced, the capacitive reactance $X_C$ increases. This again increases the impedance $Z$ and reduces the current $I$. Thus, the brightness of the bulb is reduced.

Therefore, in both cases, the brightness of the bulb is reduced.

Answer: is reduced, is reduced

</details>

---

### Q57. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR circuit, resistance is $18\ \Omega$ and impedance $33\ \Omega$. An r.m.s. Voltage of $220$ V is applied across the circuit. The true power consumed in a c. circuit is

**Options:**

- **(A)** $400$ W
- **(B)** $600$ W
- **(C)** $200$ W
- **(D)** $800$ W

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $800$ W**

**Detailed Solution:**

The true power consumed in an AC circuit is given by the formula:

$P = I_{rms}^2 R$

The rms current in the circuit is:

$I_{rms} = \dfrac{V_{rms}}{Z}$

Substituting the given values $V_{rms} = 220$ V and $Z = 33\ \Omega$:

$I_{rms} = \dfrac{220}{33} = \dfrac{20}{3}$ A

Now, substituting $I_{rms}$ and $R = 18\ \Omega$ into the power formula:

$P = \left(\dfrac{20}{3}\right)^2 \times 18$

$P = \dfrac{400}{9} \times 18$

$P = 800$ W

Answer: $800$ W

</details>

---

### Q58. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An inductor of reactance $100$ $\Omega$, a capacitor of reactance $50$ $\Omega$, and a resistor of resistance $50$ $\Omega$ are connected in series with an AC source of $10$ V, $50$ Hz. Average power dissipated by the circuit is ____

**Options:**

- **(A)** $1$ W
- **(B)** $2$ W
- **(C)** $3$ W
- **(D)** $4$ W

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$ W**

**Detailed Solution:**

Given $X_L = 100$ $\Omega$, $X_C = 50$ $\Omega$, and $R = 50$ $\Omega$.

The impedance of the series LCR circuit is given by:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$

$Z = \sqrt{50^2 + (100 - 50)^2} = \sqrt{50^2 + 50^2} = 50\sqrt{2}$ $\Omega$

The RMS current in the circuit is:

$I_{rms} = \dfrac{V_{rms}}{Z} = \dfrac{10}{50\sqrt{2}} = \dfrac{1}{5\sqrt{2}}$ A

The average power dissipated in the circuit is:

$P_{avg} = I_{rms}^2 R$

$P_{avg} = \left(\dfrac{1}{5\sqrt{2}}\right)^2 \times 50 = \dfrac{1}{50} \times 50 = 1$ W

Answer: $1$ W

</details>

---

### Q59. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown below, the ac source has voltage $V = 30 \cos(\omega t)$ volt with $\omega = 2000$ rad/s. What will be the amplitude of the current?
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/11_april_shift_1__q35_d1.png" />

**Options:**

- **(A)** $\sqrt{5}$ A
- **(B)** $\dfrac{3}{\sqrt{5}}$ A
- **(C)** $3$ A
- **(D)** $3.3$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3$ A**

**Detailed Solution:**

From the given circuit, the parameters are:
Amplitude of voltage, $V_m = 30$ V
Angular frequency, $\omega = 2000$ rad/s
Total resistance, $R = 6 + 4 = 10\ \Omega$
Inductance, $L = 5 \times 10^{-3}$ H
Capacitance, $C = 50 \times 10^{-6}$ F

The inductive reactance is:
$X_L = \omega L = 2000 \times 5 \times 10^{-3} = 10\ \Omega$

The capacitive reactance is:
$X_C = \dfrac{1}{\omega C} = \dfrac{1}{2000 \times 50 \times 10^{-6}} = 10\ \Omega$

The total impedance of the circuit is:
$Z = \sqrt{R^2 + (X_L - X_C)^2}$

Substituting the values:
$Z = \sqrt{10^2 + (10 - 10)^2} = 10\ \Omega$

The amplitude of the current is:
$I_m = \dfrac{V_m}{Z} = \dfrac{30}{10} = 3$ A

Answer: $3$ A

</details>

---

### Q60. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An inductor of $\left(\frac{100}{\pi}\right) \mathrm{mH}$, capacitor of capacitance $\left(\frac{10^{-3}}{2 \pi}\right) \mathrm{F}$ and resistance of $10 \Omega$ are connected in series with an AC voltage source of $110 \mathrm{~V}, 50 \mathrm{~Hz}$ supply. The tangent of the phase angle ' $\phi$ ' between voltage and current is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

The inductive reactance $X_L$ is given by:

$X_L = 2\pi f L = 2\pi \times 50 \times \dfrac{100 \times 10^{-3}}{\pi} = 10 \ \Omega$

The capacitive reactance $X_C$ is given by:

$X_C = \dfrac{1}{2\pi f C} = \dfrac{1}{2\pi \times 50 \times \dfrac{10^{-3}}{2\pi}} = \dfrac{1}{50 \times 10^{-3}} = 20 \ \Omega$

The tangent of the phase angle $\phi$ between voltage and current is:

$\tan \phi = \dfrac{|X_L - X_C|}{R}$

Substituting the values:

$\tan \phi = \dfrac{|10 - 20|}{10} = \dfrac{10}{10} = 1$

Answer: 1

</details>

---

### Q61. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The value of alternating e.m.f. (E) in the given circuit is


<img width=300px src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/QWwcDkf8o4Y9W4FqO0RcIWtLx0aBN4Kx4gUuVApJdKc.original.fullsize.png">

**Options:**

- **(A)** 30 V
- **(B)** 60 V
- **(C)** 50 V
- **(D)** 110 V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 50 V**

**Detailed Solution:**

From the given circuit diagram, the voltages across the inductor, capacitor, and resistor are:
$V_L = 20\text{ V}$
$V_C = 50\text{ V}$
$V_R = 40\text{ V}$

In a series LCR circuit, the total alternating e.m.f. $E$ is given by the phasor sum of the individual voltages:
$E = \sqrt{V_R^2 + (V_L - V_C)^2}$

Substituting the given values:
$E = \sqrt{40^2 + (20 - 50)^2}$
$E = \sqrt{40^2 + (-30)^2}$
$E = \sqrt{1600 + 900}$
$E = \sqrt{2500}$
$E = 50\text{ V}$

Answer: 50 V

</details>

---

### Q62. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an LC circuit, angular frequency at resonance is $\omega$. The new angular frequency when inductance is made four times and capacitance is made eight times is

**Options:**

- **(A)** $\frac{\omega}{2 \sqrt{2}}$
- **(B)** $\frac{\omega}{4 \sqrt{2}}$
- **(C)** $\frac{\omega}{4}$
- **(D)** $\frac{\omega}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\omega}{4 \sqrt{2}}$**

**Detailed Solution:**

The angular frequency of an LC circuit at resonance is given by

$\omega = \dfrac{1}{\sqrt{LC}}$

When inductance is made four times and capacitance is made eight times, the new inductance is $L' = 4L$ and the new capacitance is $C' = 8C$.

The new angular frequency is

$\omega' = \dfrac{1}{\sqrt{L'C'}} = \dfrac{1}{\sqrt{(4L)(8C)}}$

$\omega' = \dfrac{1}{\sqrt{32LC}} = \dfrac{1}{4\sqrt{2}\sqrt{LC}}$

$\omega' = \dfrac{\omega}{4\sqrt{2}}$

Answer: $\frac{\omega}{4 \sqrt{2}}$

</details>

---

### Q63. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A resistor of $100 \Omega$, inductor of self inductance $\left(\frac{4}{\pi^2}\right) \mathrm{H}$ and a capacitor of unknown capacitance are connected in series to an a.c. source of $200 \mathrm{~V}, 50 \mathrm{~Hz}$ supply. When the current and voltage are in phase, the capacitance and the power dissipated is respectively

**Options:**

- **(A)** $2.5 \times 10^{-5} \mathrm{~F}, 400 \mathrm{~W}$
- **(B)** $2 \times 10^{-5} \mathrm{~F}, 200 \mathrm{~W}$
- **(C)** $3 \times 10^{-5} \mathrm{~F}, 300 \mathrm{~W}$
- **(D)** $4 \times 10^{-5} \mathrm{~F}, 400 \mathrm{~W}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2.5 \times 10^{-5} \mathrm{~F}, 400 \mathrm{~W}$**

**Detailed Solution:**

Given:
$R = 100 \Omega$
$L = \dfrac{4}{\pi^2} \mathrm{H}$
$V = 200 \mathrm{V}$
$f = 50 \mathrm{Hz}$

Since the current and voltage are in phase, the circuit is in resonance.
At resonance, the inductive reactance equals the capacitive reactance ($X_L = X_C$).

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L}$

Angular frequency $\omega = 2\pi f = 2\pi \times 50 = 100\pi \mathrm{\,rad/s}$

Substituting the values:
$C = \dfrac{1}{(100\pi)^2 \times \dfrac{4}{\pi^2}}$

$C = \dfrac{1}{10000\pi^2 \times \dfrac{4}{\pi^2}} = \dfrac{1}{40000} = 2.5 \times 10^{-5} \mathrm{\,F}$

At resonance, the impedance of the circuit is purely resistive, so $Z = R = 100 \Omega$.

The power dissipated is given by:
$P = \dfrac{V^2}{R}$

$P = \dfrac{(200)^2}{100} = \dfrac{40000}{100} = 400 \mathrm{\,W}$

Answer: $2.5 \times 10^{-5} \mathrm{~F}, 400 \mathrm{~W}$

</details>

---

### Q64. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an LC circuit, angular frequency at resonance is ' $\omega$ '. What will be the new angular frequency when inductor's inductance is made two times and capacitor's capacitance is made four times?

**Options:**

- **(A)** $\frac{\omega}{2 \sqrt{2}}$
- **(B)** $\frac{\omega}{\sqrt{2}}$
- **(C)** $2 \omega$
- **(D)** $\frac{2 \omega}{\sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\omega}{2 \sqrt{2}}$**

**Detailed Solution:**

The angular frequency of an LC circuit at resonance is given by:

$\omega = \dfrac{1}{\sqrt{LC}}$

When the inductance is made two times and capacitance is made four times, the new inductance is $L' = 2L$ and the new capacitance is $C' = 4C$.

The new angular frequency is:

$\omega' = \dfrac{1}{\sqrt{L'C'}}$

$\omega' = \dfrac{1}{\sqrt{(2L)(4C)}}$

$\omega' = \dfrac{1}{\sqrt{8LC}}$

$\omega' = \dfrac{1}{2\sqrt{2}\sqrt{LC}}$

$\omega' = \dfrac{\omega}{2\sqrt{2}}$

Answer: $\frac{\omega}{2 \sqrt{2}}$

</details>

---

### Q65. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The frequency at resonance for the circuit is

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/7qK_lVu_tZkP_qJxXSlSTfN5sJ8W05Yj1Mb_j1R0lVE.original.fullsize.png">

**Options:**

- **(A)** $\frac{1}{4 \pi \sqrt{\mathrm{LC}}}$
- **(B)** $\frac{1}{2 \pi \sqrt{\mathrm{LC}}}$
- **(C)** $\frac{1}{\pi \sqrt{\mathrm{LC}}}$
- **(D)** $\frac{2}{\pi \sqrt{\mathrm{LC}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{\pi \sqrt{\mathrm{LC}}}$**

**Detailed Solution:**

From the given circuit diagram, the two inductors of inductance $L$ are connected in parallel. Their equivalent inductance $L_{eq}$ is:

$L_{eq} = \dfrac{L \times L}{L + L} = \dfrac{L}{2}$

The two capacitors of capacitance $C$ are connected in series. Their equivalent capacitance $C_{eq}$ is:

$C_{eq} = \dfrac{C \times C}{C + C} = \dfrac{C}{2}$

The resonant frequency $f$ of the series $L-C$ circuit is given by:

$f = \dfrac{1}{2\pi \sqrt{L_{eq} C_{eq}}}$

Substituting the values of $L_{eq}$ and $C_{eq}$:

$f = \dfrac{1}{2\pi \sqrt{\left(\dfrac{L}{2}\right) \left(\dfrac{C}{2}\right)}}$

$f = \dfrac{1}{2\pi \sqrt{\dfrac{LC}{4}}}$

$f = \dfrac{1}{2\pi \left(\dfrac{\sqrt{LC}}{2}\right)}$

$f = \dfrac{1}{\pi \sqrt{LC}}$

Answer: $\frac{1}{\pi \sqrt{\mathrm{LC}}}$

</details>

---

### Q66. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a discharging series LCR circuit $\mathrm{C}=2 \mu \mathrm{F}, \mathrm{~L}=5 \mathrm{mH}$ and $\mathrm{R}=5 \Omega$. The ratio of energy stored in the inductor to that in capacitor, when maximum current flows through the circuit is

**Options:**

- **(A)** 200:1
- **(B)** 100:1
- **(C)** 300:1
- **(D)** 500:1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 100:1**

**Detailed Solution:**

For a discharging series LCR circuit, the voltage equation is given by:

$L \dfrac{dI}{dt} + I R + \dfrac{q}{C} = 0$

When the maximum current flows through the circuit, the rate of change of current is zero, i.e., $\dfrac{dI}{dt} = 0$. Substituting this into the equation, we get:

$I R + \dfrac{q}{C} = 0 \Rightarrow q = -I R C$

The energy stored in the inductor is:

$U_L = \dfrac{1}{2} L I^2$

The energy stored in the capacitor is:

$U_C = \dfrac{q^2}{2C}$

Substituting $q = -I R C$ into the expression for $U_C$:

$U_C = \dfrac{(-I R C)^2}{2C} = \dfrac{1}{2} I^2 R^2 C$

The ratio of the energy stored in the inductor to that in the capacitor is:

$\dfrac{U_L}{U_C} = \dfrac{\dfrac{1}{2} L I^2}{\dfrac{1}{2} I^2 R^2 C} = \dfrac{L}{R^2 C}$

Given values are $L = 5 \times 10^{-3} \text{ H}$, $R = 5 \, \Omega$, and $C = 2 \times 10^{-6} \text{ F}$. Substituting these values:

$\dfrac{U_L}{U_C} = \dfrac{5 \times 10^{-3}}{(5)^2 \times 2 \times 10^{-6}}$

$\dfrac{U_L}{U_C} = \dfrac{5 \times 10^{-3}}{25 \times 2 \times 10^{-6}} = \dfrac{5 \times 10^{-3}}{50 \times 10^{-6}}$

$\dfrac{U_L}{U_C} = \dfrac{5000 \times 10^{-6}}{50 \times 10^{-6}} = 100$

Thus, the ratio is $100:1$.

Answer: 100:1

</details>

---

### Q67. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A resistor of $50 \Omega$, inductor of self inductance $\left(\frac{2}{\pi^2}\right) \mathrm{H}$ and a capacitor of unknown capacity are connected in series to an a.c. source of $100 \mathrm{~V}, 50$ Hz supply. When the voltage and current are in phase, the value of capacitance is

**Options:**

- **(A)** $10 \mu \mathrm{~F}$
- **(B)** $20 \mu \mathrm{~F}$
- **(C)** $40 \mu \mathrm{~F}$
- **(D)** $50 \mu \mathrm{~F}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $50 \mu \mathrm{~F}$**

**Detailed Solution:**

Given that the voltage and current are in phase, the circuit is in resonance.

At resonance, the inductive reactance is equal to the capacitive reactance:

$X_L = X_C$

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L}$

Substituting $\omega = 2\pi f$:

$C = \dfrac{1}{(2\pi f)^2 L}$

Given $f = 50$ Hz and $L = \dfrac{2}{\pi^2}$ H:

$C = \dfrac{1}{(2\pi \times 50)^2 \times \left(\dfrac{2}{\pi^2}\right)}$

$C = \dfrac{1}{10000\pi^2 \times \dfrac{2}{\pi^2}}$

$C = \dfrac{1}{20000}$ F

$C = 50 \times 10^{-6}$ F = $50 \mu$F

Answer: $50 \mu \mathrm{~F}$

</details>

---

### Q68. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An a.c. source of frequency ' $f$ ' is connected to a circuit containing an inductance ' $L$ ' and resistance ' $R$ ' in series. The impedance of this circuit is

**Options:**

- **(A)** $\sqrt{\mathrm{R}^2+2 \pi \mathrm{fL}^2}$
- **(B)** $\sqrt{R^2+L^2}$
- **(C)** $\mathrm{R}+2 \pi \mathrm{fL}$
- **(D)** $\sqrt{R^2+4 \pi^2 f^2 L^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{R^2+4 \pi^2 f^2 L^2}$**

**Detailed Solution:**

The impedance $Z$ of a series LR circuit is given by the formula:

$Z = \sqrt{R^2 + X_L^2}$

where $X_L$ is the inductive reactance. The inductive reactance is related to the frequency $f$ and inductance $L$ by:

$X_L = \omega L = 2 \pi f L$

Substituting the value of $X_L$ into the impedance equation, we get:

$Z = \sqrt{R^2 + (2 \pi f L)^2}$

$Z = \sqrt{R^2 + 4 \pi^2 f^2 L^2}$

Answer: $\sqrt{R^2+4 \pi^2 f^2 L^2}$

</details>

---

### Q69. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an $L R$ circuit, the value of $L$ is $\left(\frac{0.3}{\pi}\right)$ henry and the value of $R$ is $40 \Omega$, If in the circuit, an alternating e.m.f of 230 V at 50 cycles per second is connected, the impedance of the circuit and current will be respectively

**Options:**

- **(A)** $12.5 \Omega, 9.2 \mathrm{~A}$
- **(B)** $46.4 \Omega, 6.4 \mathrm{~A}$
- **(C)** $23.2 \Omega, 5 \mathrm{~A}$
- **(D)** $50 \Omega, 4.6 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $50 \Omega, 4.6 \mathrm{~A}$**

**Detailed Solution:**

The inductive reactance is given by $X_L = 2 \pi f L$

Substituting the given values:

$X_L = 2 \pi \times 50 \times \dfrac{0.3}{\pi} = 30 \, \Omega$

The impedance of the $L R$ circuit is $Z = \sqrt{R^2 + X_L^2}$

$Z = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50 \, \Omega$

The current in the circuit is $I = \dfrac{V}{Z}$

$I = \dfrac{230}{50} = 4.6 \, \text{A}$

Answer: $50 \Omega, 4.6 \mathrm{~A}$

</details>

---

### Q70. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Figure shows the combination of inductances and capacitances. Resonant frequency of the L - C circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/RKa230ISXzB8oLMhaJGvg_zH1qM3MHXAkevjaSxIsOQ.original.fullsize.png">

**Options:**

- **(A)** $\frac{1}{2 \pi \sqrt{\mathrm{LC}}}$
- **(B)** $\frac{1}{3 \pi \sqrt{\mathrm{LC}}}$
- **(C)** $\frac{1}{4 \pi \sqrt{\mathrm{LC}}}$
- **(D)** $\frac{1}{6 \pi \sqrt{\mathrm{LC}}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{6 \pi \sqrt{\mathrm{LC}}}$**

**Detailed Solution:**

From the given circuit diagram, the inductors $L$ and $2L$ are connected in series. Their equivalent inductance is:

$L_{eq} = L + 2L = 3L$

The capacitors $C$ and $2C$ are connected in parallel. Their equivalent capacitance is:

$C_{eq} = C + 2C = 3C$

The equivalent inductor and the equivalent capacitor are connected in parallel to the a.c. source, forming an $L-C$ resonant circuit. The resonant frequency of this circuit is given by:

$f = \dfrac{1}{2\pi\sqrt{L_{eq}C_{eq}}}$

Substituting the values of $L_{eq}$ and $C_{eq}$:

$f = \dfrac{1}{2\pi\sqrt{(3L)(3C)}}$

$f = \dfrac{1}{2\pi\sqrt{9LC}}$

$f = \dfrac{1}{6\pi\sqrt{LC}}$

Answer: $\frac{1}{6 \pi \sqrt{\mathrm{LC}}}$

</details>

---

### Q71. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In an a.c. circuit with pure capacitance 'C' and a.c. source $\mathrm{E}=\mathrm{E}_0 \sin \omega \mathrm{t}$, the equation of instantaneous current is given by

**Options:**

- **(A)** $I=E_0 \omega c \sin (\omega t)$
- **(B)** $I=E_0 \omega c \sin \left(\omega t+\frac{\pi}{2}\right)$
- **(C)** $I=\frac{E_0}{\omega c} \sin (\omega t)$
- **(D)** $I=\frac{E_0}{\omega c} \sin \left(\omega t+\frac{\pi}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $I=E_0 \omega c \sin \left(\omega t+\frac{\pi}{2}\right)$**

**Detailed Solution:**

The instantaneous voltage across the capacitor is given by $E = E_0 \sin \omega t$.

The charge on the capacitor at any instant is $q = CE = CE_0 \sin \omega t$.

The instantaneous current $I$ is the rate of flow of charge, given by $I = \dfrac{dq}{dt}$.

Substituting the value of $q$, we get:

$I = \dfrac{d}{dt} (CE_0 \sin \omega t)$

$I = CE_0 \omega \cos \omega t$

Using the trigonometric identity $\cos \theta = \sin\left(\theta + \dfrac{\pi}{2}\right)$, the equation becomes:

$I = E_0 \omega C \sin\left(\omega t + \dfrac{\pi}{2}\right)$

Answer: $I=E_0 \omega c \sin \left(\omega t+\frac{\pi}{2}\right)$

</details>

---

### Q72. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

When a capacitor is connected in series with an LR circuit, the alternating current flowing in the circuit

**Options:**

- **(A)** remains constant
- **(B)** may increase or decrease
- **(C)** decreases
- **(D)** is zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) may increase or decrease**

**Detailed Solution:**

The initial impedance of the LR circuit is given by $Z_1 = \sqrt{R^2 + X_L^2}$.

When a capacitor is connected in series, the circuit becomes an LCR series circuit. The new impedance is given by $Z_2 = \sqrt{R^2 + (X_L - X_C)^2}$.

The alternating current in the circuit is $I = \dfrac{V}{Z}$.

If $X_C < 2X_L$, then $(X_L - X_C)^2 < X_L^2$. This implies $Z_2 < Z_1$, so the current increases.

If $X_C > 2X_L$, then $(X_L - X_C)^2 > X_L^2$. This implies $Z_2 > Z_1$, so the current decreases.

Therefore, depending on the value of the capacitive reactance $X_C$, the current may increase or decrease.

Answer: may increase or decrease

</details>

---

### Q73. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An a.c. e.m.f. of peak value 230 V and frequency 50 Hz is connected to a circuit with $\mathrm{R}=11.5 \Omega, \mathrm{~L}=2.5 \mathrm{H}$ and a capacitor all in series. The value of capacitance is ' $C$ ' for the current in the circuit to be maximum. The value of ' $C$ ' and maximum current are respectively ( $\pi^2=10$ )

**Options:**

- **(A)** $4 \mu \mathrm{~F}, \quad 20 \mathrm{~A}$
- **(B)** $5 \mu \mathrm{~F}, \quad 10 \mathrm{~A}$
- **(C)** $2 \mu \mathrm{~F}, \quad 20 \mathrm{~A}$
- **(D)** $8 \mu \mathrm{~F}, 12 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4 \mu \mathrm{~F}, \quad 20 \mathrm{~A}$**

**Detailed Solution:**

For the current in an LCR series circuit to be maximum, the circuit must be in resonance.

At resonance, the inductive reactance equals the capacitive reactance:

$X_L = X_C$

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L} = \dfrac{1}{4 \pi^2 f^2 L}$

Substituting the given values ($f = 50$ Hz, $\pi^2 = 10$, $L = 2.5$ H):

$C = \dfrac{1}{4 \times 10 \times (50)^2 \times 2.5}$

$C = \dfrac{1}{40 \times 2500 \times 2.5} = \dfrac{1}{250000}$

$C = 4 \times 10^{-6} \text{ F} = 4 \mu\text{F}$

At resonance, the impedance of the circuit is minimum and equal to the resistance ($Z = R$).

The maximum current (peak current) is given by:

$I_0 = \dfrac{V_0}{R}$

$I_0 = \dfrac{230}{11.5} = 20 \text{ A}$

Answer: $4 \mu \mathrm{~F}, \quad 20 \mathrm{~A}$

</details>

---

### Q74. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An alternating e.m.f. having voltage $V=V_0 \sin \omega t$ is applied to a series L-C-R circuit. Given : $\left|X_L-X_C\right|=R$. The r.m.s. value of potential difference across capacitor will be

**Options:**

- **(A)** $V_0 R \omega C$
- **(B)** $\frac{V_0}{R \omega C}$
- **(C)** $\frac{V_0}{2 R \omega C}$
- **(D)** $\frac{V_0}{\sqrt{2} R \omega C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{V_0}{2 R \omega C}$**

**Detailed Solution:**

The impedance of the series L-C-R circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

Given $|X_L - X_C| = R$, we get $Z = \sqrt{R^2 + R^2} = \sqrt{2}R$.

The r.m.s. value of the applied voltage is $V_{rms} = \dfrac{V_0}{\sqrt{2}}$.

The r.m.s. current in the circuit is $I_{rms} = \dfrac{V_{rms}}{Z} = \dfrac{V_0 / \sqrt{2}}{\sqrt{2}R} = \dfrac{V_0}{2R}$.

The r.m.s. potential difference across the capacitor is $V_{C(rms)} = I_{rms} X_C$.

Since $X_C = \dfrac{1}{\omega C}$, we have $V_{C(rms)} = \dfrac{V_0}{2R} \times \dfrac{1}{\omega C} = \dfrac{V_0}{2R\omega C}$.

Answer: $\frac{V_0}{2 R \omega C}$

</details>

---

### Q75. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If maximum energy is stored in a capacitor at $\mathrm{t}=0$ then the time after which, current in the circuit will be maximum is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/IbxhEzbLUBiCrkoGjjx_AAiMREuZpBVENgFmnC8lp5c.original.fullsize.png">

**Options:**

- **(A)** $\pi \times 10^{-3} \mathrm{~s}$
- **(B)** $2 \pi \times 10^{-3} \mathrm{~s}$
- **(C)** $2 \pi \times 10^{-4} s$
- **(D)** $\pi \times 10^{-4} \mathrm{~s}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 \pi \times 10^{-4} s$**

**Detailed Solution:**

The time period of oscillation in an LC circuit is $T = 2\pi\sqrt{LC}$.

At $t = 0$, the energy in the capacitor is maximum, so the current is zero. The current becomes maximum when the energy is completely transferred to the inductor, which happens at one-fourth of the time period, i.e., $t = \dfrac{T}{4}$.

Given:
$L = 16 \text{ mH} = 16 \times 10^{-3} \text{ H}$
$C = 10 \mu\text{F} = 10 \times 10^{-6} \text{ F}$

Substituting the values to find $T$:
$T = 2\pi\sqrt{16 \times 10^{-3} \times 10 \times 10^{-6}}$
$T = 2\pi\sqrt{16 \times 10^{-8}}$
$T = 2\pi \times 4 \times 10^{-4} = 8\pi \times 10^{-4} \text{ s}$

The required time is:
$t = \dfrac{T}{4} = \dfrac{8\pi \times 10^{-4}}{4} = 2\pi \times 10^{-4} \text{ s}$

Answer: $2 \pi \times 10^{-4} s$

</details>

---

### Q76. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR resonant circuit, $R=800 \Omega, C=2 \mu F$ and voltage across resistance is 200 V . The angular frequency is $250 \mathrm{rad} / \mathrm{s}$. At resonance, the voltage across the inductance is

**Options:**

- **(A)** 400 V
- **(B)** 250 V
- **(C)** 1000 V
- **(D)** 500 V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 500 V**

**Detailed Solution:**

In a series LCR circuit, the current $I$ is given by the voltage across the resistor divided by its resistance:

$I = \dfrac{V_R}{R} = \dfrac{200}{800} = 0.25 \text{ A}$

At resonance, the inductive reactance equals the capacitive reactance ($X_L = X_C$), which means the voltage across the inductance equals the voltage across the capacitance ($V_L = V_C$).

The capacitive reactance is:

$X_C = \dfrac{1}{\omega C} = \dfrac{1}{250 \times 2 \times 10^{-6}} = \dfrac{10^6}{500} = 2000 \, \Omega$

The voltage across the inductance is:

$V_L = V_C = I X_C = 0.25 \times 2000 = 500 \text{ V}$

Answer: 500 V

</details>

---

### Q77. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An a.c. e.m.f. of peak value $=230 \mathrm{~V}$ and frequency 50 Hz is connected to a circuit with $\mathrm{R}=11.5 \Omega, \mathrm{~L}=2.5 \mathrm{H}$ and a capacitor all in series. The value of capacitance is ' C ' for the current in the circuit to be maximum. The value of C and maximum current are respectively ( $\pi^2=10$ )

**Options:**

- **(A)** $2 \mu \mathrm{F}, 10 \mathrm{~A}$
- **(B)** $4 \mu \mathrm{F}, 20 \mathrm{~A}$
- **(C)** $6 \mu \mathrm{F}, 10 \mathrm{~A}$
- **(D)** $8 \mu \mathrm{F}, 20 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \mu \mathrm{F}, 20 \mathrm{~A}$**

**Detailed Solution:**

For the current in an LCR series circuit to be maximum, the circuit must be in resonance.

At resonance, the inductive reactance equals the capacitive reactance:

$X_L = X_C$

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L} = \dfrac{1}{4 \pi^2 f^2 L}$

Substituting the given values ($f = 50 \text{ Hz}$, $L = 2.5 \text{ H}$, $\pi^2 = 10$):

$C = \dfrac{1}{4 \times 10 \times (50)^2 \times 2.5}$

$C = \dfrac{1}{40 \times 2500 \times 2.5} = \dfrac{1}{250000} = 4 \times 10^{-6} \text{ F} = 4 \mu\text{F}$

At resonance, the impedance of the circuit is minimum and equal to the resistance $R$.

The maximum current (peak current) is given by:

$I_0 = \dfrac{V_0}{R}$

$I_0 = \dfrac{230}{11.5} = 20 \text{ A}$

Answer: $4 \mu \mathrm{F}, 20 \mathrm{~A}$

</details>

---

### Q78. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The reading of the ammeter in the following circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/iV1xuSZ-2jSUMrELk6D47UfKtCaJnkGOY-0TgSCKAAQ.original.fullsize.png">

**Options:**

- **(A)** 3 A
- **(B)** 6 A
- **(C)** 12 A
- **(D)** 9 A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 6 A**

**Detailed Solution:**

In the given series LCR circuit, the total voltage $V$ is related to the voltages across the individual components by the equation:

$V = \sqrt{V_R^2 + (V_L - V_C)^2}$

From the circuit diagram, we are given:
Voltage across the inductor, $V_L = 100 \text{ V}$
Voltage across the capacitor, $V_C = 100 \text{ V}$
Source voltage, $V = 300 \text{ V}$
Resistance, $R = 50 \ \Omega$

Since $V_L = V_C = 100 \text{ V}$, the circuit is in a state of resonance. Substituting these values into the voltage equation:

$300 = \sqrt{V_R^2 + (100 - 100)^2}$

$300 = \sqrt{V_R^2 + 0}$

$V_R = 300 \text{ V}$

The current in the circuit (which is the reading of the ammeter) is given by Ohm's law for the resistor:

$I = \dfrac{V_R}{R}$

$I = \dfrac{300}{50} = 6 \text{ A}$

Answer: 6 A

</details>

---

### Q79. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A $20 \Omega$ resistance, 10 mH inductance coil and $15 \mu \mathrm{~F}$ capacitor are joined in series. When a suitable frequency alternating current source is joined to this combination, the circuit resonates. If the resistance is made $\frac{1}{3} \mathrm{rd}$, the resonant frequency

**Options:**

- **(A)** remains unchanged.
- **(B)** is doubled.
- **(C)** is quadrupled.
- **(D)** is halved.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) remains unchanged.**

**Detailed Solution:**

The resonant frequency of a series LCR circuit is given by $f = \dfrac{1}{2\pi\sqrt{LC}}$.

The formula shows that the resonant frequency depends only on the inductance $L$ and the capacitance $C$, and is independent of the resistance $R$ of the circuit.

Therefore, if the resistance is made $\dfrac{1}{3}$rd of its original value, the resonant frequency remains unchanged.

Answer: remains unchanged.

</details>

---

### Q80. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A light bulb connected in series with a capacitor and an a.c. source is glowing with a certain brightness. On reducing the capacity of capacitance and frequency of source, the brightness of the lamp (respectively)

**Options:**

- **(A)** is reduced, is increased
- **(B)** is reduced, is reduced
- **(C)** is increased, is reduced
- **(D)** is increased, is increased

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) is reduced, is reduced**

**Detailed Solution:**

The brightness of the bulb depends on the current $I$ flowing through it.

The current in the series RC circuit is given by $I = \dfrac{V}{Z}$, where the impedance is $Z = \sqrt{R^2 + X_C^2}$ and the capacitive reactance is $X_C = \dfrac{1}{2\pi f C}$.

When the capacitance $C$ is reduced, the capacitive reactance $X_C$ increases. This increases the impedance $Z$, which in turn decreases the current $I$. Hence, the brightness of the bulb is reduced.

Similarly, when the frequency $f$ of the AC source is reduced, the capacitive reactance $X_C$ increases. This again increases the impedance $Z$ and decreases the current $I$. Hence, the brightness of the bulb is reduced.

Therefore, in both cases, the brightness of the lamp is reduced.

Answer: is reduced, is reduced

</details>

---

### Q81. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a series LCR circuit, if ' $V$ ' is the effective value of the applied voltage, $V_R$ is the voltage across ' $R$ ', ' $\mathrm{V}_{\mathrm{L}}$ ' and ' $\mathrm{V}_{\mathrm{C}}$ ' are the effective voltages across ' L ' and ' C ' respectively then

**Options:**

- **(A)** $\mathrm{V}=\mathrm{V}_{\mathrm{R}}+\mathrm{V}_{\mathrm{L}}+\mathrm{V}_{\mathrm{C}}$
- **(B)** $\mathrm{V}^2=\mathrm{V}_{\mathrm{R}}^2+\mathrm{V}_{\mathrm{L}}^2+\mathrm{V}_{\mathrm{C}}^2$
- **(C)** $\mathrm{V}^2=\mathrm{V}_{\mathrm{R}}^2+\left(\mathrm{V}_{\mathrm{L}}-\mathrm{V}_{\mathrm{C}}\right)^2$
- **(D)** $\mathrm{V}^2=\mathrm{V}_{\mathrm{L}}^2+\left(\mathrm{V}_{\mathrm{R}}-\mathrm{V}_{\mathrm{C}}\right)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{V}^2=\mathrm{V}_{\mathrm{R}}^2+\left(\mathrm{V}_{\mathrm{L}}-\mathrm{V}_{\mathrm{C}}\right)^2$**

**Detailed Solution:**

In a series LCR circuit, the current $I$ is the same through all components.

The voltage across the resistor $V_R$ is in phase with the current.

The voltage across the inductor $V_L$ leads the current by $90^\circ$.

The voltage across the capacitor $V_C$ lags the current by $90^\circ$.

Thus, $V_L$ and $V_C$ are $180^\circ$ out of phase, and their resultant is $(V_L - V_C)$.

Since $V_R$ and $(V_L - V_C)$ are perpendicular to each other, the effective applied voltage $V$ is given by the phasor sum:

$V = \sqrt{V_R^2 + (V_L - V_C)^2}$

Squaring both sides, we get:

$V^2 = V_R^2 + (V_L - V_C)^2$

Answer: $\mathrm{V}^2=\mathrm{V}_{\mathrm{R}}^2+\left(\mathrm{V}_{\mathrm{L}}-\mathrm{V}_{\mathrm{C}}\right)^2$

</details>

---

### Q82. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An inductance of 2 mH , a condenser of $20 \mu \mathrm{~F}$ and a resistance of $50 \Omega$ are connected in series to an a.c. source. The reactance of inductor and condenser are same. The reactance of either of them will be

**Options:**

- **(A)** $100 \Omega$
- **(B)** $50 \Omega$
- **(C)** $40 \Omega$
- **(D)** $10 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $10 \Omega$**

**Detailed Solution:**

Given $L = 2 \times 10^{-3} \text{ H}$, $C = 20 \times 10^{-6} \text{ F}$, and $R = 50 \Omega$.

Since the reactance of the inductor and condenser are the same, the circuit is in resonance.

$X_L = X_C$

$\omega L = \dfrac{1}{\omega C}$

$\omega = \dfrac{1}{\sqrt{LC}}$

Substituting the given values:

$\omega = \dfrac{1}{\sqrt{2 \times 10^{-3} \times 20 \times 10^{-6}}} = \dfrac{1}{\sqrt{4 \times 10^{-8}}} = \dfrac{1}{2 \times 10^{-4}} = 5000 \text{ rad/s}$

The reactance of the inductor is:

$X_L = \omega L = 5000 \times 2 \times 10^{-3} = 10 \Omega$

Similarly, the reactance of the condenser is $X_C = 10 \Omega$.

Answer: $10 \Omega$

</details>

---

### Q83. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Which one of the following graph represent correctly the variation of impedance (Z) of a series LCR circuit with the frequency ( $v$ ) of applied a.c.?
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/DsIKqwikRxohrUnQuQdfZq5TIxwxDH_-K0hRHYkMpUI.original.fullsize.png"/>

**Options:**

- **(A)** A
- **(B)** B
- **(C)** C
- **(D)** D

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) B**

**Detailed Solution:**

The impedance $Z$ of a series LCR circuit is given by:

$Z = \sqrt{R^2 + (X_L - X_C)^2}$

Substituting $X_L = 2\pi\nu L$ and $X_C = \dfrac{1}{2\pi\nu C}$, we get:

$Z = \sqrt{R^2 + \left(2\pi\nu L - \dfrac{1}{2\pi\nu C}\right)^2}$

From this expression, we can observe the following:
1. At very low frequencies ($\nu \rightarrow 0$), the capacitive reactance $X_C \rightarrow \infty$, which makes $Z \rightarrow \infty$.
2. At very high frequencies ($\nu \rightarrow \infty$), the inductive reactance $X_L \rightarrow \infty$, which makes $Z \rightarrow \infty$.
3. At the resonant frequency $\nu_r = \dfrac{1}{2\pi\sqrt{LC}}$, $X_L = X_C$, so the impedance is minimum and equal to the resistance ($Z = R$).

Therefore, the graph of $Z$ versus $\nu$ starts from a high value, decreases smoothly to a minimum value $R$ at resonance, and then increases again. Graph (B) correctly represents this variation.

Answer: B

</details>

---

### Q84. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A series $L-C-R$ circuit containing a resistance ' $R$ ' has angular frequency ' $\omega$ '. At resonance the voltage across resistance and inductor are ' $\mathrm{V}_{\mathrm{R}}$ ' and ' $\mathrm{V}_{\mathrm{L}}$ ' respectively, then value of capacitance will be

**Options:**

- **(A)** $\frac{V_R}{V_L \omega R}$
- **(B)** $\frac{V_L}{V_R R \omega^2}$
- **(C)** $\frac{V_R}{V_L R \omega^2}$
- **(D)** $\frac{V_L R}{V_R \omega}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{V_R}{V_L \omega R}$**

**Detailed Solution:**

At resonance, the voltage across the inductor is equal to the voltage across the capacitor.

$V_L = V_C$

The voltage across the capacitor is given by $V_C = I X_C = \dfrac{I}{\omega C}$.

The voltage across the resistor is $V_R = I R$, which gives $I = \dfrac{V_R}{R}$.

Substituting the value of $I$ into the equation for $V_L$, we get:

$V_L = \dfrac{V_R}{R \omega C}$

Rearranging the equation to solve for $C$, we obtain:

$C = \dfrac{V_R}{V_L \omega R}$

Answer: $\frac{V_R}{V_L \omega R}$

</details>

---

### Q85. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When a coil is connected to a d.c. source of e.m.f. 12 volt, then the current of 4 A flows in it. If the same coil is connected to a 12 volt, 50 Hz a.c. source, then the current flowing in it is 2.4 A . Then self-inductance of the coil will be

**Options:**

- **(A)** 48 H
- **(B)** 12 H
- **(C)** $\frac{4}{\pi} \times 10^{-2} \mathrm{H}$
- **(D)** $\frac{8}{\pi} \times 10^{-2} \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{\pi} \times 10^{-2} \mathrm{H}$**

**Detailed Solution:**

For a d.c. source, the coil acts as a pure resistor.

$R = \dfrac{V_{dc}}{I_{dc}} = \dfrac{12}{4} = 3 \, \Omega$

For an a.c. source, the coil acts as an LR circuit with impedance $Z$.

$Z = \dfrac{V_{ac}}{I_{ac}} = \dfrac{12}{2.4} = 5 \, \Omega$

The impedance is given by $Z = \sqrt{R^2 + X_L^2}$

$5 = \sqrt{3^2 + X_L^2}$

$X_L = \sqrt{5^2 - 3^2} = 4 \, \Omega$

The inductive reactance is $X_L = 2\pi f L$

$4 = 2\pi \times 50 \times L$

$L = \dfrac{4}{100\pi} = \dfrac{4}{\pi} \times 10^{-2} \, \text{H}$

Answer: $\frac{4}{\pi} \times 10^{-2} \mathrm{H}$

</details>

---

### Q86. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

When 100 V d.c. is applied across a solenoid, a current of 1 A flows in it. When 100 a.c. is applied across it, the current drops to 0.5 A . If the frequency is 50 Hz , the impedance and inductance is

**Options:**

- **(A)** $200 \Omega, \sqrt{3} / \pi \mathrm{H}$
- **(B)** $100 \Omega, \sqrt{3} \mathrm{H}$
- **(C)** $200 \Omega, 1 \mathrm{H}$
- **(D)** $100 \Omega, 1 \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $200 \Omega, \sqrt{3} / \pi \mathrm{H}$**

**Detailed Solution:**

For d.c. circuit, the resistance of the solenoid is given by:

$R = \dfrac{V_{dc}}{I_{dc}} = \dfrac{100}{1} = 100 \, \Omega$

For a.c. circuit, the impedance of the solenoid is given by:

$Z = \dfrac{V_{ac}}{I_{ac}} = \dfrac{100}{0.5} = 200 \, \Omega$

The impedance is related to resistance and inductive reactance by:

$Z = \sqrt{R^2 + X_L^2}$

$200 = \sqrt{100^2 + X_L^2}$

$X_L^2 = 200^2 - 100^2 = 30000$

$X_L = 100\sqrt{3} \, \Omega$

The inductive reactance is $X_L = 2\pi f L$.

$100\sqrt{3} = 2\pi \times 50 \times L$

$100\sqrt{3} = 100\pi L$

$L = \dfrac{\sqrt{3}}{\pi} \, \text{H}$

Answer: $200 \Omega, \sqrt{3} / \pi \mathrm{H}$

</details>

---

### Q87. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

With gradual increase in frequency of an a.c. supply, the impedance of an LCR series circuit

**Options:**

- **(A)** increases.
- **(B)** decreases.
- **(C)** remains constant
- **(D)** first decreases, becomes minimum and then increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) first decreases, becomes minimum and then increases.**

**Detailed Solution:**

The impedance of an LCR series circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$, where $X_L = 2\pi f L$ and $X_C = \dfrac{1}{2\pi f C}$.

At low frequencies, $X_C$ is very large and $X_L$ is very small, making the impedance $Z$ large.

As the frequency $f$ increases, $X_L$ increases and $X_C$ decreases. The term $(X_L - X_C)^2$ decreases, causing the impedance $Z$ to decrease.

At the resonant frequency $f_r = \dfrac{1}{2\pi\sqrt{LC}}$, $X_L = X_C$, and the impedance becomes minimum, $Z = R$.

As the frequency increases beyond the resonant frequency, $X_L$ becomes greater than $X_C$, and the term $(X_L - X_C)^2$ increases, causing the impedance $Z$ to increase.

Thus, with a gradual increase in frequency, the impedance first decreases, becomes minimum, and then increases.

Answer: first decreases, becomes minimum and then increases.

</details>

---

### Q88. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

With an alternating voltage source frequency ' f ', inductor ' $L$ ', capacitor ' $C$ ' and resistance ' $R$ ' are connected in series. The voltage leads the current by $45^{\circ}$. The value of ' $L$ ' is $\left(\tan 45^{\circ}=1\right)$

**Options:**

- **(A)** $\left(\frac{1+2 \pi \mathrm{fCR}}{4 \pi^2 \mathrm{f}^2 \mathrm{C}}\right)$
- **(B)** $\left(\frac{1-2 \pi \mathrm{fCR}}{4 \pi^2 \mathrm{f}^2 \mathrm{C}}\right)$
- **(C)** $\left(\frac{4 \pi^2 \mathrm{f}^2 \mathrm{C}}{1+2 \pi \mathrm{fCR}}\right)$
- **(D)** $\left(\frac{4 \pi^2 \mathrm{f}^2 \mathrm{C}}{1-2 \pi \mathrm{fCR}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{1+2 \pi \mathrm{fCR}}{4 \pi^2 \mathrm{f}^2 \mathrm{C}}\right)$**

**Detailed Solution:**

In a series LCR circuit, the phase angle $\phi$ by which the voltage leads the current is given by:

$\tan \phi = \dfrac{X_L - X_C}{R}$

Given that the voltage leads the current by $45^{\circ}$, we have $\phi = 45^{\circ}$.

$\tan 45^{\circ} = \dfrac{X_L - X_C}{R}$

Since $\tan 45^{\circ} = 1$, we get:

$1 = \dfrac{X_L - X_C}{R}$

$X_L - X_C = R$

Substituting $X_L = 2\pi f L$ and $X_C = \dfrac{1}{2\pi f C}$:

$2\pi f L - \dfrac{1}{2\pi f C} = R$

$2\pi f L = R + \dfrac{1}{2\pi f C}$

$2\pi f L = \dfrac{2\pi f C R + 1}{2\pi f C}$

$L = \dfrac{1 + 2\pi f C R}{4\pi^2 f^2 C}$

Answer: $\left(\frac{1+2 \pi \mathrm{fCR}}{4 \pi^2 \mathrm{f}^2 \mathrm{C}}\right)$

</details>

---

### Q89. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An inductance of $\frac{300}{\pi} \mathrm{mH}$, a capacitance of $\frac{1}{\pi} \mathrm{mF}$ and a resistance of $20 \Omega$ are connected in series with an a.c. source of $240 \mathrm{~V}, 50 \mathrm{~Hz}$. The phase angle of the circuit is

**Options:**

- **(A)** $\tan ^{-1}(0)$
- **(B)** $\tan ^{-1}\left(\frac{1}{\sqrt{3}}\right)$
- **(C)** $\tan ^{-1}(1)$
- **(D)** $\tan ^{-1}(\sqrt{3})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\tan ^{-1}(1)$**

**Detailed Solution:**

Given:
$L = \dfrac{300}{\pi} \text{ mH} = \dfrac{0.3}{\pi} \text{ H}$
$C = \dfrac{1}{\pi} \text{ mF} = \dfrac{10^{-3}}{\pi} \text{ F}$
$R = 20 \Omega$
$f = 50 \text{ Hz}$

Inductive reactance $X_L$ is given by:
$X_L = 2\pi f L = 2\pi \times 50 \times \dfrac{0.3}{\pi} = 30 \Omega$

Capacitive reactance $X_C$ is given by:
$X_C = \dfrac{1}{2\pi f C} = \dfrac{1}{2\pi \times 50 \times \dfrac{10^{-3}}{\pi}} = \dfrac{1}{0.1} = 10 \Omega$

The phase angle $\phi$ of the circuit is given by:
$\tan \phi = \dfrac{X_L - X_C}{R}$

Substituting the values:
$\tan \phi = \dfrac{30 - 10}{20} = \dfrac{20}{20} = 1$

$\phi = \tan^{-1}(1)$

Answer: $\tan ^{-1}(1)$

</details>

---

### Q90. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the series LCR circuit, $R=\dfrac{X_L}{2}=2 X_c$. The impedance of the circuit and the phase difference between V and I will be

**Options:**

- **(A)** $\dfrac{\sqrt{5}}{2} \mathrm{R}, \tan ^{-1}\left(\dfrac{1}{2}\right)$
- **(B)** $\dfrac{\sqrt{13}}{2} R, \tan ^{-1}\left(\dfrac{3}{2}\right)$
- **(C)** $\sqrt{5} R, \tan ^{-1}(1)$
- **(D)** $\sqrt{13} \mathrm{R}, \tan ^{-1}(2)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\sqrt{13}}{2} R, \tan ^{-1}\left(\dfrac{3}{2}\right)$**

**Detailed Solution:**

Given $R = \dfrac{X_L}{2} = 2 X_C$

$X_L = 2R$

$X_C = \dfrac{R}{2}$

The impedance of the series LCR circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$

Substituting the values of $X_L$ and $X_C$:

$Z = \sqrt{R^2 + \left(2R - \dfrac{R}{2}\right)^2}$

$Z = \sqrt{R^2 + \left(\dfrac{3R}{2}\right)^2} = \sqrt{R^2 + \dfrac{9R^2}{4}} = \dfrac{\sqrt{13}}{2} R$

The phase difference $\phi$ is given by $\tan \phi = \dfrac{X_L - X_C}{R}$

$\tan \phi = \dfrac{2R - \dfrac{R}{2}}{R} = \dfrac{3}{2}$

$\phi = \tan^{-1}\left(\dfrac{3}{2}\right)$

Answer: $\dfrac{\sqrt{13}}{2} R, \tan ^{-1}\left(\dfrac{3}{2}\right)$

</details>

---

### Q91. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In series LCR circuit, 'R' represents resistance of electric bulb. If the frequency of a.c. supply is doubled, in order to keep the brightness of the bulb unchanged, the value of inductance ' L ' and capacitance ' C ' should be

**Options:**

- **(A)** both doubled.
- **(B)** made four times.
- **(C)** made eight times.
- **(D)** both halved simultaneously.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) both halved simultaneously.**

**Detailed Solution:**

The brightness of the bulb depends on the power dissipated across its resistance $R$, which is given by $P = I^2 R$.

For the brightness to remain unchanged, the current $I$ in the circuit must remain constant.

The current in a series LCR circuit is given by:

$I = \dfrac{V}{Z} = \dfrac{V}{\sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}}$

For $I$ to remain unchanged when the frequency $\omega$ is doubled ($\omega' = 2\omega$), the inductive reactance $X_L$ and capacitive reactance $X_C$ must individually remain unchanged.

For inductive reactance:

$\omega' L' = \omega L$

$(2\omega) L' = \omega L \Rightarrow L' = \dfrac{L}{2}$

For capacitive reactance:

$\dfrac{1}{\omega' C'} = \dfrac{1}{\omega C}$

$\dfrac{1}{(2\omega) C'} = \dfrac{1}{\omega C} \Rightarrow C' = \dfrac{C}{2}$

Thus, both inductance $L$ and capacitance $C$ should be halved simultaneously.

Answer: both halved simultaneously.

</details>

---

### Q92. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An a.c. voltage source $\mathrm{V}=\mathrm{V}_0 \sin \omega \mathrm{t}$. is connected across resistance ' R ' and capacitance ' $C$ ' in series. It is given that $R=\dfrac{1}{\omega \mathrm{c}}$ and the peak current is $\mathrm{I}_0$. If the angular frequency of the voltage source is changed to $\left(\dfrac{\omega}{\sqrt{3}}\right)$, then the new peak current in the circuit is

**Options:**

- **(A)** $\dfrac{\mathrm{I}_0}{2}$
- **(B)** $\dfrac{\mathrm{I}_0}{\sqrt{2}}$
- **(C)** $\sqrt{2} \mathrm{I}_0$
- **(D)** $\sqrt{3} \mathrm{I}_0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\mathrm{I}_0}{\sqrt{2}}$**

**Detailed Solution:**

The initial impedance of the circuit is given by $Z_1 = \sqrt{R^2 + X_C^2}$.

Given $X_C = \dfrac{1}{\omega C} = R$, we get $Z_1 = \sqrt{R^2 + R^2} = \sqrt{2}R$.

The initial peak current is $I_0 = \dfrac{V_0}{Z_1} = \dfrac{V_0}{\sqrt{2}R}$.

When the angular frequency is changed to $\omega' = \dfrac{\omega}{\sqrt{3}}$, the new capacitive reactance becomes $X_C' = \dfrac{1}{\omega' C} = \dfrac{\sqrt{3}}{\omega C} = \sqrt{3}R$.

The new impedance of the circuit is $Z_2 = \sqrt{R^2 + (X_C')^2} = \sqrt{R^2 + (\sqrt{3}R)^2} = \sqrt{4R^2} = 2R$.

The new peak current is $I_0' = \dfrac{V_0}{Z_2} = \dfrac{V_0}{2R}$.

Substituting $V_0 = \sqrt{2} R I_0$ from the initial case, we get:

$I_0' = \dfrac{\sqrt{2} R I_0}{2R} = \dfrac{I_0}{\sqrt{2}}$

Answer: $\dfrac{\mathrm{I}_0}{\sqrt{2}}$

</details>

---

### Q93. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The current in LR circuit if reduced to half. What will be the energy stored in it?

**Options:**

- **(A)** 4 times
- **(B)** 2 times
- **(C)** half times
- **(D)** $\left(\dfrac{1}{4}\right)^{\text {th }}$ times

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\dfrac{1}{4}\right)^{\text {th }}$ times**

**Detailed Solution:**

The energy stored in an inductor in an LR circuit is given by $U = \dfrac{1}{2} L I^2$.

When the current is reduced to half, the new current is $I' = \dfrac{I}{2}$.

The new energy stored becomes:

$U' = \dfrac{1}{2} L (I')^2$

$U' = \dfrac{1}{2} L \left(\dfrac{I}{2}\right)^2$

$U' = \dfrac{1}{4} \left(\dfrac{1}{2} L I^2\right)$

$U' = \dfrac{1}{4} U$

Thus, the energy stored becomes $\left(\dfrac{1}{4}\right)^{\text{th}}$ times the original energy.

Answer: $\left(\dfrac{1}{4}\right)^{\text {th }}$ times

</details>

---

### Q94. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The inductive reactance of a coil is ' R ' $\Omega$. If inductance of a coil is tripled and frequency of a.c supply is also tripled, then new inductive reactance will be

**Options:**

- **(A)** $\dfrac{\mathrm{R}}{9}$
- **(B)** $\dfrac{\mathrm{R}}{3}$
- **(C)** 3 R
- **(D)** 9 R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9 R**

**Detailed Solution:**

Inductive reactance is given by $X_L = \omega L = 2 \pi f L$

Initially, $X_L = R$

When inductance is tripled, $L' = 3L$

When frequency is tripled, $f' = 3f$

New inductive reactance $X_L' = 2 \pi f' L' = 2 \pi (3f) (3L) = 9 (2 \pi f L)$

$X_L' = 9 X_L = 9R$

Answer: 9 R

</details>

---

### Q95. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A series resonant circuit consists of inductor ' $L$ ' of negligible resistance and a capacitor ' C ' which produces resonant frequency ' f '. If L is changed to 3 L and ' C ' is changed to 6 C , the resonant frequency will become.

**Options:**

- **(A)** $\dfrac{\mathrm{f}}{6}$
- **(B)** $\dfrac{\mathrm{f}}{3}$
- **(C)** $\dfrac{\mathrm{f}}{2 \sqrt{2}}$
- **(D)** $\dfrac{\mathrm{f}}{3 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\mathrm{f}}{3 \sqrt{2}}$**

**Detailed Solution:**

The resonant frequency of a series L-C circuit is given by:

$f = \dfrac{1}{2\pi\sqrt{LC}}$

When the inductance is changed to $L' = 3L$ and capacitance is changed to $C' = 6C$, the new resonant frequency $f'$ becomes:

$f' = \dfrac{1}{2\pi\sqrt{L'C'}}$

$f' = \dfrac{1}{2\pi\sqrt{(3L)(6C)}}$

$f' = \dfrac{1}{2\pi\sqrt{18LC}}$

$f' = \dfrac{1}{3\sqrt{2}} \left( \dfrac{1}{2\pi\sqrt{LC}} \right)$

$f' = \dfrac{f}{3\sqrt{2}}$

Answer: $\dfrac{\mathrm{f}}{3 \sqrt{2}}$

</details>

---

### Q96. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

When a capacitor is connected in a series LR circuit to achieve resonance, the alternating current flowing in the circuit

**Options:**

- **(A)** is zero.
- **(B)** remains constant.
- **(C)** increases.
- **(D)** decreases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) increases.**

**Detailed Solution:**

The initial impedance of the series LR circuit is given by $Z_1 = \sqrt{R^2 + X_L^2}$.

When a capacitor is connected in series to achieve resonance, the capacitive reactance becomes equal to the inductive reactance, i.e., $X_C = X_L$.

The new impedance of the circuit is $Z_2 = \sqrt{R^2 + (X_L - X_C)^2} = R$.

Since $R < \sqrt{R^2 + X_L^2}$, the impedance of the circuit decreases ($Z_2 < Z_1$).

The alternating current in the circuit is given by $I = \dfrac{V}{Z}$.

As the impedance decreases, the current flowing in the circuit increases.

Answer: increases.

</details>

---

### Q97. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit diagram, in the steady state the current through the battery and the charge on the capacitor respectively are
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/EsD73js-2RP2Y9k-Cylu_YQCGdxQhVlGdb713udjtOs.original.fullsize.png"/>

**Options:**

- **(A)** 2 A and $3 \mu \mathrm{C}$
- **(B)** $\dfrac{6}{11} \mathrm{~A}$ and $\dfrac{12}{7} \mu \mathrm{C}$
- **(C)** 11 A and $3 \mu \mathrm{C}$
- **(D)** zero ampere and $3 \mu \mathrm{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 11 A and $3 \mu \mathrm{C}$**

**Detailed Solution:**

In the steady state, the capacitor acts as an open circuit, so no current flows through the branch containing the capacitor and the $4\ \Omega$ resistor.

The current from the battery flows only through the $1\ \Omega$, $2\ \Omega$, and $3\ \Omega$ resistors. These three resistors are connected in parallel across the $6\ \mathrm{V}$ battery.

The equivalent resistance $R_{eq}$ of this parallel combination is given by:
$\dfrac{1}{R_{eq}} = \dfrac{1}{1} + \dfrac{1}{2} + \dfrac{1}{3} = \dfrac{6 + 3 + 2}{6} = \dfrac{11}{6}\ \Omega^{-1}$

Thus, $R_{eq} = \dfrac{6}{11}\ \Omega$.

The steady state current $I$ through the battery is:
$I = \dfrac{V}{R_{eq}} = \dfrac{6}{6/11} = 11\ \mathrm{A}$

Since the capacitor branch is connected in parallel with the battery, the potential difference across this entire branch is $6\ \mathrm{V}$. As the steady state current through this branch is zero, the potential drop across the $4\ \Omega$ resistor is zero.

Therefore, the potential difference across the capacitor is equal to the battery voltage, which is $6\ \mathrm{V}$.

The charge $Q$ on the capacitor is:
$Q = C \times V = 0.5\ \mu\mathrm{F} \times 6\ \mathrm{V} = 3\ \mu\mathrm{C}$

Answer: 11 A and $3 \mu \mathrm{C}$

</details>

---

### Q98. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When a capacitor is connected in a series LR circuit such that the circuit resonates, the alternating current flowing in the circuit

**Options:**

- **(A)** is zero
- **(B)** increases
- **(C)** decreases
- **(D)** remains constant

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) increases**

**Detailed Solution:**

Initially, for the series LR circuit, the impedance is given by $Z_1 = \sqrt{R^2 + X_L^2}$.

The alternating current flowing in the circuit is $I_1 = \dfrac{V}{Z_1} = \dfrac{V}{\sqrt{R^2 + X_L^2}}$.

When a capacitor is connected in series such that the circuit resonates, the inductive reactance equals the capacitive reactance ($X_L = X_C$).

The new impedance of the circuit becomes $Z_2 = \sqrt{R^2 + (X_L - X_C)^2} = R$.

Since $Z_2 < Z_1$, the impedance of the circuit decreases.

Therefore, the new current $I_2 = \dfrac{V}{R}$ is greater than $I_1$, meaning the alternating current flowing in the circuit increases.

Answer: increases

</details>

---

### Q99. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

LC series resonant circuit produces resonant frequency ' f '. If. ' L ' is tripled and ' C ' is increased by 3C, the resonant frequency will be

**Options:**

- **(A)** $\dfrac{\mathrm{f}}{3}$
- **(B)** $\dfrac{\mathrm{f}}{2 \sqrt{3}}$
- **(C)** 6 f
- **(D)** $\dfrac{\mathrm{f}}{2 \sqrt{2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{\mathrm{f}}{2 \sqrt{3}}$**

**Detailed Solution:**

The resonant frequency of an LC series circuit is given by:

$f = \dfrac{1}{2\pi\sqrt{LC}}$

Given that the inductance is tripled, the new inductance is:

$L' = 3L$

The capacitance is increased by $3C$, so the new capacitance is:

$C' = C + 3C = 4C$

The new resonant frequency $f'$ is:

$f' = \dfrac{1}{2\pi\sqrt{L'C'}}$

Substituting the values of $L'$ and $C'$:

$f' = \dfrac{1}{2\pi\sqrt{(3L)(4C)}}$

$f' = \dfrac{1}{2\pi\sqrt{12LC}}$

$f' = \dfrac{1}{2\sqrt{3}} \left(\dfrac{1}{2\pi\sqrt{LC}}\right)$

$f' = \dfrac{f}{2\sqrt{3}}$

Answer: $\dfrac{\mathrm{f}}{2 \sqrt{3}}$

</details>

---

### Q100. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In series LCR resonant circuit; the capacitance is changed from C to 3 C . To obtain the same resonant frequency, the inductance should be changed from $L$ to

**Options:**

- **(A)** $\dfrac{\mathrm{L}}{3}$
- **(B)** $\dfrac{\mathrm{L}}{2}$
- **(C)** $\dfrac{\mathrm{L}}{\sqrt{3}}$
- **(D)** 3 L

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{\mathrm{L}}{3}$**

**Detailed Solution:**

The resonant frequency of a series LCR circuit is given by $f = \dfrac{1}{2\pi\sqrt{LC}}$.

For the resonant frequency to remain the same, the product of inductance and capacitance must remain constant.

$L_1 C_1 = L_2 C_2$

Given $L_1 = L$, $C_1 = C$, and $C_2 = 3C$.

$L \times C = L_2 \times 3C$

$L_2 = \dfrac{L}{3}$

Answer: $\dfrac{\mathrm{L}}{3}$

</details>

---

### Q101. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An inductor of inductance $2 \mu \mathrm{H}$ is connected in series with a resistance, a variable capacitor and an a.c. source of frequency 5 kHz . The value of capacitance for which maximum current is drawn into the circuit is $\dfrac{1}{\mathrm{x}} \mathrm{F}$, where the value of
' $x$ ' is (Take $\pi^2=10$ )

**Options:**

- **(A)** 500
- **(B)** 1000
- **(C)** 2000
- **(D)** 4000

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2000**

**Detailed Solution:**

For maximum current in an LCR series circuit, the circuit must be in resonance.

At resonance, the inductive reactance equals the capacitive reactance:

$\omega L = \dfrac{1}{\omega C}$

$C = \dfrac{1}{\omega^2 L} = \dfrac{1}{(2\pi f)^2 L}$

Given $f = 5 \times 10^3 \text{ Hz}$ and $L = 2 \times 10^{-6} \text{ H}$:

$C = \dfrac{1}{(2\pi \times 5 \times 10^3)^2 \times 2 \times 10^{-6}}$

$C = \dfrac{1}{10^8 \pi^2 \times 2 \times 10^{-6}}$

Using $\pi^2 = 10$, we get:

$C = \dfrac{1}{10^8 \times 10 \times 2 \times 10^{-6}} = \dfrac{1}{2 \times 10^3} = \dfrac{1}{2000} \text{ F}$

Comparing with $C = \dfrac{1}{x} \text{ F}$, we get $x = 2000$.

Answer: 2000

</details>

---

### Q102. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In LCR series circuit if the frequency is increased, the impedance of the circuit

**Options:**

- **(A)** increases
- **(B)** decreases
- **(C)** either increases or decreases
- **(D)** first decreases then become minimum and then increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) first decreases then become minimum and then increases.**

**Detailed Solution:**

The impedance of an LCR series circuit is given by $Z = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}$, where $\omega = 2\pi f$.

At low frequencies, the capacitive reactance $X_C = \dfrac{1}{\omega C}$ is very large and the inductive reactance $X_L = \omega L$ is very small. As the frequency $f$ increases, $X_C$ decreases and $X_L$ increases, which causes the net reactance $(X_L - X_C)$ to decrease in magnitude. Consequently, the impedance $Z$ decreases.

At the resonant frequency $f_r = \dfrac{1}{2\pi\sqrt{LC}}$, $X_L = X_C$, making the net reactance zero. At this point, the impedance becomes minimum and is equal to the resistance $R$ ($Z = R$).

If the frequency is increased further beyond resonance, $X_L$ becomes greater than $X_C$. The net reactance $(X_L - X_C)$ increases in magnitude, which causes the impedance $Z$ to increase.

Therefore, as the frequency is increased, the impedance first decreases, becomes minimum, and then increases.

Answer: first decreases then become minimum and then increases.

</details>

---

### Q103. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the given figure, choose the correct option.
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/oA94qwXSzYaggGHlPKY550jzIS218Y25MNk92L5mfT4.original.fullsize.png"/>

**Options:**

- **(A)** The r.m.s. current in circuit (B)
can never be greater than that in circuit (A)
- **(B)** The r.m.s. current in circuit (A)
is always equal to that in circuit (B)
- **(C)** The r.m.s. current in circuit (B)
can be greater than in circuit (A)
- **(D)** At resonance, current in (B)
is less than that in circuit (A)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) The r.m.s. current in circuit (B)
can never be greater than that in circuit (A)**

**Detailed Solution:**

For circuit (A), which is a purely resistive circuit, the impedance is:

$Z_A = R = 40\ \Omega$

The r.m.s. current in circuit (A) is:

$I_A = \dfrac{V_{rms}}{Z_A} = \dfrac{V_{rms}}{R}$

For circuit (B), which is a series LCR circuit, the impedance is given by:

$Z_B = \sqrt{R^2 + (X_L - X_C)^2}$

The r.m.s. current in circuit (B) is:

$I_B = \dfrac{V_{rms}}{Z_B} = \dfrac{V_{rms}}{\sqrt{R^2 + (X_L - X_C)^2}}$

Since the square of any real number is non-negative, $(X_L - X_C)^2 \ge 0$. This implies that the impedance of circuit (B) is always greater than or equal to the resistance $R$:

$Z_B \ge R$

Therefore, the current in circuit (B) will always be less than or equal to the current in circuit (A):

$I_B \le I_A$

The equality holds only at resonance (when $X_L = X_C$). Thus, the r.m.s. current in circuit (B) can never be greater than that in circuit (A).

Answer: The r.m.s. current in circuit (B)
can never be greater than that in circuit (A)

</details>

---

### Q104. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A series LCR circuit containing a resistance 'R' has angular frequency ' $\omega$ '. At resonance the voltage across resistance and inductor are ' $\mathrm{V}_{\mathrm{R}}$ ' and ' $\mathrm{V}_{\mathrm{L}}$ ' respectively, then value of inductance 'L' will be

**Options:**

- **(A)** $\dfrac{V_R R}{V_L \omega}$
- **(B)** $\dfrac{V_L}{V_R R \omega}$
- **(C)** $\dfrac{V_R \omega}{V_L R}$
- **(D)** $\dfrac{\mathrm{V}_{\mathrm{L}} \mathrm{R}}{\mathrm{V}_{\mathrm{R}}(\omega)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{\mathrm{V}_{\mathrm{L}} \mathrm{R}}{\mathrm{V}_{\mathrm{R}}(\omega)}$**

**Detailed Solution:**

In a series LCR circuit, the same current $I$ flows through all the components.

The voltage across the resistance is given by $V_R = I R$, which gives $I = \dfrac{V_R}{R}$.

The voltage across the inductor is given by $V_L = I X_L = I \omega L$.

Substituting the value of $I$ in the expression for $V_L$, we get:

$V_L = \left(\dfrac{V_R}{R}\right) \omega L$

Rearranging the above equation to solve for $L$, we get:

$L = \dfrac{V_L R}{V_R \omega}$

Answer: $\dfrac{\mathrm{V}_{\mathrm{L}} \mathrm{R}}{\mathrm{V}_{\mathrm{R}}(\omega)}$

</details>

---

### Q105. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

When 80 volt d.c. is applied across a solenoid, a current of 0.8 A flows in it. When 80 volt a.c. is applied across the same solenoid, the current becomes 0.4 A . If the frequency of a.c. source is 50 Hz , the impedance and inductance of the solenoid is nearly

**Options:**

- **(A)** $200 \Omega, 0.55 \mathrm{H}$
- **(B)** $100 \Omega, 0.8 \mathrm{H}$
- **(C)** $300 \Omega, 1.2 \mathrm{H}$
- **(D)** $200 \Omega, 1.5 \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $200 \Omega, 0.55 \mathrm{H}$**

**Detailed Solution:**

For d.c. circuit, the frequency is zero, so the inductive reactance is zero. The resistance of the solenoid is given by:

$R = \dfrac{V_{dc}}{I_{dc}} = \dfrac{80}{0.8} = 100 \, \Omega$

For a.c. circuit, the impedance of the solenoid is given by:

$Z = \dfrac{V_{ac}}{I_{ac}} = \dfrac{80}{0.4} = 200 \, \Omega$

The impedance of the solenoid is related to its resistance and inductive reactance by:

$Z = \sqrt{R^2 + X_L^2}$

$200 = \sqrt{100^2 + X_L^2}$

$X_L^2 = 200^2 - 100^2 = 30000$

$X_L = 100\sqrt{3} \, \Omega$

The inductive reactance is also given by $X_L = 2\pi f L$. Substituting the given values:

$100\sqrt{3} = 2\pi(50)L$

$100\sqrt{3} = 100\pi L$

$L = \dfrac{\sqrt{3}}{\pi} \approx \dfrac{1.732}{3.14} \approx 0.55 \, \text{H}$

Answer: $200 \Omega, 0.55 \mathrm{H}$

</details>

---

### Q106. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An inductance coil has a resistance of $80 \Omega$. When on AC signal of frequency 480 Hz is applied to the coil, the voltage leads the current by $45^{\circ}$. The inductance of the coil in henry is $\left[\sin 45^{\circ}=\cos 45^{\circ}=1 / \sqrt{2}\right]$

**Options:**

- **(A)** $\dfrac{1}{24 \pi}$
- **(B)** $\dfrac{\pi}{20}$
- **(C)** $\dfrac{\pi}{40}$
- **(D)** $\dfrac{1}{12 \pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{12 \pi}$**

**Detailed Solution:**

Given $R = 80 \Omega$, $f = 480 \text{ Hz}$, and phase angle $\phi = 45^{\circ}$.

In an RL circuit, the phase angle $\phi$ is given by $\tan \phi = \dfrac{X_L}{R} = \dfrac{\omega L}{R}$.

Substituting the given values:

$\tan 45^{\circ} = \dfrac{2 \pi f L}{R}$

$1 = \dfrac{2 \pi \times 480 \times L}{80}$

$80 = 960 \pi L$

$L = \dfrac{80}{960 \pi} = \dfrac{1}{12 \pi} \text{ H}$

Answer: $\dfrac{1}{12 \pi}$

</details>

---

### Q107. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An alternating voltage $v=200 \sqrt{2} \sin (100 t)$ is connected to a $1 \mu \mathrm{~F}$ capacitor through an a. c. ammeter. The reading of the ammeter shall be

**Options:**

- **(A)** 10 mA
- **(B)** 20 mA
- **(C)** 40 mA
- **(D)** 80 mA

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 20 mA**

**Detailed Solution:**

Given alternating voltage is $v = 200 \sqrt{2} \sin(100 t)$.

Comparing with the standard equation $v = V_0 \sin(\omega t)$, we get:

Peak voltage, $V_0 = 200 \sqrt{2}$ V

Angular frequency, $\omega = 100$ rad/s

The RMS voltage is given by:

$V_{\text{rms}} = \dfrac{V_0}{\sqrt{2}} = \dfrac{200 \sqrt{2}}{\sqrt{2}} = 200$ V

The capacitive reactance is:

$X_C = \dfrac{1}{\omega C} = \dfrac{1}{100 \times 10^{-6}} = 10^4 \, \Omega$

The reading of an a.c. ammeter is the RMS value of the current, which is:

$I_{\text{rms}} = \dfrac{V_{\text{rms}}}{X_C} = \dfrac{200}{10^4} = 2 \times 10^{-2}$ A

$I_{\text{rms}} = 20$ mA

Answer: 20 mA

</details>

---

### Q108. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

$\mathrm{L}=2 \mathrm{H}, \mathrm{C}=5 \mathrm{mF}$ and $\mathrm{R}=12 \Omega$ are connected in series to an a.c. generator of frequency 50 Hz . Then

**Options:**

- **(A)** at resonance, impedance of the circuit is zero.
- **(B)** at resonance, impedance of the circuit is $12 \Omega$.
- **(C)** the resonant frequency of the circuit is $1 / 2 \pi$.
- **(D)** the inductive reactance is less than the capacitive reactance.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) at resonance, impedance of the circuit is $12 \Omega$.**

**Detailed Solution:**

The impedance of a series LCR circuit is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$.

At resonance, the inductive reactance $X_L$ and capacitive reactance $X_C$ are equal, meaning $X_L = X_C$.

Substituting this into the impedance formula gives $Z = \sqrt{R^2 + 0} = R$.

Given $R = 12 \Omega$, the impedance of the circuit at resonance is $12 \Omega$.

To verify the other options:

The resonant frequency is $f_r = \dfrac{1}{2\pi\sqrt{LC}} = \dfrac{1}{2\pi\sqrt{2 \times 5 \times 10^{-3}}} = \dfrac{1}{2\pi\sqrt{10^{-2}}} = \dfrac{5}{\pi} \text{ Hz}$.

At the given frequency $f = 50 \text{ Hz}$, the reactances are:

$X_L = 2\pi f L = 2\pi(50)(2) = 200\pi \Omega$

$X_C = \dfrac{1}{2\pi f C} = \dfrac{1}{2\pi(50)(5 \times 10^{-3})} = \dfrac{2}{\pi} \Omega$

Clearly, $X_L > X_C$, so the inductive reactance is greater than the capacitive reactance.

Answer: at resonance, impedance of the circuit is $12 \Omega$.

</details>

---

### Q109. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In the given circuit, when $\mathrm{S}_1$ is closed, the capacitor gets fully charged. Now $\mathrm{S}_1$ is open and $\mathrm{S}_2$ is closed. Then
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/RGnuft13k4-o6X2aEfCmyDhuvNRIz2ftdXXWfkrNG7I.original.fullsize.png"/>

**Options:**

- **(A)** there is no exchange of energy between L and C .
- **(B)** the current in the circuit is in the same direction.
- **(C)** the instantaneous current in the circuit may be $\mathrm{V}\left(\sqrt{\dfrac{\mathrm{C}}{\mathrm{L}}}\right)$.
- **(D)** the energy stored in the circuit is purely in the form of magnetic energy.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) the instantaneous current in the circuit may be $\mathrm{V}\left(\sqrt{\dfrac{\mathrm{C}}{\mathrm{L}}}\right)$.**

**Detailed Solution:**

When switch $\mathrm{S}_1$ is closed and $\mathrm{S}_2$ is open, the capacitor $\mathrm{C}$ is connected in series with the battery $\mathrm{V}$ and resistor $\mathrm{R}$.

In the steady state, the capacitor is fully charged and acts as an open circuit. The current in the circuit becomes zero.

The potential difference across the capacitor is equal to the battery voltage $\mathrm{V}$.

The initial energy stored in the capacitor is purely electrical, given by $U_E = \dfrac{1}{2}\mathrm{C}\mathrm{V}^2$.

When $\mathrm{S}_1$ is opened and $\mathrm{S}_2$ is closed, the battery and resistor are disconnected. The capacitor $\mathrm{C}$ and inductor $\mathrm{L}$ form a closed $\mathrm{LC}$ circuit.

The circuit will undergo $\mathrm{LC}$ oscillations where energy continuously exchanges between the electric field of the capacitor and the magnetic field of the inductor.

By the principle of conservation of energy, the maximum magnetic energy stored in the inductor is equal to the initial electrical energy stored in the capacitor:

$\dfrac{1}{2}\mathrm{L}I_{\text{max}}^2 = \dfrac{1}{2}\mathrm{C}\mathrm{V}^2$

$I_{\text{max}}^2 = \dfrac{\mathrm{C}}{\mathrm{L}}\mathrm{V}^2$

$I_{\text{max}} = \mathrm{V}\sqrt{\dfrac{\mathrm{C}}{\mathrm{L}}}$

The instantaneous current $i$ in the $\mathrm{LC}$ circuit oscillates sinusoidally, so its value varies between $-I_{\text{max}}$ and $+I_{\text{max}}$.

Therefore, the instantaneous current may be equal to its maximum value, $\mathrm{V}\sqrt{\dfrac{\mathrm{C}}{\mathrm{L}}}$.

Answer: the instantaneous current in the circuit may be $\mathrm{V}\left(\sqrt{\dfrac{\mathrm{C}}{\mathrm{L}}}\right)$.

</details>

---

### Q110. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The reciprocal of the total effective resistance of LCR a.c. circuit is called

**Options:**

- **(A)** impedance
- **(B)** admittance
- **(C)** resistance
- **(D)** inductive and capacitive reactance

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) admittance**

**Detailed Solution:**

Std.12 $\mid$ Ch-13 $\mid$ Subtopic-13.5

</details>

---

### Q111. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An alternating voltage is applied to a series LCR circuit. If the current leads the voltage by $45^{\circ}$, then $\left(\tan 45^{\circ}=1\right)$

**Options:**

- **(A)** $X_L=X_C-R$
- **(B)** $X_L=X_C+R$
- **(C)** $X_C=\sqrt{X_L^2+R^2}$
- **(D)** $\mathrm{X}_{\mathrm{L}}=\sqrt{\mathrm{X}_{\mathrm{C}}^2+\mathrm{R}^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $X_L=X_C+R$**

**Detailed Solution:**

The phase between the voltage and the current is given as
$$
\begin{array}{ll} 
& \tan \phi=\frac{X_L-X_C}{R} \\
\therefore \quad & \tan 45^{\circ}=\frac{X_L-X_C}{R} \\
\therefore \quad & 1=\frac{X_L-X_C}{R} \\
\therefore \quad & R=X_L-X_C \\
\therefore \quad & X_L=X_C+R
\end{array}
$$

</details>

---

### Q112. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a $\mathrm{L}-\mathrm{R}$ circuit, the inductive reactance is equal to the resistance ' $R$ ' in the circuit. An emf $\mathrm{E}=\mathrm{E}_0 \cos \omega \mathrm{t}$ is applied to the circuit. The power consumed in the circuit is

**Options:**

- **(A)** $\frac{\mathrm{E}_0^2}{\sqrt{2} \mathrm{R}}$
- **(B)** $\frac{E_0^2}{4 R}$
- **(C)** $\frac{\mathrm{E}_0^2}{2 \mathrm{R}}$
- **(D)** $\frac{\mathrm{E}_0^2}{8 \mathrm{R}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{E_0^2}{4 R}$**

**Detailed Solution:**

$\mathrm{P}=\mathrm{E}_{\mathrm{rms}} \mathrm{I}_{\mathrm{rms}} \cos \phi$
$\cos \phi=\frac{R}{Z}$
Also, $I_{\text {rms }}=\frac{E_{\text {rms }}}{Z}=\frac{E_0}{Z \sqrt{2}}$
$\therefore \quad P=\frac{E_0}{\sqrt{2}} \times \frac{E_0}{Z \sqrt{2}} \times \frac{R}{Z}$
$=\frac{E_0^2 R}{2 Z^2}$
Given $X_L=R$
$\therefore \quad \mathrm{Z}=\sqrt{\mathrm{R}^2+\mathrm{R}^2}$
$=\sqrt{2} \mathrm{R}$
$\therefore \quad P=\frac{E_0^2}{4 R}$

</details>

---

### Q113. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

With increase in frequency of a.c. supply, the impedance of an $\mathrm{L}-\mathrm{C}$-R series circuit

**Options:**

- **(A)** remains constant.
- **(B)** increases.
- **(C)** decreases.
- **(D)** decreases at first, becomes minimum and then increases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreases at first, becomes minimum and then increases.**

**Detailed Solution:**

We know
$\mathrm{X}_{\mathrm{L}}=\mathrm{L} \omega$ and $\mathrm{X}_{\mathrm{C}}=\frac{1}{\mathrm{C} \omega}$
$\Rightarrow$ When the frequency increases, $X_{\mathrm{L}}^{\prime}$ increases and $X_c$ decreases.
$\therefore \quad$ The impédance of an LCR series circuit decreases at first, becomes minimum and then increases.

</details>

---

### Q114. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an oscillating LC circuit, the maximum charge on the capacitor is 'Q'. 'When the energy is stored equally between the electric and magnetic fields, the charge on the capacitor becomes

**Options:**

- **(A)** $\frac{\mathrm{Q}}{4}$
- **(B)** $\frac{\mathrm{Q}}{2}$
- **(C)** $\frac{\mathrm{Q}}{\sqrt{2}}$
- **(D)** $\frac{\mathrm{Q}}{\sqrt{3}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{Q}}{\sqrt{2}}$**

**Detailed Solution:**

Maximum energy stored in a capacitor,
$$
\mathrm{E}_1=\frac{\mathrm{Q}^2}{2 \mathrm{C}}
$$
When energy is stored equally between the electric and magnetic fields, then energy in the capacitor is $\mathrm{E}_2=\frac{1}{2} \mathrm{E}_1$
If $\mathrm{Q}^{\prime}$ is the charge on the capacitor in this case, then $\mathrm{E}_2=\frac{\mathrm{Q}^{\prime 2}}{2 \mathrm{C}}$.
$$
\begin{aligned}
\therefore \quad & \frac{\mathrm{Q}^{\prime 2}}{2 \mathrm{C}}=\frac{1}{2} \frac{\mathrm{Q}^2}{2 \mathrm{C}} \\
& \mathrm{Q}^{\prime}=\frac{\mathrm{Q}}{\sqrt{2}} .
\end{aligned}
$$

</details>

---

### Q115. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a series LCR circuit, $\mathrm{C}=2 \mu \mathrm{F}, \mathrm{L}=1 \mathrm{mH}$ and $\mathrm{R}=10 \Omega$. The ratio of the energies stored in the inductor and the capacitor, when the maximum current flows in the circuit, is

**Options:**

- **(A)** $5: 1$
- **(B)** $3: 2$
- **(C)** $1: 2$
- **(D)** $1: 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5: 1$**

**Detailed Solution:**

In resonance condition (current is maximum),
$\therefore \quad \mathrm{X}_{\mathrm{c}}=\mathrm{X}_{\mathrm{L}}$
$\therefore \quad$ The ratio of energies in the inductor and capacitor is:
$\begin{aligned}
& \frac{\mathrm{U}_{\mathrm{L}}}{\mathrm{U}_{\mathrm{C}}}=\frac{\mathrm{LI}^2}{\mathrm{CV}^2}=\frac{\mathrm{L}}{\mathrm{CR}^2} \quad \ldots\left(\because \frac{\mathrm{I}}{\mathrm{V}}=\frac{1}{\mathrm{R}}\right) \\
& \frac{\mathrm{U}_{\mathrm{L}}}{\mathrm{U}_{\mathrm{C}}}=\frac{10^{-3}}{2 \times 10^{-6} \times 10^2} \\
& \frac{\mathrm{U}_{\mathrm{L}}}{\mathrm{U}_{\mathrm{C}}}=\frac{5}{1}
\end{aligned}$

</details>

---

### Q116. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The a.c. source is connected to series LCR circuit. If voltage across $\mathrm{R}$ is $40 \mathrm{~V}$, that across $\mathrm{L}$ is $80 \mathrm{~V}$ and that across $\mathrm{C}$ is $40 \mathrm{~V}$, then the e.m.f. 'e' of a.c. source is

**Options:**

- **(A)** $40 \mathrm{~V}$
- **(B)** $40 \sqrt{2} \mathrm{~V}$
- **(C)** $80 \mathrm{~V}$
- **(D)** $160 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40 \sqrt{2} \mathrm{~V}$**

**Detailed Solution:**

The emf across the AC source is given as:
$\begin{aligned}
\mathrm{e} & =\sqrt{\left(\mathrm{V}_{\mathrm{K}}\right)^2+\left(\mathrm{V}_{\mathrm{c}}-\mathrm{V}_{\mathrm{L}}\right)^2}=\sqrt{(40)^2+(80-40)^2} \\
\mathrm{e} & =\sqrt{3200} \\
\therefore \quad \mathrm{e} & =40 \sqrt{2} \mathrm{~V}
\end{aligned}$

</details>

---

### Q117. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In series LCR circuit, the voltage across the inductance and the capacitance are not

**Options:**

- **(A)** out of phase with the voltage across the resistance by $90^{\circ}$.
- **(B)** equal in magnitude at resonance.
- **(C)** out of phase with each other by $180^{\circ}$.
- **(D)** in phase with the source voltage.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) in phase with the source voltage.**

**Detailed Solution:**

In an LCR circuit, the inductor (L) and capacitor (C) introduce phase shifts in the current compared to the source voltage due to their reactive properties. The inductor causes a phase shift of +90 degrees, leading the voltage, while the capacitor causes a phase shift of -90 degrees, lagging the voltage. Thus, voltage across $\mathrm{L}$ and $\mathrm{C}$ are not in phase with the source voltage.

</details>

---

### Q118. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

With the gradual increase in frequency of an a. c. source, the impedance of an LCR series circuit

**Options:**

- **(A)** first decreases, becomes minimum and then increases.
- **(B)** increases.
- **(C)** decreases.
- **(D)** remains constant.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) first decreases, becomes minimum and then increases.**

**Detailed Solution:**

With increase in frequency current increases initially, becomes maximum and then decreases with further increase in frequency.

</details>

---

### Q119. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit given below, the current through inductor is $0.9 \mathrm{~A}$ and through the capacitor is $0.6 \mathrm{~A}$. The current drawn from the a.c. source is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/hx-VrQgl-du8_3HyJCrTeL5RZp7LGlRUuLoeFmgx7vI.original.fullsize.png">

**Options:**

- **(A)** $1.5 \mathrm{~A}$
- **(B)** $0.9 \mathrm{~A}$
- **(C)** $0.6 \mathrm{~A}$
- **(D)** $0.3 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.3 \mathrm{~A}$**

**Detailed Solution:**

As the currents in an inductor and capacitor are out of phase by $180^{\circ}$, we can write Current through the capacitor $\mathrm{I}_{\mathrm{C}}=0.9 \mathrm{~A}$ Current through the inductor $\mathrm{I}_{\mathrm{L}}=-(0.6 \mathrm{~A})$
$\begin{aligned}
\therefore \quad \text { Total current drawn from the source } & =\mathrm{I}_{\mathrm{C}}+\mathrm{I}_{\mathrm{L}} \\
& =0.9-0.6 \\
& =0.3 \mathrm{~A}
\end{aligned}$

</details>

---

### Q120. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An alternating voltage of frequency ' $\omega$ ' is induced in electric circuit consisting of an inductance ' $\mathrm{L}$ ' and capacitance ' $\mathrm{C}$ ', connected in parallel. Then across the inductance coil

**Options:**

- **(A)** current is maximum when $\omega^2=\frac{1}{\text { LC }}$
- **(B)** current is zero
- **(C)** voltage is minimum when $\omega^2=\frac{1}{\text { LC }}$
- **(D)** voltage is maximum when $\omega^2=\frac{1}{\text { LC }}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) voltage is maximum when $\omega^2=\frac{1}{\text { LC }}$**

**Detailed Solution:**

In a parallel LC circuit
at $\omega^2=\frac{1}{\mathrm{LC}}$, the current is minimum.
As current and voltage are out of phase by $90^{\circ}$, the voltage would be maximum.

</details>

---

### Q121. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An e.m.f. $E=4 \cos (1000 t)$ volt is applied to an LR circuit of inductance $3 \mathrm{mH}$ and resistance $4 \Omega$. The maximum current in the circuit is

**Options:**

- **(A)** $\frac{4}{\sqrt{7}} \mathrm{~A}$
- **(B)** $1.0 \mathrm{~A}$
- **(C)** $\frac{4}{7} \mathrm{~A}$
- **(D)** $0.8 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.8 \mathrm{~A}$**

**Detailed Solution:**

For LR circuit,
$Z=\sqrt{R^2+(\omega L)^2}$
Comparing equation $E=4 \cos (1000 t)$ with standard equation, $\mathrm{E}=\mathrm{E}_0 \cos \omega \mathrm{t}$, we get $\omega=1000$ units and $E_0=4 \mathrm{~V}$
$\begin{aligned}
\therefore \quad Z & =\sqrt{16+\left(1000 \times 3^2 \times 10^{-6}\right)} \\
& Z=\sqrt{16+9}=5 \Omega \\
\therefore \quad & I=\frac{E_0}{Z}=\frac{4}{5}=0.8 \mathrm{~A}
\end{aligned}$

</details>

---

### Q122. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an $\mathrm{AC}$ circuit, the current is $i=5 \sin \left(100 t-\frac{\pi}{2}\right) \mathrm{A}$ and voltage is $e=200 \sin (100 t)$ volt. Power consumption in the circuit is $\left(\cos 90^{\circ}=0\right)$

**Options:**

- **(A)** $200\ W$
- **(B)** $0\ W$
- **(C)** $40\ W$
- **(D)** $1000\ W$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0\ W$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P} & =\mathrm{I}_{\mathrm{rms}} \mathrm{V}_{\mathrm{rms}} \cos \phi \\ \phi & =90^{\circ} \\ \therefore \quad \mathrm{P} & =0 \quad\left(\because \cos 90^{\circ}=0\right)\end{aligned}$

</details>

---

### Q123. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An AC voltage source of variable angular frequency $\omega$ and fixed amplitude $V_0$ is connected in series with a capacitance $C$ and an electric bulb of resistance $R$ (inductance zero). When $\omega$ is increased

**Options:**

- **(A)** Total impedance of the circuit increase.
- **(B)** The bulb glows brighter.
- **(C)** The bulb glows dimmer.
- **(D)** Total impedance of the circuit is unchanged.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The bulb glows brighter.**

**Detailed Solution:**

Potential difference across bulb,
$V=I R=\frac{V_0 R}{\sqrt{R^2+\left(\frac{1}{\omega C}\right)^2}}$
When $\omega$ is increased, potential across the bulb as well as brightness increases.

</details>

---

### Q124. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A resistor $R$, an inductor $L$ and a capacitor $C$ are connected in series to an oscillator of frequency $N$. If the resonance frequency is $N_R$, then the current lags behind voltage, when

**Options:**

- **(A)** $N=N_R$
- **(B)** $N=0$
- **(C)** $N < N_R$
- **(D)** $N>N_R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $N>N_R$**

**Detailed Solution:**

Current lags behind the voltage,
$\begin{aligned}
& X_L>X_C \\
& \Rightarrow \omega L>\frac{1}{\omega C} \\
& \Rightarrow \omega>\frac{1}{\sqrt{L C}} \\
& \Rightarrow N>N_R
\end{aligned}$

</details>

---

### Q125. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A coil having an inductance of $\frac{1}{\pi} H$ is connected in series with a resistance of $300 \Omega$. If A.C. source $(20 \mathrm{~V}-200 \mathrm{~Hz})$ is connected across the combination, the phase angle between voltage and current is

**Options:**

- **(A)** $\tan ^{-1}\left(\frac{4}{5}\right)$
- **(B)** $\tan ^{-1}\left(\frac{4}{3}\right)$
- **(C)** $\tan ^{-1}\left(\frac{5}{4}\right)$
- **(D)** $\tan ^{-1}\left(\frac{3}{4}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\tan ^{-1}\left(\frac{4}{3}\right)$**

**Detailed Solution:**

For LR circuit:
Phase angle $\tan \phi=\frac{\omega L}{R}=\frac{2 \pi \times 200}{300} \times \frac{1}{\pi}=\frac{4}{3}$
$\therefore \phi=\tan ^{-1} \frac{4}{3}$

</details>

---

### Q126. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When a capacitor is connected in series LR circuit, the alternating current flowing in the circuit.

**Options:**

- **(A)** remains constant.
- **(B)** increases.
- **(C)** increases.
- **(D)** decreases.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) increases.**

**Detailed Solution:**

Impedance of series LR circuit
$Z=\sqrt{R^2+X_L^2}$
When a capacitor is also connected in circuit, Then impedance
$Z_L=\sqrt{R^2+\left(X_L-X_C\right)^2}$
Clearly impedance of circuit decreases $\left(Z_2<Z_1\right)$, so the value of current
$I=\frac{V}{Z} \propto \frac{1}{Z}$ in the circuit increases.

</details>

---

### Q127. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Same current is flowing in two alternating circuits. The first circuit contains only inductor and the other contains only a capacitor. If the frequency of the alternating e.m.f. is increased, the values of current will

**Options:**

- **(A)** decrease in first circuit and increase in the other.
- **(B)** increase in first circuit and decrease in the other.
- **(C)** increase in both circuits.
- **(D)** decrease in both circuits.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) decrease in first circuit and increase in the other.**

**Detailed Solution:**

For inductor,
$$
I \propto \frac{1}{X_L} \propto \frac{1}{f}
$$
Hence, as frequency increases, current decreases.
For capacitor,
$I \propto \frac{1}{X_C} \propto f$
Hence, as frequency increases, current increases.

</details>

---

### Q128. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown, the AC source has voltage $\mathrm{V}=20 \cos (\omega \mathrm{t})$ volt with $\omega=2000 \mathrm{rad} / \mathrm{s}$. The magnitude of amplitude current will be nearly
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Tz7lshanMddyxSfZ9geDIvHiU9Or7vA4UEHwWTAuHPs.original.fullsize.png">

**Options:**

- **(A)** $\sqrt{5} \mathrm{~A}$
- **(B)** 3.3 A
- **(C)** 2 A
- **(D)** $\frac{2}{\sqrt{5}} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3.3 A**

**Detailed Solution:**

Current through the circuit is given by
$i=\frac{V_0}{\sqrt{R^2+\left(X_C-X_L\right)^2}}$ where $X_L=\omega L$ and $X C=\frac{1}{\omega C}$.
Given: $\mathrm{V}_0=20 \mathrm{~V},=6 \Omega, \mathrm{L}=5 \times 10^{-3} \mathrm{H}, \omega=2000 \frac{\mathrm{rad}}{\mathrm{s}}$ and $\mathrm{C}=50 \times 10^{-6} \mathrm{~F}$
$\begin{aligned}
& \therefore \mathrm{X}_{\mathrm{C}}=\frac{1}{50 \times 10^{-6} \times 2000} \Omega 10 \Omega \text { and } \mathrm{X}_{\mathrm{L}}=2000 \times 5 \times 10^{-3} \Omega=10 \Omega \\
& \because \mathrm{X}_{\mathrm{C}}=\mathrm{X}_{\mathrm{L}}
\end{aligned}$
The current is simply: $\mathrm{I}=\frac{\mathrm{v}_0}{\mathrm{R}}$
$\therefore \mathrm{i}=\frac{20}{6} \mathrm{~A}=3.3 \mathrm{~A}$

</details>

---

### Q129. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A $10 \Omega$ resistance, $5 \mathrm{mH}$ coil and $10 \mu \mathrm{F}$ capacitor are joined in series. When alternating current source of suitable frequency is joined to this combination, the circuit resonates. If the resistance is halved, the resonant frequency is

**Options:**

- **(A)** quadrupled.
- **(B)** halved.
- **(C)** doubled.
- **(D)** remains unchanged.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) remains unchanged.**

**Detailed Solution:**

Concept based.
At resonance, in LCR circuit inductive and capacitive reactance are equal:
$\begin{aligned}
& X_L=X_C \\
& \Rightarrow 2 \pi \mathrm{fL}=\frac{1}{2 \pi \mathrm{fC}} \\
& \Rightarrow \mathrm{f}^2=\left(\frac{1}{4 \pi^2 \mathrm{LC}}\right)
\end{aligned}$
The resonant frequency is independent of the resistance.

</details>

---

### Q130. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In series $L-C-R$ circuit, the capacitance is changed from $C$ to $2 C$. To obtain the same resonance frequency the inductance should be changed from $L$ to

**Options:**

- **(A)** $2 L$
- **(B)** $4 L$
- **(C)** $\frac{L}{2}$
- **(D)** $L$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{L}{2}$**

**Detailed Solution:**

Resonant frequency, $f=\frac{1}{2 \pi \sqrt{L C}}$
As the frequency is unchanged so $f=f^{\prime}$
$\begin{aligned}
& \therefore L C=L^{\prime} C^{\prime}=L^{\prime}(2 C) \\
& \therefore L^{\prime}=\frac{L}{2}
\end{aligned}$

</details>

---

### Q131. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Resistor of $2 \Omega$, inductor of $100 \mu \mathrm{H}$ and capacitor of $400 \mathrm{pF}$ are connected in series across an a.c. source of $e_{r m s}=0.1$ volt.
At resonance, voltage drop across inductor is

**Options:**

- **(A)** 20V
- **(B)** 25 V
- **(C)** 2.5 V
- **(D)** 250 V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 25 V**

**Detailed Solution:**

We know, at resonance $X_C=X_L$
$\Rightarrow \omega L=\frac{1}{\omega C} \Rightarrow \omega=\left(\frac{1}{\sqrt{L C}}\right)$
The potential drop across inductor is
$V_L=i X_L=i \sqrt{\frac{L}{C}}$
$\because$ LCR circuit in series and at resonance
$i=\frac{V}{R}=\frac{0.1}{2} \mathrm{~A}=0.05 \mathrm{~A}$
Now, $V_L=0.05 \sqrt{\left(\frac{100 \times 10^{-6}}{400 \times 10^{-12}}\right)} \mathrm{V}=2.5 \times 10^{-2} \times 10^3 \mathrm{~V}=25 \mathrm{~V}$

</details>

---

### Q132. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A one microfarad condenser is charged to $50 \mathrm{~V}$. The charging battery is then disconnected and a $10 \mathrm{mH}$ coli is connected across the capacitor so that LC oscillations occur. What is the maximum current in the coil? Assume that the circuit contains no resistance.

**Options:**

- **(A)** $0.75 \mathrm{~A}$
- **(B)** $0.25 \mathrm{~A}$
- **(C)** $0.50 \mathrm{~A}$
- **(D)** $1.00 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.50 \mathrm{~A}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Fy7jwXFnbjK8R295ZsQP70Y19KCBvYFAqU1Yi-GIPy4.original.fullsize.png">
$\begin{aligned} & \frac{\mathrm{q}}{\mathrm{C}}=-\mathrm{L} \frac{\mathrm{di}}{\mathrm{dt}}=(-\mathrm{L}) \frac{\mathrm{dq}}{\mathrm{dt}}=\frac{\mathrm{di}}{\mathrm{dq}} \Rightarrow \int_{\mathrm{Q}_0}^0 \mathrm{qdq}=(-\mathrm{LC}) \int_0^{\mathrm{i}} \max \mathrm{idi} \\ & \left.\Rightarrow \frac{\mathrm{q}^2}{2}\right|_{\mathrm{Q}_0} ^0=\left.(-\mathrm{LC}) \frac{\mathrm{i}^2}{2}\right|_0 ^{\mathrm{i}^{\mathrm{max}}} \Rightarrow 0-\mathrm{Q}_0^2=(-\mathrm{LC})\left(\mathrm{i}_{\max }{ }^2\right) \\ & \Rightarrow \mathrm{i}_{\max }=\frac{\mathrm{Q}_0}{\sqrt{\mathrm{LC}}}=\frac{\mathrm{CV}}{\sqrt{\mathrm{LC}}}=50 \sqrt{\frac{1 \times 10^{-6} \mathrm{~F}}{10 \times 10^{-3} \mathrm{H}}} \\ & =50 \times 10^{-2} \mathrm{~A} \\ & \Rightarrow \mathrm{i}=0.5 \mathrm{~A}\end{aligned}$

</details>

---

### Q133. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

At resonance, the value of current in a series L-C-R- (Symbols have their usual meanings.)

**Options:**

- **(A)** $\frac{\mathrm{e}_0}{\mathrm{R}}$
- **(B)** $\frac{\mathrm{e}_0}{\sqrt{\mathrm{r}^2+\omega^2 \mathrm{C}^2}}$
- **(C)** $\mathrm{e}_0\left[\mathrm{R}^2+\left(\omega \mathrm{L}+\frac{1}{\omega \mathrm{C}}\right)^2\right]$
- **(D)** $\frac{\mathrm{e}_0}{\sqrt{\mathrm{R}^2+\omega^2 \mathrm{~L}^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{e}_0}{\mathrm{R}}$**

**Detailed Solution:**

At resonance,
$\omega \mathrm{L}=\frac{1}{\omega \mathrm{C}}$
So,
$\mathrm{i}=\frac{\mathrm{e}_0}{\sqrt{\mathrm{R}^2+\left(\omega \mathrm{L}-\frac{1}{\omega \mathrm{C}}\right)^2}}=\frac{\mathrm{e}_0}{\sqrt{\mathrm{R}^2}}=\frac{\mathrm{e}_0}{\mathrm{R}}$

</details>

---

### Q134. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The resonant frequency of a series LCR circuit is ' $\mathrm{f}_R$ '. The circuit is connected to a sinusoidally alternating e.m.f. of frequency ' $2 \mathrm{f}_{\mathrm{R}}$ '. The inductive reactance becomes. ' $\mathrm{X}_{\mathrm{L}_1}$ ' and capacitive reactance becomes ' $\mathrm{X}_{\mathrm{C}_1}$ ' after changing the frequency. ' $\mathrm{X}_{C_1}$ ' is equal to

**Options:**

- **(A)** $2 \mathrm{X}_{\mathrm{L}_1}$
- **(B)** $\frac{1}{4} \mathrm{X}_{\mathrm{L}_1}$
- **(C)** $\frac{1}{2} \mathrm{X}_{\mathrm{L}_1}$
- **(D)** $\mathrm{x}_{\mathrm{L}_1}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{4} \mathrm{X}_{\mathrm{L}_1}$**

**Detailed Solution:**

$X_C=\frac{1}{\omega^2}$ and $X_L=(\omega L)$
We know, $\omega=2 \pi f \Rightarrow f \propto \omega$ if $f$ is doubled
$\therefore \mathrm{X}_{\mathrm{C}_1}=\frac{\mathrm{X}_{\mathrm{C}}}{2}$ and $\mathrm{X}_{\mathrm{L}_1}=2 \mathrm{X}_{\mathrm{L}}$
We know, $\mathrm{X}_{\mathrm{C}}=\mathrm{X}_{\mathrm{L}}$
$\Rightarrow 2 \mathrm{X}_{\mathrm{C}_1}=\frac{\mathrm{XL}_1}{2} \Rightarrow\left(\mathrm{X}_{\mathrm{C}_1}=\frac{\mathrm{X}_{\mathrm{L}_1}}{4}\right)$

</details>

---

### Q135. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A battery connected to a capacity $20 \mu \mathrm{F}$ is charged to a potential of $35 \mathrm{~V}$. The battery is disconnected. A pure inductor coil of $200 \mathrm{mH}$ is connected across the capacitor so that LC oscillations are set up.The maximum current in the coil is

**Options:**

- **(A)** $0.025 \mathrm{~A}$
- **(B)** $0.25 \mathrm{~A}$
- **(C)** $0.035 \mathrm{~A}$
- **(D)** 0.35 A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.35 A**

**Detailed Solution:**

Capacitance, $\mathrm{C}=20 \mu \mathrm{F}$
Voltage applied to capacitor, $\mathrm{V}=35$ volts
Inductance connected to the capacitor, $\mathrm{L}=200 \mathrm{mH}$
To find: The maximum current in the inducting coil.
The charge stored in the capacitor is given by:
$\mathrm{Q}_0=\mathrm{CV}$
The maximum current flowing in the series LC circuit is:
$I_{\text {max }}=Q_{\text {ow }}$
The frequency of a series LC circuit is given by:
$\omega=\frac{1}{\sqrt{\mathrm{LC}}}$
Substitute the values in equation of maximum current.
$\begin{aligned} & \Rightarrow I_{\max }=(\mathrm{CV}) \times \frac{1}{\sqrt{\mathrm{LC}}}=\sqrt{\frac{\mathrm{C}}{\mathrm{L}}} \mathrm{V} \\ & \therefore \mathrm{I}_{\max }=\sqrt{\frac{20 \times 10^{-6}}{200 \times 10^{-3}}} \times 35=0.35 \mathrm{~A}\end{aligned}$

</details>

---

### Q136. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An inductance coil has a resistance of $100 \Omega$. When are a.c. signal of frequency $100 \mathrm{Hzis}$ applied to the coil, the voltage leads the current by $45^{\circ}$. The inductance of the coil in henry is $\left[\sin 45^{\circ}=\cos 45^{\circ}=\frac{1}{\sqrt{2}}\right]$

**Options:**

- **(A)** $\frac{1}{\pi}$
- **(B)** $\frac{5}{2 \pi}$
- **(C)** $\frac{2}{\pi}$
- **(D)** $\frac{1}{2 \pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2 \pi}$**

**Detailed Solution:**

The phase angle in an LR circuit is given by, since $\phi=45^{\circ}$,
$\tan \phi=\frac{X_L}{X_R}=1$
Resistance of inductive coil $X_L=X_R=100 \Omega$
Thus, inductance of coil $L=\frac{X_L}{2 \pi f}$
$\therefore L=\frac{100}{2 \pi \times 100 \mathrm{~s}^{-1}}=\frac{1}{2 \pi} \mathrm{H}$

</details>

---

### Q137. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A circuit of negligible resistance has an inductor of $0.16 \mathrm{H}$ and capacitor of $25 \mu \mathrm{F}$ connected in series with an alternating voltage source. The resonating frequency of the circuit is

**Options:**

- **(A)** $\frac{150}{\pi}$
- **(B)** $\frac{200}{\pi}$
- **(C)** $\frac{250}{\pi}$
- **(D)** $\frac{400}{\pi}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{250}{\pi}$**

**Detailed Solution:**

At resonance inductive and capacitive reactance's are equal:
$\begin{aligned} & X_C=\omega C=X_L=\frac{1}{\omega L} \\ & \Rightarrow \omega=\frac{1}{\sqrt{L C}}=2 \pi f\end{aligned}$
Given, $L=0.16 \mathrm{H} \& C=25 \times 10^{-6} \mathrm{~F}$
$\begin{aligned} & \Rightarrow \omega=\frac{1}{\sqrt{4 \times 10^{-6}}} \mathrm{~s}^{-1}=\frac{1000}{2} \mathrm{~s}^{-1}=2 \pi f \\ & \Rightarrow f=\left(\frac{250}{\pi}\right) \mathrm{sec}^{-1}\end{aligned}$

</details>

---

### Q138. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In series LCR circuit, the voltage across $L, C$ and $R$ is $50 \mathrm{~V}, 20 \mathrm{~V}$ and $40 \mathrm{~V}$ respectively. The a.c. voltage applied across the combination of LCR is

**Options:**

- **(A)** $10 \mathrm{~V}$
- **(B)** $110 \mathrm{~V}$
- **(C)** $70 \mathrm{~V}$
- **(D)** $50 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $50 \mathrm{~V}$**

**Detailed Solution:**

The ac voltage across the LCR is given by:
$V_{r m s}=\sqrt{V_R^2+\left(V_L-V_C\right)^2}=\sqrt{40^2+(50-20)^2}=50 \mathrm{~V}$

</details>

---

### Q139. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In series L-C-R circuit $C=2 \mu \mathrm{F}, L=1 \mathrm{mH}$ and $R=10 \Omega$. What is the ratio of energies stored in the inductor and the capacitor, when the maximum current flows in the circuit?

**Options:**

- **(A)** $1: 8$
- **(B)** $5: 1$
- **(C)** $1: 5$
- **(D)** $8: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 5$**

**Detailed Solution:**

At maximum current condition, system is at resonance condition.
$\therefore X_C=X_L$
$\Rightarrow \frac{U_C}{U_L}=\frac{\frac{1}{2} C V^2}{\frac{1}{2} L i^2}=\frac{C i^2 R^2}{L i^2}$
$\Rightarrow \frac{U_C}{U_L}=\frac{2 \times 10^{-6}}{10^{-3}} \times 100$
Hence, we get
$\frac{U_C}{U_L}=\frac{2}{10}=\frac{1}{5}$

</details>

---

### Q140. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In LC parallel resonance circuit, choose the wrong statement

**Options:**

- **(A)** Resonance occurs when inductive and capacitive reactance is same.
- **(B)** At resonance, current is minimum.
- **(C)** At resonance, impedance is maximum.
- **(D)** At resonance, resonant frequency $=\sqrt{\mathrm{LC}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) At resonance, resonant frequency $=\sqrt{\mathrm{LC}}$**

**Detailed Solution:**

Concept based.
Resonance occurs when inductive and capacitive reactance is same.
$\begin{aligned} & X_C=X_L \\ & \Rightarrow \omega L=\frac{1}{\omega C} \\ & \Rightarrow \omega=\frac{1}{\sqrt{L C}} \\ & \therefore f=\frac{1}{2 \pi \sqrt{L C}}\end{aligned}$

</details>

---

### Q141. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an LCR series circuit, if the angular frequency is gradually in creased then match the following columns
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PK-aWZ8abv8rMj4jwDQwBZKgR8AS1hrxpzbS1crdNZk.original.fullsize.png">

**Options:**

- **(A)** $(\mathrm{A})-(\mathrm{iv}),(\mathrm{B})-(\mathrm{i}),(\mathrm{C})-(\mathrm{ii}),(\mathrm{D})-(\mathrm{iii})$
- **(B)** (A) - (i), (B) - (iii), (C) - (iv), (D) - (ii)
- **(C)** $(\mathrm{A})-(\mathrm{ii}),(\mathrm{B})-(\mathrm{iii}),(\mathrm{C})-(\mathrm{i}),(\mathrm{D})-(\mathrm{iv})$
- **(D)** $(A)-(i),(B)-(i v),(C)-(i i),(D)-(i i i)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(\mathrm{A})-(\mathrm{iv}),(\mathrm{B})-(\mathrm{i}),(\mathrm{C})-(\mathrm{ii}),(\mathrm{D})-(\mathrm{iii})$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{X}_{\mathrm{C}}=\frac{1}{\omega \mathrm{C}}, \text { so } \mathrm{X}_{\mathrm{C}} \propto \frac{1}{\omega} \\ & \therefore(\mathrm{A})-(\mathrm{iv}) \\ & \mathrm{X}_{\mathrm{L}}=\omega \mathrm{L}, \text { so } \mathrm{X}_{\mathrm{L}} \propto \omega \\ & \therefore(\mathrm{B})-(\mathrm{i})\end{aligned}$
And $\mathrm{R}$ is not a function of $\omega$
$\therefore(\mathrm{C})-(\mathrm{ii})$
Impedence $\mathrm{Z}$ is the minimum at resonance frequency.
$\therefore(\mathrm{D})-(\mathrm{iii})$

</details>

---

### Q142. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

When a.c. source is connected across a pure capacitor, the correct phase relation between current $\left(\mathrm{i}_{\mathrm{c}}\right)$ and voltage $\left(\mathrm{e}_{\mathrm{c}}\right)$ is shown in figure
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aGQ_JAT0ycf-J-mzqcZqdffb0pFaR86M8RjQ0LNiGRA.original.fullsize.png">

**Options:**

- **(A)** (B)
- **(B)** (C)
- **(C)** (D)
- **(D)** (A)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (B)**

**Detailed Solution:**

Conceptual question. The current leads the voltage by $\frac{\pi}{2}$ radians.
Ac voltage source, $\mathrm{V}=\mathrm{V}_0 \sin (\omega \mathrm{t})$
Charge at a given moment on the capacitor, $\mathrm{q}=\mathrm{CV}$
The current through the circuit: $\frac{\mathrm{dq}}{\mathrm{dt}}=\left(\omega \mathrm{CV}_0\right)=\cos (\omega \mathrm{t})$
As cos leads the $\sin$ function by $\frac{\pi}{2}$ radians.

</details>

---

### Q143. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In LCR series resonance circuit, choose the wrong statement.

**Options:**

- **(A)** At resonance, impedance is minimum.
- **(B)** At resonance, circuit is purely inductive
- **(C)** At resonance current has a maximum value.
- **(D)** Resonance occurs at $X_L=X_C$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) At resonance, circuit is purely inductive**

**Detailed Solution:**

Concept: In LCR series circuits, resonance occurs when the value of inductive and capacitive reactances have equal magnitude but have a phase difference of $180^{\circ}$. Thus, they cancel each other. The circuit is purely resistive at resonance.

</details>

---

### Q144. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A condenser of capacity ' $\mathrm{C}$ ' is charged to a potential difference of ' $\mathrm{V}_1$ '. The plates of the condenser are then connected to an ideal inductor of inductance ' $L$ '. The current through an inductor |when the potential difference across the condenser reduces to ' $\mathrm{V}$ ' is

**Options:**

- **(A)** $\frac{\mathrm{C}\left(\mathrm{V}_1^2-\mathrm{V}_2^2\right)}{\mathrm{L}}$
- **(B)** $\frac{\mathrm{C}\left(\mathrm{V}_1^2+\mathrm{V}_2^2\right)}{\mathrm{L}}$
- **(C)** $\left[\frac{\mathrm{C}\left(\mathrm{V}_1^2-\mathrm{V}_2^2\right)^{\frac{1}{2}}}{\mathrm{~L}}\right]$
- **(D)** $\left[\frac{\mathrm{C}\left(\mathrm{V}_1-\mathrm{V}_2\right)^{\frac{1}{2}}}{\mathrm{~L}}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\left[\frac{\mathrm{C}\left(\mathrm{V}_1^2-\mathrm{V}_2^2\right)^{\frac{1}{2}}}{\mathrm{~L}}\right]$**

**Detailed Solution:**

The correct option is (C).
Concept: For the LC circuit the potential drop across the circuit can be written as: $\frac{\mathrm{q}}{\mathrm{C}}+\mathrm{L} \frac{\mathrm{di}}{\mathrm{dt}}=0$
On rewriting, $\frac{\mathrm{q}}{\mathrm{C}}+\mathrm{L}\left(\frac{\mathrm{dq}}{\mathrm{dt}}\right) \frac{\mathrm{di}}{\mathrm{dt}}=0$
Therefore, $\frac{\mathrm{q}}{\mathrm{C}}+\mathrm{Li} \frac{\mathrm{di}}{\mathrm{dq}}=0$
On integrating, $\int_{\mathrm{cv}_1}^{\mathrm{cv}_2} \frac{\mathrm{q}}{\mathrm{c}} \mathrm{dq}=-\int_0^{\mathrm{i}}$ Lidi
On solving for $I=\left[\frac{\mathrm{c}\left(\mathrm{v}_1^2-\mathrm{v}_2^2\right)^{1 / 2}}{\mathrm{~L}}\right]$

</details>

---

### Q145. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In series LCR circuit, at resonance the peak value of current will be $\left[E_0\right.$ is peak emf, $R$ is resistance, $\omega L$ is inductive reactance, and $1 / \omega \mathrm{C}$ is capacitive reactance]

**Options:**

- **(A)** $\frac{E_0}{R}$
- **(B)** $\frac{E_0}{\sqrt{2} R}$
- **(C)** $\frac{E_0}{\sqrt{R^2+\left(\omega L-\frac{1}{\omega C}\right)^2}}$
- **(D)** $\frac{E_0}{\sqrt{2} \sqrt{R^2+\left(\omega L-\frac{1}{\omega C}\right)^2}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{E_0}{R}$**

**Detailed Solution:**

At resonance, the net reactance of the circuit is zero and the impedance is equal to the resistance.
$\therefore \mathrm{I}_0=\frac{\mathrm{E}_0}{\mathrm{R}}$

</details>

---

### Q146. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A circuit containing resistance $\mathrm{R}_1$, inductance $\mathrm{L}_1$ and capacitance $\mathrm{C}_1$ connected in series resonates at the same frequency ' $\mathrm{f}_{\mathrm{r}}$ ' as another circuit containing $\mathrm{R}_2, \mathrm{~L}_2$ and $\mathrm{C}_2$ in series. If two circuits are connected in series, then the new frequency at resonance is

**Options:**

- **(A)** $\frac{3}{4} f_r$
- **(B)** $\frac{3}{2} f_r$
- **(C)** $2 \mathrm{f}_{\mathrm{r}}$
- **(D)** $\mathrm{f}_{\mathrm{r}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{f}_{\mathrm{r}}$**

**Detailed Solution:**

When $\mathrm{R}_1, \mathrm{~L}_1$ and $\mathrm{C}_1$ are connected in series the resonant (angular) frequency is given by
$$
\omega_{\mathrm{r}}=\frac{1}{\sqrt{\mathrm{L}_1 \cdot \mathrm{C}_1}}
$$
Also, when $\mathrm{R}_2, \mathrm{~L}_2, \mathrm{C}_2$ are connected in series
Then $\omega_{\mathrm{r}}=\frac{1}{\sqrt{\mathrm{L}_2 \cdot \mathrm{C}_2}}$
By (1) and (2): $\mathrm{L}_1 \mathrm{C}_1=\mathrm{L}_2 \mathrm{C}_2$
If the two circuits are connected in series then the equivalent inductance is given by $\mathrm{L}=\mathrm{L}_1+\mathrm{L}_2$ and the equivalent capacitance is given by
$$
\begin{aligned}
& \mathrm{C}=\frac{\mathrm{C}_1 \mathrm{C}_2}{\mathrm{C}_1+\mathrm{C}_2} \\
& \therefore \mathrm{LC}=\left(\mathrm{L}_1+\mathrm{L}_2\right) \cdot \frac{\mathrm{C}_1 \mathrm{C}_2}{\mathrm{C}_1+\mathrm{C}_2} \\
& =\frac{\mathrm{L}_1 \mathrm{C}_1 \mathrm{C}_2+\mathrm{L}_2 \mathrm{C}_1 \mathrm{C}_2}{\mathrm{C}_1+\mathrm{C}_2}\left[\because \mathrm{L}_1 \mathrm{C}_1=\mathrm{L}_2 \mathrm{C}_2\right] \\
& =\frac{\mathrm{L}_2 \mathrm{C}_2\left(\mathrm{C}_2+\mathrm{C}_1\right)}{\mathrm{C}_1+\mathrm{C}_2}=\mathrm{L}_2 \mathrm{C}_2 \\
& \therefore \omega=\frac{1}{\sqrt{\mathrm{L}_2 \mathrm{C}_2}}=\omega_{\mathrm{r}}
\end{aligned}
$$

</details>

---

### Q147. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A series $\mathrm{L}-\mathrm{C}-\mathrm{R}$ circuit containing a resistance of $120 \Omega$ has angular frequency $4 \times 10^5 \mathrm{rad} \mathrm{s}^{-1}$. At resonance the voltage across resistance and inductor are $60 \mathrm{~V}$ and $40 \mathrm{~V}$ respectively, then the value of inductance will be

**Options:**

- **(A)** $0.2 \mathrm{mH}$
- **(B)** $0.4 \mathrm{mH}$
- **(C)** $0.8 \mathrm{mH}$
- **(D)** $0.6 \mathrm{mH}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.2 \mathrm{mH}$**

**Detailed Solution:**

At resonance, the impedance of the circuit is equal to resistance
$$
\therefore \mathrm{I}=\frac{\mathrm{V}_{\mathrm{R}}}{\mathrm{R}}=\frac{60}{120}=0.5 \mathrm{~A}
$$
Inductive reactance, $X_L=\frac{V_L}{I}=\frac{40}{0.5}=80 \Omega$
$$
\begin{aligned}
& \mathrm{X}_{\mathrm{L}}=\omega \mathrm{L} \\
& \therefore \mathrm{L}=\frac{\mathrm{X}_{\mathrm{L}}}{\omega}=\frac{80}{4 \times 10^5}=20 \times 10^{-5} \mathrm{H} \\
& =0.2 \mathrm{mH}
\end{aligned}
$$

</details>

---

### Q148. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an LCR series a.c. circuit, the voltage across each of the components $\mathrm{L}, \mathrm{C}$ and $\mathrm{R}$ is $60 \mathrm{~V}$. The voltage across the $\mathrm{LC}$ combination is

**Options:**

- **(A)** $120 \mathrm{~V}$
- **(B)** $60 \mathrm{~V}$
- **(C)** $\text { zero }$
- **(D)** $\frac{60}{\sqrt{3}} \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\text { zero }$**

**Detailed Solution:**

The voltage across $L$ and $C$ has phase difference of $\pi$ $\mathrm{X}=\mathrm{X}_{\mathrm{L}}-\mathrm{X}_{\mathrm{c}}=60-60=0$
Hence the resultant voltage across the combination is zero.

</details>

---

### Q149. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

For series LCR circuit, which one of the following is a CORRECT statement?

**Options:**

- **(A)** Potential difference across $\mathrm{R}$ and that across capacitor have phase difference of $\frac{\pi}{2}$
- **(B)** Applied e.m.f. and potential difference across resistance ' $R$ ' are in the same phase
- **(C)** Applied e.m.f. and potential difference across inductor coil has phase difference of $\frac{\pi}{2}$
- **(D)** Potential difference across capacitor and that across inductor have phase difference of $\frac{\pi}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Potential difference across $\mathrm{R}$ and that across capacitor have phase difference of $\frac{\pi}{2}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/vCAj_4GZwPLaAqt4t_h2eRSL0joEiGFt8tNMLNPr2C4.original.fullsize.png">

(A) is correct.
(B) is wrong. There is phase difference $\phi$ between the applied emf e and $\mathrm{e}_{\mathrm{R}}$
(C) is wrong. There is phase difference of $\left(\frac{\pi}{2}-\phi\right)$ between $\mathrm{e}$ and $\mathrm{e}_{\mathrm{L}}$
(D) is wrong. There is a phase difference of $\pi$ between $\mathrm{e}_{\mathrm{C}}$ and $\mathrm{e}_{\mathrm{L}}$

</details>

---

### Q150. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which graph shows the correct variation of r.m.s. current ' $\mathrm{I}$ ' with frequency ' $\mathrm{f}$ ' of a.c. in case of (LCR) series resonance circuit?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/O6Rc1j50oirwKY0SurjofDHbeg4tDDNDxL_Lh-RJqCE.original.fullsize.png">

**Options:**

- **(A)** Q
- **(B)** P
- **(C)** R
- **(D)** S

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) S**

**Detailed Solution:**

In series, $\mathrm{Z}=\sqrt{\left(2 \pi \mathrm{fL}-\frac{1}{2 \pi \mathrm{fC}}\right)^2+\mathrm{R}^2}$
Current, $I=\frac{\mathrm{V}}{\sqrt{\left(2 \pi \mathrm{fL}-\frac{1}{2 \pi \mathrm{fC}}\right)^2+\mathrm{R}^2}}$
As frequency increases, current first increases and then decreases. Current is maximum at resonance when $\mathrm{X}_{\mathrm{L}}=\mathrm{X}_{\mathrm{C}}$

</details>

---

### Q151. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In the part of an a.c. circuit as shown, the resistance $\mathrm{R}=0.2$ $\Omega$. At a certain instant $\left(\mathrm{V}_{\mathrm{A}}-\mathrm{V}_{\mathrm{B}}\right)=0.5 \mathrm{~V}, \mathrm{I}=0.5 \mathrm{~A}$ and $\frac{\Delta \mathrm{I}}{\Delta \mathrm{t}}=8 \mathrm{~A} / \mathrm{s}$. The inductance of the coil is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aqd3NVnGbxZ2xVExDCG4iS2zKZ8liVs6dtnOgr5joHI.original.fullsize.png">

**Options:**

- **(A)** $0.04 \mathrm{H}$
- **(B)** $0.02 \mathrm{H}$
- **(C)** $0.08 \mathrm{H}$
- **(D)** $0.05 \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.05 \mathrm{H}$**

**Detailed Solution:**

In the part of an a.c. circuit
$$
\begin{aligned}
& V_A-V_B=L \frac{d I}{d t}+I R \\
& 0.5=8 L+0.5 \times 0.2 \\
& \therefore 8 L=0.4 \\
& \therefore L=\frac{0.4}{8}=0.05 \mathrm{H}
\end{aligned}
$$

</details>

---

### Q152. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In the circuit shown in the figure, a.c. source gives voltage $\mathrm{V}=20 \cos (2000 \mathrm{t})$. Impedance and r.m.s current respectively will be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mkBpCgQDvVwsU3FG-YUl7KFnqa0w2KKtIqKWuQj7xpk.original.fullsize.png">

**Options:**

- **(A)** $10 \Omega, \sqrt{2} \mathrm{~A}$
- **(B)** $5 \Omega, 2 \mathrm{~A}$
- **(C)** $15 \Omega, \frac{2 \sqrt{2}}{3} \mathrm{~A}$
- **(D)** $5 \Omega, 1 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $15 \Omega, \frac{2 \sqrt{2}}{3} \mathrm{~A}$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{V}=20 \cos 2000 \mathrm{t} \therefore \omega=2000 \mathrm{rad} / \mathrm{s} \\
& \mathrm{X}_{\mathrm{L}}=\omega \mathrm{L}=2000 \times 5 \times 10^{-3}=10 \Omega \\
& \mathrm{X}_{\mathrm{C}}=\frac{1}{\omega \mathrm{C}}=\frac{1}{2000 \times 50 \times 10^{-6}}=10 \Omega \\
& \therefore \mathrm{X}_{\mathrm{L}}=\mathrm{X}_{\mathrm{C}} \text { which gives resonance. } \\
& \mathrm{Z}=\mathrm{R}=10 \Omega+5 \Omega=15 \Omega
\end{aligned}
$$
The peak current, $\mathrm{I}_0=\frac{\mathrm{V}_0}{\mathrm{R}}=\frac{20}{15}=\frac{4}{3} \mathrm{~A}$ R.M.S. current, $I_{r m s}=\frac{I_0}{\sqrt{2}}=\frac{2 \sqrt{2}}{3} \mathrm{~A}$

</details>

---

### Q153. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A capacitor of capacity ' $\mathrm{C}$ ' is charged to a potential ' $\mathrm{V}$ '. It is connected in parallel to an inductor of inductance ' $L$ '. The maximum current that will flow in the circuit is

**Options:**

- **(A)** $V \sqrt{\frac{L}{C}}$
- **(B)** $\mathrm{V} \sqrt{\mathrm{LC}}$
- **(C)** $\mathrm{V} \sqrt{\frac{\mathrm{C}}{\mathrm{L}}}$
- **(D)** $\frac{\mathrm{VC}^2}{\mathrm{~L}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{V} \sqrt{\frac{\mathrm{C}}{\mathrm{L}}}$**

**Detailed Solution:**

The charge oscillates according to the equations
$$
\begin{aligned}
& \mathrm{q}=\mathrm{q}_0 \cos \omega \mathrm{t} \\
& \mathrm{i}=-\frac{\mathrm{dq}}{\mathrm{dt}}=\omega \mathrm{q}_0 \sin \omega \mathrm{t}=\mathrm{i}_0 \sin \omega \mathrm{t} \\
& \text { where } \mathrm{i}_0=\omega \mathrm{q}_0, \omega=\frac{1}{\sqrt{\mathrm{LC}}}, \mathrm{q}_0=C V \\
& \therefore \mathrm{i}_0=\frac{1}{\sqrt{\mathrm{LC}}} \cdot \mathrm{CV}=\mathrm{V} \sqrt{\frac{\mathrm{C}}{\mathrm{L}}}
\end{aligned}
$$

</details>

---

### Q154. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

An a.c. source of angular frequency ' $\omega$ ' is fed across a resistor ' $\mathrm{R}$ ' and a capacitor ' $\mathrm{C}$ ' in series. The current registered is I. If now the frequency of source is changed to $\frac{\omega}{3}$ (but maintaining the same voltage), the current in the circuit is found to be halved. The ratio of reactance to resistance at the original frequency ' $\omega$ ' will be

**Options:**

- **(A)** $\sqrt{\frac{2}{5}}$
- **(B)** $\sqrt{\frac{1}{5}}$
- **(C)** $\sqrt{\frac{4}{5}}$
- **(D)** $\sqrt{\frac{3}{5}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{\frac{3}{5}}$**

**Detailed Solution:**

$\begin{aligned} & \text { Initial current } I=\frac{V}{Z}, \text { Final current } I^{\prime}=\frac{V}{Z^{\prime}} \\ & \frac{1}{2}=\frac{I^{\prime}}{I}=\frac{Z}{Z^{\prime}} \quad \therefore \frac{Z}{Z^{\prime}}=\frac{1}{2} \\ & \therefore \frac{Z^2}{Z^{\prime 2}}=\frac{1}{4} \quad \therefore \frac{R^2+X_c^2}{R^2+X_c^{\prime 2}}=\frac{1}{4} \\ & \therefore 4 R^2+4 X_c^2=R^2+X_c^{\prime 2} \\ & \therefore 3 R^2=X_c^{\prime 2}-4 X_c^2 \quad \ldots .(1) \\ & X_c=\frac{1}{\omega C}, X^{\prime}=\frac{3}{\omega C} \quad \therefore X^{\prime}=3 X_c \\ & \text { Putting this value of } X^{\prime} \text { in }(1) \text { we get } \\ & 3 R^2=9 X_c^2-4 X_c^2=5 X_c^2 \\ & \therefore \frac{X_c^2}{R^2}=\frac{3}{5}=0.6 \\ & \therefore \frac{X_c}{R}=\sqrt{\frac{3}{5}}\end{aligned}$

</details>

---

### Q155. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a.c. circuit, a resistance $R=40 \Omega$ and an inductance ' $L$ ' are connected in series. If the phase angle between voltage and current is $45^{\circ}$, then the value of the inductive reactance is $\left(\tan 45^{\circ}=1\right)$

**Options:**

- **(A)** $50 \Omega$
- **(B)** $40 \Omega$
- **(C)** $10 \Omega$
- **(D)** $20 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $40 \Omega$**

**Detailed Solution:**

$\begin{aligned} & \tan \phi=\tan 45^{\circ}=\frac{\mathrm{X}_{\mathrm{L}}}{\mathrm{R}} \\ & \mathrm{X}_{\mathrm{I}}=\mathrm{R}=40 \Omega\end{aligned}$

</details>

---

### Q156. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In LCR series resonant circuit, at resonance, voltage across ' $\mathrm{L}$ ' and ' $C$ ' will cancel each other because they are

**Options:**

- **(A)** $90^{\circ}$ out of phase
- **(B)** $90^{\circ}$ in phase
- **(C)** $180^{\circ}$ in phase
- **(D)** $180^{\circ}$ out of phase

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $180^{\circ}$ out of phase**

**Detailed Solution:**

In LCR series resonant circuit, at resonance, voltage across ' $\mathrm{L}$ ' and ' $\mathrm{C}$ ' will cancel each other because they are $180^{\circ}$ out of phase.

</details>

---

### Q157. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A series combination of resistor ' $\mathrm{R}$ ' and capacitor ' $\mathrm{C}$ ' is connected to an a.c. source of angular frequency ' $\omega$ '. Keeping the voltage same, if the frequency is changed to $\frac{\omega}{3}$ the current becomes half of the original current. Then the ratio of capacitive reactance and resistance at the former frequency is

**Options:**

- **(A)** $\sqrt{0.6}$
- **(B)** $\sqrt{6}$
- **(C)** $\sqrt{3}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\sqrt{0.6}$**

**Detailed Solution:**

Initial current $\mathrm{I}=\frac{\mathrm{V}}{\mathrm{Z}}$ and Final current $\mathrm{I}^{\prime}=\frac{\mathrm{V}}{\mathrm{Z}^{\prime}}$
$$
\because \mathrm{I}^{\prime}=\frac{\mathrm{I}}{2}
$$
$$
Z^{\prime}=2 Z
$$
$$
\frac{\mathrm{R}^2+\mathrm{X}_{\mathrm{c}}^2}{\mathrm{R}^2+\mathrm{X}_{\mathrm{c}}^{\prime 2}}=\frac{1}{4}
$$
$$
4 R^2+4 X_c^2=R^2+X_c^2
$$


$$
\begin{aligned}
& 3 R^2=X_c^{\prime 2}-4 X_c^2 \\
& X_c=\frac{1}{\omega C}, \quad X_c^{\prime}=\frac{3}{\omega C} \\
& X_c{ }^{\prime}=3 X_c
\end{aligned}
$$
From (1)
$$
3 R^2=9 X_c^2-4 X_c^2=5 X_c^2
$$
$$
\frac{\mathrm{X}_{\mathrm{c}}^2}{\mathrm{R}^2}=\frac{3}{5}=0.6
$$
$$
\frac{\mathrm{X}_{\mathrm{c}}}{\mathrm{R}}=\sqrt{0.6}
$$

</details>

---

### Q158. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the graphical representation of e.m.f. ' $e$ ' and current ' $i$ ' versus ' $\omega \mathrm{t}$ ' for an a.c. circuit, both emf and current reach zero, minimum and maximum value at the same time. The circuit element connected to the source will be

**Options:**

- **(A)** pure capacitor
- **(B)** combination of capacitor and inductor
- **(C)** pure resistor
- **(D)** pure inductor

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) pure resistor**

**Detailed Solution:**

Since the current and emf are in phase the circuit is purely resistive.

</details>

---

### Q159. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

An inductor coil takes current $8 \mathrm{~A}$ when connected to a $100 \mathrm{~V}$ and $50 \mathrm{~Hz} \mathrm{AC}$ source. A pure resistor under the same condition takes current of $10 \mathrm{~A}$. If inductor coil and resistor are connected in series to a $100 \mathrm{~V}$ and $40 \mathrm{~Hz}$ AC supply, then the current in the series combination of above resistor and inductor is

**Options:**

- **(A)** $\frac{10}{\sqrt{3}} \mathrm{~A}$
- **(B)** $\frac{5}{\sqrt{2}} \mathrm{~A}$
- **(C)** $10 \sqrt{2} \mathrm{~A}$
- **(D)** $5 \sqrt{2} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $5 \sqrt{2} \mathrm{~A}$**

**Detailed Solution:**

Inductive reactance when $100 \mathrm{~V}, 50 \mathrm{~Hz}$ source is connected is given by
$$
\mathrm{X}_{\mathrm{L}}=\frac{\mathrm{V}}{\mathrm{I}}=\frac{100}{8}=12.5 \Omega
$$
Resistance $\mathrm{R}=\frac{\mathrm{V}}{1}=\frac{100}{10}=10 \Omega$
Inductive reactance at new frequency of $40 \mathrm{~Hz}$
$$
\begin{aligned}
& \frac{\mathrm{X}_{\mathrm{L}}^{\prime}}{\mathrm{X}_{\mathrm{L}}}=\frac{2 \pi \mathrm{f}^{\prime} \mathrm{L}}{2 \pi \mathrm{fL}}=\frac{40}{50}=\frac{4}{5} \\
& \mathrm{X}_{\mathrm{L}}^{\prime}=\frac{4}{5} \mathrm{X}_{\mathrm{L}}=\frac{4}{5} \times 12.5=10 \Omega
\end{aligned}
$$
When they are connected in series the impedance will be given by
$$
\begin{aligned}
& Z=\sqrt{R^2+X_L^{\prime 2}}=\sqrt{(10)^2+(10)^2}=10 \sqrt{2} A \\
& I=\frac{V}{Z}=\frac{100}{10 \sqrt{2}}=5 \sqrt{2} \mathrm{~A}
\end{aligned}
$$

</details>

---

### Q160. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An inductive coil has a resistance of $100 \Omega$. When an a.c. signal of frequency $1000 \mathrm{~Hz}$ is applied to the coil the voltage leads the current by $45^{\circ}$. The inductance of the coil is

**Options:**

- **(A)** $\frac{0.25}{2 \pi} \mathrm{H}$
- **(B)** $\frac{0.05}{\pi} \mathrm{H}$
- **(C)** $\frac{0.25}{\pi} \mathrm{H}$
- **(D)** $\frac{0.5}{\pi} \mathrm{H}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{0.05}{\pi} \mathrm{H}$**

**Detailed Solution:**

$$
\tan \phi=\tan 45^{\circ}=\frac{\mathrm{X}_{\mathrm{L}}}{\mathrm{R}}
$$
or $\mathrm{X}_{\mathrm{L}}=\mathrm{R}$
$$
2 \pi \mathrm{fL}=\mathrm{R}
$$
Or $L=\frac{\mathrm{R}}{2 \pi \mathrm{f}}=\frac{100}{2 \pi \times 1000}=\frac{0.05}{\pi} \mathrm{H}$

</details>

---

### Q161. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A series LCR circuit with resistance $R=500 \mathrm{ohm}$ is connected to an a.c. source of $250 \mathrm{~V}$. When only the capacitance is removed, the current lags behind the voltage by $60^{\circ}$. When only the inductance is removed, the current leads the voltage by $60^{\circ}$. The impedance of the circuit is

**Options:**

- **(A)** $\frac{500}{\sqrt{3}} \Omega$
- **(B)** $500 \sqrt{3} \Omega$
- **(C)** $250 \Omega$
- **(D)** $500 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $500 \Omega$**

**Detailed Solution:**

When capacitance is removed
$$
\begin{aligned}
& \tan \phi=\tan 60^{\circ}=\frac{X_L}{R} \\
& \therefore \frac{X_L}{R}=\sqrt{3} \text { or } X_L=R \sqrt{3}
\end{aligned}
$$
When inductance is removed,
$$
\begin{aligned}
& \frac{X_C}{R}=\tan 60^{\circ}=\sqrt{3} \\
& \therefore X_C=R \sqrt{3} \\
& \therefore X_C=X_L
\end{aligned}
$$
Impedance, $\mathrm{Z}=\sqrt{\mathrm{R}^2+\left(\mathrm{X}_{\mathrm{L}}=\mathrm{X}_{\mathrm{C}}\right)^2}=\mathrm{R}=500 \Omega$

</details>

---

### Q162. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

When a capacitor is connected in series LR circuit, the alternating current flowing in the circuit

**Options:**

- **(A)** increases.
- **(B)** decreases.
- **(C)** remains constant.
- **(D)** is zero.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) increases.**

**Detailed Solution:**

$z=\sqrt{{R^{2}+\left(X_{L}-X_{C}\right)^{2}}}$
With capacitor the value of $z$ decreases. So, current increases.

</details>

---

### Q163. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An e.m.f. $\mathrm{E}=\mathrm{E}_{0} \sin \omega \mathrm{t}$ is applied to a circuit containing 'L' and 'R' in series.
If $X_{L}=R$, then the power dissipated in the circuit is

**Options:**

- **(A)** $\frac{\mathrm{E}_{0}^{2}}{4 \mathrm{R}}$
- **(B)** $\frac{\mathrm{E}_{0}}{2 \mathrm{R}}$
- **(C)** $\frac{\mathrm{E}_{0}}{4 \mathrm{R}}$
- **(D)** $\frac{\mathrm{E}_{0}^{2}}{2 \mathrm{R}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{E}_{0}^{2}}{2 \mathrm{R}}$**

**Detailed Solution:**

$\mathrm{E}=\mathrm{E}_{0} \sin \omega \mathrm{t}$
$P=\frac{E_{0}}{\sqrt{2}} \times \frac{I_{0}}{\sqrt{2}} \cos \theta$
$=\frac{E_{0}}{\sqrt{2}} \times \frac{E_{0}}{\sqrt{2} Z} \times \frac{R}{Z}$
$=\frac{E_{0}^{2} R}{2 Z^{2}} \quad \quad Z^{2}=R^{2}+\omega L^{2}=2 R^{2}$
$=\frac{E_{0}^{2} R}{4 R^{2}}=\frac{E_{0}^{2}}{4 R}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_qyOqHu0zyFvfOKJCaBngEfnS5kfMl6_rMu6sUvGuac.original.fullsize.png">

</details>

---

### Q164. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An alternating e.m.f. of $0 \cdot 2 \mathrm{~V}$ is applied across an LCR series circuit having $\mathrm{R}=4 \Omega, \mathrm{C}=$ $80 \mu \mathrm{F}$ and $\mathrm{L}=200 \mathrm{mH}$. At resonance the voltage drop across the inductor is

**Options:**

- **(A)** 1V
- **(B)** 2.5V
- **(C)** 3.5V
- **(D)** 10V

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2.5V**

**Detailed Solution:**

At resonance $\mathrm{X}_{\mathrm{L}}=\mathrm{X}_{\mathrm{C}}$
$\therefore$ Current $=\frac{0.2}{R}=\frac{0.2}{4}=\frac{0.1}{2}=0.05 \mathrm{~A}$
Now, $\mathrm{X}_{\mathrm{L}}=\omega \mathrm{L}=2 \pi \mathrm{f} \mathrm{L}$
$$
\begin{aligned}
\mathrm{f} &=\frac{1}{2 \pi \sqrt{\mathrm{LC}}} \\
\therefore \quad \mathrm{X}_{\mathrm{L}} &=\frac{2 \pi \mathrm{L}}{2 \pi \sqrt{\mathrm{LC}}}=\sqrt{\frac{\mathrm{L}}{\mathrm{C}}} \\
\mathrm{X}_{\mathrm{L}} &=\sqrt{\frac{200 \times 10^{-3}}{80 \times 10^{-6}}}=\frac{10^{2}}{2}=50 \Omega \\
\therefore \quad \mathrm{V}_{\mathrm{L}} &=\mathrm{i} \times \mathrm{L}=0.05 \times 50=2.5 \mathrm{~V}
\end{aligned}
$$

</details>

---

### Q165. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In LCR circuit the inductance is changed from L to $9 \mathrm{~L}$. For same resonant
frequency the capacitance should be changed from $\mathrm{C}$ to

**Options:**

- **(A)** $9 \mathrm{C}$
- **(B)** $3 \mathrm{C}$
- **(C)** $\frac{C}{9}$
- **(D)** $\frac{C}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{C}{9}$**

**Detailed Solution:**

$\omega=\frac{1}{\sqrt{\mathrm{L}_{1} \mathrm{C}_{1}}}=\frac{1}{\sqrt{\mathrm{L}_{2} \mathrm{C}_{2}}}$
$\therefore \quad \mathrm{L}_{1} \mathrm{C}_{1}=\mathrm{L}_{2} \mathrm{C}_{2}$
$\quad \mathrm{C}_{2}=\frac{\mathrm{L}_{1} \mathrm{C}_{1}}{\mathrm{~L}_{2}}=\frac{\mathrm{L}}{9 \mathrm{~L}} \times \mathrm{C}=\frac{\mathrm{C}}{9}$

</details>

---

### Q166. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A series LCR circuit has $\mathrm{R}=200 \Omega, \mathrm{L}=663 \mathrm{mH}$ and $\mathrm{C}=26 \cdot 5 \mu \mathrm{F}$. The applied
alternating voltage has an amplitude of $50 \mathrm{~V}$ and a frequency of $60 \mathrm{~Hz}$ so that
$\mathrm{X}_{\mathrm{L}}=250 \Omega$ and $\mathrm{Xc}=100 \Omega$. The peak current is

**Options:**

- **(A)** $0.33 \mathrm{~A}$
- **(B)** $0 \cdot 20 \mathrm{~A}$
- **(C)** $0.50 \mathrm{~A}$
- **(D)** $0 \cdot 25 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0 \cdot 20 \mathrm{~A}$**

**Detailed Solution:**

$\mathrm{R}=200 \Omega \quad \mathrm{L}=663 \mathrm{mH} \quad \mathrm{C}=26.5 \mu \mathrm{F}$
$\mathrm{V}_{0}=50 \mathrm{~V}, \mathrm{f}=60 \mathrm{~Hz}$
$\mathrm{X}_{\mathrm{L}}=250 \Omega, \mathrm{X}_{\mathrm{C}}=100 \Omega$
$\mathrm{Z}=\sqrt{\mathrm{R}^{2}+\left(\mathrm{X}_{1}-\mathrm{X}_{\mathrm{C}}\right)^{2}}=\sqrt{40000+22500}$
$=\sqrt{62500}=250$
$\therefore \mathrm{i}_{0}=\frac{\mathrm{V}_{0}}{\mathrm{Z}}=\frac{50}{250}=\frac{1}{5}=0.2 \mathrm{~A}$

</details>

---

### Q167. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In series LCR circuit, resistance is $18 \Omega$ and impedance is $33 \Omega$. An r.m.s. voltage of
$220 \mathrm{~V}$ is applied across the circuit. The true power consumed in a.c. circuit is

**Options:**

- **(A)** $400 \mathrm{~V}$
- **(B)** $600 \mathrm{~V}$
- **(C)** $800 \mathrm{~V}$
- **(D)** $200 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $800 \mathrm{~V}$**

**Detailed Solution:**

$I=\frac{V}{Z}=\frac{220}{33}=\frac{20}{3} A$
$P=I^{2} R=\left(\frac{20}{3}\right)^{2} \times 18=800 \mathrm{~W}$

</details>

---

### Q168. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The resonant frequency of a series LCR circuit is ' $\mathrm{f}$ '. The circuit is now connected to the sinusoidally alternating e.m.f. of frequency ' $2 \mathrm{f}^{\prime}$. The new reactance $\mathrm{X}_{\mathrm{L}}^{\prime}$ and
$\mathrm{X}_{\mathrm{C}}^{\prime}$ are related as

**Options:**

- **(A)** $\mathrm{X}_{\mathrm{C}}^{\prime}=\frac{1}{4} \mathrm{X}_{\mathrm{L}}^{\prime}$
- **(B)** $\mathrm{X}_{\mathrm{C}}^{\prime}=2 \mathrm{X}_{\mathrm{L}}^{\prime}$
- **(C)** $\mathrm{X}_{\mathrm{C}}^{\prime}=\mathrm{X}_{\mathrm{L}}^{\prime}$
- **(D)** $\mathrm{X}_{\mathrm{C}}^{\prime}=\frac{1}{2} \mathrm{X}_{\mathrm{L}}^{\prime}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{X}_{\mathrm{C}}^{\prime}=\frac{1}{4} \mathrm{X}_{\mathrm{L}}^{\prime}$**

**Detailed Solution:**

No Solution

</details>

---

### Q169. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a series <math><mi>L</mi><mi>C</mi><mi>R</mi></math> circuit <math><mi>R</mi><mo>=</mo><mn>300</mn><mi mathvariant="normal">Ω</mi><mo>,</mo><mi></mi><mi>L</mi><mo>=</mo><mn>0.9</mn><mi mathvariant="normal">H</mi><mo>,</mo><mi>C</mi><mo>=</mo><mn>2</mn><mi mathvariant="normal">µ</mi><mi mathvariant="normal">F</mi><mo>,</mo><mi></mi><mi>ω</mi><mo>=</mo><mn>1000</mn><mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></mrow><mo>/</mo><mrow><mi mathvariant="normal">s</mi><mo>.</mo></mrow></mrow></math> The impedance of the circuitis

**Options:**

- **(A)** <math><mn>500</mn><mi></mi><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mn>1300</mn><mi></mi><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mn>400</mn><mi></mi><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mn>900</mn><mi></mi><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>500</mn><mi></mi><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

<math><mi>Z</mi><mo>=</mo><msqrt><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>ω</mi><mi>L</mi><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>ω</mi><mi>C</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>  
<math><mi>ω</mi><mi>L</mi><mo> </mo><mo>=</mo><mo> </mo><mfenced separators="|"><mrow><mn>1000</mn></mrow></mfenced><mo> </mo><mfenced separators="|"><mrow><mn>0.9</mn></mrow></mfenced><mo> </mo><mo>=</mo><mo> </mo><mn>900</mn></math>  
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mi>ω</mi><mi>C</mi></mrow></mfrac><mo> </mo><mo>=</mo><mo> </mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1000</mn><mo>×</mo><mn>2</mn><mo>×</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>500</mn></math>  
<math><mo>∴</mo><mi>Z</mi><mo> </mo><mo>=</mo><mo> </mo><msqrt><msup><mrow><mfenced separators="|"><mrow><mn>300</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>900</mn><mo>-</mo><mn>500</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>  
<math><mo> </mo><mo> </mo><mo> </mo><mi>Z</mi><mo> </mo><mo>=</mo><mo> </mo><mn>500</mn><mi mathvariant="normal"></mi><mi>Ω</mi></math>

</details>

---

### Q170. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A coil has inductance 2H. The ratio of its reactance, when it is connected first to an AC source and then to DC source, is

**Options:**

- **(A)** Zero
- **(B)** 1
- **(C)** Less than 1
- **(D)** Infinity

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Infinity**

**Detailed Solution:**

Given, inductance of coil, L = 2H 
Reactance of coil, when it is connected to AC source, 
<math><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>X</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>ω</mi><mi>L</mi></mrow></mfrac></math> where, <math><mi>ω</mi><mo>=</mo></math> angular frequency 
<math><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>X</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>ω</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><mi>μ</mi><mi>ω</mi></mrow></mfrac></math>  
For DC source, inductor coil behaves pure conductor, hence <math><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>X</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>D</mi><mi>C</mi></mrow></msub><mo>=</mo><mn>0</mn></math>  
<math><mo>∴</mo><mfrac><mrow><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>X</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub></mrow><mrow><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi>X</mi></mrow><mrow><mi>L</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi>D</mi><mi>C</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>ω</mi></mrow><mrow><mn>0</mn></mrow></mfrac><mo>=</mo><mi>∞</mi></math> (at infinity)

</details>

---

### Q171. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

In series LCR circuit <math><mi>R</mi><mo>=</mo><mn>18</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math> and impedance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>. An RMS voltage of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo> </mo><mi mathvariant="normal">V</mi></math> is applied across the circuit. The true power consumed in the AC circuit is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo>&#xA0;</mo><mi mathvariant="normal">W</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo> </mo><mi mathvariant="normal">W</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn><mo> </mo><mi mathvariant="normal">W</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>800</mn><mo> </mo><mi mathvariant="normal">W</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>800</mn><mo> </mo><mi mathvariant="normal">W</mi></math>**

**Detailed Solution:**

<math><mo>P =</mo><msub><mrow><mi>e</mi></mrow><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>.</mo><msub><mrow><mi>i</mi></mrow><mrow><mi>r</mi><mi>m</mi><mi>s</mi></mrow></msub><mo>.</mo><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#981;</mi></mrow></mrow></math>
<math><mo>=</mo><msub><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">s</mi></mrow></msub><mo>.</mo><mfrac><mrow><msub><mrow><mi>e</mi></mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">s</mi></mrow></msub></mrow><mrow><mi>Z</mi></mrow></mfrac><mo>.</mo><mfrac><mrow><mi>R</mi></mrow><mrow><mi>Z</mi></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>220</mn><mo>&#215;</mo><mn>220</mn><mo>&#215;</mo><mn>18</mn></mrow><mrow><mn>33</mn><mo>&#215;</mo><mn>33</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>18</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac></math>
<math><mo>=</mo><mn>20</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>800</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">W</mi></math>

</details>

---

### Q172. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

Inductive reactance of a coil is expressed in

**Options:**

- **(A)** ampere
- **(B)** ohm
- **(C)** volt
- **(D)** weber

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) ohm**

**Detailed Solution:**

Inductive reactance or capacitive reactance are the impedance of an AC circuit which can be expressed in ohms.

</details>

---

### Q173. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

The power factor is an $L-C-R$ circuit at resonance is

**Options:**

- **(A)** zero
- **(B)** 1
- **(C)** $0.8$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

At resonance, $L-C-R$ circuit behaves as purely resistive circuit for purely resistive circuit power factor $=1$.

</details>

---

### Q174. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

If the conductance and capacitance are both doubled in $L-C$ - $R$ circuit, the resonant frequency of the circuit will

**Options:**

- **(A)** decrease to one-half the original value
- **(B)** decrease to one-fourth the original value
- **(C)** increase to twice the original value
- **(D)** decrease to twice the original value

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) decrease to one-half the original value**

**Detailed Solution:**

The resonant frequency
$$
v_{0}=\frac{1}{2 \pi \sqrt{L C}} \Rightarrow v_{0} \propto \frac{1}{\sqrt{L C}}
$$
If conductance and capacitance both are doubled, then
$$
v_{0}=\frac{1}{2}\left(\frac{1}{2 \pi} \sqrt{L C}\right)
$$
So, the resonant frequency will decrease to one-half of the original value.

</details>

---

### Q175. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The resonant frequency of an $L-C$ circuit is

**Options:**

- **(A)** $\frac{1}{2 \pi \sqrt{L C}}$
- **(B)** $\frac{1}{2 \pi} \sqrt{\frac{L}{C}}$
- **(C)** $\frac{1}{2 \pi} \sqrt{\frac{L}{C}}$
- **(D)** $\frac{1}{2 \pi} \sqrt{\frac{C}{L}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2 \pi \sqrt{L C}}$**

**Detailed Solution:**

Resonant frequency (or natural frequency) of an $L-C$ circuit is given as
$$
v_{0}=\left(\frac{1}{2 \pi \sqrt{L C}}\right)
$$

</details>

---

### Q176. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

A lamp is connected is series with a capacitor and an AC source, what happens if the capacity of the capacitor is reduced?

**Options:**

- **(A)** The lamp shines more brightly
- **(B)** The lamp shines less brightly
- **(C)** There is no change in the brightness of the lamp
- **(D)** Brightness may increase or decrease depending on the frequency of the AC

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) The lamp shines less brightly**

**Detailed Solution:**

The lamp shines less brightly because, when capacity of the capaictor is reduced, the capacitive reactance $\left(X_{C}=\frac{1}{\omega C}\right)$ increases and hence, the current through the lamp decreases.

</details>

---

### Q177. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

In a purely inductive circuit, the current is

**Options:**

- **(A)** in phase with the voltage
- **(B)** out of phase with the voltage
- **(C)** leads the voltage by $\pi / 2$
- **(D)** lags behind the voltage by $\pi / 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) lags behind the voltage by $\pi / 2$**

**Detailed Solution:**

In a purely inductive circuit (an AC circuit containing inductance only) the current lags behind the voltage by $\frac{\pi}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/CGma-_s076Ry3cNJYY-qsldiNysmgcSz-KgM5BEu1U8.original.fullsize.png">

</details>

---

### Q178. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `3`

In a $L R$ circuit of $3 \mathrm{mH}$ inductance and $4 \Omega$ resistance, $\operatorname{emf} E=4 \cos 1000 t$ volt is applied. The amplitude of current is

**Options:**

- **(A)** $0.8 Å$
- **(B)** $\frac{4}{7} Å$
- **(C)** $1.0 Å$
- **(D)** $\frac{4}{\sqrt{7}} Å$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.8 Å$**

**Detailed Solution:**

$E=E_{0} \cos \omega t$
Given $E=4 \cos 1000 t$
From Eqs. (i) and (ii), we get
Peak value of emf, $E_{0}=4 \mathrm{~V}$
Augular fiequency, $\omega=1000 \mathrm{~Hz}$
Now pcak valuc of currcnt is
$$
\begin{aligned}
i_{0} &=\frac{E_{0}}{Z}=\frac{E_{0}}{\sqrt{R^{2}+X_{L}^{2}}} \\
&=\frac{E_{0}}{\sqrt{R^{2}+\omega^{2} L^{2}}}
\end{aligned}
$$
Putting $E_{0}=4 \mathrm{~V}, R=4 \Omega$,
$$
\begin{array}{l}
\omega=1000 \mathrm{~Hz}, \\
L=3 \mathrm{mH}=3 \times 10^{-3} \mathrm{H}
\end{array}
$$
we get $i_{0}=0.8 \mathrm{~A}$

</details>

---

### Q179. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

In $L-C-R$ circuit power factor at resonance is

**Options:**

- **(A)** less than one
- **(B)** greater than one
- **(C)** unity
- **(D)** Can't predicted

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) unity**

**Detailed Solution:**

In $L$ -C- $R$ circuit power factor at resonance in unity.

</details>

---

### Q180. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

Same current is flowing in two alternating circuits. The first circuit contains only inductance and the other contains only a capacitor. If the frequency of the emf of $\mathrm{AC}$ is increased, the effecton the value of the current will be

**Options:**

- **(A)** increases in the first circuit and decreases in the other
- **(B)** increases in both the circuits
- **(C)** decreases in both the circuits
- **(D)** decreases in the first circuit and increases in the other

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) decreases in the first circuit and increases in the other**

**Detailed Solution:**

$I_{L}=\frac{V}{X_{L}}$ and $I_{C}=\frac{V}{X_{C}}$
ie, $I_{L} \propto \frac{1}{\omega}$ and $I_{C} \propto \omega$
$\therefore$ with increase in $\omega, I_{L}$ decreases while $I_{C}$ increases.

</details>

---

### Q181. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `3`

What is the value of inductance $L$ for which the current is a maximum in a series $L C R$ circuit with $C=10 \mu \mathrm{F}$ and $\omega=1000 \mathrm{~s}^{-1}$ ?

**Options:**

- **(A)** $100 \mathrm{mH}$
- **(B)** $1 \mathrm{mH}$
- **(C)** Cannot be calculated unless $R$ is known
- **(D)** $10 \mathrm{mH}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $100 \mathrm{mH}$**

**Detailed Solution:**

Current in $L C R$ series circuit,
$i=\frac{V}{\sqrt{R^{2}+\left(X_{L}-X_{C}\right)^{2}}}$
where $V$ is rms value of current, $R$ is resistance, $X_{L}$ is inductive reactance and $X_{C}$ is capacitive reactance.

For current to be maximum, denominator should be minimum which can be done, if
$$
X_{L}=X_{C}
$$
This happens in resonance state of the circuit ie,
$$
\omega L=\frac{1}{\omega C}
$$
or $\quad L=\frac{1}{\omega^{2} C}$ ...(i)
$\begin{aligned} \text { Given, } \omega &=1000 \mathrm{~s}^{-1}, C=10 \mu \mathrm{F} \\ &=10 \times 10^{-6} \mathrm{~F} \\ \text { Hence, } L &=\frac{1}{(1000)^{2} \times 10 \times 10^{-6}} \\ &=0.1 \mathrm{H} \\ &=100 \mathrm{mH} \end{aligned}$

</details>

---

### Q182. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `3`

An electron is travelling along the $x$ -direction. It encounters a magnetic field in the $y$ -direction. Its subsequent motion will be

**Options:**

- **(A)** straight line along the $x$ -direction
- **(B)** a circle in the $x z$ -plane
- **(C)** a circle in the $y z$ -plane
- **(D)** a circle in the $x y$ -plane

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a circle in the $x y$ -plane**

**Detailed Solution:**

If a particle carrying charge $q$ and moving with velocity $v$ through a point in magnetic field experiences a deflecting force $F$, then magnetic field $\overrightarrow{\mathbf{B}}$ is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bmt_gSVKI5CI7uSh1ZMggZTfcDT7LB8CBmZ9Hn89Erc.original.fullsize.png">

Here,
$$
\begin{array}{l}
\overrightarrow{\mathbf{F}}=q \overrightarrow{\mathbf{v}} \times \overrightarrow{\mathbf{B}} \\
\overrightarrow{\mathbf{v}}=v_{x} \hat{\mathbf{i}} \text { and }
\end{array}
$$
$$
\overrightarrow{\mathbf{B}}=B_{y} \hat{\mathbf{j}}
$$
$\therefore$
$$
\overrightarrow{\mathbf{F}}=e v_{x} B_{y}(\hat{\mathbf{i}} \times \hat{\mathbf{j}})=e v_{x} B_{y} \hat{\mathbf{k}}
$$
Hence, subsequent motion of the charged particle will be a circle in the $x y$ -plane.

</details>

---

