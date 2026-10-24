# JEE Main Physics - Current Electricity

## Topic 4: Combination of Resistances

**Total Questions:** 74

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Refer to the figure given below, current between terminals $A$ and $B$ is _____ A.
<img style="width: 400px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS1__q38_d1.png" />

**Options:**

- **(A)** $12.5$
- **(B)** $1.25$
- **(C)** $7.5$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1.25$**

**Detailed Solution:**

The given circuit consists of four parallel branches connected between the left and right common vertical wires.

Let's find the equivalent electromotive force (EMF) and resistance for each branch:
For the top three active branches, each contains three $5\text{ V}$ cells and three $3\ \Omega$ resistors in series.
Equivalent EMF of each active branch, $E = 5 + 5 + 5 = 15\text{ V}$.
Equivalent resistance of each active branch, $R = 3 + 3 + 3 = 9\ \Omega$.

Since these three identical active branches are connected in parallel, we can replace them with a single equivalent voltage source:
Equivalent EMF, $E_{eq} = 15\text{ V}$ (as they are identical and in parallel).
Equivalent internal resistance, $R_{eq} = \dfrac{9}{3} = 3\ \Omega$.

The fourth (bottom) branch is connected between terminals $A$ and $B$ and acts as the load for this equivalent source. It contains three $3\ \Omega$ resistors in series.
Resistance of the branch $AB$, $R_{AB} = 3 + 3 + 3 = 9\ \Omega$.

Now, the circuit is simplified to an equivalent source of $15\text{ V}$ with internal resistance $3\ \Omega$ connected across a load of $9\ \Omega$.
The current $I$ flowing between terminals $A$ and $B$ (through the bottom branch) is given by Ohm's law:
$I = \dfrac{E_{eq}}{R_{eq} + R_{AB}}$

$I = \dfrac{15}{3 + 9} = \dfrac{15}{12}\text{ A}$

$I = 1.25\text{ A}$

Answer: $1.25$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two resistors of $200 \, \Omega$ and $400 \, \Omega$ are connected in series with a battery of $100$ V. A bulb rated at $200$ V, $100$ W is connected across the $400 \, \Omega$ resistance. The potential drop across the bulb is _______ V.

**Options:**

- **(A)** $25$
- **(B)** $50$
- **(C)** $66.6$
- **(D)** $100$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $50$**

**Detailed Solution:**

The resistance of the bulb is calculated using its power rating:

$R_b = \dfrac{V^2}{P} = \dfrac{200^2}{100} = 400 \, \Omega$

The bulb is connected in parallel with the $400 \, \Omega$ resistor. The equivalent resistance of this parallel combination is:

$R_p = \dfrac{400 \times 400}{400 + 400} = 200 \, \Omega$

This parallel combination is in series with the $200 \, \Omega$ resistor. The total equivalent resistance of the circuit is:

$R_{eq} = 200 + R_p = 200 + 200 = 400 \, \Omega$

The current drawn from the battery is:

$I = \dfrac{V}{R_{eq}} = \dfrac{100}{400} = 0.25 \text{ A}$

The potential drop across the bulb is the same as the potential drop across the parallel combination:

$V_p = I \times R_p = 0.25 \times 200 = 50 \text{ V}$

Answer: $50$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A regular hexagon is formed by six wires each of resistance $r \Omega$ and the corners are joined to the centre by wires of same resistance. If the current enters at one corner and leaves at the opposite corner, the equivalent resistance of the hexagon between the two opposite corners will be

**Options:**

- **(A)** $\frac{3}{4} r$
- **(B)** $\frac{4}{5} r$
- **(C)** $\frac{3}{5} r$
- **(D)** ${ }^{\frac{5}{8} r}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{5} r$**

**Detailed Solution:**

<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/24S2_s_42_1.png">
$R_{eq} = \dfrac{2R \times \dfrac{4R}{3}}{2R + \dfrac{4R}{3}} = \dfrac{8R^2}{10R} = \dfrac{4}{5}R$

</details>

---

### Q4. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of uniform resistance $\lambda \Omega / \mathrm{m}$ is bent into a circle of radius $r$ and another piece of wire with length $2 r$ is connected between points $A$ and $B(A O B)$ as shown in figure. The equivalent resistance between points $A$ and $B$ is $\_\_\_\_$ $\Omega$. 
 <img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/23S1_q_31_1.png">

**Options:**

- **(A)** $\frac{3 \pi \lambda r}{8}$
- **(B)** $\frac{6 \pi \lambda r}{3 \pi+16}$
- **(C)** $2 \pi \lambda r$
- **(D)** $(\pi+1) 2 r \lambda$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{6 \pi \lambda r}{3 \pi+16}$**

**Detailed Solution:**

The wire bent into a circle of radius $r$ has resistance $\lambda \cdot \pi r$ for the semicircular arcs, and the straight wire of length $2r$ has resistance $\lambda \cdot 2r$. The three paths between A and B (two semicircular arcs of the circle and one straight wire through center) are in parallel.

$\frac{1}{R_{AB}} = \frac{2}{\lambda \pi r} + \frac{1}{\lambda \cdot 2r} + \frac{2}{\lambda \cdot 3\pi r}$

$= \frac{1}{\lambda r} \left[\frac{2}{\pi} + \frac{1}{2} + \frac{2}{3\pi}\right]$

$= \frac{1}{\lambda r} \left(\frac{12 + 3\pi + 4}{6\pi}\right) = \frac{1}{\lambda r} \cdot \frac{16 + 3\pi}{6\pi}$

$R_{AB} = \lambda r \left(\frac{6\pi}{16 + 3\pi}\right) = \frac{6\pi \lambda r}{3\pi + 16}$

</details>

---

### Q5. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two known resistances of $R \Omega$ and $2 R \Omega$ and one unknown resistance $X \Omega$ are connected in a circuit as shown in the figure. If the equivalent resistance between points $A$ and $B$ in the circuit is $X \Omega$, then the value of $X$ is $\_\_\_\_$ $\Omega$.
<img style="width:300px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/21S2_q_26_1.png">

**Options:**

- **(A)** $(\sqrt{3}-1) R$
- **(B)** $2(\sqrt{3}-1) R$
- **(C)** $(\sqrt{3}+1) R$
- **(D)** $R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $(\sqrt{3}-1) R$**

**Detailed Solution:**

The circuit has 2R and X in series (top branch) parallel to R (bottom branch).
The equivalent resistance is $R_{eq} = \frac{(2R + X) \cdot R}{3R + X} = X$.
Setting up the equation: $X(3R + X) = R(2R + X)$, which simplifies to $X^2 + 2RX - 2R^2 = 0$.
Using the quadratic formula: $X = \frac{-2R \pm 2R\sqrt{3}}{2} = R(-1 \pm \sqrt{3})$.
Since resistance must be positive, $X = (\sqrt{3} - 1)R$ Ω.

</details>

---

### Q6. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

From the combination of resistors with resistance values $R_1=R_2=R_3=5 \Omega$ and $R_4=10 \Omega$, which of the following combination is the best circuit to get an equivalent resistance of $6 \Omega$ ?

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/murTcJ6ozPPrm-iCZ98eyG6XffntPFiIFOMJVSLZu1g.original.fullsize.png"/>
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/gba4qCYqRlBtlUkq461q2PlEm7e6eaOtQqMT1w_0Pcs.original.fullsize.png"/>
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/yqDzzYMdLCgsMCjbeWj5gRMI2A49qVkyLhWS45DX684.original.fullsize.png"/>
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/L0AuRUlpE8uEl4ey3EluoX_Xf1FNURnhshX_8UdyvgQ.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/murTcJ6ozPPrm-iCZ98eyG6XffntPFiIFOMJVSLZu1g.original.fullsize.png"/>**

**Detailed Solution:**

$\frac{1}{\mathrm{R}_{\mathrm{P}}}=\frac{1}{10}+\frac{1}{15}=\frac{3+2}{30}=\frac{1}{6}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/33q5JbvhlPXwMoncpjE9Yn5vCIsihKGJDPL_8ucXCXs.original.fullsize.png"/>

</details>

---

### Q7. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Find the equivalent resistance between two ends of the following circuit
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5mfVNPnax-j84SFvQlBMweLNPar_xfd6C_wofN7bdH0.original.fullsize.png"/>

**Options:**

- **(A)** $\frac{r}{9}$
- **(B)** $\frac{\mathrm{r}}{3}$
- **(C)** r
- **(D)** $\frac{\mathrm{r}}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{r}{9}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MqT67CWo1KOYBXvdvP5HG6ubigMp9d8wZuKxgWg584Q.original.fullsize.png">


All are in parallel
$\mathrm{R}_{\mathrm{eq}}=\frac{\mathrm{r} / 3}{3}=\mathrm{r} / 9$

</details>

---

### Q8. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of resistance R is bent into an equilateral triangle and an identical wire is bent into $a$ square. The ratio of resistance between the two end points of an edge of the triangle to that of the square is
Options

**Options:**

- **(A)** 8/9
- **(B)** $27 / 32$
- **(C)** $32 / 27$
- **(D)** $9 / 8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $32 / 27$**

**Detailed Solution:**

For the wire bent into an equilateral triangle, each side has a resistance $\frac{R}{3}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/K_k2zGFxLJ3eLJlxsX7dg1x1amevucLIUZEZFL6Ioqw.original.fullsize.png">
$R_{\text {eq }}=\frac{\left(\frac{2 R}{3}\right)\left(\frac{R}{3}\right)}{\frac{2 R}{3}+\frac{R}{3}}=\frac{2 R}{9}=R_1$ (lets say)
For the wire bent into a square, each side has a resistance $\frac{R}{4}$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/DMomNIulDwj5wPsA5Yqu-QDOWLMCDVlijXTSTb1VnSI.original.fullsize.png">
$\begin{aligned} & R_{\text {eq }}=\frac{\left(\frac{3 R}{4}\right)\left(\frac{R}{4}\right)}{\frac{3 R}{4}+\frac{R}{4}}=\frac{3 R}{16}=R_3 \text { (lets say) } \\ & \Rightarrow \frac{R_1}{R_3}=\frac{\frac{2 R}{9}}{\frac{3 R}{16}}=\frac{32}{27}\end{aligned}$

</details>

---

### Q9. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

To determine the resistance $(R)$ of a wire, a circuit is designed below. The $V-I$ characteristic curve for this circuit is plotted for the voltmeter and the ammeter readings as shown in figure. The value of $R$ is ______ $\Omega$.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/K4bbpJ2wVDkmLLMaNHkodo_mttVD857_MbrIQUSt6xg.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2500**

**Detailed Solution:**

$\begin{aligned} & \text { Req }=\frac{10^4 R}{10^4+R} \\ & E=4 V, I=2 m A \\ & I=\frac{E}{R e q} \Rightarrow 2 \times 10^{-3}=\frac{4\left(10^4+R\right)}{10^4 R} \\ & \Rightarrow 20 R=40000+4 R\end{aligned}$
$\begin{aligned} & 16 R=40000 \\ & R=2500 \Omega\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The effective resistance between $A$ and $B$, if resistance of each resistor is $R$, will be
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/aQr027cTizDQ5UgwIYc_8lxowfJiZ5Y15gOpNZ3VKZE.original.fullsize.png">

**Options:**

- **(A)** $\frac{8 R}{3}$
- **(B)** $\frac{5 R}{3}$
- **(C)** $\frac{4 R}{3}$
- **(D)** $\frac{2}{3} R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{8 R}{3}$**

**Detailed Solution:**

From symmetry we can remove two middle resistance.
New circuit is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/s5cUnZL-5FhTJtIgzmgmyCPiKhtlKGcDcLXpLdXmlPQ.original.fullsize.png"/><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JW5YCRgJFqAoExtcpxbH2T3vCsUAE5xrYy8LwdVrdAQ.original.fullsize.png"/><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-RFW1-8rEOSrhaABcbMVLRqN795NvNIpMUJ7yhP7flg.original.fullsize.png"/><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tTOOh8s3Zyd7bOJw6A2-7PiCVxb3Hk-VHXJZ1GUJq4o.original.fullsize.png"/>

</details>

---

### Q11. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The equivalent resistance between $\mathrm{A}$ and $\mathrm{B}$ is :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/WxXU4yqReEfAuLwQ33ZaaSi5FhGXK-WhGaVQbMSLr1Y.original.fullsize.png">

**Options:**

- **(A)** $18 \Omega$
- **(B)** $19 \Omega$
- **(C)** $25 \Omega$
- **(D)** $27 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $19 \Omega$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/JK1HRf2CBoI8BRsYad4yQGPgaVkfW5Aic-e3qUvCmX8.original.fullsize.png">
$\Rightarrow \mathrm{R}_{\mathrm{eq}}=6 \Omega+5 \Omega+8 \Omega=19 \Omega$

</details>

---

### Q12. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

A wire of resistance $20 \Omega$ is divided into 10 equal parts, resulting pairs. A combination of two parts are connected in parallel and so on. Now resulting pairs of parallel combination are connected in series. The equivalent resistance of final combination is _____ $\Omega$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/YS9YIvMwQjSEwiNOPV4cqQLz1eM7iCA5IaWu3M_bsTM.original.fullsize.png">
Each part has resistance $=2 \Omega$
2 parts are connected in parallel so, $\mathrm{R}=1 \Omega$
Now, there will be 5 parts each of resistance $1 \Omega$, they are connected in series.
$\mathrm{R}_{\mathrm{eq}}=5 \mathrm{R}, \mathrm{R}_{\mathrm{eq}}=5 \Omega$

</details>

---

### Q13. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the given figure $\mathrm{R}_1=10 \Omega, \mathrm{R}_2=8 \Omega, \mathrm{R}_3=4 \Omega$ and $\mathrm{R}_4=8 \Omega$. Battery is ideal with emf $12 \mathrm{~V}$. Equivalent resistant of the circuit and current supplied by battery are respectively :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/m6wMnk96Z0dPiRSpg1pqKXM__ibr8Vp6m7nrc8bZ4yY.original.fullsize.png">

**Options:**

- **(A)** $10.5 \Omega$ and $1.14 \mathrm{~A}$
- **(B)** $12 \Omega$ and $1 \mathrm{~A}$
- **(C)** $10.5 \Omega$ and $1 \mathrm{~A}$
- **(D)** $12 \Omega$ and $11.4 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $12 \Omega$ and $1 \mathrm{~A}$**

**Detailed Solution:**

Here $\mathrm{R}_2, \mathrm{R}_3, \mathrm{R}_4$ are in parallel
$\begin{aligned}
& \frac{1}{\mathrm{R}_{234}}=\frac{1}{\mathrm{R}_2}+\frac{1}{\mathrm{R}_3}+\frac{1}{\mathrm{R}_4} \\
& \mathrm{R}_{234}=2 \Omega
\end{aligned}$
$R_{234}$ is in series with $R_1$ so
$\begin{aligned}
& \mathrm{R}_{\mathrm{eq}}=\mathrm{R}_{234}+\mathrm{R}_1=2+10=12 \Omega \\
& \mathrm{i}=\frac{12}{12}=1 \mathrm{Amp}
\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (04 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Twelve wires each having resistance $2 \Omega$ are joined to form a cube. A battery of $6 \mathrm{~V}$ emf is joined across point $a$ and $c$. The voltage difference between $e$ and $f$ is ______V.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/pyHhpUz-LETgJCEdKvcCwwxvjzgSfvQJeIKapO253dg.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/GLYUgvMJndBFRP7jigwkuCsBdKJu0sgbzPRGrqeg0aE.original.fullsize.png">
From symmetry, current through e-b & g-d =0
$\begin{aligned}
& \therefore \mathrm{R}_{\text {eq }}=\frac{3}{4} \times \mathrm{R}=\frac{3}{2} \Omega \\
& \therefore \text { Current through battery }=\frac{6 \times 2}{3}=4 \mathrm{~A} \\
& \mathrm{i}_2=\frac{4}{8} \times 2=1 \mathrm{~A} \\
& \therefore \Delta \mathrm{V} \text { across e-f }=\frac{\mathrm{i}_2}{2} \times \mathrm{R}=\frac{1}{2} \times 2=1 \mathrm{~V}
\end{aligned}$

</details>

---

### Q15. JEE Main 2023 (15 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>A network of four resistances is connected to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery, as shown in figure. The magnitude of voltage difference between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is __________ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/37c13473-3b6b-4070-b6c7-78164ae09454.png" style="width: 240px; height: 303px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<blockquote><p>The resistance in each branch is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. They are in parallel. So, net resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#39;</mo><mo>=</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.</p><p>The total current flowing through the loop,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>V</mi><mrow><mi>R</mi><mo>&#39;</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Thus, through each branch the current is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p><p>Hence, the voltage difference across the points is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>V</mi><mi>B</mi></msub><mo>=</mo><mfenced><mrow><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p></blockquote>

</details>

---

### Q16. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>In the given circuit, the current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> through the battery will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8ecf003a-d9f6-46c3-941d-01e4a46a27bf.png" style="width: 300px; height: 205px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/55560a8f-5c72-4b07-a1d3-7cd4c51763be.png" style="width: 300px; height: 205px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d4ac53ce-104f-434c-a6ce-916176c31ffe.png" style="width: 250px; height: 199px;" /></p><p>In the first circuit diagram, the diodes <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>1</mn></msub><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>D</mi><mn>3</mn></msub></math> are forward biased and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mn>2</mn></msub></math> is reverse biased(Hence, no current through it). So the circuit is simplified to the second diagram.</p><p>Hence, the equivalent resistance is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>10</mn></mrow><mrow><mn>20</mn><mo>+</mo><mn>10</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>20</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Using Ohm&#39;s law, the current is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>10</mn><mstyle displaystyle="true"><mfrac><mn>20</mn><mn>3</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>30</mn><mn>20</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q17. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/136aee8b-f116-4a95-9ad6-f35140fc48f7.png" style="width: 393px; height: 346px;" />
The current flowing through <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/136aee8b-f116-4a95-9ad6-f35140fc48f7.png" style="width: 393px; height: 346px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/45f8a1f9-0e33-4c4c-b64c-05ce66012735.png" style="width: 276px; height: 301px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d2a4098a-f7e1-4d86-9c0d-7e7af595dc1f.png" style="width: 295px; height: 296px;" /></p><p>As can be seen from the first circuit above, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>B</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>A</mi><mi>B</mi></math> are in series which is in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>A</mi></math>. So, the net resistance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#39;</mo><mo>=</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> as shown in the second diagram.</p><p>From the second diagram, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>C</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>C</mi><mi>A</mi></math> is in series which is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mi>A</mi></math>. Hence the resistance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#39;</mo><mo>&#39;</mo><mo>=</mo><mfenced><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>3</mn></mrow><mrow><mo>(</mo><mn>6</mn><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></mfenced><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> as shown in third diagram.</p><p>From third diagram, both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>D</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>D</mi><mi>A</mi></math> are in series which is parallel to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>A</mi></math>.</p><p>The equivalent resistance as can be seen from the above simplified circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.</p><p> The current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> through battery, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>2</mn></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p><p>From the second diagram, the part <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>D</mi><mi>A</mi><mi>C</mi><mi>D</mi></math> has a resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, the total current will divide equally between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>D</mi><mi>A</mi><mi>C</mi><mi>D</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>E</mi><mi>A</mi></math>. So consider <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> flowing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>D</mi></math>. Note that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math> will be the same current flowing in the first diagram through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mi>D</mi></math>.</p><p>From first diagram, when the resistances are in parallel the current is divided in the inverse ratio. Thus,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#39;</mo></math> through <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>D</mi><mo>=</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#39;</mo><mo>&#39;</mo></math> through <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q18. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> resistors each of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mo>&#8486;</mo></math> can be connected in such as to get maximum and minimum equivalent resistance. The ratio of maximum and minimum equivalent resistance will be________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

<blockquote><p>When all the resistors are connected in series, the total resistance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><mo>=</mo><mn>10</mn><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>max</mi></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>When all the resistors are connected in parallel, the total resistance is</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mi>R</mi><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>min</mi></msub><mo>=</mo><mfrac><mn>10</mn><mn>10</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Hence, the ratio,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mrow><mi>m</mi><mi>a</mi><mi>x</mi></mrow></msub><msub><mi>R</mi><mrow><mi>m</mi><mi>i</mi><mi>n</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac><mo>=</mo><mn>100</mn></math>.</p></blockquote>

</details>

---

### Q19. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The equivalent resistance of the circuit shown below between points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is :</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/74b8b29b-b5ea-4fc8-8a88-2433ea68bb71.png" style="width: 300px; height: 303px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fc361815-e504-4783-a2ff-6777aa56ac3d.png" style="width: 250px; height: 255px;" /></p><p>The resistance in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi></math> is parallel to all other resistances. Since all the resistances other than <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>b</mi></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> the potential is zero<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>V</mi><mi>x</mi></msub><mo>=</mo><msub><mi>V</mi><mi>y</mi></msub></mrow></mfenced></math> as the upper branch will become a case of balanced wheatstone bridge between <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>x</mi></msub><mo>&#38;</mo><msub><mi>V</mi><mi>y</mi></msub></math>. So, the simplified circuit looks like the one below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6cd3aef0-bf8a-4c14-a9a3-ab08a39787f8.png" style="width: 250px; height: 236px;" /></p><p>Hence, the equivalent resistance is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>16</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>=</mo><mn>3</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q20. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The equivalent resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi></math> as shown in figure is:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cad03f2e-d481-4bd1-9b22-cef1165eb44d-image.png" style="width: 400px; height: 86px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>k&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>k&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi>k&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>&#160;</mo><mi>k&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi>k&#937;</mi></math>**

**Detailed Solution:**

<blockquote><p>The equivalent circuit of the given configuration can be drawn as follows:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f56dad99-58be-4d04-b41a-4d678242a72b.png" style="width: 662px; height: 103px;" /></p><p>With reference to the above diagram, the equivalent resistance of the given configuration can be calculated as follows:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><mn>1</mn><mi>R</mi></mfrac></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mrow><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mrow><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>R</mi><mo>=</mo><mo>&#160;</mo><mn>5</mn><mi mathvariant="normal">&#937;</mi></mtd></mtr></mtable></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>In the given circuit the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub></mrow><msub><mi>I</mi><mn>2</mn></msub></mfrac></mfenced></math> is:</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4f28a9fc-ac4d-4fc3-9c6e-ea2acf32a528-9896822.PNG" style="width: 362px; height: 250px;" /> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c07bc657-e733-4881-94a6-90e5ed5b9b68-9896822_1.PNG" style="width: 351px; height: 260px;" /></p><p>Potential distribution at each point in the circuit is shown in above diagram.</p><p>Since, both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistors are maintained at same potential difference, so current will be same, thus, using Ohm&#39;s law, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>I</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>20</mn><mo>-</mo><mn>10</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Now, current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>10</mn><mn>10</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mfrac><mrow><msub><mi>I</mi><mn>1</mn></msub><mo>+</mo><msub><mi>I</mi><mn>3</mn></msub></mrow><msub><mi>I</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>1</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q22. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Equivalent resistance between the adjacent corners of a regular <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-sided polygon of uniform wire of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> would be :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>R</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mi>R</mi></mstyle></mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mi>R</mi></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mi>R</mi></mstyle></mrow><mi>n</mi></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>R</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></math>**

**Detailed Solution:**

<p>Given the total resistance of the wire is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. If the polygon has <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> numbers of side, then the resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>r</mi></mfenced></math>, as shown in the following figure, of each side can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mo>&#160;</mo><mfrac><mi>R</mi><mi>n</mi></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6e595b63-e39b-423f-97d2-f24d7beb398a-9896616.png" style="width: 300px; height: 342px;" /></p><p>Among all the resistances, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> resistances are connected in series combination, whereas, their equivalent resistance is connected in parallel with the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mi>th</mi></msup></math> resistance. The equivalent circuit diagram for the above set of resistances can be depicted as follows:</p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2d590221-a22b-416e-bf69-c761ee2bb75e-9896616_2.png" style="width: 500px; height: 169px;" /></p><p>From the above equivalent circuit diagram, the net equivalent resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfenced></math> for the entire combination can be calculated as follows-</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><mn>1</mn><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfrac></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mi>r</mi></mstyle></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mfrac><mi>R</mi><mi>n</mi></mfrac></mstyle></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mstyle displaystyle="true"><mfrac><mi>R</mi><mi>n</mi></mfrac></mstyle></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mi>n</mi><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mi>R</mi></mstyle></mrow></mfrac><mo>+</mo><mfrac><mi>n</mi><mi>R</mi></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mstyle displaystyle="true"><mi>R</mi></mstyle></mrow></mfrac></mtd></mtr><mtr><mtd><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>R</mi></mrow><msup><mi>n</mi><mn>2</mn></msup></mfrac></mtd></mtr></mtable></math></p>

</details>

---

### Q23. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The equivalent resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mi>B</mi></math> of the network shown in figure:</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f1d535d5-6c3f-42fd-8e28-afd32829a589-9896252.PNG" style="width: 425px; height: 150px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>&#160;</mo><mi>R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>&#160;</mo><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi>R</mi></math>**

**Detailed Solution:**

<p>The given circuit can be redrawn as shown below:</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b1bf5b6f-65e7-45ff-b985-a3f8cfb03a29-9896252_1.PNG" style="width: 251px; height: 220px;" /></p><p>Since the circuit is in balanced wheatstone configuration, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mrow><mn>2</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>R</mi></mrow><mrow><mn>6</mn><mi>R</mi></mrow></mfrac></math>.</p><p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor can be omitted. Now, the circuit has two branches having two resistors connected in series. </p><p>Therefore, the resistance of upper branch is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>+</mo><mn>3</mn><mi>R</mi><mo>=</mo><mn>4</mn><mi>R</mi></math> and lower branch is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi><mo>+</mo><mn>6</mn><mi>R</mi><mo>=</mo><mn>8</mn><mi>R</mi></math>.</p><p>The equivalent resistance will therefore be:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>4</mn><mi>R</mi></mrow></mfenced><mfenced><mrow><mn>8</mn><mi>R</mi></mrow></mfenced></mrow><mrow><mn>4</mn><mi>R</mi><mo>+</mo><mn>8</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>32</mn><msup><mi>R</mi><mn>2</mn></msup></mrow><mrow><mn>12</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mi>R</mi></math></p>

</details>

---

### Q24. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>If the potential difference between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> is zero, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is ______.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdcbe7f9-686f-4a25-bb20-4085d35f9a69-9895901.PNG" style="width: 250px; height: 249px;" /> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fdcbe7f9-686f-4a25-bb20-4085d35f9a69-9895901.PNG" style="width: 250px; height: 249px;" /></p><p>As potential difference between B &amp; D is zero therefore it is a balanced wheatstone bridge. So, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><msub><mi>R</mi><mn>3</mn></msub><msub><mi>R</mi><mn>4</mn></msub></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>3</mn></mrow><mrow><mn>6</mn><mo>+</mo><mn>3</mn></mrow></mfrac></mstyle></mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>x</mi><mo>&#215;</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mstyle></mfenced><mi>x</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Hence, required <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn></math>.</p>

</details>

---

### Q25. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The equivalent resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>B</mi></math> is _______.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a7eb5601-62c0-4b97-b2d2-7b026607e965-9895383.PNG" style="width: 300px; height: 204px;" />.</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><mi>&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mi>&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#937;</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d1bf5624-bf81-4d21-9190-6ecfd114fedb-a7eb5601-62c0-4b97-b2d2-7b026607e965-9895383.PNG" style="width: 300px; height: 204px;" /></p><p>Point D and G are at same potential. Same is the case with point E and F.</p><p>Now, resistance between DC and GC are in parallel combination. Similarly, resistance between CE and CF are in parallel combination. The modified circuit will be as shown below considering <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac></math> for parallel combination.</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cdc02fbc-5891-4e5c-8043-eaee2132947e-9895383_1.PNG" style="width: 250px; height: 190px;" /></p><p>Therefore, we can write</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>6</mn></mrow><mn>12</mn></mfrac><mspace linebreak="newline"/><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mi>&#937;</mi></math></p>

</details>

---

### Q26. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>In the following circuit, the magnitude of current <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub></math>, is ______ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/278dd251-46e8-49a2-ba90-b39a6ce84adf-e04ec5aa-c38b-4e10-ab7f-f88e883bab0c-9895754.png" style="width: 300px; height: 312px;" /> </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9fea15ab-ad54-415e-9103-e81cc81868ea-d2954668-50f0-4ac0-9b3e-b82b787ed717-9895754_2.png" style="width: 300px; height: 328px;" /></p><p>The figure above shows the current and voltage at different points in circuit.</p><p>Applying Kirchhoff&#39;s Junction law at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>-</mo><mo>(</mo><mi>y</mi><mo>+</mo><mn>5</mn><mo>)</mo></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Applying Kirchhoff&#39;s Junction law at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>y</mi><mo>+</mo><mn>5</mn><mo>-</mo><mi>x</mi></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>2</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving equation (1) and (2), we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math></p><p>Now, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> junction</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><msub><mi>i</mi><mn>1</mn></msub><mo>+</mo><msub><mi>i</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>y</mi><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>0</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>0</mn><mo>-</mo><mn>0</mn></mrow><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>0</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>I</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p>

</details>

---

### Q27. JEE Main 2023 (25 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>In the given circuit, the equivalent resistance between the terminal A and B is ____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#937;</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e22dc111-e69c-4bea-a268-14d7d5011a56-9894227.png" style="width: 300px; height: 195px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e22dc111-e69c-4bea-a268-14d7d5011a56-9894227.png" style="width: 300px; height: 195px;" /></p><p>In the given circuit, both <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistors get shorted out, thus no current will flow from them. Removing the resistors from which no current will flow.</p><p>Now, the circuit can be redrawn as shown below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7c2a49c7-822c-41f6-b1fd-e2dd0fd9a8f1-9894227_2.png" style="width: 300px; height: 200px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mn>3</mn><mo>+</mo><mo>(</mo><mn>2</mn><mo>&#8214;</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mn>3</mn><mo>+</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q28. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A cell of emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is connected across series combination of two resistors each of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance. A voltmeter of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is used to measure the potential difference across each resistor. The reading of the voltmeter will be:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/600606ec-53ad-4fa1-a1b1-a67242e2a4ce-52d8e4b6-8788-47af-a2c6-6e89ec097a11-9894021.PNG" style="width: 300px; height: 198px;" /></p><p>As we know, voltmeter is connected in parallel to the element being measured.</p><p>The equivalent resistance of the above circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfenced><mfrac><mrow><mn>400</mn><mo>&#215;</mo><mn>100</mn></mrow><mrow><mn>400</mn><mo>+</mo><mn>100</mn></mrow></mfrac></mfenced><mo>+</mo><mn>100</mn><mo>=</mo><mn>80</mn><mo>+</mo><mn>100</mn><mo>=</mo><mn>180</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Current through the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>90</mn><mn>180</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Reading of the voltmeter is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>R</mi></msub><mo>=</mo><mi>i</mi><mfenced><mfrac><mrow><mn>400</mn><mo>&#215;</mo><mn>100</mn></mrow><mrow><mn>400</mn><mo>+</mo><mn>100</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>80</mn><mo>=</mo><mn>40</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q29. JEE Main 2023 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>As shown in the figure, a network of resistors is connected to a battery of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> with an internal resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi>&#937;</mi></math>. The currents through the resistors <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>4</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>5</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub></math> respectively. The values of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub></math> are:</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/85ba5823-cbd8-49a0-887e-794f93adfac0-c92d76d7-1078-44ad-a775-4cebb2b91aa4-9893516.PNG" style="width: 500px; height: 191px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>24</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>6</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>6</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>24</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/85ba5823-cbd8-49a0-887e-794f93adfac0-c92d76d7-1078-44ad-a775-4cebb2b91aa4-9893516.PNG" style="width: 500px; height: 191px;" /></p><p>Equivalent resistance of circuit
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mn>3</mn><mo>+</mo><mfenced><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn><mo>+</mo><mfenced><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>5</mn></mrow><mrow><mn>20</mn><mo>+</mo><mn>5</mn></mrow></mfrac></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>&#937;</mi></math></p><p>Current through battery <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>24</mn><mn>12</mn></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mfrac><msub><mi>R</mi><mn>5</mn></msub><mrow><msub><mi>R</mi><mn>4</mn></msub><mo>+</mo><msub><mi>R</mi><mn>5</mn></msub></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mn>5</mn><mrow><mn>20</mn><mo>+</mo><mn>5</mn></mrow></mfrac><mo>&#215;</mo><mn>2</mn><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>I</mi><mn>5</mn></msub><mo>=</mo><mi>i</mi><mo>-</mo><msub><mi>I</mi><mn>4</mn></msub><mo>=</mo><mn>2</mn><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p>

</details>

---

### Q30. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>The current I flowing through the given circuit will be _____  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9a53b4e8-ff18-4928-a1ca-eed3d6afe8cc-image.png" style="width: 200px; height: 136px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Here all resistors are in parallel, so the equivalent circuit can be redrawn as shown below.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/740265da-bd52-4b0c-86c0-6952b7014ff9-image.png" style="width: 300px; height: 168px;" /></p><p>As identical resistances are in parallel, so equivalent resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mn>9</mn><mn>3</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Now, current through circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>6</mn><mn>3</mn></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p></blockquote>

</details>

---

### Q31. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

An electrical bulb rated <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi><mo>,</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>, is connected in series with another bulb rated <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>. If the voltage across combination is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>, the power consumed by the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math> bulb will be about _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">W</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<blockquote><p>Electric power is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><msup><mi>V</mi><mn>2</mn></msup><mi>R</mi></mfrac></math>, here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is voltage and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is resistance.</p><p>Now, for each bulb, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><msup><mi>V</mi><mn>2</mn></msup><mi>P</mi></mfrac><mo>=</mo><mfrac><msup><mn>220</mn><mn>2</mn></msup><mn>100</mn></mfrac><mo>=</mo><mn>484</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><msup><mi>V</mi><mn>2</mn></msup><mi>P</mi></mfrac><mo>=</mo><mfrac><msup><mn>220</mn><mn>2</mn></msup><mn>60</mn></mfrac><mo>=</mo><mn>484</mn><mfenced><mfrac><mn>10</mn><mn>6</mn></mfrac></mfenced><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Net current through the series combination is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>220</mn><mrow><mn>484</mn><mo>+</mo><mn>484</mn><mo>&#215;</mo><mfrac><mn>10</mn><mn>6</mn></mfrac></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>171</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Hence, the power consumed by the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math> bulb is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub><mo>=</mo><msup><mi>I</mi><mn>2</mn></msup><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mn>14</mn><mo>.</mo><mn>06</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p></blockquote>

</details>

---

### Q32. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo> </mo><mi>mA</mi></math> flows in the circuit as shown in figure. The value of potential difference between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/69624889-0685-4e1c-9e36-985c9a1bf66e-image.png" style="width: 180px; height: 173px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>275</mn><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>275</mn><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d7e06131-e6b8-4769-bd25-6690fb0a29de-image.png" style="width: 200px; height: 184px;" /></p><p>Using current division rule, </p><p>Current, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>5</mn><mrow><mn>10</mn><mo>+</mo><mn>5</mn></mrow></mfrac><mo>&#215;</mo><mn>15</mn><mo>&#160;</mo><mi>mA</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>mA</mi></math></p><p>Now, using Kirchhoff&#39;s voltage law- in lower loop,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><mn>5</mn><mi>i</mi><mo>-</mo><mn>10</mn><msub><mi>i</mi><mn>1</mn></msub><mo>-</mo><mn>10</mn><mi>i</mi><mo>=</mo><msub><mi>V</mi><mi>B</mi></msub></math></p><p>Potential difference between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>V</mi><mi>B</mi></msub><mo>=</mo><mn>75</mn><mo>+</mo><mn>50</mn><mo>+</mo><mn>150</mn><mo>=</mo><mn>275</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p></blockquote>

</details>

---

### Q33. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Eight copper wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> and diameter d are joined in parallel to form a single composite conductor of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>. If a single copper wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>l</mi></math> have the same resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>R</mi></mfenced></math> then its diameter will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Each wire has resistance, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mi>&#961;</mi><mfrac><mrow><mn>4</mn><mi>l</mi></mrow><mrow><mi>&#960;</mi><msup><mi mathvariant="normal">d</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Eight wire in parallel, then equivalent resistance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mi>r</mi><mn>8</mn></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math></p><p>Single copper wire of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>l</mi></math> has resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mi>&#961;</mi><mfrac><mrow><mn>2</mn><mi>l</mi><mo>&#215;</mo><mn>4</mn></mrow><mrow><mi>&#960;</mi><msubsup><mi>d</mi><mn>1</mn><mn>2</mn></msubsup></mrow></mfrac></math>.</p><p>Comparing both equations, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi><mfrac><mrow><mn>8</mn><mi>l</mi></mrow><mrow><mi>&#960;</mi><msubsup><mi>d</mi><mn>1</mn><mn>2</mn></msubsup></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mrow><mn>2</mn><mi>&#960;</mi><msup><mi>d</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>d</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn><mi>d</mi></math></p></blockquote>

</details>

---

### Q34. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>In the given figure, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>0</mn></msub></math> will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/437c9d84-5670-4410-bd3a-9ec0f70e4bad-image.png" style="width: 230px; height: 181px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ffa45f55-2d2b-404f-8aa4-bd5546e3588a-40e43433-2430-440d-a987-f6e7ade1d2f2-image.png" style="width: 250px; height: 173px;" /></p><p>Using Kirchhoff&#39;s junction rule,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>2</mn></mrow><mrow><mn>1</mn><mo>&#160;</mo><mi>k&#937;</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>4</mn></mrow><mrow><mn>1</mn><mo>&#160;</mo><mi>k&#937;</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>6</mn></mrow><mrow><mn>1</mn><mo>&#160;</mo><mi>k&#937;</mi></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi>V</mi><mn>0</mn></msub><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>0</mn></msub><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p></blockquote>

</details>

---

### Q35. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Two resistors are connected in series across a battery as shown in figure. If a voltmeter of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2000</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>  is used to measure the potential difference across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resister, the reading of the voltmeter will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b1dab62b-4b3d-45d4-8ccd-3161eb1e4deb-image.png" style="width: 200px; height: 139px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4f97b341-f99e-4c10-bd42-3f892f0a45ad-image.png" style="width: 200px; height: 192px;" /></p><p>The voltmeter resistance is given to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2000</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. The equivalent resistance in the given circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>500</mn><mo>&#215;</mo><mn>2000</mn></mrow><mrow><mn>2000</mn><mo>+</mo><mn>500</mn></mrow></mfrac><mo>+</mo><mn>600</mn><mo>=</mo><mn>1000</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.</p><p>Now, current in the circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mn>20</mn><mn>1000</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p><p>Reading of the voltmeter will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>20</mn><mo>-</mo><mn>600</mn><mo>&#215;</mo><mfrac><mn>20</mn><mn>1000</mn></mfrac><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q36. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>All resistances in figure are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> each. The value of current &#39;<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math>&#39; is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is _____ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5e66ee68-f982-4233-9740-f49683194ce6-image.png" style="width: 350px; height: 217px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/8cd39d40-186d-47ca-8675-89ad2d232b53-image.png" style="width: 300px; height: 215px;" /></p><p>Each pair on the right side of the circuit is in parallel connection, hence it can be replaced by a resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>2</mn></mfrac></math> as shown.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fcb36ad6-95ee-4612-b1f0-8a4972255bc5-image.png" style="width: 310px; height: 148px;" /></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mi>r</mi><mn>2</mn></mfrac></math> in each branch on the right side is in series, hence combined resistance value will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mn>2</mn></mfrac></math>. Upper branch having resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mn>2</mn></mfrac></math> is in parallel with another <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mn>2</mn></mfrac></math>, hence it can be written as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>r</mi></mrow><mn>4</mn></mfrac></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/97933f2e-28b1-4739-8e05-d40f9c15f36b-image.png" style="width: 300px; height: 176px;" /></p><p>Further, simplified circuit will have net resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>7</mn><mi>r</mi></mrow><mn>8</mn></mfrac></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b88fa5bd-9115-4e56-b160-b41b894b50e0-image.png" style="width: 220px; height: 192px;" /></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mfrac><mrow><mn>7</mn><mi>r</mi></mrow><mn>8</mn></mfrac><mo>+</mo><mi>r</mi><mo>=</mo><mfrac><mn>7</mn><mn>8</mn></mfrac><mo>+</mo><mn>1</mn><mo>=</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p>Now, current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>3</mn><mstyle displaystyle="true"><mfrac><mn>15</mn><mn>8</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>Hence, value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>8</mn></math>.</p>

</details>

---

### Q37. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>In the given circuit &#39;a&#39; is an arbitrary constant. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> for which the equivalent circuit resistance is minimum, will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mi>x</mi><mn>2</mn></mfrac></msqrt></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____ .</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a314768d-5e9a-466b-8a39-476d281a5a7d-image.png" style="width: 250px; height: 163px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ef73449-292e-4f29-8438-cf6e70ef18d4-image.png" style="width: 264px; height: 160px;" /></p><p>Left part of the resistors are connected in parallel, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>a</mi><mi>m</mi></mrow><mn>3</mn></mfrac></math>.</p><p>Similarly, for the right part of the resistors we can write, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mi>a</mi><mrow><mn>2</mn><mi>m</mi></mrow></mfrac></math>.</p><p>Therefore, equivalent resistance will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mi>m</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mi>a</mi><mrow><mn>2</mn><mi mathvariant="normal">m</mi></mrow></mfrac></math></p><p>Differentiating both sides w.r.t <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> to observe critical points, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">d</mi><mi>R</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi>m</mi></mrow></mfrac><mo>=</mo><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mi>a</mi><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><msup><mi>m</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mi>a</mi><mrow><mn>2</mn><msup><mi mathvariant="normal">m</mi><mn>2</mn></msup></mrow></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><msqrt><mfrac><mn>3</mn><mn>2</mn></mfrac></msqrt></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>3</mn></math>.</p>

</details>

---

### Q38. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Find the equivalent resistance between point <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/77698fa1-05ab-4049-9495-848d7bfc004e-1.jpg" style="width: 250px; height: 218px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/eef79043-2bdd-48ec-b996-97452e58d72f-2.jpg" style="width: 500px; height: 175px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/fe03758f-a129-44ae-a0ae-0d27d1ffd233-3.jpg" style="width: 500px; height: 263px;" /></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/0b33733c-882c-4aaf-bafa-6d9ba1dd5556-4.jpg" style="width: 500px; height: 228px;" /></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><mfenced><mrow><msub><mi>R</mi><mrow><mi>A</mi><mi>S</mi></mrow></msub><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#215;</mo><mn>10</mn></mrow><mrow><mfenced><mrow><msub><mi>R</mi><mrow><mi>A</mi><mi>S</mi></mrow></msub><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>5</mn><mo>+</mo><mn>5</mn></mrow></mfenced><mo>&#215;</mo><mn>10</mn></mrow><mrow><mfenced><mrow><mn>5</mn><mo>+</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mn>10</mn></mrow></mfrac><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q39. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An aluminium wire is stretched to make its length, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>%</mo></math> larger. The percentage change in resistance is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn><mo>%</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2</mn><mo>%</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>8</mn><mo>%</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>%</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>8</mn><mo>%</mo></math>**

**Detailed Solution:**

<p>Volume of wire having cross-sectional area <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and length <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>A</mi><mi>l</mi></math></p><p>Resistance of a wire is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mstyle displaystyle="true"><mfrac><mi>V</mi><mi>l</mi></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mi>V</mi></mfrac></math></p><p>As change in length is small,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8710;</mo><mi>R</mi></mrow><mi>R</mi></mfrac><mo>&#215;</mo><mn>100</mn><mo>%</mo><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#8710;</mo><mi>l</mi></mrow><mi>l</mi></mfrac><mo>&#215;</mo><mn>100</mn><mo>%</mo><mo>=</mo><mn>2</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>4</mn><mo>%</mo><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn><mo>%</mo></math></p>

</details>

---

### Q40. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

The length of a given cylindrical wire is increased to double of its original length. The percentage increase in the resistance of the wire will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>%</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **300**

**Detailed Solution:**

<p>As volume is constant, so, length doubled and area reduces to half.</p><p>Resistance of a wire is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac></math>, where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#961;</mi></math> is resistivity of a material.</p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mfenced><mrow><mn>2</mn><mi>l</mi></mrow></mfenced></mrow><mstyle displaystyle="true"><mfrac><mi>A</mi><mn>2</mn></mfrac></mstyle></mfrac><mo>=</mo><mn>4</mn><mi>R</mi></math></p><p>So percentage increase in the resistance will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mi>R</mi><mo>-</mo><mi>R</mi></mrow><mi>R</mi></mfrac><mo>&#215;</mo><mn>100</mn><mo>%</mo><mo>=</mo><mn>300</mn><mo>%</mo></math></p>

</details>

---

### Q41. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

What will be the most suitable combination of three resistors <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> so that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>22</mn><mn>3</mn></mfrac></mfenced><mi mathvariant="normal">&#937;</mi></math> is equivalent resistance of combination?

**Options:**

- **(A)** Parallel combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> connected in series with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>
- **(B)** Parallel combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> connected in series with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>
- **(C)** Series combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> connected in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>.
- **(D)** Series combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> connected in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Parallel combination of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> connected in series with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/df83c8da-e763-4447-af6b-3a597021d33d-image.png" style="width: 300px; height: 129px;" /></p><p>If the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance and the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistance are connected in parallel to each other, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>R</mi><mo>&#39;</mo></msup><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>4</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. If the resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> is now connected in series to the previous combination.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>+</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mn>6</mn><mo>=</mo><mfrac><mn>22</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q42. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>The ratio of the equivalent resistance of the network (shown in figure) between the points <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> when switch is open and switch is closed is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo><mo>&#160;</mo><mn>8</mn></math>. The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/97b76f58-b6f5-4402-a79d-fae1796b31e0-image.png" style="width: 359px; height: 118px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>When switch is closed</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi mathvariant="normal">R</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi mathvariant="normal">R</mi></mrow><mn>3</mn></mfrac></math></p><p>When open <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>R</mi><mo>&#183;</mo><mn>3</mn><mi>R</mi></mrow><mrow><mn>3</mn><mi>R</mi><mo>+</mo><mn>3</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>R</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>R</mi></mrow><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mrow><mn>3</mn><mi>R</mi></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mi>x</mi></mfrac></math></p>

</details>

---

### Q43. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

First, a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> equal resistors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> each are connected in series to a battery of E.M.F. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and internal resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>.</mo></math> A current <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math> is observed to flow. Then, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> resistors are connected in parallel to the same battery. It is observed that the current is increased <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> times, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

When the resistances of each <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> â€‹ are connected in series and parallel then,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>s</mi></msub><mo>=</mo><mn>10</mn><mi>n</mi></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>p</mi></msub><mo>=</mo><mfrac><mn>10</mn><mi>n</mi></mfrac></math>. Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mi>p</mi></msub><mo>=</mo><mn>20</mn><msub><mi>i</mi><mi>s</mi></msub></math>, <p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>20</mn><mfenced><mrow><mfrac><mn>10</mn><mi>n</mi></mfrac><mo>+</mo><mn>10</mn></mrow></mfenced></mfrac><mo>=</mo><mn>20</mn><mfenced><mfrac><mn>20</mn><mrow><mn>10</mn><mi>n</mi><mo>+</mo><mn>10</mn></mrow></mfrac></mfenced><mo>&#8658;</mo><mfrac><mrow><mn>20</mn><mi>n</mi></mrow><mrow><mn>10</mn><mo>+</mo><mn>10</mn><mi>n</mi></mrow></mfrac><mo>=</mo><mn>20</mn><mfenced><mfrac><mn>20</mn><mrow><mn>10</mn><mi>n</mi><mo>+</mo><mn>10</mn></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>20</mn></math>.</p>

</details>

---

### Q44. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If you are provided a set of resistances, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>.</mo></math> Connect these resistances to obtain an equivalent resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>.

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> in series
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> in series
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> in series
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> in series

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are in parallel with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> in series**

**Detailed Solution:**

<p><img height="95" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3afd3ab8-5949-432c-952b-d17f56a8a874-image.png" width="445" /></p><p>We can arrange the circuit like above now on solving we get a simplified circuit, </p><p><img height="60" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f5113cbf-ac0f-4738-908a-1fecbd25c974-image.png" width="273" /></p><p>here, both the resistance are connected in series then resultant resistance will be, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>+</mo><mn>14</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>=</mo><mfrac><mn>46</mn><mn>3</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, in the other case we can not get this result.</p>

</details>

---

### Q45. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>In the given figure, the emf of the cell is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and if internal resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. Calculate the power dissipated in the whole circuit:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d7958c7f-3119-4521-8ec9-b8cd04526b7a-image.png" style="width: 300px; height: 266px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1.32</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.4</mo><mi mathvariant="normal">W</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>65</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math>**

**Detailed Solution:**

<p>The above circuit in the question is arranged like that, so all the resistance are connected in parallel and the net resistance of the parallel resistor becomes, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ca34200a-b78a-4e50-9002-798e20e3ddfc-image.png" style="width: 250px; height: 255px;" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>R</mi><mi>P</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><msub><mi>R</mi><mn>1</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><msub><mi>R</mi><mn>2</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><msub><mi>R</mi><mn>3</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><msub><mi>R</mi><mn>4</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>R</mi><mi>P</mi></msub><mo>=</mo><mfrac><mn>48</mn><mn>30</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1d1a6e8a-d1ee-40b5-867c-a0e68ff3ff28-image.png" style="width: 200px; height: 194px;" /></p><p>Now the net resistance will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>n</mi><mi>e</mi><mi>t</mi></mrow></msub><mo>=</mo><mfenced><mrow><mfrac><mn>48</mn><mn>30</mn></mfrac><mo>+</mo><mn>0</mn><mo>.</mo><mn>6</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>, so the net power, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><msup><mi>V</mi><mn>2</mn></msup><mi>R</mi></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mo>.</mo><mn>2</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>2</mn><mo>.</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mo>.</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">W</mi></math></p>

</details>

---

### Q46. JEE Main 2021 (22 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A Copper <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Cu</mi><mo>)</mo></math> rod of length <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>&#160;</mo><mi>cm</mi></math> and cross-sectional area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msup><mrow><mo>&#160;</mo><mi>mm</mi></mrow><mn>2</mn></msup></math> is joined with a similar Aluminium <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>Al</mi><mo>)</mo></math> rod as shown in figure. Find the resistance of the combination between the ends <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>.</mo></math></p><p>(Take resistivity of Copper <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi>&#937;m</mi></math>, Resistivity of aluminium <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>&#160;</mo><mi>&#937;m</mi></math>)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6f7f9613-43e4-4774-ab50-3c506a7b92da-image.png" style="width: 325px; height: 127px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>170</mn><mo>&#160;</mo><mi>m&#937;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>420</mn><mo>&#160;</mo><mi>m&#937;</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>0858</mn><mo>&#160;</mo><mi>m&#937;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>858</mn><mo>&#160;</mo><mi>m&#937;</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>858</mn><mo>&#160;</mo><mi>m&#937;</mi></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mi>&#8467;</mi><mi>A</mi></mfrac><mo>&#183;</mo><mfrac><mrow><msub><mi>&#961;</mi><mn>1</mn></msub><msub><mi>&#961;</mi><mn>2</mn></msub></mrow><mrow><msub><mi>&#961;</mi><mn>1</mn></msub><mo>+</mo><msub><mi>&#961;</mi><mn>2</mn></msub></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mn>25</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>6</mn></mrow></msup></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>1</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><mn>2</mn><mo>.</mo><mn>6</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>16</mn></mrow></msup></mrow><mrow><mn>4</mn><mo>.</mo><mn>3</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>8</mn></mrow></msup></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>858</mn><mo>&#160;</mo><mi>m&#937;</mi></math>

</details>

---

### Q47. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>The voltage across the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>&#937;</mi></math> resistor in the given circuit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> volt.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/701175ca-977f-4e22-8540-c44f25f24119-image.png" style="width: 250px; height: 169px;" /></p><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> to the nearest integer is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **70**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><msub><mi>q</mi><mn>1</mn></msub></mrow></msub><mo>=</mo><mfrac><mrow><mn>50</mn><mo>&#215;</mo><mn>20</mn></mrow><mn>70</mn></mfrac><mo>=</mo><mfrac><mn>100</mn><mn>7</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4257f4af-dea7-4e5b-8dea-97c745ebc906-image.png" style="width: 250px; height: 178px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>170</mn><mn>7</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>v</mi><mn>1</mn></msub><mo>=</mo><mfenced close="]" open="["><mfrac><mfrac><mn>170</mn><mn>170</mn></mfrac><mn>7</mn></mfrac></mfenced><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>70</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>70</mn><mo>.</mo><mn>00</mn></math></p>

</details>

---

### Q48. JEE Main 2021 (17 Mar Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>The equivalent resistance of series combination of two resistors is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>.</mo></math> When they are connected in parallel, the equivalent resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi><mo>=</mo><mi>n</mi><mi>p</mi><mo>,</mo></math> then the minimum value for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is ______.</p><p>(Round off to the Nearest Integer)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mi>s</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mi>p</mi><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mi>s</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mi>n</mi><msup><mi>p</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>n</mi><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mfenced><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mrow><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mi>n</mi></math></p><p>for minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mi>R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mo>(</mo><mn>2</mn><mi>R</mi><msup><mo>)</mo><mn>2</mn></msup></mrow><msup><mi>R</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q49. JEE Main 2021 (25 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>A current of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math> enters one corner <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> of an equilateral triangle <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mi>Q</mi><mi>R</mi></math> having <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> wires of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> each and leaves by the corner <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>.</mo></math> The currents <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub></math> in ampere is</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/183f227d-b2fe-4945-bcf0-d68c5fda31fa-image.png" style="width: 140px; height: 181px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>For parallel combination, current divides in the inverse ratio of resistance.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mrow><mi>P</mi><mi>Q</mi></mrow></msub><mo>=</mo><mfrac><mn>2</mn><mn>6</mn></mfrac><mo>&#215;</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.</p>

</details>

---

### Q50. JEE Main 2020 (04 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Four resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>&#937;</mi><mo>,</mo><mn>60</mn><mo>&#160;</mo><mi>&#937;</mi><mo>,</mo><mn>90</mn><mo>&#160;</mo><mi>&#937;</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>110</mn><mo>&#160;</mo><mi>&#937;</mi></math> and  make the arms of a quadrilateral <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math>. Across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>C</mi></math> is a battery of emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&#160;</mo><mi>V</mi></math> and internal resistance negligible. The potential difference across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mi>D</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is __________</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2a1c96a4-3846-4257-9749-5b7714a8b313-image.png" style="width: 197px; height: 175px;" />  </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4a698efd-2680-44c6-a5f7-43541ba9ed37-image.png" style="width: 209px; height: 181px;" /></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>KVL</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">B</mi></msub><mo>-</mo><mn>60</mn><mfenced><mfrac><mn>40</mn><mn>100</mn></mfrac></mfenced><mo>+</mo><mn>110</mn><mfenced><mfrac><mn>40</mn><mn>200</mn></mfrac></mfenced><mo>=</mo><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">D</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">B</mi></msub><mo>-</mo><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">D</mi></msub><mo>=</mo><mn>2</mn></math> </p>

</details>

---

### Q51. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Two resistors <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>  and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>800</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> are connected in series across a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#8744;</mo></math> battery. The potential difference measured by a voltmeter of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi>k&#937;</mi></math> across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor is close to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>05</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>95</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>95</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7596e29f-e069-4392-bb83-ac8fb032bfd0-image.png" style="width: 203px; height: 160px;" /></p><p>Let voltmeter reading is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">v</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">v</mi><mn>100</mn></mfrac><mo>&#215;</mo><mn>400</mn><mo>+</mo><mfenced><mrow><mfrac><mi mathvariant="normal">v</mi><mn>10000</mn></mfrac><mo>+</mo><mfrac><mi mathvariant="normal">v</mi><mn>400</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mn>800</mn><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi mathvariant="normal">v</mi><mo>+</mo><mfrac><mrow><mn>8</mn><mi mathvariant="normal">v</mi></mrow><mn>100</mn></mfrac><mo>+</mo><mn>2</mn><mi mathvariant="normal">v</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mfrac><mrow><mn>77</mn><mi mathvariant="normal">v</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mn>6</mn><mo>&#160;</mo><mo>;</mo><mo>&#160;</mo><mi mathvariant="normal">v</mi><mo>=</mo><mfrac><mn>150</mn><mn>77</mn></mfrac><mo>=</mo><mn>1</mn><mo>.</mo><mn>95</mn><mo>&#160;</mo><mi mathvariant="normal">v</mi></math></p>

</details>

---

### Q52. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>An ideal cell of emf <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi mathvariant="normal">V</mi></math> is connected in circuit shown in figure. Each resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi mathvariant="normal">&#937;</mi></math>. The potential difference (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>) across the capacitor when it is fully charged is _____________</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/70c12406-741a-4d65-8178-44e878c49fc9-image.png" style="width: 231px; height: 183px;" />  </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1d7dc0a9-9d67-43a5-985d-624c6defd5b4-image.png" style="width: 302px; height: 181px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">i</mi><mo>=</mo><mfrac><mn>10</mn><mrow><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>3</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>Amp</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">i</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">i</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mi>AB</mi></msub><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q53. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In the given circuit diagram, a wire is joining points B and D. The current in this wire is:



<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/09ee1f61-358d-41eb-bc3b-0d1e5380cee5.jpeg" />

**Options:**

- **(A)** <math><mn>0.4</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">A</mi></math>
- **(B)** <math><mn>2</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">A</mi></math>
- **(C)** <math><mn>4</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">A</mi></math>
- **(D)** zero

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn><mi mathvariant="normal"></mi><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/68a4832a-3931-4448-b7a3-961ffa664150-image.png" />
<math><msub><mrow><mi>R</mi></mrow><mrow><mi>e</mi><mi>f</mi><mi>f</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi mathvariant="normal">&#937;</mi></math>
<math><mi>i</mi><mo>=</mo><mfrac><mrow><mn>20</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>=</mo><mn>10</mn><mi>A</mi></math>
<math><mi>I</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>i</mi></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mi>i</mi></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mo>+</mo><mfrac><mrow><mi>i</mi></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi>A</mi></math>

</details>

---

### Q54. JEE Main 2020 (08 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The series combination of two batteries, both of the same emf <math><mn>10</mn><mi></mi><mi mathvariant="normal">V</mi><mo>,</mo><mi mathvariant="normal"></mi></math> but different internal resistance of <math><mn>20</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math> and <math><mn>5</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi><mo>,</mo><mi mathvariant="normal"></mi></math> is connected to the parallel combination of two resistors <math><mn>30</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>x&#8201;</mtext><mi mathvariant="normal">&#937;</mi><mo>.</mo></math> The voltage difference across the battery of internal resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math> is zero, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>x</mtext></math> (in <math><mi mathvariant="normal">&#937;</mi><mo>)</mo></math> is____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<p></p><p><math><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi>&#1013;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mi>i</mi><mo>.</mo><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
<math><mn>0</mn><mo>=</mo><mn>10</mn><mo>-</mo><mi>i</mi><mo>&#215;</mo><mn>20</mn></math>
<math><mi>i</mi><mo>=</mo><mn>0.5</mn><mi>A</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>7.5</mn><mn>30</mn></mfrac><mo>+</mo><mfrac><mn>7.5</mn><mtext>x</mtext></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0.5</mn><mo>=</mo><mn>0.25</mn><mo>+</mo><mfrac><mn>7.5</mn><mtext>x</mtext></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7.5</mn><mtext>x</mtext></mfrac><mo>=</mo><mn>0.25</mn><mspace linebreak="newline"/><mtext>x</mtext><mo>=</mo><mfrac><mn>7.5</mn><mn>0.25</mn></mfrac><mo>=</mo><mn>30</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q55. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In the figure, potential difference between <math><mi mathvariant="normal">A</mi></math> and <math><mi mathvariant="normal">B</mi></math> is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/023832eb-f4f8-4165-93b7-b61afd233c6e-image.png" style="width: 300px; height: 168px;" />

**Options:**

- **(A)** <math><mn>10 </mn><mi mathvariant="normal">V</mi></math>
- **(B)** <math><mn>5 </mn><mi mathvariant="normal">V</mi></math>
- **(C)** <math><mn>15 </mn><mi></mi><mi mathvariant="normal">V</mi></math>
- **(D)** <math><mi mathvariant="normal">0 V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>10 </mn><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<p>Diode is in forward bias, so it will behave as simple wire so,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e959f77e-4f2f-47fa-a412-d3118c797523-image.png" />
So, <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">a</mi><mi mathvariant="normal">b</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>30</mn></mrow><mrow><mn>5</mn><mo>+</mo><mn>10</mn></mrow></mfrac><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>10&#160;</mn><mi mathvariant="normal">V</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/30ec6ae1-bcc6-45ee-a475-228f10b0ee69-image.png" /></p>

</details>

---

### Q56. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The current <math><msub><mrow><mi>I</mi></mrow><mrow><mn>1</mn></mrow></msub></math> (in <math><mi>A</mi></math> ) flowing through <math><mn>1</mn><mi mathvariant="normal">&#937;</mi></math> resistor in the following circuit is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/24bd418d-f63e-485f-9dd8-f49dfa4f5ded.png" style="height: 154px; width: 220px;" />

**Options:**

- **(A)** <math><mn>0.4</mn></math>
- **(B)** <math><mn>0.5</mn></math>
- **(C)** <math><mn>0.2</mn></math>
- **(D)** <math><mn>0.25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>0.2</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/599406A.JPG" style="width: 250px; height: 211px;" />
<math>    <mtext>I</mtext>  <mo>=</mo><mfrac>   <mn>1</mn>   <mrow>    <mn>2.5</mn></mrow>  </mfrac>  <mo>=</mo><mn>0.4</mn><mtext>A</mtext></mrow></math>
<math> <mrow> <msub> <mtext>I</mtext> <mn>1</mn> </msub> <mo>=</mo><mfrac> <mtext>I</mtext> <mn>2</mn> </mfrac> <mo>=</mo><mn>0.2</mn><mtext>A</mtext></mrow> </math>

</details>

---

### Q57. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The resistive network shown below is connected to a <math><mi mathvariant="normal">D</mi><mo>.</mo><mi mathvariant="normal">C</mi><mo>.</mo></math> source of <math><mn>16</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi><mo>.</mo></math> The power consumed by the network is <math><mn>4</mn></math> Watt. The value of <math><mi mathvariant="normal">R</mi></math> is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b771ee9a-0eb6-4af1-8e8d-64d598e0c4ee-image14.png" />

**Options:**

- **(A)** <math><mn>16</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mn>8</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mn>6</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mn>1</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>8</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub></math> for mixed series and parallel combination of</p><p>  given circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>R</mi></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>4</mn><mi>R</mi></mrow></mfrac></mstyle></mrow></mfrac><mo>+</mo><mi>R</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>6</mn><mi>R</mi></mrow></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mrow><mn>12</mn><mi>R</mi></mrow></mfrac></mstyle></mrow></mfrac><mo>+</mo><mi>R</mi></math></p><p><math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mn>8</mn><mi mathvariant="normal">R</mi></math>
Power dissipated by circuit <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><msup><mi mathvariant="normal">V</mi><mn>2</mn></msup><msub><mi mathvariant="normal">R</mi><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mo>=</mo><mfrac><msup><mn>16</mn><mn>2</mn></msup><mrow><mn>8</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mn>256</mn><mn>32</mn></mfrac><mo>=</mo><mn>8</mn><mtext>&#8201;</mtext><mi mathvariant="normal">&#937;</mi></math></p>

</details>

---

### Q58. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A metal wire of resistance <math><mn>3</mn><mtext> </mtext><mi mathvariant="normal">Ω</mi></math> is elongated to make a uniform wire of double its previous length. This new wire is now bent and the ends joined to make a circle. If two points on this circle make an angle <math><msup><mrow><mn>60</mn></mrow><mrow><mi mathvariant="normal">o</mi></mrow></msup></math> at the center, the equivalent resistance between these two points will be:

**Options:**

- **(A)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mtext> </mtext><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

We know, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi>A</mi><mi>l</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>&#961;</mi><msup><mi>l</mi><mn>2</mn></msup></mrow><mrow><mi mathvariant="normal">V</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>&#8733;</mo><msup><mi>l</mi><mn>2</mn></msup></math> , if the volume is constant.
<math><mo>&#8756;</mo><mi mathvariant="normal">&#160;</mi></math> New resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>R</mi></math>
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ca003bce-30b1-46ce-8688-da31073a4bfd-image8.png" />
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>R</mi></mrow><mn>360</mn></mfrac><mo>&#215;</mo><mn>300</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>R</mi></mrow><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mn>4</mn><mi>R</mi></mrow><mn>360</mn></mfrac><mo>&#215;</mo><mn>60</mn><mo>=</mo><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mn>3</mn></mfrac></math>
<math><mo>&#8756;</mo></math> Equivalent resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mi>R</mi><mn>1</mn></msub><msub><mi>R</mi><mn>2</mn></msub></mrow><mrow><msub><mi>R</mi><mn>1</mn></msub><mo>+</mo><msub><mi>R</mi><mn>2</mn></msub></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>10</mn><mi>R</mi></mrow><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mn>3</mn></mfrac></mrow><mrow><mfrac><mrow><mn>10</mn><mi>R</mi></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mn>3</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mi>R</mi></mrow><mn>9</mn></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#937;</mi></math>

</details>

---

### Q59. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Determine the charge on the capacitor in the following circuit:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2cce9b05-ecb3-467a-bb64-b715bcadb21e-image.png" style="width: 350px; height: 121px;" />

**Options:**

- **(A)** <math><mn>2</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">C</mi></math>
- **(B)** <math><mn>60</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">C</mi></math>
- **(C)** <math><mn>10</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">C</mi></math>
- **(D)** <math><mn>200</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">C</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>200</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">μ</mi><mi mathvariant="normal">C</mi></math>**

**Detailed Solution:**

<p>After a long time capacitor branch will behave like open circuit so circuit will be like,
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4058beaa-ba4e-407e-9a02-30769dec60b1-image.png" style="width: 270px; height: 129px;" />
Equivalent resistance is
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>6</mn><mo>+</mo><mfenced><mrow><mn>4</mn><mo>|</mo><mo>|</mo><mfenced><mrow><mn>2</mn><mo>+</mo><mn>10</mn></mrow></mfenced></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
and, the current through battery becomes <math><mfrac><mrow><mn>72</mn></mrow><mrow><mn>9</mn></mrow></mfrac><mo>=</mo><mn>8</mn><mi>&#160;</mi><mi mathvariant="normal">A</mi></math> 
From the circuit shown, current through <math><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">&#937;</mi><mi mathvariant="normal">&#160;</mi></math> resistor becomes, <math><mfrac><mrow><mn>4</mn></mrow><mrow><mo>(</mo><mn>10</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>)</mo></mrow></mfrac><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>2</mn><mi>&#160;</mi><mi mathvariant="normal">A</mi></math> </p><p>Potential available for capacitor is = potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi></math> Potential available for capacitor is: <math><mn>10</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>20</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></math>
<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi></math> Charge on capacitor <math><mi>Q</mi><mo>=</mo><mfenced separators="|"><mrow><mn>10</mn><mi>&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">F</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>20</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></mrow></mfenced><mo>=</mo><mn>200</mn><mi>&#160;</mi><mi mathvariant="normal">&#956;</mi><mi mathvariant="normal">C</mi></math></p>

</details>

---

### Q60. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A wire of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is bent to form a square <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>B</mi><mi>C</mi><mi>D</mi></math> as shown in the figure. The effective resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is:
( <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> is mid-point of arm <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mi>D</mi></math> )
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/9b37b65d-6136-4891-84f6-b5089aee9d6f-image7.png" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>64</mn></mfrac><mi>R</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac><mi>R</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>64</mn></mfrac><mi>R</mi></math>**

**Detailed Solution:**

<p>If the resistance of the wire is <em>R</em>, then each arm of the square has a resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>R</mi><mn>4</mn></mfrac></math>. Accordingly. The resistance of segments DE and EC are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>DE</mi></msub><mo>=</mo><msub><mi>R</mi><mi>EC</mi></msub><mo>=</mo><mfrac><mi>R</mi><mn>8</mn></mfrac></math>.</p><p>We can draw the resultant circuit as follows:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/57bc8af5-690a-4e71-96db-e5d87a403501-image.png" style="width: 300px; height: 287px;" /></p><p>Hence,</p><p><math><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mi mathvariant="normal">R</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>7</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>
<math><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>56</mn><mo>+</mo><mn>8</mn></mrow><mrow><mn>7</mn><mi mathvariant="normal">R</mi></mrow></mfrac></math>
<math><msub><mrow><mi mathvariant="normal">R</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">R</mi></mrow><mrow><mn>64</mn></mrow></mfrac></math></p>

</details>

---

### Q61. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A uniform metallic wire has a resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> and is bent into an equilateral triangle. Then, the resistance between any two vertices of the triangle is:

**Options:**

- **(A)** <math><mn>2</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mn>12</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mn>8</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mn>4</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>4</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

<blockquote><p>Resistance,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mfrac><mrow><mi>&#961;</mi><mi>l</mi></mrow><mi>A</mi></mfrac><mspace linebreak="newline"></mspace><mi>R</mi><mo>&#160;</mo><mi>&#945;</mi><mo>&#160;</mo><mi>l</mi><mspace linebreak="newline"></mspace><mi>s</mi><mi>a</mi><mi>y</mi><mo>&#160;</mo><msub><mi>R</mi><mrow><mi>e</mi><mi>f</mi><mi>f</mi></mrow></msub><mo>=</mo><mi>l</mi><mo>=</mo><mn>18</mn><mspace linebreak="newline"></mspace><mi>a</mi><mi>s</mi><mo>&#160;</mo><msub><mi>l</mi><mn>1</mn></msub><mo>=</mo><msub><mi>l</mi><mn>2</mn></msub><mo>=</mo><msub><mi>l</mi><mn>3</mn></msub><mo>=</mo><mi>l</mi><mo>/</mo><mn>3</mn><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>R</mi><mn>1</mn></msub><mo>=</mo><msub><mi>R</mi><mn>2</mn></msub><mo>=</mo><msub><mi>R</mi><mn>3</mn></msub><mo>=</mo><mi>R</mi><mo>=</mo><mn>18</mn><mo>/</mo><mn>3</mn><mspace linebreak="newline"></mspace><mo>=</mo><mn>6</mn></math><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c6ea8558-17bd-414b-a4f4-6bb793b4ba42-image.png" style="width: 400px; height: 169px;" /></p><p>So from diagram</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>a</mi><mi>n</mi><mi>d</mi><mo>&#160;</mo><mi>R</mi><mo>=</mo><mn>6</mn><mspace linebreak="newline"/><mi>a</mi><mi>l</mi><mi>s</mi><mi>o</mi><mo>&#160;</mo><mi>w</mi><mi>e</mi><mo>&#160;</mo><mi>k</mi><mi>n</mi><mi>o</mi><mi>w</mi><mo>&#160;</mo><mspace linebreak="newline"/><msub><mi>R</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mi>R</mi><mrow><mn>2</mn><mi>R</mi></mrow></msub><msub><mi>R</mi><mi>R</mi></msub></mrow><mrow><msub><mi>R</mi><mrow><mn>2</mn><mi>R</mi></mrow></msub><mo>+</mo><msub><mi>R</mi><mi>R</mi></msub></mrow></mfrac><mspace linebreak="newline"/><msub><mi>R</mi><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>12</mn></mrow><mrow><mn>6</mn><mo>+</mo><mn>12</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p></blockquote>

</details>

---

### Q62. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit the internal resistance of the <math><mn>18</mn><mi>V</mi></math> cell is negligible. If <math><msub><mrow><mi>R</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>400&#160;</mn><mi mathvariant="normal">&#937;</mi><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mn>100&#160;</mn><mi mathvariant="normal">&#937;</mi></math> and <math><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>500</mn><mi>&#160;</mi><mi mathvariant="normal">&#937;</mi></math> and the reading of an ideal voltmeter across <math><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math> is <math><mn>5</mn><mi>&#160;</mi><mi>V</mi><mo>,</mo></math> then the value of <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math> will be:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1e5ca536-15b5-4697-b0e2-4047ca160acd-image.png" style="width: 218px; height: 179px;" />

**Options:**

- **(A)** <math><mn>550</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(B)** <math><mn>300</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(C)** <math><mn>450</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>
- **(D)** <math><mn>230</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>300</mn><mi> </mi><mi mathvariant="normal">Ω</mi></math>**

**Detailed Solution:**

<p>Given reading of an ideal voltmeter for resistance <math><msub><mrow><mi>R</mi></mrow><mrow><mn>4</mn></mrow></msub></math>  is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>4</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mi>V</mi></math>, then current (let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub></math>)is given branch (as resistance <math><msub><mrow><mi>R</mi></mrow><mrow><mn>3</mn></mrow></msub></math> in series with resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>4</mn></msub></math>) is 
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>1</mn></msub><mo>=</mo><mfrac><mi>V</mi><msub><mi>R</mi><mn>4</mn></msub></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>500</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo>&#160;</mo><mi>A</mi></math>
Then for resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub></math>, the potential difference will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>3</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msub><mi>i</mi><mn>1</mn></msub><mo>&#160;</mo><msub><mi>R</mi><mn>3</mn></msub><mo>&#160;</mo><mo>=</mo><mn>0</mn><mo>.</mo><mn>01</mn><mo>&#215;</mo><mn>100</mn><mo>&#160;</mo><mo>=</mo><mn>1</mn><mi>V</mi></math></p><p>So, for given branch of resistance potential difference is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>3</mn></msub><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msub><mi>V</mi><mn>4</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>V</mi></math></p><p>From figure for resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>1</mn></msub><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><msub><mi>R</mi><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>4</mn></msub></math> a total applied potential difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo><mi>V</mi></math> then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mo>+</mo><mo>&#160;</mo><msub><mi>V</mi><mn>3</mn></msub><mo>+</mo><msub><mi>V</mi><mn>4</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>18</mn><mspace linebreak="newline"></mspace><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>V</mi><mn>1</mn></msub><mo>&#160;</mo><mo>=</mo><mn>18</mn><mo>-</mo><mfenced><mrow><msub><mi>V</mi><mn>3</mn></msub><mo>+</mo><msub><mi>V</mi><mn>4</mn></msub></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mn>18</mn><mo>-</mo><mn>6</mn><mo>&#160;</mo><mo>=</mo><mn>12</mn><mo>&#160;</mo><mi>V</mi></math></p><p>So, the total current drawn from the source is </p><p><math><mo>&#8756;</mo><mi>&#160;</mi></math> Current through <math><msub><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>i</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>&#183;</mo><mn>03</mn><mo>-</mo><mn>0</mn><mo>&#183;</mo><mn>01</mn><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#183;</mo><mn>02</mn><mo>&#160;</mo><mi>A</mi></math>
and potential difference for <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>2</mn></msub><mo>&#160;</mo><mo>=</mo><msub><mi>V</mi><mn>3</mn></msub><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msub><mi>V</mi><mn>4</mn></msub><mo>&#160;</mo><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi>V</mi></math> ( <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is in parallel arrangement with the resistances <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>3</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>4</mn></msub></math>)</p><p>Now the value of resistance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mn>2</mn></msub></math> is :
 <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>2</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msub><mi>i</mi><mn>2</mn></msub><mo>&#160;</mo><msub><mi>R</mi><mn>2</mn></msub><mspace linebreak="newline"></mspace><mo>&#8658;</mo><msub><mi>R</mi><mn>2</mn></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><msub><mi>V</mi><mn>2</mn></msub><msub><mi>i</mi><mn>2</mn></msub></mfrac><mo>&#160;</mo><mo>=</mo><mfrac><mn>6</mn><mrow><mn>0</mn><mo>&#183;</mo><mn>02</mn></mrow></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>300</mn><mo>&#160;</mo><mi>&#937;</mi></math></p>

</details>

---

### Q63. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit all resistance is of the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> ohm each. The equivalent resistance between <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/266ab906-cdf3-45f5-871b-5d636ca02d43-image.png" style="width: 300px; height: 157px;" />

**Options:**

- **(A)** <math><mfrac><mrow><mn>5</mn><mi>R</mi></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** 3R
- **(C)** <math><mfrac><mrow><mn>5</mn><mi>R</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>R</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/1f5da310-a28c-40ec-9f80-df3bf92ea7cc-image.png" style="width: 300px; height: 199px;" /></p><p>Resistance of ideal wire would be zero, and hence potential will be the same of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> point as shown in the figure. So effective path of current is shown in figure, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/3e4892f7-79c6-4a76-8262-680e3f204314-image.png" style="width: 240px; height: 137px;" /></p>

</details>

---

### Q64. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

In the given circuit all resistances are of value $R$ ohm each. The equivalent resistance between $A$ and $B$ is:
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/LKQN155c2wX39TULrza5_iDWFFbLJ2d269JiA7mP0eo.original.fullsize.png">

**Options:**

- **(A)** $2 R$
- **(B)** $\frac{5 R}{2}$
- **(C)** $\frac{5 R}{3}$
- **(D)** $3 R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 R$**

**Detailed Solution:**

$\mathrm{R}_{\text {senies }}=\mathrm{R}_1+\mathrm{R}_2+\ldots . \ldots+\mathrm{R}_{\mathrm{n}}$
$\frac{1}{\mathrm{R}_{\text {parallel }}}=\frac{1}{\mathrm{R}_1}+\frac{1}{\mathrm{R}_2}+\ldots \ldots+\frac{1}{\mathrm{R}_{\mathrm{n}}}$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/g26NqwG7-Qutf8-CjuC8WETA2FIEmLSWhs_QwDm07L0.original.fullsize.png">

</details>

---

### Q65. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/881a8fab-42e9-4834-8adc-4a6deb7ae842-image.png" style="width: 400px; height: 158px;" />
A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> battery with an internal resistance of <math><mn>0.5</mn><mi mathvariant="normal">&#160;&#937;</mi></math> is connected across an infinite network, as shown in the figure. All ammeters <math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>A</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>A</mi></mrow><mrow><mn>3</mn></mrow></msub></math> and voltmeter <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> are ideal.
Choose the correct statement.

**Options:**

- **(A)** Reading of <math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.
- **(B)** Reading of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.
- **(C)** Reading of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>.
- **(D)** Reading of <math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Reading of <math><msub><mrow><mi>A</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>.**

**Detailed Solution:**

<p style="text-align: justify;">In the given infinite network problems, let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be an equivalent resistance. If we connect one section of an infinite network with the replacing network using an equivalent resistance, then in this new equivalent circuit the equivalent resistance will still remain the same.</p><p style="text-align: justify;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/ec5226dc-9688-4375-afca-c0d009a4798c-image.png" style="width: 200px; height: 111px;" />
Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>R</mi><mi>eq</mi></msub><mo>=</mo><mi>x</mi></math>
<math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mn>2</mn></math>
<math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>8</mn><mo>+</mo><mn>6</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfrac></math>
<math><mn>4</mn><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>8</mn><mo>+</mo><mn>6</mn><mi>x</mi></math>
<math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>. </p><p>On solving,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mo>&#160;</mo><mo>-</mo><mn>2</mn></math>
Here, the negative value of resistance is not possible.</p><p>So, resistance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> </p><p>Reading of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mi>V</mi><mrow><mi>X</mi><mo>+</mo><mi>r</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math>, </p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mi>Volt</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>&#183;</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mi>R</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. </p><p>Then, from the above equation,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>&#160;</mo><mo>=</mo><mfrac><mn>9</mn><mrow><mn>4</mn><mo>+</mo><mn>0</mn><mo>.5</mo></mrow></mfrac><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>. </p>

</details>

---

### Q66. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/27f52da3-89b7-4c46-9a8b-e2318ef411de-image.png" style="width: 387px; height: 177px;" />

In the above circuit the current in each resistance is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/621179db-0dfa-4b9e-aed0-91952e7a3eae-image.png" style="width: 339px; height: 166px;" />

Potential difference across each resistor is zero. Hence current is zero in each resistor.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/19e6ec74-6c06-4403-b34e-7425ed0eacd1-image.png" style="width: 360px; height: 186px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub><mo>-</mo><msub><mi mathvariant="normal">E</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">E</mi><mn>3</mn></msub><mo>-</mo><msub><mi mathvariant="normal">E</mi><mn>4</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi mathvariant="normal">E</mi><mn>4</mn></msub><mo>-</mo><msub><mi mathvariant="normal">E</mi><mn>5</mn></msub><mo>=</mo><mn>0</mn></math></p><p>Hence, current through all the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> ressitor is zero.</p>

</details>

---

### Q67. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

In the electric network shown, when no current flows through the <math><mn>4</mn><mi>&#160;</mi><mi mathvariant="normal">&#937;</mi></math> resistor in the arm EB, the potential difference between the points A and D will be:

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/7ec23164-4a61-42cb-abfe-6956939f454c-image.png" style="width: 315px; height: 181px;" />

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/50296732-3148-45b7-a21b-aa18ff8e93c4-image.png" style="width: 296px; height: 184px;" />

Assuming potential at B = 0, then w.r.t. B the potential of other points are as shown in figure then

So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>A</mi></msub><mo>=</mo><mn>9</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mi>D</mi></msub><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>V</mi><mi>A</mi></msub><mo>-</mo><msub><mi>V</mi><mi>D</mi></msub><mo>=</mo><mn>9</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>5</mn><mi>&#160;</mi><mi mathvariant="normal">V</mi></math>

</details>

---

### Q68. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Six equal resistances are connected between points $\mathrm{P}, \mathrm{Q}$ and $\mathrm{R}$ as shown in figure. Then net resistance will be maximum between :
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/O9HgTewRulufr7QvovuzO4n-dIGHmgXdTMZFUfVypMY.original.fullsize.png">

**Options:**

- **(A)** $\mathrm{P}$ and $\mathrm{R}$
- **(B)** P and Q
- **(C)** Q and R
- **(D)** Any two points

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) P and Q**

**Detailed Solution:**

Resistance between $\mathrm{P}$ and $\mathrm{Q}$
$$
r_{\mathrm{PQ}}=r_{11}\left(\frac{r}{3}+\frac{r}{2}\right)=\frac{r \times \frac{5}{6} r}{r+\frac{5}{6} r}=\frac{5}{11} r
$$
Resistance between Q and R
$$
\mathrm{r}_{\mathrm{QR}}=\frac{\mathrm{r}}{2} 11\left(\mathrm{r}+\frac{\mathrm{r}}{3}\right)=\frac{\frac{\mathrm{r}}{2} \times \frac{4}{3} \mathrm{r}}{\frac{\mathrm{r}}{2}+\frac{4}{3} \mathrm{r}}=\frac{4}{11} \mathrm{r}
$$
Resistance between $\mathrm{P}$ and $\mathrm{R}$
$$
\mathrm{r}_{\mathrm{PR}}=\frac{\mathrm{r}}{3} \mathrm{l}\left(\frac{\mathrm{r}}{2}+\mathrm{r}\right)=\frac{\frac{\mathrm{r}}{3} \times \frac{3}{2} \mathrm{r}}{\frac{\mathrm{r}}{3}+\frac{3}{2} \mathrm{r}}=\frac{3}{11} \mathrm{r}
$$
Hence, it is clear that $\mathrm{r}_{\mathrm{PQ}}$ is maximum

</details>

---

### Q69. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A letter ${ }^{\prime} \mathrm{A}^{\prime}$ is constructed of a uniform wire with resistance $1.0 \Omega$ per $\mathrm{cm}$, The sides of the letter are $20 \mathrm{~cm}$ and the cross piece in the middle is $10 \mathrm{~cm}$ long. The apex angle is 60 . The resistance between the ends of the legs is close to:

**Options:**

- **(A)** $50.0 \Omega$
- **(B)** $10 \Omega$
- **(C)** $36.7 \Omega$
- **(D)** $26.7 \Omega$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $26.7 \Omega$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/MZq2eYEQH_0TbD2aY5EBlZkNH6IvjcUtzGzRAX_5MjA.original.fullsize.png">

For $\mathrm{ADE} \frac{1}{\mathrm{R}^{\prime}}=\frac{1}{2 \mathrm{x}}+\frac{1}{10}$
or $\quad R^{\prime}=\frac{20 x}{10+2 x}$
$$
\mathrm{R}_{\mathrm{BC}}=\frac{20 \mathrm{x}}{10+2 \mathrm{x}}+20-\mathrm{x}+20-\mathrm{x}
$$
or $\frac{20 \mathrm{x}}{10+2 \mathrm{x}}+40=2 \mathrm{x}$
Solving we get
$$
\mathrm{x}=10 \Omega
$$
Putting the value of $x=10 \Omega$ in equation (i) We get
$$
\begin{aligned}
\mathrm{R}_{\mathrm{BC}} & =\frac{20 \times 10}{10+2 \times 10}+20-10+20-10 \\
& =\frac{80}{3}=26.7 \Omega
\end{aligned}
$$

</details>

---

### Q70. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

The current $\mathrm{I}$ drawn from the 5 volt source will be
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/6diSZ2obgBvwccbRRba1P2FhxQt2yXAH38uLHyIv6i0.original.fullsize.png">

**Options:**

- **(A)** $0.17 \mathrm{~A}$
- **(B)** $0.33 \mathrm{~A}$
- **(C)** $0.5 \mathrm{~A}$
- **(D)** $0.67 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.5 \mathrm{~A}$**

**Detailed Solution:**

$i=\frac{5}{10}=0.5$

</details>

---

### Q71. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

An electric current is passed through a circuit containing two wires of the same material, connected in parallel. If the length and radii of the wires are in the ratio of $4 / 3$ and $2 / 3$, then the ratio of the currents passing through the wire will be

**Options:**

- **(A)** 3
- **(B)** $1 / 3$
- **(C)** $8 / 9$
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 / 3$**

**Detailed Solution:**

$$
\frac{I_1}{I_2}=\frac{R_2}{R_1}
$$
[current divider rule since voltage is same in parallel]
$$
\begin{aligned}
& \frac{I_1}{I_2}=\frac{L_2}{L_1} \times \frac{r_1^2}{r_2^2} \\
& \therefore \frac{I_1}{I_2}=\frac{3}{4} \times\left(\frac{2}{3}\right)^2=\frac{1}{3} .
\end{aligned}
$$

</details>

---

### Q72. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

The resistance of the series combination of two resistances is $S$. When they are joined in parallel through total resistance is $P$. If $S=n P$, then the minimum possible value of $n$ is

**Options:**

- **(A)** 4
- **(B)** 3
- **(C)** 2
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 4**

**Detailed Solution:**

Let resistances be $R_1$ and $R_2$
So, $S=R_1+R_2$;
$$
\begin{aligned}
& \mathrm{P}=\frac{\mathrm{R}_1 \mathrm{R}_2}{\mathrm{R}_1+\mathrm{R}_2} \\
& \mathrm{~S}=\mathrm{nP} \\
& \mathrm{R}_1+\mathrm{R}_2=\frac{\mathrm{nR}_1 \mathrm{R}_2}{\mathrm{R}_1+\mathrm{R}_2} \\
& \left(\mathrm{R}_1+\mathrm{R}_2\right)^2=\mathrm{nR}_1 \mathrm{R}_2
\end{aligned}
$$
If $R_1=R_2$, so minimum value of $n=4$.

</details>

---

### Q73. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The total current supplied to the circuit by the battery is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/tD42eiNeQH0Nv-5KVN5jyNQcRE4p04vAxl72Up5C8cI.original.fullsize.png">

**Options:**

- **(A)** $1 \mathrm{~A}$
- **(B)** $2 \mathrm{~A}$
- **(C)** $4 A$
- **(D)** $6 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $4 A$**

**Detailed Solution:**

The given circuit can be written as
$$
\mathrm{I}=\frac{6 \mathrm{~V}}{1.5 \Omega}=4 \mathrm{~A}
$$

</details>

---

### Q74. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

A 3 volt battery with negligible internal resistance is connected in a circuit as shown in the figure. The current $\mathrm{I}$, in the circuit will be


<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/D3MyIZIbBkWrKpVljcJmr10VfFtRCdrxK-E1Hc7thYM.original.fullsize.png">

**Options:**

- **(A)** $1 \mathrm{~A}$
- **(B)** $1.5 \mathrm{~A}$
- **(C)** $2 \mathrm{~A}$
- **(D)** $1 / 3 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1.5 \mathrm{~A}$**

**Detailed Solution:**

$I=\frac{3}{2}=1.5 \mathrm{~A}$<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/kiS2yc1cRK8IKPytswza6id8Ce5H3FO_eAJLum8_fOg.original.fullsize.png">

</details>

---

