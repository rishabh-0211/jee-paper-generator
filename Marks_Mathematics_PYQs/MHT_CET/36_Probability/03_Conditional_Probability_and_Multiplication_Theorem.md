# MHT CET Mathematics - Probability

## Topic 3: Conditional Probability and Multiplication Theorem

**Total Questions:** 35

---

### Q1. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two fair dice are tossed simultaneously. Let $A$ be the event that the sum of the numbers is prime, and $B$ be the event that at least one die shows a number 5. The odds against the occurrence of event $B$ given that event $A$ has already occurred is:

**Options:**

- **(A)** $11:4$
- **(B)** $11:15$
- **(C)** $11:7$
- **(D)** $4:11$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $11:4$**

**Detailed Solution:**

Total outcomes when two fair dice are tossed is $36$.

Event $A$: sum of the numbers is prime.
The possible prime sums are $2, 3, 5, 7, 11$.
Outcomes for sum $2$: $(1,1)$
Outcomes for sum $3$: $(1,2), (2,1)$
Outcomes for sum $5$: $(1,4), (2,3), (3,2), (4,1)$
Outcomes for sum $7$: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$
Outcomes for sum $11$: $(5,6), (6,5)$
Total number of outcomes in $A$, $n(A) = 1 + 2 + 4 + 6 + 2 = 15$.

Event $B$: at least one die shows a $5$.
Outcomes in $A \cap B$ (sum is prime and at least one die shows $5$): $(2,5), (5,2), (5,6), (6,5)$.
Total number of outcomes in $A \cap B$, $n(A \cap B) = 4$.

The number of outcomes in $A$ where $B$ does not occur is $n(A \cap B') = n(A) - n(A \cap B) = 15 - 4 = 11$.

The odds against the occurrence of event $B$ given that event $A$ has already occurred is the ratio of the number of unfavorable outcomes to the number of favorable outcomes within the reduced sample space $A$.

Odds against $B|A = n(A \cap B') : n(A \cap B) = 11 : 4$.

Answer: $11:4$

</details>

---

### Q2. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A man is known to speak the truth in $75\%$ of cases. If he throws an unbiased die and tells his friend that it is a six. Assuming that when he tells a lie, he specifically reports the result as a six, the probability that it is actually a six is...

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{5}{9}$
- **(C)** $\dfrac{3}{8}$
- **(D)** $\dfrac{8}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{3}{8}$**

**Detailed Solution:**

Let $S$ be the event that a six is rolled on the die.

Let $S'$ be the event that a six is not rolled.

Let $E$ be the event that the man reports a six.

The probability of rolling a six is $P(S) = \dfrac{1}{6}$.

The probability of not rolling a six is $P(S') = \dfrac{5}{6}$.

If a six is actually rolled, the man reports a six if he speaks the truth. Thus, $P(E|S) = \dfrac{75}{100} = \dfrac{3}{4}$.

If a six is not rolled, the man reports a six if he lies. Since it is given that when he lies he specifically reports a six, $P(E|S') = \dfrac{25}{100} = \dfrac{1}{4}$.

Using Bayes' theorem, the probability that it is actually a six given that he reports a six is:

$P(S|E) = \dfrac{P(S)P(E|S)}{P(S)P(E|S) + P(S')P(E|S')}$

Substituting the values:

$P(S|E) = \dfrac{\dfrac{1}{6} \times \dfrac{3}{4}}{\dfrac{1}{6} \times \dfrac{3}{4} + \dfrac{5}{6} \times \dfrac{1}{4}}$

$P(S|E) = \dfrac{\dfrac{3}{24}}{\dfrac{3}{24} + \dfrac{5}{24}}$

$P(S|E) = \dfrac{3}{8}$

Answer: $\dfrac{3}{8}$

</details>

---

### Q3. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $P(X)$ and $F(X)$ are the probability mass function and cumulative distribution function of discrete random variable $X$ where $X=\{0, 1, 2, 3,\ldots, 10\}$ and $a, b$ are integers such that $0<a<b<10$, then the conditional probability $P(X\geq a\,/\,X\leq b)$ is equal to ...

**Options:**

- **(A)** $1-\dfrac{F(a-1)}{F(b)}$
- **(B)** $1-\dfrac{F(a)}{F(b)}$
- **(C)** $1-\dfrac{F(a)}{F(b-1)}$
- **(D)** $1-\dfrac{F(a-1)}{F(b-1)}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1-\dfrac{F(a-1)}{F(b)}$**

**Detailed Solution:**

The conditional probability is given by the formula:

$P(X \geq a \mid X \leq b) = \dfrac{P(X \geq a \cap X \leq b)}{P(X \leq b)}$

Since $a < b$, the intersection of the events $X \geq a$ and $X \leq b$ is $a \leq X \leq b$.

The probability of this intersection is:

$P(a \leq X \leq b) = P(X \leq b) - P(X \leq a-1)$

Using the definition of the cumulative distribution function, $F(x) = P(X \leq x)$, we can write:

$P(a \leq X \leq b) = F(b) - F(a-1)$

The probability of the condition is:

$P(X \leq b) = F(b)$

Substituting these into the conditional probability formula gives:

$P(X \geq a \mid X \leq b) = \dfrac{F(b) - F(a-1)}{F(b)}$

$P(X \geq a \mid X \leq b) = 1 - \dfrac{F(a-1)}{F(b)}$

Answer: $1-\dfrac{F(a-1)}{F(b)}$

</details>

---

### Q4. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A fair die is rolled indefinitely. Player A wins if two consecutive rolls show 3 or 5, and player B wins if two consecutive rolls show 1 or 2 or 4 or 6. The probability that player A wins in the long run is

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{5}{21}$
- **(C)** $\dfrac{1}{7}$
- **(D)** $\dfrac{2}{21}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{5}{21}$**

**Detailed Solution:**

Let $S$ be the event of rolling a $3$ or $5$. The probability of this event is $P(S) = \dfrac{2}{6} = \dfrac{1}{3}$.

Let $F$ be the event of rolling a $1, 2, 4,$ or $6$. The probability of this event is $P(F) = \dfrac{4}{6} = \dfrac{2}{3}$.

Let $P$ be the probability that player A wins the game.
Let $P_S$ be the probability that player A wins given that the previous roll was $S$.
Let $P_F$ be the probability that player A wins given that the previous roll was $F$.

From the start of the game, the first roll is either $S$ or $F$:
$P = \dfrac{1}{3} P_S + \dfrac{2}{3} P_F$

If the previous roll was $S$, rolling another $S$ means A wins immediately. Rolling an $F$ transitions the state to $F$:
$P_S = \dfrac{1}{3}(1) + \dfrac{2}{3} P_F$

If the previous roll was $F$, rolling another $F$ means B wins immediately (so A's chance of winning becomes $0$). Rolling an $S$ transitions the state to $S$:
$P_F = \dfrac{1}{3} P_S + \dfrac{2}{3}(0) = \dfrac{1}{3} P_S$

Substituting $P_F$ into the equation for $P_S$:
$P_S = \dfrac{1}{3} + \dfrac{2}{3} \left( \dfrac{1}{3} P_S \right)$

$P_S = \dfrac{1}{3} + \dfrac{2}{9} P_S$

$\left( 1 - \dfrac{2}{9} \right) P_S = \dfrac{1}{3}$

$\dfrac{7}{9} P_S = \dfrac{1}{3} \Rightarrow P_S = \dfrac{3}{7}$

Now, find $P_F$:
$P_F = \dfrac{1}{3} \left( \dfrac{3}{7} \right) = \dfrac{1}{7}$

Finally, substitute $P_S$ and $P_F$ back into the equation for $P$:
$P = \dfrac{1}{3} \left( \dfrac{3}{7} \right) + \dfrac{2}{3} \left( \dfrac{1}{7} \right)$

$P = \dfrac{1}{7} + \dfrac{2}{21} = \dfrac{3}{21} + \dfrac{2}{21} = \dfrac{5}{21}$

Answer: $\dfrac{5}{21}$

</details>

---

### Q5. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Bag A contains 3 white and 5 black balls while bag B contains 4 white and 3 black balls. A ball is selected at random from bag A and put in bag B. If a ball is now selected at random from bag B then the probability that this ball is white ball is...

**Options:**

- **(A)** $\dfrac{20}{64}$
- **(B)** $\dfrac{31}{64}$
- **(C)** $\dfrac{35}{64}$
- **(D)** $\dfrac{32}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{35}{64}$**

**Detailed Solution:**

Let $E_1$ be the event that a white ball is transferred from bag A to bag B.

Let $E_2$ be the event that a black ball is transferred from bag A to bag B.

Let $W$ be the event that a white ball is drawn from bag B.

The probability of transferring a white ball from bag A is:

$P(E_1) = \dfrac{3}{8}$

The probability of transferring a black ball from bag A is:

$P(E_2) = \dfrac{5}{8}$

If $E_1$ occurs, bag B will contain 5 white and 3 black balls. The probability of drawing a white ball is:

$P(W|E_1) = \dfrac{5}{8}$

If $E_2$ occurs, bag B will contain 4 white and 4 black balls. The probability of drawing a white ball is:

$P(W|E_2) = \dfrac{4}{8}$

By the theorem of total probability:

$P(W) = P(E_1)P(W|E_1) + P(E_2)P(W|E_2)$

$P(W) = \left(\dfrac{3}{8}\right)\left(\dfrac{5}{8}\right) + \left(\dfrac{5}{8}\right)\left(\dfrac{4}{8}\right)$

$P(W) = \dfrac{15}{64} + \dfrac{20}{64} = \dfrac{35}{64}$

Answer: $\dfrac{35}{64}$

</details>

---

### Q6. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In an entrance test, there are multiple choice questions. There are four possible answers to each question, only one of which is correct. The probability that a student knows the answer to a question is 90%. If he gets the correct answer to a question, then the probability that he was guessing is

**Options:**

- **(A)** $\dfrac{37}{40}$
- **(B)** $\dfrac{1}{37}$
- **(C)** $\dfrac{36}{37}$
- **(D)** $\dfrac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{37}$**

**Detailed Solution:**

Let $E_1$ be the event that the student knows the answer and $E_2$ be the event that the student guesses the answer.

$P(E_1) = \dfrac{90}{100} = \dfrac{9}{10}$

$P(E_2) = 1 - P(E_1) = \dfrac{1}{10}$

Let $A$ be the event that the student gets the correct answer.

If the student knows the answer, the probability of getting it correct is $1$, so $P(A|E_1) = 1$.

If the student guesses, since there are $4$ options and only $1$ is correct, the probability of getting it correct is $\dfrac{1}{4}$, so $P(A|E_2) = \dfrac{1}{4}$.

By Bayes' theorem, the probability that the student was guessing given that he got the correct answer is:

$P(E_2|A) = \dfrac{P(E_2)P(A|E_2)}{P(E_1)P(A|E_1) + P(E_2)P(A|E_2)}$

$P(E_2|A) = \dfrac{\dfrac{1}{10} \times \dfrac{1}{4}}{\dfrac{9}{10} \times 1 + \dfrac{1}{10} \times \dfrac{1}{4}}$

$P(E_2|A) = \dfrac{\dfrac{1}{40}}{\dfrac{36}{40} + \dfrac{1}{40}} = \dfrac{1}{37}$

Answer: $\dfrac{1}{37}$

</details>

---

### Q7. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If A and B are two events such that $P(A) = \dfrac{2}{3}$, $P(B) = \dfrac{1}{2}$ and $P(A \mid B) = \dfrac{2}{3}$, then $P(A' \cup B) + P(A \cup B') = $

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $1$
- **(C)** $\dfrac{3}{2}$
- **(D)** $\dfrac{5}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{3}{2}$**

**Detailed Solution:**

Given $P(A) = \dfrac{2}{3}$, $P(B) = \dfrac{1}{2}$, $P(A \mid B) = \dfrac{2}{3}$

$P(A \cap B) = P(A \mid B) P(B) = \dfrac{2}{3} \times \dfrac{1}{2} = \dfrac{1}{3}$

$P(A' \cup B) = 1 - P(A \cap B') = 1 - (P(A) - P(A \cap B))$

$P(A' \cup B) = 1 - \left(\dfrac{2}{3} - \dfrac{1}{3}\right) = \dfrac{2}{3}$

$P(A \cup B') = 1 - P(A' \cap B) = 1 - (P(B) - P(A \cap B))$

$P(A \cup B') = 1 - \left(\dfrac{1}{2} - \dfrac{1}{3}\right) = \dfrac{5}{6}$

$P(A' \cup B) + P(A \cup B') = \dfrac{2}{3} + \dfrac{5}{6} = \dfrac{9}{6} = \dfrac{3}{2}$

</details>

---

### Q8. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If events A and B are such that $P(A) = \dfrac{1}{4}$, $P(A \cap B) = \dfrac{1}{10}$ and $P(A/B) = 2P(B/A)$ then $P(B) = $...........

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{5}$
- **(C)** $\dfrac{1}{8}$
- **(D)** $\dfrac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{8}$**

**Detailed Solution:**

Given $P(A) = \dfrac{1}{4}$ and $P(A \cap B) = \dfrac{1}{10}$

Using the definition of conditional probability:

$P(A/B) = \dfrac{P(A \cap B)}{P(B)}$

$P(B/A) = \dfrac{P(A \cap B)}{P(A)}$

Substituting these into the given relation $P(A/B) = 2P(B/A)$:

$\dfrac{P(A \cap B)}{P(B)} = 2\dfrac{P(A \cap B)}{P(A)}$

Since $P(A \cap B) \neq 0$, we can cancel it from both sides:

$\dfrac{1}{P(B)} = \dfrac{2}{P(A)}$

$P(B) = \dfrac{P(A)}{2}$

Substituting $P(A) = \dfrac{1}{4}$:

$P(B) = \dfrac{1}{4 \times 2} = \dfrac{1}{8}$

Answer: $\dfrac{1}{8}$

</details>

---

### Q9. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The cumulative distribution function of a discrete random variable X is
\(\begin{array}{|r|c|c|c|c|c|c|c|c|} \hline \mathrm{X}=x & -4 & -2 & 0 & 2 & 4 & 6 & 8 & 10 \\ \hline \mathrm{~F}(\mathrm{X}=x) & 0.1 & 0.3 & 0.5 & 0.65 & 0.75 & 0.85 & 0.90 & 1 \\ \hline \end{array}\)
then $\frac{P(X \leqslant 0)}{P(X>0)}=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 1
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1**

**Detailed Solution:**

From the given table of the cumulative distribution function, $F(x) = P(X \leqslant x)$.

We have $P(X \leqslant 0) = F(0) = 0.5$.

The probability $P(X > 0)$ is given by $1 - P(X \leqslant 0)$.

$P(X > 0) = 1 - 0.5 = 0.5$.

Therefore, $\dfrac{P(X \leqslant 0)}{P(X>0)} = \dfrac{0.5}{0.5} = 1$.

Answer: 1

</details>

---

### Q10. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A family has 3 children. The probability that all the three children are girls, given that at least one of them is a girl is

**Options:**

- **(A)** $\frac{7}{8}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{1}{7}$
- **(D)** $\frac{2}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{7}$**

**Detailed Solution:**

Let $S$ be the sample space of genders of 3 children.

$n(S) = 2^3 = 8$

Let $A$ be the event that all three children are girls.

$A = \{GGG\} \Rightarrow n(A) = 1$

Let $B$ be the event that at least one child is a girl.

$B$ includes all outcomes except all boys ($BBB$).

$n(B) = 8 - 1 = 7$

We need to find the probability of $A$ given $B$, which is $P(A|B)$.

$A \cap B = \{GGG\} \Rightarrow n(A \cap B) = 1$

$P(A|B) = \dfrac{n(A \cap B)}{n(B)} = \dfrac{1}{7}$

Answer: $\frac{1}{7}$

</details>

---

### Q11. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four defective oranges are accidentally mixed with sixteen good ones. Three oranges are drawn from the mixed lot. The probability distribution of defective oranges is

**Options:**

- **(A)** \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{28}{57} & \frac{8}{95} & \frac{8}{19} & \frac{1}{285} \\ \hline \end{array}\)
- **(B)** \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{28}{57} & \frac{8}{19} & \frac{8}{95} & \frac{1}{285} \\ \hline \end{array}\)
- **(C)** \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{28}{57} & \frac{8}{95} & \frac{1}{285} & \frac{8}{19} \\ \hline \end{array}\)
- **(D)** \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{285} & \frac{8}{95} & \frac{8}{19} & \frac{28}{57} \\ \hline \end{array}\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{28}{57} & \frac{8}{19} & \frac{8}{95} & \frac{1}{285} \\ \hline \end{array}\)**

**Detailed Solution:**

Total number of oranges = $4$ (defective) + $16$ (good) = $20$.

Number of oranges drawn = $3$.

Total number of ways to draw $3$ oranges = $^{20}C_{3} = \dfrac{20 \times 19 \times 18}{3 \times 2 \times 1} = 1140$.

Let $X$ be the number of defective oranges drawn. $X$ can take values $0, 1, 2, 3$.

$P(X = 0) = \dfrac{^{4}C_{0} \times ^{16}C_{3}}{^{20}C_{3}} = \dfrac{1 \times 560}{1140} = \dfrac{28}{57}$

$P(X = 1) = \dfrac{^{4}C_{1} \times ^{16}C_{2}}{^{20}C_{3}} = \dfrac{4 \times 120}{1140} = \dfrac{480}{1140} = \dfrac{8}{19}$

$P(X = 2) = \dfrac{^{4}C_{2} \times ^{16}C_{1}}{^{20}C_{3}} = \dfrac{6 \times 16}{1140} = \dfrac{96}{1140} = \dfrac{8}{95}$

$P(X = 3) = \dfrac{^{4}C_{3} \times ^{16}C_{0}}{^{20}C_{3}} = \dfrac{4 \times 1}{1140} = \dfrac{1}{285}$

Answer: \(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{28}{57} & \frac{8}{19} & \frac{8}{95} & \frac{1}{285} \\ \hline \end{array}\)

</details>

---

### Q12. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three urns respectively contain 2 white and 3 black, 3 white and 2 black and 1 white and 4 black balls. If one ball is drawn from each urn, then the probability that the selection contains 1 black and 2 white balls is

**Options:**

- **(A)** $\frac{13}{125}$
- **(B)** $\frac{37}{125}$
- **(C)** $\frac{28}{125}$
- **(D)** $\frac{33}{125}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{37}{125}$**

**Detailed Solution:**

Let $W_i$ and $B_i$ denote the events of drawing a white and a black ball from the $i$-th urn respectively, for $i = 1, 2, 3$.

From the given data:
$P(W_1) = \dfrac{2}{5}$, $P(B_1) = \dfrac{3}{5}$
$P(W_2) = \dfrac{3}{5}$, $P(B_2) = \dfrac{2}{5}$
$P(W_3) = \dfrac{1}{5}$, $P(B_3) = \dfrac{4}{5}$

The probability of selecting exactly 2 white and 1 black ball is the sum of the probabilities of three mutually exclusive cases:

$P(W_1 \cap W_2 \cap B_3) + P(W_1 \cap B_2 \cap W_3) + P(B_1 \cap W_2 \cap W_3)$

$= P(W_1)P(W_2)P(B_3) + P(W_1)P(B_2)P(W_3) + P(B_1)P(W_2)P(W_3)$

$= \left(\dfrac{2}{5} \times \dfrac{3}{5} \times \dfrac{4}{5}\right) + \left(\dfrac{2}{5} \times \dfrac{2}{5} \times \dfrac{1}{5}\right) + \left(\dfrac{3}{5} \times \dfrac{3}{5} \times \dfrac{1}{5}\right)$

$= \dfrac{24}{125} + \dfrac{4}{125} + \dfrac{9}{125}$

$= \dfrac{37}{125}$

Answer: $\frac{37}{125}$

</details>

---

### Q13. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A coin is tossed until one head appears or a tail appears 4 times in succession. The probability distribution of the number of tosses is

**Options:**

- **(A)** <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{2}$ </td> <td>$\frac{1}{4}$ </td> </tr> </tbody> </table>
- **(B)** <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{4}$ </td> <td>$\frac{1}{2}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{8}$ </td> </tr> </tbody> </table>
- **(C)** <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{4}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{2}$ </td> </tr> </tbody> </table>
- **(D)** <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{2}$ </td> <td>$\frac{1}{4}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{8}$ </td> </tr> </tbody> </table>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{2}$ </td> <td>$\frac{1}{4}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{8}$ </td> </tr> </tbody> </table>**

**Detailed Solution:**

Let $X$ denote the number of tosses. The possible values of $X$ are $1, 2, 3, 4$.

For $X = 1$, the first toss must be a head.
$P(X = 1) = P(H) = \dfrac{1}{2}$

For $X = 2$, the first toss is a tail and the second is a head.
$P(X = 2) = P(TH) = \dfrac{1}{2} \times \dfrac{1}{2} = \dfrac{1}{4}$

For $X = 3$, the first two tosses are tails and the third is a head.
$P(X = 3) = P(TTH) = \dfrac{1}{2} \times \dfrac{1}{2} \times \dfrac{1}{2} = \dfrac{1}{8}$

For $X = 4$, the first three tosses are tails. The fourth toss can be either a head or a tail, as both will terminate the experiment (either a head appears or four tails appear in succession).
$P(X = 4) = P(TTTH) + P(TTTT) = \left(\dfrac{1}{2}\right)^4 + \left(\dfrac{1}{2}\right)^4 = \dfrac{1}{16} + \dfrac{1}{16} = \dfrac{1}{8}$

The probability distribution is $X = 1, 2, 3, 4$ with probabilities $\dfrac{1}{2}, \dfrac{1}{4}, \dfrac{1}{8}, \dfrac{1}{8}$ respectively.

Answer: <table> <thead> <tr> <th>X </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}(\mathrm{X}=x)$ </td> <td>$\frac{1}{2}$ </td> <td>$\frac{1}{4}$ </td> <td>$\frac{1}{8}$ </td> <td>$\frac{1}{8}$ </td> </tr> </tbody> </table>

</details>

---

### Q14. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $\mathrm{k}=1,2,3$ the box $\mathrm{B}_{\mathrm{k}}$ contains k red balls and $(\mathrm{k}+1)$ white balls. Let $\mathrm{P}\left(\mathrm{B}_1\right)=\frac{1}{2}, \mathrm{P}\left(\mathrm{B}_2\right)=\frac{1}{3}$ and $\mathrm{P}\left(\mathrm{B}_3\right)=\frac{1}{6}$. A box is selected at random and a ball is drawn from it. If a red ball is drawn from it, then the probability that it comes from box $B_2$ is

**Options:**

- **(A)** $\frac{35}{78}$
- **(B)** $\frac{14}{39}$
- **(C)** $\frac{10}{13}$
- **(D)** $\frac{12}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{14}{39}$**

**Detailed Solution:**

Let $E_1, E_2, E_3$ be the events of selecting boxes $B_1, B_2, B_3$ respectively, and $R$ be the event of drawing a red ball.

Given probabilities of selecting the boxes are:
$P(E_1) = \dfrac{1}{2}$, $P(E_2) = \dfrac{1}{3}$, $P(E_3) = \dfrac{1}{6}$

The number of red and white balls in box $B_k$ is $k$ and $k+1$ respectively. The probability of drawing a red ball from each box is:
$P(R|E_1) = \dfrac{1}{1+2} = \dfrac{1}{3}$

$P(R|E_2) = \dfrac{2}{2+3} = \dfrac{2}{5}$

$P(R|E_3) = \dfrac{3}{3+4} = \dfrac{3}{7}$

By Bayes' theorem, the probability that the red ball came from box $B_2$ is:
$P(E_2|R) = \dfrac{P(E_2)P(R|E_2)}{P(E_1)P(R|E_1) + P(E_2)P(R|E_2) + P(E_3)P(R|E_3)}$

Substituting the values:
$P(E_2|R) = \dfrac{\dfrac{1}{3} \times \dfrac{2}{5}}{\left(\dfrac{1}{2} \times \dfrac{1}{3}\right) + \left(\dfrac{1}{3} \times \dfrac{2}{5}\right) + \left(\dfrac{1}{6} \times \dfrac{3}{7}\right)}$

$P(E_2|R) = \dfrac{\dfrac{2}{15}}{\dfrac{1}{6} + \dfrac{2}{15} + \dfrac{1}{14}}$

Taking the LCM of the denominators $6, 15,$ and $14$, which is $210$:
$P(E_2|R) = \dfrac{\dfrac{28}{210}}{\dfrac{35}{210} + \dfrac{28}{210} + \dfrac{15}{210}}$

$P(E_2|R) = \dfrac{28}{35 + 28 + 15}$

$P(E_2|R) = \dfrac{28}{78} = \dfrac{14}{39}$

Answer: $\frac{14}{39}$

</details>

---

### Q15. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X has the following probability distribution
A random variable X has the following probability distribution
\(\begin{array}{|r|c|c|c|c|c|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}): & \mathrm{k} & 2 \mathrm{k} & 4 \mathrm{k} & 2 \mathrm{k} & \mathrm{k} \\
\hline
\end{array}\)
then the value of \(\mathrm{P}(1 \leqslant \mathrm{X}<4 / \mathrm{X} \leqslant 2)=\)

**Options:**

- **(A)** $\frac{5}{6}$
- **(B)** $\frac{6}{7}$
- **(C)** $\frac{7}{8}$
- **(D)** $\frac{8}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{6}{7}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is always $1$.

$\sum P(X) = k + 2k + 4k + 2k + k = 1$

$10k = 1 \Rightarrow k = \dfrac{1}{10}$

We need to find the conditional probability $P(1 \leqslant X < 4 \mid X \leqslant 2)$.

By the definition of conditional probability:

$P(1 \leqslant X < 4 \mid X \leqslant 2) = \dfrac{P((1 \leqslant X < 4) \cap (X \leqslant 2))}{P(X \leqslant 2)}$

The values of $X$ satisfying $1 \leqslant X < 4$ are $1, 2, 3$.

The values of $X$ satisfying $X \leqslant 2$ are $0, 1, 2$.

The intersection of these two conditions gives $X = 1, 2$.

Therefore, the required probability is:

$P(1 \leqslant X < 4 \mid X \leqslant 2) = \dfrac{P(X = 1) + P(X = 2)}{P(X = 0) + P(X = 1) + P(X = 2)}$

Substituting the given probabilities in terms of $k$:

$P(1 \leqslant X < 4 \mid X \leqslant 2) = \dfrac{2k + 4k}{k + 2k + 4k}$

$P(1 \leqslant X < 4 \mid X \leqslant 2) = \dfrac{6k}{7k} = \dfrac{6}{7}$

Answer: $\frac{6}{7}$

</details>

---

### Q16. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A$ and $B$ are independent events with $P(B)=\frac{2}{5}, P(A \cup B)=\frac{11}{20}$, then $\mathrm{P}\left(\mathrm{A}^{\prime} \mid \mathrm{B}\right)$ is root of the equation

**Options:**

- **(A)** $4 x^2-7 x+3=0$
- **(B)** $4 x^2+7 x+3=0$
- **(C)** $4 x^2-3 x-7=0$
- **(D)** $6 x^2-5 x+1=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4 x^2-7 x+3=0$**

**Detailed Solution:**

Since $A$ and $B$ are independent events, $A'$ and $B$ are also independent.

Therefore, $P(A' \mid B) = P(A')$.

We know that $P(A \cup B) = 1 - P(A' \cap B')$.

Since $A'$ and $B'$ are independent, $P(A' \cap B') = P(A')P(B')$.

Given $P(B) = \dfrac{2}{5}$, we have $P(B') = 1 - \dfrac{2}{5} = \dfrac{3}{5}$.

Substituting the values in the formula:

$\dfrac{11}{20} = 1 - P(A') \times \dfrac{3}{5}$

$P(A') \times \dfrac{3}{5} = 1 - \dfrac{11}{20} = \dfrac{9}{20}$

$P(A') = \dfrac{9}{20} \times \dfrac{5}{3} = \dfrac{3}{4}$

Thus, $P(A' \mid B) = \dfrac{3}{4}$.

Substituting $x = \dfrac{3}{4}$ in $4x^2 - 7x + 3 = 0$:

$4\left(\dfrac{3}{4}\right)^2 - 7\left(\dfrac{3}{4}\right) + 3 = 4\left(\dfrac{9}{16}\right) - \dfrac{21}{4} + 3 = \dfrac{9}{4} - \dfrac{21}{4} + \dfrac{12}{4} = 0$

Hence, $P(A' \mid B)$ is a root of $4x^2 - 7x + 3 = 0$.

Answer: $4 x^2-7 x+3=0$

</details>

---

### Q17. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A box contains 9 tickets numbered 1 to 9 both inclusive. If 3 tickets are drawn from the box one at a time, then the probability that they are alternatively either {odd, even, odd} or {even, odd, even} is

**Options:**

- **(A)** $\frac{5}{17}$
- **(B)** $\frac{4}{17}$
- **(C)** $\frac{5}{16}$
- **(D)** $\frac{5}{18}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5}{18}$**

**Detailed Solution:**

The box contains 9 tickets numbered 1 to 9.

Number of odd tickets = 5 (1, 3, 5, 7, 9)

Number of even tickets = 4 (2, 4, 6, 8)

The tickets are drawn one at a time without replacement.

The probability of drawing tickets in the order {odd, even, odd} is:

$P(OEO) = \dfrac{5}{9} \times \dfrac{4}{8} \times \dfrac{4}{7} = \dfrac{80}{504} = \dfrac{10}{63}$

The probability of drawing tickets in the order {even, odd, even} is:

$P(EOE) = \dfrac{4}{9} \times \dfrac{5}{8} \times \dfrac{3}{7} = \dfrac{60}{504} = \dfrac{5}{42}$

The total probability is the sum of these two probabilities:

$P = P(OEO) + P(EOE) = \dfrac{10}{63} + \dfrac{5}{42}$

$P = \dfrac{20}{126} + \dfrac{15}{126} = \dfrac{35}{126}$

$P = \dfrac{5}{18}$

Answer: $\frac{5}{18}$

</details>

---

### Q18. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Numbers are selected at random, one at a time from two digit numbers $10,11,12 \ldots ., 99$ with replacement. An event E occurs if and only if the product of the two digits of a selected number is 18 . If four numbers are selected, then probability that the event E occurs at least 3 times is

**Options:**

- **(A)** $\frac{87}{90^4}$
- **(B)** $\frac{348}{90^4}$
- **(C)** $\quad 87\left(\frac{4}{90}\right)^4$
- **(D)** $\left(\frac{4}{10}\right)^4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad 87\left(\frac{4}{90}\right)^4$**

**Detailed Solution:**

Total number of two-digit numbers from $10$ to $99$ is $99 - 10 + 1 = 90$.

Let $E$ be the event that the product of the digits of the selected number is $18$. The possible pairs of digits whose product is $18$ are $(2, 9)$ and $(3, 6)$.

The two-digit numbers satisfying this condition are $29, 92, 36,$ and $63$.

Number of favorable outcomes = $4$.

Probability of success $p = P(E) = \dfrac{4}{90}$.

Probability of failure $q = 1 - p = 1 - \dfrac{4}{90} = \dfrac{86}{90}$.

Four numbers are selected, so the number of trials $n = 4$.

The probability that event $E$ occurs at least $3$ times is given by $P(X \ge 3) = P(X = 3) + P(X = 4)$.

Using the binomial distribution formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X \ge 3) = ^{4}C_{3} p^3 q^1 + ^{4}C_{4} p^4 q^0$

$P(X \ge 3) = 4 \left(\dfrac{4}{90}\right)^3 \left(\dfrac{86}{90}\right) + 1 \left(\dfrac{4}{90}\right)^4$

$P(X \ge 3) = \left(\dfrac{4}{90}\right)^3 \left( \dfrac{4 \times 86}{90} + \dfrac{4}{90} \right)$

$P(X \ge 3) = \left(\dfrac{4}{90}\right)^3 \left( \dfrac{344 + 4}{90} \right)$

$P(X \ge 3) = \left(\dfrac{4}{90}\right)^3 \left( \dfrac{348}{90} \right)$

$P(X \ge 3) = \left(\dfrac{4}{90}\right)^3 \left( 87 \times \dfrac{4}{90} \right)$

$P(X \ge 3) = 87 \left(\dfrac{4}{90}\right)^4$

Answer: $\quad 87\left(\frac{4}{90}\right)^4$

</details>

---

### Q19. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four fair dice are thrown independently 27 times. Then the expected number of times, at least two dice show up a three or a five is

**Options:**

- **(A)** 11
- **(B)** 12
- **(C)** 9
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

Let $p$ be the probability of getting a $3$ or a $5$ on a single throw of a fair die.

$p = \dfrac{2}{6} = \dfrac{1}{3}$

The probability of not getting a $3$ or a $5$ is $q = 1 - p = \dfrac{2}{3}$.

Let $X$ be the number of dice showing a $3$ or a $5$ when $4$ dice are thrown. The probability that at least two dice show a $3$ or a $5$ is $P(X \ge 2)$.

$P(X \ge 2) = 1 - P(X = 0) - P(X = 1)$

$P(X = 0) = ^{4}C_{0} \left(\dfrac{1}{3}\right)^0 \left(\dfrac{2}{3}\right)^4 = \dfrac{16}{81}$

$P(X = 1) = ^{4}C_{1} \left(\dfrac{1}{3}\right)^1 \left(\dfrac{2}{3}\right)^3 = 4 \times \dfrac{1}{3} \times \dfrac{8}{27} = \dfrac{32}{81}$

$P(X \ge 2) = 1 - \left(\dfrac{16}{81} + \dfrac{32}{81}\right) = 1 - \dfrac{48}{81} = \dfrac{33}{81} = \dfrac{11}{27}$

The expected number of times this event occurs in $27$ independent throws is given by $N \times P(X \ge 2)$, where $N = 27$.

Expected value $= 27 \times \dfrac{11}{27} = 11$

Answer: 11

</details>

---

### Q20. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A multiple choice examination has 5 questions. Each question has three alternative answers of which exactly one is correct. The probability that a student will get 4 or more correct answers just by guessing is

**Options:**

- **(A)** $\frac{17}{243}$
- **(B)** $\frac{13}{243}$
- **(C)** $\frac{11}{243}$
- **(D)** $\frac{10}{243}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{11}{243}$**

**Detailed Solution:**

Let $X$ be the number of correct answers.

Number of questions, $n = 5$

Probability of a correct answer by guessing, $p = \dfrac{1}{3}$

Probability of a wrong answer, $q = 1 - p = \dfrac{2}{3}$

The probability of getting 4 or more correct answers is $P(X \ge 4) = P(X = 4) + P(X = 5)$.

Using the binomial distribution formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X = 4) = ^{5}C_{4} \left(\dfrac{1}{3}\right)^4 \left(\dfrac{2}{3}\right)^1 = 5 \times \dfrac{1}{81} \times \dfrac{2}{3} = \dfrac{10}{243}$

$P(X = 5) = ^{5}C_{5} \left(\dfrac{1}{3}\right)^5 \left(\dfrac{2}{3}\right)^0 = 1 \times \dfrac{1}{243} \times 1 = \dfrac{1}{243}$

$P(X \ge 4) = \dfrac{10}{243} + \dfrac{1}{243} = \dfrac{11}{243}$

Answer: $\frac{11}{243}$

</details>

---

### Q21. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains 4 Red and 6 Black balls. A ball is drawn at random from the bag, its colour is observed and this ball along with 3 additional balls of the same colour are returned to the bag. If now a ball is drawn at random from the bag, then the probability that this drawn ball is red is

**Options:**

- **(A)** $\dfrac{41}{65}$
- **(B)** $\dfrac{24}{65}$
- **(C)** $\dfrac{26}{65}$
- **(D)** $\dfrac{28}{65}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{26}{65}$**

**Detailed Solution:**

Let $E_1$ be the event that the first ball drawn is red and $E_2$ be the event that the first ball drawn is black.

$P(E_1) = \dfrac{4}{10}$

$P(E_2) = \dfrac{6}{10}$

Let $A$ be the event that the second ball drawn is red.

If $E_1$ occurs, $3$ additional red balls are added. The bag now contains $7$ red and $6$ black balls.

$P(A|E_1) = \dfrac{7}{13}$

If $E_2$ occurs, $3$ additional black balls are added. The bag now contains $4$ red and $9$ black balls.

$P(A|E_2) = \dfrac{4}{13}$

By the law of total probability:

$P(A) = P(E_1)P(A|E_1) + P(E_2)P(A|E_2)$

$P(A) = \dfrac{4}{10} \times \dfrac{7}{13} + \dfrac{6}{10} \times \dfrac{4}{13}$

$P(A) = \dfrac{28}{130} + \dfrac{24}{130} = \dfrac{52}{130} = \dfrac{26}{65}$

Answer: $\dfrac{26}{65}$

</details>

---

### Q22. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A lot of 100 bulbs contains 10 defective bulbs. Five bulbs are selected at random from the lot and are sent to retail store. Then the probability that the store will receive at most one defective bulb is

**Options:**

- **(A)** $\frac{7}{5}\left(\frac{9}{10}\right)^4$
- **(B)** $\frac{7}{5}\left(\frac{9}{10}\right)^5$
- **(C)** $\frac{6}{5}\left(\frac{9}{10}\right)^4$
- **(D)** $\frac{6}{5}\left(\frac{9}{10}\right)^5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{7}{5}\left(\frac{9}{10}\right)^4$**

**Detailed Solution:**

Let $\mathrm{X}$ denote the number of defective bulbs. $\mathrm{p}=$ Probability that a bulb is defective
$\begin{aligned}
& =\frac{10}{100}=\frac{1}{10} \\
& q=1-p=1-\frac{1}{10}=\frac{9}{10} \\
& P(X=r)={ }^5 C_r\left(\frac{1}{10}\right)^r\left(\frac{9}{10}\right)^{5-r}, r=0,1, \ldots, 5
\end{aligned}$
$\begin{aligned}
\therefore \quad & P(X \leq 1) \\
& =P(X=0)+P(X=1) \\
& ={ }^5 C_0\left(\frac{1}{10}\right)^0\left(\frac{9}{10}\right)^5+{ }^5 C_1\left(\frac{1}{10}\right)^1\left(\frac{9}{10}\right)^4 \\
& =\left(\frac{9}{10}\right)^5+5 \times \frac{1}{10} \times\left(\frac{9}{10}\right)^4 \\
& =\frac{7}{5}\left(\frac{9}{10}\right)^4
\end{aligned}$

</details>

---

### Q23. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three critics review a book. For the three critics the odds in favour of the book are $2: 5$, $3: 4$ and $4: 3$ respectively. The probability that the majority is in favour of the book, is given by

**Options:**

- **(A)** $\frac{183}{343}$
- **(B)** $\frac{160}{343}$
- **(C)** $\frac{209}{343}$
- **(D)** $\frac{134}{343}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{134}{343}$**

**Detailed Solution:**

The probability that the first critic favours the book is $\mathrm{P}(\mathrm{A})=\frac{2}{2+5}=\frac{2}{7}$
$$
\therefore \quad \mathrm{P}\left(\mathrm{A}^{\prime}\right)=1-\frac{2}{7}=\frac{5}{7}
$$

The probability that the second critic favours the book is $\mathrm{P}(\mathrm{B})=\frac{3}{3+4}=\frac{3}{7}$
$$
\therefore \quad \mathrm{P}\left(\mathrm{B}^{\prime}\right)=1-\frac{3}{7}=\frac{4}{7}
$$

The probability that the third critic favours the book is $\mathrm{P}(\mathrm{C})=\frac{4}{4+3}=\frac{4}{7}$
$$
\therefore \quad \mathrm{P}\left(\mathrm{C}^{\prime}\right)=1-\frac{4}{7}=\frac{3}{7}
$$
$\therefore \quad$ Majority will be in favour of the book if at least two critics favour the book.
Hence, the probability is
$\begin{aligned} & \mathrm{P}\left(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C}^{\prime}\right)+\mathrm{P}\left(\mathrm{A} \cap \mathrm{B}^{\prime} \cap \mathrm{C}\right) \\ & \quad+\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B} \cap \mathrm{C}\right)+\mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C}) \\ & =\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}\left(\mathrm{C}^{\prime}\right)+\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}\left(\mathrm{B}^{\prime}\right) \cdot \mathrm{P}(\mathrm{C}) \\ & +\mathrm{P}\left(\mathrm{A}^{\prime}\right) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}(\mathrm{C})+\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}(\mathrm{C})\end{aligned}$
$\begin{aligned} & =\frac{2}{7} \times \frac{3}{7} \times \frac{3}{7}+\frac{2}{7} \times \frac{4}{7} \times \frac{4}{7}+\frac{5}{7} \times \frac{3}{7} \times \frac{4}{7}+\frac{2}{7} \times \frac{3}{7} \times \frac{4}{7} \\ & =\frac{18}{343}+\frac{32}{343}+\frac{60}{343}+\frac{24}{343} \\ & =\frac{134}{343}\end{aligned}$

</details>

---

### Q24. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\mathrm{A}, \mathrm{B}, \mathrm{C}$ are three events, one of which must and only one can happen. The odds in favor of $A$ are $4: 6$, the odds against B are $7: 3$. Thus, odds against $\mathrm{C}$ are

**Options:**

- **(A)** $7:3$
- **(B)** $4:6$
- **(C)** $6:4$
- **(D)** $3:7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7:3$**

**Detailed Solution:**

Odd in favor of $\mathrm{A}$ is $4: 6$.
$\therefore \quad \mathrm{P}(\mathrm{A})=\frac{4}{10}$
Odd against $\mathrm{B}$ is $7: 3$
$\therefore \quad \mathrm{P}(\mathrm{B})=\frac{3}{10}$
Since only one of the events A, B and C can happen, we get
$\begin{array}{ll} 
& \mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})+\mathrm{P}(\mathrm{C})=1 \\
\therefore & \frac{4}{10}+\frac{3}{10}+\mathrm{P}(\mathrm{C})=1 \\
\therefore & \mathrm{P}(\mathrm{C})=\frac{3}{10} \\
\therefore \quad & \mathrm{P}\left(\mathrm{C}^{\prime}\right)=\frac{7}{10}
\end{array}$
$\therefore \quad$ odds against the event $\mathrm{C}$ are $\mathrm{P}\left(\mathrm{C}^{\prime}\right): \mathrm{P}(\mathrm{C})$
$\begin{aligned}
& =\frac{7}{10}: \frac{3}{10} \\
& =7: 3
\end{aligned}$

</details>

---

### Q25. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{P}(\mathrm{A})=\frac{3}{10}, \mathrm{P}(\mathrm{B})=\frac{3}{5}, \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{3}{5}$, then $\mathrm{P}(\mathrm{A} / \mathrm{B}) \times \mathrm{P}(\mathrm{B} / \mathrm{A})=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{12}$
- **(C)** $\frac{1}{10}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{12}$**

**Detailed Solution:**

$$
\mathrm{P}\left(\frac{\mathrm{A}}{\mathrm{B}}\right) \times \mathrm{P}\left(\frac{\mathrm{B}}{\mathrm{A}}\right)=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{B})} \times \frac{\mathrm{P}(\mathrm{B} \cap \mathrm{A})}{\mathrm{P}(\mathrm{A})}
$$
We know that $\mathrm{P}(\mathrm{A} \cup \mathrm{B})=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B})$
$$
\begin{aligned}
& \frac{3}{5}=\frac{3}{10}+\frac{2}{5}-\mathrm{P}(\mathrm{A} \cap \mathrm{B}) \Rightarrow \mathrm{P}(\mathrm{A} \cap \mathrm{B})=\frac{1}{10} \\
& \therefore \text { Given expression }=\frac{\left(\frac{1}{10}\right)}{\left(\frac{2}{5}\right)} \times \frac{\left(\frac{1}{10}\right)}{\left(\frac{3}{10}\right)}=\frac{1}{4} \times \frac{1}{3}=\frac{1}{12}
\end{aligned}
$$

</details>

---

### Q26. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A problem in statistics is given to three students $\mathrm{P}, \mathrm{Q}$ and $\mathrm{R}$. Their chances of solving
the problem are $\frac{1}{2}, \frac{1}{3}, \frac{1}{4}$ respectively. If all of them try independently, then the
probability that the problem is solved, is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{4}$**

**Detailed Solution:**

(B)
P (Problem will be solved)
$=1-\mathrm{P}$ (Problem will not be solved by $\mathrm{P}, \mathrm{Q} \& \mathrm{R}$ )
$=1-\left[\left(1-\frac{1}{2}\right)\left(1-\frac{1}{3}\right)\left(1-\frac{1}{4}\right)\right]$ $=1-\left(\frac{1}{2} \times \frac{2}{3} \times \frac{3}{4}\right)=1-\frac{1}{4}=\frac{3}{4}$

</details>

---

### Q27. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $P\left(A^{\prime}\right)=0 \cdot 6, P(B)=0 \cdot 8$ and $P(B / A)=0 \cdot 3$, then $P(A / B)=$

**Options:**

- **(A)** $\frac{7}{20}$
- **(B)** $\frac{3}{20}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{9}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{20}$**

**Detailed Solution:**

Given $P\left(A^{\prime}\right)=0.6 \Rightarrow P(A)=1-0.6=0.4, P(B)=0.8, P(B / A)=0.3$ 
We know that $\mathrm{P}(\mathrm{B} / \mathrm{A})=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{A})}$ and $\mathrm{P}(\mathrm{A} / \mathrm{B})=\frac{\mathrm{P}(\mathrm{A} \cap \mathrm{B})}{\mathrm{P}(\mathrm{B})}$
Here $P(A \cap B)=P(A) \cdot P(B / A)=(0.4)(0.3)=0.12$
Also $\quad P(A \cap B)=P(A / B) \cdot P(B)$
$\therefore \mathrm{P}(\mathrm{A} / \mathrm{B})=\frac{0.12}{0.8}=\frac{12}{80}=\frac{3}{20}$

</details>

---

### Q28. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that the person who undergoes certain operation will survive is $0 \cdot 2 .$
If 5 patients undergo similar operations, then the probability that exactly four will survive is

**Options:**

- **(A)** $0.0042$
- **(B)** $0.0084$
- **(C)** $0 \cdot 0032$
- **(D)** $0 \cdot 0064$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0 \cdot 0064$**

**Detailed Solution:**

Since there are 5 patients, n = 5
P(Pprobability of patient survive) = 0.2
$\begin{aligned} \quad & p-0.2 \Rightarrow q=1-p=1-0.2=08 \\ & P(x=4)={ }^{5} C_{4}(0.2)^{4}(0.8)^{1}=5 \times 0.0016 \times 0.8=0.0064 \end{aligned}$

</details>

---

### Q29. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A multiple choice examination has 5 questions. Each question has three alternative answers of which exactly one is correct. The probability that a student will get at least one correct answer is

**Options:**

- **(A)** $\frac{80}{243}$
- **(B)** $\frac{32}{243}$
- **(C)** $\frac{163}{243}$
- **(D)** $\frac{211}{243}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{211}{243}$**

**Detailed Solution:**

There are 5 questions and each question has 3 options of which one is correct. $\therefore$ Probability of getting correct answer $=\frac{1}{3}$
Thus $\mathrm{n}=5, \mathrm{p}=\frac{1}{3}, \mathrm{q}=\frac{2}{3}$
$P$ (at least one correct answer)
$=1-P($ None is correct $)$
$=1-{ }^{5} C_{0}\left(\frac{1}{3}\right)^{0}\left(\frac{2}{3}\right)^{5}=1-1 \times 1 \times \frac{32}{243}$ $=\frac{243-32}{243}=\frac{211}{243}$

</details>

---

### Q30. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

An urn contains 4 red and 5 white balls. Two balls are drawn one after the other
without replacement, then the probability that both the balls are red is

**Options:**

- **(A)** $\frac{5}{6}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{4}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{6}$**

**Detailed Solution:**

Red balls $=4$ and White balls $=5 \Rightarrow$ Total balls $=4+5=9$ Two balls are drawn one after the other without replacement
$n(S)={ }^{9} C_{1} \times{ }^{8} C_{1}=9 \times 8$
$\text { Required probability }=\frac{{ }^{4} C_{1} \times{ }^{3} C_{1}}{9 \times 8}=\frac{4 \times 3}{9 \times 8}=\frac{1}{3 \times 2}=\frac{1}{6}$

</details>

---

### Q31. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a person wins a prize on a lottery ticket is $\frac{1}{4} .$ If he purchases
5 lottery tickets at random, then the probability that he wins at least one prize is

**Options:**

- **(A)** $\frac{121}{1024}$
- **(B)** $\frac{774}{1024}$
- **(C)** $\frac{781}{1024}$
- **(D)** $\frac{223}{1024}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{781}{1024}$**

**Detailed Solution:**

$\operatorname{Var}(x)=E\left(x^{2}\right)-[E(x)]^{2}$
$0.96=1-[E(x)]^{2} \Rightarrow[E(x)]^{2}=1-0.96=0.04 \quad \therefore E(x)=0.2$

</details>

---

### Q32. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two cards are drawn from a pack of well shuffled 52 playing cards one by one without replacement. Then the probability that both cards are queens is

**Options:**

- **(A)** $\frac{1}{221}$
- **(B)** $\frac{1}{220}$
- **(C)** $\frac{3}{220}$
- **(D)** $\frac{2}{221}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{221}$**

**Detailed Solution:**

Two cards are drawn from a pack of 52 cards without replacement. Total queen cards are 4
$\begin{array}{l}
\therefore P\left(1^{\text {st }} \text { queen card }\right)=\frac{4}{52} \text { and } P\left(2^{\text {nd }} \text { queen card }\right)=\frac{3}{51} \\
\therefore \text { Required probability }=\frac{4 \times 3}{52 \times 51}=\frac{1}{221}
\end{array}$

</details>

---

### Q33. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

If $E_{1}$ denotes the events of coming sum 6 in throwing two dice and $E_{2}$ be the event of coming 2 in any one of the two, then $P\left(E_{2} / \mathrm{E}_{1}\right.$ ) is

**Options:**

- **(A)** $1 / 5$
- **(B)** $4 / 5$
- **(C)** $3 / 5$
- **(D)** $2 / 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 / 5$**

**Detailed Solution:**

$E_{1}$ can occur as $\{(1,5),(5,1,),(2,4),(4,2),$,
$(3,3)\}$
$$
\begin{array}{l}
E_{2} \text { -as }\{(2,1),(2,2),(2,3),(2,4),(2,5),(2,6), \\
(6,2),(5,2),(4,2),(3,2),(1,2)\}
\end{array}
$$
$\therefore \quad P\left(E_{2} / E_{1}\right)=$ Probability of $E_{2}$ when $E_{1}$ has occured
$$
=2 / 5
$$

</details>

---

### Q34. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `2`

Three boxes contain respectively 3 white and 1 black, 2 white and 2 black, 1 white and 3 black balls, from each of the boxes one ball is drawn at random. The probability that 2 white and 1 black balls will be drawn, is

**Options:**

- **(A)** $13 / 12$
- **(B)** $1 / 4$
- **(C)** $1 / 32$
- **(D)** $3 / 16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $13 / 12$**

**Detailed Solution:**

Given, Box $(\mathrm{I})=3 W, 1 B ;$ Box $(\mathrm{II})=2 W, 2 B ;$ Box
$$
(\mathrm{III})=1 W, 3 B .
$$
$\therefore$ Required probability
$$
\begin{array}{l}
=P(B W W)+P(W B W)+P(W W B) \\
=P(B) P(W) P(W)+P(W) P(B) P(W) \\
\quad+P(W) P(W) P(B) \\
=\frac{1}{4} \times \frac{2}{4} \times \frac{1}{4}+\frac{3}{4} \times \frac{2}{4} \times \frac{1}{4}+\frac{3}{4} \times \frac{2}{4} \times \frac{3}{4} \\
=\frac{2+6+18}{64}=\frac{26}{64} \\
=\frac{13}{32}
\end{array}
$$

</details>

---

### Q35. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

Given $P(A)=0.5, P(B)=0.4, P(A \cap B)=0.3$,
then $P\left(A^{\prime} / B^{\prime}\right)$ is equal to

**Options:**

- **(A)** $1 / 3$
- **(B)** $1 / 2$
- **(C)** $2 / 3$
- **(D)** $3 / 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2 / 3$**

**Detailed Solution:**

$$
\text {  } \begin{aligned}
P\left(A^{\prime} \mid B^{\prime}\right)=& \frac{P\left(A^{\prime} \cap B^{\prime}\right)}{P\left(B^{\prime}\right)} \\
&=\frac{P(A \cup B)^{\prime}}{P\left(B^{\prime}\right)} \\
&=\frac{1-P(A \cup B)}{1-P(B)} \\
&=\frac{1-[P(A)+P(B)-P(A \cap B)]}{1-P(B)} \\
&=\frac{1-[0.5+0.4-0.3]}{1-0.4} \\
&=\frac{0.4}{0.6} \\
&=\frac{2}{3}
\end{aligned}
$$

</details>

---

