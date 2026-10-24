# MHT CET Mathematics - Probability

## Topic 7: Bernoulli Trial and Binomial Distribution

**Total Questions:** 89

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the random variable $X \sim B(4, 0.5)$, then probability $P(X < 3 \,/\, X \geq 1) = \ldots$

**Options:**

- **(A)** $\dfrac{1}{4}$
- **(B)** $\dfrac{3}{4}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{2}{3}$**

**Detailed Solution:**

Given $X \sim B(4, 0.5)$, the probability mass function is $P(X = x) = ^{4}C_{x} (0.5)^{x} (0.5)^{4-x} = ^{4}C_{x} \left(\dfrac{1}{2}\right)^{4} = \dfrac{^{4}C_{x}}{16}$.

We need to find $P(X < 3 \mid X \geq 1) = \dfrac{P(X < 3 \cap X \geq 1)}{P(X \geq 1)} = \dfrac{P(1 \leq X \leq 2)}{P(X \geq 1)}$.

Calculating the numerator:
$P(1 \leq X \leq 2) = P(X = 1) + P(X = 2) = \dfrac{^{4}C_{1}}{16} + \dfrac{^{4}C_{2}}{16} = \dfrac{4}{16} + \dfrac{6}{16} = \dfrac{10}{16}$.

Calculating the denominator:
$P(X \geq 1) = 1 - P(X = 0) = 1 - \dfrac{^{4}C_{0}}{16} = 1 - \dfrac{1}{16} = \dfrac{15}{16}$.

Therefore, $P(X < 3 \mid X \geq 1) = \dfrac{\dfrac{10}{16}}{\dfrac{15}{16}} = \dfrac{10}{15} = \dfrac{2}{3}$.

Answer: $\dfrac{2}{3}$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X$ follows a Binomial distribution with parameters $n = 8$ and $p = \dfrac{1}{2}$ then $P(|X - 4| \leq 2)$

**Options:**

- **(A)** $\dfrac{59}{64}$
- **(B)** $\dfrac{119}{128}$
- **(C)** $\dfrac{117}{128}$
- **(D)** $\dfrac{29}{32}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{119}{128}$**

**Detailed Solution:**

Given $X$ follows a Binomial distribution with $n = 8$ and $p = \dfrac{1}{2}$.

The probability mass function is given by $P(X = r) = ^{8}C_{r} \left(\dfrac{1}{2}\right)^{r} \left(\dfrac{1}{2}\right)^{8-r} = \dfrac{^{8}C_{r}}{256}$.

We need to find $P(|X - 4| \leq 2)$.

$|X - 4| \leq 2 \Rightarrow -2 \leq X - 4 \leq 2 \Rightarrow 2 \leq X \leq 6$

The required probability is $P(2 \leq X \leq 6) = 1 - (P(X = 0) + P(X = 1) + P(X = 7) + P(X = 8))$.

Calculating the individual probabilities:

$P(X = 0) = \dfrac{^{8}C_{0}}{256} = \dfrac{1}{256}$

$P(X = 1) = \dfrac{^{8}C_{1}}{256} = \dfrac{8}{256}$

$P(X = 7) = \dfrac{^{8}C_{7}}{256} = \dfrac{8}{256}$

$P(X = 8) = \dfrac{^{8}C_{8}}{256} = \dfrac{1}{256}$

Substituting these values:

$P(2 \leq X \leq 6) = 1 - \left(\dfrac{1 + 8 + 8 + 1}{256}\right) = 1 - \dfrac{18}{256} = \dfrac{238}{256} = \dfrac{119}{128}$

Answer: $\dfrac{119}{128}$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum and product of mean and variance of a binomial distribution are 3 and 2 respectively. Then, $P(X > 0) = \ldots$

**Options:**

- **(A)** $\dfrac{15}{16}$
- **(B)** $\dfrac{1}{16}$
- **(C)** $\dfrac{1}{4}$
- **(D)** $\dfrac{11}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{15}{16}$**

**Detailed Solution:**

Let the mean be $m = np$ and variance be $v = npq$.

Given $m + v = 3$ and $mv = 2$.

Solving these equations, we get $m = 2, v = 1$ or $m = 1, v = 2$.

For a binomial distribution, variance is always less than the mean since $q < 1$. Thus, $m = 2$ and $v = 1$.

$np = 2$ and $npq = 1$

Dividing the two equations, $q = \dfrac{1}{2}$.

Since $p + q = 1$, $p = \dfrac{1}{2}$.

Substituting $p$ in $np = 2$, we get $n = 4$.

$P(X > 0) = 1 - P(X = 0)$

$P(X > 0) = 1 - ^{4}C_{0} p^0 q^4 = 1 - \left(\dfrac{1}{2}\right)^4$

$P(X > 0) = 1 - \dfrac{1}{16} = \dfrac{15}{16}$

Answer: $\dfrac{15}{16}$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

It is known that $10\%$ of certain articles manufactured are defective. What is the probability that in a random sample of $12$ such articles, $9$ are defective?

**Options:**

- **(A)** $22\left(\dfrac{9^3}{10^{12}}\right)$
- **(B)** $22\left(\dfrac{9^{12}}{10^{12}}\right)$
- **(C)** $22\left(\dfrac{9^3}{10^9}\right)$
- **(D)** $22\left(\dfrac{9^3}{10^{11}}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $22\left(\dfrac{9^3}{10^{11}}\right)$**

**Detailed Solution:**

Let $p$ be the probability of a defective article.

$p = \dfrac{10}{100} = \dfrac{1}{10}$

Let $q$ be the probability of a non-defective article.

$q = 1 - p = 1 - \dfrac{1}{10} = \dfrac{9}{10}$

The number of trials is $n = 12$.

The probability of getting exactly $9$ defective articles is given by the binomial distribution formula:

$P(X = 9) = ^{12}C_{9} p^9 q^3$

$P(X = 9) = ^{12}C_{9} \left(\dfrac{1}{10}\right)^9 \left(\dfrac{9}{10}\right)^3$

$^{12}C_{9} = \dfrac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$

$P(X = 9) = 220 \times \dfrac{1}{10^9} \times \dfrac{9^3}{10^3}$

$P(X = 9) = 220 \times \dfrac{9^3}{10^{12}}$

$P(X = 9) = 22 \times \dfrac{9^3}{10^{11}}$

Answer: $22\left(\dfrac{9^3}{10^{11}}\right)$

</details>

---

### Q5. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $X \sim B(10, 0.4)$, then the probability that $X$ takes a value at least 2 is:

**Options:**

- **(A)** $1 - 5(0.4)(0.6)^9$
- **(B)** $1 - (0.6)^9(4.6)$
- **(C)** $1 - (0.4)^{10}$
- **(D)** $0.66$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 - (0.6)^9(4.6)$**

**Detailed Solution:**

Given $X \sim B(n, p)$ with $n = 10$ and $p = 0.4$.

The probability of failure is $q = 1 - p = 0.6$.

The probability that $X$ takes a value at least 2 is $P(X \ge 2)$.

$P(X \ge 2) = 1 - P(X < 2) = 1 - [P(X = 0) + P(X = 1)]$

Using the binomial probability formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X = 0) = ^{10}C_{0} (0.4)^0 (0.6)^{10} = (0.6)^{10}$

$P(X = 1) = ^{10}C_{1} (0.4)^1 (0.6)^9 = 10(0.4)(0.6)^9 = 4(0.6)^9$

Adding these probabilities:

$P(X = 0) + P(X = 1) = (0.6)^{10} + 4(0.6)^9 = (0.6)^9 (0.6 + 4) = 4.6(0.6)^9$

Therefore, $P(X \ge 2) = 1 - 4.6(0.6)^9$.

Answer: $1 - (0.6)^9(4.6)$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A coin is tossed n times. The probability of getting a head at least once is greater than $0.8$, then the least value of n is

**Options:**

- **(A)** $2$
- **(B)** $3$
- **(C)** $4$
- **(D)** $5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3$**

**Detailed Solution:**

Let $n$ be the number of times the coin is tossed.

The probability of getting a head in a single toss is $p = \dfrac{1}{2}$ and the probability of getting a tail is $q = \dfrac{1}{2}$.

The probability of getting at least one head in $n$ tosses is given by $1 - P(\text{no head}) = 1 - \left(\dfrac{1}{2}\right)^n$.

According to the given condition, $1 - \left(\dfrac{1}{2}\right)^n > 0.8$

$\left(\dfrac{1}{2}\right)^n < 1 - 0.8$

$\left(\dfrac{1}{2}\right)^n < 0.2$

$\dfrac{1}{2^n} < \dfrac{1}{5}$

$2^n > 5$

The smallest integer $n$ that satisfies this inequality is $n = 3$.

Answer: $3$

</details>

---

### Q7. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a person hits a target is $0.6$. If he fires $5$ shots at the target, then the probability that he hits the target at least once is

**Options:**

- **(A)** $0.96912$
- **(B)** $0.46980$
- **(C)** $0.89716$
- **(D)** $0.98976$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.98976$**

**Detailed Solution:**

Let $p$ be the probability of hitting the target and $q$ be the probability of missing the target.

Given $p = 0.6$

$q = 1 - p = 1 - 0.6 = 0.4$

Number of shots fired, $n = 5$

The probability of hitting the target at least once is given by $1 - P(X = 0)$, where $P(X = 0)$ is the probability of missing all $5$ shots.

$P(X = 0) = ^{5}C_{0} p^{0} q^{5} = (0.4)^{5}$

$(0.4)^{5} = 0.01024$

Required probability $= 1 - 0.01024 = 0.98976$

Answer: $0.98976$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Suppose that $60\%$ of all families own a mobile set. If $11$ families are interviewed at random, then the probability that $8$ families own a mobile set is..... (Given that $(0.6)^8 = 0.0168$)

**Options:**

- **(A)** $0.1235$
- **(B)** $0.1677$
- **(C)** $0.1774$
- **(D)** $0.5321$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.1774$**

**Detailed Solution:**

Let $p$ be the probability that a family owns a mobile set.

$p = 0.6$

$q = 1 - p = 0.4$

Number of families interviewed, $n = 11$.

The probability that exactly $8$ families own a mobile set is given by the binomial distribution formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$.

$P(X = 8) = ^{11}C_{8} (0.6)^8 (0.4)^3$

$^{11}C_{8} = ^{11}C_{3} = \dfrac{11 \times 10 \times 9}{3 \times 2 \times 1} = 165$

Substituting the given value $(0.6)^8 = 0.0168$:

$P(X = 8) = 165 \times 0.0168 \times 0.064$

$P(X = 8) = 10.56 \times 0.0168 = 0.177408$

Rounding to four decimal places, the probability is $0.1774$.

Answer: $0.1774$

</details>

---

### Q9. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the mean of a binomial distribution is twice its variance and $n = 18$, then the probability of success is...

**Options:**

- **(A)** $1$
- **(B)** $\dfrac{1}{2}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1}{2}$**

**Detailed Solution:**

Let $p$ be the probability of success and $q$ be the probability of failure in the binomial distribution.

The mean of the binomial distribution is $np$ and the variance is $npq$.

Given that the mean is twice its variance:

$np = 2npq$

Since $n = 18$ and $p \neq 0$, dividing both sides by $np$ gives:

$1 = 2q$

$q = \dfrac{1}{2}$

The probability of success is $p = 1 - q$.

$p = 1 - \dfrac{1}{2} = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A coin whose faces are marked as $5$ and $3$ is tossed $4$ times. The probability that the sum of the numbers on the coin is greater than $17$ is ___

**Options:**

- **(A)** $\dfrac{5}{8}$
- **(B)** $\dfrac{1}{16}$
- **(C)** $\dfrac{5}{16}$
- **(D)** $\dfrac{11}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{5}{16}$**

**Detailed Solution:**

Let $x$ be the number of times the face marked $5$ appears in $4$ tosses.

The number of times the face marked $3$ appears is $4 - x$.

The sum of the numbers on the coin is $S = 5x + 3(4 - x) = 2x + 12$.

For the sum to be greater than $17$:

$2x + 12 > 17$

$2x > 5 \Rightarrow x > 2.5$

Since $x$ is an integer and $0 \le x \le 4$, the possible values for $x$ are $3$ and $4$.

Assuming a fair coin, the probability of getting either face is $\dfrac{1}{2}$.

The probability of getting the face marked $5$ exactly $3$ times is:

$P(x = 3) = ^{4}C_{3} \left(\dfrac{1}{2}\right)^3 \left(\dfrac{1}{2}\right)^1 = \dfrac{4}{16}$

The probability of getting the face marked $5$ exactly $4$ times is:

$P(x = 4) = ^{4}C_{4} \left(\dfrac{1}{2}\right)^4 \left(\dfrac{1}{2}\right)^0 = \dfrac{1}{16}$

The required probability is:

$P(S > 17) = P(x = 3) + P(x = 4) = \dfrac{4}{16} + \dfrac{1}{16} = \dfrac{5}{16}$

Answer: $\dfrac{5}{16}$

</details>

---

### Q11. MHT CET 2026 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Given that $X\sim B(20, p)$ if $E(X)=8$ then $Var(X)$ is

**Options:**

- **(A)** $\dfrac{8}{5}$
- **(B)** $\dfrac{2}{5}$
- **(C)** $\dfrac{24}{5}$
- **(D)** $\dfrac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{24}{5}$**

**Detailed Solution:**

For a binomial distribution $X \sim B(n, p)$, the expected value is given by $E(X) = np$ and the variance is given by $Var(X) = npq$, where $q = 1 - p$.

Given $n = 20$ and $E(X) = 8$.

$np = 8$

$20p = 8$

$p = \dfrac{8}{20} = \dfrac{2}{5}$

The value of $q$ is:

$q = 1 - p = 1 - \dfrac{2}{5} = \dfrac{3}{5}$

The variance is:

$Var(X) = npq = 8 \times \dfrac{3}{5} = \dfrac{24}{5}$

Answer: $\dfrac{24}{5}$

</details>

---

### Q12. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Four cards are drawn successively with replacement from well shuffled deck of 52 cards, then the probability that only two cards are club cards is ...........

**Options:**

- **(A)** $\dfrac{26}{128}$
- **(B)** $\dfrac{24}{128}$
- **(C)** $\dfrac{27}{128}$
- **(D)** $\dfrac{28}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{27}{128}$**

**Detailed Solution:**

Probability of drawing a club card, $p = \dfrac{13}{52} = \dfrac{1}{4}$

Probability of not drawing a club card, $q = 1 - p = \dfrac{3}{4}$

Number of trials, $n = 4$

Number of successes, $r = 2$

Using binomial distribution, $P(X = r) = ^{n}C_{r} p^{r} q^{n-r}$

$P(X = 2) = ^{4}C_{2} \left(\dfrac{1}{4}\right)^{2} \left(\dfrac{3}{4}\right)^{2}$

$P(X = 2) = 6 \times \dfrac{1}{16} \times \dfrac{9}{16}$

$P(X = 2) = \dfrac{54}{256} = \dfrac{27}{128}$

Answer: $\dfrac{27}{128}$

</details>

---

### Q13. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X \sim B(n, p)$ follows a binomial distribution with $n = 6$. If $9P(X = 4) = P(X = 2)$, then the probability of success $p$ is..

**Options:**

- **(A)** $0.125$
- **(B)** $0.75$
- **(C)** $0.25$
- **(D)** $0.375$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.25$**

**Detailed Solution:**

Given $X \sim B(n, p)$ with $n = 6$.

The probability mass function is $P(X = k) = ^{n}C_{k} p^k (1-p)^{n-k}$.

Substituting $k = 4$ and $k = 2$ in the given condition $9P(X = 4) = P(X = 2)$:

$9 \times ^{6}C_{4} p^4 (1-p)^2 = ^{6}C_{2} p^2 (1-p)^4$

Since $^{6}C_{4} = ^{6}C_{2} = 15$, dividing both sides by $15 p^2 (1-p)^2$ gives:

$9p^2 = (1-p)^2$

Taking the square root on both sides, since $p > 0$ and $1-p > 0$:

$3p = 1 - p$

$4p = 1$

$p = 0.25$

Answer: $0.25$

</details>

---

### Q14. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability that a bomb will hit the target is $0.8$. Out of 6 bombs dropped, probability that at least 1 will miss the target is...

**Options:**

- **(A)** $\left(\dfrac{1}{5}\right)^6$
- **(B)** $1 - \left(\dfrac{1}{5}\right)^6$
- **(C)** $\left(\dfrac{4}{5}\right)^6$
- **(D)** $1 - \left(\dfrac{4}{5}\right)^6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1 - \left(\dfrac{4}{5}\right)^6$**

**Detailed Solution:**

Probability of a bomb hitting the target, $p = 0.8 = \dfrac{4}{5}$

Probability of a bomb missing the target, $q = 1 - p = 0.2 = \dfrac{1}{5}$

Total number of bombs dropped, $n = 6$

The probability that at least one bomb misses the target is $1 - P(\text{no bomb misses the target})$

$P(\text{no bomb misses the target}) = P(\text{all 6 bombs hit the target}) = p^6 = \left(\dfrac{4}{5}\right)^6$

Required probability $= 1 - \left(\dfrac{4}{5}\right)^6$

Answer: $1 - \left(\dfrac{4}{5}\right)^6$

</details>

---

### Q15. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If in $6$ trials, X is a binomial random variable which follows the relation $9P(x = 4) = P(x = 2)$, then the probability of failure is...

**Options:**

- **(A)** $0.125$
- **(B)** $0.25$
- **(C)** $0.375$
- **(D)** $0.75$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.75$**

**Detailed Solution:**

Let $p$ be the probability of success and $q$ be the probability of failure in a single trial, where $p + q = 1$.

For a binomial distribution with $n = 6$ trials, the probability of $x$ successes is given by $P(X = x) = ^{6}C_{x} p^{x} q^{6-x}$.

Given the relation:

$9P(X = 4) = P(X = 2)$

Substituting the binomial probabilities:

$9 \times ^{6}C_{4} p^{4} q^{2} = ^{6}C_{2} p^{2} q^{4}$

Since $^{6}C_{4} = ^{6}C_{2} = 15$, we can cancel it from both sides:

$9 p^{4} q^{2} = p^{2} q^{4}$

Dividing both sides by $p^{2} q^{2}$ (assuming $p, q \neq 0$):

$9 p^{2} = q^{2}$

Taking the square root on both sides (since probabilities are non-negative):

$3p = q$

We know that $p + q = 1$. Substituting $p = \dfrac{q}{3}$:

$\dfrac{q}{3} + q = 1$

$\dfrac{4q}{3} = 1$

$q = \dfrac{3}{4} = 0.75$

Thus, the probability of failure is $0.75$.

</details>

---

### Q16. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A fair die is thrown 4 times. If getting a prime number on the die is considered as a success, then the probability of getting no success at all is $\ldots$

**Options:**

- **(A)** $\dfrac{1}{16}$
- **(B)** $\dfrac{15}{16}$
- **(C)** $\dfrac{1}{81}$
- **(D)** $\dfrac{16}{81}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{16}$**

**Detailed Solution:**

The possible outcomes when a fair die is thrown are $1, 2, 3, 4, 5, 6$.

The prime numbers on a die are $2, 3, 5$.

Probability of getting a prime number (success) in a single throw is $p = \dfrac{3}{6} = \dfrac{1}{2}$.

Probability of not getting a prime number (failure) in a single throw is $q = 1 - p = \dfrac{1}{2}$.

The die is thrown $4$ times, so $n = 4$.

The probability of getting no success at all ($0$ successes) is given by the binomial distribution:

$P(X = 0) = ^{4}C_{0} p^{0} q^{4}$

$P(X = 0) = 1 \times \left(\dfrac{1}{2}\right)^{0} \times \left(\dfrac{1}{2}\right)^{4} = \dfrac{1}{16}$

Answer: $\dfrac{1}{16}$

</details>

---

### Q17. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed 9 times. On each toss, a man predicts that the outcome will be heads. The probability that the number of successful predictions is strictly greater than the number of unsuccessful predictions is...

**Options:**

- **(A)** $\dfrac{3}{4}$
- **(B)** $\dfrac{1}{6}$
- **(C)** $\dfrac{1}{2}$
- **(D)** $-\dfrac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{2}$**

**Detailed Solution:**

Let $X$ be the number of successful predictions, which corresponds to the number of heads obtained in $9$ tosses.

The number of unsuccessful predictions is $9 - X$.

The condition that the number of successful predictions is strictly greater than the number of unsuccessful predictions is $X > 9 - X$, which gives $2X > 9$, or $X \ge 5$.

Since the coin is fair, the probability of getting heads is $p = \dfrac{1}{2}$ and tails is $q = \dfrac{1}{2}$.

The probability of getting exactly $r$ heads is $P(X = r) = ^{9}C_{r} \left(\dfrac{1}{2}\right)^{9}$.

The required probability is $P(X \ge 5) = P(X = 5) + P(X = 6) + P(X = 7) + P(X = 8) + P(X = 9)$.

Using the property $^{n}C_{r} = ^{n}C_{n-r}$, we have $P(X = r) = P(X = 9-r)$.

Thus, $P(X \ge 5) = P(X \le 4)$.

Since the sum of all probabilities is $1$, $P(X \ge 5) + P(X \le 4) = 1$.

Substituting $P(X \le 4) = P(X \ge 5)$, we get $2P(X \ge 5) = 1$.

$P(X \ge 5) = \dfrac{1}{2}$

Answer: $\dfrac{1}{2}$

</details>

---

### Q18. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

On average, one out of 10 persons is busy. If six persons are selected at random, then the probability that at least 5 of them will be busy is...

**Options:**

- **(A)** $\dfrac{25}{(10)^6}$
- **(B)** $\dfrac{35}{(10)^6}$
- **(C)** $\dfrac{45}{(10)^6}$
- **(D)** $\dfrac{55}{(10)^6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{55}{(10)^6}$**

**Detailed Solution:**

The probability that a person is busy is $p = \dfrac{1}{10}$.

The probability that a person is not busy is $q = 1 - p = \dfrac{9}{10}$.

The number of persons selected is $n = 6$.

The probability that at least 5 persons are busy is $P(X \ge 5) = P(X = 5) + P(X = 6)$.

Using the binomial distribution $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X = 5) = ^{6}C_{5} \left(\dfrac{1}{10}\right)^5 \left(\dfrac{9}{10}\right)^1 = 6 \times \dfrac{9}{10^6} = \dfrac{54}{10^6}$

$P(X = 6) = ^{6}C_{6} \left(\dfrac{1}{10}\right)^6 \left(\dfrac{9}{10}\right)^0 = 1 \times \dfrac{1}{10^6} = \dfrac{1}{10^6}$

$P(X \ge 5) = \dfrac{54}{10^6} + \dfrac{1}{10^6} = \dfrac{55}{10^6}$

Answer: $\dfrac{55}{(10)^6}$

</details>

---

### Q19. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and the variance of a binomial variate X are 1 and 0.75 respectively, then which of the following is true?

**Options:**

- **(A)** $P(X = 0) = 3P(X = 4)$
- **(B)** $P(X = 1) = 2P(X = 2)$
- **(C)** $P(X = 3) = 3P(X = 4)$
- **(D)** $3P(X = 0) = 4P(X = 1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $P(X = 1) = 2P(X = 2)$**

**Detailed Solution:**

Given mean $np = 1$ and variance $npq = 0.75 = \dfrac{3}{4}$.

Dividing variance by mean:

$q = \dfrac{npq}{np} = \dfrac{3}{4}$

Since $p + q = 1$, $p = 1 - \dfrac{3}{4} = \dfrac{1}{4}$.

Substituting $p$ in $np = 1$:

$n \left(\dfrac{1}{4}\right) = 1 \Rightarrow n = 4$

The probability of $X = r$ is given by $P(X = r) = ^{n}C_{r} p^r q^{n-r}$.

Calculating $P(X = 1)$ and $P(X = 2)$:

$P(X = 1) = ^{4}C_{1} \left(\dfrac{1}{4}\right)^1 \left(\dfrac{3}{4}\right)^3 = 4 \times \dfrac{1}{4} \times \dfrac{27}{64} = \dfrac{27}{64}$

$P(X = 2) = ^{4}C_{2} \left(\dfrac{1}{4}\right)^2 \left(\dfrac{3}{4}\right)^2 = 6 \times \dfrac{1}{16} \times \dfrac{9}{16} = \dfrac{54}{256} = \dfrac{27}{128}$

Comparing the two probabilities:

$2P(X = 2) = 2 \times \dfrac{27}{128} = \dfrac{27}{64} = P(X = 1)$

Thus, $P(X = 1) = 2P(X = 2)$.

Answer: $P(X = 1) = 2P(X = 2)$

</details>

---

### Q20. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a fair coin is tossed 8 times, then the probability of getting at most 2 heads is...

**Options:**

- **(A)** $\dfrac{37}{64}$
- **(B)** $\dfrac{37}{256}$
- **(C)** $\dfrac{37}{128}$
- **(D)** $\dfrac{37}{512}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{37}{256}$**

**Detailed Solution:**

Let $X$ be the number of heads obtained in $8$ tosses of a fair coin.

The probability of getting a head is $p = \dfrac{1}{2}$ and a tail is $q = \dfrac{1}{2}$.

The probability of getting exactly $r$ heads is given by $P(X = r) = ^{8}C_{r} \left(\dfrac{1}{2}\right)^r \left(\dfrac{1}{2}\right)^{8-r} = \dfrac{^{8}C_{r}}{256}$.

The probability of getting at most $2$ heads is $P(X \le 2) = P(X = 0) + P(X = 1) + P(X = 2)$.

$P(X \le 2) = \dfrac{^{8}C_{0}}{256} + \dfrac{^{8}C_{1}}{256} + \dfrac{^{8}C_{2}}{256}$

$P(X \le 2) = \dfrac{1 + 8 + 28}{256} = \dfrac{37}{256}$

Answer: $\dfrac{37}{256}$

</details>

---

### Q21. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two dice are thrown successively 4 times and getting a doublet is called a success. The probability of getting at least 1 success is

**Options:**

- **(A)** $\dfrac{50}{1296}$
- **(B)** $\dfrac{1246}{1296}$
- **(C)** $\dfrac{625}{1296}$
- **(D)** $\dfrac{671}{1296}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{671}{1296}$**

**Detailed Solution:**

Probability of getting a doublet in a single throw of two dice is $p = \dfrac{6}{36} = \dfrac{1}{6}$.

Probability of not getting a doublet is $q = 1 - \dfrac{1}{6} = \dfrac{5}{6}$.

The dice are thrown $n = 4$ times.

Probability of getting at least one success is $P(X \ge 1) = 1 - P(X = 0)$.

$P(X = 0) = ^{4}C_{0} p^{0} q^{4} = \left(\dfrac{5}{6}\right)^{4} = \dfrac{625}{1296}$.

$P(X \ge 1) = 1 - \dfrac{625}{1296} = \dfrac{671}{1296}$.

Answer: $\dfrac{671}{1296}$

</details>

---

### Q22. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The centers for disease control have determined that when a person is given a vaccine, the probability that the person will develop immunity to a virus is $0.8$. If $8$ people are given this vaccine, then the probability that exactly $4$ will develop immunity is...

**Options:**

- **(A)** $(0.2)(0.8)^4$
- **(B)** $(0.112)(0.8)^4$
- **(C)** $(0.112)(0.8)^6$
- **(D)** $(0.2)^4(0.8)^4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(0.112)(0.8)^4$**

**Detailed Solution:**

Let $p$ be the probability of developing immunity, $p = 0.8$.

Let $q$ be the probability of not developing immunity, $q = 1 - p = 0.2$.

The number of trials is $n = 8$.

Using the binomial distribution formula, the probability of exactly $r$ successes is given by $P(X = r) = ^{n}C_{r} p^r q^{n-r}$.

For $r = 4$ successes:

$P(X = 4) = ^{8}C_{4} (0.8)^4 (0.2)^4$

Calculating $^{8}C_{4}$:

$^{8}C_{4} = \dfrac{8!}{4!(8-4)!} = \dfrac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = 70$

Substituting this back into the probability expression:

$P(X = 4) = 70 \times (0.8)^4 \times (0.2)^4$

Since $(0.2)^4 = 0.0016$:

$70 \times (0.2)^4 = 70 \times 0.0016 = 0.112$

Therefore, $P(X = 4) = (0.112)(0.8)^4$.

Answer: $(0.112)(0.8)^4$

</details>

---

### Q23. MHT CET 2026 (13 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a multiple-choice examination, there are $10$ questions with one correct option out of $4$ options for each question. A student gets $4$ marks for each correct answer and $1$ mark is deducted for each incorrect answer. The probability that a student, guessing randomly on every question, scores $30$ marks in this exam is...

**Options:**

- **(A)** $\dfrac{45}{4^{10}}$
- **(B)** $\dfrac{135}{4^{10}}$
- **(C)** $\dfrac{405}{4^{10}}$
- **(D)** $\dfrac{810}{4^{10}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{405}{4^{10}}$**

**Detailed Solution:**

Let $x$ be the number of correct answers and $y$ be the number of incorrect answers.

$x + y = 10$

The total marks scored is given by $4x - y = 30$.

Substituting $y = 10 - x$, we get:

$4x - (10 - x) = 30$

$5x = 40 \Rightarrow x = 8$

The student must answer exactly $8$ questions correctly and $2$ questions incorrectly.

The probability of guessing a correct answer is $p = \dfrac{1}{4}$ and an incorrect answer is $q = \dfrac{3}{4}$.

Using binomial distribution, the probability of getting exactly $8$ correct answers is:

$P(X = 8) = ^{10}C_{8} \left(\dfrac{1}{4}\right)^{8} \left(\dfrac{3}{4}\right)^{2}$

$P(X = 8) = 45 \times \dfrac{1}{4^{8}} \times \dfrac{9}{4^{2}}$

$P(X = 8) = \dfrac{405}{4^{10}}$

Answer: $\dfrac{405}{4^{10}}$

</details>

---

### Q24. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The odds in favour of A winning a game of table tennis against B are 1:2. If 3 games are to be played, then the probability of A winning at least two games out of the three is.....

**Options:**

- **(A)** $\dfrac{1}{27}$
- **(B)** $\dfrac{2}{27}$
- **(C)** $\dfrac{5}{27}$
- **(D)** $\dfrac{7}{27}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{7}{27}$**

**Detailed Solution:**

Given odds in favour of A winning are $1:2$.

Probability of A winning a game is $p = \dfrac{1}{1+2} = \dfrac{1}{3}$.

Probability of A losing a game is $q = 1 - p = \dfrac{2}{3}$.

Total number of games played is $n = 3$.

Probability of A winning at least two games is $P(X \ge 2) = P(X = 2) + P(X = 3)$.

Using binomial distribution, $P(X = r) = ^{n}C_{r} p^{r} q^{n-r}$.

$P(X \ge 2) = ^{3}C_{2} \left(\dfrac{1}{3}\right)^{2} \left(\dfrac{2}{3}\right)^{1} + ^{3}C_{3} \left(\dfrac{1}{3}\right)^{3} \left(\dfrac{2}{3}\right)^{0}$

$P(X \ge 2) = 3 \times \dfrac{1}{9} \times \dfrac{2}{3} + 1 \times \dfrac{1}{27} \times 1$

$P(X \ge 2) = \dfrac{6}{27} + \dfrac{1}{27} = \dfrac{7}{27}$

Answer: $\dfrac{7}{27}$

</details>

---

### Q25. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $X \sim B\left(6, \dfrac{1}{2}\right)$. Then the maximum probability occurs at

**Options:**

- **(A)** $X = 1$
- **(B)** $X = 2$
- **(C)** $X = 3$
- **(D)** $X = 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $X = 3$**

**Detailed Solution:**

Given $X \sim B\left(6, \dfrac{1}{2}\right)$, the probability mass function is given by

$P(X = x) = ^{6}C_{x} \left(\dfrac{1}{2}\right)^{x} \left(1 - \dfrac{1}{2}\right)^{6-x} = ^{6}C_{x} \left(\dfrac{1}{2}\right)^{6}$

To maximize $P(X = x)$, the binomial coefficient $^{6}C_{x}$ must be maximum.

For an even integer $n$, the maximum value of $^{n}C_{x}$ occurs at $x = \dfrac{n}{2}$.

Here $n = 6$, so the maximum value occurs at $x = \dfrac{6}{2} = 3$.

Thus, the maximum probability occurs at $X = 3$.

</details>

---

### Q26. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X \sim B(n, p)$, then the value of $\dfrac{P(X = k)}{P(X = k - 1)}$ is

**Options:**

- **(A)** $\left(\dfrac{n - k}{k}\right)\dfrac{p}{q}$
- **(B)** $\left(\dfrac{n - k + 1}{k}\right)\dfrac{p}{q}$
- **(C)** $\left(\dfrac{n - k}{k - 1}\right)\dfrac{p}{q}$
- **(D)** $\left(\dfrac{n - k + 1}{k - 1}\right)\dfrac{p}{q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\left(\dfrac{n - k + 1}{k}\right)\dfrac{p}{q}$**

**Detailed Solution:**

For a binomial distribution $X \sim B(n, p)$, the probability of $k$ successes is given by $P(X = k) = ^{n}C_{k} p^k q^{n-k}$, where $q = 1 - p$.

Substituting $k$ and $k-1$, we get:

$P(X = k) = ^{n}C_{k} p^k q^{n-k}$

$P(X = k - 1) = ^{n}C_{k-1} p^{k-1} q^{n-k+1}$

Taking the ratio of the two probabilities:

$\dfrac{P(X = k)}{P(X = k - 1)} = \dfrac{^{n}C_{k} p^k q^{n-k}}{^{n}C_{k-1} p^{k-1} q^{n-k+1}}$

$\dfrac{P(X = k)}{P(X = k - 1)} = \dfrac{^{n}C_{k}}{^{n}C_{k-1}} \cdot \dfrac{p}{q}$

Using the property of combinations $\dfrac{^{n}C_{r}}{^{n}C_{r-1}} = \dfrac{n - r + 1}{r}$:

$\dfrac{P(X = k)}{P(X = k - 1)} = \left(\dfrac{n - k + 1}{k}\right)\dfrac{p}{q}$

Answer: $\left(\dfrac{n - k + 1}{k}\right)\dfrac{p}{q}$

</details>

---

### Q27. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability mass function of a random variable X is given by
$P(X = x) = \dfrac{{}^{5}C_x}{2^5}$, for $x = 0, 1, 2, 3, 4, 5$ and $= 0$, otherwise.
Then which of the following is correct?

**Options:**

- **(A)** $p(x \leq 2) = p(x \geq 3)$
- **(B)** $p(x \leq 2) > p(x \geq 3)$
- **(C)** $p(x \leq 2) < p(x \geq 3)$
- **(D)** $p(x \leq 2) = 2p(x \geq 3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $p(x \leq 2) = p(x \geq 3)$**

**Detailed Solution:**

The given probability mass function is $P(X = x) = \dfrac{^{5}C_x}{2^5}$.

We evaluate $P(X \leq 2)$ and $P(X \geq 3)$.

$P(X \leq 2) = P(X = 0) + P(X = 1) + P(X = 2)$

$P(X \geq 3) = P(X = 3) + P(X = 4) + P(X = 5)$

Using the property of combinations $^{n}C_r = ^{n}C_{n-r}$, we have:

$^{5}C_0 = ^{5}C_5 \Rightarrow P(X = 0) = P(X = 5)$

$^{5}C_1 = ^{5}C_4 \Rightarrow P(X = 1) = P(X = 4)$

$^{5}C_2 = ^{5}C_3 \Rightarrow P(X = 2) = P(X = 3)$

Adding the corresponding terms gives:

$P(X = 0) + P(X = 1) + P(X = 2) = P(X = 3) + P(X = 4) + P(X = 5)$

$P(X \leq 2) = P(X \geq 3)$

Answer: $p(x \leq 2) = p(x \geq 3)$

</details>

---

### Q28. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $X \sim B(n, p)$. If $E(X) = 2$ and $\text{Var}(X) = 1$, then the probability of getting at most one success is .....

**Options:**

- **(A)** $0.0625$
- **(B)** $0.2500$
- **(C)** $0.3125$
- **(D)** $0.6875$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.3125$**

**Detailed Solution:**

For a binomial distribution $X \sim B(n, p)$, the mean and variance are given by:

$E(X) = np = 2$

$\text{Var}(X) = npq = 1$

Dividing the variance by the mean:

$q = \dfrac{npq}{np} = \dfrac{1}{2}$

Since $p + q = 1$, we get $p = \dfrac{1}{2}$.

Substituting $p$ in $np = 2$:

$n \left(\dfrac{1}{2}\right) = 2 \Rightarrow n = 4$

The probability of getting at most one success is:

$P(X \le 1) = P(X = 0) + P(X = 1)$

$P(X \le 1) = ^{4}C_{0} \left(\dfrac{1}{2}\right)^0 \left(\dfrac{1}{2}\right)^4 + ^{4}C_{1} \left(\dfrac{1}{2}\right)^1 \left(\dfrac{1}{2}\right)^3$

$P(X \le 1) = \dfrac{1}{16} + \dfrac{4}{16} = \dfrac{5}{16}$

$P(X \le 1) = 0.3125$

Answer: $0.3125$

</details>

---

### Q29. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability that an event A happens in a trial is 0.4 . If three independent trials are made, then the probability that A happens at least once is

**Options:**

- **(A)** 0.784
- **(B)** 0.745
- **(C)** 0.754
- **(D)** 0.775

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0.784**

**Detailed Solution:**

Let $p$ be the probability that event A happens in a trial, so $p = 0.4$.

The probability that event A does not happen in a trial is $q = 1 - p = 1 - 0.4 = 0.6$.

For $n = 3$ independent trials, the probability that A happens at least once is given by $1 - P(\text{A does not happen in any trial})$.

$P(\text{at least once}) = 1 - q^3$

$P(\text{at least once}) = 1 - (0.6)^3$

$P(\text{at least once}) = 1 - 0.216 = 0.784$

Answer: 0.784

</details>

---

### Q30. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a person is not a sportsperson is $\frac{1}{6}$. Then the probability that out of the 6 members of the family, 5 are sportspersons is

**Options:**

- **(A)** $\left(\frac{5}{6}\right)^5$
- **(B)** $6\left(\frac{5}{6}\right)^5$
- **(C)** $5\left(\frac{5}{6}\right)^6$
- **(D)** $\left(\frac{5}{6}\right)^6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{5}{6}\right)^5$**

**Detailed Solution:**

Let $p$ be the probability that a person is a sportsperson and $q$ be the probability that a person is not a sportsperson.

Given $q = \dfrac{1}{6}$

$p = 1 - q = 1 - \dfrac{1}{6} = \dfrac{5}{6}$

Number of members in the family, $n = 6$

We need to find the probability that exactly 5 are sportspersons, so $r = 5$.

Using binomial distribution, $P(X = r) = ^{n}C_{r} p^r q^{n-r}$

$P(X = 5) = ^{6}C_{5} \left(\dfrac{5}{6}\right)^5 \left(\dfrac{1}{6}\right)^1$

$P(X = 5) = 6 \times \left(\dfrac{5}{6}\right)^5 \times \dfrac{1}{6}$

$P(X = 5) = \left(\dfrac{5}{6}\right)^5$

Answer: $\left(\frac{5}{6}\right)^5$

</details>

---

### Q31. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a student is not a swimmer is $\frac{1}{5}$. The probability that out of 5 students selected at random 4 are swimmers is

**Options:**

- **(A)** $\left(\frac{4}{5}\right)^4$
- **(B)** $\left(\frac{4}{5}\right)^4\left(\frac{1}{5}\right)$
- **(C)** $\left(\frac{4}{5}\right)^5 \times \frac{1}{5}$
- **(D)** $\left(\frac{4}{5}\right)^3 \times \frac{1}{5^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\left(\frac{4}{5}\right)^4$**

**Detailed Solution:**

Let $p$ be the probability that a student is a swimmer and $q$ be the probability that a student is not a swimmer.

Given $q = \dfrac{1}{5}$, so $p = 1 - q = 1 - \dfrac{1}{5} = \dfrac{4}{5}$.

The number of students selected is $n = 5$.

The probability that exactly $4$ students are swimmers is given by the binomial distribution:

$P(X = 4) = ^{5}C_{4} p^4 q^{5-4}$

$P(X = 4) = 5 \times \left(\dfrac{4}{5}\right)^4 \times \left(\dfrac{1}{5}\right)$

$P(X = 4) = \left(\dfrac{4}{5}\right)^4$

Answer: $\left(\frac{4}{5}\right)^4$

</details>

---

### Q32. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A pair of fair dice is thrown 4 times. If getting the same number on both dice is considered as a success, then the probability of two successes are

**Options:**

- **(A)** $\frac{25}{216}$
- **(B)** $\frac{25}{36}$
- **(C)** $\frac{25}{108}$
- **(D)** $\frac{25}{104}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{25}{216}$**

**Detailed Solution:**

Let $p$ be the probability of getting the same number on both dice (a doublet) in a single throw.

The possible doublets are $(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)$.

$p = \dfrac{6}{36} = \dfrac{1}{6}$

The probability of failure is $q = 1 - p = 1 - \dfrac{1}{6} = \dfrac{5}{6}$.

The number of trials is $n = 4$.

The probability of getting exactly $r = 2$ successes is given by the binomial distribution formula:

$P(X = 2) = ^{4}C_{2} p^2 q^2$

$P(X = 2) = 6 \times \left(\dfrac{1}{6}\right)^2 \times \left(\dfrac{5}{6}\right)^2$

$P(X = 2) = 6 \times \dfrac{1}{36} \times \dfrac{25}{36}$

$P(X = 2) = \dfrac{25}{216}$

Answer: $\frac{25}{216}$

</details>

---

### Q33. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $x \sim B\left(6, \frac{1}{2}\right)$, then $p(|x-2| \leqslant 1)=$

**Options:**

- **(A)** $\frac{31}{32}$
- **(B)** $\frac{41}{64}$
- **(C)** $\frac{51}{64}$
- **(D)** $\frac{63}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{41}{64}$**

**Detailed Solution:**

Given $x \sim B\left(6, \dfrac{1}{2}\right)$, we have $n = 6$, $p = \dfrac{1}{2}$, and $q = 1 - p = \dfrac{1}{2}$.

The probability mass function is $P(X = x) = ^{n}C_{x} p^x q^{n-x} = ^{6}C_{x} \left(\dfrac{1}{2}\right)^6 = \dfrac{^{6}C_{x}}{64}$.

The given condition is $|x - 2| \leqslant 1$.

$-1 \leqslant x - 2 \leqslant 1$

$1 \leqslant x \leqslant 3$

Since $x$ takes integer values, $x$ can be $1, 2,$ or $3$.

$P(|x - 2| \leqslant 1) = P(x = 1) + P(x = 2) + P(x = 3)$

$P(x = 1) = \dfrac{^{6}C_{1}}{64} = \dfrac{6}{64}$

$P(x = 2) = \dfrac{^{6}C_{2}}{64} = \dfrac{15}{64}$

$P(x = 3) = \dfrac{^{6}C_{3}}{64} = \dfrac{20}{64}$

$P(|x - 2| \leqslant 1) = \dfrac{6 + 15 + 20}{64} = \dfrac{41}{64}$

Answer: $\frac{41}{64}$

</details>

---

### Q34. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed 100 times. The chance of getting a head even number of times is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{3}{8}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Let $X$ be the number of heads obtained when a fair coin is tossed $100$ times.

$X$ follows a binomial distribution with $n = 100$, $p = \dfrac{1}{2}$, and $q = \dfrac{1}{2}$.

The probability of getting exactly $r$ heads is given by $P(X = r) = ^{100}C_{r} \left(\dfrac{1}{2}\right)^{100}$.

The probability of getting an even number of heads is:

$P(X = 0) + P(X = 2) + P(X = 4) + \dots + P(X = 100)$

$= \left( ^{100}C_{0} + ^{100}C_{2} + ^{100}C_{4} + \dots + ^{100}C_{100} \right) \left(\dfrac{1}{2}\right)^{100}$

We know that the sum of binomial coefficients for even terms is $2^{n-1}$.

Therefore, $^{100}C_{0} + ^{100}C_{2} + ^{100}C_{4} + \dots + ^{100}C_{100} = 2^{99}$.

The required probability is $2^{99} \times \left(\dfrac{1}{2}\right)^{100} = \dfrac{2^{99}}{2^{100}} = \dfrac{1}{2}$.

Answer: $\frac{1}{2}$

</details>

---

### Q35. MHT CET 2025 (22 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a certain kind of component will survive a given test is $\frac{2}{3}$. The probability that at most 2 components out of 4 tested, will survive is

**Options:**

- **(A)** $\frac{31}{3^4}$
- **(B)** $\frac{32}{3^4}$
- **(C)** $\frac{33}{3^4}$
- **(D)** $\frac{35}{3^4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{33}{3^4}$**

**Detailed Solution:**

Let $X$ be the number of components that survive. $X$ follows a binomial distribution with $n = 4$ and probability of survival $p = \dfrac{2}{3}$.

The probability of failure is $q = 1 - p = \dfrac{1}{3}$.

The probability that at most 2 components survive is $P(X \le 2)$.

$P(X \le 2) = 1 - P(X > 2) = 1 - [P(X = 3) + P(X = 4)]$

Using the binomial probability formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X = 3) = ^{4}C_{3} \left(\dfrac{2}{3}\right)^3 \left(\dfrac{1}{3}\right)^1 = 4 \times \dfrac{8}{27} \times \dfrac{1}{3} = \dfrac{32}{81}$

$P(X = 4) = ^{4}C_{4} \left(\dfrac{2}{3}\right)^4 \left(\dfrac{1}{3}\right)^0 = 1 \times \dfrac{16}{81} \times 1 = \dfrac{16}{81}$

$P(X \le 2) = 1 - \left(\dfrac{32}{81} + \dfrac{16}{81}\right)$

$P(X \le 2) = 1 - \dfrac{48}{81} = \dfrac{33}{81}$

$P(X \le 2) = \dfrac{33}{3^4}$

Answer: $\frac{33}{3^4}$

</details>

---

### Q36. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Numbers are selected at random, one at a time from the two-digit numbers $00,01,02$, -------, 99 with replacement. An event E occurs only if the product of the two digits of a selected number is 24 . If four numbers are selected, then probability, that the event E occurs at least 3 times, is

**Options:**

- **(A)** $\frac{24}{(25)^4}$
- **(B)** $\frac{4}{(25)^4}$
- **(C)** $\frac{97}{(25)^4}$
- **(D)** $\frac{96}{(25)^4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{97}{(25)^4}$**

**Detailed Solution:**

The sample space consists of two-digit numbers from $00$ to $99$. Total number of possible outcomes is $100$.

Event E occurs if the product of the two digits of a selected number is $24$. The pairs of digits whose product is $24$ are $(3, 8)$, $(8, 3)$, $(4, 6)$, and $(6, 4)$.

The numbers corresponding to these pairs are $38, 83, 46, 64$.

Number of favorable outcomes for event E is $4$.

Probability of event E occurring in a single selection is $p = \dfrac{4}{100} = \dfrac{1}{25}$.

Probability of event E not occurring is $q = 1 - p = 1 - \dfrac{1}{25} = \dfrac{24}{25}$.

Four numbers are selected, so the number of trials is $n = 4$. Let $X$ be the number of times event E occurs. $X$ follows a binomial distribution.

The probability that event E occurs at least 3 times is $P(X \ge 3) = P(X = 3) + P(X = 4)$.

Using the binomial probability formula $P(X = r) = ^{n}C_{r} p^{r} q^{n-r}$:

$P(X = 3) = ^{4}C_{3} \left(\dfrac{1}{25}\right)^3 \left(\dfrac{24}{25}\right)^1 = 4 \times \dfrac{1}{25^3} \times \dfrac{24}{25} = \dfrac{96}{25^4}$

$P(X = 4) = ^{4}C_{4} \left(\dfrac{1}{25}\right)^4 \left(\dfrac{24}{25}\right)^0 = 1 \times \dfrac{1}{25^4} \times 1 = \dfrac{1}{25^4}$

$P(X \ge 3) = \dfrac{96}{25^4} + \dfrac{1}{25^4} = \dfrac{97}{(25)^4}$

Answer: $\frac{97}{(25)^4}$

</details>

---

### Q37. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $X$ follows the Binomial distribution $B(10, p)$ such that $5 P(X=0)=P(X=1)$, then the value of $\frac{P(X=5)}{P(X=6)}$ is equal to

**Options:**

- **(A)** $\frac{6}{5}$
- **(B)** $\frac{12}{5}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{12}{5}$**

**Detailed Solution:**

For a Binomial distribution $B(n, p)$, the probability of $x$ successes is given by $P(X=x) = ^{n}C_{x} p^x q^{n-x}$, where $q = 1 - p$.

Given $n = 10$ and $5 P(X=0) = P(X=1)$.

Substituting the formula, we get:

$5 \times ^{10}C_{0} p^0 q^{10} = ^{10}C_{1} p^1 q^9$

$5 q^{10} = 10 p q^9$

Dividing both sides by $5 q^9$, we get:

$q = 2p$

Since $p + q = 1$, we have:

$p + 2p = 1 \Rightarrow 3p = 1 \Rightarrow p = \dfrac{1}{3}$

Thus, $q = \dfrac{2}{3}$.

We need to find the value of $\dfrac{P(X=5)}{P(X=6)}$:

$\dfrac{P(X=5)}{P(X=6)} = \dfrac{^{10}C_{5} p^5 q^5}{^{10}C_{6} p^6 q^4}$

$\dfrac{P(X=5)}{P(X=6)} = \dfrac{^{10}C_{5}}{^{10}C_{6}} \times \dfrac{q}{p}$

$\dfrac{P(X=5)}{P(X=6)} = \dfrac{\dfrac{10!}{5!5!}}{\dfrac{10!}{6!4!}} \times \dfrac{\dfrac{2}{3}}{\dfrac{1}{3}}$

$\dfrac{P(X=5)}{P(X=6)} = \dfrac{6!4!}{5!5!} \times 2$

$\dfrac{P(X=5)}{P(X=6)} = \dfrac{6}{5} \times 2 = \dfrac{12}{5}$

Answer: $\frac{12}{5}$

</details>

---

### Q38. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed 99 times. If X is the number of times head occur then $\mathrm{P}[\mathrm{X}=\mathrm{r}]$ is maximum when $\mathrm{r}=$

**Options:**

- **(A)** $48$
- **(B)** $49$
- **(C)** $51$
- **(D)** $52$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $49$**

**Detailed Solution:**

The random variable $X$ follows a binomial distribution with $n = 99$ and $p = \dfrac{1}{2}$.

The probability of getting $r$ heads is given by $P[X=r] = ^{99}C_{r} \left(\dfrac{1}{2}\right)^{r} \left(\dfrac{1}{2}\right)^{99-r} = ^{99}C_{r} \left(\dfrac{1}{2}\right)^{99}$.

$P[X=r]$ is maximum when the binomial coefficient $^{99}C_{r}$ is maximum.

For an odd integer $n$, the binomial coefficient $^{n}C_{r}$ is maximum when $r = \dfrac{n-1}{2}$ or $r = \dfrac{n+1}{2}$.

Substituting $n = 99$, we get $r = \dfrac{99-1}{2} = 49$ or $r = \dfrac{99+1}{2} = 50$.

Among the given options, $r = 49$ is present.

Answer: $49$

</details>

---

### Q39. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If X is a binomial variable with range $\{0,1,2,3,4\}$ and $P(X=3)=3 P(X=4)$ then the parameter ' $p$ ' of the binomial distribution is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{3}{4}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{4}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{7}$**

**Detailed Solution:**

The range of the binomial variable $X$ is $\{0, 1, 2, 3, 4\}$, which implies $n = 4$.

The probability mass function of a binomial distribution is $P(X=x) = ^{n}C_{x} p^x q^{n-x}$, where $q = 1 - p$.

Given $P(X=3) = 3 P(X=4)$.

Substituting the values, we get:

$^{4}C_{3} p^3 q^1 = 3 \times ^{4}C_{4} p^4 q^0$

$4 p^3 q = 3 p^4$

Since $p \neq 0$, dividing both sides by $p^3$ gives:

$4 q = 3 p$

Substituting $q = 1 - p$:

$4(1 - p) = 3 p$

$4 - 4p = 3p$

$7p = 4$

$p = \dfrac{4}{7}$

Answer: $\frac{4}{7}$

</details>

---

### Q40. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\quad X \sim B(n, p)$ then $\frac{P(X=k)}{P(X=k-1)}=$

**Options:**

- **(A)** $\frac{\mathrm{n}-\mathrm{k}}{\mathrm{k}-1} \cdot \frac{\mathrm{p}}{\mathrm{q}}$
- **(B)** $\frac{\mathrm{n}-\mathrm{k}+1}{\mathrm{k}+1} \cdot \frac{\mathrm{p}}{\mathrm{q}}$
- **(C)** $\frac{\mathrm{n}+1}{\mathrm{k}} \cdot \frac{\mathrm{q}}{\mathrm{p}}$
- **(D)** $\frac{\mathrm{n}-\mathrm{k}+1}{\mathrm{k}} \cdot \frac{\mathrm{p}}{\mathrm{q}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{n}-\mathrm{k}+1}{\mathrm{k}} \cdot \frac{\mathrm{p}}{\mathrm{q}}$**

**Detailed Solution:**

For a binomial distribution $X \sim B(n, p)$, the probability mass function is given by:

$P(X=k) = ^{n}C_{k} p^k q^{n-k}$

Similarly, for $X = k-1$:

$P(X=k-1) = ^{n}C_{k-1} p^{k-1} q^{n-k+1}$

Taking the ratio of the two probabilities:

$\dfrac{P(X=k)}{P(X=k-1)} = \dfrac{^{n}C_{k} p^k q^{n-k}}{^{n}C_{k-1} p^{k-1} q^{n-k+1}}$

$\dfrac{P(X=k)}{P(X=k-1)} = \dfrac{^{n}C_{k}}{^{n}C_{k-1}} \cdot \dfrac{p}{q}$

Expanding the combination terms:

$\dfrac{^{n}C_{k}}{^{n}C_{k-1}} = \dfrac{\dfrac{n!}{k!(n-k)!}}{\dfrac{n!}{(k-1)!(n-k+1)!}}$

$\dfrac{^{n}C_{k}}{^{n}C_{k-1}} = \dfrac{(k-1)!(n-k+1)!}{k!(n-k)!}$

$\dfrac{^{n}C_{k}}{^{n}C_{k-1}} = \dfrac{n-k+1}{k}$

Substituting this back into the ratio:

$\dfrac{P(X=k)}{P(X=k-1)} = \dfrac{n-k+1}{k} \cdot \dfrac{p}{q}$

Answer: $\frac{\mathrm{n}-\mathrm{k}+1}{\mathrm{k}} \cdot \frac{\mathrm{p}}{\mathrm{q}}$

</details>

---

### Q41. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

One hundred identical coins, each with probability p , of showing up heads are tossed once. If $0 \lt \mathrm{p} \lt 1$ and the probability of heads showing on 50 coins is equal to that of heads showing on 51 coins, then the value of $p$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{49}{101}$
- **(C)** $\frac{50}{101}$
- **(D)** $\frac{51}{101}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{51}{101}$**

**Detailed Solution:**

Let $X$ be the number of heads obtained when 100 coins are tossed. Then $X$ follows a binomial distribution with parameters $n = 100$ and probability of success $p$.

The probability of getting exactly $k$ heads is given by $P(X = k) = ^{100}C_{k} p^k (1-p)^{100-k}$.

Given that the probability of 50 heads is equal to the probability of 51 heads:

$P(X = 50) = P(X = 51)$

$^{100}C_{50} p^{50} (1-p)^{50} = ^{100}C_{51} p^{51} (1-p)^{49}$

Dividing both sides by $p^{50} (1-p)^{49}$:

$^{100}C_{50} (1-p) = ^{100}C_{51} p$

Expanding the combinations:

$\dfrac{100!}{50! 50!} (1-p) = \dfrac{100!}{51! 49!} p$

$\dfrac{1-p}{50} = \dfrac{p}{51}$

Cross-multiplying yields:

$51(1-p) = 50p$

$51 - 51p = 50p$

$101p = 51$

$p = \dfrac{51}{101}$

Answer: $\frac{51}{101}$

</details>

---

### Q42. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability that a person who undergoes a bypass surgery will recover is 0.6 . the probability that of the six patients who undergo similar operations, half of them will recover is

**Options:**

- **(A)** 0.2762
- **(B)** 0.1852
- **(C)** 0.2074
- **(D)** 0.7235

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0.2762**

**Detailed Solution:**

Let $X$ be the number of patients who recover from the bypass surgery.

The probability of recovery for a single patient is $p = 0.6$.

The probability of not recovering is $q = 1 - p = 1 - 0.6 = 0.4$.

The total number of patients is $n = 6$.

We need to find the probability that exactly half of them recover, which means $r = 3$.

Using the binomial probability formula:

$P(X = r) = ^{n}C_{r} p^r q^{n-r}$

Substitute the given values:

$P(X = 3) = ^{6}C_{3} (0.6)^3 (0.4)^3$

$P(X = 3) = \dfrac{6 \times 5 \times 4}{3 \times 2 \times 1} \times 0.216 \times 0.064$

$P(X = 3) = 20 \times 0.013824$

$P(X = 3) = 0.27648$

The calculated probability is $0.27648$, which is closest to the given option $0.2762$ (likely a typographical error in the options).

Answer: 0.2762

</details>

---

### Q43. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Minimum number of times a fair coin must be tossed, so that the probability of getting at least one head, is more than $99 \%$ is

**Options:**

- **(A)** 5
- **(B)** 6
- **(C)** 7
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

Let the coin be tossed $n$ times.

Probability of getting at least one head is $1 - P(\text{no head})$.

$P(\text{at least one head}) = 1 - \left(\dfrac{1}{2}\right)^n$

Given that this probability is more than $99\%$, we have:

$1 - \left(\dfrac{1}{2}\right)^n > \dfrac{99}{100}$

$\left(\dfrac{1}{2}\right)^n < 1 - \dfrac{99}{100}$

$\dfrac{1}{2^n} < \dfrac{1}{100}$

$2^n > 100$

Since $2^6 = 64$ and $2^7 = 128$, the minimum integer value of $n$ satisfying the inequality is $7$.

Answer: 7

</details>

---

### Q44. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a Binomial distribution consisting of 5 independent trials, probabilities of exactly 1 and 2 successes are 0.4096 and 0.2048 respectively, then the probability, of getting exactly 4 successes, is

**Options:**

- **(A)** $\dfrac{80}{243}$
- **(B)** $\dfrac{40}{243}$
- **(C)** $\dfrac{32}{625}$
- **(D)** $\dfrac{4}{625}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{4}{625}$**

**Detailed Solution:**

Let $p$ be the probability of success and $q$ be the probability of failure in a single trial. Given the number of trials $n = 5$.

The probability of exactly $x$ successes is given by $P(X = x) = ^{n}C_{x} p^x q^{n-x}$.

Given $P(X = 1) = 0.4096$ and $P(X = 2) = 0.2048$.

$P(X = 1) = ^{5}C_{1} p^1 q^4 = 5 p q^4 = 0.4096$

$P(X = 2) = ^{5}C_{2} p^2 q^3 = 10 p^2 q^3 = 0.2048$

Dividing the first equation by the second equation:

$\dfrac{5 p q^4}{10 p^2 q^3} = \dfrac{0.4096}{0.2048}$

$\dfrac{q}{2p} = 2 \Rightarrow q = 4p$

Since $p + q = 1$, substituting $q = 4p$ gives:

$p + 4p = 1 \Rightarrow 5p = 1 \Rightarrow p = \dfrac{1}{5}$

Therefore, $q = \dfrac{4}{5}$.

The probability of getting exactly 4 successes is:

$P(X = 4) = ^{5}C_{4} p^4 q^1 = 5 \left(\dfrac{1}{5}\right)^4 \left(\dfrac{4}{5}\right) = 5 \times \dfrac{1}{625} \times \dfrac{4}{5} = \dfrac{4}{625}$

Answer: $\dfrac{4}{625}$

</details>

---

### Q45. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and the variance of a Binomial variate $X$ are 2 and 1 respectively, then the probability that $X$ takes a value greater than one is equal to

**Options:**

- **(A)** $\dfrac{5}{16}$
- **(B)** $\dfrac{11}{16}$
- **(C)** $\dfrac{12}{16}$
- **(D)** $\dfrac{15}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{11}{16}$**

**Detailed Solution:**

Mean of the Binomial variate $X$ is $np = 2$

Variance of $X$ is $npq = 1$

Dividing variance by mean, we get $q = \dfrac{1}{2}$

Since $p + q = 1$, $p = \dfrac{1}{2}$

Substituting $p$ in $np = 2$, we get $n = 4$

The probability that $X$ takes a value greater than one is $P(X > 1) = 1 - P(X \le 1)$

$P(X \le 1) = P(X = 0) + P(X = 1)$

$P(X = 0) = ^{4}C_{0} \left(\dfrac{1}{2}\right)^{4} = \dfrac{1}{16}$

$P(X = 1) = ^{4}C_{1} \left(\dfrac{1}{2}\right)^{4} = \dfrac{4}{16}$

$P(X > 1) = 1 - \left(\dfrac{1}{16} + \dfrac{4}{16}\right) = 1 - \dfrac{5}{16} = \dfrac{11}{16}$

Answer: $\dfrac{11}{16}$

</details>

---

### Q46. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the mean and the variance of Binomial variate $X$ are 2 and 1 respectively, then the probability that X takes a value greater than or equal to one is

**Options:**

- **(A)** $\dfrac{1}{16}$
- **(B)** $\dfrac{9}{16}$
- **(C)** $\dfrac{3}{4}$
- **(D)** $\dfrac{15}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{15}{16}$**

**Detailed Solution:**

Let the binomial distribution have parameters $n$ and $p$.

Given mean $= np = 2$ and variance $= npq = 1$.

Dividing variance by mean, we get $q = \dfrac{npq}{np} = \dfrac{1}{2}$.

Since $p + q = 1$, we have $p = 1 - \dfrac{1}{2} = \dfrac{1}{2}$.

Substituting $p$ in the mean equation, $n \left(\dfrac{1}{2}\right) = 2 \Rightarrow n = 4$.

The probability that $X$ takes a value greater than or equal to one is $P(X \ge 1) = 1 - P(X = 0)$.

$P(X = 0) = ^{4}C_{0} p^{0} q^{4} = \left(\dfrac{1}{2}\right)^{4} = \dfrac{1}{16}$.

Therefore, $P(X \ge 1) = 1 - \dfrac{1}{16} = \dfrac{15}{16}$.

Answer: $\dfrac{15}{16}$

</details>

---

### Q47. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For an entry to a certain course, a candidate is given twenty problems to solve. If the probability that the candidate can solve any problem is $\dfrac{3}{7}$, then the probability that he can solve at most two problems is

**Options:**

- **(A)** $\dfrac{256}{49}\left(\dfrac{4}{7}\right)^{18}$
- **(B)** $\dfrac{1966}{49}\left(\dfrac{4}{7}\right)^{18}$
- **(C)** $\dfrac{1710}{49}\left(\dfrac{4}{7}\right)^{18}$
- **(D)** $\dfrac{1726}{49}\left(\dfrac{4}{7}\right)^{18}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{1966}{49}\left(\dfrac{4}{7}\right)^{18}$**

**Detailed Solution:**

Let $p$ be the probability of solving a problem, so $p = \dfrac{3}{7}$.

Let $q$ be the probability of not solving a problem, so $q = 1 - p = \dfrac{4}{7}$.

The total number of problems is $n = 20$.

The probability of solving at most two problems is given by $P(X \le 2) = P(X = 0) + P(X = 1) + P(X = 2)$.

Using the binomial distribution formula $P(X = r) = ^{n}C_{r} p^r q^{n-r}$:

$P(X = 0) = ^{20}C_{0} \left(\dfrac{3}{7}\right)^0 \left(\dfrac{4}{7}\right)^{20} = \left(\dfrac{4}{7}\right)^{20}$

$P(X = 1) = ^{20}C_{1} \left(\dfrac{3}{7}\right)^1 \left(\dfrac{4}{7}\right)^{19} = 20 \left(\dfrac{3}{7}\right) \left(\dfrac{4}{7}\right)^{19}$

$P(X = 2) = ^{20}C_{2} \left(\dfrac{3}{7}\right)^2 \left(\dfrac{4}{7}\right)^{18} = 190 \left(\dfrac{9}{49}\right) \left(\dfrac{4}{7}\right)^{18}$

Adding these probabilities together:

$P(X \le 2) = \left(\dfrac{4}{7}\right)^{18} \left[ \left(\dfrac{4}{7}\right)^2 + 20 \left(\dfrac{3}{7}\right) \left(\dfrac{4}{7}\right) + 190 \left(\dfrac{9}{49}\right) \right]$

$P(X \le 2) = \left(\dfrac{4}{7}\right)^{18} \left[ \dfrac{16}{49} + \dfrac{240}{49} + \dfrac{1710}{49} \right]$

$P(X \le 2) = \dfrac{1966}{49} \left(\dfrac{4}{7}\right)^{18}$

Answer: $\dfrac{1966}{49}\left(\dfrac{4}{7}\right)^{18}$

</details>

---

### Q48. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A multiple choice examination has 5 questions. Each question has three alternative answers of which exactly one is correct. The probability, that a student will get 4 or more correct answers just by guessing, is

**Options:**

- **(A)** $\dfrac{10}{3^5}$
- **(B)** $\dfrac{17}{3^5}$
- **(C)** $\dfrac{13}{3^5}$
- **(D)** $\dfrac{11}{3^5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{11}{3^5}$**

**Detailed Solution:**

Let $p$ be the probability of guessing a correct answer and $q$ be the probability of guessing an incorrect answer.

$p = \dfrac{1}{3}$ and $q = \dfrac{2}{3}$

Let $X$ be the number of correct answers. The probability of getting $r$ correct answers out of $n$ questions is given by the binomial distribution:

$P(X = r) = ^{n}C_{r} p^{r} q^{n-r}$

The probability of getting 4 or more correct answers is $P(X \ge 4) = P(X = 4) + P(X = 5)$.

$P(X = 4) = ^{5}C_{4} \left(\dfrac{1}{3}\right)^{4} \left(\dfrac{2}{3}\right)^{1} = 5 \times \dfrac{1}{81} \times \dfrac{2}{3} = \dfrac{10}{3^5}$

$P(X = 5) = ^{5}C_{5} \left(\dfrac{1}{3}\right)^{5} \left(\dfrac{2}{3}\right)^{0} = 1 \times \dfrac{1}{243} \times 1 = \dfrac{1}{3^5}$

$P(X \ge 4) = \dfrac{10}{3^5} + \dfrac{1}{3^5} = \dfrac{11}{3^5}$

Answer: $\dfrac{11}{3^5}$

</details>

---

### Q49. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has the following. -probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/KfxKu8a1O8MkYXV6pcV1CtAvTqkATcQUTfVZeXf7PdY.original.fullsize.png"/>
Then $\mathrm{P}(\mathrm{X}\gt2)$ is equal to

**Options:**

- **(A)** $\dfrac{7}{12}$
- **(B)** $\dfrac{23}{36}$
- **(C)** $\dfrac{1}{36}$
- **(D)** $\dfrac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{23}{36}$**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities must be equal to $1$.

$\sum P(X) = 1$

$k^2 + 2k + k + 2k + 5k^2 = 1$

$6k^2 + 5k - 1 = 0$

$(6k - 1)(k + 1) = 0$

This gives $k = \dfrac{1}{6}$ or $k = -1$.

Since probability cannot be negative, $k$ must be greater than $0$. Therefore, $k = \dfrac{1}{6}$.

We need to find $P(X > 2)$:

$P(X > 2) = P(X = 3) + P(X = 4) + P(X = 5)$

$P(X > 2) = k + 2k + 5k^2$

$P(X > 2) = 3k + 5k^2$

Substituting $k = \dfrac{1}{6}$:

$P(X > 2) = 3\left(\dfrac{1}{6}\right) + 5\left(\dfrac{1}{6}\right)^2$

$P(X > 2) = \dfrac{3}{6} + \dfrac{5}{36}$

$P(X > 2) = \dfrac{18}{36} + \dfrac{5}{36} = \dfrac{23}{36}$

Answer: $\dfrac{23}{36}$

</details>

---

### Q50. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn' successively with replacement from a well shuffled pack of 52 cards. Then mean of number of kings is

**Options:**

- **(A)** $\dfrac{1}{13}$
- **(B)** $\dfrac{1}{169}$
- **(C)** $\dfrac{2}{13}$
- **(D)** $\dfrac{4}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{2}{13}$**

**Detailed Solution:**

Let $X$ be the random variable denoting the number of kings drawn.

Since the cards are drawn with replacement, the draws are independent and $X$ follows a binomial distribution.

The probability of drawing a king in a single draw is $p = \dfrac{4}{52} = \dfrac{1}{13}$.

The number of trials is $n = 2$.

The mean of a binomial distribution is given by $E(X) = np$.

Substituting the values, we get $E(X) = 2 \times \dfrac{1}{13} = \dfrac{2}{13}$.

Answer: $\dfrac{2}{13}$

</details>

---

### Q51. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Two cards are drawn successively with replacement from a well- shuffled pack of 52. cards. Let X denote the random variable of number of kings obtained in the two drawn cards. Then $\mathrm{P}(x=1)+\mathrm{P}(x=2)$ equals

**Options:**

- **(A)** $\dfrac{49}{169}$
- **(B)** $\dfrac{24}{169}$
- **(C)** $\dfrac{52}{169}$
- **(D)** $\dfrac{25}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{25}{169}$**

**Detailed Solution:**

Probability of drawing a king in a single draw, $p = \dfrac{4}{52} = \dfrac{1}{13}$

Probability of not drawing a king, $q = 1 - p = \dfrac{12}{13}$

Since the cards are drawn with replacement, the number of kings $X$ follows a binomial distribution with $n=2$.

We need to find $P(X=1) + P(X=2)$.

$P(X=1) = ^{2}C_{1} p^{1} q^{1} = 2 \times \dfrac{1}{13} \times \dfrac{12}{13} = \dfrac{24}{169}$

$P(X=2) = ^{2}C_{2} p^{2} q^{0} = 1 \times \left(\dfrac{1}{13}\right)^{2} = \dfrac{1}{169}$

$P(X=1) + P(X=2) = \dfrac{24}{169} + \dfrac{1}{169} = \dfrac{25}{169}$

Alternatively, $P(X=1) + P(X=2) = 1 - P(X=0) = 1 - ^{2}C_{0} q^{2} = 1 - \left(\dfrac{12}{13}\right)^{2} = 1 - \dfrac{144}{169} = \dfrac{25}{169}$

Answer: $\dfrac{25}{169}$

</details>

---

### Q52. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a random variable X have a Binomial distribution with mean 8 and variance 4 . If $\mathrm{P}(x \leqslant 2)=\dfrac{\mathrm{k}}{2^{16}}$, then k is equal to

**Options:**

- **(A)** 17
- **(B)** 121
- **(C)** 1
- **(D)** 137

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 137**

**Detailed Solution:**

For a binomial distribution, mean is given by $np$ and variance is given by $npq$.

Given $np = 8$ and $npq = 4$.

Dividing the variance by the mean, we get:

$q = \dfrac{npq}{np} = \dfrac{4}{8} = \dfrac{1}{2}$

Since $p + q = 1$, we have $p = 1 - \dfrac{1}{2} = \dfrac{1}{2}$.

Substituting $p = \dfrac{1}{2}$ into $np = 8$:

$n \left(\dfrac{1}{2}\right) = 8 \Rightarrow n = 16$

The probability $P(X \leqslant 2)$ is given by:

$P(X \leqslant 2) = P(X = 0) + P(X = 1) + P(X = 2)$

$P(X \leqslant 2) = ^{16}C_{0} \left(\dfrac{1}{2}\right)^{16} + ^{16}C_{1} \left(\dfrac{1}{2}\right)^{16} + ^{16}C_{2} \left(\dfrac{1}{2}\right)^{16}$

$P(X \leqslant 2) = \left(1 + 16 + \dfrac{16 \times 15}{2}\right) \dfrac{1}{2^{16}}$

$P(X \leqslant 2) = (1 + 16 + 120) \dfrac{1}{2^{16}} = \dfrac{137}{2^{16}}$

Comparing this with $\dfrac{k}{2^{16}}$, we get $k = 137$.

Answer: 137

</details>

---

### Q53. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{X} \sim \mathrm{B}\left(6, \dfrac{1}{2}\right)$, then $\mathrm{P}[|x-4| \leqslant 2]$ is

**Options:**

- **(A)** $\dfrac{115}{128}$
- **(B)** $\dfrac{63}{64}$
- **(C)** $\dfrac{57}{64}$
- **(D)** $\dfrac{7}{64}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{57}{64}$**

**Detailed Solution:**

Given $X \sim B\left(6, \dfrac{1}{2}\right)$, the probability mass function is $P(X = x) = ^{6}C_{x} \left(\dfrac{1}{2}\right)^{x} \left(\dfrac{1}{2}\right)^{6-x} = ^{6}C_{x} \left(\dfrac{1}{2}\right)^{6}$.

We need to find $P(|X - 4| \leqslant 2)$.

$|X - 4| \leqslant 2 \Rightarrow -2 \leqslant X - 4 \leqslant 2 \Rightarrow 2 \leqslant X \leqslant 6$.

Since the maximum value of $X$ is $6$, we can calculate this as:

$P(2 \leqslant X \leqslant 6) = 1 - P(X < 2) = 1 - [P(X = 0) + P(X = 1)]$.

$P(X = 0) = ^{6}C_{0} \left(\dfrac{1}{2}\right)^{6} = \dfrac{1}{64}$.

$P(X = 1) = ^{6}C_{1} \left(\dfrac{1}{2}\right)^{6} = \dfrac{6}{64}$.

$P(2 \leqslant X \leqslant 6) = 1 - \left(\dfrac{1}{64} + \dfrac{6}{64}\right) = 1 - \dfrac{7}{64} = \dfrac{57}{64}$.

Answer: $\dfrac{57}{64}$

</details>

---

### Q54. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let in a Binomial distribution, consisting of 5 independent trials, probabilities of exactly 1 and 2 successes be 0.4096 and 0.2048 respectively. Then the probability of getting exactly 3 successes is equal to

**Options:**

- **(A)** $\dfrac{80}{243}$
- **(B)** $\dfrac{40}{243}$
- **(C)** $\dfrac{32}{625}$
- **(D)** $\dfrac{128}{625}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{32}{625}$**

**Detailed Solution:**

Let the probability of success be $p$ and failure be $q = 1 - p$.

Given $n = 5$, $P(X = 1) = 0.4096$ and $P(X = 2) = 0.2048$.

$P(X = 1) = ^{5}C_{1} p q^4 = 5 p q^4 = 0.4096$

$P(X = 2) = ^{5}C_{2} p^2 q^3 = 10 p^2 q^3 = 0.2048$

Dividing the two equations, we get:

$\dfrac{5 p q^4}{10 p^2 q^3} = \dfrac{0.4096}{0.2048}$

$\dfrac{q}{2p} = 2 \Rightarrow q = 4p$

Since $p + q = 1$, we have $p + 4p = 1 \Rightarrow p = \dfrac{1}{5}$ and $q = \dfrac{4}{5}$.

The probability of getting exactly 3 successes is:

$P(X = 3) = ^{5}C_{3} p^3 q^2$

$P(X = 3) = 10 \times \left(\dfrac{1}{5}\right)^3 \times \left(\dfrac{4}{5}\right)^2$

$P(X = 3) = 10 \times \dfrac{1}{125} \times \dfrac{16}{25} = \dfrac{160}{3125} = \dfrac{32}{625}$

Answer: $\dfrac{32}{625}$

</details>

---

### Q55. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Ten bulbs are drawn successively, with replacement, from a lot containing $10 \%$ defective bulbs, then the probability that there is at least one defective bulb, is

**Options:**

- **(A)** $1-\left(\dfrac{1}{10}\right)^{10}$
- **(B)** $\quad 1-\left(\dfrac{3}{10}\right)^{10}$
- **(C)** $1-\left(\dfrac{9}{10}\right)^{10}$
- **(D)** $1-\left(\dfrac{7}{10}\right)^{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1-\left(\dfrac{9}{10}\right)^{10}$**

**Detailed Solution:**

Let $p$ be the probability of drawing a defective bulb.

$p = \dfrac{10}{100} = \dfrac{1}{10}$

Let $q$ be the probability of drawing a non-defective bulb.

$q = 1 - p = 1 - \dfrac{1}{10} = \dfrac{9}{10}$

The number of trials is $n = 10$.

Let $X$ be the random variable representing the number of defective bulbs drawn. Since the bulbs are drawn with replacement, $X$ follows a binomial distribution.

The probability of getting at least one defective bulb is $P(X \ge 1)$.

$P(X \ge 1) = 1 - P(X = 0)$

$P(X = 0) = ^{10}C_{0} p^0 q^{10} = \left(\dfrac{9}{10}\right)^{10}$

$P(X \ge 1) = 1 - \left(\dfrac{9}{10}\right)^{10}$

Answer: $1-\left(\dfrac{9}{10}\right)^{10}$

</details>

---

### Q56. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the mean and the variance of a Binomial distribution for 5 trials is 1.8 , then the value of $\mathrm{p}$ is

**Options:**

- **(A)** 0.4
- **(B)** 0.8
- **(C)** 0.18
- **(D)** 0.2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.2**

**Detailed Solution:**

According to the given condition,
mean + variance $=1.8$
$\begin{aligned} & \Rightarrow n p+n p q=1.8 \\ & \Rightarrow 5 p+5 p q=1.8 \\ & \Rightarrow 5 p+5 p(1-p)=1.8 \\ & \Rightarrow 5 p+5 p-5 p^2=1.8 \\ & \Rightarrow 5 p^2-10 p+1.8=0 \\ & \Rightarrow 50 p^2-100 p+18=0 \\ & \Rightarrow(10 p-2)(5 p-9)=0 \\ & \Rightarrow p=\frac{2}{10}=0.2 \text { or } p=\frac{9}{5}=1.8\end{aligned}$
Since $0 < \mathrm{p} < 1$,
$\mathrm{p}=0.2$

</details>

---

### Q57. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{X}$ be random variable having Binomial distribution $\mathrm{B}(7, \mathrm{p})$. If $\mathrm{P}[\mathrm{X}=3]=5 \mathrm{P}[\mathrm{X}=4]$, then variance of $\mathrm{X}$ is

**Options:**

- **(A)** $\frac{7}{6}$
- **(B)** $\frac{35}{36}$
- **(C)** $\frac{77}{36}$
- **(D)** $\frac{1}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{35}{36}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{P}(\mathrm{X}=3)=5 \mathrm{P}(\mathrm{X}=4) \\ & \Rightarrow{ }^7 \mathrm{C}_3 \mathrm{p}^3 \mathrm{q}^4=5^7 \mathrm{C}_4 \mathrm{p}^4 \mathrm{q}^3 \\ & \Rightarrow 5 \mathrm{p}=\mathrm{q} \\ & \Rightarrow 5 \mathrm{p}=1-\mathrm{p} \\ & \Rightarrow 6 \mathrm{p}=1 \\ & \Rightarrow \mathrm{p}=\frac{1}{6} \\ & \Rightarrow \mathrm{q}=1-\frac{1}{6}=\frac{5}{6} \\ & \text { Variance }=\mathrm{npq} \\ & =7 \times \frac{1}{6} \times \frac{5}{6} \\ & =\frac{35}{36}\end{aligned}$

</details>

---

### Q58. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For a binomial variate $X$ with $n=6$ if $P(X=4)=\frac{135}{2^{12}}$, then its variance is

**Options:**

- **(A)** $\frac{8}{9}$
- **(B)** $\frac{1}{4}$
- **(C)** 4
- **(D)** $\frac{9}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{9}{8}$**

**Detailed Solution:**

$\begin{aligned} & \text { Given, } P(X=4)=\frac{135}{2^{12}} \\ & \Rightarrow{ }^6 C_4 p^4 q^2=\frac{135}{2^{12}} \\ & \Rightarrow 15 p^4 q^2=\frac{135}{2^{12}} \\ & \Rightarrow p^4 q^2=\frac{3^2}{2^{12}} \\ & \Rightarrow p^2 q=\frac{3}{2^6} \\ & \Rightarrow p^2(1-p)=\frac{3}{64} \\ & \Rightarrow p^2(1-p)=\left(\frac{1}{4}\right)^2 \cdot\left(1-\frac{1}{4}\right) \\ & \Rightarrow p=\frac{1}{4} \\ & \text { and } q=1-\frac{1}{4}=\frac{3}{4} \\ & \text { Variance }=n p q \\ & \quad=6 \times \frac{1}{4} \times \frac{3}{4} \\ & =\frac{9}{8}\end{aligned}$

</details>

---

### Q59. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a Binomial distribution with $\mathrm{n}=4$, if $2 \mathrm{P}(\mathrm{X}=3)=3 \mathrm{P}(\mathrm{X}=2)$, then the variance is

**Options:**

- **(A)** $\frac {36}{169}$
- **(B)** $\frac {144}{169}$
- **(C)** $\frac {9}{169}$
- **(D)** $\frac {16}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac {144}{169}$**

**Detailed Solution:**

$\begin{aligned} & P(X=3)={ }^4 C_3 p^3(1-p)=4 p^3(1-p) \\ & P(X=2)={ }^4 C_2 p^2(1-p)^2=6 p^2(1-p)^2 \\ & \text { Given } 2 \mathrm{P}(\mathrm{X}=3)=3 \mathrm{P}(\mathrm{X}=2) \\ & \therefore \quad 8 \mathrm{p}^3(1-\mathrm{p})=18 \mathrm{p}^2(1-\mathrm{p})^2 \\ & \therefore \quad 8 \mathrm{p}=18(1-\mathrm{p}) \\ & \therefore \quad \mathrm{p}=\frac{9}{13} \\ & \text { Variance }=n p(1-p) \\ & =4 \times \frac{9}{13}\left(1-\frac{9}{13}\right) \\ & =\frac{144}{169} \\ & \end{aligned}$

</details>

---

### Q60. MHT CET 2022 (11 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let a random variable $X$ have a Binomial distribution with mean 8 and variance 4 , If $P(X \leq 2)=\frac{k}{2^{16}}$ then $k$ is equal to

**Options:**

- **(A)** 121
- **(B)** 17
- **(C)** 137
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 137**

**Detailed Solution:**

$\begin{aligned}
& n p=8, n p q=4 \\
& \Rightarrow q=\frac{1}{2}, p=\frac{1}{2} \text { and } n=16
\end{aligned}$
Now $P(x \leq 2)=n_{C_0} p^0 q^n+n_{C_1} p^1 q^{n-1}+n_{C_2} p^2 q^{n-2}$
$\begin{aligned}
& =\left\{{ }^{16} C_0+{ }^{16} C_1+{ }^{16} C_2\right\}\left(\frac{1}{2}\right)^{16} \\
& =\frac{137}{2^{16}} \\
& \Rightarrow k=137
\end{aligned}$

</details>

---

### Q61. MHT CET 2022 (10 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability of success for the Binomial distribution satisfying the relation, $4 P(X=4)=P(X=2)$ and having the parameter $n=6$, is

**Options:**

- **(A)** $\frac{1}{5}$
- **(B)** $\frac{5}{6}$
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{3}$**

**Detailed Solution:**

$\begin{aligned} & 4 \cdot P(x=4)=P(x=2) \\ & \Rightarrow 4 \cdot{ }^6 C_4 P^4 \cdot q^2={ }^6 C_2 p^2 q^4 \\ & \Rightarrow \frac{p^2}{q^2}=\frac{1}{4}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/SYJFseBjAb3WjSrBadyGqORfS20cPCLmVj5EUoCrEmw.original.fullsize.png">
$\begin{aligned} & \Rightarrow 3 p=1 \\ & \Rightarrow p=\frac{1}{3}\end{aligned}$

</details>

---

### Q62. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

One coin is thrown 100 times, then the probability of getting head in odd number is

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{1}{5}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{3}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

$n=100, p=\frac{1}{2}, q=\frac{1}{2}$
$p(x=r$ where $r$ is odd $)=\sum_{r=\text { odd }}^n C_r p^r q^{n-r}$
$\begin{aligned} & =\sum_{r=\text { odd }}^{100} C_r\left(\frac{1}{2}\right)^r\left(\frac{1}{2}\right)^{100-r} \\ & =\left(\frac{1}{2}\right)^{100} \sum_{r=\text { odd }}{ }^{100} C_r \\ & =\left(\frac{1}{2}\right)^{100} \times 2^{99}=\frac{1}{2}\end{aligned}$

</details>

---

### Q63. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For a Binomial variate $x$, mean is 2 and variance is 1 , Then odds in favor of $X=0$ are

**Options:**

- **(A)** 4:1
- **(B)** 15:1
- **(C)** 1:15
- **(D)** 1:4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1:15**

**Detailed Solution:**

Mean $=n p=2$, variance $=n p q=1$
$\Rightarrow q=\frac{1}{2}, p=\frac{1}{2}$ and $n=4$
Now $P(x=0)={ }^4 C_0 P^0 \cdot q^4=1 \times 1 \times\left(\frac{1}{2}\right)^4=\frac{1}{16}$
$\Rightarrow$ odds in favour of $p(x=0)=\frac{\frac{1}{16}}{1-\frac{1}{16}}=1: 15$

</details>

---

### Q64. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a certain examination, a candidate has to pass in each of the 5 subjects. Hence, the number of ways he can fail is

**Options:**

- **(A)** $5 !$
- **(B)** 5
- **(C)** $2^5-1$
- **(D)** $2^5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2^5-1$**

**Detailed Solution:**

In each subject either he can pass or he can fail Total number of ways $=2^5$
Number of ways which he can pass is only Hence, the number of ways in which he can fail $=2^5-1$

</details>

---

### Q65. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a Binomial distribution, $n=4$ and $2 P(X=3)=3 P(X=2)$, then $q=$

**Options:**

- **(A)** $\frac{2}{13}$
- **(B)** $\frac{11}{13}$
- **(C)** $\frac{9}{13}$
- **(D)** $\frac{4}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{13}$**

**Detailed Solution:**

$\begin{aligned} & 2 P(x=3)=3 p(x=2) \\ & \Rightarrow 2 \times{ }^4 c_3(1-q)^3 q=3 \times{ }^4 c_2(1-q)^2 q^2 \\ & \Rightarrow 2 \times 4 \times(1-q)=3 \times 6 \times q \\ & \Rightarrow \frac{4}{9}=\frac{q}{1-q} \\ & \Rightarrow q=\frac{4}{13}\end{aligned}$

</details>

---

### Q66. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If $X \sim B\left(8, \frac{1}{2}\right)$, then $P(|x-4| \leq 2)=$

**Options:**

- **(A)** $\frac{119}{128}$
- **(B)** $\frac{117}{128}$
- **(C)** $\frac{1}{n}$
- **(D)** $\frac{116}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{119}{128}$**

**Detailed Solution:**

$X \sim B\left(8, \frac{1}{2}\right) \Rightarrow n=8$ and $p=\frac{1}{2}$ i.e., $q=\frac{1}{2}$
Now $p(|x-4| \leq 2)=p(-2 \leq x-4 \leq 2)=p(2 \leq x \leq 6)$
$\begin{aligned} & \text { i.e., } p(x=2, x=3, x=4, x=5, x=6) \\ & =1-{ }^8 C_0\left(\frac{1}{2}\right)^0 \cdot\left(\frac{1}{2}\right)^8-{ }^8 C_1\left(\frac{1}{2}\right)^1\left(\frac{1}{2}\right)^7-{ }^8 C_7\left(\frac{1}{2}\right)^7\left(\frac{1}{2}\right)^1-{ }^8 C_8\left(\frac{1}{2}\right)^8\left(\frac{1}{2}\right)^0 \\ & =1-\left(\frac{1}{2}\right)^8\{1+8+8+1\} \\ & =1-\frac{18}{256}=1-\frac{9}{128}=\frac{119}{128}\end{aligned}$

</details>

---

### Q67. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For a Binomial distribution, $n=6$, if $9 P(X=4)=P(X=2)$, then $q=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{4}$
- **(C)** $\frac{3}{4}$
- **(D)** $\frac{2}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{4}$**

**Detailed Solution:**

$\begin{aligned} & 9 P(X=4)=P(X=2) \\ & \Rightarrow 9{ }^n C_4 P^4 \cdot q^{n-4}={ }^n C_2 P^2 q^{n-2} \\ & \Rightarrow 9 \frac{{ }^n C_4}{{ }^n C_2}=\frac{q^2}{P^2}=\left(\frac{q}{1-q}\right)^2 \\ & \Rightarrow \frac{q}{1-q}=3 \Rightarrow q=\frac{3}{4}\end{aligned}$

</details>

---

### Q68. MHT CET 2022 (06 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn successively with replacement from a well shuffled pack of 52 cards. The mean of number of kings is

**Options:**

- **(A)** $\frac{4}{169}$
- **(B)** $\frac{1}{13}$
- **(C)** $\frac{1}{169}$
- **(D)** $\frac{2}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{2}{13}$**

**Detailed Solution:**

Here, $n=2, p=\frac{1}{13}$ and $q=\frac{12}{13}$
Mean, $n p=2 \times \frac{1}{13}=\frac{2}{13}$

</details>

---

### Q69. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An unbiased die is tossed 500 times. The standard deviation of getting sixes in these 500 tosses is

**Options:**

- **(A)** $\frac{625}{9}$
- **(B)** $\sqrt{\frac{250}{3}}$
- **(C)** $\frac{25}{3}$
- **(D)** $\frac{250}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{25}{3}$**

**Detailed Solution:**

$\mathrm{n}=500, \mathrm{P}=\frac{1}{6}, \mathrm{q}=\frac{5}{6}$
S.D. $=\sqrt{\mathrm{npq}}=\sqrt{500 \times \frac{1}{6} \times \frac{5}{6}}=\sqrt{\frac{2500}{36}}=\frac{50}{6}=\frac{25}{3}$

</details>

---

### Q70. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A die is thrown five times. If getting an odd number is a success, then the probability of getting at least 4 successes is

**Options:**

- **(A)** $\frac{13}{16}$
- **(B)** $\frac{5}{32}$
- **(C)** $\frac{1}{32}$
- **(D)** $\frac{3}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{16}$**

**Detailed Solution:**

Here, $n=5, p=\frac{1}{2}, q=\frac{1}{2}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/yoxgzkEj6-dAaiSLEVkLMiB0Juu7sS-DNpT6bddFsI0.original.fullsize.png">
Probability of getting at least 4 successes
$\begin{aligned} & \mathrm{P}(\mathrm{x}=4 \text { or } \mathrm{x}=5)={ }^5 \mathrm{C}_4\left(\frac{1}{2}\right)^4\left(\frac{1}{2}\right)^1+{ }^5 \mathrm{C}_5\left(\frac{1}{2}\right)^5\left(\frac{1}{2}\right)^{\circ} \\ & =5 \times \frac{1}{16} \times \frac{1}{2}+1 \times \frac{1}{32} \times 1 \\ & =\frac{5}{32}+\frac{1}{32} \\ & =\frac{6}{32}=\frac{3}{16}\end{aligned}$

</details>

---

### Q71. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A bag contains 4 red and 3 black balls. One ball is drawn and then replaced in the bag and the process is repeated. Let $X$ denote the number of times black ball is drawn in 3 draws. Assuming that at each draw each ball is equally likely to be selected, then the probability distribution of $X$ is given by

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/PYiS939m1KnOHqaPi9_fiCNnfe7yUClVRqTCs4xJVUI.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/zosdAFfOmAJyonxJd3odxnt90nLTNSdM7HFIw6Pe7Ps.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/8aKyPGAnS0Aiyj6JFEtvZmhxOFtU0CBfT1N8jG3Mnu4.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/-LIBh4gAiTiDoLLlndlhmFSdRAfO63JFn0axX10ob2U.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/-LIBh4gAiTiDoLLlndlhmFSdRAfO63JFn0axX10ob2U.original.fullsize.png">**

**Detailed Solution:**

Probability of drawing one black ball $={ }^3 \mathrm{C}_0\left(\frac{3}{7}\right)^0\left(\frac{4}{7}\right)^3=\left(\frac{4}{7}\right)^3$
Probability of drawing two black ball
$={ }^3 \mathrm{C}_1\left(\frac{3}{7}\right)^1\left(\frac{4}{7}\right)^2=3 \times \frac{3}{7} \times\left(\frac{4}{7}\right)^2=\frac{9}{7}\left(\frac{4}{7}\right)^2$
Probability of drawing zero black balls
$={ }^3 C_2\left(\frac{3}{7}\right)^2\left(\frac{4}{7}\right)^1=3 \times\left(\frac{3}{7}\right)^2 \times \frac{4}{7}=\frac{12}{7}\left(\frac{3}{7}\right)^2$
Probability of drawing three black balls $={ }^3 \mathrm{C}_3\left(\frac{3}{7}\right)^3\left(\frac{4}{7}\right)^0=\left(\frac{3}{7}\right)^3$

</details>

---

### Q72. MHT CET 2022 (05 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

It is observed that $30 \%$ of the students appearing for a certain entrance test are science students. If 5 students are randomly selected from this group,the probability of having 2 science students among these students is

**Options:**

- **(A)** $0.3087$
- **(B)** $0.2547$
- **(C)** $0.1087$
- **(D)** $0.3437$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.3087$**

**Detailed Solution:**

The required probability $={ }^5 C_2\left(\frac{30}{100}\right)^2 \times\left(\frac{70}{100}\right)^3$
$\begin{aligned} & =10 \times \frac{3}{10} \times \frac{3}{10} \times \frac{7}{10} \times \frac{7}{10} \times \frac{7}{10} \\ & =\frac{3087}{10000}=0.3087\end{aligned}$

</details>

---

### Q73. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed for a fixed number of times. If probability of getting 7 heads is equal to probability of getting 9 heads, then probability of getting 2 heads is

**Options:**

- **(A)** $\frac{1}{15}$
- **(B)** $\frac{15}{2^{13}}$
- **(C)** $\frac{15}{2^8}$
- **(D)** $\frac{2}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{15}{2^{13}}$**

**Detailed Solution:**

$\mathrm{p}=$ probability of getting head $=\frac{1}{2}$ and
$\mathrm{q}=$ probability of not getting head $\frac{1}{2}$
$\mathrm{P}(\mathrm{X}=\mathrm{x})={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{x}}\left(\frac{1}{2}\right)^{\mathrm{x}}\left(\frac{1}{2}\right)^{\mathrm{n}-\mathrm{x}}$
As per data given, we write
$\begin{aligned}
& \mathrm{P}(\mathrm{x}=7)=\mathrm{P}(\mathrm{x}=9) \\
& \therefore{ }^n \mathrm{C}_7\left(\frac{1}{2}\right)^7\left(\frac{1}{2}\right)^{\mathrm{n}-7}={ }^{\mathrm{n}} \mathrm{C}_9\left(\frac{1}{2}\right)^9\left(\frac{1}{2}\right)^{\mathrm{n}-9} \\
& \therefore \quad{ }^{\mathrm{n}} \mathrm{C}_7={ }^{\mathrm{n}} \mathrm{C}_9 \\
& \therefore \quad \mathrm{n}=16
\end{aligned}$
when $x=2$, we get
$\mathrm{P}(\mathrm{x}=2)={ }^{16} \mathrm{C}_2\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^{14}=\frac{16 \times 15}{2}\left(\frac{1}{2}\right)^{16}=\frac{15}{(2)^{13}}$

</details>

---

### Q74. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed 100 times. The probability of getting a head for even number of times is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{3}{8}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

We have $n=100$ and probability of getting head $=1 / 2$
Let $\mathrm{p}=1 / 2 \Rightarrow \mathrm{q}=1 / 2$
Probability of getting head even number of times $=$
$$
\begin{aligned}
& \mathrm{P}(\mathrm{X}=2)+(\mathrm{X}=4)+\ldots . .+(\mathrm{X}=100)] \\
& =\left[{ }^{100} \mathrm{C}_2\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^{98}+\ldots .+{ }^{100} \mathrm{C}_{100}\left(\frac{1}{2}\right)^{100}\left(\frac{1}{2}\right)^{\circ}\right] \\
& =\left(\frac{1}{2}\right)^{100}\left[{ }^{100} \mathrm{C}_2+{ }^{100} \mathrm{C}_4+\ldots .+{ }^{100} \mathrm{C}_{100}\right] \\
& =\left(\frac{1}{2}\right)^{100}\left[2^{100-1}\right]=\frac{1}{(2)^{100}} \times(2)^{99}=\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q75. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The probability distribution of the number of doublets in four throws of a pair of dice is given by

**Options:**

- **(A)** \begin{array}{|l|l|l|l|l|l|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}): & \frac{1}{5} & \frac{1}{5} & \frac{1}{5} & \frac{1}{5} & \frac{1}{5} \\
\hline
\end{array}
- **(B)** \begin{array}{|l|l|l|l|l|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 \\
\hline \mathrm{P}(\mathrm{X}): & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} \\
\hline
\end{array}
- **(C)** \begin{array}{|l|l|l|l|l|l|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}): & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} \\
\hline
\end{array}
- **(D)** \begin{array}{|l|l|l|l|l|l|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}): & \frac{625}{1296} & \frac{125}{324} & \frac{25}{216} & \frac{5}{324} & \frac{1}{1296} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \begin{array}{|l|l|l|l|l|l|}
\hline \mathrm{X}: & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}): & \frac{625}{1296} & \frac{125}{324} & \frac{25}{216} & \frac{5}{324} & \frac{1}{1296} \\
\hline
\end{array}**

**Detailed Solution:**

Let $\mathrm{p}=$ Probability of getting a doublet in a throw of pair of dice.
$$
\mathrm{p}=\frac{6}{36}=\frac{1}{6} \text { and } \mathrm{q}=1-\frac{1}{6}=\frac{5}{6}
$$
Dice are thrown 4 times.
Let $\mathrm{X}=0,1,2,3,4$ denote number of times a doublet is obtained.
When $\mathrm{X}=0, \mathrm{p}=\frac{5}{6} \times \frac{5}{6} \times \frac{5}{6} \times \frac{5}{6}=\frac{625}{1296}$
When $\mathrm{X}=1, \mathrm{p}=\left({ }^4 \mathrm{C}_1\right) \times \frac{1}{6} \times \frac{5}{6} \times \frac{5}{6} \times \frac{5}{6}=\frac{125}{324}$
$$
\begin{aligned}
& X=2, p=\left({ }^4 C_2\right) \times \frac{1}{6} \times \frac{1}{6} \times \frac{5}{6} \times \frac{5}{6}=\frac{25}{216} \\
& X=3, p=\left({ }^4 C_3\right) \times \frac{1}{6} \times \frac{1}{6} \times \frac{1}{6} \times \frac{5}{6}=\frac{5}{324} \\
& X=4, p=\frac{1}{6} \times \frac{1}{6} \times \frac{1}{6} \times \frac{1}{6}=\frac{1}{1296}
\end{aligned}
$$

</details>

---

### Q76. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the mean and variance of a binomial distribution are 4 and 2 respectively, then probability of getting 2 heads is

**Options:**

- **(A)** $\frac{28}{256}$
- **(B)** $\frac{37}{256}$
- **(C)** $\frac{128}{256}$
- **(D)** $\frac{219}{256}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{28}{256}$**

**Detailed Solution:**

We have $n p=4$ and $n p q=2$
$$
\therefore \mathrm{q}=\frac{2}{4}=\frac{1}{2} \quad \Rightarrow \mathrm{p}=1-\frac{1}{2}=\frac{1}{2} \text { and } \mathrm{n}\left(\frac{1}{2}\right)=4 \Rightarrow \mathrm{n}=8
$$
$\therefore$
$$
P(x=2)={ }^8 C_2\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^6=\frac{8 !}{2 ! 6 !}\left(\frac{1}{2}\right)^8=\frac{8 \times 7}{2 \times 2^3 \times 2^5}=\frac{7}{64}=\frac{28}{256}
$$

</details>

---

### Q77. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If is observed that $25 \%$ of the cases related to child labour reported to the police station are solved. If 6 new cases are reported, then the probability that at least 5 of them will be solved is

**Options:**

- **(A)** $\frac{19}{1024}$
- **(B)** $\frac{19}{4096}$
- **(C)** $\left(\frac{1}{4}\right)^6$
- **(D)** $\frac{19}{2048}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{19}{4096}$**

**Detailed Solution:**

We have probability of cases getting solved $=25 \%=\frac{1}{4}$
$\mathrm{p}=\frac{1}{4} \Rightarrow \mathrm{q}=\frac{3}{4}$ and we have $\mathrm{n}=6, \mathrm{x}=5,6$
Hence required probability
$$
\begin{aligned}
& =\left[{ }^6 \mathrm{C}_5\left(\frac{1}{4}\right)^5\left(\frac{3}{4}\right)^1\right]+\left[{ }^6 \mathrm{C}_6\left(\frac{1}{4}\right)^6\left(\frac{3}{4}\right)^0\right] \\
& =\frac{(6)(3)}{(4)^6}+\frac{1}{(4)^6}=\frac{19}{(4)^6}=\frac{19}{4096}
\end{aligned}
$$

</details>

---

### Q78. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

It is known that a box of 8 batteries contains 3 defective pieces and a person randomly selects two batteries from the box. If $X$ is the number of defective batteries selected,
then $P(X \leq 1)=$

**Options:**

- **(A)** $\frac{25}{28}$
- **(B)** $\frac{14}{28}$
- **(C)** $\frac{10}{28}$
- **(D)** $\frac{13}{28}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{25}{28}$**

**Detailed Solution:**

We have probability of selecting defective batteries $=\frac{3}{8}$
$$
\begin{aligned}
\therefore & p=\frac{3}{8} \text { and } q=\frac{5}{8} \\
\therefore & P(X=0)+P(X=1) \\
&=\left[{ }^{2} C_{0}\left(\frac{3}{8}\right)^{0} \times\left(\frac{5}{8}\right)^{2}\right]+\left[{ }^{2} C_{1}\left(\frac{3}{8}\right)^{1} \times\left(\frac{5}{8}\right)^{1}\right] \\
&=\frac{25}{64}+\frac{2 \times 3 \times 5}{64}=\frac{55}{64}
\end{aligned}
$$

</details>

---

### Q79. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A die is thrown 100 times. If the success is in getting an even number, then the variance of number of successes is

**Options:**

- **(A)** $1.10$
- **(B)** $25$
- **(C)** 50
- **(D)** 100

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $25$**

**Detailed Solution:**

Let
A = event "Obtainimen an even mumber when a fail tie is therwn
$\therefore p=\frac{3}{6}=\frac{1}{2} \Rightarrow 1-1-p-\frac{1}{2}$
$\therefore$ Varianco ovor 100 trails $-1100-100 \times \frac{1}{2} \times \frac{1}{2}-25$

</details>

---

### Q80. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the mean and the variance of a binomial distribution for 5 trials is $1 \cdot 8$,
then $\mathrm{p}=$

**Options:**

- **(A)** $0 \cdot 4$
- **(B)** $0 \cdot 2$
- **(C)** $0 \cdot 8$
- **(D)** $0 \cdot 18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0 \cdot 2$**

**Detailed Solution:**

(B)
We have $n=5$ and $n p+n p q=1.8$
$5 p+5 p q=1.8 \Rightarrow 5 p(1+q)=1.8$
$\therefore 5 \mathrm{p}[1+(1-\mathrm{p})]=1.8 \Rightarrow 5 \mathrm{p}(2-\mathrm{p})=1.8$
$\therefore 5 p^{2}-10 p+1.8=0$
$\therefore 5 p^{2}-p-9 p+1.8=0 \quad \Rightarrow p(5 p-1)-1.8(5 p-1)=0$
$\therefore(p-1.8)(59-1)=0 \Rightarrow p=\frac{1}{5}, 1.8$ (impossible)
$\therefore \quad \mathrm{p}=0.2$

</details>

---

### Q81. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Given $X \sim B(n, p)$, If $E(X)=4$ and $\operatorname{Var}(X)=2 \cdot 4$, then $\mathrm{n}=$

**Options:**

- **(A)** 20
- **(B)** 15
- **(C)** 5
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 10**

**Detailed Solution:**

(A)
$\begin{array}{l}
\mathrm{E}(\mathrm{X})=4 \Rightarrow \mathrm{np}=4 \\
\operatorname{Var}(\mathrm{X})=\mathrm{npq}=2.4 \Rightarrow 4 \mathrm{q}=2.4 \Rightarrow \mathrm{q}=\frac{3}{5} \\
\therefore \mathrm{p}=\frac{2}{5} \text { and } \mathrm{n}\left(\frac{2}{5}\right)=4 \Rightarrow \mathrm{n}=10
\end{array}$

</details>

---

### Q82. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Out of 100 people selected at random, 10 have common cold. If five persons selected at random from the group, then the probability that at most one person will have common cold is

**Options:**

- **(A)** $0.9254$
- **(B)** $0.9185$
- **(C)** $0.9851$
- **(D)** $0.9245$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.9185$**

**Detailed Solution:**

(C)
Let probability of having common cold $\mathrm{p}=\frac{10}{100}=\frac{1}{10} \Rightarrow \mathrm{q}=\frac{9}{10}$ Here $\mathrm{n}=5$, and $\mathrm{x}=0,1$.
Hence required probability
$\begin{array}{l}
={ }^{5} \mathrm{C}_{0}\left(\frac{1}{10}\right)^{0}\left(\frac{9}{10}\right)^{5}+{ }^{5} \mathrm{C}_{1}\left(\frac{1}{10}\right)^{1}\left(\frac{9}{10}\right)^{4} \\
=\left(\frac{9}{10}\right)^{5}+\frac{5(9)^{4}}{(10)^{5}}=\frac{\left(9^{4}\right)[9+5]}{(10)^{5}}=\frac{81 \times 81 \times 14}{10^{5}}=0.9185
\end{array}$

</details>

---

### Q83. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The probability that bomb will miss the target is $0 \cdot 2$. Then the probability that out of 10 bombs dropped exactly 2 will hit the target is

**Options:**

- **(A)** $\frac{288}{5^{10}}$
- **(B)** $\frac{144}{5^{9}}$
- **(C)** $\frac{144}{5^{10}}$
- **(D)** $\frac{288}{5^{9}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{144}{5^{9}}$**

**Detailed Solution:**

$(\mathrm{C})$
We have probability of missing the target $0.2$
Let $\mathrm{p}=1-0.2=0.8, \mathrm{q}=0.2, \mathrm{n}=10$ and $\mathrm{r}=2$
Hence required probability $={ }^{10} \mathrm{C}_{2}(0.8)^{2}(0.2)^{8}$
$=\frac{10 !}{2 ! 8 !} \times\left(\frac{8}{10}\right)^{2} \times\left(\frac{2}{10}\right)^{8}=\frac{45 \times 64 \times 2^{8}}{10^{10}}=\frac{9 \times 5 \times 2^{14}}{2^{10} \times 5^{10}}=\frac{9 \times 2^{4}}{5^{9}}=\frac{144}{5^{9}}$

</details>

---

### Q84. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a fair coin is tossed 8 times, then the probability that it shows heads more than tails is

**Options:**

- **(A)** $\frac{91}{256}$
- **(B)** $\frac{97}{256}$
- **(C)** $\frac{93}{256}$
- **(D)** $\frac{95}{256}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{93}{256}$**

**Detailed Solution:**

Given $n=8 .$ Here $p=\frac{1}{2}, q=\frac{1}{2}$
$\begin{aligned} P(x>4) &=P(x=5)+P(x=6)+P(x=7)+P(x=8) \\ &={ }^{8} C_{5}\left(\frac{1}{2}\right)^{5}\left(\frac{1}{2}\right)^{3}+{ }^{8} C_{6}\left(\frac{1}{2}\right)^{6}\left(\frac{1}{2}\right)^{2}+{ }^{8} C_{7}\left(\frac{1}{2}\right)^{7}\left(\frac{1}{2}\right)^{1}+{ }^{8} C_{8}\left(\frac{1}{2}\right)^{8}\left(\frac{1}{2}\right)^{0} \\ &=\frac{56}{256}+\frac{28}{256}+\frac{8}{256}+\frac{1}{256}=\frac{93}{256} \end{aligned}$

</details>

---

### Q85. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a box containing 100 bulbs, 10 are defective. The probability that out of 20 bulbs selected at random, none is defective is

**Options:**

- **(A)** $10\left(\frac{1}{10}\right)^{20}$
- **(B)** $20\left(\frac{9}{10}\right)^{20}$
- **(C)** $5\left(\frac{1}{10}\right)^{20}$
- **(D)** $\left(\frac{9}{10}\right)^{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(\frac{9}{10}\right)^{20}$**

**Detailed Solution:**

Let $\mathrm{X}$ denote number of defective bulbs out of 20 bulbs $\mathrm{p}=$ probability of getting defective bulb $=\frac{10}{100}=\frac{1}{10}$ $\therefore \mathrm{q}=1-\frac{1}{10}=\frac{9}{10}$ and $\mathrm{n}=20$, Probability of getting no detective bulb is $={ }^{20} \mathrm{C}_{0}\left(\frac{9}{10}\right)^{20}\left(\frac{1}{10}\right)^{0}=\left(\frac{9}{10}\right)^{20}$

</details>

---

### Q86. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A fair coin is tossed 2 times. A person receives $â‚¹ X^{3}$ if he gets $X$ number of heads.
His expected gain is $=$

**Options:**

- **(A)** $â‚¹ 2.00$
- **(B)** $â‚¹ 1.00$
- **(C)** $â‚¹ 2.50$
- **(D)** $â‚¹ 5.20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $â‚¹ 2.50$**

**Detailed Solution:**

A fair coin is tossed 2 times. Possible outcomes are HH, HT, TH, TT $\therefore X$ takes values $0,1,2$
$$
\therefore P(X=0)=\frac{1}{4}, P(X=1)=\frac{2}{4}=\frac{1}{2}, P(X=2)=\frac{1}{4}
$$
Given a person receives $â‚¹ X^{3}$ if we gets $X$ no. of heads.
$$
\begin{aligned}
\therefore \text { Expected gain } &=\left(\frac{1}{4} \times 0\right)+\left(\frac{1}{2} \times 1^{3}\right)+\left(\frac{1}{4} \times 2^{3}\right) \\
&=0+\frac{1}{2}+\frac{8}{4}=2.5
\end{aligned}
$$

</details>

---

### Q87. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $X \sim B(4, p)$ and $2 P(X=3)=3 P(X=2)$ then value of $p$ is

**Options:**

- **(A)** $\frac{9}{13}$
- **(B)** $\frac{4}{13}$
- **(C)** $\frac{1}{13}$
- **(D)** $\frac{12}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{9}{13}$**

**Detailed Solution:**

Given $X \sim B(4, p)$ and $2 P(X=3)=3 P(X=2)$
$2\left[{ }^{4} C_{3} p^{3} q^{1}\right]=3\left[{ }^{4} C_{2} p^{2} q^{2}\right]$
$2 \times 4 p^{3} q=3 \times 6 p^{2} q^{2}$
$\therefore p=\frac{9 q}{4} \Rightarrow p=\frac{9}{4}(1-p) \Rightarrow p=\frac{9}{4}-\frac{9}{4} p$
$\left(1+\frac{9}{4}\right) p=\frac{9}{4} \Rightarrow \frac{13 p}{4}=\frac{9}{4} \Rightarrow p=\frac{9}{13}$

</details>

---

### Q88. MHT CET 2012

*Type:* `singleCorrect` | *Level:* `1`

15 coins are tossed, then the probability of getting 10 heads will be

**Options:**

- **(A)** $\frac{511}{32768}$
- **(B)** $\frac{1001}{32768}$
- **(C)** $\frac{3003}{32768}$
- **(D)** $\frac{3005}{32768}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3003}{32768}$**

**Detailed Solution:**

$\therefore$ Required probability $={ }^{15} C_{10}\left(\frac{1}{2}\right)^{10}\left(\frac{1}{2}\right)^{5}$
$={ }^{15} C_{5} \frac{1}{2^{15}}$
$=\frac{15 \times 14 \times 13 \times 12 \times 11}{5 \times 4 \times 3 \times 2 \times 1} \times \frac{1}{2^{15}}$
$=\frac{3003}{32768}$

</details>

---

### Q89. MHT CET 2011

*Type:* `singleCorrect` | *Level:* `1`

If $x$ follows the Binomial distribution with parameters $n=6$ and $p$ and $9 P(X=4)$ $=P(X=2)$, then $p$ is

**Options:**

- **(A)** $1 / 4$
- **(B)** $1 / 3$
- **(C)** $1 / 2$
- **(D)** $2 / 3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1 / 4$**

**Detailed Solution:**

Given, $9 P(X=4)=P(X=2)$
$\therefore \quad 9 \cdot{ }^{6} C_{4} p^{4}(1-p)^{2}={ }^{6} C_{2} p^{2}(1-p)^{4}$
$\Rightarrow \quad \frac{(1-p)^{2}}{p^{2}}=9$
$\Rightarrow \quad \frac{1-p}{p}=3$
$\Rightarrow \quad p=1 / 4$

</details>

---

