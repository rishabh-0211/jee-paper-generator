# JEE Advanced Physics - Thermal Properties of Matter

## Topic 4: Conduction

**Total Questions:** 7

---

### Q1. JEE Advanced 2026 (Paper 1)

*Type:* `numerical` | *Level:* `3`

As shown in the figure, an insulated container is fitted with a thermally conducting but immovable partition $(P_1)$ and a freely movable but thermally insulated piston $(P_2)$. The partition $P_1$ with thermal conductivity $K$, cross sectional area $A$ and width $x$ divides the container into two sections, $S_1$ and $S_2$, each containing one mole of a monoatomic gas. The piston $P_2$ moves freely such that the gas in $S_2$ is always at the atmospheric pressure. Initially, the difference between the temperatures of $S_1$ and $S_2$ is $\Delta T_0$. The time it takes for the temperature difference to become $\dfrac{\Delta T_0}{2}$ is $n x R / K A$, where $R$ is the universal gas constant. The value of $n$ is:
[Given: $\ln 2 \approx 0.7$]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p1_english__q27_d1.png" />

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.66**

**Detailed Solution:**

Let $T_1$ and $T_2$ be the temperatures of the gases in sections $S_1$ and $S_2$ respectively. Assume $T_1 > T_2$, so heat flows from $S_1$ to $S_2$.

The rate of heat transfer through the partition $P_1$ is given by Fourier's law of heat conduction:
$\dfrac{dQ}{dt} = \dfrac{KA}{x} (T_1 - T_2)$

For section $S_1$, the volume is constant (since $P_1$ is immovable). Thus, the process is isochoric. The heat lost by $S_1$ is:
$dQ = -n_1 C_V dT_1$
Since the gas is monoatomic and $n_1 = 1$ mole, $C_V = \dfrac{3}{2}R$.
$\Rightarrow dT_1 = -\dfrac{2 dQ}{3R}$

For section $S_2$, the pressure is constant (since $P_2$ is freely movable and exposed to atmospheric pressure). Thus, the process is isobaric. The heat gained by $S_2$ is:
$dQ = n_2 C_P dT_2$
Since the gas is monoatomic and $n_2 = 1$ mole, $C_P = \dfrac{5}{2}R$.
$\Rightarrow dT_2 = \dfrac{2 dQ}{5R}$

The change in the temperature difference $d(\Delta T) = d(T_1 - T_2)$ is:
$d(T_1 - T_2) = dT_1 - dT_2 = -\dfrac{2 dQ}{3R} - \dfrac{2 dQ}{5R} = -\dfrac{16 dQ}{15R}$

Substituting the rate of heat transfer $\dfrac{dQ}{dt}$ into the equation:
$\dfrac{d(T_1 - T_2)}{dt} = -\dfrac{16}{15R} \left( \dfrac{KA}{x} (T_1 - T_2) \right)$

Let $\Delta T = T_1 - T_2$. The differential equation becomes:
$\dfrac{d(\Delta T)}{\Delta T} = -\dfrac{16 KA}{15 R x} dt$

Integrating both sides from $t = 0$ to $t$, where the temperature difference goes from $\Delta T_0$ to $\dfrac{\Delta T_0}{2}$:
$\int_{\Delta T_0}^{\Delta T_0 / 2} \dfrac{d(\Delta T)}{\Delta T} = -\dfrac{16 KA}{15 R x} \int_0^t dt$

$\ln\left(\dfrac{1}{2}\right) = -\dfrac{16 KA}{15 R x} t$

$-\ln 2 = -\dfrac{16 KA}{15 R x} t$

$t = \dfrac{15 R x \ln 2}{16 KA}$

Given that $\ln 2 \approx 0.7$:
$t = \dfrac{15 \times 0.7}{16} \dfrac{x R}{KA} = \dfrac{10.5}{16} \dfrac{x R}{KA} = \dfrac{21}{32} \dfrac{x R}{KA} = 0.65625 \dfrac{x R}{KA}$

Comparing this with the given expression $t = n \dfrac{x R}{K A}$, we get:
$n = 0.65625$

Answer: $0.66$

</details>

---

### Q2. JEE Advanced 2019 (Paper 1)

*Type:* `singleCorrect` | *Level:* `3`

A current carrying wire heats a metal rod. The wire provides a constant power <math><mfenced separators="|"><mrow><mi mathvariant="normal">P</mi></mrow></mfenced></math> to the rod. The metal rod is enclosed in an insulated container. It is observed that the temperature <math><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi></mrow></mfenced></math> in the metal rod changes with time <math><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced></math> as:
<math><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>=</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">&#946;</mi><msup><mrow><mi mathvariant="normal">t</mi></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow></msup></mrow></mfenced></math>
where <math><mi mathvariant="normal">&#946;</mi></math> is a constant with appropriate dimension while <math><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></math> is a constant with dimension of temperature. The heat capacity of the metal is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn><mi mathvariant="normal">P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>-</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><msup><mrow><mi mathvariant="normal">β</mi></mrow><mrow><mn>4</mn></mrow></msup><msubsup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn><mi mathvariant="normal">P</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>-</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">β</mi></mrow><mrow><mn>4</mn></mrow></msup><msubsup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>3</mn></mrow></msubsup></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>4</mn><mi mathvariant="normal">P</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>-</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>4</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">β</mi></mrow><mrow><mn>4</mn></mrow></msup><msubsup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msubsup></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn><mi mathvariant="normal">P</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>-</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">β</mi></mrow><mrow><mn>4</mn></mrow></msup><msubsup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></msubsup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>4</mn><mi mathvariant="normal">P</mi><msup><mrow><mfenced separators="|"><mrow><mi mathvariant="normal">T</mi><mfenced separators="|"><mrow><mi mathvariant="normal">t</mi></mrow></mfenced><mo>-</mo><msub><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mi mathvariant="normal">β</mi></mrow><mrow><mn>4</mn></mrow></msup><msubsup><mrow><mi mathvariant="normal">T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></msubsup></mrow></mfrac></math>**

**Detailed Solution:**

Heat required for small increment in temperature of a substance is given by
 <math><mi>d</mi><mi>Q</mi><mo>=</mo><mi>m</mi><mo>.</mo><mi>s</mi><mo>.</mo><mi>d</mi><mi>T</mi></math> 
where,  <math><mi>m</mi><mo>=</mo></math> mass of substances
or  <math><mi>s</mi><mo>=</mo></math> specific heat of substance
Now, heat capacity,  <math><mi>H</mi><mo>=</mo><mi>m</mi><mo>.</mo><mi>s</mi><mo>.</mo></math> 
 <math><mo>∴</mo><mtext>  </mtext><mi>d</mi><mi>Q</mi><mo>=</mo><mi>H</mi><mo>.</mo><mi>d</mi><mi>T</mi></math> 
 <math><mo>⇒</mo></math>  Rate of heat absorption by the rod,  <math><mfrac><mrow><mi>d</mi><mi>Q</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>P</mi><mo>=</mo><mi>H</mi><mo>⋅</mo><mfrac><mrow><mi>d</mi><mi>T</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac></math>  .......(1)
But given that, temperature of rod as a function of time is
 <math><mi>T</mi><mo>=</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>β</mi><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow></msup></mrow></mfenced></math>  ......(2)
 <math><mo>⇒</mo><mfrac><mrow><mi>d</mi><mi>T</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>⋅</mo><mi>β</mi><mo>⋅</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><msup><mrow><mi>t</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math> 
Putting it in (1) gives
 <math><mi>P</mi><mo>=</mo><mi>H</mi><mo>⋅</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>⋅</mo><mi>β</mi><mo>⋅</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>⋅</mo><msup><mrow><mi>t</mi></mrow><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math> 
 <math><mo>⇒</mo><mi>H</mi><mo>=</mo><mfrac><mrow><mn>4</mn><mi>P</mi><mo>⋅</mo><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow></msup></mrow><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>⋅</mo><mi>β</mi></mrow></mfrac></math> 
 <math><mo>⇒</mo><mi>H</mi><mo>=</mo><mn>4</mn><mi>P</mi><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>T</mi><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><msubsup><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow><mrow><mn>4</mn></mrow></msubsup><mo>⋅</mo><msup><mrow><mi>B</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfrac></math> 
Now using equation  <math><mo>(</mo><mn>2</mn><mo>)</mo></math> 
 <math><mi>T</mi><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>=</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>β</mi><mo>⋅</mo><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow></msup></math> 
 <math><mo>⇒</mo><msup><mrow><mi>t</mi></mrow><mrow><mrow><mrow><mn>3</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow></msup><mo>=</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>T</mi><mo>-</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><msub><mrow><mi>T</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>β</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></math>

</details>

---

### Q3. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `1`

<p>Two conducting cylinders of equal length but different radii are connected in series between two heat baths kept at temperatures <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><mn>300</mn><mi> </mi><mi mathvariant="normal">K</mi><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><mn>100</mn><mi> </mi><mi mathvariant="normal">K</mi></math> as shown in the figure. The radius of the bigger cylinder is twice that of the smaller one and the thermal conductivities of the materials of the smaller and the larger cylinders are <math><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></math>, respectively. If the temperature at the junction of the two cylinders in the steady state is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mi mathvariant="normal"> </mi><mi mathvariant="normal">K</mi></math>, then <math><mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>/</mo><mrow><msub><mrow><mi>K</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mrow></math> is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jjtbutazbyombqzfxreixlkjvxhyiqfrepxpuwmhvaylkrxeai.jpeg"/></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/yrmxkywwgiczwjeikqyzapddxpxfjhmceybdwkcqrlvulnprdf.jpeg"/>
We have in steady state, 
<math><mfenced separators="|"><mrow><mfrac><mrow><mn>200</mn><mo>-</mo><mn>300</mn></mrow><mrow><mfrac><mrow><mi>L</mi></mrow><mrow><msub><mrow><mi>k</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>200</mn><mo>-</mo><mn>100</mn></mrow><mrow><mfrac><mrow><mi>L</mi></mrow><mrow><msub><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msub><mi>π</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>0</mn></math>
<math><mo>⇒</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>k</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>π</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>×</mo><mn>100</mn></mrow><mrow><mi>L</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>100</mn><msub><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msub><mi>π</mi><mo>×</mo><mn>4</mn><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mi>L</mi></mrow></mfrac></math>
<math><mo>⇒</mo><mi> </mi><mfrac><mrow><msub><mrow><mi>k</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>4</mn></math>

</details>

---

### Q4. JEE Advanced 2013 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

The figure below shows the variation of specific heat capacity (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math>) of a solid as a function of temperature (<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math>). The temperature is increased continuously from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> at a constant rate. Ignoring any volume change, the following statement (s) is (are) correct to a reasonable approximation.
<img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM0012624_Quest_1.jpg" style="width: 272px; height: 212px;" />

**Options:**

- **(A)** The rate at which heat is absorbed in the range <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> varies linearly with temperature T.
- **(B)** Heat absorbed in increasing the temperature from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> is less than the heat required for increasing the temperature from<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>-</mo><mn>500</mn><mi mathvariant="normal">K</mi></math>.
- **(C)** There is no change in the rate of heat absorption in the range <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>-</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>.
- **(D)** The rate of heat absorption increases in the range <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>-</mo><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) The rate of heat absorption increases in the range <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>-</mo><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>.**

**Detailed Solution:**

<math> <mrow> <mtext>q&#160;</mtext> <mo>=</mo> <mtext>&#160;mCT</mtext> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mtext>dq</mtext> </mrow> <mrow> <mtext>dt</mtext> </mrow> </mfrac> <mo>=</mo> <mtext>mc</mtext> <mfrac> <mrow> <mtext>dT</mtext> </mrow> <mrow> <mtext>dt</mtext> </mrow> </mfrac> </mrow> </math>
R = rate of absorption of heat <math> <mrow> <mo>=</mo> <mfrac> <mrow> <mtext>dq</mtext> </mrow> <mrow> <mtext>dt</mtext> </mrow> </mfrac> <mo>&#8733;</mo> <mtext>C</mtext> </mrow> </math>
(i) in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>
The graph between (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>) appears to be a straight line upto a reasonable approximation.
(ii) <math> <mrow> <mo>&#916;</mo> <mtext>q</mtext> <mo>=</mo> <mtext>mC</mtext> <mo>&#916;</mo> <mtext>T</mtext> </mrow> </math> as C  is more in (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>-</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>) then (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>100</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>) so heat is increasing.
(iii) C remains constant so there no change in R  from (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>-</mo><mn>500</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>)
(iv) C is increases so R is increases in range (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>-</mo><mn>300</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math>)

</details>

---

### Q5. JEE Advanced 2013 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Two rectangular blocks, having identical dimensions, can be arranged either in configuration <math> <mrow> <mtext>I</mtext> </mrow> </math> or in configuration <math> <mrow> <mtext>I</mtext><mtext>I</mtext> </mrow> </math> as shown in the figure. One of the blocks has thermal conductivity <math> <mrow> <mtext>K</mtext> </mrow> </math> and the other <math> <mrow> <mtext>2 K</mtext> </mrow> </math>. The temperature difference between the ends along the x-axis is the same in both the configurations. It takes <math> <mrow> <mtext>9 s</mtext> </mrow> </math> to transport a certain amount of heat from the hot end to cold end in the configuration <math> <mrow> <mtext>I</mtext> </mrow> </math>. The time to transport the same amount of heat in the configuration <math> <mrow> <mtext>II</mtext> </mrow> </math> is
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/EM00012544_JEE_ADVANCED_2013.jpg"/></p>

**Options:**

- **(A)** <math> <mrow> <mtext>2.0 s</mtext> </mrow> </math>
- **(B)** <math> <mrow> <mtext>3.0 s</mtext> </mrow> </math>
- **(C)** <math> <mrow> <mtext>4.5 s</mtext> </mrow> </math>
- **(D)** <math> <mrow> <mtext>6.0 s</mtext> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mtext>2.0 s</mtext> </mrow> </math>**

**Detailed Solution:**

<p>In the first combination, the 2 blocks are having thermal conductivity <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>K</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>K</mi></math> respectively are in series combination.</p><p>Therefore the Keq will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>K</mi><mo>&#160;</mo></mrow></mfrac><mo>&#160;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>K</mi></mrow></mfrac></math></p><p>and the Keq in case of parallel combination is 3K</p><p><math> <mrow> <mtext>Heat transferred</mtext> <mo>=</mo> <mtext>Rate</mtext> <mo>&#215;</mo> <mtext>time. &#8203;</mtext></mrow></math>
<math> <mrow> <mo>&#8756;&#160;&#160;&#160;</mo> <msub> <mtext>Rate</mtext> <mn>1</mn> </msub> <mo>&#215;</mo> <msub> <mtext>time</mtext> <mn>1</mn> </msub> <mo>=</mo> <msub> <mtext>Rate</mtext> <mn>2</mn> </msub> <mo>&#215;</mo> <msub> <mtext>time</mtext> <mn>2</mn> </msub> <mn>.</mn> </mrow> </math>
<math> <mrow> <mfrac> <mrow> <mo>&#916;</mo> <mtext>T</mtext> <mo>&#215;</mo> <mn>9</mn> </mrow> <mrow> <mfrac> <mrow> <mtext>L</mtext> </mrow> <mrow> <mtext>KA</mtext> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mtext>L</mtext> </mrow> <mrow> <mn>2</mn> <mtext>KA</mtext> </mrow> </mfrac> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mtext>&#916;</mtext> <mtext>T</mtext> <mo>&#215;</mo> <mtext>t</mtext> </mrow> <mrow> <mfrac> <mrow> <mn>L</mn> </mrow> <mrow> <mtext>3KA</mtext> </mrow> </mfrac> </mrow> </mfrac> </mrow> </math>
<math> <mrow> <mo>&#8658;&#160;&#160;</mo> <mtext>t</mtext> <mo>=</mo> <mn>2</mn> </mrow> </math></p>

</details>

---

### Q6. JEE Advanced 2011 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `3`

A composite block is made of slabs $A, B, C, D$ and $E$ of different thermal conductivities (given in terms of a constant, $K$ ) and sizes (given in terms of length, $L$ ) as shown in the figure. All slabs are of same width. Heat $Q$ flows only from left to right through the blocks. Then, in steady state
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/E0zfPXPVD6anEcAXH-PQnBX7KAEIvnco_WbswydRJsM.original.fullsize.png">

**Options:**

- **(A)** heat flow through $A$ and $E$ slabs are same
- **(B)** heat flow through slab $E$ is maximum
- **(C)** temperature difference across slab $E$ is smallest
- **(D)** heat flow through $C=$ heat flow through $B$ + heat flow through $D$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) heat flow through $C=$ heat flow through $B$ + heat flow through $D$**

**Detailed Solution:**

Thermal resistance
$$
\begin{aligned}
& R=\frac{l}{K A} \\
& \therefore \quad R_A=\frac{L}{(2 K)(4 L w)}=\frac{1}{8 K w} \\
& \text { (Here, } w=\text { width) } \\
& R_B=\frac{4 L}{3 K(L w)}=\frac{4}{3 K w} \\
& R_C=\frac{4 L}{(4 K)(2 L w)}=\frac{1}{2 K w} \\
& R_D=\frac{4 L}{(5 K)(L w)}=\frac{4}{5 K w} \\
& R_E=\frac{L}{(6 K)(L w)}=\frac{1}{6 K w} \\
& R_A: R_B: R_C: R_D: R_E \\
&=15: 160: 60: 96: 12
\end{aligned}
$$
So, let us write, $R_A=15 R, R_B=160 R$ etc and draw a simple electrical circuit as shown in figure.


<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/AGHLRh_Fhiti6oMHUfQ1FIukEOkNLjb8FmuxSaIUu0A.original.fullsize.png">



$H=$ Heat current $=$ Rate of heat flow.
$$
H_A=H_E=H
$$
[let]
$\therefore$ Option (a) is correct.
In parallel, current distributes in inverse ratio of resistance.
$$
\begin{aligned}
& \therefore H_B: H_C: H_D=\frac{1}{R_B}: \frac{1}{R_C}: \frac{1}{R_D} \\
& =\frac{1}{160}: \frac{1}{60}: \frac{1}{96} \\
& =9: 24: 15 \\
& \therefore \quad H_B=\left(\frac{9}{9+24+15}\right) H=\frac{3}{16} H \\
& H_C=\left(\frac{24}{9+24+15}\right) H=\frac{1}{2} H \\
& \text { and } \quad H_D=\left(\frac{15}{9+24+15}\right) H=\frac{5}{16} H \\
&
\end{aligned}
$$

$$
H_C=H_B+H_D
$$
$\therefore$ Option (d) is correct.
Temperature difference (let us call it $T$ )
$=($ Heat current $) \times($ Thermal resistance $)$
$T_A=H_A R_A=(H)(15 R)=15 \mathrm{HR}$
$T_B=H_B R_B=\left(\frac{3}{16} H\right)(160 R)=30 H R$
$T_C=H_C R_C=\left(\frac{1}{2} H\right)(60 R)=30 H R$
$T_D=H_D R_D=\left(\frac{5}{16} H\right)(96 R)=30 H R$
$T_E=H_E R_E=(H)(12 R)=12 \mathrm{HR}$
Here, $T_E$ is minimum. Therefore, option
(c) is also correct.
$\therefore$ Correct options are (a), (c) and (d).
Analysis of Question
(i) From calculation point of view, question is difficult otherwise question is simple.
(ii) In heat transfer, questions are mainly asked from conduction and radiation topic.

</details>

---

### Q7. JEE Advanced 2009 (Paper 2)

*Type:* `numerical` | *Level:* `2`

A metal rod $A B$ of length $10 x$ has its one end $A$ in ice at $0^{\circ} \mathrm{C}$ and the other end $B$ in water at $100^{\circ} \mathrm{C}$. If a point $P$ on the rod is maintained at $400^{\circ} \mathrm{C}$, then it is found that equal amounts of water and ice evaporate and melt per unit time. The latent heat of evaporation of water is $540 \mathrm{calg}^{-1}$ and latent heat of melting of ice is $80 \mathrm{calg}^{-1}$. If the point $P$ is at a distance of $\lambda x$ from the ice end $A$, find the value of $\lambda$. [Neglect any heat loss to the surrounding.]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/YfSQoXhjZNvHl8wU_-OPaLyrnErrKwulkUaBdtVyaCo.original.fullsize.png">


Heat will flow both sides from point $P$.
$$
\begin{aligned}
L_1 \frac{d m_1}{d t} & =\left(\frac{\text { Temperature difference }}{\text { Thermal resistance }}\right)_1 \\
& =\frac{400}{(\lambda x) / k A} \\
L_1 \frac{d m_2}{d t} & =\frac{400-100}{(100-\lambda) x / k A}
\end{aligned}
$$
In about two equations,
$$
\begin{aligned}
& \frac{d m_1}{d t}=\frac{d m_2}{d t} \quad \text { (given) } \\
& L_1=80 \mathrm{calg}^{-1} \text { and } L_2=540 \mathrm{calg}^{-1}
\end{aligned}
$$
Solving these two equations we get $\lambda=9$.

</details>

---

