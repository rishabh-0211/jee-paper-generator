# MHT CET Physics - Semiconductors

## Topic 7: Logic gates

**Total Questions:** 88

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

To get output zero for the following circuit, the correct choice for the input is

<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/20_may_shift_1__q31_d1.png" />

a. $A = 1, B = 1, C = 0$
b. $A = 0, B = 1, C = 0$
c. $A = 1, B = 1, C = 1$
d. $A = 1, B = 0, C = 1$

**Options:**

- **(A)** a and b
- **(B)** c and d
- **(C)** a and c
- **(D)** b and d

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a and b**

**Detailed Solution:**

From the given logic circuit, the output of the OR gate is $A + B$.

This output is fed into an AND gate along with input $C$.

Therefore, the final output $Y$ is given by the Boolean expression:

$Y = (A + B) \cdot C$

We need the output $Y$ to be $0$. Let us evaluate the given choices:

For choice a: $A = 1, B = 1, C = 0 \Rightarrow Y = (1 + 1) \cdot 0 = 1 \cdot 0 = 0$

For choice b: $A = 0, B = 1, C = 0 \Rightarrow Y = (0 + 1) \cdot 0 = 1 \cdot 0 = 0$

For choice c: $A = 1, B = 1, C = 1 \Rightarrow Y = (1 + 1) \cdot 1 = 1 \cdot 1 = 1$

For choice d: $A = 1, B = 0, C = 1 \Rightarrow Y = (1 + 0) \cdot 1 = 1 \cdot 1 = 1$

Thus, choices a and b give an output of zero.

Answer: a and b

</details>

---

### Q2. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a two input logic gate, when one input is '1' and the other is '0' (zero), the output is '1'. But even if both inputs are '0' (zero), the output is '1'. The logic gate is

**Options:**

- **(A)** an AND gate.
- **(B)** an X-OR gate.
- **(C)** a NAND gate.
- **(D)** a NOR gate.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) a NAND gate.**

**Detailed Solution:**

Let the inputs be $A$ and $B$, and the output be $Y$.

According to the given conditions:
When $A = 1$ and $B = 0$, $Y = 1$
When $A = 0$ and $B = 0$, $Y = 1$

Let us check the truth tables of the given logic gates:

For an AND gate:
$A = 0, B = 0 \Rightarrow Y = 0$
$A = 1, B = 0 \Rightarrow Y = 0$

For an X-OR gate:
$A = 0, B = 0 \Rightarrow Y = 0$
$A = 1, B = 0 \Rightarrow Y = 1$

For a NAND gate:
$A = 0, B = 0 \Rightarrow Y = 1$
$A = 1, B = 0 \Rightarrow Y = 1$

For a NOR gate:
$A = 0, B = 0 \Rightarrow Y = 1$
$A = 1, B = 0 \Rightarrow Y = 0$

The given conditions are only satisfied by the NAND gate.

Answer: a NAND gate.

</details>

---

### Q3. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the logic circuit given below, for
a) input $A=0$ and input $B=1$, and
b) input $A=1$ and input $B=1$, the output $E$ is respectively
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/19_may_shift_2__q33_d1.png" />

**Options:**

- **(A)** zero and one.
- **(B)** one and zero.
- **(C)** zero and zero.
- **(D)** one and one.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) one and one.**

**Detailed Solution:**

From the given logic circuit diagram, we can determine the Boolean expressions for the intermediate outputs $C$ and $D$, and the final output $E$.

The top AND gate receives inputs $A$ and $B$. Therefore, its output is:
$C = A \cdot B$

The bottom AND gate receives input $B$ and the inverted input of $A$ (which is $\bar{A}$). Therefore, its output is:
$D = \bar{A} \cdot B$

The OR gate receives inputs $C$ and $D$. The final output $E$ is:
$E = C + D$
$E = A \cdot B + \bar{A} \cdot B$

Simplifying the Boolean expression for $E$:
$E = B \cdot (A + \bar{A})$
Since $A + \bar{A} = 1$, we get:
$E = B \cdot 1 = B$

Now, evaluating the given conditions:
a) For input $A = 0$ and $B = 1$:
$E = B = 1$

b) For input $A = 1$ and $B = 1$:
$E = B = 1$

Thus, the output $E$ is one and one respectively.

Answer: one and one.

</details>

---

### Q4. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If two inputs of a NOR gate are shorted, the resulting gate is

**Options:**

- **(A)** a NAND gate.
- **(B)** an OR gate.
- **(C)** an AND gate.
- **(D)** a NOT gate.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) a NOT gate.**

**Detailed Solution:**

The Boolean expression for a NOR gate with inputs $A$ and $B$ is $Y = \overline{A + B}$.

When the two inputs are shorted, $A = B$.

Substituting $B = A$ in the expression, we get $Y = \overline{A + A}$.

According to Boolean algebra, $A + A = A$.

Therefore, $Y = \overline{A}$, which is the Boolean expression for a NOT gate.

Answer: a NOT gate.

</details>

---

### Q5. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An AND gate is followed by a NOT gate in series. With two input $A$ and $B$, the Boolean expression for the output $Y$ will be

**Options:**

- **(A)** $\overline{A+B}$
- **(B)** $\overline{A \cdot B}$
- **(C)** $A \cdot B$
- **(D)** $A + B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\overline{A \cdot B}$**

**Detailed Solution:**

The output of an AND gate with inputs $A$ and $B$ is given by $Y' = A \cdot B$.

This output is then fed into a NOT gate in series. The NOT gate inverts the input signal.

Therefore, the final output $Y$ is the complement of $Y'$, which is $Y = \overline{A \cdot B}$.

This combination of an AND gate followed by a NOT gate is known as a NAND gate.

Answer: $\overline{A \cdot B}$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output Y, when all the three inputs are first high and then low, will respectively be
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/14_may_shift_2__q40_d1.png" />

**Options:**

- **(A)** $1, 0$
- **(B)** $1, 1$
- **(C)** $0, 0$
- **(D)** $0, 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0, 1$**

**Detailed Solution:**

Let the three inputs from top to bottom be $A$, $B$, and $C$.

The first logic gate is an AND gate. Its output is $A \cdot B$.

The second logic gate is a NAND gate. Its inputs are $(A \cdot B)$ and $C$.

The final output $Y$ is given by the Boolean expression:
$Y = \overline{(A \cdot B) \cdot C} = \overline{A \cdot B \cdot C}$

Case 1: When all three inputs are high ($A=1, B=1, C=1$)
$Y = \overline{1 \cdot 1 \cdot 1} = \overline{1} = 0$

Case 2: When all three inputs are low ($A=0, B=0, C=0$)
$Y = \overline{0 \cdot 0 \cdot 0} = \overline{0} = 1$

Therefore, the outputs are $0$ and $1$ respectively.

Answer: $0, 1$

</details>

---

### Q7. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The following circuit is equivalent to
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/13_may_shift_2__q48_d1.png" />

**Options:**

- **(A)** AND gate
- **(B)** NAND gate
- **(C)** NOR gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NOR gate**

**Detailed Solution:**

Output of the first gate (NOR gate) is $Y_1 = \overline{A + B}$.

The second gate is a NAND gate with both inputs connected together, which acts as a NOT gate. Its output is $Y_2 = \overline{Y_1} = \overline{\overline{A + B}} = A + B$.

The third gate is a NOT gate. Its output is $Y = \overline{Y_2} = \overline{A + B}$.

The final output $Y = \overline{A + B}$ represents a NOR gate.

Answer: NOR gate

</details>

---

### Q8. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The output $Y$ of the given logic circuit is similar to the output of
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/12_may_shift_2__q43_d1.png" />

**Options:**

- **(A)** AND gate
- **(B)** NAND gate
- **(C)** OR gate
- **(D)** NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NOR gate**

**Detailed Solution:**

From the given logic circuit, we can identify the intermediate outputs:

The top gate is a NOR gate with inputs $A$ and $B$. Its output is $\overline{A + B}$.

The bottom gate is a NAND gate with inputs $A$ and $B$. Its output is $\overline{A \cdot B}$.

These two outputs are fed into an AND gate. Therefore, the final output $Y$ is:

$Y = (\overline{A + B}) \cdot (\overline{A \cdot B})$

Using De Morgan's laws, we can expand the terms:
$\overline{A + B} = \bar{A} \cdot \bar{B}$
$\overline{A \cdot B} = \bar{A} + \bar{B}$

Substituting these into the expression for $Y$:

$Y = (\bar{A} \cdot \bar{B}) \cdot (\bar{A} + \bar{B})$

Expanding the expression:

$Y = (\bar{A} \cdot \bar{B} \cdot \bar{A}) + (\bar{A} \cdot \bar{B} \cdot \bar{B})$

Since $\bar{A} \cdot \bar{A} = \bar{A}$ and $\bar{B} \cdot \bar{B} = \bar{B}$, we get:

$Y = (\bar{A} \cdot \bar{B}) + (\bar{A} \cdot \bar{B})$

Since $X + X = X$ in Boolean algebra:

$Y = \bar{A} \cdot \bar{B}$

Applying De Morgan's law again:

$Y = \overline{A + B}$

This is the Boolean expression for a NOR gate.

Answer: NOR gate

</details>

---

### Q9. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The truth table for the system of four NAND gates as shown in the figure is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/may/watermarked_images/12_may_shift_1__q50_d1.png" />

**Options:**

- **(A)** <table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr></table>
- **(B)** <table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr></table>
- **(C)** <table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr></table>
- **(D)** <table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr></table>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr></table>**

**Detailed Solution:**

Let the intermediate outputs be $y_1$, $y_2$, and $y_3$.

The output of the first NAND gate is:
$y_1 = \overline{A \cdot B}$

The outputs of the second and third NAND gates are:
$y_2 = \overline{A \cdot y_1} = \overline{A \cdot \overline{AB}} = \bar{A} + AB = \bar{A} + B$
$y_3 = \overline{B \cdot y_1} = \overline{B \cdot \overline{AB}} = \bar{B} + AB = A + \bar{B}$

The final output $Y$ from the fourth NAND gate is:
$Y = \overline{y_2 \cdot y_3} = \overline{(\bar{A} + B) \cdot (A + \bar{B})}$

Expanding the expression inside the complement:
$y_2 \cdot y_3 = \bar{A}A + \bar{A}\bar{B} + BA + B\bar{B} = 0 + \bar{A}\bar{B} + AB + 0 = AB + \bar{A}\bar{B}$

Thus, the final output is:
$Y = \overline{AB + \bar{A}\bar{B}} = \overline{AB} \cdot \overline{\bar{A}\bar{B}} = (\bar{A} + \bar{B}) \cdot (A + B) = \bar{A}A + \bar{A}B + \bar{B}A + \bar{B}B = \bar{A}B + A\bar{B}$

This is the Boolean expression for an XOR gate. The truth table for an XOR gate is:
A B Y
0 0 0
0 1 1
1 0 1
1 1 0

Answer:<table style="border-collapse:collapse;width:auto;"><tr><th style="border:1px solid;width:25px;text-align:center;">A</th><th style="border:1px solid;width:25px;text-align:center;">B</th><th style="border:1px solid;width:25px;text-align:center;">Y</th></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td><td style="border:1px solid;width:25px;text-align:center;">1</td></tr><tr><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">1</td><td style="border:1px solid;width:25px;text-align:center;">0</td></tr></table>

</details>

---

### Q10. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In Boolean expression $A + B = Y$ implies that

**Options:**

- **(A)** $Y$ exists when $A$ or $B$ exists but not when both $A$ and $B$ exist.
- **(B)** $Y$ exists only when $A$ and $B$ both exist.
- **(C)** $Y$ exists when both $A$ and $B$ do not exist.
- **(D)** $Y$ exists when $A$ exists or $B$ exists or both $A$ and $B$ exist

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $Y$ exists when $A$ exists or $B$ exists or both $A$ and $B$ exist**

**Detailed Solution:**

The Boolean expression $A + B = Y$ represents the logical OR operation.

In an OR operation, the output $Y$ is true (exists) if input $A$ is true, or input $B$ is true, or both inputs $A$ and $B$ are true.

Thus, $Y$ exists when $A$ exists, or $B$ exists, or both $A$ and $B$ exist.

Answer: $Y$ exists when $A$ exists or $B$ exists or both $A$ and $B$ exist

</details>

---

### Q11. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The output Y of the following digital logic circuit will be '1' (one) for the inputs
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/19_april_shift_1__q50_d1.png" />

**Options:**

- **(A)** $A = 1$ , $B = 0$ , $C = 0$
- **(B)** $A = 1$ , $B = 0$ , $C = 1$
- **(C)** $A = 1$ , $B = 1$ , $C = 0$
- **(D)** $A = 1$ , $B = 1$ , $C = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $A = 1$ , $B = 1$ , $C = 1$**

**Detailed Solution:**

From the given logic circuit, the gates can be identified as follows:
1. A NOT gate with input $A$, giving output $\bar{A}$.
2. An AND gate with inputs $B$ and $C$, giving output $B \cdot C$.
3. An OR gate taking the outputs of the NOT and AND gates as inputs.

The Boolean expression for the final output $Y$ is:
$Y = \bar{A} + B \cdot C$

For the output to be $Y = 1$, either $\bar{A} = 1$ (which means $A = 0$) or $B \cdot C = 1$ (which means $B = 1$ and $C = 1$).

Since all given options have $A = 1$, we have $\bar{A} = 0$.
Thus, for $Y = 1$, the condition $B \cdot C = 1$ must be satisfied, which requires $B = 1$ and $C = 1$.

Therefore, the correct input combination is $A = 1$, $B = 1$, $C = 1$.

Answer: $A = 1$ , $B = 1$ , $C = 1$

</details>

---

### Q12. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Boolean expression for the given combination of logic gates is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/18_april_shift_2__q49_d1.png" />

**Options:**

- **(A)** $Y = (A+B)\cdot\bar{C}$
- **(B)** $Y = (A\cdot B)\cdot\bar{C}$
- **(C)** $Y = (A+B) + C$
- **(D)** $Y = (A\cdot B) + \bar{C}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $Y = (A\cdot B) + \bar{C}$**

**Detailed Solution:**

The given logic circuit consists of an AND gate, a NOT gate, and an OR gate.

The inputs $A$ and $B$ are connected to the AND gate. The output of this AND gate is $A \cdot B$.

The input $C$ is connected to the NOT gate. The output of this NOT gate is $\bar{C}$.

These two signals, $A \cdot B$ and $\bar{C}$, are fed as inputs to the OR gate.

The final output $Y$ is the logical OR of these two inputs, which gives:
$Y = (A \cdot B) + \bar{C}$

Answer: $Y = (A\cdot B) + \bar{C}$

</details>

---

### Q13. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a two input logic gate, when the inputs are 'zero' and 'zero' the output is 'one'. When the inputs are 'one' and 'zero' the output is 'zero'. The type of logic gate is

**Options:**

- **(A)** NAND
- **(B)** OR
- **(C)** NOR
- **(D)** XOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NOR**

**Detailed Solution:**

Let the inputs be $A$ and $B$, and the output be $Y$.

Given conditions:
When $A = 0$ and $B = 0$, $Y = 1$.
When $A = 1$ and $B = 0$, $Y = 0$.

Checking the given options:
For a NAND gate: $Y = \overline{A \cdot B}$. If $A = 1, B = 0$, $Y = \overline{0} = 1$. This does not match.
For an OR gate: $Y = A + B$. If $A = 0, B = 0$, $Y = 0$. This does not match.
For a NOR gate: $Y = \overline{A + B}$. If $A = 0, B = 0$, $Y = \overline{0} = 1$. If $A = 1, B = 0$, $Y = \overline{1} = 0$. This matches both conditions.
For an XOR gate: $Y = A \oplus B$. If $A = 0, B = 0$, $Y = 0$. This does not match.

Therefore, the logic gate is a NOR gate.

Answer: NOR

</details>

---

### Q14. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output Y of the given logic circuit is
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_2__q49_d1.png" />

**Options:**

- **(A)** $\overline{(A \cdot B)} + \overline{(C \cdot B)}$
- **(B)** $\overline{(A + B)} \cdot \overline{(B \cdot C)}$
- **(C)** $\overline{(A \cdot B)} + \overline{(B + C)}$
- **(D)** $(A + B) + (B + C)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\overline{(A \cdot B)} + \overline{(B + C)}$**

**Detailed Solution:**

The given logic circuit consists of three gates.

The upper gate is a NAND gate with inputs $A$ and $B$. Its output is $\overline{A \cdot B}$.

The lower gate is a NOR gate with inputs $B$ and $C$. Its output is $\overline{B + C}$.

The final gate is an OR gate which takes the outputs of the NAND and NOR gates as its inputs.

Therefore, the final output $Y$ is given by the logical OR operation of these two intermediate outputs:

$Y = \overline{A \cdot B} + \overline{B + C}$

Answer: $\overline{(A \cdot B)} + \overline{(B + C)}$

</details>

---

### Q15. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following logic gates will have an output of '1' (one) for the given inputs?
<img style="width: 530px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/17_april_shift_1__q49_d1.png" />

**Options:**

- **(A)** D
- **(B)** B
- **(C)** A
- **(D)** C

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) B**

**Detailed Solution:**

Let us evaluate the output for each logic gate given in the options:

For gate (A): It is a NAND gate with inputs $1$ and $1$.
Output $Y = \overline{1 \cdot 1} = \overline{1} = 0$

For gate (B): It is a NAND gate with inputs $1$ and $0$.
Output $Y = \overline{1 \cdot 0} = \overline{0} = 1$

For gate (C): It is a NOR gate with inputs $0$ and $1$.
Output $Y = \overline{0 + 1} = \overline{1} = 0$

For gate (D): It is an XOR gate with inputs $0$ and $0$.
Output $Y = 0 \oplus 0 = 0$

Therefore, only gate (B) has an output of $1$.

Answer: B

</details>

---

### Q16. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the following digital circuit, the output 'Y' will be '1' (one) for inputs 'A' and 'B' having values
<img style="width: 300px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_2__q50_d1.png" />

**Options:**

- **(A)** $A = 0 , B = 0$
- **(B)** $A = 0 , B = 1$
- **(C)** $A = 1 , B = 0$
- **(D)** $A = 1 , B = 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $A = 1 , B = 1$**

**Detailed Solution:**

The Boolean expression for the output $Y$ can be determined from the logic circuit.

The top gate is a NAND gate with inputs $A$ and $B$. Its output is $Y_1 = \overline{A \cdot B}$.

The middle gate is a NOT gate with input $A$. Its output is $\overline{A}$.

The bottom gate is a NOR gate with inputs $\overline{A}$ and $B$. Its output is $Y_2 = \overline{\overline{A} + B}$.

The final gate is a NOR gate with inputs $Y_1$ and $Y_2$. Its output is $Y = \overline{Y_1 + Y_2}$.

Substituting the expressions for $Y_1$ and $Y_2$ into the final output equation:

$Y = \overline{\overline{A \cdot B} + \overline{\overline{A} + B}}$

Using De Morgan's laws, the expression simplifies to:

$Y = \overline{(\overline{A \cdot B})} \cdot \overline{(\overline{\overline{A} + B})}$

$Y = (A \cdot B) \cdot (\overline{A} + B)$

Expanding the expression:

$Y = A \cdot B \cdot \overline{A} + A \cdot B \cdot B$

Since $A \cdot \overline{A} = 0$ and $B \cdot B = B$, the expression becomes:

$Y = 0 + A \cdot B$

$Y = A \cdot B$

Given that the output $Y = 1$:

$A \cdot B = 1$

This condition is satisfied only when both inputs are $1$.

Therefore, $A = 1$ and $B = 1$.

Answer: $A = 1 , B = 1$

</details>

---

### Q17. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

To get the truth table shown from the following logic circuit, the gate G should be
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/16_april_shift_1__q50_d1.png" />

**Options:**

- **(A)** NAND gate.
- **(B)** NOR gate.
- **(C)** AND gate.
- **(D)** OR gate.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) AND gate.**

**Detailed Solution:**

From the given logic circuit, the output $Y$ is given by the Boolean expression:

$Y = A + G(A, B)$

From the given truth table, we can observe that the output $Y$ is identical to the input $A$ for all combinations of $A$ and $B$.

Thus, $Y = A$.

Equating the two expressions for $Y$, we get:

$A + G(A, B) = A$

Let us check the given options for gate G:

If G is an AND gate, $G(A, B) = A \cdot B$.

Then, $Y = A + A \cdot B = A(1 + B) = A \cdot 1 = A$.

This perfectly matches the required condition.

Checking other options:
If G is an OR gate, $Y = A + (A + B) = A + B \neq A$.
If G is a NAND gate, $Y = A + \overline{A \cdot B}$. For $A=0, B=0$, $Y = 0 + 1 = 1 \neq 0$.
If G is a NOR gate, $Y = A + \overline{A + B}$. For $A=0, B=0$, $Y = 0 + 1 = 1 \neq 0$.

Therefore, the gate G must be an AND gate.

Answer: AND gate.

</details>

---

### Q18. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In which of the logic gate the following statement is true? "The output is high when either of the inputs is high but not if both inputs are high"

**Options:**

- **(A)** NAND
- **(B)** NOR
- **(C)** X-OR
- **(D)** OR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) X-OR**

**Detailed Solution:**

The given statement states that the output is high ($1$) when either of the inputs is high ($1$), but the output is low ($0$) if both inputs are high ($1$).

This corresponds to the following truth table:
$A = 0, B = 0 \Rightarrow Y = 0$
$A = 1, B = 0 \Rightarrow Y = 1$
$A = 0, B = 1 \Rightarrow Y = 1$
$A = 1, B = 1 \Rightarrow Y = 0$

This is the characteristic truth table of an Exclusive-OR (X-OR) gate.

Answer: X-OR

</details>

---

### Q19. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The resultant gate and its Boolean expression in the given circuit is
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/15_april_shift_1__q34_d1.png" />

**Options:**

- **(A)** $\text{AND}, \overline{\text{A} + \text{B}}$
- **(B)** $\text{NAND}, \text{A} + \text{B}$
- **(C)** $\text{OR}, \text{A} + \text{B}$
- **(D)** $\text{NOR}, \text{A} - \text{B}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\text{OR}, \text{A} + \text{B}$**

**Detailed Solution:**

The given circuit consists of a NOR gate followed by a NOT gate.

The output of the NOR gate is given by:
$C = \overline{A + B}$

This output $C$ is then passed through a NOT gate. The final output $Y$ is:
$Y = \overline{C}$

Substituting the value of $C$, we get:
$Y = \overline{\overline{A + B}}$

Using the property of Boolean algebra $\overline{\overline{X}} = X$, we have:
$Y = A + B$

This is the Boolean expression for an OR gate.

Answer: $\text{OR}, \text{A} + \text{B}$

</details>

---

### Q20. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the logic circuit diagram, when all the four inputs, A, B, C, D are 'one' the outputs $Y_1$, $Y_2$, $Y_3$ are respectively (1, 1, 0). When the inputs A and C are changed to zero and B and D are still 'one', then the outputs $Y_1$, $Y_2$, $Y_3$ are respectively change to
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/14_april_shift_2__q38_d1.png" />

**Options:**

- **(A)** $1, 1, 1$
- **(B)** $1, 0, 0$
- **(C)** $0, 1, 0$
- **(D)** $0, 0, 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1, 0, 0$**

**Detailed Solution:**

From the given logic circuit diagram, we can determine the Boolean expressions for the outputs $Y_1$, $Y_2$, and $Y_3$.

The output $Y_1$ is the result of a NOR gate with inputs $A$ and $B$, followed by a NOT gate:
$Y_1 = \overline{\overline{A + B}} = A + B$

The output $Y_2$ is the result of an AND gate with inputs $C$ and $D$:
$Y_2 = C \cdot D$

The output $Y_3$ is the result of a NOR gate with inputs $Y_1$ and $Y_2$:
$Y_3 = \overline{Y_1 + Y_2}$

Given the new input conditions: $A = 0$, $B = 1$, $C = 0$, and $D = 1$.

Substituting these values into the expressions:
$Y_1 = 0 + 1 = 1$
$Y_2 = 0 \cdot 1 = 0$
$Y_3 = \overline{1 + 0} = \overline{1} = 0$

Therefore, the outputs $Y_1$, $Y_2$, and $Y_3$ are $1, 0, 0$ respectively.

Answer: $1, 0, 0$

</details>

---

### Q21. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the case of NAND gate, if A and B are inputs and Y is the output then

**Options:**

- **(A)** $Y = \overline{A + B}$
- **(B)** $Y = A \cdot B$
- **(C)** $Y = \overline{A \cdot B}$
- **(D)** $Y = A + B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $Y = \overline{A \cdot B}$**

**Detailed Solution:**

A NAND gate is a combination of an AND gate followed by a NOT gate.

The Boolean expression for an AND gate with inputs $A$ and $B$ is $Y' = A \cdot B$.

Passing this output through a NOT gate gives the final output $Y = \overline{Y'}$.

Therefore, the Boolean expression for a NAND gate is $Y = \overline{A \cdot B}$.

Answer: $Y = \overline{A \cdot B}$

</details>

---

### Q22. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

What does the following combination of gates produce?
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/mht_cet_pyqs_2026/april/watermarked_images/11_april_shift_1__q39_d1.png" />

**Options:**

- **(A)** NAND gate
- **(B)** NOR gate
- **(C)** XOR gate
- **(D)** AND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) NAND gate**

**Detailed Solution:**

From the given logic circuit diagram:

The output of gate $G_1$ (NOT gate) is $\overline{A}$.
The output of gate $G_2$ (NOT gate) is $\overline{B}$.

These are fed as inputs to gate $G_3$, which is a NOR gate. The output of $G_3$ is:
$Y' = \overline{\overline{A} + \overline{B}}$

This output is then fed to gate $G_4$, which is another NOT gate. The final output $Y$ is:
$Y = \overline{Y'} = \overline{\overline{\overline{A} + \overline{B}}}$
$Y = \overline{A} + \overline{B}$

Using De Morgan's theorem, we can write:
$\overline{A} + \overline{B} = \overline{A \cdot B}$

The boolean expression $Y = \overline{A \cdot B}$ represents a NAND gate.

Answer: NAND gate

</details>

---

### Q23. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An AND gate is followed by a NOT gate in series. With two inputs 'A' and 'B', the Boolean expression for the output 'Y' will be

**Options:**

- **(A)** $\overline{\mathrm{A}+\mathrm{B}}$
- **(B)** $\overline{\mathrm{A} \cdot \mathrm{B}}$
- **(C)** $\mathrm{A} \cdot \mathrm{B}$
- **(D)** $\mathrm{A}+\mathrm{B}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\overline{\mathrm{A} \cdot \mathrm{B}}$**

**Detailed Solution:**

The output of an AND gate with inputs $\mathrm{A}$ and $\mathrm{B}$ is given by $\mathrm{A} \cdot \mathrm{B}$.

When this output is passed through a NOT gate in series, it gets inverted.

The final output $\mathrm{Y}$ is the complement of the AND gate output, which is $\mathrm{Y} = \overline{\mathrm{A} \cdot \mathrm{B}}$.

This combination is known as a NAND gate.

Answer: $\overline{\mathrm{A} \cdot \mathrm{B}}$

</details>

---

### Q24. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Out of the following gates, identify the gates which will give an output as '0' (zero) for the given inputs.

<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/l2pN3hSw5HuS62xsjh-63xR9Fnl41uEEbx7-janwTfw.original.fullsize.png">

**Options:**

- **(A)** (A) and (C)
- **(B)** (B) and (D)
- **(C)** (B) and (C)
- **(D)** (A) and (D)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) (A) and (C)**

**Detailed Solution:**

Let us analyze the output of each logic gate given in the options:

For gate (A): The symbol represents a NAND gate. The inputs are $1$ and $1$. 
The Boolean expression for a NAND gate is $Y = \overline{A \cdot B}$.
Output $Y = \overline{1 \cdot 1} = \overline{1} = 0$.

For gate (B): The symbol represents a NOR gate. The inputs are $0$ and $0$. 
The Boolean expression for a NOR gate is $Y = \overline{A + B}$.
Output $Y = \overline{0 + 0} = \overline{0} = 1$.

For gate (C): The symbol represents an AND gate. The inputs are $1$ and $0$. 
The Boolean expression for an AND gate is $Y = A \cdot B$.
Output $Y = 1 \cdot 0 = 0$.

For gate (D): The symbol represents an XOR gate. The inputs are $0$ and $1$. 
The Boolean expression for an XOR gate is $Y = A \oplus B$.
Output $Y = 0 \oplus 1 = 1$.

Therefore, the gates which give an output of '0' are (A) and (C).

Answer: (A) and (C)

</details>

---

### Q25. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a certain 2-inputs logic gate, when inputs $\mathrm{A}=0$ and $\mathrm{B}=0$, then output $C=1$. And also when inputs $A=0, B=1$, then again output $C=1$. The gate must be

**Options:**

- **(A)** OR
- **(B)** AND
- **(C)** NAND
- **(D)** NOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NAND**

**Detailed Solution:**

For an OR gate, when $A=0$ and $B=0$, the output is $C=0$.

For an AND gate, when $A=0$ and $B=0$, the output is $C=0$.

For a NOR gate, when $A=0$ and $B=1$, the output is $C=0$.

For a NAND gate, the output is $1$ unless both inputs are $1$. Thus, when $A=0, B=0$, the output is $C=1$ and when $A=0, B=1$, the output is $C=1$.

Therefore, the given conditions are satisfied only by a NAND gate.

Answer: NAND

</details>

---

### Q26. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

One of the following values of inputs $\mathrm{A}, \mathrm{B}$ and C respectively gives output $(\mathrm{Y})$ of the following combination of logic gates as ' 1 ' is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/2xjAu66bk002QQ8BQzEcfSefo2dL9hZAT7BOB1y5uxs.original.fullsize.png">

**Options:**

- **(A)** 0,0,0
- **(B)** 0,1,0
- **(C)** 1,0,0
- **(D)** 1,0,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1,0,1**

**Detailed Solution:**

From the given logic circuit, the inputs B and C are connected to an OR gate, producing an output $B + C$.

This output and input A are connected to an AND gate. The final output Y is given by the Boolean expression:
$Y = A \cdot (B + C)$

We require the output $Y = 1$. For an AND gate to output 1, both its inputs must be 1. This implies $A = 1$ and $B + C = 1$.

Evaluating the given options:
For $A=0, B=0, C=0$: $Y = 0 \cdot (0 + 0) = 0$
For $A=0, B=1, C=0$: $Y = 0 \cdot (1 + 0) = 0$
For $A=1, B=0, C=0$: $Y = 1 \cdot (0 + 0) = 0$
For $A=1, B=0, C=1$: $Y = 1 \cdot (0 + 1) = 1$

Thus, the input combination $1, 0, 1$ gives the output $Y = 1$.

Answer: 1,0,1

</details>

---

### Q27. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

To get output of the following logic circuit as ' 0 ' (zero), the inputs $\mathrm{A}, \mathrm{B}$, C should NOT be, respectively,
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/t4SGUmXikKDKINfbEY7IFCeLyevZt7TvEeselZrcCEk.original.fullsize.png">

**Options:**

- **(A)** 1,1,0
- **(B)** 0,1,0
- **(C)** 1,0,1
- **(D)** 0,0,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0,0,1**

**Detailed Solution:**

The logic circuit consists of a NOR gate and an AND gate.

The inputs to the NOR gate are $A$ and $B$, so its output is $\overline{A + B}$.

This output and input $C$ are fed into the AND gate. The final output $Y$ is given by the Boolean expression:

$Y = (\overline{A + B}) \cdot C$

The question asks for the input combination that should NOT be used to get an output of $0$. This means we need to find the inputs that result in an output of $1$.

For $Y = 1$, both inputs to the AND gate must be $1$.

Therefore, $\overline{A + B} = 1$ and $C = 1$.

For the NOR gate output to be $1$, both inputs $A$ and $B$ must be $0$.

Thus, $A = 0$ and $B = 0$.

The required inputs are $A = 0, B = 0, C = 1$.

Answer: 0,0,1

</details>

---

### Q28. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logic gate for which the output goes 'HIGH' or '1' only when an odd number of 'HIGH' or '1' are at its input, is

**Options:**

- **(A)** OR gate
- **(B)** NAND gate
- **(C)** Ex-OR gate
- **(D)** NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Ex-OR gate**

**Detailed Solution:**

The truth table for a two-input Ex-OR (Exclusive-OR) gate is as follows:
Input A = $0$, Input B = $0$ $\Rightarrow$ Output = $0$
Input A = $0$, Input B = $1$ $\Rightarrow$ Output = $1$
Input A = $1$, Input B = $0$ $\Rightarrow$ Output = $1$
Input A = $1$, Input B = $1$ $\Rightarrow$ Output = $0$

The output is 'HIGH' or '$1$' only when exactly one of the inputs is '$1$' (which is an odd number of 'HIGH' inputs). In general, for any number of inputs, an Ex-OR gate gives a 'HIGH' output if and only if an odd number of its inputs are 'HIGH'. Hence, it is also known as an odd parity generator.

Answer: Ex-OR gate

</details>

---

### Q29. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the logic circuit given, $\mathrm{A}, \mathrm{B}$ and C are the inputs and Y is the output. The output Y is HIGH
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/un9QHZsqmW_Z_eO2n5KTaHal0r0tnkSqVzC_8EboxjA.original.fullsize.png">

**Options:**

- **(A)** for all the HIGH inputs.
- **(B)** for all the LOW inputs.
- **(C)** when $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=0$
- **(D)** when $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) when $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=0$**

**Detailed Solution:**

From the given logic circuit, the inputs to the NOR gate are $B$ and $C$. Its output is $\overline{B+C}$.

This output is fed to an AND gate along with input $A$.

The final output $Y$ is given by the Boolean expression:
$Y = A \cdot (\overline{B+C})$

For the output $Y$ to be HIGH ($Y = 1$), both inputs to the AND gate must be HIGH ($1$).
Therefore, $A = 1$ and $\overline{B+C} = 1$.

For $\overline{B+C} = 1$, we must have $B+C = 0$, which implies $B = 0$ and $C = 0$.

Thus, the output $Y$ is HIGH when $A = 1$, $B = 0$, and $C = 0$.

Answer: when $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=0$

</details>

---

### Q30. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the following combination of logic gates, the output $Y$ can be written in the terms of inputs A and B as
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/f37ij1ujSF58nJIDTBJJVxMa34QnfAXtP_xtF4mtVtM.original.fullsize.png">

**Options:**

- **(A)** $(\mathrm{A} \cdot \overline{\mathrm{B}})+(\overline{\mathrm{A}} \cdot \mathrm{B})$
- **(B)** $(\mathrm{A} \cdot \mathrm{B})+(\overline{\mathrm{A}} \cdot \mathrm{B})$
- **(C)** $(\overline{\mathrm{A} \cdot \mathrm{B}})+(\overline{\mathrm{A}} \cdot \mathrm{B})$
- **(D)** $(\overline{\mathrm{A} \cdot \mathrm{B}}) \cdot(\mathrm{A} \cdot \overline{\mathrm{B}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\overline{\mathrm{A} \cdot \mathrm{B}})+(\overline{\mathrm{A}} \cdot \mathrm{B})$**

**Detailed Solution:**

Let us analyze the logic circuit step-by-step:

The inputs to the top AND gate are $A$ and $B$. Its output is $A \cdot B$.

This output passes through a NOT gate, giving $\overline{A \cdot B}$.

The inputs to the bottom AND gate are $\overline{A}$ (since input $A$ passes through a NOT gate) and $B$. Its output is $\overline{A} \cdot B$.

These two outputs are fed into an OR gate.

Therefore, the final output $Y$ is the logical OR of these two signals, which is given by:
$Y = (\overline{A \cdot B}) + (\overline{A} \cdot B)$

Answer: $(\overline{\mathrm{A} \cdot \mathrm{B}})+(\overline{\mathrm{A}} \cdot \mathrm{B})$

</details>

---

### Q31. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following logic gates is called as Universal gate?

**Options:**

- **(A)** OR
- **(B)** X-OR
- **(C)** AND
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NAND**

**Detailed Solution:**

A universal gate is a logic gate that can be used to implement any other logic gate or Boolean function without requiring any other type of gate.

The NAND and NOR gates are the two universal logic gates.

Among the given options, NAND is the universal gate.

Answer: NAND

</details>

---

### Q32. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The resultant logic gate from the combination of following gates is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/zTbgco5GIyXRIaG_Ila4FQIQvvzvhbMqnT6HxhvY9ks.original.fullsize.png">

**Options:**

- **(A)** OR
- **(B)** NAND
- **(C)** AND
- **(D)** NOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR**

**Detailed Solution:**

From the given logic circuit, the inputs $A$ and $B$ are first passed through NOT gates.

The outputs of the NOT gates are $\overline{A}$ and $\overline{B}$.

These outputs are then fed as inputs to a NAND gate. The Boolean expression for the final output $Y$ is:
$Y = \overline{\overline{A} \cdot \overline{B}}$

Using De Morgan's theorem ($\overline{X \cdot Y} = \overline{X} + \overline{Y}$), we can simplify the expression:
$Y = \overline{\overline{A}} + \overline{\overline{B}}$

Since the double inversion of a variable is the variable itself ($\overline{\overline{A}} = A$), we get:
$Y = A + B$

The Boolean expression $Y = A + B$ represents an OR gate.

Answer: OR

</details>

---

### Q33. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a given logic circuit, the output Y when all the three inputs $\mathrm{A}, \mathrm{B}, \mathrm{C}$ are first low and then high will be respectively
<img src="https://cdn.quizrr.in/question-assets/mhtcet/mhtcet2025/amcKTFRvsW3YHamCjJC7KSvDNDF5t0GgFDwZS5q57jE.original.fullsize.png">

**Options:**

- **(A)** $(0,0)$
- **(B)** $(0,1)$
- **(C)** $(1,0)$
- **(D)** $(1,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(1,0)$**

**Detailed Solution:**

From the given logic circuit diagram, we can identify the following gates:
1. The gate connected to input $A$ is a NOT gate. Its output is $\bar{A}$.
2. The gate connected to inputs $B$ and $C$ is a NAND gate. Its output is $\overline{B \cdot C}$.
3. These two outputs are fed into an OR gate. Therefore, the Boolean expression for the final output $Y$ is:
$Y = \bar{A} + \overline{B \cdot C}$

Case 1: When all three inputs are low ($A = 0, B = 0, C = 0$)
$Y = \bar{0} + \overline{0 \cdot 0}$
$Y = 1 + \bar{0}$
$Y = 1 + 1 = 1$

Case 2: When all three inputs are high ($A = 1, B = 1, C = 1$)
$Y = \bar{1} + \overline{1 \cdot 1}$
$Y = 0 + \bar{1}$
$Y = 0 + 0 = 0$

The output $Y$ when the inputs are first low and then high is $1$ and $0$ respectively. Thus, the correct pair is $(1, 0)$.

Answer: $(1,0)$

</details>

---

### Q34. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Boolean expression for the given combination of logic gates is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/M1nKVneRpWdQavdVsqI8QTG93W_HKbnQ7Kkfxa3F02M.original.fullsize.png"/>

**Options:**

- **(A)** $\mathrm{Y}=(\overline{\mathrm{A}} \cdot \mathrm{B})+\mathrm{C}$
- **(B)** $\mathrm{Y}=(\overline{\mathrm{A}}+\mathrm{B}) \cdot \mathrm{C}$
- **(C)** $\mathrm{Y}=\overline{\mathrm{A}}+(\mathrm{B} \cdot \mathrm{C})$
- **(D)** $\mathrm{Y}=\overline{\mathrm{A}} \cdot(\mathrm{B}+\mathrm{C})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{Y}=\overline{\mathrm{A}}+(\mathrm{B} \cdot \mathrm{C})$**

**Detailed Solution:**

From the given logic circuit diagram:

The input $A$ is connected to a NOT gate, so its output is $\overline{A}$.

The inputs $B$ and $C$ are connected to an AND gate, so its output is $B \cdot C$.

These two outputs are then fed as inputs to an OR gate. The OR gate performs logical addition.

Therefore, the final output $Y$ is given by the Boolean expression:
$Y = \overline{A} + (B \cdot C)$

Answer: $\mathrm{Y}=\overline{\mathrm{A}}+(\mathrm{B} \cdot \mathrm{C})$

</details>

---

### Q35. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

To get the truth table shown from the following logic circuit, the logic gate G should be
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Q0vyl33KEZ9h6HJ9C4_BY8dEWgqDm7NSPNhnqdqV9Dw.original.fullsize.png"/>

**Options:**

- **(A)** AND
- **(B)** OR
- **(C)** NAND
- **(D)** NOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NAND**

**Detailed Solution:**

From the given logic circuit, the output $Y$ is the result of an OR gate with inputs $A$ and the output of gate $G$.

Let the output of gate $G$ be $Y_G$. The Boolean expression for the circuit is:

$Y = A + Y_G$

From the given truth table, we can analyze the required output of gate $G$ for different inputs:

For $A = 0, B = 0$, the output is $Y = 1$.

$0 + Y_G(0, 0) = 1 \Rightarrow Y_G(0, 0) = 1$

For $A = 0, B = 1$, the output is $Y = 1$.

$0 + Y_G(0, 1) = 1 \Rightarrow Y_G(0, 1) = 1$

Now let us check the given options for gate $G$:

If $G$ is an AND gate: $Y_G(0, 0) = 0 \cdot 0 = 0 \neq 1$.

If $G$ is an OR gate: $Y_G(0, 0) = 0 + 0 = 0 \neq 1$.

If $G$ is a NOR gate: $Y_G(0, 1) = \overline{0 + 1} = 0 \neq 1$.

If $G$ is a NAND gate: $Y_G(0, 0) = \overline{0 \cdot 0} = 1$ and $Y_G(0, 1) = \overline{0 \cdot 1} = 1$.

Let us verify the remaining cases for a NAND gate:

For $A = 1, B = 0$: $Y_G(1, 0) = \overline{1 \cdot 0} = 1 \Rightarrow Y = 1 + 1 = 1$.

For $A = 1, B = 1$: $Y_G(1, 1) = \overline{1 \cdot 1} = 0 \Rightarrow Y = 1 + 0 = 1$.

This perfectly matches the given truth table. Therefore, the logic gate $G$ is a NAND gate.

Answer: NAND

</details>

---

### Q36. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The truth table of the following circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/E6iB0o8lhJIRIL0be3axLM1mSGkzVWBD3dI3_W_p9PM.original.fullsize.png"/>

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Do8XErTgr5F4d_E-HJIKI56i8jFhmNlBxrBJjm8ypLw.original.fullsize.png"/>
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/6ulUTF_nWy5Odte9A5nPaN0ptTbixLnFGprmsfg1z90.original.fullsize.png"/>
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/hd71Z_xLPDaoiCN_wWQesaaMCYKdWPrMGjRdLgSDg14.original.fullsize.png"/>
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/WCT2zd6DjVCbL4ojAKOat9-PUVakcGfveOqZ8jVjsdo.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/hd71Z_xLPDaoiCN_wWQesaaMCYKdWPrMGjRdLgSDg14.original.fullsize.png"/>**

**Detailed Solution:**

The given circuit consists of three NAND gates.

The first NAND gate has its two inputs tied together and connected to $A$. It acts as a NOT gate. Its output is $Y_1 = \overline{A \cdot A} = \overline{A}$.

The second NAND gate has its two inputs tied together and connected to $B$. It also acts as a NOT gate. Its output is $Y_2 = \overline{B \cdot B} = \overline{B}$.

The third NAND gate takes $Y_1$ and $Y_2$ as inputs. Its output $Y$ is given by:
$Y = \overline{Y_1 \cdot Y_2}$

Substituting the values of $Y_1$ and $Y_2$:
$Y = \overline{\overline{A} \cdot \overline{B}}$

Using De Morgan's theorem ($\overline{X \cdot Y} = \overline{X} + \overline{Y}$):
$Y = \overline{\overline{A}} + \overline{\overline{B}}$
$Y = A + B$

This is the Boolean expression for an OR gate. The truth table for an OR gate is:
If $A = 0, B = 0$, then $Y = 0 + 0 = 0$
If $A = 0, B = 1$, then $Y = 0 + 1 = 1$
If $A = 1, B = 0$, then $Y = 1 + 0 = 1$
If $A = 1, B = 1$, then $Y = 1 + 1 = 1$

This matches the truth table in the third option.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/hd71Z_xLPDaoiCN_wWQesaaMCYKdWPrMGjRdLgSDg14.original.fullsize.png"/>

</details>

---

### Q37. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two different logic gates giving output ' 1 ' for the inputs $(1,0)$ and then for $(0,1)$ are

**Options:**

- **(A)** 'AND', 'OR'
- **(B)** 'OR', 'NOR'
- **(C)** 'NAND', 'NOR'
- **(D)** 'NAND', 'OR'

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 'NAND', 'OR'**

**Detailed Solution:**

Let the inputs be $A$ and $B$. We need to find the logic gates that give an output $Y = 1$ for the input combinations $(A=1, B=0)$ and $(A=0, B=1)$.

For an OR gate, the Boolean expression is $Y = A + B$.
If $A=1, B=0$, $Y = 1 + 0 = 1$.
If $A=0, B=1$, $Y = 0 + 1 = 1$.

For a NAND gate, the Boolean expression is $Y = \overline{A \cdot B}$.
If $A=1, B=0$, $Y = \overline{1 \cdot 0} = \overline{0} = 1$.
If $A=0, B=1$, $Y = \overline{0 \cdot 1} = \overline{0} = 1$.

For an AND gate, $Y = A \cdot B$.
If $A=1, B=0$, $Y = 1 \cdot 0 = 0$.

For a NOR gate, $Y = \overline{A + B}$.
If $A=1, B=0$, $Y = \overline{1 + 0} = \overline{1} = 0$.

Thus, the two different logic gates that give an output of $1$ for both sets of inputs are NAND and OR.

Answer: 'NAND', 'OR'

</details>

---

### Q38. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the following digital logic circuit, the correct truth-table is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/fsM3fSMK3VCkbil7g-g5s3jjoAtO2vQOz03nNazwvkc.original.fullsize.png"/>
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/w6Pe-z-vd-G2U-iuV5FVawgqd2hTN6NGq3B_JxYFW10.original.fullsize.png"/>

**Options:**

- **(A)** Q
- **(B)** P
- **(C)** S
- **(D)** R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) R**

**Detailed Solution:**

The given logic circuit consists of a NOT gate and a NAND gate.

The input $A$ passes through the NOT gate, so its output is $\overline{A}$.

The inputs to the NAND gate are $\overline{A}$ and $B$.

The Boolean expression for the output $Y$ of the NAND gate is:
$Y = \overline{\overline{A} \cdot B}$

Using De Morgan's theorem:
$Y = \overline{\overline{A}} + \overline{B} = A + \overline{B}$

Evaluating $Y$ for all possible combinations of inputs $A$ and $B$:
If $A = 0, B = 0$, then $Y = 0 + \overline{0} = 0 + 1 = 1$
If $A = 0, B = 1$, then $Y = 0 + \overline{1} = 0 + 0 = 0$
If $A = 1, B = 0$, then $Y = 1 + \overline{0} = 1 + 1 = 1$
If $A = 1, B = 1$, then $Y = 1 + \overline{1} = 1 + 0 = 1$

This corresponds to the truth table (R).

Answer: R

</details>

---

### Q39. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Following combination of gates is equivalent to
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/Xy0Bw53I4x7OYKT_8idsT-BjHJ7CQVkyBW3O8g65nc0.original.fullsize.png"/>

**Options:**

- **(A)** NAND gate
- **(B)** OR gate
- **(C)** NOR gate
- **(D)** X-OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) X-OR gate**

**Detailed Solution:**

Let the output of the first NAND gate be $Y_1$.

$Y_1 = \overline{A \cdot B}$

The output of the upper NAND gate is $Y_2$.

$Y_2 = \overline{A \cdot Y_1} = \overline{A \cdot \overline{A \cdot B}} = \overline{A \cdot (\overline{A} + \overline{B})} = \overline{A\overline{A} + A\overline{B}} = \overline{A\overline{B}}$

The output of the lower NAND gate is $Y_3$.

$Y_3 = \overline{B \cdot Y_1} = \overline{B \cdot \overline{A \cdot B}} = \overline{B \cdot (\overline{A} + \overline{B})} = \overline{\overline{A}B + B\overline{B}} = \overline{\overline{A}B}$

The final output $Y$ is from the last NAND gate with inputs $Y_2$ and $Y_3$.

$Y = \overline{Y_2 \cdot Y_3} = \overline{Y_2} + \overline{Y_3}$

Substituting $Y_2$ and $Y_3$:

$Y = \overline{\overline{A\overline{B}}} + \overline{\overline{\overline{A}B}} = A\overline{B} + \overline{A}B$

This is the Boolean expression for an X-OR gate.

Answer: X-OR gate

</details>

---

### Q40. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The logic gate represented by following logic circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/kzIibDMj1EwY2aliYmCRbJSG7q4mGXqsfSzLG5d1iWQ.original.fullsize.png"/>

**Options:**

- **(A)** OR gate.
- **(B)** AND gate.
- **(C)** NOR gate.
- **(D)** X-OR gate.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) X-OR gate.**

**Detailed Solution:**

From the given logic circuit, we can identify the gates and their outputs:

The top gate is a NAND gate with inputs $A$ and $B$. Its output is $\overline{A \cdot B}$.

The bottom gate is an OR gate with inputs $A$ and $B$. Its output is $A + B$.

The final gate is an AND gate, which takes the outputs of the NAND and OR gates as its inputs. Therefore, the final output $Y$ is given by:

$Y = (\overline{A \cdot B}) \cdot (A + B)$

Using De Morgan's laws, we can expand $\overline{A \cdot B}$ as $\overline{A} + \overline{B}$:

$Y = (\overline{A} + \overline{B}) \cdot (A + B)$

Expanding the expression, we get:

$Y = \overline{A} \cdot A + \overline{A} \cdot B + \overline{B} \cdot A + \overline{B} \cdot B$

Since $\overline{A} \cdot A = 0$ and $\overline{B} \cdot B = 0$, the expression simplifies to:

$Y = 0 + \overline{A} \cdot B + A \cdot \overline{B} + 0$

$Y = A \cdot \overline{B} + \overline{A} \cdot B$

This is the standard Boolean expression for an Exclusive-OR (X-OR) gate.

Answer: X-OR gate.

</details>

---

### Q41. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

What is the output Y in the following circuit, when all the three inputs A, B, C are first 'zero' and then 'one'?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aYvfooak2UdaDxd--A_eQJ_BM6Bkymmse4Bu3XcM1vw.original.fullsize_2.png"/>

**Options:**

- **(A)** 0,0
- **(B)** 0,1
- **(C)** 1,0
- **(D)** 1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1,0**

**Detailed Solution:**

The given circuit consists of an AND gate followed by a NAND gate.

Let the output of the first gate (AND gate) be $X$.
$X = A \cdot B$

The output of the second gate (NAND gate) is $Y$.
$Y = \overline{X \cdot C} = \overline{(A \cdot B) \cdot C}$

Case 1: When all inputs are zero ($A = 0, B = 0, C = 0$)
$X = 0 \cdot 0 = 0$
$Y = \overline{0 \cdot 0} = \overline{0} = 1$

Case 2: When all inputs are one ($A = 1, B = 1, C = 1$)
$X = 1 \cdot 1 = 1$
$Y = \overline{1 \cdot 1} = \overline{1} = 0$

Therefore, the output $Y$ is $1, 0$.

Answer: 1,0

</details>

---

### Q42. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The resultant gate and its Boolean expression in the given circuit is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/KTMElDEudWTv_fQbgSEsImaWJoydzR1jLCnQelnPDWg.original.fullsize.png"/>

**Options:**

- **(A)** OR, A+B
- **(B)** AND, A - B
- **(C)** NOR, A+B
- **(D)** NAND, $\overline{\mathrm{A}+\mathrm{B}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR, A+B**

**Detailed Solution:**

The given logic circuit consists of a NOR gate followed by a NOT gate.

The first gate is a NOR gate with inputs $A$ and $B$. Its output is given by $\overline{A+B}$.

This output is then fed as an input to the second gate, which is a NOT gate. The NOT gate inverts its input.

Therefore, the final output $Y$ is:

$Y = \overline{\overline{A+B}}$

According to the involution law of Boolean algebra, the double complement of a variable is the variable itself ($\overline{\overline{X}} = X$).

$Y = A + B$

The Boolean expression $A + B$ represents an OR gate.

Answer: OR, A+B

</details>

---

### Q43. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the logic circuit diagram, when all the four inputs $\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}$ are one, the outputs $\mathrm{Y}_1, \mathrm{Y}_2, \mathrm{Y}_3$ are respectively $(1,1,0)$. When all the inputs A, B , C , D are changed to 'zero', the outputs $\mathrm{Y}_1, \mathrm{Y}_2, \mathrm{Y}_3$ respectively change to
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/xDYacnuQTEJ93JIx0fwlnXdiki4-KKjiiEtqJJQmhYE.original.fullsize.png"/>

**Options:**

- **(A)** $(0,1,0)$
- **(B)** $(0,0,1)$
- **(C)** $(1,1,0)$
- **(D)** $(1,1,1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(0,0,1)$**

**Detailed Solution:**

From the given logic circuit diagram, we can identify the logic gates and their corresponding Boolean expressions:

1. The gate producing $Y_1$ is an OR gate with inputs $A$ and $B$.
Therefore, $Y_1 = A + B$

2. The gate with inputs $C$ and $D$ is a NAND gate, so its output is $\overline{C \cdot D}$. This output is fed into a NOT gate to produce $Y_2$.
Therefore, $Y_2 = \overline{\overline{C \cdot D}} = C \cdot D$

3. The final gate producing $Y_3$ is a NOR gate with inputs $Y_1$ and $Y_2$.
Therefore, $Y_3 = \overline{Y_1 + Y_2}$

When all inputs are changed to 'zero', i.e., $A = 0, B = 0, C = 0, D = 0$:
$Y_1 = 0 + 0 = 0$
$Y_2 = 0 \cdot 0 = 0$
$Y_3 = \overline{0 + 0} = \overline{0} = 1$

Thus, the outputs $(Y_1, Y_2, Y_3)$ are $(0, 0, 1)$.

Answer: $(0,0,1)$

</details>

---

### Q44. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The truth table for the given logic circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_TSVYqbp-lk29E4JjOjK9YclVYjHGpGj3-cQfOQaMh8.original.fullsize.png"/>
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/N5lFUm-muZBpDZQmaUYWBHkBGNQRJ5ArRruiRyGDum0.original.fullsize.png"/>

**Options:**

- **(A)** P
- **(B)** Q
- **(C)** S
- **(D)** R

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) P**

**Detailed Solution:**

The given logic circuit consists of a NOR gate, an AND gate, and a NAND gate.

The output of the upper NOR gate is $Y_1 = \overline{A + B}$.

The output of the lower AND gate is $Y_2 = A \cdot B$.

These two outputs are fed into a NAND gate. The final output $Y$ is given by:

$Y = \overline{Y_1 \cdot Y_2}$

$Y = \overline{(\overline{A + B}) \cdot (A \cdot B)}$

Using De Morgan's law, $\overline{A + B} = \overline{A} \cdot \overline{B}$. Substituting this into the expression for $Y$:

$Y = \overline{(\overline{A} \cdot \overline{B}) \cdot (A \cdot B)}$

Rearranging the terms, we get:

$Y = \overline{(\overline{A} \cdot A) \cdot (\overline{B} \cdot B)}$

Since $A \cdot \overline{A} = 0$ and $B \cdot \overline{B} = 0$, the expression simplifies to:

$Y = \overline{0 \cdot 0} = \overline{0} = 1$

Thus, the output $Y$ is always $1$ regardless of the input values of $A$ and $B$.

This corresponds to the truth table (P).

Answer: P

</details>

---

### Q45. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The combination of NAND gates is shown in figure (I) and (II). For the given inputs, the outputs in both the combinations are respectively.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ZjcB5K1y85jDzX0sq99wGC2Ol7nHyCYji9n4in4q0UE.original.fullsize_2.png"/>

**Options:**

- **(A)** 0,0
- **(B)** 0,1
- **(C)** 1,0
- **(D)** 1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0,1**

**Detailed Solution:**

For combination (I):

The first two NAND gates have their inputs tied together, so they act as NOT gates.

The input to both the top and bottom NAND gates is $0$. Their outputs will be $\overline{0 \cdot 0} = 1$.

These outputs ($1$ and $1$) are fed as inputs to the third NAND gate.

The final output of combination (I) is $\overline{1 \cdot 1} = 0$.

For combination (II):

The first NAND gate has inputs $1$ and $1$. Its output is $\overline{1 \cdot 1} = 0$.

This output is fed into the second NAND gate, which has its inputs tied together (acting as a NOT gate).

The final output of combination (II) is $\overline{0 \cdot 0} = 1$.

Therefore, the outputs of the combinations are $0$ and $1$ respectively.

Answer: 0,1

</details>

---

### Q46. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Boolean expression for 'XOR' gate $C=(A \oplus B)$ is equal to

**Options:**

- **(A)** $(\mathrm{A} \cdot \mathrm{B})+(\overline{\mathrm{A}} \cdot \overline{\mathrm{B}})$
- **(B)** $\mathrm{A}+(\overline{\mathrm{A}} \cdot \overline{\mathrm{B}})$
- **(C)** $(\mathrm{A} \cdot \mathrm{B})+\overline{\mathrm{B}}$
- **(D)** $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$**

**Detailed Solution:**

The Boolean expression for an XOR gate is given by $C = A \oplus B$.

The output of an XOR gate is high ($1$) only when the inputs are different (one is high and the other is low).

Therefore, the expression can be written as $C = (\overline{A} \cdot B) + (A \cdot \overline{B})$.

Answer: $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$

</details>

---

### Q47. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The logic gate combination circuit shown in the figure performs the logic function of
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/PUOLVktL6iykzivpV9cwRnNEx-HdfsGmZk9kOSZk8ZM.original.fullsize.png"/>

**Options:**

- **(A)** OR gate
- **(B)** NOR gate
- **(C)** XOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) XOR gate**

**Detailed Solution:**

From the given logic circuit diagram:

The inputs to the upper AND gate are $A$ and $\bar{B}$ (from the NOT gate connected to $B$). Thus, the output of the upper AND gate is $A\bar{B}$.

The inputs to the lower AND gate are $\bar{A}$ (from the NOT gate connected to $A$) and $B$. Thus, the output of the lower AND gate is $\bar{A}B$.

These two outputs are fed into an OR gate. The final output $Y$ is the logical sum of these inputs:

$Y = A\bar{B} + \bar{A}B$

This is the standard Boolean expression for an Exclusive-OR (XOR) gate.

Answer: XOR gate

</details>

---

### Q48. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logic circuit in figure is equivalent to
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/oHd1VTo3MWCAsuRp2-hWaw56p1jCytIaRjEvzghJ5OY.original.fullsize.png"/>

**Options:**

- **(A)** OR gate
- **(B)** AND gate
- **(C)** NOR gate
- **(D)** NAND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NAND gate**

**Detailed Solution:**

The given logic circuit consists of three gates connected in series.

The first gate is a NAND gate with inputs $A$ and $B$. Its output is $Y_1 = \overline{A \cdot B}$.

The second gate is a NOR gate with both of its inputs tied together, which makes it act as a NOT gate. Its output is $Y_2 = \overline{Y_1 + Y_1} = \overline{Y_1}$.

The third gate is also a NOT gate. Its output is $Y = \overline{Y_2} = \overline{\overline{Y_1}} = Y_1$.

Since the two NOT gates in series cancel each other out, the final output is simply the output of the first gate, $Y = \overline{A \cdot B}$.

This is the boolean expression for a NAND gate.

Answer: NAND gate

</details>

---

### Q49. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output of following combination is same as that of
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ZbhRSiOLyOVzl2WVKz3Cl50G9SjdrZUKYj02Cg8n5UM.original.fullsize.png">

**Options:**

- **(A)** AND gate
- **(B)** OR gate
- **(C)** NAND gate
- **(D)** NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NOR gate**

**Detailed Solution:**

Considering the truth table for the given circuit,
\begin{array}{|c|c|c|c|c|}
\hline \mathbf{A} & \mathbf{B} & \frac{\mathbf{C}=}{\mathbf{A}+\mathbf{B}} & \frac{\mathbf{D}=}{\mathbf{A}+\mathbf{B}} & \begin{array}{c}
\mathbf{Y}= \\
\mathbf{C}+\mathbf{D}
\end{array} \\
\hline 0 & 0 & 1 & 1 & 1 \\
\hline 0 & 1 & 0 & 0 & 0 \\
\hline 1 & 0 & 0 & 0 & 0 \\
\hline 1 & 1 & 0 & 0 & 0 \\
\hline
\end{array}
$\therefore$ The output of the given combination is same as that of a NOR gate.

</details>

---

### Q50. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Boolean expression for the following combination is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9jKnO2vf2lns_N99kJjfMXqXRM71JeRZ-aARnnRMZc0.original.fullsize.png">

**Options:**

- **(A)** $(\overline{\mathrm{A}+\mathrm{B}})\cdot(\mathrm{A}+\mathrm{B})$
- **(B)** $(\overline{\mathrm{A} \cdot \mathrm{B}})+(\mathrm{A} \cdot \mathrm{B})$
- **(C)** $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$
- **(D)** $(\overline{\mathrm{A}}+\mathrm{B})\cdot(\mathrm{A}+\overline{\mathrm{B}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$**

**Detailed Solution:**

The boolean expression is $(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$

</details>

---

### Q51. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If two inputs of a NAND gate are shorted, the resulting gate is

**Options:**

- **(A)** an OR gate
- **(B)** a AND gate
- **(C)** an NOT gate
- **(D)** a NOR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) an NOT gate**

**Detailed Solution:**

No Solution Available

</details>

---

### Q52. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the following digital logic circuit, the output Y will be ' 1 ' for inputs
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/owy7kGuTv8i8irUYPOOjUiBySz7BRrwFzh8TJGv7mPI.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{A}=0, \mathrm{~B}=0$
- **(B)** $\mathrm{A}=0, \mathrm{~B}=1$
- **(C)** $\mathrm{A}=1, \mathrm{~B}=0$
- **(D)** $\mathrm{A}=1, \mathrm{~B}=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{A}=1, \mathrm{~B}=1$**

**Detailed Solution:**

$\therefore \quad$ There are two NOR gates, one NOT gate, and one NAND gate.
$\therefore \quad$ Output of NAND gate: $\overline{A \cdot B}$
Output of NOT and NOR Gate: $\overline{\overline{\mathrm{A}}+\mathrm{B}}$
Final output: $\overline{(\overline{\mathrm{A} \cdot \mathrm{B}})+(\overline{\overline{\mathrm{A}}+\mathrm{B}})}$
So, the output $\mathrm{Y}$ is 1 only if the input $\mathrm{A}$ and $\mathrm{B}$ is 1.
$$
\begin{aligned}
& \mathrm{A}=1 \\
& \mathrm{~B}=1 \\
& \mathrm{Y}=\overline{\overline{1 \cdot 1}+\overline{1}+1} \\
& \mathrm{Y}=1
\end{aligned}
$$

</details>

---

### Q53. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The logic gate combination circuit shown in the figure performs the logic function of
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/VBQQj5laWoZye-2blGXn6rnSesU8eb6VGWRLFxAtD54.original.fullsize.png">

**Options:**

- **(A)** AND gate
- **(B)** NAND gate
- **(C)** OR gate
- **(D)** The gate is not operational

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The gate is not operational**

**Detailed Solution:**

[Note: The gate at the output in the circuit is AND gate. It requires minimum two inputs. As, there is only one input the gate is not operational.]

</details>

---

### Q54. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The following logic gate combination is equivalent to
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3I3fdjcN6uSpyr6T6f6PwEtTCx08l6AzNClvi_y0R2g.original.fullsize.png">

**Options:**

- **(A)** NAND gate
- **(B)** OR gate
- **(C)** XOR gate
- **(D)** NOT gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) XOR gate**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/162_FPqL6zm4dmSWurxjhky7MibMzOXFcv397OfVT78.original.fullsize.png">


$$
\begin{aligned}
& \therefore \quad Y=\overline{A \cdot B} \cdot(A+B) \\
& \therefore \quad Y=(\bar{A}+\bar{B}) \cdot(A+B) \quad \cdots(\because \bar{A} \cdot \bar{B}=\bar{A}+\bar{B}) \\
& \therefore \quad Y=\bar{A} \cdot B+\bar{B} \cdot A \\
& \therefore \quad Y=A \cdot \bar{B}+B \cdot \bar{c}
\end{aligned}
$$
This représents XOR gate,

</details>

---

### Q55. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the digital circuit the inputs are as shown in figure. The Boolean expression for output $\mathrm{Y}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/LHSKKcNEQmTkuRLXaaQdUYv6C8YGnvk1irS24ivkqb4.original.fullsize.png">

**Options:**

- **(A)** $\overline{\mathrm{A}+\mathrm{B}}+\overline{\mathrm{C}}$
- **(B)** $\overline{\mathrm{A} \cdot \mathrm{B}} \cdot \overline{\mathrm{C}}$
- **(C)** $\overline{\mathrm{A} \cdot \mathrm{B}}+\overline{\mathrm{C}}$
- **(D)** $\overline{\mathrm{A}+\mathrm{B}} \cdot \overline{\mathrm{C}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\overline{\mathrm{A} \cdot \mathrm{B}}+\overline{\mathrm{C}}$**

**Detailed Solution:**

In the given circuit, there is AND, NOR and a NOT gate.
Output of AND gate: $\overline{\mathrm{A} \cdot \mathrm{B}}$
Output of NOT gate: $\overline{\mathrm{C}}$
$\therefore \quad$ The boolean expression will be:
$\overline{\mathrm{A} \cdot \mathrm{B}}+\overline{\mathrm{C}}$

</details>

---

### Q56. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the case of NAND gate, if A and B are the inputs and $Y$ is the output then

**Options:**

- **(A)** $\mathrm{Y}=\mathrm{A} \cdot \mathrm{B}$
- **(B)** $Y=\overrightarrow{A-B}$
- **(C)** $Y=\overline{A+B}$
- **(D)** $\mathrm{Y}=\overline{\mathrm{A} \cdot \mathrm{B}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{Y}=\overline{\mathrm{A} \cdot \mathrm{B}}$**

**Detailed Solution:**

No Solution Available

</details>

---

### Q57. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output of an 'OR' gate is connected to both the inputs of a 'NAND' gate. The combination will serve as

**Options:**

- **(A)** OR gate
- **(B)** NOT gate
- **(C)** NOR gate
- **(D)** AND gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NOR gate**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9nL61AcffcEnB3x4p2iKkybIpuCRw2QkYh_A02qkylg.original.fullsize.png">

\begin{array}{|c|c|}
\hline Output of OR gate & Output of NAND gate \\
\hline 0 & 1 \\
\hline 1 & 0 \\
\hline 1 & 0 \\
\hline 1 & 0 \\
\hline
\end{array}
Truth table of a NOR gate<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/vGHIli9xfW0IsYkMxSlcZCWJG7nYejouLyK0CNx_23U.original.fullsize.png">

The output matches with that of a NOR gate.
$\therefore \quad$ The combination represents a NOR gate.

</details>

---

### Q58. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

To obtain the truth-table shown, from the following logic circuit, the gate $\mathrm{G}$ should be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/7m4PP_F5wCKGRHy602wRw-9CSWGSCb03fLKmHPgIxFs.original.fullsize.png">

\begin{array}{|l|l|l|}
\hline \mathrm{A} & \mathrm{B} & \mathrm{Y} \\
\hline 0 & 0 & 1 \\
\hline 0 & 1 & 0 \\
\hline 1 & 0 & 1 \\
\hline 1 & 1 & 1 \\
\hline
\end{array}

**Options:**

- **(A)** AND
- **(B)** NAND
- **(C)** OR
- **(D)** NOR

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) NOR**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6ByWC5S__evvY-0wS5nzzco0Bp-Dcc_IcB5_5GOk6f8.original.fullsize.png">

The truth table for given configuration is as shown below.
\begin{array}{|c|c|c|c|c|}
\hline Case & \mathbf{A} & \mathbf{B} & \mathbf{C} & \mathbf{A}+\mathbf{C}=\mathrm{Y} \\
\hline I & 0 & 0 & \mathrm{C}_1 & 0+\mathrm{C}_1=1 \\
\hline II & 0 & 1 & \mathrm{C}_2 & 0+\mathrm{C}_2=0 \\
\hline III & 1 & 0 & \mathrm{C}_3 & 1+\mathrm{C}_3=1 \\
\hline IV & 1 & 1 & \mathrm{C}_4 & 1+\mathrm{C}_4=1 \\
\hline
\end{array}
Considering case (I), in order to have output $\mathrm{Y})$ as $1, \mathrm{C}_1$ has to be 1 . For input values, $\mathrm{A}=0$ and $\mathrm{B}=0$, if $\mathrm{C}_1$ is to be high, the gate $\mathrm{G}$ could be either NAND or NOR.
Considering case (II), in order to have output (Y) as $0, C_2$ has to be 0 . For input values, $\mathrm{A}=0$ and $\mathrm{B}=1$. If $\mathrm{C}_2$ is to be 0 , the gate must be NOR.

</details>

---

### Q59. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

To get the truth table shown, from the following logic circuit, the Gate $\mathrm{G}$ should be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bH2q29xSFaWognqA9VhF1tY4buSIYF8Ng3Nt_pF97RU.original.fullsize.png">

\begin{array}{|c|c|c|}
\hline \mathrm{A} & \mathrm{B} & \mathrm{Y} \\
\hline 0 & 0 & 0 \\
\hline 0 & 1 & 0 \\
\hline 1 & 0 & 1 \\
\hline 1 & 1 & 1 \\
\hline
\end{array}

**Options:**

- **(A)** OR
- **(B)** AND
- **(C)** NOR
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) AND**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/kIpesruhowOgvH0Rge_-_Wb1lrcPQNGi82faL9sVZKE.original.fullsize.png">

Truth table for $\mathrm{Y}$, with the possible values of $\mathrm{C}$ is,
\begin{array}{|c|c|c|}
\hline \mathbf{A} & \mathbf{C} & \mathbf{Y} \\
\hline 0 & 0 & 0 \\
\hline 0 & 0 & 0 \\
\hline 1 & 0,1 & 1 \\
\hline 1 & 0,1 & 1 \\
\hline
\end{array}
For gate $\mathrm{G}$
\begin{array}{|c|c|c|c|}
\hline & A & B & C \\
\hline (I) & 0 & 0 & 0 \\
\hline (II) & 0 & 1 & 0 \\
\hline (III) & 1 & 0 & 0,1 \\
\hline (IV) & 1 & 1 & 0,1 \\
\hline
\end{array}
$\mathrm{G}$ is not a NOT gate as NOT gate takes only one input. (II) indicates $\mathrm{G}$ is not a OR gate as OR gate would give high output for the inputs in (II). Also, (II) indicates it is not a XOR gate as XOR would also give high output for inputs in (II). Hence, the given truth table is satisfied only by AND gate.

</details>

---

### Q60. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The combination of logic gates shown below becomes
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/aiyHUigSTCOv6WAhPwR4QRwdpkaxwv4k6ooPR0cqoig.original.fullsize.png">

**Options:**

- **(A)** X-OR gate
- **(B)** NAND gate
- **(C)** NOR gate
- **(D)** OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) OR gate**

**Detailed Solution:**

This combination is a OR gate (Logical)

</details>

---

### Q61. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Tz5H2AkpI4iKzAduSWJoBNsUojJtte4MkKGyo3qmj70.original.fullsize.png">
The values taken by $C, D, E, F$ are respectively

**Options:**

- **(A)** $0,1,0,0$
- **(B)** $1,0,1,1$
- **(C)** $0,1,0,1$
- **(D)** $1,1,1,0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1,1,1,0$**

**Detailed Solution:**

The Boolean expression for NAND gate is:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bd_goM71-6c2CHkeHQ4VL2bJTKb6PO30RfkLUgMzVgk.original.fullsize.png">

</details>

---

### Q62. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The truth-table for the two-input Ex-OR gate is (A, B are the inputs, $\mathrm{Y}$ is the output).
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/wlhTw5Wgg3mJoyVVbuq5TL3My1ez_432UoVjxkta0Mc.original.fullsize.png">

**Options:**

- **(A)** P
- **(B)** Q
- **(C)** R
- **(D)** S

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) S**

**Detailed Solution:**

The Boolean expression for Exclusive-OR gate is as follows:
$Y=(A \oplus B)=\bar{A} \cdot B+A \cdot \bar{B}$"ō"
The output of an Exclusive-OR gate ONLY goes "HIGH" when its two input terminals are at "DIFFERENT" logic levels with respect to each other.
Therefore, option table S is correct.

</details>

---

### Q63. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The Boolean expression for two-input Ex-OR gate is (A, B are inputs, Y is output)

**Options:**

- **(A)** $Y=(\bar{A}+B) \cdot(A+\bar{B})$
- **(B)** $\mathrm{Y}=(\mathrm{A}, \mathrm{B})+(\overline{\mathrm{A}}+\overline{\mathrm{B}})$
- **(C)** $\mathrm{Y}=(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$
- **(D)** $\mathrm{Y}=(\mathrm{A} \cdot \mathrm{B})+(\overline{\mathrm{A}}+\mathrm{B})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{Y}=(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$**

**Detailed Solution:**

Truth table
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/drZCKuSgSHhbZQ45NTFsuu6WZ2cUHM0_PJxB_VLPWt4.original.fullsize.png">

Output equation: $\mathrm{Y}=\mathrm{A} \oplus \mathrm{B}=(\overline{\mathrm{A}} \cdot \mathrm{B})+(\mathrm{A} \cdot \overline{\mathrm{B}})$
Key points to remember:
(1) the output is low when both the inputs are the same
(2) the output is high when both the inputs are different

</details>

---

### Q64. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A combination of logic gates is as shown in figure. ' $P$ ', ' $Q$ ', ' $R$ ' and ' $\mathrm{S}$ ' are the inputs and ' $\mathrm{X}$ ', ' $\mathrm{Y}$ ' and ' $\mathrm{Z}$ ' are outputs. When inputs $\mathrm{P}$ and $\mathrm{R}$ are 'low' and $\mathrm{Q}$ and $\mathrm{S}$ are 'high', the outputs $\mathrm{X}, \mathrm{Y}$ and $\mathrm{Z}$ are respectively
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/TKqqz9vkFV16jHUZhq_q5eiHFCtudyNew1ttjGu3hEs.original.fullsize.png">

**Options:**

- **(A)** 0,1,0
- **(B)** 0,1,1
- **(C)** 1,0,0
- **(D)** 1,1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0,1,0**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RIJfK8FD1VzUxWo_8bGVyPi5Lebm8FAfd59awwAquA0.original.fullsize.png">

$(\mathrm{x}, \mathrm{y}, \mathrm{z})=(0,1,0)$

</details>

---

### Q65. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the following combination of logic gates, when all the three inputs $A$, $B$ and $C$ are first 'high' and then 'low', the output $Y$ will be respectively.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/B9MO3Voo7duf_HMbQ9cXyJFSsLEFnHsMvpNZyqYIdJ4.original.fullsize.png">

**Options:**

- **(A)** 0,0
- **(B)** 0,1
- **(C)** 1,0
- **(D)** 1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0,1**

**Detailed Solution:**

Let inputs $A, B$ and $C$ are given to the circuit.
Gate-I is AND gate while gate-II is NAND gate.
Output $Y=\overline{(A . B . C)}$
When $A=1, B=1, C=1$, then
$Y=\overline{(1 \cdot 1) \cdot 1}=\overline{1 \cdot 1}=\overline{1}=0$
When $A=0, B=0, C=0$, then
$Y=\overline{(0.0) \cdot 0}=\overline{0.0}=1$

</details>

---

### Q66. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

To get an output 1 from the logic circuit shown in the figure, the input can be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/WWq3arl7C7BQlgrDFjj4UyQwb0fQrrk8JiLWbGbqCbg.original.fullsize.png">

**Options:**

- **(A)** A=1, B=0, C=0
- **(B)** A=1, B=0, C=1
- **(C)** A=1, B=1, C=0
- **(D)** A=0, B=0, C=1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) A=1, B=1, C=0**

**Detailed Solution:**

To get final output as 1 , the output of OR gate must be 1 and $C$ must be 1 . So, $A=1, B=1, C=0$

</details>

---

### Q67. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

What will be the input of A and B for the Boolean expression $\overline{(\mathrm{A}+\mathrm{B}) \cdot(\mathrm{A} \cdot \mathrm{B})}=1$

**Options:**

- **(A)** 1,0
- **(B)** 0,0
- **(C)** 0,1
- **(D)** 1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0,0**

**Detailed Solution:**

$\overline{(A+B) \cdot(A \cdot B)}=1$
Answer can be formed by trial and error.
$\begin{aligned} & (0,0) \Rightarrow \mathrm{A}=0, \mathrm{~B}=0 \\ & \overline{(0+0) \cdot(0 \cdot 0)}=(\overline{0}) \cdot(\overline{0})=1 \cdot 1=1\end{aligned}$

</details>

---

### Q68. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The output of OR gate is ' 1 '

**Options:**

- **(A)** if either input is 'zero'
- **(B)** Only if both inputs are 'zero'
- **(C)** if either or both inputs are ' 1 '
- **(D)** Only if both inputs are ' 1 '

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) if either or both inputs are ' 1 '**

**Detailed Solution:**

Concept based.
For Or gate if either of the inputs are one then output is one. Also if both the inputs are one then also the output is one.

</details>

---

### Q69. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

What is the output $\mathrm{Y}$ in the following circuit, when all the three inputs $A$ $, B, C$ are firs 0 then 1 ?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/V595uvIUNE2i59_GaYBP-s36-pmy9KrBvOaRMPzmNzE.original.fullsize.png">

**Options:**

- **(A)** 0,0
- **(B)** 0,1
- **(C)** 1,1
- **(D)** 1,0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1,0**

**Detailed Solution:**

Boolean expression for the gate combination is given by,
$Y=\overline{(A \cdot B) \cdot C}=\overline{A B C}$
If $A=B=C=0$ then $Y_0=\overline{0}=1$
If $A=B=C=0$ then $Y_1=\overline{1}=0$

</details>

---

### Q70. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Which one of the following logic gates is called as Universal gate?

**Options:**

- **(A)** NOR
- **(B)** NOT
- **(C)** Ex-OR
- **(D)** AND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) NOR**

**Detailed Solution:**

NOR gate is considered universal gate. As other gates can be formed from this gate.

</details>

---

### Q71. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a given combination of logic gates, the inputs $A, B$ and $C$ are as follows. $A=B=C=0$ and $A=B=1, C=0$ then the logic states of output $D$ are respectively
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/nafBmeJgGAeAYGoogUib3v8iIe1ACdRRPmKWNSU2VJM.original.fullsize.png">

**Options:**

- **(A)** 0,0
- **(B)** 0,1
- **(C)** 1,0
- **(D)** 1,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1,1**

**Detailed Solution:**

The output $\mathrm{D}$ for the given combination:
$D=(A+\bar{B}) \cdot C=(A+\bar{B})+C$
If $A=B=C=0$ then $D=(0+\overline{0})+\overline{0}=\overline{0}+\overline{0}=1+1=1$
if $=B=1, C=0$ then $D=(1+\overline{1})+\overline{0}=\overline{1}+\overline{0}=0+1=1$

</details>

---

### Q72. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The output of a 'NAND' gate is shown in the truth-table (A and B are inputs, $\mathrm{Y}$ is output)
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/qSW2kJA0zAAWZqUKPB8MbVZlK5g4HTeqo-Vjv48MqXo.original.fullsize.png">

**Options:**

- **(A)** Q
- **(B)** R
- **(C)** S
- **(D)** P

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) S**

**Detailed Solution:**

Concept based.
A NAND gate (NOT-AND) is a logic gate which produces an output which is false only if all its inputs are true; thus its output is complement to that of an AND gate.

</details>

---

### Q73. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the logic circuit diagram, A, B and C are the inputs, $\mathrm{Y}$ is the output. The output $\mathrm{Y}$ is ' $\mathrm{HIGH}$ '
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/BySGnDEmanuFZOrHkflz0BnBUF2OgORMh3bfi3UPR14.original.fullsize.png">

**Options:**

- **(A)** when $\mathrm{A}=1, \mathrm{~B}=0, \mathrm{C}=1$
- **(B)** for all the input ' $\mathrm{HIGH}$ '
- **(C)** for all the inputs 'LOW'
- **(D)** when $A=1, B=0, C=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) when $A=1, B=0, C=0$**

**Detailed Solution:**

The output Y is
$$
\begin{aligned}
& Y=\overline{(A+B)} \cdot C \\
& B=0, C=0 \text { and } A=1 \text { should give } Y=1 .
\end{aligned}
$$

</details>

---

### Q74. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The output Y when all the three inputs A, B, C are first low and then high will be
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/tPQrJzAPPTwuyONgN3v7yuSVwpD_2SQgvcwuK__wfes.original.fullsize.png">

**Options:**

- **(A)** 1,0
- **(B)** 1,1
- **(C)** 0,0
- **(D)** 0,1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1,0**

**Detailed Solution:**

The correct option is (A).
See the figure below:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/sDL4cnxdLsAwNNUuco1pWlOUNCp1vqEA0x7DVCFrwGU.original.fullsize.png">
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/CPZatNyBFAno4HfYaCqa1s2j1CWcq8o6I7hoXZOEr_0.original.fullsize.png">
Therefore, answer is $(1,0)$.

</details>

---

### Q75. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a two input AND gate, the four entries are shown in the truth table. Identify the correct ones out of these (A, B = input, $\mathrm{Y}=$ output)
\begin{array}{|l|l|l|l|}
\hline Entry & \mathrm{A} & \mathrm{B} & \mathrm{Y} \\
\hline 1 & 0 & 1 & 0 \\
\hline 2 & 1 & 0 & 0 \\
\hline 3 & 1 & 1 & 1 \\
\hline 4 & 0 & 0 & 1 \\
\hline
\end{array}

**Options:**

- **(A)** 1 and 2 only
- **(B)** 1,2 and 3 only
- **(C)** 1, 3 and 4 only
- **(D)** 2 , and 4 only

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1,2 and 3 only**

**Detailed Solution:**

Conceptual

</details>

---

### Q76. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The resultant gate and its Boolean expression in the given circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/KM5pWitafuaTmPEbvjVB52fcQwNFrRnaiUhvhneXoWA.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{NOR}, \overline{\mathrm{A}+\mathrm{B}}$
- **(B)** $AND, A.B$
- **(C)** $\text { OR, A } + B$
- **(D)** $NAND, \overline{\mathrm{AB}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $AND, A.B$**

**Detailed Solution:**

Truth table:
\begin{array}{|l|l|l|l|l|}
\hline A & B & C & D & Y \\
\hline 0 & 0 & 1 & 1 & 0 \\
\hline 0 & 1 & 1 & 0 & 0 \\
\hline 1 & 0 & 0 & 1 & 0 \\
\hline 1 & 1 & 0 & 0 & 1 \\
\hline
\end{array}
This is truth table of AND gate. $\therefore \mathrm{Y}=\mathrm{A} \cdot \mathrm{B}$

</details>

---

### Q77. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The Boolean equation for the circuit given in the figure is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/81ade2e1-b3ca-4d4c-b68a-3b9f4dba71b5-image.png" style="width: 250px; height: 113px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>A</mi><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow><mo>&#175;</mo></mover></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi>B</mi><mo>&#175;</mo></mover></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/a281616f-cff5-40d4-b0ce-ea4e60a37153-image.png" style="width: 300px; height: 160px;" /></p><p>In the above diagram, we have the combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOT</mi></math> gate and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math> gate.</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>NOT</mi></math> gate</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo mathvariant="italic">=</mo><mover><mi>A</mi><mo mathvariant="italic">&#175;</mo></mover><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">&#160;</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">.</mo><mo mathvariant="italic">.</mo><mfenced><mn>1</mn></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>OR</mi></math> gate</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mi>X</mi><mo>+</mo><mi>B</mi><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mi>Y</mi><mo>=</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced close="]" open="["><mrow><mtext>Using</mtext><mo>&#160;</mo><mfenced><mn>1</mn></mfenced></mrow></mfenced></math></p><p>Hence, the output expression of the given arrangement of gates is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mover><mi>A</mi><mo>&#175;</mo></mover><mo>+</mo><mi>B</mi></mrow></mfenced></math>. </p></blockquote>

</details>

---

### Q78. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the output of the following logic circuit to be ' 1 ', the values of inputs A and B should be respectively
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ltuo-c7wjWSM4lV2YUSWmXBIQvhyzux7qsrzF-Um4JY.original.fullsize.png">

**Options:**

- **(A)** 0 and 1
- **(B)** 0 and 0
- **(C)** 1 and 1
- **(D)** 1 and 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0 and 0**

**Detailed Solution:**

For output $Y$ to be ' 1 ', the output of the OR gate should be ' 0 '. This is possible only when both the inputs are zero.

</details>

---

### Q79. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following gates will give an output ' 1 ' for the given inputs?
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/4JrQP5US10igjv38foxX0mnCY6rRVzT4NCETIN-3t4o.original.fullsize.png">

**Options:**

- **(A)** II and III
- **(B)** I and IV
- **(C)** I and III
- **(D)** II and IV

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) II and IV**

**Detailed Solution:**

(I) NAND gate gives output ' 0 ' when inputs are 1,1
(II) NOR gate gives output ' 1 ' when inputs are 0, 0
(III) NAND gate gives output ' 1 ' when inputs are 0,1
(IV) EX-OR gate gives output ' 0 ' when inputs are 1,0
$\therefore$ Ans. II and III

</details>

---

### Q80. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A logic gate which gives output' HIGH' only when its two input terminals are at different logic levels with respect to each other is

**Options:**

- **(A)** NOR gate
- **(B)** OR gate
- **(C)** AND gate
- **(D)** X-OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) X-OR gate**

**Detailed Solution:**

$\mathrm{X}-\mathrm{OR}$ gate give 'High' Output only when one input is high and the other is low.

</details>

---

### Q81. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Combination of NAND gates is shown in the figure. It is equivalent to which gate:
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/5PORl0MPh-AwTk7kJt_4KkWDSQacnK2cExMTF_qYHlk.original.fullsize.png">

**Options:**

- **(A)** NOR gate
- **(B)** AND gate
- **(C)** OR gate
- **(D)** X-OR gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) OR gate**

**Detailed Solution:**

The two NAND gates whose two inputs are joined together behave like NOT gates. The truth table can be written as
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/--dYmX09pNfrTZmfLa9B3E1UticRkFkjoAcRbu5BSbQ.original.fullsize.png">

We see that the output $y$ is ' 1 ' if $A$ or $B$ or both are ' 1 '. Hence it behaves as OR gate.

</details>

---

### Q82. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two different logic gates giving output ' 0 ' for the inputs $(0,1)$ and then for $(1,0)$ are

**Options:**

- **(A)** 'AND', 'NAND'
- **(B)** 'NAND', 'NOR'
- **(C)** ' $\mathrm{OR}$ ', 'AND'
- **(D)** 'NOR', 'AND'

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 'NOR', 'AND'**

**Detailed Solution:**

In AND gate, output is 1 only if both the inputs are ' 1 '. Hence output will be ' 0 ' for $(0,1)$ and $(1,0)$
In NOR gate, output is ' 1 ' only if both the inputs are ' 0 '. Hence output will be ' 0 ' for $(0,1)$ and $(1,0)$

</details>

---

### Q83. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The output of an ' $\mathrm{OR}$ ' gate is 'one'

**Options:**

- **(A)** only when both inputs are 'one'
- **(B)** only when both inputs are 'zero'
- **(C)** only when either input is 'zero'
- **(D)** if either or both inputs are 'one'

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) if either or both inputs are 'one'**

**Detailed Solution:**

Theory based

</details>

---

### Q84. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For which logic gate the following statement is true? The output is high if and only if all inputs are high.

**Options:**

- **(A)** AND
- **(B)** OR
- **(C)** NOR
- **(D)** NAND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) AND**

**Detailed Solution:**

Theory question

</details>

---

### Q85. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The resultant gate and its Boolean expression for the given circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Gm4GhGeeOPBuwaxMhCxG6EZEnstdPfeKKLBqK0MnZGI.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{OR}, \mathrm{A}+\mathrm{B}$
- **(B)** $\mathrm{NAND}, \overline{\mathrm{A} \cdot \mathrm{B}}$
- **(C)** $\mathrm{NOR}, \overline{\mathrm{A}+\mathrm{B}}$
- **(D)** $\mathrm{AND}, \mathrm{A} \cdot \mathrm{B}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{AND}, \mathrm{A} \cdot \mathrm{B}$**

**Detailed Solution:**

No Solution

</details>

---

### Q86. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The resultant gate and its Boolean expression for the given circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Gz7kDoC97j5Zkjya7NZk2Pyl-KKGkYdVCY0NUQ9APy4.original.fullsize.png">

**Options:**

- **(A)** OR, $A+B$
- **(B)** $\mathrm{NOR}, \overline{A+B}$
- **(C)** $\quad \mathrm{NAND}, \overline{A \cdot B}$
- **(D)** $\quad A N D, A \cdot B$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) OR, $A+B$**

**Detailed Solution:**

Here a NOR gate is followed by a NOT gate which gives an OR gate which has Boolean expression $A+B$

</details>

---

### Q87. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

How many NAND gates are required to form an AND gate?

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Two NAND gates are required as follow
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/_sRhkvImg8fxiPxxIlhvgkMEehMQpZ9Oc9woqjkSQvA.original.fullsize.png">

$$
Y=\overline{\overline{A B}} \cdot \overline{A B}=A B
$$

</details>

---

### Q88. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

When the two inputs of a NAND gate are shorted, the resulting gate is

**Options:**

- **(A)** $\mathrm{NOR}$
- **(B)** $\mathrm{OR}$
- **(C)** NOT
- **(D)** AND

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) NOT**

**Detailed Solution:**

The circuit diagram of a NAND gate when its two inputs are shorted, is given as NAND $=$ AND $+$ NOT
The truth table of this logic gate is given as
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rwIbOIFWRJa2HmaeDDRkdaDwSfrC4VdbiKhkQXnrA7U.original.fullsize.png">

\begin{array}{c|c|c}
A & Y & \bar{Y} \\
\hline 0 & 0 & 1 \\
\hline 1 & 1 & 0
\end{array}
Hence, if the input is zero then output is 1 and when input is 1 than output is zero. So, the resulting gate is NOT gate.

</details>

---

