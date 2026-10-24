# JEE Main Physics - Semiconductors

## Topic 8: Logic gates

**Total Questions:** 82

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output $Y$ for the given inputs $A$ and $B$ to the circuit is:
<img style="width: 500px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d1.jpg" />

**Options:**

- **(A)** <img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d2.jpg" />
- **(B)** <img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d3.jpg" />
- **(C)** <img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d4.jpg" />
- **(D)** <img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d5.jpg" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q45_d3.jpg" />**

**Detailed Solution:**

From the circuit:
Top AND gate output: $A \cdot B$
Bottom AND gate output: $\bar{A} \cdot B$ (the $A$ input passes through a NOT gate)
The OR gate combines these:
$Y = (A \cdot B) + (\bar{A} \cdot B)$

Factoring out $B$:
$Y = B \cdot (A + \bar{A})$

Using $A + \bar{A} = 1$:
$Y = B \cdot 1 = B$

So $Y$ is independent of $A$ and follows $B$ exactly.

Reading the input waveform of $B$:
From $t = 0$ to $t = 1\text{ s}$: $B = 1$
From $t = 1$ to $t = 2\text{ s}$: $B = 1$
From $t = 2$ to $t = 3\text{ s}$: $B = 0$

Hence, $Y$ is $1$ from $0$ to $2\text{ s}$ and $0$ from $2$ to $3\text{ s}$.

This matches the waveform shown in option $(2)$.

Hence, the correct option is $(2)$.

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Refer to the logic circuit given below. For two inputs $(A=1, B=1)$ and $(A=0, B=1)$, output $(Y)$ will be __________.
<img style="width: 400px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/06APRS2__q43_d1.jpg" />

**Options:**

- **(A)** $1, 0$ respectively
- **(B)** $0, 1$ respectively
- **(C)** $0, 0$ respectively
- **(D)** $1, 1$ respectively

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0, 0$ respectively**

**Detailed Solution:**

From the given logic circuit, we can determine the Boolean expression for the output $Y$.

The output of the NOT gate is $\bar{A}$.

The inputs to the OR gate are $\bar{A}$ and $B$, so its output is $\bar{A} + B$.

The inputs to the AND gate are $\bar{A}$ and $B$, so its output is $\bar{A} \cdot B$.

These two outputs are fed into a NOR gate. The final output $Y$ is given by:

$Y = \overline{(\bar{A} + B) + (\bar{A} \cdot B)}$

Simplifying the Boolean expression:

$Y = \overline{\bar{A} + B + \bar{A}B}$

$Y = \overline{\bar{A} + B(1 + \bar{A})}$

$Y = \overline{\bar{A} + B}$

Using De Morgan's laws:

$Y = \overline{\bar{A}} \cdot \bar{B} = A \cdot \bar{B}$

Now, we evaluate $Y$ for the given input combinations:

For $A = 1, B = 1$:

$Y = 1 \cdot \bar{1} = 1 \cdot 0 = 0$

For $A = 0, B = 1$:

$Y = 0 \cdot \bar{1} = 0 \cdot 0 = 0$

Therefore, the outputs are $0$ and $0$ respectively.

Answer: $0, 0$ respectively

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the given logic circuit, which of the following inputs combination will make both LED$-1$ and LED$-2$ to glow?
<img style="width: 450px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS1__q45_d1.png" />

**Options:**

- **(A)** $A = 0, B = 1, C = 1$
- **(B)** $A = 1, B = 0, C = 0$
- **(C)** $A = 1, B = 0, C = 1$
- **(D)** $A = 1, B = 1, C = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $A = 1, B = 0, C = 1$**

**Detailed Solution:**

Let the output of the OR gate be $Y_1$.

$Y_1 = A + B$

For LED-1 to glow, $Y_1$ must be $1$, which means $A + B = 1$.

Let the output of the first AND gate be $Y_2$.

$Y_2 = Y_1 \cdot C = (A + B) \cdot C$

Let the output of the second AND gate be $Y_3$.

$Y_3 = A \cdot Y_2 = A \cdot (A + B) \cdot C$

For LED-2 to glow, $Y_3$ must be $1$.

Simplifying the Boolean expression for $Y_3$:

$Y_3 = (A \cdot A + A \cdot B) \cdot C$

$Y_3 = (A + AB) \cdot C$

$Y_3 = A(1 + B) \cdot C$

$Y_3 = A \cdot C$

For $Y_3 = 1$, we require $A = 1$ and $C = 1$.

If $A = 1$, then $Y_1 = 1 + B = 1$ for any value of $B$, satisfying the condition for LED-1 to glow.

From the given options, the combination $A = 1, B = 0, C = 1$ satisfies these conditions.

Answer: $A = 1, B = 0, C = 1$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two $4$ bits binary numbers, $A = 1101$ and $B = 1010$ are given in the inputs of a logic circuit shown in figure below. The output $(Y)$ will be:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/04APRS1__q38_d1.png" />

**Options:**

- **(A)** $Y = 1101$
- **(B)** $Y = 0010$
- **(C)** $Y = 0111$
- **(D)** $Y = 1000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $Y = 1101$**

**Detailed Solution:**

From the given logic circuit, the input $A$ passes through a NOT gate, giving $\overline{A}$.

This output $\overline{A}$ and the input $B$ are then fed into a NAND gate.

The Boolean expression for the final output $Y$ is:
$Y = \overline{\overline{A} \cdot B}$

Given the $4$-bit binary inputs:
$A = 1101$
$B = 1010$

First, find the bitwise NOT of $A$:
$\overline{A} = \overline{1101} = 0010$

Next, find the bitwise AND of $\overline{A}$ and $B$:
$\overline{A} \cdot B = 0010 \cdot 1010 = 0010$

Finally, apply the NOT operation for the NAND gate:
$Y = \overline{0010} = 1101$

Alternatively, using De Morgan's laws:
$Y = \overline{\overline{A} \cdot B} = A + \overline{B}$
$Y = 1101 + \overline{1010} = 1101 + 0101 = 1101$

Therefore, the output $Y$ is $1101$.

Answer: $Y = 1101$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X$ and $Y$ are the inputs, the given circuit works as _______.
<img style="width:600px;"  src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/02APRS2__q30_d1.png" />

**Options:**

- **(A)** OR gate
- **(B)** AND gate
- **(C)** NAND gate
- **(D)** NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NOR gate**

**Detailed Solution:**

The circuit consists of four NAND gates.

The first two NAND gates have their inputs tied together, acting as NOT gates. Their outputs are $\overline{X}$ and $\overline{Y}$.

These outputs are fed into the third NAND gate. The output of this gate is:
$y' = \overline{\overline{X} \cdot \overline{Y}}$

Using De Morgan's theorem:
$y' = \overline{\overline{X}} + \overline{\overline{Y}} = X + Y$

This output is fed into the fourth NAND gate, which also has its inputs tied together, acting as a NOT gate. The final output is:
Output $= \overline{X + Y}$

This represents the Boolean expression for a NOR gate.

Answer: NOR gate

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Identify the correct truth table of the given logic circuit.
<img style="width:400px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_q_28_1.png">

**Options:**

- **(A)** \(\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 1 \\ \hline 0 & 1 & 0 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}\)
- **(B)** \(\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 1 \\ \hline 0 & 1 & 1 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}\)
- **(C)** \(\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 0 \\ \hline 0 & 1 & 1 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}\)
- **(D)** \(\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 0 \\ \hline 0 & 1 & 0 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 0 \\ \hline 0 & 1 & 0 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}\)**

**Detailed Solution:**

Analysing the logic circuit:

The output is $Y = A \cdot \overline{A \cdot B}$

$= A \cdot (\bar{A} + \bar{B})$

$= A\bar{A} + A\bar{B} = 0 + A\bar{B} = A\bar{B}$

Truth table:
$A=0, B=0 \Rightarrow Y=0$
$A=0, B=1 \Rightarrow Y=0$
$A=1, B=0 \Rightarrow Y=1$
$A=1, B=1 \Rightarrow Y=0$

</details>

---

### Q7. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the given logic gate circuit, which of the following is the correct truth table? 
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S2_q_39_1.png">

**Options:**

- **(A)** \(\begin{array}{c|c|c} n & m & z \\ \hline 0 & 0 & 0 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{array}\)
- **(B)** \(\begin{array}{c|c|c} n & m & z \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \\ 1 & 0 & 0 \end{array}\)
- **(C)** \(\begin{array}{c|c|c} n & m & z \\ \hline 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{array}\)
- **(D)** \(\begin{array}{c|c|c} n & m & z \\ \hline 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{array}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(\begin{array}{c|c|c} n & m & z \\ \hline 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{array}\)**

**Detailed Solution:**

The given logic circuit consists of an OR gate and a NAND gate.
The output of the OR gate is $y = n + m$.
The inputs to the NAND gate are $n$ and $y$.
The final output $z$ is given by $z = \overline{n \cdot y} = \overline{n \cdot (n + m)}$.
Using Boolean algebra: $n \cdot (n + m) = n \cdot n + n \cdot m = n + n \cdot m = n(1 + m) = n$.
Therefore, $z = \overline{n}$.
Let's verify this with the truth table:
<table border='1'><tr><th>n</th><th>m</th><th>y = n + m</th><th>z = NAND(n, y)</th></tr><tr><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td></tr></table>
Comparing this with the given options, option (4) matches the calculated truth table.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The correct truth table for the given input data of the following logic gate is : 
 Inputs 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S2_q_30_1.png">

**Options:**

- **(A)** \(\begin{array}{|c|c|c|c|c|} \hline A & B & C & D & Y \\ \hline 1 & 1 & 0 & 1 & 0 \\ \hline 0 & 0 & 1 & 1 & 0 \\ \hline 1 & 0 & 1 & 0 & 1 \\ \hline 1 & 1 & 1 & 1 & 1 \\ \hline \end{array}\)
- **(B)** \(\begin{array}{|c|c|c|c|c|} \hline A & B & C & D & Y \\ \hline 1 & 1 & 0 & 1 & 0 \\ \hline 0 & 0 & 1 & 1 & 1 \\ \hline 1 & 0 & 1 & 0 & 1 \\ \hline 1 & 1 & 1 & 1 & 1 \\ \hline \end{array}\)
- **(C)** \(\begin{array}{|c|c|c|c|c|} \hline A & B & C & D & Y \\ \hline 1 & 1 & 0 & 1 & 1 \\ \hline 0 & 0 & 1 & 1 & 0 \\ \hline 1 & 0 & 1 & 0 & 0 \\ \hline 1 & 1 & 1 & 1 & 1 \\ \hline \end{array}\)
- **(D)** \(\begin{array}{|c|c|c|c|c|} \hline A & B & C & D & Y \\ \hline 1 & 1 & 0 & 1 & 1 \\ \hline 0 & 0 & 1 & 1 & 0 \\ \hline 1 & 0 & 1 & 0 & 1 \\ \hline 1 & 1 & 1 & 1 & 0 \\ \hline \end{array}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \(\begin{array}{|c|c|c|c|c|} \hline A & B & C & D & Y \\ \hline 1 & 1 & 0 & 1 & 1 \\ \hline 0 & 0 & 1 & 1 & 0 \\ \hline 1 & 0 & 1 & 0 & 0 \\ \hline 1 & 1 & 1 & 1 & 1 \\ \hline \end{array}\)**

**Detailed Solution:**

<img style="width:450px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S2_s_30.png">

</details>

---

### Q9. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Find the correct combination of $\mathrm{A}, \mathrm{B}, \mathrm{C}$ and D inputs which can cause the LED to glow.
<img style="width:250px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_q_35_1_v2.png">

**Options:**

- **(A)** 1101
- **(B)** 0011
- **(C)** 1000
- **(D)** 0100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1101**

**Detailed Solution:**

The LED will glow if it is forward biased, which means the potential at the p-side must be higher than the potential at the n-side.
Let $Y_1$ be the output of the upper NAND gate (p-side) and $Y_2$ be the output of the lower NOR gate (n-side).
For the LED to glow, we need $Y_1 = 1$ and $Y_2 = 0$.
The upper circuit consists of two NOT gates (NOR gates with shorted inputs) followed by a NAND gate.
Output of first NOT gate is $\bar{A}$, and second is $\bar{B}$.
$Y_1 = \overline{\bar{A} \cdot \bar{B}} = \overline{\bar{A}} + \overline{\bar{B}} = A + B$ (using De Morgan's Law).
The lower circuit is a NOR gate with inputs $C$ and $D$.
$Y_2 = \overline{C + D}$.
Condition 1: $Y_1 = 1 \implies A + B = 1$. This means at least one of $A$ or $B$ must be 1.
Condition 2: $Y_2 = 0 \implies \overline{C + D} = 0 \implies C + D = 1$. This means at least one of $C$ or $D$ must be 1.
Checking the options:
(1) $A=1, B=1, C=0, D=1$: $Y_1 = 1+1 = 1$ and $Y_2 = \overline{0+1} = 0$. (Satisfied)
(2) $A=0, B=0, C=1, D=1$: $Y_1 = 0+0 = 0$. (Not satisfied)
(3) $A=1, B=0, C=0, D=0$: $Y_2 = \overline{0+0} = 1$. (Not satisfied)
(4) $A=0, B=1, C=0, D=0$: $Y_2 = \overline{0+0} = 1$. (Not satisfied)
Thus, the correct combination is 1101.

</details>

---

### Q10. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The given circuit works as : 
 <img style="width:500px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S1_q_40_1.png">

**Options:**

- **(A)** AND gate
- **(B)** NAND gate
- **(C)** NOR gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) NAND gate**

**Detailed Solution:**

Let the inputs be A and B. The circuit is composed of NOR gates.
A NOR gate with its inputs tied together acts as a NOT gate.
The output of the first NOR gate (input A) is $Y_1 = \overline{A+A} = \bar{A}$.
The output of the second NOR gate (input B) is $Y_2 = \overline{B+B} = \bar{B}$.
These outputs are fed into a third NOR gate. Its output is $Y_3 = \overline{Y_1 + Y_2} = \overline{\bar{A} + \bar{B}}$.
Using De Morgan's theorem, $Y_3 = (\overline{\bar{A}}) \cdot (\overline{\bar{B}}) = A \cdot B$.
This output $Y_3$ is the input to the fourth NOR gate, which is configured as a NOT gate.
The final output is $Y_{out} = \overline{Y_3} = \overline{A \cdot B}$.
The expression $\overline{A \cdot B}$ represents a NAND gate.

</details>

---

### Q11. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider the following logic circuit.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zS7ywEGbj81vSAHFPfa0RFUt6oFeSVnZIJH-YVSY7KQ.original.fullsize.png"/>
The output is $\mathrm{Y}=0$ when :

**Options:**

- **(A)** $\mathrm{A}=1$ and $\mathrm{B}=1$
- **(B)** $\mathrm{A}=0$ and $\mathrm{B}=1$
- **(C)** $\mathrm{A}=1$ and $\mathrm{B}=0$
- **(D)** $\mathrm{A}=0$ and $\mathrm{B}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\mathrm{A}=1$ and $\mathrm{B}=1$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uzHl0kYsCGoXD3inWyVtRr6GBZD_STGedw3XNkyoqkI.original.fullsize.png"/>
$\begin{aligned}
& \mathrm{Y}_1=\mathrm{A} \cdot \mathrm{~B}, \mathrm{Y}_2=\overline{\mathrm{A}}+\mathrm{B} \\
& \mathrm{Y}=\overline{\mathrm{Y}_1 \cdot \mathrm{Y}_2}=\overline{\mathrm{Y}}_1+\overline{\mathrm{Y}}_2 \\
& \mathrm{Y}=\overline{\mathrm{A} \cdot \mathrm{~B}}+\overline{\mathrm{A}+\mathrm{B}} \\
& \mathrm{Y}=\overline{\mathrm{A}}+\overline{\mathrm{B}}+\mathrm{A} \cdot \overline{\mathrm{~B}}
\end{aligned}$
$\begin{array}{|c|c|c|} \hline A & B & Y \\ \hline 0 & 0 & 1 \\ \hline 1 & 0 & 1 \\ \hline 0 & 1 & 1 \\ \hline 1 & 1 & 0 \\ \hline \end{array}$

</details>

---

### Q12. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The Boolean expression $\mathrm{Y}=\mathrm{A} \overline{\mathrm{B}} \mathrm{C}+\overline{\mathrm{A}} \overline{\mathrm{C}}$ can be realised with which of the following gate configurations.
A. One 3-input AND gate, 3 NOT gates and one 2input OR gate, One 2-input AND gate,
B. One 3-input AND gate, 1 NOT gate, One 2input NOR gate and one 2-input OR gate
C. 3-input OR gate, 3 NOT gates and one 2-input AND gate
Choose the correct answer from the options given below

**Options:**

- **(A)** B, C Only
- **(B)** A,B Only
- **(C)** A, B, C Only
- **(D)** A, C Only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) A,B Only**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ljhWCIs01uM_LD9XLVWqRjQK6rU0X6fPSmwWyFtlQyc.original.fullsize.png"/>
$\because \overline{\mathrm{A}} \cdot \overline{\mathrm{C}}+\overline{\mathrm{A}+\mathrm{C}} \equiv \mathrm{NOR}$ gate

</details>

---

### Q13. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The truth table corresponding to the circuit given below is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/buTi8FyGGrd7QC2TsdlkYgHoDDIG1Il0UUr9eyhv4NU.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ADDFWGlQawhR-KxYHFle-xZb-BdmKnPMfYFRxH3A6xk.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5NSpata6sXPpnGTn-DY8hXOUPgpM3QzUPOOIFx9D3CA.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pmDicgd0HctVJsuTwo2XWsDcmSxjgP12ySjdb9SOVwY.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QLKLPfACAVm7oJ1O9077-N183C2jssrUDVgxNhnNqbU.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5NSpata6sXPpnGTn-DY8hXOUPgpM3QzUPOOIFx9D3CA.original.fullsize.png"/>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Uw1L_9EXebXaaL6slIPzvoNEAPQOO3JNAbu1zG5qjCY.original.fullsize.png"/>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qXAmve0pMlM8inBrk9VdvjlpcbgRygP3u8LqlY1j4Do.original.fullsize.png"/>

</details>

---

### Q14. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Choose the correct logic circuit for the given truth table having inputs A and B.
$\begin{array}{|c|c|c|} \hline \text{Inputs} & & \text{Output} \\ \hline A & B & Y \\ \hline 0 & 0 & 0 \\ \hline 0 & 1 & 0 \\ \hline 1 & 0 & 1 \\ \hline 1 & 1 & 1 \\ \hline \end{array}$

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_vJDFNNG0eg1SGZx5pN4hzZbNZQSVILbTBf_VxQ7yu8.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dyTilMlp8LBu2-8XH2pH-CQS7fznuFYltFenz5XCZGc.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/T9svxTwNbCrUYwi4SAQa_9jQHijh6L8VWoMHxpDuxqY.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vGWvwXOQq0gOFzdSCm5B9Sb3pSwXPoaMYhl3sS-tTls.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dyTilMlp8LBu2-8XH2pH-CQS7fznuFYltFenz5XCZGc.original.fullsize.png"/>**

**Detailed Solution:**

Only option (2) matches with the truth table

</details>

---

### Q15. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In the digital circuit shown in the figure, for the given inputs the P and Q values are :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BKSL_LTevT0TaTScfrimmbqvp1sOUyKo0k5HuFgyL2c.original.fullsize.png"/>

**Options:**

- **(A)** $P=1, Q=1$
- **(B)** $P=0, Q=0$
- **(C)** $P=0, Q=1$
- **(D)** $P=1, Q=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $P=0, Q=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tvs3rxSLvtWUptAtc-jmBGCMhfklb07jRBmWQ8okLQk.original.fullsize.png"/>

</details>

---

### Q16. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The truth table for the circuit given below is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZBH8TjgadYLofzQ95AFOTf56ChJMjpl65mCrC9NUeHk.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/UmZ3B6-aOPn6EUaReWzzRidxn3IPkOdIeqxViCdiLnM.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/p5qKbmGzJJc41-p3db2BrJ5Pi2f5_0h06rMww2AXvJ4.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ZIa--NJvQDdZpEaUBK0Vf2Y0zbW1PPpSIQeKmNn_VDg.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ucPu1GSqDovyj7EGBDZ6NkUAumGDI1plckhYfMYDBJ0.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ucPu1GSqDovyj7EGBDZ6NkUAumGDI1plckhYfMYDBJ0.original.fullsize.png"/>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jEsmHQmHqPb7TE6f0bsf22QyJdtN_kFHGx0N8Ns4VrI.original.fullsize.png">

</details>

---

### Q17. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/BkG07Xo5wOArBeJYM9lrXyLfLWXWPAILHyi6ZhSjKs0.original.fullsize.png"/>

For the circuit shown above, equivalent GATE is :

**Options:**

- **(A)** OR gate
- **(B)** NAND gate
- **(C)** NOT gate
- **(D)** AND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR gate**

**Detailed Solution:**

$\begin{array}{l|l|l}
A & B & Y \\
\hline 0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1
\end{array}$
$\Rightarrow$ OR Gate

</details>

---

### Q18. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following circuits has the same outpur as that of the given circuit?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xCI86ZDwT_cqlPqxW0hfqHXjqxnYmkQRZc8et7Rhf-k.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vpvra1Q8RnVG-Kn-fAU6JXJ0-5DQU4dzmJN-mfsMkww.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/VmI-Qpkuo0mxykHGPYAnDEbcxwVMu_Fbo5ljkx5xSRM.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3K0qZ293Jm1RZJz27kaCS8mLNWesG3DzXGaMm3bU0Bk.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gkLHig9SRraUb_51p_K_C1qCOXMVjBM20YohV9XJPwc.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/VmI-Qpkuo0mxykHGPYAnDEbcxwVMu_Fbo5ljkx5xSRM.original.fullsize.png"/>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vqFjROqMj_thHjSCJ3CJ8zfmmZT4PKEcxOByZzDPneg.original.fullsize.png">


$\begin{aligned} & \mathrm{P}=\mathrm{A} \cdot \overline{\mathrm{B}} \\ & \mathrm{Q}=\mathrm{A} \cdot \mathrm{B} \\ & \mathrm{Y}=\overline{\mathrm{P}+\mathrm{Q}}=\overline{\mathrm{A} \cdot \overline{\mathrm{B}}+\mathrm{A} \cdot \mathrm{B}} \\ & =\overline{\mathrm{A} \cdot(\mathrm{B}+\overline{\mathrm{B}})}=\overline{\mathrm{A} \cdot \mathrm{I}} \\ & \mathrm{Y}=\overline{\mathrm{A}}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output of the circuit is low (zero) for :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Gyq8y3R7vrEWGcAyIKh786FlvQ9awB0nHJV9pbER9n4.original.fullsize.png"/>


(A) $\mathrm{X}=0, \mathrm{Y}=0$
(B) $X=0, Y=1$
(C) $X=1, Y=0$
(D) $\mathrm{X}=1, \mathrm{Y}=1$

Choose the correct answer from the options given below :

**Options:**

- **(A)** (B), (C) and (D) only
- **(B)** (A), (B) and (C) only
- **(C)** (A), (C) and (D) only
- **(D)** (A), (B) and (D) only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (B), (C) and (D) only**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1ewPpGUjC3pW9rN_4re2fDxzgpj312_vEaEW7OyKCDU.original.fullsize.png">


$\begin{array}{c|c|c}
x & y & \\
\hline 0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 0
\end{array}$

</details>

---

### Q20. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5FlfMWzwy0aiLAvnj59Jc3GPW697E-n3QryfnQL6ljc.original.fullsize.png"/>




\begin{array}{c|c|c} A & B & Y \\\hline 0 & 0 & 1 \\0 & 1 & 1 \\1 & 0 & 0 \\1 & 1 & 1\end{array}


To obtain the given truth table, following logic gate should be placed at G:

**Options:**

- **(A)** OR Gate
- **(B)** AND Gate
- **(C)** NOR Gate
- **(D)** NAND Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NOR Gate**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OaF_pJ0A_vJDbGOpMtI9J9VqVG0P0uPXnDMe6roMjus.original.fullsize.png">




For NOR gate : $\overline{\mathrm{A} \overline{\mathrm{B}}}=\overrightarrow{\mathrm{A}}+\mathrm{B}$<img src="data:image/jpeg;base64,/9j/4QAYRXhpZgAASUkqAAgAAAAAAAAAAAAAAP/sABFEdWNreQABAAQAAABQAAD/4QMvaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjM0OTksIDIwMTgvMDgvMTMtMTY6NDA6MjIgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFRDQwREJDRkVFQzAxMUVGOTFFOEJFQjM4QUMyMjI0NCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFRDQwREJEMEVFQzAxMUVGOTFFOEJFQjM4QUMyMjI0NCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkVENDBEQkNERUVDMDExRUY5MUU4QkVCMzhBQzIyMjQ0IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkVENDBEQkNFRUVDMDExRUY5MUU4QkVCMzhBQzIyMjQ0Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+/+4ADkFkb2JlAGTAAAAAAf/bAIQAAgICAgICAgICAgMCAgIDBAMCAgMEBQQEBAQEBQYFBQUFBQUGBgcHCAcHBgkJCgoJCQwMDAwMDAwMDAwMDAwMDAEDAwMFBAUJBgYJDQsJCw0PDg4ODg8PDAwMDAwPDwwMDAwMDA8MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM/8AAEQgAqwD1AwERAAIRAQMRAf/EAHgAAQADAQEBAQEAAAAAAAAAAAAGBwgFBAkBAwEBAAAAAAAAAAAAAAAAAAAAABAAAAYCAgEDAgMEBwkAAAAAAAECAwQFBgcREgghExQiFTFBFlFhI3axYrO2FzgJcTIzJXUmNkYYEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwD7+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADiZLkNRiOO32V5BLTAosZrpVrczlEZkzFhtKeecMi9T6oQZ8EA5Wvs8xjaGEYtsPC7ErXFsxrWLSkndTQpTD6SURLQr1QtB8pWk/VKiNJ+pAJgAAKFu/IzAqLZVhqN+qy2wzutp0ZC/UVmOWU4lVLj5xkzW3Y7K0LaN5Jt8pM/qIy49AE311tTBdrV9tYYRcLsP09Yu0+SVcuJKrbGssGCSpyLOgTmmJMdwiUR8ONlyRkZckfICwwHCyfIImKY/b5JPiT50KljLly4lXEenzFtt+qvZix0rddURevVCTM/wAiAQ7U+3cK3ZgFbs3XsuVaYhcnI+1T34r0Vx8orimnTQy8lK/RxCk+pfiRkA6GtNk45tnE4ebYkix/T1i663XSrKC/XrkJZV0N5luQhCltKMj6OEXVZeqTMvUBPgAAAAAAAAAAAAAAAAAAAAAAAAAAAZp8hcgkvS9b61rsbtsvXlt0m9y6kpExly/05jTjEySZplyIzRtvz1wYrqVLLs085wR8cAKS8S8ik4BtbdfjbbY3bYXT/Ne2hpKiu0xm3047fyVfdYbKIkiS0lqDaG50InDV1eIzIgH0DAAHz7ymHnUz/ULmN4DkNDjlonx0gqkSsgppV1HW1+rJpEhDMW0qlIV24Psbii45Lr68kEi8XnTxjcXktrbLmCstxKs6bNc8zyE6Squ5i3MRUeuKJE9ttVeURqGbXxnFPK4+v5D3YzSG4gAB80L/AF1Y688nGtFYPkKse0t5ZV91mGb4pHStt6qn0io33lNM+2tPxm7tuQ22+RFy3/EWyaFmjqH0kgQIVXBhVlZDZr62uYbi18CMhLTLDDKSQ2022giSlKEkRERFwRAPWAAAAAAAAAAAAAAAAAAAAAAAAAAACBt63xVvYr+1Et2R5lIp00K5KrWwVCKAlz3SaRXKkHDQfuF2NSWSUZ+pmA4WQ6S15lOzsQ3DcQLNzYGCRXYWL28a5tIjMeNIPl9pUKPKbiupe9PcJxpRLIkkrnqXAWyAAKJvPHHWOQbEn7XmFlMTPrKqRRyr+ry7I6xX2xt45CYTbUGxYabZJ0zc6ISRdzNX4mZgJlgGqMC1id+7htGuDYZXLROym+mzJlpa2chpHttLm2Vi9JlyPbR9KCcdUSC5JPHICxAABT99orXeS7OxzcNtGu3M+xJpcfHbNjILiNGisPe2T7KIDExEQ23/AGk+6g2jS5x9ZKAXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMy+SeyMqw89M4Pg9n9hyXdWwa/EjyVLDMl6srCjyJ9lLjNSUOsKfJiKbbXutrQSl9jQrrwYeHUee5dF3ruvQ2X5FIzGPhVXjuV4Nk9gxEZsXK27RIZkxJhwWIrCzjyYivbWTSVGhZEvspPYw1QAAMkZLmWb575M2ejcYzaw15jGDa8jZZkl5SRq56xmWtzPeiQY3e0iTmUMR2Yq3VElslLWpJGrok0qCWeK21Mh29pyqyLMSjHmtJb3eLZg/Da9mO/YUFlIrnJLbfJkgn0spdNJeiTUaS9CAaLAAGUMw2Jsii8udMa0bv649a5/i2VW0qhZrSRNKVSNwSbN+e4+8biTXJUpJNNs8ccK9z8QGrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAGY/JXXOU5arS+dYVVqyDIdKbCr8texpp5liRZVSo8mvso0VclxpknyYlG62TjiEqNHQ1J7cgPFqPBcrm743ZvnKcdlYjBzKqx3E8Ex6xcjqsft1IiQ/KmykRHpDbXyJMsyaQbnckN9lkk19SDVIAAyPkeI5lr/ybtN40OGWefYnneu4uKZDVUTsErGFb0tg9LgvG1PlRELYksyltGpKzNtaEmsiQo1JCV+Kmrci1JpuroMzSwzmt9cXeV5fEiuk+xGn5BZSLFcVDqfpX8dLyWjUn6VKSak+hkA0aAAMabGxzYdh5g6Gzuo1nd22BYHjuTUmR5gxKp0Rm3shKB7DiGH7FqWttn46/dMmOxenRKwGywAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARbLc4w/A4UGxzPJK/GYNnMTXV0mxfQwl+Wttx5LDXYy7rNtlaiSXrwlR/gRgIXQ790plFnApsd2ljVza2s92rrYESwZccfnMJWp2K2klfU6gm1mpBfUXU+S9AFugACJV+eYfbZff4DW5BFm5hi0OJYZFQsqNT0ONOU4mMt3guqfcNlfBc8+n4AJaAAIkvPMPbzeNrdWQRf11LqH75jGSUapJ1sZ5mO7JMiIySlLj7afqMjPt6EfqAW2eYfRZTimE22QRYWWZwcssUoFqM5E34EdcqSptKSPhLbTalGpXBenHPPoAloAAh+c59ietqBeS5nbFU1Xyo0COaWXpUiTMmupYixIkWMh1+Q+84okoaaQpaj/AASA8WDbMw7Yv39rGLCQuxxSamuyihsYUussq6S40h9tEqDOaYfbJxpaVtqNHVaT7IUovUBPQABXmxNs631NArbLYuYV2KR7mY1Apm5azN+ZJecQ0hqNHbJbryu7qSPog+vJGrgvUBYYAAAK8kbZ1vF2LW6kczCuVsm1hvz4uGsrN6amNGbS646+hslEwnotJp9009ufp5AWGAAAAAAAAAAAAAi+GUNpjGN19Jc5ZZZzZQjfORlFuiK3Mk+6+46gnUw2Y7Je2lZNp6tl9KS55VyZh3ZEGHLegSJUZt9+rfOVXOrSRqZeUy5HNxB/ko2nlo5/Yoy/MBi3w+rEWuu90x+rBSmt7bIkVkmQz76I8tnIZC2H/b7IMzbWRHwSi5/DkBVmF7i8gJGmfHfc+Q7Kr7I9uZpgmO2+JxqCJGYYj2945X2C0ye63DU+w4jgiJPtqQRpM+Vcg39sPY9jinlti7WdWFRD1lsPXNPjkyuYgsyl1WTFQOz4MlxUZZLbM7N0iMiSs0pShalpNZLD37GLYVDvryMt8Hz86HIcN8fcWuDyGbWQ58ic/Wz8pfaQ62aGoyEOqb4d6MkfB/w/bP1AacyTML/KPFa22HW2sjEMmu9YLyeLaVJNe7BmPU/ziOP8pt9BdVnwRqSZkX4GSuDAUljuUZzRal8dMbo9iTpFtkGrnL1+BGhV8zJpLsSsrPirZKRFRXtV8RUhfyHZRpcUtUdtLqnHDJQVrjGSbF3bsfxOzSqyuHr/ADnYPjdf3VzkUerbsUR35k/Fnn/iRJLpNp5dV6e53Ikcp47GS0h7sP2Hl+ys58KrjP24Sszx/YG1sSyKzrGlMwbCTjdTdVK50VtSlGhEj4vc0kZklRqIvQiAWvqjZu6tpI1Ztqjk1qNYZlY2LOa43aPQGmYUBTz8WCmrcYa+X86PJabafRIcUh1RudEMn0SQbXAYr8tPdPYHhcUrn7Ae7YRzuf8Ah/NKltTr+37/AHeev7/38APzXPul52eS5V/P21Wu8AVkPT/c+4+7bFG7/wBf43PH9UBtUAAYn/1Av8ub/wDPWB/3orQG2AAAAYn2f/np8Vf5F2N/RUANsAAAAAAAAAAAAi2R4XjeWTcUsb+AubMwi3Te4y6iTIYKPPTHeik6pLDjaXS9qQ4no6SkevPXkiMgScKxuZmVTn8iAteWUdXMpauyKTIShuDPdYekNHHS4TCzWuO2fZSDUnjhKiIz5CSutpeacZWaiQ6k0KNC1IURKLg+q0GSkn+wyPkgFa4Bp7AdX1GSUWD19jUVuW2c66vW3bq2muOWFktTkuS2/MlvusuOrUa1G0pP1fV+PqAjifHLUbWqK/Skagnxde0smNNoK9F1bKm10qFLTOiSIVm5LXNYWxIQTjZoeLqfoXoZkA8SvGHTDtZsaok45YTIe2DrXM9OTe3Dz05+oajtwpRvrmG63Jb+K2v5CFJeUsu6lmr1AdV7x81XIn5TayKi3fsc2xdjDcpmuZFeqcmUsf3vbjLUc/0VzIdUbqeHVKcWpSzUtRmE7qMFxakweFreDWKVhdfTpoI1NLkSJv8Ay1LPxijrflOOvOJ9r6OVrM+PzAVbG8YNMxGcFZj0Fq3/AIc10qlxiR+orw5BVU0mUv1sx855uzIikxmklHkqcaSlCUpSSS6gP61PjRqLHq7BK3Ham4x//DWsk0mG2dfkFyxPi1cw2jkQVzCme88wr2GuG3VKSj20e2SOiOoSP/A/WCZ2tLGPjrsCTp9UpevEQbGwiMwVzWVx5S1sR5LbUlTzbiycVIS4auyjUZmozMOHiXjdp/Bc5t9hYrjUmpvbqwk28qAi0sV07dlNSpMqfHp1yVQGJDyVqJTrbKV8KURGXZXIXoAhud4BieyqA8bzGsOyrUS4tjDW0+9ElRJ0F1L8SZElRltPx32XEEpDja0qI/z45AeLBdZYjrtWQycdiSnLfL5qLHK8is5kixsrKS0yiO0qTLluOuqS00hLbaCMkNpLhCUlyAn4AAqzbGmcB3bRw8a2LCs7OihTGZ7VbAubOobXJjutvsOO/bZUY3TadaStvuZ9FF2TwYCx6+C1WQIVcw5IeYgMNx2Xpb7sqQpLaSSSnX31LddWZF9S1qNSj9TMzAewAAVBfaL15kuzcc2/bx7t3PcRbcYxyyYyC4jRorLxNk+yiAxMRENt/wBpHuoNo0ucF3JQC3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF82iT5uJZFHrL6djFgqA8qLfViYqpcZbae/ZopjElnk+vB9mleh+nB8GQUL4VZPkWaeK2ksry27mZHkt9jqJlzeWDyn5Ml9bzvZbjizMzP8v3F6F6ANRAADFt9Lsdq+XGRaktr++qte631hX3q6aht59G5MvMgsZLCZT8msfjPuJjRonDSDX0Stal9exJNISvw3z7KM/wBIQns0tXb/ACnDciyPDbbIZHX3rD9P20mAxKdNJERuOMNtm4rj6l9lfmA1OAAPk7d5pnuRePXk95RQ85yKszzXed5M9rSIxbTWaiBS4dYoiM1r1Q08mDIRKajO/IN5lSlqd57EaG+gfUyhtW76ipbxps2WrmBGnNMq9TQmQ0l0kmf7SJXADrAAAAAAAAAAAAAAAAAAAAAAAAAAAAjmXt3r2MXrGMwIVpfSIbjNbBsZbkCK446XT+LJajy1tkRGZ8kyr8OOPXkgpXxN1tnGndB6+1XsFmlTfYHA+1fNoZ78+JLZQo1of7SYcJbalGsyNHRRFxz3Pngg0aAAMxZVrLO6Dfju+Nb19PkruR4MjCswxG3sXanlyBNcnVlgxKaiTSV1N91l5CkEfQ0rQajSaFBK/HLUcrSWp6TCLW0YvMkcmWd7mFzFQptiTb3c5+xmmylf1e0hx822zURKNCUmoiPkBeQAA+fWQeMezla+3joDG5NC1rHduZ2OQIzd+c+1ZUdTkUtmbdV6axMNxEh1KyeRGX8hKTS4k3Opt8OBvuDDjV0KJXwmiYhwGG48RlP4IaaSSEJL/YREQD1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOHkuQwMUobTIrNmdIr6hg5EpmsgyrKWpBGRfwokNt55w/X1JKD4L1PgiMyCM6o2Zju5NdYps/Em5jWNZlD+fTIsGksyfYNakJNxtC3CSZ9eeOx+n4+voAsIAAVBuXdmHaMx+uyTM4t3JgWtnDqIf2etfmkUmdJZiME++kkx46VOPpIjfdR29SR2UXAC3wAAAVBZbsw6r3FjGjpEW7/WmWVlhb1sk619qr+NWttOPmU98m2nlF7yCMmDc6qPhfQwFvgAAAAAAAAAAAAAAAAAAAAAAAAAAAAOPkX/j95/0+V/ZKAZX8A/8m3j3/KrP9s6A2AAAMT/6gRkXjm/yfH/fWB/3orQG2AAAAYn2eZf/AHT4qlz/AOi7G/oqAG2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAHIvsfospqJ2P5NTQsgorRsmrKmsWG5MWQglEokusukpCy5Ij4MgHJwzAsH1zTnj2v8PpcIoTeVJ+y0MFivie8siJTnsxkNo7KJJEZ8fkAloAAg+cay1zsyJCgbGwPH88g1rinq+HkFbGsmmHFdey20SW3CSo+pepF+QCWV9fAqYEKqq4bFdWVrDcWvr4zaWmWGGkkhttttJElKUpIiIiLgiAewAAV3aai1VeZfB2Dda2xi2zusW05W5nMqoj1rHUxwTSmpi2jeQaOpccK9OAFiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/9k=">

</details>

---

### Q21. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/UM9y_LSXZ1iSJo00z9lHxoDSyH7xZxOHkiyrnNIU3pU.original.fullsize.png">
In the truth table of the above circuit the value of $\mathrm{X}$ and $\mathrm{Y}$ are :

**Options:**

- **(A)** 0,0
- **(B)** 1,1
- **(C)** 1,0
- **(D)** 0,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1,1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_Tym7px3do9kNc_vvaHIlGwbr09dED-rJJL6bEA95oM.original.fullsize.png"/><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/l0PcMgb115Mq73B2owHCtaSOSgZWvgBBRUuHzGCafXs.original.fullsize.png"/>

</details>

---

### Q22. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The output $\mathrm{Y}$ of following circuit for given inputs is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/KHTV-zcI1mTIEc9jyq-I0MjXCooKl0pUP1DS6uEJiT4.original.fullsize.png">

**Options:**

- **(A)** $\Lambda \cdot B(\Lambda+B)$
- **(B)** 0
- **(C)** $\overline{\mathrm{A}} \cdot \mathrm{B}$
- **(D)** $A \cdot B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0**

**Detailed Solution:**

By truth table
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ET6SXCdB2mlRd4f42uFxEHcbm-zPD3sKhPbqXqwQa8g.original.fullsize.png">

</details>

---

### Q23. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The correct truth table for the following logic circuit is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/GmintP7SRaiw9TZmDTiqGS4A2Bb-KWSvlux5j2wANGg.original.fullsize.png">

**Options:**

- **(A)** $\begin{array}{|l|l|l|}
\hline A & B & Y \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}$
- **(B)** $\begin{array}{|l|l|l|}
\hline A & B & Y \\
\hline 0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}$
- **(C)** $\begin{array}{|l|l|l|}
\hline A & B & Y \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 0 \\
1 & 1 & 0 \\
\hline
\end{array}$
- **(D)** $\begin{array}{|l|l|l|}
\hline A & B & Y \\
\hline 0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\begin{array}{|l|l|l|}
\hline A & B & Y \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/keEEPyLglnmD-EVtlTMXV6LEXDMPl8N9Nk5VkMv3OIg.original.fullsize.png">

</details>

---

### Q24. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The output $(Y)$ of logic circuit given below is 0 only when :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7rADKUJt9nEHRXZugOeCeWzhtrbzvZ3IjcykiiuXv2M.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{A}=1, \mathrm{~B}=0$
- **(B)** $\mathrm{A}=0, \mathrm{~B}=1$
- **(C)** $\mathrm{A}=0, \mathrm{~B}=0$
- **(D)** $\mathrm{A}=1, \mathrm{~B}=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A}=0, \mathrm{~B}=0$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/X6rRZHH7RibEeOe4jNKGz2aY_YiLY9TJQ40gP6K7hzw.original.fullsize.png">

</details>

---

### Q25. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Following gates section is connected in a complete suitable circuit.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/uDz_Rk2h8A8DHEvWE2ejmuX7NM9EgDy3_n0kb6m3SLw.original.fullsize.png"/>
$\text { For which of the following combination, bulb will glow (ON) : }$

**Options:**

- **(A)** $\mathrm{A}=0, \mathrm{~B}=0, \mathrm{C}=0, \mathrm{D}=1$
- **(B)** $\mathrm{A}=0, \mathrm{~B}=1, \mathrm{C}=1, \mathrm{D}=1$
- **(C)** $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=0, \mathrm{D}=0$
- **(D)** $\mathrm{A}=1, \mathrm{~B}=1, \mathrm{C}=1, \mathrm{D}=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=0, \mathrm{D}=0$**

**Detailed Solution:**

Bulb will glow if bulb have potential drop on it. One end of bulb must be at high (1) and other must be at low (0).
Option (3) satisfy this condition
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DEpomuw8j6JG8zgonzwiPEQy2DscwpWNNxVe75qAYUU.original.fullsize.png">

</details>

---

### Q26. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Identify the logic gate given in the circuit:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/w_GmbwLno3YChurCxCz-OfHswLWH5tTreshZNq0zD2I.original.fullsize.png">

**Options:**

- **(A)** NAND-gate
- **(B)** AND gate
- **(C)** NOR gate
- **(D)** OR- gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) OR- gate**

**Detailed Solution:**

$\mathrm{Y}=\overline{\overline{\mathrm{A}} \cdot \overline{\mathrm{B}}}$
By De-Morgan Law
$\begin{aligned}
& \mathrm{Y}=\overline{\overline{\mathrm{A}+\mathrm{B}}} \\
& \mathrm{Y}=\mathrm{A}+\mathrm{B}
\end{aligned}$
Hence OR gate

</details>

---

### Q27. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The output of the given circuit diagram is</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f82c6103-ad48-467a-aeab-65c2519e2691.png" style="width: 300px; height: 157px;"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/efa50f0a-54c8-4ccb-b9c9-b7f1f26f0729.png" style="width: 120px; height: 179px;"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/863fecd0-e5a7-4373-96bd-824fca4226d7.png" style="width: 120px; height: 185px;"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b3e1e598-b9e6-4a2b-9e33-694fdb24f0ca.png" style="width: 120px; height: 169px;"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7df38dad-0f02-4bdf-8dab-1df738674fd9.png" style="width: 120px; height: 174px;"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b3e1e598-b9e6-4a2b-9e33-694fdb24f0ca.png" style="width: 120px; height: 169px;"/>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/075453a4-6492-415f-8a60-966a9962fe1e.png" style="width: 350px; height: 181px;"/></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo> </mo><mover><mi>A</mi><mo>¯</mo></mover><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>1</mn><mo>;</mo><mo> </mo><mover><mi>A</mi><mo>¯</mo></mover><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn><mo>;</mo><mo> </mo><mover><mi>B</mi><mo>¯</mo></mover><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>1</mn><mo>;</mo><mover><mrow><mo> </mo><mi>B</mi></mrow><mo>¯</mo></mover><mo>=</mo><mn>0</mn></math></p><p>Using De Morgan's theorem, we can write </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><mfenced><mrow><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>¯</mo></mover></mrow></mfenced><mo>+</mo><mfenced><mrow><mover><mi>A</mi><mo>¯</mo></mover><mo>+</mo><mi>B</mi></mrow></mfenced></mrow><mo>¯</mo></mover><mspace linebreak="newline"></mspace><mo>=</mo><mover><mfenced><mrow><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>¯</mo></mover></mrow></mfenced><mo>¯</mo></mover><mo>·</mo><mover><mfenced><mrow><mover><mi>A</mi><mo>¯</mo></mover><mo>+</mo><mi>B</mi></mrow></mfenced><mo>¯</mo></mover><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mover><mi>A</mi><mo>¯</mo></mover><mo>·</mo><mi>B</mi></mrow></mfenced><mo>·</mo><mfenced><mrow><mi>A</mi><mo>·</mo><mover><mi>B</mi><mo>¯</mo></mover></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q28. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the logic operation performed by the given circuit.</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a17d19de-7fa5-4721-bcfd-1ea7d866daa5.png" style="width: 350px; height: 123px;"/>

**Options:**

- **(A)** NAND
- **(B)** NOR
- **(C)** OR
- **(D)** AND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) OR**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a17d19de-7fa5-4721-bcfd-1ea7d866daa5.png" style="width: 350px; height: 123px;"/></p><p>From De-Morgan's law we can write:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><menclose notation="top"><mi>A</mi></menclose><mo>·</mo><menclose notation="top"><mi>B</mi></menclose></mrow><mo>¯</mo></mover><mo>=</mo><mover><mover><mi>A</mi><mo>¯</mo></mover><mo>¯</mo></mover><mo>+</mo><mover><mover><mi>B</mi><mo>¯</mo></mover><mo>¯</mo></mover><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math></p>

</details>

---

### Q29. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The truth table for this given circuit is:</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e8ff550e-6895-47a7-95c9-2c44ffb04be3.png" style="width: 350px; height: 188px;"/>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/98b31638-fb1e-45c7-b0ec-b6b126f59314.png" style="width: 150px; height: 189px;"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/20f0ff41-f66a-4796-b24d-f749c8284249.png" style="width: 150px; height: 192px;"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fe91c9d1-2495-4d83-b8fc-568bcf5cc602.png" style="width: 150px; height: 191px;"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/42fc576c-85ad-41ff-ab22-22d24f0ee009.png" style="width: 150px; height: 194px;"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/20f0ff41-f66a-4796-b24d-f749c8284249.png" style="width: 150px; height: 192px;"/>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e1234d37-52ba-46ce-9ef5-82ec9e4f0527.png" style="width: 350px; height: 154px;"/></p><p>With respect to the above diagram, the final output can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Y</mi><mo>=</mo><mi mathvariant="normal">A</mi><mo>·</mo><mi mathvariant="normal">B</mi><mo>+</mo><mover><mi mathvariant="normal">A</mi><mo>¯</mo></mover><mo>·</mo><mi mathvariant="normal">B</mi><mspace linebreak="newline"></mspace><mo>=</mo><mo>(</mo><mi mathvariant="normal">A</mi><mo>+</mo><mover><mi mathvariant="normal">A</mi><mo>¯</mo></mover><mo>)</mo><mo>·</mo><mi mathvariant="normal">B</mi><mspace linebreak="newline"></mspace><mo>⇒</mo><mi mathvariant="normal">Y</mi><mo>=</mo><mn>1</mn><mo>.</mo><mi mathvariant="normal">B</mi><mspace linebreak="newline"></mspace><mo>⇒</mo><mi mathvariant="normal">Y</mi><mo>=</mo><mi mathvariant="normal">B</mi></math></p><p>Hence, the required truth table can be written as follows:</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/20f0ff41-f66a-4796-b24d-f749c8284249.png" style="width: 150px; height: 192px;"/>

</details>

---

### Q30. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The truth table of the given circuit diagram is :</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/34642b45-fa74-42cb-bf45-bd4d1ab33ea2.png" style="width: 450px; height: 136px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mtext> A </mtext></mtd><mtd><mtext> B </mtext></mtd><mtd><mtext> Y </mtext></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mtext> A </mtext></mtd><mtd><mtext> B </mtext></mtd><mtd><mtext> Y </mtext></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mtext> A </mtext></mtd><mtd><mtext> B </mtext></mtd><mtd><mtext> Y </mtext></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mtext> A </mtext></mtd><mtd><mtext> B </mtext></mtd><mtd><mtext> Y </mtext></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mtext> A </mtext></mtd><mtd><mtext> B </mtext></mtd><mtd><mtext> Y </mtext></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/84ad5488-a928-4d1f-935c-be710da97fef.png" style="width: 450px; height: 162px;"/></p><p>From the diagram, it is clear that the first set of gates are NOT gates, the second set of gates are AND gates and the third and final gate is an OR gate.</p><p>The final output from all the combination of the gates can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Y</mi><mo>=</mo><mi mathvariant="normal">A</mi><mo>·</mo><mover><mi mathvariant="normal">B</mi><mo>¯</mo></mover><mo>+</mo><mover><mi mathvariant="normal">A</mi><mo>¯</mo></mover><mo>·</mo><mi mathvariant="normal">B</mi></math></p><p>This indicates a XOR GATE. Hence, this option indicates the correct truth table.</p>

</details>

---

### Q31. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The output from a NAND gate having inputs A and B given below will be,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/61e57134-4166-43d4-9e92-f5121d1d1159.png" style="width: 400px; height: 148px;" /></p><p> </p>

**Options:**

- **(A)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ad3a251-e920-41f9-b2b2-2f9e28920cd2.png" style="width: 250px; height: 98px;" /></p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e0a75c50-7301-4e7e-8b27-172e38559596.png" style="width: 250px; height: 98px;" /></p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6b89b585-6a82-41d0-92a3-f7554994405f.png" style="width: 250px; height: 100px;" /></p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9188cf82-9516-451d-a94f-815d8886fb76.png" style="width: 250px; height: 98px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e0a75c50-7301-4e7e-8b27-172e38559596.png" style="width: 250px; height: 98px;" /></p>**

**Detailed Solution:**

<blockquote><p>The output of NAND gate is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mo>(</mo><mi>A</mi><mi>B</mi><msup><mo>)</mo><mo>&#39;</mo></msup></math>.</p><p>The truth table is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> would be zero only when both A and B are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> . Clearly, for all other input conditions the output will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>. Hence, this is the right option.</p></blockquote>

</details>

---

### Q32. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the following circuit and given inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>,</mo></math> choose the correct option for output <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8216;</mo><mi>Y</mi><mo>&#8217;</mo></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5c0792f4-1342-4a09-99da-5f13dd036b9a.png" style="width: 300px; height: 103px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5d69a46a-50e6-413b-8496-1130392a3803.png" style="width: 450px; height: 298px;" /></p>

**Options:**

- **(A)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3f50963c-212d-40e6-94ee-58d683ae1eeb.png" style="width: 300px; height: 152px;" /></p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1b91a6b2-2f48-41b3-ab18-47a3dc79d574.png" style="width: 300px; height: 158px;" /></p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c62d8017-c11b-4318-a918-d997af042452.png" style="width: 300px; height: 145px;" /></p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dfb61e76-fd05-48ae-b8df-b5744c3bf231.png" style="width: 300px; height: 146px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3f50963c-212d-40e6-94ee-58d683ae1eeb.png" style="width: 300px; height: 152px;" /></p>**

**Detailed Solution:**

<blockquote><p>The signal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is given to a NOR gate and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is given to an OR gate. The output of these two signals is given to a NAND gate. Using the laws of Boolean algebra,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><menclose notation="top"><mi>A</mi></menclose><mo>&#160;</mo><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>&#160;</mo><mo>=</mo><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math>.</p><p>Analysing from the input graphs, one can see,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>1</mn></msub><mo>-</mo><msub><mi>t</mi><mn>2</mn></msub><mo>:</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><msub><mi>t</mi><mn>2</mn></msub><mo>-</mo><msub><mi>t</mi><mn>3</mn></msub><mo>:</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><msub><mi>t</mi><mn>3</mn></msub><mo>-</mo><msub><mi>t</mi><mn>4</mn></msub><mo>:</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><msub><mi>t</mi><mn>4</mn></msub><mo>-</mo><msub><mi>t</mi><mn>5</mn></msub><mo>:</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mspace linebreak="newline"></mspace><msub><mi>t</mi><mn>5</mn></msub><mo>-</mo><msub><mi>t</mi><mn>6</mn></msub><mo>:</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn></math></p></blockquote>

</details>

---

### Q33. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The logic operations performed by the given digital circuit is equivalent to:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8007954b-8034-4c8f-95ad-3443bb68d53e.png" style="width: 400px; height: 147px;" />

**Options:**

- **(A)** NOR
- **(B)** AND
- **(C)** OR
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) AND**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8c69b60f-1bd1-4a17-8466-26f811d3d5b8.png" style="width: 400px; height: 198px;" /></p><p>As shown in the figure the various logic gates have been mentioned.</p><p>Let the output before the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mi>O</mi><mi>T</mi></math> gate be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi></math>.</p><p>Using the expression for the logic gates, it can be written</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><menclose notation="top"><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>&#183;</mo><mo>(</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi><mo>)</mo></menclose></math></p><p>Hence, the output <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><menclose notation="top"><mi>Z</mi></menclose><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>&#183;</mo><mo>(</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi><mo>)</mo><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>Y</mi><mo>=</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi></math></p><p>Hence the digital circuit is equivalent to an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>N</mi><mi>D</mi></math> gate.</p></blockquote>

</details>

---

### Q34. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The logic performed by the circuit shown in figure is equivalent to</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/895d8e5b-1950-462b-9fda-00091e45daac-image.png" style="width: 400px; height: 126px;" /></p>

**Options:**

- **(A)** AND
- **(B)** NOR
- **(C)** OR
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) AND**

**Detailed Solution:**

<p>All the gates used in the given configuration are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> gates. Thus, the output can be found as follows-</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>Y</mi></mtd><mtd><mo>=</mo></mtd><mtd><menclose notation="top"><mfenced><mrow><menclose notation="top"><mi>a</mi></menclose><mo>+</mo><menclose notation="top"><mi>b</mi></menclose></mrow></mfenced></menclose></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><menclose notation="top"><mfenced><menclose notation="top"><mi>a</mi><mi>b</mi></menclose></mfenced></menclose></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mi>a</mi><mi>b</mi></mtd></mtr></mtable></math></p><p>The output of the given configuration can also be verified by the following truth table:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Output</mi><mo>&#160;</mo><mi>from</mi><mo>&#160;</mo><mi>first</mi><mo>&#160;</mo><mi>gate</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Output</mi><mo>&#160;</mo><mi>from</mi><mo>&#160;</mo><mi>second</mi><mo>&#160;</mo><mi>gate</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>	</tbody></table><p>The calculation and the truth table clearly shows that the configuration represents <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math> gate.</p>

</details>

---

### Q35. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>For the logic circuit shown, the output waveform at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Y</mi></math> is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ad2e4a01-f430-4319-a082-87a4b40041a8.png" style="width: 314px; height: 217px;" /><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/722734c6-beb0-434d-9d39-6364b0da1b13.png" style="width: 357px; height: 159px;" /></p>

**Options:**

- **(A)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8a71316c-97d8-44b3-a677-9f84acb914ab.png" style="width: 250px; height: 109px;" /></p><p> </p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/63aa432b-9ac6-4075-8821-3966823a9f3c.png" style="width: 200px; height: 108px;" /></p><p> </p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/344e9b0a-b7a3-475d-8b14-264d35a489c1.png" style="width: 200px; height: 94px;" /></p><p> </p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/88f7ba41-9989-4761-bd50-c283cc91e36d.png" style="width: 200px; height: 91px;" /></p><p> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8a71316c-97d8-44b3-a677-9f84acb914ab.png" style="width: 250px; height: 109px;" /></p><p> </p>**

**Detailed Solution:**

<blockquote><p>All the gates used in the diagram represent NAND gates.</p><p>Thus, the output <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> can be calculated as follows</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>Y</mi></mtd><mtd><mo>=</mo></mtd><mtd><menclose notation="top"><menclose notation="top"><mi>A</mi></menclose><mo>&#183;</mo><menclose notation="top"><mi>B</mi></menclose></menclose></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><menclose notation="top"><menclose notation="top"><mi>A</mi></menclose></menclose><mo>+</mo><menclose notation="top"><menclose notation="top"><mi>B</mi></menclose></menclose></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mi>A</mi><mo>+</mo><mi>B</mi></mtd></mtr></mtable></math></p><p>The above equation suggests that the output of the given combination yields the same result as an OR gate.</p><p>The truth table can be written as follows</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>A</mi></menclose></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>B</mi></menclose></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><menclose notation="top"><menclose notation="top"><mi>A</mi></menclose><mo>&#183;</mo><menclose notation="top"><mi>B</mi></menclose></menclose></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>	</tbody></table><p>Hence, this is the correct output.</p></blockquote>

</details>

---

### Q36. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Name the logic gate equivalent to the diagram attached</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/06cb392d-6968-474c-9877-9fbf1ce81c02-image.png" style="width: 300px; height: 249px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NAND</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math>**

**Detailed Solution:**

<blockquote><p>Let&#39;s assume that when the path is short, the state is called state <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and when it is open, the state is called state <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>.</p><p style="text-align: justify;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/af514519-5760-42d8-b239-07f01eb186d0.png" style="width: 300px; height: 251px;" /></p><p>Depending up on whether the path is short or not in the circuit, the following table can be obtained:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Out</mi></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>	</tbody></table><p>The above table is similar to the truth table corresponding to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> gate. Hence, the circuit indicates a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> logic gate.</p></blockquote>

</details>

---

### Q37. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The output <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> for the inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of circuit is given by</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f3439b96-3177-4a22-88c5-7132400cd36e-9895411.PNG" style="width: 400px; height: 134px;" /></p><p>Truth table of the shown circuit is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f3439b96-3177-4a22-88c5-7132400cd36e-9895411.PNG" style="width: 400px; height: 134px;" /></p><p>Output using DeMorgan&#39;s theorem can be written as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><menclose notation="top"><mfenced><mrow><menclose notation="top"><mfenced><mrow><mi>A</mi><mo>&#183;</mo><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose></mrow></mfenced></menclose><mo>&#183;</mo><menclose notation="top"><mfenced><mrow><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose><mo>&#183;</mo><mi>B</mi></mrow></mfenced></menclose></mrow></mfenced></menclose><mspace linebreak="newline"></mspace><mo>=</mo><menclose notation="top"><menclose notation="top"><mfenced><mrow><mi>A</mi><mo>&#183;</mo><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose></mrow></mfenced></menclose></menclose><mo>+</mo><menclose notation="top"><menclose notation="top"><mfenced><mrow><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose><mo>&#183;</mo><mi>B</mi></mrow></mfenced></menclose></menclose><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mi>A</mi><mo>&#183;</mo><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose></mrow></mfenced><mo>+</mo><mfenced><mrow><menclose notation="top"><mi>A</mi><mo>&#183;</mo><mi>B</mi></menclose><mo>&#183;</mo><mi>B</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mi>A</mi><mo>&#183;</mo><mfenced><mrow><menclose notation="top"><mi>A</mi></menclose><mo>+</mo><menclose notation="top"><mi>B</mi></menclose></mrow></mfenced></mrow></mfenced><mo>+</mo><mfenced><mrow><mfenced><mrow><menclose notation="top"><mi>A</mi></menclose><mo>+</mo><menclose notation="top"><mi>B</mi></menclose></mrow></mfenced><mo>&#183;</mo><mi>B</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mi>A</mi><mo>&#183;</mo><menclose notation="top"><mi>A</mi></menclose><mo>+</mo><mi>A</mi><mo>&#183;</mo><menclose notation="top"><mi>B</mi></menclose><mo>+</mo><menclose notation="top"><mi>A</mi></menclose><mo>&#183;</mo><mi>B</mi><mo>+</mo><menclose notation="top"><mi>B</mi></menclose><mo>&#183;</mo><mi>B</mi><mspace linebreak="newline"></mspace><mo>=</mo><mfenced><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><menclose notation="top"><mi>A</mi></menclose><mo>+</mo><menclose notation="top"><mi>B</mi></menclose></mrow></mfenced></math></p><p>Which represents XOR gate.</p><p>Therefore, required truth table will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mfenced></math></p>

</details>

---

### Q38. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The output waveform of the given logical circuit for the following inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> as shown below, is</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1b53ce63-4a17-4b3d-860d-0fcb29b81d89-9895337.PNG" style="width: 257px; height: 300px;" /></p>

**Options:**

- **(A)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/66ace8b9-40df-4e1c-9f03-3fc224c3affc-9895337_1.PNG" style="width: 329px; height: 130px;" />
- **(B)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c4cd5f92-274c-4a47-932a-a780c6955a61-9895337_2.PNG" style="width: 320px; height: 110px;" />
- **(C)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d185e4eb-07fe-4574-a70a-fb4cc4367ddf-9895337_3.PNG" style="width: 292px; height: 140px;" />
- **(D)** <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40f85be9-fe91-4c1a-a883-e2962f6829c0-9895337_4.PNG" style="width: 287px; height: 130px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40f85be9-fe91-4c1a-a883-e2962f6829c0-9895337_4.PNG" style="width: 287px; height: 130px;" />**

**Detailed Solution:**

<p>In the given logical circuit, all logic gates are NAND gate.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e6d63d7a-44fc-4bbd-9aaf-ddea76954c38-9895337.PNG" style="width: 369px; height: 125px;" /></p><p>Here, the inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are inverted using NOT gate (made using NAND gate), then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>A</mi><mo>&#175;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#175;</mo></mover></math> are applied as inputs in other NAND gate.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><menclose notation="top"><mi>A</mi><mo>.</mo><mi>A</mi></menclose></mfenced><mo>=</mo><menclose notation="top"><mi>A</mi></menclose></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>B</mi><mo>.</mo><mi>B</mi></menclose><mo>=</mo><menclose notation="top"><mi>B</mi></menclose></math></p><p>Output at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><menclose notation="top"><mi>A</mi></menclose><mo>.</mo><menclose notation="top"><mi>B</mi></menclose></mrow></mfenced><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math>.</p><p>The above boolean expression is for OR gate.</p><p>Truth table of OR gate is </p><table border="1" cellpadding="1" cellspacing="1" style="width: 300px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>	</tbody></table><p>The output waveform is shown below.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/40f85be9-fe91-4c1a-a883-e2962f6829c0-9895337_4.PNG" style="width: 287px; height: 130px;" /></p>

</details>

---

### Q39. JEE Main 2023 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>For the given logic gates combination, the correct truth table will be</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/46b7b809-757f-4fdd-b9d0-468c7d3d554d-9895008.PNG" style="width: 400px; height: 148px;" /></p>

**Options:**

- **(A)** <table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><strong>A</strong></td>			<td><strong>B</strong></td>			<td><strong>X</strong></td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>0</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>0</td>		</tr>	</tbody></table>
- **(B)** <table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><strong>A</strong></td>			<td><strong>B</strong></td>			<td><strong>X</strong></td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>0</td>		</tr>	</tbody></table>
- **(C)** <table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><strong>A</strong></td>			<td><strong>B</strong></td>			<td><strong>X</strong></td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>0</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>0</td>		</tr>	</tbody></table>
- **(D)** <table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><strong>A</strong></td>			<td><strong>B</strong></td>			<td><strong>X</strong></td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>1</td>		</tr>	</tbody></table>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><strong>A</strong></td>			<td><strong>B</strong></td>			<td><strong>X</strong></td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>0</td>		</tr>	</tbody></table>**

**Detailed Solution:**

<p>A HIGH output (1) results only if all the inputs to the AND gate are HIGH (1). If not all inputs to the AND gate are HIGH, LOW output results.</p><p>But in case of OR Gate, for the output to be 1, at least input one OR two must be 1.</p><p>NOR Gate reverses the logic state.</p><p>Therefore, for all possible combination of inputs, outputs at different stages will look like as given below.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/756664fc-32c5-4bba-8efa-0f8cca0ea65d-24694ff9-af60-4c3c-9855-076c0fd5d83e-9895008_1.PNG" style="width: 400px; height: 157px;" /></p>

</details>

---

### Q40. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The logic gate equivalent to the given circuit diagram is :</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2fc50d1d-7921-44bb-b9a1-436b9d03de9c-9893962.PNG" style="width: 283px; height: 330px;" /></p>

**Options:**

- **(A)** OR
- **(B)** NAND
- **(C)** NOR
- **(D)** AND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) NAND**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c5c28c37-8865-4368-aa88-168124184ad5-186b919e-8a5d-473e-a1b2-0983dcf9157f-9885018_2.png" style="width: 500px; height: 641px;" /></p><p>When both switches are open, the current will flow through the bulb and it will glow.</p><p>When switch A is closed and switch B is open, the current will flow through the bulb and it will glow. </p><p>When switch A is open and switch B is closed, the current will flow through bulb and it will glow.</p><p>When both the switches are closed, since the resistance of left arm of circuit is negligible, the current will flow through the left arm and hence the bulb will not glow. </p><p>The truth table is given as:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><strong>A</strong></td>			<td style="text-align: center;"><strong>B</strong></td>			<td style="text-align: center;"><strong>Bulb</strong></td>		</tr>		<tr>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>		</tr>		<tr>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>		</tr>		<tr>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>		</tr>		<tr>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>		</tr>	</tbody></table><p>Which shows that the given circuit is a NAND gate.</p>

</details>

---

### Q41. JEE Main 2022 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A logic gate circuit has two inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and output <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math>. The voltage waveforms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> are shown below</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e9c504d7-1da4-4703-aa00-baf2dbe5341b-image.png" style="width: 250px; height: 150px;" /></p><p>The logic gate circuit is</p>

**Options:**

- **(A)** AND gate
- **(B)** OR gate
- **(C)** NOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) AND gate**

**Detailed Solution:**

<blockquote><p>Making Truth table of the given wave from,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d15ca6c-4cb6-4dc0-a021-62ea4bb90dc2-image.png" style="width: 160px; height: 183px;" /></p><p>It is clear from the above table that the output is present when both the inputs are high. Even when any of the input is not present, the output is low. This is the function of the AND gate. Hence, the logic gate present is AND gate.</p></blockquote>

</details>

---

### Q42. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the circuit, the logical value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>1</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>1</mn></math> when potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo> </mo><mi mathvariant="normal">V</mi></math> and the logical value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mn>0</mn></math> when potential at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mi mathvariant="normal">V</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4f4d7f8f-4d4b-42d5-aa24-a033363b22c1-image.png" style="width: 221px; height: 170px;" /></p><p>The truth table of the given circuit will be :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>**

**Detailed Solution:**

<blockquote><p>When both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> have logical value &lsquo;<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>&rsquo; both diode are reverse bias and current will flow in resistor hence output will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> volt i.e. logical value &lsquo;<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>&rsquo;.</p><p>In all other case conduction will take place, hence output will be zero volt i.e. logical value &lsquo;<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>&rsquo;. So truth table is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math></p><p>Thus, given circuit is equivalent to an AND gate.</p></blockquote>

</details>

---

### Q43. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the correct Logic Gate for the following output <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>Y</mi></mfenced></math> of two inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6f5c1a41-12be-426e-b121-1ca32370e457-image.png" style="width: 300px; height: 179px;" /></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1470c692-4572-4422-beea-198d2695cb05-image.png" style="width: 200px; height: 62px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3493c58c-e381-4240-8784-d24dcc0cc22f-image.png" style="width: 210px; height: 62px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5e7c6e9a-2c66-4397-aa04-76e0ecfa5dd4-image.png" style="width: 200px; height: 57px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/24b9b7c0-1778-4465-a776-5f3b673932e8-image.png" style="width: 190px; height: 63px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3493c58c-e381-4240-8784-d24dcc0cc22f-image.png" style="width: 210px; height: 62px;" />**

**Detailed Solution:**

<p>For the given input and output, truth table is given below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6f5c1a41-12be-426e-b121-1ca32370e457-image.png" style="width: 300px; height: 179px;" /></p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>Input A</td>			<td>Input B</td>			<td>Output</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>1</td>		</tr>	</tbody></table><p>Clearly, it is a NAND gate. Therefore, the answer is B.</p>

</details>

---

### Q44. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the logic operation performed by the given circuit </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/01be7a3e-ad14-4ccb-936b-063bd980a113-image.png" style="width: 450px; height: 151px;" /></p>

**Options:**

- **(A)** AND gate
- **(B)** OR gate
- **(C)** NOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) AND gate**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b7dc9b21-f736-4ac1-8595-5558b1416717-image.png" style="width: 550px; height: 223px;" /></p><p>According to the circuit,</p><p>Output<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mover><mrow><mover><mi mathvariant="normal">A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">B</mi><mo>&#175;</mo></mover></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right left right left right left right left right left right left" columnspacing="0em 2em 0em 2em 0em 2em 0em 2em 0em 2em 0em" rowspacing="3pt"><mtr><mtd></mtd><mtd><mo>=</mo><mover><mi mathvariant="normal">A</mi><mo accent="false">&#175;</mo></mover><mo>&#8901;</mo><mover><mi mathvariant="normal">B</mi><mo accent="false">&#175;</mo></mover></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo><mi mathvariant="normal">A</mi><mo>&#8901;</mo><mi mathvariant="normal">B</mi></mtd></mtr></mtable></math></p><p>Thus, the given circuit is a AND gate.</p>

</details>

---

### Q45. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the following logic circuit the sequence of the inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>.</mo></math> The output <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> for this sequence will be :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1c2281f9-234b-4c86-a7fb-40d7cfd07ae8-image.png" style="width: 400px; height: 195px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn></math>**

**Detailed Solution:**

<p>Look at the above circuit, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> can be found by the idea of AND gate, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi></math> and the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>, can be calculated by the idea of OR gate, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math>. Then expression for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> can be taken by the idea of NAND gate, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Y</mi><mo>=</mo><mover><mrow><mi>P</mi><mo>&#183;</mo><mi>Q</mi></mrow><mo>&#175;</mo></mover></math> by the idea of Demorgan&#39;s theorem, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mi>P</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>Q</mi><mo>&#175;</mo></mover><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/68f6302a-4f57-4e0f-b3aa-7cf866d613c0-image.png" style="width: 325px; height: 141px;" />
 </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="none solid" rowlines="solid none none none"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi><mo>=</mo><mover><mi mathvariant="normal">A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">B</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mi mathvariant="normal">B</mi><mo>&#175;</mo></mover></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p>

</details>

---

### Q46. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Four NOR gates are connected as shown in figure. The truth table for the given figure is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ddef7d0e-f5f3-4309-8889-7ca247df802c-image.png" style="width: 401px; height: 136px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="none solid"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="none solid"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="none solid"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="none solid"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="none solid"><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eaeea166-ac58-4c74-b031-ab19a48cc249-image.png" style="width: 440px; height: 178px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mover><mrow><mover><mrow><mo>(</mo><mi mathvariant="normal">A</mi><mo>+</mo><mover><mrow><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi></mrow><mo>&#175;</mo></mover><mo>)</mo></mrow><mo>&#175;</mo></mover><mo>+</mo><mover><mrow><mo>(</mo><mi mathvariant="normal">B</mi><mo>+</mo><mover><mrow><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi></mrow><mo>&#175;</mo></mover><mo>)</mo></mrow><mo>&#175;</mo></mover></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mo>(</mo><mi mathvariant="normal">A</mi><mo>+</mo><mover><mrow><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi></mrow><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mo>(</mo><mi mathvariant="normal">B</mi><mo>+</mo><mover><mrow><mi mathvariant="normal">A</mi><mo>+</mo><mi mathvariant="normal">B</mi></mrow><mo>&#175;</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid" frame="solid" rowlines="solid"><mtr><mtd><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mi mathvariant="normal">B</mi><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mi mathvariant="normal">Y</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p>

</details>

---

### Q47. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the logic operation carried out by the given circuit:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b0b3d1dc-1e5e-4261-9cf0-f8020034fd65-image.png" style="width: 366px; height: 129px;" /></p>

**Options:**

- **(A)** OR
- **(B)** AND
- **(C)** NAND
- **(D)** NOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NOR**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/849e2649-f0c0-4254-abfa-f62d6699403f-image.png" style="width: 325px; height: 148px;" /></p><p>In the above circuit diagram of the gate, the result of the above combination is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math>, using Demorgan&#39;s theorem, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Z</mi><mo>=</mo><mover><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></math>, so this circuit is equivalent to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> gate.</p>

</details>

---

### Q48. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Find the truth table for the function <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> represented in the following figure.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/190e084c-51f1-4d30-868d-df24684b9f27-image.png" style="width: 359px; height: 130px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="solid" frame="solid"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="solid" frame="solid"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="solid" frame="solid"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="solid" frame="solid"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable rowlines="solid none none none" columnlines="solid" frame="solid"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2c3674b7-ca05-4aec-8631-7462ebbdce3d-image.png" style="width: 365px; height: 147px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>A</mi><mo mathvariant="italic">&#183;</mo><mi>B</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid" frame="solid" rowlines="solid none none none"><mtr><mtd><mo mathvariant="italic">&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mo mathvariant="italic">&#160;</mo><mi>B</mi><mo>&#160;</mo></mtd><mtd><mo>&#160;</mo><mi>Y</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math></p>

</details>

---

### Q49. JEE Main 2021 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Identify the logic operation carried out.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e7e7a890-bd6b-4bc1-9b9f-8110dc26c576-image.png" style="width: 256px; height: 133px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NAND</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/130b696d-8a5c-4ce1-90a8-178e7c259c02-image.png" style="width: 335px; height: 145px;" />

</details>

---

### Q50. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Which one of the following will be the output of the given circuit?</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/05cccf33-daf8-43ef-92a0-d76d30223e4f-d43.png" style="width: 507px; height: 100px;" /></p>

**Options:**

- **(A)** NOR Gate
- **(B)** NAND Gate
- **(C)** AND Gate
- **(D)** XOR Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) XOR Gate**

**Detailed Solution:**

<p>Output of the above circuit can be obtained as

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>(</mo><mover><mrow><mi>A</mi><mo>&#8901;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>)</mo><mo>&#8901;</mo><mo>(</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#8901;</mo><mo>(</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>.</mo><mi>B</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>.</mo><mi>A</mi><mo>+</mo><mi>A</mi><mo>.</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi><mo>.</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>.</mo><mi>B</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>.</mo><mi>A</mi><mo>+</mo><mn>0</mn><mo>+</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>.</mo><mi>B</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>.</mo><mi>A</mi></math>, which is XOR gate</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e96252bc-0437-4416-bfb8-7d16bc09bc2c-d44.png" style="width: 496px; height: 180px;" /></p>

</details>

---

### Q51. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The output of the given combination gates represents:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0e55aed4-1c50-437e-8d31-5e886b3e7669-image.png" style="width: 450px; height: 121px;" /></p>

**Options:**

- **(A)** XOR Gate
- **(B)** NAND Gate
- **(C)** AND Gate
- **(D)** NOR Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) NAND Gate**

**Detailed Solution:**

<p>By De Morgan&#39;s theorem, we have</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/44f234dd-ae1c-4509-a128-71c22405ecd0-image.png" style="width: 500px; height: 126px;" /></p><p>Here the output of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> gives <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>A</mi><mo>&#175;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>B</mi><mo>&#175;</mo></mover></math>. This output is fed as inputs to NAND gate and the output is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#183;</mo><mi>B</mi></math>, when when again fed as input to NAND gate to get output as <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></math>.</p>

</details>

---

### Q52. JEE Main 2021 (16 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The following logic gate is equivalent to : </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b3d8dc36-bf75-4544-b442-df31101405a6-image.png" style="width: 402px; height: 108px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> Gate
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math> Gate
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math> Gate
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NAND</mi></math> Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> Gate**

**Detailed Solution:**

<p>Truth table for the given logic gate : </p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>	</tbody></table><p>The truth table is similar to that of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOR</mi></math> gate.</p>

</details>

---

### Q53. JEE Main 2021 (16 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>In the logic circuit shown in the figure, if input <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> respectively, the output at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> would be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _________.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/46e9c281-3b90-4d58-8f65-38a9f4e7304c-image.png" style="width: 369px; height: 116px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d3e1f06e-0012-4a05-aa16-90ab28de3bc1-image.png" style="width: 369px; height: 142px;" />

</details>

---

### Q54. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Draw the output signal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> in the given combination of gates.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/42f52421-0824-4b81-ad89-1902dcce0b82-image.png" style="width: 550px; height: 164px;" /></p>

**Options:**

- **(A)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41af3bc3-8e86-4b31-a2f7-5050a745eaf3-image.png" style="width: 200px; height: 85px;" /></p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/843e6bd8-0106-465c-9e26-5a3f21578616-image.png" style="width: 200px; height: 82px;" /></p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a278244b-d4b2-4acd-87b0-87fe26f55e21-image.png" style="width: 200px; height: 84px;" /></p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f65f0750-f00a-4c3c-8aa1-a428ae0390e0-image.png" style="width: 200px; height: 85px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41af3bc3-8e86-4b31-a2f7-5050a745eaf3-image.png" style="width: 200px; height: 85px;" /></p>**

**Detailed Solution:**

According to gates by Demorgan&#39;s law <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>=</mo><mi>A</mi><mo>&#183;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math> By observation.

</details>

---

### Q55. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The truth table for the following logic circuit is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8afcc53f-8e54-4fcc-85aa-8e31f32bdf48-image.png" style="width: 331px; height: 95px;" /></p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73647d00-0ccb-4d97-ba1a-f8521026d2b3-image.png" style="width: 192px; height: 193px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3d6e61a1-4a40-46a1-b6f4-33cc81f1e30b-image.png" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7db9770e-0bc1-4de1-b511-fbea07f6c9a1-image.png" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6658c8f4-140e-4e30-a3b0-56bf3a1e1ce6-image.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/73647d00-0ccb-4d97-ba1a-f8521026d2b3-image.png" style="width: 192px; height: 193px;" />**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mrow><mo>(</mo><mi>A</mi><mover><mi>B</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mi>B</mi><mo>)</mo></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mrow><mi>A</mi><menclose notation="top"><mi>B</mi></menclose></mrow><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mi>B</mi></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi><mo>)</mo><mo>&#183;</mo><mo>(</mo><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mi>A</mi><mo>+</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mover><mi>B</mi><mo>&#175;</mo></mover><mo>+</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi><mo>+</mo><mi>B</mi><mover><mi>B</mi><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mi>A</mi><mi>B</mi><mo>+</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mover><mi>B</mi><mo>&#175;</mo></mover></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6edc295f-583f-4cc2-96e5-3c1d04f06d7e-image.png" style="width: 364px; height: 223px;" /></p>

</details>

---

### Q56. JEE Main 2021 (24 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6648ae79-4bfb-4c7d-b8f5-04ba1daed0fa-image.png" style="width: 330px; height: 87px;" /></p><p>The logic circuit shown above is equivalent to :</p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c888919b-92d7-471e-ad77-a89abd7cc876-image.png" style="width: 330px; height: 106px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/799a532e-0dc8-4dce-b9f0-5d3a6793292a-image.png" style="width: 330px; height: 87px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1807da73-446c-481d-acab-e0a03826c37f-image.png" style="width: 330px; height: 108px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b9ea4d43-6382-4663-bd77-9f1fa3719495-image.png" style="width: 330px; height: 108px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1807da73-446c-481d-acab-e0a03826c37f-image.png" style="width: 330px; height: 108px;" />**

**Detailed Solution:**

<p>Truth table of the given gate:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left left left"><mtr><mtd><mo>&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mi>B</mi><mo>&#160;</mo></mtd><mtd><mi>C</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p><p>Truth table of option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left left left"><mtr><mtd><mo>&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mi>B</mi><mo>&#160;</mo></mtd><mtd><mi>C</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math></p><p>Truth table of option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left left left"><mtr><mtd><mo>&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mi>B</mi><mo>&#160;</mo></mtd><mtd><mi>C</mi><mo>&#160;</mo></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></math></p><p>Truth table of option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left left left"><mtr><mtd><mo>&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mi>B</mi><mo>&#160;</mo></mtd><mtd><mi>C</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p><p>Truth table of option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left left left"><mtr><mtd><mo>&#160;</mo><mi>A</mi><mo>&#160;</mo></mtd><mtd><mi>B</mi><mo>&#160;</mo></mtd><mtd><mi>C</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p><p>Since option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> has same truth table, hence answer is option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math> is correct.</p><p>Given Boolean expression can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover></mrow><mo>&#175;</mo></mover><mo>=</mo><mi>C</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mi>B</mi></math></p>

</details>

---

### Q57. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Identify the correct output signal <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> in the given combination of gates (as shown <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>) for the given inputs <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mi>B</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aaee9960-9cf1-42b6-bb11-7b2c5744663c-image.png" style="width: 320px; height: 86px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a4f4a12e-0db2-40ba-af42-bad65431f635-image.png" style="width: 270px; height: 183px;" />   </p>

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cffc4e4f-1811-4c7d-b3de-9b43a8e71b8a-image.png" style="width: 250px; height: 83px;" />
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/45924226-2de9-4f9e-86aa-f450cfd9342f-image.png" style="width: 250px; height: 79px;" />
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e68c0123-922d-4b9a-a9bc-3578d144e8dd-image.png" style="width: 250px; height: 85px;" />
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/67f726e3-f664-4e4b-828e-9028bf886eeb-image.png" style="width: 250px; height: 81px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/67f726e3-f664-4e4b-828e-9028bf886eeb-image.png" style="width: 250px; height: 81px;" />**

**Detailed Solution:**

<p>Truth table</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fd81abcb-2d8b-44fc-9f26-f71f545fdf21-image.png" style="width: 250px; height: 214px;" />  </p><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#183;</mo><mover><mi>B</mi><mo>&#175;</mo></mover></mrow><mo>&#175;</mo></mover><mo>=</mo><mover><mover><mi>A</mi><mo>&#175;</mo></mover><mo>&#175;</mo></mover><mo>+</mo><mover><mover><mi>B</mi><mo>&#175;</mo></mover><mo>&#175;</mo></mover><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math></p><p><img height="161" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9bf02c37-6433-4e66-a225-996f78dff4d6-image.png" width="691" /></p>

</details>

---

### Q58. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Identify the operation performed by the circuit given below :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/030373f2-f6f8-49bb-97df-d543a587270c-image.png" style="width: 377px; height: 198px;" />  </p>

**Options:**

- **(A)** NAND
- **(B)** OR
- **(C)** AND
- **(D)** NOT

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) AND**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b00c56c3-ee37-4e75-9811-5bfef4f1db9f-image.png" style="width: 167px; height: 80px;" /></p><p>Behaves like a NOT gate so boolean equation will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mover><mrow><mover><mi mathvariant="normal">A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">B</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">C</mi><mo>&#175;</mo></mover></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mi mathvariant="normal">A</mi><mo>&#183;</mo><mi mathvariant="normal">B</mi><mo>&#183;</mo><mi mathvariant="normal">C</mi></math></p><p>Whole arrangement behaves like an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AND</mi></math> gate </p>

</details>

---

### Q59. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>In the following, digital circuit, what will be the output a &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Z</mi></math>&#39;, when the input <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">A</mi><mo>,</mo><mi mathvariant="normal">B</mi></mrow></mfenced></math> are  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/99fad8c5-56a2-4e54-8257-2f9f4498f895-image.png" style="width: 465px; height: 150px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>0</mn></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d794763f-3cac-4c85-b54f-27c6f6267792-image.png" style="width: 385px; height: 135px;" /></p><table border="1" cellpadding="1" cellspacing="1" style="width: 300px;">	<tbody>		<tr>			<td style="text-align: center;">A</td>			<td style="text-align: center;">B</td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>A</mi><mi>B</mi></menclose></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>A</mi><mo>+</mo><mi>B</mi></menclose></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfenced><menclose notation="top"><mi>A</mi><mi>B</mi></menclose></mfenced><mo>.</mo><mfenced><menclose notation="top"><mi>A</mi><mo>+</mo><mi>B</mi></menclose></mfenced></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>=</mo><mi>P</mi><mo>+</mo><mfenced><menclose notation="top"><mi>A</mi><mi>B</mi></menclose></mfenced></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>Q</mi></menclose><mo>=</mo><menclose notation="top"><mi>z</mi></menclose></math></td>		</tr>		<tr>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>		</tr>		<tr>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>		</tr>		<tr>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>		</tr>		<tr>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">1</td>			<td style="text-align: center;">0</td>			<td style="text-align: center;">0</td>		</tr>	</tbody></table>

</details>

---

### Q60. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit, value of <math><mi>Y</mi></math> is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b90efe06-fb36-4e1e-8e7b-38884296b5c6-image.png" style="width: 250px; height: 204px;" />

**Options:**

- **(A)** <math><mn>0</mn></math>
- **(B)** toggles between <math><mn>0</mn></math> and <math><mn>1</mn></math>
- **(C)** will not execute
- **(D)** <math><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>0</mn></math>**

**Detailed Solution:**

<math><mi>Y</mi><mo>=</mo><mover accent="false"><mrow><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>-</mo></mover><mo>∙</mo><mi>A</mi></mrow><mo>¯</mo></mover></math>  
<math><mi></mi><mo>=</mo><mover accent="true"><mrow><mi>A</mi><mi>B</mi></mrow><mo>̿</mo></mover><mo>+</mo><mover accent="false"><mrow><mi>A</mi></mrow><mo>¯</mo></mover></math>  
<math><mi></mi><mo>=</mo><mi>A</mi><mi>B</mi><mo>+</mo><mover accent="false"><mrow><mi>A</mi></mrow><mo>¯</mo></mover></math>  
<math><mo>=</mo><mn>0</mn><mo>+</mo><mn>0</mn></math>  
<math><mi></mi><mo>=</mo><mn>0</mn><mi mathvariant="normal"></mi></math>

</details>

---

### Q61. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Boolean relation at the output stage- <math><mi>Y</mi></math> for the following circuit is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41c8f060-4da1-4123-8afe-e20c1382b9ef.jpeg" />

**Options:**

- **(A)** <math><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>
- **(B)** <math><mi>A</mi><mo>+</mo><mi>B</mi></math>
- **(C)** <math><mi>A</mi><mo>∙</mo><mi>B</mi></math>
- **(D)** <math><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mo>∙</mo><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mo>∙</mo><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>**

**Detailed Solution:**

First part of figure shown is OR gate and
Second part of figure shown is NOT gate
So <math><msub><mrow><mi>Y</mi></mrow><mrow><mi>P</mi></mrow></msub><mo>=</mo><mi>O</mi><mi>R</mi><mo>+</mo><mi>N</mi><mi>O</mi><mi>T</mi><mo>=</mo><mi>N</mi><mi>O</mi><mi>R</mi><mo> </mo><mi>g</mi><mi>a</mi><mi>t</mi><mi>e</mi></math>
<math> <mrow> <mi>Y</mi><mo>=</mo><mover accent="true"> <mrow> <mi>A</mi><mo>+</mo><mi>B</mi></mrow> <mo stretchy="true">¯</mo> </mover> <mo>=</mo><mover accent="true"> <mi>A</mi> <mo stretchy="true">¯</mo> </mover> <mo>.</mo><mover accent="true"> <mi>B</mi> <mo stretchy="true">¯</mo> </mover> </mrow> </math>

</details>

---

### Q62. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following gives a reversible operation?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f6427356-2c90-424a-831b-671586c0f22a.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1481c81f-b663-42ef-8aea-36ee6141755e.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7cafe35b-1e84-4ab6-92b6-f9d18fe89204.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5b46cc1a-13a1-4715-9d18-76f703f65002.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5b46cc1a-13a1-4715-9d18-76f703f65002.png">**

**Detailed Solution:**

<p>A logic gate gives the reversible operation if we can recover input data from the output.</p><p>For example, a NOT gate gives the reversible operation because we always know that the input is the reverse of the output.</p><p>For the given logic gate, let the input is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>.</p><p>So, the output, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><mi>X</mi><mo>+</mo><mi>X</mi></mrow><mo>&#175;</mo></mover><mo>=</mo><mover><mi>X</mi><mo>&#175;</mo></mover></math> (NOT gate)</p>

</details>

---

### Q63. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The truth table for the circuit given in the figure is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c6f3ddfe-5883-44b4-90d3-63f106ade095-image.png" style="width: 344px; height: 94px;" />

**Options:**

- **(A)** <math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mtd></mtr></mtable></mrow></mfenced></math>
- **(B)** <math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mtd></mtr></mtable></mrow></mfenced></math>
- **(C)** <math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced></math>
- **(D)** <math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced open="|" close="|" separators="|"><mrow><mtable><mtr><mtd><mi mathvariant="normal">A</mi></mtd><mtd><mi mathvariant="normal">B</mi></mtd><mtd><mi mathvariant="normal">Y</mi></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2425df6f-bc3e-4241-90f8-c3e789f97476-image.png" style="width: 350px; height: 99px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math>
and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mover><mrow><mi>A</mi><mo>.</mo><mi>C</mi></mrow><mo>&#175;</mo></mover></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid" rowlines="solid none none none"><mtr><mtd><mi>A</mi></mtd><mtd><mi>B</mi></mtd><mtd><mi>C</mi><mo>=</mo><mo>(</mo><mi>A</mi><mo>+</mo><mi>B</mi><mo>)</mo></mtd><mtd><mi>A</mi><mi>C</mi></mtd><mtd><mi>y</mi><mo>=</mo><mover><mrow><mi>A</mi><mo>.</mo><mi>C</mi></mrow><mo>&#175;</mo></mover></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable></math></p>

</details>

---

### Q64. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The logic gate equivalent to the given logic circuit is: 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/abee80f2-6e26-4f09-a8ca-e699385a16f7-image10.png">

**Options:**

- **(A)** NAND
- **(B)** AND
- **(C)** NOR
- **(D)** OR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) OR**

**Detailed Solution:**

From the diagram,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><mover accent="true"><mrow><mover accent="true"><mi mathvariant="normal">A</mi><mo>-</mo></mover><mo>.</mo><mover accent="true"><mi mathvariant="normal">B</mi><mo>-</mo></mover></mrow><mrow><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></mrow></mover></math>
From De Morgan&rsquo;s law,
<math><mi mathvariant="normal">y</mi><mo>=</mo><mover accent="true"><mrow><mover accent="true"><mrow><mi mathvariant="normal">A</mi></mrow><mo>-</mo></mover></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mover accent="true"><mrow><mi mathvariant="normal">B</mi></mrow><mo>-</mo></mover></mrow><mo>-</mo></mover></math>
<math><mo>=</mo><mi mathvariant="normal">A</mi><mo>+</mo><mtext>&#8201;</mtext><mi mathvariant="normal">B</mi></math>
<math><mo>&#8756;</mo></math> Given circuit represents &lsquo;OR&rsquo; gate

</details>

---

### Q65. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The output of the given logic circuit is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d42452d4-965e-442b-8511-c5294bd1339d-image.png" style="width: 346px; height: 153px;" />

**Options:**

- **(A)** <math><mi>A</mi><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>
- **(B)** <math><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mi>B</mi></math>
- **(C)** <math><mi>A</mi><mi>B</mi><mo>+</mo><mover accent="false"><mrow><mi>A</mi><mi>B</mi></mrow><mo>¯</mo></mover></math>
- **(D)** <math><mi>A</mi><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mi>B</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>A</mi><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>**

**Detailed Solution:**

<math> <mrow>  <mi>y</mi><mo>=</mo><mover accent='true'>   <mrow>    <mrow><mo>(</mo>     <mrow>      <mover accent='true'>       <mrow>        <mi>A</mi><mo>.</mo><mover accent='true'>         <mrow>          <mi>A</mi><mo>.</mo><mi>B</mi></mrow>         <mo stretchy='true'>&#x00AF;</mo>        </mover>        </mrow>       <mo stretchy='true'>&#x00AF;</mo>      </mover>      </mrow>    <mo>)</mo></mrow><mo>.</mo><mrow><mo>(</mo>     <mrow>      <mover accent='true'>       <mrow>        <mi>A</mi><mo>.</mo><mi>B</mi></mrow>       <mo stretchy='true'>&#x00AF;</mo>      </mover>      <mo>+</mo><mi>B</mi></mrow>    <mo>)</mo></mrow></mrow>   <mo stretchy='true'>&#x00AF;</mo>  </mover>  </mrow></math>
</br><math><mi>A</mi><mo>.</mo><mover accent="false"><mrow><mi>A</mi><mo>.</mo><mi>B</mi></mrow><mo>¯</mo></mover><mo>+</mo><mo>(</mo><mi>A</mi><mo>.</mo><mi>B</mi><mo>)</mo><mo>.</mo><mover accent="true"><mrow><mi>B</mi></mrow><mo>̄</mo></mover></math>
</br><math><mo>=</mo><mi>A</mi><mo>⋅</mo><mfenced separators="|"><mrow><mover accent="true"><mrow><mi>A</mi></mrow><mo>-</mo></mover><mo>+</mo><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></mrow></mfenced></math>

<math><mo>=</mo><mi>A</mi><mover accent="true"><mrow><mi>B</mi></mrow><mo>-</mo></mover></math>

</details>

---

### Q66. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

To get output <mi mathvariant="normal">&#39;1&#39;</mi><mi mathvariant="normal"> at <math><mi>R</mi><mo>,</mo></math> for the given logic gate circuit the input values must be:</mi>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/659934b7-0a09-4733-bb37-7ead5cd383bb-image.png" style="width: 366px; height: 160px;" />

**Options:**

- **(A)** <math><mi>X</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>Y</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi>X</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>Y</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi>X</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>Y</mi><mo>=</mo><mn>1</mn></math>
- **(D)** <math><mi>X</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>Y</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>X</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>Y</mi><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ab66530b-9b7a-4910-bb5a-c6364d60630a-image.png" style="width: 370px; height: 184px;" />


<math> <mrow> <mi>R</mi><mo>=</mo><mover accent="true"> <mrow> <mrow><mo>(</mo> <mrow> <mover accent="true"> <mi>X</mi> <mo stretchy="true">&#175;</mo> </mover> <mo>+</mo><mi>Y</mi></mrow> <mo>)</mo></mrow><mo>+</mo><mrow><mo>(</mo> <mrow> <mover accent="true"> <mrow> <mi>X</mi><mo>&#8901;</mo><mover accent="true"> <mi>Y</mi> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow></mrow> <mo stretchy="true">&#175;</mo> </mover> <mo>=</mo><mrow><mo>(</mo> <mrow> <mover accent="true"> <mrow> <mover accent="true"> <mi>X</mi> <mo stretchy="true">&#175;</mo> </mover> <mo>+</mo><mi>Y</mi></mrow> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow><mo>&#8901;</mo><mrow><mo>(</mo> <mrow> <mover accent="true"> <mrow> <mover accent="true"> <mrow> <mi>X</mi><mo>.</mo><mover accent="true"> <mi>Y</mi> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow><mo>=</mo><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>.</mo><mover accent="true"> <mi>Y</mi> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow><mo>&#8901;</mo><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>.</mo><mover accent="true"> <mi>Y</mi> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow><mo>=</mo><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>.</mo><mover accent="true"> <mi>Y</mi> <mo stretchy="true">&#175;</mo> </mover> </mrow> <mo>)</mo></mrow></mrow> </math></p></blockquote>

</details>

---

### Q67. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

Truth table for the given circuit will be
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Hgc-kn9IXwqHTgTGCm3CHBKKm5gI0rwh7uHzxT7gM68.original.fullsize.png">

**Options:**

- **(A)** $$
\begin{array}{cc|c}
\mathrm{x} & \mathrm{y} & \mathrm{z} \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 0
\end{array}
$$
- **(B)** $$
\begin{array}{cc|c}
\mathrm{x} & \mathrm{y} & \mathrm{z} \\
\hline 0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1
\end{array}
$$
- **(C)** $$
\begin{array}{cc|c}
x & y & z \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1
\end{array}
$$
- **(D)** $$
\begin{array}{cc|c}
\mathrm{x} & \mathrm{y} & \mathrm{z} \\
\hline 0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1
\end{array}
$$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $$
\begin{array}{cc|c}
x & y & z \\
\hline 0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1
\end{array}
$$**

**Detailed Solution:**

Truth table of the circuit is as follows
$$
\begin{array}{|c|c|c|c|c|c|}
\hline x & y & \bar{x} & a=x \cdot y & b=\bar{x} \cdot y & z=\overline{a \cdot b} \\
\hline 0 & 0 & 1 & 0 & 0 & 1 \\
\hline 0 & 1 & 1 & 0 & 1 & 1 \\
\hline 1 & 0 & 0 & 0 & 0 & 1 \\
\hline 1 & 1 & 0 & 1 & 0 & 1 \\
\hline
\end{array}
$$

</details>

---

### Q68. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

To get an output of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> from the circuit shown in the figure the input must be:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/28a0c112-007a-4e2e-a45d-f73281d3a7e2-image.png" style="width: 350px; height: 112px;" />

**Options:**

- **(A)** <math><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></math>
- **(C)** <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>1</mn></math>
- **(D)** <math><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi> </mi><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi> </mi><mi>c</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

Output of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math> gate must be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math> <mrow> <mi>c</mi><mo>=</mo><mn>1</mn></mrow> </math>

So, <math><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>=</mo><mn>0</mn></math>

or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q69. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The truth table given in fig. represents:<table border="1" style="width: 100px; height: 150px;">	<tbody>		<tr>			<td>A</td>			<td>B</td>			<td>Y</td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>0</td>			<td>1</td>		</tr>		<tr>			<td>1</td>			<td>1</td>			<td>1</td>		</tr>	</tbody></table>

**Options:**

- **(A)** OR-Gate
- **(B)** NAND-Gate
- **(C)** AND-Gate
- **(D)** NOR-Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR-Gate**

**Detailed Solution:**

<p>The given truth table represents OR gate.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/26b8b872-4687-4cdf-8409-0b4fa4a202ab-image.png" style="width: 160px; height: 84px;" /></p><p>Its boolean algebra is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>A</mi><mo>+</mo><mi>B</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are input and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> is output.</p><p>OR gate gives output <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> if any one of its input is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></p>

</details>

---

### Q70. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If a, b, c, d are inputs to a gate and <math><mi mathvariant="normal">x</mi></math> is its output, then, as per the following time graph, the gate is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/33452c88-c2d0-43e7-bab7-ab17d20e85ec-image.png" style="width: 330px; height: 208px;" />

**Options:**

- **(A)** OR
- **(B)** NAND
- **(C)** NOT
- **(D)** AND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR**

**Detailed Solution:**

<table border="1">	<tbody>		<tr>			<td>a</td>			<td>b</td>			<td>c</td>			<td>d</td>			<td>X</td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>0</td>			<td>0</td>			<td>0</td>			<td>1</td>			<td>1</td>		</tr>	</tbody></table>

When any input is one, output is one, hence the gate is &#39;OR&#39; gate.

</details>

---

### Q71. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8ad979f8-1236-408a-b134-941deeb37b04-image.png" style="width: 300px; height: 164px;" />

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are input terminals</p><p>Logic <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Logic <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Which logic gate operation, the following circuit does?</p><p>Note: This question was awarded a bonus. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> option changed. </p>

**Options:**

- **(A)** OR gate.
- **(B)** NOR gate.
- **(C)** Output will always be one.
- **(D)** XOR gate.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Output will always be one.**

**Detailed Solution:**

As <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is directly connected to the output, the output will always be one and independent of the input.

</details>

---

### Q72. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

<p>Identify the gate and match <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>Y</mi></math> in the bracket to check.

    <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0b21e6c9-57c5-4213-8b31-9abcb3fa12c9-image.png" style="width: 307px; height: 116px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>O</mi><mi>R</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>0</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mi>O</mi><mi>R</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>0</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mi>O</mi><mi>T</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>N</mi><mi>D</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>N</mi><mi>D</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5b94a801-e668-42b9-bf2b-967ab821296a-image.png" style="width: 336px; height: 79px;" /></p><p>The output of the first NAND gate</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>Y</mi><mo>&#39;</mo></msup><mo>=</mo><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></math></p><p>The output of the second NAND gate</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><mfenced><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></mfenced><mo>&#183;</mo><mfenced><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></mfenced></mrow><mo>&#175;</mo></mover><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mfenced><mover><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>&#175;</mo></mover></mfenced><mo>+</mo><mfenced><mover><mover><mrow><mi>A</mi><mo>&#183;</mo><mi>B</mi></mrow><mo>&#175;</mo></mover><mo>&#175;</mo></mover></mfenced><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mi>A</mi><mo>&#183;</mo><mi>B</mi></math></p><p>So, the equivalent circuit will be an AND gate.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>N</mi><mi>D</mi><mo>&#160;</mo><mo>(</mo><mi>A</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>Y</mi><mo>=</mo><mn>1</mn><mo>)</mo></math></p>

</details>

---

### Q73. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following circuits correctly represents the following truth table ?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4FTP63dh1GWnRox0nx_7EE-5O4lTxMPIPs1lT1NgiCU.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jG0uF8BMja45CDMPjKC7ToBDNeC_YI36X8ZnGZ7SW8A.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5ndQh7EpH7uCdLepiaD3E21NC_hqv1LN0enwBAflwqQ.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cN3ljyquNoUDqOCiRrvzoirqSSqm-fawJz8OjmdXz6s.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xgE2q2ZSyQpIS98wnEx_yyEQiDjvLSBzCGVATEzSMts.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jG0uF8BMja45CDMPjKC7ToBDNeC_YI36X8ZnGZ7SW8A.original.fullsize.png">**

**Detailed Solution:**

For circuit 1
$A \cdot B=\overline{Y+\bar{A}}=C$
A B $\overline{Y+\bar{A}}=C$
$\begin{array}{lllll}0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & 0 & 0\end{array}$

</details>

---

### Q74. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A system of four gates is set up as shown. The 'truth table' corresponding to this system is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/45eDWiZgxut8tK4-clvU40A-XacQyNNwAs_hzOEeh24.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fUOw7ZvvE46indwU_yIlhQ2_a4vbh3iPzKOPo3YE0SY.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LzM4ax4PUrK8zm7hF4Zajtp4_Uheon6t3a46dvGcwDI.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/vBCQdL2sYmhMXRZVZMJH1Z11jB8DLKLJzdWlzFuWRpk.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zHNN1XzYNi5aQeD6vhC6PRbpH4o_F6xTcQqcFMAtYkI.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fUOw7ZvvE46indwU_yIlhQ2_a4vbh3iPzKOPo3YE0SY.original.fullsize.png">**

**Detailed Solution:**

In the given system all four gate is NOR gate
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OCo3EKnHm1lb0nNSYMNx7U7_SD3fJi1QusFj7eYlqUM.original.fullsize.png">

</details>

---

### Q75. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Consider two npn transistors as shown in figure. If 0 Volts corresponds to false and 5 Volts correspond to true then the output at C corresponds to :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TOvKFmxB7C-ONJ4z4ShPAHOPxTWSxtzj2A-_1WpiR-A.original.fullsize.png">

**Options:**

- **(A)** A NAND B
- **(B)** A OR B
- **(C)** AAND B
- **(D)** ANOR B

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) A NAND B**

**Detailed Solution:**

The output at $\mathrm{C}$ corresponds to A NAND
$$
\mathrm{B} \text { or } \overline{\mathrm{A} \cdot \mathrm{B}}=\mathrm{C}
$$

</details>

---

### Q76. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The figure shows a combination of two NOT gates and a NOR gate.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/AzwW-A8OEg4KCWGktKBsFKoVqlnG-7ImiRtFm2u1d28.original.fullsize.png">

The combination is equivalent to $\mathrm{a}$

**Options:**

- **(A)** NAND gate
- **(B)** NOR gate
- **(C)** AND gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) AND gate**

**Detailed Solution:**

Truth table is as shown :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/drdI-lbMa6zltZr5JUeqvm-VLocVVbmTahgRsDyTuzA.original.fullsize.png">

Thus the combination of two NOT gates and one NOR gate is equivalent to a AND gate.

</details>

---

### Q77. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following is the Boolean expression for NOR gate?

**Options:**

- **(A)** $Y=\overline{A+B}$
- **(B)** $Y=\overline{A \cdot B}$
- **(C)** $Y=A \cdot B$
- **(D)** $Y=\bar{A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $Y=\overline{A+B}$**

**Detailed Solution:**

NOR gate is the combination of NOT and OR gate. Boolean expression for NOR gate is $Y=\overline{A+B}$

</details>

---

### Q78. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

Which logic gate with inputs $\mathrm{A}$ and $\mathrm{B}$ performs the same operation as that performed by the following circuit?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pJWt13QxQks7lFUGxJ1Eo8S5awOZA1EyIXgbtzmGUiw.original.fullsize.png">

**Options:**

- **(A)** NAND gate
- **(B)** OR gate
- **(C)** NOR gate
- **(D)** AND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) OR gate**

**Detailed Solution:**

When either of $A$ or $B$ is 1 i.e. closed then lamp will glow.
In this case, Truth table
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qKEYQetW2pzGC-zs5e0RE1894iOsQmrZu22ucdCFlKA.original.fullsize.png">

</details>

---

### Q79. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

Truth table for system of four NAND gates as shown in figure is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2_J3F71mC7sc2ZqIXkW7s8d2R9QWwpbwQatH8vTRFas.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HlLbDm9SQnl3sprT1uRSUTfg9WH9zff3bk3yH1vWiy8.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/StFmd47ThB064hAqvIKW71M_05tT6EdM4vZTZBw6T3Y.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/mFWkaUaKOfCLeHud6nbIpEy7_pm-4131t-rL9OcGqh0.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Qk8PW99xtwCCkn-OtEvsB1WQI803dzbVSqtTD65N1Fc.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HlLbDm9SQnl3sprT1uRSUTfg9WH9zff3bk3yH1vWiy8.original.fullsize.png">**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/334_7YUGJDaNsLGYso97c0D0wzJ5bRTU_VuiLJBPDmY.original.fullsize.png">

</details>

---

### Q80. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

The combination of gates shown below yields 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/wvCKzLX-ENc4IhkjQ_-neCQMownw4P2LC4nXQuQ3Kww.original.fullsize.png">

**Options:**

- **(A)** OR gate
- **(B)** NOT gate
- **(C)** XOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR gate**

**Detailed Solution:**

Truth table for given combination is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/xE3LWrUM6RelXiU8PEuJRu5vd1pNbKCbYnD-7sk9ciM.original.fullsize.png">

This comes out to be truth table of OR gate

</details>

---

### Q81. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

The logic circuit shown below has the input waveforms 'A' and 'B' as shown. Pick out the correct output waveform.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LaJYx_YTn6Ccj4gzb2OSfjrnernWy3bvsVeRKvkFwsQ.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SwJkaXuKttDeJW3Y9AY7nGpw7clOkk7_LjYkR0kir_Q.original.fullsize.png">

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ntpgErNsubb_zOBpikO4vWX01rghNV3bQEEBFKvvWgA.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TBURl2fTDgm7l82f0_AYUi8eOnQSjWvN_KRZ0fcaMT0.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tESMNALJBL9fYXc40wcYsswAbUiLbpE_2yfs1hK_6jY.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QF37ngM6LH__n76EIxHVp7pHkCNbfbIu9DI8zyiwI9U.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ntpgErNsubb_zOBpikO4vWX01rghNV3bQEEBFKvvWgA.original.fullsize.png">**

**Detailed Solution:**

Truth Table
\begin{array}{|l|l|l|}
\hlineA & B & Y \\
\hline 1 & 1 & 1 \\
\hline 1 & 0 & 0 \\
\hline 0 & 1 & 0 \\
\hline 0 & 0 & 0 \\
\hline
\end{array}
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Qo_K0pTSyAgy7Lazzmc92YmqEsD-3yvVNgRZe4cfFAI.original.fullsize.png">

</details>

---

### Q82. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

In the circuit below, $A$ and $B$ represent two inputs and $C$ represents the output. The circuit represents
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fxSluxhr8PrlSe_UdM2zVKaSaXq3jH6FuBupyUUL_PU.original.fullsize.png">

**Options:**

- **(A)** NOR gate
- **(B)** AND gate
- **(C)** NAND gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) OR gate**

**Detailed Solution:**

\begin{array}{l|l|l}
\mathrm{A} & \mathrm{B} & \mathrm{C} \\
\hline 0 & 0 & 0 \\
\hline 0 & 1 & 1 \\
\hline 1 & 0 & 1 \\
\hline 1 & 1 & 1
\end{array}

</details>

---

