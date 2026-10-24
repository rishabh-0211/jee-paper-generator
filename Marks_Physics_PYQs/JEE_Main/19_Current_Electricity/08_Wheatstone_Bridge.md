# JEE Main Physics - Current Electricity

## Topic 8: Wheatstone Bridge

**Total Questions:** 35

---

### Q1. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A Wheatstone bridge is initially at room temperature and all arms of the bridge have same value of resistances $\left(R_{1}=R_{2}=R_{3}=R_{4}\right)$. When $R_{3}$ resistance is heated to some temperature, its resistance value has gone up by $10 \%$. The potential difference $\left(V_{a}-V_{b}\right)$ (after $R_{3}$ is heated) is $\_\_\_\_$ V. 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S2_q_38_1.png">

**Options:**

- **(A)** 1.05
- **(B)** 0.95
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.95**

**Detailed Solution:**

Initially, the Wheatstone bridge is balanced with $R_1 = R_2 = R_3 = R_4 = R$.
Since the bridge is balanced, the potential difference across the bridge is zero: $V_a - V_b = 0$ V.
When $R_3$ is heated and its resistance increases by 10%: $R_3' = 1.1R$
The voltage at node $a$ (between $R_1$ and $R_2$): $V_a = 40 \times \frac{R_2}{R_1 + R_2} = 40 \times \frac{R}{R + R} = 40 \times \frac{1}{2} = 20$ V
The voltage at node $b$ (between $R_3'$ and $R_4$): $V_b = 40 \times \frac{R_4}{R_3' + R_4} = 40 \times \frac{R}{1.1R + R} = 40 \times \frac{1}{2.1} \approx 19.05$ V
Therefore: $V_a - V_b = 20 - 19.05 = 0.95$ V

</details>

---

### Q2. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `3`

The equivalent resistance between the points $A$ and $B$ in the following circuit is $\frac{x}{5} \Omega$. The value of $x$ is $\_\_\_\_$. 
 <img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/28S1_q_46_1.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

Using Kirchhoff's laws on the bridge circuit with resistances $6\Omega, 3\Omega, 3\Omega, 3\Omega, 6\Omega$ and applying a 1V test voltage:

From the loop equation:
$6i_1 + 3(2i_1 - i) = 3(i - i_1)$

$15i_1 = 6i \Rightarrow i_1 = \frac{2}{5}i$ ...(1)

From the second loop:
$3(i - i_1) + 6i_1 = 1$
$3i + 3i_1 = 1$

$\left(3 + \frac{6}{5}\right)i = 1$

$i = \frac{5}{21}$ A $= \frac{1V}{R_{eq}}$

$R_{eq} = \frac{21}{5} = 4.2 \ \Omega$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 2)

*Type:* `numerical` | *Level:* `2`

In a meter bridge experiment to determine the value of unknown resistance, first the resistances $2 \Omega$ and $3 \Omega$ are connected in the left and right gaps of the bridge and the null point is obtained at a distance $l \mathrm{~cm}$ from the left. Now when an unknown resistance $x \Omega$ is connected in parallel to $3 \Omega$ resistance, the null point is shifted by 10 cm to the right of wire. The value of unknown resistance $x$ is $\_\_\_\_$ $\Omega$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Meter bridge null point condition: $\frac{R_1}{R_2} = \frac{l}{100-l}$
Initial: $R_1 = 2Ω$, $R_2 = 3Ω$, null at $l$ cm
$\frac{2}{3} = \frac{l}{100-l}$ gives $2(100-l) = 3l$, so $l = 40$ cm
When $xΩ$ connected in parallel with $3Ω$: $R_2' = \frac{3x}{3+x}Ω$
New null point at $(40+10) = 50$ cm from left:
$\frac{2}{R_2'} = \frac{50}{50} = 1$
$\frac{2(3+x)}{3x} = 1$ gives $6 + 2x = 3x$
$x = 6Ω$

</details>

---

### Q4. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two resistors $2 \Omega$ and $3 \Omega$ are connected in the gaps of bridge as shown in figure. The null point is obtained with the contact of jockey at some point on wire $X Y$. When an unknown resistor is connected in parallel with $3 \Omega$ resistor, the null point is shifted by 22.5 cm toward $Y$. The resistance of unknown resistor is $\_\_\_\_$ $\Omega$. 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S1_q_31_1.png">

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

In a Wheatstone bridge with 2Ω and 3Ω, the null point is found when $\frac{R_1}{R_2} = \frac{l}{L-l}$.
Initial balance: $\frac{2}{3} = \frac{l_1}{L-l_1}$ gives $l_1 = \frac{2L}{5}$.
For standard wire length $L = 100$ cm, $l_1 = 40$ cm.
When unknown resistance $R$ is connected in parallel with 3Ω, equivalent resistance becomes $\frac{3R}{3+R}$.
New null point: $\frac{2}{\frac{3R}{3+R}} = \frac{l_2}{L-l_2}$, which simplifies to $\frac{2(3+R)}{3R} = \frac{l_2}{L-l_2}$.
Null point shifts 22.5 cm toward Y: $l_2 = 40 + 22.5 = 62.5$ cm.
Substituting: $\frac{2(3+R)}{3R} = \frac{62.5}{37.5} = \frac{5}{3}$
$6(3+R) = 15R \Rightarrow 18 = 9R \Rightarrow R = 2$ Ω

</details>

---

### Q5. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A meter bridge with two resistances $R_{1}$ and $R_{2}$ as shown in figure was balanced (null point) at 40 cm from the point $P$. The null point changed to 50 cm from the point $P$, when $16 \Omega$ resistance is connected in parallel to $R_{2}$. The values of resistances $R_{1}$ and $R_{2}$ are $\_\_\_\_$.
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_q_31_1.png">

**Options:**

- **(A)** $R_{2}=4 \Omega, R_{1}=\frac{4}{3} \Omega$
- **(B)** $R_{2}=16 \Omega, R_{1}=\frac{16}{3} \Omega$
- **(C)** $R_{2}=12 \Omega, R_{1}=\frac{12}{3} \Omega$
- **(D)** $R_{2}=8 \Omega, R_{1}=\frac{16}{3} \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $R_{2}=8 \Omega, R_{1}=\frac{16}{3} \Omega$**

**Detailed Solution:**

Initial balance at 40 cm: $\frac{R_1}{R_2} = \frac{40}{60} = \frac{2}{3}$ ...(i)
With $16\,\Omega$ parallel to $R_2$, null point at 50 cm:
$\frac{R_1}{\frac{16R_2}{16+R_2}} = \frac{50}{50} = 1 \Rightarrow R_1 = \frac{16R_2}{16+R_2}$ ...(ii)
From (i): $R_1 = \frac{2}{3}R_2$.
Substituting in (ii): $\frac{2}{3}R_2 = \frac{16R_2}{16+R_2}$.
$\frac{2}{3} = \frac{16}{16+R_2} \Rightarrow 2(16+R_2) = 48 \Rightarrow R_2 = 8\,\Omega$.
$R_1 = \frac{16}{3}\,\Omega$.

</details>

---

### Q6. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `2`

The heat generated in 1 minute between points $A$ and $B$ in the given circuit, when a battery of 9 V with internal resistance of $1 \Omega$ is connected across these points is $\_\_\_\_$ J. 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S1_q_49_1.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1080**

**Detailed Solution:**

Wheatstone bridge with P = 1Ω, Q = 2Ω, R = 2Ω, S = 4Ω
$\frac{P}{Q} = \frac{R}{S} = \frac{1}{2}$ → Bridge is balanced, no current through middle 1Ω.
$R_{AB}$: Upper (3Ω) and Lower (6Ω) in parallel = $\frac{3 \times 6}{9} = 2Ω$
Total resistance = 1 + 2 = 3Ω
Current $I = \frac{9}{3} = 3$ A
Power between A and B: $P = I^2 R_{AB} = 9 \times 2 = 18$ W
Heat in 1 min = $18 \times 60 = 1080$ J

</details>

---

### Q7. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of resistance $R$ is bent into a triangular pyramid as shown in figure with each segment having same length. The resistance between points $A$ and $B$ is $R / n$. The value of $n$ is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/HsWmDbUUe_Pd9cZYFulcp1g80hj77OA34OGdvg5aHaw.original.fullsize.png"/>

**Options:**

- **(A)** 16
- **(B)** 14
- **(C)** 10
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 12**

**Detailed Solution:**

As $r=\frac{R}{6}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ugV3KH7Irs6GVJ4RACoUGQTmHQ_MQfXG5dAG1Pr2m4.original.fullsize.png"/>
(As balanced wheat stone bridge is formed) Now, Equivalent resistance between A and B can be written as
$\frac{1}{\mathrm{R}_{\mathrm{AB}}}=\frac{1}{2 \mathrm{r}}+\frac{1}{2 \mathrm{r}}+\frac{1}{\mathrm{r}}=\frac{2}{\mathrm{r}}$
$\mathrm{R}_{\mathrm{AB}}=\frac{\mathrm{R}}{12}$

</details>

---

### Q8. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of unknown resistance $(x)$ for which the potential difference between $B$ and $D$ will be zero in the arrangement shown, is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OmPEbB895N08rB0sbcyO1qYTCuAuPJ3bOnqe1Y7kPaU.original.fullsize.png">

**Options:**

- **(A)** $3 \Omega$
- **(B)** $42 \Omega$
- **(C)** $9 \Omega$
- **(D)** $6 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $6 \Omega$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/SzVAN7gTBYvbbCvDpe4mw_NSF7ezGJgngzOY3ZTz6yE.original.fullsize.png">
In case of balanced Wheatstone Bridge
$\begin{aligned}
& \frac{V_{A B}}{V_{A D}}=\frac{V_{B C}}{V_{C D}} \Rightarrow \frac{12}{6+x}=\frac{0.5}{0.5} \\
& x=6 \Omega
\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a metre-bridge when a resistance in the left gap is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">Ω</mi></math> and unknown resistance in the right gap, the balance length is found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo> </mo><mi>cm</mi><mo>.</mo></math> On shunting the unknown resistance with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi mathvariant="normal">Ω</mi><mo>,</mo></math> the balance length changes by:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo> </mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>62</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn><mo> </mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>cm</mi></math>**

**Detailed Solution:**

<p>In first circuit:<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/628b1d13-d60d-40f4-99c8-7152c6addd8f.png" style="width: 200px; height: 128px;"/></p><p>For balanced condition, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>40</mn></mfrac><mo>=</mo><mfrac><mi>X</mi><mn>60</mn></mfrac><mo>⇒</mo><mi>X</mi><mo>=</mo><mn>3</mn><mi>Ω</mi></math></p><p>In second case:</p><p>Net resistance of the right side due to shunting becomes,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">X</mi><mo>'</mo></msup><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>3</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>.</mo><mn>2</mn><mo> </mo><mi>Ω</mi></math></p><p>Again for balanced condition, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mi>ℓ</mi></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>2</mn></mrow><mrow><mn>100</mn><mo>-</mo><mi>ℓ</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>200</mn><mo>-</mo><mn>2</mn><mi>ℓ</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>2</mn><mi>ℓ</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">ℓ</mi><mo>=</mo><mfrac><mn>200</mn><mrow><mn>3</mn><mo>.</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>62</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>cm</mi></math></p><p>Clearly, balance length changes by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>.</mo><mn>5</mn><mo> </mo><mi>cm</mi></math>.</p>

</details>

---

### Q10. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The resistance per centimeter of a meter bridge wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo> </mo><mi>Ω</mi></math> resistance in left gap. Balancing length from left end is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo> </mo><mi>cm</mi></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo> </mo><mi>Ω</mi></math> resistance in right gap. Now the wire is replaced by another wire of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>r</mi></math> resistance per centimeter. The new balancing length for same settings will be at

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo> </mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo> </mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo> </mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo> </mo><mi>cm</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f7ed16bb-dc2f-4be6-b380-4ed39a9c7ed2.png" style="width: 200px; height: 164px;"/></p><p>For first case:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>X</mi><mrow><mi>r</mi><msub><mi mathvariant="script">l</mi><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>25</mn><mrow><mi>r</mi><msub><mi mathvariant="script">l</mi><mn>2</mn></msub></mrow></mfrac></math> ... (i)</p><p>For second case:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>X</mi><mrow><mfenced><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><msub><msup><mi mathvariant="script">l</mi><mo>'</mo></msup><mn>1</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>25</mn><mrow><mfenced><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mi mathvariant="script">l</mi><msub><mo>'</mo><mn>2</mn></msub></mrow></mfrac></math> ... (ii)</p><p>From (i) and (ii), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="script">l</mi><msub><mo>'</mo><mn>1</mn></msub></mrow><msub><mi mathvariant="script">l</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mi mathvariant="script">l</mi><msub><mo>'</mo><mn>2</mn></msub></mstyle><mstyle displaystyle="true"><msub><mi mathvariant="script">l</mi><mn>2</mn></msub></mstyle></mfrac></math> also total length is constant.</p><p>Therefore, balance length doesn't change and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="script">l</mi><msub><mo>'</mo><mn>1</mn></msub><mo>=</mo><msub><mi mathvariant="script">l</mi><mn>1</mn></msub><mo>=</mo><mn>40</mn><mo> </mo><mi>cm</mi></math></p>

</details>

---

### Q11. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Wheatstone bridge principle is used to measure the specific resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>S</mi><mn>1</mn></msub></mfenced></math> of given wire, having length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>, radius <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">X</mi></math> is the resistance of wire, then specific resistance is : <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi>X</mi><mfenced><mfrac><mrow><mi>π</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mi>L</mi></mfrac></mfenced></math>. If the length of the wire gets doubled then the value of specific resistance will be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mn>1</mn></msub><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><msub><mi mathvariant="normal">S</mi><mn>1</mn></msub></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>S</mi><mn>1</mn></msub><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math>**

**Detailed Solution:**

<p>The specific resistance of a material, also known as electrical resistivity, is a measure of how strongly a specific material opposes the flow of electric current.</p><p>Specific resistance is an intrinsic property of a material and is dependent on factors such as the material's composition, temperature, and crystal structure. It is the counterpart of conductivity, with which it is inversely proportional.</p><p>Hence, even if the length of the wire is doubled, the specific resistance remains the same, i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math>.</p>

</details>

---

### Q12. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo> </mo><mi>cm</mi></math> and radius <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>7</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup><mo> </mo><mi mathvariant="normal">m</mi></math> connected across the right gap of a meter bridge. When a resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">Ω</mi></math> is connected on the left gap by using a resistance box, the balance length is found to be at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo> </mo><mi>cm</mi></math> from the left end. If the resistivity of the wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">Ω</mi><mo> </mo><mi mathvariant="normal">m</mi></math>, then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>70</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>**

**Detailed Solution:**

<p>From the null point condition of a Meter Bridge, it follows that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">Ω</mi></mrow><mn>60</mn></mfrac><mo>=</mo><mfrac><mi>X</mi><mrow><mn>100</mn><mo>-</mo><mn>60</mn></mrow></mfrac><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>X</mi><mo>=</mo><mfrac><mn>40</mn><mn>60</mn></mfrac><mo>×</mo><mn>4</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">Ω</mi><mspace linebreak="newline"></mspace><mo>=</mo><mn>3</mn><mo> </mo><mi mathvariant="normal">Ω</mi></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>X</mi></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mi>ρ</mi><mi>l</mi></mrow><mi mathvariant="normal">A</mi></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mrow><mi>ρ</mi><mi>l</mi></mrow><mrow><mi>π</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></mtd></mtr></mtable></math></p><p>From equation (1), it follows that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>=</mo><mi>ρ</mi><mo>×</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow><mrow><mi>π</mi><mo>×</mo><msup><mfenced><mrow><msqrt><mn>7</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mspace linebreak="newline"></mspace><mo>⇒</mo><mi>ρ</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>×</mo><mi>π</mi><mo>×</mo><msup><mfenced><mrow><msqrt><mn>7</mn></msqrt><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mn>0</mn><mo>.</mo><mn>1</mn></mrow></mfrac><mspace linebreak="newline"></mspace><mo>≈</mo><mn>66</mn><mo>×</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>7</mn></mrow></msup><mo> </mo><mi mathvariant="normal">Ω</mi><mo> </mo><mi mathvariant="normal">m</mi></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>66</mn></math>.</p>

</details>

---

### Q13. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>In meter bridge experiment for measuring unknown resistance &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>&#39;, the null point is obtained at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi>cm</mi></math> from the left side as shown at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi>k&#937;</mi></math>, then the value of unknown resistance &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>&#39; will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/01a26563-b9b7-4065-a3e0-60a885a51f56-image.png" style="width: 350px; height: 189px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2400**

**Detailed Solution:**

<blockquote><p>Using balanced wheatstone condition in meter bridge</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mi>S</mi></mfrac><mo>=</mo><mfrac><mn>70</mn><mn>30</mn></mfrac></math></p><p>Given here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>5</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi>k&#937;</mi></math>.</p><p>The, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>S</mi><mn>30</mn></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup></mrow><mn>70</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>3</mn><mn>7</mn></mfrac><mo>&#215;</mo><mn>5</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mn>3</mn></msup><mo>=</mo><mn>2400</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q14. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>A battery of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo> </mo><mi mathvariant="normal">V</mi></math> is connected to the circuit as shown below. The current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> drawn from the battery is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aa933cbc-e136-48db-8fda-7e846893bff2-image.png" style="width: 180px; height: 199px;" /></p><p> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>11</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<blockquote><p>The given circuit in the question is a case of a balanced Wheatstone bridge. Therefore, the circuit can be simplified as given below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c774b239-1fe7-4894-807a-86abed4fef47-image.png" style="width: 220px; height: 160px;" /></p><p>The equivalent resistance for the given circuit will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>3</mn><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>6</mn><mo>+</mo><mn>6</mn></mrow></mfenced></mrow></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Therefore, the current supplied by the battery is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi>V</mi><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>6</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q15. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Resistance are connected in a meter bridge circuit as shown in the figure. The balancing length <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>cm</mi></math>. Now an unknown resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is connected in series with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and new balancing length is found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi>cm</mi></math> measured from the same end. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/479d12ea-d21b-4c71-922e-e326f818711f-image_alt.png" style="width: 250px; height: 141px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

<blockquote><p>Applying balanced condition for meter bridge</p><p>Initially, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>P</mi><mi>Q</mi></mfrac><mo>=</mo><mfrac><mrow><mn>40</mn><mo>&#160;</mo><mi>cm</mi></mrow><mrow><mn>60</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Finally, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mo>+</mo><mi>x</mi></mrow><mi>Q</mi></mfrac><mo>=</mo><mfrac><mrow><mn>80</mn><mo>&#160;</mo><mi>cm</mi></mrow><mrow><mn>20</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>1</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Dividing equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math> by (<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mo>+</mo><mi>x</mi></mrow><mi>P</mi></mfrac><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mi>P</mi></mfrac><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mfrac><mi>x</mi><mi>P</mi></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>5</mn><mi>P</mi><mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> in the given circuit will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6dfc67e9-e11f-4aa3-a71d-587f31990641-image.png" style="width: 350px; height: 161px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<blockquote><p>The circuit can be redrawn as :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8989a341-3d3a-4ae6-8af2-8e9b978d035f-1.jpg" style="width: 177px; height: 191px;" /></p><p>We can see that the circuit is a balanced Wheatstone bridge</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>AB</mi></msub><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Current through cell <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>V</mi><msub><mi>R</mi><mi>AB</mi></msub></mfrac><mo>=</mo><mfrac><mn>40</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q17. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>Current measured by the ammeter <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>A</mi></mfenced></math> in the reported circuit when no current flows through <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi mathvariant="normal">&#937;</mi></math> resistance, will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ffa47324-3a31-4013-a3df-0caa8dc5f916-image.png" style="width: 200px; height: 187px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ffa47324-3a31-4013-a3df-0caa8dc5f916-image.png" style="width: 200px; height: 187px;" /></p><p>This is a Wheatstone circuit. For the current to be zero in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> the Wheatstone circuit should be balanced. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>6</mn></mfrac><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Now, the equivalent resistance across the battery will be, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>+</mo><mn>6</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>3</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Therefore, the current measured by the ammeter is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi>V</mi><mi>R</mi></mfrac><mo>=</mo><mfrac><mn>36</mn><mrow><mn>3</mn><mo>.</mo><mn>6</mn></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p>

</details>

---

### Q18. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>A meter bridge setup is shown in the figure. It is used to determine an unknown resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> using a given resistor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. The galvanometer <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>G</mi></mfenced></math> shows null defection when tapping key is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn><mo>&#160;</mo><mi>cm</mi></math> mark from end <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. If the end correction for end <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>cm</mi></math>, then the determined value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/589c2781-a0ff-480f-9225-7c2c9144779e-image.png" style="width: 270px; height: 177px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<p>Using the conditions of a balanced wheatstone bridge and adding the end correction.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mi>l</mi><mo>+</mo><mi>e</mi></mrow><mrow><mfenced><mrow><mi>L</mi><mo>+</mo><mi>e</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>l</mi><mo>+</mo><mi>e</mi></mrow></mfenced></mrow></mfrac><mo>&#8658;</mo><mfrac><mn>15</mn><mfenced><mrow><mn>43</mn><mo>+</mo><mn>2</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><mi>R</mi><mfenced><mrow><mn>102</mn><mo>-</mo><mn>45</mn></mrow></mfenced></mfrac><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mfrac><mn>57</mn><mn>45</mn></mfrac><mo>&#215;</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>R</mi><mo>=</mo><mn>19</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q19. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Consider a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn><mo>&#160;</mo><mi>cm</mi></math> long wire <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> as shown in the figure. The galvanometer jockey is placed at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi></math> at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. The galvanometer shows zero deflection.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a7fa89a5-4202-48fb-8d54-fedcec0900ac-image.png" style="width: 366px; height: 230px;" /></p><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, to the nearest integer, is</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **48**

**Detailed Solution:**

<p>In balanced conditions,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mi>x</mi><mrow><mn>72</mn><mo>-</mo><mi>x</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>48</mn><mo>&#160;</mo><mi>cm</mi></math>.</p>

</details>

---

### Q20. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>The four arms of a Wheatstone bridge have resistances as shown in the figure. A galvanometer of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mi>&#937;</mi></math> resistance is connected across BD. Calculate the current through the galvanometer when a potential difference of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is maintained across AC.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d3ba302-e327-4686-b182-0ac55d3a6079-image.png" style="width: 227px; height: 213px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>44</mn><mi>&#956;</mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>44</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi>mA</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>87</mn><mi>&#956;</mi><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi>mA</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f30bc76c-bb02-4725-8c2f-bfe336c691f8-image.png" style="width: 243px; height: 241px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mn>10</mn></mrow><mn>100</mn></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>15</mn></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn><mi>x</mi><mo>-</mo><mn>20</mn><mi>y</mi><mo>=</mo><mn>30</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mo>-</mo><mn>10</mn></mrow><mn>60</mn></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mi>x</mi></mrow><mn>15</mn></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mi>y</mi><mo>-</mo><mn>4</mn><mi>x</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>on solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>865</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>792</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;</mi><mi>V</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>073</mn><mi>R</mi><mo>=</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>i</mi><mo>=</mo><mn>4</mn><mo>.</mo><mn>87</mn><mo>&#160;</mo><mi>mA</mi></math></p>

</details>

---

### Q21. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Five equal resistances are connected in a network as shown in figure. The net resistance between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e2eac899-646b-4371-80b7-a0cfc6807514-image.png" style="width: 194px; height: 179px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>R</mi></mrow><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>**

**Detailed Solution:**

<p>This diagram can be drawn like</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/daf45804-3486-4177-bb77-3078bb98cb94-image.png" style="width: 257px; height: 192px;" /></p><p>It is a wheat stone bridge</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi>R</mi><mo>&#215;</mo><mn>2</mn><mi>R</mi></mrow><mrow><mn>2</mn><mi>R</mi><mo>+</mo><mn>2</mn><mi>R</mi></mrow></mfrac><mo>&#8658;</mo><mi>R</mi></math></p>

</details>

---

### Q22. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The value of current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub></math> flowing from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">C</mi></math> in the circuit diagram is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cba9f4a1-9952-463d-b268-081576e134bb-image.png" style="width: 300px; height: 224px;" />  </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>75</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/25452a43-0a8d-4a53-afa0-69d4c22a91b0-image.png" style="width: 301px; height: 242px;" /> </p><p>The Diagram shown in the question represents the balanced wheatstone bridge. It satisfy the condition of balanced wheat stone bridge.
Multiplication of dimensionally opposite resistance is same.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn><mo>&#8658;</mo><mn>4</mn><mo>=</mo><mn>4</mn></math>
When the circuit is balanced wheat stone bridge then current through the branch <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>D</mi></math> is zero, so it can be removed.</p><p>Now, after removing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>D</mi></math> wire voltage across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.</p><p>So, current will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>8</mn><mrow><mn>4</mn><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi>A</mi></math> </p>

</details>

---

### Q23. JEE Main 2020 (09 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

In a meter bridge experiment <math><mi>S</mi></math> is a standard resistance. <math><mi>R</mi></math> is a resistance wire. It is found that balancing length is <math><mi>l</mi><mo>=</mo><mn>25</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi><mo>.</mo></math> If <math><mi>R</mi></math> is replaced by a wire of hall length and half diameter that of <math><mi>R</mi></math> of same material, then the balancing distance <math><mi>l</mi><mi>&#39;</mi></math> (in <math><mi mathvariant="normal">c</mi><mi mathvariant="normal">m</mi></math> ) will now be ______________.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3a084e1c-0d66-4a24-893e-c9220c259f09-image.png" style="width: 350px; height: 186px;" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **40**

**Detailed Solution:**

<math><mfrac><mrow><mi>X</mi></mrow><mrow><mi>R</mi></mrow></mfrac><mo>=</mo><mi></mi><mfrac><mrow><mn>75</mn></mrow><mrow><mn>25</mn></mrow></mfrac><mo>=</mo><mn>3</mn></math>
<math><mi>R</mi><mo>=</mo><mi></mi><mfrac><mrow><mi>p</mi><mi>l</mi></mrow><mrow><mi>A</mi></mrow></mfrac><mo>=</mo><mi></mi><mfrac><mrow><mn>4</mn><mi>p</mi><mi>l</mi></mrow><mrow><mi>&#960;</mi><msup><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></math>
<math><msup><mrow><mi>R</mi></mrow><mrow><mi>&#39;</mi></mrow></msup><mo>=</mo><mi></mi><mfrac><mrow><mn>4</mn><mi>p</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>&#960;</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>=</mo><mn>2</mn><mi>R</mi></math>
<math><mi>&#960;</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
then <math><mfrac><mrow><mi>X</mi></mrow><mrow><mi>R</mi><mi>&#39;</mi></mrow></mfrac><mo>=</mo><mi></mi><mfenced separators="|"><mrow><mfrac><mrow><mn>100</mn><mo>-</mo><mi>l</mi></mrow><mrow><mi>l</mi></mrow></mfrac></mrow></mfenced></math>
<math><mfrac><mrow><mn>100</mn><mo>-</mo><mi>l</mi></mrow><mrow><mi>l</mi></mrow></mfrac><mo>=</mo><mi></mi><mfrac><mrow><mi>X</mi></mrow><mrow><mn>2</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mi></mi><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>40.00</mn><mo>&#160;</mo><mi>c</mi><mi>m</mi></math>

</details>

---

### Q24. JEE Main 2020 (08 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Four resistances of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> respectively in cyclic order to form Wheatstone&rsquo;s network. The resistance that is to be connected in parallel with the resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> to balance the network is ______________ <math><mi mathvariant="normal">&#937;</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fefbb6b7-b7ab-4c19-8ecc-111383a4bbc4.jpeg" />
<math><mfrac><mrow><mn>10</mn><mi>R</mi></mrow><mrow><mn>10</mn><mo>+</mo><mi>R</mi></mrow></mfrac><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>15</mn><mo>&#215;</mo><mn>4</mn></math>
On solving
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>&#937;</mi></math>

</details>

---

### Q25. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a Wheatstone bridge (see fig.), Resistances $P$ and $Q$ are approximatelyequal. When $R=400 \Omega$, the bridge is balanced. On interchanging $\mathrm{P}$ and $\mathrm{Q}$, the value of $\mathrm{R},$ for balance, is $405 \Omega$. The value of $Y$ is close to

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/YsHiimzSujIKP9zVcVW-Mh6wSFLwl3XGPDNM9DB8Cvk.original.fullsize.png">

**Options:**

- **(A)** $401.5 \mathrm{ohm}$
- **(B)** $404.5 \mathrm{ohm}$
- **(C)** $403.5 \mathrm{ohm}$
- **(D)** $402.5 \mathrm{ohm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $402.5 \mathrm{ohm}$**

**Detailed Solution:**

$402.5 \mathrm{ohm}$

</details>

---

### Q26. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The Wheatstone bridge shown in the figure below, gets balanced when the carbon resistor used as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub></math> has the colour code (orange, red, brown). The resistors <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, respectively. Assuming that the colour code for the carbon resistors gives their accurate values, the colour code for the carbon resistor, used as <math><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></math>, would be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cffc70ba-29c5-41ff-997b-4d311ab1f26f-image.png" style="width: 300px; height: 333px;" /></p>

**Options:**

- **(A)** brown, blue, black.
- **(B)** brown, blue, brown.
- **(C)** grey, black, brown.
- **(D)** red, green, brown.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) brown, blue, brown.**

**Detailed Solution:**

<p>Colour band <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> indicate the first two significant figures of resistance in &#39;ohm&#39;, while the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> band gives the decimal multiplier i.e., the number of zeros that follows the two significant figures <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>.</p><p>The last band <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> indicates the tolerance in percentage about the indicated value or in other word, it represents the percentage accuracy of the indicated value. </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d339d85a-80e7-45bf-b14c-62412e232ffd-image.png" style="width: 600px; height: 148px;" /></p><p>For <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math>, the given colour of the rings of a carbon resistor are orange, red, brown then, the value of resistance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mn>32</mn><mo>&#215;</mo><msup><mn>10</mn><mn>1</mn></msup></math></p><p>Condition for balance in the Wheat stone&#39;s bridge is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>3</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>2</mn></msub><msub><mi>R</mi><mn>4</mn></msub></mfrac></math>

So, <math><mfrac><mrow><mn>320</mn></mrow><mrow><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>80</mn></mrow><mrow><mn>40</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>=</mo><mn>160</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, so colour coding of resistor <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub></math> is</p><p>Brown<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>1</mn></math></p><p>Blue<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>6</mn></math></p><p>Brown<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#215;</mo><msup><mn>10</mn><mn>1</mn></msup><mo>&#8658;</mo><mn>160</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q27. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

In a meter bridge as shown in the figure, it is given that resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mn>12.5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> <span style="font-size:12px;"><span style="color: rgb(34, 34, 34); font-family: arial, sans-serif;"> </span></span>and that the balance is obtained at a distance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> from end <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> (by jockey <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>J</mi></math>). After interchanging the resistances <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> a new balance point is found at a distance <math><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub></math> from end <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>. What are the values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math><span style="color: rgb(34, 34, 34); font-family: arial, sans-serif; font-size: 14px;">) </span>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math>?<mrow><mn></mn></mrow>

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ef40e046-bbbf-4993-96ac-471902ab0eb2-image.png" style="width: 370px; height: 224px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mo>.</mo><mn>15</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math>**

**Detailed Solution:**

For a balanced meter bridge, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>y</mi><mo>)&#215;&#8203;</mo><mn>39.5</mn><mo>=</mo><mi>x</mi><mo>&#215;</mo><mfenced separators="|"><mrow><mn>100</mn><mo>-</mo><mn>39.5</mn></mrow></mfenced></math>, 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mrow><mn>12.5</mn><mo>&#215;</mo><mn>39.5</mn></mrow><mn>60.5</mn></mfrac><mo>=</mo><mn>8.16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. When <math><mi>x</mi><mi>&#160;and&#160;</mi><mi>y</mi></math> are interchanged <math> <mrow> <msub> <mi>l</mi> <mn>1</mn> </msub> </mrow> </math> and <math> <mrow> <mrow><mo>(</mo> <mrow> <mn>100</mn><mo>&#8722;</mo><msub> <mi>l</mi> <mn>1</mn> </msub> </mrow> <mo>)</mo></mrow> </mrow> </math> will also interchange, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub><mo>=</mo><mn>60.</mn><mn>5</mn><mo>&#160;</mo><mi>cm</mi><mo>.</mo></math>

</details>

---

### Q28. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

In a meter bridge, as shown in the figure, it is given that resistance $Y=12.5 \Omega$ and that the balance is obtained at a distance $39.5 \mathrm{~cm}$ from end $A$ (by jockey J). After interchanging the resistances $X$ and $Y$, a new balance point is found at a distance $l_2$ from end $A$. What are the values of $X$ and $l_2$ ?
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9ARBdNrbmVz8S9-WtxlCyY8c3KaEGpE5KSUKLsGXVAs.original.fullsize.png">

**Options:**

- **(A)** $19.15 \Omega$ and $39.5 \mathrm{~cm}$
- **(B)** $8.16 \Omega$ and $60.5 \mathrm{~cm}$
- **(C)** $19.15 \Omega$ and $60.5 \mathrm{~cm}$
- **(D)** $8.16 \Omega$ and $39.5 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $8.16 \Omega$ and $60.5 \mathrm{~cm}$**

**Detailed Solution:**

For a balanced meter bridge,
$$
\begin{aligned}
&\frac{\mathrm{X}}{39.5}=\frac{\mathrm{Y}}{(100-39.5)} \\
&\Rightarrow \mathrm{Y}=39.5=\mathrm{X} \times(100-39.5) \\
&or \ldots \mathrm{X}=\frac{12.5 \times 39.5}{60.5}=8.16 \Omega
\end{aligned}
$$
When $\mathrm{X}$ and $\mathrm{Y}$ are interchanged $l_1$ and (100 $-l_1$ ) will also interchange so, $l_2=60.5 \mathrm{~cm}$

</details>

---

### Q29. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `3`

On interchanging the resistances, the balance point of a meter bridge shifts to the left by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math>. The resistance of their series combination is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>k&#937;</mi></math> . How much was the resistance on the left slot before interchanging the resistances?

**Options:**

- **(A)** <math><mn>910</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mn>990</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mn>505</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mn>550</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>550</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dcef6876-24e7-4042-ad25-833e1ed41394-image.png" style="width: 200px; height: 148px;" />
<math><mfrac><mrow><mi>a</mi></mrow><mrow><mi>b</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>l</mi></mrow><mrow><mn>100</mn><mo>-</mo><mi>l</mi></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math>

<math> <mrow> <mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1000</mn></mrow> </math>

<math> <mrow> <mfrac> <mi>b</mi> <mi>a</mi> </mfrac> <mo>=</mo><mfrac> <mrow> <mi>l</mi><mo>&#8722;</mo><mn>10</mn></mrow> <mrow> <mn>110</mn><mo>&#8722;</mo><mi>l</mi></mrow> </mfrac> </mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>100</mn><mo>&#8722;</mo><mi>l</mi></mrow> <mi>l</mi> </mfrac> <mo>=</mo><mfrac> <mrow> <mi>l</mi><mo>&#8722;</mo><mn>10</mn></mrow> <mrow> <mn>110</mn><mo>&#8722;</mo><mi>l</mi></mrow> </mfrac> </mrow> </math>

<math> <mrow> <msup> <mi>l</mi> <mn>2</mn> </msup> <mo>&#8722;</mo><mn>10</mn><mi>l</mi><mo>=</mo><mn>11000</mn><mo>+</mo><msup> <mi>l</mi> <mn>2</mn> </msup> </mrow> </math>

<math> <mrow> <mo>&#8722;</mo><mn>100</mn><mtext>&#8201;</mtext><mi>l</mi><mo>=</mo><mn>110</mn><mtext>&#8201;</mtext><mi>l</mi></mrow> </math>

<math> <mrow> <mn>200</mn><mi>l</mi><mo>=</mo><mn>11000</mn></mrow> </math>

<math> <mrow> <mi>l</mi><mo>=</mo><mfrac> <mrow> <mn>110</mn></mrow> <mn>2</mn> </mfrac> <mo>=</mo><mn>55</mn></mrow> </math>

<math> <mrow> <mfrac> <mrow> <mn>55</mn></mrow> <mrow> <mn>45</mn></mrow> </mfrac> <mo>=</mo><mfrac> <mi>a</mi> <mi>b</mi> </mfrac> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>550</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mtext>&#8201;</mtext><mi>b</mi><mo>=</mo><mn>450</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math>

</details>

---

### Q30. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

In a meter bridge experiment resistances are connected as shown in the figure. Initially resistance <math><mi>P</mi><mo>=</mo><mn>4&#160;</mn><mi mathvariant="normal">&#937;</mi></math> and the neutral point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> . Now an unknown resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is connected in series to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> and the new position of the neutral point is at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi>cm</mi></math> from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> . The value of unknown resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is -

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/35ff46be-ad57-498c-b883-2a004dd5b2d6-image.png" style="width: 350px; height: 252px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>33</mn></mrow><mrow><mn>5 </mn></mrow></mfrac><mi mathvariant="normal"> Ω</mi></math>
- **(B)** <math><mn>6</mn><mi> </mi><mi mathvariant="normal"> Ω</mi></math>
- **(C)** <math><mfrac><mrow><mn>20</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal"> Ω</mi></math>
- **(D)** <math><mn>7</mn><mi mathvariant="normal"> Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>20</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal"> Ω</mi></math>**

**Detailed Solution:**

<p>Given initially a resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is connected in the left gap and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is connected in the right gap of meter bridge and the null point is obtained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#160;</mo><mi>cm</mi></math>,</p><p>From the balanced condition of the Wheatstone bridge </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>P</mi><mi>Q</mi></mfrac><mo>=</mo><mfrac><mi>R</mi><mi>S</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math> is the resistance per unit length of meter bridge wire than</p><p>For wire <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>N</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>&#961;</mi><mi>l</mi><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi>&#961;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>l</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>40</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfenced></math> </p><p>And for NB wire </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>&#961;</mi><mfenced><mrow><mn>100</mn><mo>-</mo><mi>l</mi></mrow></mfenced><mspace linebreak="newline"/><mi>Q</mi><mo>=</mo><mo>&#160;</mo><mi>&#961;</mi><mfenced><mrow><mn>100</mn><mo>-</mo><mn>60</mn></mrow></mfenced><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi>&#961;</mi></math>  </p><p>On substituting the values from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>60</mn></mfrac><mo>=</mo><mfrac><mi>Q</mi><mn>40</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Q</mi><mo>=</mo><mfrac><mn>16</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mi>&#160;</mi><mi mathvariant="normal">&#937;</mi></math></p><p>Now an unknown resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is connected in series with the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance and the null point is obtained at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>80</mn><mo>&#160;</mo><mi>cm</mi></math> </p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>&#961;</mi><mo>&#160;</mo><mi>l</mi><mo>&#160;</mo><mo>=</mo><mn>80</mn><mo>&#160;</mo><mi>l</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>&#961;</mi><mfenced><mrow><mn>100</mn><mo>-</mo><mi>l</mi></mrow></mfenced><mspace linebreak="newline"></mspace><mi>Q</mi><mo>=</mo><mo>&#160;</mo><mi>&#961;</mi><mfenced><mrow><mn>100</mn><mo>-</mo><mn>80</mn></mrow></mfenced><mo>=</mo><mo>&#160;</mo><mn>20</mn><mo>&#160;</mo><mi>&#961;</mi></math></p><p>Then from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>+</mo><mi>R</mi></mrow><mn>80</mn></mfrac><mo>=</mo><mfrac><mi>Q</mi><mn>20</mn></mfrac><mspace linebreak="newline"/><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mi>R</mi></mrow><mn>80</mn></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>3</mn></mfrac></mstyle><mn>20</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><mo>&#160;</mo><mi>Q</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></mrow></mfenced><mspace linebreak="newline"/><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mi>R</mi></mrow><mn>80</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>60</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mspace linebreak="newline"/><mo>&#8658;</mo><mo>&#160;</mo><mi>R</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mn>20</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q31. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

Which of the following statements is false?

**Options:**

- **(A)** Kirchhoff's second law represents energy conservation
- **(B)** Wheatstone bridge is the most sensitive when all the four resistances are of the same order of magnitude
- **(C)** In a balanced Wheatstone bridge if the cell and the galvanometer are exchanged, the null point is disturbed
- **(D)** A rheostat can be used as a potential divider

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) In a balanced Wheatstone bridge if the cell and the galvanometer are exchanged, the null point is disturbed**

**Detailed Solution:**

<p>Let us assume <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>R</mi><mn>4</mn></msub></math> is connected balanced wheat stone bridge, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>3</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>2</mn></msub><msub><mi>R</mi><mn>4</mn></msub></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> as shown below,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/41a068b4-0b7a-4dec-b0d0-aeada99a2def-image.png" style="width: 170px; height: 199px;" /> 
                                                                   
If galvanometer and cell is exchanged, then circuit becomes as shown in below figure, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/620fa190-d812-4e10-bfd9-9652fbf2c15f-image.png" style="width: 170px; height: 187px;" />
                                                                        

The circuit is redrawn and can be visualised as below figure, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c433b183-fc93-496d-924b-98debda54f30-image.png" style="width: 170px; height: 156px;" />

                                                                     
In this case, if it is balanced, then there must be, 
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>3</mn></msub><msub><mi>R</mi><mn>4</mn></msub></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math>

Equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> realises that, both equations are same, which means null point is not affected.</p>

</details>

---

### Q32. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

In a metre bridge experiment null point is obtained at $40 \mathrm{~cm}$ from one end of the wire when resistance $\mathrm{X}$ is balanced against another resistance $\mathrm{Y}$. If $\mathrm{X} < \mathrm{Y}$, then the new position of the null point from the same end, if one decides to balance a resistance of $3 \mathrm{X}$ against $\mathrm{Y}$, will be close to :

**Options:**

- **(A)** $80 \mathrm{~cm}$
- **(B)** $75 \mathrm{~cm}$
- **(C)** $67 \mathrm{~cm}$
- **(D)** $50 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $67 \mathrm{~cm}$**

**Detailed Solution:**

From question, $\frac{x}{y}=\frac{40}{100-40}=\frac{2}{3}$
$$
\Rightarrow \mathrm{x}=\frac{2}{3} \mathrm{y}
$$
Again, $\frac{3 x}{y}=\frac{Z}{100-Z}$
or $\frac{3 \times \frac{2 y}{3}}{y}=\frac{Z}{100-Z}$
Solving we get $\mathrm{Z}=67 \mathrm{~cm}$
Therefore new position of null point
$$
\cong 67 \mathrm{~cm}
$$

</details>

---

### Q33. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `1`

In a sensitive meter bridge apparatus the bridge wire should possess

**Options:**

- **(A)** high resistivity and low temperature coefficient.
- **(B)** low resistivity and high temperature coefficient.
- **(C)** low resistivity and low temperature coefficient.
- **(D)** high resistivity and high temperature coefficient.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) high resistivity and low temperature coefficient.**

**Detailed Solution:**

Bridge wire in a sensitive meter bridge wire should be of high resistivity and low temperature coefficient.

</details>

---

### Q34. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

In a Wheatstone's bridge, there resistances $\mathrm{P}, \mathrm{Q}$ and $\mathrm{R}$ connected in the three arms and the fourth arm is formed by two resistances $\mathrm{S}_1$ and $\mathrm{S}_2$ connected in parallel. The condition for bridge to be balanced will be

**Options:**

- **(A)** $\frac{\mathrm{P}}{\mathrm{Q}}=\frac{\mathrm{R}}{\mathrm{S}_1+\mathrm{S}_2}$
- **(B)** $\frac{\mathrm{P}}{\mathrm{Q}}=\frac{2 \mathrm{R}}{\mathrm{S}_1+\mathrm{S}_2}$
- **(C)** $\frac{\mathrm{P}}{\mathrm{Q}}=\frac{\mathrm{R}\left(\mathrm{S}_1+\mathrm{S}_2\right)}{\mathrm{S}_1 \mathrm{~S}_2}$
- **(D)** $\frac{\mathrm{P}}{\mathrm{Q}}=\frac{\mathrm{R}\left(\mathrm{S}_1+\mathrm{S}_2\right)}{2 \mathrm{~S}_1 \mathrm{~S}_2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{\mathrm{P}}{\mathrm{Q}}=\frac{\mathrm{R}\left(\mathrm{S}_1+\mathrm{S}_2\right)}{\mathrm{S}_1 \mathrm{~S}_2}$**

**Detailed Solution:**

$\frac{\mathrm{P}}{\mathrm{Q}}=\frac{\mathrm{R}\left(\mathrm{S}_1+\mathrm{S}_2\right)}{\mathrm{S}_1 \mathrm{~S}_2}$

</details>

---

### Q35. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

In a metre bridge experiment null point is obtained at $20 \mathrm{~cm}$ from one end of the wire when resistance $X$ is balanced against another resistance $Y$. If $X < Y$, then where will be the new position of the null point from the same end, if one decides to balance a resistance of $4 X$ against Y?

**Options:**

- **(A)** $50 \mathrm{~cm}$
- **(B)** $80 \mathrm{~cm}$
- **(C)** $40 \mathrm{~cm}$
- **(D)** $70 \mathrm{~cm}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $50 \mathrm{~cm}$**

**Detailed Solution:**

We have from meter bridge experiment, $\frac{\mathrm{R}_1}{\mathrm{R}_2}=\frac{\ell_1}{\ell_2}$, where $\ell_2=\left(100-\ell_1\right) \mathrm{cm}$ In the first case, $X / Y=20 / 80$ In the second case $\frac{4 X}{Y}=\frac{\ell}{100-\ell}$ $\ell=50 \mathrm{~cm}$.

</details>

---

