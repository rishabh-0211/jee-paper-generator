# JEE Advanced Mathematics - Permutation Combination

## Topic 3: Combination

**Total Questions:** 4

---

### Q1. JEE Advanced 2026 (Paper 2)

*Type:* `numerical` | *Level:* `3`

A bookshelf contains $6$ distinct books of Mathematics and $5$ distinct books of Physics. From these $11$ books, $6$ books are chosen at random. Let $X$ be the absolute value of the difference between the number of Mathematics books chosen and the number of Physics books chosen. If $\alpha$ is the mean of the random variable $X$, then the value of $77\alpha$ is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **100**

**Detailed Solution:**

Total number of ways to choose $6$ books from $11$ books is $^{11}C_{6} = 462$.

Let $M$ and $P$ be the number of Mathematics and Physics books chosen respectively. Since $6$ books are chosen, $M + P = 6$.

The random variable $X$ is given by $X = |M - P| = |2M - 6|$.

The possible selections of $(M, P)$, the corresponding values of $X$, and the number of ways are as follows:

For $M=1, P=5$: $X = |1 - 5| = 4$, Number of ways $= ^{6}C_{1} \times ^{5}C_{5} = 6 \times 1 = 6$

For $M=2, P=4$: $X = |2 - 4| = 2$, Number of ways $= ^{6}C_{2} \times ^{5}C_{4} = 15 \times 5 = 75$

For $M=3, P=3$: $X = |3 - 3| = 0$, Number of ways $= ^{6}C_{3} \times ^{5}C_{3} = 20 \times 10 = 200$

For $M=4, P=2$: $X = |4 - 2| = 2$, Number of ways $= ^{6}C_{4} \times ^{5}C_{2} = 15 \times 10 = 150$

For $M=5, P=1$: $X = |5 - 1| = 4$, Number of ways $= ^{6}C_{5} \times ^{5}C_{1} = 6 \times 5 = 30$

For $M=6, P=0$: $X = |6 - 0| = 6$, Number of ways $= ^{6}C_{6} \times ^{5}C_{0} = 1 \times 1 = 1$

The mean $\alpha$ of the random variable $X$ is given by:

$\alpha = \dfrac{\sum X_i f_i}{\sum f_i}$

$\alpha = \dfrac{4(6) + 2(75) + 0(200) + 2(150) + 4(30) + 6(1)}{462}$

$\alpha = \dfrac{24 + 150 + 0 + 300 + 120 + 6}{462}$

$\alpha = \dfrac{600}{462} = \dfrac{100}{77}$

Therefore, the value of $77\alpha$ is:

$77\alpha = 77 \times \dfrac{100}{77} = 100$

Answer: $100$

</details>

---

### Q2. JEE Advanced 2018 (Paper 2)

*Type:* `singleCorrect` | *Level:* `2`

In a high school, a committee has to be formed from a group of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> boys
<math><msub><mrow><mi>M</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>M</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>M</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>M</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>M</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>M</mi></mrow><mrow><mn>6</mn></mrow></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> girls <math><msub><mrow><mi>G</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>G</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>G</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>G</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>G</mi></mrow><mrow><mn>5</mn></mrow></msub></math>.
(i) Let <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> be the total number of ways in which the committee can be formed such that the committee has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> members, having exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> boys and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> girls.
(ii) Let <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub></math> be the total number of ways in which the committee can be formed such that the committee has at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> members, and having an equal number of boys and girls.
(iii) Let <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>3</mn></mrow></msub></math> be the total number of ways in which the committee can be formed such that the committee has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> members, at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> of them being girls.
(iv) Let <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>4</mn></mrow></msub></math> be the total number of ways in which the committee can be formed such that the committee has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> members, having at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> girls and such that both <math><msub><mrow><mi>M</mi></mrow><mrow><mn>1</mn></mrow></msub></math> and <math><msub><mrow><mi>G</mi></mrow><mrow><mn>1</mn></mrow></msub></math> are NOT in the committee together.<table border="1">	<tbody>		<tr>			<td>LIST-I</td>			<td>LIST-II</td>		</tr>		<tr>			<td>A. The value of <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is</td>			<td>P. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>136</mn></math></td>		</tr>		<tr>			<td>B. The value of <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is</td>			<td>Q. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>189</mn></math></td>		</tr>		<tr>			<td>C. The value of <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>3</mn></mrow></msub></math> is</td>			<td>R. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn></math></td>		</tr>		<tr>			<td>D. The value of <math><msub><mrow><mi>&#945;</mi></mrow><mrow><mn>4</mn></mrow></msub></math> is</td>			<td>S. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math></td>		</tr>		<tr>			<td> </td>			<td>T. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>381</mn></math></td>		</tr>		<tr>			<td> </td>			<td>U. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>461</mn></math></td>		</tr>	</tbody></table>The correct option is:

**Options:**

- **(A)** a-s;b-u;c-t;d-q;
- **(B)** a-u;b-t;c-q;d-p;
- **(C)** a-t;b-r;c-s;d-p;
- **(D)** a-t;b-r;c-q;d-p;

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) a-s;b-u;c-t;d-q;**

**Detailed Solution:**

<math><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math> <math><msub><mrow><mi>α</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mi> </mi><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>200</mn></math>
So <math><mi>P</mi><mo>→</mo><mn>4</mn></math>
<math><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced></math> <math><msub><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>2</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>11</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mo>-</mo><mn>1</mn><mo>=</mo><mn>461</mn></math>
So <math><mi>Q</mi><mo>→</mo><mn>6</mn></math>
<math><mfenced separators="|"><mrow><mn>3</mn></mrow></mfenced></math> <math><msub><mrow><mi>α</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>11</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>5</mn></mtd></mtr></mtable></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>381</mn></math>
So <math><mi>R</mi><mo>→</mo><mn>5</mn></math>
<math><mfenced separators="|"><mrow><mn>4</mn></mrow></mfenced></math> <math><msub><mrow><mi>α</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>3</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>6</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>4</mn></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable></mrow></mfenced><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd></mtr></mtable></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mn>5</mn></mtd></mtr><mtr><mtd><mn>4</mn></mtd></mtr></mtable></mrow></mfenced><mo>=</mo><mn>189</mn></math>
So <math><mi>S</mi><mo>→</mo><mn>2</mn></math>

</details>

---

### Q3. JEE Advanced 2016 (Paper 1)

*Type:* `singleCorrect` | *Level:* `1`

A debate club consists of 6 girls and 4 boys. A team of 4 members is to be selected from this club including the selection of a captain (from among these 4 members) for the team. If the team has to include at most one boy, then the number of ways of selecting the team is

**Options:**

- **(A)** 380
- **(B)** 320
- **(C)** 260
- **(D)** 95

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 380**

**Detailed Solution:**

<p>There are 2 cases-</p><p>i. All the 4 are girls</p><p>ii. 3 girls and 1 boy</p><p>So the answer is </p><p><math><mfenced separators="|"><mrow><msup><mrow></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>+</mo><msup><mrow></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>.</mo><mi> </mi><msup><mrow></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow></mfenced><mo>.</mo><mi> </mi><msup><mrow></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>380</mn></math>     (<math><msup><mrow></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo></math> No. of ways of selecting captain)</p>

</details>

---

### Q4. JEE Advanced 2014 (Paper 2)

*Type:* `singleCorrect` | *Level:* `1`

<strong> Paragraph: </strong>

Box $1$ contains three cards bearing numbers $1,2,3$; box $2$ contains five cards bearing numbers $1,2,3,4,5$; and box $3$ contains seven cards bearing numbers $1,2,3,4,5,6,7$. A card is drawn from each of the boxes. Let $x_{i}$ be the number on the card drawn from the $i^{t h}$ box, $i=1,2,3$.


 <strong> Question: </strong>

The probability that $x_{1}, x_{2}, x_{3}$ are in an arithmetic progression, is

**Options:**

- **(A)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>11</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>11</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>**

**Detailed Solution:**

Here <math><mn>2</mn><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>=</mo></math> even
Hence number of favorable ways <math><mo>=</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>1</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>3</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mn>11</mn></math>

</details>

---

