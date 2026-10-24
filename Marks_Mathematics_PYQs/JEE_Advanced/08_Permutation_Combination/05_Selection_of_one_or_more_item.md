# JEE Advanced Mathematics - Permutation Combination

## Topic 5: Selection of one or more item

**Total Questions:** 3

---

### Q1. JEE Advanced 2023 (Paper 2)

*Type:* `numerical` | *Level:* `2`

<p>Consider the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#215;</mo><mn>6</mn></math> square in the figure. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>A</mi><mn>49</mn></msub></math> be the points of intersections (dots in the picture) in some order. We say that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>j</mi></msub></math> are friends if they are adjacent along a row or along a column. Assume that each point <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub></math> has an equal chance of being chosen.</p>

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/d33e0b30-a00c-486d-8560-c6e3e5f7757d.png" style="width: 200px; height: 197px;" /></p>

<p>(There are two questions based on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>PARAGRAPH</mi><mo>&#160;</mo><mo>&#34;</mo><mi>II</mi><mo>&#34;</mo></math>, the question given below is one of them)</p>

Two distinct points are chosen randomly out of the points <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>A</mi><mn>49</mn></msub></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> be the probability that they are friends. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mi>p</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0.5**

**Detailed Solution:**

<blockquote><p>Given,</p><p>We have to choose two distinct points randomly,</p><p>Now number of ways of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> adjacent dots in row will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math> {as if you pick any dot then you have pick second dot from remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> dots, so total ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>=</mo><mn>6</mn></math>}</p><p>Similarly, number of ways of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> adjacent dots in column<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo></math>Number of ways of selecting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> adjacent dots from the given diagram we will  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>7</mn><mo>+</mo><mn>6</mn><mo>&#215;</mo><mn>7</mn><mo>=</mo><mn>84</mn></math></p><p>So, probability is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>84</mn><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>49</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mn>84</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>49</mn><mo>&#215;</mo><mn>48</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7</mn><mi>p</mi><mo>=</mo><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>84</mn><mo>&#215;</mo><mn>2</mn></mrow><mrow><mn>49</mn><mo>&#215;</mo><mn>48</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>.</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q2. JEE Advanced 2021 (Paper 2)

*Type:* `multipleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi><mo>+</mo><mn>2</mn><mo>&#8804;</mo><mn>10</mn><mo>,</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi></mrow></mfenced><mo>:</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi><mo>&#60;</mo><mi>k</mi><mo>&#60;</mo><mi>l</mi><mo>,</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>.....</mn><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p>and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>4</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi></mrow></mfenced><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>l</mi><mo>&#160;</mo><mtext>are&#160;distint&#160;elements&#160;in</mtext><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p>If the total number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>r</mi></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mi>r</mi></msub><mo>,</mo><mi>r</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></math> then which of the following statements is (are) TRUE?</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>1000</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>44</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>3</mn></msub><mo>=</mo><mn>220</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>n</mi><mn>4</mn></msub><mn>12</mn></mfrac><mo>=</mo><mn>420</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>n</mi><mn>4</mn></msub><mn>12</mn></mfrac><mo>=</mo><mn>420</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>i</mi></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></mrow></mfenced><mo>:</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>...</mn><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>1000</mn></math></p><p>i.e., number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced><mo>:</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi><mo>+</mo><mn>2</mn><mo>&#8804;</mo><mn>10</mn><mo>,</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>...</mn><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 100px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>j</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8942;</mo></math></td>			<td> </td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>9</mn></math></td>		</tr>	</tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>44</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi></mrow></mfenced><mo>:</mo><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#60;</mo><mi>j</mi><mo>&#60;</mo><mi>k</mi><mo>&#60;</mo><mi>l</mi><mo>,</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>....10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>3</mn></msub><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>210</mn></math></p><p>i.e. number of elements in <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mn>210</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>4</mn></msub><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>l</mi></mrow></mfenced><mo>:</mo><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>l</mi><mo>&#160;</mo><mtext>are&#160;distinct&#160;elements&#160;in</mtext><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>.......</mn><mo>,</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>4</mn></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mo>&#215;</mo><mn>4</mn><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5040</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>n</mi><mn>4</mn></msub><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>5040</mn><mn>12</mn></mfrac><mo>=</mo><mn>420</mn></math></p>

</details>

---

### Q3. JEE Advanced 2006

*Type:* `singleCorrect` | *Level:* `3`

If $r, s, t$ are prime numbers and $p, q$ are the positive integers such that LCM of $p, q$ is $r^2 s^4 t^2$, then the number of ordered pairs $(p, q)$ is

**Options:**

- **(A)** 252
- **(B)** 254
- **(C)** 225
- **(D)** 224

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 225**

**Detailed Solution:**

Since, $r, s, t$ are prime numbers.
$\therefore$ Selection of $p$ and $q$ are as under
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_advanced/PK48_ScZ9Uo3f0yPK15Dvens-4AMMDMQM64oOlmGudc.original.fullsize.png">

$\therefore$ Total number of ways to select $s=9$.
Similarly, the number of ways to select $t=5$.
$\therefore$ Total number of ways $=5 \times 9 \times 5=225$.

</details>

---

