# BITSAT Physics - Semiconductors

## Topic 6: Logic gates

**Total Questions:** 8

---

### Q1. BITSAT 2024 (Memory Based Paper 3)

*Type:* `singleCorrect` | *Level:* `1`

Identify the correct output signal $Y$ in the given combination of gates for the given inputs $A$ and $B$ shown in the figure.
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/ujSic0Voj43cWH_-8RAbCTD-57kRnTK75jckshvhsUQ.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/YfXeDGQopqG6tMO5t6bC5Djle4SojKoPa39YOjWcw0E.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/Og9uTtikOfzAFM6iPQyP6E_tqGRNjJJEpp5nQcFAkEw.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/Tr_4KU5tXPA1dcoxKjGcJuQ3ccXFAUjEP3rQJNmmPRY.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/hEC3w66VRNtau_bAtSGt-suDIqN7tYeEOyvX-F91-QA.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/hEC3w66VRNtau_bAtSGt-suDIqN7tYeEOyvX-F91-QA.original.fullsize.png"/>**

**Detailed Solution:**

Given circuit can be shown as below
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/XZ-14F-tXvMgToujctQ1nR6f40En5VQ2UikgrArsaC4.original.fullsize.png"/>
Output, $Y=\overline{(\bar{A})(\bar{B})}=\bar{A}+\bar{B}=A+B$
The truth table will be<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/owlNEKb3-6zWtEmBYGWfImgbzzMXvm_89e-jGwqQXoI.original.fullsize.png"/>
The corresponding input and output waveforms are shown below.<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/qHUvT4JHyfp2YLpiFJvb21DAYQRFpcrM09evhjCcbas.original.fullsize.png"/>

</details>

---

### Q2. BITSAT 2024 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Identify the logic gate given in the circuit :
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/IvHjKsLo7Y1TZ5aAmCQc1hUgIWWLHOPX9l-ij77VNtc.original.fullsize.png"/>

**Options:**

- **(A)** NAND - gate
- **(B)** OR - gate
- **(C)** AND gate
- **(D)** NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) OR - gate**

**Detailed Solution:**

Output $\mathrm{Y}=\overline{\overline{\mathrm{A}} \cdot \overline{\mathrm{B}}}=\overline{\overline{\mathrm{A}+\mathrm{B}}}$ (ByDe-Morgan Law)
$\therefore Y=\mathrm{A}+\mathrm{B}$
This Boolean expression represents OR gate.

</details>

---

### Q3. BITSAT 2024 (Memory Based Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

Identify the logic operation performed by the following circuit.
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/pevr52nFLbuFxxUyqtWTiGAnE0iwx04freEB4-busxc.original.fullsize.png"/>

**Options:**

- **(A)** OR
- **(B)** AND
- **(C)** NOT
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) AND**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/df6PRL8vzhUjUVysJRvpsUhjaTC89_YUQTq_sUBcVZQ.original.fullsize.png"/>
$\mathrm{Y}=\overline{\overline{\mathrm{A}}+\overline{\mathrm{B}}}$
$=\overline{\overline{\mathrm{A}}} \cdot \overline{\overline{\mathrm{B}}}$
$=\mathrm{A} . \mathrm{B}$
So, $\mathrm{Y}=\mathrm{A} \cdot \mathrm{B}$
Therefore gate is AND gate.

</details>

---

### Q4. BITSAT 2023 (Memory Based Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

The logic operations performed by the given digital circuit is equivalent to:
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/BXaO_1eHuJsLMucprGNkUpNXeKEp53ZePPE4tLgOYQ4.original.fullsize.png">

**Options:**

- **(A)** AND
- **(B)** NOR
- **(C)** OR
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) AND**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/qVK9FXd8k-4NE2hDvgG2qByCP2qAhE1Tjun1aGX-xP4.original.fullsize.png">

$\begin{aligned} & \mathrm{Y}=\overline{\mathrm{Z}}=(\mathrm{A}+\mathrm{B}) \cdot(\mathrm{A} \cdot \mathrm{B})=\mathrm{A} \cdot \mathrm{A} \cdot \mathrm{B}+\mathrm{AB} \cdot \mathrm{B} \\ & \mathrm{Y}=\mathrm{AB}+\mathrm{AB}=\mathrm{A} \cdot \mathrm{B} \\ & \therefore \text { It is an } \mathrm{AND} \text { Gate. }\end{aligned}$

</details>

---

### Q5. BITSAT 2014

*Type:* `singleCorrect` | *Level:* `1`

The combination of gates shown below yields

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/EWo1Hg-0repPdxILuFh0Yk--LVUav_v0Q1Eqs-uv1iE.original.fullsize.png">

**Options:**

- **(A)** OR gate
- **(B)** NOT gate
- **(C)** XOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR gate**

**Detailed Solution:**

The final boolean expression is,

$$

X=\overline{(\bar{A} \cdot \bar{B})}=\overline{\bar{A}}+\overline{\bar{B}}=A+B \Rightarrow \text { OR gate }

$$

</details>

---

### Q6. BITSAT 2013

*Type:* `singleCorrect` | *Level:* `1`

The circuit is equivalent to

<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/vqymBaCvABIHeItSBnvLirbFMdZc6HFR5hwbqpZuYgE.original.fullsize.png">

**Options:**

- **(A)** AND gate
- **(B)** OR gate
- **(C)** Not gate
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) OR gate**

**Detailed Solution:**

$\begin{aligned} \mathrm{Y} &=\mathrm{A}+(\overline{\mathrm{A}} \cdot \mathrm{B})=(\mathrm{A}+\overline{\mathrm{A}}) \cdot(\mathrm{A}+\mathrm{B}) \\ &=\mathrm{A}+\mathrm{B} \\ \Rightarrow & \mathrm{OR} \text { gate } \end{aligned}$

</details>

---

### Q7. BITSAT 2011

*Type:* `singleCorrect` | *Level:* `1`

The output of an OR gate is connected to both the inputs of a NAND gate. The combination will serve as a:

**Options:**

- **(A)** NOT gate
- **(B)** NOR gate
- **(C)** AND gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) NOR gate**

**Detailed Solution:**

$(\overline{A+B})=$ NOR gate When both inputs of NAND gate are connected, it behaves as NOT gate $\mathrm{OR}+\mathrm{NOT}=\mathrm{NOR}$

</details>

---

### Q8. BITSAT 2009

*Type:* `singleCorrect` | *Level:* `2`

The truth table given below correspond to the logic gate
\begin{tabular}{cc|c}
$\mathrm{A}$ & $\mathrm{B}$ & $\mathrm{X}$ \\
\hline 0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
1 & 1 & 0
\end{tabular}

**Options:**

- **(A)** $\mathrm{OR}$
- **(B)** NOR
- **(C)** AND
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) NOR**

**Detailed Solution:**

The given gate is a NOR gate. The output is high, when all inputs are low.
Truth Table:
\begin{tabular}{|c|c|c|}
\hline $\mathbf{A}$ & $\mathbf{B}$ & $\mathbf{Y}$ \\
\hline 0 & 0 & 1 \\
\hline 1 & 0 & 0 \\
\hline 0 & 1 & 0 \\
\hline 1 & 1 & 0 \\
\hline \multicolumn{2}{|c|} { Logic Symbols } \\
\hline
\end{tabular}
<img src="https://cdn-question-pool.getmarks.app/pyq/bitsat/SAl1pjY7HKepM_U07OxoNd3okXgOIZ1vojjvHw6KR7A.original.fullsize.png">

Boolean expression: $\overline{\mathrm{A}+\mathrm{B}}=\mathrm{Y}$

</details>

---

