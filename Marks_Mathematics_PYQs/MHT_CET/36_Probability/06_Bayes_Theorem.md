# MHT CET Mathematics - Probability

## Topic 6: Baye's Theorem

**Total Questions:** 7

---

### Q1. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a certain city, the ratio of men to women is $5:4$. It is found that $80\%$ of men and $90\%$ of women are literate. If a person selected at random is found to be illiterate, then the probability that the person is a man is....

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{5}{7}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{2}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{5}{7}$**

**Detailed Solution:**

Let $M$ and $W$ be the events that the selected person is a man and a woman respectively.

$P(M) = \dfrac{5}{9}$ and $P(W) = \dfrac{4}{9}$

Let $I$ be the event that the selected person is illiterate.

Given that $80\%$ of men and $90\%$ of women are literate, the probabilities of them being illiterate are:

$P(I|M) = 1 - 0.8 = 0.2 = \dfrac{1}{5}$

$P(I|W) = 1 - 0.9 = 0.1 = \dfrac{1}{10}$

By Bayes' theorem, the probability that the person is a man given that they are illiterate is:

$P(M|I) = \dfrac{P(M)P(I|M)}{P(M)P(I|M) + P(W)P(I|W)}$

$P(M|I) = \dfrac{\dfrac{5}{9} \times \dfrac{1}{5}}{\dfrac{5}{9} \times \dfrac{1}{5} + \dfrac{4}{9} \times \dfrac{1}{10}}$

$P(M|I) = \dfrac{\dfrac{1}{9}}{\dfrac{1}{9} + \dfrac{2}{45}} = \dfrac{\dfrac{5}{45}}{\dfrac{7}{45}} = \dfrac{5}{7}$

</details>

---

### Q2. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $E_1$ and $E_2$ are equally likely, mutually exclusive and exhaustive events and $P(A|E_1) = 0.2$, $P(A|E_2) = 0.3$, then $P(E_1|A)$ equal to...

**Options:**

- **(A)** $\dfrac{1}{5}$
- **(B)** $\dfrac{4}{5}$
- **(C)** $\dfrac{2}{3}$
- **(D)** $\dfrac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2}{5}$**

**Detailed Solution:**

Since $E_1$ and $E_2$ are equally likely, mutually exclusive and exhaustive events, $P(E_1) = P(E_2) = \dfrac{1}{2}$.

Given $P(A|E_1) = 0.2$ and $P(A|E_2) = 0.3$.

Using Bayes' theorem,

$P(E_1|A) = \dfrac{P(A|E_1)P(E_1)}{P(A|E_1)P(E_1) + P(A|E_2)P(E_2)}$

$P(E_1|A) = \dfrac{0.2 \times \dfrac{1}{2}}{0.2 \times \dfrac{1}{2} + 0.3 \times \dfrac{1}{2}}$

$P(E_1|A) = \dfrac{0.2}{0.2 + 0.3} = \dfrac{0.2}{0.5} = \dfrac{2}{5}$

Answer: $\dfrac{2}{5}$

</details>

---

### Q3. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A certain disease has a prevalence of $1\%$ in the population. A diagnostic test for the disease has a sensitivity of $98\%$ and a specificity of $95\%$. If a person from this population tests positive, then the probability that they actually have the disease is...

**Options:**

- **(A)** $98\%$
- **(B)** $95\%$
- **(C)** $16.5\%$
- **(D)** $1\%$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $16.5\%$**

**Detailed Solution:**

Let $D$ be the event that the person has the disease, and $T$ be the event that the test is positive.

We have $P(D) = 0.01$ and $P(D^c) = 1 - 0.01 = 0.99$.

The sensitivity is $P(T|D) = 0.98$.

The specificity is $P(T^c|D^c) = 0.95$, which gives $P(T|D^c) = 1 - 0.95 = 0.05$.

Using Bayes' theorem, the probability that the person has the disease given a positive test is:

$P(D|T) = \dfrac{P(T|D)P(D)}{P(T|D)P(D) + P(T|D^c)P(D^c)}$

Substituting the values:

$P(D|T) = \dfrac{0.98 \times 0.01}{0.98 \times 0.01 + 0.05 \times 0.99}$

$P(D|T) = \dfrac{0.0098}{0.0098 + 0.0495}$

$P(D|T) = \dfrac{0.0098}{0.0593} = \dfrac{98}{593}$

$P(D|T) \approx 0.1652$

Converting to percentage, the probability is approximately $16.5\%$.

Answer: $16.5\%$

</details>

---

### Q4. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed a fixed number of times. If the probability of getting 5 tails is same as the probability of getting 7 tails, then the probability of getting 3 tails is

**Options:**

- **(A)** $\frac{44}{2^{13}}$
- **(B)** $\frac{55}{2^{10}}$
- **(C)** $\frac{55}{2^{13}}$
- **(D)** $\frac{44}{2^{10}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{55}{2^{10}}$**

**Detailed Solution:**

Let the coin be tossed $n$ times.

The probability of getting $r$ tails in $n$ tosses of a fair coin is given by $P(X = r) = ^{n}C_{r} \left(\dfrac{1}{2}\right)^n$.

Given $P(X = 5) = P(X = 7)$

$^{n}C_{5} \left(\dfrac{1}{2}\right)^n = ^{n}C_{7} \left(\dfrac{1}{2}\right)^n$

$^{n}C_{5} = ^{n}C_{7}$

Using the property $^{n}C_{x} = ^{n}C_{y} \Rightarrow n = x + y$, we get:

$n = 5 + 7 = 12$

The probability of getting 3 tails is:

$P(X = 3) = ^{12}C_{3} \left(\dfrac{1}{2}\right)^{12}$

$P(X = 3) = \dfrac{12 \times 11 \times 10}{3 \times 2 \times 1} \times \dfrac{1}{2^{12}}$

$P(X = 3) = \dfrac{220}{2^{12}}$

$P(X = 3) = \dfrac{55 \times 4}{2^2 \times 2^{10}} = \dfrac{55}{2^{10}}$

Answer: $\frac{55}{2^{10}}$

</details>

---

### Q5. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A doctor assumes that patient has one of three diseases $\mathrm{d} 1, \mathrm{~d} 2$ or d 3. Before any test he assumes an equal probability for each disease. He carries out a test that will be positive with probability 0.7 if the patient has disease $\mathrm{d} 1,0.5$ if the patient has disease d2 and 0.8 if the patient has disease d3. Given that the outcome of the test was positive then probability that patient has disease d2 is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{1}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4}$**

**Detailed Solution:**

Let $E_1, E_2, E_3$ be the events that the patient has disease $d_1, d_2, d_3$ respectively.

Since the doctor assumes an equal probability for each disease:

$P(E_1) = P(E_2) = P(E_3) = \dfrac{1}{3}$

Let $A$ be the event that the test is positive. The given conditional probabilities are:

$P(A|E_1) = 0.7$

$P(A|E_2) = 0.5$

$P(A|E_3) = 0.8$

By Bayes' theorem, the probability that the patient has disease $d_2$ given that the test is positive is $P(E_2|A)$:

$P(E_2|A) = \dfrac{P(E_2)P(A|E_2)}{P(E_1)P(A|E_1) + P(E_2)P(A|E_2) + P(E_3)P(A|E_3)}$

$P(E_2|A) = \dfrac{\dfrac{1}{3} \times 0.5}{\dfrac{1}{3} \times 0.7 + \dfrac{1}{3} \times 0.5 + \dfrac{1}{3} \times 0.8}$

$P(E_2|A) = \dfrac{0.5}{0.7 + 0.5 + 0.8}$

$P(E_2|A) = \dfrac{0.5}{2.0} = \dfrac{1}{4}$

Answer: $\frac{1}{4}$

</details>

---

### Q6. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Bag I contains 3 red and 2 green balls and Bag II contains 5 red and 3 green balls. A ball is drawn from one of the bag at random and it is found to be green. Then the probability that it is drawn from Bag I is

**Options:**

- **(A)** $\frac{8}{31}$
- **(B)** $\frac{12}{31}$
- **(C)** $\frac{14}{31}$
- **(D)** $\frac{16}{31}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{16}{31}$**

**Detailed Solution:**

Let $E_1$ and $E_2$ be the events of selecting Bag I and Bag II respectively.

$P(E_1) = P(E_2) = \dfrac{1}{2}$

Let $G$ be the event of drawing a green ball.

Probability of drawing a green ball from Bag I is $P(G|E_1) = \dfrac{2}{5}$

Probability of drawing a green ball from Bag II is $P(G|E_2) = \dfrac{3}{8}$

By Bayes' theorem, the probability that the green ball is drawn from Bag I is:

$P(E_1|G) = \dfrac{P(E_1)P(G|E_1)}{P(E_1)P(G|E_1) + P(E_2)P(G|E_2)}$

$P(E_1|G) = \dfrac{\dfrac{1}{2} \times \dfrac{2}{5}}{\dfrac{1}{2} \times \dfrac{2}{5} + \dfrac{1}{2} \times \dfrac{3}{8}}$

$P(E_1|G) = \dfrac{\dfrac{2}{5}}{\dfrac{2}{5} + \dfrac{3}{8}}$

$P(E_1|G) = \dfrac{\dfrac{2}{5}}{\dfrac{16 + 15}{40}}$

$P(E_1|G) = \dfrac{2}{5} \times \dfrac{40}{31} = \dfrac{16}{31}$

Answer: $\frac{16}{31}$

</details>

---

### Q7. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Suppose that $5 \%$ of men and $0.25 \%$ of women have gray hair. A gray hair person is selected at random. If there are equal number of males and females, then the probability that the person selected being men is

**Options:**

- **(A)** $\frac{20}{21}$
- **(B)** $\cdot \frac{10}{21}$
- **(C)** $\frac{1}{21}$
- **(D)** $\frac{11}{21}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{20}{21}$**

**Detailed Solution:**

A grey haired person is selected at eandom, the probability that this person is male $=\mathrm{P}(\mathrm{M} / \mathrm{G})$ Here $M$ is men, $W$ is women, $G$ is grey hair.
$$
\begin{aligned}
\therefore \mathrm{P}(\mathrm{M} / \mathrm{G}) &=\frac{\mathrm{P}(\mathrm{M}) \times \mathrm{P}(\mathrm{G} / \mathrm{M})}{\mathrm{P}(\mathrm{M}) \times \mathrm{P}(\mathrm{G} / \mathrm{M})+\mathrm{P}(\mathrm{W}) \times \mathrm{P}(\mathrm{G} / \mathrm{W})} \\
&=\frac{\frac{1}{2} \times \frac{5}{100}}{\left(\frac{1}{2} \times \frac{5}{100}\right)+\left(\frac{1}{2} \times \frac{0.25}{100}\right)}=\frac{20}{21}
\end{aligned}
$$

</details>

---

