# JEE Main Physics - Current Electricity

## Topic 6: Kirchoffs Laws

**Total Questions:** 22

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `numerical` | *Level:* `3`

The stored charge in the capacitor in steady state of the following circuit is ________ $\mu$C.
<img style="width: 350px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/08APRS2__q49_d1.jpg" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **200**

**Detailed Solution:**

In steady state, the capacitor acts as an open circuit, meaning no current flows through the branch containing the $100\ \mu\text{F}$ capacitor. Consequently, no current flows through the $10\ \Omega$ resistor in series with it on the top right.

The voltage across the capacitor will be equal to the voltage across the $4\ \Omega$ vertical resistor.

Let's simplify the circuit to find this voltage. The $12\ \Omega$ resistor on the left is in parallel with the $12\ \text{V}$ battery, so the voltage across the rest of the circuit remains $12\ \text{V}$.

For the rightmost part of the active circuit, the $4\ \Omega$ top resistor, the $4\ \Omega$ vertical resistor, and the $2\ \Omega$ bottom resistor are in series. Their equivalent resistance is:
$R_{\text{right}} = 4\ \Omega + 4\ \Omega + 2\ \Omega = 10\ \Omega$

This $10\ \Omega$ equivalent resistance is in parallel with the $10\ \Omega$ vertical resistor in the middle. The equivalent resistance of this parallel combination is:
$R_{\text{mid}} = \dfrac{10 \times 10}{10 + 10} = 5\ \Omega$

Now, the total resistance of the main circuit connected to the $12\ \text{V}$ source is the sum of the $5\ \Omega$ top-left resistor, the $5\ \Omega$ equivalent middle resistance, and the $2\ \Omega$ bottom-left resistor:
$R_{\text{total}} = 5\ \Omega + 5\ \Omega + 2\ \Omega = 12\ \Omega$

The total current flowing from the $12\ \text{V}$ source into this main branch is:
$I = \dfrac{12\ \text{V}}{12\ \Omega} = 1\ \text{A}$

The voltage across the parallel combination (the middle section) is:
$V_{\text{mid}} = I \times R_{\text{mid}} = 1\ \text{A} \times 5\ \Omega = 5\ \text{V}$

This $5\ \text{V}$ is applied across the right branch which has a total resistance of $10\ \Omega$. The current through this branch is:
$I_{\text{right}} = \dfrac{5\ \text{V}}{10\ \Omega} = 0.5\ \text{A}$

The voltage across the $4\ \Omega$ vertical resistor is:
$V_{4\Omega} = I_{\text{right}} \times 4\ \Omega = 0.5\ \text{A} \times 4\ \Omega = 2\ \text{V}$

Since the capacitor is in parallel with this $4\ \Omega$ resistor (with no voltage drop across the $10\ \Omega$ resistor in its branch), the voltage across the capacitor is also $2\ \text{V}$.

The stored charge in the capacitor is:
$Q = C \times V = 100\ \mu\text{F} \times 2\ \text{V} = 200\ \mu\text{C}$

Answer: $200$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Refer to the circuit diagram given below. The heat generated across the $6\,\Omega$ resistance in $100$ second is $\dfrac{\alpha}{100}$ J. The value of $\alpha$ is _______. (Nearest integer)
<img style="width: 300px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/06APRS1__q46_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3477**

**Detailed Solution:**

Taking the right-hand wire as the reference node at $0\text{ V}$, let the left junction (where the $3\,\Omega$, $4\,\Omega$ and $6\,\Omega$ resistors meet) be Node A at potential $V_A$.

Bottom branch: The positive terminal of the $2\text{ V}$ battery is at the reference, so its negative terminal (and hence the left end of the $3\,\Omega$ resistor) is at $-2\text{ V}$.
Top branch: The positive terminal of the $3\text{ V}$ battery is at the reference, so its negative terminal (and hence the node between the $6\,\Omega$ resistor and the $3\text{ V}$ battery) is at $-3\text{ V}$.

Applying KCL at Node A (sum of currents leaving the node is zero):
$\dfrac{V_A - 0}{4} + \dfrac{V_A - (-2)}{3} + \dfrac{V_A - (-3)}{6} = 0$

$\dfrac{V_A}{4} + \dfrac{V_A + 2}{3} + \dfrac{V_A + 3}{6} = 0$

Multiplying throughout by $12$:
$3V_A + 4(V_A + 2) + 2(V_A + 3) = 0$

$3V_A + 4V_A + 8 + 2V_A + 6 = 0$

$9V_A + 14 = 0 \Rightarrow V_A = -\dfrac{14}{9}\text{ V}$

Current through the $6\,\Omega$ resistor (from Node A towards the $-3\text{ V}$ point):
$I_6 = \dfrac{V_A - (-3)}{6} = \dfrac{-\dfrac{14}{9} + 3}{6} = \dfrac{\dfrac{13}{9}}{6} = \dfrac{13}{54}\text{ A}$

Heat generated in the $6\,\Omega$ resistor in $t = 100\text{ s}$:
$H = I_6^2 \cdot R \cdot t = \left(\dfrac{13}{54}\right)^2 \cdot 6 \cdot 100$

$H = \dfrac{169}{2916} \cdot 600 = \dfrac{169 \cdot 100}{486} = \dfrac{16900}{486}\text{ J}$

Given $H = \dfrac{\alpha}{100}\text{ J}$:
$\dfrac{\alpha}{100} = \dfrac{16900}{486}$

$\alpha = \dfrac{16900 \cdot 100}{486} = \dfrac{1690000}{486} \approx 3477.37$

Rounding to the nearest integer:
$\alpha = 3477$

Hence, the answer is $3477$.

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Under steady state condition the potential difference across the capacitor in the circuit is _______ V.
<img style="width: 200px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS2__q37_d1.jpg" />

**Options:**

- **(A)** $0.5$
- **(B)** $1.5$
- **(C)** $0$
- **(D)** $2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.5$**

**Detailed Solution:**

In steady state, the capacitor acts as an open circuit, meaning no current flows through the middle branch.

The circuit simplifies to a single loop containing the $2 \text{ V}$ battery, the $6 \Omega$ resistor, and the $2 \Omega$ resistor.

The total resistance of this loop is $R_{\text{eq}} = 2 + 6 = 8 \Omega$.

The current flowing through the loop is $I = \dfrac{2}{8} = 0.25 \text{ A}$.

The potential difference across the parallel branches is equal to the voltage drop across the $2 \Omega$ resistor:
$V = I \times 2 = 0.25 \times 2 = 0.5 \text{ V}$

Since there is no current in the middle branch, the voltage drop across the $4 \Omega$ resistor is zero. Thus, the entire potential difference of $0.5 \text{ V}$ appears across the capacitor.

Answer: $0.5$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Refer to the figure given below. The values of $I_1$, $I_2$ and $I_3$ are __________.
<img style="width: 300px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS1__q34_d1.png" />

**Options:**

- **(A)** $I_1 = 2.5$ A, $I_2 = 1.875$ A, $I_3 = 1.875$ A
- **(B)** $I_1 = 1.875$ A, $I_2 = 2.5$ A, $I_3 = 1.875$ A
- **(C)** $I_1 = 1.875$ A, $I_2 = 1.875$ A, $I_3 = 2.5$ A
- **(D)** $I_1 = 2.5$ A, $I_2 = 2.5$ A, $I_3 = 1.875$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $I_1 = 2.5$ A, $I_2 = 1.875$ A, $I_3 = 1.875$ A**

**Detailed Solution:**

Using the principle of superposition, we analyse the circuit with one source active at a time.

Case 1: Only the $10\text{ V}$ source is active (the $5\text{ V}$ source is replaced by a short circuit).

With the $5\text{ V}$ source shorted, the top and bottom nodes of the bridge are directly connected by a wire, forming a Wheatstone bridge.

Checking for balance:
Left arm ratio: $\dfrac{4}{4} = 1$
Right arm ratio: $\dfrac{2}{2} = 1$

The ratios are equal, so the bridge is balanced. Hence, no current flows through the middle branch connecting the two nodes, and the contribution to $I_2$ from the $10\text{ V}$ source is $0\text{ A}$.

Equivalent resistance of the balanced bridge:
$(4 + 2)\,\Omega \parallel (4 + 2)\,\Omega = 6\,\Omega \parallel 6\,\Omega = 3\,\Omega$

Total resistance including the series $1\,\Omega$ resistor:
$R_{eq} = 3 + 1 = 4\,\Omega$

Current drawn from the $10\text{ V}$ source:
$I_{1(10V)} = \dfrac{10}{4} = 2.5\text{ A}$

This current splits equally between the two $6\,\Omega$ branches, so the current through the bottom $4\,\Omega$ resistor is:
$I_{3(10V)} = \dfrac{2.5}{2} = 1.25\text{ A}$

Case 2: Only the $5\text{ V}$ source is active (the $10\text{ V}$ source is replaced by a short circuit).

Now the $5\text{ V}$ source is applied across the top and bottom nodes, and the $1\,\Omega$ resistor lies in the middle branch between the left and centre nodes.

For the left branch ($4\,\Omega$ and $4\,\Omega$ in series), the potential at the midpoint is $\dfrac{5}{2} = 2.5\text{ V}$.
For the right branch ($2\,\Omega$ and $2\,\Omega$ in series), the potential at the midpoint is also $\dfrac{5}{2} = 2.5\text{ V}$.

Since both midpoints are at the same potential, no current flows through the $1\,\Omega$ middle branch. Hence, the contribution to $I_1$ from the $5\text{ V}$ source is $0\text{ A}$.

Equivalent resistance seen by the $5\text{ V}$ source:
$(4 + 4)\,\Omega \parallel (2 + 2)\,\Omega = 8\,\Omega \parallel 4\,\Omega = \dfrac{8 \times 4}{8 + 4} = \dfrac{8}{3}\,\Omega$

Total current supplied by the $5\text{ V}$ source:
$I_{2(5V)} = \dfrac{5}{8/3} = \dfrac{15}{8} = 1.875\text{ A}$

Current through the left branch (which includes the bottom $4\,\Omega$ resistor):
$I_{3(5V)} = \dfrac{5}{8} = 0.625\text{ A}$

Applying superposition:
$I_1 = I_{1(10V)} + I_{1(5V)} = 2.5 + 0 = 2.5\text{ A}$
$I_2 = I_{2(10V)} + I_{2(5V)} = 0 + 1.875 = 1.875\text{ A}$
$I_3 = I_{3(10V)} + I_{3(5V)} = 1.25 + 0.625 = 1.875\text{ A}$

Hence, the correct option is $(1)\ I_1 = 2.5\text{ A},\ I_2 = 1.875\text{ A},\ I_3 = 1.875\text{ A}$.

</details>

---

### Q5. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The voltage and the current between $A$ and $B$ points shown in the circuit are _____.
<img style="width:350px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/04APRS1__q43_d1.png" />

**Options:**

- **(A)** $24$ V, $12$ A
- **(B)** $24$ V, $4$ A
- **(C)** $18$ V, $12$ A
- **(D)** $27$ V, $4$ A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $24$ V, $4$ A**

**Detailed Solution:**

The four parallel branches between the common left node $A$ and the common right node are all identical: each consists of a $27\text{ V}$ source in series with a $3\ \Omega$ resistor. In the third branch, the two cells $(14\text{ V}$ and $13\text{ V})$ aid each other, giving a net EMF of $14 + 13 = 27\text{ V}$.

Thevenin equivalent between $A$ and $B$:
Since all four branches have the same EMF and polarity in parallel:
$V_{th} = 27\text{ V}$

The four $3\ \Omega$ resistors in parallel give:
$R_{th} = \dfrac{3}{4} = 0.75\ \Omega$

Load branch (diagonal):
The diagonal connecting $A$ and $B$ consists of two $3\ \Omega$ resistors in series, so:
$R_L = 3 + 3 = 6\ \Omega$

Current through the diagonal branch:
$I = \dfrac{V_{th}}{R_{th} + R_L} = \dfrac{27}{0.75 + 6} = \dfrac{27}{6.75} = 4\text{ A}$

Voltage across $A$ and $B$:
$V_{AB} = I \cdot R_L = 4 \times 6 = 24\text{ V}$

Hence, the voltage is $24\text{ V}$ and the current is $4\text{ A}$, which corresponds to option $(2)\ 24\text{ V},\ 4\text{ A}$.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The reading of the ammeter $(A)$ in steady state in the following circuit (assuming negligible internal resistance of the ammeter) is $\_\_\_\_$ A. 
 <img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_q_29_1_v2.png">

**Options:**

- **(A)** 1
- **(B)** $1 / 2$
- **(C)** 0
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

In steady state, 
 <img style="width:400px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_s_29_1.png">
The ammeter reads 1 A.

</details>

---

### Q7. JEE Main 2025 (28 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The value of current I in the electrical circuit as given below, when potential at A is equal to the potential at B, will be ____ A.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aLwCpyfWnQreR1j0QKAlhgjpu57sza1dTPbModrFIgQ.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/TV5QA-mQSJSoZrJbEshrA_ACjvV60xoND2PsZXMNqZw.original.fullsize.png">




$\begin{aligned} & \mathrm{V}_{\mathrm{A}}=\mathrm{V}_{\mathrm{B}} \Rightarrow \text { the bridge is balanced } \\ & \Rightarrow \frac{10}{\mathrm{R}}=\frac{20}{40} \\ & \mathrm{R}=20 \Omega \\ & \mathrm{I}=\frac{40}{20}=2 \mathrm{~A}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (22 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The net current flowing in the given circuit is_______ A.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/kKwFUANHLrlZET3zaDf9MrsmFhSJOkaVZdlF6bWHEC8.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cn6swmDoqSfCHrXHTG3LpumdbGaRiBLg3rWTEvDntqE.original.fullsize.png">




$\begin{aligned} & \mathrm{R}_{\mathrm{eq}}=2 \Omega \\ & \mathrm{I}=\frac{2}{2}=1 \mathrm{~A}\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (09 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

The current flowing through the $1 \Omega$ resistor is $\frac{n}{10}$ A. The value of $n$ is _________
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/dsNPB_ZV4lFNqlrPpx-DseCEynLkUV2IkpZBB3cre4U.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hKS1JBsBOxMFRz8YY5btAl2TZ7Z1jVhGOkV7weJL-bY.original.fullsize.png">
$\begin{aligned} & \frac{y-5}{2}+\frac{y-0}{2}+\frac{y-x+10}{1}=0 \\ & y-5+y+2 y-2 x+20=0 \\ & 4 y-2 x+15=0 \quad \ldots .(\text { (i) } \\ & \frac{x-5}{4}+\frac{x-0}{4}+\frac{x-10-y}{1}=0 \\ & x-5+x+4 x-40-4 y=0 \\ & 6 x-4 y-45=0 \quad . .(i) \\ & \frac{-2 x+4 y+15=0 . .(i i)}{4 x-30=0} \\ & x=\frac{15}{2} \& 4 y-15+15=0 \\ & y=0 \\ & i=\frac{y-x+10}{1} \\ & i=\frac{0-7.5+10}{1} \\ & i=2.5 A=\frac{n}{10} A \\ & n=25\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A potential divider circuit is shown in figure. The output voltage <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>0</mn></msub></math> is</p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fd09cbf0-70e3-4a7d-969c-cb462a26c061.png" style="width: 500px; height: 201px;"/>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo> </mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo> </mo><mi>mV</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">V</mi><mspace linebreak="newline"></mspace></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo> </mo><mi>mV</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">V</mi><mspace linebreak="newline"></mspace></math>**

**Detailed Solution:**

<p>Equivalent resistance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mn>3300</mn><mo>+</mo><mn>7</mn><mfenced><mn>100</mn></mfenced><mo>=</mo><mn>4000</mn><mo> </mo><mi mathvariant="normal">Ω</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><p>Now, current through circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>4</mn><mn>4000</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>1000</mn></mfrac><mo> </mo><mi mathvariant="normal">A</mi></math></p><p>Potential drop <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub><mo>=</mo><mi>i</mi><mi>R</mi><mo>=</mo><mfrac><mn>1</mn><mn>1000</mn></mfrac><mo>×</mo><mn>500</mn><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo> </mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q11. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Figure shows a part of an electric circuit. The potentials at points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> respectively. The current through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor will be,</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/454ecff4-7703-4833-9d2a-1bb9bbdaa3a9-image.png" style="width: 250px; height: 122px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2cacfb7c-557c-48b4-9dba-c46c6141d4ba.png" style="width: 300px; height: 147px;" /></p><p>Let the potential be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> at the junction.</p><p>By using <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>I</mi><mi>R</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>-</mo><mi>x</mi><mo>=</mo><mn>10</mn><msub><mi>i</mi><mn>1</mn></msub><mspace linebreak="newline"></mspace><mi>x</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>20</mn><msub><mi>i</mi><mn>2</mn></msub><mspace linebreak="newline"></mspace><mi>x</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>30</mn><msub><mi>i</mi><mn>3</mn></msub></math></p><p>By using Kirchhoff&#39;s law,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><msub><mi>i</mi><mn>2</mn></msub><mo>+</mo><msub><mi>i</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>30</mn><mo>-</mo><mi>x</mi></mrow><mn>10</mn></mfrac><mo>+</mo><mfrac><mrow><mn>12</mn><mo>-</mo><mi>x</mi></mrow><mn>20</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mo>-</mo><mi>x</mi></mrow><mn>30</mn></mfrac><mo>=</mo><mn>0</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mrow><mn>90</mn><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>18</mn><mo>-</mo><mn>1</mn><mo>.</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>2</mn><mo>-</mo><mi>x</mi></mrow><mn>30</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>The current through the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>2</mn></msub><mo>=</mo><mfenced><mfrac><mrow><mn>30</mn><mo>-</mo><mn>12</mn></mrow><mn>20</mn></mfrac></mfenced><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>i</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>8</mn><mn>20</mn></mfrac><mi mathvariant="normal">A</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q12. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> wire is bent to form a square loop. A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> supply having an internal resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is connected across one of its sides. The potential drop across the diagonals of the square loop is __________<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **45**

**Detailed Solution:**

<p>Here assume current as</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/93dac662-2a12-4738-9d66-7ca0a830ecb6-image.png" style="width: 277px; height: 204px;" /></p><p>By KVL in the outer loop</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo><mn>12</mn><mi>i</mi><mo>-</mo><mn>4</mn><mi>i</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mi>i</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>i</mi><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn><mo>.</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>45</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p>

</details>

---

### Q13. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ca83c9ae-b4a8-4983-b32d-fabd99efad48-image.png" style="width: 411px; height: 162px;" /></p><p>The value of current in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a182b373-0060-4513-a814-7ea6e118cd32-image.png" style="width: 383px; height: 187px;" /></p><p>Applying <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mi>C</mi><mi>L</mi></math> at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>V</mi><mo>-</mo><mn>0</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mi>V</mi><mo>-</mo><mn>90</mn></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mrow><mi>V</mi><mo>-</mo><mn>140</mn></mrow><mn>20</mn></mfrac><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mo>&#160;</mo><mi>V</mi><mo>+</mo><mn>12</mn><mo>&#160;</mo><mi>V</mi><mo>-</mo><mn>1080</mn><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>V</mi><mo>-</mo><mn>420</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>V</mi><mo>=</mo><mn>60</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Current in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">V</mi><mo>-</mo><mn>0</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
Hence, option <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo></math></p>

</details>

---

### Q14. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>In the figure shown, the current in the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery is close to :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0cab1338-8121-4a0a-8869-73f3cd83eeff-image.png" style="width: 339px; height: 180px;" />    </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>71</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from positive to negative terminal
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>42</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from positive to negative terminal
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>21</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from positive to negative terminal
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>36</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from negative to postive terminal

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>21</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from positive to negative terminal**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/88d104b5-65d3-4d11-abfb-7149da8732fc-image.png" style="width: 337px; height: 200px;" />  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>-</mo><mn>10</mn><mfenced><mrow><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mn>2</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>-</mo><mn>17</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>+</mo><mn>20</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>10</mn><mo>+</mo><mn>4</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><mfenced><mrow><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>+</mo><mn>10</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><mn>17</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><mn>20</mn><mo>&#8594;</mo><mo>&#215;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn><mo>&#8594;</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>138</mn><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mfrac><mn>30</mn><mn>138</mn></mfrac><mo>=</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>217</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub></math> is negative it means current flows from positive to negative terminal</p><p> </p>

</details>

---

### Q15. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>In the circuit, given in the figure currents in different branches and value of one resistor are shown. Then potential at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with respect to the point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1af15679-6a09-455c-b818-e52fcfe0d8d1-image.png" style="width: 254px; height: 163px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>2</mn><mi>V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mi>V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8211;</mo><mn>1</mn><mi>V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>1</mn><mi>V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>1</mn><mi>V</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1af15679-6a09-455c-b818-e52fcfe0d8d1-image.png" style="width: 254px; height: 163px;" /></p><p>Using kirchhoff&#39;s law in the circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi><mi>D</mi><mi>B</mi></math>, we get</p><p>Voltage at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>= voltage at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> + voltage of battery of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> + potential difference across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance - voltage of battery of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">A</mi></msub><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>(</mo><mn>1</mn><mo>)</mo><mo>-</mo><mn>2</mn><mo>=</mo><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">B</mi></msub></math></p><p>Now potential at point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> with respect to point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>V</mi><mi>B</mi></msub><mo>-</mo><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q16. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit diagram, the currents, <math><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mo>-</mo><mn>0.3</mn><mtext>&#8201;</mtext><mi>A</mi><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi>I</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>0.8</mn><mtext>&#8201;</mtext><mi>A</mi></math> and <math><msub><mrow><mi>I</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>0.4</mn><mtext>&#8201;</mtext><mi>A</mi><mo>,</mo></math> are flowing as shown. The currents <math><msub><mrow><mi>I</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mtext>&#8201;</mtext><msub><mrow><mi>I</mi></mrow><mrow><mn>3</mn></mrow></msub></math> and <math><msub><mrow><mi>I</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>,</mo></math> respectively, are:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b9b6f02e-f843-44bb-a305-7827dec8f2bb-image.png" style="width: 300px; height: 176px;" />

**Options:**

- **(A)** <math><mn>0.4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>1.1</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi></math>
- **(B)** <math><mn>1.1</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mo>-</mo><mn>0.4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi></math>
- **(C)** <math><mn>1.1</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi></math>
- **(D)** <math><mo>-</mo><mn>0</mn><mo>.</mo><mn>4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0</mn><mo>.</mo><mn>4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>1</mn><mo>.</mo><mn>1</mn><mtext> </mtext><mi>A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1.1</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi><mo>,</mo><mtext> </mtext><mn>0.4</mn><mtext> </mtext><mi>A</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>i</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>=</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>3</mn><mi mathvariant="normal">A</mi><mo>,</mo><msub><mi mathvariant="normal">I</mi><mn>4</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn><mi mathvariant="normal">A</mi><mo>,</mo><msub><mi mathvariant="normal">I</mi><mn>5</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mi mathvariant="normal">A</mi><mo>,</mo><mspace linebreak="newline"/><mi>i</mi><mi>n</mi><mo>&#160;</mo><mi>s</mi><mi>e</mi><mi>r</mi><mi>i</mi><mi>e</mi><mi>s</mi><mo>&#160;</mo><mi>c</mi><mi>o</mi><mi>n</mi><mi>n</mi><mi>e</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>c</mi><mi>u</mi><mi>r</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mo>&#160;</mo><mi>w</mi><mi>i</mi><mi>l</mi><mi>l</mi><mo>&#160;</mo><mi>b</mi><mi>e</mi><mo>&#160;</mo><mi>s</mi><mi>a</mi><mi>m</mi><mi>e</mi><mo>,</mo><mo>&#160;</mo><mi>h</mi><mi>e</mi><mi>n</mi><mi>c</mi><mi>e</mi><mo>&#160;</mo><msub><mi mathvariant="normal">I</mi><mn>5</mn></msub><mo>=</mo><msub><mi mathvariant="normal">I</mi><mn>6</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mi mathvariant="normal">A</mi><mo>,</mo><mspace linebreak="newline"/><mi>A</mi><mi>c</mi><mi>c</mi><mi>o</mi><mi>r</mi><mi>d</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo>&#160;</mo><mi>t</mi><mi>o</mi><mo>&#160;</mo><mi>k</mi><mi>i</mi><mi>r</mi><mi>c</mi><mi>h</mi><mi>o</mi><mi>f</mi><mi>f</mi><mo>'</mo><mi>s</mi><mo>&#160;</mo><mi>j</mi><mi>u</mi><mi>n</mi><mi>c</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>r</mi><mi>u</mi><mi>l</mi><mi>e</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mi>l</mi><mi>g</mi><mi>e</mi><mi>b</mi><mi>r</mi><mi>a</mi><mi>i</mi><mi>c</mi><mo>&#160;</mo><mi>s</mi><mi>u</mi><mi>m</mi><mo>&#160;</mo><mi>o</mi><mi>f</mi><mo>&#160;</mo><mi>t</mi><mi>h</mi><mi>e</mi><mo>&#160;</mo><mi>c</mi><mi>u</mi><mi>r</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi>s</mi><mo>&#160;</mo><mi>m</mi><mi>e</mi><mi>e</mi><mi>t</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo>&#160;</mo><mi>a</mi><mi>t</mi><mo>&#160;</mo><mi>t</mi><mi>t</mi><mi>h</mi><mi>e</mi><mo>&#160;</mo><mi>j</mi><mi>u</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>i</mi><mi>s</mi><mo>&#160;</mo><mi>z</mi><mi>e</mi><mi>r</mi><mi>o</mi><mo>.</mo><mspace linebreak="newline"/><mi>i</mi><mo>.</mo><mi>e</mi><mo>&#160;</mo><mi>c</mi><mi>u</mi><mi>r</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi>s</mi><mo>&#160;</mo><mi>f</mi><mi>l</mi><mi>o</mi><mi>w</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo>&#160;</mo><mi>i</mi><mi>n</mi><mi>t</mi><mi>o</mi><mo>&#160;</mo><mi>t</mi><mi>h</mi><mi>e</mi><mo>&#160;</mo><mi>j</mi><mi>u</mi><mi>n</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>i</mi><mi>s</mi><mo>&#160;</mo><mi>t</mi><mi>a</mi><mi>k</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>a</mi><mi>s</mi><mo>&#160;</mo><mi>p</mi><mi>o</mi><mi>s</mi><mi>i</mi><mi>t</mi><mi>i</mi><mi>v</mi><mi>e</mi><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mi>c</mi><mi>u</mi><mi>r</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mo>&#160;</mo><mi>f</mi><mi>l</mi><mi>o</mi><mi>w</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo>&#160;</mo><mi>o</mi><mi>u</mi><mi>t</mi><mo>&#160;</mo><mi>o</mi><mi>f</mi><mo>&#160;</mo><mi>t</mi><mi>h</mi><mi>e</mi><mo>&#160;</mo><mi>j</mi><mi>u</mi><mi>n</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi>i</mi><mi>s</mi><mo>&#160;</mo><mi>t</mi><mi>a</mi><mi>k</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>a</mi><mi>s</mi><mo>&#160;</mo><mi>n</mi><mi>e</mi><mi>g</mi><mi>a</mi><mi>t</mi><mi>i</mi><mi>v</mi><mi>e</mi><mo>.</mo><mspace linebreak="newline"/><mi>A</mi><mi>t</mi><mo>&#160;</mo><mi>t</mi><mi>h</mi><mi>e</mi><mo>&#160;</mo><mi>j</mi><mi>u</mi><mi>n</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>-</mo><msub><mi mathvariant="normal">I</mi><mn>4</mn></msub><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><mo>-</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>-</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>.</mo><mn>1</mn><mi mathvariant="normal">A</mi><mspace linebreak="newline"/><mi>At</mi><mo>&#160;</mo><mi>junction</mi><mo>&#160;</mo><mi mathvariant="normal">Q</mi><mo>,</mo><mspace linebreak="newline"/><mo>&#160;</mo><msub><mi mathvariant="normal">I</mi><mn>6</mn></msub><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>3</mn></msub><mo>-</mo><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mo>-</mo><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>+</mo><msub><mi mathvariant="normal">I</mi><mn>3</mn></msub><mo>-</mo><mn>1</mn><mo>.</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>.</mo><mn>3</mn><mo>=</mo><mn>0</mn><mspace linebreak="newline"/><mo>&#8658;</mo><msub><mi mathvariant="normal">I</mi><mn>3</mn></msub><mo>=</mo><mn>1</mn><mo>.</mo><mn>1</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>7</mn><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn><mi mathvariant="normal">A</mi></math>It is problem of kirchhof&#39;s current law.

<math><msub><mrow><mi>I</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>=</mo><mn>0.4</mn><mi>&#160;</mi><mi>A</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mn>0.8</mn><mi>&#160;</mi><mi>A</mi><mo>-</mo><mi>O</mi><mo>.</mo><mn>4</mn><mi>A</mi><mo>=</mo><mn>0.4</mn><mo>&#160;</mo><mi>A</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfenced separators="|"><mrow><mn>0.8</mn><mo>+</mo><mn>0.3</mn></mrow></mfenced><mi>A</mi><mo>=</mo><mn>1.1</mn><mi>&#160;</mi><mi>A</mi></math>

</details>

---

### Q17. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the circuit shown, the potential difference between $\mathrm{A}$ and $B$ is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/hV08eiGJ8CdHXXYggRMCLoJpA9SmTNg9bcAnQOKcGVo.original.fullsize.png">

**Options:**

- **(A)** $1 \mathrm{~V}$
- **(B)** $2 \mathrm{~V}$
- **(C)** $3 V$
- **(D)** $6 \mathrm{~V}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2 \mathrm{~V}$**

**Detailed Solution:**

Given, $E_{1}=1 \mathrm{~V}, \mathrm{E}_{2}=2 \mathrm{~V}, \mathrm{E}_{3}=3 \mathrm{~V}, \mathrm{r}_{1}=1 \Omega$

$\mathrm{r}_{2}=1 \Omega$ and $\mathrm{r}_{3}=1 \Omega$

$\mathrm{V}_{\mathrm{AB}}=\mathrm{V}_{\mathrm{CD}}=\frac{\frac{\mathrm{E}_{1}}{\mathrm{r}_{1}}+\frac{\mathrm{E}_{2}}{\mathrm{r}_{2}}+\frac{\mathrm{E}_{3}}{\mathrm{r}_{3}}}{\frac{1}{\mathrm{r}_{1}}+\frac{1}{\mathrm{r}_{2}}+\frac{1}{\mathrm{r}_{3}}}=\frac{1}{\frac{1}{1}+\frac{1}{1}+\frac{1}{1}+\frac{3}{1}}=\frac{6}{3}=2 \mathrm{~V}$

</details>

---

### Q18. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit the cells have zero internal resistance. The currents (in amperes) passing through resistance <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> respectively, are:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9de4db59-eeb9-4f61-9395-1380647b6b40-image.png" style="width: 250px; height: 149px;" />

**Options:**

- **(A)** <math><mn>0</mn><mo>,</mo><mi> </mi><mn>1</mn></math>
- **(B)** <math><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn></math>
- **(C)** <math><mn>0.5</mn><mi> </mi><mo>,</mo><mi> </mi><mn>0</mn></math>
- **(D)** <math><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0.5</mn><mi> </mi><mo>,</mo><mi> </mi><mn>0</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c679c54d-f579-41a1-b391-efb3eaf08f26-image.png" style="width: 260px; height: 157px;" />

Assume <math><msub><mrow><mi>V</mi></mrow><mrow><mi>F</mi></mrow></msub></math> as <math><mn>0</mn></math>

<math> <mrow> <mi>a</mi><mi>s</mi><mtext>&#8201;</mtext><mtext>&#8201;</mtext><msub> <mi>V</mi> <mi>E</mi> </msub> <mo>=</mo><msub> <mi>V</mi> <mi>B</mi></msub></mrow></math>

<math><mo>&#8658;</mo></math> Current in <math> <mrow> <msub> <mi>R</mi> <mn>2</mn> </msub> </mrow> </math> is zero

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>V</mi><mi>D</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>I</mi><mo>=</mo><mfrac><mn>10</mn><mn>20</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> from <math><mi>A</mi></math> to <math><mi>D</mi></math>

</details>

---

### Q19. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

When the switch <math><mi>S</mi><mo>,</mo></math> in the circuit shown, is closed, then the value of current <math><mi>i</mi></math> will be:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/57e2d5e7-8fd6-4ca1-8325-ffc7ae3df691-image.png" style="width: 350px; height: 206px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4884fcdb-7201-41f9-a5d7-727920154f82-image.png" style="width: 350px; height: 203px;" />

<math><mi>i</mi><mo>=</mo><msub><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msub></math>

<math><mfrac><mrow><mi>V</mi><mo>-</mo><mn>0</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mi>V</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>10</mn><mo>-</mo><mi>V</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<math><mn>2</mn><mi>V</mi><mo>+</mo><mi>V</mi><mo>-</mo><mn>10</mn><mo>+</mo><mn>2</mn><mo>(</mo><mi>V</mi><mo>-</mo><mn>20</mn><mo>)</mo><mo>=</mo><mn>0</mn></math>

<math><mn>5</mn><mi>V</mi><mo>-</mo><mn>50</mn><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

</details>

---

### Q20. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The circuit shown here has two batteries of $8.0 \mathrm{~V}$ and $16.0 \mathrm{~V}$ and three resistors $3 \Omega, 9 \Omega$ and $9 \Omega$ and a capacitor of $5.0 \mu \mathrm{F}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ruMIBwDLv3t420IDSJu4USmJOX48Et7OwhI_TjiHHCU.original.fullsize.png">

How much is the current $\mathrm{I}$ in the circuit in steady state?

**Options:**

- **(A)** $1.6 \mathrm{~A}$
- **(B)** $0.67 \mathrm{~A}$
- **(C)** $2.5 \mathrm{~A}$
- **(D)** $0.25 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.67 \mathrm{~A}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/Kw2ny53nH6GJ9Vdz0Gm4lwdmLJCEWc_iYXMPqlctjXg.original.fullsize.png">

In steady state capacitor is fully charged hence no current will flow through line 2.
By simplyfing the circuit<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tb1veEjmkwMnuboQCsTv4zZPSRwcYe-BW__tR6Yzdu0.original.fullsize.png">

Hence resultant potential difference across resistances will be $8.0 \mathrm{~V}$.
Thus current $\mathrm{I}=\frac{\mathrm{V}}{\mathrm{R}}=\frac{8.0}{3+9}=\frac{8}{12}$
or, $\mathrm{I}=\frac{2}{3}=0.67 \mathrm{~A}$

</details>

---

### Q21. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

A $5 \mathrm{~V}$ battery with internal resistance $2 \Omega$ and a $2 \mathrm{~V}$ battery with internal resistance $1 \Omega$ are connected to a $10 \Omega$ resistor as shown in the figure. The current in the $10 \Omega$ resistor is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/P6SgtvvaC8-i4FIS80TCIiX8PxPEXJLQLDfeWoTMosE.original.fullsize.png">

**Options:**

- **(A)** $0.27 A P_2$ to $P_1$
- **(B)** $0.03 A P_1$ to $P_2$
- **(C)** $0.03 A P_2$ to $P_1$
- **(D)** $0.27 \mathrm{~A} \mathrm{P} P_1$ to $P_2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.03 A P_2$ to $P_1$**

**Detailed Solution:**

$$
\begin{aligned}
& V_{P_2}-V_{P_1}=\frac{\frac{5}{2}+\frac{0}{10}-\frac{2}{1}}{\frac{1}{2}+\frac{1}{10}+\frac{1}{1}} \\
& I=\frac{V_{P_2}-V_{P_1}}{10}=0.03 \text { from } P_2 \rightarrow P_1
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pbSNzkZRi6-ZJlBoRxqYD6XQr7THDLzGxp9K2YGDHg0.original.fullsize.png">

</details>

---

### Q22. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

The Kirchhoff's first law $\left(\sum i=0\right)$ and second law $\left(\sum i R=\sum E\right)$, where the symbols have their usual meanings, are respectively based on

**Options:**

- **(A)** conservation of charge, conservation of energy
- **(B)** conservation of charge, conservation of momentum
- **(C)** conservation of energy, conservation of charge
- **(D)** conservation of momentum, conservation of charge

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) conservation of charge, conservation of energy**

**Detailed Solution:**

Conservation of charge, conservation of energy

</details>

---

