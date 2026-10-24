# JEE Main Mathematics - Probability

## Topic 3: Conditional Probability and Multiplication Theorem

**Total Questions:** 39

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A candidate has to go to the examination centre to appear in an examination. The candidate uses only one means of transportation for the entire distance out of bus, scooter and car. The probabilities of the candidate going by bus, scooter and car, respectively, are $\dfrac{2}{5}$, $\dfrac{1}{5}$ and $\dfrac{2}{5}$. The probabilities that the candidate reaches late at the examination centre are $\dfrac{1}{5}$, $\dfrac{1}{3}$ and $\dfrac{1}{4}$ if the candidate uses bus, scooter and car, respectively. Given that the candidate reached late at the examination centre, the probability that the candidate travelled by bus is:

**Options:**

- **(A)** $\dfrac{11}{37}$
- **(B)** $\dfrac{12}{37}$
- **(C)** $\dfrac{13}{37}$
- **(D)** $\dfrac{14}{37}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{12}{37}$**

**Detailed Solution:**

Let $E_1$, $E_2$, and $E_3$ be the events that the candidate travels by bus, scooter, and car, respectively.

The probabilities of choosing these modes of transport are:
$P(E_1) = \dfrac{2}{5}$
$P(E_2) = \dfrac{1}{5}$
$P(E_3) = \dfrac{2}{5}$

Let $A$ be the event that the candidate reaches the examination centre late. The conditional probabilities of reaching late are:
$P(A|E_1) = \dfrac{1}{5}$
$P(A|E_2) = \dfrac{1}{3}$
$P(A|E_3) = \dfrac{1}{4}$

We need to find the probability that the candidate travelled by bus given that they reached late, which is $P(E_1|A)$.

Using Bayes' theorem:
$P(E_1|A) = \dfrac{P(E_1)P(A|E_1)}{P(E_1)P(A|E_1) + P(E_2)P(A|E_2) + P(E_3)P(A|E_3)}$

Substituting the given values:
$P(E_1|A) = \dfrac{\dfrac{2}{5} \times \dfrac{1}{5}}{\left(\dfrac{2}{5} \times \dfrac{1}{5}\right) + \left(\dfrac{1}{5} \times \dfrac{1}{3}\right) + \left(\dfrac{2}{5} \times \dfrac{1}{4}\right)}$

$P(E_1|A) = \dfrac{\dfrac{2}{25}}{\dfrac{2}{25} + \dfrac{1}{15} + \dfrac{1}{10}}$

Taking the LCM of the denominators $25$, $15$, and $10$, which is $150$:
$P(E_1|A) = \dfrac{\dfrac{12}{150}}{\dfrac{12}{150} + \dfrac{10}{150} + \dfrac{15}{150}}$

$P(E_1|A) = \dfrac{12}{12 + 10 + 15} = \dfrac{12}{37}$

Answer: $\dfrac{12}{37}$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains 6 blue and 6 green balls. Pairs of balls are drawn without replacement until the bag is empty. The probability that each drawn pair consists of one blue and one green ball is :

**Options:**

- **(A)** $\dfrac{63}{925}$
- **(B)** $\dfrac{17}{231}$
- **(C)** $\dfrac{16}{231}$
- **(D)** $\dfrac{64}{925}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{16}{231}$**

**Detailed Solution:**

The probability that the first pair drawn consists of one blue and one green ball is:

$P_1 = \dfrac{^{6}C_{1} \times ^{6}C_{1}}{^{12}C_{2}} = \dfrac{36}{66} = \dfrac{6}{11}$

Since the balls are drawn without replacement, $5$ blue and $5$ green balls remain. The probability that the second pair consists of one blue and one green ball is:

$P_2 = \dfrac{^{5}C_{1} \times ^{5}C_{1}}{^{10}C_{2}} = \dfrac{25}{45} = \dfrac{5}{9}$

Continuing this process for all $6$ pairs, the probabilities are:

$P_3 = \dfrac{^{4}C_{1} \times ^{4}C_{1}}{^{8}C_{2}} = \dfrac{16}{28} = \dfrac{4}{7}$

$P_4 = \dfrac{^{3}C_{1} \times ^{3}C_{1}}{^{6}C_{2}} = \dfrac{9}{15} = \dfrac{3}{5}$

$P_5 = \dfrac{^{2}C_{1} \times ^{2}C_{1}}{^{4}C_{2}} = \dfrac{4}{6} = \dfrac{2}{3}$

$P_6 = \dfrac{^{1}C_{1} \times ^{1}C_{1}}{^{2}C_{2}} = \dfrac{1}{1} = 1$

The required probability is the product of these individual probabilities:

$P = P_1 \times P_2 \times P_3 \times P_4 \times P_5 \times P_6$

$P = \dfrac{6}{11} \times \dfrac{5}{9} \times \dfrac{4}{7} \times \dfrac{3}{5} \times \dfrac{2}{3} \times 1$

Canceling common factors in the numerator and denominator:

$P = \dfrac{6 \times 4 \times 2}{11 \times 9 \times 7} = \dfrac{48}{693} = \dfrac{16}{231}$

Answer: $\dfrac{16}{231}$

</details>

---

### Q3. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A bag contains 19 unbiased coins and one coin with head on both sides. One coin drawn at random is tossed and head turns up. If the probability that the drawn coin was unbiased, is $\frac{\mathrm{m}}{\mathrm{n}}, \operatorname{gcd}(\mathrm{m}, \mathrm{n})=1$, then $\mathrm{n}^2-\mathrm{m}^2$ is equal to :

**Options:**

- **(A)** 80
- **(B)** 60
- **(C)** 72
- **(D)** 64

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 80**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/09ryI03KLTfOI6erLKGwaVxVwEoNM-Sfm3mjvZeoi-E.original.fullsize.png"/>
$\begin{aligned} & \text { Required probability }=\frac{\frac{19}{20} \times \frac{1}{2}}{\frac{19}{20} \times \frac{1}{2}+\frac{1}{20} \times 1}=\frac{19}{21} \\ & \therefore \frac{\mathrm{~m}}{\mathrm{n}}=\frac{19}{21} \\ & \Rightarrow \mathrm{n}^2-\mathrm{m}^2=441-361=80\end{aligned}$

</details>

---

### Q4. JEE Main 2025 (4 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

A card from a pack of 52 cards is lost. From the remaining 51 cards, $n$ cards are drawn and are found to be spades. If the probability of the lost card to be a spade is $\frac{11}{50}$, the n is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

n cards are drawn \& are found all spade, thus remaining spades $=13-\mathrm{x}$ remaining total cards $=52-\mathrm{x}$
Now given that $\mathrm{P}($ lost card is spade $)=\frac{11}{50}$
$\begin{aligned}
& \text { i.e. } \frac{{ }^{13-\mathrm{n}} \mathrm{C}_1}{{ }^{52-\mathrm{n}} \mathrm{C}_1}=\frac{11}{50} \\
& 50(13-\mathrm{n})=11(52-\mathrm{n}) \\
& 39 \mathrm{n}=78 \\
& \mathrm{n}=2
\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Given three indentical bags each containing 10 balls, whose colours are as follows :
$\begin{array}{cccc} & \text{Red} & \text{Blue} & \text{Green} \\ \text{Bag I} & 3 & 2 & 5 \\ \text{Bag II} & 4 & 3 & 3 \\ \text{Bag III} & 5 & 1 & 4\end{array}$
A person chooses a bag at random and takes out a ball. If the ball is Red, the probability that it is from bag I is p and if the balls is Green, the probability that it is from bag III is q , then the value of $\left(\frac{1}{\mathrm{p}}+\frac{1}{\mathrm{q}}\right)$ is :

**Options:**

- **(A)** $6$
- **(B)** $9$
- **(C)** $7$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/QXxpsMDtXTkUgw-aqUALTGgKF5l9Mwgn0-Vj5t69zAM.original.fullsize.png"/>
$\mathrm{p}=\mathrm{P}\left(\frac{\mathrm{B}_{\mathrm{I}}}{\mathrm{R}}\right)=\frac{\frac{1}{3}\left(\frac{3}{10}\right)}{\frac{1}{3}\left(\frac{3}{10}+\frac{4}{10}+\frac{5}{10}\right)}=\frac{1}{4}$
$\begin{aligned} & \mathrm{q}=\left(\frac{\mathrm{B}_{\mathrm{III}}}{\mathrm{G}}\right)=\frac{\frac{1}{3}\left(\frac{4}{10}\right)}{\frac{1}{3}\left(\frac{5}{10}+\frac{3}{10}+\frac{4}{10}\right)}=\frac{1}{3} \\ & \therefore \frac{1}{\mathrm{p}}+\frac{1}{\mathrm{q}}=7\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $A$ and $B$ are two events such that $P(A \cap B)=0.1$, and $P(A \mid B)$ and $P(B \mid A)$ are the roots of the equation $12 x^2-7 x+1=0$, then the value of $\frac{\mathrm{P}(\overline{\mathrm{A}} \cup \overline{\mathrm{B}})}{\mathrm{P}(\overline{\mathrm{A}} \cap \overline{\mathrm{B}})}$ is :

**Options:**

- **(A)** $\frac{4}{3}$
- **(B)** $\frac{7}{4}$
- **(C)** $\frac{5}{3}$
- **(D)** $\frac{9}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{4}$**

**Detailed Solution:**

$P(A \cap B)=0.1, P(A \mid B)$ and $P(B \mid A)$ are the roots of the equation $12 x^2-7 x+1=0$
$\begin{aligned}
& \Rightarrow \quad P(A \mid B) P(B \mid A)=\frac{1}{12} \\
& \Rightarrow \quad \frac{P(A \cap B)}{P(B)} \times \frac{P(A \cap B)}{P(A)}=\frac{1}{12} \\
& \Rightarrow \quad P(A) P(B)=12(0.1)^2 \\
& =0.12
\end{aligned}$

Also, $P(A \mid B)+P(B \mid A)=\frac{7}{12}$
$\begin{aligned}
\Rightarrow & P(A \cap B)\left(\frac{1}{P(B)}+\frac{1}{P(A)}\right)=\frac{7}{12} \\
\Rightarrow & P(A)+P(B)=\frac{7}{12} \times \frac{0.12}{0.1} \\
\Rightarrow & P(A)+P(B)=0.7 \\
& \frac{P(\bar{A} \cup \bar{B})}{P(\bar{A} \cap \bar{B})}=\frac{P(\overline{A \cap B})}{P(\overline{A U B})} \\
& =\frac{1-P(A \cap B)}{1-P(A \cup B)} \\
& =\frac{1-0.1}{1-(0.7-0.1)}=\frac{0.9}{0.4}=\frac{9}{4}
\end{aligned}$

</details>

---

### Q7. JEE Main 2024 (04 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

In a tournament, a team plays 10 matches with probabilities of winning and losing each match as $\frac{1}{3}$ and $\frac{2}{3}$ respectively. Let $x$ be the number of matches that the team wins, and $y$ be the number of matches that team loses. If the probability $\mathrm{P}(|x-y| \leq$ 2) is $p$, then $3^9 p$ equals ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8288**

**Detailed Solution:**

$\begin{aligned} & P(W)=\frac{1}{3} \quad P(L)=\frac{2}{3} \\ & x=\text { number of matches that team wins } \\ & y=\text { number of matches that team loses } \\ & |x-y| \leq 2 \text { and } x+y=10 \\ & |x-y|=0,1,2 \quad x, y \in N\end{aligned}$
Case-I
$\begin{aligned}
& -I:|x-y|=0 \Rightarrow x=y \\
& \because x+y=10 \Rightarrow x=5=y \\
& P(|x-y|=0)={ }^{10} C_5\left(\frac{1}{3}\right)^5\left(\frac{2}{3}\right)^5
\end{aligned}$
Case-II : $|\mathrm{x}-\mathrm{y}|=1 \Rightarrow \mathrm{x}-\mathrm{y}= \pm 1$
$\begin{array}{|c|c|}
\hline \mathrm{x}=\mathrm{y}+1 & \mathrm{x}=\mathrm{y}-1 \\
\hline\because \mathrm{x}+\mathrm{y}=10 & \because \mathrm{x}+\mathrm{y}=10 \\
\hline 2 \mathrm{y}=9 & 2 \mathrm{y}=11 \\
\hline \text{Not possible} & \text{Not possible} \\
\hline
\end{array}$
$\begin{aligned} & \text { Case-III : }|\mathrm{x}-\mathrm{y}|=2 \Rightarrow \mathrm{x}-\mathrm{y}= \pm 2 \\ & x-y=2 \quad \text { OR } \quad x-y=-2 \\ & \because \mathrm{x}+\mathrm{y}=10 \quad \because \mathrm{x}+\mathrm{y}=10 \\ & x=6, y=4 \quad x=4, y=6 \\ & \mathrm{P}(|\mathrm{x}-\mathrm{y}|=2)={ }^{10} \mathrm{C}_6\left(\frac{1}{3}\right)^6\left(\frac{2}{3}\right)^4+{ }^{10} \mathrm{C}_4\left(\frac{1}{3}\right)^4\left(\frac{2}{3}\right)^6 \\ & \mathrm{p}={ }^{10} \mathrm{C}_5 \frac{2^5}{3^{10}}+{ }^{10} \mathrm{C}_6 \frac{2^4}{3^{10}}+{ }^{10} \mathrm{C}_4 \frac{2^6}{3^{10}} \\ & 3^9 \mathrm{p}=\frac{1}{3}\left({ }^{10} \mathrm{C}_5 2^5+{ }^{10} \mathrm{C}_6 2^4+{ }^{10} \mathrm{C}_4 2^6\right) \\ & =8288 \\ & \end{aligned}$

</details>

---

### Q8. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bag<math xmlns="http://www.w3.org/1998/Math/MathML"><mo> </mo><mi>A</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> red balls and bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> white, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> red balls. One bag is selected at random and a ball is drawn from it. The probability of drawing the ball from the bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math>, if the ball drawn in white, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>10</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given: Given balls in bags are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>→</mo><mn>3</mn><mi>W</mi><mo>,</mo><mo> </mo><mn>7</mn><mi>R</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>→</mo><mn>3</mn><mi>W</mi><mo>,</mo><mo> </mo><mn>2</mn><mi>R</mi></math></p><p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>:</mo><mi>A</mi></math> is selected</p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/79ddbbb7-6d97-4e5f-a908-87ba0a29098b.png" style="width: 169px; height: 95px;"/></p><p>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub><mo>:</mo><mi>B</mi></math> is selected</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">E</mi></math>: white ball is drawn</p><p>Using Baye's theorem,
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">P</mi><mo>(</mo><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub><mo>)</mo><mo>·</mo><mi mathvariant="normal">P</mi><mfenced><mstyle displaystyle="true"><mfrac><mi mathvariant="normal">E</mi><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub></mfrac></mstyle></mfenced></mrow><mrow><mi mathvariant="normal">P</mi><mfenced><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub></mfenced><mo>·</mo><mi mathvariant="normal">P</mi><mfenced><mfrac><mi mathvariant="normal">E</mi><msub><mi mathvariant="normal">E</mi><mn>1</mn></msub></mfrac></mfenced><mo>+</mo><mi mathvariant="normal">P</mi><mfenced><msub><mi mathvariant="normal">E</mi><mn>2</mn></msub></mfenced><mo>·</mo><mi mathvariant="normal">P</mi><mfenced><mfrac><mi mathvariant="normal">E</mi><msub><mi mathvariant="normal">E</mi><mn>2</mn></msub></mfrac></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mfrac><mn>3</mn><mn>10</mn></mfrac></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mfrac><mn>3</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>×</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mfrac><mn>3</mn><mn>20</mn></mfrac><mrow><mfrac><mn>3</mn><mn>20</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><mn>20</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>3</mn><mrow><mn>3</mn><mo>+</mo><mn>6</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mfrac><msub><mi>E</mi><mn>1</mn></msub><mi>E</mi></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p></blockquote>

</details>

---

### Q9. JEE Main 2024 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>y</mi></math> are chosen with replacement from the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>…</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>10</mn><mo>}</mo></math>. Then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>|</mo><mo>&gt;</mo><mn>5</mn></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>121</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>62</mn><mn>121</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>60</mn><mn>121</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>121</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>121</mn></mfrac></math>**

**Detailed Solution:**

<p>Given set is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>10</mn></mrow></mfenced></math>.</p><p>So, total number of outcomes are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>11</mn><mo>×</mo><mn>11</mn></mrow></mfenced><mo>=</mo><mn>121</mn></math></p><p>Favourable outcomes are:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>0</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>8</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>9</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>,</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mn>10</mn></mrow></mfenced></math> </p><p>And the same number of elements when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>y</mi></math> are interchanged.</p><p>So, the number of favourable outcomes are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>.</p><p>So, the required probability is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mn>30</mn><mn>121</mn></mfrac></math>.</p>

</details>

---

### Q10. JEE Main 2024 (27 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An urn contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> white and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> black balls. Two successive draws of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> balls are made without replacement. The probability, that the first draw gives all white balls and the second draw gives all black balls, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>256</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>715</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>715</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>256</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>715</mn></mfrac></math>**

**Detailed Solution:**

<p>Total number of balls in the bag <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>15</mn></math>.</p><p>Number of white balls <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn></math>.</p><p>Number of black balls <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math>.</p><p>Four balls are drawn at random at a time.</p><p>The probability that first draw give four white balls</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>91</mn></mfrac></math></p><p>The balls are not replaced.</p><p>Now, the probability that second draw give four black balls</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>21</mn><mn>55</mn></mfrac></math></p><p>The probability that the first draw give four white balls  and second draw give four black balls</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>91</mn></mfrac><mo>×</mo><mfrac><mn>21</mn><mn>55</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>715</mn></mfrac></math></p><p>Hence, the required probability is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>715</mn></mfrac></math>.</p>

</details>

---

### Q11. JEE Main 2024 (27 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

A fair die is tossed repeatedly until a six is obtained. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> denote the number of tosses required and let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">a</mi><mo>=</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>=</mo><mn>3</mn><mo>)</mo><mo>,</mo><mi mathvariant="normal">b</mi><mo>=</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>3</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">c</mi><mo>=</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn><mo>∣</mo><mi mathvariant="normal">X</mi><mo>&gt;</mo><mn>3</mn><mo>)</mo></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">b</mi><mo>+</mo><mi mathvariant="normal">c</mi></mrow><mi mathvariant="normal">a</mi></mfrac></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mtext>getting</mtext><mo> </mo><mn>6</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>,</mo><mo> </mo><mi>P</mi><mfenced><mrow><mtext>not getting</mtext><mo> </mo><mn>6</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>=</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>=</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>×</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>×</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>=</mo><mfrac><mn>25</mn><mn>216</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>×</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>×</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup><mo>·</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>4</mn></msup><mo>·</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mo>∞</mo></msub><mo>=</mo><mi mathvariant="normal">a</mi><mo>+</mo><mi>ar</mi><mo>+</mo><msup><mi>ar</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>∞</mo><mo>=</mo><mfrac><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mfrac><mfrac><mn>25</mn><mn>216</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mfrac><mn>25</mn><mn>216</mn></mfrac><mo>×</mo><mfrac><mn>6</mn><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">b</mi><mo>=</mo><mfrac><mn>25</mn><mn>36</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn><mo>)</mo><mo>=</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup><mo>·</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>6</mn></msup><mo>·</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn><mo>)</mo><mo>=</mo><mfrac><mrow><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup><mo>·</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn><mo>)</mo><mo>=</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">c</mi><mo>=</mo><mi mathvariant="normal">P</mi><mfenced><mfrac><mrow><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn></mrow><mrow><mi mathvariant="normal">X</mi><mo>&gt;</mo><mn>3</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi mathvariant="normal">P</mi><mfenced><mrow><mfenced><mrow><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn></mrow></mfenced><mo>∩</mo><mfenced><mrow><mi mathvariant="normal">X</mi><mo>&gt;</mo><mn>3</mn></mrow></mfenced></mrow></mfenced></mrow><mrow><mi mathvariant="normal">P</mi><mfenced><mrow><mi mathvariant="normal">X</mi><mo>&gt;</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi mathvariant="normal">P</mi><mfenced><mrow><mi mathvariant="normal">X</mi><mo>≥</mo><mn>6</mn></mrow></mfenced></mrow><mrow><mi mathvariant="normal">P</mi><mfenced><mrow><mi mathvariant="normal">X</mi><mo>&gt;</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">c</mi><mo>=</mo><mfrac><mn>25</mn><mn>36</mn></mfrac><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">b</mi><mo>+</mo><mi mathvariant="normal">c</mi></mrow><mi mathvariant="normal">a</mi></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>36</mn></mfrac><mo>+</mo><mfrac><mn>25</mn><mn>36</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>216</mn></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">b</mi><mo>+</mo><mi mathvariant="normal">c</mi></mrow><mi mathvariant="normal">a</mi></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>50</mn><mn>36</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>25</mn><mn>216</mn></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">b</mi><mo>+</mo><mi mathvariant="normal">c</mi></mrow><mi mathvariant="normal">a</mi></mfrac><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q12. JEE Main 2023 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

A bag contains six balls of different colours. Two balls are drawn in succession with replacement. The probability that both the balls are of the same colour is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math>. Next four balls are drawn in succession with replacement and the probability that exactly three balls are of the same colours is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>:</mo><mo>&#160;</mo><mi>q</mi><mo>=</mo><mi>m</mi></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>:</mo><mi>n</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **14**

**Detailed Solution:**

<p>Given,</p><p>A bag contains six balls of different colours, two balls are drawn in succession with replacement,</p><p>The probability that both the balls are of the same colour will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mfrac><mn>6</mn><mn>36</mn></mfrac></math></p><p>Now Next four balls are drawn in succession with replacement and the probability that exactly three balls are of the same colours is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math>,</p><p>So, probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>4</mn></mmultiscripts></mrow><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>120</mn><mn>1296</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>54</mn></mfrac></math></p><p>Now the ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>q</mi></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p>Now, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>&#8658;</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>14</mn></math></p>

</details>

---

### Q13. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If an unbiased die, marked with <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></math> on its faces is thrown five times, then the probability that the product of the outcomes is positive, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>881</mn><mn>2592</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>521</mn><mn>2592</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>440</mn><mn>2592</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>27</mn><mn>288</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>521</mn><mn>2592</mn></mfrac></math>**

**Detailed Solution:**

<p>The unbiased die is thrown five times such that the product of the outcomes is positive, then either all outcomes are positive or any two are negative.</p><p>Either all outcomes are positive or any two are negative.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>p</mi></math> (positive) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mi>p</mi></math> (negative) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Required probability</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>5</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>1</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>521</mn><mn>2592</mn></mfrac></math></p>

</details>

---

### Q14. JEE Main 2022 (28 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two events such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8739;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8739;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>. Consider </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math>,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math>. Then</p>

**Options:**

- **(A)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">S</mi><mn>2</mn></mrow></mfenced></math> are true
- **(B)** Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are false
- **(C)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> is true
- **(D)** Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">S</mi><mn>2</mn></mrow></mfenced></math> are true**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be two events such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8739;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8739;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>, </p><p>Now using the formula of conditional probability we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8739;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>B</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle><mrow><mi>P</mi><mfenced><mi>B</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac></math></p><p>Now again using formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8739;</mo><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle><mrow><mi>P</mi><mfenced><mi>A</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>18</mn></mfrac></math></p><p>Now we know that,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced></math> </p><p>{also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math>}</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><msup><mi>A</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>-</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>18</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Both <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>1</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mn>2</mn></mrow></mfenced></math> are true.</p></blockquote>

</details>

---

### Q15. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are two events such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><menclose notation="right"><mi>A</mi></menclose><msup><mi>B</mi><mo>'</mo></msup></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><menclose notation="right"><mi>B</mi></menclose><msup><mi>A</mi><mo>'</mo></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>8</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>We know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>+</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>30</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mtext>Only&#160;A</mtext><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>30</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>30</mn></mfrac></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><msup><mi>A</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mtext>Only&#160;B</mtext><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>30</mn></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>30</mn></mfrac></math></p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/390d7f37-86e4-4e8e-b475-83e1c0acb89a-image.png" style="width: 243px; height: 169px;" /></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8739;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8739;</mo><msup><mi>A</mi><mo>&#39;</mo></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msup><mi>B</mi><mo>&#39;</mo></msup></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>B</mi><mo>&#8745;</mo><msup><mi>A</mi><mo>&#39;</mo></msup></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msup><mi>A</mi><mo>&#39;</mo></msup></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mn>9</mn><mn>30</mn></mfrac><mfrac><mn>4</mn><mn>5</mn></mfrac></mfrac><mo>+</mo><mfrac><mfrac><mn>5</mn><mn>30</mn></mfrac><mfrac><mn>2</mn><mn>3</mn></mfrac></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math></p></blockquote>

</details>

---

### Q16. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A biased die is marked with numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>32</mn><mo>,</mo><mn>32</mn></math> on its faces and the probability of getting a face with mark <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac></math>. If the die is thrown thrice, then the probability, that the sum of the numbers obtained is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>, is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><msup><mn>2</mn><mn>11</mn></msup></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><msup><mn>2</mn><mn>12</mn></msup></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msup><mn>2</mn><mn>10</mn></msup></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><msup><mn>2</mn><mn>12</mn></msup></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>13</mn><msup><mn>2</mn><mn>12</mn></msup></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mn>2</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mn>4</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mn>8</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mn>16</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mn>32</mn></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>32</mn></mfrac></math></p><p>When we get the faces as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>32</mn></math> then the probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>32</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>1024</mn></mfrac></math></p><p>When we get the faces as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>16</mn></math> then the probability will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4096</mn></mfrac></math></p><p>Hence, the required probability will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>1024</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4096</mn></mfrac><mo>=</mo><mfrac><mn>13</mn><mn>4096</mn></mfrac></math></p>

</details>

---

### Q17. JEE Main 2022 (25 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> be two events such that the conditional probabilities <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8739;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>2</mn></msub><mo>&#8739;</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msubsup><mi>E</mi><mn>1</mn><mo>&#39;</mo></msubsup><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>1</mn><mo>&#39;</mo></msubsup></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>2</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msup><mi>E</mi><mo>&#39;</mo></msup><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><msup><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8746;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>&#39;</mo></msup><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>7</mn><mn>24</mn></mfrac><mo>=</mo><mfrac><mn>17</mn><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msubsup><mi>E</mi><mn>2</mn><mo>&#39;</mo></msubsup></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#183;</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math></p>

</details>

---

### Q18. JEE Main 2022 (24 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

In an examination, there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> true-false type questions. Out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>, a student can guess the answer of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> questions correctly with probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> questions correctly with probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>. If the probability that the student guesses the answers of exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> questions correctly out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>27</mn><mi>k</mi></mrow><msup><mn>4</mn><mn>10</mn></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **479**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>:</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>&#8594;</mo></math>Correct answer</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>10</mn></mrow></mfenced><mo>;</mo><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> Correct answer</p><p>Now total ways in which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> Correct answer is given will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>Case&#160;(i)&#160;&#160;</mtext><mfenced><mrow><mn>4</mn><mo>,</mo><mn>4</mn></mrow></mfenced><mo>:</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>4</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>4</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>Case</mi><mo>&#160;</mo><mtext>(ii)&#160;</mtext><mfenced><mrow><mn>3</mn><mo>,</mo><mn>5</mn></mrow></mfenced><mo>:</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>1</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>5</mn></msup><mo>&#183;</mo><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mtext>Case&#160;(iii)</mtext><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mn>6</mn></mrow></mfenced><mo>:</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>6</mn></msup></math></p><p>Total probability  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>10</mn></msup></mfrac><mfenced close="]" open="["><mrow><msup><mn>3</mn><mn>4</mn></msup><mo>&#215;</mo><mn>15</mn><mo>&#215;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#215;</mo><msup><mn>3</mn><mn>3</mn></msup><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>&#215;</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>27</mn><msup><mn>4</mn><mn>10</mn></msup></mfrac><mfenced close="]" open="["><mrow><mn>2</mn><mo>.</mo><mn>7</mn><mo>&#215;</mo><mn>15</mn><mo>+</mo><mn>72</mn><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>27</mn><mi>k</mi></mrow><msup><mn>4</mn><mn>10</mn></msup></mfrac></math></p><p>We get,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">K</mi><mo>=</mo><mn>479</mn></math></p>

</details>

---

### Q19. JEE Main 2021 (26 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A fair die is tossed until six is obtained on it. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the number of required tosses, then the conditional probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#10878;</mo><mn>5</mn><mo>&#8739;</mo><mi>X</mi><mo>&#62;</mo><mn>2</mn><mo>)</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>36</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>36</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>125</mn><mn>216</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>36</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mrow><mi>x</mi><mo>&#8805;</mo><mn>5</mn></mrow><mrow><mi>x</mi><mo>&#62;</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>x</mi><mo>&#8805;</mo><mn>5</mn><mo>&#8745;</mo><mi>x</mi><mo>&#62;</mo><mn>2</mn><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><mi>x</mi><mo>&#62;</mo><mn>2</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>4</mn></msup><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>5</mn></msup><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo></mrow><mrow><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#183;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>&#8734;</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mrow><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>4</mn></msup><mo>&#183;</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></mfrac><mfrac><mrow><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>5</mn><mn>6</mn></mfrac></mrow></mfrac></mfrac><mo>=</mo><msup><mfenced><mfrac><mn>5</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>25</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q20. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a game two players <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> take turns in throwing a pair of fair dice starting with player <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and total of scores on the two dice, in each throw is noted. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> wins the game if he throws a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> before <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> throws a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> wins the game if he throws a total of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> before <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> throws a total of six. The game stops as soon as either of the players wins. The probability of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> winning the game is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>31</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>61</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>61</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>30</mn><mn>61</mn></mfrac></math>**

**Detailed Solution:**

<p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>&#8594;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>5</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>5</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>3</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>2</mn><mo>)</mo></math>
Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#8594;</mo><mo>(</mo><mn>1</mn><mo>,</mo><mn>6</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>6</mn><mo>,</mo><mn>1</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>5</mn><mo>,</mo><mn>2</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>2</mn><mo>,</mo><mn>5</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>)</mo><mo>,</mo><mo>(</mo><mn>4</mn><mo>,</mo><mn>3</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>A</mi><mo>&#160;</mo><mtext>wins</mtext><mo>)</mo><mo>=</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>)</mo><mi>P</mi><mo>(</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p>We see that this is an infinite G.P. with common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mover><mi>A</mi><mo>&#175;</mo></mover><mo>)</mo><mo>&#215;</mo><mi>P</mi><mo>(</mo><mover><mi>B</mi><mo>&#175;</mo></mover><mo>)</mo></math></p><p>Thus, probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi></math> wins <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi mathvariant="normal">P</mi><mo>(</mo><mi mathvariant="normal">A</mi><mo>)</mo></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">P</mi><mo>(</mo><mover><mi mathvariant="normal">A</mi><mo>&#175;</mo></mover><mo>)</mo><mi mathvariant="normal">P</mi><mo>(</mo><mover><mi mathvariant="normal">B</mi><mo>&#175;</mo></mover><mo>)</mo></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mn>5</mn><mn>36</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>31</mn><mn>36</mn></mfrac><mo>&#183;</mo><mfrac><mn>30</mn><mn>36</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>30</mn><mn>61</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A die is thrown two times and the sum of the scores appearing on the die is observed to be a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>. Then the conditional probability that the score <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> has appeared at least once is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>A die is thrown two times.</p><p>Total number of possible outcomes<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>36</mn></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> is the event that sum of the score appearing on the die is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p><p>Possible outcomes in favor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced></mrow></mfenced></math>.</p><p>Number of favorable outcomes<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>E</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> is the event that at least one <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> appear.</p><p>Possible outcomes in favor of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>&#8745;</mo><mi>F</mi><mo>=</mo><mfenced close="}" open="{"><mfenced><mrow><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></mrow></mfenced></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>36</mn></mfrac></math>.</p><p>We have to find conditional probability of occurrence of at least one <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> given that sum of scores is multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>F</mi><mo>/</mo><mi>E</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>E</mi></mfenced></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>36</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>.</p>

</details>

---

### Q22. JEE Main 2020 (02 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>E</mi><mi>C</mi></msup></math> denote the complement of an event <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>3</mn></msub></math> be any pairwise independent events with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>&#62;</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced><mo>=</mo><mn>0</mn></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfenced><mrow><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup><mo>&#8745;</mo><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mrow></mfenced><mo>/</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>3</mn></msub></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mfenced><mo>-</mo><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mn>3</mn></msub></mfenced><mo>-</mo><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mfenced><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mfenced><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mfenced><mrow><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup><mo>&#8745;</mo><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mrow></mfenced><mo>/</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><mfenced><mrow><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup><mo>&#8745;</mo><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>P</mi><mo>(</mo><msub><mi>E</mi><mn>1</mn></msub><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>-</mo><mfenced open="{" close="}"><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced><mo>-</mo><mn>0</mn></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>&#8745;</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><msub><mi>E</mi><mn>1</mn></msub></mfenced></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>2</mn></msub><mo>/</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced><mrow><msub><mi>E</mi><mn>3</mn></msub><mo>/</mo><msub><mi>E</mi><mn>1</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>3</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>3</mn><mi>C</mi></msubsup></mfenced><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>2</mn></msub></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msubsup><mi>E</mi><mn>2</mn><mi>C</mi></msubsup></mfenced><mo>-</mo><mi>P</mi><mfenced><msub><mi>E</mi><mn>3</mn></msub></mfenced></math></p>

</details>

---

### Q23. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Box <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> cards numbered <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> and Box <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> cards numbered <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>. A box is selected at random and a card is drawn from it. The number on the card is found to be a non-prime number. The probability that the card was drawn from Box <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>17</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>17</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>17</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>B</mi><mn>1</mn></msub></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>=</mo><mi>P</mi><mfenced><msub><mi>B</mi><mn>2</mn></msub></mfenced></math></p><p>Box <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub></math> have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> non-prime numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>14</mn><mo>,</mo><mo>&#160;</mo><mn>15</mn><mo>,</mo><mo>&#160;</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mn>18</mn><mo>,</mo><mo>&#160;</mo><mn>20</mn><mo>,</mo><mo>&#160;</mo><mn>21</mn><mo>,</mo><mo>&#160;</mo><mn>22</mn><mo>,</mo><mo>&#160;</mo><mn>24</mn><mo>,</mo><mo>&#160;</mo><mn>25</mn><mo>,</mo><mo>&#160;</mo><mn>26</mn><mo>,</mo><mo>&#160;</mo><mn>27</mn><mo>,</mo><mo>&#160;</mo><mn>28</mn><mo>,</mo><mo>&#160;</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi><mo>/</mo><msub><mi>B</mi><mn>1</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>20</mn><mn>30</mn></mfrac></math></p><p>Box <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>B</mi><mn>1</mn></msub></math> have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> non-prime numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mn>32</mn><mo>,</mo><mo>&#160;</mo><mn>33</mn><mo>,</mo><mo>&#160;</mo><mn>34</mn><mo>,</mo><mo>&#160;</mo><mn>35</mn><mo>,</mo><mo>&#160;</mo><mn>36</mn><mo>,</mo><mo>&#160;</mo><mn>38</mn><mo>,</mo><mo>&#160;</mo><mn>39</mn><mo>,</mo><mo>&#160;</mo><mn>40</mn><mo>,</mo><mo>&#160;</mo><mn>42</mn><mo>,</mo><mo>&#160;</mo><mn>44</mn><mo>,</mo><mo>&#160;</mo><mn>45</mn><mo>,</mo><mo>&#160;</mo><mn>46</mn><mo>,</mo><mo>&#160;</mo><mn>48</mn><mo>,</mo><mo>&#160;</mo><mn>49</mn><mo>,</mo><mo>&#160;</mo><mn>50</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi><mo>/</mo><msub><mi>B</mi><mn>2</mn></msub></mrow></mfenced><mo>=</mo><mfrac><mn>15</mn><mn>20</mn></mfrac></math></p><p>Probability of non-prime<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><msub><mi>B</mi><mn>1</mn></msub></mfenced><mo>.</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi><mo>/</mo><msub><mi>B</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><msub><mi>B</mi><mn>2</mn></msub></mfenced><mo>.</mo><mi>P</mi><mfenced><mrow><mi>N</mi><mi>P</mi><mo>/</mo><msub><mi>B</mi><mn>2</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>20</mn><mn>30</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>15</mn><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><msub><mi>B</mi><mn>1</mn></msub><mo>/</mo><mi>N</mi><mi>P</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>20</mn><mn>30</mn></mfrac></mrow><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>20</mn><mn>30</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mfrac><mn>15</mn><mn>20</mn></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>17</mn></mfrac></math></p>

</details>

---

### Q24. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>A</mi></math> and <math><mi>B</mi></math> be two independent events such that <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math> and <math><mi>P</mi><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>.</mo></math> Then, which of the following is true?

**Options:**

- **(A)** <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mi>B</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mi>B</mi><mi>'</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi><mi>'</mi></mrow><mrow><mi>B</mi><mi>'</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mfenced separators="|"><mrow><mi>A</mi><mo>∪</mo><mi>B</mi></mrow></mfenced></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mi>B</mi><mi>'</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

A &amp; B are independent events, so
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>A</mi><msup><mi>B</mi><mi>&#39;</mi></msup></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>A</mi><mo>&#8745;</mo><msup><mi>B</mi><mo>&#39;</mo></msup><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><msup><mi>B</mi><mo>&#39;</mo></msup><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>&#183;</mo><mi>P</mi><mo>(</mo><msup><mi>B</mi><mo>&#39;</mo></msup><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><msup><mi>B</mi><mo>&#39;</mo></msup><mo>)</mo></mrow></mfrac><mo>=</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>

</details>

---

### Q25. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Assume that each born child is equally likely to be a boy or girl. If two families have two children each, then the conditional probability that all children are girls given that at least two are girls is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>12</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>11</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>17</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>11</mn></mfrac></math>**

**Detailed Solution:**

Family has four children in total.<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Total number of ways in which at least two girls are there</p><p>is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>4</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>+</mo><mn>4</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mo>+</mo><mn>4</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mo>=</mo><mn>11</mn></math></p><p>Favourable case in which all are girls is <math><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>P</mi><mo>=</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></math></p>

</details>

---

### Q26. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math><mi>A</mi></math> and <math><mi>B</mi><mi>&#160;</mi></math> be two non-null events such that <math><mi>A</mi><mo>&#8834;</mo><mi>B</mi><mo>.</mo></math> Then, which of the following statements is always correct?

**Options:**

- **(A)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>≥</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math>
- **(B)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced></math>
- **(C)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>≤</mo><mi> </mi><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math>
- **(D)** <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>≥</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math>**

**Detailed Solution:**

<p>Lets draw the venn diagram according to question, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/98480e4a-e9de-4d95-91f0-324fe32c9477-image6.png" /></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mfrac><mi>A</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><mi>B</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><mi>B</mi><mo>)</mo></mrow></mfrac><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>[</mo><mi>A</mi><mo>&#8834;</mo><mi>B</mi><mo>&#8658;</mo><mi>A</mi><mo>&#8745;</mo><mi>B</mi><mo>=</mo><mi>A</mi><mo>]</mo></math></p><p>Now, since <math><mi>P</mi><mo>(</mo><mi>B</mi><mo>)</mo><mo>&#8804;</mo><mn>1</mn></math></p><p><math><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>A</mi></mrow><mrow><mi>B</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>B</mi></mrow></mfenced></mrow></mfrac><mo>&#8805;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi></mrow></mfenced></math></p><p><math><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>|</mo><mi>B</mi></mrow></mfenced><mo>&#8805;</mo><mi>P</mi><mo>(</mo><mi>A</mi><mo>)</mo></math></p>

</details>

---

### Q27. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two integers are selected at random from the set $\{1,2, \ldots, 11\}$. Given that the sum of selected numbers is even, the conditional probability that both the numbers are even is :

**Options:**

- **(A)** $\frac{7}{10}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{3}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{5}$**

**Detailed Solution:**

Probability of getting sum of selected two numbers is even

$=P\left(E_{1}\right)=\frac{{ }^{5} C_{2}+{ }^{5} C_{2}}{{ }^{11} C_{2}}$

Probability of getting sum is even and selected numbers are also even $P\left(E_{2}\right)=\frac{{ }^{5} C_{2}}{{ }^{11} C_{2}}$

Hence, $P\left(\frac{E_{2}}{E_{1}}\right)=\frac{{ }^{5} C_{2}}{{ }^{6} C_{2}+{ }^{5} C_{2}}=\frac{10}{15+10}=\frac{2}{5}$.

</details>

---

### Q28. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `2`

A player $X$ has a biased coin whose probability of showing heads is $p$ and a player $Y$ has a fair coin. They start playing a game with their own coins and play alternately. The player who throws a head first is a winner. If $X$ starts the game, and the probability of winning the game by both the players is equal, then the value of ' $p$ ' is

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

If the outcome is one of the following: $H, T T H, T T T T H, \ldots$, then $X$ wins As subsequent tosses are independent, so the probability that $X$ wins is
$$
p+\frac{p}{4}+\frac{p}{16}+\ldots=\frac{4 p}{3} .
$$
Similarly $Y$ wins if the outcome is one of the following: $T H, T T T H, T T T T T H, \ldots$
Therefore, the probability that $Y$ wins is
$$
\frac{1-p}{2}+\frac{1-p}{8}+\frac{1-p}{32}=\frac{2(1-p)}{3}
$$
Since, the probability of winning the game by both the players is equal then, we have
$$
\frac{4 p}{3}=\frac{2(1-p)}{3} \Rightarrow p=\frac{1}{3}
$$

</details>

---

### Q29. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>F</mi></math> be two independent events. The probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>F</mi></math> happen is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math> and the probability that neither <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi></math> nor <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi></math> happens is <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> , then a value of <math><mfrac><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>E</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced separators="|"><mrow><mi>F</mi></mrow></mfenced></mrow></mfrac></math> is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>E</mi><mo>&#8745;</mo><mi>F</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mi>E</mi></mfenced><mo>.</mo><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mi>F</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>12</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced separators="|"><mrow><mover><mi>E</mi><mo>-</mo></mover><mo>&#8745;</mo><mover><mi>F</mi><mo>-</mo></mover></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mover><mi>E</mi><mo>-</mo></mover></mfenced><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mi>P</mi><mfenced separators="|"><mover><mi>F</mi><mo>-</mo></mover></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>E</mi></mfenced></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mi>F</mi></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>

<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mi>x</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>-</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mo>&#8658;</mo><mfrac><mrow><mn>12</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><mrow><mn>12</mn><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mn>12</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>12</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>x</mi><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mn>4</mn><mi>x</mi><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>1</mn><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi>&#160;</mi><mi>y</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mfrac><mn>1</mn><mn>3</mn></mfrac><mfrac><mn>1</mn><mn>4</mn></mfrac></mfrac><mo>&#160;</mo><mo>&#38;</mo><mi>&#160;</mi><mfrac><mfrac><mn>1</mn><mn>4</mn></mfrac><mfrac><mn>1</mn><mn>3</mn></mfrac></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>x</mi><mi>y</mi></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfrac><mstyle displaystyle="true"><mn>3</mn></mstyle><mstyle displaystyle="true"><mn>4</mn></mstyle></mfrac></math></p>

</details>

---

### Q30. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

Three persons P, Q and R independently try to hit a target. If the probabilities of their hitting the target are <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> and <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math> respectively, then the probability that the target is hit by P or Q but not by R is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>39</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>21</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let probability of hitting target by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>1</mn></msub></math> ,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>2</mn></msub></math> ,and by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>E</mi><mn>3</mn></msub></math></p><p>From the question Required probability is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><msub><mi>E</mi><mn>1</mn></msub><mo>)</mo><mi>P</mi><mo>(</mo><msub><mi>E</mi><mn>2</mn></msub><mo>)</mo><mi>P</mi><mo>(</mo><mover><msub><mi>E</mi><mn>3</mn></msub><mo>&#175;</mo></mover><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mover><msub><mi>E</mi><mn>1</mn></msub><mo>&#175;</mo></mover><mo>)</mo><mi>P</mi><mo>(</mo><msub><mi>E</mi><mn>2</mn></msub><mo>)</mo><mi>P</mi><mo>(</mo><mover><msub><mi>E</mi><mn>3</mn></msub><mo>&#175;</mo></mover><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><msub><mi>E</mi><mn>1</mn></msub><mo>)</mo><mi>P</mi><mo>(</mo><mover><msub><mi>E</mi><mn>2</mn></msub><mo>&#175;</mo></mover><mo>)</mo><mi>P</mi><mo>(</mo><mover><msub><mi>E</mi><mn>3</mn></msub><mo>&#175;</mo></mover><mo>)</mo></math><math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>12</mn><mo>+</mo><mn>9</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>21</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math></p>

</details>

---

### Q31. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `2`

For three events, <math><mi>A</mi><mo>,</mo><mi>&#160;</mi><mi>B</mi></math> and <math><mi>C</mi><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(Exactly one of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> occurs)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi></math>(Exactly one of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> occurs)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>P</mi></math>(Exactly one of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> occurs) <math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(All the three events occur simultaneously) <math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>.</mo></math>

Then the probability that at least one of the events occurs, is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>32</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>64</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/23ee4e96-1f15-40fb-af11-9a7c8333a6af-image.png" style="width: 247px; height: 170px;" /></p><p><math><mi>a</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>g</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>+</mo><mi>f</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>g</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>

Adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>+</mo><mi>g</mi><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math>

Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mi>a</mi><mo>+</mo><mfenced separators="|"><mrow><mi>b</mi><mo>+</mo><mi>c</mi><mo>+</mo><mi>d</mi><mo>+</mo><mi>e</mi><mo>+</mo><mi>f</mi><mo>+</mo><mi>g</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>P</mi><mfenced separators="|"><mrow><mi>A</mi><mo>&#8746;</mo><mi>B</mi><mo>&#8746;</mo><mi>C</mi></mrow></mfenced><mo>=</mo><mfrac><mn>7</mn><mn>16</mn></mfrac></math></p>

</details>

---

### Q32. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> identical balls are to be placed in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> identical boxes, then the probability that one of the boxes contains exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> balls is</p>

**Options:**

- **(A)** <math ><mn>22</mn><msup><mrow><mfenced separators="|"><mrow><mi> </mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi> </mi></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup></math>
- **(B)** <math ><mfrac><mrow><mn>5</mn></mrow><mrow><mn>19</mn></mrow></mfrac></math>
- **(C)** <math> <mrow> <mtext>55</mtext> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>2</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> </mrow> </msup> </mrow> </math>
- **(D)** <math> <mrow> <mtext>220</mtext> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </msup> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math ><mfrac><mrow><mn>5</mn></mrow><mrow><mn>19</mn></mrow></mfrac></math>**

**Detailed Solution:**

<strong>B<sub>1</sub>      B<sub>2</sub>      B<sub>3</sub></strong>

12      0         0

11       1        0

10       1        1

10       2        0

<u><strong>9         3        0</strong></u>

9         2        1

8         4        0

<u><strong>8         3        1</strong></u>

8         2        2

7         5        0

7         4        1

<u><strong>7        3         2</strong></u>

6        6         0

6        5         1

6        4         2

<u><strong>6        3         3</strong></u>

5        5        2

<u><strong>5         4        3</strong></u>

4         4        4

Total number of possibilities<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn></math>.

Number of favourable case <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math>

Required probability <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mrow><mn>1</mn><mn>9</mn></mrow></mfrac></math>

</details>

---

### Q33. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The probability of a man hitting a target is $\frac{2}{5}$. He fires at the target $k$ times $(k$, a given number). Then the minimum $k$, so that the probability of hitting the target at least once is more than $\frac{7}{10}$, is :

**Options:**

- **(A)** 3
- **(B)** 5
- **(C)** 2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{2}{5}+\frac{3}{5} \times \frac{2}{5}+\left(\frac{3}{5}\right)^2 \times \frac{2}{5}+\ldots \ldots+\left(\frac{3}{5}\right)^k \cdot \frac{2}{5}>\frac{7}{10} \\
\Rightarrow & \frac{2}{5}\left[1+\frac{3}{5}+\left(\frac{3}{5}\right)^2+\ldots \ldots+\left(\frac{3}{5}\right)^k\right]>\frac{7}{10} \\
\Rightarrow & \frac{2}{5} \times \frac{1-\left(\frac{3}{5}\right)^k}{1-\frac{3}{5}}>\frac{7}{10} \Rightarrow 1-\left(\frac{3}{5}\right)^k>\frac{7}{10} \\
\Rightarrow & \left(\frac{3}{5}\right)^k < \frac{3}{10} \Rightarrow k \geq 3
\end{aligned}
$$
Hence minimum value of $k=3$

</details>

---

### Q34. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

There are two balls in an urn. Each ball can be either white or black. If a white ball is put into the urn and there after a ball is drawn at random from the urn, then the probability that it is white is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

Total possible event when one ball is taken out $={ }^3 \mathrm{C}_1$ Let $E$ : The event of 1 white ball coming out
No. of ways to 1 white ball coming out $={ }^2 \mathrm{C}_1$
$$
\therefore P(E)=\frac{{ }^2 C_1}{{ }^3 C_1}=\frac{2}{3}
$$

</details>

---

### Q35. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If six students, including two particular students $A$ and $B$, stand in a row, then the probability that $A$ and $B$ are separated with one student in between them is

**Options:**

- **(A)** $\frac{8}{15}$
- **(B)** $\frac{4}{15}$
- **(C)** $\frac{2}{15}$
- **(D)** $\frac{1}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{15}$**

**Detailed Solution:**

Consider a group of three students $A, B$ and an other student in between $A$ and $B$. Choice for a student between $A$ and $B$ is 4. $A$ and $B$ can interchange their places in the group in 2 ways.
Now the group of three students (student $A$, student $B$ and a student in between $A$ and $B$ ) and the remaining 3 students can be stand in a row in 4 ! ways.
Hence total number of ways to stand in a row such that $A$ and $B$ are separated with one student in between them $=4 \times 2 \times 4$ !
Now total number of ways to stand 6 student stand in a row without any restriction $=6 !$
Hence required probability
$$
=\frac{4 \times 2 \times 4 !}{6 !}=\frac{4 \times 2}{6 \times 5}=\frac{4}{15}
$$

</details>

---

### Q36. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `2`

An urn contains nine balls of which three are red, four are blue and two are green. Three balls are drawn at random without replacement from the urn. The probability that the three balls have different colour is

**Options:**

- **(A)** $\frac{2}{7}$
- **(B)** $\frac{1}{21}$
- **(C)** $\frac{2}{23}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{7}$**

**Detailed Solution:**

$\mathrm{n}(\mathrm{S})={ }^9 \mathrm{C}_3$
$\mathrm{n}(\mathrm{E})={ }^3 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1 \times{ }^2 \mathrm{C}_1$
Probability $=\frac{3 \times 4 \times 2}{{ }^9 \mathrm{C}_3}=\frac{24 \times 3 !}{9 !} \times 6 !=\frac{24 \times 6}{9 \times 8 \times 7}=\frac{2}{7}$

</details>

---

### Q37. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `2`

A die is thrown. Let $A$ be the event that the number obtained is greater than 3 . Let $B$ be the event that the number obtained is less than 5 . Then $P(A \cup B)$ is

**Options:**

- **(A)** $\frac{3}{5}$
- **(B)** 0
- **(C)** 1
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

$$
A=\{4,5,6\}, B=\{1,2,3,4\} \text {. }
$$
Obviously $P(A \cup B)=1$.

</details>

---

### Q38. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The probability that A speaks truth is $\frac{4}{5}$, while this probability for $B$ is $\frac{3}{4}$. The probability that they contradict each other when asked to speak on a fact is

**Options:**

- **(A)** $\frac{3}{20}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{7}{20}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{20}$**

**Detailed Solution:**

$\mathrm{E}_1$ : event denoting that $A$ speaks truth
$\mathrm{E}_2$ : event denoting that $B$ speaks truth
Probability that both contradicts each other $=P\left(E_1 \cap \bar{E}_2\right)+P\left(\bar{E}_1 \cap E_2\right)=\frac{4}{5} \cdot \frac{1}{4}+\frac{1}{5} \cdot \frac{3}{4}=\frac{7}{20}$

</details>

---

### Q39. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

A problem in mathematics is given to three students $\mathrm{A}, \mathrm{B}, \mathrm{C}$ and their respective probability of solving the problem is $\frac{1}{2}, \frac{1}{3}$ and $\frac{1}{4}$. Probability that the problem is solved is

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{4}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/-eVnb22g7XX_lycm1EQs0Nr9Yfyh-ECsKSEZt7lsTNw.original.fullsize.png">

</details>

---

