# MHT CET Mathematics - Probability

## Topic 4: Independent Events

**Total Questions:** 17

---

### Q1. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A husband and wife appeared for an interview for two vacancies in an office. The probability of the husband's selection is $\dfrac{1}{5}$ and that of the wife's selection is $\dfrac{1}{7}$, then the probability that exactly one of them is selected is...

**Options:**

- **(A)** $\dfrac{1}{35}$
- **(B)** $\dfrac{11}{35}$
- **(C)** $\dfrac{2}{7}$
- **(D)** $\dfrac{1}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{7}$**

**Detailed Solution:**

Let $H$ be the event that the husband is selected and $W$ be the event that the wife is selected.

Given $P(H) = \dfrac{1}{5}$ and $P(W) = \dfrac{1}{7}$.

The probability that the husband is not selected is $P(H') = 1 - \dfrac{1}{5} = \dfrac{4}{5}$.

The probability that the wife is not selected is $P(W') = 1 - \dfrac{1}{7} = \dfrac{6}{7}$.

The probability that exactly one of them is selected is given by $P(H \cap W') + P(H' \cap W)$.

Since the events are independent, this is equal to $P(H)P(W') + P(H')P(W)$.

Substituting the values, we get $\dfrac{1}{5} \times \dfrac{6}{7} + \dfrac{4}{5} \times \dfrac{1}{7} = \dfrac{6}{35} + \dfrac{4}{35} = \dfrac{10}{35} = \dfrac{2}{7}$.

Answer: $\dfrac{2}{7}$

</details>

---

### Q2. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three ships A, B, C sail from England to India. If the odds in favour of their safe arrival are 2:5, 3:7 and 6:11 respectively, then the probability that the exactly two ships arrive safely is

**Options:**

- **(A)** $\dfrac{24}{119}$
- **(B)** $\dfrac{24}{1190}$
- **(C)** $\dfrac{66}{1190}$
- **(D)** $\dfrac{84}{1190}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{24}{119}$**

**Detailed Solution:**

Let $P(A)$, $P(B)$, and $P(C)$ be the probabilities of safe arrival for ships A, B, and C respectively.

Given the odds in favour of their safe arrival, we can find their probabilities:
$P(A) = \dfrac{2}{2+5} = \dfrac{2}{7} \Rightarrow P(\bar{A}) = 1 - \dfrac{2}{7} = \dfrac{5}{7}$

$P(B) = \dfrac{3}{3+7} = \dfrac{3}{10} \Rightarrow P(\bar{B}) = 1 - \dfrac{3}{10} = \dfrac{7}{10}$

$P(C) = \dfrac{6}{6+11} = \dfrac{6}{17} \Rightarrow P(\bar{C}) = 1 - \dfrac{6}{17} = \dfrac{11}{17}$

The probability that exactly two ships arrive safely is the sum of the probabilities of three mutually exclusive cases: A and B arrive but C does not, A and C arrive but B does not, and B and C arrive but A does not.

Required probability $= P(A)P(B)P(\bar{C}) + P(A)P(\bar{B})P(C) + P(\bar{A})P(B)P(C)$

Substituting the values:
$= \left(\dfrac{2}{7} \times \dfrac{3}{10} \times \dfrac{11}{17}\right) + \left(\dfrac{2}{7} \times \dfrac{7}{10} \times \dfrac{6}{17}\right) + \left(\dfrac{5}{7} \times \dfrac{3}{10} \times \dfrac{6}{17}\right)$

$= \dfrac{66}{1190} + \dfrac{84}{1190} + \dfrac{90}{1190}$

$= \dfrac{66 + 84 + 90}{1190}$

$= \dfrac{240}{1190} = \dfrac{24}{119}$

Answer: $\dfrac{24}{119}$

</details>

---

### Q3. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability that event A happens in a trial is 0.4. If three independent trials are made, then the probability that A happens at least once is.......

**Options:**

- **(A)** $0.216$
- **(B)** $0.926$
- **(C)** $0.064$
- **(D)** $0.784$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.784$**

**Detailed Solution:**

Let $P(A)$ be the probability that event A happens in a single trial.

$P(A) = 0.4$

The probability that event A does not happen in a single trial is $P(A') = 1 - 0.4 = 0.6$.

Since the trials are independent, the probability that A does not happen in any of the three trials is $(P(A'))^3 = (0.6)^3 = 0.216$.

The probability that A happens at least once in three trials is $1 - P(\text{A does not happen in any trial})$.

$1 - 0.216 = 0.784$

Answer: $0.784$

</details>

---

### Q4. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $A$ and $B$ are independent events such that $P\left(A \cap B^{\prime}\right)=\frac{3}{25}$ and $\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)=\frac{8}{25}$, then $\mathrm{P}(\mathrm{A})=$

**Options:**

- **(A)** $\frac{3}{8}$
- **(B)** $\frac{4}{5}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{5}$**

**Detailed Solution:**

Let $P(A) = x$ and $P(B) = y$.

Since $A$ and $B$ are independent events, $A$ and $B'$ are independent, and $A'$ and $B$ are independent.

$P(A \cap B') = P(A)P(B') = x(1 - y) = \dfrac{3}{25}$

$P(A' \cap B) = P(A')P(B) = (1 - x)y = \dfrac{8}{25}$

Subtracting the first equation from the second, we get:

$(1 - x)y - x(1 - y) = \dfrac{8}{25} - \dfrac{3}{25}$

$y - xy - x + xy = \dfrac{5}{25}$

$y - x = \dfrac{1}{5} \Rightarrow y = x + \dfrac{1}{5}$

Substituting $y$ in the first equation:

$x\left(1 - x - \dfrac{1}{5}\right) = \dfrac{3}{25}$

$x\left(\dfrac{4}{5} - x\right) = \dfrac{3}{25}$

$\dfrac{4x}{5} - x^2 = \dfrac{3}{25}$

$25x^2 - 20x + 3 = 0$

$(5x - 1)(5x - 3) = 0$

$x = \dfrac{1}{5}$ or $x = \dfrac{3}{5}$

Since $\dfrac{3}{5}$ is not in the given options, $P(A) = \dfrac{1}{5}$.

Answer: $\frac{1}{5}$

</details>

---

### Q5. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two friends A and B apply independently for a job in the same company. The probabilities of A getting selected is $\frac{2}{5}$ and that of B is $\frac{4}{7}$. Then the probability, that exactly one of them is selected, is

**Options:**

- **(A)** $\frac{8}{35}$
- **(B)** $\frac{18}{35}$
- **(C)** $\frac{26}{35}$
- **(D)** $\frac{34}{35}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{18}{35}$**

**Detailed Solution:**

Let $A$ and $B$ be the events that friend A and friend B are selected, respectively.

$P(A) = \dfrac{2}{5}$

$P(B) = \dfrac{4}{7}$

$P(A') = 1 - P(A) = 1 - \dfrac{2}{5} = \dfrac{3}{5}$

$P(B') = 1 - P(B) = 1 - \dfrac{4}{7} = \dfrac{3}{7}$

Since the events are independent, the probability that exactly one of them is selected is given by:

$P(A \cap B') + P(A' \cap B) = P(A)P(B') + P(A')P(B)$

$= \left(\dfrac{2}{5} \times \dfrac{3}{7}\right) + \left(\dfrac{3}{5} \times \dfrac{4}{7}\right)$

$= \dfrac{6}{35} + \dfrac{12}{35}$

$= \dfrac{18}{35}$

Answer: $\frac{18}{35}$

</details>

---

### Q6. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three persons $\mathrm{P}, \mathrm{Q}$ and R independently try to hit a target. If the probabilities of their hitting the target are $\frac{3}{4}, \frac{1}{2}$ and $\frac{5}{8}$ respectively, then the probability that the target is hit by P or Q but not by $R$, is

**Options:**

- **(A)** $\frac{15}{64}$
- **(B)** $\frac{21}{64}$
- **(C)** $\frac{39}{64}$
- **(D)** $\frac{9}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{21}{64}$**

**Detailed Solution:**

Let the events that P, Q, and R hit the target be $A$, $B$, and $C$ respectively.

Given probabilities are:
$P(A) = \dfrac{3}{4} \Rightarrow P(A') = \dfrac{1}{4}$
$P(B) = \dfrac{1}{2} \Rightarrow P(B') = \dfrac{1}{2}$
$P(C) = \dfrac{5}{8} \Rightarrow P(C') = \dfrac{3}{8}$

The probability that the target is hit by P or Q is given by $P(A \cup B)$.
$P(A \cup B) = 1 - P(A' \cap B')$

Since the events are independent:
$P(A \cup B) = 1 - P(A')P(B') = 1 - \left(\dfrac{1}{4} \times \dfrac{1}{2}\right) = 1 - \dfrac{1}{8} = \dfrac{7}{8}$

The probability that the target is hit by P or Q but not by R is $P((A \cup B) \cap C')$.

Since $A \cup B$ and $C'$ are independent events:
$P((A \cup B) \cap C') = P(A \cup B) \times P(C') = \dfrac{7}{8} \times \dfrac{3}{8} = \dfrac{21}{64}$

Answer: $\frac{21}{64}$

</details>

---

### Q7. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{A}, \mathrm{B}$ and C be three events, which are pairwise independent and $\overline{\mathrm{E}}$ denote the complement of an event E . If $\mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C})=0$ and $\mathrm{P}(\mathrm{C})\gt0$, then $\mathrm{P}((\overline{\mathrm{A}} \cap \overline{\mathrm{B}}) / C)$ is equal to

**Options:**

- **(A)** $\quad \mathrm{P}(\mathrm{A})+\mathrm{P}(\overline{\mathrm{B}})$
- **(B)** $\quad \mathrm{P}(\overline{\mathrm{A}})-\mathrm{P}(\overline{\mathrm{B}})$
- **(C)** $\quad \mathrm{P}(\overline{\mathrm{A}})-\mathrm{P}(\mathrm{B})$
- **(D)** $\quad \mathrm{P}(\overline{\mathrm{A}})+\mathrm{P}(\overline{\mathrm{B}})$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\quad \mathrm{P}(\overline{\mathrm{A}})-\mathrm{P}(\mathrm{B})$**

**Detailed Solution:**

By the definition of conditional probability:

$\mathrm{P}((\overline{\mathrm{A}} \cap \overline{\mathrm{B}}) / \mathrm{C}) = \dfrac{\mathrm{P}(\overline{\mathrm{A}} \cap \overline{\mathrm{B}} \cap \mathrm{C})}{\mathrm{P}(\mathrm{C})}$

Using De Morgan's laws, $\overline{\mathrm{A}} \cap \overline{\mathrm{B}} = \overline{\mathrm{A} \cup \mathrm{B}}$. Thus, the numerator can be written as:

$\mathrm{P}(\overline{\mathrm{A}} \cap \overline{\mathrm{B}} \cap \mathrm{C}) = \mathrm{P}(\mathrm{C} \cap \overline{\mathrm{A} \cup \mathrm{B}}) = \mathrm{P}(\mathrm{C}) - \mathrm{P}(\mathrm{C} \cap (\mathrm{A} \cup \mathrm{B}))$

By the distributive property of sets and the addition rule for probabilities:

$\mathrm{P}(\mathrm{C} \cap (\mathrm{A} \cup \mathrm{B})) = \mathrm{P}((\mathrm{C} \cap \mathrm{A}) \cup (\mathrm{C} \cap \mathrm{B}))$

$\mathrm{P}(\mathrm{C} \cap (\mathrm{A} \cup \mathrm{B})) = \mathrm{P}(\mathrm{C} \cap \mathrm{A}) + \mathrm{P}(\mathrm{C} \cap \mathrm{B}) - \mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C})$

Since $\mathrm{A}$, $\mathrm{B}$, and $\mathrm{C}$ are pairwise independent, we have:

$\mathrm{P}(\mathrm{C} \cap \mathrm{A}) = \mathrm{P}(\mathrm{C})\mathrm{P}(\mathrm{A})$

$\mathrm{P}(\mathrm{C} \cap \mathrm{B}) = \mathrm{P}(\mathrm{C})\mathrm{P}(\mathrm{B})$

We are also given that $\mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C}) = 0$. Substituting these values:

$\mathrm{P}(\mathrm{C} \cap (\mathrm{A} \cup \mathrm{B})) = \mathrm{P}(\mathrm{C})\mathrm{P}(\mathrm{A}) + \mathrm{P}(\mathrm{C})\mathrm{P}(\mathrm{B}) - 0 = \mathrm{P}(\mathrm{C})(\mathrm{P}(\mathrm{A}) + \mathrm{P}(\mathrm{B}))$

Therefore, the numerator becomes:

$\mathrm{P}(\overline{\mathrm{A}} \cap \overline{\mathrm{B}} \cap \mathrm{C}) = \mathrm{P}(\mathrm{C}) - \mathrm{P}(\mathrm{C})(\mathrm{P}(\mathrm{A}) + \mathrm{P}(\mathrm{B})) = \mathrm{P}(\mathrm{C})(1 - \mathrm{P}(\mathrm{A}) - \mathrm{P}(\mathrm{B}))$

Now, substituting this back into the conditional probability formula:

$\mathrm{P}((\overline{\mathrm{A}} \cap \overline{\mathrm{B}}) / \mathrm{C}) = \dfrac{\mathrm{P}(\mathrm{C})(1 - \mathrm{P}(\mathrm{A}) - \mathrm{P}(\mathrm{B}))}{\mathrm{P}(\mathrm{C})}$

$\mathrm{P}((\overline{\mathrm{A}} \cap \overline{\mathrm{B}}) / \mathrm{C}) = 1 - \mathrm{P}(\mathrm{A}) - \mathrm{P}(\mathrm{B})$

Using the property of complementary events, $1 - \mathrm{P}(\mathrm{A}) = \mathrm{P}(\overline{\mathrm{A}})$. Hence:

$\mathrm{P}((\overline{\mathrm{A}} \cap \overline{\mathrm{B}}) / \mathrm{C}) = \mathrm{P}(\overline{\mathrm{A}}) - \mathrm{P}(\mathrm{B})$

Answer: $\quad \mathrm{P}(\overline{\mathrm{A}})-\mathrm{P}(\mathrm{B})$

</details>

---

### Q8. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If A and B are two independent events such that $\mathrm{P}\left(\mathrm{A}^{\prime}\right)=0.75^{\circ}, \mathrm{P}(\mathrm{A} \cup \mathrm{B})=0.65$ and $\mathrm{P}(\mathrm{B})=\mathrm{p}$, then value of $p$ is

**Options:**

- **(A)** $\frac{9}{14}$
- **(B)** $\frac{7}{15}$
- **(C)** $\frac{5}{14}$
- **(D)** $\frac{8}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{8}{15}$**

**Detailed Solution:**

Given $P(A') = 0.75$, we have $P(A) = 1 - P(A') = 1 - 0.75 = 0.25$.

Since $A$ and $B$ are independent events, $P(A \cap B) = P(A)P(B) = 0.25p$.

Using the formula for the union of two events:

$P(A \cup B) = P(A) + P(B) - P(A \cap B)$

Substituting the given values:

$0.65 = 0.25 + p - 0.25p$

$0.40 = 0.75p$

$p = \dfrac{0.40}{0.75} = \dfrac{40}{75} = \dfrac{8}{15}$

Answer: $\frac{8}{15}$

</details>

---

### Q9. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A and B are independent events with $\mathrm{P}(\mathrm{A})=\dfrac{3}{10}$, $\mathrm{P}(\mathrm{B})=\dfrac{2}{5}$, then $\mathrm{P}\left(\mathrm{A}^{\prime} \cup \mathrm{B}\right)$ has the value

**Options:**

- **(A)** $\dfrac{41}{50}$
- **(B)** $\dfrac{41}{125}$
- **(C)** $\dfrac{7}{25}$
- **(D)** $\dfrac{7}{50}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{41}{50}$**

**Detailed Solution:**

Given $\mathrm{P}(\mathrm{A}) = \dfrac{3}{10}$ and $\mathrm{P}(\mathrm{B}) = \dfrac{2}{5}$.

Since $\mathrm{A}$ and $\mathrm{B}$ are independent events, $\mathrm{A}$ and $\mathrm{B}^{\prime}$ are also independent.

$\mathrm{P}(\mathrm{B}^{\prime}) = 1 - \mathrm{P}(\mathrm{B}) = 1 - \dfrac{2}{5} = \dfrac{3}{5}$

Using the property of complementary events and De Morgan's laws:

$\mathrm{P}(\mathrm{A}^{\prime} \cup \mathrm{B}) = 1 - \mathrm{P}(\mathrm{A} \cap \mathrm{B}^{\prime})$

$\mathrm{P}(\mathrm{A}^{\prime} \cup \mathrm{B}) = 1 - \mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B}^{\prime})$

$\mathrm{P}(\mathrm{A}^{\prime} \cup \mathrm{B}) = 1 - \left(\dfrac{3}{10}\right) \left(\dfrac{3}{5}\right)$

$\mathrm{P}(\mathrm{A}^{\prime} \cup \mathrm{B}) = 1 - \dfrac{9}{50} = \dfrac{41}{50}$

Answer: $\dfrac{41}{50}$

</details>

---

### Q10. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Four persons can hit a target correctly with probabilities $\dfrac{1}{2}, \dfrac{1}{3}, \dfrac{1}{4}$ and $\dfrac{1}{5}$ respectively. If all hit at the target independently, then the probability that the target would be hit, is

**Options:**

- **(A)** $\dfrac{1}{5}$
- **(B)** $\dfrac{3}{5}$
- **(C)** $\dfrac{2}{5}$
- **(D)** $\dfrac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{4}{5}$**

**Detailed Solution:**

Let the events of hitting the target by the four persons be $A, B, C, D$.

$P(A) = \dfrac{1}{2}, P(B) = \dfrac{1}{3}, P(C) = \dfrac{1}{4}, P(D) = \dfrac{1}{5}$

The probability that none of them hits the target is given by $P(\bar{A}) P(\bar{B}) P(\bar{C}) P(\bar{D})$.

$P(\bar{A}) = 1 - \dfrac{1}{2} = \dfrac{1}{2}$

$P(\bar{B}) = 1 - \dfrac{1}{3} = \dfrac{2}{3}$

$P(\bar{C}) = 1 - \dfrac{1}{4} = \dfrac{3}{4}$

$P(\bar{D}) = 1 - \dfrac{1}{5} = \dfrac{4}{5}$

Probability that the target is not hit is $\dfrac{1}{2} \times \dfrac{2}{3} \times \dfrac{3}{4} \times \dfrac{4}{5} = \dfrac{1}{5}$.

The probability that the target is hit is $1 - \dfrac{1}{5} = \dfrac{4}{5}$.

Answer: $\dfrac{4}{5}$

</details>

---

### Q11. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A man and his wife appear for an interview for two posts. The probability of the husband's selection is $\dfrac{1}{7}$. and that of the wife's selection is $\dfrac{1}{5}$. If they appear for the interview independently, then the probability that only one of them is selected, is

**Options:**

- **(A)** $\dfrac{1}{7}$
- **(B)** $\dfrac{2}{7}$
- **(C)** $\dfrac{6}{7}$
- **(D)** $\dfrac{4}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2}{7}$**

**Detailed Solution:**

Let $H$ be the event that the husband is selected and $W$ be the event that the wife is selected.

$P(H) = \dfrac{1}{7}$ and $P(W) = \dfrac{1}{5}$

$P(H') = 1 - \dfrac{1}{7} = \dfrac{6}{7}$ and $P(W') = 1 - \dfrac{1}{5} = \dfrac{4}{5}$

The probability that only one of them is selected is given by $P(H \cap W') + P(H' \cap W)$.

Since the events are independent, this is equal to $P(H)P(W') + P(H')P(W)$.

Substituting the values, we get $\dfrac{1}{7} \times \dfrac{4}{5} + \dfrac{6}{7} \times \dfrac{1}{5} = \dfrac{4}{35} + \dfrac{6}{35} = \dfrac{10}{35} = \dfrac{2}{7}$.

Answer: $\dfrac{2}{7}$

</details>

---

### Q12. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$\mathrm{A}$ and $\mathrm{B}$ are independent events with $\mathrm{P}(\mathrm{A})=\frac{1}{4}$ and $P(A \cup B)=2 P(B)-P(A)$, then $P(B)$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{5}$**

**Detailed Solution:**

$$
\begin{array}{ll} 
& \mathrm{P}(\mathrm{A} \cup \mathrm{B})=2 \mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A}) \\
\therefore \quad & \mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B})=2 \mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A}) \\
\therefore \quad & \mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B})=2 \mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A})
\end{array}
$$
$\ldots[\because A$ and $B$ are independent events $]$
$$
\begin{array}{ll}
\therefore \quad & \mathrm{P}(\mathrm{B})+\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B})=2 \mathrm{P}(\mathrm{A}) \\
\therefore \quad \mathrm{P}(\mathrm{B})=\frac{2 \mathrm{P}(\mathrm{A})}{(1+\mathrm{P}(\mathrm{A}))}=\frac{2 \times \frac{1}{4}}{\left(1+\frac{1}{4}\right)}=\frac{2}{5}
\end{array}
$$

</details>

---

### Q13. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An experiment succeeds twice as often as it fails. Then the probability, that in the next 6 trials there will be atleast 4 successes, is

**Options:**

- **(A)** $\frac{1}{729}$
- **(B)** $\frac{496}{729}$
- **(C)** $\frac{233}{729}$
- **(D)** $\frac{491}{729}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{496}{729}$**

**Detailed Solution:**

Experiment succeeds twice as often as it fails.
$\therefore \quad$ According to the given condition, if ' $\mathrm{p}$ ' is success and ' $q$ ' is failure, then $p=2 q$
$$
\begin{aligned}
\therefore \quad \mathrm{p}+\mathrm{q}=1 & \Rightarrow 2 \mathrm{q}+\mathrm{q}=1 \\
& \Rightarrow \mathrm{q}=\frac{1}{3} \text { and } \mathrm{p}=\frac{2}{3}
\end{aligned}
$$
Here, $\mathrm{n}=6$
Let $\mathrm{X}$ be the random variable
$$
\therefore \quad \mathrm{X} \sim \mathrm{B}(\mathrm{n}, \mathrm{p})
$$
$\therefore \quad$ Required probability
$$
\begin{aligned}
& =\mathrm{P}(\mathrm{X} \geq 4) \\
& =\mathrm{P}(\mathrm{X}=4)+\mathrm{P}(\mathrm{X}=5)+\mathrm{P}(\mathrm{X}=6) \\
& ={ }^6 \mathrm{C}_4 \mathrm{p}^4 \mathrm{q}^2+{ }^6 \mathrm{C}_5 \mathrm{p}^5 \mathrm{q}+{ }^6 \mathrm{C}_6 \mathrm{p}^6 \\
& =15 \times\left(\frac{2}{3}\right)^4\left(\frac{1}{3}\right)^2+6\left(\frac{2}{3}\right)^5\left(\frac{1}{3}\right)+\left(\frac{2}{3}\right)^6 \\
& =\frac{496}{729}
\end{aligned}
$$

</details>

---

### Q14. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A problem in statistics is given to three students $\mathrm{A}, \mathrm{B}$ and $\mathrm{C}$. Their probabilities of solving the problem are $\frac{1}{2}, \frac{1}{3}$ and $\frac{1}{4}$ respectively, If all of them try independently, then the probability, that problem is solved, is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{4}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}(\mathrm{A}) & =\frac{1}{2} \\ \therefore \quad \mathrm{P}\left(\mathrm{A}^{\prime}\right) & =1-\frac{1}{2}=\frac{1}{2} \\ \mathrm{P}(\mathrm{B}) & =\frac{1}{3}\end{aligned}$
$\begin{array}{ll}\therefore \quad & \mathrm{P}\left(\mathrm{B}^{\prime}\right)=1-\frac{1}{3}=\frac{2}{3} \\ & \mathrm{P}(\mathrm{C})=\frac{1}{4} \\ \therefore \quad & \mathrm{P}\left(\mathrm{C}^{\prime}\right)=1-\frac{1}{4}=\frac{3}{4} \\ \therefore \quad & \mathrm{P}(\mathrm{Problem} \text { is not solve }) \\ & =\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}^{\prime} \cap \mathrm{C}^{\prime}\right) \\ & =\mathrm{P}\left(\mathrm{A}^{\prime}\right) \cdot \mathrm{P}\left(\mathrm{B}^{\prime}\right) \cdot \mathrm{P}\left(\mathrm{C}^{\prime}\right) \\ & \quad \ldots\left[\because \mathrm{A}^{\prime}, \mathrm{B}^{\prime}, \mathrm{C}^{\prime} \text { are independent }\right]\end{array}$
$\begin{aligned} & =\frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} \\ & =\frac{1}{4}\end{aligned}$
$\begin{aligned} \therefore \quad & \text { P(the problem will be solve) } \\ & =1-\mathrm{P} \text { (Problem is not solved) } \\ & =1-\frac{1}{4} \\ & =\frac{3}{4}\end{aligned}$

</details>

---

### Q15. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{A}$ and $\mathrm{B}$ are two independent events and $\mathrm{P}(\mathrm{A})=\frac{3}{5}, \mathrm{P}(\mathrm{B})=\frac{2}{3}$, then $\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}^{\prime}\right)=$

**Options:**

- **(A)** $\frac{7}{15}$
- **(B)** $\frac{2}{15}$
- **(C)** $\frac{4}{15}$
- **(D)** $\frac{1}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{15}$**

**Detailed Solution:**

$\mathrm{P}(\mathrm{A})=\frac{2}{3} \Rightarrow \mathrm{P}\left(\mathrm{A}^{\prime}\right)=1-\mathrm{P}(\mathrm{A})=1-\frac{2}{3}=\frac{1}{3}$
$\therefore \mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B}\right)=\mathrm{P}\left(\mathrm{A}^{\prime}\right) \cdot \mathrm{P}(\mathrm{B})$
$=\frac{1}{3} \times \frac{3}{5}=\frac{1}{5}$

</details>

---

### Q16. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $A$ and $B$ are independent events and $P(A)=\frac{2}{3}, P(B)=\frac{3}{5}$, then $P\left(A^{\prime} \cap B\right)=$

**Options:**

- **(A)** $\frac{4}{15}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{5}$**

**Detailed Solution:**

$\mathrm{P}(\mathrm{A})=\frac{3}{5}, \mathrm{P}(\mathrm{B})=\frac{2}{3}$ and $\mathrm{A}, \mathrm{B}$ are independent events.
$$
\begin{aligned}
\therefore P(A \cap B) &=P(A) \times P(B)=\frac{3}{5} \times \frac{2}{3}=\frac{2}{5} \\
P(A \cup B) &=P(A)+P(B)-P(A \cap B) \\
&=\frac{3}{5}+\frac{2}{3}-\frac{2}{5}=\frac{13}{15} \\
\therefore P(A \cup B)^{\prime} &=1-\frac{13}{15}=\frac{2}{15} \\
P\left(A^{\prime} \cap B^{\prime}\right) &=P(A \cup B)^{\prime}=\frac{2}{15}
\end{aligned}
$$

</details>

---

### Q17. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `2`

The odds against a certain event are $5: 2$ and the odds in favour of another independent event are $6: 5 .$ The probability that at least one of the events will happen, is

**Options:**

- **(A)** $\frac{25}{77}$
- **(B)** $\frac{52}{77}$
- **(C)** $\frac{12}{77}$
- **(D)** $\frac{65}{77}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{52}{77}$**

**Detailed Solution:**

Let $A$ and $B$ are two given events.
$$
\begin{array}{l}
\therefore \quad P(A)=\frac{2}{7}, P(B)=\frac{6}{11} \\
\therefore \text { Required probability }=1-P(\bar{A}) P(\bar{B}) \\
\quad=1-\left(1-\frac{2}{7}\right)\left(1-\frac{6}{11}\right) \\
=\frac{52}{77}
\end{array}
$$

</details>

---

