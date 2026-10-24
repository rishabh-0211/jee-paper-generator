# JEE Advanced Chemistry - Thermodynamics (C)

## Topic 2: First Law and Basic Fundamentals of Thermodynamics

**Total Questions:** 15

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

An ideal gas ($0.5$ mol), initially at $2$ bar pressure, is compressed at a constant temperature of $600$ K in two steps: first, against a constant external pressure of $P$ bar ($2 < P < 8$), and then against constant external pressure of $8$ bar. At each step, the compression is stopped only when the pressure of the gas becomes equal to the external pressure. The total work done on the gas in these steps is $W$. Considering all possible values of $P$ ($2 < P < 8$) and taking the gas constant as $R$ (in J K$^{-1}$ mol$^{-1}$), the minimum value of $|W|$ (in J) is

**Options:**

- **(A)** $207R$
- **(B)** $600R$
- **(C)** $630R$
- **(D)** $900R$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $600R$**

**Detailed Solution:**

Let the initial, intermediate, and final volumes of the gas be $V_1$, $V_2$, and $V_3$ respectively.

Using the ideal gas equation $V = \dfrac{nRT}{P}$, we have:
$V_1 = \dfrac{nRT}{2}$
$V_2 = \dfrac{nRT}{P}$
$V_3 = \dfrac{nRT}{8}$

The work done on the gas during the first step against a constant external pressure $P$ is:
$W_1 = -P_{ext,1}(V_2 - V_1) = -P \left( \dfrac{nRT}{P} - \dfrac{nRT}{2} \right) = nRT \left( \dfrac{P}{2} - 1 \right)$

The work done on the gas during the second step against a constant external pressure of $8$ bar is:
$W_2 = -P_{ext,2}(V_3 - V_2) = -8 \left( \dfrac{nRT}{8} - \dfrac{nRT}{P} \right) = nRT \left( \dfrac{8}{P} - 1 \right)$

The total work done on the gas is:
$W = W_1 + W_2 = nRT \left( \dfrac{P}{2} - 1 \right) + nRT \left( \dfrac{8}{P} - 1 \right) = nRT \left( \dfrac{P}{2} + \dfrac{8}{P} - 2 \right)$

To find the minimum value of $W$, we need to minimize the expression $\left( \dfrac{P}{2} + \dfrac{8}{P} \right)$.

Using the AM-GM inequality:
$\dfrac{P}{2} + \dfrac{8}{P} \ge 2 \sqrt{\dfrac{P}{2} \times \dfrac{8}{P}} = 2 \sqrt{4} = 4$

The minimum value is $4$, which occurs when $\dfrac{P}{2} = \dfrac{8}{P} \Rightarrow P^2 = 16 \Rightarrow P = 4$ bar. This value of $P$ lies within the given range $(2 < P < 8)$.

Substituting this minimum value back into the work equation:
$W_{min} = nRT (4 - 2) = 2nRT$

Given $n = 0.5$ mol and $T = 600$ K:
$W_{min} = 2 \times 0.5 \times R \times 600 = 600R$

Answer: $600R$

</details>

---

### Q2. JEE Advanced 2025 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Considering ideal gas behavior, the expansion work done (in kJ) when 144 g of water is electrolyzed completely under constant pressure at 300 K is _____
Use: Universal gas constant $(\mathrm{R})=8.3 \mathrm{~J} \mathrm{~K}^{-1} \mathrm{~mol}^{-1}$; Atomic mass (in amu): $\mathrm{H}=1, \mathrm{O}=16$ (mark absolute value as answer)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29.88**

**Detailed Solution:**

in official answer key answer was [-29.95 to -29.8] OR [29.8 to 29.95], we have updated the question to make it valid.
$\begin{array}{lcc}
\mathrm{H}_2 \mathrm{O}(l) \rightarrow & \mathrm{H}_2(\mathrm{~g})+ & \frac{1}{2} \mathrm{O}_2(\mathrm{~g}) \\
144 \mathrm{~g} & - & - \\
8 \mathrm{~mol} & 8 \mathrm{~mol} & 4 \mathrm{~mol} \\
\mathrm{~W}=-\mathrm{P} \Delta \mathrm{~V}= & -(\Delta \mathrm{n}) \mathrm{RT}
\end{array}$
$\begin{aligned}
&\text { Change in gaseous moles }=12\\
&\Rightarrow \mathrm{W}=-\frac{12 \times 8.3 \times 300}{1000} \mathrm{~kJ}=-29.88 \mathrm{~kJ} .
\end{aligned}$

</details>

---

### Q3. JEE Advanced 2023 (Paper 1)

*Type:* `numerical` | *Level:* `2`

<p>One mole of an ideal monoatomic gas undergoes two reversible processes <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi><mo>)</mo></math> as shown in the given figure:</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/c0f9eca0-1921-4fb9-9579-db85df006fd9.png" style="width: 420px; height: 351px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></math> is an adiabatic process. If the total heat absorbed in the entire process <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi><mo>)</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mn>10</mn></math>, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>logV</mi><mn>3</mn></msub></math> is
[Use molar heat capacity of the gas at constant pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">p</mi><mo>,</mo><mi mathvariant="normal">m</mi></mrow></msub><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi mathvariant="normal">R</mi></math>]</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></mrow></msub><mo>=</mo><mn>0</mn></math>                              <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;(</mtext><mo>&#8757;</mo><mtext>&#160;adiabatic)&#160;</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></mrow></msub><mo>+</mo><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">c</mi></mrow></msub><mo>=</mo><msub><mi>nRT</mi><mn>2</mn></msub><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mrow><mo>&#160;</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfrac></mfenced></math>     ...(i)</p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;E</mi><mo>=</mo><mi mathvariant="normal">q</mi><mo>+</mo><mi mathvariant="normal">w</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;E</mi><mo>=</mo><mn>0</mn></math>                  (since isothermic)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi><mo>=</mo><mo>-</mo><mi mathvariant="normal">w</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mo>-</mo><msub><mi>nRT</mi><mn>2</mn></msub><mi>ln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mrow><mo>&#160;</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>nRT</mi><mn>2</mn></msub><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mrow><mo>&#160;</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">B</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi>nRT</mi><mn>2</mn></msub><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mrow><mo>&#160;</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">B</mi><mo stretchy="false">&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mo>&#8289;</mo><mfenced separators="|"><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>[</mo><mi>Since</mi><mo>&#160;</mo><mi mathvariant="normal">n</mi><mo>&#160;</mo><mo>=</mo><mn>1</mn><mo>]</mo></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">B</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mn>1</mn></msub><mo>&#160;</mo><msubsup><mi mathvariant="normal">V</mi><mn>1</mn><mrow><mi mathvariant="normal">&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><msub><mi mathvariant="normal">T</mi><mn>2</mn></msub><mo>&#160;</mo><msubsup><mi mathvariant="normal">V</mi><mn>2</mn><mrow><mi mathvariant="normal">&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>600</mn><mo>&#160;</mo><msubsup><mi mathvariant="normal">V</mi><mn>1</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>=</mo><mn>60</mn><mo>&#160;</mo><msubsup><mi mathvariant="normal">V</mi><mn>2</mn><mrow><mi>&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msubsup><mi mathvariant="normal">V</mi><mn>2</mn><mrow><mi mathvariant="normal">&#947;</mi><mo>-</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mn>5</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>=</mo><msubsup><mi mathvariant="normal">V</mi><mn>2</mn><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>-</mo><mn>1</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow><mn>5</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>=</mo><msubsup><mi mathvariant="normal">V</mi><mn>2</mn><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub><mo>=</mo><msup><mn>10</mn><mrow><mfrac><mn>5</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></msup><mo>=</mo><msup><mn>10</mn><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub><mo>=</mo><msup><mn>10</mn><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math>
From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi>nRT</mi><mn>2</mn></msub><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></mfenced></math>
Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">q</mi><mrow><mi mathvariant="normal">A</mi><mo>&#8594;</mo><mi mathvariant="normal">C</mi></mrow></msub><mo>=</mo><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mn>10</mn><mo>=</mo><msub><mi>RT</mi><mn>2</mn></msub><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mrow><mo>&#160;</mo><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>10</mn><mo>=</mo><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mn>10</mn><mo>=</mo><mi>ln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msup><mn>10</mn><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>=</mo><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msup><mn>10</mn><mfrac><mn>5</mn><mn>2</mn></mfrac></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><mo>=</mo><msup><mn>10</mn><mrow><mn>1</mn><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></msup><mo>=</mo><msup><mn>10</mn><mfrac><mn>7</mn><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>logV</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mi>log</mi><msup><mn>10</mn><mrow><mn>7</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q4. JEE Advanced 2021 (Paper 2)

*Type:* `numerical` | *Level:* `2`

One mole of an ideal gas at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>900</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>, undergoes two reversible processes, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> followed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math>, as shown below. If the work done by the gas in the two processes are same, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></math> is<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/b3bdc189-7931-4ec2-bb46-c10b595deea3-image.png" style="width: 280px; height: 210px;" /></p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">U</mi></math> : internal energy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>:</mo></math> entropy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>:</mo></math> pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi><mo>:</mo></math> volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">R</mi></math> : gas constant) </p><p>(Given: molar heat capacity at constant volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">V</mi><mo>,</mo><mi mathvariant="normal">m</mi></mrow></msub></math> of the gas is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><mi mathvariant="normal">R</mi></math>)</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p><strong>Process -I:</strong> Adiabatic reversible process.</p><p>(Since entropy is constant)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">W</mi><mi mathvariant="normal">I</mi></msub><mo>=</mo><mi>&#916;U</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>450</mn><mo>&#8722;</mo><mn>2250</mn></mrow></mfenced><mi mathvariant="normal">R</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1800</mn><mo>&#160;</mo><mi mathvariant="normal">R</mi></math></p><p><strong>Process II:</strong> Isothermal reversible process.</p><p>(since internal energy is constant and entropy is increased)</p><p>Work done:</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable equalcolumns="true" equalrows="true"><mtr><mtd><msub><mi mathvariant="normal">W</mi><mi>II</mi></msub><mo>=</mo><mo>&#8722;</mo><mi>nRTln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">f</mi></msub><msub><mi mathvariant="normal">V</mi><mi mathvariant="normal">i</mi></msub></mfrac></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><msub><mi mathvariant="normal">W</mi><mi>II</mi></msub><mo>=</mo><mo>&#8722;</mo><mi>nRTln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></mfenced></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">W</mi><mi>II</mi></msub><mo>=</mo><mo>&#8722;</mo><mfrac><mn>900</mn><mn>5</mn></mfrac><mi>Rln</mi><mfenced><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi mathvariant="normal">W</mi><mi>II</mi></msub></mfenced><mo>=</mo><mfrac><mn>900</mn><mn>5</mn></mfrac><mi>Rln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">U</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi>nRT</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>450</mn><mo>&#160;</mo><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mi>nRT</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>nRT</mi><mo>=</mo><mfrac><mn>900</mn><mn>5</mn></mfrac><mi mathvariant="normal">R</mi></math></p><p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><msub><mi mathvariant="normal">W</mi><mi mathvariant="normal">I</mi></msub></mfenced><mo>=</mo><mfenced close="|" open="|"><msub><mi mathvariant="normal">W</mi><mi>II</mi></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1800</mn><mi mathvariant="normal">R</mi><mo>=</mo><mfrac><mn>900</mn><mn>5</mn></mfrac><mi mathvariant="normal">R</mi><mo>&#160;</mo><mi>ln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ln</mi><mfrac><msub><mi mathvariant="normal">V</mi><mn>3</mn></msub><msub><mi mathvariant="normal">V</mi><mn>2</mn></msub></mfrac><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q5. JEE Advanced 2021 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

An ideal gas undergoes a reversible isothermal expansion from state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> to state II followed by a reversible adiabatic expansion from state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> to state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>III</mi><mo>.</mo></math> The correct plot <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">s</mi></mfenced></math> representing the changes from state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> to state <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>III</mi></math> is(are)<p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi></math>: pressure, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">V</mi></math>: volume, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math>: temperature, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">H</mi></math>: enthalpy, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math>: entropy)</p>

**Options:**

- **(A)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/b0ddc9e5-4cbd-45ef-a179-6f2e363a3ebd-image.png" style="width: 180px; height: 181px;" /></p>
- **(B)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/ad1259a6-e1e2-4f03-8a24-a701a1cf19a6-image.png" style="width: 180px; height: 173px;" /></p>
- **(C)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/3f784a9f-2f04-4f90-9df0-e6abf5d142a1-image.png" style="width: 180px; height: 181px;" /></p>
- **(D)** <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cea52900-7d8d-475b-82da-66a37fa83d87-image.png" style="width: 180px; height: 177px;" /></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/cea52900-7d8d-475b-82da-66a37fa83d87-image.png" style="width: 180px; height: 177px;" /></p>**

**Detailed Solution:**

Reversible isothermal expansion from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi><mo>&#8594;</mo><mi>II</mi></math> during this process<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi><mo>=</mo></math> constant</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;H</mi><mo>=</mo><mi>&#916;U</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">H</mi><mo>=</mo></math> constant.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;S</mi><mo>&#8800;</mo><mn>0</mn></math> Entropy will increase <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PV</mi><mo>=</mo></math> constant.</p><p>and during adiabatic reversible expansion.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">q</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;U</mi><mo>=</mo><mi mathvariant="normal">w</mi><mo>=</mo><mo>&#8722;</mo><mi>ve</mi></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi></math> will decrease</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;H</mi><mo>=</mo><msub><mi>nc</mi><mi mathvariant="normal">p</mi></msub><mi>&#916;T</mi><mo>=</mo><mo>-</mo><mi>ve</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">H</mi></math> will decrease</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#916;S</mi><mo>=</mo><mn>0</mn></math> (isoentropic process)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo></math>constant. and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>pv</mi><mi mathvariant="normal">r</mi></msup><mo>=</mo></math> constant.</p><p>Keeping in mind correct graph are 1,2 and 4.</p><p> </p>

</details>

---

### Q6. JEE Advanced 2020 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>In thermodynamics, the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>-</mo><mi mathvariant="normal">V</mi></math> work done is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">w</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><msub><mi>dVP</mi><mi>ext</mi></msub></math>. For a system undergoing a particular process, the work done is,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">w</mi><mo>=</mo><mo>-</mo><mo>&#8747;</mo><mi>dV</mi><mfenced><mrow><mfrac><mi>RT</mi><mrow><mi mathvariant="normal">V</mi><mo>-</mo><mi mathvariant="normal">b</mi></mrow></mfrac><mo>-</mo><mfrac><mi mathvariant="normal">a</mi><msup><mi mathvariant="normal">V</mi><mn>2</mn></msup></mfrac></mrow></mfenced></math>. This equation is applicable to a</p>

**Options:**

- **(A)** system that satisfies the van der Waals equation of state.
- **(B)** process that is reversible and isothermal.
- **(C)** process that is reversible and adiabatic.
- **(D)** process that is irreversible and at constant pressure.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) process that is reversible and adiabatic.**

**Detailed Solution:**

\(W=-\int P_{\text {ext }} d v\)

From van der waal equation of state for one mole gas \(p+\frac{a}{v^{2}}(v-b)=\mathrm{RT}\)

\(p=\frac{\mathrm{RT}}{(v-b)}-\frac{a}{v^{2}}\)

For reversible process

\(p_{\text {ext }}=p_{\text {gas }}\)

\(W=-\int \frac{\text {RT }}{(v-b)}-\frac{a}{v^{2}}\)

process is only not applicable for irreversible process.

</details>

---

### Q7. JEE Advanced 2018 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>A reversible cyclic process for an ideal gas is shown below. Here, <math><mi>P</mi><mo>,</mo><mi> </mi><mi>V</mi><mo>,</mo><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>T</mi></math> are pressure, volume and temperature, respectively. The thermodynamic parameters <math><mi>q</mi><mo>,</mo><mi> </mi><mi>w</mi><mo>,</mo><mi> </mi><mi>H</mi><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>U</mi></math> are heat, work, enthalpy and internal energy, respectively.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/2fcdab9c-3af5-47c3-a08f-eca603449393-image.png"/>
The correct option(s) is (are)</p>

**Options:**

- **(A)** <math><msub><mrow><mi>q</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mrow><mi>w</mi></mrow><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math>
- **(B)** <math><mi> </mi><msub><mrow><mi>w</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mi> </mi></math>
- **(C)** <math><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub><mo>&lt;</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mrow><mi>q</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub></math>
- **(D)** <math><mi> </mi><mi> </mi><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mi mathvariant="normal"> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal"> </mi><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub><mo>&gt;</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi> </mi><mi> </mi><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mi mathvariant="normal"> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi mathvariant="normal"> </mi><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub><mo>&gt;</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub></math>**

**Detailed Solution:**

AC → Isochoric
AB → Isothermal
BC → Isobaric
 <math><mo>#</mo><msub><mrow><mi>q</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>V</mi></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math> 
 <math><msub><mrow><mi>W</mi></mrow><mrow><mi>A</mi><mi>B</mi></mrow></msub><mo>=</mo><mi>n</mi><mi>R</mi><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mrow><mrow><mi mathvariant="normal">ln</mi></mrow><mo>⁡</mo><mrow><mfenced separators="|"><mrow><mfrac><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow></mrow></math>      A (wrong)
 <math><mo>#</mo><msub><mrow><mi>q</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>A</mi><mi>C</mi></mrow></msub><mo>=</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>P</mi></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced></math> 
 <math><msub><mrow><mi>W</mi></mrow><mrow><mi>B</mi><mi>C</mi></mrow></msub><mo>=</mo><mo>-</mo><msub><mrow><mi>P</mi></mrow><mrow><mn>2</mn></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>V</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math>      B (correct)
 <math><mo>#</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>P</mi></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced><mo>&lt;</mo><mi>n</mi><msub><mrow><mi>C</mi></mrow><mrow><mi>V</mi></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></math>              C (correct)
 <math><mo>∆</mo><msub><mrow><mi>H</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub><mo>&lt;</mo><mo>∆</mo><msub><mrow><mi>U</mi></mrow><mrow><mi>C</mi><mi>A</mi></mrow></msub></math> 
 <math><mo>#</mo><mi>D</mi></math>      (wrong)

</details>

---

### Q8. JEE Advanced 2016 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

One mole of an ideal gas at <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> in thermal contact with its surroundings expands isothermally from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi mathvariant="normal">L</mi></math> against a constant pressure of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>0</mn><mo>&#160;</mo><mi>atm</mi></math>. In this process, the change in entropy of the surroundings <math><mfenced separators="|"><mrow><mo>&#8710;</mo><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">r</mi></mrow></msub></mrow></mfenced></math> in <math><mi mathvariant="normal">J</mi><mi mathvariant="normal">&#160;</mi><msup><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> is:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>&#160;</mo><mi mathvariant="normal">L</mi><mo>&#160;</mo><mi>atm</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>101</mn><mo>.</mo><mn>3</mn><mo>&#160;</mo><mi mathvariant="normal">J</mi></mrow></mfenced></math>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo><mn>763</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>.</mo><mn>013</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>.</mo><mn>013</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn><mo>.</mo><mn>763</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn><mo>.</mo><mn>013</mn></math>**

**Detailed Solution:**

From <math><msup><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi></mrow></msup></math> law of thermodynamics,
<math><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">s</mi></mrow></msub><mo>=</mo><mo>&#8710;</mo><mi mathvariant="normal">U</mi><mo>-</mo><mi mathvariant="normal">w</mi><mo>=</mo><mn>0</mn><mo>-</mo><mfenced close="]" open="[" separators="|"><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi><mi mathvariant="normal">t</mi></mrow></msub><mo>.</mo><mo>&#8710;</mo><mi mathvariant="normal">V</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">m</mi><mo>&#215;</mo><mfenced separators="|"><mrow><mn>2.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">L</mi><mo>-</mo><mn>1.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">L</mi></mrow></mfenced><mo>=</mo><mn>3.0</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">L</mi><mo>&#160;</mo><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">m</mi></math>
<math><mo>&#8756;</mo><mo>&#8710;</mo><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">r</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">v</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">u</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">r</mi></mrow></msub></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">y</mi><mi mathvariant="normal">s</mi></mrow></msub></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac></math>
<math><mo>=</mo><mo>-</mo><mfrac><mrow><mn>3.0</mn><mo>&#215;</mo><mn>101.3</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi></mrow><mrow><mn>300</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">K</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mn>1</mn><mo>.013</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">J</mi><mo>/</mo><mi mathvariant="normal">K</mi></math>
Alternate solution:
<math><mo>&#8710;</mo><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi mathvariant="normal">surr</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">surr</mi></mrow></msub></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">sys</mi></mrow></msub></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">W</mi></mrow><mrow><mi mathvariant="normal">sys</mi></mrow></msub></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac></math>
<math><mo>&#8757;</mo></math> For the isothermal process:
<math><mo>&#8710;</mo><mi mathvariant="normal">U</mi><mo>=</mo><mn>0</mn></math>     <math><msub><mrow><mi mathvariant="normal">q</mi></mrow><mrow><mi mathvariant="normal">sys</mi></mrow></msub><mo>=</mo><mo>-</mo><msub><mrow><mi mathvariant="normal">W</mi></mrow><mrow><mi mathvariant="normal">sys</mi></mrow></msub></math>
<math><mo>&#8710;</mo><msub><mrow><mi mathvariant="normal">S</mi></mrow><mrow><mi mathvariant="normal">surr.</mi></mrow></msub><mo>=</mo><mfrac><mrow><mo>-</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mi mathvariant="normal">ext</mi></mrow></msub><mfenced separators="|"><mrow><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">f</mi></mrow></msub><mo>-</mo><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mi mathvariant="normal">i</mi></mrow></msub></mrow></mfenced></mrow><mrow><mi mathvariant="normal">T</mi></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mo>-</mo><mn>3</mn><mo>(</mo><mn>2</mn><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>300</mn></mrow></mfrac><mo>&#215;</mo><mn>101.3</mn></math>
<math><mo>=</mo><mo>-</mo><mn>1.013</mn><mi mathvariant="normal">&#160; J</mi><mo>/</mo><mi mathvariant="normal">K</mi></math>

</details>

---

### Q9. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

<p>An ideal gas in a thermally insulated vessel at internal pressure = <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub></math> , volume = <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and absolute temperature = <math><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>1</mn></mrow></msub></math> expands irreversibly against zero external pressure, as shown in the diagram. The final internal pressure, volume and absolute temperature of the gas are <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub></math> , <math><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub></math> and <math><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>2</mn></mrow></msub></math> , respectively. For this expansion,

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image2-1ac2a0f3-ab7f-4534-9566-f76b23fbae75.jpg"/></p>

**Options:**

- **(A)** <math><mi mathvariant="normal">q</mi><mo>=</mo><mn>0</mn></math>
- **(B)** <math><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
- **(C)** <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></math>
- **(D)** <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><msubsup><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow><mrow><mi mathvariant="normal">γ</mi></mrow></msubsup><mo>=</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><msubsup><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">γ</mi></mrow></msubsup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub></math>**

**Detailed Solution:**

Since container is thermally insulated. So, q = 0, and it is a case of free expansion therefore W = 0 and 
 <math><mo>∆</mo><mi mathvariant="normal">E</mi><mo>=</mo><mn>0</mn></math> 
So,  <math><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  
Also,  <math><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi mathvariant="normal">V</mi></mrow><mrow><mn>2</mn></mrow></msub></math>

</details>

---

### Q10. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong> A fixed mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi mathvariant="normal">m</mi><mo>&#39;</mo></math> of a gas is subjected to transformation of states from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> and back to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> as shown in the figure



<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012647_Ques1_1..jpg" style="width: 248px; height: 206px;" />
 <strong> Question : </strong>The pair of isochoric processes among the transformation of states is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> to  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math>**

**Detailed Solution:**

<math> <mrow> <mtext>L</mtext> <mo>&#160;&#8594;&#160;</mo> <mtext>M</mtext> </mrow> </math> and <math> <mrow> <mtext>N</mtext> <mo>&#160;&#8594;&#160;</mo> <mtext>K</mtext> </mrow> </math> are isochoric processes at constant volume

</details>

---

### Q11. JEE Advanced 2013 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong> A fixed mass <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi mathvariant="normal">m</mi><mo>&#39;</mo></math> of a gas is subjected to transformation of states from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> and back to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> as shown in the figure



<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012647_Ques1_1..jpg" style="width: 248px; height: 206px;" />
 <strong> Question : </strong>The succeeding operations that enable this transformation of states are

**Options:**

- **(A)** Heating, cooling, heating, cooling
- **(B)** Cooling, heating, cooling, heating
- **(C)** Heating, cooling, cooling, heating
- **(D)** Cooling, heating, heating, cooling

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) Heating, cooling, cooling, heating**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> isobaric process, volume increases with increase in temperature i.e., Heating
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> isochoric process, pressures decreases with decrease in temperature i.e., cooling
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> isobaric process, volume decreases with decrease in temp i.e., cooling
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi></math> isochoric process, pressures increases with increase in temperature i.e., heating

</details>

---

### Q12. JEE Advanced 2012 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

The reversible expansion of an ideal gas under adiabatic and isothermal conditions is shown in the figure. Which of the following statement(s) is (are) correct?

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/eo2Y8s7OU5kL5byObpI5g2PjgFs-pKTedMEUhZEyH5E.original.fullsize.png">

**Options:**

- **(A)** $T_{1}=T_{2}$
- **(B)** $T_{3}>T_{1}$
- **(C)** $w_{\text {isothermal }}>w_{\text {adiahatic }}$
- **(D)** $\Delta U_{\text {isothermal }}>\Delta U_{\text {adiabatic }}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\Delta U_{\text {isothermal }}>\Delta U_{\text {adiabatic }}$**

**Detailed Solution:**

$T_{1}=T_{2}$ because process is isothermal.

Work done in adiabatic process is less than in isothermal process because area covered by isothermal curve is more than the area covered by the adiabatic curve.

In adiabatic process expansion occurs byusing internal energy, hence, it decreases while in isothermal process temperature remains constant, that's why no change in internal energy.

</details>

---

### Q13. JEE Advanced 2012 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

For an ideal gas, consider only P-V work in going from an initial state $\mathrm{X}$ to the final state $\mathrm{Z}$. The final state $\mathrm{Z}$ can be reached by either of the two paths shown in the figure. Which of the following choice(s) is (are) correct?

[Take $\Delta \mathrm{S}$ as change in entropy and w as work done].

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/sUaDDrqK6xaVRvm7zYNxFwLWFJ_-V9oHMI5FoRk7u7Y.original.fullsize.png">

**Options:**

- **(A)** $\Delta \mathrm{S}_{x \rightarrow z}=\Delta \mathrm{S}_{x \rightarrow y}+\Delta \mathrm{S}_{y \rightarrow z}$
- **(B)** $\mathrm{w}_{x \rightarrow z}=\mathrm{w}_{x \rightarrow y}+\mathrm{w}_{y \rightarrow z}$
- **(C)** $\mathrm{w}_{x \rightarrow y \rightarrow z}=\mathrm{w}_{x \rightarrow y}$
- **(D)** $\Delta \mathrm{S}_{x \rightarrow y \rightarrow z}=\Delta \mathrm{S}_{x \rightarrow y}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\mathrm{w}_{x \rightarrow y \rightarrow z}=\mathrm{w}_{x \rightarrow y}$**

**Detailed Solution:**

$\Delta S_{X \rightarrow Z}=\Delta S_{X \rightarrow Y}+\Delta S_{Y \rightarrow Z}$ [Entropy is a state function, hence additive]

$w_{X \rightarrow Y \rightarrow Z}=w_{X \rightarrow Y}$ [Work done in $Y \rightarrow Z$ is zero because it is an isochoric process].

</details>

---

### Q14. JEE Advanced 2010 (Paper 2)

*Type:* `numerical` | *Level:* `3`

One mole of an ideal gas is taken from $a$ to $b$ along two paths denoted by the solid and the dashed lines as shown in the graph below. If the work done along the solid line path is $W_s$ and that along the dotted line path is $W_d$, then the integer closest to the ratio $\frac{W_d}{W_s}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/v5OJsPNE5bM9jw0nhHQppgggg6_GeY4sEcPU19pQ4wg.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Solid line represents reversible isothermal process.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/sH7FLf3CnNk6SLizs2CpYGsL1ts_CnefDrRK8phgEt0.original.fullsize.png">

So, work $W_s=-4 \times 0.5 \ln \left(\frac{5.5}{0.5}\right)=-2 \ln 11 \mathrm{~L}-\mathrm{atm}$
Dotted line represents irreversible process
So, work
$$
W_d=-\left\{4 \times 1.5+1 \times 1+\frac{2}{3} \times 2.5\right\}=-\left\{6+1+\frac{5}{3}\right\} \mathrm{L}-\mathrm{atm}=-\frac{26}{3} \mathrm{~L}-\mathrm{atm}
$$
So $\quad \frac{W_d}{W_s}=\frac{26}{3 \times 2 \ln 11} \approx 2$
Energetics
Conceptual
III

</details>

---

### Q15. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `1`

A monoatomic ideal gas undergoes a process in which the ratio of $P$ to $V$ at any instant is constant and equals to 1 . What is the molar heat capacity of the gas?

**Options:**

- **(A)** $\frac{4 R}{2}$
- **(B)** $\frac{3 R}{2}$
- **(C)** $\frac{5 R}{2}$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4 R}{2}$**

**Detailed Solution:**

The molar heat capacity for any process is given by a following expression
$C=C_V+\frac{R}{1-\gamma}$ when $p V^\gamma=$ constant and $C_p / C_V=\gamma$
Here, $\frac{p}{V}=1$ i.e., $p V^{-1}=$ constant
$$
\therefore \quad C=\frac{3}{2} R+\frac{R}{1-(-1)}=\frac{3}{2} R+\frac{R}{2}=\frac{4}{2} R
$$

</details>

---

