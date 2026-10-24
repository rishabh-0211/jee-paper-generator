# JEE Main Mathematics - Probability

## Topic 6: Baye's Theorem

**Total Questions:** 20

---

### Q1. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A letter is known to have arrived by post either from KANPUR or from ANANTPUR. On the envelope just two consecutive letters AN are visible. The probability, that the letter came from ANANTPUR, is:

**Options:**

- **(A)** $\dfrac{7}{10}$
- **(B)** $\dfrac{10}{17}$
- **(C)** $\dfrac{12}{19}$
- **(D)** $\dfrac{7}{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{10}{17}$**

**Detailed Solution:**

Let $E_1$ be the event that the letter came from KANPUR and $E_2$ be the event that the letter came from ANANTPUR.

Since the letter is equally likely to come from either city, $P(E_1) = P(E_2) = \dfrac{1}{2}$.

Let $A$ be the event that the two consecutive visible letters are AN.

In the word KANPUR, there are 6 letters, so there are 5 pairs of consecutive letters: KA, AN, NP, PU, UR. The pair AN appears exactly once. Thus, $P(A|E_1) = \dfrac{1}{5}$.

In the word ANANTPUR, there are 8 letters, so there are 7 pairs of consecutive letters: AN, NA, AN, NT, TP, PU, UR. The pair AN appears exactly twice. Thus, $P(A|E_2) = \dfrac{2}{7}$.

By Bayes' theorem, the probability that the letter came from ANANTPUR given that AN is visible is:

$P(E_2|A) = \dfrac{P(E_2) P(A|E_2)}{P(E_1) P(A|E_1) + P(E_2) P(A|E_2)}$

$P(E_2|A) = \dfrac{\dfrac{1}{2} \times \dfrac{2}{7}}{\dfrac{1}{2} \times \dfrac{1}{5} + \dfrac{1}{2} \times \dfrac{2}{7}}$

$P(E_2|A) = \dfrac{\dfrac{2}{7}}{\dfrac{1}{5} + \dfrac{2}{7}}$

$P(E_2|A) = \dfrac{\dfrac{2}{7}}{\dfrac{17}{35}} = \dfrac{2}{7} \times \dfrac{35}{17} = \dfrac{10}{17}$

Answer: $\dfrac{10}{17}$

</details>

---

### Q2. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A bag contains 10 balls out of which $k$ are red and ($10-k$) are black, where $0 \leq k \leq 10$. If three balls are drawn at random without replacement and all of them are found to be black, then the probability that the bag contains 1 red and 9 black balls is:

**Options:**

- **(A)** $\frac{14}{55}$
- **(B)** $\frac{7}{55}$
- **(C)** $\frac{7}{110}$
- **(D)** $\frac{7}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{14}{55}$**

**Detailed Solution:**

Using Bayes' theorem:
$P(k=1|\text{all black}) = \frac{P(\text{all black}|k=1) \cdot P(k=1)}{P(\text{all black})}$ where $P(k) = \frac{1}{11}$ for each $k \in \{0,1,...,10\}$. 
 When $k=1$: $P(\text{all 3 black}|k=1) = \frac{\binom{9}{3}}{\binom{10}{3}} = \frac{84}{120} = \frac{7}{10}$. 
 Calculating $P(\text{all black}) = \frac{1}{11}\sum_{k=0}^{10} \frac{\binom{10-k}{3}}{120}$.
Numerator is $120 + 84 + 56 + 35 + 20 + 10 + 4 + 1 = 330$. 
 So $P(\text{all black}) = \frac{1}{11} \cdot \frac{330}{120} = \frac{1}{4}$. 
 Therefore $P(k=1|\text{all black}) = \frac{\frac{7}{10} \cdot \frac{1}{11}}{\frac{1}{4}} = \frac{7}{10} \cdot \frac{4}{11} = \frac{28}{110} = \frac{14}{55}$

</details>

---

### Q3. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Bag $B_1$ contains 6 white and 4 blue balls, Bag $B_2$ contains 4 white and 6 blue balls, and Bag $B_3$ contains 5 white and 5 blue balls. One of the bags is selected at random and a ball is drawn from it. If the ball is white, then the probability, that the ball is drawn from Bag $B_2$, is :

**Options:**

- **(A)** $\frac{4}{15}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{4}{15}$**

**Detailed Solution:**

$E_1: B a g B_1$ is selected
$\begin{array}{lll}
B_1 & B_2 & B_3 \\
\text { 6W4B } & 4 \mathrm{~W} 6 \mathrm{~B} & 5 \mathrm{~W} 5 \mathrm{~B}
\end{array}$


$\mathrm{E}_2:$ bag $\mathrm{B}_2$ is selected
$E_3: B a g B_3$ is selected
A : Drawn ball is white
We have to find $\mathrm{P}\left(\frac{\mathrm{E}_2}{\mathrm{~A}}\right)$


$P\left(\frac{E_2}{A}\right)=\frac{P\left(E_2\right) P\left(\frac{A}{E_2}\right)}{P\left(E_1\right) P\left(\frac{A}{E_1}\right)+P\left(E_2\right) P\left(\frac{A}{E_2}\right)+P\left(E_3\right) P\left(\frac{A}{E_3}\right)}$


$\begin{aligned} & =\frac{\frac{1}{3} \times \frac{4}{10}}{\frac{1}{3} \times \frac{6}{10}+\frac{1}{3} \times \frac{4}{10}+\frac{1}{3} \times \frac{5}{10}} \\ & =\frac{4}{15}\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two balls are selected at random one by one without replacement from a bag containing 4 white and 6 black balls. If the probability that the first selected ball is black, given that the second selected ball is also black, is $\frac{m}{n}$, where $\operatorname{gcd}(m, n)=1$, then $m+n$ is equal to :

**Options:**

- **(A)** $4$
- **(B)** $14$
- **(C)** $13$
- **(D)** $11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $14$**

**Detailed Solution:**

Bag contains 4 white and 6 black balls
$A$ : first ball selected is black
$B$ : Second ball is also black
$\begin{aligned}
& P\left(\frac{A}{B}\right)=\frac{\frac{6}{10} \times \frac{5}{9}}{\frac{4}{10} \times \frac{6}{9}+\frac{6}{10} \times \frac{5}{9}}=\frac{30}{24+30} \\
& =\frac{30}{54}=\frac{5}{9} \\
& m+n=5+9=14
\end{aligned}$

</details>

---

### Q5. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are three bags $X, Y$ and $Z$. Bag $X$ contains 5 one-rupee coins and 4 five-rupee coins; Bag $Y$ contains 4 one-rupee coins and 5 five-rupee coins and Bag Z contains 3 one-rupee coins and 6 five-rupee coins. A bag is selected at random and a coin drawn from it at random is found to be a one-rupee coin. Then the probability, that it came from bag Y, is :

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{5}{12}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/VuO9lgtA2qb4sPeKkGmxF0DCYAHZdwbp8WWn37Hr_ls.original.fullsize.png">

</details>

---

### Q6. JEE Main 2024 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A company has two plants $A$ and $B$ to manufacture motorcycles. $60 \%$ motorcycles are manufactured at plant $A$ and the remaining are manufactured at plant $B .80 \%$ of the motorcycles manufactured at plant $A$ are rated of the standard quality, while $90 \%$ of the motorcycles manufactured at plant $B$ are rated of the standard quality. A motorcycle picked up randomly from the total production is found to be of the standard quality. If $p$ is the probability that it was manufactured at plant $B$, then $126 p$ is

**Options:**

- **(A)** 54
- **(B)** 66
- **(C)** 64
- **(D)** 56

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 54**

**Detailed Solution:**

$\begin{array}{|l|c|c|}
\hline & \text{A} & \text{B} \\
\hline \text{Manufactured} & 60 \% & 40 \% \\
\hline \text{Standard quality} & 80 \% & 90 \% \\
\hline
\end{array}$
$\mathrm{P}$ (Manufactured at $\mathrm{B} /$ found standard quality $)=$ ?
A : Found S.Q
B : Manufacture B
$\mathrm{C}$ : Manufacture A
$\begin{aligned}
& P\left(E_1\right)=\frac{40}{100} \\
& P\left(E_2\right)=\frac{60}{100} \\
& P\left(A / E_1\right)=\frac{90}{100} \\
& P\left(A / E_2\right)=\frac{80}{100} \\
& \because P\left(E_1 / A\right)=\frac{P\left(A / E_1\right) P\left(E_1\right)}{P\left(A / E_1\right) P\left(E_1\right)+P\left(A / E_2\right) P\left(E_2\right)}=\frac{3}{7} \\
& \therefore 126 P=54
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (04 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three urns A, B and C contain 7 red, 5 black; 5 red, 7 black and 6 red, 6 black balls, respectively. One of the urn is selected at random and a ball is drawn from it. If the ball drawn is black, then the probability that it is drawn from urn $\mathrm{A}$ is :

**Options:**

- **(A)** $\frac{5}{18}$
- **(B)** $\frac{5}{16}$
- **(C)** $\frac{4}{17}$
- **(D)** $\frac{7}{18}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{18}$**

**Detailed Solution:**

$\begin{array}{ccc}\text { A } & \text { B } & \text { C } \\ 7 \mathrm{R}, 5 \mathrm{~B} & 5 \mathrm{R}, 7 \mathrm{~B} & 6 \mathrm{R}, 6 \mathrm{~B}\end{array}$
$\begin{aligned} & \mathrm{P}(\mathrm{B})=\frac{1}{3} \cdot \frac{5}{12}+\frac{1}{3} \cdot \frac{7}{12}+\frac{1}{3} \cdot \frac{6}{12} \\ & \text { required probability }=\frac{\frac{1}{3} \cdot \frac{5}{12}}{\frac{1}{3} \cdot\left[\frac{5}{12}+\frac{7}{12}+\frac{6}{12}\right]}=\frac{5}{18}\end{aligned}$

</details>

---

### Q8. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> balls, whose colours are either white or black. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> balls are drawn at random without replacement and it was found that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> balls are white and other <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> balls are black. The probability that the bag contains equal number of white and black balls is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>Total Possible cases of balls in the bag could be:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>W</mi><mo>,</mo><mn>6</mn><mi>B</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mi>W</mi><mo>,</mo><mn>5</mn><mi>B</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mi>W</mi><mo>,</mo><mn>4</mn><mi>B</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>5</mn><mi>W</mi><mo>,</mo><mn>3</mn><mi>B</mi></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>6</mn><mi>W</mi><mo>,</mo><mn>2</mn><mi>B</mi></mrow></mfenced></math></p><p>The favourable case is to choose <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>W</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>B</mi></math> from the bag having <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mi>W</mi><mo>,</mo><mn>4</mn><mi>B</mi></mrow></mfenced></math></p><p>So, the required probability is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle><mrow><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle><mo>+</mo><mstyle displaystyle="true"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>×</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts></mfrac></mstyle></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>6</mn><mo>×</mo><mn>6</mn></mstyle><mstyle displaystyle="true"><mn>15</mn><mo>+</mo><mn>3</mn><mo>×</mo><mn>10</mn><mo>+</mo><mn>36</mn><mo>+</mo><mn>30</mn><mo>+</mo><mn>15</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>36</mn></mstyle><mstyle displaystyle="true"><mn>126</mn></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>2</mn></mstyle><mstyle displaystyle="true"><mn>7</mn></mstyle></mfrac></math></p>

</details>

---

### Q9. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In a bolt factory, machines <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> manufacture respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>%</mo><mo>,</mo><mo>&#160;</mo><mn>30</mn><mo>%</mo></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>%</mo></math> of the total bolts. Of their output <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> percent are respectively defective bolts. A bolt is drawn at random from the product. If the bolt drawn is found the defective then the probability that it is manufactured by the machine <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>14</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>28</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>14</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>&#8801;</mo></math>Event that product is defective, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>100</mn></mfrac><mspace linebreak="newline"/><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>100</mn></mfrac><mspace linebreak="newline"/><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>C</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>100</mn></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>C</mi><mi>X</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mi>C</mi></mfenced><mi>P</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>X</mi><mi>C</mi></mfrac></mstyle></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>A</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>B</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>C</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>X</mi><mi>C</mi></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mfrac><mi>C</mi><mi>X</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>50</mn><mn>100</mn></mfrac></mstyle><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>100</mn></mfrac></mstyle></mrow><mrow><mfrac><mn>20</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>100</mn></mfrac><mo>+</mo><mfrac><mn>30</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>4</mn><mn>100</mn></mfrac><mo>+</mo><mfrac><mn>50</mn><mn>100</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>100</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mfrac><mi>C</mi><mi>X</mi></mfrac></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>100</mn></mstyle><mrow><mn>60</mn><mo>+</mo><mn>120</mn><mo>+</mo><mn>100</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mfrac><mi>C</mi><mi>X</mi></mfrac></mfenced><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>5</mn></mstyle><mn>14</mn></mfrac></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q10. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> balls. Two balls are drawn from it at random and both are found to be black. The probability that the bag contains at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> black balls is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>7</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>7</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>Let the bag contains black balls<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>B</mi></mfenced></math> and non-black balls <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mover><mi>B</mi><mo>&#175;</mo></mover></mfenced></math>, then we can have the following possibilities:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>6</mn><mi>B</mi><mo>,</mo><mn>0</mn><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mi>B</mi><mo>,</mo><mn>1</mn><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mi>B</mi><mo>,</mo><mn>2</mn><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mi>B</mi><mo>,</mo><mn>3</mn><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced><mo>,</mo><mspace linebreak="newline"></mspace><mfenced><mrow><mn>2</mn><mi>B</mi><mo>,</mo><mn>4</mn><mover><mi>B</mi><mo>&#175;</mo></mover></mrow></mfenced></mrow></mfenced></math></p><p>All the events are equally likely, i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math>.</p><p>Required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac></mrow><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#215;</mo><mfrac><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>25</mn><mn>35</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>7</mn></mfrac></math></p>

</details>

---

### Q11. JEE Main 2023 (25 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>%</mo></math> of the population are smokers. A smoker has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math> times more chances to develop lung cancer then a non-smoker. A person is diagnosed with lung cancer and the probability that this person is a smoker is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>10</mn></mfrac></math>.Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Given,</p><p>In a city, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>%</mo></math> of the population is smoker</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mtext>smoker</mtext></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mtext>non-smoking</mtext></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>75</mn></math></p><p>And smoker has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math> times more chance of being diagnosed with lung cancer,</p><p>So, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mtext>Lung&#160;cancer</mtext><mtext>non-smoker</mtext></mfrac></mfenced><mo>=</mo><mi>p</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mtext>Lung&#160;cancer</mtext><mtext>smoker</mtext></mfrac></mfenced><mo>=</mo><mn>27</mn><mi>p</mi></math>,</p><p>Now,  a person is selected at random and found to be diagnosed with lung cancer,</p><p>So, total probability of having a lung cancer will be </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mtext>Lung&#160;cancer</mtext></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#215;</mo><mn>27</mn><mi>p</mi><mo>+</mo><mn>0</mn><mo>.</mo><mn>75</mn><mo>&#215;</mo><mi>p</mi></math></p><p>So the probability of him being smoker (using bayes&#39; theorem) will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mtext>smoker</mtext><mtext>Lung&#160;cancer</mtext></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#215;</mo><mn>27</mn><mi>p</mi></mrow><mrow><mn>0</mn><mo>.</mo><mn>25</mn><mo>&#215;</mo><mn>27</mn><mi>p</mi><mo>+</mo><mn>0</mn><mo>.</mo><mn>75</mn><mo>&#215;</mo><mi>p</mi></mrow></mfrac><mo>=</mo><mfrac><mn>27</mn><mn>30</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>10</mn></mfrac></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>10</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>10</mn></mfrac></math>,</p><p>Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>. </p>

</details>

---

### Q12. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

The urns <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> black; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> black and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> black balls respectively. One of the urns is selected at random and a ball is drawn. If the ball drawn is red and the probability that it is drawn from urn <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4</mn></math>, then the square of length of the side of largest equilateral triangle, inscribed in the parabola <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mi>&#955;</mi><mi>x</mi></math> with one vertex at vertex of parabola is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **432**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> be the event of drawing red balls.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>C</mi></mfrac></mfenced><mo>=</mo><mfrac><mi>&#955;</mi><mrow><mn>4</mn><mo>+</mo><mi>&#955;</mi></mrow></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>C</mi><mi>R</mi></mfrac></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>P</mi><mfenced><mi>C</mi></mfenced><mi>P</mi><mfenced><mstyle displaystyle="true"><mfrac><mi>R</mi><mi>C</mi></mfrac></mstyle></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>A</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>B</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>C</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>R</mi><mi>C</mi></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle><mo>&#215;</mo><mfenced><mstyle displaystyle="true"><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mstyle></mfenced></mrow><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>10</mn></mfrac></mstyle><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced></mstyle><mstyle displaystyle="true"><mfrac><mn>9</mn><mn>10</mn></mfrac><mo>+</mo><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced></mstyle></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>10</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>9</mn><mn>10</mn></mfrac><mo>+</mo><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mi>&#955;</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mn>9</mn><mn>10</mn></mfrac><mo>+</mo><mfenced><mfrac><mi>&#955;</mi><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mi>&#955;</mi></mrow><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>19</mn><mi>&#955;</mi><mo>+</mo><mn>36</mn></mrow><mrow><mn>5</mn><mfenced><mrow><mi>&#955;</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><mi>&#955;</mi><mo>=</mo><mn>19</mn><mi>&#955;</mi><mo>+</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>&#955;</mi><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>6</mn></math></p><p>So, parabola is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn><mi>x</mi><mo>=</mo><mn>4</mn><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mi>x</mi></math></p><p>Comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mi>a</mi><mi>x</mi></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Hence, we have</p><p><img alt="" src="https://cdn-question-pool.getmarks.app/pyq/jee_main/5a9ec8fa-b8a8-4d6c-82a8-c887ddb0d47e-9885007.png" style="width: 350px; height: 224px;" /></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>&#8801;</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>t</mi><mn>2</mn></msup><mo>,</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mi>t</mi></mrow></mfenced></math></p><p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8710;</mo><mi>O</mi><mi>P</mi><mi>Q</mi></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>tan</mi><mfenced><mrow><mn>30</mn><mo>&#176;</mo></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>a</mi><mi>t</mi></mrow><mrow><mi>a</mi><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mi>t</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mi>t</mi></mfrac><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>2</mn><msqrt><mn>3</mn></msqrt></math></p><p>Side length of triangle<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mi>a</mi><mi>t</mi><mo>=</mo><mn>12</mn><msqrt><mn>3</mn></msqrt></math></p><p>Square of side of triangle</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>12</mn><msqrt><mn>3</mn></msqrt></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>432</mn></math> units</p>

</details>

---

### Q13. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> black and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> white balls and Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> red, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> black and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> white balls. One ball is transferred from Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">I</mi></math> to Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> and then a ball is draw from Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math>. The ball so drawn is found to be black in colour. Then the probability, that the transferred ball is red, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>18</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>10</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>18</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>In bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8594;</mo><mn>3</mn><mi>R</mi><mo>,</mo><mo>&#160;</mo><mn>4</mn><mi>B</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>3</mn><mi>W</mi></math></p><p>And in bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#8594;</mo><mn>2</mn><mi>R</mi><mo>,</mo><mo>&#160;</mo><mn>5</mn><mi>B</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2</mn><mi>W</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>:</mo></math> Drawn ball from bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>II</mi></math> is black</p><p>And let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>:</mo></math> Red ball transferred</p><p>Now by total probability theorem we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>6</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac><mo>=</mo><mfrac><mn>54</mn><mn>90</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac></math></p><p>So, by bayes theorem we have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>B</mi><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac></mrow><mrow><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>6</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>9</mn></mfrac><mo>&#215;</mo><mfrac><mn>5</mn><mn>10</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>15</mn><mrow><mn>15</mn><mo>+</mo><mn>24</mn><mo>+</mo><mn>15</mn></mrow></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>54</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>18</mn></mfrac></math></p></blockquote>

</details>

---

### Q14. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> black and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> red balls and bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> black, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> red and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> white balls. One bag is chosen at random and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> balls drawn from it at random are found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> red and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> black. If the probability that both balls come from Bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>11</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to _____

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> event denotes the selection for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mi>st</mi></msup></math> bag</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> event denotes the selection for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>nd</mi></msup></math> bag</p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Let the event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo></math> selected balls are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> red &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> black</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>2</mn></msub></mfrac></mfenced><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts></mrow><msub><mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><msub><mi>C</mi><mn>2</mn></msub></msub></mfrac><mo>=</mo><mfrac><mn>12</mn><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mrow><mo>&#160;</mo><mi>A</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>1</mn></msub></mfrac></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>1</mn></msub></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>2</mn></msub></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>5</mn></mfrac></mstyle></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>11</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q15. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

An electric instrument consists of two units. Each unit must function independently for the instrument to operate. The probability that the first unit functions is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>9</mn></math> and that of the second unit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>8</mn><mo>.</mo></math> The instrument is switched on and it fails to operate. If the probability that only the first unit failed and second unit is functioning is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>98</mn><mi>p</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **28**

**Detailed Solution:**

<p>Given that</p><p>An electric instrument consists of two units. Each unit must function independently for the instrument to operate. The probability that the first unit functions is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>9</mn></math> and that of the second unit is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>8</mn><mo>.</mo></math> The instrument is switched on and it fails to operate. If the probability that only the first unit failed and second unit is functioning is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>.</mo></math> </p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>=</mo></math> Event of first unit is working </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>=</mo></math> Event of second unit is working</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>9</mn><mo>&#160;&#160;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>8</mn></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><menclose notation="top"><mi>E</mi></menclose></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mover><mi>E</mi><mo>&#175;</mo></mover><mn>1</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#160;&#160;</mo><mi>P</mi><mfenced><msub><mover><mi>E</mi><mo>&#175;</mo></mover><mn>2</mn></msub></mfenced><mo>=</mo><mn>0</mn><mo>.</mo><mn>2</mn></math></p><p>By using Baye&#39;s theorem</p><p>Required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><menclose notation="top"><msub><mi>E</mi><mn>1</mn></msub></menclose></mfenced></mrow><mrow><mi>P</mi><mfenced><menclose notation="top"><msub><mi>E</mi><mn>2</mn></msub></menclose></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><menclose notation="top"><msub><mi>E</mi><mn>1</mn></msub></menclose></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><menclose notation="top"><msub><mi>E</mi><mn>2</mn></msub></menclose></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>&#215;</mo><mi>P</mi><mfenced><menclose notation="top"><msub><mi>E</mi><mn>1</mn></msub></menclose></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mrow><mn>0</mn><mo>.</mo><mn>8</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>1</mn></mrow><mrow><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>+</mo><mn>0</mn><mo>.</mo><mn>9</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>2</mn><mo>+</mo><mn>0</mn><mo>.</mo><mn>1</mn><mo>&#215;</mo><mn>0</mn><mo>.</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mfrac><mfenced><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>100</mn></mfrac></mstyle></mfenced><mstyle displaystyle="true"><mfrac><mfenced><mrow><mn>2</mn><mo>&#160;</mo><mo>+</mo><mn>18</mn><mo>&#160;</mo><mo>+</mo><mn>8</mn></mrow></mfenced><mn>100</mn></mfrac></mstyle></mfrac><mo>=</mo><mo>&#160;</mo><mfrac><mn>8</mn><mn>28</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>98</mn><mi>P</mi><mo>=</mo><mn>98</mn><mo>&#215;</mo><mfrac><mn>8</mn><mn>28</mn></mfrac><mo>=</mo><mn>28</mn></math></p>

</details>

---

### Q16. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A pack of cards has one card missing. Two cards are drawn randomly and are found to be spades. The probability that the missing card is not a spade, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mn>867</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>50</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>22</mn><mn>425</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>50</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub></math> : Event denotes spade is missing </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>;</mo><mi>P</mi><mfenced><msub><mover><mi>E</mi><mo>&#175;</mo></mover><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> : Event drawn two cards are spade </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><msub><mi>E</mi><mn>1</mn></msub></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>12</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts></mfrac></mfenced><mo>,</mo><mo>&#160;</mo><mi>P</mi><mfenced><mfrac><mi>A</mi><mover><msub><mi>E</mi><mn>1</mn></msub><mo>&#175;</mo></mover></mfrac></mfenced><mo>=</mo><mfenced><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>13</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none/><mprescripts/><none/><mn>51</mn></mmultiscripts></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfenced><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts></mfrac></mfenced></mrow><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfenced><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts></mfrac></mfenced><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfenced><mfrac><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>51</mn></mmultiscripts></mfrac></mfenced></mrow></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>39</mn><mn>50</mn></mfrac></math></p>

</details>

---

### Q17. JEE Main 2021 (25 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a group of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math> people, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>160</mn></math> are smokers and non-vegetarian; <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> are smokers and vegetarian and the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn></math> are non-smokers and vegetarian. Their chances of getting a particular chest disorder are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn><mo>%</mo><mo>,</mo><mn>20</mn><mo>%</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>%</mo></math> respectively. A person is chosen from the group at random and is found to be suffering from the chest disorder. The probability that the selected person is a smoker and non-vegetarian is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>45</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>45</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>45</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>28</mn><mn>45</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>28</mn><mn>45</mn></mfrac></math>**

**Detailed Solution:**

<p>Consider following events
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> : Person chosen is a smoker and non
vegetarian.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> : Person chosen is a smoker and vegetarian.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> : Person chosen is a non-smoker and vegetarian</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> : Person chosen has a chest disorder</p><p>Given</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>160</mn><mn>400</mn></mfrac><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>100</mn><mn>400</mn></mfrac><mi>P</mi><mfenced><mi>C</mi></mfenced><mo>=</mo><mfrac><mn>140</mn><mn>400</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>A</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>35</mn><mn>100</mn></mfrac><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>20</mn><mn>100</mn></mfrac><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>C</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>10</mn><mn>100</mn></mfrac></math></p><p>To find</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>A</mi></mfrac></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>A</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>B</mi></mfrac></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>C</mi></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mfrac><mi>E</mi><mi>C</mi></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>160</mn><mn>400</mn></mfrac><mo>&#215;</mo><mfrac><mn>35</mn><mn>100</mn></mfrac></mrow><mrow><mfrac><mn>160</mn><mn>400</mn></mfrac><mo>&#215;</mo><mfrac><mn>35</mn><mn>100</mn></mfrac><mo>+</mo><mfrac><mn>100</mn><mn>400</mn></mfrac><mo>&#215;</mo><mfrac><mn>20</mn><mn>100</mn></mfrac><mo>+</mo><mfrac><mn>140</mn><mn>400</mn></mfrac><mo>&#215;</mo><mfrac><mn>10</mn><mn>100</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>28</mn><mn>45</mn></mfrac></math></p><p>option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced></math></p>

</details>

---

### Q18. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Two different families <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are blessed with equal number of children. There are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> tickets to be distributed amongst the children of these families so that no child gets more than one ticket. If the probability that all the tickets go to the children of the family <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>,</mo></math> then the number of children in each family is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> number of children be there in each family.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mn>3</mn></msub><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow><mrow><msup><mi>&#160;</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><msub><mi>C</mi><mn>3</mn></msub><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mn>3</mn></msub></mrow><mrow><msup><mi>&#160;</mi><mrow><mn>2</mn><mi>n</mi></mrow></msup><msub><mi>C</mi><mn>3</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mi>n</mi><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p></blockquote>

</details>

---

### Q19. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A box <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> red and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> black balls. Another box <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> red and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> black balls. If two balls are drawn at random, without replacement from a randomly, selected box and one ball turns out to be white while the other ball turns out to be red, then the probability that both balls are drawn from box <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mrow><mn>8</mn><mi>&#160;</mi></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>16</mn><mi> </mi></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mrow><mn>16</mn><mi>&#160;</mi></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>32</mn><mi> </mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mrow><mn>16</mn><mi>&#160;</mi></mrow></mfrac></math>**

**Detailed Solution:**

<p>Probability that box <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Probability that box <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is selected <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>&#160;</mi></mrow></mfrac></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> be the event that one ball is white while the other is red.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>A</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mfrac><mrow><mn>2</mn><mo>&#183;</mo><mn>3</mn></mrow><mrow><msup><mrow/><mn>7</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>&#183;</mo><mn>2</mn></mrow><mrow><msup><mrow/><mn>9</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mfrac><mn>6</mn><mn>21</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>36</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>16</mn><mn>63</mn></mfrac></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>B</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>/</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>E</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>16</mn><mn>63</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>16</mn></mfrac></math></p>

</details>

---

### Q20. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `2`

A box ' $A$ ' contanis 2 white, 3 red and 2 black balls. Another box ' $B^{\prime}$ contains 4 white, 2 red and 3 black balls. If two balls are drawn at random, without replacement, from a randomly selected box and one ball turns out to be white while the other ball turns out to be red, then the probability that both balls are drawn from box ' $B^{\prime}$ is

**Options:**

- **(A)** $\frac{7}{16}$
- **(B)** $\frac{9}{32}$
- **(C)** $\frac{7}{8}$
- **(D)** $\frac{9}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{7}{16}$**

**Detailed Solution:**

Probability of drawing a white ball and then a red ball from bag $B$ is given by
$$
\frac{{ }^4 C_1 \times{ }^2 C_1}{{ }^9 C_2}=\frac{2}{9}
$$
Probability of drawing a white ball and then a red ball from bag $A$ is given by
$$
\frac{{ }^2 C_1 \times{ }^3 C_1}{{ }^7 C_2}=\frac{2}{7}
$$
Hence, the probability of drawing a white ball and then a red ball from bag $B$
$$
=\frac{\frac{2}{9}}{\frac{2}{7}+\frac{2}{9}}=\frac{2 \times 7}{18+14}=\frac{7}{16}
$$

</details>

---

