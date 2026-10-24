# MHT CET Mathematics - Statistics

## Topic 1: Statistics

**Total Questions:** 5

---

### Q1. MHT CET 2024 (04 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The variance of first 50 even natural numbers is

**Options:**

- **(A)** 833
- **(B)** 473
- **(C)** $\dfrac{437}{4}$
- **(D)** $\dfrac{833}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 833**

**Detailed Solution:**

Let the first $50$ even natural numbers be $x_i = 2i$, where $i = 1, 2, \dots, 50$.

The variance of a variable $x$ is given by $\text{Var}(x) = \dfrac{\sum x_i^2}{n} - \left(\dfrac{\sum x_i}{n}\right)^2$.

We know that if $x_i = 2i$, then $\text{Var}(x) = 4 \text{Var}(i)$.

The variance of the first $n$ natural numbers is $\dfrac{n^2 - 1}{12}$.

For $n = 50$, the variance of the first $50$ natural numbers is $\dfrac{50^2 - 1}{12} = \dfrac{2500 - 1}{12} = \dfrac{2499}{12}$.

Therefore, the variance of the first $50$ even natural numbers is $4 \times \dfrac{2499}{12} = \dfrac{2499}{3} = 833$.

Answer: 833

</details>

---

### Q2. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A student scores the following marks in five tests : $54,45,41,43,57$. His score is not known for the sixth test. If the mean score is 48 in six tests, then the standard deviation of marks in six tests is

**Options:**

- **(A)** $\dfrac{100}{\sqrt{3}}$
- **(B)** $\dfrac{10}{\sqrt{3}}$
- **(C)** $\dfrac{100}{3}$
- **(D)** $\dfrac{10}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\dfrac{10}{\sqrt{3}}$**

**Detailed Solution:**

Let the score in the sixth test be $x$.

Given that the mean score of six tests is $48$, we have:

$\dfrac{54 + 45 + 41 + 43 + 57 + x}{6} = 48$

$\dfrac{240 + x}{6} = 48$

$240 + x = 288 \Rightarrow x = 48$

The scores in the six tests are $54, 45, 41, 43, 57, 48$.

The variance $\sigma^2$ is given by $\dfrac{\sum (x_i - \bar{x})^2}{n}$.

Calculating the sum of squared deviations from the mean:

$\sum (x_i - 48)^2 = (54 - 48)^2 + (45 - 48)^2 + (41 - 48)^2 + (43 - 48)^2 + (57 - 48)^2 + (48 - 48)^2$

$\sum (x_i - 48)^2 = 6^2 + (-3)^2 + (-7)^2 + (-5)^2 + 9^2 + 0^2$

$\sum (x_i - 48)^2 = 36 + 9 + 49 + 25 + 81 + 0 = 200$

The variance is $\sigma^2 = \dfrac{200}{6} = \dfrac{100}{3}$.

The standard deviation is $\sigma = \sqrt{\dfrac{100}{3}} = \dfrac{10}{\sqrt{3}}$.

Answer: $\dfrac{10}{\sqrt{3}}$

</details>

---

### Q3. MHT CET 2024 (03 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the probability distribution
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/lkgPuhVHNMRMw4_t4zPjePidwHiVVwsPhwKdW2tCp4o.original.fullsize.png"/>
Then the $\operatorname{Var}(\mathrm{X})$ is
(Given :
$\left.(0.25)^2=0.0625,(0.35)^2=0 \cdot 1225,(0.45)^2=0 \cdot 2025\right)$

**Options:**

- **(A)** 0.8275
- **(B)** 1.1225
- **(C)** 1.8275
- **(D)** $2 \cdot 0725$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1.8275**

**Detailed Solution:**

The variance of a random variable $X$ is given by the formula:

$\operatorname{Var}(X) = E(X^2) - [E(X)]^2$

First, we calculate the expected value $E(X)$:

$E(X) = \sum x_i p(x_i)$

$E(X) = (-2)(0\cdot 1) + (-1)(0\cdot 2) + (0)(0\cdot 2) + (1)(0\cdot 3) + (2)(0\cdot 15) + (3)(0\cdot 05)$

$E(X) = -0\cdot 2 - 0\cdot 2 + 0 + 0\cdot 3 + 0\cdot 3 + 0\cdot 15$

$E(X) = -0\cdot 4 + 0\cdot 75 = 0\cdot 35$

Next, we calculate $E(X^2)$:

$E(X^2) = \sum x_i^2 p(x_i)$

$E(X^2) = (-2)^2(0\cdot 1) + (-1)^2(0\cdot 2) + (0)^2(0\cdot 2) + (1)^2(0\cdot 3) + (2)^2(0\cdot 15) + (3)^2(0\cdot 05)$

$E(X^2) = 4(0\cdot 1) + 1(0\cdot 2) + 0(0\cdot 2) + 1(0\cdot 3) + 4(0\cdot 15) + 9(0\cdot 05)$

$E(X^2) = 0\cdot 4 + 0\cdot 2 + 0 + 0\cdot 3 + 0\cdot 6 + 0\cdot 45$

$E(X^2) = 1\cdot 95$

Now, we substitute these values into the variance formula:

$\operatorname{Var}(X) = 1\cdot 95 - (0\cdot 35)^2$

Given that $(0\cdot 35)^2 = 0\cdot 1225$:

$\operatorname{Var}(X) = 1\cdot 95 - 0\cdot 1225 = 1\cdot 8275$

Answer: 1.8275

</details>

---

### Q4. MHT CET 2020 (14 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A die is thrown 100 times, then the standard deviation of getting an even number is

**Options:**

- **(A)** 10
- **(B)** 5
- **(C)** 20
- **(D)** 15

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

Let $x$ denote the number of succeses in 100 Then $x$ follows binomial distribution with $n=1008$ $p=y_{2}, q=\frac{1}{2}$
$\therefore$ variance of $x=n p q=100 \times \frac{1}{2} \times \frac{1}{2}=25$
$\begin{array}{l}\text { Standard } \\ \text { Deviation }\end{array}=\sqrt{\text { vatiance }}=\sqrt{25}$
$=5$

</details>

---

### Q5. MHT CET 2020 (12 Oct Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $\mathrm{X}$ takes the values $0,1,2$. Its mean is $1 \cdot 2 .$ If $\mathrm{P}(\mathrm{X}=0)=0.3$,
then $\mathrm{P}(\mathrm{X}=1)=$

**Options:**

- **(A)** $0.1$
- **(B)** $0.5$
- **(C)** $0.2$
- **(D)** $0.4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $0.2$**

**Detailed Solution:**

Random variable
$\begin{array}{l}
x \text { takes }=0,1,2 \\
\sum x_{i} P\left(x_{i}\right)=\text { Mean } \\
1.2=(0 * 0.3)+1 \times P(x=1)+2 \times P(x=2) \\
P(x=1)+2 P(x=2)=1.2 \rightarrow(1) \\
P(x=1)+P(x=2)+P(x=0)=1 \\
P(x=1)+P(x=2)=0.7 \rightarrow(2)
\end{array}$
By Solving (1) \& (2)
$\begin{array}{l}
P(x=2)=0.5 \\
P(x=1)=0.2 .
\end{array}$

</details>

---

