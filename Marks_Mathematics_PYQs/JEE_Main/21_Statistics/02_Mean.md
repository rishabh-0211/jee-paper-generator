# JEE Main Mathematics - Statistics

## Topic 2: Mean

**Total Questions:** 25

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A data consists of $20$ observations $x_1, x_2, \ldots, x_{20}$. If $\sum_{i=1}^{20}(x_i + 5)^2 = 2500$ and $\sum_{i=1}^{20}(x_i - 5)^2 = 100$, then the ratio of mean to standard deviation of this data is:

**Options:**

- **(A)** $2:1$
- **(B)** $3:1$
- **(C)** $3:2$
- **(D)** $4:1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3:1$**

**Detailed Solution:**

Given $\sum_{i=1}^{20}(x_i + 5)^2 = 2500$ and $\sum_{i=1}^{20}(x_i - 5)^2 = 100$.

Expanding the first equation:
$\sum_{i=1}^{20} (x_i^2 + 10x_i + 25) = 2500$
$\sum_{i=1}^{20} x_i^2 + 10 \sum_{i=1}^{20} x_i + 500 = 2500$
$\sum_{i=1}^{20} x_i^2 + 10 \sum_{i=1}^{20} x_i = 2000$  --- (1)

Expanding the second equation:
$\sum_{i=1}^{20} (x_i^2 - 10x_i + 25) = 100$
$\sum_{i=1}^{20} x_i^2 - 10 \sum_{i=1}^{20} x_i + 500 = 100$
$\sum_{i=1}^{20} x_i^2 - 10 \sum_{i=1}^{20} x_i = -400$  --- (2)

Subtracting (2) from (1):
$20 \sum_{i=1}^{20} x_i = 2400 \Rightarrow \sum_{i=1}^{20} x_i = 120$

Adding (1) and (2):
$2 \sum_{i=1}^{20} x_i^2 = 1600 \Rightarrow \sum_{i=1}^{20} x_i^2 = 800$

Mean ($\mu$) is given by:
$\mu = \dfrac{\sum_{i=1}^{20} x_i}{20} = \dfrac{120}{20} = 6$

Variance ($\sigma^2$) is given by:
$\sigma^2 = \dfrac{\sum_{i=1}^{20} x_i^2}{20} - \mu^2 = \dfrac{800}{20} - 6^2 = 40 - 36 = 4$

Standard deviation ($\sigma$) is $\sqrt{4} = 2$.

The ratio of mean to standard deviation is:
$\dfrac{\mu}{\sigma} = \dfrac{6}{2} = \dfrac{3}{1}$

Answer: $3:1$

</details>

---

### Q2. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A variable $X$ takes values $0, 0, 2, 6, 12, 20, \ldots, n(n-1)$ with frequencies ${}^nC_0, {}^nC_1, {}^nC_2, {}^nC_3, {}^nC_4, {}^nC_5, \ldots, {}^nC_n$, respectively. If the mean of this data is $60$, then its median is :

**Options:**

- **(A)** $56$
- **(B)** $42$
- **(C)** $72$
- **(D)** $90$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $56$**

**Detailed Solution:**

The given variable $X$ takes values $x_r = r(r-1)$ with frequencies $f_r = {}^{n}C_{r}$ for $r = 0, 1, 2, \ldots, n$.

The mean of the data is given by $\bar{X} = \dfrac{\sum_{r=0}^{n} f_r x_r}{\sum_{r=0}^{n} f_r}$.

We know that $\sum_{r=0}^{n} f_r = \sum_{r=0}^{n} {}^{n}C_{r} = 2^n$.

The sum of the products is:

$\sum_{r=0}^{n} f_r x_r = \sum_{r=0}^{n} r(r-1)\, {}^{n}C_{r}$

Using the property $r(r-1)\, {}^{n}C_{r} = n(n-1)\, {}^{n-2}C_{r-2}$, we get:

$\sum_{r=2}^{n} n(n-1)\, {}^{n-2}C_{r-2} = n(n-1)\, 2^{n-2}$

Substituting these into the mean formula:

$\bar{X} = \dfrac{n(n-1)\, 2^{n-2}}{2^n} = \dfrac{n(n-1)}{4}$

Given that the mean is $60$:

$\dfrac{n(n-1)}{4} = 60 \Rightarrow n(n-1) = 240$

Since $16 \times 15 = 240$, we have $n = 16$.

The total frequency is $N = 2^{16}$. Since $N$ is even, the median is the average of the $(2^{15})$-th and $(2^{15} + 1)$-th observations.

The cumulative frequency up to $r = 7$ is:

$\sum_{r=0}^{7} {}^{16}C_{r} = \dfrac{2^{16} - {}^{16}C_{8}}{2} = 2^{15} - \dfrac{1}{2}\, {}^{16}C_{8}$

This value is strictly less than $2^{15}$.

The cumulative frequency up to $r = 8$ is:

$\sum_{r=0}^{8} {}^{16}C_{r} = 2^{15} + \dfrac{1}{2}\, {}^{16}C_{8}$

This value is strictly greater than $2^{15}$.

Thus, both the $(2^{15})$-th and $(2^{15} + 1)$-th observations fall in the class corresponding to $r = 8$.

The value of the variable for $r = 8$ is $x_8 = 8(8-1) = 56$.

Therefore, the median is $56$.

Answer: $56$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean deviation about the mean for the data
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><td style="border: 1px solid black; padding: 5px;">$x_i$</td><td style="border: 1px solid black; padding: 5px;">$5$</td><td style="border: 1px solid black; padding: 5px;">$7$</td><td style="border: 1px solid black; padding: 5px;">$9$</td><td style="border: 1px solid black; padding: 5px;">$10$</td><td style="border: 1px solid black; padding: 5px;">$12$</td><td style="border: 1px solid black; padding: 5px;">$15$</td></tr><tr><td style="border: 1px solid black; padding: 5px;">$f_i$</td><td style="border: 1px solid black; padding: 5px;">$8$</td><td style="border: 1px solid black; padding: 5px;">$6$</td><td style="border: 1px solid black; padding: 5px;">$2$</td><td style="border: 1px solid black; padding: 5px;">$2$</td><td style="border: 1px solid black; padding: 5px;">$2$</td><td style="border: 1px solid black; padding: 5px;">$6$</td></tr></table>is equal to:

**Options:**

- **(A)** $\dfrac{40}{13}$
- **(B)** $\dfrac{42}{13}$
- **(C)** $\dfrac{44}{13}$
- **(D)** $\dfrac{46}{13}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{44}{13}$**

**Detailed Solution:**

Mean $\bar{x} = \dfrac{\sum f_i x_i}{\sum f_i}$

$\sum f_i = 8 + 6 + 2 + 2 + 2 + 6 = 26$

$\sum f_i x_i = 8(5) + 6(7) + 2(9) + 2(10) + 2(12) + 6(15)$

$\sum f_i x_i = 40 + 42 + 18 + 20 + 24 + 90 = 234$

$\bar{x} = \dfrac{234}{26} = 9$

Mean deviation about mean $= \dfrac{\sum f_i |x_i - \bar{x}|}{\sum f_i}$

$\sum f_i |x_i - \bar{x}| = 8|5 - 9| + 6|7 - 9| + 2|9 - 9| + 2|10 - 9| + 2|12 - 9| + 6|15 - 9|$

$\sum f_i |x_i - \bar{x}| = 8(4) + 6(2) + 2(0) + 2(1) + 2(3) + 6(6)$

$\sum f_i |x_i - \bar{x}| = 32 + 12 + 0 + 2 + 6 + 36 = 88$

Mean deviation $= \dfrac{88}{26} = \dfrac{44}{13}$

Answer: $\dfrac{44}{13}$

</details>

---

### Q4. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Suppose that the mean and median of the non-negative numbers $21, 8, 17, a, 51, 103, b, 13, 67, (a > b)$, are $40$ and $21$, respectively. If the mean deviation about the median is $26$, then $2a$ is equal to:

**Options:**

- **(A)** $109$
- **(B)** $117$
- **(C)** $161$
- **(D)** $131$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $131$**

**Detailed Solution:**

The given numbers are $21, 8, 17, a, 51, 103, b, 13, 67$. There are $9$ numbers in total.

Given that the mean is $40$, the sum of the numbers is:
$\sum x_i = 9 \times 40 = 360$

The sum of the known numbers is:
$21 + 8 + 17 + 51 + 103 + 13 + 67 = 280$

Therefore, the sum of $a$ and $b$ is:
$a + b = 360 - 280 = 80$

The median of the $9$ numbers is $21$. Arranging the known numbers in ascending order, we get:
$8, 13, 17, 21, 51, 67, 103$

There are $3$ numbers less than $21$ and $3$ numbers greater than $21$. For $21$ to be the median (the $5^{\text{th}}$ observation), one of the unknown numbers must be $\le 21$ and the other must be $\ge 21$. Since $a > b$, we must have:
$a \ge 21$ and $b \le 21$

The mean deviation about the median is $26$, so the sum of absolute deviations from the median is:
$\sum |x_i - 21| = 9 \times 26 = 234$

The sum of absolute deviations of the known numbers from $21$ is:
$|8 - 21| + |13 - 21| + |17 - 21| + |21 - 21| + |51 - 21| + |67 - 21| + |103 - 21|$
$= 13 + 8 + 4 + 0 + 30 + 46 + 82 = 183$

The sum of absolute deviations of $a$ and $b$ from $21$ is:
$|a - 21| + |b - 21| = 234 - 183 = 51$

Since $a \ge 21$ and $b \le 21$, we can remove the absolute values:
$(a - 21) + (21 - b) = 51$
$a - b = 51$

We now have a system of two equations:
$a + b = 80$
$a - b = 51$

Adding the two equations, we get:
$2a = 131$

Answer: $131$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of $n$ observations are $8$ and $16$, respectively. If the sum of the first $(n-1)$ observations is $48$ and the sum of squares of the first $(n-1)$ observations is $496$, then the value of $n$ is:

**Options:**

- **(A)** $21$
- **(B)** $16$
- **(C)** $13$
- **(D)** $7$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $7$**

**Detailed Solution:**

Let the $n$-th observation be $x_n$.

Given mean $\bar{x} = 8$, we have:

$\dfrac{\sum_{i=1}^{n-1} x_i + x_n}{n} = 8$

$\dfrac{48 + x_n}{n} = 8 \Rightarrow x_n = 8n - 48$

Given variance $\sigma^2 = 16$, we have:

$\dfrac{\sum_{i=1}^{n-1} x_i^2 + x_n^2}{n} - (\bar{x})^2 = 16$

$\dfrac{496 + x_n^2}{n} - 64 = 16$

$\dfrac{496 + x_n^2}{n} = 80$

$496 + x_n^2 = 80n$

Substituting $x_n = 8n - 48$:

$496 + (8n - 48)^2 = 80n$

$496 + 64n^2 - 768n + 2304 = 80n$

$64n^2 - 848n + 2800 = 0$

Dividing by $16$:

$4n^2 - 53n + 175 = 0$

$4n^2 - 28n - 25n + 175 = 0$

$4n(n - 7) - 25(n - 7) = 0$

$(4n - 25)(n - 7) = 0$

Since $n$ must be an integer, $n = 7$.

Answer: $7$

</details>

---

### Q6. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the mean of the data
<table style="border: 1px solid black; border-collapse: collapse; width: auto;"><tr><th style="border: 1px solid black; padding: 5px;">Class</th><th style="border: 1px solid black; padding: 5px;">$5-10$</th><th style="border: 1px solid black; padding: 5px;">$10-15$</th><th style="border: 1px solid black; padding: 5px;">$15-20$</th><th style="border: 1px solid black; padding: 5px;">$20-25$</th><th style="border: 1px solid black; padding: 5px;">$25-30$</th><th style="border: 1px solid black; padding: 5px;">$30-35$</th></tr><tr><td style="border: 1px solid black; padding: 5px;">Frequency</td><td style="border: 1px solid black; padding: 5px;">$2$</td><td style="border: 1px solid black; padding: 5px;">$k$</td><td style="border: 1px solid black; padding: 5px;">$28$</td><td style="border: 1px solid black; padding: 5px;">$54$</td><td style="border: 1px solid black; padding: 5px;">$k+1$</td><td style="border: 1px solid black; padding: 5px;">$5$</td></tr></table>
is $21$, then $k$ is one of the roots of the equation :

**Options:**

- **(A)** $2x^2 - 23x - 10 = 0$
- **(B)** $4x^2 - 35x + 24 = 0$
- **(C)** $2x^2 - 19x - 10 = 0$
- **(D)** $2x^2 - 35x + 98 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2x^2 - 19x - 10 = 0$**

**Detailed Solution:**

The class marks (mid-points) $x_i$ for the given classes are $7.5, 12.5, 17.5, 22.5, 27.5, 32.5$.

The sum of the frequencies is:
$\sum f_i = 2 + k + 28 + 54 + (k + 1) + 5 = 2k + 90$

The sum of the products $f_i x_i$ is:
$\sum f_i x_i = 2(7.5) + k(12.5) + 28(17.5) + 54(22.5) + (k + 1)(27.5) + 5(32.5)$

$\sum f_i x_i = 15 + 12.5k + 490 + 1215 + 27.5k + 27.5 + 162.5$

$\sum f_i x_i = 40k + 1910$

The mean is given as $21$. Using the formula for the mean $\bar{x} = \dfrac{\sum f_i x_i}{\sum f_i}$:

$\dfrac{40k + 1910}{2k + 90} = 21$

$40k + 1910 = 21(2k + 90)$

$40k + 1910 = 42k + 1890$

$2k = 20 \Rightarrow k = 10$

Now, substituting $x = 10$ into the given options to check which equation has $10$ as a root:

For $2x^2 - 19x - 10 = 0$:
$2(10)^2 - 19(10) - 10 = 200 - 190 - 10 = 0$

Thus, $k = 10$ is a root of $2x^2 - 19x - 10 = 0$.

Answer: $2x^2 - 19x - 10 = 0$

</details>

---

### Q7. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\mathrm{X}=\{x \in \mathrm{~N}: 1 \leq x \leq 19\}$ and for some $a, b \in \mathbb{R}, \mathrm{Y}=\{a x+b: x \in \mathrm{X}\}$. If the mean and variance of the elements of Y are 30 and 750, respectively, then the sum of all possible values of $b$ is

**Options:**

- **(A)** 60
- **(B)** 100
- **(C)** 80
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 60**

**Detailed Solution:**

Mean of $X = \frac{1+19}{2} = 10$, Variance of $X = \frac{19^2-1}{12} = 30$.
For $Y = aX + b$: Mean of $Y = 10a + b = 30$ and Variance of $Y = a^2 \cdot 30 = 750$.
$a^2 = 25 \Rightarrow a = 5$ or $a = -5$.
If $a = 5$: $b = 30 - 50 = -20$.
If $a = -5$: $b = 30 + 50 = 80$.
Sum of all possible values of $b = -20 + 80 = 60$.

</details>

---

### Q8. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let the mean and variance of 7 observations $2,4,10, x, 12,14, y, x>y$, be 8 and 16 respectively. Two numbers are chosen from $\{1,2,3, x-4, y, 5\}$ one after another without replacement, then the probability, that the smaller number among the two chosen numbers is less than 4, is :

**Options:**

- **(A)** $\frac{3}{5}$
- **(B)** $\frac{1}{3}$
- **(C)** $\frac{2}{5}$
- **(D)** $\frac{4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{4}{5}$**

**Detailed Solution:**

Mean = 8 gives $x + y = 14$.
Variance = 16 gives $(x-8)^2 + (y-8)^2 = 4$.
Solving: $x = 8$, $y = 6$ (since $x > y$).
Set becomes $\{1, 2, 3, 4, 6, 5\} = \{1, 2, 3, 4, 5, 6\}$.
Total ways to choose 2 numbers = $\binom{6}{2} = 15$.
Favorable cases (smaller $< 4$): smaller = 1 gives 5 pairs, smaller = 2 gives 4 pairs, smaller = 3 gives 3 pairs.
Total favorable = 12.
Probability $= \frac{12}{15} = \frac{4}{5}$.

</details>

---

### Q9. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `2`

The mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> numbers
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#215;</mo><mn>8</mn><mo>,</mo><mn>10</mn><mo>&#215;</mo><mn>10</mn><mo>,</mo><mn>13</mn><mo>&#215;</mo><mn>12</mn><mo>,</mo><mn>16</mn><mo>&#215;</mo><mn>14</mn><mo>,</mo><mo>&#8230;</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **398**

**Detailed Solution:**

<p>Given that </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>13</mn><mo>-</mo><mo>-</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>,</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mi>A</mi><mo>.</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi><mo>&#160;</mo></mrow></msup></math>term of an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>&#160;</mo><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>t</mi><mi>r</mi></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mo>+</mo><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>&#160;</mo><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>r</mi></msub><mo>&#160;</mo><mo>=</mo><mn>3</mn><mi>r</mi><mo>&#160;</mo><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#160;</mo><msub><mi>t</mi><mi>r</mi></msub><mo>&#160;</mo><mo>=</mo><mn>2</mn><mi>r</mi><mo>&#160;</mo><mo>+</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mo>(</mo><mn>3</mn><mi>r</mi><mo>+</mo><mn>4</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>6</mn><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>6</mn><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>26</mn><mi>r</mi><mo>+</mo><mn>24</mn></mrow></mfenced><mo>=</mo><mn>6</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>26</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mn>1</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mi>r</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>,</mo><mo>&#160;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mi>r</mi><mn>3</mn></msup><mo>&#160;</mo><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mo>&#160;</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#160;</mo><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced><mo>+</mo><mn>26</mn><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>24</mn><mfenced><mn>10</mn></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2310</mn><mo>+</mo><mn>1430</mn><mo>+</mo><mn>240</mn><mo>=</mo><mn>3980</mn></math>
mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>398</mn></math></p>

</details>

---

### Q10. JEE Main 2021 (18 Mar Shift 1)

*Type:* `numerical` | *Level:* `1`

The mean age of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> teachers in a school is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> years. A teacher retires at the age of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math> years and a new teacher is appointed in his place. If the mean age of the teachers in this school now is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math> years, then the age (in years) of the newly appointed teacher is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **35**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>25</mn></mfrac><mo>=</mo><mn>40</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>60</mn><mo>+</mo><mi>N</mi></mrow><mn>25</mn></mfrac><mo>=</mo><mn>39</mn></math></p><p>Let age of newly appointed teacher is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1000</mn><mo>-</mo><mn>60</mn><mo>+</mo><mi>N</mi><mo>=</mo><mn>975</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>N</mi><mo>=</mo><mn>35</mn></math> year</p>

</details>

---

### Q11. JEE Main 2020 (06 Sep Shift 2)

*Type:* `numerical` | *Level:* `3`

Consider the data on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi></math> taking the values <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msup><mn>2</mn><mi mathvariant="normal">n</mi></msup></math> with frequencies <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>,</mo><mo>&#160;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>,</mo><mo>&#160;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">n</mi><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts></math> respectively. If the mean of this data is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>728</mn><msup><mn>2</mn><mi mathvariant="normal">n</mi></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi></math> is equal to ....... .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

<table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math> (observation)</td>			<td>0</td>			<td>2</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>2</mn></msup></math>................</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi mathvariant="normal">n</mi></msup></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math> (frequency)</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts></math>.............</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts></math></td>		</tr>	</tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msub><mi>f</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub></mrow><mrow><mi>&#931;</mi><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>0</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mrow><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mi>n</mi></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>2</mn><mi>n</mi></msup></mfrac><mo>=</mo><mfrac><mn>728</mn><msup><mn>2</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mn>3</mn><mi>n</mi></msup><mo>=</mo><msup><mn>3</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q12. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If for some <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>, the frequency distribution of the marks obtained by <math><mn>20</mn></math> students in a test is:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>Marks</td>			<td>2</td>			<td>3</td>			<td>5</td>			<td>7</td>		</tr>		<tr>			<td>Frequency distribution</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>		</tr>	</tbody></table><p>Then the mean of the marks is :</p>

**Options:**

- **(A)** <math><mn>3.0</mn></math>
- **(B)** <math><mn>2.5</mn></math>
- **(C)** <math><mn>3.2</mn></math>
- **(D)** <math><mn>2.8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2.8</mn></math>**

**Detailed Solution:**

<p>Total students <math><mo>=</mo><mn>20</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mi>x</mi><mo>=</mo><mn>20</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>x</mi><mo>+</mo><mi>x</mi><mo>=</mo><mn>20</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>x</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>x</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mo>-</mo><mn>4</mn><mo>,</mo><mi>&#160;</mi><mn>3</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfenced separators="|"><mrow><mo>&#8757;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>x</mi><mo>=</mo><mn>3</mn></math></p><p>Average <math><mo>=</mo><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>&#215;</mo><mn>2</mn><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mn>3</mn><mo>+</mo><mn>5</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mo>+</mo><mn>7</mn><mo>&#215;</mo><mi>x</mi></mrow><mrow><mn>20</mn></mrow></mfrac></math></p><p><math><mo>=</mo><mfrac><mrow><mn>32</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>21</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mn>2.8</mn></math></p><p>Hence, required mean is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>8</mn></math></p>

</details>

---

### Q13. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the deviations of <math><mn>50</mn></math> observations from <math><mn>30</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>, then the mean of these observations is :

**Options:**

- **(A)** <math><mn>30</mn></math>
- **(B)** <math><mn>51</mn></math>
- **(C)** <math><mn>50</mn></math>
- **(D)** <math><mn>31</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>31</mn></math>**

**Detailed Solution:**

Let the observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mi>&#160;</mi><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>50</mn></msub></math>.

Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>30</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>30</mn></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced separators="|"><mrow><msub><mi>x</mi><mn>50</mn></msub><mo>-</mo><mn>30</mn></mrow></mfenced><mo>=</mo><mn>50</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>x</mi><mn>50</mn></msub><mo>=</mo><mn>50</mn><mo>+</mo><mfenced><mrow><mn>30</mn><mo>&#215;</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mn>1550</mn></math>

Now, Mean <math><mo>=</mo><mfrac><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>50</mn></mrow></msub></mrow><mrow><mn>50</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1550</mn></mrow><mrow><mn>50</mn></mrow></mfrac><mo>=</mo><mn>31</mn></math>.

</details>

---

### Q14. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `1`

If the mean of the data: $7,8,9,7,8,7, \lambda, 8$ is 8 , then the variance of this data is

**Options:**

- **(A)** $\frac{9}{8}$
- **(B)** 2
- **(C)** $\frac{7}{8}$
- **(D)** 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 1**

**Detailed Solution:**

$$
\text { } \begin{aligned}
&\bar{x}=\frac{7+8+9+7+8+7+\lambda+8}{8}=8 \\
&\Rightarrow \frac{54+\lambda}{8}=8 \Rightarrow \lambda=10
\end{aligned}
$$
Now variance $=\sigma^2$
$$
\begin{aligned}
&(7-8)^2+(8-8)^2+(9-8)^2+(7-8)^2+(8-8)^2 \\
&=\frac{+(7-8)^2+(10-8)^2+(8-8)^2}{8} \\
&\Rightarrow \sigma^2=\frac{1+0+1+1+0+1+4+0}{8}=\frac{8}{8}=1 \\
&
\end{aligned}
$$
Hence, the variance is 1 .

</details>

---

### Q15. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The mean of a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> observation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>. If each observations is multiplied by non-zero number <math><mi>&#955;</mi></math> and then each of them is decreased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>, their mean remains the same. Then, <math><mi>&#955;</mi></math> is equal to :

**Options:**

- **(A)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><mi>&#160;</mi><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>30</mn></msub></math>.</p><p>Given mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>&#160;</mi><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>30</mn></msub><mo>=</mo><mn>75</mn><mo>&#215;</mo><mn>30</mn></math></p><p>Now according to question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#955;</mi><mo>(</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>&#160;</mi><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>30</mn></msub><mo>)</mo><mo>-</mo><mn>25</mn><mo>&#215;</mo><mn>30</mn></mrow><mn>30</mn></mfrac><mo>=</mo><mfrac><mrow><mn>75</mn><mo>&#215;</mo><mn>30</mn></mrow><mn>30</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced separators="|"><mrow><mn>75</mn><mo>&#215;</mo><mn>30</mn></mrow></mfenced><mo>=</mo><mn>100</mn><mo>&#215;</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q16. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

The mean of a set of 30 observations is 75 . If each other observation is multiplied by a nonzero number $\lambda$ and then each of them is decreased by 25 , their mean remains the same. The $\lambda$ is equal to
equal to $\{0\}$

**Options:**

- **(A)** $\frac{10}{3}$
- **(B)** $\frac{4}{3}$
- **(C)** $\frac{1}{3}$
- **(D)** $\frac{2}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{4}{3}$**

**Detailed Solution:**

As mean is a linear operation, so if each observation is multiplied by $\lambda$ and decreased by 25 then the mean becomes 75 $\lambda-25$.
According to the question,
$$
75 \lambda-25=75 \Rightarrow \lambda=\frac{4}{3}
$$

</details>

---

### Q17. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The mean age of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> teachers in a school is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> years. A teacher retires at the age of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math> years and a new teacher is appointed in his place. If the mean age of the teachers in this school now is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>39</mn></math> years, then the age (in years) of the newly appointed teacher is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>**

**Detailed Solution:**

Mean age can be calculated as

<math><mover accent="true"><mrow><mi>x</mi></mrow><mo>-</mo></mover><mo>=</mo><mfrac><mrow><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>&#8230;</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>25</mn></mrow></msub></mrow><mrow><mn>25</mn></mrow></mfrac><mo>=</mo><mn>40</mn></math>

<math> <mo>&#8658;</mo> </math> <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>25</mn></mrow></msub><mo>=</mo><mn>1000</mn></math>

Let age of new teacher be A, then

<math><mn>1000</mn><mo>-</mo><mn>60</mn><mo>+</mo><mi>A</mi><mo>=</mo><mn>39</mn><mo>&#215;</mo><mn>25</mn><mo>=</mo><mn>975</mn></math>

<math> <mo>&#8658;</mo> </math> <math><mi>A</mi><mo>=</mo><mn>975</mn><mo>-</mo><mn>940</mn><mo>=</mo><mn>35</mn></math>

</details>

---

### Q18. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo><mn>4</mn></math>. If three of the observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>6</mn></math>; then the value of the remaining two is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>11</mn></math>
- **(D)** None of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>11</mn></math>**

**Detailed Solution:**

<p><math><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>6</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>16</mn></math></p><p>Now <math><mn>12.4</mn><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>16</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>1</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mn>62&#160;</mn></math><math><mo>=</mo><mn>26</mn><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math></p><p><math><mo>&#8658;</mo><mn>36</mn><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>y</mi><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math></p><p>Shifting of the origin to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>5</mn><mo>,</mo><mn>5</mn></mrow></mfenced></math> the equations will become </p><p><math><msup><mrow><mn>6</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>6</mn></math></p><p>Solving them and again will get the <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn></math>.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mn>6</mn></math> or</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>6</mn></math>.</p><p>But by shifting the origin back to original position, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>6</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>11</mn></math></p><p>(or)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>6</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>11</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>0</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>5</mn></math></p><p>Hence, the values of the remaining two are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>11</mn></math>.</p>

</details>

---

### Q19. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

A factory is operating in two shifts, day and night, with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>70</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> workers, respectively.If per day mean wage of the day shift workers is, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8377;</mo><mn>54</mn></math> and per day mean wage of all the workers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8377;</mo><mn>60</mn></math>, then per day mean wage of the night shift workers (in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8377;</mo></math>) is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>74</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>69</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>74</mn></math>**

**Detailed Solution:**

<math><mfrac><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mi>&#160;</mi><msub><mrow><mover accent="false"><mrow><mi>x</mi></mrow><mo>&#175;</mo></mover></mrow><mrow><mn>1</mn><mi>&#160;</mi><mi>&#160;</mi></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub><mi>&#160;</mi><msub><mrow><mover accent="false"><mrow><mi>x</mi></mrow><mo>&#175;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub></mrow><mrow><msub><mrow><mi>n</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfrac><mi>&#160;</mi><mo>=</mo><mi>&#160;</mi><mover accent="false"><mrow><mi>x</mi></mrow><mo>&#175;</mo></mover></math>

<math><mfrac><mrow><mn>70</mn><mo>&#8901;</mo><mfenced separators="|"><mrow><mn>54</mn></mrow></mfenced><mo>+</mo><mn>30</mn><mi>&#160;</mi><mfenced separators="|"><mrow><msub><mrow><mover accent="false"><mrow><mi>x</mi></mrow><mo>&#175;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub></mrow></mfenced></mrow><mrow><mn>70</mn><mo>+</mo><mn>30</mn></mrow></mfrac><mo>=</mo><mn>60</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3780</mn><mo>+</mo><mn>30</mn><mi>&#160;</mi><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mrow><mn>2</mn><mi>&#160;</mi></mrow></msub><mo>=</mo><mn>6000</mn></math>

<math><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><msub><mrow><mover accent="false"><mrow><mi>x</mi></mrow><mo>&#175;</mo></mover></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>6000</mn><mo>-</mo><mn>3780</mn></mrow><mrow><mn>30</mn></mrow></mfrac></math>

<math><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>2220</mn></mrow><mrow><mn>30</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>74</mn></math>

</details>

---

### Q20. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `1`

<p>The mean of a data set comprising of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>16</mi></math> observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>16</mi></math>. If one of the observation value <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>16</mi></math> is deleted and three new observations valued <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>, 4</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">5</mi></math> are added to the data, then the mean of the resultant data is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.0</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>.8</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>.0</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.8</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.0</mo></math>**

**Detailed Solution:**

Given, <math> <mrow> <mfrac> <mrow> <mrow><mo>(</mo> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>i</mi><mo>=</mo><mn>1</mn>&#160;</mrow><mrow><mn>15</mn> </mrow> </munderover> <mrow> <msub> <mi>x</mi> <mi>i</mi> </msub> </mrow> </mstyle> </mrow> <mo>)</mo></mrow><mo>+</mo><mn>16</mn> </mrow> <mrow> <mn>16</mn> </mrow> </mfrac> <mo>=</mo><mn>16</mn> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>x</mi><mi>i</mi></msub></math> <math> <mo>+16</mo><mo>=</mo> <mtext>256</mtext> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>240</mn></math>

Required mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mtext>&#8201;</mtext><mo>=</mo><mtext>&#8201;</mtext><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn></mstyle><mn>18</mn></mfrac><mo>=</mo><mfrac><mrow><mn>240</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn></mrow><mn>18</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>252</mi><mi>18</mi></mfrac><mo>=</mo><mi>14</mi></math>

</details>

---

### Q21. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

In a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> distinct observations, each of the observation below the median of all the observations is increased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and each of the remaining observations is decreased by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>. Then, the mean of the new set of observations :

**Options:**

- **(A)** Increases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> .
- **(B)** Increases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> .
- **(C)** Decreases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> .
- **(D)** Decreases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Increases by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> .**

**Detailed Solution:**

New mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mrow><mtext>n</mtext><mi>&#931;</mi><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mtext>5n</mtext></mrow></mfenced><mo>+</mo><mfenced><mrow><mtext>n</mtext><mi>&#931;</mi><msub><mi>y</mi><mi>i</mi></msub><mo>-</mo><mtext>3n</mtext></mrow></mfenced></mrow><mtext>2n</mtext></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced close="}" open="{"><mfrac><mrow><mtext>n</mtext><mi>&#931;</mi><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mtext>n</mtext><mi>&#931;</mi><msub><mi>y</mi><mi>i</mi></msub></mrow><mtext>2n</mtext></mfrac></mfenced><mo>+</mo><mfrac><mtext>2n</mtext><mtext>2n</mtext></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>old mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mfrac><mtext>2n</mtext><mtext>2n</mtext></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math>old mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>1</mn></math>

</details>

---

### Q22. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The mean of a data set consisting of 20 observations is 40 . If one observation 53 was wrongly recorded as 33 , then the correct mean will be:

**Options:**

- **(A)** 41
- **(B)** 49
- **(C)** $40.5$
- **(D)** $42.5$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 41**

**Detailed Solution:**

$$
\text { Correct mean }=\frac{20 \times 40-33+55}{20}=41.1
$$
Nearest option : (a) 41

</details>

---

### Q23. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

The average marks of boys in a class is $52$ and that of girls is $42$. The average marks of boys and girls combined is $50$. The percentage of boys in the class is

**Options:**

- **(A)** $40$
- **(B)** $20$
- **(C)** $80$
- **(D)** $60$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $80$**

**Detailed Solution:**

$52 x+42 y=50(x+y)$
$2 x=8 y$
$\Rightarrow \frac{x}{y}=\frac{4}{1}$ and $\frac{x}{x+y}=\frac{4}{5}$
$\therefore \%$ of boys $=80$.

</details>

---

### Q24. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{x}_1, \mathrm{x}_2, \ldots, \mathrm{x}_{\mathrm{n}}$ be $\mathrm{n}$ observations such that $\sum \mathrm{x}_{\mathrm{i}}^2=400$ and $\sum \mathrm{x}_{\mathrm{i}}=80$. Then a possible value of $\mathrm{n}$ among the following is

**Options:**

- **(A)** 15
- **(B)** 18
- **(C)** 9
- **(D)** 12

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 18**

**Detailed Solution:**

$$
\begin{aligned}
& \frac{\sum x_i^2}{n} \geq\left(\frac{\sum x_i}{n}\right)^2 \\
& \Rightarrow n \geq 16
\end{aligned}
$$

</details>

---

### Q25. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `1`

In a class of 100 students there are 70 boys whose average marks in a subject are 75. If the average marks of the complete class is 72, then what is the average of the girls?

**Options:**

- **(A)** 73
- **(B)** 65
- **(C)** 68
- **(D)** 74

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 65**

**Detailed Solution:**

Total student $=100 ;$ for 70 stds $75 \times 70=5250 \Rightarrow 7200-5250=1950$
$$
\text { Average of girls }=\frac{1950}{30}=65
$$

</details>

---

