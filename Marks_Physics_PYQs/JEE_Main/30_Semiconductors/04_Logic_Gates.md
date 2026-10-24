# JEE Main Physics - Semiconductors

## Topic 4: Logic Gates

**Total Questions:** 1

---

### Q1. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two p-n junction diodes $D_{1}$ and $D_{2}$ are connected as shown in figure. $A$ and $B$ are input signals and $C$ is the output. The given circuit will function as a $\_\_\_\_$. 
 <img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_q_31_1.png">

**Options:**

- **(A)** NOR Gate
- **(B)** NAND Gate
- **(C)** OR Gate
- **(D)** AND Gate

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) AND Gate**

**Detailed Solution:**

If $A = 0$ and $B = 0$: Both diodes are forward biased. The potential at $C$ is pulled down to approximately $0V$ (logic 0).
If $A = 0$ and $B = 1$: Diode $D_1$ is forward biased, pulling the potential at $C$ down to $0V$ (logic 0). Diode $D_2$ is reverse biased.
If $A = 1$ and $B = 0$: Diode $D_2$ is forward biased, pulling the potential at $C$ down to $0V$ (logic 0). Diode $D_1$ is reverse biased.
If $A = 1$ and $B = 1$: Both diodes are reverse biased. No current flows through the resistor $R$, so the potential at $C$ remains at $V_{dc} = 5V$ (logic 1).
The truth table is:
<table style='width:auto;text-align:center;border-collapse:collapse;' border='1'><tr><th> A </th><th> B </th><th> C </th></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>
This truth table corresponds to the AND gate logic operation $C = A \cdot B$.
Therefore, the circuit functions as an AND gate.

</details>

---

