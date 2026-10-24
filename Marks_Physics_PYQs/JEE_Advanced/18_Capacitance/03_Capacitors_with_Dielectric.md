# JEE Advanced Physics - Capacitance

## Topic 3: Capacitors with Dielectric

**Total Questions:** 5

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

<strong>Passage:</strong> A container of height $2$ m, length $2$ m and breadth $1$ m is made of insulating vertical walls and two large area horizontal metal plates ($M_1$ and $M_2$) which extend far beyond the vertical walls in all directions. The container is partitioned into two equal chambers with a thin insulating vertical wall. The partition wall contains a small hole of cross-sectional area $\sqrt{10}$ cm$^2$ near its bottom edge. Initially the hole is closed and the left chamber of the container is completely filled with a liquid of dielectric constant $\epsilon_r = 15$ and the right chamber is empty ($\epsilon_r = 1$). At time $t = 0$, the hole is opened and the liquid flows from the left chamber to the right chamber. In both the chambers, the space above the liquid has $\epsilon_r = 1$ and is maintained at atmospheric pressure. The schematic of the container at a time $t > 0$ is shown in the figure.
[Given: acceleration due to gravity is $10$ ms$^{-2}$.]
<img style="width: 400px" src="https://cdn.quizrr.in/question-assets/jee_adv/2026/watermarked_images/p2_english__q33_d1.png" />

<strong>Question:</strong> The difference in the capacitance (in F) between the metal plates at $t = 0$ and that at $t = 500$ s is $(8 - n)\epsilon_0$, where $\epsilon_0$ is the permittivity of free space. The value of $n$ is:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1.97**

**Detailed Solution:**

Let $A$ be the area of each chamber. $A = 1 \times 1 = 1 \text{ m}^2$. Distance between plates is $d = 2 \text{ m}$.

At $t = 0$, the left chamber is completely filled with liquid ($\epsilon_r = 15$) and right chamber is empty ($\epsilon_r = 1$).

Initial capacitance $C(0) = C_1 + C_2 = \dfrac{15 \epsilon_0 A}{d} + \dfrac{\epsilon_0 A}{d} = \dfrac{15 \epsilon_0 (1)}{2} + \dfrac{\epsilon_0 (1)}{2} = 8 \epsilon_0$.

Let $y_1$ and $y_2$ be the liquid levels in the left and right chambers at time $t$. By conservation of volume, $y_1 + y_2 = 2 \text{ m}$.

Let $h = y_1 - y_2$. The velocity of efflux from the left chamber is $v = \sqrt{2gh}$.

Rate of flow $Q = -A \dfrac{dy_1}{dt} = a \sqrt{2gh}$, where $a = \sqrt{10} \times 10^{-4} \text{ m}^2$ is the hole area.

Since $y_1 + y_2 = 2$, we have $dy_2 = -dy_1$, so $dh = 2dy_1 \Rightarrow \dfrac{dy_1}{dt} = \dfrac{1}{2} \dfrac{dh}{dt}$.

$-\dfrac{1}{2} \dfrac{dh}{dt} = a \sqrt{2gh} \Rightarrow \dfrac{dh}{\sqrt{h}} = -2a \sqrt{2g} dt$.

Integrating from $t=0$ ($h=2$) to $t=500 \text{ s}$ ($h$):

$\int_{2}^{h} h^{-1/2} dh = -2a \sqrt{2g} \int_{0}^{500} dt$

$2\sqrt{h} - 2\sqrt{2} = -2 (\sqrt{10} \times 10^{-4}) (\sqrt{20}) (500) = -\sqrt{200} \times 10^{-4} \times 1000 = -10\sqrt{2} \times 0.1 = -\sqrt{2}$.

$2\sqrt{h} = \sqrt{2} \Rightarrow \sqrt{h} = \dfrac{1}{\sqrt{2}} \Rightarrow h = 0.5 \text{ m}$.

From $y_1 + y_2 = 2$ and $y_1 - y_2 = 0.5$, we get $y_1 = 1.25 \text{ m}$ and $y_2 = 0.75 \text{ m}$.

At $t=500 \text{ s}$, each chamber acts as two capacitors in series (liquid and air).

$C_{left} = \dfrac{1}{\dfrac{y_1}{15\epsilon_0 A} + \dfrac{2-y_1}{\epsilon_0 A}} = \dfrac{15\epsilon_0}{30 - 14y_1} = \dfrac{15\epsilon_0}{30 - 14(1.25)} = \dfrac{15\epsilon_0}{12.5} = \dfrac{6}{5} \epsilon_0 = 1.2 \epsilon_0$.

$C_{right} = \dfrac{1}{\dfrac{y_2}{15\epsilon_0 A} + \dfrac{2-y_2}{\epsilon_0 A}} = \dfrac{15\epsilon_0}{30 - 14y_2} = \dfrac{15\epsilon_0}{30 - 14(0.75)} = \dfrac{15\epsilon_0}{19.5} = \dfrac{150}{195} \epsilon_0 = \dfrac{10}{13} \epsilon_0$.

$C(500) = C_{left} + C_{right} = \dfrac{6}{5} \epsilon_0 + \dfrac{10}{13} \epsilon_0 = \dfrac{128}{65} \epsilon_0 \approx 1.97 \epsilon_0$.

Difference in capacitance $= C(0) - C(500) = 8\epsilon_0 - \dfrac{128}{65}\epsilon_0 = \left(8 - \dfrac{128}{65}\right)\epsilon_0$.

Comparing this with the given expression $(8 - n)\epsilon_0$, we get $n = \dfrac{128}{65} = 1.97$

</details>

---

### Q2. JEE Advanced 2023 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>A container has a base of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi>cm</mi><mo>&#215;</mo><mn>5</mn><mo>&#160;</mo><mi>cm</mi></math> and height <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi>cm</mi></math>, as shown in the figure. It has two parallel electrically conducting walls each of area <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>&#160;</mo><mi>cm</mi><mo>&#215;</mo><mn>50</mn><mo>&#160;</mo><mi>cm</mi></math>. The remaining walls of the container are thin and non-conducting. The container is being filled with a liquid of dielectric constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> at a uniform rate of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn><mo>&#160;</mo><msup><mi>cm</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup></math>. What is the value of the capacitance of the container after <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> seconds?</p><p>[Given: Permittivity of free space <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#949;</mi><mn>0</mn></msub><mo>=</mo><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8722;</mo><mn>12</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">C</mi><mn>2</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">N</mi><mrow><mo>&#8722;</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><msup><mi mathvariant="normal">m</mi><mrow><mo>&#8722;</mo><mn>2</mn></mrow></msup></math>, the effects of the non-conducting walls on the capacitance are negligible]</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/b1769d59-50df-45c1-a827-c79e1adef763.png" style="width: 300px; height: 284px;" /></p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mo>&#160;</mo><mi>pF</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mo>&#160;</mo><mi>pF</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>81</mn><mo>&#160;</mo><mi>pF</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>135</mn><mo>&#160;</mo><mi>pF</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mo>&#160;</mo><mi>pF</mi></math>**

**Detailed Solution:**

<blockquote><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/8abad4a2-1814-4083-865c-1553ed8fb08e.png" style="width: 250px; height: 294px;" /></p><p>Height of the liquid column <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mtext>volume</mtext><mtext>base&#160;area</mtext></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>h</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>250</mn><mo>&#160;</mo><msup><mi>cm</mi><mn>3</mn></msup><mo>&#160;</mo><msup><mi mathvariant="normal">s</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>10</mn><mo>&#160;</mo><mi mathvariant="normal">s</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><mn>50</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>5</mn><mo>&#160;</mo><mi>cm</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mi>cm</mi></math></p><p>Now capacitance of the upper part can be written as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>A</mi><mn>1</mn></msub><msub><mi>&#949;</mi><mn>0</mn></msub></mrow><mi>d</mi></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mfenced close="]" open="["><mrow><mfenced><mrow><mn>0</mn><mo>.</mo><mn>50</mn><mo>-</mo><mn>0</mn><mo>.</mo><mn>10</mn></mrow></mfenced><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>50</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow></mfenced></mrow><mfenced><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><mn>36</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">F</mi></math></p><p>Capacitance for the lower part can be written as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mi>A</mi><mn>2</mn></msub><msub><mi>&#949;</mi><mn>0</mn></msub></mrow><mi>d</mi></mfrac><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mfenced><mrow><mn>0</mn><mo>.</mo><mn>10</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mn>9</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>12</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>5</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn><mo>.</mo><mn>27</mn><mo>&#215;</mo><msup><mn>10</mn><mrow><mo>&#8211;</mo><mn>10</mn></mrow></msup><mo>&#160;</mo><mi mathvariant="normal">F</mi></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/480c454a-e050-4af7-8174-dcdc0ad4f916.png" style="width: 300px; height: 336px;" /></p><p>Both part of the capacitor can be considered as connected in parallel,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mrow><mi>e</mi><mi>f</mi><mi>f</mi></mrow></msub><mo>=</mo><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>63</mn><mo>&#160;</mo><mi>pF</mi></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2019 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A parallel plate capacitor of capacitance <math><mi mathvariant="normal">C</mi></math> has spacing d between two plates having area <math><mi mathvariant="normal">A</mi><mo>.</mo></math> The region between the plates is filled with <math><mi mathvariant="normal">N</mi></math> dielectric layers, parallel to its plates, each with thickness <math><mi mathvariant="normal">&#948;</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow></mfrac><mo>.</mo></math> The dielectric constant of the <math><msup><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> layer is <math><msub><mrow><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">m</mi></mrow></msub><mo>=</mo><mi mathvariant="normal">K</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mi mathvariant="normal">N</mi></mrow></mfrac></mrow></mfenced><mo>.</mo></math> For a very large <math><mi mathvariant="normal">N</mi><mfenced separators="|"><mrow><mo>&#62;</mo><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><mo>,</mo></math> the capacitance <math><mi mathvariant="normal">C</mi></math> is <math><mi mathvariant="normal">&#945;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi mathvariant="normal">K</mi><msub><mrow><mo>&#8712;</mo></mrow><mrow><mn>0</mn></mrow></msub><mi mathvariant="normal">A</mi></mrow><mrow><mi mathvariant="normal">d</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>.</mo></math> The value of <math><mi mathvariant="normal">&#945;</mi></math> will be____
<math><mo>[</mo><msub><mrow><mo>&#8712;</mo></mrow><mrow><mn>0</mn></mrow></msub></math> is the permittivity of free space]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/jwwygxeqqbmykrfpcajhkvetzcahgnqzyoewhdzovabgxtponi.png"/>

Let <math><msup><mrow><mi>m</mi></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> layer is at a distance <math><mi mathvariant="normal">‘</mi><mi mathvariant="normal">x</mi><mi mathvariant="normal">’</mi></math> from left plate.

Also, let there be a small strip of thickness 'dx' having small capacitance <math><mi>′</mi><mi>′</mi><mi>d</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>C</mi></mrow></mfrac></mrow></mfenced><mi>′</mi><mi>′</mi></math> with medium <math><mi>′</mi><mi>′</mi><msub><mrow><mi>K</mi></mrow><mrow><mi>m</mi></mrow></msub><mi>′</mi><mi>′</mi></math> in between.

<math><mo>⇒</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>m</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>D</mi></mrow><mrow><mi>N</mi></mrow></mfrac></math>

Also, <math><mi>d</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>C</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mi>m</mi></mrow></msub><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><msub><mrow><mi>K</mi></mrow><mrow><mi>m</mi></mrow></msub><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>K</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>m</mi></mrow><mrow><mi>N</mi></mrow></mfrac></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>K</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mi>D</mi></mrow></mfrac></mrow></mfenced></mrow></mfrac></math>

<math><mo>⇒</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>e</mi><mi>q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mo>∫</mo><mi>d</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>C</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mrow><munderover><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mi>D</mi></mrow></munderover><mrow><mfrac><mrow><mi>D</mi><mi>d</mi><mi>x</mi></mrow><mrow><mi>K</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi><mfenced separators="|"><mrow><mi>D</mi><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></mrow></math>

<math><mfrac><mrow><mn>1</mn></mrow><mrow><msub><mrow><mi>C</mi></mrow><mrow><mi>e</mi><mi>q</mi></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>D</mi></mrow><mrow><mi>K</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi></mrow></mfrac><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>2</mn></math>

<math><msub><mrow><mi>C</mi></mrow><mrow><mi>e</mi><mi>q</mi></mrow></msub><mo>=</mo><mfrac><mrow><mi>K</mi><msub><mrow><mi>ε</mi></mrow><mrow><mn>0</mn></mrow></msub><mi>A</mi></mrow><mrow><mi>D</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">n</mi><mn>2</mn></mrow></mfrac><mo>⋅</mo></math> Therefore <math><mi>α</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q4. JEE Advanced 2015 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `3`

<p>A parallel plate capacitor having plates of area <math><mi mathvariant="normal">S</mi></math> and plate separation <math><mi mathvariant="normal">d</mi></math> , has capacitance <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> in air. When two dielectrics of different relative permittivities ( <math><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mi mathvariant="normal"> </mi></math> and <math><msub><mrow><mi mathvariant="normal">ε</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>4</mn></math> ) are introduced between the two plates as shown in the figure, the capacitance becomes <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub></math> . The ratio <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></math> is

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image10-00858567-f376-486b-be8c-e64f8146c3f4.jpg"/></p>

**Options:**

- **(A)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mfrac><mrow><mn>5</mn><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>=</mo><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
In new setup we have 3 different setups
i.  <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><msup><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mi mathvariant="normal">′</mi></mrow></msup><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mn>2</mn><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
ii.  <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>2</mn></mrow></msub></math> 
 <math><msup><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mi mathvariant="normal">′</mi><mi mathvariant="normal">′</mi></mrow></msup><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>2</mn></mrow></msub><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mfrac><mrow><mi mathvariant="normal">d</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfrac><mo>=</mo><mn>4</mn><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
iii.  <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>,</mo><mi mathvariant="normal"> </mi><mi mathvariant="normal">d</mi><mo>,</mo><mi mathvariant="normal"> </mi><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><msup><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mi mathvariant="normal">′</mi><mi mathvariant="normal">′</mi><mi mathvariant="normal">′</mi></mrow></msup><mo>=</mo><mfrac><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>1</mn></mrow></msub><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>=</mo><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image11-8247136b-678d-49c1-81a5-296746d0e4f3.jpg"/> 
 <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac></mrow></mfenced></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>14</mn></mrow><mrow><mn>6</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> 
 <math><mo>∴</mo><mfrac><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q5. JEE Advanced 2014 (Paper 1)

*Type:* `multipleCorrect` | *Level:* `2`

<p>A parallel plate capacitor has a dielectric slab of dielectric constant K between its plates that covers 1/3 of the area of its plates, as shown in the figure. The total capacitance of the capacitor is C while that of the portion with dielectric in between is <math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></math> . When the capacitor is charged, the plate area covered by the dielectric gets charge <math><msub><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and the rest of the area gets charge <math><msub><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn></mrow></msub></math> . The electric field in the dielectric is <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and that in the other portion is <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub></math> . Choose the correct option/options, ignoring edge effects.

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/image2-95418e85-0042-4c6f-8564-a2a5d886ae5b.png"/></p>

**Options:**

- **(A)** <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi mathvariant="normal">K</mi></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><msub><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msub><mrow><mi mathvariant="normal">Q</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mi mathvariant="normal">K</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mi mathvariant="normal">C</mi></mrow><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">K</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mi mathvariant="normal">C</mi></mrow><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mi mathvariant="normal">K</mi></mrow><mrow><mi mathvariant="normal">K</mi></mrow></mfrac></math>**

**Detailed Solution:**

As <math><mi mathvariant="normal">E</mi><mo>=</mo><mfrac><mrow><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac></math>
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac></math>
<math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac></math>
(As both parts have some P.D.) upper capacitor have capacitance
<math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi mathvariant="normal">K</mi><msub><mrow><mi mathvariant="normal">&epsilon;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi mathvariant="normal">A</mi><mo>/</mo><mi mathvariant="normal">d</mi><mi mathvariant="normal"> </mi></math>
Lower capacitor
<math><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mrow><mi mathvariant="normal">&epsilon;</mi></mrow><mrow><mn>0</mn></mrow></msub><mi mathvariant="normal">A</mi><mo>/</mo><mi mathvariant="normal">d</mi></math>
<math><mo>&there4;</mo></math> equivalent capacitance
<math><mi mathvariant="normal">C</mi><mo>=</mo><mfenced separators="|"><mrow><mi mathvariant="normal">k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><msub><mrow><mi mathvariant="normal">ϵ</mi></mrow><mrow><mn>0</mn></mrow></msub><mi mathvariant="normal">A</mi><mo>/</mo><mi mathvariant="normal">d</mi></math>
<math><mo>&there4;</mo><mfrac><mrow><mi mathvariant="normal">C</mi></mrow><mrow><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">k</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi mathvariant="normal">k</mi></mrow></mfrac></math>
And <math><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>1</mn></mrow></msub><mi mathvariant="normal"> </mi><mo>:</mo><msub><mrow><mi mathvariant="normal">E</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>:</mo><mfrac><mrow><mi mathvariant="normal">v</mi></mrow><mrow><mi mathvariant="normal">d</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math>

</details>

---

