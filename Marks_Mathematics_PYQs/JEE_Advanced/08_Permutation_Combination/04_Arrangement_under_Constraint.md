# JEE Advanced Mathematics - Permutation Combination

## Topic 4: Arrangement under Constraint

**Total Questions:** 15

---

### Q1. JEE Advanced 2024 (Paper 1)

*Type:* `numerical` | *Level:* `3`

A group of 9 students, $\mathrm{s}_1, \mathrm{~s}_2, \ldots \ldots, \mathrm{s}_9$, is to be divided to from three teams $\mathrm{X}, \mathrm{Y}$, and $\mathrm{Z}$ of sizes 2,3 , and 4 , respectively. Suppose that $s_1$ cannot be selected for the team $\mathrm{X}$, and $\mathrm{s}_2$ cannot be selected for the team Y. Then the number of ways to from such teams, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **665**

**Detailed Solution:**

$\begin{array}{ccc}\mathrm{x} & \mathrm{y} & \mathrm{z} \\ 2 & 3 & 4 \end{array}$
C-i) when $x$ does not contain $\mathrm{S}_1$, but contains $\mathrm{S}_2$
\(\underset{\text{(for }x)}{{ }^7 C_1} \times \underset{\text{(for }y,z)}{\frac{7!}{3!4!}}=245\)
C-ii) When $\mathrm{x}$ does not contain $\mathrm{S}_1, \mathrm{~S}_2$ and $\mathrm{y}$ does not contain $\mathrm{S}_2$ i.e. \(\underset{\text{(for }x)}{{ }^{7} \mathrm{C}_2} \times \underset{\text{(for }y,z)}{\frac{6!}{3!3!}}=420\)
so total No. of ways $665$

</details>

---

### Q2. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the set of all five digit numbers formed using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>0</mn></math>. For example, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22240</mn></math> is in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> while <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>02244</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44422</mn></math> are not in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>. Suppose that each element of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> has an equal chance of being chosen. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> be the conditional probability that an element chosen at random is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> given that it is a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>38</mn><mo>&#160;</mo><mi>p</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **31**

**Detailed Solution:**

<blockquote><p>First we will find the sample space in which the number of five-digit numbers are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>,</p><p>So, fixing zero at the last place we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo><menclose notation="bottom"><mn>0</mn></menclose></mrow><mo>&#9183;</mo></munder></math></p><p>Now in first four place following number can take place,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2224</mn><mo>&#160;</mo><mo>&#8594;</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2244</mn><mo>&#8594;</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>6</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2221</mn><mo>&#8594;</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>4</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2241</mn><mo>&#8594;</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>12</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2441</mn><mo>&#8594;</mo><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>12</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>So, total sample space will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>12</mn><mo>=</mo><mn>38</mn></math> </p><p>Now finding the number of favourable outcomes,</p><p>So, Number of five-digit numbers divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> but <u>&#39;not&#39;</u> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></p><p>Now fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> in last two places, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>-</mo><mo>-</mo><mo>-</mo><menclose notation="bottom"><mn>1</mn></menclose><mo>&#160;</mo><menclose notation="bottom"><mn>0</mn></menclose></mrow><mo>&#9183;</mo></munder></math></p><p>So, the first three places can be occupied by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>222</mn><mo>&#160;</mo><mo>&#8594;</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>224</mn><mo>&#160;</mo><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>244</mn><mo>&#160;</mo><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>So, total number of numbers which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> but not <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>7</mn></math></p><p>So, favourable number of five-digit numbers that are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> <u>and</u> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>=</mo><mn>38</mn><mo>-</mo><mn>7</mn><mo>=</mo><mn>31</mn></math></p><p>Hence, probability is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>31</mn><mn>38</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>38</mn><mo>&#160;</mo><mi>p</mi><mo>=</mo><mn>31</mn></math></p></blockquote>

</details>

---

### Q3. JEE Advanced 2022 (Paper 1)

*Type:* `numerical` | *Level:* `3`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit integers in the closed interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mn>2022</mn><mo>,</mo><mn>4482</mn></mrow></mfenced></math> formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **569**

**Detailed Solution:**

<blockquote><p>Given the number to be formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math> </p><p>Now assuming counting integers starting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>Case-I: if zero on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> place</p><p>(i) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi></math>, now here at unit place <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> number can take place except zero {as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2020</mn><mo>&#60;</mo><mn>2022</mn></math>}, so <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> possible way.</p><p>(ii) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mn>0</mn><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi></math>, now here at ten&#39;s place <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> number <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math> can take place  and at unit place all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> number can take place so total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>24</mn></math> possible way</p><p>Case-II: If non-zero number on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> place</p><p>i.e <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><munder><mrow><mo>&#160;</mo><munder><mrow><mo>&#160;</mo><mi>_</mi></mrow><mo>&#9183;</mo></munder></mrow><mn>5</mn></munder><mo>&#160;</mo><mo>&#160;</mo><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder><munder><mrow><mo>&#160;</mo><munder><mrow><mo>&#160;</mo><mi>_</mi></mrow><mo>&#9183;</mo></munder></mrow><mn>6</mn></munder></math>, here at hundredth place <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> possibility will be there and at unit and ten&#39;s place <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>6</mn></math> possibility will be there, so in total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>180</mn></math> possible cases,</p><p>Case -III when counting integers starting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd></mtr></mtable></math> here total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>216</mn></math> possible cases</p><p>Case -IV when counting integers starting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p><p>(i) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> place</p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>4</mn></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>3</mn></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd></mtr></mtable></math> here total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>108</mn></math> possible cases</p><p>(ii) If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> on <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> place</p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>3</mn></mtd><mtd><mn>4</mn></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd><mtd><munder><munder><mi>_</mi><mo>&#9183;</mo></munder><mn>6</mn></munder></mtd></mtr></mtable></math> here total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>36</mn></math> possible cases</p><p>So, total possible cases will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>180</mn><mo>+</mo><mn>216</mn><mo>+</mo><mn>108</mn><mo>+</mo><mn>36</mn><mo>=</mo><mn>569</mn></math> numbers</p></blockquote>

</details>

---

### Q4. JEE Advanced 2020 (Paper 2)

*Type:* `numerical` | *Level:* `1`

An engineer is required to visit a factory for exactly four days during the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> days of every month and it is mandatory that no two visits take place on consecutive days. Then the number of all possible ways in which such visits to the factory can be made by the engineer during <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mn>15</mn></math> June <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2021</mn></math> is_____

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **495**

**Detailed Solution:**

<p>Selection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> non-consecutive days out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> days is same as first remove <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> objects from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> objects, so remainging objects are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> having <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> gaps in which these <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> objects can be placed again.</p><p>So, total number of ways is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>12</mn><mo>.</mo><mn>11</mn><mo>.</mo><mn>10</mn><mo>.</mo><mn>9</mn></mrow><mrow><mn>4</mn><mo>.</mo><mn>3</mn><mo>.</mo><mn>2</mn><mo>.</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>495</mn></math>.</p>

</details>

---

### Q5. JEE Advanced 2019 (Paper 2)

*Type:* `numerical` | *Level:* `1`

Five persons <math><mi mathvariant="normal">A</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">B</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">C</mi><mo>,</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">D</mi></math> and <math><mi mathvariant="normal">E</mi></math> are seated in a circular arrangement. If each of them is given a hat of one of the three colours red, blue and green, then the number of ways of distributing the hats such that the persons seated in adjacent seats get different coloured hats is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<p>Given that no two persons sitting adjacent, have the hat of same colour, so hats of all colour must be used, also <math><mn>3</mn></math> hats of same colour cannot be used as at least two hats of same colour will become consecutive, so the only combination will be <math><mn>2</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>1</mn><mo>.</mo></math>
Three cases are possible
<math> <mrow> <mfenced close="}" open=""> <mrow> <mtable equalcolumns="true" equalrows="true"> <mtr> <mtd> <mrow> <mi>a</mi><mo stretchy="false">)</mo><mo> </mo><mn>2</mn><mi>R</mi><mo>,</mo><mo> </mo><mn>2</mn><mi>B</mi><mo>,</mo><mo> </mo><mn>1</mn><mi>G</mi></mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mi>b</mi><mo stretchy="false">)</mo><mo> </mo><mn>2</mn><mi>B</mi><mo>,</mo><mo> </mo><mn>2</mn><mi>G</mi><mo>,</mo><mo> </mo><mn>1</mn><mi>R</mi></mrow> </mtd> </mtr> <mtr> <mtd> <mrow> <mi>c</mi><mo stretchy="false">)</mo><mo> </mo><mn>2</mn><mi>R</mi><mo>,</mo><mo> </mo><mn>2</mn><mi>G</mi><mo>,</mo><mo> </mo><mn>1</mn><mi>B</mi></mrow> </mtd> </mtr> </mtable></mrow> </mfenced><mo>−</mo><mn>3</mn></mrow> </math> way
Select are person for single colour hat <math><mo>=</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi> </mi></mrow><mrow><mn>5</mn></mrow></mmultiscripts></math> (let say green)
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/589495s.png"/>
Now remaining <math><mn>4</mn></math> hats can be distributed alternatively in two ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>B</mi><mi>R</mi><mi>B</mi><mi>R</mi><mo> </mo><mi>or</mi><mo> </mo><mi>R</mi><mi>B</mi><mi>R</mi><mi>B</mi></mrow></mfenced></math>
Total number of ways <math><mo>=</mo><mn>3</mn><mo>×</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi> </mi></mrow><mrow><mn>5</mn></mrow></mmultiscripts><mo>×</mo><mn>2</mn></math>
<math><mo>=</mo><mn>30</mn></math></p>

</details>

---

### Q6. JEE Advanced 2018 (Paper 1)

*Type:* `numerical` | *Level:* `1`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers which are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>, with digits from the set <math><mo>{</mo><mn>1,2</mn><mo>,</mo><mn>3,4</mn><mo>,</mo><mn>5</mn><mo>}</mo></math> and the repetition of digits is allowed, is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **625**

**Detailed Solution:**

Option for last two digits are <math><mfenced separators="|"><mrow><mn>12</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>24</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>32</mn></mrow></mfenced><mo>,</mo><mfenced separators="|"><mrow><mn>44</mn></mrow></mfenced><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">e</mi><mi> </mi><mfenced separators="|"><mrow><mn>52</mn></mrow></mfenced></math> .
<math><mo>∴</mo><mi> </mi></math> Total number of 5 digit numbers
<math><mo>=</mo><mi> </mi><mi> </mi><mn>5</mn><mo>×</mo><mn>5</mn><mo>×</mo><mn>5</mn><mo>×</mo><mn>5</mn><mo>=</mo><mn>625</mn></math>
<math><mi> </mi></math>

</details>

---

### Q7. JEE Advanced 2017 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Words of length<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> are formed using the letters A, B, C, D, E, F, G, H, I, J. Let <math><mi>x</mi></math> be the number of such words where no letter is repeated; and let <math><mi>y</mi></math> be the number of such words where exactly one letter is repeated twice and no other letter is repeated. The, <math><mfrac><mrow><mi>y</mi></mrow><mrow><mn>9</mn><mi>x</mi></mrow></mfrac><mo>=</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo></math>number of ways in which<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> letter word can be formed using the given ten distinct letters.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>10</mn><mo>!</mo></math></p><p><math><mi>y</mi><mo>=</mo></math> number of ways, in which<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> letter words can be formed, in which exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> letter is repeated twice and remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> letters are distinct.</p><p><math><mi>y</mi><mo>=</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>8</mn></mrow></msub><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></math><math> <mrow> <mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mfrac> <mrow> <mn>10</mn><mo>!</mo> </mrow> <mrow> <mn>2</mn><mo>!</mo> </mrow> </mfrac> <mo>=</mo><mn>5</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>10</mn><mo>!</mo> </mrow> </math></p><p><math><mfrac><mrow><mi>y</mi></mrow><mrow><mn>9</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>10</mn><mo>!</mo></mrow><mrow><mn>9</mn><mo>&#215;</mo><mn>10</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q8. JEE Advanced 2015 (Paper 1)

*Type:* `numerical` | *Level:* `2`

Let n be the number of ways in which 5 boys and 5 girls can stand in a queue in such a way that all the girls stand consecutively in the queue. Let m be the number of ways in which 5 boys and 5 girls can stand in queue in such a way that exactly four girls stand consecutively in the queue. Then the value of <math><mfrac><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></mfrac></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<math><mi mathvariant="normal">n</mi><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><munder underaccent="false"><mrow><mn>6</mn></mrow><mo>_</mo></munder><mo>.</mo></mrow></mfenced><munder underaccent="false"><mrow><mn>5</mn></mrow><mo>_</mo></munder></math> 
 <math><mi mathvariant="normal">m</mi><mo>=</mo><msup><mrow/><mrow><mn>5</mn></mrow></msup><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>×</mo><msup><mrow/><mrow><mn>6</mn></mrow></msup><msub><mrow><mi mathvariant="normal">P</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>×</mo><mn>4</mn><mo>!</mo><mo>×</mo><mn>5</mn><mo>!</mo></math> 
 <math><mfrac><mrow><mi mathvariant="normal">m</mi></mrow><mrow><mi mathvariant="normal">n</mi></mrow></mfrac><mo>=</mo><mn>5</mn></math>

</details>

---

### Q9. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

Three boys and two girls stand in a queue. The probability that the number of boys ahead of every girl is atleast one more than the number of girls ahead of her is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>**

**Detailed Solution:**

Either a girl start the sequence or will be at second position and will not acquire the last position as well.
Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced separators="|"><mrow><msup><mi>&#160;</mi><mn>3</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>&#215;</mo><mn>2</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>+</mo><msup><mi>&#160;</mi><mn>2</mn></msup><mi>&#160;</mi><msub><mi>C</mi><mn>1</mn></msub><mo>&#215;</mo><mn>2</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn><mo>!</mo></mrow></mfenced><mrow><mi>&#160;</mi><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

</details>

---

### Q10. JEE Advanced 2014 (Paper 1)

*Type:* `numerical` | *Level:* `3`

Let <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>&#60;</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>5</mn></mrow></msub></math> be positive integers such that <math><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>=</mo><mn>20</mn></math> . Then the number of such distinct arrangements <math><mfenced separators="|"><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>n</mi></mrow><mrow><mn>5</mn></mrow></msub></mrow></mfenced></math> is _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

When  <math><msub><mrow><mi>n</mi></mrow><mrow><mn>5</mn></mrow></msub></math>  takes value from 10 to 6 the carry forward moves from 0 to 4 which can be arranged in   <math><msup><mrow/><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><mo>+</mo><mfrac><mrow><msup><mrow/><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow/><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mrow/><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>4</mn></mrow></msub></mrow><mrow><mn>1</mn></mrow></mfrac><mo>=</mo><mn>7</mn></math> 
Alternate solution
Possible solutions are
1, 2, 3, 4, 10
1, 2, 3, 5, 9
1, 2, 3, 6, 8
1, 2, 4, 5, 8
1, 2, 4, 6, 7
1, 3, 4, 5, 7
2, 3, 4, 5, 6
Hence 7 solutions are there.

</details>

---

### Q11. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $a_{n}$ denote the number of all $n$-digit positive integers formed by the digits 0,1 or both such that no consecutive digits in them are 0 . Let $b_{n}=$ the number of such $n$-digit integers ending with digit 1 and $c_{n}=$ the number of such $n$-digit integers ending with digit 0 .

<strong> Question:</strong> Which of the following is correct?

**Options:**

- **(A)** $a_{17}=a_{16}+a_{15}$
- **(B)** $c_{17} \neq c_{16}+c_{15}$
- **(C)** $b_{17} \neq b_{16}+c_{16}$
- **(D)** $a_{17}=c_{17}+b_{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a_{17}=a_{16}+a_{15}$**

**Detailed Solution:**

By recurring formula, $a_{17}=a_{16}+a_{15}$ is correct

Also $c_{17} \neq c_{16}+c_{15}$

$\Rightarrow a_{15} \neq a_{14}+a_{13}\left(\because c_{n}=a_{n-2}\right)$

$\therefore$ Incorrect

Similarly, other parts are also incorrect.

</details>

---

### Q12. JEE Advanced 2012 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $a_{n}$ denote the number of all $n$-digit positive integers formed by the digits 0,1 or both such that no consecutive digits in them are 0 . Let $b_{n}=$ the number of such $n$-digit integers ending with digit 1 and $c_{n}=$ the number of such $n$-digit integers ending with digit 0 .

<strong> Question:</strong> The value of $b_{6}$ is

**Options:**

- **(A)** 7
- **(B)** 8
- **(C)** 9
- **(D)** 11

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 8**

**Detailed Solution:**

$\because a_{n}=$ number of all $n$ digit +ve integers formed by the digits 0,1 or both such that no consecutive digits in them are 0 .

and $b_{n}=$ number of such $n$ digit integers ending with 1 $c_{n}=$ number of such $n$ digit integers ending with 0

Clearly, $a_{n}=b_{n}+c_{n}\left(\because a_{n}\right.$ can end with 0 or 1)

Also $b_{n}=a_{n-1}$ and $c_{n}=a_{n-2}[\because$ if last digit is 0 , second last has to be 1]

$\therefore$ We get $a_{n}=a_{n-1}+a_{n-2}, n \geq 3$

Also $a_{1}=1, a_{2}=2$,

Now by this recurring formula, we get

$\begin{aligned} a_{3} &=a_{2}+a_{1}=3 \\ a_{4} &=a_{3}+a_{2}=3+2=5 \\ a_{5} &=a_{4}+a_{3}=5+3=8 \\ \text { Also } b_{6} &=a_{5}=8 \end{aligned}$

</details>

---

### Q13. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `2`

<strong>Paragraph:</strong>
Let $A$ be the set of all $3 \times 3$ symmetric matrices all of whose entries are either 0 or 1 . Five of these entries are 1 and four of them are 0 .<strong>Question:</strong>
The number of matrices in $A$ is

**Options:**

- **(A)** 12
- **(B)** 6
- **(C)** 9
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

Case $I$ When all three diagonal elements are 1 , then
Number of matrices $={ }^3 C_1=3$
Case II When two diagonal elements are zero and one element is one no, then Number of matrices $={ }^3 C_1 \cdot{ }^3 C_1=9$
$\therefore$ Total matrices $=3+9=12$

</details>

---

### Q14. JEE Advanced 2009 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

The number of seven digit integers, with sum of the digits equal to 10 and formed by using the digits 1,2 and 3 only, is

**Options:**

- **(A)** 55
- **(B)** 66
- **(C)** 77
- **(D)** 88

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 77**

**Detailed Solution:**

There are two possible cases arise:
Case I Five 1's, one 2's, one 3's
$\therefore$ Number of numbers $=\frac{7 !}{5 !}=42$
Case II Four 1's, three 2's
$\therefore$ Number of numbers $=\frac{7 !}{4 ! 3 !}=35$
$\therefore$ Total number of numbers $=42+35=77$

</details>

---

### Q15. JEE Advanced 2008 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider all possible permutations of the letters of the word ENDEANOEL. Match the Statements/Expressions in Column I with the Statements/Expressions in Column II.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/1Oj7xgNtMlSTH_bJ2EXv-IV_L6I5OltoIjA2nwL0Yr0.original.fullsize.png">

**Options:**

- **(A)** (A) r, (B) q, (C) s, (D) p
- **(B)** (A) p, (B) s, (C) q, (D) q
- **(C)** (A) p, (B) r, (C) s, (D) q
- **(D)** (A) r, (B) s, (C) r, (D) p

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) (A) p, (B) s, (C) q, (D) q**

**Detailed Solution:**

(A) If ENDEA is fixed word, then assume this as a single letter.
Total number of letters $=5$ and total number of arrangements $=5$ ! .
(B) If $E$ is at first and last places, then total number of permutations
$$
\frac{7 !}{2 !}=21 \times 5 !
$$
(C) If $\mathrm{D}, \mathrm{L}, \mathrm{N}$ are not in last five positions
$$
\leftarrow \mathrm{D}, \mathrm{L}, \mathrm{N}, \mathrm{N} \rightarrow \leftarrow \text { E, E, E, A, O } \rightarrow
$$
Total number of permutations $=\frac{4 !}{2 !} \times \frac{5 !}{3 !}=2 \times 5$ ! .
(D) Total number of odd positions $=5$
Permutations of AEEEO are $\frac{5 !}{3 !}$
Total number of even positions $=4$
Number of permutations of $\mathrm{N}, \mathrm{N}, \mathrm{D}, \mathrm{L}=\frac{4 !}{2 !}$
Hence, total number of permutations $=\frac{5 !}{3 !} \times \frac{4 !}{2 !}=2 \times 5 !$.

</details>

---

