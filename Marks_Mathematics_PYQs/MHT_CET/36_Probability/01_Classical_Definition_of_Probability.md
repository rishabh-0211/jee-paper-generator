# MHT CET Mathematics - Probability

## Topic 1: Classical Definition of Probability

**Total Questions:** 77

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $a$ and $b$ be the numbers obtained in two trials of tossing a fair die. The probability that the matrix $\begin{bmatrix} a & 2 \\ 6 & b \end{bmatrix}$ is not invertible is

**Options:**

- **(A)** $\dfrac{1}{9}$
- **(B)** $\dfrac{1}{18}$
- **(C)** $\dfrac{1}{6}$
- **(D)** $\dfrac{1}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{9}$**

**Detailed Solution:**

Let the given matrix be $A = \begin{bmatrix} a & 2 \\ 6 & b \end{bmatrix}$.

For the matrix $A$ to be not invertible, its determinant must be equal to zero.

$|A| = ab - 12 = 0 \Rightarrow ab = 12$

Since $a$ and $b$ are the numbers obtained in two trials of tossing a fair die, $a, b \in \{1, 2, 3, 4, 5, 6\}$.

The possible pairs $(a, b)$ satisfying $ab = 12$ are $(2, 6), (3, 4), (4, 3)$, and $(6, 2)$.

The number of favorable outcomes is $4$.

The total number of possible outcomes in two trials of tossing a fair die is $6 \times 6 = 36$.

The required probability is $\dfrac{4}{36} = \dfrac{1}{9}$.

Answer: $\dfrac{1}{9}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two fair dice are thrown. The probability that the sum of the scores is $7$ such that the number on the second die is greater than that on the first die is ...

**Options:**

- **(A)** $\dfrac{1}{6}$
- **(B)** $\dfrac{1}{12}$
- **(C)** $\dfrac{3}{4}$
- **(D)** $\dfrac{1}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{12}$**

**Detailed Solution:**

Total number of possible outcomes when two dice are thrown is $6 \times 6 = 36$.

Let $E$ be the event that the sum of the scores on the two dice is $7$ and the number on the second die is greater than the number on the first die.

The outcomes where the sum of the scores is $7$ are $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$.

The favorable outcomes where the number on the second die is greater than the number on the first die are $(1, 6), (2, 5), (3, 4)$.

Number of favorable outcomes is $3$.

Required probability is $\dfrac{3}{36} = \dfrac{1}{12}$.

Answer: $\dfrac{1}{12}$

</details>

---

### Q3. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Six faces of a die are marked with the numbers $-3, -2, -1, 0, 1, 2$. If such two dice are thrown simultaneously, then the probability of getting the product of the numbers on the uppermost surfaces as $\pm 3$ or sum of the numbers on the uppermost surfaces is divisible by $2$, is ....

**Options:**

- **(A)** $\dfrac{19}{36}$
- **(B)** $\dfrac{7}{18}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $\dfrac{2}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}$**

**Detailed Solution:**

Total number of possible outcomes when two dice are thrown is $6 \times 6 = 36$.

Let $A$ be the event that the product of the numbers on the uppermost surfaces is $\pm 3$.
The possible pairs $(x, y)$ such that $xy = 3$ or $xy = -3$ from the given numbers $\{-3, -2, -1, 0, 1, 2\}$ are:
$(-3, -1), (-1, -3), (-3, 1), (1, -3)$
Thus, $n(A) = 4$.

Let $B$ be the event that the sum of the numbers on the uppermost surfaces is divisible by $2$ (i.e., the sum is even).
The sum of two numbers is even if both are even or both are odd.
The given numbers can be categorized as:
Even numbers: $\{-2, 0, 2\}$ (3 numbers)
Odd numbers: $\{-3, -1, 1\}$ (3 numbers)
Number of ways to get an even sum = (Even, Even) + (Odd, Odd)
$n(B) = (3 \times 3) + (3 \times 3) = 9 + 9 = 18$.

Now, we find the intersection $A \cap B$, which represents outcomes where the product is $\pm 3$ and the sum is even.
Observing the pairs in event $A$, all of them consist of two odd numbers. The sum of two odd numbers is always even.
Therefore, all outcomes in $A$ are also in $B$, which means $A \subset B$.
Thus, $n(A \cap B) = n(A) = 4$.

We need to find the probability of $A \cup B$ (product is $\pm 3$ OR sum is divisible by $2$).
Using the principle of inclusion-exclusion:
$n(A \cup B) = n(A) + n(B) - n(A \cap B)$
$n(A \cup B) = 4 + 18 - 4 = 18$

The required probability is:
$P(A \cup B) = \dfrac{n(A \cup B)}{\text{Total outcomes}} = \dfrac{18}{36} = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q4. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If a fair die is thrown, then the odds in favor of getting a perfect square on the uppermost face are:

**Options:**

- **(A)** $1 : 3$
- **(B)** $2 : 3$
- **(C)** $1 : 2$
- **(D)** $2 : 5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 : 2$**

**Detailed Solution:**

The sample space for throwing a fair die is $S = \{1, 2, 3, 4, 5, 6\}$.

The total number of possible outcomes is $n(S) = 6$.

Let $E$ be the event of getting a perfect square on the uppermost face. The perfect squares in the sample space are $1$ and $4$.

So, $E = \{1, 4\}$ and the number of favorable outcomes is $n(E) = 2$.

The number of unfavorable outcomes is $n(E') = n(S) - n(E) = 6 - 2 = 4$.

The odds in favor of an event are given by the ratio of the number of favorable outcomes to the number of unfavorable outcomes.

Odds in favor $= n(E) : n(E') = 2 : 4 = 1 : 2$.

Answer: $1 : 2$

</details>

---

### Q5. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A fair die is thrown. The odds in favor of getting a number which is a perfect square on the uppermost face of the die are...

**Options:**

- **(A)** $\dfrac{2}{3}$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

The sample space for a fair die is $S = \{1, 2, 3, 4, 5, 6\}$.

The event $E$ of getting a perfect square is $E = \{1, 4\}$.

The number of favorable outcomes is $n(E) = 2$.

The number of unfavorable outcomes is $n(E') = 6 - 2 = 4$.

The odds in favor of an event are given by the ratio of the number of favorable outcomes to the number of unfavorable outcomes.

Odds in favor $= \dfrac{n(E)}{n(E')} = \dfrac{2}{4} = \dfrac{1}{2}$.

Answer: $\dfrac{1}{2}$

</details>

---

### Q6. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The number is selected randomly from the integers $1$ to $100$. The probability that the number selected has exactly three factors is ...

**Options:**

- **(A)** $\dfrac{1}{25}$
- **(B)** $\dfrac{1}{20}$
- **(C)** $\dfrac{9}{100}$
- **(D)** $\dfrac{1}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{25}$**

**Detailed Solution:**

A number has exactly three factors if and only if it is the square of a prime number.

Let the number be $N = p^2$, where $p$ is a prime number.

Since $N \le 100$, we have $p^2 \le 100$, which gives $p \le 10$.

The prime numbers less than or equal to $10$ are $2, 3, 5, 7$.

The numbers with exactly three factors between $1$ and $100$ are $4, 9, 25, 49$.

There are $4$ such numbers.

The total number of integers from $1$ to $100$ is $100$.

The required probability is $\dfrac{4}{100} = \dfrac{1}{25}$.

Answer: $\dfrac{1}{25}$

</details>

---

### Q7. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three numbers are chosen from 1 to 30. The probability that minimum is 10 and maximum is 26 is _______

**Options:**

- **(A)** $\dfrac{1}{406}$
- **(B)** $\dfrac{3}{812}$
- **(C)** $\dfrac{5}{812}$
- **(D)** $\dfrac{7}{812}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{812}$**

**Detailed Solution:**

Total number of ways to select 3 numbers from 30 is $^{30}C_{3}$.

$^{30}C_{3} = \dfrac{30 \times 29 \times 28}{3 \times 2 \times 1} = 4060$

For the minimum to be 10 and the maximum to be 26, two of the selected numbers must be exactly 10 and 26.

The third number must be chosen from the integers strictly between 10 and 26.

The integers between 10 and 26 are 11, 12, ..., 25.

The number of such integers is $26 - 10 - 1 = 15$.

Thus, the number of favorable selections is 15.

The required probability is $\dfrac{15}{4060} = \dfrac{3}{812}$.

Answer: $\dfrac{3}{812}$

</details>

---

### Q8. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A fair die is thrown at random. Let A be the event that the number obtained on the die is a non-even prime number and B be the event that the number obtained on the die is an odd number.
Let $p : P(A) = \dfrac{1}{3}$, $q$ : A and B are independent events.
Then the truth values of statements $p$ and $q$ respectively are.....

**Options:**

- **(A)** T , T
- **(B)** T , F
- **(C)** F , T
- **(D)** F , F

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) T , F**

**Detailed Solution:**

Sample space $S = \{1, 2, 3, 4, 5, 6\}$

Event $A$ is getting a non-even prime number.
$A = \{3, 5\}$
$P(A) = \dfrac{2}{6} = \dfrac{1}{3}$
Statement $p$ is True.

Event $B$ is getting an odd number.
$B = \{1, 3, 5\}$
$P(B) = \dfrac{3}{6} = \dfrac{1}{2}$

$A \cap B = \{3, 5\}$
$P(A \cap B) = \dfrac{2}{6} = \dfrac{1}{3}$

$P(A) \times P(B) = \dfrac{1}{3} \times \dfrac{1}{2} = \dfrac{1}{6}$

Since $P(A \cap B) \neq P(A) \times P(B)$, events $A$ and $B$ are not independent.
Statement $q$ is False.

The truth values of $p$ and $q$ are T and F respectively.

Answer: T , F

</details>

---

### Q9. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

It is known that a box of $8$ batteries contains $3$ defective pieces and a person randomly selects $2$ batteries from this box. Then the probability distribution of the number of defective batteries is

**Options:**

- **(A)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$0$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>
- **(B)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>
- **(C)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$0$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>
- **(D)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$0$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>**

**Detailed Solution:**

Total number of batteries = $8$
Number of defective batteries = $3$
Number of non-defective batteries = $5$

Let $X$ be the random variable representing the number of defective batteries selected. Since $2$ batteries are drawn, the possible values of $X$ are $0, 1, 2$.

Total number of ways to select $2$ batteries from $8$ is $^{8}C_{2} = 28$.

Probability of selecting $0$ defective batteries ($X = 0$):
$P(X = 0) = \dfrac{^{5}C_{2}}{^{8}C_{2}} = \dfrac{10}{28}$

Probability of selecting $1$ defective battery ($X = 1$):
$P(X = 1) = \dfrac{^{3}C_{1} \times ^{5}C_{1}}{^{8}C_{2}} = \dfrac{3 \times 5}{28} = \dfrac{15}{28}$

Probability of selecting $2$ defective batteries ($X = 2$):
$P(X = 2) = \dfrac{^{3}C_{2}}{^{8}C_{2}} = \dfrac{3}{28}$

Thus, the probability distribution is:
$X = 0, P(X = 0) = \dfrac{10}{28}$
$X = 1, P(X = 1) = \dfrac{15}{28}$
$X = 2, P(X = 2) = \dfrac{3}{28}$

Answer: <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$0$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{10}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{15}{28}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{28}$</td></tr></table>

</details>

---

### Q10. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn at random from a standard pack of $52$ cards. Then the probability that the draw consists of exactly one face card and exactly one ace card is...

**Options:**

- **(A)** $\dfrac{7}{221}$
- **(B)** $\dfrac{5}{221}$
- **(C)** $\dfrac{8}{221}$
- **(D)** $\dfrac{9}{221}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{8}{221}$**

**Detailed Solution:**

Total number of cards in a standard pack $= 52$

Total number of ways to draw $2$ cards $= ^{52}C_{2} = \dfrac{52 \times 51}{2} = 1326$

Number of face cards (Jack, Queen, King of each suit) $= 4 \times 3 = 12$

Number of ace cards $= 4$

Number of ways to draw exactly one face card and exactly one ace card $= ^{12}C_{1} \times ^{4}C_{1} = 12 \times 4 = 48$

Required probability $= \dfrac{48}{1326} = \dfrac{8}{221}$

Answer: $\dfrac{8}{221}$

</details>

---

### Q11. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three numbers are chosen at random from numbers 1 to 20 . The probability that they are consecutive is

**Options:**

- **(A)** $\frac{1}{190}$
- **(B)** $\frac{1}{120}$
- **(C)** $\frac{3}{190}$
- **(D)** $\frac{5}{190}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{190}$**

**Detailed Solution:**

Total number of ways to choose $3$ numbers from $20$ numbers is $^{20}C_{3}$.

$^{20}C_{3} = \dfrac{20 \times 19 \times 18}{3 \times 2 \times 1} = 1140$

The favorable outcomes are the sets of $3$ consecutive numbers: $(1, 2, 3), (2, 3, 4), \dots, (18, 19, 20)$.

The number of such sets is $18$.

The required probability is $\dfrac{18}{1140} = \dfrac{3}{190}$.

Answer: $\frac{3}{190}$

</details>

---

### Q12. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If 6 boys and 3 girls are to be seated on chairs for a photograph, then the probability that the end seats are occupied by the girls and no two girls are side by side is

**Options:**

- **(A)** $\frac{5}{84}$
- **(B)** $\frac{5}{42}$
- **(C)** $\frac{1}{12}$
- **(D)** $\frac{5}{28}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{5}{84}$**

**Detailed Solution:**

Total number of people = $6$ boys + $3$ girls = $9$.

Total number of ways to arrange $9$ people in a row = $9!$

For the end seats to be occupied by girls, the $1^{\text{st}}$ and $9^{\text{th}}$ seats must be occupied by girls. 

To ensure no two girls are side by side, the seats adjacent to the ends (the $2^{\text{nd}}$ and $8^{\text{th}}$ seats) must be occupied by boys.

The remaining $1$ girl can be seated in any of the remaining $5$ seats (i.e., $3^{\text{rd}}, 4^{\text{th}}, 5^{\text{th}}, 6^{\text{th}},$ or $7^{\text{th}}$ seat).

Number of ways to choose the seat for the $3^{\text{rd}}$ girl = $5$

Number of ways to arrange the $3$ girls in these $3$ designated seats = $3!$

Number of ways to arrange the $6$ boys in the remaining $6$ seats = $6!$

Total number of favorable arrangements = $5 \times 3! \times 6!$

Required probability = $\dfrac{5 \times 3! \times 6!}{9!} = \dfrac{5 \times 6 \times 6!}{9 \times 8 \times 7 \times 6!} = \dfrac{30}{504} = \dfrac{5}{84}$

Answer: $\frac{5}{84}$

</details>

---

### Q13. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

An urn contains 6 yellow balls and $x$ black balls. When two balls are drawn at random, the probability that both are yellow is $\frac{5}{26}$, then the value of $x$ is

**Options:**

- **(A)** 7
- **(B)** 5
- **(C)** 11
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7**

**Detailed Solution:**

Total number of balls in the urn is $6 + x$.

The probability of drawing two yellow balls is given by $\dfrac{^{6}C_{2}}{^{6+x}C_{2}}$.

Given that this probability is $\dfrac{5}{26}$, we have:

$\dfrac{^{6}C_{2}}{^{6+x}C_{2}} = \dfrac{5}{26}$

$\dfrac{\dfrac{6 \times 5}{2}}{\dfrac{(6+x)(5+x)}{2}} = \dfrac{5}{26}$

$\dfrac{30}{(6+x)(5+x)} = \dfrac{5}{26}$

$(6+x)(5+x) = \dfrac{30 \times 26}{5}$

$x^2 + 11x + 30 = 156$

$x^2 + 11x - 126 = 0$

$(x+18)(x-7) = 0$

Since the number of balls cannot be negative, $x = 7$.

Answer: 7

</details>

---

### Q14. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability that a non leap year selected at random will contain 52 Saturdays or 53 Sundays is

**Options:**

- **(A)** $\frac{1}{7}$
- **(B)** $\frac{6}{7}$
- **(C)** $\frac{2}{7}$
- **(D)** $\frac{5}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{6}{7}$**

**Detailed Solution:**

A non-leap year has $365$ days, which consists of $52$ complete weeks and $1$ extra day.

The extra day can be any of the $7$ days of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.

Let $A$ be the event that the year contains exactly $52$ Saturdays. This happens if the extra day is not a Saturday.

$P(A) = \dfrac{6}{7}$

Let $B$ be the event that the year contains exactly $53$ Sundays. This happens if the extra day is a Sunday.

$P(B) = \dfrac{1}{7}$

The event $A \cap B$ represents the year having exactly $52$ Saturdays and $53$ Sundays, which happens when the extra day is a Sunday.

$P(A \cap B) = \dfrac{1}{7}$

The probability of having $52$ Saturdays or $53$ Sundays is given by $P(A \cup B)$.

$P(A \cup B) = P(A) + P(B) - P(A \cap B)$

$P(A \cup B) = \dfrac{6}{7} + \dfrac{1}{7} - \dfrac{1}{7} = \dfrac{6}{7}$

Answer: $\frac{6}{7}$

</details>

---

### Q15. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A box contains 8 red and $x$ number of green balls. 3 balls are drawn at random, if the probability that 3 balls being red is $\frac{7}{15}$ then number of green balls is _______

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** 3
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

Total number of balls in the box is $8 + x$.

Number of ways to draw 3 balls from $8 + x$ balls is $^{8+x}C_{3}$.

Number of ways to draw 3 red balls from 8 red balls is $^{8}C_{3}$.

Probability of drawing 3 red balls is given by:

$P = \dfrac{^{8}C_{3}}{^{8+x}C_{3}} = \dfrac{7}{15}$

We know that $^{8}C_{3} = \dfrac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$.

Substituting this in the probability equation:

$\dfrac{56}{^{8+x}C_{3}} = \dfrac{7}{15}$

$^{8+x}C_{3} = \dfrac{56 \times 15}{7} = 120$

Using the formula for combinations, $^{n}C_{3} = \dfrac{n(n-1)(n-2)}{6}$:

$\dfrac{(8+x)(7+x)(6+x)}{6} = 120$

$(8+x)(7+x)(6+x) = 720$

Since $10 \times 9 \times 8 = 720$, we can compare the terms:

$8+x = 10$

$x = 2$

Answer: 2

</details>

---

### Q16. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a box containing 100 apples, 10 are defective. The probability that in a sample of 6 apples drawn with replacement, 3 are defective is

**Options:**

- **(A)** $0.1548$
- **(B)** $0.1458$
- **(C)** $0.01854$
- **(D)** $0.01458$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.01458$**

**Detailed Solution:**

Let $p$ be the probability of drawing a defective apple.

$p = \dfrac{10}{100} = \dfrac{1}{10}$

$q = 1 - p = 1 - \dfrac{1}{10} = \dfrac{9}{10}$

The number of trials is $n = 6$.

Let $X$ be the number of defective apples. The probability of getting exactly $3$ defective apples is given by the binomial distribution:

$P(X = 3) = ^{6}C_{3} p^3 q^3$

$P(X = 3) = ^{6}C_{3} \left(\dfrac{1}{10}\right)^3 \left(\dfrac{9}{10}\right)^3$

$P(X = 3) = 20 \times \dfrac{1}{1000} \times \dfrac{729}{1000}$

$P(X = 3) = \dfrac{14580}{1000000} = 0.01458$

Answer: $0.01458$

</details>

---

### Q17. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a single toss of a fair die, the odds against the event that number 4 or 5 turns up is

**Options:**

- **(A)** $2 : 1$
- **(B)** $1: 3$
- **(C)** $2: 3$
- **(D)** $1: 1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 : 1$**

**Detailed Solution:**

The sample space for a single toss of a fair die is $S = \{1, 2, 3, 4, 5, 6\}$.

$n(S) = 6$

Let $E$ be the event that number $4$ or $5$ turns up.

$E = \{4, 5\}$

$n(E) = 2$

Let $E'$ be the event that number $4$ or $5$ does not turn up.

$n(E') = n(S) - n(E) = 6 - 2 = 4$

The odds against an event are given by the ratio of the number of unfavorable outcomes to the number of favorable outcomes.

Odds against event $E = \dfrac{n(E')}{n(E)} = \dfrac{4}{2} = \dfrac{2}{1}$

The odds against the event are $2 : 1$.

Answer: $2 : 1$

</details>

---

### Q18. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If two numbers $p$ and $q$ are chosen randomly from the set $\{1,2,3,4\}$, one by one, with replacement, then the probability of getting $p^2 \ge 4 q$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{7}{16}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{9}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7}{16}$**

**Detailed Solution:**

The total number of ways to choose $p$ and $q$ from the set $\{1, 2, 3, 4\}$ with replacement is $4 \times 4 = 16$.

We need to find the number of pairs $(p, q)$ that satisfy the condition $p^2 \ge 4q$.

For $p = 1$, $1^2 \ge 4q \Rightarrow 1 \ge 4q$. No value of $q \in \{1, 2, 3, 4\}$ satisfies this.

For $p = 2$, $2^2 \ge 4q \Rightarrow 4 \ge 4q \Rightarrow q \le 1$. The only possible value is $q = 1$. (1 outcome)

For $p = 3$, $3^2 \ge 4q \Rightarrow 9 \ge 4q \Rightarrow q \le 2.25$. The possible values are $q = 1, 2$. (2 outcomes)

For $p = 4$, $4^2 \ge 4q \Rightarrow 16 \ge 4q \Rightarrow q \le 4$. The possible values are $q = 1, 2, 3, 4$. (4 outcomes)

The total number of favorable outcomes is $0 + 1 + 2 + 4 = 7$.

The required probability is $\dfrac{7}{16}$.

Answer: $\frac{7}{16}$

</details>

---

### Q19. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If two fair dice are rolled, then the probability that the sum of the numbers on the upper faces is at least 9 , is

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{4}{11}$
- **(C)** $\frac{5}{18}$
- **(D)** $\frac{5}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{18}$**

**Detailed Solution:**

When two fair dice are rolled, the total number of possible outcomes is $n(S) = 6 \times 6 = 36$.

Let $A$ be the event that the sum of the numbers on the upper faces is at least $9$. The possible sums are $9, 10, 11,$ and $12$.

The favorable outcomes are:
Sum $= 9$: $(3, 6), (4, 5), (5, 4), (6, 3)$
Sum $= 10$: $(4, 6), (5, 5), (6, 4)$
Sum $= 11$: $(5, 6), (6, 5)$
Sum $= 12$: $(6, 6)$

The number of favorable outcomes is $n(A) = 4 + 3 + 2 + 1 = 10$.

The required probability is $P(A) = \dfrac{n(A)}{n(S)} = \dfrac{10}{36} = \dfrac{5}{18}$.

Answer: $\frac{5}{18}$

</details>

---

### Q20. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The probability, that a year selected at random will have 53 Mondays, is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{3}{28}$
- **(C)** $\frac{5}{28}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{28}$**

**Detailed Solution:**

Let $L$ be the event that the randomly selected year is a leap year, and $L'$ be the event that it is a non-leap year.

The probability of a year being a leap year is $P(L) = \dfrac{1}{4}$, and the probability of it being a non-leap year is $P(L') = \dfrac{3}{4}$.

Let $E$ be the event that the year has $53$ Mondays.

A leap year has $366$ days, which consists of $52$ complete weeks and $2$ extra days. The possible combinations for the $2$ extra consecutive days are (Sunday, Monday), (Monday, Tuesday), (Tuesday, Wednesday), (Wednesday, Thursday), (Thursday, Friday), (Friday, Saturday), and (Saturday, Sunday).

Out of these $7$ equally likely outcomes, $2$ contain a Monday. Thus, $P(E|L) = \dfrac{2}{7}$.

A non-leap year has $365$ days, which consists of $52$ complete weeks and $1$ extra day. This extra day can be any of the $7$ days of the week.

Thus, $P(E|L') = \dfrac{1}{7}$.

By the law of total probability:

$P(E) = P(L)P(E|L) + P(L')P(E|L')$

$P(E) = \left(\dfrac{1}{4} \times \dfrac{2}{7}\right) + \left(\dfrac{3}{4} \times \dfrac{1}{7}\right)$

$P(E) = \dfrac{2}{28} + \dfrac{3}{28} = \dfrac{5}{28}$

Answer: $\frac{5}{28}$

</details>

---

### Q21. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a class of 300 students, every student reads 5 news papers and every news paper is read by 60 students. Then the number of newspapers is

**Options:**

- **(A)** at least 30
- **(B)** at most 20
- **(C)** exactly 25
- **(D)** exactly 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) exactly 25**

**Detailed Solution:**

Let the number of newspapers be $N$.

The total number of student-newspaper reading pairs can be calculated in two ways.

Considering the students, there are $300$ students and each reads $5$ newspapers. Total readings $= 300 \times 5 = 1500$.

Considering the newspapers, there are $N$ newspapers and each is read by $60$ students. Total readings $= N \times 60$.

Equating the two values:

$N \times 60 = 1500$

$N = \dfrac{1500}{60} = 25$

The number of newspapers is exactly $25$.

Answer: exactly 25

</details>

---

### Q22. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

An urn contains nine balls of which three are red, four are blue and two are green. Three balls are drawn at random without replacement from the urn. The probability, that the three balls have different colours, is

**Options:**

- **(A)** $\dfrac{1}{3}$
- **(B)** $\dfrac{2}{7}$
- **(C)** $\dfrac{1}{21}$
- **(D)** $\dfrac{2}{23}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{2}{7}$**

**Detailed Solution:**

Total number of balls in the urn is $3 + 4 + 2 = 9$.

The total number of ways to draw $3$ balls from $9$ balls without replacement is $^{9}C_{3}$.

$^{9}C_{3} = \dfrac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$

For the three balls to have different colours, we must draw exactly $1$ red, $1$ blue, and $1$ green ball.

The number of ways to choose $1$ red ball from $3$ is $^{3}C_{1} = 3$.

The number of ways to choose $1$ blue ball from $4$ is $^{4}C_{1} = 4$.

The number of ways to choose $1$ green ball from $2$ is $^{2}C_{1} = 2$.

The total number of favourable outcomes is $3 \times 4 \times 2 = 24$.

The required probability is $\dfrac{24}{84} = \dfrac{2}{7}$.

Answer: $\dfrac{2}{7}$

</details>

---

### Q23. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let A and B be two events such that the probability that exactly one of them occurs is $\dfrac{2}{5}$ and the probability that A or B occurs is $\dfrac{1}{2}$, then the probability of both of them occur together is

**Options:**

- **(A)** 0.1
- **(B)** 0.2
- **(C)** 0.01
- **(D)** 0.02

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0.1**

**Detailed Solution:**

Let $P(A)$ and $P(B)$ be the probabilities of events $A$ and $B$ respectively.

The probability that exactly one of the events occurs is given by $P(A \cup B) - P(A \cap B)$.

We are given that $P(A \cup B) - P(A \cap B) = \dfrac{2}{5}$.

The probability that $A$ or $B$ occurs is $P(A \cup B) = \dfrac{1}{2}$.

Substituting the value of $P(A \cup B)$ in the first equation:

$\dfrac{1}{2} - P(A \cap B) = \dfrac{2}{5}$

$P(A \cap B) = \dfrac{1}{2} - \dfrac{2}{5}$

$P(A \cap B) = \dfrac{5 - 4}{10} = \dfrac{1}{10} = 0.1$

The probability that both of them occur together is $0.1$.

Answer: 0.1

</details>

---

### Q24. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Three houses are available in a locality. Three persons apply for the houses. Each applies for one house without consulting others. The probability that all the three persons apply for the same house is

**Options:**

- **(A)** $\dfrac{1}{9}$
- **(B)** $\dfrac{2}{9}$
- **(C)** $\dfrac{7}{9}$
- **(D)** $\dfrac{8}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{9}$**

**Detailed Solution:**

Total number of ways in which $3$ persons can apply for $3$ houses is $3 \times 3 \times 3 = 27$.

The number of ways in which all three persons apply for the same house is $3$ (either all apply for the first house, the second house, or the third house).

The required probability is $\dfrac{3}{27} = \dfrac{1}{9}$.

Answer: $\dfrac{1}{9}$

</details>

---

### Q25. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

There are 6 positive and 8 negative numbers. From these four numbers are chosen at random and multiplied. Then the probability, that the product is a negative number, is

**Options:**

- **(A)** $\frac {496}{1001}$
- **(B)** $\frac {505}{1001}$
- **(C)** $\frac {490}{1001}$
- **(D)** $\frac {504}{1001}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac {496}{1001}$**

**Detailed Solution:**

Total number of numbers $=8+6=14$ 4 numbers can be chosen out of 14 numbers in ${ }^{14} \mathrm{C}_4$ ways
The product of 4 numbers will be negative, if i. one is negative and three are positive
OR
ii. three are negative and one is positive.
$\begin{aligned}
\therefore \quad \text { Required probability } & =\frac{\left({ }^8 \mathrm{C}_1 \times{ }^6 \mathrm{C}_3\right)+\left({ }^8 \mathrm{C}_3 \times{ }^6 \mathrm{C}_1\right)}{{ }^{14} \mathrm{C}_4} \\
& =\frac{(8 \times 20)+(56 \times 6)}{1001} \\
& =\frac{160+336}{1001}=\frac{496}{1001}
\end{aligned}$

</details>

---

### Q26. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For an initial screening of an entrance exam, a candidate is given fifty problems to solve. If the probability that the candidate can solve any problem is $\frac{4}{5}$, then the probability, that he is unable to solve less than two problems, is

**Options:**

- **(A)** $\frac{201}{5}\left(\frac{1}{5}\right)^{49}$
- **(B)** $\frac{316}{25}\left(\frac{4}{5}\right)^{48}$
- **(C)** $\frac{54}{5}\left(\frac{4}{5}\right)^{49}$
- **(D)** $\frac{164}{25}\left(\frac{1}{5}\right)^{48}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{54}{5}\left(\frac{4}{5}\right)^{49}$**

**Detailed Solution:**

$q=$ Probability that the candidate can solve any problem $=\frac{4}{5}$
$$
\mathrm{p}=1-\frac{4}{5}=\frac{1}{5}
$$

Also, $\mathrm{n}=50$
$\begin{aligned} \therefore \quad & \text { Required probability }=\mathrm{P}(\mathrm{X} < 2) \\ & =\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1) \\ & ={ }^{50} \mathrm{C}_0\left(\frac{1}{5}\right)^0\left(\frac{4}{5}\right)^{50}+{ }^{50} \mathrm{C}_1\left(\frac{1}{5}\right)^1\left(\frac{4}{5}\right)^{49} \\ & =\left(\frac{4}{5}\right)^{50}+50\left(\frac{1}{5}\right)\left(\frac{4}{5}\right)^{49} \\ & =\left(\frac{4}{5}+\frac{50}{5}\right)\left(\frac{4}{5}\right)^{49} \\ & =\left(\frac{54}{5}\right)\left(\frac{4}{5}\right)^{49}\end{aligned}$

</details>

---

### Q27. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two cards are drawn successively with replacement from well shuffled pack of 52 cards, then the probability distribution of number of queens is

**Options:**

- **(A)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{144}{169} & \frac{24}{169} & \frac{1}{169} \\
\hline
\end{array}
- **(B)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{1}{169} & \frac{24}{169} & \frac{144}{169} \\
\hline
\end{array}
- **(C)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{24}{169} & \frac{1}{169} & \frac{144}{169} \\
\hline
\end{array}
- **(D)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{1}{169} & \frac{25}{169} & \frac{143}{169} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{144}{169} & \frac{24}{169} & \frac{1}{169} \\
\hline
\end{array}**

**Detailed Solution:**

Let $\mathrm{X}$ denote the number of queens.
$\therefore \quad$ Possible values of $\mathrm{X}$ are $0,1,2$.
$$
\begin{aligned}
& \mathrm{P}(\text { queen })=\frac{4}{52}=\frac{1}{13} \\
& \begin{aligned}
\mathrm{P}(\text { not a queen }) & =\frac{48}{52}=\frac{12}{13} \\
\mathrm{P}(\mathrm{X}=0) & =\frac{12}{13} \times \frac{12}{13} \\
& =\frac{144}{169} \\
\mathrm{P}(\mathrm{X}=1) & =\left(\frac{1}{13} \times \frac{12}{13}\right)+\left(\frac{12}{13} \times \frac{1}{13}\right) \\
& =\frac{12}{169}+\frac{12}{169}=\frac{24}{169} \\
\mathrm{P}(\mathrm{X}=2) & =\frac{1}{13} \times \frac{1}{13} \\
& =\frac{1}{169}
\end{aligned}
\end{aligned}
$$
\begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}[\mathrm{X}=x] & \frac{144}{169} & \frac{24}{169} & \frac{1}{169} \\
\hline
\end{array}

The probability distribution of $\mathrm{X}$ is

</details>

---

### Q28. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two dice are rolled, If both dice have six faces numbered $1,2,3,5,7,11$, then the probability that the sum of the numbers on upper most face is prime is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{1}{9}$
- **(D)** $\frac{2}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4}$**

**Detailed Solution:**

Two dice are rolled.
$\therefore \quad \mathrm{n}(\mathrm{S})=36$
A : Event that the sum of the numbers on upper most face is prime.
$\begin{aligned} \therefore \quad & A=\{(1,1),(1,2),(2,1),(2,3),(2,5),(2,11), \\ & (3,2),(5,2),(11,2)\}\end{aligned}$
$\therefore \quad \mathrm{P}(\mathrm{A})=\frac{9}{36}=\frac{1}{4}$

</details>

---

### Q29. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A card is drawn at random from a well shuffled pack of 52 cards. The probability that it is black card or face card is

**Options:**

- **(A)** $\frac{3}{13}$
- **(B)** $\frac{5}{13}$
- **(C)** $\frac{6}{13}$
- **(D)** $\frac{8}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{8}{13}$**

**Detailed Solution:**

Here, $\mathrm{n}(\mathrm{S})=52$
Let event A : A black card is drawn. event $B$ : A face card is drawn.
$$
n(A)=26, n(B)=12, n(A \cap B)=6
$$
Required probability
$$
\begin{aligned}
& =P(A \cup B) \\
& =P(A)+P(B)-P(A \cap B) \\
& =\frac{26}{52}+\frac{12}{52}-\frac{6}{52} \\
& =\frac{32}{52}=\frac{8}{13}
\end{aligned}
$$

</details>

---

### Q30. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A box contains 100 tickets numbered 1 to 100 . A ticket is drawn at random from the box. Then the probability, that number on the ticket is a perfect square, is

**Options:**

- **(A)** $\frac{1}{10}$
- **(B)** $\frac{3}{10}$
- **(C)** $\frac{7}{100}$
- **(D)** $\frac{9}{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{10}$**

**Detailed Solution:**

Let $X$ : Event that number on the ticket is perfect square.
$$
\begin{array}{ll}
\therefore \quad & \mathrm{X}=\{1,4,9,16,25,36,49,64,81,100\} \\
\therefore \quad & \mathrm{n}(\mathrm{X})=10 \\
& \text { Also, } \mathrm{n}(\mathrm{S})=100
\end{array}
$$
$\therefore \quad$ Required probability $=\frac{\mathrm{n}(\mathrm{x})}{\mathrm{n}(\mathrm{S})}=\frac{10}{100}=\frac{1}{10}$

</details>

---

### Q31. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

An irregular six faced die is thrown and the probability that, in 5 throws it will give 3 even numbers is twice the probability that it will give 2 even numbers. The number of times, in 6804 sets of 5 throws, you expect to give no even number is

**Options:**

- **(A)** $18$
- **(B)** $28$
- **(C)** $27$
- **(D)** $19$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $28$**

**Detailed Solution:**

Let $\mathrm{p}$ be the probability of getting even number.
Let random variable $\mathrm{X} \sim \mathrm{B}(\mathrm{n}, \mathrm{p})$
Given that $P(X=3)=2 P(X=2)$
$\therefore \quad{ }^5 \mathrm{C}_3 \mathrm{p}^3 \mathrm{q}^2=2{ }^5 \mathrm{C}_2 \mathrm{p}^2 \mathrm{q}^3$
$\therefore \quad \mathrm{p}=2 \mathrm{q}$
$\therefore \quad \mathrm{p}+\mathrm{q}=1 \Rightarrow \mathrm{p}=\frac{2}{3}$ and $\mathrm{q}=\frac{1}{3}$
$\therefore \quad \mathrm{P}(\mathrm{X}=0)={ }^5 \mathrm{C}_0 \mathrm{p}^0 \mathrm{q}^5=\frac{1}{3^5}$
$\therefore \quad$ In 1 set of 5 throws, number of times getting no even number is $\frac{1}{3^5}$.
$\therefore \quad$ In 6804 sets of 5 throws, number of times getting no even number is
$$
\frac{1}{3^5} \times 6804=28
$$

</details>

---

### Q32. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three of six vertices of a regular hexagon are chosen at random. The probability that the triangle with these three vertices is equilateral, equals

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{1}{10}$
- **(D)** $\frac{1}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{10}$**

**Detailed Solution:**

The number of triangles that can be drawn using 6 vertices is given by
$$
\mathrm{n}(\mathrm{S})={ }^6 \mathrm{C}_3=20
$$
$A$ : Event of selecting equilateral triangle. The equilateral triangle can be drawn if selected three vertices are alternate.
$\begin{aligned} & \therefore \quad \mathrm{n}(\mathrm{A})=2 \\ & \therefore \quad \mathrm{P}(\mathrm{A})=\frac{2}{20}=\frac{1}{10}\end{aligned}$

</details>

---

### Q33. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a game, 3 coins are tossed. A person is paid $₹ 7 /$, if he gets all heads or all tails; and he is supposed to pay $₹ 3 /-$, if he gets one head or two heads. The amount he can expect to win on an average per game is $₹$

**Options:**

- **(A)** $-0.5$
- **(B)** $0.5$
- **(C)** $1$
- **(D)** $-$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-0.5$**

**Detailed Solution:**

In a game, 3 coins are tossed, $\mathrm{P}($ getting all heads or all tails $)=\frac{2}{8}=\frac{1}{4}$
$\mathrm{P}($ getting one head or two heads $)=\frac{6}{8}=\frac{3}{4}$
Let $\mathrm{X}$ : number of rupees the person gets.
$\begin{aligned}
& P(X=7)=\frac{1}{4} \\
& P(X=-3)=\frac{3}{4}
\end{aligned}$
$\therefore \quad$ The amount he can expect to win $=$ Mean
$\begin{aligned}
& =\sum x_i \mathrm{p}_{\mathrm{i}} \\
& =7\left(\frac{1}{4}\right)+-3\left(\frac{3}{4}\right) \\
& =-0.5
\end{aligned}$

</details>

---

### Q34. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The three ships namely A, B and C sail from India to Africa. If the odds in favour of the ships reaching safely are $2: 5,3: 7$ and $6: 11$ respectively, then probability of all of them arriving safely is

**Options:**

- **(A)** $\frac{18}{595}$
- **(B)** $\frac{11}{34}$
- **(C)** $\frac{196}{217}$
- **(D)** $\frac{1}{595}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{18}{595}$**

**Detailed Solution:**

The probability that ship ' $A$ ' reaches safely is $\mathrm{P}(\mathrm{A})=\frac{2}{2+5}=\frac{2}{7}$
The probability that ship ' $B$ ' reaches safely is $\mathrm{P}(\mathrm{B})=\frac{3}{3+7}=\frac{3}{10}$
The probability that ship ' $\mathrm{C}$ ' reaches safely is $\mathrm{P}(\mathrm{C})=\frac{6}{6+11}=\frac{6}{17}$
$\therefore \quad$ Probability that all of them arriving safely $=\mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C})$ $=\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}(\mathrm{C})$
[Since A, B, C are all independent events]
$\begin{aligned}
& =\frac{2}{7} \times \frac{3}{10} \times \frac{6}{17} \\
& =\frac{18}{595}
\end{aligned}$

</details>

---

### Q35. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Three critics review a book. For the three critics the odds in favor of the book are $2: 5$, $3: 4$ and $4: 3$ respectively. The probability that the majority is in favor of the book, is given by

**Options:**

- **(A)** $\frac{183}{343}$
- **(B)** $\frac{160}{343}$
- **(C)** $\frac{209}{343}$
- **(D)** $\frac{134}{343}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{134}{343}$**

**Detailed Solution:**

The probability that the first critic favors the book is $\mathrm{P}(\mathrm{A})=\frac{2}{2+5}=\frac{2}{7}$
$\therefore \quad \mathrm{P}\left(\mathrm{A}^{\prime}\right)=1-\frac{2}{7}=\frac{5}{7}$
The probability that the second critic favors the book is $\mathrm{P}(\mathrm{B})=\frac{3}{3+4}=\frac{3}{7}$
$\therefore \quad \mathrm{P}\left(\mathrm{B}^{\prime}\right)=1-\frac{3}{7}=\frac{4}{7}$
The probability that the third critic favors the book is $\mathrm{P}(\mathrm{C})=\frac{4}{4+3}=\frac{4}{7}$
$\therefore \quad \mathrm{P}\left(\mathrm{C}^{\prime}\right)=1-\frac{4}{7}=\frac{3}{7}$
$\therefore \quad$ Majority will be in favor of the book if at least two critics favor the book.
Hence, the probability is
$\begin{aligned}
& \mathrm{P}\left(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C}^{\prime}\right)+\mathrm{P}\left(\mathrm{A} \cap \mathrm{B}^{\prime} \cap \mathrm{C}\right) \\
& \quad+\mathrm{P}\left(\mathrm{A}^{\prime} \cap \mathrm{B} \cap \mathrm{C}\right)+\mathrm{P}(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C}) \\
& =\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}\left(\mathrm{C}^{\prime}\right)+\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}\left(\mathrm{B}^{\prime}\right) \cdot \mathrm{P}(\mathrm{C}) \\
& \quad+\mathrm{P}\left(\mathrm{A}^{\prime}\right) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}(\mathrm{C})+\mathrm{P}(\mathrm{A}) \cdot \mathrm{P}(\mathrm{B}) \cdot \mathrm{P}(\mathrm{C}) \\
& =\frac{2}{7} \times \frac{3}{7} \times \frac{3}{7}+\frac{2}{7} \times \frac{4}{7} \times \frac{4}{7}+\frac{5}{7} \times \frac{3}{7} \times \frac{4}{7}+\frac{2}{7} \times \frac{3}{7} \times \frac{4}{7} \\
& =\frac{18}{343}+\frac{32}{343}+\frac{60}{343}+\frac{24}{343}=\frac{134}{343}
\end{aligned}$

</details>

---

### Q36. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A man takes a step forward with probability 0.4 and backwards with probability 0.6 . The probability that at the end of eleven steps, he is one step away from the starting point is

**Options:**

- **(A)** ${ }^{11} \mathrm{C}_6(0.24)^6$
- **(B)** ${ }^{11} \mathrm{C}_6(0.4)^6(0.6)^5$
- **(C)** ${ }^{11} \mathrm{C}_6(0.24)^5$
- **(D)** ${ }^{11} \mathrm{C}_6(0.4)^5(0.6)^6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) ${ }^{11} \mathrm{C}_6(0.4)^6(0.6)^5$**

**Detailed Solution:**

Let a step forward be a success and the step backward be a failure.
$\therefore \quad$ Probability of success $=\mathrm{p}=0.4$, and Probability of failure $=q=0.6$
Now, in 11 steps number of successes $=6$, number of failure $=5$
OR
number of successes $=5$, number of failures $=6$
Required probability $={ }^{11} \mathrm{C}_6 \mathrm{p}^6 \mathrm{q}^5+{ }^{11} \mathrm{C}_5 \mathrm{p}^5 \mathrm{q}^6$.
$\begin{aligned}
& =\frac{11 !}{6 ! 5 !} p^6 q^5+\frac{11 !}{5 ! 6 !} p^5 q^6 \\
& ={ }^{11} C_6 p^5 q^5(p+q) \\
& ={ }^{11} C_6(0-4)^5(0-6)^5(1) \\
& ={ }^{11} C_6(0 \cdot 4)^5(0 \cdot 6)^5 \\
& ={ }^{11} C_6(0 \cdot 24)^5
\end{aligned}$

</details>

---

### Q37. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

$A, B, C$ are three events, one of which must and only one can happen the odds in favour of $A$ are $4: 6$, odds against $B$ are $7: 3$, then odds against $C$ are

**Options:**

- **(A)** 7:3
- **(B)** 3:7
- **(C)** 6:4
- **(D)** 4:6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7:3**

**Detailed Solution:**

$P(A)=\frac{4}{4+6}=\frac{2}{5}, P(B)=\frac{3}{3+7}=\frac{3}{10}$
$\because A, B$ and $C$ are mutually exclusive and exhaustive
$\begin{aligned}
& \Rightarrow P(A)+P(B)+P(C)=1 \\
& \Rightarrow \frac{2}{5}+\frac{3}{10}+P(C)=1 \\
& \Rightarrow P(C)=\frac{3}{10}
\end{aligned}$
Now, odds against to the event $C=\frac{1-P(C)}{P(C)}=\frac{1-\frac{3}{10}}{\frac{3}{10}}=\frac{7}{3}$

</details>

---

### Q38. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the p.m.f. of a discrete random variable $X$ is $P(X=x)=\frac{c}{x^3}$, $x=1,2,3=0$, otherwise then $E(X)$ is equal to

**Options:**

- **(A)** $\frac{297}{294}$
- **(B)** $\frac{249}{225}$
- **(C)** $\frac{343}{297}$
- **(D)** $\frac{294}{251}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{294}{251}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/6U456WzQvA4mIrCJ2FWFrglMVbXh74iyWxz_0EQN8H4.original.fullsize.png">

$\begin{aligned} & \because \sum P_i=1 \\ & \Rightarrow \frac{251}{216} C \\ & \Rightarrow C=\frac{216}{251} \\ & \text { now } E(x)=\sum p_i x_i=\frac{49}{36} C=\frac{49}{36} \times \frac{216}{251}=\frac{294}{251}\end{aligned}$

</details>

---

### Q39. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three critics review a book. For the three critics, the odds in favour of the book are $(5: 2),(4: 3)$ and $(3: 4)$ respectively. The probability that the majority is in favour of the book is

**Options:**

- **(A)** $\frac{149}{343}$
- **(B)** $\frac{185}{343}$
- **(C)** $\frac{209}{343}$
- **(D)** $\frac{129}{343}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{209}{343}$**

**Detailed Solution:**

$P\left(C_1\right)=\frac{5}{5+2}=\frac{5}{7}, P\left(C_2\right)=\frac{4}{4+3}=\frac{4}{7}, P\left(C_3\right)=\frac{3}{3+4}=\frac{3}{7}$
now, required probability
$\begin{aligned} & =P\left(C_1\right) \cdot P\left(C_2\right) \cdot P\left(\bar{C}_3\right)+P\left(\bar{C}_1\right) \cdot P\left(C_2\right) P\left(C_3\right)+P\left(C_1\right) \cdot P\left(\bar{C}_2\right) \cdot P\left(C_3\right)+P\left(C_1\right) \cdot P\left(C_2\right) \cdot P\left(C_3\right) \\ & =\frac{5}{7} \cdot \frac{4}{7} \cdot \frac{4}{7}+\frac{2}{7} \cdot \frac{4}{7} \cdot \frac{3}{7}+\frac{5}{7} \cdot \frac{3}{7} \cdot \frac{3}{7}+\frac{5}{7} \cdot \frac{4}{7} \cdot \frac{3}{7} \\ & =\frac{80+24+45+60}{343}=\frac{209}{343}\end{aligned}$

</details>

---

### Q40. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A fair die is tossed twice in succession. If $X$ denotes the number of sixes in two tosses, then the probability distribution of $X$ is given by

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/KM-t-xSmxUyjp74KupNfsHgpngv5f90l9NqUtJfHgNk.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ouQApMAY8emOlXftChfRmAbJUUoHEIy1pSB0bTGQEfI.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mCXlKv5W6CRdh1xCFxd_HClyDt6LsGM3J2jkiWLTLh0.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/89O400INOAPHQ6OL6vLEDXJ98ArZY0XqUyPRYnrX1Ck.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ouQApMAY8emOlXftChfRmAbJUUoHEIy1pSB0bTGQEfI.original.fullsize.png">**

**Detailed Solution:**

$P($ zero sin $)=\frac{25}{36}, P($ one sin $)=\frac{10}{36}, P($ two sixes $)=\frac{1}{36}$
Hence probability distribution
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/fuxKafAangpFhj_RyUtRGZdIJLH70JK570SCb2__dy4.original.fullsize.png">

</details>

---

### Q41. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The total number of ways, of dividing 52 cards amongst 4 players, so that 3 players have 17 cards each and fourth player has just one card, are

**Options:**

- **(A)** $\frac{52 !}{(17 !)^3}$
- **(B)** $\frac{52 !}{(17 !)^2}$
- **(C)** $\frac{52 !}{17 !}$
- **(D)** $\frac{52 !}{17}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{52 !}{(17 !)^3}$**

**Detailed Solution:**

Number of ways $=\frac{52 !}{17 ! \cdot 17 ! \cdot 17 ! \cdot 1 ! \cdot 3 !}=\frac{52 !}{(17 !)^3 \cdot 3 !}$
[By division into groups]

</details>

---

### Q42. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

One ticket is selected at random from 50 tickets numbered $\{00,01,02, \ldots . ., 49\}$. Then the probability that the sum of the igits on the selected ticket is 8 , given that the product of these digits is zero, is

**Options:**

- **(A)** $\frac{1}{50}$
- **(B)** $\frac{1}{14}$
- **(C)** $\frac{14}{50}$
- **(D)** $\frac{1}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{14}$**

**Detailed Solution:**

$\begin{aligned} & S=\{00,01,02, \ldots \ldots ., 49\}, n(S)=50 \\ & E_1=\{08,17,26,35,44\}, n\left(E_1\right)=5 \\ & E_2=\{00,01,02,03,04,05,06,07,08,09,10,20,30,40\}, n\left(E_2\right)=14 \\ & E_1 \cap E_2=\{08\}, n\left(E_1 \cap E_2\right)=1 \\ & \text { Required probability }=p\left(E_1 / E_2\right)=\frac{n\left(E_1 \cap E_2\right)}{n\left(E_2\right)}=\frac{1}{14}\end{aligned}$

</details>

---

### Q43. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that at least one of the events $A$ and $B$ occurs is 0.6 . If $A$ and $B$ occur simultaneously with probability 0.2 , then $P\left(A^{\prime}\right)+P\left(B^{\prime}\right)$ is equal to

**Options:**

- **(A)** 0.8
- **(B)** 0.4
- **(C)** 1.4
- **(D)** 1.2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1.2**

**Detailed Solution:**

$\begin{aligned} & P(A \cup B)=0.6 \text { and } P(A \cap B)=0.2 \\ & \text { Now } P\left(A^{\prime}\right)+P\left(B^{\prime}\right)=1-P(A)+1-P(B) \\ & =2-\{P(A)+P(B)\} \\ & =2-\{P(A \cup B)+P(A \cap B)\} \\ & =2-\{0.6+0.2\} \\ & =2-0.8 \\ & =1.2\end{aligned}$

</details>

---

### Q44. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

There are 2 shelves. One shelf has 5 Physics and 3 Bilogy books and other has 4 Physics and 2 Biology books. Then probability of drawing a Physics book is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{31}{48}$
- **(C)** $\frac{9}{14}$
- **(D)** $\frac{9}{38}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{31}{48}$**

**Detailed Solution:**

The required probability $=P\left(S_1\right) \cdot P\left(P / S_1\right)+P\left(S_2\right) \cdot P\left(P / S_2\right)$
$=\frac{1}{2} \times \frac{5}{8}+\frac{1}{2} \times \frac{4}{6}=\frac{31}{48}$

</details>

---

### Q45. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A family with three children is chose at random. The probability that the oldest and youngest children are of the same gender is

**Options:**

- **(A)** $\frac{3}{8}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{2}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

$\mathrm{S}=\{\mathrm{BBB}, \mathrm{BBG}, \mathrm{BGB}, \mathrm{BGG}, \mathrm{GBB}, \mathrm{GBG}, \mathrm{GGB}, \mathrm{GGG}\}$
$\mathrm{E}=\{\mathrm{BBB}, \mathrm{BGB}, \mathrm{GBG}, \mathrm{GGG}\}$
$P(\mathrm{E})=\frac{n(\mathrm{E})}{n(\mathrm{~S})}=\frac{4}{8}=\frac{1}{2}$

</details>

---

### Q46. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Five letters are placed at random in five addressed envelopes. The probability that all the letters are not dispatched in the respective right envelopes is

**Options:**

- **(A)** $\frac{1}{120}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{119}{120}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{119}{120}$**

**Detailed Solution:**

The number of ways in which all the litters go to the correct envelope is 1
Probability that all letter go to correct envelope $=\frac{1}{5 !}$
Probability that all letter do not go to correct envelope $=1-\frac{1}{5 !}$
$=\frac{119}{120}$

</details>

---

### Q47. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The incidence of occupational disease in an industry is such that the workmen have a $10 \%$ chance of suffering from it. The probability that out of 5 workmen, 3 or more will contract the disease is

**Options:**

- **(A)** $0.0856$
- **(B)** $0.000856$
- **(C)** $0.00856$
- **(D)** $0.0000856$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.00856$**

**Detailed Solution:**

$\begin{aligned} & { }^5 C_3\left(\frac{1}{10}\right)^3 \cdot\left(\frac{9}{10}\right)^2+{ }^5 C_4\left(\frac{1}{10}\right)^4\left(\frac{9}{10}\right)^1+{ }^5 C_5\left(\frac{1}{10}\right)^5\left(\frac{9}{10}\right)^0 \\ & =10 \times \frac{81}{10^5}+5 \times \frac{9}{10^5}+1 \times \frac{1}{10^5} \\ & =\frac{810+45+1}{10^5}=\frac{856}{10^5}=0.00856\end{aligned}$

</details>

---

### Q48. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $P^{\prime}\left(A^{\prime}\right)+P\left(B^{\prime}\right) P(A \cup B)=0.7$ then $P^{\prime}\left(A^{\prime}\right)+P\left(B^{\prime}\right)$ is

**Options:**

- **(A)** $1.1$
- **(B)** $0.6$
- **(C)** $1.8$
- **(D)** $1.6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1.1$**

**Detailed Solution:**

$\begin{aligned} & P\left(A^{\prime}\right)+P\left(B^{\prime}\right)=1-P(A)+1-P(B) \\ & =2-\{P(A)+P(B)\} \\ & =2-\{P(A \cup B)+P(A \cap B)\} \\ & =2-\{0.7+0.2\} \\ & =2-0.9 \\ & =1.1\end{aligned}$

</details>

---

### Q49. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\omega$ be a complex cube root of unity with $\omega \neq 1$. A fair die is thrown three times. If $r_1, r_2$ and $r_3$ are the numbers obtained on the die, then the probability that $\omega^{r_1}+\omega^{r_2}+\omega^{r_3}=0$, is

**Options:**

- **(A)** $\frac{1}{36}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{1}{9}$
- **(D)** $\frac{2}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{9}$**

**Detailed Solution:**

Solution:
$\begin{aligned} & \because \omega^{r_1}+\omega^{r_2}+\omega^{r_3}=0 \\ & \Rightarrow \text { each of } r_1, r_2, r_3 \text { belongs to each of the categories } 3 k, 3 k+1, \\ & 3 k+2\end{aligned}$
So the required probability
$3 \times \frac{1}{3} \times \frac{1}{3} \times \frac{1}{3}=\frac{2}{9}$

</details>

---

### Q50. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If three distinct numbers are chosen randomly from first 100 natural numbers, then the probability that all three of them are divisible by both 2 and 3 is

**Options:**

- **(A)** $\frac{4}{35}$
- **(B)** $\frac{4}{55}$
- **(C)** $\frac{4}{1155}$
- **(D)** $\frac{80}{231}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{4}{1155}$**

**Detailed Solution:**

First 100 natural numbers are $\{1,2,3,4,5, \ldots . ., 100\}$
Numbers divisible by both 2 and 3 are $\{6,12,18, \ldots . ., 96\}$ (total 16)
Now the required probability $=\frac{{ }^{16} C_3}{{ }^{100} C_3}=\frac{\frac{\lfloor 16}{\left\lfloor\left\lfloor\frac{16-3}{\lfloor 100}\right.\right.}}{\frac{13\lfloor 100-3}{\lfloor\lfloor}}$
$\begin{aligned} & =\frac{\lfloor 16}{3 \underline{3} 13} \times \frac{\underline{3} \mid 97}{\underline{100}} \\ & =\frac{14 \times 15 \times 16}{98 \times 99 \times 100}=\frac{4}{1155} \\ & \end{aligned}$

</details>

---

### Q51. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that least one of the events $E_1$ and occurs is 0.6. If the simultaneous occurrence of $E_1$ and $E_2$ is 0.2 , $\mathrm{P}\left(\mathrm{E}_1{ }^{\prime}\right)+\mathrm{P}\left(\mathrm{E}_2^{\prime}\right)=$

**Options:**

- **(A)** 0.4
- **(B)** 1.6
- **(C)** 1.2
- **(D)** 0.8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1.2**

**Detailed Solution:**

$\begin{aligned} & P\left(E_1 \cup E_2\right)=P\left(E_1\right)+P\left(E_2\right)-P\left(E_1 \cap E_2\right) \\ & \therefore 0.6=\left[1-P\left(E_1{ }^{\prime}\right)+1-P\left(E_2{ }^{\prime}\right)-P\left(E_1 \cap E_2\right)\right] \\ & P\left(E_1{ }^{\prime}\right)+P\left(E_2{ }^{\prime}\right)=2-0.2-0.6=1.2\end{aligned}$

</details>

---

### Q52. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let two cards are drawn at random from a pack of 52 playing cards. Let $\mathrm{X}$ be the number of aces obtained. Then the values of $\mathrm{E}(\mathrm{X})$ is

**Options:**

- **(A)** $\frac{5}{13}$
- **(B)** $\frac{1}{13}$
- **(C)** $\frac{2}{13}$
- **(D)** $\frac{37}{221}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{13}$**

**Detailed Solution:**

' $\mathrm{X}$ ' can take values 0.1 .2 .
Probability of getting no ace card.
$$
=\frac{{ }^{48} \mathrm{C}_2}{{ }^{52} \mathrm{C}_2}=\frac{48 !}{2 ! 46 !} \times \frac{2 ! 50 !}{52 !}=\frac{188}{221}
$$
Probability of getting 1 ace card
$$
=\frac{{ }^4 \mathrm{C}_1 \times{ }^{48} \mathrm{C}_1}{{ }^{52} \mathrm{C}_2}=\frac{4 \times 48}{52 !} 2 ! 50 !=\frac{32}{221}
$$
Probability of getting 2 ace cards
$$
\begin{aligned}
& =\frac{{ }^4 \mathrm{C}_2 \times{ }^{48} \mathrm{C}_1}{{ }^{52} \mathrm{C}_2}=\frac{4 !}{2 ! 2 !} \times \frac{2 ! 50 !}{52 !}=\frac{1}{221} \\
& \mathrm{E}(\mathrm{X})=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\
& =(0)\left(\frac{188}{221}\right)+(1)\left(\frac{32}{221}\right)+(2)\left(\frac{1}{221}\right)=\frac{2}{13}
\end{aligned}
$$

</details>

---

### Q53. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Rooms in a hotel are numbered from 1 to 19 . Rooms are allocated at random as guests arrive. The first guest to arrive is given a room which is a prime number. The probability that the second guest to arrive is given a room which is a prime number is

**Options:**

- **(A)** $\frac{8}{19} \times \frac{7}{18}$
- **(B)** $\frac{8}{19}$
- **(C)** $\frac{8}{19} \times \frac{7}{19}$
- **(D)** $\frac{7}{18}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7}{18}$**

**Detailed Solution:**

Prime numbers from 1 to 19 are $2,3,5,7,11,13,17,19$ i.e. 8 such numbers. The room with prime number is given to the first guest.
$\therefore$ The probability that second guest will get a room with prime number $=\frac{7}{18}$.

</details>

---

### Q54. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A coin is tossed three times. If $\mathrm{X}$ denote the absolute difference between the number of heads and the number of tails, then, $\mathrm{P}(\mathrm{X}=1)=$

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{2}{3}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{4}$**

**Detailed Solution:**

A coin is tossed 3 times
$$
\Rightarrow \mathrm{n}(\mathrm{S})=8
$$
Possibilities are : $(1 \mathrm{H}, 2 \mathrm{~T}),(2 \mathrm{H}, 1 \mathrm{~T}),(3 \mathrm{H}, 0 \mathrm{~T}),(0 \mathrm{H}, 3 \mathrm{~T})$
Thus values of $\mathrm{X}$ can be 1 and 3 .
Now $(1 \mathrm{H}, 2 \mathrm{~T})$ can occur in 3 ways. Also $(2 \mathrm{H}, 1 \mathrm{~T})$ can occur in 3 ways.
$$
\therefore \mathrm{P}(\mathrm{X}=1)=\frac{6}{8}=\frac{3}{4}
$$

</details>

---

### Q55. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For two events $\mathrm{A}$ and $\mathrm{B}, \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{5}{6}, \mathrm{P}(\mathrm{A})=\frac{1}{6}, \mathrm{P}(\mathrm{B})=\frac{2}{3}$, then $\mathrm{A}$ and $\mathrm{B}$ are

**Options:**

- **(A)** independent
- **(B)** mutually exhaustive
- **(C)** mutually exclusive
- **(D)** complementary

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) mutually exclusive**

**Detailed Solution:**

$$
\begin{aligned}
& \text { We have, } \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\frac{5}{6}, \mathrm{P}(\mathrm{A})=\frac{1}{6}, \mathrm{P}(\mathrm{B})=\frac{2}{3} \\
& \mathrm{P}(\mathrm{A} \cup \mathrm{B})=\mathrm{P}(\mathrm{A})+\mathrm{P}(\mathrm{B})-\mathrm{P}(\mathrm{A} \cap \mathrm{B}) \\
& \therefore \frac{5}{6}=\frac{1}{6}+\frac{3}{2}-\mathrm{P}(\mathrm{A} \cap \mathrm{B}) \Rightarrow \mathrm{P}(\mathrm{A} \cap \mathrm{B})=0
\end{aligned}
$$
Thus A and B are mutually exclusive events.

</details>

---

### Q56. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A coin is tossed and a die is thrown. The probability that the outcome will be head or a number greater than 4 or both, is

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** $\frac{1}{6}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{2}{3}$**

**Detailed Solution:**

The probability of getting head when a coin is thrown $=\frac{1}{2}$ The probability of getting a number greater than 4 when a die is thrown
$$
=\frac{2}{6}=\frac{1}{3}
$$
Hence required probability $=\left(\frac{1}{2}\right)\left(\frac{2}{3}\right)+\left(\frac{1}{2}\right)\left(\frac{1}{3}\right)+\left(\frac{1}{2}\right)\left(\frac{1}{3}\right)=\frac{4}{6}=\frac{2}{3}$

</details>

---

### Q57. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A lot of 100 bulbs contains 10 defective bulbs. Five bulbs selected at random from the lot and sent to retail store, then the probability that the store will receive at most one defective bulb is

**Options:**

- **(A)** 0.59049
- **(B)** 0.91854
- **(C)** 0.6561
- **(D)** 0.32805

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.91854**

**Detailed Solution:**

Probability of finding defective bulb $=\frac{10}{100}=0.1$
Let $\mathrm{p}=0.1 \Rightarrow 1=0.9$
We have $\mathrm{n}=5$ and to get required probability $\mathrm{x}=0$ and $\mathrm{x}=1$
$$
\begin{aligned}
& \therefore \mathrm{P}={ }^5 \mathrm{C}_0(0.1)^2(0.9)^5+{ }^5 \mathrm{C}_1(0.1)^1(0.9)^4 \\
& (0.9)^5+(5)(0.1)(0.9)^4 \\
& =(0.9)^4[0.9+0.5]=(0.9)_4(1.4) \\
& =(0.81)(0.81)(1.4)=(0.6561)(1.4)=0.91854
\end{aligned}
$$

</details>

---

### Q58. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two unbiased dice are thrown. Then the probability that neither a doublet nor a total of 10 will appear is

**Options:**

- **(A)** $\frac{1}{12}$
- **(B)** $\frac{1}{36}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{7}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{7}{9}$**

**Detailed Solution:**

Number of ways of getting doublet $=6$
Number of ways getting a total of 10 are $\Rightarrow(4,6),(5,5),(6,4)$ i.e. 3 ways
Here $(5,5)$ is common.
$\therefore$ Total ways of getting doublet or total of 10 are $6+3-1=8$
Hence required probability $=\frac{36-8}{36}=\frac{28}{36}=\frac{7}{9}$

</details>

---

### Q59. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two dice are rolled simultaneously. The probability that the sum of the two numbers on the dice is a prime number, is

**Options:**

- **(A)** $\frac{5}{11}$
- **(B)** $\frac{5}{12}$
- **(C)** $\frac{7}{12}$
- **(D)** $\frac{7}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{12}$**

**Detailed Solution:**

The sum of numbers on the two dice can be $(2,3, \ldots ., 12)$ and prime numbers in this list are 2, 3, 5, 7, 11 .
$2 \Rightarrow(1,1)$ and $3 \Rightarrow(1,2),(2,1)$ and 5
$\Rightarrow(1,4),(2,3),(3,2),(4,1)$,
$7 \Rightarrow(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ and 11
$\Rightarrow(5,6),(6,5)$
Thus $\mathrm{n}(\mathrm{s})=6 \times 6=36$ and $\mathrm{n}(\mathrm{E})=15$
Hence required probability $=\frac{15}{36}=\frac{5}{12}$

</details>

---

### Q60. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The odds in favour of getting sum multiple of 3, when pair of dice are thrown is

**Options:**

- **(A)** $4: 5$
- **(B)** $2: 3$
- **(C)** $1: 2$
- **(D)** $3: 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1: 2$**

**Detailed Solution:**

(A)
When a pair of dice is thrown, then total outcomes are $6 \times 6=36$.
Now the odds in favour of getting the sum, which is multiple of 3 are
$(1,2)(2,1) \Rightarrow \operatorname{sum} 3$
$(3,3),(2,4),(4,2),(1,5),(5,1) \Rightarrow \operatorname{sum} 6$
$(4,5),(5,4),(6,3),(3,6) \Rightarrow \operatorname{sum} 9$
$(6,6) \Rightarrow$ sum 12
Thus Number of favourable cases $=2+5+4+1=12$
So, odds in fovour $=\frac{12}{24}=\frac{1}{2}$

</details>

---

### Q61. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The odds in favour of drawing a king from a pack of 52 playing cards is

**Options:**

- **(A)** 1:12
- **(B)** 4:1
- **(C)** 12:1
- **(D)** 1:4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1:12**

**Detailed Solution:**

(B)
Probability of drawing a king $=\frac{4}{52}=\frac{1}{13}$
$\therefore$ Probability of NOT drawing a king $=\frac{12}{13}$
Hence odds is favour of drawing a king $=1: 12$.

</details>

---

### Q62. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The letters of the word ' LOGARITHM' are arranged at random. The probability that arrangements starts with vowel and end with consonant is

**Options:**

- **(A)** $\frac{71}{9 !}$
- **(B)** $\frac{18}{9 !}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

$(C)$
The word LOGARITHM contains 3 vowels and 6 consonants.
Starting vowel can be chosen from 3 vowels in 3 distinct ways and the end consonant could be chosen from 6 consonants in 6 distinct ways and the rest of 7 letters can be permuted among themselves in $7 !$ ways.
So total number of ways this arrangement could be done are $3 \times 6 \times 7 !$.
So, the probability that words could start with vowel and end with consonant $=\frac{3 \times 6 \times 7 !}{9 !}=\frac{1}{4}$

</details>

---

### Q63. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $n(X)=700, n(A)=200, n(B)=300, n(A \cap B)=100$, where $X$ is universal set and $A$ and $\mathrm{B}$ are subsets of $\mathrm{X}$, then $\mathrm{n}\left(\mathrm{A}^{\prime} \cap \mathrm{B}^{\prime}\right)=$

**Options:**

- **(A)** 300
- **(B)** 400
- **(C)** 340
- **(D)** 240

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 300**

**Detailed Solution:**

$\mathrm{n}(\mathrm{A} \cap \mathrm{B})=\mathrm{n}(\mathrm{A} \cup \mathrm{B})$
$=\mathrm{n}(\mathrm{u})-\mathrm{n}(\mathrm{A} \cup \mathrm{B})$
$=\mathrm{n}(\mathrm{u})-\{\mathrm{n}(\mathrm{A})+\mathrm{n}(\mathrm{B})-\mathrm{n}(\mathrm{A} \cap \mathrm{B})\}$
$=700-\{200+300-100\}=300$

</details>

---

### Q64. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a single throw of three dice, the probability of getting a sum at least 5 is

**Options:**

- **(A)** $\frac{53}{54}$
- **(B)** $\frac{51}{54}$
- **(C)** $\frac{1}{54}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{53}{54}$**

**Detailed Solution:**

Here $n(S)=6 \times 6 \times 6=216$
Sum less than $5 \equiv\{(1,1,1),(1,1,2),(1,2,1),(2,1,1)\}$
Here $\mathrm{P}($ sum less than 5$)=\frac{4}{216}=\frac{1}{54}$
$\therefore \mathrm{P}($ at least 5$)=\mathrm{P}(\geq 5)=1-\mathrm{P}( < 5)$
$=1-\frac{1}{54}=\frac{53}{54}$

</details>

---

### Q65. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

It is observed that <math><mn>25</mn><mi>%</mi></math> of the cases related to child labour reported to the police station are solved. If <math><mi></mi><mn>6</mn></math> new cases are reported, then the probability that atleast <math><mn>5</mn></math> of them will be solved is ________

**Options:**

- **(A)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math>
- **(B)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>1024</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>2048</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>4096</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>4096</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>P</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo> </mo><mo> </mo><mo> </mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo> </mo><mo> </mo><mi>n</mi><mo>=</mo><mn>6</mn></math>  
Required Probability <math><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>6</mn></mrow></mfenced></math>  
<math><mo>=</mo><msup><mrow><mi></mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math>  
<math><mo>∵</mo><mfenced separators="|"><mrow><mi>p</mi><mi></mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mi>r</mi></mrow></mfenced></mrow></mfenced><mo>=</mo><msup><mrow><mi></mi></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><msup><mrow><mi>p</mi></mrow><mrow><mi>r</mi></mrow></msup><msup><mrow><mi>q</mi></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup></math>  
<math><mo>=</mo><mfrac><mrow><mn>19</mn></mrow><mrow><mn>4096</mn></mrow></mfrac></math>

</details>

---

### Q66. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that three cards drawn from a pack of 52 cards, all are red is

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>**

**Detailed Solution:**

Total number of ways that three card drawn from a pack of 52 cards are <math><msup><mrow></mrow><mrow><mn>52</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></math> and number of ways that three red. cards drawn are <math><msup><mrow></mrow><mrow><mn>26</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></math> . 
Required probability <math><mo>=</mo><mfrac><mrow><msup><mrow></mrow><mrow><mn>26</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mrow><msup><mrow></mrow><mrow><mn>52</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>26</mn><mo>×</mo><mn>25</mn><mo>×</mo><mn>24</mn></mrow><mrow><mn>52</mn><mo>×</mo><mn>51</mn><mo>×</mo><mn>50</mn></mrow></mfrac></math>  
<math><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>17</mn></mrow></mfrac></math>

</details>

---

### Q67. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `3`

Letters in the word <math> <mrow> <mtext>HULULULU</mtext> </mrow> </math> are rearranged. The probability of all three <math> <mtext>L</mtext> </math> being together is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>28</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>23</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>28</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>S</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mn>8</mn><mo>!</mo></mrow> <mrow> <mn>4</mn><mo>!</mo><mtext> </mtext><mn>3</mn><mo>!</mo></mrow> </mfrac> </mrow> </math>      (total arrangements) 
<math> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>A</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mn>6</mn><mo>!</mo></mrow> <mrow> <mn>4</mn><mo>!</mo></mrow> </mfrac> </mrow> </math>        (Arrangement when all L together)
So, the required probability is
 <math> <mrow> <mi>P</mi><mrow><mo>(</mo> <mi>A</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>A</mi> <mo>)</mo></mrow></mrow> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>S</mi> <mo>)</mo></mrow></mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mfrac> <mrow> <mn>6</mn><mo>!</mo></mrow> <mrow> <mn>4</mn><mo>!</mo></mrow> </mfrac> </mrow> <mrow> <mfrac> <mrow> <mn>8</mn><mo>!</mo></mrow> <mrow> <mn>4</mn><mo>!</mo><mtext> </mtext><mn>3</mn><mo>!</mo></mrow> </mfrac> </mrow> </mfrac> <mo>=</mo><mfrac> <mrow> <mn>6</mn><mo>!</mo><mtext> </mtext><mo>× </mo><mn>3</mn><mo>!</mo></mrow> <mrow> <mn>8</mn><mo>!</mo></mrow> </mfrac> </mrow> </math>
<math> <mrow> <mi>P</mi><mrow><mo>(</mo> <mi>A</mi> <mo>)</mo></mrow><mo>=</mo><mfrac> <mrow> <mn>6</mn><mo>!</mo><mtext> </mtext><mo>× </mo><mn>3</mn> </mrow> <mrow> <mn>8</mn><mo>×</mo><mn>7</mn><mo>×</mo><mn>6</mn><mo>!</mo></mrow> </mfrac> <mo>=</mo><mfrac> <mn>3</mn> <mrow> <mn>28</mn></mrow> </mfrac> </mrow> </math>

</details>

---

### Q68. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

A boy tosses fair coin <math> <mn>3</mn> </math> times. If he gets ₹ <math><mn>2</mn><mi>x</mi></math> for <math><mi>x</mi></math> heads then his expected gain equals to ₹........

**Options:**

- **(A)** <math><mn>1</mn></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mn>3</mn></math>
- **(D)** <math><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>3</mn></math>**

**Detailed Solution:**

For <math><mi>x</mi></math> heads, he gets <math><mi>y</mi><mo>=</mo><mn>2</mn><mi>x</mi></math><table border="1">	<tbody>		<tr>			<td>x</td>			<td>0</td>			<td>1</td>			<td>2</td>			<td>3</td>		</tr>		<tr>			<td>y</td>			<td>0</td>			<td>2</td>			<td>4</td>			<td>6</td>		</tr>		<tr>			<td>p (y)</td>			<td><math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math></td>		</tr>	</tbody></table>Excepted gain <math>  <mrow>   <mo>=</mo><mstyle displaystyle='true'>    <mo>&#x2211;</mo> <mrow>     <msub>      <mi>y</mi>      <mi>i</mi>     </msub>     <msub>      <mi>p</mi>      <mi>i</mi>     </msub>     </mrow>   </mstyle></mrow></math>
<math><mo>=</mo><mn>0</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>6</mn><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>6</mn></mrow><mrow><mn>8</mn></mrow></mfrac><mo>=</mo><mn>3</mn></math>

</details>

---

### Q69. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

The odds against solving a problem by $A$ and $B$ are $3: 2$ and $2: 1$ respectively, then the probability that the problem will be solved, is

**Options:**

- **(A)** $\frac{3}{5}$
- **(B)** $\frac{2}{15}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{11}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{5}$**

**Detailed Solution:**

Given, $P(A)=\frac{3}{2+3}=\frac{3}{5}, P(B)=\frac{2}{2+1}=\frac{2}{3}$
and $P(\bar{A})=1-\frac{3}{5}=\frac{2}{5}, P(\bar{B})=1-\frac{2}{3}=\frac{1}{3}$
$\therefore$ Required probability
$$
\begin{array}{l}
=P(A \cap \bar{B})+P(\bar{A} \cap B)+P(\bar{A} \cap \bar{B}) \\
=P(A) \cdot P(\bar{B})+P(\bar{A}) \cdot P(B)+P(\bar{A}) \cdot P(\bar{B}) \\
=\frac{3}{5} \cdot \frac{1}{3}+\frac{2}{5} \cdot \frac{2}{3}+\frac{2}{5} \cdot \frac{1}{3} \\
=\frac{1}{5}+\frac{4}{15}+\frac{2}{15} \\
=\frac{3+4+2}{15}=\frac{9}{15}=\frac{3}{5}
\end{array}
$$

</details>

---

### Q70. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `2`

One card is drawn at random from a pack of playing cards the probability that it is an ace or black king or the queen of the heart will be

**Options:**

- **(A)** $\frac{3}{52}$
- **(B)** $\frac{7}{52}$
- **(C)** $\frac{6}{52}$
- **(D)** $\frac{1}{52}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7}{52}$**

**Detailed Solution:**

$\therefore$ Required probability $=\frac{{ }^{4} C_{1}+{ }^{2} C_{1}+{ }^{1} C_{1}}{{ }^{52} C_{1}}$
$=\frac{4+2+1}{52}=\frac{7}{52}$

</details>

---

### Q71. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

A four digit number is to be formed using the digits 1, 2, $3,4,5,6,7$ (no digit is being repeated in any number). Then, the probability that it is $>4000$, is

**Options:**

- **(A)** $3 / 2$
- **(B)** $1 / 2$
- **(C)** 4/7
- **(D)** $3 / 7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4/7**

**Detailed Solution:**

Total cases $={ }^{7} P_{4}=840$
Favourable cases $=4 \times 6 \times 5 \times 4=480$
$\therefore$ Required probability $=\frac{480}{840}=\frac{4}{7}$

</details>

---

### Q72. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `2`

If two dice are thrown together. Then, the probability that the sum of the numbers appearing on them is a prime number, is

**Options:**

- **(A)** $1 / 2$
- **(B)** $3 / 7$
- **(C)** $5 / 12$
- **(D)** $7 / 12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $5 / 12$**

**Detailed Solution:**

Total cases $=36$
Prime number are $2,3,5,7,11$. $\therefore$ Favourable cases $=15$
Required probability $=\frac{15}{36}=\frac{5}{12}$

</details>

---

### Q73. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `3`

From a group of 8 boys and 3 girls, a commitee of 5 members to be formed. Find the probability that 2 particular girls are included in the committe is

**Options:**

- **(A)** $\frac{4}{11}$
- **(B)** $\frac{2}{11}$
- **(C)** $\frac{6}{11}$
- **(D)** $\frac{8}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{11}$**

**Detailed Solution:**

Total $\quad$ number $\quad$ of $\quad$ ways $={ }^{8} \mathrm{C}_{2}{ }^{3} \mathrm{C}_{3}+{ }^{8} \mathrm{C}_{3}{ }^{3} \mathrm{C}_{2}+{ }^{8} \mathrm{C}_{4}{ }^{3} \mathrm{C}_{1}+{ }^{8} \mathrm{C}_{5}{ }^{3} \mathrm{C}_{0}$
$=28 \times 1+56 \times 3+70 \times 3+56 \times 1$
$=462$
Number of ways in which 2 particular girls are included ${ }^{9} C_{3}=84$
$\therefore$ Required probability $=\frac{84}{462}=\frac{2}{11}$

</details>

---

### Q74. MHT CET 2009

*Type:* `singleCorrect` | *Level:* `2`

Given $P(A \cup B)=0.6, P(A \cap B)=0.2$, the probability of exactly one of the event occurs is

**Options:**

- **(A)** $0.4$
- **(B)** $0.2$
- **(C)** $0.6$
- **(D)** $0.8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.4$**

**Detailed Solution:**

Given, $P(A \cup B)=0.6, P(A \cap B)=0.2$
Probability of exactly one of the event occurs is
$P(\bar{A} \cap B)+P(A \cap \bar{B})$
$=P(B)-P(A \cap B)+P(A)-P(A \cap B)$
$=P(A \cup B)+P(A \cap B)-2 P(A \cap B)$
$\quad[\because P(A \cup B)=P(A)+P(B)-P(A \cap B)]$
$=P(A \cup B)-P(A \cap B)$
$=0.6-0.2$
$=0.4$

</details>

---

### Q75. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `2`

A parents has two children. If one of them is boy, then the probability that other is, also a boy, is

**Options:**

- **(A)** $1 / 2$
- **(B)** $1 / 4$
- **(C)** $1 / 3$
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1 / 3$**

**Detailed Solution:**

Total cases are $B B, B G, G B, G G=4$ Favourable cases are $B B, B G, G B=3$ Let $P(A)=$ Probability of a boy in two children
$$
=\frac{3}{4}
$$
The probability that the second child is also a boy is $P(A \cap B)=\frac{1}{4}$
We have to find $P(B / A)=\frac{P(A \cap B)}{P(A)}=\frac{1 / 4}{3 / 4}=\frac{1}{3}$

</details>

---

### Q76. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

Three letters, to each of which corresponds an envelope, are placed in the envelopes at random. The probability that all the letters are not placed in the right envelopes, is

**Options:**

- **(A)** $\frac{1}{6}$
- **(B)** $\frac{5}{6}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{5}{6}$**

**Detailed Solution:**

Three letters can be placed in 3 envelopes in $3 !$ ways, whereas there is only one way of placing them in their right envelopes. So, probability that all the letters are placed in the right envelopes $=\frac{1}{3 !}$
Hence, required probability $=1-\frac{1}{3 !}=\frac{5}{6}$

</details>

---

### Q77. MHT CET 2007

*Type:* `singleCorrect` | *Level:* `1`

Two dice are rolled one after the other. The probability that the number on the first is smaller than the number on the second, is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{7}{18}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{5}{12}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{5}{12}$**

**Detailed Solution:**

Let $A_{i}=$ Event of getting a number $i$ on first die.
$B_{i}=$ Event of getting a number more than $i$ on
second die.
The required probability
$$

</details>

---

