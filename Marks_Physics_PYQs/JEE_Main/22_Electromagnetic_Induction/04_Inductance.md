# JEE Main Physics - Electromagnetic Induction

## Topic 4: Inductance

**Total Questions:** 13

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

In the given circuit below inductance values of $L_1$, $L_2$ and $L_3$ are same. The magnetic energy stored in the entire circuit is $(U_t)$ and that stored in the $L_2$ inductor is $(U_l)$. $U_t / U_l$ is __________.
(Ignore the mutual inductance if any)
<img style="width: 300px" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_april_watermarked/05APRS1__q50_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

Let the inductance of each inductor be $L$, so $L_1 = L_2 = L_3 = L$.

Let the total current flowing through the circuit be $I$. This current flows entirely through $L_1$.

Since $L_2$ and $L_3$ are connected in parallel and have equal inductances, the current $I$ divides equally between them. Therefore, the current through $L_2$ is $\dfrac{I}{2}$ and the current through $L_3$ is $\dfrac{I}{2}$.

The magnetic energy stored in an inductor is given by $U = \dfrac{1}{2} L i^2$.

The energy stored in the inductor $L_2$ is:
$U_l = \dfrac{1}{2} L \left(\dfrac{I}{2}\right)^2 = \dfrac{1}{8} L I^2$

The equivalent inductance of the entire circuit is:
$L_{eq} = L_1 + \dfrac{L_2 L_3}{L_2 + L_3} = L + \dfrac{L \cdot L}{L + L} = L + \dfrac{L}{2} = \dfrac{3L}{2}$

The total magnetic energy stored in the entire circuit is:
$U_t = \dfrac{1}{2} L_{eq} I^2 = \dfrac{1}{2} \left(\dfrac{3L}{2}\right) I^2 = \dfrac{3}{4} L I^2$

The ratio of the total energy to the energy stored in $L_2$ is:
$\dfrac{U_t}{U_l} = \dfrac{\dfrac{3}{4} L I^2}{\dfrac{1}{8} L I^2} = \dfrac{3}{4} \times 8 = 6$

Answer: $6$

</details>

---

### Q2. JEE Main 2026 (22 January Shift 1)

*Type:* `numerical` | *Level:* `2`

Inductance of a coil with $10^{4}$ turns is 10 mH and it is connected to a dc source of 10 V with internal resistance of $10 \Omega$. The energy density in the inductor when the current reaches $\left(\frac{1}{e}\right)$ of its maximum value is $\alpha \pi \times \frac{1}{e^{2}} \mathrm{~J} / \mathrm{m}^{3}$. The value of $\alpha$ is $\_\_\_\_$. ($\mu_{0}=4 \pi \times 10^{-7} \mathrm{Tm} / \mathrm{A}$).

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **20**

**Detailed Solution:**

$\mathrm{L}=10 \times 10^{-3} \mathrm{H}$
$\mathrm{N}=10^4$
<img style="width:200px;" src="https://cdn-question-pool.getmarks.app/pyq/jee_main_2026_watermark_improved/22S1_s_50.png">
$I_0=\frac{10}{10}=1 \mathrm{~A} \text { (max current) }$
$I=\frac{1}{\mathrm{e}}$
$E_{\mathrm{d}}=\frac{B^2}{2 \mu_0}$
$B=\mu_0 n I$
$L=\mu_0 n^2 \pi R^2 \ell$
$E_d=\frac{\mu_0 n^2 I^2}{2}$
$=\frac{4 \pi \times 10^{-7} \times 10^8 \times \frac{1}{\mathrm{e}^2}}{2}$
$=\frac{20 \pi}{\mathrm{e}^2}$

</details>

---

### Q3. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>In the given figure, an inductor and resistor are connected in series with a battery of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>emf</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> volt. <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>E</mi><mi>a</mi></msup><mrow><mn>2</mn><mi>b</mi></mrow></mfrac><mo>&#160;</mo><mi mathvariant="normal">J</mi><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> represents the maximum rate at which the energy is stored in the magnetic field (inductor). The numerical value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><mi>a</mi></mfrac></math> will be _____.</p><p style="text-align: center;"><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a75be6cd-840c-45db-ae10-cfea5230d182.png" style="width: 300px; height: 186px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<blockquote><p>The formula to calculate the current flowing through an L-R circuit is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mfrac><mi>E</mi><mi>R</mi></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>The energy stored within the inductor can be calculated as follows:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>E</mi><mtext>induction&#160;</mtext></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><msup><mi>i</mi><mn>2</mn></msup></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><mfrac><msup><mi>E</mi><mn>2</mn></msup><msup><mi>R</mi><mn>2</mn></msup></mfrac><msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup></mrow></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></mtd></mtr></mtable></math></p><p>The rate of change of energy stored within the inductor is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced><msub><mi>E</mi><mtext>induction&#160;</mtext></msub></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mn>2</mn><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup></mrow></mfenced><mo>&#183;</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup><mo>&#183;</mo><mfrac><mi>R</mi><mi>L</mi></mfrac><mo>&#183;</mo><mfrac><mrow><msup><mi>E</mi><mn>2</mn></msup><mi>L</mi></mrow><mrow><mn>2</mn><msup><mi>R</mi><mn>2</mn></msup></mrow></mfrac></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msup><mi>E</mi><mn>2</mn></msup><mi>R</mi></mfrac><mfenced close="]" open="["><mrow><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup><mo>-</mo><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mn>2</mn><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></mtd></mtr></mtable></math></p><p>For maximum rate,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>d</mi><mn>2</mn></msup><mi>E</mi></mrow><mrow><mi>d</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>From equation (3) and (4), it can be written that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced close="]" open="["><mrow><mfrac><mstyle displaystyle="true"><msup><mi>E</mi><mn>2</mn></msup></mstyle><mstyle displaystyle="true"><mi>R</mi></mstyle></mfrac><mfenced close="]" open="["><mrow><msup><mi>e</mi><mfrac><mstyle displaystyle="true"><mo>-</mo><mi>R</mi><mi>t</mi></mstyle><mstyle displaystyle="true"><mi>L</mi></mstyle></mfrac></msup><mo>-</mo><msup><mi>e</mi><mfrac><mstyle displaystyle="true"><mo>-</mo><mn>2</mn><mi>R</mi><mi>t</mi></mstyle><mstyle displaystyle="true"><mi>L</mi></mstyle></mfrac></msup></mrow></mfenced><mo>&#160;</mo></mrow></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mn>0</mn></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup><mo>=</mo><mn>2</mn><msup><mi>e</mi><mfrac><mrow><mo>-</mo><mn>2</mn><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup><mo>&#160;&#160;</mo></mtd></mtr><mtr><mtd></mtd><mtd><mo>&#8658;</mo></mtd><mtd><msup><mi>e</mi><mfrac><mrow><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></msup><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>5</mn></mfenced></mtd></mtr></mtable></math></p><p>From equation (3) and (5), it can be written, under maximum energy stored condition for the circuit, that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mfrac><mi>d</mi><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mfenced><msub><mi>E</mi><mtext>induction&#160;</mtext></msub></mfenced></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msup><mi>E</mi><mn>2</mn></msup><mi>R</mi></mfrac><mfenced close="]" open="["><mrow><msup><mn>2</mn><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><msup><mi>E</mi><mn>2</mn></msup><mrow><mn>4</mn><mi>R</mi></mrow></mfrac></mtd></mtr></mtable></math></p><p>Substitute the values of the resistance and compare with the given expression to obtain the values of the parameters.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><mi>a</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mi>b</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>2</mn><mi>R</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mn>50</mn></mtd></mtr></mtable></math></p><p>Hence, the required ratio is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>=</mo><mn>25</mn></math></p></blockquote>

</details>

---

### Q4. JEE Main 2023 (11 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

A coil has an inductance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">H</mi></math> and resistance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math>. A <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math> is applied across the coil. The energy stored in the magnetic field after the current has built up to its equilibrium value will be _____ <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **625**

**Detailed Solution:**

<p>The data given is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mi mathvariant="normal">H</mi><mspace linebreak="newline"/><mi>R</mi><mo mathvariant="italic">=</mo><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi><mspace linebreak="newline"/><mi>V</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></math></p><p>Using Ohm&#39;s law, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>I</mi><mi>R</mi></math>,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">V</mi></mrow><mrow><mn>4</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>The energy of an inductor is given by 
      <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>L</mi><msup><mi>I</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mfenced><mfrac><mn>25</mn><mn>4</mn></mfrac></mfenced><mo>=</mo><mn>625</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">J</mi></math></p>

</details>

---

### Q5. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The energy of an electromagnetic wave contained in a small volume oscillates with</p>

**Options:**

- **(A)** Double the frequency of the wave
- **(B)** The frequency of the wave
- **(C)** Half the frequency of the wave
- **(D)** Zero frequency

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Double the frequency of the wave**

**Detailed Solution:**

<blockquote><p>The formula to calculate the energy confined within the electric component of an electromagnetic wave can be written as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>u</mi><mi>E</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>E</mi><mn>2</mn></msup><mi>d</mi><mi>V</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Let&#39;s assume that the equation of the electric component is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mo>&#160;</mo><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Substitute the expression for the electric field component from equation (2) into equation (1) and simplify to obtain the expression for the energy confined within the small volume <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mi>V</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="right center left" columnspacing="0px"><mtr><mtd><msub><mi>u</mi><mi>E</mi></msub></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mfenced close="]" open="["><mrow><msub><mi>E</mi><mn>0</mn></msub><mo>&#160;</mo><mi>sin</mi><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced></mrow></mfenced><mn>2</mn></msup><mi>d</mi><mi>V</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>&#949;</mi><mn>0</mn></msub><msup><msub><mi>E</mi><mn>0</mn></msub><mn>2</mn></msup><msup><mi>sin</mi><mn>2</mn></msup><mfenced><mrow><mi>&#969;</mi><mi>t</mi><mo>+</mo><mi>&#981;</mi></mrow></mfenced><mi>d</mi><mi>V</mi></mtd></mtr><mtr><mtd></mtd><mtd><mo>=</mo></mtd><mtd><mfrac><mn>1</mn><mn>4</mn></mfrac><msub><mi>&#949;</mi><mn>0</mn></msub><msup><msub><mi>E</mi><mn>0</mn></msub><mn>2</mn></msup><mfenced close="]" open="["><mrow><mn>1</mn><mo>-</mo><mi>cos</mi><mfenced><mrow><mn>2</mn><mi>&#969;</mi><mi>t</mi><mo>+</mo><mn>2</mn><mi>&#981;</mi></mrow></mfenced></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></mtd></mtr></mtable></math></p><p>From equation (3), it can be concluded that the frequency of oscillation of the energy confined within a small volume is double the frequency of the wave.</p></blockquote>

</details>

---

### Q6. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>For the plane electromagnetic wave given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><msub><mi>E</mi><mn>0</mn></msub><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>&#8211;</mo><mi>k</mi><mi>x</mi><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><msub><mi>B</mi><mn>0</mn></msub><mi>sin</mi><mo>(</mo><mi>&#969;</mi><mi>t</mi><mo>-</mo><mi>k</mi><mi>x</mi><mo>)</mo><mo>,</mo></math> the ratio of average electric energy density to average magnetic energy density is </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<blockquote><p>The formula to calculate the average electric energy density is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>U</mi><mi>E</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msub><mi>&#949;</mi><mn>0</mn></msub><msup><mi>E</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>and, the formula to calculate average magnetic energy density is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>U</mi><mi>B</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msub><mi>&#956;</mi><mn>0</mn></msub></mrow></mfrac><msup><mi>B</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>For any particular electromagnetic wave, both magnetic and electric field are equally involved in contributing to energy density. Hence, the ratio of average electric energy density to magnetic energy density is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p></blockquote>

</details>

---

### Q7. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Two coils of self inductance <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>2</mn></msub></math> are connected in series combination having mutual inductance of the coils as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>. The equivalent self inductance of the combination will be</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/42385901-12f9-4eb9-80a7-9d42b05e90b4-image.png" style="width: 220px; height: 69px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>L</mi><mn>1</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><msub><mi>L</mi><mn>2</mn></msub></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>M</mi></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>+</mo><msub><mi>L</mi><mn>2</mn></msub><mo>-</mo><mn>2</mn><mi>M</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>+</mo><msub><mi>L</mi><mn>2</mn></msub><mo>+</mo><mi>M</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>+</mo><msub><mi>L</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><mi>M</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mn>1</mn></msub><mo>+</mo><msub><mi>L</mi><mn>2</mn></msub><mo>-</mo><mn>2</mn><mi>M</mi></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/cd0f0ba9-33d5-4c16-821c-892cef71d0ca-image.png" style="width: 230px; height: 101px;" /></p><p>Here self inductances are in series but their mutual inductances are linked oppositely.</p><p>As the inductors connected are in series opposition, hence magnetic flux will be opposing each other. Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>L</mi><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><msub><mi>L</mi><mn>1</mn></msub><mo>+</mo><msub><mi>L</mi><mn>2</mn></msub><mo>-</mo><mn>2</mn><mi>M</mi></math></p>

</details>

---

### Q8. JEE Main 2021 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>Consider an electrical circuit containing a two way switch <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>.</mo></math> Initially <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is open and then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> is connected to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>.</mo></math> As the current in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>6</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> attains a maximum value of steady-state level, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> is disconnected from <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math> and immediately connected to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub><mo>.</mo></math> Potential drop across <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math> resistor immediately after <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> is connected to <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi mathvariant="normal">V</mi><mo>.</mo></math> (Round off to the Nearest Integer)</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/c4ff0db2-b9a5-4e4c-ad8e-6bd96d2198c3-image.png" style="width: 300px; height: 139px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub></math> are connected, then the steady state current in the inductor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi><mo>=</mo><mfrac><mn>6</mn><mn>6</mn></mfrac><mo>=</mo><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">A</mi></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub></math> are connected then current through inductor remains same. So potential difference across <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">&#937;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mi>I</mi><mi>r</mi><mo>=</mo><mn>1</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>3</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math></p>

</details>

---

### Q9. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A coil of self inductance <math><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">H</mi></math> and resistance of <math><mn>0.1</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#937;</mi></math> is connected through a switch to a battery of internal resistance <math><mtext>&#160;</mtext><mn>0.9</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#937;</mi></math> . After the switch is closed, the time taken for the current to attain <math><mn>80</mn><mi mathvariant="normal">%</mi></math> of the saturation value is: <math> <mrow> <mrow><mo>[</mo> <mrow> <mi>ln</mi><mn>5</mn><mo>=</mo><mn>1.6</mn></mrow> <mo>]</mo></mrow></mrow> </math>

**Options:**

- **(A)** <math><mn>0.103</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>
- **(B)** <math><mn>0.002</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>
- **(C)** <math><mn>0.324</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>
- **(D)** <math><mn>0.016</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>0.016</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">s</mi></math>**

**Detailed Solution:**

<p>The instantaneous current in an LR circuit is given by the equation :
(instantaneous current) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>=</mo><msub><mi mathvariant="normal">I</mi><mi>s</mi></msub><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mi>R</mi><mi>t</mi></mrow><mi>L</mi></mfrac></mrow></msup></mrow></mfenced></math></p><p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>,</mo><mo>&#160;</mo><msub><mi mathvariant="normal">I</mi><mi mathvariant="normal">s</mi></msub><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">t</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">L</mi></math> are the instantaneous current, saturation current, resistance, time and inductance respectively.</p><p>Given that the current becomes so percent of saturation current.
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mn>0.8</mn></mrow></mfenced><msub><mrow><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">I</mi></mrow><mrow><mi>s</mi></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">I</mi></mrow><mrow><mi>s</mi></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>e</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mi>R</mi><mi>t</mi></mrow><mrow><mi>L</mi></mrow></mfrac></mrow></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>1</mn><mtext>&#937;</mtext><mo>+</mo><mn>0</mn><mo>.</mo><mn>9</mn><mtext>&#937;</mtext><mo>=</mo><mn>1</mn><mtext>&#937;</mtext></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0.8</mn><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mn>1</mn><mo>&#215;</mo><mi>t</mi></mrow><mrow><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfrac></mrow></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0.8</mn><mo>=</mo><mn>1</mn><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>100</mn><mi>t</mi></mrow></msup><mi mathvariant="normal">&#160;</mi></math>
Therefore, the time is:
<math><mi mathvariant="normal">t</mi><mo>=</mo><mfrac><mrow><mrow><mrow><mi>l</mi><mi mathvariant="normal">n</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mn>0.8</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></mrow><mrow><mn>100</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mrow><mrow><mi mathvariant="italic">ln</mi></mrow><mo>&#8289;</mo><mrow><mfenced separators="|"><mrow><mn>5</mn></mrow></mfenced></mrow></mrow></mrow><mrow><mn>100</mn></mrow></mfrac><mo>=</mo><mn>0.016</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">s</mi></math></p>

</details>

---

### Q10. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The self induced emf of a coil is <math><mn>25</mn></math> volts. When the current in it is changed at uniform rate from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi mathvariant="normal">A</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mi mathvariant="normal">A</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mi mathvariant="normal">s</mi></math> , the change in the energy of the inductance is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>637.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>740</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>437.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>540</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>437.5</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math>**

**Detailed Solution:**

<p>Induced emf / back emf in an inductor coil is given by </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|" separators="|"><mi mathvariant="normal">&#949;</mi></mfenced><mo>=</mo><mfrac><mi>Ldi</mi><mi>dt</mi></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><mo>=</mo><mi mathvariant="normal">L</mi><mo>&#215;</mo><mfrac><mfenced separators="|"><mrow><mn>25</mn><mo>-</mo><mn>10</mn></mrow></mfenced><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi mathvariant="normal">L</mi><mo>=</mo><mfrac><mn>25</mn><mn>15</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mi mathvariant="normal">H</mi></math>

Energy of inductor is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>Li</mi><mn>2</mn></msup></math></p><p>Energy change <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#9651;</mo><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi mathvariant="normal">L</mi><mfenced><mrow><msup><msub><mi mathvariant="normal">I</mi><mn>2</mn></msub><mn>2</mn></msup><mo>-</mo><msup><msub><mi mathvariant="normal">I</mi><mn>1</mn></msub><mn>2</mn></msup></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8710;</mo><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mn>625</mn><mo>-</mo><mn>100</mn></mrow></mfenced><mo>&#160;</mo><mi mathvariant="normal">J</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi mathvariant="normal">E</mi><mo>=</mo><mn>437</mn><mo>.5</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></math></p>

</details>

---

### Q11. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

An ideal capacitor of capacitance $0.2 \mu \mathrm{F}$ is charged to a potential difference of $10 \mathrm{~V}$. The charging battery is then disconnected. The capacitor is then connected to an ideal inductor of self inductance $0.5 \mathrm{mH}$. The current at a time when the potential difference across the capacitor is $5 \mathrm{~V}$, is:

**Options:**

- **(A)** $0.17 \mathrm{~A}$
- **(B)** $0.15 \mathrm{~A}$
- **(C)** $0.34 \mathrm{~A}$
- **(D)** $0.25 \mathrm{~A}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.17 \mathrm{~A}$**

**Detailed Solution:**

Given: Capacitance, $C=0.2 \mu \mathrm{F}=0.2 \times 10^{-6}$ $\mathrm{F}$
Inductance $\mathrm{L}=0.5 \mathrm{mH}=0.5 \times 10^{-3} \mathrm{H}$
Current $\mathrm{I}$ = ?
Using energy conservation
$$
\frac{1}{2} C V^2=\frac{1}{2} C V_1^2+\frac{1}{2} L I^2
$$
$\frac{1}{2} \times 0.2 \times 10^{-6} \times 10^2+0$
$=\frac{1}{2} \times 0.2 \times 10^{-6} \times 5^2+\frac{1}{2} \times 0.5 \times 10^{-3} I^2$
$\therefore \quad I=\sqrt{3} \times 10^{-1} \mathrm{~A}=0.17 \mathrm{~A}$

</details>

---

### Q12. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

In the circuit shown below, the key $\mathrm{K}$ is closed at $\mathrm{t}=0$. The current through the battery is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/OL8UitofjZCK2t-T-_CHQZ8qxgA6RJc6s5gSK1w5aFg.original.fullsize.png">

**Options:**

- **(A)** $\frac{\mathrm{VR}_1 \mathrm{R}_2}{\sqrt{\mathrm{R}_1^2+\mathrm{R}_2^2}}$ at $\mathrm{t}=0$ and $\frac{\mathrm{V}}{\mathrm{R}_2}$ at $\mathrm{t}=\infty$
- **(B)** $\frac{V}{R_2}$ at $t=0$ and $\frac{V\left(R_1+R_2\right)}{R_1 R_2}$ at $t=\infty$
- **(C)** $\frac{V}{R_2}$ at $t=0$ and $\frac{V R_1 R_2}{\sqrt{R_1^2+R_2^2}}$ at $t=\infty$
- **(D)** $\frac{V\left(R_1+R_2\right)}{R_1 R_2}$ at $t=0$ and $\frac{V}{R_2}$ at $t=\infty$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{V}{R_2}$ at $t=0$ and $\frac{V\left(R_1+R_2\right)}{R_1 R_2}$ at $t=\infty$**

**Detailed Solution:**

At $\mathrm{t}=0$, inductor behaves like an infinite resistance
So at $t=0, i=\frac{V}{R_2}$ and at $t=\infty$, inductor behaves like a conducting wire
$$
\mathrm{i}=\frac{\mathrm{V}}{\mathrm{R}_{\text {eq }}}=\frac{\mathrm{V}\left(\mathrm{R}_1+\mathrm{R}_2\right)}{\mathrm{R}_1 \mathrm{R}_2}
$$

</details>

---

### Q13. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The inductance between A and D is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/r_eEGNWze1ioHe--X3ACh228YGyVruIGIEthx_I5iMo.original.fullsize.png">

**Options:**

- **(A)** 3.66 H
- **(B)** 9 H
- **(C)** 0.66 H
- **(D)** 1 H

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1 H**

**Detailed Solution:**

The given circuit clearly shows that the inductors are in parallel we have, $\frac{1}{L}=\frac{1}{3}+\frac{1}{3}+\frac{1}{3}$ or $L=1$

</details>

---

