# JEE Main Mathematics - Probability

## Topic 5: Total Probability

**Total Questions:** 13

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains $(N+1)$ coins $- N$ fair coins, and one coin with 'Head' on both sides. A coin is selected at random and tossed. If the probability of getting 'Head' is $\dfrac{9}{16}$, then $N$ is equal to:

**Options:**

- **(A)** $5$
- **(B)** $7$
- **(C)** $8$
- **(D)** $9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $7$**

**Detailed Solution:**

Let $E_1$ be the event of selecting a fair coin and $E_2$ be the event of selecting the two-headed coin.

$P(E_1) = \dfrac{N}{N+1}$

$P(E_2) = \dfrac{1}{N+1}$

Let $H$ be the event of getting a Head.

$P(H|E_1) = \dfrac{1}{2}$

$P(H|E_2) = 1$

Using the theorem of total probability:

$P(H) = P(E_1)P(H|E_1) + P(E_2)P(H|E_2)$

$P(H) = \left(\dfrac{N}{N+1}\right)\left(\dfrac{1}{2}\right) + \left(\dfrac{1}{N+1}\right)(1)$

$P(H) = \dfrac{N+2}{2(N+1)}$

Given $P(H) = \dfrac{9}{16}$:

$\dfrac{N+2}{2(N+1)} = \dfrac{9}{16}$

$\dfrac{N+2}{N+1} = \dfrac{9}{8}$

$8N + 16 = 9N + 9$

$N = 7$

Answer: $7$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probabilities that players $A$ and $B$ of a team are selected for the captaincy for a tournament are $0.6$ and $0.4$, respectively. If $A$ is selected the captain, the probability that the team wins the tournament is $0.8$ and if $B$ is selected the captain, the probability that the team wins the tournament is $0.7$. Then the probability, that the team wins the tournament, is :

**Options:**

- **(A)** $0.74$
- **(B)** $0.76$
- **(C)** $0.72$
- **(D)** $0.78$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.76$**

**Detailed Solution:**

Let $A$ be the event that player A is selected as captain, and $B$ the event that player B is selected as captain. Let $W$ be the event that the team wins the tournament.

Given:
$P(A) = 0.6$, $P(B) = 0.4$
$P(W \mid A) = 0.8$, $P(W \mid B) = 0.7$

By the law of total probability:
$P(W) = P(A) \cdot P(W \mid A) + P(B) \cdot P(W \mid B)$

$P(W) = (0.6)(0.8) + (0.4)(0.7)$

$P(W) = 0.48 + 0.28 = 0.76$

Hence, the correct option is $(2)\ 0.76$.

</details>

---

### Q3. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bag A contains 9 white and 8 black balls, while bag B contains 6 white and 4 black balls. One ball is randomly picked up from the bag B and mixed up with the balls in the bag A. Then a ball is randomly drawn from the bag A. If the probability, that the ball drawn is white, is $\frac{\mathrm{p}}{\mathrm{q}}, \operatorname{gcd}(\mathrm{p}, \mathrm{q})=1$, then $\mathrm{p}+\mathrm{q}$ is equal to

**Options:**

- **(A)** 23
- **(B)** 24
- **(C)** 21
- **(D)** 22

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 23**

**Detailed Solution:**

Bag A: 9W, 8B. Bag B: 6W, 4B.
Case 1: White transferred from B (prob $= \frac{6}{10}$). A becomes 10W, 8B. $P(\text{white from A}) = \frac{10}{18} = \frac{5}{9}$.
Case 2: Black transferred from B (prob $= \frac{4}{10}$). A becomes 9W, 9B. $P(\text{white from A}) = \frac{9}{18} = \frac{1}{2}$.
Total probability $= \frac{6}{10} \cdot \frac{5}{9} + \frac{4}{10} \cdot \frac{1}{2} = \frac{1}{3} + \frac{1}{5} = \frac{8}{15}$.
$p = 8, q = 15, \gcd(8,15) = 1$. So $p + q = 23$.

</details>

---

### Q4. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bag 1 contains 4 white balls and 5 black balls, and Bag 2 contains $n$ white balls and 3 black balls. One ball is drawn randomly from Bag 1 and transferred to Bag 2. A ball is then drawn randomly from Bag 2. If the probability, that the ball drawn is white, is $29 / 45$, then $n$ is equal to :

**Options:**

- **(A)** 6
- **(B)** 3
- **(C)** 5
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 6**

**Detailed Solution:**

Bag $1 \rightarrow 4 w, 5 B$
Bag $2 \rightarrow n w, 3 B$
$(\mathrm{I}) \rightarrow$ Transferred ball is white $P(w)=\frac{n+1}{n+4} \cdot \frac{4}{9}$
(II) $\rightarrow$ Transferred ball is black $P(w)=\frac{5}{9} \cdot \frac{n}{n+4}$
$\begin{aligned}
& \frac{4 n+4}{9 n+36}+\frac{5 n}{9 n+36}=\frac{29}{45} \\
& \frac{9 n+4}{9 n+36}=\frac{29}{45} \Rightarrow n=6
\end{aligned}$

</details>

---

### Q5. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>When a certain biased die is rolled, a particular face occurs with probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mi>x</mi></math> and its opposite face occurs with probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mi>x</mi><mo>.</mo></math> All other faces occur with probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>.</mo></math></p><p>Note that opposite faces sum to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> in any die. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>,</mo></math> and the probability of obtaining total sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>,</mo></math> when such a die is rolled twice, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><mn>96</mn></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<p>Probability of obtaining total sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mo>=</mo></math></p><p>Probability of getting opposite faces.</p><p>Probability of getting opposite faces</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></mfenced><mspace linebreak="newline"></mspace><mo>=</mo><mfrac><mn>13</mn><mn>96</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p>

</details>

---

### Q6. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

A fair coin is tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo></math> times such that the probability of getting at least one head is at least <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>9</mn><mo>.</mo></math> Then the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>When a coin is tossed, then probability of head, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mtext>Head</mtext></mfenced><mo>=</mo><mi>P</mi><mfenced><mtext>Tail</mtext></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mi>P</mi></math> (All tail)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8805;</mo><mn>0</mn><mo>.</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8805;</mo><mn>0</mn><mo>.</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8804;</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>n</mi><mi>min</mi></msub><mo>=</mo><mn>4</mn><mo>.</mo></math></p>

</details>

---

### Q7. JEE Main 2021 (17 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a computer program generate only the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to form a string of binary numbers with probability of occurrence of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> at even places be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and probability of occurrence of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> at the odd place be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>.</mo></math> Then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> is followed by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>01</mn></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>18</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>Given the probability that the digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> appear at the even place is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo></math> hence the probability that the digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> appear at the even place is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math><gwmw style="display:none;"></gwmw></p><p>And the probability that the digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> appear at the odd place is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo></math> hence the probability that the digit <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> appear at the odd place is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>.</mo></math></p><p>For the digits <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mn>10</mn><mo>&#39;</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#39;</mo><mn>01</mn><mo>&#39;</mo></math> we have the following possibilities </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>o</mi><mi>d</mi><mi>d</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd><mtd><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd><mtd><mpadded lspace="-1px"><mi>o</mi><mi>d</mi><mi>d</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mpadded></mtd><mtd><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd></mtr></mtable></math></p><p>Or</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd><mtd><mi>o</mi><mi>d</mi><mi>d</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd><mtd><mpadded lspace="-1px"><mi>e</mi><mi>v</mi><mi>e</mi><mi>n</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mpadded></mtd><mtd><mi>o</mi><mi>d</mi><mi>d</mi><mo>&#160;</mo><mi>p</mi><mi>l</mi><mi>a</mi><mi>c</mi><mi>e</mi></mtd></mtr></mtable></math></p><p>Thus, the required probability is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>18</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>18</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q8. JEE Main 2020 (04 Sep Shift 1)

*Type:* `numerical` | *Level:* `3`

The probability of a man hitting a target is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>.</mo></math> The least number of shots required, so that the probability of his hitting the target at least once is greater than <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo></math> is....

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">p</mi><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>,</mo><mtext>&#8201;</mtext><mi mathvariant="normal">q</mi><mo>=</mo><mfrac><mn>9</mn><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> (not hitting in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> trials) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>9</mn><mn>10</mn></mfrac></mfenced><mi mathvariant="normal">n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi></math> (at least one hit)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mfrac><mn>9</mn><mn>10</mn></mfrac></mfenced><mi mathvariant="normal">n</mi></msup><mo>&#62;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>9</mn><mn>10</mn></mfrac></mfenced><mi mathvariant="normal">n</mi></msup><mo>&#60;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>0</mn><mo>.9</mo></mrow></mfenced><mi mathvariant="normal">n</mi></msup><mo>&#60;</mo><mn>0</mn><mo>.</mo><mn>75</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>=</mo><mn>3</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>729</mn><mo>&#60;</mo><mn>0</mn><mo>.</mo><mn>75</mn></math> which is true.</p>

</details>

---

### Q9. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Minimum number of times a fair coin must be tossed so that the probability of getting at least one <strong>head </strong>is more than <math><mn>99</mn><mi>%</mi><mi>&#160;</mi></math> is:

**Options:**

- **(A)** <math><mn>8</mn></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>7</mn></math>**

**Detailed Solution:**

<p>Let coin is tossed <math><mi>n</mi></math> times.</p><p>The probability of getting a head in a single throw of a die is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p><p>By using binomial theorem, we know that the probability that an event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> appear <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> times in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> trials is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>p</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>q</mi><mi>r</mi></msup><mo>,</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>.</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo></math>at least are head<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mo>(</mo></math>no head<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup></math></p><p>Using, the given condition, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8805;</mo><mn>0.99</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#8804;</mo><mn>1</mn><mo>-</mo><mn>0.99</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>&#8804;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>100</mn></mrow></mfrac></math></p><p>As, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>6</mn></msup><mo>=</mo><mn>64</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>7</mn></msup><mo>=</mo><mn>128</mn><mo>,</mo></math> hence, the minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>.</mo></math></p>

</details>

---

### Q10. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The minimum number of times one has to toss a fair coin so that the probability of observing at least one head is at least <math><mn>90</mn><mi>%</mi></math> is:

**Options:**

- **(A)** <math><mn>2</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>4</mn></math>**

**Detailed Solution:**

Let a fair coin is tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> times, then
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>at</mi><mo>&#160;</mo><mi>least</mi><mo>&#160;</mo><mi>one</mi><mo>&#160;</mo><mi>head</mi><mo>)</mo><mi>&#160;</mi><mo>=</mo><mn>1</mn><mo>&#8211;</mo><mi>P</mi><mo>(</mo><mi>all</mi><mo>&#160;</mo><mi>tails</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#8211;</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mi>n</mi></msup><mo>&#62;</mo><mfrac><mn>90</mn><mn>100</mn></mfrac></math> (given)
<math><mo>&#8658;</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>&#60;</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>90</mn></mrow><mrow><mn>100</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
<math><mo>&#8658;</mo><msup><mrow><mn>2</mn></mrow><mrow><mi>n</mi></mrow></msup><mo>&#62;</mo><mn>10</mn></math>
<math><mo>&#8658;</mo><mi>n</mi><mo>&#8805;</mo><mn>4</mn></math>

</details>

---

### Q11. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the probability of hitting a target by a shooter, in any shot is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo></math> then the minimum number of independent shots at the target required by him so that the probability of hitting the target at least once is greater than <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>,</mo></math> is:

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>5</mn></math>
- **(C)** <math><mn>6</mn></math>
- **(D)** <math><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>5</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>hitting</mi><mtext>&#8201;</mtext><mi>target</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

Let number of trials <math><mo>=</mo><mi>n</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi mathvariant="normal">h</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">g</mi><mtext>&#8201;&#8201;</mtext><mi mathvariant="normal">t</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">g</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">t</mi><mtext>&#8201;&#8201;</mtext><mi mathvariant="normal">a</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">t</mi><mtext>&#8201;</mtext><mi mathvariant="normal">o</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi></mrow></mfenced></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>not</mi><mo>&#160;</mo><mi>hit</mi></mrow></mfenced></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>&#62;</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced><mo>&#62;</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup></math>

So minimum number of trials <math><mo>=</mo><mn>5</mn></math>

</details>

---

### Q12. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An unbiased coin is tossed. If the outcome is a head then a pair of unbiased dice is rolled and the sum of the numbers obtained on them is noted. If the toss of the coin results in tail then a card from a well-shuffled pack of nine cards numbered <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1,</mn><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><mn>9</mn></math> is randomly picked and the number on the card is noted. The probability that the noted number is either <math><mn>7</mn></math> or <math><mn>8</mn></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>72</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>72</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>72</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the event that the noted number is either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> be the event that the toss of coin results in head and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> be the event that the toss of coin results in tail.</p><p>Then, we have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo></math>getting the sum of the numbers on the pair of dice as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>)</mo></math></p><p>The total number of cases, when a pair of dice is thrown are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mn>6</mn><mo>=</mo><mn>36</mn></math> and the cases of getting sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>11</mn></math> cases.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>11</mn><mn>36</mn></mfrac></math></p><p>Similarly, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mo>(</mo></math>getting the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> from the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p><p>Now, using the total probability theorem, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mi>P</mi><mfenced><mrow><mi>A</mi><mo>|</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>11</mn><mn>36</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>11</mn><mn>72</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>72</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q13. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An urn contains <math><mn>5</mn></math> red and <math><mn>2</mn></math> green balls. A ball is drawn at random from the urn. If the drawn ball is green, then a red ball is added to the urn and if the drawn ball is red, then a green ball is added to the urn; the original ball is not returned to the urn. Now, a second ball is drawn at random from it. The probability that the second ball is red, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>26</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>27</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>32</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>**

**Detailed Solution:**

Let <math><mi>A</mi></math> is event that <math><mn>2</mn><mi>n</mi><mi>d</mi></math> drawn ball is red.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><mfenced separators="|"><mi>A</mi></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mi>R</mi></mfenced><mo>&#215;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>/</mo><mi>R</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mi>G</mi></mfenced><mo>&#215;</mo><mi>P</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>A</mi><mo>/</mo><mi>G</mi></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>7</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>7</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>32</mn></mrow><mrow><mn>49</mn></mrow></mfrac></math>

</details>

---

