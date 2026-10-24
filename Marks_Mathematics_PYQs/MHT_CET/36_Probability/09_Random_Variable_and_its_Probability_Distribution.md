# MHT CET Mathematics - Probability

## Topic 9: Random Variable and its Probability Distribution

**Total Questions:** 179

---

### Q1. MHT CET 2026 (20 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two numbers are selected without replacement from the first six positive integers. Let X denote the number of prime numbers obtained. The mean value of X is .......

**Options:**

- **(A)** $0.6$
- **(B)** $1$
- **(C)** $1.2$
- **(D)** $0.8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1$**

**Detailed Solution:**

The first six positive integers are $1, 2, 3, 4, 5, 6$.

The prime numbers in this set are $2, 3, 5$. There are $3$ prime numbers and $3$ non-prime numbers.

Two numbers are selected without replacement. The total number of ways to select $2$ numbers is $^{6}C_{2} = 15$.

Let $X$ denote the number of prime numbers obtained. $X$ can take values $0, 1, 2$.

$P(X = 0) = \dfrac{^{3}C_{0} \times ^{3}C_{2}}{15} = \dfrac{3}{15}$

$P(X = 1) = \dfrac{^{3}C_{1} \times ^{3}C_{1}}{15} = \dfrac{9}{15}$

$P(X = 2) = \dfrac{^{3}C_{2} \times ^{3}C_{0}}{15} = \dfrac{3}{15}$

The mean value of $X$ is given by $E(X) = \sum x_i P(x_i)$.

$E(X) = 0 \times \dfrac{3}{15} + 1 \times \dfrac{9}{15} + 2 \times \dfrac{3}{15} = \dfrac{9 + 6}{15} = 1$

Answer: $1$

</details>

---

### Q2. MHT CET 2026 (19 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The variance of randam variable $X$, for the following probability mass function (p. m. f.) is ...
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{5}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{2}{5}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{2}{5}$</td></tr></table>

**Options:**

- **(A)** $\dfrac{14}{25}$
- **(B)** $\dfrac{11}{5}$
- **(C)** $\dfrac{\sqrt{14}}{5}$
- **(D)** $\dfrac{11}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{14}{25}$**

**Detailed Solution:**

$E(X) = \sum x_i P(x_i) = 1 \times \dfrac{1}{5} + 2 \times \dfrac{2}{5} + 3 \times \dfrac{2}{5} = \dfrac{11}{5}$

$E(X^2) = \sum x_i^2 P(x_i) = 1^2 \times \dfrac{1}{5} + 2^2 \times \dfrac{2}{5} + 3^2 \times \dfrac{2}{5} = \dfrac{1}{5} + \dfrac{8}{5} + \dfrac{18}{5} = \dfrac{27}{5}$

$Var(X) = E(X^2) - [E(X)]^2 = \dfrac{27}{5} - \left(\dfrac{11}{5}\right)^2$

$Var(X) = \dfrac{135}{25} - \dfrac{121}{25} = \dfrac{14}{25}$

Answer: $\dfrac{14}{25}$

</details>

---

### Q3. MHT CET 2026 (19 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X takes the values 0, 1, 2, 3 and its mean is $1.3$. If $P(X=3) = 2P(X=1)$ and $P(X=2) = 0.3$, then $P(X = 0)$ is

**Options:**

- **(A)** $0.2$
- **(B)** $0.1$
- **(C)** $0.3$
- **(D)** $0.4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.4$**

**Detailed Solution:**

Let $P(X=1) = p$ and $P(X=0) = q$.

Given $P(X=3) = 2P(X=1) = 2p$ and $P(X=2) = 0.3$.

The sum of all probabilities is $1$:

$P(X=0) + P(X=1) + P(X=2) + P(X=3) = 1$

$q + p + 0.3 + 2p = 1$

$q + 3p = 0.7$

The mean of the random variable $X$ is given by $E(X) = \sum x_i P(x_i)$:

$E(X) = 0 \cdot P(X=0) + 1 \cdot P(X=1) + 2 \cdot P(X=2) + 3 \cdot P(X=3)$

$1.3 = 0 \cdot q + 1 \cdot p + 2 \cdot 0.3 + 3 \cdot 2p$

$1.3 = p + 0.6 + 6p$

$7p = 0.7 \Rightarrow p = 0.1$

Substituting $p = 0.1$ in the first equation:

$q + 3(0.1) = 0.7$

$q = 0.4$

Thus, $P(X=0) = 0.4$.

Answer: $0.4$

</details>

---

### Q4. MHT CET 2026 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a discrete random variable (r.v.) $X$ is given below:
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$0$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$k$</td><td style="border: 1px solid black; padding: 10px;">$2k$</td><td style="border: 1px solid black; padding: 10px;">$4k$</td><td style="border: 1px solid black; padding: 10px;">$2k$</td><td style="border: 1px solid black; padding: 10px;">$k$</td></tr></table>
Then the value of $P[X \leq E(X)]$ is:

**Options:**

- **(A)** $\dfrac{7}{10}$
- **(B)** $\dfrac{1}{10}$
- **(C)** $\dfrac{3}{10}$
- **(D)** $\dfrac{9}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{7}{10}$**

**Detailed Solution:**

The sum of probabilities of a probability distribution is always $1$.

$\sum P(X=x) = k + 2k + 4k + 2k + k = 1$

$10k = 1 \Rightarrow k = \dfrac{1}{10}$

The expected value $E(X)$ is given by $\sum x P(X=x)$.

$E(X) = 0(k) + 1(2k) + 2(4k) + 3(2k) + 4(k)$

$E(X) = 2k + 8k + 6k + 4k = 20k$

Substituting $k = \dfrac{1}{10}$, we get $E(X) = 20 \times \dfrac{1}{10} = 2$.

We need to find $P[X \leq E(X)]$, which is $P(X \leq 2)$.

$P(X \leq 2) = P(X=0) + P(X=1) + P(X=2)$

$P(X \leq 2) = k + 2k + 4k = 7k$

Substituting $k = \dfrac{1}{10}$, we get $P(X \leq 2) = \dfrac{7}{10}$.

Answer: $\dfrac{7}{10}$

</details>

---

### Q5. MHT CET 2026 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability mass function (p.m.f.) of a random variable X is as follows:
$P(X=0) = 3k^3,\ P(X=1) = 4k - 10k^2,\ P(X=2) = 5k - 1,\ P(X=x) = 0$ for any value of $x$, then the value of $k$ is:

**Options:**

- **(A)** $\dfrac{3}{4}$
- **(B)** $\dfrac{3}{7}$
- **(C)** $\dfrac{1}{3}$
- **(D)** $\dfrac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{3}$**

**Detailed Solution:**

For a valid probability mass function, the sum of all probabilities must be equal to $1$.

$\sum P(X=x) = 1$

$P(X=0) + P(X=1) + P(X=2) = 1$

$3k^3 + (4k - 10k^2) + (5k - 1) = 1$

$3k^3 - 10k^2 + 9k - 2 = 0$

$(k - 1)(3k^2 - 7k + 2) = 0$

$(k - 1)(k - 2)(3k - 1) = 0$

This gives $k = 1$, $k = 2$, or $k = \dfrac{1}{3}$.

For $k = 1$, $P(X=0) = 3(1)^3 = 3$, which is not possible since probability cannot exceed $1$.

For $k = 2$, $P(X=0) = 3(2)^3 = 24$, which is also not possible.

For $k = \dfrac{1}{3}$, the probabilities are:

$P(X=0) = 3\left(\dfrac{1}{3}\right)^3 = \dfrac{1}{9}$

$P(X=1) = 4\left(\dfrac{1}{3}\right) - 10\left(\dfrac{1}{3}\right)^2 = \dfrac{2}{9}$

$P(X=2) = 5\left(\dfrac{1}{3}\right) - 1 = \dfrac{2}{3}$

Since all probabilities lie in the interval $[0, 1]$ and their sum is $1$, $k = \dfrac{1}{3}$ is the only valid value.

Answer: $\dfrac{1}{3}$

</details>

---

### Q6. MHT CET 2026 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two numbers are selected at random without replacement from the first $n$ natural numbers. Let X denote the larger of the two numbers obtained. If $E(X) = \dfrac{14}{3}$, then the value of $n$ is

**Options:**

- **(A)** $2$
- **(B)** $4$
- **(C)** $6$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6$**

**Detailed Solution:**

Total number of ways to select two numbers from the first $n$ natural numbers is $^{n}C_{2} = \dfrac{n(n-1)}{2}$.

Let $X$ be the larger of the two numbers. The possible values of $X$ are $2, 3, \dots, n$.

For $X = k$, the larger number is $k$, so the smaller number must be selected from $1, 2, \dots, k-1$. The number of ways to do this is $k-1$.

Thus, the probability $P(X = k) = \dfrac{k-1}{^{n}C_{2}} = \dfrac{2(k-1)}{n(n-1)}$.

The expected value $E(X)$ is given by:

$E(X) = \sum_{k=2}^{n} k P(X = k) = \sum_{k=2}^{n} k \dfrac{2(k-1)}{n(n-1)}$

$E(X) = \dfrac{2}{n(n-1)} \sum_{k=2}^{n} k(k-1)$

Using the standard summation formula $\sum_{k=1}^{n} k(k-1) = \dfrac{n(n-1)(n+1)}{3}$, we get:

$E(X) = \dfrac{2}{n(n-1)} \times \dfrac{n(n-1)(n+1)}{3} = \dfrac{2(n+1)}{3}$

Given $E(X) = \dfrac{14}{3}$, we have:

$\dfrac{2(n+1)}{3} = \dfrac{14}{3}$

$2(n+1) = 14$

$n+1 = 7$

$n = 6$

Answer: $6$

</details>

---

### Q7. MHT CET 2026 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let X be a random variable with the probability density function defined by
$f(x) = \dfrac{1}{x^2},\ 1 < x < \infty$
$= 0$ otherwise.
If $C_1 = \{x : 1 < x < 2\}$ and $C_2 = \{x : 4 < x < 5\}$ then $P(C_1 \cup C_2) =$

**Options:**

- **(A)** $0.36$
- **(B)** $0.44$
- **(C)** $0.63$
- **(D)** $0.55$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.55$**

**Detailed Solution:**

Since $C_1$ and $C_2$ are disjoint intervals, $P(C_1 \cup C_2) = P(C_1) + P(C_2)$.

$P(C_1) = \int_{1}^{2} f(x) dx = \int_{1}^{2} \dfrac{1}{x^2} dx = \left[ -\dfrac{1}{x} \right]_{1}^{2} = -\dfrac{1}{2} - (-1) = \dfrac{1}{2} = 0.5$

$P(C_2) = \int_{4}^{5} f(x) dx = \int_{4}^{5} \dfrac{1}{x^2} dx = \left[ -\dfrac{1}{x} \right]_{4}^{5} = -\dfrac{1}{5} - \left(-\dfrac{1}{4}\right) = \dfrac{1}{4} - \dfrac{1}{5} = 0.25 - 0.20 = 0.05$

$P(C_1 \cup C_2) = 0.5 + 0.05 = 0.55$

Answer: $0.55$

</details>

---

### Q8. MHT CET 2026 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $X$ be a continuous r. v. with p. d. f.
$f(x) = \begin{cases} kx^3, & 0 \leq x \leq 1 \\ 0, & \text{otherwise} \end{cases}$
then $P\left(X \leq \dfrac{3}{4} \mid X > \dfrac{1}{4}\right) = \ldots$

**Options:**

- **(A)** $\dfrac{1}{16}$
- **(B)** $\dfrac{255}{256}$
- **(C)** $\dfrac{16}{51}$
- **(D)** $\dfrac{11}{165}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{16}{51}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, the total probability must be $1$.

$\int_{-\infty}^{\infty} f(x) dx = 1$

$\int_{0}^{1} kx^3 dx = 1$

$k \left[ \dfrac{x^4}{4} \right]_{0}^{1} = 1 \Rightarrow \dfrac{k}{4} = 1 \Rightarrow k = 4$

Thus, $f(x) = 4x^3$ for $0 \leq x \leq 1$.

Using the definition of conditional probability:

$P\left(X \leq \dfrac{3}{4} \mid X > \dfrac{1}{4}\right) = \dfrac{P\left(\dfrac{1}{4} < X \leq \dfrac{3}{4}\right)}{P\left(X > \dfrac{1}{4}\right)}$

Evaluating the numerator:

$P\left(\dfrac{1}{4} < X \leq \dfrac{3}{4}\right) = \int_{1/4}^{3/4} 4x^3 dx = \left[ x^4 \right]_{1/4}^{3/4} = \left(\dfrac{3}{4}\right)^4 - \left(\dfrac{1}{4}\right)^4 = \dfrac{81}{256} - \dfrac{1}{256} = \dfrac{80}{256}$

Evaluating the denominator:

$P\left(X > \dfrac{1}{4}\right) = \int_{1/4}^{1} 4x^3 dx = \left[ x^4 \right]_{1/4}^{1} = 1^4 - \left(\dfrac{1}{4}\right)^4 = 1 - \dfrac{1}{256} = \dfrac{255}{256}$

Substituting these values into the conditional probability formula:

$P\left(X \leq \dfrac{3}{4} \mid X > \dfrac{1}{4}\right) = \dfrac{\dfrac{80}{256}}{\dfrac{255}{256}} = \dfrac{80}{255}$

Dividing the numerator and the denominator by $5$ gives:

$\dfrac{80}{255} = \dfrac{16}{51}$

Answer: $\dfrac{16}{51}$

</details>

---

### Q9. MHT CET 2026 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A continuous random variable X has the following probability distribution function (p.d.f.)
$f(x) = \begin{cases} kx^2 & \text{for } 0 \leq x \leq 3 \\ 0 & \text{otherwise} \end{cases}$
If $P(X > a) = 0.5$, then the value of $a$ is...

**Options:**

- **(A)** $\sqrt[3]{6.75}$
- **(B)** $\sqrt[3]{13.5}$
- **(C)** $\sqrt[3]{9}$
- **(D)** $\sqrt[3]{18}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt[3]{13.5}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, the total probability is $1$.

$\int_{0}^{3} kx^2 dx = 1$

$k \left[ \dfrac{x^3}{3} \right]_{0}^{3} = 1$

$k \left( \dfrac{27}{3} \right) = 1 \Rightarrow 9k = 1 \Rightarrow k = \dfrac{1}{9}$

The probability density function is $f(x) = \dfrac{1}{9}x^2$ for $0 \leq x \leq 3$.

Given $P(X > a) = 0.5$, we have:

$\int_{a}^{3} \dfrac{1}{9}x^2 dx = 0.5$

$\dfrac{1}{9} \left[ \dfrac{x^3}{3} \right]_{a}^{3} = 0.5$

$\dfrac{1}{27} (27 - a^3) = 0.5$

$1 - \dfrac{a^3}{27} = 0.5$

$\dfrac{a^3}{27} = 0.5$

$a^3 = 13.5$

$a = \sqrt[3]{13.5}$

Answer: $\sqrt[3]{13.5}$

</details>

---

### Q10. MHT CET 2026 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability mass function (p.m.f) of a random variable $X$ is $p(x) = \dfrac{x + 3}{k}, x = -2, -1, 0, 1$ and $p(x) = 0$ otherwise, then the value of $E(x) = ...$

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $-1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0$**

**Detailed Solution:**

The sum of probabilities of a probability mass function is $1$.

$\sum p(x) = 1$

$p(-2) + p(-1) + p(0) + p(1) = 1$

$\dfrac{-2 + 3}{k} + \dfrac{-1 + 3}{k} + \dfrac{0 + 3}{k} + \dfrac{1 + 3}{k} = 1$

$\dfrac{1}{k} + \dfrac{2}{k} + \dfrac{3}{k} + \dfrac{4}{k} = 1$

$\dfrac{10}{k} = 1 \Rightarrow k = 10$

The expected value $E(X)$ is given by $\sum x p(x)$.

$E(X) = (-2)p(-2) + (-1)p(-1) + (0)p(0) + (1)p(1)$

$E(X) = (-2)\left(\dfrac{1}{10}\right) + (-1)\left(\dfrac{2}{10}\right) + (0)\left(\dfrac{3}{10}\right) + (1)\left(\dfrac{4}{10}\right)$

$E(X) = \dfrac{-2 - 2 + 0 + 4}{10} = 0$

Answer: $0$

</details>

---

### Q11. MHT CET 2026 (20 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the following probability distribution of a random variable $X$, the Expected value and Variance of $X$ are respectively
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$1/5$</td><td style="border: 1px solid black; padding: 10px;">$2/5$</td><td style="border: 1px solid black; padding: 10px;">$2/5$</td></tr></table>

**Options:**

- **(A)** $\dfrac{27}{5}, \dfrac{27}{25}$
- **(B)** $\dfrac{11}{5}, \dfrac{14}{25}$
- **(C)** $\dfrac{4}{5}, \dfrac{14}{25}$
- **(D)** $\dfrac{7}{5}, \dfrac{11}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{11}{5}, \dfrac{14}{25}$**

**Detailed Solution:**

The expected value of $X$ is given by $E(X) = \sum x_i P(x_i)$

$E(X) = 1 \times \dfrac{1}{5} + 2 \times \dfrac{2}{5} + 3 \times \dfrac{2}{5} = \dfrac{1}{5} + \dfrac{4}{5} + \dfrac{6}{5} = \dfrac{11}{5}$

The expected value of $X^2$ is given by $E(X^2) = \sum x_i^2 P(x_i)$

$E(X^2) = 1^2 \times \dfrac{1}{5} + 2^2 \times \dfrac{2}{5} + 3^2 \times \dfrac{2}{5} = \dfrac{1}{5} + \dfrac{8}{5} + \dfrac{18}{5} = \dfrac{27}{5}$

The variance of $X$ is given by $Var(X) = E(X^2) - (E(X))^2$

$Var(X) = \dfrac{27}{5} - \left(\dfrac{11}{5}\right)^2 = \dfrac{27}{5} - \dfrac{121}{25} = \dfrac{135 - 121}{25} = \dfrac{14}{25}$

Answer: $\dfrac{11}{5}, \dfrac{14}{25}$

</details>

---

### Q12. MHT CET 2026 (20 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let X be a continuous random variable with the probability density function(p.d.f.) given by
$f(x) = \begin{cases} kx, & 0 \leq x < 1 \\ k, & 1 \leq x < 2 \\ -kx + 3k, & 2 \leq x < 3 \\ 0, & \text{otherwise} \end{cases}$
$P(2 < X \leq 3) = \cdots$

**Options:**

- **(A)** $\dfrac{1}{2}$
- **(B)** $\dfrac{1}{3}$
- **(C)** $\dfrac{1}{4}$
- **(D)** $\dfrac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{4}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, the total probability must be $1$.

$\int_{-\infty}^{\infty} f(x) dx = 1$

$\int_{0}^{1} kx dx + \int_{1}^{2} k dx + \int_{2}^{3} (-kx + 3k) dx = 1$

$k \left[ \dfrac{x^2}{2} \right]_0^1 + k [x]_1^2 + k \left[ -\dfrac{x^2}{2} + 3x \right]_2^3 = 1$

$\dfrac{k}{2} + k(2 - 1) + k \left( \left(-\dfrac{9}{2} + 9\right) - \left(-\dfrac{4}{2} + 6\right) \right) = 1$

$\dfrac{k}{2} + k + k \left( \dfrac{9}{2} - 4 \right) = 1$

$\dfrac{k}{2} + k + \dfrac{k}{2} = 1$

$2k = 1 \Rightarrow k = \dfrac{1}{2}$

Now, we need to find $P(2 < X \leq 3)$:

$P(2 < X \leq 3) = \int_{2}^{3} f(x) dx = \int_{2}^{3} (-kx + 3k) dx$

$P(2 < X \leq 3) = k \left[ -\dfrac{x^2}{2} + 3x \right]_2^3 = \dfrac{k}{2}$

Substituting $k = \dfrac{1}{2}$, we get:

$P(2 < X \leq 3) = \dfrac{1}{4}$

Answer: $\dfrac{1}{4}$

</details>

---

### Q13. MHT CET 2026 (19 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn at random from a box which contains 5 cards numbered 1, 1, 2, 2 & 3. If X denotes the sum of the numbers, then the expected value of X is...

**Options:**

- **(A)** $2.6$
- **(B)** $3.8$
- **(C)** $3.2$
- **(D)** $3.6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3.6$**

**Detailed Solution:**

Total number of ways to draw 2 cards from 5 cards is $^{5}C_{2} = 10$.

Let $X$ be the sum of the numbers on the two drawn cards. The possible values of $X$ are $2, 3, 4, 5$.

The probabilities for each sum are:

$P(X = 2) = \dfrac{^{2}C_{2}}{10} = \dfrac{1}{10}$

$P(X = 3) = \dfrac{^{2}C_{1} \times ^{2}C_{1}}{10} = \dfrac{4}{10}$

$P(X = 4) = \dfrac{^{2}C_{1} \times ^{1}C_{1} + ^{2}C_{2}}{10} = \dfrac{3}{10}$

$P(X = 5) = \dfrac{^{2}C_{1} \times ^{1}C_{1}}{10} = \dfrac{2}{10}$

The expected value $E(X)$ is given by $\sum X P(X)$:

$E(X) = 2 \times \dfrac{1}{10} + 3 \times \dfrac{4}{10} + 4 \times \dfrac{3}{10} + 5 \times \dfrac{2}{10}$

$E(X) = \dfrac{2 + 12 + 12 + 10}{10} = \dfrac{36}{10} = 3.6$

Answer: $3.6$

</details>

---

### Q14. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Given the probability density function (p.d.f.) of the random variable X, $f(x) = \dfrac{1}{2a}$, $0 < x < 2a$, $a > 0$
$= 0$, otherwise, then which of the following is correct ?

**Options:**

- **(A)** $P\left(X < \dfrac{a}{2}\right) = P\left(X > \dfrac{a}{2}\right)$
- **(B)** $P\left(X < \dfrac{a}{2}\right) < P\left(X > \dfrac{3a}{2}\right)$
- **(C)** $P\left(X < \dfrac{a}{2}\right) > P\left(X > \dfrac{3a}{2}\right)$
- **(D)** $P\left(X < \dfrac{a}{2}\right) = P\left(X > \dfrac{3a}{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $P\left(X < \dfrac{a}{2}\right) = P\left(X > \dfrac{3a}{2}\right)$**

**Detailed Solution:**

The given probability density function is $f(x) = \dfrac{1}{2a}$ for $0 < x < 2a$, and $0$ otherwise.

We calculate the probability $P\left(X < \dfrac{a}{2}\right)$:

$P\left(X < \dfrac{a}{2}\right) = \int_{0}^{\dfrac{a}{2}} f(x) dx = \int_{0}^{\dfrac{a}{2}} \dfrac{1}{2a} dx = \dfrac{1}{2a} [x]_{0}^{\dfrac{a}{2}} = \dfrac{1}{2a} \left(\dfrac{a}{2} - 0\right) = \dfrac{1}{4}$

Next, we calculate the probability $P\left(X > \dfrac{3a}{2}\right)$:

$P\left(X > \dfrac{3a}{2}\right) = \int_{\dfrac{3a}{2}}^{2a} f(x) dx = \int_{\dfrac{3a}{2}}^{2a} \dfrac{1}{2a} dx = \dfrac{1}{2a} [x]_{\dfrac{3a}{2}}^{2a} = \dfrac{1}{2a} \left(2a - \dfrac{3a}{2}\right) = \dfrac{1}{2a} \left(\dfrac{a}{2}\right) = \dfrac{1}{4}$

Comparing the two probabilities, we get:

$P\left(X < \dfrac{a}{2}\right) = P\left(X > \dfrac{3a}{2}\right) = \dfrac{1}{4}$

Answer: $P\left(X < \dfrac{a}{2}\right) = P\left(X > \dfrac{3a}{2}\right)$

</details>

---

### Q15. MHT CET 2026 (19 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Consider a game of tossing a six sided fair die. If the face that comes up is $6$, the player wins Rs. $36$ and he loses Rs. $k^2$, where $k$ is the face that comes up $k = \{1, 2, 3, 4, 5\}$, then the expected winning amount in this game in Rs. is...

**Options:**

- **(A)** $\dfrac{19}{6}$
- **(B)** $-\dfrac{19}{6}$
- **(C)** $\dfrac{3}{2}$
- **(D)** $-\dfrac{3}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\dfrac{19}{6}$**

**Detailed Solution:**

Let $X$ be the random variable representing the winning amount.

The possible values of $X$ corresponding to the outcomes $1, 2, 3, 4, 5, 6$ on the die are $-1^2, -2^2, -3^2, -4^2, -5^2, 36$ respectively, which simplifies to $-1, -4, -9, -16, -25, 36$.

Since the die is fair, the probability of each outcome is $\dfrac{1}{6}$.

The expected winning amount is given by $E(X) = \sum x_i P(x_i)$.

$E(X) = \dfrac{1}{6}(-1) + \dfrac{1}{6}(-4) + \dfrac{1}{6}(-9) + \dfrac{1}{6}(-16) + \dfrac{1}{6}(-25) + \dfrac{1}{6}(36)$

$E(X) = \dfrac{1}{6}(-1 - 4 - 9 - 16 - 25 + 36)$

$E(X) = \dfrac{1}{6}(-55 + 36)$

$E(X) = -\dfrac{19}{6}$

Answer: $-\dfrac{19}{6}$

</details>

---

### Q16. MHT CET 2026 (18 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the p. d. f. of a continuous random variable X is given by $f(x) = \begin{cases} k(9 + 8x - x^2), & \text{for } -1 \leq x \leq 4 \\ 0, & \text{otherwise} \end{cases}$ then the value of $k$ is $\ldots$

**Options:**

- **(A)** $\dfrac{1}{125}$
- **(B)** $\dfrac{3}{250}$
- **(C)** $\dfrac{3}{125}$
- **(D)** $\dfrac{1}{250}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{3}{250}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, the total probability must be $1$.

$\int_{-\infty}^{\infty} f(x) dx = 1$

$\int_{-1}^{4} k(9 + 8x - x^2) dx = 1$

$k \left[ 9x + 4x^2 - \dfrac{x^3}{3} \right]_{-1}^{4} = 1$

$k \left( \left( 9(4) + 4(4)^2 - \dfrac{4^3}{3} \right) - \left( 9(-1) + 4(-1)^2 - \dfrac{(-1)^3}{3} \right) \right) = 1$

$k \left( \left( 36 + 64 - \dfrac{64}{3} \right) - \left( -9 + 4 + \dfrac{1}{3} \right) \right) = 1$

$k \left( \left( 100 - \dfrac{64}{3} \right) - \left( -5 + \dfrac{1}{3} \right) \right) = 1$

$k \left( \dfrac{236}{3} - \left( -\dfrac{14}{3} \right) \right) = 1$

$k \left( \dfrac{250}{3} \right) = 1$

$k = \dfrac{3}{250}$

Answer: $\dfrac{3}{250}$

</details>

---

### Q17. MHT CET 2026 (18 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $F(x)$ be the cumulative distribution function (c.d.f.) of a continuous random variable $X$. If $F(b) = 0.7$ and $P(X > a) = 0.4$, then the value of $P(a < X < b)$ is ...

**Options:**

- **(A)** $0.1$
- **(B)** $0.2$
- **(C)** $0.3$
- **(D)** $0.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.1$**

**Detailed Solution:**

The cumulative distribution function $F(x)$ is defined as $F(x) = P(X \le x)$.

Given $F(b) = 0.7$, we have $P(X \le b) = 0.7$.

We are also given $P(X > a) = 0.4$.

Since $P(X \le a) + P(X > a) = 1$, we get:

$P(X \le a) = 1 - 0.4 = 0.6$

For a continuous random variable, the probability $P(a < X < b)$ is given by:

$P(a < X < b) = P(X \le b) - P(X \le a)$

Substituting the values:

$P(a < X < b) = 0.7 - 0.6 = 0.1$

Answer: $0.1$

</details>

---

### Q18. MHT CET 2026 (17 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a discrete random variable $X$ takes the values $1, 2, 3, 4$ such that $2P(X = 1) = 3P(X = 2) = P(X = 3) = 5P(X = 4)$, then $P(X = 4) = \ldots$

**Options:**

- **(A)** $\dfrac{15}{61}$
- **(B)** $\dfrac{30}{61}$
- **(C)** $\dfrac{10}{61}$
- **(D)** $\dfrac{6}{61}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{6}{61}$**

**Detailed Solution:**

Let $P(X = 4) = k$.

From the given relation $2P(X = 1) = 3P(X = 2) = P(X = 3) = 5P(X = 4)$, we have:

$P(X = 3) = 5k$

$P(X = 2) = \dfrac{5k}{3}$

$P(X = 1) = \dfrac{5k}{2}$

Since the sum of all probabilities for a discrete random variable is $1$:

$P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) = 1$

$\dfrac{5k}{2} + \dfrac{5k}{3} + 5k + k = 1$

$k \left( \dfrac{15}{6} + \dfrac{10}{6} + \dfrac{30}{6} + \dfrac{6}{6} \right) = 1$

$k \left( \dfrac{61}{6} \right) = 1$

$k = \dfrac{6}{61}$

Therefore, $P(X = 4) = \dfrac{6}{61}$.

Answer: $\dfrac{6}{61}$

</details>

---

### Q19. MHT CET 2026 (17 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A box contains 8 red and N green balls. Two balls are drawn at random from it. If X is the random variable representing the number of green balls drawn and $E(X) = 1.2$, then $N = \ldots$

**Options:**

- **(A)** $4$
- **(B)** $8$
- **(C)** $12$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $12$**

**Detailed Solution:**

Total number of balls $= N + 8$

Two balls are drawn at random. Let $X$ be the number of green balls drawn. The possible values of $X$ are $0, 1, 2$.

$P(X=1) = \dfrac{^{N}C_{1} \times ^{8}C_{1}}{^{N+8}C_{2}} = \dfrac{16N}{(N+8)(N+7)}$

$P(X=2) = \dfrac{^{N}C_{2}}{^{N+8}C_{2}} = \dfrac{N(N-1)}{(N+8)(N+7)}$

The expected value $E(X)$ is given by:

$E(X) = 1 \times P(X=1) + 2 \times P(X=2)$

$E(X) = \dfrac{16N + 2N(N-1)}{(N+8)(N+7)} = \dfrac{2N(N+7)}{(N+8)(N+7)} = \dfrac{2N}{N+8}$

Given $E(X) = 1.2$, we have:

$\dfrac{2N}{N+8} = 1.2$

$2N = 1.2N + 9.6$

$0.8N = 9.6$

$N = 12$

Answer: $12$

</details>

---

### Q20. MHT CET 2026 (16 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $X$ has a probability mass function $P(x) = \begin{cases} kx^2, & \text{for } x = 1, 2, 3, 4 \\ 0, & \text{otherwise} \end{cases}$, then the mean of $X$ is ...

**Options:**

- **(A)** $3.232$
- **(B)** $2.221$
- **(C)** $3.333$
- **(D)** $2.222$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3.333$**

**Detailed Solution:**

The sum of all probabilities must be equal to $1$.

$\sum_{x=1}^{4} P(x) = 1$

$k(1^2 + 2^2 + 3^2 + 4^2) = 1$

$k(1 + 4 + 9 + 16) = 1$

$30k = 1 \Rightarrow k = \dfrac{1}{30}$

The mean of the random variable $X$ is given by $E(X) = \sum_{x=1}^{4} x P(x)$.

$E(X) = \sum_{x=1}^{4} x(kx^2) = k \sum_{x=1}^{4} x^3$

$E(X) = \dfrac{1}{30} (1^3 + 2^3 + 3^3 + 4^3)$

$E(X) = \dfrac{1}{30} (1 + 8 + 27 + 64)$

$E(X) = \dfrac{100}{30} = \dfrac{10}{3} = 3.333$

Answer: $3.333$

</details>

---

### Q21. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable X has the probability distribution
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td><td style="border: 1px solid black; padding: 10px;">$5$</td><td style="border: 1px solid black; padding: 10px;">$6$</td><td style="border: 1px solid black; padding: 10px;">$7$</td><td style="border: 1px solid black; padding: 10px;">$8$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$0.23$</td><td style="border: 1px solid black; padding: 10px;">$0.15$</td><td style="border: 1px solid black; padding: 10px;">$0.12$</td><td style="border: 1px solid black; padding: 10px;">$0.10$</td><td style="border: 1px solid black; padding: 10px;">$0.20$</td><td style="border: 1px solid black; padding: 10px;">$0.07$</td><td style="border: 1px solid black; padding: 10px;">$0.08$</td><td style="border: 1px solid black; padding: 10px;">$0.05$</td></tr></table>
for the events E = {X is a prime number} and F = {X $\leq$ 3}, then P (E$\cup$F)=

**Options:**

- **(A)** $0.55$
- **(B)** $0.70$
- **(C)** $0.87$
- **(D)** $0.78$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.78$**

**Detailed Solution:**

The event $E$ is that $X$ is a prime number. From the given values, the prime numbers are $2, 3, 5, 7$.

$E = \{2, 3, 5, 7\}$

The event $F$ is that $X \leq 3$. From the given values, the numbers less than or equal to $3$ are $1, 2, 3$.

$F = \{1, 2, 3\}$

The union of events $E$ and $F$ is:

$E \cup F = \{1, 2, 3, 5, 7\}$

The probability $P(E \cup F)$ is the sum of the probabilities of these individual outcomes:

$P(E \cup F) = P(X=1) + P(X=2) + P(X=3) + P(X=5) + P(X=7)$

Substituting the values from the probability distribution table:

$P(E \cup F) = 0.23 + 0.15 + 0.12 + 0.20 + 0.08$

$P(E \cup F) = 0.78$

Answer: $0.78$

</details>

---

### Q22. MHT CET 2026 (16 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The probability distribution of a random variable X is given by
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$k$</td><td style="border: 1px solid black; padding: 10px;">$2k$</td><td style="border: 1px solid black; padding: 10px;">$3k$</td><td style="border: 1px solid black; padding: 10px;">$4k$</td></tr></table>
Then the c.d.f. of X is given by

**Options:**

- **(A)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{6}{10}$</td><td style="border: 1px solid black; padding: 10px;">$1$</td></tr></table>
- **(B)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{6}{10}$</td><td style="border: 1px solid black; padding: 10px;">$1$</td></tr></table>
- **(C)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{5}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td></tr></table>
- **(D)** <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{6}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$1$</td></tr></table>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{6}{10}$</td><td style="border: 1px solid black; padding: 10px;">$1$</td></tr></table>**

**Detailed Solution:**

Since the sum of all probabilities in a probability distribution is $1$, we have:

$\sum P(X=x) = 1$

$k + 2k + 3k + 4k = 1$

$10k = 1 \Rightarrow k = \dfrac{1}{10}$

The probabilities are:
$P(X=1) = \dfrac{1}{10}$
$P(X=2) = \dfrac{2}{10}$
$P(X=3) = \dfrac{3}{10}$
$P(X=4) = \dfrac{4}{10}$

The cumulative distribution function (c.d.f.) $F(x)$ is given by $F(x) = P(X \le x)$.

$F(1) = P(X \le 1) = P(X=1) = \dfrac{1}{10}$

$F(2) = P(X \le 2) = P(X=1) + P(X=2) = \dfrac{1}{10} + \dfrac{2}{10} = \dfrac{3}{10}$

$F(3) = P(X \le 3) = F(2) + P(X=3) = \dfrac{3}{10} + \dfrac{3}{10} = \dfrac{6}{10}$

$F(4) = P(X \le 4) = F(3) + P(X=4) = \dfrac{6}{10} + \dfrac{4}{10} = 1$

Answer: <table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$F(X = x)$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{1}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{3}{10}$</td><td style="border: 1px solid black; padding: 10px;">$\dfrac{6}{10}$</td><td style="border: 1px solid black; padding: 10px;">$1$</td></tr></table>

</details>

---

### Q23. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the following probability distribution, the standard deviation of the random variable X is
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">X</td><td style="border: 1px solid black; padding: 10px;">2</td><td style="border: 1px solid black; padding: 10px;">3</td><td style="border: 1px solid black; padding: 10px;">4</td></tr><tr><td style="border: 1px solid black; padding: 10px;">p(X=$x$)</td><td style="border: 1px solid black; padding: 10px;">0.2</td><td style="border: 1px solid black; padding: 10px;">0.5</td><td style="border: 1px solid black; padding: 10px;">0.3</td></tr></table>

**Options:**

- **(A)** $0.5$
- **(B)** $0.6$
- **(C)** $0.61$
- **(D)** $0.7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.7$**

**Detailed Solution:**

$E(X) = \sum x_i p_i = 2(0.2) + 3(0.5) + 4(0.3)$

$E(X) = 0.4 + 1.5 + 1.2 = 3.1$

$E(X^2) = \sum x_i^2 p_i = 4(0.2) + 9(0.5) + 16(0.3)$

$E(X^2) = 0.8 + 4.5 + 4.8 = 10.1$

$\text{Var}(X) = E(X^2) - (E(X))^2$

$\text{Var}(X) = 10.1 - (3.1)^2 = 10.1 - 9.61 = 0.49$

$\text{Standard deviation} = \sqrt{\text{Var}(X)} = \sqrt{0.49} = 0.7$

Answer: $0.7$

</details>

---

### Q24. MHT CET 2026 (15 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X has the following probability distribution
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">X</td><td style="border: 1px solid black; padding: 10px;">1</td><td style="border: 1px solid black; padding: 10px;">2</td><td style="border: 1px solid black; padding: 10px;">3</td><td style="border: 1px solid black; padding: 10px;">4</td><td style="border: 1px solid black; padding: 10px;">5</td><td style="border: 1px solid black; padding: 10px;">6</td><td style="border: 1px solid black; padding: 10px;">7</td><td style="border: 1px solid black; padding: 10px;">8</td></tr><tr><td style="border: 1px solid black; padding: 10px;">P(X=$x$)</td><td style="border: 1px solid black; padding: 10px;">0.15</td><td style="border: 1px solid black; padding: 10px;">0.23</td><td style="border: 1px solid black; padding: 10px;">0.12</td><td style="border: 1px solid black; padding: 10px;">0.10</td><td style="border: 1px solid black; padding: 10px;">0.20</td><td style="border: 1px solid black; padding: 10px;">0.08</td><td style="border: 1px solid black; padding: 10px;">0.07</td><td style="border: 1px solid black; padding: 10px;">0.05</td></tr></table>
For the event E = { X is a prime number } and F = { X &lt; 4 }, P(E$\cup$F) =

**Options:**

- **(A)** $0.87$
- **(B)** $0.77$
- **(C)** $0.35$
- **(D)** $0.50$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.77$**

**Detailed Solution:**

Event $E = \{X \text{ is a prime number}\} = \{2, 3, 5, 7\}$

Event $F = \{X < 4\} = \{1, 2, 3\}$

The union of the two events is $E \cup F = \{1, 2, 3, 5, 7\}$

The probability of $E \cup F$ is the sum of the probabilities of these individual outcomes:

$P(E \cup F) = P(X=1) + P(X=2) + P(X=3) + P(X=5) + P(X=7)$

Substituting the values from the given probability distribution:

$P(E \cup F) = 0.15 + 0.23 + 0.12 + 0.20 + 0.07 = 0.77$

Answer: $0.77$

</details>

---

### Q25. MHT CET 2026 (15 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The Variance of the following probability distribution of X is
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 10px;">X</th><th style="border: 1px solid black; padding: 10px;">$0$</th><th style="border: 1px solid black; padding: 10px;">$1$</th><th style="border: 1px solid black; padding: 10px;">$2$</th><th style="border: 1px solid black; padding: 10px;">$3$</th></tr><tr><td style="border: 1px solid black; padding: 10px;">P(X)</td><td style="border: 1px solid black; padding: 10px;">$q^3$</td><td style="border: 1px solid black; padding: 10px;">$3q^2 p$</td><td style="border: 1px solid black; padding: 10px;">$3qp^2$</td><td style="border: 1px solid black; padding: 10px;">$p^3$</td></tr></table>where $0 < p < 1, q = 1 - p$

**Options:**

- **(A)** $3p^2 q$
- **(B)** $3pq$
- **(C)** $3pq^2$
- **(D)** $3q$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3pq$**

**Detailed Solution:**

The given probability distribution represents a binomial distribution with parameters $n = 3$ and probability of success $p$, since $P(X = x) = ^{3}C_{x} p^x q^{3-x}$ for $x = 0, 1, 2, 3$.

For a binomial distribution, the variance is given by $npq$.

Substituting $n = 3$, the variance is $3pq$.

Alternatively, calculating the variance using expectations:

$E(X) = \sum x P(x) = 0(q^3) + 1(3q^2 p) + 2(3qp^2) + 3(p^3)$

$E(X) = 3p(q^2 + 2pq + p^2) = 3p(q+p)^2 = 3p$

$E(X^2) = \sum x^2 P(x) = 0(q^3) + 1(3q^2 p) + 4(3qp^2) + 9(p^3)$

$E(X^2) = 3p(q^2 + 4pq + 3p^2) = 3p((q+p)^2 + 2p(q+p)) = 3p(1 + 2p) = 3p + 6p^2$

$\text{Variance} = E(X^2) - (E(X))^2$

$\text{Variance} = 3p + 6p^2 - (3p)^2 = 3p - 3p^2 = 3p(1-p) = 3pq$

Answer: $3pq$

</details>

---

### Q26. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X has the following probability distribution
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 10px;">$X = x$</td><td style="border: 1px solid black; padding: 10px;">$1$</td><td style="border: 1px solid black; padding: 10px;">$2$</td><td style="border: 1px solid black; padding: 10px;">$3$</td><td style="border: 1px solid black; padding: 10px;">$4$</td><td style="border: 1px solid black; padding: 10px;">$5$</td><td style="border: 1px solid black; padding: 10px;">$6$</td><td style="border: 1px solid black; padding: 10px;">$7$</td><td style="border: 1px solid black; padding: 10px;">$8$</td></tr><tr><td style="border: 1px solid black; padding: 10px;">$P(X=x)$</td><td style="border: 1px solid black; padding: 10px;">$0.15$</td><td style="border: 1px solid black; padding: 10px;">$0.23$</td><td style="border: 1px solid black; padding: 10px;">$0.10$</td><td style="border: 1px solid black; padding: 10px;">$0.12$</td><td style="border: 1px solid black; padding: 10px;">$0.20$</td><td style="border: 1px solid black; padding: 10px;">$0.08$</td><td style="border: 1px solid black; padding: 10px;">$0.07$</td><td style="border: 1px solid black; padding: 10px;">$0.05$</td></tr></table>
For the events $E = \{X \text{ is a prime number}\}$, $F = \{X < 4\}$, $P(E \cup F)$ is

**Options:**

- **(A)** $0.5$
- **(B)** $0.77$
- **(C)** $0.35$
- **(D)** $0.75$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0.75$**

**Detailed Solution:**

The event $E$ is that $X$ is a prime number. From the given values of $X$, the prime numbers are $2, 3, 5, 7$.

$E = \{2, 3, 5, 7\}$

The event $F$ is that $X < 4$. From the given values of $X$, the numbers less than $4$ are $1, 2, 3$.

$F = \{1, 2, 3\}$

The union of events $E$ and $F$ is:

$E \cup F = \{1, 2, 3, 5, 7\}$

The probability $P(E \cup F)$ is the sum of the probabilities of these individual outcomes:

$P(E \cup F) = P(X=1) + P(X=2) + P(X=3) + P(X=5) + P(X=7)$

Substituting the given probabilities:

$P(E \cup F) = 0.15 + 0.23 + 0.10 + 0.20 + 0.07 = 0.75$

Answer: $0.75$

</details>

---

### Q27. MHT CET 2026 (13 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X takes the values 0, 1, 2, 3 and its mean is $1.3$. If $P(X=3) = 2P(X=1)$ and $P(X=2) = 0.3$, then $P(X=0)$ is

**Options:**

- **(A)** $0.3$
- **(B)** $0.4$
- **(C)** $0.2$
- **(D)** $0.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.4$**

**Detailed Solution:**

Let $P(X=1) = p$ and $P(X=0) = q$.

Given $P(X=3) = 2P(X=1) = 2p$ and $P(X=2) = 0.3$.

The sum of all probabilities is $1$:

$P(X=0) + P(X=1) + P(X=2) + P(X=3) = 1$

$q + p + 0.3 + 2p = 1$

$q + 3p = 0.7$

The mean of the random variable is given as $1.3$:

$\sum x_i P(x_i) = 1.3$

$0(q) + 1(p) + 2(0.3) + 3(2p) = 1.3$

$p + 0.6 + 6p = 1.3$

$7p = 0.7 \Rightarrow p = 0.1$

Substituting the value of $p$ in the first equation:

$q + 3(0.1) = 0.7$

$q = 0.4$

Thus, $P(X=0) = 0.4$.

Answer: $0.4$

</details>

---

### Q28. MHT CET 2026 (11 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A player tosses two fair coins, he wins Rs. $5$ if two heads appear, Rs. $3$ if one head appears and Rs. $2$ if no head appears, then the variance of the winning amount is

**Options:**

- **(A)** $1.1875$
- **(B)** $1.8175$
- **(C)** $1.1785$
- **(D)** $1.8157$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1.1875$**

**Detailed Solution:**

Let $X$ be the random variable denoting the winning amount.

The possible outcomes for the number of heads when tossing two fair coins are $0, 1,$ and $2$.

The probabilities and corresponding winning amounts are:
$P(X = 5) = P(2 \text{ heads}) = \dfrac{1}{4}$
$P(X = 3) = P(1 \text{ head}) = \dfrac{1}{2}$
$P(X = 2) = P(0 \text{ heads}) = \dfrac{1}{4}$

The expected value $E(X)$ is given by:
$E(X) = \sum X P(X) = 5 \times \dfrac{1}{4} + 3 \times \dfrac{1}{2} + 2 \times \dfrac{1}{4} = \dfrac{5}{4} + \dfrac{6}{4} + \dfrac{2}{4} = \dfrac{13}{4}$

The expected value of $X^2$, $E(X^2)$ is:
$E(X^2) = \sum X^2 P(X) = 25 \times \dfrac{1}{4} + 9 \times \dfrac{1}{2} + 4 \times \dfrac{1}{4} = \dfrac{25}{4} + \dfrac{18}{4} + \dfrac{4}{4} = \dfrac{47}{4}$

The variance of $X$ is:
$\text{Var}(X) = E(X^2) - [E(X)]^2 = \dfrac{47}{4} - \left(\dfrac{13}{4}\right)^2$

$\text{Var}(X) = \dfrac{47}{4} - \dfrac{169}{16} = \dfrac{188 - 169}{16} = \dfrac{19}{16} = 1.1875$

Answer: $1.1875$

</details>

---

### Q29. MHT CET 2026 (11 April Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the following function is probability density function of r.v. X
$f(x) = kx^2(1-x)$, for $0 < x < 1 = 0$, otherwise, then the value of $k$ is

**Options:**

- **(A)** $-12$
- **(B)** $\dfrac{1}{12}$
- **(C)** $\dfrac{1}{6}$
- **(D)** $12$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $12$**

**Detailed Solution:**

For a function to be a probability density function, the total probability over its entire domain must be $1$.

$\int_{-\infty}^{\infty} f(x) dx = 1$

$\int_{0}^{1} kx^2(1-x) dx = 1$

$k \int_{0}^{1} (x^2 - x^3) dx = 1$

$k \left[ \dfrac{x^3}{3} - \dfrac{x^4}{4} \right]_{0}^{1} = 1$

$k \left( \dfrac{1}{3} - \dfrac{1}{4} \right) = 1$

$k \left( \dfrac{4 - 3}{12} \right) = 1$

$k \left( \dfrac{1}{12} \right) = 1$

$k = 12$

Answer: $12$

</details>

---

### Q30. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A student studies for X number of hours during a randomly selected school day. The probability that X can take the values, has the following form, where k is some constant.
$P(X=x)= \begin{cases}0.2, & \text { if } x=0 \\ k x, & \text { if } x=1 \text { or } 2 \\ k(6-x), & \text { if } x=3 \text { or } 4 \\ 0, & \text { otherwise }\end{cases}$

The probability that the student studies for at most two hours is

**Options:**

- **(A)** 0.1
- **(B)** 0.5
- **(C)** 0.3
- **(D)** 0.7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.5**

**Detailed Solution:**

The sum of probabilities of all possible values of $X$ is $1$.

$\sum P(X=x) = 1$

$P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) = 1$

$0.2 + k(1) + k(2) + k(6-3) + k(6-4) = 1$

$0.2 + k + 2k + 3k + 2k = 1$

$0.2 + 8k = 1$

$8k = 0.8$

$k = 0.1$

The probability that the student studies for at most two hours is $P(X \le 2)$.

$P(X \le 2) = P(X=0) + P(X=1) + P(X=2)$

$P(X \le 2) = 0.2 + k + 2k$

$P(X \le 2) = 0.2 + 3k$

Substituting $k = 0.1$:

$P(X \le 2) = 0.2 + 3(0.1) = 0.5$

Answer: 0.5

</details>

---

### Q31. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X \sim B(35, p)$ such that $7 P(X=0)=P(X=1)$ then the value of $\frac{\mathrm{P}(\mathrm{X}=15)}{\mathrm{P}(\mathrm{X}=20)}$ is equal to

**Options:**

- **(A)** $\frac{3125}{7776}$
- **(B)** 3125
- **(C)** 7776
- **(D)** $\frac{625}{1296}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3125**

**Detailed Solution:**

Given $X \sim B(n, p)$ with $n = 35$.

The probability mass function of a binomial distribution is given by:
$P(X=x) = ^{n}C_{x} p^x q^{n-x}$

We are given the condition:
$7 P(X=0) = P(X=1)$

Substituting the formula for $x=0$ and $x=1$:
$7 \times ^{35}C_{0} p^0 q^{35} = ^{35}C_{1} p^1 q^{34}$

$7 q^{35} = 35 p q^{34}$

Dividing both sides by $7 q^{34}$:
$q = 5p$

Since $p + q = 1$, we have:
$p + 5p = 1 \Rightarrow 6p = 1 \Rightarrow p = \dfrac{1}{6}$ and $q = \dfrac{5}{6}$

We need to find the value of $\dfrac{P(X=15)}{P(X=20)}$:
$\dfrac{P(X=15)}{P(X=20)} = \dfrac{^{35}C_{15} p^{15} q^{20}}{^{35}C_{20} p^{20} q^{15}}$

Using the property $^{n}C_{r} = ^{n}C_{n-r}$, we know that $^{35}C_{15} = ^{35}C_{20}$. Thus, the combination terms cancel out:
$\dfrac{P(X=15)}{P(X=20)} = \dfrac{q^{20-15}}{p^{20-15}} = \dfrac{q^5}{p^5} = \left(\dfrac{q}{p}\right)^5$

Substituting $q = 5p$:
$\left(\dfrac{5p}{p}\right)^5 = 5^5 = 3125$

Answer: 3125

</details>

---

### Q32. MHT CET 2025 (5 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn successively with replacement from fair playing 52 cards. let X denote number of kings obtained when two cards are drawn, then $\mathrm{E}\left(\mathrm{X}^2\right)=$

**Options:**

- **(A)** $\frac{24}{169}$
- **(B)** $\frac{26}{169}$
- **(C)** $\frac{27}{169}$
- **(D)** $\frac{28}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{28}{169}$**

**Detailed Solution:**

Let $X$ be the number of kings obtained in two draws.

Since the cards are drawn with replacement, $X$ follows a binomial distribution with $n = 2$.

The probability of drawing a king in a single draw is $p = \dfrac{4}{52} = \dfrac{1}{13}$.

The probability of not drawing a king is $q = 1 - p = \dfrac{12}{13}$.

The probability distribution of $X$ is given by $P(X = x) = ^{n}C_{x} p^x q^{n-x}$:

$P(X = 0) = ^{2}C_{0} \left(\dfrac{1}{13}\right)^0 \left(\dfrac{12}{13}\right)^2 = \dfrac{144}{169}$

$P(X = 1) = ^{2}C_{1} \left(\dfrac{1}{13}\right)^1 \left(\dfrac{12}{13}\right)^1 = \dfrac{24}{169}$

$P(X = 2) = ^{2}C_{2} \left(\dfrac{1}{13}\right)^2 \left(\dfrac{12}{13}\right)^0 = \dfrac{1}{169}$

The expected value $E(X^2)$ is calculated as:

$E(X^2) = \sum x^2 P(X = x)$

$E(X^2) = 0^2 \times \dfrac{144}{169} + 1^2 \times \dfrac{24}{169} + 2^2 \times \dfrac{1}{169}$

$E(X^2) = 0 + \dfrac{24}{169} + \dfrac{4}{169} = \dfrac{28}{169}$

Alternatively, using the properties of binomial distribution:

$E(X^2) = \text{Var}(X) + [E(X)]^2 = npq + (np)^2$

$E(X^2) = 2 \times \dfrac{1}{13} \times \dfrac{12}{13} + \left(2 \times \dfrac{1}{13}\right)^2 = \dfrac{24}{169} + \dfrac{4}{169} = \dfrac{28}{169}$

Answer: $\frac{28}{169}$

</details>

---

### Q33. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a meeting $70 \%$ of the members favour and $30 \%$ oppose a certain proposal. A member is selected at random. We take $\mathrm{X}=0$ if he opposed the proposal and we take $\mathrm{X}=1$, if the member is in favour. Then variance of $X$ is

**Options:**

- **(A)** $\frac{21}{100}$
- **(B)** $\frac{5}{17}$
- **(C)** $\frac{2}{15}$
- **(D)** $\frac{23}{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{21}{100}$**

**Detailed Solution:**

Let $X$ be the random variable representing the member's opinion.

Given that $70 \%$ of the members favour the proposal, $P(X=1) = \dfrac{70}{100} = \dfrac{7}{10}$.

Given that $30 \%$ of the members oppose the proposal, $P(X=0) = \dfrac{30}{100} = \dfrac{3}{10}$.

The expected value of $X$ is:
$E(X) = \sum X P(X) = 1 \times \dfrac{7}{10} + 0 \times \dfrac{3}{10} = \dfrac{7}{10}$

The expected value of $X^2$ is:
$E(X^2) = \sum X^2 P(X) = 1^2 \times \dfrac{7}{10} + 0^2 \times \dfrac{3}{10} = \dfrac{7}{10}$

The variance of $X$ is given by:
$Var(X) = E(X^2) - (E(X))^2$

$Var(X) = \dfrac{7}{10} - \left(\dfrac{7}{10}\right)^2$

$Var(X) = \dfrac{7}{10} - \dfrac{49}{100} = \dfrac{70 - 49}{100} = \dfrac{21}{100}$

Answer: $\frac{21}{100}$

</details>

---

### Q34. MHT CET 2025 (27 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the following probability distribution, the standard deviation of the random variable X is
\(\begin{array}{|c|c|c|c|} \hline \mathbf{X} & \mathbf{2} & \mathbf{3} & \mathbf{4} \\ \hline \mathrm{P}(\mathrm{X}=\mathrm{x}) & 0.2 & 0.5 & 0.3 \\ \hline \end{array}\)

**Options:**

- **(A)** $0.7$
- **(B)** $0.49$
- **(C)** $3.1$
- **(D)** $0.07$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.7$**

**Detailed Solution:**

The expected value (mean) of $X$ is given by:

$E(X) = \sum x_i P(x_i) = 2(0.2) + 3(0.5) + 4(0.3)$

$E(X) = 0.4 + 1.5 + 1.2 = 3.1$

The expected value of $X^2$ is given by:

$E(X^2) = \sum x_i^2 P(x_i) = 2^2(0.2) + 3^2(0.5) + 4^2(0.3)$

$E(X^2) = 4(0.2) + 9(0.5) + 16(0.3)$

$E(X^2) = 0.8 + 4.5 + 4.8 = 10.1$

The variance of $X$ is:

$Var(X) = E(X^2) - [E(X)]^2$

$Var(X) = 10.1 - (3.1)^2$

$Var(X) = 10.1 - 9.61 = 0.49$

The standard deviation of $X$ is:

$\sigma = \sqrt{Var(X)} = \sqrt{0.49} = 0.7$

Answer: $0.7$

</details>

---

### Q35. MHT CET 2025 (26 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X has the following probability distribution :
\(\begin{array}{|c|c|c|c|c|} \hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\ \hline \mathrm{P}(\mathrm{X}=x) & 0.1 & 0.2 & 0.3 & 0.4 \\ \hline \end{array}\)
The mean and standard deviation of X are respectively

**Options:**

- **(A)** 2 and 3
- **(B)** 3 and 1
- **(C)** 3 and $\sqrt{2}$
- **(D)** 2 and 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3 and 1**

**Detailed Solution:**

The mean of the random variable $X$ is given by $E(X) = \sum x_i P(x_i)$.

$E(X) = 1(0.1) + 2(0.2) + 3(0.3) + 4(0.4)$

$E(X) = 0.1 + 0.4 + 0.9 + 1.6 = 3$

The variance of $X$ is given by $Var(X) = E(X^2) - (E(X))^2$.

$E(X^2) = \sum x_i^2 P(x_i)$

$E(X^2) = 1^2(0.1) + 2^2(0.2) + 3^2(0.3) + 4^2(0.4)$

$E(X^2) = 0.1 + 0.8 + 2.7 + 6.4 = 10$

$Var(X) = 10 - (3)^2 = 10 - 9 = 1$

The standard deviation is $\sigma = \sqrt{Var(X)} = \sqrt{1} = 1$.

The mean and standard deviation are $3$ and $1$ respectively.

Answer: 3 and 1

</details>

---

### Q36. MHT CET 2025 (26 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The following is p.d.f. of continuous random variable X $\mathrm{f}(x)= \begin{cases}\frac{x}{8} & , \text { if } 0 < x < 4 \\ 0 & , \text { otherwise }\end{cases}$
Then $F(0.5), F(1.7)$ and $F(5)$ is respectively

**Options:**

- **(A)** $\frac{1}{64}, 1,0.18$
- **(B)** $0.0156,0.18,1$
- **(C)** $0.18,0.0156,1$
- **(D)** $1,0.0156,0.18$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.0156,0.18,1$**

**Detailed Solution:**

The cumulative distribution function $F(x)$ is given by $F(x) = \int_{-\infty}^{x} f(t) dt$.

For $0 < x < 4$, $F(x) = \int_{0}^{x} \dfrac{t}{8} dt = \left[ \dfrac{t^2}{16} \right]_{0}^{x} = \dfrac{x^2}{16}$.

For $x \ge 4$, $F(x) = \int_{0}^{4} \dfrac{t}{8} dt = \left[ \dfrac{t^2}{16} \right]_{0}^{4} = 1$.

Calculating the required values:

$F(0.5) = \dfrac{(0.5)^2}{16} = \dfrac{0.25}{16} = \dfrac{1}{64} = 0.015625 \approx 0.0156$

$F(1.7) = \dfrac{(1.7)^2}{16} = \dfrac{2.89}{16} = 0.180625 \approx 0.18$

$F(5) = 1$ since $5 \ge 4$.

The values are $0.0156, 0.18, 1$ respectively.

Answer: $0.0156,0.18,1$

</details>

---

### Q37. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider the probability distribution
\(\begin{array}{|r|c|c|c|c|c|} \hline \mathrm{X}=x & 1 & 2 & 3 & 4 & 5 \\ \hline \mathrm{P}(\mathrm{X}=x) & \mathrm{K} & 2 \mathrm{K} & \mathrm{K}^2 & 2 \mathrm{K} & 5 \mathrm{K}^2 \\ \hline \end{array}\)
Then the value of $\mathrm{P}(\mathrm{X} > 2)$ is

**Options:**

- **(A)** $\frac{7}{12}$
- **(B)** $\frac{1}{36}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{23}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is $1$.

$\sum P(X=x) = 1$

$K + 2K + K^2 + 2K + 5K^2 = 1$

$6K^2 + 5K - 1 = 0$

$(6K - 1)(K + 1) = 0$

$K = \dfrac{1}{6}$ or $K = -1$

Since probability cannot be negative, $K = \dfrac{1}{6}$.

We need to find $P(X > 2)$:

$P(X > 2) = P(X=3) + P(X=4) + P(X=5)$

$P(X > 2) = K^2 + 2K + 5K^2 = 6K^2 + 2K$

Substituting $K = \dfrac{1}{6}$:

$P(X > 2) = 6\left(\dfrac{1}{6}\right)^2 + 2\left(\dfrac{1}{6}\right)$

$P(X > 2) = \dfrac{6}{36} + \dfrac{2}{6} = \dfrac{1}{6} + \dfrac{2}{6} = \dfrac{3}{6} = \dfrac{1}{2}$

Answer: $\frac{1}{2}$

</details>

---

### Q38. MHT CET 2025 (25 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A player tosses two coins. He wins Rs. 10, if 2 heads appears, Rs. 5, if one head appear and Rs. 2 if no head appears. Then variance of winning amount is

**Options:**

- **(A)** 38.5
- **(B)** 5.5
- **(C)** 8.25
- **(D)** 44.00

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8.25**

**Detailed Solution:**

Let $X$ be the winning amount. The possible outcomes for the number of heads when two coins are tossed are $0, 1, 2$.

The probabilities are:
$P(0 \text{ heads}) = \dfrac{1}{4}$
$P(1 \text{ head}) = \dfrac{1}{2}$
$P(2 \text{ heads}) = \dfrac{1}{4}$

The corresponding winning amounts are:
$X = 2$ for $0$ heads
$X = 5$ for $1$ head
$X = 10$ for $2$ heads

The expected value $E(X)$ is:
$E(X) = \sum X P(X) = 2 \times \dfrac{1}{4} + 5 \times \dfrac{1}{2} + 10 \times \dfrac{1}{4}$
$E(X) = 0.5 + 2.5 + 2.5 = 5.5$

The expected value of $X^2$ is:
$E(X^2) = \sum X^2 P(X) = 2^2 \times \dfrac{1}{4} + 5^2 \times \dfrac{1}{2} + 10^2 \times \dfrac{1}{4}$
$E(X^2) = 1 + 12.5 + 25 = 38.5$

The variance of $X$ is:
$Var(X) = E(X^2) - [E(X)]^2$
$Var(X) = 38.5 - (5.5)^2$
$Var(X) = 38.5 - 30.25 = 8.25$

Answer: 8.25

</details>

---

### Q39. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $X$ has the following probability distribution of $X$
\(\begin{array}{|l|c|c|c|c|c|c|c|c|} \hline \mathrm{X}=x & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\ \hline \mathrm{P}(\mathrm{X}=x) & 0 & \mathrm{k} & 2 \mathrm{k} & 2 \mathrm{k} & 3 \mathrm{k} & \mathrm{k}^2 & 2 \mathrm{k}^2 & 7 \mathrm{k}^2+\mathrm{k} \\ \hline \end{array}\)
Then $\mathrm{P}(\mathrm{X} \geqslant 6)=$

**Options:**

- **(A)** $\frac{19}{100}$
- **(B)** $\frac{81}{100}$
- **(C)** $\frac{9}{100}$
- **(D)** $\frac{91}{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{19}{100}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is always $1$.

$\sum P(X=x) = 1$

$0 + k + 2k + 2k + 3k + k^2 + 2k^2 + 7k^2 + k = 1$

$10k^2 + 9k - 1 = 0$

$(10k - 1)(k + 1) = 0$

Since probability cannot be negative, $k = \dfrac{1}{10}$.

We need to find $P(X \geqslant 6)$:

$P(X \geqslant 6) = P(X = 6) + P(X = 7)$

$P(X \geqslant 6) = 2k^2 + 7k^2 + k = 9k^2 + k$

Substituting $k = \dfrac{1}{10}$:

$P(X \geqslant 6) = 9\left(\dfrac{1}{10}\right)^2 + \dfrac{1}{10}$

$P(X \geqslant 6) = \dfrac{9}{100} + \dfrac{10}{100} = \dfrac{19}{100}$

Answer: $\frac{19}{100}$

</details>

---

### Q40. MHT CET 2025 (25 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $X$ denote the number of hours you study on a Sunday. It is known that.
$\mathrm{P}(\mathrm{X}=\mathrm{x})=\left\{\begin{array}{cl}
0.1 & , \text { if } x=0 \\
\mathrm{k} x & , \text { if } x=1 \text { or } 2 \\
\mathrm{k}(5-x) & , \text { if } x=3 \text { or } 4 \\
0 & , \text { otherwise }
\end{array}\right.$
where k is constant. Then the probability that you study at least two hours on a Sunday is

**Options:**

- **(A)** $0.55$
- **(B)** $0.15$
- **(C)** $0.75$
- **(D)** $0.3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.75$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is $1$.

$\sum P(X=x) = 1$

$P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) = 1$

$0.1 + k(1) + k(2) + k(5-3) + k(5-4) = 1$

$0.1 + k + 2k + 2k + k = 1$

$0.1 + 6k = 1$

$6k = 0.9$

$k = 0.15$

The probability of studying at least two hours is $P(X \ge 2)$.

$P(X \ge 2) = P(X=2) + P(X=3) + P(X=4)$

$P(X \ge 2) = 2k + 2k + k = 5k$

$P(X \ge 2) = 5 \times 0.15 = 0.75$

Answer: $0.75$

</details>

---

### Q41. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a random variable X is given by
<table> <thead> <tr> <th>$\mathrm{X}=x_i$ </th> <th>0 </th> <th>1 </th> <th>2 </th> <th>3 </th> <th>4 </th> </tr> </thead> <tbody> <tr> <td>$\mathrm{P}\left(\mathrm{X}=x_i\right)$ </td> <td>$0.4$ </td> <td>$0.3$ </td> <td>$0.1$ </td> <td>$0.1$ </td> <td>$0.1$ </td> </tr> </tbody> </table>
Then the variance of X is

**Options:**

- **(A)** $1.76$
- **(B)** $2.45$
- **(C)** $3.2$
- **(D)** $4.$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1.76$**

**Detailed Solution:**

The expected value $E(X)$ is given by $\sum x_i P(x_i)$.

$E(X) = 0(0.4) + 1(0.3) + 2(0.1) + 3(0.1) + 4(0.1)$

$E(X) = 0 + 0.3 + 0.2 + 0.3 + 0.4 = 1.2$

The expected value of $X^2$, $E(X^2)$ is given by $\sum x_i^2 P(x_i)$.

$E(X^2) = 0^2(0.4) + 1^2(0.3) + 2^2(0.1) + 3^2(0.1) + 4^2(0.1)$

$E(X^2) = 0 + 0.3 + 0.4 + 0.9 + 1.6 = 3.2$

The variance of $X$ is given by $Var(X) = E(X^2) - [E(X)]^2$.

$Var(X) = 3.2 - (1.2)^2$

$Var(X) = 3.2 - 1.44 = 1.76$

Answer: $1.76$

</details>

---

### Q42. MHT CET 2025 (23 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has following p.d.f.
$\mathrm{f}(\mathrm{x})=\mathrm{k} x(1-x), 0 \leqslant x \leqslant 1$
and $\mathrm{P}(x>a)=\frac{20}{27}$, then $a=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{3}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, $\int_{0}^{1} f(x) dx = 1$

$\int_{0}^{1} k(x - x^2) dx = 1$

$k \left[ \dfrac{x^2}{2} - \dfrac{x^3}{3} \right]_{0}^{1} = 1$

$k \left( \dfrac{1}{2} - \dfrac{1}{3} \right) = 1 \Rightarrow k \left( \dfrac{1}{6} \right) = 1 \Rightarrow k = 6$

Given $P(X > a) = \dfrac{20}{27}$

$\int_{a}^{1} 6(x - x^2) dx = \dfrac{20}{27}$

$6 \left[ \dfrac{x^2}{2} - \dfrac{x^3}{3} \right]_{a}^{1} = \dfrac{20}{27}$

$6 \left( \dfrac{1}{6} - \left( \dfrac{a^2}{2} - \dfrac{a^3}{3} \right) \right) = \dfrac{20}{27}$

$1 - 3a^2 + 2a^3 = \dfrac{20}{27}$

$2a^3 - 3a^2 + \dfrac{7}{27} = 0$

$54a^3 - 81a^2 + 7 = 0$

By substituting the given options, for $a = \dfrac{1}{3}$:

$54 \left( \dfrac{1}{27} \right) - 81 \left( \dfrac{1}{9} \right) + 7 = 2 - 9 + 7 = 0$

Thus, $a = \dfrac{1}{3}$ is the correct value.

Answer: $\frac{1}{3}$

</details>

---

### Q43. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a game a man wins $₹ 40$ if he gets 5 or 6 on a throw of a fair die and loses ₹ 20 for getting any other number on the die. If he decides to throw the die either till he gets a five or six or to a maximum of three throws, then his expected gain/loss (in rupees) is

**Options:**

- **(A)** $-10$
- **(B)** 10
- **(C)** 0
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0**

**Detailed Solution:**

Let $p$ be the probability of getting a 5 or 6 on a single throw of a fair die. 

$p = \dfrac{2}{6} = \dfrac{1}{3}$

Let $q$ be the probability of getting any other number (1, 2, 3, or 4). 

$q = \dfrac{4}{6} = \dfrac{2}{3}$

The man throws the die until he gets a 5 or 6, or up to a maximum of 3 throws. The possible outcomes and their corresponding probabilities and gains are:

1. Success on the first throw:
Probability $= \dfrac{1}{3}$
Gain $= 40$

2. Failure on the first throw, success on the second:
Probability $= \dfrac{2}{3} \times \dfrac{1}{3} = \dfrac{2}{9}$
Gain $= -20 + 40 = 20$

3. Failure on the first two throws, success on the third:
Probability $= \left(\dfrac{2}{3}\right)^2 \times \dfrac{1}{3} = \dfrac{4}{27}$
Gain $= -20 - 20 + 40 = 0$

4. Failure on all three throws:
Probability $= \left(\dfrac{2}{3}\right)^3 = \dfrac{8}{27}$
Gain $= -20 - 20 - 20 = -60$

The expected gain/loss $E(X)$ is the sum of the products of the probabilities and their respective gains:

$E(X) = \left(\dfrac{1}{3} \times 40\right) + \left(\dfrac{2}{9} \times 20\right) + \left(\dfrac{4}{27} \times 0\right) + \left(\dfrac{8}{27} \times -60\right)$

$E(X) = \dfrac{40}{3} + \dfrac{40}{9} + 0 - \dfrac{480}{27}$

$E(X) = \dfrac{360 + 120 - 480}{27}$

$E(X) = \dfrac{480 - 480}{27} = 0$

Answer: 0

</details>

---

### Q44. MHT CET 2025 (23 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let mean and standard deviation of probability distribution
\(\begin{array}{|r|r|c|c|c|} \hline \mathrm{X}=x & -3 & 0 & 1 & \alpha \\ \hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{4} & \mathrm{~K} & \frac{1}{4} & \frac{1}{3} \\ \hline \end{array}\)
be $\mu$ and $\sigma$ respectively and if $\sigma-\mu=2$ then $\sigma=$

**Options:**

- **(A)** $\frac{3}{2}$
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{7}{2}$
- **(D)** $\frac{9}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{7}{2}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is always $1$.

$\dfrac{1}{4} + K + \dfrac{1}{4} + \dfrac{1}{3} = 1$

$\dfrac{5}{6} + K = 1 \Rightarrow K = \dfrac{1}{6}$

The mean $\mu$ is given by $E(X)$:

$\mu = \sum x_i P(x_i) = -3\left(\dfrac{1}{4}\right) + 0\left(\dfrac{1}{6}\right) + 1\left(\dfrac{1}{4}\right) + \alpha\left(\dfrac{1}{3}\right) = \dfrac{\alpha}{3} - \dfrac{1}{2}$

The expected value of $X^2$ is:

$E(X^2) = \sum x_i^2 P(x_i) = (-3)^2\left(\dfrac{1}{4}\right) + 0^2\left(\dfrac{1}{6}\right) + 1^2\left(\dfrac{1}{4}\right) + \alpha^2\left(\dfrac{1}{3}\right) = \dfrac{9}{4} + \dfrac{1}{4} + \dfrac{\alpha^2}{3} = \dfrac{5}{2} + \dfrac{\alpha^2}{3}$

The variance is $\sigma^2 = E(X^2) - \mu^2$.

Given $\sigma - \mu = 2 \Rightarrow \sigma = \mu + 2$.

Squaring both sides:

$\sigma^2 = (\mu + 2)^2 = \mu^2 + 4\mu + 4$

Equating the two expressions for $\sigma^2$:

$E(X^2) - \mu^2 = \mu^2 + 4\mu + 4$

$E(X^2) = 2\mu^2 + 4\mu + 4$

Substituting the values of $\mu$ and $E(X^2)$:

$\dfrac{5}{2} + \dfrac{\alpha^2}{3} = 2\left(\dfrac{\alpha}{3} - \dfrac{1}{2}\right)^2 + 4\left(\dfrac{\alpha}{3} - \dfrac{1}{2}\right) + 4$

$\dfrac{5}{2} + \dfrac{\alpha^2}{3} = 2\left(\dfrac{\alpha^2}{9} - \dfrac{\alpha}{3} + \dfrac{1}{4}\right) + \dfrac{4\alpha}{3} - 2 + 4$

$\dfrac{5}{2} + \dfrac{\alpha^2}{3} = \dfrac{2\alpha^2}{9} - \dfrac{2\alpha}{3} + \dfrac{1}{2} + \dfrac{4\alpha}{3} + 2$

$\dfrac{5}{2} + \dfrac{\alpha^2}{3} = \dfrac{2\alpha^2}{9} + \dfrac{2\alpha}{3} + \dfrac{5}{2}$

$\dfrac{\alpha^2}{3} - \dfrac{2\alpha^2}{9} - \dfrac{2\alpha}{3} = 0$

$\dfrac{\alpha^2}{9} - \dfrac{2\alpha}{3} = 0$

$\alpha^2 - 6\alpha = 0 \Rightarrow \alpha(\alpha - 6) = 0$

Thus, $\alpha = 0$ or $\alpha = 6$.

Since the values of a random variable in a probability distribution table must be distinct, and $0$ is already a value of $X$, we must have $\alpha = 6$.

Substituting $\alpha = 6$ into the expression for $\mu$:

$\mu = \dfrac{6}{3} - \dfrac{1}{2} = 2 - \dfrac{1}{2} = \dfrac{3}{2}$

Finally, substituting $\mu$ to find $\sigma$:

$\sigma = \mu + 2 = \dfrac{3}{2} + 2 = \dfrac{7}{2}$

Answer: $\frac{7}{2}$

</details>

---

### Q45. MHT CET 2025 (22 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $X$ has p.d.f.
$\mathrm{f}(x)= \begin{cases}\frac{a x^2}{2}+\mathrm{b} x & , \text { if } 1 \leqslant x \leqslant 3 \\ 0 & , \text { otherwise }\end{cases}$
and $f(2)=\frac{3}{5}$, then the values of $a$ and $b$ are, respectively

**Options:**

- **(A)** $11,-10$
- **(B)** $-\frac{3}{5}, \frac{9}{10}$
- **(C)** $\frac{1}{6}, \frac{5}{6}$
- **(D)** $9,-8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-\frac{3}{5}, \frac{9}{10}$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, $\int_{-\infty}^{\infty} f(x) dx = 1$.

$\int_{1}^{3} \left( \dfrac{a x^2}{2} + b x \right) dx = 1$

$\left[ \dfrac{a x^3}{6} + \dfrac{b x^2}{2} \right]_{1}^{3} = 1$

$\left( \dfrac{27a}{6} + \dfrac{9b}{2} \right) - \left( \dfrac{a}{6} + \dfrac{b}{2} \right) = 1$

$\dfrac{26a}{6} + 4b = 1 \Rightarrow \dfrac{13a}{3} + 4b = 1$

Given $f(2) = \dfrac{3}{5}$, we have:

$\dfrac{a(2)^2}{2} + b(2) = \dfrac{3}{5}$

$2a + 2b = \dfrac{3}{5} \Rightarrow a + b = \dfrac{3}{10} \Rightarrow b = \dfrac{3}{10} - a$

Substituting the value of $b$ in the first equation:

$\dfrac{13a}{3} + 4\left( \dfrac{3}{10} - a \right) = 1$

$\dfrac{13a}{3} - 4a + \dfrac{6}{5} = 1$

$\dfrac{a}{3} = 1 - \dfrac{6}{5} = -\dfrac{1}{5}$

$a = -\dfrac{3}{5}$

Substituting $a$ in $b = \dfrac{3}{10} - a$:

$b = \dfrac{3}{10} - \left( -\dfrac{3}{5} \right) = \dfrac{3}{10} + \dfrac{6}{10} = \dfrac{9}{10}$

Answer: $-\frac{3}{5}, \frac{9}{10}$

</details>

---

### Q46. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The c.d.f. of a discrete random variable X is
\(\begin{array}{|c|c|c|c|c|c|c|c|c|} \hline \mathrm{X} & -3 & -1 & 0 & 1 & 3 & 5 & 7 & 9 \\ \hline \mathrm{~F}(\mathrm{X}=\mathrm{x}) & 0.1 & 0.3 & 0.5 & 0.65 & 0.75 & 0.85 & 0.90 & 1 \\ \hline \end{array}\)
Then $\frac{P[X=-3]}{P[X < 0]}=$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{6}$
- **(D)** $\frac{1}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{3}$**

**Detailed Solution:**

From the given cumulative distribution function $F(x)$, we know that $F(x) = P(X \le x)$.

The probability $P(X = -3)$ is given by:
$P(X = -3) = F(-3) = 0.1$

The probability $P(X < 0)$ includes all values of $X$ strictly less than $0$. From the given table, the values of $X$ less than $0$ are $-3$ and $-1$. Thus:
$P(X < 0) = P(X \le -1) = F(-1) = 0.3$

Now, we calculate the required ratio:
$\dfrac{P[X = -3]}{P[X < 0]} = \dfrac{0.1}{0.3} = \dfrac{1}{3}$

Answer: $\frac{1}{3}$

</details>

---

### Q47. MHT CET 2025 (21 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable X has p.m. f. $\mathrm{P}(\mathrm{X}=x)=\frac{{ }^4 \mathrm{C}_x}{2^4}, x=0,1,2,3,4$ and $\mu$ and $\sigma^2$ are mean and variance respectively of random variable $X$, then

**Options:**

- **(A)** $\mu=2, \quad \sigma^2=4$
- **(B)** $\mu=2, \quad \sigma^2=1$
- **(C)** $\mu=3, \quad \sigma^2=4$
- **(D)** $\mu=2, \quad \sigma^2=5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mu=2, \quad \sigma^2=1$**

**Detailed Solution:**

The given probability mass function is $P(X=x) = \dfrac{^{4}C_{x}}{2^4}$ for $x = 0, 1, 2, 3, 4$.

This can be written as $P(X=x) = ^{4}C_{x} \left(\dfrac{1}{2}\right)^x \left(\dfrac{1}{2}\right)^{4-x}$.

This represents a binomial distribution with parameters $n = 4$ and $p = \dfrac{1}{2}$.

The mean of a binomial distribution is given by $\mu = np$.

$\mu = 4 \times \dfrac{1}{2} = 2$

The variance of a binomial distribution is given by $\sigma^2 = npq$, where $q = 1 - p = \dfrac{1}{2}$.

$\sigma^2 = 4 \times \dfrac{1}{2} \times \dfrac{1}{2} = 1$

Thus, $\mu = 2$ and $\sigma^2 = 1$.

Answer: $\mu=2, \quad \sigma^2=1$

</details>

---

### Q48. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ takes values $0,1,2,3$,... with probabilities.
$\mathrm{P}(\mathrm{X}=x)=\mathrm{k}(x+1)\left(\frac{1}{2}\right)^x, \mathrm{k}$ is a constant, then $\mathrm{P}(\mathrm{X}=1)=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{1}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{4}$**

**Detailed Solution:**

The sum of all probabilities of a random variable is $1$.

$\sum_{x=0}^{\infty} P(X=x) = 1$

$\sum_{x=0}^{\infty} k(x+1)\left(\dfrac{1}{2}\right)^x = 1$

$k \left[ 1 + 2\left(\dfrac{1}{2}\right) + 3\left(\dfrac{1}{2}\right)^2 + \dots \right] = 1$

The series in the bracket is an arithmetico-geometric progression of the form $1 + 2r + 3r^2 + \dots = \dfrac{1}{(1-r)^2}$ where $r = \dfrac{1}{2}$.

$k \left[ \dfrac{1}{(1 - 1/2)^2} \right] = 1$

$k (4) = 1 \Rightarrow k = \dfrac{1}{4}$

Substituting $k = \dfrac{1}{4}$ and $x = 1$ in the given probability function:

$P(X=1) = \dfrac{1}{4}(1+1)\left(\dfrac{1}{2}\right)^1$

$P(X=1) = \dfrac{1}{4} \times 2 \times \dfrac{1}{2} = \dfrac{1}{4}$

Answer: $\frac{1}{4}$

</details>

---

### Q49. MHT CET 2025 (21 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The following is the probability distribution of X
<table> <thead> <tr> <th>X </th> <th>0 </th> <th>1 </th> <th>2 </th> <th>3 </th> </tr> </thead> <tbody> <tr> <td>$P(\mathrm{X}=x)$ </td> <td>$\frac{1+\mathrm{p}}{5}$ </td> <td>$\frac{2-2 \mathrm{p}}{5}$ </td> <td>$\frac{2-\mathrm{p}}{5}$ </td> <td>$\frac{2 \mathrm{p}}{5}$ </td> </tr> </tbody> </table>
For a minimum value of p, the value of $5 \mathrm{E}(\mathrm{X})$ is

**Options:**

- **(A)** $5$
- **(B)** $6$
- **(C)** $7$
- **(D)** $8$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $6$**

**Detailed Solution:**

For a valid probability distribution, all probabilities must be non-negative, i.e., $P(X=x) \ge 0$ for all $x$.

$\dfrac{1+p}{5} \ge 0 \Rightarrow p \ge -1$

$\dfrac{2-2p}{5} \ge 0 \Rightarrow p \le 1$

$\dfrac{2-p}{5} \ge 0 \Rightarrow p \le 2$

$\dfrac{2p}{5} \ge 0 \Rightarrow p \ge 0$

Taking the intersection of all these conditions, we get $0 \le p \le 1$.

The minimum possible value of $p$ is $0$.

The expected value $E(X)$ is given by:

$E(X) = \sum x P(X=x)$

$E(X) = 0 \left(\dfrac{1+p}{5}\right) + 1 \left(\dfrac{2-2p}{5}\right) + 2 \left(\dfrac{2-p}{5}\right) + 3 \left(\dfrac{2p}{5}\right)$

$E(X) = \dfrac{0 + 2 - 2p + 4 - 2p + 6p}{5} = \dfrac{6 + 2p}{5}$

$5E(X) = 6 + 2p$

Substituting the minimum value $p = 0$:

$5E(X) = 6 + 2(0) = 6$

Answer: $6$

</details>

---

### Q50. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ takes the values.
0,1,2,3,........ with probability
$\mathrm{P}(\mathrm{X}=x)=\mathrm{k}(x+1)\left(\frac{1}{5}\right)^x$, where k is a constant. Then $\mathrm{P}(\mathrm{X}=0)$ is

**Options:**

- **(A)** $\frac{16}{25}$
- **(B)** $\frac{7}{25}$
- **(C)** $\frac{19}{25}$
- **(D)** $\frac{18}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{16}{25}$**

**Detailed Solution:**

The sum of all probabilities for a random variable must be equal to $1$.

$\sum_{x=0}^{\infty} \mathrm{P}(\mathrm{X}=x) = 1$

$\sum_{x=0}^{\infty} \mathrm{k}(x+1)\left(\dfrac{1}{5}\right)^x = 1$

$\mathrm{k} \left[ 1 + 2\left(\dfrac{1}{5}\right) + 3\left(\dfrac{1}{5}\right)^2 + 4\left(\dfrac{1}{5}\right)^3 + \dots \right] = 1$

The series in the bracket is of the form $1 + 2r + 3r^2 + \dots = (1-r)^{-2}$, where $r = \dfrac{1}{5}$.

$\mathrm{k} \left(1 - \dfrac{1}{5}\right)^{-2} = 1$

$\mathrm{k} \left(\dfrac{4}{5}\right)^{-2} = 1$

$\mathrm{k} \left(\dfrac{25}{16}\right) = 1 \Rightarrow \mathrm{k} = \dfrac{16}{25}$

We need to find $\mathrm{P}(\mathrm{X}=0)$:

$\mathrm{P}(\mathrm{X}=0) = \mathrm{k}(0+1)\left(\dfrac{1}{5}\right)^0 = \mathrm{k} \times 1 \times 1 = \mathrm{k}$

$\mathrm{P}(\mathrm{X}=0) = \dfrac{16}{25}$

Answer: $\frac{16}{25}$

</details>

---

### Q51. MHT CET 2025 (20 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two numbers are selected at random, without replacement from the first 6 positive integers. Let X denote the larger of the two numbers. Then $\mathrm{E}(\mathrm{X})=$

**Options:**

- **(A)** $\frac{14}{3}$
- **(B)** $\frac{3}{14}$
- **(C)** $\frac{14}{5}$
- **(D)** $\frac{15}{41}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{14}{3}$**

**Detailed Solution:**

The sample space consists of all possible pairs of 2 numbers selected from the first 6 positive integers.

Total number of ways to select 2 numbers is $^{6}C_{2} = \dfrac{6 \times 5}{2} = 15$.

Let $X$ be the larger of the two numbers. The possible values of $X$ are $2, 3, 4, 5, 6$.

For $X = x$, the other number must be selected from the $x-1$ numbers smaller than $x$. Thus, the number of favourable outcomes is $x-1$.

The probability distribution of $X$ is:
$P(X=2) = \dfrac{1}{15}$
$P(X=3) = \dfrac{2}{15}$
$P(X=4) = \dfrac{3}{15}$
$P(X=5) = \dfrac{4}{15}$
$P(X=6) = \dfrac{5}{15}$

The expected value is $E(X) = \sum x P(X=x)$.

$E(X) = 2\left(\dfrac{1}{15}\right) + 3\left(\dfrac{2}{15}\right) + 4\left(\dfrac{3}{15}\right) + 5\left(\dfrac{4}{15}\right) + 6\left(\dfrac{5}{15}\right)$

$E(X) = \dfrac{2 + 6 + 12 + 20 + 30}{15}$

$E(X) = \dfrac{70}{15} = \dfrac{14}{3}$

Answer: $\frac{14}{3}$

</details>

---

### Q52. MHT CET 2025 (20 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn simultaneously from a well shuffled pack of 52 cards. If $X$ is the random variable of getting queens, then the value of $2 E(X)+3 E\left(X^2\right)$ for the number of queens is

**Options:**

- **(A)** $\frac{132}{221}$
- **(B)** $\frac{108}{221}$
- **(C)** $\frac{176}{221}$
- **(D)** $\frac{68}{221}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{176}{221}$**

**Detailed Solution:**

Let $X$ be the random variable representing the number of queens obtained when two cards are drawn simultaneously from a pack of $52$ cards.

The possible values for $X$ are $0, 1, 2$.

Total number of ways to draw $2$ cards from $52$ cards is $^{52}C_{2} = \dfrac{52 \times 51}{2} = 1326$.

The probability distribution of $X$ is:
$P(X = 0) = \dfrac{^{48}C_{2}}{^{52}C_{2}} = \dfrac{1128}{1326} = \dfrac{188}{221}$

$P(X = 1) = \dfrac{^{4}C_{1} \times ^{48}C_{1}}{^{52}C_{2}} = \dfrac{4 \times 48}{1326} = \dfrac{192}{1326} = \dfrac{32}{221}$

$P(X = 2) = \dfrac{^{4}C_{2}}{^{52}C_{2}} = \dfrac{6}{1326} = \dfrac{1}{221}$

Now, we calculate the expected value $E(X)$:
$E(X) = \sum x_{i} P(x_{i}) = 0 \times \dfrac{188}{221} + 1 \times \dfrac{32}{221} + 2 \times \dfrac{1}{221} = \dfrac{34}{221}$

Next, we calculate $E(X^2)$:
$E(X^2) = \sum x_{i}^2 P(x_{i}) = 0^2 \times \dfrac{188}{221} + 1^2 \times \dfrac{32}{221} + 2^2 \times \dfrac{1}{221} = \dfrac{32}{221} + \dfrac{4}{221} = \dfrac{36}{221}$

Finally, we find the value of $2 E(X) + 3 E(X^2)$:
$2 E(X) + 3 E(X^2) = 2 \left( \dfrac{34}{221} \right) + 3 \left( \dfrac{36}{221} \right)$

$= \dfrac{68}{221} + \dfrac{108}{221} = \dfrac{176}{221}$

Answer: $\frac{176}{221}$

</details>

---

### Q53. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In a game, 3 coins are tossed. A person is paid ₹150 if he gets all heads or all tails and he is supposed to pay ₹50 if he gets one head or two heads. The amount he can expect to win / lose on an average per game in ₹ is

**Options:**

- **(A)** $100$
- **(B)** $0$
- **(C)** $200$
- **(D)** $-100$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0$**

**Detailed Solution:**

When 3 coins are tossed, the total number of outcomes in the sample space is $2^3 = 8$.

Let $X$ be the amount won in the game.

The outcomes for getting all heads or all tails are HHH and TTT. The probability of this event is $P(X = 150) = \dfrac{2}{8} = \dfrac{1}{4}$.

The remaining outcomes have either one head or two heads. The probability of this event is $P(X = -50) = \dfrac{6}{8} = \dfrac{3}{4}$.

The expected amount won or lost on an average per game is given by the expected value $E(X) = \sum x_i P(x_i)$.

$E(X) = 150 \times \dfrac{1}{4} + (-50) \times \dfrac{3}{4}$

$E(X) = \dfrac{150}{4} - \dfrac{150}{4} = 0$

Answer: $0$

</details>

---

### Q54. MHT CET 2025 (19 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let X be a discrete random variable. The probability distribution of X is given below
\(\begin{array}{|l|c|c|c|} \hline \mathrm{X} & 30 & 10 & -10 \\ \hline \mathrm{P}(\mathrm{X}) & \frac{1}{5} & \mathrm{~A} & \mathrm{~B} \\ \hline \end{array}\)
and $\mathrm{E}(\mathrm{X})=4$, then the value of AB is equal to

**Options:**

- **(A)** $\frac{3}{10}$
- **(B)** $\frac{2}{15}$
- **(C)** $\frac{1}{15}$
- **(D)** $\frac{3}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{20}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is always $1$.

$\dfrac{1}{5} + A + B = 1$

$A + B = \dfrac{4}{5}$

The expected value is given by $\mathrm{E}(\mathrm{X}) = \sum \mathrm{X} \mathrm{P}(\mathrm{X})$.

$30\left(\dfrac{1}{5}\right) + 10A - 10B = 4$

$6 + 10A - 10B = 4$

$10A - 10B = -2$

$A - B = -\dfrac{1}{5}$

Adding the two equations for $A+B$ and $A-B$ gives:

$2A = \dfrac{4}{5} - \dfrac{1}{5} = \dfrac{3}{5}$

$A = \dfrac{3}{10}$

Substituting the value of $A$ in the first equation:

$\dfrac{3}{10} + B = \dfrac{4}{5}$

$B = \dfrac{4}{5} - \dfrac{3}{10} = \dfrac{8 - 3}{10} = \dfrac{5}{10} = \dfrac{1}{2}$

The value of $AB$ is:

$AB = \dfrac{3}{10} \times \dfrac{1}{2} = \dfrac{3}{20}$

Answer: $\frac{3}{20}$

</details>

---

### Q55. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $X$ follows the Binomial distribution $B(33, p)$ such that $3 P(X=0)=P(X=1)$, then the variance of $X$ is

**Options:**

- **(A)** $\frac{11}{144}$
- **(B)** $\frac{35}{48}$
- **(C)** $\frac{121}{48}$
- **(D)** $\frac{33}{144}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{121}{48}$**

**Detailed Solution:**

Given $X \sim B(n, p)$ with $n = 33$.

The probability mass function is $P(X=x) = ^{n}C_{x} p^x q^{n-x}$, where $q = 1 - p$.

We are given $3 P(X=0) = P(X=1)$.

Substituting the values:

$3 \times ^{33}C_{0} p^0 q^{33} = ^{33}C_{1} p^1 q^{32}$

$3 q^{33} = 33 p q^{32}$

$3 q = 33 p$

$q = 11 p$

Since $p + q = 1$:

$p + 11 p = 1$

$12 p = 1 \Rightarrow p = \dfrac{1}{12}$

Therefore, $q = 1 - \dfrac{1}{12} = \dfrac{11}{12}$.

The variance of a Binomial distribution is given by $npq$.

$\text{Var}(X) = 33 \times \dfrac{1}{12} \times \dfrac{11}{12}$

$\text{Var}(X) = \dfrac{363}{144} = \dfrac{121}{48}$

Answer: $\frac{121}{48}$

</details>

---

### Q56. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable X has the p.d.f.
$\mathrm{f}(x)=\left\{\begin{array}{cl}\frac{\mathrm{k}}{x^2+1} & , \text { if } 0 < x < \infty \\ 0 & , \text { otherwise }\end{array}\right.$
then c.d.f. of X is

**Options:**

- **(A)** $2 \tan ^{-1} x$
- **(B)** $\frac{\pi}{2} \tan ^{-1} x$
- **(C)** $\frac{2}{\pi} \tan ^{-1} x$
- **(D)** $\tan ^{-1} x$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{\pi} \tan ^{-1} x$**

**Detailed Solution:**

Since $f(x)$ is a probability density function, the total probability is $1$.

$\int_{-\infty}^{\infty} f(x) dx = 1$

$\int_{0}^{\infty} \dfrac{k}{x^2+1} dx = 1$

$k [\tan^{-1} x]_{0}^{\infty} = 1$

$k \left(\dfrac{\pi}{2} - 0\right) = 1 \Rightarrow k = \dfrac{2}{\pi}$

The cumulative distribution function (c.d.f.) $F(x)$ is given by:

$F(x) = \int_{-\infty}^{x} f(t) dt$

For $x > 0$,

$F(x) = \int_{0}^{x} \dfrac{2}{\pi(t^2+1)} dt$

$F(x) = \dfrac{2}{\pi} [\tan^{-1} t]_{0}^{x} = \dfrac{2}{\pi} \tan^{-1} x$

Answer: $\frac{2}{\pi} \tan ^{-1} x$

</details>

---

### Q57. MHT CET 2025 (19 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The probability distribution of a discrete random variable X is
\(\begin{array}{||c|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 & 4 \\ \hline \mathrm{P}(\mathrm{X}=x) & 2 \mathrm{k} & \mathrm{k} & 2 \mathrm{k} & 4 \mathrm{k} & \mathrm{k} \\ \hline \end{array}\)
If $\mathrm{a}=\mathrm{P}(x < 3)$ and $\mathrm{b}=\mathrm{P}(2 < \mathrm{x} < 4)$, then

**Options:**

- **(A)** $a=b$
- **(B)** $\mathrm{a} < \mathrm{b}$
- **(C)** $a>b$
- **(D)** $a=\frac{1}{2} b$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $a>b$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is $1$.

$\sum P(X=x) = 2k + k + 2k + 4k + k = 1$

$10k = 1 \Rightarrow k = \dfrac{1}{10}$

Given $a = P(X < 3) = P(X=0) + P(X=1) + P(X=2)$

$a = 2k + k + 2k = 5k = 5 \times \dfrac{1}{10} = \dfrac{1}{2}$

Given $b = P(2 < X < 4) = P(X=3)$

$b = 4k = 4 \times \dfrac{1}{10} = \dfrac{2}{5}$

Since $\dfrac{1}{2} > \dfrac{2}{5}$, we have $a > b$.

Answer: $a>b$

</details>

---

### Q58. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The cumulative distribution function of a discrete random variable X is given by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/zC1DQff-6poDs5OPocr2hWr5GFm8eDJe3VK3tPFb2KE.original.fullsize.png"/>
Then $\mathrm{E}\left(\mathrm{X}^2\right)=$

**Options:**

- **(A)** 0.2
- **(B)** 1.2
- **(C)** 0.8
- **(D)** 2.5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1.2**

**Detailed Solution:**

From the given cumulative distribution function $F(x)$, we can find the probability mass function $P(X=x)$ using the relation $P(X=x_i) = F(x_i) - F(x_{i-1})$.

$P(X = -1) = F(-1) = 0.3$
$P(X = 0) = F(0) - F(-1) = 0.7 - 0.3 = 0.4$
$P(X = 1) = F(1) - F(0) = 0.8 - 0.7 = 0.1$
$P(X = 2) = F(2) - F(1) = 1 - 0.8 = 0.2$

The expected value of $X^2$ is given by:
$\mathrm{E}(X^2) = \sum x^2 P(X=x)$

Substituting the values:
$\mathrm{E}(X^2) = (-1)^2(0.3) + (0)^2(0.4) + (1)^2(0.1) + (2)^2(0.2)$
$\mathrm{E}(X^2) = 1(0.3) + 0(0.4) + 1(0.1) + 4(0.2)$
$\mathrm{E}(X^2) = 0.3 + 0 + 0.1 + 0.8$
$\mathrm{E}(X^2) = 1.2$

Answer: 1.2

</details>

---

### Q59. MHT CET 2024 (16 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If a discrete random variable $X$ is defined as follows
$\mathrm{P}[\mathrm{X}=x]=\left\{\begin{array}{cl}
\frac{\mathrm{k}(x+1)}{5^x}, & \text { if } x=0,1,2 \ldots \ldots \\
0, & \text { otherwise }
\end{array}\right.$
then $\mathrm{k}=$

**Options:**

- **(A)** $\frac{19}{25}$
- **(B)** $\frac{18}{25}$
- **(C)** $\frac{16}{25}$
- **(D)** $\frac{7}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{16}{25}$**

**Detailed Solution:**

For a discrete random variable, the sum of all probabilities must be equal to $1$.

$\sum_{x=0}^{\infty} P[X=x] = 1$

$\sum_{x=0}^{\infty} \dfrac{k(x+1)}{5^x} = 1$

$k \left( 1 + \dfrac{2}{5} + \dfrac{3}{5^2} + \dfrac{4}{5^3} + \dots \right) = 1$

Let $S = 1 + \dfrac{2}{5} + \dfrac{3}{5^2} + \dfrac{4}{5^3} + \dots$

Multiplying by $\dfrac{1}{5}$ on both sides:

$\dfrac{1}{5}S = \dfrac{1}{5} + \dfrac{2}{5^2} + \dfrac{3}{5^3} + \dots$

Subtracting the second equation from the first:

$S - \dfrac{1}{5}S = 1 + \left(\dfrac{2}{5} - \dfrac{1}{5}\right) + \left(\dfrac{3}{5^2} - \dfrac{2}{5^2}\right) + \dots$

$\dfrac{4}{5}S = 1 + \dfrac{1}{5} + \dfrac{1}{5^2} + \dfrac{1}{5^3} + \dots$

The right side is an infinite geometric progression with first term $a = 1$ and common ratio $r = \dfrac{1}{5}$.

$\dfrac{4}{5}S = \dfrac{1}{1 - \dfrac{1}{5}}$

$\dfrac{4}{5}S = \dfrac{1}{\dfrac{4}{5}} = \dfrac{5}{4}$

$S = \dfrac{25}{16}$

Substituting $S$ back into the probability sum equation:

$k \times \dfrac{25}{16} = 1$

$k = \dfrac{16}{25}$

Answer: $\frac{16}{25}$

</details>

---

### Q60. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $X$ takes the values $0,1,2,3$ and its mean is 1.3. If $\mathrm{P}(\mathrm{X}=3)=2 \mathrm{P}(\mathrm{X}=1)$ and $P(X=2)=0.3$, then $P(X=0)$ is

**Options:**

- **(A)** 0.2
- **(B)** 0.3
- **(C)** 0.1
- **(D)** 0.4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.4**

**Detailed Solution:**

Let $P(X=0) = p_0$, $P(X=1) = p_1$, $P(X=2) = p_2$, and $P(X=3) = p_3$.

Given $p_2 = 0.3$ and $p_3 = 2p_1$.

The mean of the random variable $X$ is given by $E(X) = \sum x_i p_i = 1.3$.

$0 \cdot p_0 + 1 \cdot p_1 + 2 \cdot p_2 + 3 \cdot p_3 = 1.3$

$p_1 + 2(0.3) + 3(2p_1) = 1.3$

$7p_1 + 0.6 = 1.3$

$7p_1 = 0.7 \Rightarrow p_1 = 0.1$

The sum of all probabilities is $\sum p_i = 1$.

$p_0 + p_1 + p_2 + p_3 = 1$

$p_0 + p_1 + 0.3 + 2p_1 = 1$

$p_0 + 3p_1 = 0.7$

Substituting $p_1 = 0.1$:

$p_0 + 3(0.1) = 0.7$

$p_0 = 0.7 - 0.3 = 0.4$

Thus, $P(X=0) = 0.4$.

Answer: 0.4

</details>

---

### Q61. MHT CET 2024 (16 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If a random variable $X$ has the following probability distribution values
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/so0y9Za5Hv8w2aala-3uZSslkNrSGddQDn5uqU5epaI.original.fullsize.png"/>
Then $P(X \geq 6)$ has the value

**Options:**

- **(A)** $\frac{19}{100}$
- **(B)** $\frac{81}{100}$
- **(C)** $\frac{9}{100}$
- **(D)** $\frac{91}{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{19}{100}$**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities must be equal to $1$.

$\sum P(X) = 1$

$0 + k + 2k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1$

$10k^2 + 9k = 1$

$10k^2 + 9k - 1 = 0$

$10k^2 + 10k - k - 1 = 0$

$10k(k + 1) - 1(k + 1) = 0$

$(10k - 1)(k + 1) = 0$

$k = \dfrac{1}{10}$ or $k = -1$

Since probability cannot be negative, $k = \dfrac{1}{10}$.

We need to find $P(X \geq 6)$:

$P(X \geq 6) = P(X = 6) + P(X = 7)$

$P(X \geq 6) = 2k^2 + (7k^2 + k)$

$P(X \geq 6) = 9k^2 + k$

Substituting $k = \dfrac{1}{10}$:

$P(X \geq 6) = 9\left(\dfrac{1}{10}\right)^2 + \dfrac{1}{10}$

$P(X \geq 6) = \dfrac{9}{100} + \dfrac{10}{100}$

$P(X \geq 6) = \dfrac{19}{100}$

Answer: $\frac{19}{100}$

</details>

---

### Q62. MHT CET 2024 (15 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Suppose three coins are tossed simultaneously. If X denotes the number of heads, then probability distribution of X is

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/q6B0C88wQ7jVO2Ne5nhxDbSzXPJ7JDPOjkei6JNetvA.original.fullsize.png"/>
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/QF_oBadeEfmpdIFtqDI_pQsNsB58dyKBKao085yq-io.original.fullsize.png"/>
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/yrsa1MkU-iTlkUOqfl2fKk-PuyQKHNT-PHsp5QB_gKk.original.fullsize.png"/>
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/buHM1SqVBLjzGvob5a5JPg0g-h4OrZqkxMf9ojRDwyU.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/QF_oBadeEfmpdIFtqDI_pQsNsB58dyKBKao085yq-io.original.fullsize.png"/>**

**Detailed Solution:**

When three coins are tossed simultaneously, the total number of possible outcomes is $2^3 = 8$.

The sample space is $S = \{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\}$.

Let $X$ denote the number of heads. The possible values of $X$ are $0, 1, 2, 3$.

$P(X = 0) = P(\{TTT\}) = \dfrac{1}{8}$

$P(X = 1) = P(\{HTT, THT, TTH\}) = \dfrac{3}{8}$

$P(X = 2) = P(\{HHT, HTH, THH\}) = \dfrac{3}{8}$

$P(X = 3) = P(\{HHH\}) = \dfrac{1}{8}$

This matches the probability distribution given in the second option.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/QF_oBadeEfmpdIFtqDI_pQsNsB58dyKBKao085yq-io.original.fullsize.png"/>

</details>

---

### Q63. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $X$ has the following probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/W4IodHzy2YLNlbXFR6czB3myb-yWHviSdebyJnHqyzU.original.fullsize.png"/>
Then $\mathrm{p}(x \geq 2)$ is equal to

**Options:**

- **(A)** $\frac{35}{36}$
- **(B)** $\frac{34}{36}$
- **(C)** $\frac{33}{36}$
- **(D)** $\frac{31}{36}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{35}{36}$**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities is $1$.

$\sum p(x) = 1$

$k^2 + 2k + k + 2k + 5k^2 = 1$

$6k^2 + 5k - 1 = 0$

$(6k - 1)(k + 1) = 0$

$k = \dfrac{1}{6}$ or $k = -1$

Since probability cannot be negative, $k = \dfrac{1}{6}$.

$p(x \geq 2) = 1 - p(x < 2)$

$p(x \geq 2) = 1 - p(1)$

$p(x \geq 2) = 1 - k^2$

$p(x \geq 2) = 1 - \left(\dfrac{1}{6}\right)^2$

$p(x \geq 2) = 1 - \dfrac{1}{36} = \dfrac{35}{36}$

Answer: $\frac{35}{36}$

</details>

---

### Q64. MHT CET 2024 (15 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For the probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/jI8ml16edWVH9ekTfR0v8EphGtd0IuUpJ4bl_ZgZZVY.original.fullsize.png"/>
The Expected value of X is

**Options:**

- **(A)** 1.45
- **(B)** 1.55
- **(C)** 2.45
- **(D)** 2.55

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2.45**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities must be equal to $1$.

$\sum p(x) = 1$

$k + 0.3 + 0.15 + 0.15 + 0.1 + 2k = 1$

$3k + 0.7 = 1$

$3k = 0.3 \Rightarrow k = 0.1$

The expected value of $X$ is given by $E(X) = \sum x \cdot p(x)$.

$E(X) = (0 \times k) + (1 \times 0.3) + (2 \times 0.15) + (3 \times 0.15) + (4 \times 0.1) + (5 \times 2k)$

Substituting $k = 0.1$:

$E(X) = (0 \times 0.1) + (1 \times 0.3) + (2 \times 0.15) + (3 \times 0.15) + (4 \times 0.1) + (5 \times 0.2)$

$E(X) = 0 + 0.3 + 0.3 + 0.45 + 0.4 + 1.0$

$E(X) = 2.45$

Answer: 2.45

</details>

---

### Q65. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A random variable X takes the values $0,1,2$, $3, \ldots$ with probability $\mathrm{P}(\mathrm{X}=x)=\mathrm{k}(x+1)\left(\frac{1}{5}\right)^x$, where k is a constant, then $\mathrm{P}(\mathrm{X}=0)$ is

**Options:**

- **(A)** $\frac{16}{25}$
- **(B)** $\frac{7}{25}$
- **(C)** $\frac{19}{25}$
- **(D)** $\frac{18}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{16}{25}$**

**Detailed Solution:**

The sum of all probabilities of a random variable is $1$.

$\sum_{x=0}^{\infty} P(X=x) = 1$

$\sum_{x=0}^{\infty} k(x+1)\left(\dfrac{1}{5}\right)^x = 1$

$k \left[ 1 + 2\left(\dfrac{1}{5}\right) + 3\left(\dfrac{1}{5}\right)^2 + \ldots \right] = 1$

The series in the bracket is an arithmetico-geometric progression whose sum is given by $(1-r)^{-2} = 1 + 2r + 3r^2 + \ldots$ where $r = \dfrac{1}{5}$.

$k \left(1 - \dfrac{1}{5}\right)^{-2} = 1$

$k \left(\dfrac{4}{5}\right)^{-2} = 1$

$k \left(\dfrac{25}{16}\right) = 1 \Rightarrow k = \dfrac{16}{25}$

We need to find $P(X=0)$.

$P(X=0) = k(0+1)\left(\dfrac{1}{5}\right)^0 = k = \dfrac{16}{25}$

Answer: $\frac{16}{25}$

</details>

---

### Q66. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has the following probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/6PC4mtaZpBV0pholHy2Ri2geXViFnLBkYR33-qbNRzU.original.fullsize.png"/>
For the event $E=\{X$ is a prime number $\}$, $F=\{X \lt 4\}$, then $P(E \cup F)$ is

**Options:**

- **(A)** 0.5
- **(B)** 0.77
- **(C)** 0.35
- **(D)** 0.75

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.75**

**Detailed Solution:**

From the given probability distribution, the possible values of $X$ are $\{1, 2, 3, 4, 5, 6, 7, 8\}$.

Event $E = \{X \text{ is a prime number}\} = \{2, 3, 5, 7\}$.

Event $F = \{X < 4\} = \{1, 2, 3\}$.

The union of events $E$ and $F$ is $E \cup F = \{1, 2, 3, 5, 7\}$.

The probability of $E \cup F$ is the sum of the probabilities of these individual outcomes:

$P(E \cup F) = P(X=1) + P(X=2) + P(X=3) + P(X=5) + P(X=7)$

Substituting the values from the table:

$P(E \cup F) = 0.15 + 0.23 + 0.10 + 0.20 + 0.07$

$P(E \cup F) = 0.75$

Answer: 0.75

</details>

---

### Q67. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If three fair coins are tossed, then variance of number of heads obtained, is

**Options:**

- **(A)** 0.25
- **(B)** 3
- **(C)** 0.75
- **(D)** 1.5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.75**

**Detailed Solution:**

Let $X$ be the number of heads obtained when three fair coins are tossed.

The random variable $X$ follows a binomial distribution with number of trials $n = 3$ and probability of getting a head $p = \dfrac{1}{2}$.

The probability of not getting a head is $q = 1 - p = \dfrac{1}{2}$.

The variance of a binomial distribution is given by $Var(X) = npq$.

Substituting the values, we get:

$Var(X) = 3 \times \dfrac{1}{2} \times \dfrac{1}{2} = \dfrac{3}{4} = 0.75$

Answer: 0.75

</details>

---

### Q68. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The p.m.f. of a random variable $X$ is given by
$\begin{aligned}
\mathrm{P}[\mathrm{X}=x] & =\frac{\binom{5}{x}}{2^5}, \text { if } x=0,1,2,3,4,5 \\
& =0, \text { otherwise }
\end{aligned}$
Then which of the following is not correct?

**Options:**

- **(A)** $\mathrm{P}[\mathrm{X}=0]=\mathrm{P}[\mathrm{X}=5]$
- **(B)** $\mathrm{P}[\mathrm{X} \leq 1]=\mathrm{P}[\mathrm{X} \geq 4]$
- **(C)** $\mathrm{P}[\mathrm{X} \leq 2]=\mathrm{P}[\mathrm{X} \geq 3]$
- **(D)** $\mathrm{P}[\mathrm{X} \leq 2]\gt\mathrm{P}[\mathrm{X} \geq 3]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{P}[\mathrm{X} \leq 2]\gt\mathrm{P}[\mathrm{X} \geq 3]$**

**Detailed Solution:**

The given p.m.f. is $P(X=x) = \dfrac{^{5}C_{x}}{2^5}$ for $x=0,1,2,3,4,5$.

Calculating the probabilities for each value of $x$:
$P(X=0) = \dfrac{^{5}C_{0}}{32} = \dfrac{1}{32}$
$P(X=1) = \dfrac{^{5}C_{1}}{32} = \dfrac{5}{32}$
$P(X=2) = \dfrac{^{5}C_{2}}{32} = \dfrac{10}{32}$
$P(X=3) = \dfrac{^{5}C_{3}}{32} = \dfrac{10}{32}$
$P(X=4) = \dfrac{^{5}C_{4}}{32} = \dfrac{5}{32}$
$P(X=5) = \dfrac{^{5}C_{5}}{32} = \dfrac{1}{32}$

Checking the given options:
$P(X=0) = P(X=5) = \dfrac{1}{32}$ (Correct)

$P(X \leq 1) = P(X=0) + P(X=1) = \dfrac{6}{32}$
$P(X \geq 4) = P(X=4) + P(X=5) = \dfrac{6}{32}$
Thus, $P(X \leq 1) = P(X \geq 4)$ (Correct)

$P(X \leq 2) = P(X=0) + P(X=1) + P(X=2) = \dfrac{16}{32} = \dfrac{1}{2}$
$P(X \geq 3) = P(X=3) + P(X=4) + P(X=5) = \dfrac{16}{32} = \dfrac{1}{2}$
Thus, $P(X \leq 2) = P(X \geq 3)$ (Correct)

Since $P(X \leq 2) = P(X \geq 3)$, the statement $P(X \leq 2) \gt P(X \geq 3)$ is not correct.

Answer: $\mathrm{P}[\mathrm{X} \leq 2]\gt\mathrm{P}[\mathrm{X} \geq 3]$

</details>

---

### Q69. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A random variable X assumes values $1,2,3, \ldots \ldots ., \mathrm{n}$ with equal probabilities. If $\operatorname{var}(X): E(X)=4: 1$, then $n$ is equal to

**Options:**

- **(A)** 20
- **(B)** 15
- **(C)** 25
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 25**

**Detailed Solution:**

The random variable $X$ assumes values $1, 2, 3, \ldots, n$ with equal probabilities.

$P(X=i) = \dfrac{1}{n}$ for $i = 1, 2, \ldots, n$

The expected value $E(X)$ is given by:

$E(X) = \sum_{i=1}^{n} i P(X=i) = \dfrac{1}{n} \dfrac{n(n+1)}{2} = \dfrac{n+1}{2}$

The expected value of $X^2$ is given by:

$E(X^2) = \sum_{i=1}^{n} i^2 P(X=i) = \dfrac{1}{n} \dfrac{n(n+1)(2n+1)}{6} = \dfrac{(n+1)(2n+1)}{6}$

The variance of $X$ is:

$\operatorname{var}(X) = E(X^2) - (E(X))^2 = \dfrac{(n+1)(2n+1)}{6} - \dfrac{(n+1)^2}{4} = \dfrac{n^2-1}{12}$

Given $\operatorname{var}(X) : E(X) = 4 : 1$, we have:

$\dfrac{\operatorname{var}(X)}{E(X)} = 4$

$\dfrac{\dfrac{n^2-1}{12}}{\dfrac{n+1}{2}} = 4$

$\dfrac{n-1}{6} = 4$

$n - 1 = 24$

$n = 25$

Answer: 25

</details>

---

### Q70. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $x$ has the following probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/UOI1sea7XvmoCbKW54MociX1a1An7kMw77und2AYlkw.original.fullsize.png"/>
For the events $\mathrm{E}=\{\mathrm{X}$ is prime number $\}$
$F=\{X \lt 4\}$
Then $P(E \cup F)=$

**Options:**

- **(A)** 0.87
- **(B)** 0.35
- **(C)** 0.77
- **(D)** 0.50

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.77**

**Detailed Solution:**

From the given probability distribution, the possible values of $X$ are $\{1, 2, 3, 4, 5, 6, 7, 8\}$.

The event $E$ is defined as $X$ being a prime number. The prime numbers in the given set are $2, 3, 5,$ and $7$.
Therefore, $E = \{2, 3, 5, 7\}$.

The event $F$ is defined as $X < 4$. The numbers less than $4$ in the given set are $1, 2,$ and $3$.
Therefore, $F = \{1, 2, 3\}$.

The union of events $E$ and $F$ is:
$E \cup F = \{2, 3, 5, 7\} \cup \{1, 2, 3\} = \{1, 2, 3, 5, 7\}$

The probability of $E \cup F$ is the sum of the probabilities of these individual outcomes:
$P(E \cup F) = P(X=1) + P(X=2) + P(X=3) + P(X=5) + P(X=7)$

Substituting the values from the given table:
$P(E \cup F) = 0.15 + 0.23 + 0.12 + 0.20 + 0.07$
$P(E \cup F) = 0.77$

Answer: 0.77

</details>

---

### Q71. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In a game, 3 coins are tossed. A person is paid $₹ 100$, if he gets all heads or all tails; and he is supposed to pay ₹ 40 , if he gets one head or two heads. The amount he can expect to win/lose on an average per game in ( $₹$ ) is

**Options:**

- **(A)** 10 loss
- **(B)** 5 loss
- **(C)** 5 gain
- **(D)** 10 gain

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5 loss**

**Detailed Solution:**

Total number of possible outcomes when 3 coins are tossed is $2^3 = 8$.

The probability of getting all heads or all tails (HHH, TTT) is $\dfrac{2}{8} = \dfrac{1}{4}$.

The probability of getting one head or two heads is $\dfrac{6}{8} = \dfrac{3}{4}$.

Let $X$ be the amount won or lost in a game.

$X = 100$ with probability $\dfrac{1}{4}$

$X = -40$ with probability $\dfrac{3}{4}$

The expected amount is $E(X) = 100 \times \dfrac{1}{4} + (-40) \times \dfrac{3}{4}$.

$E(X) = 25 - 30 = -5$

Since the expected value is negative, the person can expect a loss of ₹ 5 per game.

Answer: 5 loss

</details>

---

### Q72. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A service station manager sells gas at an average of ₹ 100 per hour on a rainy day, ₹ 150 per hour on a dubious day, ₹ 250 per hour on a fair day and ₹ 300 on a clear sky. If weather bureau statistics show the probabilities of weather as follows, then his mathematical expectation is
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/DF-qq4bvAYQYcBOdonAgHjnxXntsPlwIWWOWIaG0zRA.original.fullsize.png"/>

**Options:**

- **(A)** 257.5
- **(B)** 252.5
- **(C)** 250
- **(D)** 247.5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 252.5**

**Detailed Solution:**

Let $X$ be the random variable representing the sales per hour. The probability distribution of $X$ based on the given data is:

$P(X = 300) = 0.50$ (Clear)
$P(X = 250) = 0.30$ (Fair)
$P(X = 150) = 0.15$ (Dubious)
$P(X = 100) = 0.05$ (Rainy)

The mathematical expectation $E(X)$ is given by the formula:
$E(X) = \sum x_i p_i$

Substituting the values:
$E(X) = (300 \times 0.50) + (250 \times 0.30) + (150 \times 0.15) + (100 \times 0.05)$

$E(X) = 150 + 75 + 22.5 + 5$

$E(X) = 252.5$

Therefore, the mathematical expectation is ₹ $252.5$.

Answer: 252.5

</details>

---

### Q73. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A bag contains 4 red and 3 black balls. One ball is drawn and then replaced in the bag and the process is repeated. Let X denote the number of times black ball is drawn in 3 draws. Assuming that at each draw each ball is equally likely to be selected, then probability distribution of X is given by

**Options:**

- **(A)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/itpqdz_BP2UTAq-5btM5y30jpx6_DWp0xyi3QETTGU0.original.fullsize.png"/>
- **(B)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/CgjBa2h9avaaujQ65A74l6bX7uxYvI1Gj-uoWBX4r14.original.fullsize.png"/>
- **(C)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/-iMRfe3pDl6GSZ9fmJ968440LDejWVd_UAk8ZzY0azM.original.fullsize.png"/>
- **(D)** <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/sU2tRZDdcNQRc25H6D4JOltZt_XEAWvhdfh2gQAk10o.original.fullsize.png"/>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/itpqdz_BP2UTAq-5btM5y30jpx6_DWp0xyi3QETTGU0.original.fullsize.png"/>**

**Detailed Solution:**

Total number of balls = $4$ (red) + $3$ (black) = $7$.

Probability of drawing a black ball, $p = \dfrac{3}{7}$.

Probability of drawing a red ball, $q = \dfrac{4}{7}$.

Number of draws, $n = 3$.

Since the balls are replaced after each draw, the draws are independent. Thus, the number of black balls drawn, $X$, follows a binomial distribution.

$P(X = x) = ^{n}C_{x} p^{x} q^{n-x} = ^{3}C_{x} \left(\dfrac{3}{7}\right)^{x} \left(\dfrac{4}{7}\right)^{3-x}$

For $x = 0$: $P(X = 0) = ^{3}C_{0} \left(\dfrac{3}{7}\right)^{0} \left(\dfrac{4}{7}\right)^{3} = \left(\dfrac{4}{7}\right)^{3}$

For $x = 1$: $P(X = 1) = ^{3}C_{1} \left(\dfrac{3}{7}\right)^{1} \left(\dfrac{4}{7}\right)^{2} = 3 \times \dfrac{3}{7} \times \left(\dfrac{4}{7}\right)^{2} = \dfrac{9}{7} \left(\dfrac{4}{7}\right)^{2}$

For $x = 2$: $P(X = 2) = ^{3}C_{2} \left(\dfrac{3}{7}\right)^{2} \left(\dfrac{4}{7}\right)^{1} = 3 \times \left(\dfrac{3}{7}\right)^{2} \times \dfrac{4}{7} = \dfrac{12}{7} \left(\dfrac{3}{7}\right)^{2}$

For $x = 3$: $P(X = 3) = ^{3}C_{3} \left(\dfrac{3}{7}\right)^{3} \left(\dfrac{4}{7}\right)^{0} = \left(\dfrac{3}{7}\right)^{3}$

Comparing these probabilities with the given tables, the first option matches exactly.

Answer: <img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/itpqdz_BP2UTAq-5btM5y30jpx6_DWp0xyi3QETTGU0.original.fullsize.png"/>

</details>

---

### Q74. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A random variable X takes values $-1,0,1,2$ with probabilities $\dfrac{1+3 p}{4}, \dfrac{1-p}{4}, \dfrac{1+2 p}{4}, \dfrac{1-4 p}{4}$ respectively, where p varies over $\mathbb{R}$. Then the minimum and maximum values of the mean of X are respectively.

**Options:**

- **(A)** $-\dfrac{7}{4}$ and $\dfrac{1}{2}$
- **(B)** $-\dfrac{1}{16}$ and $\dfrac{5}{16}$
- **(C)** $-\dfrac{7}{4}$ and $\dfrac{5}{16}$
- **(D)** $-\dfrac{1}{16}$ and $\dfrac{5}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $-\dfrac{1}{16}$ and $\dfrac{5}{4}$**

**Detailed Solution:**

Since the given expressions represent probabilities, they must be non-negative. Thus, we have the following inequalities:

$\dfrac{1+3p}{4} \ge 0 \Rightarrow p \ge -\dfrac{1}{3}$

$\dfrac{1-p}{4} \ge 0 \Rightarrow p \le 1$

$\dfrac{1+2p}{4} \ge 0 \Rightarrow p \ge -\dfrac{1}{2}$

$\dfrac{1-4p}{4} \ge 0 \Rightarrow p \le \dfrac{1}{4}$

Taking the intersection of all these conditions, the valid range for $p$ is:

$p \in \left[-\dfrac{1}{3}, \dfrac{1}{4}\right]$

The mean of the random variable $X$ is given by $E(X) = \sum x_i P(X=x_i)$:

$E(X) = (-1)\left(\dfrac{1+3p}{4}\right) + (0)\left(\dfrac{1-p}{4}\right) + (1)\left(\dfrac{1+2p}{4}\right) + (2)\left(\dfrac{1-4p}{4}\right)$

$E(X) = \dfrac{-1 - 3p + 0 + 1 + 2p + 2 - 8p}{4}$

$E(X) = \dfrac{2 - 9p}{4}$

Since $E(X)$ is a decreasing function of $p$, its minimum value occurs at the maximum value of $p$, and its maximum value occurs at the minimum value of $p$.

For the minimum value, substitute $p = \dfrac{1}{4}$:

$E(X)_{\text{min}} = \dfrac{2 - 9\left(\dfrac{1}{4}\right)}{4} = \dfrac{2 - \dfrac{9}{4}}{4} = -\dfrac{1}{16}$

For the maximum value, substitute $p = -\dfrac{1}{3}$:

$E(X)_{\text{max}} = \dfrac{2 - 9\left(-\dfrac{1}{3}\right)}{4} = \dfrac{2 + 3}{4} = \dfrac{5}{4}$

Therefore, the minimum and maximum values of the mean of $X$ are $-\dfrac{1}{16}$ and \dfrac{5}{4} respectively.

Answer: $-\dfrac{1}{16}$ and $\dfrac{5}{4}$

</details>

---

### Q75. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $X$ is a random variable with distribution given below
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9514v0G5RONoR9l904z7mpOjzsU-VG_z0f97d9nEXxQ.original.fullsize.png"/>
Then the value of $k$ and its variance are respectively given by

**Options:**

- **(A)** $\dfrac{1}{8}, \dfrac{22}{27}$
- **(B)** $\dfrac{1}{8}, \dfrac{23}{27}$
- **(C)** $\dfrac{1}{8}, \dfrac{8}{9}$
- **(D)** $\dfrac{1}{8}, \dfrac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{1}{8}, \dfrac{3}{4}$**

**Detailed Solution:**

The sum of all probabilities in a probability distribution is equal to $1$.

$\sum P(X = x_i) = 1$

$k + 3k + 3k + k = 1$

$8k = 1 \Rightarrow k = \dfrac{1}{8}$

The expected value (mean) of $X$ is given by $E(X) = \sum x_i P(X = x_i)$.

$E(X) = 0 \cdot k + 1 \cdot 3k + 2 \cdot 3k + 3 \cdot k = 12k$

Substituting $k = \dfrac{1}{8}$, we get $E(X) = 12 \times \dfrac{1}{8} = \dfrac{3}{2}$.

Now, calculate $E(X^2) = \sum x_i^2 P(X = x_i)$.

$E(X^2) = 0^2 \cdot k + 1^2 \cdot 3k + 2^2 \cdot 3k + 3^2 \cdot k = 0 + 3k + 12k + 9k = 24k$

Substituting $k = \dfrac{1}{8}$, we get $E(X^2) = 24 \times \dfrac{1}{8} = 3$.

The variance of $X$ is given by $Var(X) = E(X^2) - [E(X)]^2$.

$Var(X) = 3 - \left(\dfrac{3}{2}\right)^2 = 3 - \dfrac{9}{4} = \dfrac{12 - 9}{4} = \dfrac{3}{4}$

Thus, the value of $k$ is $\dfrac{1}{8}$ and its variance is $\dfrac{3}{4}$.

Answer: $\dfrac{1}{8}, \dfrac{3}{4}$

</details>

---

### Q76. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The expected value of the sum of the two numbers obtained on the uppermost faces, when two fair dice are rolled, is

**Options:**

- **(A)** 7
- **(B)** 12
- **(C)** 6
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 7**

**Detailed Solution:**

Let $X$ and $Y$ be the random variables representing the numbers on the first and second dice respectively.

The expected value of the number on a single fair die is given by

$E(X) = \sum_{i=1}^{6} x_i P(x_i) = 1\left(\dfrac{1}{6}\right) + 2\left(\dfrac{1}{6}\right) + 3\left(\dfrac{1}{6}\right) + 4\left(\dfrac{1}{6}\right) + 5\left(\dfrac{1}{6}\right) + 6\left(\dfrac{1}{6}\right)$

$E(X) = \dfrac{1 + 2 + 3 + 4 + 5 + 6}{6} = \dfrac{21}{6} = \dfrac{7}{2}$

Similarly, for the second die, $E(Y) = \dfrac{7}{2}$.

By the linearity of expectation, the expected value of the sum is

$E(X + Y) = E(X) + E(Y) = \dfrac{7}{2} + \dfrac{7}{2} = 7$

Answer: 7

</details>

---

### Q77. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If $\mathrm{P}(\mathrm{X}=2)=0.3, \mathrm{P}(\mathrm{X}=3)=0.4, \mathrm{P}(\mathrm{X}=4)=0.3$, then the variance of random variable X is

**Options:**

- **(A)** 1.6
- **(B)** 6.6
- **(C)** 3.6
- **(D)** 0.6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.6**

**Detailed Solution:**

The mean of the random variable $X$ is given by $E(X) = \sum x_i P(x_i)$

$E(X) = 2(0.3) + 3(0.4) + 4(0.3) = 0.6 + 1.2 + 1.2 = 3$

The expected value of $X^2$ is given by $E(X^2) = \sum x_i^2 P(x_i)$

$E(X^2) = 2^2(0.3) + 3^2(0.4) + 4^2(0.3) = 4(0.3) + 9(0.4) + 16(0.3) = 1.2 + 3.6 + 4.8 = 9.6$

The variance of $X$ is given by $Var(X) = E(X^2) - [E(X)]^2$

$Var(X) = 9.6 - (3)^2 = 9.6 - 9 = 0.6$

Answer: 0.6

</details>

---

### Q78. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable has the following probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/R3VDDxctbERF4Nm-dgeAZr0800nQ_SqWoTAVt0ZtqGI.original.fullsize.png"/>
The then value of $p$ is

**Options:**

- **(A)** $\dfrac{1}{10}$
- **(B)** $\dfrac{1}{30}$
- **(C)** $\dfrac{1}{100}$
- **(D)** $\dfrac{3}{20}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\dfrac{1}{10}$**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities must be equal to $1$.

$\sum P(x) = 1$

Substituting the given probabilities from the table:

$0 + 2p + 2p + 3p + p^2 + 2p^2 + 7p^2 + 2p = 1$

Combining the like terms, we get:

$10p^2 + 9p = 1$

$10p^2 + 9p - 1 = 0$

$10p^2 + 10p - p - 1 = 0$

$10p(p + 1) - 1(p + 1) = 0$

$(10p - 1)(p + 1) = 0$

This gives $p = \dfrac{1}{10}$ or $p = -1$.

Since probability cannot be negative, $p \ge 0$.

Therefore, $p = \dfrac{1}{10}$.

Answer: $\dfrac{1}{10}$

</details>

---

### Q79. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Two cards are drawn successively with replacement from a well shuffled pack of 52 cards. Let X denote the random variable of number of jacks obtained in the two drawn cards. Then $\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2)$ equals

**Options:**

- **(A)** $\dfrac{24}{169}$
- **(B)** $\dfrac{52}{169}$
- **(C)** $\dfrac{25}{169}$
- **(D)** $\dfrac{49}{169}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{25}{169}$**

**Detailed Solution:**

Probability of drawing a jack in a single draw, $p = \dfrac{4}{52} = \dfrac{1}{13}$

Probability of not drawing a jack, $q = 1 - p = \dfrac{12}{13}$

Since the cards are drawn with replacement, the number of jacks $X$ follows a binomial distribution with $n = 2$ and $p = \dfrac{1}{13}$.

We need to find $P(X=1) + P(X=2)$.

$P(X=1) = ^{2}C_{1} p^{1} q^{1} = 2 \times \dfrac{1}{13} \times \dfrac{12}{13} = \dfrac{24}{169}$

$P(X=2) = ^{2}C_{2} p^{2} q^{0} = 1 \times \left(\dfrac{1}{13}\right)^{2} = \dfrac{1}{169}$

$P(X=1) + P(X=2) = \dfrac{24}{169} + \dfrac{1}{169} = \dfrac{25}{169}$

Alternatively, $P(X=1) + P(X=2) = 1 - P(X=0) = 1 - ^{2}C_{0} q^{2} = 1 - \left(\dfrac{12}{13}\right)^{2} = 1 - \dfrac{144}{169} = \dfrac{25}{169}$

Answer: $\dfrac{25}{169}$

</details>

---

### Q80. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A person throws an unbiased die. If the number shown is even, he gains an amount equal to the number shown: If the number is odd, he loses an amount equal to the number shown. Then his expectation is ₹.

**Options:**

- **(A)** 1
- **(B)** 1.5
- **(C)** 2
- **(D)** 0.5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0.5**

**Detailed Solution:**

Let $X$ be the random variable representing the amount gained or lost.

The possible outcomes of throwing an unbiased die are $1, 2, 3, 4, 5, 6$, each with a probability of $\dfrac{1}{6}$.

For even numbers ($2, 4, 6$), the person gains the amount, so $X$ takes values $2, 4, 6$.

For odd numbers ($1, 3, 5$), the person loses the amount, so $X$ takes values $-1, -3, -5$.

The expected value $E(X)$ is given by:

$E(X) = \sum X_i P(X_i)$

$E(X) = (-1)\left(\dfrac{1}{6}\right) + (2)\left(\dfrac{1}{6}\right) + (-3)\left(\dfrac{1}{6}\right) + (4)\left(\dfrac{1}{6}\right) + (-5)\left(\dfrac{1}{6}\right) + (6)\left(\dfrac{1}{6}\right)$

$E(X) = \dfrac{-1 + 2 - 3 + 4 - 5 + 6}{6}$

$E(X) = \dfrac{3}{6} = 0.5$

Answer: 0.5

</details>

---

### Q81. MHT CET 2024 (03 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $x$ has the following probability distribution. Then value of $k$ is and $\mathrm{P}(3 \lt x \leq 6)$ has the value
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/ID6w5-a5K39L_juMYQAggdko-hVNzHt96QoSkfeM_XQ.original.fullsize.png"/>

**Options:**

- **(A)** $\dfrac{1}{20}, \dfrac{3}{7}$
- **(B)** $\dfrac{5}{21}, \dfrac{3}{7}$
- **(C)** $\dfrac{1}{21}, \dfrac{3}{7}$
- **(D)** $\dfrac{1}{20}, \dfrac{4}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{1}{21}, \dfrac{3}{7}$**

**Detailed Solution:**

For a valid probability distribution, the sum of all probabilities must be equal to $1$.

$\sum P(x) = 1$

$k + 2k + 3k + 4k + 4k + 3k + 2k + k + k = 1$

$21k = 1$

$k = \dfrac{1}{21}$

Now, we need to find the value of $P(3 < x \leq 6)$. The possible values of $x$ in this range are $4, 5,$ and $6$.

$P(3 < x \leq 6) = P(x=4) + P(x=5) + P(x=6)$

$P(3 < x \leq 6) = 4k + 3k + 2k = 9k$

Substituting the value of $k = \dfrac{1}{21}$:

$P(3 < x \leq 6) = 9 \times \dfrac{1}{21} = \dfrac{9}{21} = \dfrac{3}{7}$

Answer: $\dfrac{1}{21}, \dfrac{3}{7}$

</details>

---

### Q82. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $X$ has the following probability distribution
\(\begin{array}{|c|c|c|c|c|c|} \hline \mathrm{X} & 0 & 1 & 2 & 3 & 4 \\ \hline \mathrm{P}(\mathrm{x}) & 0 & 0.2 & 0.4 & 0.3 & 0.1 \\ \hline \end{array}\)
The mean and variance of X are respectively

**Options:**

- **(A)** $2.3$ and $6.1$
- **(B)** $2.3$ and $0.81$
- **(C)** $2.3$ and $0.1$
- **(D)** $2.3$ and $0.9$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2.3$ and $0.81$**

**Detailed Solution:**

The mean of the random variable $X$ is given by $\mu = \sum x_i P(x_i)$

$\mu = 0(0) + 1(0.2) + 2(0.4) + 3(0.3) + 4(0.1)$

$\mu = 0 + 0.2 + 0.8 + 0.9 + 0.4 = 2.3$

The variance of $X$ is given by $\sigma^2 = \sum x_i^2 P(x_i) - \mu^2$

$\sum x_i^2 P(x_i) = 0^2(0) + 1^2(0.2) + 2^2(0.4) + 3^2(0.3) + 4^2(0.1)$

$\sum x_i^2 P(x_i) = 0 + 0.2 + 1.6 + 2.7 + 1.6 = 6.1$

$\sigma^2 = 6.1 - (2.3)^2$

$\sigma^2 = 6.1 - 5.29 = 0.81$

Answer: $2.3$ and $0.81$

</details>

---

### Q83. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability distribution of a random variable X is given by
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/OLIJ-NtXroOs1MlyHZsVsFdA_nzzaTw6rQBIAvkGvaI.original.fullsize.png"/>
Then the variance of X is

**Options:**

- **(A)** 1.76
- **(B)** 2.45
- **(C)** 3.2
- **(D)** 4.8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1.76**

**Detailed Solution:**

The mean of the random variable $X$ is given by:

$E(X) = \sum x_i P(x_i)$

$E(X) = 0(0.4) + 1(0.3) + 2(0.1) + 3(0.1) + 4(0.1)$

$E(X) = 0 + 0.3 + 0.2 + 0.3 + 0.4 = 1.2$

The expected value of $X^2$ is given by:

$E(X^2) = \sum x_i^2 P(x_i)$

$E(X^2) = 0^2(0.4) + 1^2(0.3) + 2^2(0.1) + 3^2(0.1) + 4^2(0.1)$

$E(X^2) = 0 + 0.3 + 0.4 + 0.9 + 1.6 = 3.2$

The variance of $X$ is:

$Var(X) = E(X^2) - [E(X)]^2$

$Var(X) = 3.2 - (1.2)^2$

$Var(X) = 3.2 - 1.44 = 1.76$

Answer: 1.76

</details>

---

### Q84. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If a discrete random variable $X$ takes values $0,1,2,3, \ldots \ldots .$. with probability $\mathrm{P}(\mathrm{X}=x)=\mathrm{k}(x+1) 5^{-x}$, where k is a constant, then $\mathrm{P}(\mathrm{X}=0)$ is

**Options:**

- **(A)** $\dfrac{7}{25}$
- **(B)** $\dfrac{16}{25}$
- **(C)** $\dfrac{18}{25}$
- **(D)** $\dfrac{19}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{16}{25}$**

**Detailed Solution:**

The sum of all probabilities for a discrete random variable is equal to $1$.

$\sum_{x=0}^{\infty} \mathrm{P}(\mathrm{X}=x) = 1$

$\sum_{x=0}^{\infty} \mathrm{k}(x+1)5^{-x} = 1$

Let $S = \sum_{x=0}^{\infty} (x+1)5^{-x} = 1 + \dfrac{2}{5} + \dfrac{3}{5^2} + \dfrac{4}{5^3} + \ldots$

Multiplying by $\dfrac{1}{5}$:

$\dfrac{1}{5}S = \dfrac{1}{5} + \dfrac{2}{5^2} + \dfrac{3}{5^3} + \ldots$

Subtracting the second equation from the first:

$S - \dfrac{1}{5}S = 1 + \dfrac{1}{5} + \dfrac{1}{5^2} + \dfrac{1}{5^3} + \ldots$

$\dfrac{4}{5}S = \dfrac{1}{1 - \dfrac{1}{5}}$

$\dfrac{4}{5}S = \dfrac{5}{4}$

$S = \dfrac{25}{16}$

Since $\mathrm{k}S = 1$, we get $\mathrm{k} = \dfrac{16}{25}$.

The probability at $x=0$ is:

$\mathrm{P}(\mathrm{X}=0) = \mathrm{k}(0+1)5^{-0} = \mathrm{k} = \dfrac{16}{25}$

Answer: $\dfrac{16}{25}$

</details>

---

### Q85. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The p.m.f. of a random variable $\mathrm{X}$ is $\mathrm{P}(x)=\left\{\begin{array}{cl}\frac{2 x}{\mathrm{n}(\mathrm{n}+1)} & , \quad x=1,2,3, \ldots \mathrm{n} \\ 0 & , \text { otherwise }\end{array}\right.$, then $\mathrm{E}(\mathrm{X})$ is

**Options:**

- **(A)** $\frac{\mathrm{n}+1}{6}$
- **(B)** $\frac{\mathrm{2n}+1}{6}$
- **(C)** $\frac{\mathrm{n}+1}{3}$
- **(D)** $\frac{\mathrm{2n}+1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{\mathrm{2n}+1}{3}$**

**Detailed Solution:**

\begin{array}{|l|c|c|c|c|c|}
\hlineX & 1 & 2 & 3 & \ldots & n \\
\hlineP(X) & \frac{2}{n(n+1)} & \frac{4}{n(n+1)} & \frac{6}{n(n+1)} & \cdots & \frac{2 n}{n(n+1)} \\
\hline
\end{array}
$\begin{aligned} \mathrm{E}(\mathrm{X}) & =\sum x_{\mathrm{i}} \cdot \mathrm{P}\left(x_{\mathrm{i}}\right) \\ & =1 \cdot \frac{2}{\mathrm{n}(\mathrm{n}+1)}+2 \cdot \frac{4}{\mathrm{n}(\mathrm{n}+1)}+3 \cdot \frac{6}{\mathrm{n}(\mathrm{n}+1)} \\ & +\ldots+\mathrm{n} \cdot \frac{2 \mathrm{n}}{\mathrm{n}(\mathrm{n}+1)} \\ & =\frac{2}{\mathrm{n}(\mathrm{n}+1)}\left(1+4+9+\ldots+\mathrm{n}^2\right) \\ & =\frac{2}{\mathrm{n}(\mathrm{n}+1)}\left(1^2+2^2+3^2+\ldots+\mathrm{n}^2\right) \\ & =\frac{2}{\mathrm{n}(\mathrm{n}+1)} \cdot \frac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6} \\ & =\frac{2 \mathrm{n}+1}{3}\end{aligned}$

</details>

---

### Q86. MHT CET 2023 (14 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A fair die with numbers 1 to 6 on their faces is thrown. Let $\mathrm{X}$ denote the number of factors of the number, on the uppermost face, then the probability distribution of $\mathrm{X}$ is

**Options:**

- **(A)** \begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{6} & \frac{1}{2} & \frac{1}{6} & \frac{1}{6} \\
\hline
\end{array}
- **(B)** \begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} & \frac{1}{2} \\
\hline
\end{array}
- **(C)** \begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{2} & \frac{1}{6} & \frac{1}{6} & \frac{1}{6} \\
\hline
\end{array}
- **(D)** \begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{6} & \frac{1}{6} & \frac{1}{2} & \frac{1}{6} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{6} & \frac{1}{2} & \frac{1}{6} & \frac{1}{6} \\
\hline
\end{array}**

**Detailed Solution:**

$S=\{1,2,3,4,5,6\}$
The values of $\mathrm{X}$ for the possible outcomes of the experiment are as follows:
$\begin{aligned}
& X(1)=1, X(2)=2, X(3)=2, X(4)=3 \\
& X(5)=2, X(6)=4 \\
& P(X=1)=P[\{1\}]=\frac{1}{6} \\
& P(X=2)=P[\{2,3,5\}]=\frac{3}{6}=\frac{1}{2} \\
& P(X=3)=P[\{4\}]=\frac{1}{6} \\
& P(X=4)=P[\{6\}]=\frac{1}{6}
\end{aligned}$
The probability distribution of $\mathrm{X}$ is
\begin{array}{|l|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{6} & \frac{1}{2} & \frac{1}{6} & \frac{1}{6} \\
\hline
\end{array}

</details>

---

### Q87. MHT CET 2023 (14 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{f}(x)= \begin{cases}3\left(1-2 x^2\right) & ; 0 < x < 1 \\ 0 & ; \text { otherwise }\end{cases}$ is a probability density function of $\mathrm{X}$, then $\mathrm{P}\left(\frac{1}{4} < x < \frac{1}{3}\right)$ is

**Options:**

- **(A)** $\frac{75}{243}$
- **(B)** $\frac{23}{96}$
- **(C)** $\frac{179}{864}$
- **(D)** $\frac{52}{243}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{179}{864}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}\left(\frac{1}{4} < x < \frac{1}{3}\right)= & \int_{\frac{1}{4}}^{\frac{1}{3}} \mathrm{f}(x) \mathrm{d} x=\int_{\frac{1}{4}}^{\frac{1}{3}} 3\left(1-2 x^2\right) \mathrm{d} x \\ & =\left[3 x-2 x^3\right]_{\frac{1}{4}}^{\frac{1}{3}} \\ & =\left(1-\frac{2}{27}\right)-\left(\frac{3}{4}-\frac{1}{32}\right) \\ & =\frac{1}{4}+\frac{1}{32}-\frac{2}{27} \\ & =\frac{179}{864}\end{aligned}$

</details>

---

### Q88. MHT CET 2023 (13 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $\mathrm{X}$ has the probability distribution
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline \mathrm{P}(\mathrm{X}=x) & 0.15 & 0.23 & 0.12 & 0.20 & 0.08 & 0.10 & 0.05 & 0.07 \\\hline\end{array}
For the events $\mathrm{E}=\{\mathrm{X}$ is a prime number $\}$ and $\mathrm{F}=\{x < 5\}, \mathrm{P}(\mathrm{E} \cup \mathrm{F})$ is

**Options:**

- **(A)** 0.63
- **(B)** 0.75
- **(C)** 0.83
- **(D)** 0.90

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.83**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}(\mathrm{E})= & \mathrm{P}(\mathrm{X}=2 \text { or } \mathrm{X}=3 \text { or } \mathrm{X}=5 \text { or } \mathrm{X}=7) \\ = & \mathrm{P}(\mathrm{X}=2)+\mathrm{P}(\mathrm{X}=3)+\mathrm{P}(\mathrm{X}=5) \\ & +\mathrm{P}(\mathrm{X}=7)\end{aligned}$
$\begin{aligned} & =0.15+0.23+0.12+0.20 \\ & =0.7\end{aligned}$
$\begin{aligned} \mathrm{P}(\mathrm{E} \cap \mathrm{F}) & =\mathrm{P}(\mathrm{X} \text { is a prime number less than } 5) \\ & =\mathrm{P}(\mathrm{X}=2)+\mathrm{P}(\mathrm{X}=3) \\ & =0.23+0.12 \\ & =0.35 \\ \mathrm{P}(\mathrm{E} \cup \mathrm{F}) & =\mathrm{P}(\mathrm{E})+\mathrm{P}(\mathrm{F})-\mathrm{P}(\mathrm{E} \cap \mathrm{F}) \\ & =0.48+0.7-0.35 \\ & =0.83\end{aligned}$

</details>

---

### Q89. MHT CET 2023 (13 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $\mathrm{X}$ has the following probability distribution
\begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & 4 \mathrm{k}-10 \mathrm{k}^2 & 5 \mathrm{k}-1 & 3 \mathrm{k}^3 \\
\hline
\end{array} then $\mathrm{P}(\mathrm{X} < 2)$ is

**Options:**

- **(A)** $\frac{2}{9}$
- **(B)** $\frac{5}{9}$
- **(C)** $\frac{8}{9}$
- **(D)** $\frac{4}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{8}{9}$**

**Detailed Solution:**

$\begin{aligned} & \text { Since } \sum_{x=0}^2 \mathrm{P}(\mathrm{X}=x)=1 \\ & 4 \mathrm{k}-10 \mathrm{k}^2+5 \mathrm{k}-1+3 \mathrm{k}^3=1 \\ & \Rightarrow 3 \mathrm{k}^3-10 \mathrm{k}^2+9 \mathrm{k}-2=0 \\ & \Rightarrow(\mathrm{k}-1)(\mathrm{k}-2)(3 \mathrm{k}-1)=0 \\ & \Rightarrow \mathrm{k}=1 \text { or } \mathrm{k}=2 \text { or } \mathrm{k}=\frac{1}{3} \\ & \begin{aligned} & \text { For } \mathrm{k}=1 \text { or } \mathrm{k}=2 \\ & \mathrm{P}(\mathrm{X}=0) < 0, \text { which is not possible } \\ & \mathrm{k}=\frac{1}{3} \quad\end{aligned} \\ & \begin{aligned} \text { Now, } \mathrm{P}(\mathrm{X} < 2) & =\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1) \\ & =4 \mathrm{k}-10 \mathrm{k}^2+5 \mathrm{k}-1 \\ & =9 \mathrm{k}-10 \mathrm{k}^2-1 \\ & =9\left(\frac{1}{3}\right)-10\left(\frac{1}{9}\right)-1 \\ & =\frac{8}{9}\end{aligned}\end{aligned}$

</details>

---

### Q90. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Three fair coins with faces numbered 1 and 0 are tossed simultaneously. Then variance $(\mathrm{X})$ of the probability distribution of random variable $\mathrm{X}$, where $\mathrm{X}$ is the sum of numbers on the upper most faces, is

**Options:**

- **(A)** $0.7$
- **(B)** $0.75$
- **(C)** $0.65$
- **(D)** $0.6$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.75$**

**Detailed Solution:**

Possible value of $\mathrm{X}$ are $0,1,2,3$ Here,
$\mathrm{S}=\{000,001,010,1,00,111,110,101,011\}$
$\mathrm{n}(\mathrm{S})=8$
$$
\begin{aligned}
& \therefore \mathrm{E}(\mathrm{X})=\sum x_{\mathrm{i}} \mathrm{p}_{\mathrm{i}}=0+\frac{3}{8}+\frac{6}{8}+\frac{3}{8}=\frac{12}{8} \\
& \mathrm{E}\left(\mathrm{X}^2\right)= \\
& \therefore \quad \sum x_{\mathrm{i}}^2 \mathrm{p}_{\mathrm{i}}^2=0+\frac{3}{8}+\frac{12}{8}+\frac{9}{8}=\frac{24}{8} \\
& \quad=3-\left(\frac{3}{2}\right)^2 \\
& =3-\frac{9}{4} \\
& =\frac{3}{4} \\
& =0.75
\end{aligned}
$$

</details>

---

### Q91. MHT CET 2023 (12 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The discrete random variable $\mathrm{X}$ can take all possible integer values from 1 to $\mathrm{k}$, each with a probability $\frac{1}{\mathrm{k}}$, then its variance is

**Options:**

- **(A)** $\frac{\mathrm{k}^2-1}{12}$
- **(B)** $\frac{\mathrm{k}^2-1}{6}$
- **(C)** $\frac{\mathrm{k}^2+1}{12}$
- **(D)** $\frac{\mathrm{k}^2+1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{k}^2-1}{12}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/eCy2k0IadFcD0_0nJ5bnjDLkAPfXvH0uiQFIe2iJXME.original.fullsize.png">

$\begin{aligned} & \mathrm{E}(\mathrm{X})=\sum_{\mathrm{i}=1}^{\mathrm{k}} x_{\mathrm{i}} \mathrm{p}_{\mathrm{i}}=\frac{1}{\mathrm{k}}+\frac{2}{\mathrm{k}}+\ldots+\frac{\mathrm{k}}{\mathrm{k}}=\frac{\mathrm{k}+1}{2} \\ & \mathrm{E}\left(\mathrm{X}^2\right)=\sum_{\mathrm{i}=1}^{\mathrm{k}} x_{\mathrm{i}}^2 \mathrm{p}_{\mathrm{i}}=\frac{1^2+2^2+3^2+\ldots+\mathrm{k}^2}{\mathrm{k}} \\ & =\frac{(\mathrm{k}+1)(2 \mathrm{k}+1)}{6} \\ & \therefore \quad \text { Variance }=\mathrm{E}\left(\mathrm{X}^2\right)-[\mathrm{E}(\mathrm{X})]^2 \\ & =\frac{2 \mathrm{k}^2+3 \mathrm{k}+1}{6}-\frac{\mathrm{k}^2+2 \mathrm{k}+1}{4} \\ & \end{aligned}$
$\begin{aligned} & =\frac{4 \mathrm{k}^2+6 \mathrm{k}+2-3 \mathrm{k}^2-6 \mathrm{k}-3}{12} \\ & =\frac{\mathrm{k}^2-1}{12}\end{aligned}$

</details>

---

### Q92. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn successively with replacement from a well shuffled pack of 52 cards. Then the probability distribution of number of jacks is

**Options:**

- **(A)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{144}{169} & \frac{24}{169} & \frac{1}{169} \\
\hline
\end{array}
- **(B)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{169} & \frac{144}{169} & \frac{24}{169} \\
\hline
\end{array}
- **(C)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{24}{169} & \frac{1}{169} & \frac{144}{169} \\
\hline
\end{array}
- **(D)** \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{144}{169} & \frac{1}{169} & \frac{24}{169} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{144}{169} & \frac{24}{169} & \frac{1}{169} \\
\hline
\end{array}**

**Detailed Solution:**

Let $\mathrm{X}$ denotes the number of jacks
$\therefore \quad$ Possible values of $\mathrm{X}$ are $0,1,2$
$$
\therefore \quad \mathrm{P}(\mathrm{X}=0)=\frac{{ }^{48} \mathrm{C}_1 \times{ }^{48} \mathrm{C}_1}{{ }^{52} \mathrm{C}_1 \times{ }^{52} \mathrm{C}_1}=\frac{144}{169}
$$
$$
\begin{aligned}
& \mathrm{P}(\mathrm{X}=1)=\frac{{ }^{48} \mathrm{C}_1 \times{ }^4 \mathrm{C}_1}{{ }^{52} \mathrm{C}_1 \times{ }^{52} \mathrm{C}_1}+\frac{{ }^4 \mathrm{C}_1 \times{ }^{52} \mathrm{C}_1}{{ }^{52} \mathrm{C}_1 \times{ }^{52} \mathrm{C}_1}=\frac{24}{169} \\
& \mathrm{P}(\mathrm{X}=2)=\frac{{ }^4 \mathrm{C}_1 \times{ }^4 \mathrm{C}_1}{{ }^{52} \mathrm{C}_1 \times{ }^{52} \mathrm{C}_1}=\frac{1}{169}
\end{aligned}
$$
$\therefore \quad$ Option (A) is correct.

</details>

---

### Q93. MHT CET 2023 (12 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The p.m.f of random variate $\mathrm{X}$ is
$$
\mathrm{P}(\mathrm{X})= \begin{cases}\frac{2 x}{\mathrm{n}(\mathrm{n}+1)}, & x=1,2,3, \ldots \ldots, \mathrm{n} \\ 0, & \text { otherwise }\end{cases}
$$
Then $E(X)=$

**Options:**

- **(A)** $\frac{\mathrm{n}+1}{3}$
- **(B)** $\frac{2 \mathrm{n}+1}{3}$
- **(C)** $\frac{\mathrm{n}+2}{3}$
- **(D)** $\frac{2 \mathrm{n}-1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2 \mathrm{n}+1}{3}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}(\mathrm{X}) & =\left\{\begin{array}{l}\frac{2 x}{\mathrm{n}(\mathrm{n}+1)}, x=1,2,3, \ldots, \mathrm{n} \\ 0, \text { othewise }\end{array}\right. \\ \therefore \quad \mathrm{E}(\mathrm{X}) & =\sum_{\mathrm{i}=1}^{\mathrm{n}} x_{\mathrm{i}} \mathrm{p}\left(x_{\mathrm{i}}\right) \\ & =\frac{2}{\mathrm{n}(\mathrm{n}+1)}+\frac{8}{\mathrm{n}(\mathrm{n}+1)}+\ldots+\frac{2 \mathrm{n}^2}{\mathrm{n}(\mathrm{n}+1)} \\ & =\frac{2\left(1^2+2^2+\ldots+\mathrm{n}^2\right)}{\mathrm{n}(\mathrm{n}+1)} \\ & =\frac{2 \mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6 \mathrm{n}(\mathrm{n}+1)} \\ & =\frac{2 \mathrm{n}+1}{3}\end{aligned}$

</details>

---

### Q94. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let a random variable $\mathrm{X}$ have a Binomial distribution with mean 8 and variance 4 . If $P(X \leq 2)=\frac{K}{2^{16}}$, then $K$ is

**Options:**

- **(A)** $17$
- **(B)** $121$
- **(C)** $136$
- **(D)** $137$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $137$**

**Detailed Solution:**

Let $\mathrm{X} \sim \mathrm{B}(\mathrm{n}, \mathrm{p})$
According to the given conditions, Mean $=n p=8$ and variance $=n p q=4$ $\Rightarrow \mathrm{p}=\mathrm{q}=\frac{1}{2}$ and $\mathrm{n}=16$
$P(X \leq 2)=\frac{K}{2^{16}}$
$\Rightarrow \mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2)=\frac{\mathrm{K}}{2^{16}}$
$\begin{aligned}
\therefore \quad{ }^{16} \mathrm{C}_0\left(\frac{1}{2}\right)^0\left(\frac{1}{2}\right)^{16}+{ }^{16} \mathrm{C}_1\left(\frac{1}{2}\right)^1 & \left(\frac{1}{2}\right)^{15} \\
& +{ }^{16} \mathrm{C}_2\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^{14}=\frac{\mathrm{K}}{2^{16}}
\end{aligned}$
$\begin{array}{ll}
\therefore & \frac{1+16+120}{2^{16}}=\frac{K}{2^{16}} \\
\therefore & K=137
\end{array}$

</details>

---

### Q95. MHT CET 2023 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A fair die is tossed twice in succession. If $\mathrm{X}$ denotes the number of fours in two tosses, then the probability distribution of $\mathrm{X}$ is given by

**Options:**

- **(A)** \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{1}{36} & \frac{25}{36} & \frac{5}{18} \\
\hline
\end{array}
- **(B)** \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{25}{36} & \frac{1}{36} & \frac{5}{18} \\
\hline
\end{array}
- **(C)** \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{25}{36} & \frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}
- **(D)** \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{5}{18} & \frac{1}{36} & \frac{25}{36} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{25}{36} & \frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}**

**Detailed Solution:**

A fair die is tossed twice in succession.
$\therefore \quad$ Sample space (S)
$\begin{aligned}
= & (1,1),(1,2),(1,3),(1,4),(1,5),(1,6), \\
& (2,1),(2,2),(2,3),(2,4),(2,5),(2,6), \\
& (3,1),(3,2),(3,3),(3,4),(3,5),(3,6), \\
& (4,1),(4,2),(4,3),(4,4),(4,5),(4,6), \\
& (5,1),(5,2),(5,3),(5,4),(5,5),(5,6), \\
& (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)\}
\end{aligned}$
$X:$ Number of fours in two tosses.
$\therefore \quad$ Possible values of $\mathrm{X}$ are: $0,1,2$.
$\therefore \quad$ Probability distribution of $\mathrm{X}$ is as follows:
\begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x_{\mathrm{i}} & 0 & 1 & 2 \\
\hline \mathrm{P}_{\mathrm{i}} & \frac{25}{36} & \frac{10}{36}=\frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}

</details>

---

### Q96. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A binomial random variable $\mathrm{X}$ satisfies 9.p $(\mathrm{X}=4)=\mathrm{p}(\mathrm{X}=2)$ when $\mathrm{n}=6$. Then $\mathrm{p}$ is equal to

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{4}$**

**Detailed Solution:**

$\begin{aligned} & \text { 9. } p(X=4)=p(X=2) \text { and } n=6 \\ & \Rightarrow 9 \times{ }^6 C_4 p^4 q^2={ }^6 C_2 p^2 q^4 \\ & \Rightarrow 9 p^2=q^2 \\ & \Rightarrow 3 p=q \\ & \Rightarrow 3 p=1-p \\ & \Rightarrow p=\frac{1}{4}\end{aligned}$

</details>

---

### Q97. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

From a lot of 20 baskets, which includes 6 defective baskets, a sample of 2 baskets is drawn at random one by one without replacement. The expected value of number of defective basket is

**Options:**

- **(A)** $0.6$
- **(B)** $0.06$
- **(C)** $0.006$
- **(D)** $1.07$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $0.6$**

**Detailed Solution:**

Let $\mathrm{X}$ denotes the number of defective baskets.
$\therefore \quad$ Possible values of $\mathrm{X}$ are $0,1,2$.
Now, selection of baskets is done without replacement, we get
$$
P(X=0)=\frac{14}{20} \times \frac{13}{19}=\frac{182}{380}
$$

</details>

---

### Q98. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A fair die is tossed twice in succession. If $\mathrm{X}$ denotes the number of sixes in two tosses, then the probability distribution of $\mathrm{X}$ is given by

**Options:**

- **(A)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{25}{36} & \frac{1}{36} & \frac{5}{18} \\
\hline
\end{array}
- **(B)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{5}{18} & \frac{1}{36} & \frac{25}{36} \\
\hline
\end{array}
- **(C)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{25}{36} & \frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}
- **(D)** \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{5}{18} & \frac{25}{36} & \frac{1}{36} \\
\hline
\end{array}

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) \begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{25}{36} & \frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}**

**Detailed Solution:**

$\mathrm{X}$ can take values 0,1 and 2 .
$P(X=0)=$ Probability of not getting six $=\frac{25}{36}$
$\mathrm{P}(\mathrm{X}=1)=$ Probability of getting one six
$=\frac{10}{36}=\frac{5}{18}$
$P(X=2)=$ Probability of getting two sixes $=\frac{1}{36}$
The probability distribution of $\mathrm{X}$ is
\begin{array}{|l|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{25}{36} & \frac{5}{18} & \frac{1}{36} \\
\hline
\end{array}

</details>

---

### Q99. MHT CET 2023 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of mean and variance of a Binomial Distribution is $\frac{15}{2}$ for 10 trials, then the variance is

**Options:**

- **(A)** $1.5$
- **(B)** $2.5$
- **(C)** $4.5$
- **(D)** $3.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2.5$**

**Detailed Solution:**

$\begin{array}{ll} & \text { Mean }+ \text { variance }=\frac{15}{2} \\ & \Rightarrow n p+n p q=\frac{15}{2} \\ & \Rightarrow n p+n p(1-p)=\frac{15}{2} \quad \ldots[\because p+q=1] \\ & \Rightarrow n\left(2 p-p^2\right)=\frac{15}{2} \\ & \Rightarrow 2 p-p^2=\frac{15}{2 \times 10} \quad \ldots[n=10] \\ & \Rightarrow 4 p^2-8 p+3=0 \\ & \Rightarrow(2 p-3)(2 p-1)=0 \\ & \Rightarrow p=\frac{3}{2} \text { or } p=\frac{1}{2} \\ & p=\frac{1}{2}...[0 < p < 1] \\ & q=1-\frac{1}{2}=\frac{1}{2} \\ & \text { Variance }=n p q=10 \times \frac{1}{2} \times \frac{1}{2}=2.5\end{array}$

</details>

---

### Q100. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A player tosses 2 fair coins. He wins $₹ 5$ if 2 heads appear, ₹ 2 if one head appears and ₹ 1 if no head appears. Then the variance of his winning amount in $₹$ is

**Options:**

- **(A)** 6
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{9}{4}$
- **(D)** $\frac{17}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{9}{4}$**

**Detailed Solution:**

When player tosses 2 fair coins, then $\mathrm{S}=\{\mathrm{HH}, \mathrm{HT}, \mathrm{TH}, \mathrm{TT}\}$
Let $\mathrm{X}$ be a random variable that denotes the amount received by player.
Then, $X$ can take values 5,2 and 1
Now, $\mathrm{P}(\mathrm{X}=5)=\frac{1}{4}, \mathrm{P}(\mathrm{X}=2)=\frac{1}{2}$ and $\mathrm{P}(\mathrm{X}=1)=\frac{1}{4}$
$\therefore \quad$ The probability distribution of $\mathrm{X}$ is as follows:
\begin{array}{|c|c|c|c|}
\hline \mathrm{X} & 5 & 2 & 1 \\
\hline \mathrm{P}(\mathrm{X}) & \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\
\hline
\end{array}
$\begin{aligned}
\text { Variance of } \mathrm{X} & =\sum \mathrm{X}^2 \mathrm{P}(\mathrm{X})-[\Sigma \mathrm{XP}(\mathrm{X})]^2 \\
& =\left[\frac{25}{4}+2+\frac{1}{4}\right]-\left[\frac{5}{4}+1+\frac{1}{4}\right]^2 \\
& =\frac{34}{4}-\left(\frac{10}{4}\right)^2 \\
& =\frac{34}{4}-\frac{25}{4} \\
& =\frac{9}{4}
\end{aligned}$

</details>

---

### Q101. MHT CET 2023 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The p.d.f. of a discrete random variable is defined as
$f(x)= \begin{cases}\mathrm{k} x^2, & 0 \leq x \leq 6 \\ 0, & \text { otherwise }\end{cases}$
Then the value of $F(4)$ (c.d.f) is

**Options:**

- **(A)** $\frac{30}{91}$
- **(B)** $\frac{30}{97}$
- **(C)** $\frac{15}{47}$
- **(D)** $\frac{15}{97}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{30}{91}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{f}(x) & =\mathrm{k} x^2, 0 \leq x \leq 6 \\ \mathrm{k}(0)^2 & +\mathrm{k}(1)^2+\mathrm{k}(2)^2+\mathrm{k}(3)^2+\mathrm{k}(4)^2 \\ \Rightarrow \mathrm{k} & +4 \mathrm{k}(5)^2+\mathrm{k}(6)^2=1 \\ \Rightarrow & 91 \mathrm{k}=1 \\ \Rightarrow \mathrm{k} & =\frac{1}{91} \\ \mathrm{~F}(4) & =\mathrm{P}(\mathrm{X} \leq 4)=\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1) \\ & =\mathrm{k}(0)^2+\mathrm{k}(\mathrm{k})^2+\mathrm{k}(2)^2+\mathrm{k}(3)^2+\mathrm{k}(4)^2 \\ & =\mathrm{k}+4 \mathrm{k}+9 \mathrm{k}+16 \mathrm{k} \\ & =30 \mathrm{k} \\ & =30\left(\frac{1}{91}\right) \\ & =\frac{30}{91}\end{aligned}$

</details>

---

### Q102. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $\mathrm{X}$ assumes values 1,2 , $3, \ldots ., \mathrm{n}$ with equal probabilities, if $\operatorname{var}(\mathrm{X})=\mathrm{E}(\mathrm{X})$, then $\mathrm{n}$ is

**Options:**

- **(A)** 4
- **(B)** 5
- **(C)** 7
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 7**

**Detailed Solution:**

$\begin{aligned} & \mathrm{X}=1,2,3, \ldots \mathrm{n} \\ & \begin{aligned} \mathrm{P}(\mathrm{X}) & =\frac{1}{\mathrm{n}} \\ \mathrm{E}(\mathrm{X}) & =\sum_{\mathrm{i}=1}^{\mathrm{n}} x_{\mathrm{i}} \mathrm{p}_{\mathrm{i}} \\ & =\frac{(1+2+3+\ldots+\mathrm{n})}{\mathrm{n}} \\ & =\frac{\mathrm{n}(\mathrm{n}+1)}{2 \mathrm{n}} \\ \mathrm{E}(\mathrm{X}) & =\frac{\mathrm{n}+1}{2}\end{aligned}\end{aligned}$
$\begin{aligned} & \operatorname{Var}(\mathrm{X})=\sum_{\mathrm{i}=1}^{\mathrm{n}} x_{\mathrm{i}}^2 \mathrm{p}_{\mathrm{i}}-[\mathrm{E}(\mathrm{X})]^2 \\ & =\frac{1^2+2^2+3^2+\ldots+\mathrm{n}^2}{\mathrm{n}}-\left(\frac{\mathrm{n}+1}{2}\right)^2 \\ & =\frac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6 \mathrm{n}}-\left(\frac{\mathrm{n}+1}{2}\right)^2 \\ & =\frac{(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}-\left(\frac{\mathrm{n}+1}{2}\right)^2 \\ & \operatorname{Var}(X)=E(X) \\ & \text {...[Given] } \\ & \frac{(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}-\left(\frac{\mathrm{n}+1}{2}\right)^2=\frac{\mathrm{n}+1}{2} \\ & \frac{2 \mathrm{n}^2+\mathrm{n}+2 \mathrm{n}+1}{6}-\left(\frac{\mathrm{n}^2+2 \mathrm{n}+1}{4}\right)=\frac{\mathrm{n}+1}{2} \\ & \frac{4 n^2+6 n+2-3 n^2-6 n-3}{12}=\frac{n+1}{2} \\ & \mathrm{n}^2-1=6(\mathrm{n}+1) \\ & \mathrm{n}^2-1=6 \mathrm{n}+6 \\ & \mathrm{n}^2-6 \mathrm{n}-7=0 \\ & \therefore \quad \mathrm{n}=-1 \text { or } \mathrm{n}=7 \\ & \text { But } \mathrm{n} \neq-1 \\ & \therefore \quad \mathrm{n}=7 \\ & \end{aligned}$

</details>

---

### Q103. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three fair coins numbered 1 and 0 are tossed simultaneously. Then variance $\operatorname{Var}(\mathrm{X})$ of the probability distribution of random variable $\mathrm{X}$, where $X$ is the sum of numbers on the uppermost faces, is

**Options:**

- **(A)** 0.7
- **(B)** 0.75
- **(C)** 0.65
- **(D)** 0.62

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.75**

**Detailed Solution:**

Three fair coins numbered 1,0 are tossed.
$\therefore \quad$ Sample space $=\{111,110,101,011,100,010$, $001,000\}$
$\therefore \quad \mathrm{n}(\mathrm{S})=8$
$\mathrm{X}$ represents the sum of numbers on upper most face
$\begin{aligned}
\therefore \quad & P(X=0)=\frac{1}{8}, \\
& P(X=1)=\frac{3}{8}, \\
& P(X=2)=\frac{3}{8}, \\
& P(X=3)=\frac{1}{8}
\end{aligned}$
$\therefore \quad$ Probability distribution of $\mathrm{X}$ is
\begin{array}{|c|c|c|c|c|}
\hline \mathrm{X} & 0 & 1 & 2 & 3 \\
\hline \mathrm{P}(\mathrm{X}) & \frac{1}{8} & \frac{3}{8} & \frac{3}{8} & \frac{1}{8} \\
\hline
\end{array}
$\begin{aligned}
\mathrm{E}(\mathrm{X}) & =\sum_{x=0}^3 x_{\mathrm{i}} \mathrm{P}\left(x_{\mathrm{i}}\right) \\
\mathrm{E}(\mathrm{X}) & =0 \times \frac{1}{8}+1 \times \frac{3}{8}+2 \times \frac{3}{8}+3 \times \frac{1}{8} \\
& =\frac{12}{8}=\frac{3}{2} \\
\mathrm{E}\left(\mathrm{X}^2\right) & =\sum_{x=0}^3 x_1^2 \mathrm{P}\left(x_{\mathrm{i}}\right)=3 \\
\text { Variance of } \mathrm{X} & =\mathrm{E}\left(\mathrm{X}^2\right)-[\mathrm{E}(\mathrm{X})]^2 \\
& =3-\left(\frac{3}{2}\right)^2 \\
& =3-\frac{9}{4} \\
& =\frac{3}{4}=0.75
\end{aligned}$

</details>

---

### Q104. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability mass function of random variable $\mathrm{X}$ is given by
$\mathrm{P}[\mathrm{X}=\mathrm{r}]=\left\{\begin{array}{ll}
\frac{{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}}}{32}, & \mathrm{n}, \mathrm{r} \in \mathbb{N} \\
0, & \text { otherwise }
\end{array} \text {, then } \mathrm{P}[\mathrm{X} \leq 2]=\right.$

**Options:**

- **(A)** $\frac {1}{3}$
- **(B)** $\frac {1}{2}$
- **(C)** $\frac {1}{4}$
- **(D)** $\frac {1}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac {1}{2}$**

**Detailed Solution:**

$\begin{aligned} & \text { Since } \sum_{x=0}^{\mathrm{n}} \mathrm{P}(\mathrm{X}=\mathrm{n})=1 \\ & \frac{{ }^n C_0+{ }^n C_1+{ }^n C_2 \ldots+\ldots+{ }^n C_n}{32}=1 \\ & 2^{\mathrm{n}}=32 \\ & \therefore \quad \mathrm{n}=5 \\ & \mathrm{P}(\mathrm{X} \leq 2)=\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2) \\ & =\frac{{ }^5 \mathrm{C}_0}{32}+\frac{{ }^5 \mathrm{C}_1}{32}+\frac{{ }^5 \mathrm{C}_2}{32}=\frac{1}{2} \\ & \end{aligned}$

</details>

---

### Q105. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If p.m.f. of a r.v.X is $P(X=x)=\frac{1}{10}$, for $x=1,2,3, \ldots \ldots, 10=0$, otherwise, then $\operatorname{Var}(x)$ is equal to

**Options:**

- **(A)** $\frac{11}{2}$
- **(B)** $\frac{33}{4}$
- **(C)** $\frac{121}{4}$
- **(D)** $\frac{77}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{33}{4}$**

**Detailed Solution:**

$\begin{aligned} & \operatorname{Var}(x)=\sum P_i x_i^2-\left(\sum P_i x_i\right)^2=\frac{1}{10}\left(1^2+2^2+3^2 \ldots .+10^2\right) \\ & -\left\{\frac{1}{10}(1+2+3+\ldots . .+10)\right\}^2 \\ & =\frac{1}{10} \times \frac{10 \times 11 \times 21}{6}-\left(\frac{1}{10} \times \frac{10 \times 11}{2}\right)^2 \\ & =38.5-30.25=8.25=\frac{33}{4}\end{aligned}$

</details>

---

### Q106. MHT CET 2022 (10 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For given data $N=60, \sum X^2=18000$ and $\sum X=960$, then variance of data is

**Options:**

- **(A)** 54
- **(B)** 34
- **(C)** 22
- **(D)** 44

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 44**

**Detailed Solution:**

Variance $=\frac{\sum x^2}{N}-\left(\frac{\sum x}{N}\right)^2=\frac{18000}{60}-\left(\frac{960}{60}\right)^2=300-256=44$

</details>

---

### Q107. MHT CET 2022 (08 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two cards are drawn successively with replacement from a well shuffled pack of 52 cards. Then the probability distribution of number of kings is

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Tg1XclrqvdY3tDAzRFtihfznA1COhwUu-vlvzbvsP98.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/XEnTt68jK0pf1boVV5wqv55tHrx_t_q1ve4Nqo6gNyg.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/GwerpwlvtzPx5LMDuE4yaWnf_mh1qah4Znyks5QOxIQ.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/LjWXCH8fPXB1fM-rP3hkjFmqJfqxyc1pTETawl9ZH_Q.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/GwerpwlvtzPx5LMDuE4yaWnf_mh1qah4Znyks5QOxIQ.original.fullsize.png">**

**Detailed Solution:**

here $n=2, p=\frac{4}{52}=\frac{1}{13}$
$q=\frac{48}{52}=\frac{12}{13}$
Now $P(x=0)={ }^2 C_0\left(\frac{1}{13}\right)^0 \cdot\left(\frac{12}{13}\right)^2=\frac{144}{169}$
$\begin{aligned}
& P(x=1)={ }^2 C_1\left(\frac{1}{13}\right)^1 \cdot\left(\frac{12}{13}\right)^1=\frac{24}{169} \\
& P(x=2)={ }^2 C_2\left(\frac{1}{13}\right)^2 \cdot\left(\frac{12}{13}\right)^0=\frac{1}{169}
\end{aligned}$
Hence, option (C) is correct

</details>

---

### Q108. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

For the following frequency distribution
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/TcarhvMyQnU9mTzQfkOoNde8ZvN7gF1LXv5aeRzwXwk.original.fullsize.png">

The variance is

**Options:**

- **(A)** 2.85
- **(B)** 2.18
- **(C)** 2.37
- **(D)** 2.49

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2.85**

**Detailed Solution:**

$\begin{array}{cccc}\boldsymbol{x}_{\mathbf{i}} & \boldsymbol{f}_{\mathbf{i}} & \boldsymbol{f}_{\mathrm{i}} \boldsymbol{x}_{\mathbf{i}} & \boldsymbol{f}_{\mathbf{i}} \mathbf{x}_{\mathbf{i}}{ }^2 \\ 5 & 3 & 15 & 75 \\ 6 & 7 & 42 & 252 \\ 7 & 4 & 28 & 196 \\ 8 & 2 & 16 & 128 \\ 10 & \frac{4}{N=20} & \frac{40}{\sum f_i x_i=141} & \frac{400}{\sum f_i x_i^2=1051}\end{array}$
$\begin{aligned} & \text { Variance }=\frac{\sum f_i x_i^2}{N}-\left(\frac{\sum f_i x_i}{N}\right)^2 \\ & =\frac{1051}{20}-\left(\frac{141}{20}\right)^2 \\ & =52.55-(7.05)^2 \\ & =52.55-49.7025 \\ & =2.85\end{aligned}$

</details>

---

### Q109. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A player tosses 2 fair coins. He with Rs. 5 if 2 heads appear, Rs. 2 if 1 head appears and Rs. 1 if no head appear, then the variance of his winning amount is

**Options:**

- **(A)** $\frac{9}{4}$
- **(B)** 6
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{17}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{9}{4}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/w_bmw2E5cQGYPfsdb12xHy5lVHa0odRFXLhJM5cmPl0.original.fullsize.png">

Variance $=\sum p_i x_i{ }^2-\left(\sum p_i x_i\right)^2$
$=\frac{17}{2}-\frac{25}{4}=\frac{9}{4}$

</details>

---

### Q110. MHT CET 2022 (08 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $P[X=x]=\left\{\begin{array}{cc}\frac{K \cdot 2^x}{x !}, & x=0,1,2,3 \\ 0, & \text { otherwise }\end{array}\right.$ Forms p.m.f., then value of $K$ is

**Options:**

- **(A)** $\frac{5}{19}$
- **(B)** $\frac{2}{19}$
- **(C)** $\frac{3}{19}$
- **(D)** $\frac{1}{19}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{19}$**

**Detailed Solution:**

$\begin{aligned} & \sum P(x)=1 \\ & \Rightarrow k \cdot \frac{2^0}{0 !}+k \cdot \frac{2^1}{1 !}+k \cdot \frac{2^2}{2 !}+k \cdot \frac{2^3}{3 !}=1 \\ & \Rightarrow \frac{19}{3} k=1 \\ & \Rightarrow k=\frac{3}{19}\end{aligned}$

</details>

---

### Q111. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Following is the probability distribution of smart phones sold in a shop per day
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/67y_00xZz5PxPtlqUe2DXLnwut68sIpNCqERuhNsQVw.original.fullsize.png">
Then $E(x)=$

**Options:**

- **(A)** $2.45$
- **(B)** $2.55$
- **(C)** $0.55$
- **(D)** $0.75$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2.45$**

**Detailed Solution:**

$\because k+0.3+0.15+0.15+0.1+2 k=1$
$\Rightarrow k=0.1$
Now $E(x)=\sum p_i x_i=2.45$

</details>

---

### Q112. MHT CET 2022 (07 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $\mathrm{X}$ assumes value $1,2,3, \ldots \ldots . n$ with equal probabilities. If the ratio of variance of $=\sum p_i x_i^2-\left(\sum p_i x_i\right)^2$ to expected value of $\mathrm{X}$ is equal to 4 , then the value of $n$ is

**Options:**

- **(A)** 35
- **(B)** 50
- **(C)** 30
- **(D)** 25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 25**

**Detailed Solution:**

$\begin{aligned} & \text { Variance }=\sum p_i X_i^2-\left(\sum p_i X_i\right)^2 \\ & =\frac{1}{n} \times \frac{n(n+1)(2 n+1)}{6}-\left\{\frac{1}{n} \times \frac{n(n+1)}{2}\right\}^2 \\ & =\frac{n(n+1)}{2 n}\left\{\frac{2 n+1}{3}-\frac{n(n+1)}{2 n}\right\} \\ & \text { Expected value }=\sum p_i x_i=\frac{1}{n} \cdot \frac{n(n+1)}{2}=\frac{n(n+1)}{2 n} \\ & \text { Ratio }=\frac{2 n+1}{3}-\frac{n(n+1)}{2 n}\end{aligned}$
$\Rightarrow n^2-25 n=0$
$\Rightarrow n(n-25)=0$
$\Rightarrow n=0$ or $n=25$
$\Rightarrow n=25$ as $n=0$ is not possible

</details>

---

### Q113. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has the following probability distribution
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ROfvwE11ZMI9BFDP0cEeC-4LA43eiadcIYCK90Mrsvc.original.fullsize.png">
Then $P\left(X^3 2\right)=$

**Options:**

- **(A)** $\frac{45}{49}$
- **(B)** $\frac{15}{49}$
- **(C)** $\frac{1}{49}$
- **(D)** $\frac{40}{49}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{45}{49}$**

**Detailed Solution:**

$\begin{aligned} & \sum P(x)=1 \\ & \Rightarrow 49 k=1\end{aligned}$
Now, $P\left(x^3 2\right)=1-P(X<2)$
$\begin{aligned} & =1-\{P(X=0)+P(x=1)\} \\ & =1-\left\{\frac{1}{49}+\frac{3}{49}\right\} \\ & =\frac{45}{49}\end{aligned}$

</details>

---

### Q114. MHT CET 2022 (07 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Two numbers are selected at random from the first six positive integers. If $X$ denotes the larger of two numbers, then $\operatorname{Var}(X)=$

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{14}{3}$
- **(C)** $\frac{14}{9}$
- **(D)** $\frac{70}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{14}{9}$**

**Detailed Solution:**

$\begin{array}{cccc}\mathbf{X}_{\mathbf{i}} & \mathbf{P}_{\mathbf{i}} & \mathbf{P}_{\mathbf{i}} \mathbf{X}_{\mathbf{i}} & \mathbf{P}_{\mathbf{i}} \mathbf{X}_{\mathbf{i}}{ }^2 \\ \mathbf{1} & \frac{0}{15} & \mathbf{0} & \mathbf{0} \\ \mathbf{2} & \frac{1}{15} & \frac{2}{15} & \frac{4}{15} \\ \mathbf{4} & \frac{2}{15} & \frac{6}{15} & \frac{18}{15} \\ 5 & \frac{3}{15} & \frac{12}{15} & \frac{48}{15} \\ \mathbf{6} & \frac{4}{15} & \frac{20}{15} & \frac{100}{15} \\ & \frac{5}{15} & \frac{30}{15} & \frac{180}{15}\end{array}$
$\overline{\sum p_i x_i=\frac{70}{15}} \quad \overline{\sum p_i x_i^2=\frac{350}{15}}$.
$\begin{aligned} & \operatorname{Var}(x)=\sum p_i x_i{ }^2-\left(\sum p_i x_i\right)^2 \\ & =\frac{70}{3}-\frac{196}{9} \\ & =\frac{210-196}{9}=\frac{14}{9}\end{aligned}$

</details>

---

### Q115. MHT CET 2022 (06 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A coin is tossed twice in succession. Let $X$ represent the number of tails in two tosses, then the probability distribution of $\mathrm{X}$ is given by

**Options:**

- **(A)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/9Yt8oHOhxx-x5F900yyGheODHEJIaCADzGfad1kOlrU.original.fullsize.png">
- **(B)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/AjwTXZb4IsN6lQolj5gyANybeNkfsBh4mAQbqpAM4_o.original.fullsize.png">
- **(C)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/iow8xuVYL333H7En2lS3jjh0v49kjW8N0cO7FtAULp0.original.fullsize.png">
- **(D)** <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bdid5PCv0MV2fkxrfvb21gELnqhzLruuUXl9rHPpJww.original.fullsize.png">

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/bdid5PCv0MV2fkxrfvb21gELnqhzLruuUXl9rHPpJww.original.fullsize.png">**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/fCkzqRa0KFd_XxTRMSgySrFKUpE633whOaDbGYY__fs.original.fullsize.png">

</details>

---

### Q116. MHT CET 2022 (05 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/jdm-ZQhXCulcLYU8reIQdYJ-Et0F6dT516lLymOiWA0.original.fullsize.png">

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{3}{2}$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{8}$**

**Detailed Solution:**

Here, $\mathrm{K}+\frac{1}{6}+\frac{3}{8}+2 \mathrm{~K}+\frac{1}{12}=1$
$\begin{aligned} & \Rightarrow 3 K+\frac{4+9+2}{24}=1 \\ & \Rightarrow 3 K=1-\frac{15}{24}=\frac{9}{24}=\frac{1}{8}\end{aligned}$

</details>

---

### Q117. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Two dice are thrown simultaneously. If $\mathrm{X}$ denotes the number of sixes, then the expectation of $\mathrm{X}$ is

**Options:**

- **(A)** 3
- **(B)** 2
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{3}$**

**Detailed Solution:**

Probability of getting $6=\frac{1}{6}$
$\mathrm{X}$ denotes number of times of getting 6 , So $\mathrm{x}$ can take values $0,1,2$.
$\begin{aligned}
\mathrm{P}(\mathrm{x} & =0)=\frac{5}{6} \times \frac{5}{6}=\frac{25}{36} \\
\mathrm{P}(\mathrm{x} & =1)=\left(\frac{1}{6} \times \frac{5}{6}\right)+\left(\frac{5}{6} \times \frac{1}{6}\right)=\frac{10}{36} \\
\mathrm{P}(\mathrm{x} & =2)=\frac{1}{6} \times \frac{1}{6}=\frac{1}{36} \\
\mathrm{E}(\mathrm{x}) & =\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\
& =\left(\frac{25}{36}\right)(0)+\left(\frac{10}{36}\right)(1)+\left(\frac{1}{36}\right)(2)=\frac{10+2}{36}=\frac{1}{3}
\end{aligned}$

</details>

---

### Q118. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a random variable $\mathrm{X}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/69uqfz2shNVhqG4E8pSXN7yTGOaSwyDSPxwQDxRFP74.original.fullsize.png">

Then $\operatorname{Var}(\mathrm{X})=$

**Options:**

- **(A)** $\frac{\mathrm{n}^2-1}{12}$
- **(B)** $\frac{\mathrm{n}^2-\mathrm{n}}{6}$
- **(C)** $\frac{\mathrm{n}^2-\mathrm{n}}{12}$
- **(D)** $\frac{\mathrm{n}^2-1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{\mathrm{n}^2-1}{12}$**

**Detailed Solution:**

$\begin{aligned} \therefore \quad \Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} & =\frac{1}{\mathrm{n}}+\frac{2}{\mathrm{n}}+\frac{3}{\mathrm{n}}+\ldots .+\frac{\mathrm{n}}{\mathrm{n}} \\ & =\frac{1+2+3+\ldots \mathrm{n}}{\mathrm{n}}=\frac{\mathrm{n}(\mathrm{n}+1)}{2(\mathrm{n})}=\frac{\mathrm{n}+1}{2}\end{aligned}$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/1xVkcxoeY0Sd246uTZdfcFBioq7M-bT6sg3a0SEOOdo.original.fullsize.png">

$\begin{aligned} & \quad \sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2=\frac{1}{\mathrm{n}}+\frac{4}{\mathrm{n}}+\frac{9}{\mathrm{n}}+\ldots .+\frac{\mathrm{n}^2}{\mathrm{n}} \\ & \quad \Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2=\frac{1}{\mathrm{n}}+\frac{4}{\mathrm{n}}+\frac{9}{\mathrm{n}}+\ldots .+\frac{\mathrm{n}^2}{\mathrm{n}} \\ & \quad=\frac{1+4+9+\ldots \mathrm{n}^2}{\mathrm{n}}=\frac{\mathrm{n}(\mathrm{n}+1)(2 \mathrm{n}+1)}{6 \mathrm{n}}=\frac{(\mathrm{n}+1)(2 \mathrm{n}+1)}{6} \\ & \therefore \quad \operatorname{Var}(\mathrm{x})=\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2-\left(\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}\right)^2 \\ & \quad=\frac{(\mathrm{n}+1)(2 \mathrm{n}+1)}{6}-\left[\frac{(\mathrm{n}+1)}{2}\right]^2=\frac{2 \mathrm{n}^2+3 \mathrm{n}+1}{6}-\frac{\mathrm{n}^2+2 \mathrm{n}+1}{4} \\ & =\frac{4 \mathrm{n}^2+6 \mathrm{n}+2-3 \mathrm{n}^2-6 \mathrm{n}-3}{12}=\frac{\mathrm{n}^2-1}{12}\end{aligned}$

</details>

---

### Q119. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean of the numbers obtained on throwing a die having written 1 on three faces, 2 on two faces and 5 on one face is

**Options:**

- **(A)** 5
- **(B)** $\frac{8}{3}$
- **(C)** 1
- **(D)** 2

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 2**

**Detailed Solution:**

Probability of getting $1=\frac{3}{6}=\frac{1}{2}$
Probability of getting $2=\frac{2}{6}=\frac{1}{3}$
Probability of getting $5=\frac{1}{6} \therefore \quad$ Mean $=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}=2$
\begin{array}{|l|l|l|}
\hline \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\
\hline 1 & 1 / 2 & 1 / 2 \\
\hline 2 & 1 / 3 & 2 / 3 \\
\hline 5 & 1 / 6 & 5 / 6 \\
\hline \multicolumn{2}{|l|}{ Total } & 2 \\
\hline
\end{array}

</details>

---

### Q120. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $\mathrm{f}$ defined by $\mathrm{f}(\mathrm{x})= \begin{cases}\mathrm{K}\left(\mathrm{x}-\mathrm{x}^2\right) & \text { if } 0 < \mathrm{x} < 1 \\ 0 & \text {, other wise }\end{cases}$ is the p.d.f. of a r.v.x, then the value of $\mathrm{P}\left(\mathrm{X} < \frac{1}{2}\right)$ is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

Given $\mathrm{f}$ is a the p.d.f. of a r.v.x.
$$
\begin{aligned}
& \therefore \int_0^1 \mathrm{f}(\mathrm{x}) \mathrm{dx}=1 \Rightarrow \int_0^1 \mathrm{~K}\left(\mathrm{x}-\mathrm{x}^2\right) \mathrm{dx}=1 \\
& \mathrm{~K}\left[\frac{\mathrm{x}^2}{2}-\frac{\mathrm{x}^3}{3}\right]_0^1=1 \Rightarrow \mathrm{K}\left(\frac{1}{2}-\frac{1}{3}\right)=1 \Rightarrow \frac{\mathrm{K}}{6}=1 \\
& \mathrm{~K}=6 \\
& \left.\therefore \mathrm{P}\left(\mathrm{X} < \frac{1}{2}\right)=\int_0^{\frac{1}{2}} 6\left(\mathrm{x}-\mathrm{x}^2\right) \mathrm{dx}=\left[\frac{6 \mathrm{x}^2}{2}\right]_0^1-\left[\frac{6 \mathrm{x}^3}{3}\right]_0^1\right] \\
& =\left[3 \mathrm{x}^2-2 \mathrm{x}^3\right]_0^{\frac{1}{2}}=\frac{3}{4}-\frac{2}{8}=\frac{3}{4}-\frac{1}{4}=\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q121. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable $\mathrm{X}$ has the following probability distribution
\begin{array}{|r|l|l|l|l|l|l|l|l|l|}
\hline \mathrm{x} & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline \mathrm{P}(\mathrm{X}=\mathrm{x}) & \mathrm{K} & 2 \mathrm{~K} & 3 \mathrm{~K} & 4 \mathrm{~K} & 4 \mathrm{~K} & 3 \mathrm{~K} & 2 \mathrm{~K} & \mathrm{~K} & \mathrm{~K} \\
\hline
\end{array}
Then $\mathrm{P}(3 < \mathrm{x} \leq 6)=$

**Options:**

- **(A)** $\frac{3}{7}$
- **(B)** $\frac{4}{7}$
- **(C)** $\frac{13}{21}$
- **(D)** $\frac{8}{21}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{7}$**

**Detailed Solution:**

We know that
$$
\begin{aligned}
& \mathrm{k}+2 \mathrm{k}+3 \mathrm{k}+4 \mathrm{k}+4 \mathrm{k}+3 \mathrm{k}+2 \mathrm{k}+\mathrm{k}+\mathrm{k}=1 \Rightarrow 21 \mathrm{k}=1 \\
& \Rightarrow \mathrm{k}=\frac{1}{21}
\end{aligned}
$$
When $x=4, P=4 k=\frac{4}{21}$, When $x=5, P=3 k=\frac{3}{21}$,
When $\mathrm{x}=6, \mathrm{P}=2 \mathrm{k}=\frac{2}{21}$
$$
\therefore \mathrm{P}(3 < \mathrm{x} \leq 6)==\frac{4+3+2}{21}=\frac{9}{21}=\frac{3}{7}
$$

</details>

---

### Q122. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the probability distribution given by following
\begin{array}{|l|l|l|l|l|l|l|l|}
\hline \mathrm{X} & 5 & 6 & 7 & 8 & 9 & 10 & 11 \\
\hline \mathrm{P}(\mathrm{X}=\mathrm{x}) & 0.07 & 0.2 & 0.3 & \mathrm{k} & 0.07 & 0.04 & 0.02 \\
\hline
\end{array}
$$
\operatorname{Var}(\mathrm{X})=
$$

**Options:**

- **(A)** 2.56
- **(B)** 2.85
- **(C)** 1.65
- **(D)** 3.85

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1.65**

**Detailed Solution:**

We have $0.07+0.2+0.3+\mathrm{k}+0.07+0.04+0.02=1$ $\therefore \mathrm{k}=0.3$
\begin{array}{|l|l|l|l|}
\hline \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}{ }^2 \\
\hline 5 & 0.07 & 0.35 & 1.75 \\
\hline 6 & 0.2 & 1.2 & 7.2 \\
\hline 7 & 0.3 & 2.1 & 14.7 \\
\hline 8 & 0.3 & 2.4 & 19.2 \\
\hline 9 & 0.07 & 0.63 & 5.67 \\
\hline 10 & 0.04 & 0.4 & 4 \\
\hline 11 & 0.02 & 0.22 & 2.42 \\
\hline \multicolumn{2}{|l|}{ Total } & 7.3 & 54.94 \\
\hline
\end{array}
Variance $(\mathrm{x})=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2-\left(\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}\right)^2=(54.94)-(7.3)^2=1.65$

</details>

---

### Q123. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a discrete random variable $\mathrm{X}$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/Wu46b4OAHsFfBiEAVat6A_G8MWkw4xpK6WpS3md-Wxs.original.fullsize.png">

Find the value of $\mathrm{P}(2 < \mathrm{X} < 6)$

**Options:**

- **(A)** $\frac{4}{21}$
- **(B)** $\frac{1}{21}$
- **(C)** $\frac{10}{21}$
- **(D)** $\frac{4}{7}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{7}$**

**Detailed Solution:**

We have $\mathrm{K}+2 \mathrm{~K}+3 \mathrm{~K}+4 \mathrm{~K}+5 \mathrm{~K}+6 \mathrm{~K}=1 \Rightarrow \mathrm{K}=\frac{1}{21}$
$$
\begin{aligned}
& \therefore \mathrm{P}(2 < \mathrm{x} < 6)=\mathrm{P}(\mathrm{x}=3)+\mathrm{P}(\mathrm{x}=4)+\mathrm{P}(\mathrm{x}=5) \\
& =\frac{3}{21}+\frac{4}{21}+\frac{5}{21}=\frac{12}{21}=\frac{4}{7}
\end{aligned}
$$

</details>

---

### Q124. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the probability distribution function of a random variable $\mathrm{X}$ is given as
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/ar6dMYKxuMNksRGHNZ-4c15Fdp7Ov5vPrrSVdBb7SDU.original.fullsize.png">

Then $F(0)$ is equal to

**Options:**

- **(A)** $P(X>0)$
- **(B)** $1-P(X>0)$
- **(C)** $1-\mathrm{P}(\mathrm{X} < 0)$
- **(D)** $\mathrm{P}(\mathrm{X} < 0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1-P(X>0)$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/2_l0ODZnqaLDfsI-HIJLCCdrFbF9mZrXUXstluR6qTY.original.fullsize.png">

$\begin{aligned} & \therefore F(0)=1-[P(x=1)+P(x=2)] \\ & =1-P(X>0)\end{aligned}$

</details>

---

### Q125. MHT CET 2021 (22 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The distribution function $\mathrm{F}(\mathrm{X})$ of discrete random variable $\mathrm{X}$ is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/kbhYSQK4eH8fCJH423PyOwz_GKfMGFvVU2iwMB0AIfk.original.fullsize.png">

Then $P[X=4]+P[X=5]=$

**Options:**

- **(A)** 0.14
- **(B)** 0.85
- **(C)** 0.37
- **(D)** 0.23

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.37**

**Detailed Solution:**

We have
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/E49gMNoAXjMG1CjZ9lDkxSCbEgjhE__Zl_eKMLWwRyo.original.fullsize.png">

$$
\begin{aligned}
& \therefore P(x=1)=0.2, P(x=2)=0.17, P(x=3)=0.11 \\
& P(x=4)=0.14, P 9 x=5)=0.23, P(x=6)=0.15
\end{aligned}
$$
Thus $\mathrm{P}(\mathrm{x}=4)+\mathrm{P}(\mathrm{x}=5)=0.14+0.23=0.37$

</details>

---

### Q126. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $\mathrm{X}$ has following distribution
\begin{array}{|l|l|l|l|l|l|l|}
\hline \mathrm{X}=\mathrm{x} & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline \mathrm{P}(\mathrm{X}=\mathrm{x}) & \mathrm{k} & 3 \mathrm{k} & 5 \mathrm{k} & 7 \mathrm{k} & 8 \mathrm{k} & \mathrm{K} \\
\hline
\end{array}
Then $\mathrm{P}(2 \leq \mathrm{x} < 5)=$

**Options:**

- **(A)** $\frac{7}{25}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{24}{25}$
- **(D)** $\frac{23}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{3}{5}$**

**Detailed Solution:**

We have $\mathrm{k}+3 \mathrm{k}+5 \mathrm{k}+7 \mathrm{x}+8 \mathrm{k}+\mathrm{k}=1 \Rightarrow \mathrm{k}=\frac{1}{25}$
$$
\therefore \mathrm{P}(2 \leq \mathrm{x} \leq 5)=\frac{1}{25}(3+5+7)=\frac{15}{25}=\frac{3}{5}
$$

</details>

---

### Q127. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A bakerman sells 5 types of cakes. Profit due to sale of each type of cake is respectively Rs 2 , Rs 2.5 , Rs 3, Rs 1.5 and Rs 1 . The demands for these cakes are $20 \%, 5 \%, 10 \%$ and $15 \%$ respectively, then the expected profit per cake is

**Options:**

- **(A)** Rs 1.725
- **(B)** Rs 0.01725
- **(C)** Rs 0.1725
- **(D)** Rs 17.25

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Rs 1.725**

**Detailed Solution:**

$\begin{aligned} & \text { Expected value }=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\ & =(2)\left(\frac{20}{100}\right)+(2.5)\left(\frac{5}{100}\right)+(3)\left(\frac{10}{100}\right)+(1.5)\left(\frac{50}{100}\right)+(1)\left(\frac{15}{100}\right) \\ & =0.4+0.125+0.3+0.75+0.15=1.725\end{aligned}$

</details>

---

### Q128. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{x}$ is a random variable with p.m.f. as follows.
$$
\begin{aligned}
& P(X=x)=\frac{5}{16}, x=0,1 \\
& =\frac{k x}{48}, x=2, \text { then } E(x)= \\
& =\frac{1}{4}, x=3
\end{aligned}
$$

**Options:**

- **(A)** 1.1875
- **(B)** 1.3125
- **(C)** 1.5625
- **(D)** 0.5625

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 1.3125**

**Detailed Solution:**

From given data, we write
When $\mathrm{x}=0, \mathrm{P}=\frac{5}{16}=\frac{15}{48}$
$$
\begin{aligned}
& x=1, P=\frac{5}{16}=\frac{15}{48} \\
& x=2, P=\frac{2 k}{48} \\
& x=3, P=\frac{1}{4}=\frac{12}{48}
\end{aligned}
$$

Here $\sum \mathrm{Pi}=1$
$$
\begin{aligned}
& \therefore \frac{15}{48}+\frac{15}{48}+\frac{2 \mathrm{k}}{48}+\frac{12}{48}=1 \Rightarrow \mathrm{k}=3 \\
& \therefore \text { When } \mathrm{x}=2, \mathrm{P}=\frac{6}{48}=\frac{1}{8}
\end{aligned}
$$

$$
\begin{aligned}
& \text { Now } \mathrm{E}=\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\
& =\left[\left(\frac{5}{16}\right)(0)\right]+\left[\left(\frac{5}{16}\right)(1)\right]+\left[\left(\frac{1}{8}\right)(2)\right]+\left[\left(\frac{1}{4}\right)(3)\right]=0+\frac{5}{16}+\frac{1}{4}+\frac{3}{4}=\frac{21}{16}=1.3125
\end{aligned}
$$

</details>

---

### Q129. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The p.m.f of a random variable $\mathrm{X}$ is
$P(X=x)=\frac{1}{2^5}\left(\begin{array}{l}5 \\ x\end{array}\right), \quad x=0,12345$ then $=0 \quad$ otherwise,

**Options:**

- **(A)** $\mathrm{P}(\mathrm{X} \leq 2) < \mathrm{P}(\mathrm{X} \geq 3)$
- **(B)** $\mathrm{P}(\mathrm{X} \leq 2)>\mathrm{P}(\mathrm{X} \geq 3)$
- **(C)** $\mathrm{P}(\mathrm{X} \leq 2)=2 \mathrm{P}(\mathrm{X} \geq 3)$
- **(D)** $\mathrm{P}(\mathrm{X} \leq 2)=\mathrm{P}(\mathrm{X} \geq 3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\mathrm{P}(\mathrm{X} \leq 2)=\mathrm{P}(\mathrm{X} \geq 3)$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{P}(\mathrm{X}=\mathrm{x})=\frac{1}{32}{ }^5 \mathrm{C}_{\mathrm{x}} \text {, where } \mathrm{x}=0,1,2,3,4,5 \\
& =0, \text { otherwise } \\
& \therefore \mathrm{P}(\mathrm{X} \leq 2)=\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2) \\
& =\frac{1}{32}\left[{ }^5 \mathrm{C}_0+{ }^5 \mathrm{C}_1+{ }^5 \mathrm{C}_2\right]=\frac{1}{32}(1+5+10)=\frac{16}{32}=\frac{1}{2} \\
& \mathrm{P}(\mathrm{X} \geq 3)=\mathrm{P}(\mathrm{X}=3)+\mathrm{P}(\mathrm{X}=4)+\mathrm{P}(\mathrm{X}=5) \\
& =\frac{1}{32}\left[{ }^5 \mathrm{C}_3+{ }^5 \mathrm{C}_4+{ }^5 \mathrm{C}_5\right]=\frac{1}{32}(10+5+1)=\frac{16}{32}=\frac{1}{2}
\end{aligned}
$$

</details>

---

### Q130. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$$
\text { The variance of the following probability distribution is, }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/o0PFiw7hV_8Kn4Evu0fMe4bI6vpnItNw808O5OaY9xs.original.fullsize.png">

**Options:**

- **(A)** $\frac{1}{8}$
- **(B)** $\frac{5}{8}$
- **(C)** $\frac{1}{4}$
- **(D)** $\frac{3}{8}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{8}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/EYdWm6ifmGWOMFt1DmsCxZq1FbSWx8XkFldfFbd94mE.original.fullsize.png">


$$
\begin{aligned}
& \text { Variance }=\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2-\left(\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}\right)^2 \\
& =\frac{5}{8}-\left(\frac{1}{2}\right)^2=\frac{5}{8}-\frac{1}{4}=\frac{3}{8}
\end{aligned}
$$

</details>

---

### Q131. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $X \sim B(4, p)$ and $P(X=0)=\frac{16}{81}$, then $P(X=4)=$

**Options:**

- **(A)** $\frac{1}{81}$
- **(B)** $\frac{1}{16}$
- **(C)** $\frac{1}{8}$
- **(D)** $\frac{1}{27}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{81}$**

**Detailed Solution:**

We have $\mathrm{n}=4$ and $\mathrm{P}(\mathrm{x}=0)=\frac{16}{81}$
$$
\begin{aligned}
& \therefore \frac{16}{81}={ }^4 \mathrm{C}_0(\mathrm{p})^4(\mathrm{q})^0 \\
& \therefore \frac{16}{81}=(\mathrm{p})^4 \Rightarrow \mathrm{P}=\frac{2}{3} \Rightarrow \mathrm{q}=\frac{1}{3} \\
& \therefore \mathrm{P}(\mathrm{x}=4)={ }^4 \mathrm{C}_4(\mathrm{p})^0(\mathrm{q})^4=(1)(1)\left(\frac{1}{3}\right)^4=\frac{1}{81}
\end{aligned}
$$

</details>

---

### Q132. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Rajesh has just bought a VCR from Maharashtra Electronics and the shop offers after sales service contract for Rs. 1000 for the next five years. Considering the experience of VCR users, the following distribution of maintenance expenses for the next five years is formed.
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mmi7kUTgpShWquImh_eHmDJmc8BKQn5Kwl270t-VfDQ.original.fullsize.png">

The expected value of maintenance cost is

**Options:**

- **(A)** Rs. 800
- **(B)** Rs. 770
- **(C)** Rs. 700
- **(D)** Rs. 900

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Rs. 770**

**Detailed Solution:**

$\begin{aligned} & \text { Expected value }=\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \\ & =(0)(0.35)+(500)(0.25)+(1000)(0.15)+(1500)(0.1) \\ & +(2000)(0.08)+(2500)(0.05)+(3000)(0.02) \\ & =0+125+150+150+160+125+60=770\end{aligned}$

</details>

---

### Q133. MHT CET 2021 (20 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $\mathrm{X}$ has the following probability distribution
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/3g52CqgvhA88bffVqg1Azwfbs6klriObNO1Rv26cBkQ.original.fullsize.png">

Then $F(4)=$

**Options:**

- **(A)** $\frac{3}{10}$
- **(B)** $\frac{1}{10}$
- **(C)** $\frac{7}{10}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{5}$**

**Detailed Solution:**

$\begin{aligned} & \text { Here } \mathrm{k}+2 \mathrm{k}+2 \mathrm{k}+3 \mathrm{k}+\mathrm{k}^2+2 \mathrm{k}^2+7 \mathrm{k}^2+\mathrm{k}=1 \\ & \therefore 10 \mathrm{k}^2+9 \mathrm{k}-1=0 \Rightarrow(10 \mathrm{k}-1)(\mathrm{k}+1)=0 \\ & \therefore \mathrm{k}=\frac{1}{10} \quad \ldots(\mathrm{k} \geq 0) \\ & \therefore \mathrm{F}(4)=\mathrm{k}+2 \mathrm{k}+2 \mathrm{k}+3 \mathrm{k}=8 \mathrm{k}=\frac{8}{10}=\frac{4}{5}\end{aligned}$

</details>

---

### Q134. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X \sim B\left(8, \frac{1}{2}\right)$, then $P(|x-4| \leq 2)=$

**Options:**

- **(A)** $\frac{119}{128}$
- **(B)** $\frac{29}{128}$
- **(C)** $\frac{238}{728}$
- **(D)** $\frac{119}{228}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{119}{128}$**

**Detailed Solution:**

We have $\mathrm{n}=8, \mathrm{p}=\frac{1}{2} \quad \Rightarrow \mathrm{q}=\frac{1}{2}$
To find $\mathrm{P}(|\mathrm{X}-4| \leq 2) \quad \Rightarrow \mathrm{X}=2,3,4,5,6$
Hence required probability
$$
\begin{array}{l}
={ }^{8} C_{2}\left(\frac{1}{2}\right)^{6}\left(\frac{1}{2}\right)^{2}+{ }^{8} C_{3}\left(\frac{1}{2}\right)^{5}\left(\frac{1}{2}\right)^{3}+{ }^{8} C_{4}\left(\frac{1}{2}\right)^{4}\left(\frac{1}{2}\right)^{4}+{ }^{8} C_{5}\left(\frac{1}{2}\right)^{3}\left(\frac{1}{2}\right)^{5}+{ }^{8} C_{6}\left(\frac{1}{2}\right)^{2}\left(\frac{1}{2}\right)^{6} \\
=\left(\frac{1}{2}\right)^{8}\left[{ }^{8} C_{2}+{ }^{8} C_{3}+{ }^{8} C_{4}+{ }^{8} C_{5}+{ }^{8} C_{6}\right] \\
=\frac{1}{256}[28+56+70+56+28]=\frac{238}{256}=\frac{119}{128}
\end{array}
$$

</details>

---

### Q135. MHT CET 2020 (20 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability distribution of a random variable $X$ is given by \begin{array}{|c|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 \\
\hline \mathrm{P}(\mathrm{X}=x) & \frac{1}{5} & \frac{2}{5} & \frac{2}{5} \\
\hline
\end{array} 
then the variance of $\mathrm{X}$ is

**Options:**

- **(A)** $\frac{14}{25}$
- **(B)** $\frac{9}{25}$
- **(C)** $\frac{6}{25}$
- **(D)** $\frac{1}{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{14}{25}$**

**Detailed Solution:**

\begin{array}{|c|c|c|c|}
\hline \mathrm{x}_{1} & \mathrm{p}\left(\mathrm{x}_{\mathrm{i}}\right) & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^{2} \\
\hline 0 & \frac{1}{5} & 0 & 0 \\
\hline 1 & \frac{2}{5} & \frac{2}{5} & \frac{2}{5} \\
\hline 2 & \frac{2}{5} & \frac{4}{5} & \frac{8}{5} \\
\hline
\end{array}
$$
\begin{aligned}
\therefore \Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} &=\frac{6}{5} \quad \text { and } \quad \Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^{2}=\frac{10}{5}=2 \\
\text { Variance } &=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^{2}-\left(\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}\right)^{2} \\
&=2-\left(\frac{6}{5}\right)^{2} \quad=2-\frac{36}{25}=\frac{14}{25}
\end{aligned}
$$

</details>

---

### Q136. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If a discrete random variable X has probability distribution as follows
$\begin{array}{|c|c|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 & 3 \\
\hline \mathrm{P}[\mathrm{X}=x] & \mathrm{k} & 3 \mathrm{k} & 3 \mathrm{k} & \mathrm{k} \\
\hline
\end{array}$
Then $\operatorname{var}(\mathrm{X})=$

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{22}{27}$
- **(C)** $\frac{24}{27}$
- **(D)** $\frac{23}{27}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{3}{4}$**

**Detailed Solution:**

Here $\mathrm{k}+3 \mathrm{k}+3 \mathrm{k}+\mathrm{k}=8 \mathrm{k}=1 \Rightarrow \mathrm{k}=\frac{1}{8}$
$\begin{aligned} \sum \mathrm{P}_{\left(\mathrm{x}_{1}\right)} \mathrm{x}_{\mathrm{i}} &=0 \times \frac{1}{8}+1 \times \frac{3}{8}+2 \times \frac{3}{8}+3 \times \frac{1}{8}=\frac{12}{8}=\frac{3}{2} \text { and } \\ \sum \mathrm{P}_{\left(\mathrm{x}_{i}\right)} \mathrm{x}_{\mathrm{i}}^{2} &=\left(0 \times \frac{1}{8}\right)+\left(1 \times \frac{3}{8}\right)+\left(4 \times \frac{3}{8}\right)+\left(9 \times \frac{1}{8}\right)=\frac{24}{8}=3 \\ \text { Variance } &=\mathrm{V}(\mathrm{X}) \\ &=\sum \mathrm{P}_{\left(\mathrm{x}_{i}\right)} \mathrm{x}_{\mathrm{i}}^{2}-\left[\sum \mathrm{P}_{\left(\mathrm{x}_{i}\right)} \mathrm{x}_{\mathrm{i}}\right]^{2} \\ &=3-\left(\frac{3}{2}\right)^{2}=3-\frac{9}{4}=\frac{3}{4} \end{aligned}$

</details>

---

### Q137. MHT CET 2020 (20 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If $f(x)=\frac{x}{8}$, if $0 < x < 4$
$=0$, otherwise is probability density function (p.d.f) of c.r.v. $X$ and $F(x)$ is c.d.f. associated with $f(x)$, then $\mathrm{F}(0 \cdot 5)=$

**Options:**

- **(A)** $\frac{1}{64}$
- **(B)** $\frac{1}{8}$
- **(C)** $\frac{1}{32}$
- **(D)** $\frac{1}{128}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{64}$**

**Detailed Solution:**

$F(x)=\int_{0}^{x} f(y) d y=\int_{0}^{x} \frac{y}{8} d y=\frac{1}{8}\left[\frac{y^{2}}{2}\right]_{0}^{x}$
$=\frac{1}{16}\left(x^{2}-0\right)=\frac{x^{2}}{16}$
$\therefore F(0.5)=\frac{(0.5)^{2}}{16}=\frac{1}{4 \times 16}=\frac{1}{64}$

</details>

---

### Q138. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $X$ is a r. v. with c. d. f. $F(x)$ and its probability distribution is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/nXz0Ca6CTVEM8_8G32UXJBgFf9KywFr7EDBYzCZ7iEk.original.fullsize.png">

then, $\mathrm{F}(1 \cdot 5)-\mathrm{F}(-0 \cdot 5)=$

**Options:**

- **(A)** $0 \cdot 2$
- **(B)** $0 \cdot 3$
- **(C)** $0 \cdot 1$
- **(D)** $0 \cdot 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $0 \cdot 4$**

**Detailed Solution:**

(B)
$\begin{array}{l}
F(1.5)-F(-0.5) \\
=P[X \leq 1.5]-P[X \leq-0.5] \\
=[P(X=-1.5)+P(X=-0.5)+P(X=0.5)+P(X=1.5)]-[P(X=-1.5)+P(X=-0.5)] \\
=P(X=0.5)+P(X=1.5)=0.15+0.25=0.4
\end{array}$

</details>

---

### Q139. MHT CET 2020 (19 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The c. d. f. $F(x)$ associated with p. d. f. $f(x)=3\left(1-2 x^{2}\right)$ if $0 < x < 1$
$=0$
otherwise
is $k\left(x-\frac{2 x^{3}}{k}\right)$, then value of $k$ is

**Options:**

- **(A)** 3
- **(B)** 1
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{1}{6}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

(D)
Since $f(x)$ is p.d.f. of r.v. therefore c.d.f. is
$F(x)=\int_{0}^{1} 3\left(1-2 x^{2}\right) d x=\left[3\left(x-\frac{2 x^{3}}{3}\right)\right]_{0}^{1}$
From given data, we get $k=3$

</details>

---

### Q140. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the p.m.f. of a r.v. $X$ is
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/li7PIl9RuMg1C8RKfUKitEVg076Leh_wTw_0KrOSQLg.original.fullsize.png">

then, the standard deviation of $\mathrm{X}$ is (given $p+q=1$ )

**Options:**

- **(A)** $2 \sqrt{q}$
- **(B)** $\sqrt{2 p q}$
- **(C)** $2 \sqrt{p}$
- **(D)** $\sqrt{p q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\sqrt{2 p q}$**

**Detailed Solution:**

(B)
\begin{array}{|c|c|c|c|}
\hline \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} & \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^{2} \\
\hline 0 & \mathrm{q}^{2} & 0 & 0 \\
\hline 1 & 2 \mathrm{pq} & 2 \mathrm{pq} & 2 \mathrm{pq} \\
\hline 2 & \mathrm{p}^{2} & 2 \mathrm{p}^{2} & 4 \mathrm{p}^{2} \\
\hline Total & & 2 \mathrm{pq}+2 \mathrm{p}^{2} & 2 \mathrm{pq}+4 \mathrm{p}^{2} \\
\hline
\end{array}
$\operatorname{Mean}(\mu)=\mathrm{E}(\mathrm{x})=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}} \quad=2 \mathrm{p}(\mathrm{p}+\mathrm{q})=2 \mathrm{p} \quad \ldots[\because \mathrm{p}+\mathrm{q}=1$, given $]$
Variance $\left(\sigma_{\mathrm{x}}^{2}\right)=\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}{ }^{2}-\mu^{2}$
$=2 \mathrm{pq}+4 \mathrm{p}^{2}-4 \mathrm{p}^{2}=2 \mathrm{pq}$
Standard deviation $\left(\sigma_{x}\right)=\sqrt{2 \mathrm{pq}}$

</details>

---

### Q141. MHT CET 2020 (19 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The c.d.f. $\mathrm{F}(x)$ of discrete r.v. $\mathrm{X}$ is given by
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/RxudHcN-tAzK4OTj214wKotLMZLi_mJE032XdMc-v-I.original.fullsize.png">

then $P[X=3]=$

**Options:**

- **(A)** $0 \cdot 85$
- **(B)** $0 \cdot 10$
- **(C)** $0 \cdot 75$
- **(D)** $0 \cdot 65$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0 \cdot 10$**

**Detailed Solution:**

(B)
$\begin{aligned}
\mathrm{P}[\mathrm{X}=3] &=\mathrm{F}(3)-\mathrm{F}(2) \\
&=0.75-0.65=0.10
\end{aligned}$

</details>

---

### Q142. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If a die is thrown at random, then the expectation of the number on it is

**Options:**

- **(A)** 2.4
- **(B)** 3.5
- **(C)** 2.1
- **(D)** 3.3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3.5**

**Detailed Solution:**

(D)
When a die is thrown, probability of getting any number from 1 to 6 is $\frac{1}{6}$. Expectation of a number on it to occur
$\begin{array}{l}
=\left(1 \times \frac{1}{6}\right)+\left(2 \times \frac{1}{6}\right)+\left(3 \times \frac{1}{6}\right)+\left(4 \times \frac{1}{6}\right)+\left(5 \times \frac{1}{6}\right)+\left(6 \times \frac{1}{6}\right) \\
=\frac{1}{6}(1+2+3+4+5+6)=\frac{21}{6}=3.5
\end{array}$

</details>

---

### Q143. MHT CET 2020 (16 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The p.d.f. of a continuous r.v. $\mathrm{X}$ is given by $\mathrm{f}(x)=\frac{x}{8}, 0 < x < 4$ $=0$, otherwise, then $\mathrm{P}(\mathrm{X} \leq 2)$ is

**Options:**

- **(A)** $\frac{5}{16}$
- **(B)** $\frac{9}{16}$
- **(C)** $\frac{7}{16}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{4}$**

**Detailed Solution:**

(C)
$\begin{aligned} \mathrm{P}(\mathrm{x} \leq 2) &=\int_{0}^{2} \mathrm{f}(\mathrm{x}) \mathrm{dx} \\ &=\int_{0}^{2} \frac{\mathrm{x}}{8} \mathrm{dx}=\frac{1}{8}\left[\frac{\mathrm{x}^{2}}{2}\right]_{0}^{2} \Rightarrow \frac{2^{2}}{16}-0=\frac{4}{16}=\frac{1}{4} \end{aligned}$

</details>

---

### Q144. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the p.m.f. of a r.v. $\mathrm{X}$ is given by $\mathrm{P}(\mathrm{X}=x)=\frac{\left(\begin{array}{l}5 \\ x\end{array}\right)}{2^{5}}$ if $x=0,1,2, \ldots \ldots 5$ $=0$ otherwise then which of the following is not true?

**Options:**

- **(A)** $P(X \leq 1)=P(X \geq 4)$
- **(B)** $P(X \leq 2) \geq P(X \geq 4)$
- **(C)** $P(X \leq 3) \leq P(X \geq 3)$
- **(D)** $P(X \leq 2)=P(X \geq 3)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $P(X \leq 3) \leq P(X \geq 3)$**

**Detailed Solution:**

(B)
$\begin{aligned}
P(X \leq 2) &=P(X=0)+P(X=1)+P(X=2) \\
&=\frac{{ }^{5} C_{0}}{2^{5}}+\frac{{ }^{5} C_{1}}{2^{5}}+\frac{{ }^{5} C_{2}}{2^{5}}=\frac{1+5+10}{2^{5}}=\frac{16}{2^{5}} \\
P(X \geq 4) &=P(X=4)+P(X=5) \\
&=\frac{C_{4}}{2^{4}}+\frac{C_{6}}{2^{6}}=\frac{5+1}{2^{5}}=\frac{6}{2^{5}}
\end{aligned}$
$\begin{aligned} \mathrm{P}(\mathrm{X} \leq 3) &=\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1)+\mathrm{P}(\mathrm{X}=2)+\mathrm{P}(\mathrm{X}=3) \\ &=\frac{{ }^{5} \mathrm{C}_{0}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{1}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{2}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{3}}{2^{5}}=\frac{1+5+10+10}{2^{5}}=\frac{26}{2^{5}} \\ \mathrm{P}(\mathrm{X} \geq 3) &=\mathrm{P}(\mathrm{X}=3)+\mathrm{P}(\mathrm{X}=4)+\mathrm{P}(\mathrm{X}=5) \\ &=\frac{{ }^{5} \mathrm{C}_{3}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{4}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{5}}{2^{5}}=\frac{10+5+1}{2^{5}}=\frac{16}{2^{5}} \\ \mathrm{P}(\mathrm{X} \leq 1) &=\mathrm{P}(\mathrm{X}=0)+\mathrm{P}(\mathrm{X}=1) \\ &=\frac{{ }^{5} \mathrm{C}_{0}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{1}}{2^{5}}=\frac{1+5}{2^{5}}=\frac{6}{2^{5}} \end{aligned}$

</details>

---

### Q145. MHT CET 2020 (16 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The p.d.f. of c.r.v. $X$ is given by $f(x)=\frac{x+2}{18}$ if -2 < x < 4=0 otherwise then $\mathrm{P}[|x| < 1]=$

**Options:**

- **(A)** $\frac{1}{18}$
- **(B)** $\frac{4}{9}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{2}{9}$**

**Detailed Solution:**

(A)
$\begin{array}{c}
f(x)=\frac{x+2}{18}, \quad-2 < x < 4 \\
=0, \quad \text { otherwise } \\
\begin{aligned}
P(|x| < 1)=P(-1 < x < 1) &=\int_{-1}^{1} \frac{x+2}{18} \mathrm{dx} \\
&=\int_{-1}^{1} f(x) d x=\frac{1}{18}\left[\frac{1}{2}+2-\frac{1}{2}+2\right]=\frac{4}{18}=\frac{2}{9}
\end{aligned}
\end{array}$

</details>

---

### Q146. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the p.m.f. is given by $\mathrm{P}(\mathrm{X})=\mathrm{k}\left(\begin{array}{c}4 \\ x\end{array}\right)$, for $x=0,1,2,3,4, \mathrm{k}>0$
$=0$, otherwise then the value of $\mathrm{k}$ is

**Options:**

- **(A)** $\frac{3}{16}$
- **(B)** $\frac{7}{16}$
- **(C)** $\frac{1}{16}$
- **(D)** $\frac{5}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{16}$**

**Detailed Solution:**

For $P(X=0)=k\left(\begin{array}{l}4 \\ 0\end{array}\right)=k \times{ }^{4} C_{0}=k \times 1=k$
$\therefore P(X=1)=k\left(\begin{array}{l}4 \\ 1\end{array}\right)=k \times{ }^{4} C_{1}=k(4)=4 k$
$$
\begin{array}{l}
P(X=2)=k\left(\begin{array}{l}
4 \\
2
\end{array}\right)=k \times{ }^{4} C_{2}=k(6)=6 k \\
P(X=3)=k\left(\begin{array}{l}
4 \\
3
\end{array}\right)=k x^{4} C_{3}=k(4)=4 k \\
P(x=4)=k\left(\begin{array}{l}
4 \\
4
\end{array}\right)=k \times 4 C_{4}=(k)(1)=k
\end{array}
$$
Since $P(X)$ is p.m.f.
$$
k+4 k+6 k+4 k+k=1 \Rightarrow 16 k=1 \Rightarrow k=\frac{1}{16}
$$

</details>

---

### Q147. MHT CET 2020 (15 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the probability distribution of X given below
$\begin{array}{|c|c|c|c|c|c|} \hline X=x & -2 & -1 & 0 & 1 & 2 \\ \hline \mathrm{P}(\mathrm{X}=x) & 0 \cdot 2 & 0 \cdot 3 & 0 \cdot 1 & 0 \cdot 15 & 0 \cdot 25 \\ \hline \end{array}$
The variance of $X$ is

**Options:**

- **(A)** $2.4257$
- **(B)** $2.5427$
- **(C)** $2.5742$
- **(D)** $2.2475$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2.2475$**

**Detailed Solution:**

$\sum_{i=1}^{n} x_{i} P_{i}=E(X)$
$\begin{aligned} E(X) &=(-2)(0.2)+(-1)(0.3)+0(0.1)+1(0.15)+2(0.25) \\ &=-0.4-0.3+0.15+0.50=-0.7+0.65=-0.05 \\ E\left(X^{2}\right) &=\sum_{i=1}^{n} x_{i}^{2} P_{i} \\ &=4(0.2)+1(0.3)+0(0.1)+1(0.15)+4(0.25) \\ &=0.8+0.3+0.15+1=2.25 \\ &=E\left(X^{2}\right)-[E(X)]^{2} \\ &=2.25-0.0025=2.2475 \end{aligned}$

</details>

---

### Q148. MHT CET 2020 (15 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $f(x)=\frac{x+2}{18},-2 < x < 4$
$=0 \quad, \quad$ otherwise,
is the p. d. f. of a r. v. X, then the value of $\mathrm{P}(|\mathrm{X}| < 2)$ is

**Options:**

- **(A)** $\frac{5}{9}$
- **(B)** $\frac{4}{9}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{9}$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}(|\mathrm{x}| < 2) &=\int_{-2}^{2} \frac{\mathrm{x}+2}{18} \mathrm{dx}=\frac{1}{18}\left[\frac{\mathrm{x}^{2}}{2}+2 \mathrm{x}\right]_{-2}^{2} \\ &=\frac{1}{18}[(2-2)+2(2+2)]=\frac{8}{18}=\frac{4}{9} \end{aligned}$

</details>

---

### Q149. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a discrete r. v. $X$ is \begin{array}{|c|c|c|c|c|c|}
\hline \mathrm{X}=x & 0 & 1 & 2 & 3 & 4 \\
\hline \mathrm{P}(\mathrm{X}=x) & k & 2 k & 4 \mathrm{k} & 2 k & k \\
\hline
\end{array}
then value of $\mathrm{P}(\mathrm{X} \leq 2)$ is

**Options:**

- **(A)** $\frac{1}{10}$
- **(B)** $\frac{7}{10}$
- **(C)** $\frac{3}{10}$
- **(D)** $\frac{9}{10}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{7}{10}$**

**Detailed Solution:**

Here $\mathrm{k}+2 \mathrm{k}+4 \mathrm{k}+2 \mathrm{k}+\mathrm{k}=10 \mathrm{k}=1 \Rightarrow \mathrm{k}=\frac{1}{10}$
Now $\mathrm{P}(\mathrm{X} \leq 2)=\mathrm{P}(0)+\mathrm{P}(1)+\mathrm{P}(2)=\frac{1}{10}+\frac{2}{10}+\frac{4}{10}=\frac{7}{10}$

</details>

---

### Q150. MHT CET 2020 (14 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the error involved in making a certain measurement is continuous random variable $\mathrm{X}$ with probability density function $f(x)=k\left(4-x^{2}\right)$ if $-2 \leq x \leq 2$
$=0 \quad$, otherwise
then, $\mathrm{P}[-1 < \mathrm{X} < 1]=$

**Options:**

- **(A)** $\frac{13}{16}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{11}{16}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{11}{16}$**

**Detailed Solution:**

Since the function represents a p.d.f.
$$
\begin{aligned}
& \int_{-2}^{2} k\left(4-x^{2}\right) d x=1 \\
\therefore & 2 \int_{0}^{2} k\left(4-x^{2}\right) d x=1 \Rightarrow 2 k\left[4 x-\frac{x^{3}}{3}\right]_{-0}^{2}=1 \\
\therefore & 2 k\left(8-\frac{8}{3}\right)=1 \Rightarrow 2 k\left(\frac{16}{3}\right)=1 \Rightarrow k=\frac{3}{32} \\
\therefore & P[-1 < x < 1] \\
&\left.=\int_{-1}^{1}\left(\frac{3}{32}\right)-4-x^{2}\right] d x=\frac{6}{32} \int\left(4-x^{2}\right) d x \\
&=\frac{6}{32} 4 x-\frac{x^{3}}{3}-0 \\
&=\frac{6}{32} 4-\frac{1}{3}=\frac{6}{32} \times \frac{11}{3}=\frac{11}{16}
\end{aligned}
$$

</details>

---

### Q151. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The p. d. f. of a continuous random variable $\mathrm{X}$ is given by
$f(x)=\frac{1}{2} \quad$ if $\quad 0 < x < 2$
$=0 \quad$ otherwise
and if $a=P\left(X < \frac{1}{2}\right), b=P\left(X>\frac{3}{2}\right)$, then relation between $a$ and $b$ is

**Options:**

- **(A)** $a-b=0$
- **(B)** $2a-b=0$
- **(C)** $3a-b=0$
- **(D)** $a-2 b=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $a-b=0$**

**Detailed Solution:**

$\begin{aligned} a &=PX < \frac{1}{2}=\int f(x) d x \\ &=\int f(x) d x-\int f(x) d x=0+\int \frac{1}{2} d x \\ &=\frac{1}{2}[x] \frac{1}{2}=\frac{1}{2} \frac{1}{2}-0 \quad=\frac{1}{4}=a=\frac{1}{4} \\ b &=P\left(X>\frac{3 a}{2}=\int f(x) d x\right.\\ &=\int_{\frac{3}{2}}^{2} f(x) d x+\int_{2}^{\infty} f(x) d x=\int_{\frac{3}{2}}^{2} \frac{1}{2} d x+0 \\ &=\frac{1}{2}[x]_{\frac{3}{2}}^{2}=\frac{1}{2}\left(2-\frac{3}{2}\right)=\frac{1}{2} \times \frac{1}{2}=\frac{1}{4} \Rightarrow b=\frac{1}{4} \\ \therefore & a-b=\frac{1}{4}-\frac{1}{4}=0 \quad \end{aligned}$

</details>

---

### Q152. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The cumulative distribution function of a continuous random variable $\mathrm{X}$ is given by
$F(X=x)=\frac{\sqrt{x}}{2}$, then $P[X>1]$ is

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{1}{\sqrt{2}}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{1}{2}$**

**Detailed Solution:**

Given c.d.f. is $f(x)=\frac{\sqrt{x}}{2}$
$\begin{aligned} \therefore P(0) &=0 \text { and } P(1)=\frac{1}{2} \\ P[x>1] &=1-P[x \leq 1] \\ &=1-\left(0+\frac{1}{2}\right)=\frac{1}{2} \end{aligned}$

</details>

---

### Q153. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If $\mu$ and $a^{2}$ are mean and variance of a random variable $X$ whose p. $m . f$. is given
by $P(X=x)=\left(\begin{array}{l}6 \\ x\end{array}\right)\left(\frac{1}{x}\right)^{x}\left(\frac{2}{x}\right)^{6-x}, x=0,1,2,3, \ldots \ldots 6$, then the value of $2 \mu+12 \sigma^{2}=$

**Options:**

- **(A)** 4
- **(B)** 8
- **(C)** 20
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 20**

**Detailed Solution:**

We have $P(X=x)={ }^{6} C_{x}\left(\frac{1}{3}\right)^{3}\left(\frac{2}{3}\right)^{6-x}$
$=\left(\frac{1}{3}+\frac{2}{3}\right)^{6}$
Thus, $\mathrm{n}=6, \mathrm{p}=\frac{1}{3}$ and $\mathrm{q}=\frac{2}{3}$
$\therefore$ Mean $=\mathrm{np}=(6)\left(\frac{1}{3}\right)=2$ and variance $=(6)\left(\frac{1}{3}\right)\left(\frac{2}{3}\right)=\frac{4}{3}$
$\therefore 2 \mu+12 \sigma^{2}=2(2)+12\left(\frac{4}{3}\right)=4+16=20$

</details>

---

### Q154. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the p. m. f. of a random variable $\mathrm{X}$ is
\begin{array}{|c|c|c|c|c|c|}
\hline \mathrm{X} & 1 & 2 & 3 & 4 & 5 \\
\hline \mathrm{P}(\mathrm{X}=x) & k & \frac{k}{3} & \frac{k}{4} & \frac{k}{2} & \frac{k}{2} \\
\hline
\end{array}
then $k=$

**Options:**

- **(A)** $\frac{15}{31}$
- **(B)** $\frac{1}{12}$
- **(C)** $\frac{11}{12}$
- **(D)** $\frac{12}{31}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{12}{31}$**

**Detailed Solution:**

Here $\mathrm{k}+\frac{\mathrm{k}}{3}+\frac{\mathrm{k}}{4}+\frac{\mathrm{k}}{2}+\frac{\mathrm{k}}{2}=1$
$\therefore \mathrm{k}\left(\frac{12+4+3+6+6}{12}\right)=1 \Rightarrow \mathrm{k}\left(\frac{31}{12}\right)=1 \Rightarrow \mathrm{k}=\frac{12}{13}$

</details>

---

### Q155. MHT CET 2020 (13 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the probability density function of a continuous random variable is $f(x)=\frac{x^{3}}{3}$ if $-1 < x < 2$
$=0$, otherwise,
then the cumulative distribution function of $X$ is

**Options:**

- **(A)** $\frac{1}{14}\left[x^{4}-1\right]$
- **(B)** $\frac{1}{10}\left[x^{4}-1\right]$
- **(C)** $\frac{1}{16}\left[x^{4}-1\right]$
- **(D)** $\frac{1}{12}\left[x^{4}-1\right]$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{12}\left[x^{4}-1\right]$**

**Detailed Solution:**

c.d.f. of $x$ is given by
$\begin{aligned}
\mathrm{f}(\mathrm{x}) &=\int_{-1}^{\mathrm{x}} \mathrm{f}(\mathrm{y}) \mathrm{dy} \quad=\int_{-1}^{\mathrm{x}} \frac{\mathrm{y}^{3}}{3} \mathrm{dy} \\
&=\left[\frac{\mathrm{y}^{4}}{12}\right]_{-1}^{\mathrm{x}}=\frac{1}{12}\left(\mathrm{x}^{4}-1\right)
\end{aligned}$

</details>

---

### Q156. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Given below is the probability distribution of discrete r.v. X
\begin{array}{|c|c|c|c|c|c|c|}
\hline \mathrm{X}=x & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline \mathrm{P}[\mathrm{X}=x] & \mathrm{k} & 0 & 2 \mathrm{k} & 5 \mathrm{k} & \mathrm{k} & 3 \mathrm{k} \\
\hline
\end{array}
Then $\mathrm{P}[\mathrm{X} \geq 4]=$

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{2}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{3}{4}$**

**Detailed Solution:**

Here $k+0+2 k+5 k+k+3 k=1 \Rightarrow k=\frac{1}{12}$
$\therefore P(X \geq 4)=5 k+k+3 k$
$=9 k=\frac{9}{12}=\frac{3}{4}$

</details>

---

### Q157. MHT CET 2020 (13 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the function $f$ defined by $f(x)=K\left(x-x^{2}\right)$ if $0 < x < 1$
$=0 \quad, \quad$ other wise
is the p.d.f. of a r. v. $X$, then the value of $P\left(X < \frac{1}{2}\right)$ is

**Options:**

- **(A)** $\frac{1}{4}$
- **(B)** $\frac{1}{2}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{1}{2}$**

**Detailed Solution:**

Given $f$ to a the p.df of a r.v.x.
$\begin{aligned}
& \int f(x) d x=1 \Rightarrow \int_{0}^{1} K\left(x-x^{2}\right) d x=1 \\
& K\left[\frac{x^{2}}{2}-\frac{x^{3}}{3}\right]_{0}^{1}=1 \Rightarrow K\left(\frac{1}{2}-\frac{1}{3}\right)=1 \Rightarrow \frac{K}{6}=1 \\
K &=6 \\
\therefore & P\left(x < \frac{1}{2}\right)=\int_{0}^{\frac{1}{2}} 6\left(x-x^{2}\right) d x=\left[\frac{6 x^{2}}{2}\right]_{0}^{1}-\left[\frac{6 x^{3}}{3}\right]_{0}^{1} \\
&=\left[3 x^{2}-2 x^{3}\right]_{0}^{\frac{1}{2}}=\frac{3}{4}-\frac{2}{8}=\frac{3}{4}-\frac{1}{4}=\frac{1}{2}
\end{aligned}$

</details>

---

### Q158. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The probability mass function of a random variable $X$ is $P(X=x)=\frac{5}{2^{5}} \quad$ if $\quad x=0,1,2,3,4,5$
$=0$
otherwise then, $P(X \leq 2)=$

**Options:**

- **(A)** $P(X>3)$
- **(B)** $P(X \geq 3)$
- **(C)** $P(X \geq 2)$
- **(D)** $P(X>4)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $P(X \geq 3)$**

**Detailed Solution:**

$\begin{aligned} \mathrm{P}(\mathrm{x} \leq 2) \quad &=\mathrm{P}(\mathrm{x}=0)+\mathrm{P}(\mathrm{x}=1)+\mathrm{P}(\mathrm{x}=2) \\ &=\frac{{ }^{5} \mathrm{C}_{0}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{1}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{2}}{2^{5}} \\ &=\frac{1}{2^{5}}(1+5+10)=\frac{16}{32} \\ \mathrm{P}(\mathrm{x} \geq 3) \quad &=\mathrm{P}(\mathrm{x}=3)+\mathrm{P}(\mathrm{x}=4)+\mathrm{P}(\mathrm{x}=5) \\ &=\frac{{ }^{5} \mathrm{C}_{3}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{4}}{2^{5}}+\frac{{ }^{5} \mathrm{C}_{5}}{2^{5}} \\ &=\frac{1}{2^{5}}(10+5+1)=\frac{16}{32} \end{aligned}$

</details>

---

### Q159. MHT CET 2020 (12 Oct Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

$\quad$ The p.d.f. of a random variable $\mathrm{X}$ is given by $f(x)=\frac{k}{\sqrt{x}} \quad$ if $0 \leq x \leq 4$
$=0$
otherwise, then $\mathrm{P}(1 < X < 4)=$

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{1}{5}$
- **(D)** $\frac{3}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{1}{2}$**

**Detailed Solution:**

Given $\mathrm{f}(\mathrm{x})=\frac{\mathrm{K}}{\sqrt{\mathrm{x}}}, \quad$ if $0 \leq \mathrm{x} \leq 4$
$\quad=0, \quad$ otherwise
$\therefore \quad \int_{0}^{4} \frac{\mathrm{K}}{\sqrt{\mathrm{x}}} \mathrm{dx}=1 \Rightarrow \mathrm{K}\left[\frac{\mathrm{x}^{\frac{1}{2}}}{\left(\frac{1}{2}\right)}\right]_{0}^{4}=1 \Rightarrow 2 \mathrm{~K}(\sqrt{4}-0)=1$
$\therefore \quad 4 \mathrm{~K}=1 \Rightarrow \mathrm{K}=\frac{1}{4}$
$\therefore \mathrm{P}(1 < \mathrm{x} < 4)=\int_{1}^{4}\left[\frac{\left(\frac{1}{4}\right)}{\sqrt{\mathrm{x}}}\right) \mathrm{dx}$
$=\frac{1}{4} \int_{1}^{4} \mathrm{x}^{-\frac{1}{2}} \mathrm{dx}=\frac{1}{4}\left[\frac{\mathrm{x}^{\frac{1}{2}}}{\left(\frac{1}{2}\right)}\right]_{1}^{4}=\frac{2}{4}\left[4^{\frac{1}{2}}-1\right]=\frac{1}{2}(2-1)=\frac{1}{2}$

</details>

---

### Q160. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the <math><mi>c</mi><mo>.</mo><mi></mi><mi>d</mi><mo>.</mo><mi></mi><mi>f</mi></math> . (cumulative distribution function) is given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>25</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>,</mo></math> then <math><mi>P</mi><mfenced separators="|"><mrow><mn>27</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>33</mn></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Cumulative distribution function is given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>25</mn></mrow><mrow><mn>10</mn></mrow></mfrac><mo>,</mo></math>  then <math><mi>f′</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>d</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></math>  
now, <math><mo> </mo><mo> </mo><mi>p</mi><mfenced separators="|"><mrow><mn>27</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>27</mn></mrow><mrow><mn>33</mn></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac><msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>27</mn></mrow><mrow><mn>33</mn></mrow></msubsup><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q161. MHT CET 2019 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A random variable <math><mi>X</mi></math> has following probability distribution 
<table border='1px solid'> <thead> <tr> <th> <math><mi>X</mi><mo>=</mo><mi>x</mi></math> </th> <th> <math><mn>1</mn></math> </th> <th> <math><mn>2</mn></math> </th> <th> <math><mn>3</mn></math> </th> <th> <math><mn>4</mn></math> </th> <th> <math><mn>5</mn></math> </th> <th> <math><mn>6</mn></math> </th> </tr> </thead> <tbody> <tr> <td> <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mi>x</mi></mrow></mfenced></math> </td> <td> <math><mi>K</mi></math> </td> <td> <math><mn>3</mn><mi>K</mi></math> </td> <td> <math><mn>5</mn><mi>K</mi></math> </td> <td> <math><mn>7</mn><mi>K</mi></math> </td> <td> <math><mn>8</mn><mi>K</mi></math> </td> <td> <math><mi>K</mi></math> </td> </tr> </tbody> </table> 
Then, <math><mi>P</mi><mfenced separators="|"><mrow><mn>2</mn><mo>≤</mo><mi>X</mi><mo>&lt;</mo><mn>5</mn></mrow></mfenced><mo>=</mo></math> ________

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>23</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>24</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given: Probability distribution 
<table border='1px solid'> <thead> <tr> <th> <math><mi>X</mi><mo>=</mo><mi>x</mi></math> </th> <th> <math><mn>1</mn></math> </th> <th> <math><mn>2</mn></math> </th> <th> <math><mn>3</mn></math> </th> <th> <math><mn>4</mn></math> </th> <th> <math><mn>5</mn></math> </th> <th> <math><mn>6</mn></math> </th> </tr> </thead> <tbody> <tr> <td> <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mi>x</mi></mrow></mfenced></math> </td> <td> <math><mi>K</mi></math> </td> <td> <math><mn>3</mn><mi>K</mi></math> </td> <td> <math><mn>5</mn><mi>K</mi></math> </td> <td> <math><mn>7</mn><mi>K</mi></math> </td> <td> <math><mn>8</mn><mi>K</mi></math> </td> <td> <math><mi>K</mi></math> </td> </tr> </tbody> </table> 
<math><mo>∵</mo><mi mathvariant="normal"></mi><mrow><munderover><mo stretchy="true">∑</mo><mrow><mn>1</mn><mo>=</mo><mn>1</mn></mrow><mrow><mn>6</mn></mrow></munderover><mrow><mi>p</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></mrow></mrow><mo>&#8658;</mo><mn>25</mn><mi>k</mi><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>  
then, <math><mo> </mo><mi>p</mi><mfenced separators="|"><mrow><mn>2</mn><mo>≤</mo><mi>x</mi><mo>&lt;</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>4</mn></mrow></mfenced></math>  
<math><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mn>5</mn><mi>k</mi><mo>+</mo><mn>7</mn><mi>k</mi></math>  
<math><mo>=</mo><mn>15</mn><mi>k</mi><mo>&#8658;</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q162. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the standard deviation of the random variable X is <math><msqrt><mn>3</mn><mi>p</mi><mi>q</mi></msqrt></math> and mean is 3p then <math><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mo>…</mo><mo>.</mo></math>

**Options:**

- **(A)** <math><mn>3</mn><mi>p</mi><mi>q</mi><mo>+</mo><mn>3</mn><msup><mrow><mi>q</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>3</mn><mi>p</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>p</mi></mrow></mfenced></math>
- **(C)** <math><mn>3</mn><mi>p</mi><mi>q</mi><mo>+</mo><mn>3</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup></math>
- **(D)** <math><mn>3</mn><mi>q</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>q</mi></mrow></mfenced></math> ]

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>3</mn><mi>p</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>p</mi></mrow></mfenced></math>**

**Detailed Solution:**

Key Idea: Use p +q =1 and <math><mi>V</mi><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mi>E</mi><msup><mrow><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>E</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>  
We have standard deviation of X = <math><msqrt><mn>3</mn><mi>p</mi><mi>q</mi></msqrt></math>  
<math><mo>&#8658;</mo><mi>V</mi><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>p</mi><mi>q</mi></math>  
and mean, <math><mi>E</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mi>p</mi></math>  
Now, <math><mn>3</mn><mi>p</mi><mi>q</mi><mo>=</mo><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>3</mn><mi>p</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mfenced separators="|"><mrow><mo>∵</mo><mi>V</mi><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>X</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mi>E</mi><msup><mrow><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>X</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>3</mn><mi>p</mi><mi>q</mi><mo>+</mo><mn>9</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>=</mo><mn>3</mn><mi>p</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>p</mi></mrow></mfenced><mo>+</mo><mn>9</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn><mi></mi></mrow></msup><mfenced separators="|"><mrow><mo>∵</mo><mi>p</mi><mo>+</mo><mi>q</mi><mo>=</mo><mn>1</mn></mrow></mfenced></math>  
<math><mo>=</mo><mn>3</mn><mi>p</mi><mo>-</mo><mn>3</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>9</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup></math>  
<math><mo>&#8658;</mo><mn>3</mn><mi>p</mi><mo>+</mo><mn>6</mn><msup><mrow><mi>p</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>&#8658;</mo><mn>3</mn><mi>p</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>p</mi></mrow></mfenced></math>

</details>

---

### Q163. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The p. d. f. of a random variable x is given by <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mo>,</mo><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>4</mn><mi>a</mi><mo>,</mo><mfenced separators="|"><mrow><mi>a</mi><mo>&gt;</mo><mn>0</mn></mrow></mfenced></math> =0, otherwise and <math><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&lt;</mo><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>k</mi><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&gt;</mo><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math> then K = …….

**Options:**

- **(A)** 1
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

We have p. d. f. of a random variable x is given by 
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mo>,</mo><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>4</mn><mi>a</mi><mo>.</mo><mfenced separators="|"><mrow><mi>a</mi><mo>&gt;</mo><mn>0</mn></mrow></mfenced></math>  
and also, <math><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&lt;</mo><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mi>k</mi><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&gt;</mo><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mrow><mi>d</mi><mi>x</mi><mo>=</mo><mi>k</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mn>4</mn><mi>a</mi></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mo>&#8658;</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi><mo>=</mo><mi>k</mi><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mn>4</mn><mi>a</mi></mrow></msubsup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></mrow></mrow></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mrow><mi>d</mi><mi>x</mi></mrow></mrow><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><mn>4</mn><mi>a</mi></mrow></mfrac><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mn>4</mn><mi>a</mi></mrow></msubsup><mrow><mi>d</mi><mi>x</mi></mrow></mrow></math>  
<math><mo>&#8658;</mo><msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mn>0</mn></mrow><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msubsup><mo>=</mo><mi>k</mi><msubsup><mrow><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><mrow><mn>4</mn><mi>a</mi></mrow></msubsup></math>  
<math><mo>&#8658;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mi>k</mi><mfenced separators="|"><mrow><mn>4</mn><mi>a</mi><mo>-</mo><mfrac><mrow><mn>5</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mi>k</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn><mi>a</mi></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>1</mn></math>

</details>

---

### Q164. MHT CET 2019 (Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In a binomial distribution, mean is 18 and variance is 12 then p = ….

**Options:**

- **(A)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

We know that, mean = <math><mi>n</mi><mi>p</mi><mo>=</mo><mn>18</mn></math> and variance <math><mo>=</mo><mi>n</mi><mo>=</mo><mi>p</mi><mi>q</mi><mo>=</mo><mn>12</mn></math>  
Now, <math><mfrac><mrow><mn>2</mn><mi>p</mi><mi>q</mi></mrow><mrow><mi>n</mi><mi>p</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>18</mn></mrow></mfrac><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>  
<math><mo>∴</mo><mi>p</mi><mo>=</mo><mo>-</mo><mn>1</mn><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

</details>

---

### Q165. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

A player tosses 2 fair coins. He wins Rs. 5 if 2 heads appear, Rs. 2 If 1 head appear and Rs. 1 if no head appears, then variance of his winning amount is

**Options:**

- **(A)** 6
- **(B)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

When player tosses 2 fair coins then
<math><mi>S</mi><mo>=</mo><mfenced close="}" open="{" separators="|"><mrow><mi>H</mi><mi>T</mi><mo>,</mo><mi>T</mi><mi>H</mi><mo>,</mo><mi>T</mi><mi>T</mi><mo>,</mo><mi>H</mi><mi>H</mi></mrow></mfenced></math>
Let X be a random variable that denotes the amount received by the player.
Then, X can take value 5, 2 and 1.
Now, <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
and <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
Thus, the probability distribution of X is
<math><mover accent="true"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><munder><mrow><mtext>       </mtext><mi>X</mi><mtext>        </mtext><mn>5</mn><mtext>         </mtext><mn>2</mn><mtext>         </mtext><mn>1</mn></mrow><mrow><mover accent="false"><mrow></mrow><mo>¯</mo></mover></mrow></munder></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mtext> </mtext><mfrac><mrow><mtext>  </mtext><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mtd></mtr></mtable></mrow><mo>-</mo></mover></math>
<math><mo>∴</mo><mi></mi></math> Variance of <math><mi>X</mi><mo>=</mo><msup><mrow><mo>∑</mo><msup><mrow><mi>X</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>-</mo><mfenced close="]" open="[" separators="|"><mrow><mo>∑</mo><mi>X</mi><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
Now <math><mo>∑</mo><mi>X</mi><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>5</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>2</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mo>∴</mo><mi></mi></math> Variance of <math><mi>X</mi><mo>=</mo><mo>∑</mo><msup><mrow><mi>X</mi></mrow><mrow><mn>2</mn></mrow></msup><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mo>∑</mo><mi>X</mi><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>25</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mn>4</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>1</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>25</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfrac><mrow><mn>25</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>9</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

</details>

---

### Q166. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The pdf of a random variable X is <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn><mo>=</mo></math> 0 otherwise. The <math><mi>P</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&lt;</mo><mi>X</mi><mo>&lt;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>179</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>159</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>169</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>189</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>179</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>**

**Detailed Solution:**

We have, p.d.f of a random varlabe
X is <math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>,</mo><mn>0</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>1</mn></math>
<math><mo>=</mo><mn>0</mn><mo>,</mo></math> otherwise
<math><mo>∴</mo><mi>p</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>&lt;</mo><mi>X</mi><mo>&lt;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msubsup><mrow><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mrow><msubsup><mo stretchy="true">∫</mo><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msubsup><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mi>d</mi><mi>x</mi></mrow></mrow></math>
<math><mo>=</mo><mn>3</mn><msubsup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>x</mi><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>4</mn></mrow></mrow></mrow><mrow><mrow><mrow><mn>1</mn></mrow><mo>/</mo><mrow><mn>3</mn></mrow></mrow></mrow></msubsup></math>
<math><mo>=</mo><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math>
<math><mo>=</mo><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow></mfenced></math>
<math><mo>=</mo><mn>3</mn><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>37</mn></mrow><mrow><mn>1728</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mn>3</mn><mo>×</mo><mfrac><mrow><mn>179</mn></mrow><mrow><mn>2592</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>179</mn></mrow><mrow><mn>864</mn></mrow></mfrac></math>

</details>

---

### Q167. MHT CET 2019 (Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let X be the number of successes in ‘n’ independent Bernoulli trials with probability of success <math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> . The least value of ‘n’ so that <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>≥</mo><mn>1</mn></mrow></mfenced><mo>≥</mo><mn>0.9375</mn></math> is….

**Options:**

- **(A)** 2
- **(B)** 1
- **(C)** 4
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2**

**Detailed Solution:**

We have, <math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>  
It is given that <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>≥</mo><mn>1</mn></mrow></mfenced><mo>≥</mo><mn>0.9375</mn></math>  
<math><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>≥</mo><mn>0.9375</mn></math>  
<math><mo>=</mo><mn>1</mn><msup><mrow><mo>-</mo></mrow><mrow><mi>n</mi></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>p</mi></mrow><mrow><mn>0</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mi>g</mi></mrow></mfenced></mrow><mrow><mi>n</mi><mo>-</mo><mn>0</mn></mrow></msup><mo>≥</mo><mn>0.9375</mn></math>  
<math><mo>=</mo><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mo>≥</mo><mn>0.9375</mn></math>  
<math><mo>=</mo><mn>1</mn><mo>-</mo><mn>0.9375</mn><mo>≥</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup></math>  
<math><mo>=</mo><mn>0.0625</mn><mo>≥</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup></math>  
<math><mo>=</mo><mfrac><mrow><mn>625</mn></mrow><mrow><mn>10000</mn></mrow></mfrac><mo>≥</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup></math>  
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>≥</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup></math>  
<math><mo>=</mo><mn>16</mn><mo>≤</mo><msup><mrow><mn>4</mn></mrow><mrow><mi>n</mi></mrow></msup></math>  
<math><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>2</mn></math>

</details>

---

### Q168. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

A coin is tossed three times. If <math><mi>X</mi></math> denotes the absolute difference between the number of heads and the number of tails then <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math> <mrow> <mi>H</mi><mtext> </mtext><mi>H</mi><mtext> </mtext><mi>H</mi><mo>−</mo><mn>3</mn><mi>H</mi></mrow> </math> and <math> <mrow> <mn>0</mn><mi>T</mi></mrow> </math>
<math> <mrow> <mi>H</mi><mtext> </mtext><mi>H</mi><mtext> </mtext><mi>T</mi><mo>−</mo><mn>2</mn><mi>H</mi></mrow> </math> and <math> <mrow> <mn>1</mn><mi>T</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>H</mi><mtext> </mtext><mi>T</mi><mtext> </mtext><mi>H</mi><mo>−</mo><mn>2</mn><mi>H</mi></mrow> </math> and <math> <mrow> <mn>1</mn><mi>T</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>H</mi><mtext> </mtext><mi>T</mi><mtext> </mtext><mi>T</mi><mo>−</mo><mn>1</mn><mi>H</mi></mrow> </math> and <math> <mrow> <mn>2</mn><mi>T</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>T</mi><mtext> </mtext><mi>H</mi><mtext> </mtext><mi>H</mi><mo>−</mo><mn>2</mn><mi>H</mi></mrow> </math> and <math> <mrow> <mn>1</mn><mi>T</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>T</mi><mtext> </mtext><mi>H</mi><mtext> </mtext><mi>T</mi><mo>−</mo><mn>2</mn><mi>T</mi></mrow> </math> and <math> <mrow> <mn>1</mn><mi>H</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>T</mi><mtext> </mtext><mi>T</mi><mtext> </mtext><mi>H</mi><mo>−</mo><mn>2</mn><mi>T</mi></mrow> </math> and <math> <mrow> <mn>1</mn><mi>H</mi><mo>=</mo><mrow><mo>|</mo> <mrow> <mi>n</mi><mrow><mo>(</mo> <mi>H</mi> <mo>)</mo></mrow><mo>−</mo><mi>n</mi><mrow><mo>(</mo> <mi>T</mi> <mo>)</mo></mrow></mrow> <mo>|</mo></mrow><mo>=</mo><mn>1</mn></mrow> </math>
<math> <mrow> <mi>T</mi><mtext> </mtext><mi>T</mi><mtext> </mtext><mi>T</mi><mo>−</mo><mn>3</mn><mi>T</mi></mrow> </math>
<math> <mrow> <mi>P</mi><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>=</mo><mn>1</mn></mrow> <mo>)</mo></mrow><mo>=</mo><mfrac> <mn>6</mn> <mn>8</mn> </mfrac> <mo>=</mo><mfrac> <mn>3</mn> <mn>4</mn> </mfrac> </mrow> </math>
<strong>Or (second method)</strong>
Probability distribution of X
 <table border="1" cellpadding="1" cellspacing="1" style="width:100%;">	<tbody>		<tr>			<td>Out come</td>			<td>3T</td>			<td>2T1H</td>			<td>1T2H</td>			<td>3H</td>		</tr>		<tr>			<td>X</td>			<td>3</td>			<td>1</td>			<td>1</td>			<td>3</td>		</tr>		<tr>			<td>P</td>			<td><math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> </mrow> </math></td>			<td><math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> </mrow> </math></td>			<td><math> <mrow> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> </mrow> </math></td>			<td><math> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> </mrow> </math></td>		</tr>	</tbody></table>
<math><mrow><mo>⇒</mo> <mtext>P</mtext> <mfenced close=")" open="(" separators=","> <mrow> <mtext>X</mtext> <mo>=</mo> <mn>1</mn> </mrow> </mfenced> <mo>=</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> <mo>+</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>8</mn> </mrow> </mfrac> <mo>=</mo> <mfrac> <mrow> <mn>3</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>

</details>

---

### Q169. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>X</mi><mo>~</mo><mi>B</mi><mfenced separators="|"><mrow><mi>n</mi><mo>,</mo><mi> </mi><mi>p</mi></mrow></mfenced></math> with <math><mi>n</mi><mo>=</mo><mn>10</mn><mo>,</mo><mi> </mi><mi>p</mi><mo>=</mo><mn>0.4</mn></math> then <math><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>X</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mn>4</mn></math>
- **(B)** <math><mn>2.4</mn></math>
- **(C)** <math><mn>3.6</mn></math>
- **(D)** <math><mn>18.4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>18.4</mn></math>**

**Detailed Solution:**

Given <math> <mrow> <mi>X</mi><mo>∼</mo><mi>B</mi><mrow><mo>(</mo> <mrow> <mi>n</mi><mo>,</mo><mtext> </mtext><mi>p</mi></mrow> <mo>)</mo></mrow><mo>;</mo><mi>n</mi><mo>=</mo><mn>10</mn><mo>,</mo><mtext> </mtext><mi>p</mi><mo>=</mo><mn>0.4</mn></mrow> </math>
<math> <mrow> <mo>&rArr;</mo><mi>q</mi><mo>=</mo><mn>0.6</mn></math>
We know that <math> <mrow> <mi>V</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow><mo>=</mo><mi>n</mi><mi>p</mi><mi>q</mi><mtext> </mtext>
<mi>E</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow><mo>=</mo><mi>n</mi><mi>p</mi></mrow> </math>
<math> <mo>&rArr;</mo><mrow> <mi>V</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow><mo>=</mo><mn>10</mn><mo>×</mo><mn>0.4</mn><mo>×</mo><mn>0.6</mn><mo>=</mo><mn>2.4</mn></mrow> </math> 
 <math> <mrow> <mi>E</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow><mo>=</mo><mn>10</mn><mo>×</mo><mn>0.4</mn><mo>=</mo><mn>4</mn></mrow> </math>
Also <math> <mrow> <mtext> </mtext><mi>V</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow><mo>=</mo><mi>E</mi><mrow><mo>(</mo> <mrow> <msup> <mi>X</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow><mo>−</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mi>E</mi><mrow><mo>(</mo> <mi>X</mi> <mo>)</mo></mrow></mrow> <mo>)</mo></mrow></mrow> <mn>2</mn> </msup> </mrow> </math>
<math> <mrow><mo>&rArr;</mo> <mn>2.4</mn><mo>+</mo><msup> <mn>4</mn> <mn>2</mn> </msup> <mo>=</mo><mi>E</mi><mrow><mo>(</mo> <mrow> <msup> <mi>X</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow></mrow> </math>
<math> <mrow><mo>&rArr;</mo> <mi>E</mi><mrow><mo>(</mo> <mrow> <msup> <mi>X</mi> <mn>2</mn> </msup> </mrow> <mo>)</mo></mrow><mo>=</mo><mn>18.4</mn></mrow> </math>

</details>

---

### Q170. MHT CET 2018

*Type:* `singleCorrect` | *Level:* `2`

A die is rolled. If <math><mi>X</mi></math> denotes the number of positive divisors of the outcome then the range of the random variable <math><mi>X</mi></math> is

**Options:**

- **(A)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn></mrow></mfenced></math>
- **(B)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>
- **(C)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn><mo>,</mo><mi> </mi><mn>5</mn><mo>,</mo><mi> </mi><mn>6</mn></mrow></mfenced></math>
- **(D)** <math><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>5</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>,</mo><mi> </mi><mn>2</mn><mo>,</mo><mi> </mi><mn>3</mn><mo>,</mo><mi> </mi><mn>4</mn></mrow></mfenced></math>**

**Detailed Solution:**

The possible outcomes with their positive divisors are:-
\(
\begin{array}{|c|c|c|}
\hline \text { outcome } & \text { positive divisors } & \text { number (X) } \\
\hline 1 & 1 & 1 \\
\hline 2 & 1,2 & 2 \\
\hline 3 & 1,3 & 2 \\
\hline 4 & 1,2,4 & 3 \\
\hline 5 & 1,5 & 2 \\
\hline 6 & 1,2,3,6 \\
\hline
\end{array}
\)
Hence, Range of \(X=\{1,2,3,4\}\)

</details>

---

### Q171. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `2`

For the following distribution function <math><mi>F</mi><mo>(</mo><mi>x</mi><mo>)</mo></math> of a random variable <math><mi>X</mi></math>

<table border="1">
	<tbody>
		<tr>
			<td>x</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
		</tr>
		<tr>
			<td>F(x)</td>
			<td>0.2</td>
			<td>0.37</td>
			<td>0.48</td>
			<td>0.62</td>
			<td>0.85</td>
			<td>1</td>
		</tr>
	</tbody>
</table>
<math><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mn>3</mn><mo>&lt;</mo><mi>X</mi><mi> </mi><mo>≤</mo><mn>5</mn></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math > <mrow>  <mn>0.48</mn> </mrow></math>
- **(B)** <math > <mrow>  <mn>0.37</mn> </mrow></math>
- **(C)** <math > <mrow>  <mn>0.27</mn> </mrow></math>
- **(D)** <math > <mrow>  <mn>1.47</mn> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math > <mrow>  <mn>0.37</mn> </mrow></math>**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/mhixbhrdiydlbxlvjsmvzhugddsgddkgeggzgxcaujikowgewg.jpeg" />
<math><mi>P</mi><mfenced separators="|"><mrow><mn>3</mn><mo>&lt;</mo><mi>x</mi><mo>≤</mo><mn>5</mn></mrow></mfenced><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mi> </mi><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>5</mn><mo>)</mo></math>
<math> <mrow> <mo>=</mo><mrow><mo>(</mo> <mrow> <mi>F</mi><mrow><mo>(</mo> <mn>4</mn> <mo>)</mo></mrow><mo>−</mo><mi>F</mi><mrow><mo>(</mo> <mn>3</mn> <mo>)</mo></mrow></mrow> <mo>)</mo></mrow><mo>+</mo><mrow><mo>(</mo> <mrow> <mi>F</mi><mrow><mo>(</mo> <mn>5</mn> <mo>)</mo></mrow><mo>−</mo><mi>F</mi><mrow><mo>(</mo> <mn>4</mn> <mo>)</mo></mrow></mrow> <mo>)</mo></mrow></mrow> </math>
<math><mo>=</mo><mn>0.14</mn><mo>+</mo><mn>0.23</mn></math>
<math><mo>=</mo><mn>0.37</mn></math>

</details>

---

### Q172. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `3`

A box contains <math> <mn>6</mn> </math> pens, <math> <mn>2</mn> </math> of which are defective. Two pens are taken randomly from the box. If random variable <math><mi>x</mi><mo>:</mo></math> Number of defective pens obtained, then standard deviation of <math><mi>x</mi><mo>=</mo></math>

**Options:**

- **(A)** <math><mo>±</mo><mi> </mi><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn><mo>√</mo><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>16</mn></mrow><mrow><mn>45</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn><msqrt><mn>5</mn></msqrt></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>x</mi></math> : no. of defective pens
Two pens are taken from box
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>x</mi></math> can taken values 0, 1, 2
<math><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mo>×</mo><mn>3</mn></mrow><mrow><mn>6</mn><mo>×</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math><mi>p</mi><mi> </mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>×</mo><msup><mrow><mi> </mi></mrow><mrow><mn>4</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>×</mo><mn>4</mn><mo>×</mo><mn>2</mn><mo>×</mo><mn>1</mn></mrow><mrow><mn>6</mn><mo>×</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math><mi>p</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>2</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msup><mrow><mi> </mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>×</mo><mn>2</mn><mo>×</mo><mn>1</mn></mrow><mrow><mn>6</mn><mo>×</mo><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math><table border="1">	<tbody>		<tr>			<td>x</td>			<td>P</td>			<td><math><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><msub><mrow><mi>p</mi></mrow><mrow><mi>i</mi></mrow></msub></math></td>			<td><math><msubsup><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msubsup><msub><mrow><mi>p</mi></mrow><mrow><mi>i</mi></mrow></msub></math></td>		</tr>		<tr>			<td>0</td>			<td><math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>			<td>0</td>			<td>0</td>		</tr>		<tr>			<td>1</td>			<td><math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>8</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>		</tr>		<tr>			<td>2</td>			<td><math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>			<td><math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math></td>		</tr>	</tbody></table><math><mi>E</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>10</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>15</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
Standard deviation <math><mo>=</mo><msqrt><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mi>E</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
Standard deviation <math><mo>=</mo><msqrt><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></msqrt></math>
<math><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></msqrt></math>
<math><mo>=</mo><msqrt><mfrac><mrow><mn>4</mn><mo>×</mo><mn>4</mn></mrow><mrow><mn>45</mn></mrow></mfrac></msqrt></math>
<math><mo>=</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn><mo>√</mo><mn>5</mn></mrow></mfrac></math>

</details>

---

### Q173. MHT CET 2017

*Type:* `singleCorrect` | *Level:* `1`

A random variable <math><mi>X</mi><mo>∽</mo><mi>B</mi><mo>(</mo><mi>n</mi><mo>,</mo><mi> </mi><mi>p</mi><mo>)</mo><mo>.</mo></math> If values of mean and variance of <math><mi>X</mi></math> are <math> <mrow> <mn>18</mn> </mrow> </math> and <math> <mrow> <mn>12</mn> </mrow> </math> respectively then total number of possible values of <math><mi>X</mi></math> are

**Options:**

- **(A)** <math > <mrow>  <mn>54</mn> </mrow></math>
- **(B)** <math > <mrow>  <mn>55</mn> </mrow></math>
- **(C)** <math > <mrow>  <mn>12</mn> </mrow></math>
- **(D)** <math > <mrow>  <mn>18</mn> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math > <mrow>  <mn>55</mn> </mrow></math>**

**Detailed Solution:**

Mean = np = 18
Variance = npq = 12
<math> <mo>⇒</mo> </math> <math><mfrac><mrow><mi>n</mi><mi>p</mi><mi>q</mi></mrow><mrow><mi>n</mi><mi>p</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>18</mn></mrow></mfrac></math>
<math> <mo>⇒</mo> </math> <math><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math> <mo>⇒</mo> </math> <math><mi>p</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>q</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math> <mo>⇒</mo> </math> <math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
Now <math><mi>n</mi><mi>p</mi><mo>=</mo><mn>18</mn></math>
<math> <mo>⇒</mo> </math> <math><mi>n</mi><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mn>18</mn></math>
<math> <mo>⇒</mo> </math> <math><mi>n</mi><mo>=</mo><mn>54</mn></math>
<math> <mo>⇒</mo> </math> <math><mo>∴</mo><mi> </mi><mi> </mi><mi> </mi><mi> </mi></math> Values of <math><mi>X</mi></math> are
0, 1, 2, ........... 54
<math><mo>∴</mo><mi> </mi><mi> </mi><mn>55</mn><mi> </mi></math> Values.

</details>

---

### Q174. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

If random variable <math><mi>X</mi><mo>∼</mo><mi>B</mi><mfenced separators="|"><mrow><mi>n</mi><mo>=</mo><mn>5</mn><mo>,</mo><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></math> then <math><mi>P</mi><mfenced separators="|"><mrow><mn>2</mn><mo>&lt;</mo><mi>X</mi><mo>&lt;</mo><mn>4</mn></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mfrac><mrow><mn>80</mn></mrow><mrow><mn>243</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>40</mn></mrow><mrow><mn>243</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>40</mn></mrow><mrow><mn>343</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>80</mn></mrow><mrow><mn>343</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>40</mn></mrow><mrow><mn>243</mn></mrow></mfrac></math>**

**Detailed Solution:**

Given
<math><mi>n</mi><mo>=</mo><mn>5</mn></math>
<math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mo>∴</mo><mi> </mi><mi> </mi><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
<math><mi>P</mi><mfenced separators="|"><mrow><mn>2</mn><mo>&lt;</mo><mi>x</mi><mo>&lt;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>3</mn></mrow></mfenced></math>
<math><mo>=</mo><msup><mrow><mi> </mi></mrow><mrow><mn>5</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>=</mo><mfrac><mrow><mn>5</mn><mo>×</mo><mn>4</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>27</mn></mrow></mfrac><mo>×</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>40</mn></mrow><mrow><mn>243</mn></mrow></mfrac></math>

</details>

---

### Q175. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `3`

If the probability distribution function of a random variable is given as

 
<table border="1">
	<tbody>
		<tr>
			<td><math><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub></math></td>
			<td><math><mo>-</mo><mn>2</mn></math></td>
			<td><math><mo>-</mo><mn>1</mn></math></td>
			<td><math><mn>0</mn></math></td>
			<td><math><mn>1</mn></math></td>
			<td><math><mn>2</mn></math></td>
		</tr>
		<tr>
			<td><math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow></mfenced></math></td>
			<td><math><mn>0.2</mn></math></td>
			<td><math><mn>0.3</mn></math></td>
			<td><math><mn>0.15</mn></math></td>
			<td><math><mn>0.25</mn></math></td>
			<td><math><mn>0.1</mn></math></td>
		</tr>
	</tbody>
</table>
Then <math><mi>F</mi><mfenced separators="|"><mrow><mn>0</mn></mrow></mfenced><mo>=</mo></math>

**Options:**

- **(A)** <math><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi><mo>&lt;</mo><mn>0</mn></mrow></mfenced></math>
- **(B)** <math><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi><mo>&gt;</mo><mn>0</mn></mrow></mfenced></math>
- **(C)** <math><mn>1</mn><mo>-</mo><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi><mo>&gt;</mo><mn>0</mn></mrow></mfenced></math>
- **(D)** <math><mn>1</mn><mo>-</mo><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi><mo>&lt;</mo><mn>0</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1</mn><mo>-</mo><mi>P</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi><mo>&gt;</mo><mn>0</mn></mrow></mfenced></math>**

**Detailed Solution:**

<math> <mrow> <mi>F</mi><mrow><mo>(</mo> <mrow> <msub> <mi>X</mi> <mi>i</mi> </msub> </mrow> <mo>)</mo></mrow></mrow> </math> is defind as <math> <mrow> <mi>F</mi><mrow><mo>(</mo> <mrow> <msub> <mi>X</mi> <mi>i</mi> </msub> </mrow> <mo>)</mo></mrow><mo>=</mo><mi>P</mi><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>≤</mo><msub> <mi>X</mi> <mi>i</mi> </msub> </mrow> <mo>)</mo></mrow></mrow> </math>
<math> <mrow> <mo>⇒</mo><mi>F</mi><mrow><mo>(</mo> <mn>0</mn> <mo>)</mo></mrow><mo>=</mo><mi>P</mi><mrow><mo>(</mo> <mrow> <mi>X</mi><mo>≤</mo><mn>0</mn></mrow> <mo>)</mo></mrow></mrow> </math>
<math> <mrow> <mo>           =</mo><mn>1</mn><mo>−</mo><mi>P</mi><mrow><mo>(</mo> <mrow><mi>X</mi><mo>&gt;</mo><mn>0</mn></mrow> <mo>)</mo></mrow></mrow> </math>

</details>

---

### Q176. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `3`

If random variable <math> <mrow> <mi>X</mi><mo>:</mo> </mrow> </math> waiting time in minutes for bus and probability distribution function of <math> <mrow> <mi>X</mi><mo>:</mo> </mrow> </math> is given by



<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi></mtd></mtr></mtable></mrow></mfenced></math>



Then probability of waiting time not more than <math> <mn>4</mn> </math> minutes is = _______

**Options:**

- **(A)** <math > <mrow>  <mn>0.3</mn> </mrow></math>
- **(B)** <math > <mrow>  <mn>0.8</mn> </mrow></math>
- **(C)** <math > <mrow>  <mn>0.2</mn> </mrow></math>
- **(D)** <math > <mrow>  <mn>0.5</mn> </mrow></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math > <mrow>  <mn>0.8</mn> </mrow></math>**

**Detailed Solution:**

As given,
<math><mi>f</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mfenced close="" open="{" separators="|"><mrow><mtable><mtr><mtd><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>,</mo></mtd><mtd><mn>0</mn><mo>≤</mo><mi>x</mi><mo>≤</mo><mn>5</mn></mtd></mtr><mtr><mtd><mn>0</mn><mo>,</mo></mtd><mtd><mi mathvariant="normal">o</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">w</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">s</mi><mi mathvariant="normal">e</mi></mtd></mtr></mtable></mrow></mfenced></math>
Now, probability of waiting time not more than 4 minutes is <math><mo>=</mo><mn>4</mn><mo>×</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>0.8</mn></math>

</details>

---

### Q177. MHT CET 2016

*Type:* `singleCorrect` | *Level:* `2`

Let <math><mi>X</mi><mo>~</mo><mi>B</mi><mfenced separators="|"><mrow><mi>n</mi><mo>,</mo><mi>p</mi></mrow></mfenced><mo>,</mo></math> if
<math><mi>E</mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>5</mn><mo>,</mo><mi> </mi><mi>V</mi><mi>a</mi><mi>r</mi><mi> </mi><mfenced separators="|"><mrow><mi>X</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mo>.</mo><mn>5</mn></math> then <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&lt;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mo>…</mo></math>

**Options:**

- **(A)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup></math>
- **(B)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>**

**Detailed Solution:**

Here,
 <math><mi>E</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mi>P</mi><mo>=</mo><mn>5</mn><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>V</mi><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced><mo>=</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>2.5</mn></math> 
 <math><mo>∴</mo><mi> </mi><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2.5</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> 
 <math><mo>∴</mo><mi> </mi><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi> </mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">d</mi><mi> </mi><mi>n</mi><mo>=</mo><mn>10</mn></math>  
Now,  <math><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>)</mo></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi> </mi><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mi> </mi></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math> 
 <math><mo>⇒</mo><mi> </mi><mi> </mi><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>&lt;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>

</details>

---

### Q178. MHT CET 2010

*Type:* `singleCorrect` | *Level:* `1`

Two coins are tossed simultaneously. Then, the value of $E(X)$, where $X$ denotes the number of heads is

**Options:**

- **(A)** $\frac{1}{2}$
- **(B)** 2
- **(C)** 1
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1**

**Detailed Solution:**

Here, $n=2, \quad p=\frac{1}{2}$
$$
E(X)=\text { mean }=n p=2 \times \frac{1}{2}=1
$$

</details>

---

### Q179. MHT CET 2008

*Type:* `singleCorrect` | *Level:* `3`

A random variable $X$ has the probability distribution
\begin{array}{l|c|c|c|c|c|c|c|c}
\hlinex & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hlineP(x) & 0.15 & 0.23 & 0.12 & 0.10 & 0.20 & 0.08 & 0.07 & 0.05 \\
\hline
\end{array}
For the events $E=\{x$ is prime number $\}$ and $F=\{x < 4\}$ the probability of $P(E \cup F)$ is

**Options:**

- **(A)** $0.50$
- **(B)** $0.77$
- **(C)** $0.35$
- **(D)** $0.87$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.77$**

**Detailed Solution:**

Given, $E=\{x$ is a prime number $\}$
$$
\begin{aligned}
P(E) &=P(2)+P(3)+P(5)+P(7) \\
&=0.23+0.12+0.20+0.07=0.62 \\
\text { and } \quad F &=\{x < 4\} \\
P(F) &=P(1)+P(2)+P(3) \\
&=0.15+0.23+0.12=0.50 \\
\text { and } \quad P(E \cap F) &=P(2)+P(3) \\
=& 0.23+0.12=0.35 \\
\therefore \quad P(E \cup F) &=P(E)+P(F)-P(E \cap F) \\
&=0.62+0.50-0.35 \\
&=0.77
\end{aligned}
$$

</details>

---

