# MHT CET Physics - Current Electricity

## Topic 3: Electric Cell or Battery

**Total Questions:** 9

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an electric circuit shown, each cell has e.m.f. $2V$ and internal resistance $1\,\Omega$. The external resistance is $2\,\Omega$. The value of current (in A) is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/15_may_shift_2__q39_d1.png" />

**Options:**

- **(A)** $2$
- **(B)** $1.25$
- **(C)** $0.4$
- **(D)** $1.2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1.2$**

**Detailed Solution:**

From the given circuit diagram, three cells are connected in series.

By observing the symbols of the cells, all three cells are oriented in the same direction (the longer line representing the positive terminal is on the left for each cell). Therefore, their electromotive forces (e.m.f.) will add up.

Total e.m.f. of the combination, $E_{eq} = E_1 + E_2 + E_3$
$E_{eq} = 2\text{ V} + 2\text{ V} + 2\text{ V} = 6\text{ V}$

The internal resistances of the cells are also in series.
Total internal resistance, $r_{eq} = r_1 + r_2 + r_3$
$r_{eq} = 1\,\Omega + 1\,\Omega + 1\,\Omega = 3\,\Omega$

The external resistance in the circuit is $R = 2\,\Omega$.

The total resistance of the circuit is the sum of the external resistance and the equivalent internal resistance:
$R_{total} = R + r_{eq} = 2\,\Omega + 3\,\Omega = 5\,\Omega$

The current $I$ flowing through the circuit is given by Ohm's law:
$I = \dfrac{E_{eq}}{R_{total}}$
$I = \dfrac{6}{5}\text{ A} = 1.2\text{ A}$

Answer: $1.2$

</details>

---

### Q2. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the following circuit, the current through $6 \Omega$ resistor is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/wf9rMqjrfYH9cFzl0X0f7s6hasfR3EP5GoPwNmc0Nv0.original.fullsize.png">

**Options:**

- **(A)** $\frac{1}{5} \mathrm{~A}$
- **(B)** $\frac{2}{5} \mathrm{~A}$
- **(C)** $\frac{1}{4} \mathrm{~A}$
- **(D)** $\frac{3}{4} \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{5} \mathrm{~A}$**

**Detailed Solution:**

The given circuit consists of two parallel branches, each containing a battery of emf $E = 3\text{ V}$ and an internal resistance $r = 3\Omega$.

For these two identical cells connected in parallel, the equivalent emf $E_{eq}$ is:

$E_{eq} = E = 3\text{ V}$

The equivalent internal resistance $r_{eq}$ of the two $3\Omega$ resistors in parallel is:

$r_{eq} = \dfrac{3 \times 3}{3 + 3} = 1.5\Omega$

This equivalent cell is connected across the external resistor $R = 6\Omega$.

The current $I$ through the $6\Omega$ resistor is given by Ohm's law for a complete circuit:

$I = \dfrac{E_{eq}}{R + r_{eq}}$

Substituting the values:

$I = \dfrac{3}{6 + 1.5} = \dfrac{3}{7.5}$

$I = \dfrac{30}{75} = \dfrac{2}{5}\text{ A}$

Answer: $\frac{2}{5} \mathrm{~A}$

</details>

---

### Q3. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The new switching circuit for the following circuit by simplifying the given circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/kqbO7rgj0yoiPmskEuxGaj0RnbqJ4JsAsaap5TYuUzg.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/N8LSrJYRy6dHPhUlGcZXeY2ctNEpDUDKUuBZSQ9g6P4.original.fullsize.png"/>
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/9vV8T0HN0Ozh5W_-Jz_S_Stx8b6mJDPe2pkZ841iCx4.original.fullsize.png"/>
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Y7VuvoFHqs1HbcPfPniu1nbpUl96CML-ug1bal2wmug.original.fullsize.png"/>
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/iQQlOTxzblR_PXUCKhat67FydaAeU6U6qQi--Zhu04s.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Y7VuvoFHqs1HbcPfPniu1nbpUl96CML-ug1bal2wmug.original.fullsize.png"/>**

**Detailed Solution:**

Let $p$ and $q$ represent the closed states of switches $S_1$ and $S_2$ respectively.

The switches $S_1'$ and $S_2'$ represent the states $\sim p$ and $\sim q$.

The given circuit consists of two parallel branches.

The upper branch has switch $S_1$ in series with a parallel combination of $S_2$ and $S_1$. Its boolean expression is:

$p \land (q \lor p)$

By the absorption law, this simplifies to:

$p \land (q \lor p) = p$

The lower branch has switches $S_1'$, $S_2'$, and $S_1$ in series. Its boolean expression is:

$\sim p \land \sim q \land p$

Since $p \land \sim p = F$ (False), this simplifies to:

$F \land \sim q = F$

The total expression for the circuit is the disjunction (OR) of the upper and lower branches:

$p \lor F = p$

This means the entire circuit is equivalent to a single switch $S_1$.

Therefore, the simplified circuit corresponds to the option with only switch $S_1$.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Y7VuvoFHqs1HbcPfPniu1nbpUl96CML-ug1bal2wmug.original.fullsize.png"/>

</details>

---

### Q4. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two batteries, one of e.m.f. $12 \mathrm{~V}$ and internal resistance $2 \Omega$ and other of e.m.f. $6 \mathrm{~V}$ and internal resistance $1 \Omega$, are connected as shown in the figure. What will be the reading of the voltmeter 'V'?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/b9N5msIBvv77vlYmmgYydTHJXyd_RHaaDVjFPoTUZfE.original.fullsize.png">

**Options:**

- **(A)** $12 \mathrm{~V}$
- **(B)** $8 \mathrm{~V}$
- **(C)** $6 \mathrm{~V}$
- **(D)** $4 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8 \mathrm{~V}$**

**Detailed Solution:**

The formula for the equivalent emf of the parallel combination of batteries is
$\varepsilon_e=r_{\text {eq }}\left(\frac{e_1}{r_1}+\frac{c_2}{r_2}\right)$
Here, $r_{\mathrm{rq}}$ is the equivalent resistance
$\begin{aligned}
& \frac{1}{r_{\text {eq }}}=\frac{1}{r_1}+\frac{1}{r_2} \\
& \frac{1}{r_{\text {84 }}}=\frac{1}{2}+\frac{1}{1} \\
& \frac{1}{r_{\text {eq }}}=\frac{3}{2}
\end{aligned}$
Substituting the values
$\begin{aligned}
\varepsilon_e & =r_{\infty}\left(\frac{e_1}{r_1}+\frac{e_2}{r_2}\right) \\
\varepsilon_{\mathrm{e}} & =\frac{2}{3}\left(\frac{12}{2}+\frac{6}{1}\right) \\
\varepsilon_e & =\frac{2}{3} \times 12 \\
\therefore \quad \varepsilon_e & =8 \mathrm{~V}
\end{aligned}$

</details>

---

### Q5. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In a potentiometer experiment, when three cells $\mathrm{A}, \mathrm{B}$ and $\mathrm{C}$ are connected in series, the balancing length is found to be $420 \mathrm{~cm}$. If cells A and B are connected in series the balancing length is $220 \mathrm{~cm}$ and for cells B and C connected in series the balancing length is $320 \mathrm{~cm}$. The emf of cells A, B and C are respectively in the ratio of

**Options:**

- **(A)** 2:3:5
- **(B)** 5:4:3
- **(C)** 1:1.2:2
- **(D)** 1.2:1:2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1:1.2:2**

**Detailed Solution:**

$\begin{aligned} & \mathrm{E}_{\mathrm{A}}+\mathrm{E}_{\mathrm{B}}+\mathrm{E}_{\mathrm{C}}=\mathrm{x}(420) \quad[\mathrm{x}=\text { potential gradient }] \\ & \mathrm{E}_{\mathrm{A}}+\mathrm{E}_{\mathrm{B}}=\mathrm{x}(220) \quad \therefore \mathrm{E}_{\mathrm{C}}=\mathrm{x}(420)-\mathrm{x}(220)=\mathrm{x}(200) \\ & \mathrm{E}_{\mathrm{B}}+\mathrm{E}_{\mathrm{C}}=\mathrm{x}(320) \quad \therefore \mathrm{E}_{\mathrm{B}}=\mathrm{x}(320)-\mathrm{x}(200)=\mathrm{x}(120) \\ & \mathrm{E}_{\mathrm{A}}=\mathrm{x}(220)-\mathrm{E}_{\mathrm{B}}=\mathrm{x}(100) \\ & \therefore \mathrm{E}_{\mathrm{A}}: \mathrm{E}_{\mathrm{B}}: \mathrm{E}_{\mathrm{C}}=100: 120: 200=1: 1.2: 2\end{aligned}$

</details>

---

### Q6. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit, current flowing through it is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/hK1_mZP4c1qttuwbANXA-C1BUxWBIC3nxeIobBj2eGk.original.fullsize.png">

**Options:**

- **(A)** $5 \mathrm{~A}$
- **(B)** $4 \mathrm{~A}$
- **(C)** $2 \mathrm{~A}$
- **(D)** $3 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5 \mathrm{~A}$**

**Detailed Solution:**

$i=\frac{200-10}{38}=\frac{190}{38}=5 \mathrm{~A}$

</details>

---

### Q7. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A $10 \mathrm{~m}$ long wire of resistance $20 \Omega$ is connected in series with a battery of e.m.f.
3 volt and a resistance of $10 \Omega$. The potential gradient along the wire in volt/meter
is

**Options:**

- **(A)** $0 \cdot 02$
- **(B)** $1 \cdot 2$
- **(C)** $0 \cdot 10$
- **(D)** $0 \cdot 20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0 \cdot 20$**

**Detailed Solution:**

(B)
Total resistance $\mathrm{R}=20+10=30 \Omega$
current I $=\frac{\mathrm{E}}{\mathrm{R}}=\frac{3}{30}=0.1 \mathrm{~A}$
p.d. acros wire $V=I R_{w}$
$=0.1 \times 20=2 \mathrm{~V}$
$\begin{aligned} \therefore \text { Potential gradient } &=\frac{\mathrm{V}}{\mathrm{L}} \\ &=\frac{2}{10}=0.2 \mathrm{~V} / \mathrm{m} \end{aligned}$

</details>

---

### Q8. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown, the potential difference across the $4.5 \mu \mathrm{F}$ capacitor is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aV131VI3amXRt8yNS98wRtV1ZjuklfRvfYknkbP9E0k.original.fullsize.png">

**Options:**

- **(A)** $\frac{8}{3}$ volt
- **(B)** 8 volt
- **(C)** 6 volt
- **(D)** 4 volt

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8 volt**

**Detailed Solution:**

$\vec{A}+(\hat{\imath}-2 \hat{\jmath}+2 \hat{k})+(-2 \hat{i}+\hat{\jmath}-\hat{k})=\frac{\hat{\jmath}}{\begin{array}{l}\text { unit } \\ \text { vector } \\ \text { along } \\ y-a x i s\end{array}}$
$\vec{A}=\hat{i}+2 \hat{\jmath}-\hat{k}$
$|\vec{A}|=\sqrt{6}$

</details>

---

### Q9. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Using Kirchhoff's law, find the current flowing through the given circuit.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/vuDIYRiOOrdPosDumP6GGFZsbIR_fp05V2XsuhRIxgM.original.fullsize.png">

**Options:**

- **(A)** $7 \cdot 5 \mathrm{~A}$
- **(B)** $5 \mathrm{~A}$
- **(C)** $10 A$
- **(D)** $3 A$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $5 \mathrm{~A}$**

**Detailed Solution:**

The two cells are opposing each other. The net emf in the circuit is $(200-10)=190 \mathrm{~V}$. $\therefore$ current $I=\frac{V}{R}=\frac{190}{38}=5 A$

</details>

---

