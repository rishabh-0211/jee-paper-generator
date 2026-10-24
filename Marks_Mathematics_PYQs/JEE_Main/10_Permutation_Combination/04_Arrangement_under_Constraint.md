# JEE Main Mathematics - Permutation Combination

## Topic 4: Arrangement under Constraint

**Total Questions:** 35

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

Two players $A$ and $B$ play a series of games of badminton. The player, who wins $5$ games first, wins the series. Assuming that no game ends in a draw, the number of ways, in which player $A$ wins the series is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **126**

**Detailed Solution:**

Player $A$ wins the series if $A$ wins $5$ games before $B$ wins $5$ games. The series can last for a minimum of $5$ games and a maximum of $9$ games.

If player $A$ wins the series in exactly $n$ games, then $A$ must win the $n$-th game, and $A$ must win exactly $4$ out of the first $n-1$ games. The number of ways this can happen is given by $^{n-1}C_{4}$.

The possible values for $n$ are $5, 6, 7, 8,$ and $9$.

Total number of ways for $A$ to win the series is the sum of the number of ways $A$ can win in $5, 6, 7, 8,$ or $9$ games:

Total ways $= ^{4}C_{4} + ^{5}C_{4} + ^{6}C_{4} + ^{7}C_{4} + ^{8}C_{4}$

Using the property $^{n}C_{r} + ^{n}C_{r-1} = ^{n+1}C_{r}$, we can simplify the sum:
$^{4}C_{4} = ^{5}C_{5}$
$^{5}C_{5} + ^{5}C_{4} = ^{6}C_{5}$
$^{6}C_{5} + ^{6}C_{4} = ^{7}C_{5}$
$^{7}C_{5} + ^{7}C_{4} = ^{8}C_{5}$
$^{8}C_{5} + ^{8}C_{4} = ^{9}C_{5}$

Therefore, the total number of ways is:
$^{9}C_{5} = \dfrac{9!}{5!4!} = \dfrac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126$

Answer: $126$

</details>

---

### Q2. JEE Main 2025 (23 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of ways, 5 boys and 4 girls can sit in a row so that either all the boys sit together or no two boys sit together, is $\qquad$ -

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17280**

**Detailed Solution:**

A : number of ways that all boys sit together $=5!\times 5!$
B : number of ways if no 2 boys
sit together $=4!\times 5$ !
$\mathrm{A} \cap \mathrm{B}=\phi$
Required no. of ways $=5!\times 5!+4!\times 5!=17280$

</details>

---

### Q3. JEE Main 2025 (23 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of words, which can be formed using all the letters of the word "DAUGHTER", so that all the vowels never come together, is

**Options:**

- **(A)** $36000$
- **(B)** $37000$
- **(C)** $34000$
- **(D)** $35000$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $36000$**

**Detailed Solution:**

DAUGHTER
Total words $=8$ !
Total words in which vowels are together $=6!\times 3!$ words in which all vowels are not together
$\begin{aligned}
& =8!-6!\times 3! \\
& =6![56-6] \\
& =720 \times 50 \\
& =36000
\end{aligned}$

Ans.(3)

</details>

---

### Q4. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a group of 3 girls and 4 boys, there are two boys $B_1$ and $B_2$. The number of ways, in which these girls and boys can stand in a queue such that all the girls stand together, all the boys stand together, but $B_1$ and $B_2$ are not adjacent to each other, is :

**Options:**

- **(A)** 96
- **(B)** 144
- **(C)** 120
- **(D)** 72

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 144**

**Detailed Solution:**

Total - when $\mathrm{B}_1$ and $\mathrm{B}_2$ are together
$=2!(3!4!)-2!(3!(3!2!))=144$

</details>

---

### Q5. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

From all the English alphabets, five letters are chosen and are arranged in alphabetical order. The total number of ways, in which the middle letter is ' M ', is :

**Options:**

- **(A)** $5148$
- **(B)** $6084$
- **(C)** $4356$
- **(D)** $14950$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5148$**

**Detailed Solution:**

$\begin{aligned}
& \underbrace{A B}_{12} \quad \underbrace{\text { MN........Z }}_{13} \\
& =\underset{\substack{\text { Selection of two } \\
\text { leters before } \mathrm{M}}}{{ }^{12} \mathrm{C}_2} \times \underset{\substack{\text { Selection of two } \\
\text { leter after } \mathrm{M}}}{{ }^{13} \mathrm{C}_2}=5148
\end{aligned}$

</details>

---

### Q6. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

60 words can be made using all the letters of the word BHBJO, with or without meaning. If these words are written as in a dictionary, then the $50^{\text {th }}$ word is :

**Options:**

- **(A)** JBBOH
- **(B)** OBBJH
- **(C)** OBBHJ
- **(D)** HBBJO

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) OBBJH**

**Detailed Solution:**

$\mathrm{B} \mathrm{B} \mathrm{H} \mathrm{J} \mathrm{O}$
B____$4 !=24$
H____$\frac{4 !}{2 !}=12$
j____$\frac{4 !}{2 !}=12$
O B B H J
O B B J H $\rightarrow 50^{\text {th }}$ rank

</details>

---

### Q7. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

All the letters of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>W</mi><mi>E</mi><mi>N</mi><mi>T</mi><mi>Y</mi></math> are written in all possible ways with or without meaning and these words are written as in a dictionary. The serial number of the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>W</mi><mi>E</mi><mi>N</mi><mi>T</mi><mi>Y</mi></math> IS

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **553**

**Detailed Solution:**

<p>We have to find the rank of word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>W</mi><mi>E</mi><mi>N</mi><mi>T</mi><mi>Y</mi></math>.</p><p>Words starting from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>720</mn><mn>2</mn></mfrac><mo>=</mo><mn>360</mn></math></p><p>Words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>E</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mn>2</mn></mfrac><mo>=</mo><mn>60</mn></math></p><p>Words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>N</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mn>2</mn></mfrac><mo>=</mo><mn>60</mn></math></p><p>Words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>E</mi><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>N</mi><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Words starting with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>T</mi><mo>=</mo><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math></p><p>Then the next word will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi><mi>T</mi><mi>W</mi><mi>E</mi><mi>N</mi><mi>T</mi><mi>Y</mi></math> and its rank will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>360</mn><mo>+</mo><mn>60</mn><mo>+</mo><mn>60</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>553</mn></math></p>

</details>

---

### Q8. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> be in A.P. Nine-digit numbers are to be formed using each of these three digits thrice such that three consecutive digits are in A.P. at least once. How many such numbers can be formed?

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1260**

**Detailed Solution:**

<p>Three numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi></math> are in A.P. ad they are used to making <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo></math> digit number using each digit thrice such that atleast three consecutive digits are in A.P., So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>a</mi></math> will also be in A.P.</p><p>Now, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> position to put <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mfenced><mrow><mi>c</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>a</mi></mrow></mfenced></math> as <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><munder><mrow><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi></mrow><mo>&#9183;</mo></munder><mrow><mn>7</mn><mo>&#160;</mo><mi>positions</mi></mrow></munder><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mo>&#160;</mo></math>.</p><p>Number of such numbers is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>&#183;</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1260</mn></math></p>

</details>

---

### Q9. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of five-digit numbers, greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40000</mn></math> and divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, which can be formed using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> without repetition, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>132</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>**

**Detailed Solution:**

<p>We need to find the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> digit numbers greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40000</mn></math> and divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p>Case I : Numbers start with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p>Here if the number starts with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> it should end with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> to be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/07bd479b-a542-4264-ac04-51f8fcf40369.png" style="width: 380px; height: 77px;" /></p><p>Case II : Number starts with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> and the last digit can have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/299d2694-a7da-4eed-9e94-4d95394b61b4.png" style="width: 200px; height: 78px;" /></p><p>Case III : The number starts with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and the last digit should have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>.</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/f36ffd05-fe48-445a-9b3a-9cc9fcddef14.png" style="width: 210px; height: 80px;" /></p><p>Total numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>120</mn></math>.</p><p>Hence this is the correct option.</p>

</details>

---

### Q10. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of permutations, of the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> without repetition, which neither contain the string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>153</mn></math> nor the string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2467</mn></math>, is _______ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4898**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>7</mn></math></p><p>Now total numbers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> digit number will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>!</mo></math> without repetition,</p><p>Now total numbers which contain string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>154</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>!</mo></math></p><p>Total numbers which contain string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2367</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>!</mo></math></p><p>And number which contain both string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2367</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>154</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>So, total number which does not contain string <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>154</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2367</mn></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>!</mo><mo>-</mo><mfenced><mrow><mn>5</mn><mo>!</mo><mo>+</mo><mn>4</mn><mo>!</mo><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5040</mn><mo>-</mo><mfenced><mrow><mn>120</mn><mo>+</mo><mn>24</mn><mo>-</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5040</mn><mo>-</mo><mn>142</mn><mo>=</mo><mn>4898</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q11. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the number of words, with or without meaning. which can be made using all the letters of the word MATHEMATICS in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> do not come together, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>6</mn><mo>!</mo><mo>)</mo><mi>k</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2835</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5670</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1890</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>945</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5670</mn></math>**

**Detailed Solution:**

<blockquote><p>The word &#39;MATHEMATICS&#39; consists of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> letters including two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>'</mo><mi>s</mi></math>, two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mo>'</mo><mi>s</mi></math> and two <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>'</mo><mi>s</mi></math>,</p><p>Now, first we will arrange letters <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>M</mi><mi>_</mi><mi>A</mi><mi>_</mi><mi>T</mi><mi>_</mi><mi>H</mi><mi>_</mi><mi>E</mi><mi>_</mi><mi>M</mi><mi>_</mi><mi>A</mi><mi>_</mi><mi>T</mi><mi>_</mi><mi>I</mi><mi>_</mi></math>.</p><p>Here, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> gaps to fill <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>S</mi></math>.</p><p>The number of words with or without meaning can be formed from the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>MATHEMATICS</mi></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>S</mi></math> does not come together is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#215;</mo><mn>2</mn><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>9</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5670</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q12. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The number of arrangements of the letters of the word &quot;INDEPENDENCE&quot; in which all the vowels always occur together is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16800</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33600</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18000</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14800</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16800</mn></math>**

**Detailed Solution:**

<blockquote><p>There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> vowels in the given word which are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>E</mi><mo>'</mo><mi>s</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#8201;</mo><mn>1</mn><mi>I</mi></math>.</p><p>Since they have to always occur together we take them as a single object <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>&#160;</mo><mi>E</mi><mo>&#160;</mo><mi>E</mi><mo>&#160;</mo><mi>E</mi><mo>&#160;</mo><mi>I</mi></math> for the time being.</p><p>This single object together with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> remaining object will account for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> objects.</p><p>There <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> objects in which there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>N</mi><mo>&#39;</mo><mi>s</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#8201;</mo><mn>2</mn><mi>D</mi><mo>&#39;</mo><mi>s</mi></math> can be arrangement in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>8</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math> ways.</p><p>Corresponding to each of their arrangements the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> vowels <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>,</mo><mi>E</mi><mo>,</mo><mi>E</mi><mo>,</mo><mi>E</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>I</mi></math> which can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac></math></p><p>Hence, required number of arrangements.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>8</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>16800</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q13. JEE Main 2023 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of words, with or without meaning, that can be formed using all the letters of the word ASSASSINATION so that the vowels occur together, is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **50400**

**Detailed Solution:**

<p>In the word <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ASSASSINATION</mi></math>, we will treat all the vowels that is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AAAIIO</mi></math>  as one letter only.</p><p>Now, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>AAAIIO</mi></mfenced><mi>SSSSNNT</mi></math></p><p>This has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>=</mo><mo>(</mo><mn>7</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>1</mn><mo>)</mo></math> letters of which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi></math> occurs <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> times, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">N</mi></math> occur <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> times,</p><p>Thus, the number of ways of  arranging these letters <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>8</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>840</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> vowels in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> occurs <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#160;</mo></math>times, and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> occur two times, they can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>60</mn><mo>&#160;</mo><mtext>&#160;ways.&#160;</mtext></math></p><p> Therefore, required number of ways<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mo>(</mo><mn>840</mn><mo>&#160;</mo><mo>&#215;</mo><mo>&#160;</mo><mn>60</mn><mo>)</mo><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>50400</mn><mo>.</mo></math></p>

</details>

---

### Q14. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of seven digits odd numbers, that can be formed using all the seven digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **240**

**Detailed Solution:**

<p>To find the number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> digit odd number formed by using the seven digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></math></p><p>We will take following cases,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo></math> fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> as unit place,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><mn>2</mn><mo>&#160;</mo><mtext>is&#160;repeating&#160;three&#160;times&#160;and&#160;3&#160;is&#160;repeating&#160;two&#160;times</mtext></mrow></mfenced></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo></math> fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> unit place,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo></math> fixing <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> as unit place,</p><p>So total number of ways will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac></math></p><p>Now adding all the cases we will get, total number of ways as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>60</mn><mo>+</mo><mn>120</mn><mo>+</mo><mn>60</mn><mo>=</mo><mn>240</mn></math></p>

</details>

---

### Q15. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

Number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-digit numbers (the repetition of digits is allowed) which are made using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> , and are divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> , is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p>Given,</p><p>We have to form four-digit number using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math></p><p>Now for number to be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> we need to fix the last digit as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> as  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mn>5</mn></math>, so that number can be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and for divisibility by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> the addition of all number should be divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>,</p><p>So making cases where sum is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> we get,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>as&#160;</mtext><mn>1</mn><mo>,1,2&#160;&#38;&#160;5</mo><mtext>&#160;sum&#160;is&#160;divisible&#160;by&#160;</mtext><mn>3</mn></mrow></mfenced></math></p><p>So, total ways for case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways,</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>-</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext><mo>,</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>3</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mtext>&#160;ways</mtext></math></p><p>So, total ways for case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> ways.</p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>-</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>&#8594;</mo><mn>6</mn><mtext>&#160;ways</mtext></math></p><p>Case <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>-</mo><mo>&#160;</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>&#8594;</mo><mn>3</mn><mo>&#160;</mo><mtext>ways</mtext></math></p><p>So, adding all cases we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>21</mn></math> ways.</p>

</details>

---

### Q16. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

The number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> digit numbers, that can be formed using all the digits of the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>123412341</mn></math> so that the even digits occupy only even places, is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>According to the question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math></p><p>there are four even digits as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> are repeating two times each. 
So, the even digits will occupy the even places in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>!</mo></mrow><mrow><mo>(</mo><mn>2</mn><mo>!</mo><mo>&#160;</mo><mn>2</mn><mo>!</mo><mo>)</mo></mrow></mfrac><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>6</mn></math> ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> are repeating two and three times respectively.
So, the remaining places will be occupied by odd digits in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mo>(</mo><mn>3</mn><mo>!</mo><mo>&#160;</mo><mn>2</mn><mo>!</mo><mo>)</mo></mrow></mfrac><mo>=</mo><mn>10</mn></math> ways</p><p>Therefore, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> digits that can be formed <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>6</mn><mo>&#215;</mo><mn>10</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>60</mn></math>.
Hence, the answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>.</p>

</details>

---

### Q17. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all passwords which are six to eight characters long, where each character is either an alphabet from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>,</mo><mi>D</mi><mo>,</mo><mi>E</mi></mrow></mfenced></math> or a number from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> with the repetition of characters allowed. If the number of passwords in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> whose at least one character is a number from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#215;</mo><msup><mn>5</mn><mn>6</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7073**

**Detailed Solution:**

<blockquote><p>Given total available characters is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and total digits are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>,</p><p>So, for<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>6</mn><mo>-</mo></math>digit password, the number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>6</mn></msup><mo>-</mo><msup><mn>5</mn><mn>6</mn></msup></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>-</mo></math>digit password, the number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>7</mn></msup><mo>-</mo><msup><mn>5</mn><mn>7</mn></msup></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>-</mo></math>digit password, the number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>8</mn></msup><mo>-</mo><msup><mn>5</mn><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>  Total ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mn>10</mn><mn>6</mn></msup><mo>+</mo><msup><mn>10</mn><mn>7</mn></msup><mo>+</mo><msup><mn>10</mn><mn>8</mn></msup></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mn>5</mn><mn>6</mn></msup><mo>+</mo><msup><mn>5</mn><mn>7</mn></msup><mo>+</mo><msup><mn>5</mn><mn>8</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mn>6</mn></msup><msup><mn>5</mn><mn>6</mn></msup><mo>+</mo><msup><mn>2</mn><mn>7</mn></msup><msup><mn>5</mn><mn>7</mn></msup><mo>+</mo><msup><mn>2</mn><mn>8</mn></msup><msup><mn>5</mn><mn>8</mn></msup><mo>-</mo><msup><mn>5</mn><mn>6</mn></msup><mo>-</mo><msup><mn>5</mn><mn>7</mn></msup><mo>-</mo><msup><mn>5</mn><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>5</mn><mn>6</mn></msup><mfenced><mrow><msup><mn>2</mn><mn>6</mn></msup><mo>+</mo><mn>5</mn><mo>&#183;</mo><msup><mn>2</mn><mn>7</mn></msup><mo>+</mo><mn>25</mn><mo>&#183;</mo><msup><mn>2</mn><mn>8</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mn>5</mn><mo>-</mo><mn>25</mn></mrow></mfenced><mo>=</mo><mn>7073</mn><mo>&#183;</mo><msup><mn>5</mn><mn>6</mn></msup></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#215;</mo><msup><mn>5</mn><mn>6</mn></msup></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>7073</mn></math></p></blockquote>

</details>

---

### Q18. JEE Main 2022 (29 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><msub><mi>b</mi><mn>3</mn></msub><msub><mi>b</mi><mn>4</mn></msub></math> be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>-element permutation with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>i</mi></msub><mo>&#8712;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>100</mn></mrow></mfenced></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#8804;</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>i</mi></msub><mo>&#8800;</mo><msub><mi>b</mi><mi>j</mi></msub></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>&#8800;</mo><mi>j</mi></math>, such that either <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msub><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>3</mn></msub></math> are consecutive integers or <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>3</mn></msub><mo>,</mo><msub><mi>b</mi><mn>4</mn></msub></math> are consecutive integers. Then the number of such permutations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><msub><mi>b</mi><mn>3</mn></msub><msub><mi>b</mi><mn>4</mn></msub></math> is equal to ______.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18915**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>i</mi></msub><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mn>100</mn></mrow></mfenced></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo></math> set when <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>2</mn></msub><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>3</mn></msub></math> are consecutive</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mn>97</mn><mo>+</mo><mn>97</mn><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>97</mn><mo>&#160;</mo><mfenced><mrow><mtext>added</mtext><mo>&#160;</mo><mn>98</mn><mo>&#160;</mo><mtext>times</mtext></mrow></mfenced><mo>=</mo><mn>97</mn><mo>&#215;</mo><mn>98</mn><mo>=</mo><mn>9506</mn></math></p><p>Similarly when <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>2</mn></msub><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>3</mn></msub><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>4</mn></msub></math> are consecutive</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mn>97</mn><mo>&#215;</mo><mn>98</mn><mo>=</mo><mn>9506</mn></math></p><p>Now when <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>&#160;</mo><msub><mi>b</mi><mn>3</mn></msub><mo>&#160;</mo><msub><mi>b</mi><mn>4</mn></msub></math> are consecutive then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>97</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mfenced><mrow><mi>A</mi><mi>U</mi><mi>B</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>n</mi><mfenced><mi>B</mi></mfenced><mo>-</mo><mi>n</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p>Number of required permutation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9506</mn><mo>+</mo><mn>9506</mn><mo>-</mo><mn>97</mn><mo>=</mo><mn>18915</mn></math></p>

</details>

---

### Q19. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The total number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>-digit numbers, formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math> without repetition, which are multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p>Given set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Here sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>7</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn></math></p><p>So there will be two cases</p><p>Case (i) When numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Arrangement will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mn>6</mn></math></p><p>In unit place <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> can take place because for multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> number should be even &amp; sum of digits should be multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>.</p><p>So total way in which remaining number can be taken will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>!</mo><mo>&#215;</mo><mn>2</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>48</mn></math> ways</p><p>Case (ii) When numbers are  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></mrow></mfenced></math></p><p>Arrangement will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mi>_</mi><mo>&#160;</mo><mn>2</mn></math> </p><p>So total way in which remaining number can be taken will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>!</mo><mo>=</mo><mn>24</mn></math> ways</p><p>Adding case (i) &amp; case (ii), we get</p><p>required <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>-digit numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>+</mo><mn>48</mn><mo>=</mo><mn>72</mn></math></p>

</details>

---

### Q20. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of six letter words (with or without meaning), formed using all the letters of the word &#39;VOWELS&#39;, so that all the consonants never come together, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **576**

**Detailed Solution:**

<p>Given word &#39;VOWELS&#39;</p><p>Number of words Arranging all the letters <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>6</mn><mo>!</mo></math></p><p>In the given word Consonants are W, L, S.</p><p>Treating all the consonants as one unit then number of units will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo></math></p><p>No of such arrangements <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>!</mo><mo>.</mo><mfenced><mrow><mn>3</mn><mo>!</mo></mrow></mfenced></math></p><p>VOWELS all the consonants never come together <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>Total - all consonants come together <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>!</mo><mo>-</mo><mn>4</mn><mo>!</mo><mo>&#215;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>576</mn></math></p>

</details>

---

### Q21. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> students in class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>6</mn></math> students in class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> students in class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo></math> If the number of ways, in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> students can be selected from them so as to include at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> students from each class and at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> students from the total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> students of class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mi>k</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **238**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mi>Class</mi><mo>&#160;</mo></mtd><mtd><msup><mn>10</mn><mrow><mi>th</mi><mo>&#160;</mo></mrow></msup></mtd><mtd><msup><mn>11</mn><mrow><mi>th</mi><mo>&#160;</mo></mrow></msup></mtd><mtd><msup><mn>12</mn><mrow><mi>th</mi><mo>&#160;</mo></mrow></msup></mtd></mtr><mtr><mtd><mi>Total</mi><mo>&#160;</mo><mi>student</mi><mo>&#160;</mo></mtd><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>8</mn></mtd></mtr></mtable></math></p><p>From these students, we can choose two students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>, three students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math> students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo></math></p><p>So, total number of ways  is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></math></p><p>Again, From these students, we can choose two students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo></math> two students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>6</mn></math> students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo></math></p><p>Number of selection <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></math></p><p>Again, from these students, we can choose three students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>, two students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math> students from class <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo></math> So, total number of ways  is  <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Total number of ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced><mo>+</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>7</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>23800</mn></math></p><p>According to question <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mi>k</mi><mo>=</mo><mn>23800</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>238</mn></math></p>

</details>

---

### Q22. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the digits are not allowed to repeat in any number formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo></math> then the number of all numbers greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>000</mn></math> is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **96**

**Detailed Solution:**

<p>We have to form a number greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>000</mn></math> by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo></math> hence, the first place of the number can&#39;t be zero.</p><p>Thus, for the first place we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> choices i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math> and the remaining places can be filled with any of the digits, thus we have respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></math> choices.</p><p>Hence, using the fundamental principle of multiplication, the total numbers which are greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>000</mn></math> are</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/d71239ae-9ae1-4f58-9f50-1318ef46fcaf-image.png" style="width: 222px; height: 73px;" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>=</mo><mn>96</mn><mo>.</mo></math></p>

</details>

---

### Q23. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of times the digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> will be written when listing the integers from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **300**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mn>3</mn><mrow><mo>-</mo><mo>-</mo></mrow></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><msub><mn>3</mn><mo>-</mo></msub><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mo>-</mo><mn>3</mn><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>=</mo><mn>100</mn></math></p><p>Total is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn></math>.</p>

</details>

---

### Q24. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The number of seven digit integers with sum of the digits equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and formed by using the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> only is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>77</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>82</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>42</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>77</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">I</mi></mfenced></math> First possiblity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math><p>required number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>42</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>II</mi></mfenced></math> Second possiblity is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>2</mn></math></p><p>required number <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>35</mn></math></p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>42</mn><mo>+</mo><mn>35</mn><mo>=</mo><mn>77</mn></math></p>

</details>

---

### Q25. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

The total number of numbers, lying between <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math> that can be formed with the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo></math> if the repetition of digits is not allowed and numbers are divisible by either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **32**

**Detailed Solution:**

<p>We need three digits numbers.</p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>15</mn></math></p><p>So, number of possible triplets for multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>2</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>&#215;</mo><mo>&#8970;</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>-</mo><mn>1</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mo>&#8970;</mo><mn>2</mn><mo>=</mo><mn>32</mn></math></p><p>Alternate:</p><p> <img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/de484a07-7077-457a-87c0-de15d33b908d-image.png" style="width: 161px; height: 67px;" /></p><p>divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>12</mn></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/b06d9520-ac3e-4adf-b2d9-adee41d9c630-image.png" style="width: 97px; height: 61px;" /></p><p>Divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mn>12</mn><mo>&#8594;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>&#8594;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>15</mn><mo>&#8594;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#8594;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>24</mn><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>&#8594;</mo><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></mtd></mtr><mtr><mtd><mn>42</mn><mo>&#8594;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>&#8594;</mo><menclose notation="bottom"><mn>3</mn><mo>!</mo><mo>=</mo><mn>6</mn></menclose></mtd></mtr></mtable><mspace linebreak="newline"></mspace><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>24</mn></math></p><p>Divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>;</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>;</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>;</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></math></p><p>Required No. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>4</mn><mo>=</mo><mn>32</mn></math></p>

</details>

---

### Q26. JEE Main 2020 (06 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

The number of words (with or without meaning) that can be formed from all the letters of the word<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#34;</mo><mi>L</mi><mi>E</mi><mi>T</mi><mi>T</mi><mi>E</mi><mi>R</mi><mo>&#34;</mo></math> in which vowels never come together is.....

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **120**

**Detailed Solution:**

<p> Consonants are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">L</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">T</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">R</mi></math></p><p>Vowels are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi><mo>,</mo><mo>&#160;</mo><mi mathvariant="normal">E</mi><mo>,</mo></math></p><p>Total number of words (without meaning) from letters of word <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi>LETTER</mi><mo>&#39;</mo><mo>=</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>180</mn></math></p><p>Total number of words (with or without meaning) from letters of word <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mi>LETTER</mi><mo>&#39;</mo></math> if vowels are together <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Required <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>180</mn><mo>-</mo><mn>60</mn><mo>=</mo><mn>120</mn></math></p>

</details>

---

### Q27. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two families with three members each and one family with four members are to be seated in a row. In how many ways can they be seated so that the same family members are not separated ?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>!</mo><mo>&#160;</mo><mn>3</mn><mo>!</mo><mo>&#160;</mo><mn>4</mn><mo>!</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>!</mo><msup><mo>)</mo><mn>3</mn></msup><mo>&#183;</mo><mo>(</mo><mn>4</mn><mo>!</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>(</mo><mn>3</mn><mo>!</mo><mo>)</mo><mn>2</mn><mo>.</mo><mfenced><mrow><mn>4</mn><mo>!</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;3!&#160;</mtext><msup><mfenced><mrow><mn>4</mn><mo>!</mo></mrow></mfenced><mn>3</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>3</mn><mo>!</mo><msup><mo>)</mo><mn>3</mn></msup><mo>&#183;</mo><mo>(</mo><mn>4</mn><mo>!</mo><mo>)</mo></math>**

**Detailed Solution:**

<p>We will use the concept &#39;objects are together&#39;</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><munder><mrow><mo>&#160;</mo><mn>3</mn><mo>!&#160;</mo></mrow><mo>&#9183;</mo></munder><mtext>Total&#160;3&#160;families</mtext></munder><mo>&#215;</mo><munder><munder><msup><mfenced><mrow><mn>3</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup><mo>&#9183;</mo></munder><mtext>families&#160;with&#160;all&#160;3&#160;members&#160;together</mtext></munder><mo>&#215;</mo><munder><munder><mrow><mo>&#160;</mo><mn>4</mn><mo>!&#160;</mo></mrow><mo>&#9183;</mo></munder><mtext>family&#160;with&#160;all&#160;4&#160;together</mtext></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>3</mn><mo>!</mo><msup><mo>)</mo><mn>3</mn></msup><mo>&#215;</mo><mn>4</mn><mo>!</mo></math></p>

</details>

---

### Q28. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Total number of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>-</mo></math> digit numbers in which only and all the five digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> appears, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>6</mn><mo>!</mo></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>!</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mn>6</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>6</mn><mo>!</mo></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>6</mn><mo>!</mo></mrow></mfenced></math>**

**Detailed Solution:**

<p>As we have to make a six-digit number by using all the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>,</mo></math> hence exactly one of the digits is repeating.</p><p>For the digit to repeat we have <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>5</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn></math> choices.
And, six digits in which one is repeating can be arranged in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac></math> ways.
Hence, total such numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#215;</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mfenced><mrow><mn>6</mn><mo>!</mo></mrow></mfenced><mo>.</mo></math></p>

</details>

---

### Q29. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The number of four-digit numbers strictly greater than <math><mn>4321</mn></math> that can be formed using the digit <math><mn>0,1</mn><mo>,</mo><mn>2,3</mn><mo>,</mo><mn>4,5</mn></math> (repetition of digits is allowed) is:

**Options:**

- **(A)** <math><mn>360</mn></math>
- **(B)** <math><mn>288</mn></math>
- **(C)** <math><mn>306</mn></math>
- **(D)** <math><mn>310</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>310</mn></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/e77814f1-b212-4da3-8456-c767436a466b-image6.png"> 
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/504d664a-9ef3-4625-9716-5351a838e40e-image7.jpeg"> 
<math><mo>∴</mo></math> Total Numbers <math><mo>=</mo><mn>216</mn><mo>+</mo><mn>72</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>310</mn></math>

</details>

---

### Q30. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider a class of <math><mn>5</mn></math> girls and <math><mn>7</mn></math> boys. The number of different teams consisting of <math><mn>2</mn></math> girls and <math><mn>3</mn></math> boys that can be formed from this class, if there are two specific boys <math><mi>A</mi></math> and <math><mi>B</mi><mo>,</mo></math> who refuse to be the members of the same team, is:

**Options:**

- **(A)** <math><mn>300</mn></math>
- **(B)** <math><mn>200</mn></math>
- **(C)** <math><mn>500</mn></math>
- **(D)** <math><mn>350</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>300</mn></math>**

**Detailed Solution:**

<math><mfenced close="}" open="" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup/><mn>7</mn><mi>B</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup/><mn>5</mn><mi>G</mi></mrow></mtd></mtr></mtable></mrow></mfenced><mo>→</mo><mfenced separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup/><mn>3</mn><mi>B</mi></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup/><mn>2</mn><mi>G</mi></mrow></mtd></mtr></mtable></mrow></mfenced></math> 

        Total number of ways of forming a team of  <math><mn>3</mn></math>  boys and  <math><mn>2</mn></math>  girls  <math><mo>=</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>7</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>×</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>5</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>7.6</mn><mo>.</mo><mn>5</mn></mrow><mrow><mn>1.2</mn><mo>.</mo><mn>3</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>5.4</mn></mrow><mrow><mn>1.2</mn></mrow></mfrac><mo>=</mo><mn>350</mn></math> 

        Total number of ways of forming a team if two specific boys  <math><msub><mrow><mi>B</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>B</mi></mrow><mrow><mn>2</mn></mrow></msub></math>  always join the team

         <math><mo>=</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>5</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>×</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>5</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mn>50</mn></math> 

        So, the total number of ways of forming a team so that two specific boys never come together

         <math><mo>=</mo><mn>350</mn><mo>-</mo><mn>50</mn><mo>=</mo><mn>300</mn></math>

</details>

---

### Q31. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

From <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> different novels and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> different dictionaries, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> novels and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> dictionary are to be selected and arranged in a row on a shelf so that the dictionary is always in the middle. The number of such arrangements is:

**Options:**

- **(A)** At least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>750</mn></math> but less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>
- **(B)** At least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>
- **(C)** Less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math>
- **(D)** At least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math> but less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>750</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) At least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math>**

**Detailed Solution:**

<math><msub><mrow><mi>N</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>N</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><mi>D</mi><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>N</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>N</mi></mrow><mrow><mn>4</mn></mrow></msub></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>&#8594;</mo></math> Novels

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>&#8594;</mo></math> Dictionary

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math> can be chosen in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> ways

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>1</mn></msub><mo>&#8594;</mo><mn>6</mn></math>

<math><msub><mrow><mi>N</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>&#8594;</mo><mn>5</mn></math>

<math><msub><mrow><mi>N</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#8594;</mo><mn>4</mn></math>

<math><msub><mrow><mi>N</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>&#8594;</mo><mn>3</mn></math>

Total ways <math><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>1080</mn></math>

</details>

---

### Q32. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The number of ways in which an examiner can assign 30 marks to 8 questions, giving not less than 2 marks to any question, is :

**Options:**

- **(A)** ${ }^{30} C_7$
- **(B)** ${ }^{21} C_8$
- **(C)** ${ }^{21} C_7$
- **(D)** ${ }^{30} C_8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) ${ }^{21} C_7$**

**Detailed Solution:**

30 marks to be alloted to 8 questions. Each question has to be given $\geq 2$ marks Let questions be $a, b, c, d, e, f, g, h$ and $a+b+c+d+e+f+g+h=30$
Let $a=a_1+2$ so, $a_1 \geq 0$ $b=a_2+2$ so, $a_2 \geq 0, \ldots \ldots . a_8 \geq 0$
So, $\left.\begin{array}{c}a_1+a_2+\ldots \ldots+a_8 \\ +2+2+\ldots . .+2\end{array}\right\}=30$ $\Rightarrow a_1+a_2+\ldots \ldots+a_8=30-16=14$
So, this is a problem of distributing 14 articles in 8 groups.
Number of ways $={ }^{14+8-1} \mathrm{C}_{8-1}={ }^{21} \mathrm{C}_7$

</details>

---

### Q33. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

A committee of 4 persons is to be formed from 2 ladies, 2 old men and 4 young men such that it includes at least 1 lady, at least 1 old man and at most 2 young men. Then the total number of ways in which this committee can be formed is :

**Options:**

- **(A)** 40
- **(B)** 41
- **(C)** 16
- **(D)** 32

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 41**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/2jZivFEq5kEbu-y3iTE23TBnLtX9mI25ydM5fdm08ms.original.fullsize.png">

Required number of ways
$$
\begin{aligned}
& ={ }^2 \mathrm{C}_1 \times{ }^2 \mathrm{C}_1 \times{ }^2 \mathrm{C}_2+{ }^2 \mathrm{C}_1 \times{ }^2 \mathrm{C}_2 \times{ }^4 \mathrm{C}_1+{ }^2 \mathrm{C}_2 \times \\
& { }^2 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1+{ }^2 \mathrm{C}_2 \times{ }^2 \mathrm{C}_2 \times{ }^4 \mathrm{C}_0 \\
& =2 \times 2 \times \frac{4 \times 3}{2} \\
& \quad \quad \quad 2 \times 1 \times 4+1 \times 2 \times 4+1 \times 1 \times 1
\end{aligned}
$$

</details>

---

### Q34. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

How many different words can be formed by jumbling the letters in the word MISSISSIPPI in which no two $\mathrm{S}$ are adjacent?

**Options:**

- **(A)** $8 \cdot{ }^6 \mathrm{C}_4 \cdot{ }^7 \mathrm{C}_4$
- **(B)** $6.8 \cdot{ }^7 \mathrm{C}_4$
- **(C)** $6 \cdot 7 \cdot{ }^8 \mathrm{C}_4$
- **(D)** $7 \cdot{ }^6 \mathrm{C}_4 \cdot{ }^8 \mathrm{C}_4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $7 \cdot{ }^6 \mathrm{C}_4 \cdot{ }^8 \mathrm{C}_4$**

**Detailed Solution:**

Other than $\mathrm{S}$, seven letters $\mathrm{M}, \mathrm{I}, \mathrm{I}, \mathrm{I}, \mathrm{P}, \mathrm{P}, \mathrm{I}$ can be arranged in $\frac{7 !}{2 ! 4 !}=7.5 .3$.
Now four $\mathrm{S}$ can be placed in 8 spaces in ${ }^8 \mathrm{C}_4$ ways.
Desired number of ways $=7.5 \cdot 3 \cdot{ }^8 \mathrm{C}_4=7 \cdot{ }^6 \mathrm{C}_4 \cdot{ }^8 \mathrm{C}_4$

</details>

---

### Q35. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

How many ways are there to arrange the letters in the word GARDEN with the vowels in alphabetical order?

**Options:**

- **(A)** 120
- **(B)** 480
- **(C)** 360
- **(D)** 240

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 360**

**Detailed Solution:**

Since in half the arrangement $A$ will be before $E$ and other half $E$ will be before $A$. Hence total number of ways $=\frac{6 !}{2}=360$.

</details>

---

