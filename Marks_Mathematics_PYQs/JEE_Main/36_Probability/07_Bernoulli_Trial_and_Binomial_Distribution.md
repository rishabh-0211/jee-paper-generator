# JEE Main Mathematics - Probability

## Topic 7: Bernoulli Trial and Binomial Distribution

**Total Questions:** 26

---

### Q1. JEE Main 2026 (04 April Shift 1)

*Type:* `numerical` | *Level:* `2`

A coin is tossed $8$ times. If the probability that exactly $4$ heads appear in the first six tosses and exactly $3$ heads appear in the last five tosses is $p$, then $96p$ is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Let the outcomes of the $8$ tosses be denoted by $X_1, X_2, X_3, X_4, X_5, X_6, X_7, X_8$.

Let $A$ be the number of heads in the first $3$ tosses ($X_1, X_2, X_3$).
Let $B$ be the number of heads in the next $3$ tosses ($X_4, X_5, X_6$).
Let $C$ be the number of heads in the last $2$ tosses ($X_7, X_8$).

According to the given conditions:
Number of heads in the first six tosses: $A + B = 4$
Number of heads in the last five tosses: $B + C = 3$

Since $C$ is the number of heads in $2$ tosses, $C \le 2$. Thus, $B = 3 - C \ge 1$. Also, $B \le 3$.
The possible values for $B$ are $1, 2, 3$. We analyze each case:

Case 1: $B = 1$
Then $C = 2$ and $A = 3$.
Number of ways = $^{3}C_{3} \times ^{3}C_{1} \times ^{2}C_{2} = 1 \times 3 \times 1 = 3$

Case 2: $B = 2$
Then $C = 1$ and $A = 2$.
Number of ways = $^{3}C_{2} \times ^{3}C_{2} \times ^{2}C_{1} = 3 \times 3 \times 2 = 18$

Case 3: $B = 3$
Then $C = 0$ and $A = 1$.
Number of ways = $^{3}C_{1} \times ^{3}C_{3} \times ^{2}C_{0} = 3 \times 1 \times 1 = 3$

Total number of favorable outcomes = $3 + 18 + 3 = 24$
Total number of possible outcomes for $8$ coin tosses = $2^8 = 256$

The probability $p$ is given by:
$p = \dfrac{24}{256} = \dfrac{3}{32}$

We need to find the value of $96p$:
$96p = 96 \times \dfrac{3}{32} = 3 \times 3 = 9$

Answer: $9$

</details>

---

### Q2. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A man throws a fair coin repeatedly. He gets $10$ points for each head he throws and $5$ points for each tail he throws. If the probability that he gets exactly $30$ points is $\dfrac{m}{n}$, $\gcd(m, n) = 1$, then $m + n$ is equal to:

**Options:**

- **(A)** $53$
- **(B)** $55$
- **(C)** $107$
- **(D)** $105$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $107$**

**Detailed Solution:**

Let $h$ be the number of heads and $t$ be the number of tails obtained.

The total points obtained is $10h + 5t$.

For the man to get exactly $30$ points, we must have:

$10h + 5t = 30 \Rightarrow 2h + t = 6$

Since $h$ and $t$ are non-negative integers, the possible pairs of $(h, t)$ are $(3, 0)$, $(2, 2)$, $(1, 4)$, and $(0, 6)$.

For each pair, the number of possible sequences of heads and tails is given by $^{h+t}C_{h}$, and the probability of any specific sequence is $\left(\dfrac{1}{2}\right)^{h+t}$.

The total probability is the sum of the probabilities of all these mutually exclusive cases:

For $h = 3, t = 0$, the probability is $^{3}C_{3} \left(\dfrac{1}{2}\right)^{3} = 1 \times \dfrac{1}{8} = \dfrac{8}{64}$.

For $h = 2, t = 2$, the probability is $^{4}C_{2} \left(\dfrac{1}{2}\right)^{4} = 6 \times \dfrac{1}{16} = \dfrac{24}{64}$.

For $h = 1, t = 4$, the probability is $^{5}C_{1} \left(\dfrac{1}{2}\right)^{5} = 5 \times \dfrac{1}{32} = \dfrac{10}{64}$.

For $h = 0, t = 6$, the probability is $^{6}C_{0} \left(\dfrac{1}{2}\right)^{6} = 1 \times \dfrac{1}{64} = \dfrac{1}{64}$.

Total probability $= \dfrac{8}{64} + \dfrac{24}{64} + \dfrac{10}{64} + \dfrac{1}{64} = \dfrac{43}{64}$.

Thus, $m = 43$ and $n = 64$.

Since $\gcd(43, 64) = 1$, the fraction is in its simplest form.

$m + n = 43 + 64 = 107$.

Answer: $107$

</details>

---

### Q3. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

From a lot containing 10 defective and 90 non-defective bulbs, 8 bulbs are selected one by one with replacement. Then the probability of getting at least 7 defective bulbs is

**Options:**

- **(A)** $\frac{67}{10^{8}}$
- **(B)** $\frac{7}{10^{7}}$
- **(C)** $\frac{81}{10^{8}}$
- **(D)** $\frac{73}{10^{8}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{73}{10^{8}}$**

**Detailed Solution:**

Binomial distribution with $n=8$, $p=\frac{1}{10}$, $q=\frac{9}{10}$.
$P(X \ge 7) = P(X=7) + P(X=8)$
$P(X=7) = \binom{8}{7}\left(\frac{1}{10}\right)^7\left(\frac{9}{10}\right) = \frac{72}{10^8}$
$P(X=8) = \left(\frac{1}{10}\right)^8 = \frac{1}{10^8}$
$P(X \ge 7) = \frac{73}{10^8}$

</details>

---

### Q4. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a die be rolled <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> times. Let the probability of getting odd numbers seven times be equal to the probability of getting odd numbers nine times. If the probability of getting even numbers twice is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><msup><mn>2</mn><mn>15</mn></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(getting odd <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> times) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi></math>(getting odd <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> times).</p><p>This is the case of binomial distribution with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> successes and probability of success <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>p</mi><mo>=</mo><mfrac><mn>3</mn><mn>6</mn></mfrac></math> and failure is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>.</p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mi>p</mi></mfenced><mi>k</mi></msup><msup><mfenced><mi>q</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mi>k</mi></mrow></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>9</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>7</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>9</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>9</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mn>2</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo><mi>even</mi><mo>&#160;</mo><mo>)</mo><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>14</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>4</mn></mrow><msup><mn>2</mn><mn>15</mn></msup></mfrac><mo>=</mo><mfrac><mn>60</mn><msup><mn>2</mn><mn>15</mn></msup></mfrac><mo>=</mo><mfrac><mi>k</mi><msup><mn>2</mn><mn>15</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>60</mn></math></p><p>Hence this is the required option.</p></blockquote>

</details>

---

### Q5. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>A pair of dice is thrown <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> times. For each throw, a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> is considered a success. If the probability of at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> successes is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><msup><mn>3</mn><mn>11</mn></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>82</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>164</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>123</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>123</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that,</p><p>A pair of dice is thrown <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> times.</p><p>Required Sample space is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mn>6</mn></mrow></mfenced></mrow></mfenced></math></p><p>Total number of observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn></math></p><p>Now, a sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> is observed in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p>No of favourable outcomes <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(success) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>4</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(failure) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>9</mn></mfrac></math></p><p>We know that for a binomial distribution, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mi>n</mi><mo>,</mo><mi>p</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mi>k</mi></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mi>k</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>p</mi><mi>k</mi></msup><msup><mi>q</mi><mrow><mi>n</mi><mo>-</mo><mi>k</mi></mrow></msup></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8805;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math>Required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#8805;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>9</mn></mfrac></mfenced><mn>4</mn></msup><mfrac><mn>8</mn><mn>9</mn></mfrac><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>9</mn></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>&#183;</mo><mfrac><mn>8</mn><msup><mn>9</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>9</mn><mn>5</mn></msup></mfrac><mo>=</mo><mfrac><mn>41</mn><msup><mn>9</mn><mn>5</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>41</mn><mo>&#215;</mo><mn>3</mn></mrow><mrow><msup><mn>3</mn><mn>10</mn></msup><mo>&#215;</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mn>123</mn><msup><mn>3</mn><mn>11</mn></msup></mfrac></math></p><p>But given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#8805;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mfrac><mi>k</mi><msup><mn>3</mn><mn>11</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>k</mi><msup><mn>3</mn><mn>11</mn></msup></mfrac><mo>=</mo><mfrac><mn>123</mn><msup><mn>3</mn><mn>11</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>123</mn></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q6. JEE Main 2022 (29 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

The sum and product of the mean and variance of a binomial distribution are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>82</mn><mo>.</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1350</mn></math> respectively. They the number of trials in the binomial distribution is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **96**

**Detailed Solution:**

<blockquote><p>Given, sum of mean and variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>82</mn><mo>.</mo><mn>5</mn></math></p><p>Product of roots is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1350</mn></math></p><p>Now, Mean and variance are the roots of </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfenced><mtext>sum&#160;of&#160;roots</mtext></mfenced><mi>x</mi><mo>+</mo><mtext>product&#160;of&#160;roots</mtext><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>82</mn><mo>.</mo><mn>5</mn><mi>x</mi><mo>+</mo><mn>1350</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>60</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>22</mn><mo>.</mo><mn>5</mn></math></p><p>So, mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mo>=</mo><mn>60</mn></math> and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>22</mn><mo>.</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>22</mn><mo>.</mo><mn>5</mn></mrow><mn>60</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mfrac><mn>60</mn><mfrac><mn>5</mn><mn>8</mn></mfrac></mfrac><mo>=</mo><mn>96</mn></math></p></blockquote>

</details>

---

### Q7. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> have a binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mi>n</mi><mo>,</mo><mi>p</mi></mrow></mfenced></math> such that the sum and the product of the mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>128</mn></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#62;</mo><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mi>k</mi><msup><mn>2</mn><mi>n</mi></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>528</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>529</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>629</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>630</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>529</mn></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo></math>Mean and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo></math>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>M</mi><mo>&#62;</mo><mi>V</mi></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>+</mo><mi>V</mi><mo>=</mo><mn>24</mn><mo>,</mo><mo>&#160;</mo><mi>M</mi><mi>V</mi><mo>=</mo><mn>128</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>M</mi><mo>=</mo><mn>16</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi><mo>=</mo><mn>8</mn></math></p><p>Now, mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>=</mo><mn>16</mn></math></p><p>and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>n</mi><mo>=</mo><mn>32</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#62;</mo><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mfenced><mrow><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mi>k</mi><msup><mn>2</mn><mi>n</mi></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac><mfenced><mrow><mmultiscripts><mi>C</mi><mn>30</mn><none/><mprescripts/><none/><mn>32</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>31</mn><none/><mprescripts/><none/><mn>32</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>32</mn><none/><mprescripts/><none/><mn>32</mn></mmultiscripts></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>32</mn><mo>&#215;</mo><mn>31</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>32</mn><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>496</mn><mo>+</mo><mn>33</mn><mo>=</mo><mn>529</mn></math></p></blockquote>

</details>

---

### Q8. JEE Main 2022 (26 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a binomially distributed random variable with mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>3</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>73</mn><mn>27</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>146</mn><mn>27</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>146</mn><mn>81</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>126</mn><mn>81</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>146</mn><mn>27</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>=</mo><mn>4</mn></math></p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn><mi>P</mi><mfenced><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>54</mn><mfenced open="[" close="]"><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>54</mn><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>4</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>1</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>5</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>0</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>54</mn><mfenced><mrow><mn>15</mn><mo>&#215;</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>+</mo><mn>6</mn><mo>&#215;</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><msup><mn>3</mn><mn>3</mn></msup><mfenced><mfrac><mn>73</mn><msup><mn>3</mn><mn>6</mn></msup></mfrac></mfenced><mo>=</mo><mfrac><mn>146</mn><mn>27</mn></mfrac></math></p></blockquote>

</details>

---

### Q9. JEE Main 2022 (26 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean and variance of a binomial distribution are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mn>3</mn></mfrac></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>243</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>4</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mn>5</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>64</mn><mn>81</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>27</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>145</mn><mn>243</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>27</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>=</mo><mi>&#945;</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mfrac><mi>&#945;</mi><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>243</mn></mfrac></math>  </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>q</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><msup><mi>p</mi><mn>1</mn></msup><mo>=</mo><mfrac><mn>4</mn><mn>243</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>n</mi><msup><mn>3</mn><mi>n</mi></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>243</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>6</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>5</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>27</mn></mfrac></math></p></blockquote>

</details>

---

### Q10. JEE Main 2022 (25 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum and the product of mean and variance of a binomial distribution are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>128</mn></math> respectively, then the probability of one or two successes is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><msup><mn>2</mn><mn>32</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><msup><mn>2</mn><mn>29</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><msup><mn>2</mn><mn>28</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><msup><mn>2</mn><mn>27</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><msup><mn>2</mn><mn>28</mn></msup></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo></math>probability of success and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo></math>probability of failure, </p><p>Now given,</p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>+</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>24</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mtext>i</mtext></mfenced></math></p><p>Product <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>&#215;</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>128</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mtext>ii</mtext></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>q</mi></math> ....<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtext>iii</mtext></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtext>i</mtext></mfenced></math> , <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtext>ii</mtext></mfenced></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mtext>iii</mtext></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>n</mi><mo>=</mo><mn>32</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>32</mn></mmultiscripts><mi>p</mi><msup><mi>q</mi><mn>31</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>32</mn></mmultiscripts><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>30</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>33</mn><msup><mn>2</mn><mn>28</mn></msup></mfrac></math></p></blockquote>

</details>

---

### Q11. JEE Main 2022 (27 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a random variable having binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>7</mn><mo>,</mo><mi>p</mi></mrow></mfenced></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>4</mn></mrow></mfenced></math>, then the sum of the mean and the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>105</mn><mn>16</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>77</mn><mn>36</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>36</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>35</mn><mn>36</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>77</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<p>Let probability of success is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and failure is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>
Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>7</mn></math>,</p><p>also , <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mo>&#160;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>4</mn></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mi>p</mi><mn>3</mn></msup><msup><mi>q</mi><mn>4</mn></msup><mo>=</mo><mn>5</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mi>p</mi><mn>4</mn></msup><msup><mi>q</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mn>5</mn><mi>p</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mn>6</mn><mi>p</mi><mo>=</mo><mn>1</mn></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mo>=</mo><mn>7</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac></math></p><p>and Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>7</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#183;</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>35</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Sum of mean and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>7</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>35</mn><mn>36</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>77</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q12. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let a biased coin be tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> times. If the probability of getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> heads is equal to the probability of getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> heads, then the probability of getting atmost two heads is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>275</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>41</mn><msup><mn>5</mn><mn>5</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>36</mn><msup><mn>5</mn><mn>4</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>46</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mn>4</mn><mo>&#160;</mo><mi>heads</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mn>5</mn><mo>&#160;</mo><mi>heads</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>5</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mi>p</mi><mn>4</mn></msup><mi>q</mi><mo>=</mo><msup><mo>&#160;</mo><mn>5</mn></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mi>p</mi><mn>5</mn></msup><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mn>5</mn><mi>q</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>,</mo><mi>p</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>)</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> (at most <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> heads) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>q</mi><mn>5</mn></msup><msup><mo>+</mo><mn>5</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mi>p</mi><msup><mi>q</mi><mn>4</mn></msup><msup><mo>+</mo><mn>5</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup><mo>+</mo><mn>5</mn><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><msup><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced><mn>4</mn></msup><mo>+</mo><mn>10</mn><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>46</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac></math></p>

</details>

---

### Q13. JEE Main 2022 (24 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If a random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> follows the Binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mfenced><mrow><mn>33</mn><mo>,</mo><mi>p</mi></mrow></mfenced></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>15</mn></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>18</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>16</mn></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>17</mn></mrow></mfenced></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1320</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1088</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1088</mn><mn>1089</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><mn>1331</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1320</mn></math>**

**Detailed Solution:**

<p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo></math>success, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo></math>failure</p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>33</mn></mmultiscripts></mfenced><mfenced><msup><mi>p</mi><mn>0</mn></msup></mfenced><mfenced><msup><mi>q</mi><mn>33</mn></msup></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>33</mn></mmultiscripts><mfenced><msup><mi>p</mi><mn>1</mn></msup></mfenced><mfenced><msup><mi>q</mi><mn>32</mn></msup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mi>q</mi><mo>=</mo><mn>33</mn><mo>&#215;</mo><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mn>11</mn><mi>p</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>+</mo><mn>11</mn><mi>p</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mi>p</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mfrac><mn>11</mn><mn>12</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>15</mn></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>18</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>16</mn></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>17</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>33</mn></mmultiscripts><msup><mi>p</mi><mn>15</mn></msup><msup><mi>q</mi><mn>18</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>18</mn><none></none><mprescripts></mprescripts><none></none><mn>33</mn></mmultiscripts><msup><mi>p</mi><mn>18</mn></msup><msup><mi>q</mi><mn>15</mn></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>16</mn><none></none><mprescripts></mprescripts><none></none><mn>33</mn></mmultiscripts><msup><mi>p</mi><mn>16</mn></msup><msup><mi>q</mi><mn>17</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>17</mn><none></none><mprescripts></mprescripts><none></none><mn>33</mn></mmultiscripts><msup><mi>p</mi><mn>17</mn></msup><msup><mi>q</mi><mn>16</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>q</mi><mn>3</mn></msup><msup><mi>p</mi><mn>3</mn></msup></mfrac><mo>-</mo><mfrac><mi>q</mi><mi>p</mi></mfrac><mo>=</mo><mfrac><mi>q</mi><mi>p</mi></mfrac><mfenced><mrow><msup><mfenced><mfrac><mi>q</mi><mi>p</mi></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mn>11</mn><mn>1</mn></mfrac><mfenced><mrow><msup><mn>11</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#215;</mo><mn>120</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1320</mn></math></p>

</details>

---

### Q14. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Each of the persons <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> independently tosses three fair coins. The probability that both of them get the same number of heads is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>16</mn></mfrac></math>**

**Detailed Solution:**

<p>Each of the persons A and B independently tosses three fair coins. </p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the number of heads obtained by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> be the number of heads obtained by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>.</p><p>Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> are binomial variate with parameters, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Probability that both <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> obtain the same number of heads</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><mi>Y</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><mi>Y</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><mi>Y</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><mi>Y</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>&#215;</mo><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mn>3</mn><mo>&#215;</mo><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mn>3</mn><mo>&#215;</mo><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>&#215;</mo><mo>&#160;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>6</mn></msup><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>20</mn><mn>64</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac></math></p>

</details>

---

### Q15. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let in a Binomial distribution, consisting of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> independent trials, probabilities of exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> successes be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>4096</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>2048</mn></math>  respectively. Then the probability of getting exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> successes is equal to :<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>625</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>243</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>243</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>128</mn><mn>625</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>32</mn><mn>625</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#183;</mo><mi>p</mi><mo>.</mo><msup><mi>q</mi><mn>4</mn></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>4096</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#183;</mo><msup><mi>p</mi><mn>2</mn></msup><mo>&#183;</mo><msup><mi>q</mi><mn>3</mn></msup><mo>=</mo><mn>0</mn><mo>.</mo><mn>2048</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>q</mi><mrow><mn>2</mn><mi>p</mi></mrow></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mn>4</mn><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p>Now</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>5</mn></mfrac></mfenced><mn>3</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>125</mn><mo>&#215;</mo><mn>25</mn></mrow></mfrac><mo>=</mo><mfrac><mn>32</mn><mn>625</mn></mfrac></math></p>

</details>

---

### Q16. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A fair coin is tossed a fixed number of times. If the probability of getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> heads is equal to probability of getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> heads, then the probability of getting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> heads is<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><msup><mn>2</mn><mn>14</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><msup><mn>2</mn><mn>12</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><msup><mn>2</mn><mn>8</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math>**

**Detailed Solution:**

Let the coin be tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-times<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>H</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>T</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> heads)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>7</mn></msup><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>2</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> heads)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>9</mn></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>9</mn></msup><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>2</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> heads)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>heads)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> heads)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>14</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>8</mn></mrow><msup><mn>2</mn><mn>16</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> heads)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>15</mn><msup><mn>2</mn><mn>13</mn></msup></mfrac></math></p>

</details>

---

### Q17. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For an initial screening of an admission test, a candidate is given fifty problems to solve. If the probability that the candidate can solve any problem is <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo></math> then the probability that he is unable to solve less than two problems is

**Options:**

- **(A)** <math><mfrac><mrow><mn>201</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>49</mn></mrow></msup></math>
- **(B)** <math><mfrac><mrow><mn>164</mn></mrow><mrow><mn>25</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>48</mn></mrow></msup></math>
- **(C)** <math><mfrac><mrow><mn>316</mn></mrow><mrow><mn>25</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>48</mn></mrow></msup></math>
- **(D)** <math><mfrac><mrow><mn>54</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>49</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>54</mn></mrow><mrow><mn>5</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>49</mn></mrow></msup></math>**

**Detailed Solution:**

Let, <math><mi>X</mi><mo>=</mo></math>The number of questions, student are unable to solve.
<math><mi>p</mi><mo>=</mo><mi>P</mi><mi>&#160;</mi></math> (the student answers a question correctly) <math><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><mi>&#160;</mi><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math> (probability that the student does not answer a question correctly)
Also, <math><mi>n</mi><mo>=</mo><mn>50</mn></math> (Total number of question)
Hence, required probability:
<math><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#60;</mo><mn>2</mn><mo>)</mo></math>
<math><mi>&#160;</mi><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#160;</mi><mn>50</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mi>&#160;</mi><msup><mfenced separators="|"><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mn>50</mn></msup><mo>+</mo><msup><mi>&#160;</mi><mn>50</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mfenced separators="|"><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mn>49</mn></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>5</mn></mfrac></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>54</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi mathvariant="normal">&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>49</mn></mrow></msup></math>

</details>

---

### Q18. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let a random variable <math><mi>X</mi></math> has a binomial distribution with mean <math><mn>8</mn></math> and variance 4. If <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>≤</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>16</mn></mrow></msup></mrow></mfrac><mo>,</mo></math> then the value of <math><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><mn>121</mn></math>
- **(B)** <math><mn>1</mn></math>
- **(C)** <math><mn>17</mn></math>
- **(D)** <math><mn>137</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>137</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be the number of times the experiment is done, <math><mi>p</mi></math> is the probability of the success and <math><mi>q</mi></math> is the probability of the failure.</p><p><math><mo>&#8756;</mo></math> <math><mi>n</mi><mi>p</mi><mo>=</mo><mn>8</mn></math> (mean), <math><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>4</mn></math> (variance)</p><p><math><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8658;</mo><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>p</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>p</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>p</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced><msup><mo>=</mo><mn>16</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mi>p</mi><mn>0</mn></msup><msup><mi>q</mi><mn>16</mn></msup><msup><mo>+</mo><mn>16</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mi>p</mi><mn>1</mn></msup><msup><mi>q</mi><mn>15</mn></msup><msup><mo>+</mo><mn>16</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mn>14</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>16</mn></msup><mo>+</mo><mn>16</mn><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>16</mn></msup><mo>+</mo><mn>120</mn><mo>&#215;</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>16</mn></msup><mfenced separators="|"><mn>137</mn></mfenced><mo>=</mo><mfrac><mn>137</mn><msup><mn>2</mn><mn>16</mn></msup></mfrac><mo>=</mo><mfrac><mi>k</mi><msup><mn>2</mn><mn>16</mn></msup></mfrac></math></p><p><math><mo>&#8756;</mo><mtext>&#8201;</mtext><mi>k</mi><mo>=</mo><mn>137</mn></math></p>

</details>

---

### Q19. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

An unbiased coin is tossed eight times. The probability of obtaining at least one head and at least one tail is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>127</mn></mrow><mrow><mn>128</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>63</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>255</mn></mrow><mrow><mn>256</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>127</mn></mrow><mrow><mn>128</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Probability of at least one head and at least one tail can be calculated as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>1</mn><mo>-{</mo><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">H</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">d</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">A</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">T</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">l</mi></mrow></mfenced><mo>}</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfenced open="{" close="}" separators="|"><mrow><mfrac><mn>1</mn><msup><mn>2</mn><mn>8</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>8</mn></msup></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>7</mn></msup></mfrac></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>128</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>127</mn></mrow><mrow><mn>128</mn></mrow></mfrac></math></p>

</details>

---

### Q20. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

An experiment succeeds twice as often as it fails. The probability of at least <math> <mn>5</mn> </math> successes in the six trials of this experiment is

**Options:**

- **(A)** <math><mfrac><mrow><mn>496</mn></mrow><mrow><mn>729</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>192</mn></mrow><mrow><mn>729</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>240</mn></mrow><mrow><mn>729</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>256</mn><mn>729</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>256</mn><mn>729</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> be the probability of successes and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> be the probability of failure.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>2</mn><mi>q</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></math></p><p>gives <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>For having at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> successes in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> trials,</p><p>Required probability<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>5</mn></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>5</mn></msup><mfenced separators="|"><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>6.2</mn><mn>5</mn></msup><mo>+</mo><mn>64</mn></mrow><msup><mn>3</mn><mn>6</mn></msup></mfrac><mo>=</mo><mfrac><mn>256</mn><mn>729</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

A multiple choice examination has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> questions. Each question has three alternative answers out of which exactly one is correct. The probability that a student will get <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> or more correct answers just by guessing is :

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>1</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>0</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>7</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>3</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>1</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> or more correct answers means and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><mn>0</mn></math> wrong answers.
for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> wrong questions  <math> <mrow> <msup> <mspace></mspace> <mn>5</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <msup> <mo>&#215;</mo> <mn>2</mn> </msup> <msub> <mtext>C</mtext> <mn>1</mn> </msub> <mo>=</mo> <mn>1</mn> <mn>0</mn> </mrow> </math>

for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> wrong questions <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn></math>

Hence favourable ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn></math>

Total ways of answering <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>5</mn></msup></math>

Hence probability = <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>1</mn> </mrow> <mrow> <msup> <mn>3</mn> <mn>5</mn> </msup> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q22. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `2`

Consider 5 independent Bernoulli's trials each with probability of success $\mathrm{p}$. If the probability of at least one failure is greater than or equal to $\frac{31}{32}$, then $\mathrm{p}$ lies in the interval

**Options:**

- **(A)** $\left(\frac{3}{4}, \frac{11}{12}\right]$
- **(B)** $\left[0, \frac{1}{2}\right]$
- **(C)** $\left(\frac{11}{12}, 1\right]$
- **(D)** $\left(\frac{1}{2}, \frac{3}{4}\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left[0, \frac{1}{2}\right]$**

**Detailed Solution:**

$\mathrm{n}=5$
Success $=\mathrm{p}$
Failure $=\mathrm{q}$
$\mathrm{P}$ (at least one failure) $\geq \frac{31}{32}$
$1-\mathrm{P}$ (no failure) $\geq \frac{31}{32}$
$1-\mathrm{P}(\mathrm{x}=5) \geq \frac{31}{32}$
$1-{ }^5 \mathrm{C}_5 \mathrm{p}^5 \geq \frac{31}{32}$
$-\mathrm{p}^5 \geq-\frac{1}{32}$
$\mathrm{p}^5 \leq \frac{1}{32}$
$\mathrm{p} \leq \frac{1}{2}$
$\mathrm{p} \in\left[0, \frac{1}{2}\right]$

</details>

---

### Q23. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

In a binomial distribution $B\left(n, p=\frac{1}{4}\right)$, if the probability of at least one success is greater than or equal to $\frac{9}{10}$, then $n$ is greater than

**Options:**

- **(A)** $\frac{1}{\log _{10}{ }^4-\log _{10}{ }^3}$
- **(B)** $\frac{1}{\log _{10} 4+\log _{10} 3}$
- **(C)** $\frac{9}{\log _{10}{ }^4-\log _{10} 3}$
- **(D)** $\frac{4}{\log _{10}{ }^4-\log _{10} 3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{\log _{10}{ }^4-\log _{10}{ }^3}$**

**Detailed Solution:**

$$
1-q^n \geq \frac{9}{10} \Rightarrow\left(\frac{3}{4}\right)^n \leq \frac{1}{10} \Rightarrow n \geq-\log _{\frac{3}{4}} 10 \Rightarrow n \geq \frac{1}{\log _{10}{ }^4-\log _{10}{ }^3}
$$

</details>

---

### Q24. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

Two aeroplanes I and II bomb a target in succession. The probabilities of I and II scoring a hit correctly are $0.3$ and $0.2$, respectively. The second plane will bomb only if the first misses the target. The probability that the target is hit by the second plane is

**Options:**

- **(A)** $0.06$
- **(B)** $0.14$
- **(C)** $0.2$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) None of these**

**Detailed Solution:**

The desired probability
$\begin{aligned}
& =0.7 \times 0.2+(0.7)(0.8)(0.7)(0.2)+(0.7)(0.8)(0.7)(0.8)(0.7)(0.2)+\ldots . \\
& =0.14\left[1+(0.56)+(0.56)^2+\ldots\right] \\
& =0.14\left[\frac{1}{1-0.56}\right]=\frac{0.14}{0.44}=\frac{7}{22}.
\end{aligned}$

</details>

---

### Q25. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The mean and the variance of a binomial distribution are 4 and 2 respectively. Then the probability of 2 successes is

**Options:**

- **(A)** $\frac{37}{256}$
- **(B)** $\frac{219}{256}$
- **(C)** $\frac{128}{256}$
- **(D)** $\frac{28}{256}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{28}{256}$**

**Detailed Solution:**

Given that $n \mathrm{p}=4, \mathrm{n} p \mathrm{q}=2 \Rightarrow \mathrm{q}=1 / 2 \Rightarrow \mathrm{p}=1 / 2, \mathrm{n}=8 \Rightarrow \mathrm{p}(\mathrm{x}=2)={ }^8 \mathrm{C}_2\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^6=\frac{28}{256}$

</details>

---

### Q26. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of a random variable $\mathrm{X}$ having binomial distribution are 4 and 2 respectively, then $\mathrm{P}$ $(\mathrm{X}=1)$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{32}$
- **(C)** $\frac{1}{16}$
- **(D)** $\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{32}$**

**Detailed Solution:**

$\left.\begin{array}{c}\mathrm{np}=4 \\ \mathrm{npq}=2\end{array}\right\} \Rightarrow \mathrm{q}=\frac{1}{2} \cdot \mathrm{p}=\frac{1}{2}, \mathrm{n}=8$
$\mathrm{p}(\mathrm{X}=1)={ }^8 \mathrm{C}_1\left(\frac{1}{2}\right)\left(\frac{1}{2}\right)^7=8 \cdot \frac{1}{2^8}=\frac{1}{2^5}=\frac{1}{32}$

</details>

---

