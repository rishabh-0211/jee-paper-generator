# JEE Main Mathematics - Statistics

## Topic 6: Measures of Dispersion

**Total Questions:** 108

---

### Q1. JEE Main 2026 (08 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A set of four observations has mean $1$ and variance $13$. Another set of six observations has mean $2$ and variance $1$. Then, the variance of all these $10$ observations is equal to:

**Options:**

- **(A)** $5.96$
- **(B)** $6.14$
- **(C)** $6.04$
- **(D)** $6.24$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $6.04$**

**Detailed Solution:**

Given for the first set: $n_1 = 4$, $\bar{x}_1 = 1$, $\sigma_1^2 = 13$.

$\sigma_1^2 = \dfrac{\sum x_i^2}{n_1} - (\bar{x}_1)^2$

$13 = \dfrac{\sum x_i^2}{4} - 1^2 \Rightarrow \sum x_i^2 = 56$

Also, $\sum x_i = n_1 \bar{x}_1 = 4 \times 1 = 4$

Given for the second set: $n_2 = 6$, $\bar{x}_2 = 2$, $\sigma_2^2 = 1$.

$\sigma_2^2 = \dfrac{\sum y_i^2}{n_2} - (\bar{x}_2)^2$

$1 = \dfrac{\sum y_i^2}{6} - 2^2 \Rightarrow \sum y_i^2 = 30$

Also, $\sum y_i = n_2 \bar{x}_2 = 6 \times 2 = 12$

For the combined set of $10$ observations:

Total sum $\sum z_i = \sum x_i + \sum y_i = 4 + 12 = 16$

Combined mean $\bar{z} = \dfrac{16}{10} = 1.6$

Total sum of squares $\sum z_i^2 = \sum x_i^2 + \sum y_i^2 = 56 + 30 = 86$

Combined variance $\sigma^2 = \dfrac{\sum z_i^2}{10} - (\bar{z})^2$

$\sigma^2 = \dfrac{86}{10} - (1.6)^2 = 8.6 - 2.56 = 6.04$

Answer: $6.04$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the mean and the variance of seven observations $2, 4, \alpha, 8, \beta, 12, 14$, $\alpha < \beta$, be $8$ and $16$ respectively. Then the quadratic equation whose roots are $3\alpha + 2$ and $2\beta + 1$ is :

**Options:**

- **(A)** $x^2 - 35x + 306 = 0$
- **(B)** $x^2 - 41x + 420 = 0$
- **(C)** $x^2 - 45x + 506 = 0$
- **(D)** $x^2 - 37x + 342 = 0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $x^2 - 41x + 420 = 0$**

**Detailed Solution:**

Given the mean of the seven observations is $8$:

$\dfrac{2 + 4 + \alpha + 8 + \beta + 12 + 14}{7} = 8$

$\dfrac{40 + \alpha + \beta}{7} = 8$

$\alpha + \beta = 16$

Given the variance of the observations is $16$:

$\dfrac{\sum x_i^2}{n} - (\text{Mean})^2 = 16$

$\dfrac{2^2 + 4^2 + \alpha^2 + 8^2 + \beta^2 + 12^2 + 14^2}{7} - 8^2 = 16$

$\dfrac{4 + 16 + \alpha^2 + 64 + \beta^2 + 144 + 196}{7} - 64 = 16$

$\dfrac{424 + \alpha^2 + \beta^2}{7} = 80$

$424 + \alpha^2 + \beta^2 = 560$

$\alpha^2 + \beta^2 = 136$

Using the identity $(\alpha + \beta)^2 = \alpha^2 + \beta^2 + 2\alpha\beta$:

$16^2 = 136 + 2\alpha\beta$

$256 = 136 + 2\alpha\beta$

$2\alpha\beta = 120 \Rightarrow \alpha\beta = 60$

Solving for $\alpha$ and $\beta$, they are the roots of the equation $t^2 - 16t + 60 = 0$, which are $6$ and $10$.

Since $\alpha < \beta$, we have $\alpha = 6$ and $\beta = 10$.

The roots of the required quadratic equation are $3\alpha + 2$ and $2\beta + 1$:

$3\alpha + 2 = 3(6) + 2 = 20$

$2\beta + 1 = 2(10) + 1 = 21$

Sum of the roots $= 20 + 21 = 41$

Product of the roots $= 20 \times 21 = 420$

The required quadratic equation is $x^2 - (\text{Sum})x + (\text{Product}) = 0$:

$x^2 - 41x + 420 = 0$

Answer: $x^2 - 41x + 420 = 0$

</details>

---

### Q3. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For $10$ observations $x_1, x_2, \ldots, x_{10}$, if $\sum_{i=1}^{10}(x_i+2)^2=180$ and $\sum_{i=1}^{10}(x_i-1)^2=90$, then their standard deviation is:

**Options:**

- **(A)** $2$
- **(B)** $\sqrt{3}$
- **(C)** $2\sqrt{2}$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3$**

**Detailed Solution:**

Given $\sum_{i=1}^{10}(x_i+2)^2=180$

$\Rightarrow \sum_{i=1}^{10} x_i^2 + 4\sum_{i=1}^{10} x_i + 40 = 180$

$\Rightarrow \sum_{i=1}^{10} x_i^2 + 4\sum_{i=1}^{10} x_i = 140$

Also given $\sum_{i=1}^{10}(x_i-1)^2=90$

$\Rightarrow \sum_{i=1}^{10} x_i^2 - 2\sum_{i=1}^{10} x_i + 10 = 90$

$\Rightarrow \sum_{i=1}^{10} x_i^2 - 2\sum_{i=1}^{10} x_i = 80$

Subtracting the second equation from the first:

$6\sum_{i=1}^{10} x_i = 60 \Rightarrow \sum_{i=1}^{10} x_i = 10$

Substituting this value in the second equation:

$\sum_{i=1}^{10} x_i^2 - 2(10) = 80 \Rightarrow \sum_{i=1}^{10} x_i^2 = 100$

The standard deviation is given by:

$\sigma = \sqrt{\dfrac{\sum x_i^2}{n} - \left(\dfrac{\sum x_i}{n}\right)^2}$

$\sigma = \sqrt{\dfrac{100}{10} - \left(\dfrac{10}{10}\right)^2}$

$\sigma = \sqrt{10 - 1} = \sqrt{9} = 3$

Answer: $3$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The mean and variance of 10 observations are 9 and 34.2, respectively. If 8 of these observations are $2,3,5,10,11,13,15,21$, then the mean deviation about the median of all the 10 observations is

**Options:**

- **(A)** 4
- **(B)** 7
- **(C)** 5
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 5**

**Detailed Solution:**

Given 10 observations with mean = 9 and variance = 34.2.
Eight known values: 2, 3, 5, 10, 11, 13, 15, 21. 
 Sum of all 10: $\sum x_i = 90$.
Sum of 8 known: 80. So the two unknowns sum to 10. 
 From variance: $\sum x_i^2 = 10(34.2 + 81) = 1152$.
Sum of squares of 8 known: 1094. So unknown squares sum to 58. 
 With $x_9 + x_{10} = 10$ and $x_9^2 + x_{10}^2 = 58$: we get $x_9 x_{10} = 21$, giving roots $t^2 - 10t + 21 = 0$, so the unknowns are 3 and 7. 
 All 10 sorted: 2, 3, 3, 5, 7, 7, 10, 11, 13, 15, 21.
Median = $\frac{7+10}{2} = 8.5$. 
 Mean deviation = $\frac{1}{10}(6.5 + 5.5 + 5.5 + 3.5 + 1.5$ $+ 1.5 + 2.5 + 4.5 + 6.5 + 12.5)$ $= \frac{50}{10} = 5$

</details>

---

### Q5. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of a data of 10 observations are 10 and 2, respectively. If an observations $\alpha$ in this data is replaced by $\beta$, then the mean and variance become 10.1 and 1.99, respectively. Then $\alpha+\beta$ equals

**Options:**

- **(A)** 15
- **(B)** 5
- **(C)** 10
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 20**

**Detailed Solution:**

$n=10$, mean $=10$, variance $=2$.
So $\sum x_i = 100$ and $\sum x_i^2 = 10(2+100)=1020$.
After replacing $\alpha$ by $\beta$:
new mean $=10.1 \Rightarrow \sum x_i - \alpha + \beta = 101 \Rightarrow \beta - \alpha = 1$
New variance $=1.99 \Rightarrow \frac{\sum x_i^2 - \alpha^2 + \beta^2}{10} - (10.1)^2 = 1.99$
$\sum x_i^2 - \alpha^2 + \beta^2 = 10(1.99+102.01) = 1040$
$\beta^2 - \alpha^2 = 1040 - 1020 = 20$
$(\beta-\alpha)(\beta+\alpha) = 20 \Rightarrow 1 \cdot (\alpha+\beta) = 20$
$\alpha + \beta = 20$

</details>

---

### Q6. JEE Main 2026 (23 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the mean and the variance of the data 
 \(\begin{array}{|c|c|c|c|c|} \hline \text{Class} & 4\text{-}8 & 8\text{-}12 & 12\text{-}16 & 16\text{-}20 \\ \hline \text{Frequency} & 3 & \lambda & 4 & 7 \\ \hline \end{array}\) 
 are $\mu$ and 19 respectively, then the value of $\lambda+\mu$ is

**Options:**

- **(A)** 21
- **(B)** 19
- **(C)** 20
- **(D)** 18

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 19**

**Detailed Solution:**

Class midpoints: $6, 10, 14, 18$.
Frequencies: $3, \lambda, 4, 7$. $N = 14 + \lambda$.
Mean $\mu = \frac{200 + 10\lambda}{14 + \lambda}$.
$\sum f_i x_i^2 = 3(36) + 100\lambda + 4(196) + 7(324) = 3160 + 100\lambda$.
Variance: $19 = \frac{3160+100\lambda}{N} - \mu^2$.
Let $u = 14+\lambda$:
$19u^2 = u(1760+100u) - (60+10u)^2 \Rightarrow 19u^2 - 560u + 3600 = 0$.
$u = \frac{560 \pm 200}{38}$, so $u = 20 \Rightarrow \lambda = 6$.
$\mu = \frac{260}{20} = 13$. Hence $\lambda + \mu = 6 + 13 = 19$.

</details>

---

### Q7. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the mean and variance of 8 numbers $-10,-7,-1, x, y, 9,2,16$ be $\frac{7}{2}$ and $\frac{293}{4}$, respectively. Then the mean of 4 numbers $x, y, x+y+1,|x-y|$ is :

**Options:**

- **(A)** 11
- **(B)** 12
- **(C)** 10
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 11**

**Detailed Solution:**

Mean $= \frac{7}{2}$: $-10-7-1+x+y+9+2+16 = 28 \Rightarrow x+y = 19$.
Variance $= \frac{293}{4}$: $\frac{\sum x_i^2}{8} - \frac{49}{4} = \frac{293}{4} \Rightarrow \sum x_i^2 = 684$.
Known squares: $100+49+1+81+4+256 = 491$, so $x^2+y^2 = 193$.
$(x-y)^2 = x^2+y^2-2xy = 193 - (361-193) = 25 \Rightarrow |x-y| = 5$.
$x+y+1 = 20$.
Mean of $x, y, x+y+1, |x-y| = \frac{19 + 20 + 5}{4} = \frac{44}{4} = 11$.

</details>

---

### Q8. JEE Main 2026 (22 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean deviation about the median of the numbers $\mathrm{k}, 2 \mathrm{k}, 3 \mathrm{k}, \ldots. ., 1000 \mathrm{k}$ is 500, then $\mathrm{k}^{2}$ is equal to :

**Options:**

- **(A)** 9
- **(B)** 1
- **(C)** 4
- **(D)** 16

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4**

**Detailed Solution:**

The sequence $k, 2k, 3k, \ldots, 1000k$ has 1000 terms.
The median is $\frac{500k + 501k}{2} = \frac{1001k}{2}$.
The mean deviation is $MD = \frac{1}{1000}\sum_{i=1}^{1000}|ik - \text{median}|$.
For $i \leq 500$: deviation = $\frac{1001k}{2} - ik$, giving $\sum_{i=1}^{500}(\frac{1001}{2} - i) = 125000$.
By symmetry, the sum for $i \geq 501$ is also $125000$.
Thus $MD = \frac{k}{1000} \cdot 250000 = 250k = 500$, so $k = 2$ and $k^2 = 4$.

</details>

---

### Q9. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and standard deviation of 100 observations are 40 and 5.1 , respectively, By mistake one observation is taken as 50 instead of 40. If the correct mean and the correct standard deviation are $\mu$ and $\sigma$ respectively, then $10(\mu+\sigma)$ is equal to

**Options:**

- **(A)** 445
- **(B)** 451
- **(C)** 447
- **(D)** 449

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 449**

**Detailed Solution:**

$\begin{aligned}
& \text { Actual means }=\mu=\frac{100(40)-50+40}{100} \\
& \mu=40-\frac{1}{10}=39.9
\end{aligned}$
Incorrect variance
$\begin{aligned} & (5.1)^2=\frac{\sum \mathrm{x}_{\mathrm{i}}^2}{100}-(\overline{\mathrm{x}})^2 \\ & \sum \mathrm{x}_{\mathrm{i}}^2=100 \times\left(40^2\right)+100(5.1)^2 \\ & \sum \mathrm{x}_{\mathrm{i}}^2=16 \times 10^4+(5.1)^2 \times 100=162601 \\ & \sigma^2=\frac{\sum \mathrm{x}_{\mathrm{i}}^2-50^2+40^2}{100}-(\mu)^2 \\ & \sigma^2=1617.01-(39.9)^2=25 \\ & \sigma=5 \\ & 10(\mu+\sigma)=10(39.9+5) \\ & =10 \times 44.9=449\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the mean and the standard deviation of the observation $2,3,3,4,5,7$, a, b be 4 and $\sqrt{2}$ respectively. Then the mean deviation about the mode of these observations is :

**Options:**

- **(A)** $1$
- **(B)** $\frac{3}{4}$
- **(C)** $2$
- **(D)** $\frac{1}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1$**

**Detailed Solution:**

$\begin{aligned} & \frac{24+a+b}{8}=4 \\ & a+b=8 \\ & 2=\frac{4+1+1+0+1+9+(a-4)^2+(b-4)^2}{8} \\ & 16=48+a^2+b^2-8 a-8 b \\ & a^2+b^2=32 \\ & 32=2 a b \\ & a b=16 \\ & a=4 b=4 \\ & \text { mode }=4 \\ & \text { mean deviation }=\frac{2+1+1+0+1+3+0+0}{8}=1 \\ & \text { option }(1)\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the Mean and Variance of five observations $x_1=1, x_2=3, x_3=a, x_4=7$ and $x_5=b, a \gt b$, be 5 and 10 respectively. Then the Variance of the observations $n+x_n, n=1,2, \ldots \ldots . .5$ is

**Options:**

- **(A)** $17$
- **(B)** $16.4$
- **(C)** $17.4$
- **(D)** $16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $16$**

**Detailed Solution:**

$\begin{aligned} & \bar{x}=\frac{\sum x_i}{n}=\frac{1+3+a+7+b}{5}=5 \\ & a+b=14 \\ & \sigma^2=\frac{\sum x_i^2}{n}-(\bar{x})^2 \\ & \Rightarrow \frac{1^2+3^2+a^2+7^2+b^2}{5}-25=10 \\ & a^2+b^2=116 \\ & a \gt b \quad a=10 \quad b=4 \\ & n+x_n: 2,5,13,11,9\end{aligned}$
$\begin{aligned} & \sigma^2=\frac{2^2+5^2+13^2+11^2+9^2}{5}-\left(\frac{2+5+13+11+9}{5}\right)^2 \\ & =80-64=16\end{aligned}$
option 4

</details>

---

### Q12. JEE Main 2025 (2 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and the variance of $6,4, a, 8, b, 12,10$, 13 are 9 and 9.25 respectively, then $a+b+a b$ is equal to :

**Options:**

- **(A)** $105$
- **(B)** $103$
- **(C)** $100$
- **(D)** $106$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $103$**

**Detailed Solution:**

$\begin{aligned} & \because \text { mean }=9 \\ & \therefore 53+\mathrm{a}+\mathrm{b}=72 \\ & \Rightarrow \mathrm{a}+\mathrm{b}=19 \\ & \because \sigma^2=\frac{37}{4} \text { and }(\overline{\mathrm{X}})^2+\sigma^2=\frac{\sum \mathrm{x}_1^2}{\mathrm{~N}} \\ & \Rightarrow 81+\frac{37}{4}=\frac{529+\mathrm{a}^2+\mathrm{b}^2}{8} \\ & \Rightarrow 648+74=529+\mathrm{a}^2+\mathrm{b}^2 \\ & \Rightarrow \mathrm{a}^2+\mathrm{b}^2=193 \\ & \because \mathrm{a}+\mathrm{b}=19 \Rightarrow \mathrm{a}^2+\mathrm{b}^2+2 \mathrm{ab}=361 \\ & \Rightarrow 2 \mathrm{ab}=168 \\ & \Rightarrow \mathrm{ab}=84 \\ & \therefore \mathrm{a}+\mathrm{b}+\mathrm{ab}=103\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let \(x_1, x_2, \ldots, x_{10}\) be ten observations such that \(\sum_{i=1}^{10}\left(x_i-2\right)=30, \sum_{i=1}^{10}\left(x_i-\beta\right)^2=98, \beta\gt2\), and their variance is \(\frac{4}{5}\). If \(\mu\) and \(\sigma^2\) are respectively the mean and the variance of \(2\left(x_1-1\right)+4 \beta\), \(2\left(x_2-1\right)+4 \beta, \ldots ., 2\left(x_{10}-1\right)+4 \beta\), then \(\frac{\beta \mu}{\sigma^2}\) is equal to :

**Options:**

- **(A)** 100
- **(B)** 120
- **(C)** 110
- **(D)** 90

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 100**

**Detailed Solution:**

$\begin{aligned}
& \sum_{l=1}^{10}\left(x_l-2\right)=30 \\
& \sum_{i=1}^{10} x_l=50 \\
& \Rightarrow \text { Mean }=5 \\
& \text { Variance }=\frac{4}{5}=\frac{\sum x_l^2}{10}-(\bar{x})^2 \\
& \frac{4}{5}=\frac{\sum x_l^2}{10}-25 \\
& \Rightarrow \sum x_l^2=258
\end{aligned}$
Now, $\sum_{l=1}^{10}\left(x_l-\beta\right)^2=98$
$\begin{aligned}
& \sum_{l=1}^{10} x_l^2-2 \beta \sum_{l=1}^{10} x_l+10 \beta^2=98 \\
& \Rightarrow 258-2 \beta(50)+10 \beta^2=98 \\
& \Rightarrow 10 \beta^2-100 \beta+160=0 \\
& \Rightarrow \beta^2-10 \beta+16=0 \\
& \Rightarrow \beta=8 \text { as } \beta>2
\end{aligned}$
Now, as per the question
$2\left(x_1-1\right)+4 \beta, 2\left(x_2-1\right)+4 \beta, \ldots 2\left(x_{10}-1\right)+4 \beta$
Can be simplified as
$2 x_1+30,2 x_2+30, \ldots, 2 x_{10}+30$
$\begin{aligned} & \mu=2(5)+30=40 \\ & \sigma^2=2^2\left(\frac{4}{5}\right)=\frac{16}{5} \\ & \frac{\beta \mu}{\sigma^2}=\frac{8 \times 40}{\frac{16}{5}}=100\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For a statistical data $\mathrm{x}_1, \mathrm{x}_2, \ldots, \mathrm{x}_{10}$ of 10 values, a student obtained the mean as 5.5 and $\sum_{i=1}^{10} x_i^2=371$. He later found that he had noted two values in the data incorrectly as 4 and 5 , instead of the correct values 6 and 8 , respectively. The variance of the corrected data is

**Options:**

- **(A)** $9$
- **(B)** $5$
- **(C)** $7$
- **(D)** $4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $7$**

**Detailed Solution:**

$\begin{aligned} & \text { Mean } \overline{\mathrm{x}}=5.5 \\ & =\sum_{\mathrm{i}=1}^{10} \mathrm{x}_{\mathrm{i}}=5.5 \times 10=55 \\ & =\sum_{\mathrm{i}=1}^{10} \mathrm{x}_{\mathrm{i}}^2=371 \\ & \left(\sum \mathrm{x}_{\mathrm{i}}\right)_{\text {new }}=55-(4+5)+(6+8)=60 \\ & \\ & \left(\sum \mathrm{x}_{\mathrm{i}}^2\right)_{\text {new }}=371-\left(4^2+5^2\right)+\left(6^2+8^2\right)=430\end{aligned}$


$\begin{aligned} & \text { Variance } \sigma^2=\frac{\sum \mathrm{x}_{\mathrm{i}}^2}{10}-\left(\frac{\sum \mathrm{x}_{\mathrm{i}}}{10}\right)^2 \\ & \sigma^2=\frac{430}{10}-\left(\frac{60}{10}\right)^2 \\ & \sigma^2=43-36 \\ & \sigma^2=7\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (23 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The variance of the numbers $8,21,34,47, \ldots, 320$ is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8788**

**Detailed Solution:**

$\begin{aligned}
& 8+(n-1) 13=320 \\
& 13 n=325 \\
& n=25 \\
& \text { no. of terms }=25
\end{aligned}$
$\begin{aligned}
& \text { mean }=\frac{\sum \mathrm{x}_{\mathrm{i}}}{\mathrm{n}}=\frac{8+21+\ldots+320}{25}=\frac{\frac{25}{2}(8+320)}{25} \\
& \text { variance } \sigma^2=\frac{\sum \mathrm{x}_{\mathrm{i}}^2}{\mathrm{n}}-(\text { mean })^2 \\
& =\frac{8^2+21^2+\ldots .+320^2}{13}-(164)^2 \\
& =8788
\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Consider <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> observation <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>..</mo><msub><mi>x</mi><mn>10</mn></msub></math>, such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>α</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>40</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>,</mo><mi>β</mi></math> are positive integers. Let the mean and the variance of the observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>84</mn><mn>25</mn></mfrac></math> respectively. The <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>β</mi><mi>α</mi></mfrac></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>x</mi><mn>10</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>α</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mn>10</mn><mi>α</mi><mo>=</mo><mn>2</mn></math></p><p>Mean, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi><mo>=</mo><mfrac><mn>6</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mrow><mo>∑</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>10</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∑</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>10</mn><mi>α</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mn>1</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>40</mn></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>y</mi><mi>i</mi></msub><mo>=</mo><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>β</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msubsup><mi>σ</mi><mi>y</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>∑</mo><msubsup><mi>y</mi><mi>i</mi><mn>2</mn></msubsup><mo>−</mo><msup><mfenced><mover><mi>y</mi><mo>¯</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>84</mn><mn>25</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>∑</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>β</mi></mrow></mfenced><mn>2</mn></msup><mo>−</mo><msup><mfenced><mfrac><mstyle displaystyle="true"><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>−</mo><mi>β</mi></mrow></mfenced></mstyle><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>84</mn><mn>25</mn></mfrac><mo>=</mo><mn>4</mn><mo>−</mo><msup><mfenced><mfrac><mrow><mn>12</mn><mo>−</mo><mn>10</mn><mi>β</mi></mrow><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mrow><mn>6</mn><mo>−</mo><mn>5</mn><mi>β</mi></mrow><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>−</mo><mfrac><mn>84</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mrow><mn>6</mn><mo>−</mo><mn>5</mn><mi>β</mi></mrow><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>16</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>6</mn><mo>−</mo><mn>5</mn><mi>β</mi><mo>=</mo><mo>±</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>β</mi><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math> (not possible) or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>β</mi><mi>α</mi></mfrac><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q17. JEE Main 2024 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the median and the mean deviation about the median of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>170</mn><mo>,</mo><mn>125</mn><mo>,</mo><mn>230</mn><mo>,</mo><mn>190</mn><mo>,</mo><mn>210</mn><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>170</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>205</mn><mn>7</mn></mfrac></math> respectively. Then the mean deviation about the mean of these <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observations is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>**

**Detailed Solution:**

<p>Given observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>125</mn><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mn>170</mn><mo>,</mo><mn>190</mn><mo>,</mo><mn>210</mn><mo>,</mo><mn>230</mn></math>.</p><p>Median<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>170</mn></math></p><p>Mean deviation about median is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>205</mn><mn>7</mn></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mn>205</mn><mn>7</mn></mfrac><mo>=</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mn>45</mn><mo>+</mo><mn>60</mn><mo>+</mo><mn>20</mn><mo>+</mo><mn>40</mn><mo>+</mo><mn>170</mn><mo>−</mo><mi>a</mi><mo>+</mo><mn>170</mn><mo>−</mo><mi>b</mi></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>300</mn></math></p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>170</mn><mo>+</mo><mn>125</mn><mo>+</mo><mn>230</mn><mo>+</mo><mn>190</mn><mo>+</mo><mn>210</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>175</mn></math></p><p>Mean deviation about mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>50</mn><mo>+</mo><mn>175</mn><mo>−</mo><mi>a</mi><mo>+</mo><mn>175</mn><mo>−</mo><mi>b</mi><mo>+</mo><mn>5</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>35</mn><mo>+</mo><mn>55</mn></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>30</mn></math></p>

</details>

---

### Q18. JEE Main 2024 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the mean and the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo> </mo><mi>b</mi><mo>,</mo><mo> </mo><mn>68</mn><mo>,</mo><mo> </mo><mn>44</mn><mo>,</mo><mo> </mo><mn>48</mn><mo>,</mo><mo> </mo><mn>60</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>194</mn></math>, respectively if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&gt;</mo><mi>b</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>190</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>**

**Detailed Solution:**

<p>Mean, <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>68</mn><mo>+</mo><mn>44</mn><mo>+</mo><mn>48</mn><mo>+</mo><mn>60</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>55</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>220</mn><mo>=</mo><mn>330</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>110</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Variance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>σ</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>∑</mo><mrow></mrow><mrow></mrow></munderover></mstyle><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced><mn>2</mn></msup></mrow><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>σ</mi><mn>2</mn></msup><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mn>13</mn><mn>2</mn></msup><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup><mo>+</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup></mstyle><mn>6</mn></mfrac><mo>=</mo><mn>194</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>364</mn><mo>=</mo><mn>1164</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><mn>110</mn><mo>-</mo><mi>b</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>b</mi><mo>-</mo><mn>55</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>800</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><msup><mfenced><mrow><mn>55</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>800</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>55</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>b</mi><mo>=</mo><mn>35</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>=</mo><mn>75</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>=</mo><mn>75</mn><mo>+</mo><mn>105</mn><mo>=</mo><mn>180</mn></math></p>

</details>

---

### Q19. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>If the variance <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>σ</mi><mn>2</mn></msup></math> of the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid" frame="solid" rowlines="solid"><mtr><mtd><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub></mtd><mtd><mn>0</mn></mtd><mtd><mn>1</mn></mtd><mtd><mn>5</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>10</mn></mtd><mtd><mn>12</mn></mtd><mtd><mn>17</mn></mtd></mtr><mtr><mtd><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>2</mn></mtd><mtd><mn>6</mn></mtd><mtd><mn>3</mn></mtd><mtd><mn>3</mn></mtd></mtr></mtable></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>k</mi></mfenced></math> is ______ {where <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mo>.</mo></mfenced></math> denotes the greatest integer funciton}</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **29**

**Detailed Solution:**

<blockquote><p>Finding the <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mo> </mo><mo>&amp;</mo><mo> </mo><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub><msup><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mn>2</mn></msup></math> we get, </p><p><img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/65fd7a2b-8492-4636-abe9-d668833434e9.png" style="width: 512px; height: 338px;"/></p><p>Now, from above table we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>∑</mo><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mo>=</mo><mn>176</mn></math></p><p>Now, finding  <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">x</mi><mo>¯</mo></mover><mo>=</mo><mfrac><mrow><mo>∑</mo><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub></mrow><mrow><mo>∑</mo><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub></mrow></mfrac><mo>=</mo><mfrac><mn>176</mn><mn>22</mn></mfrac><mo>=</mo><mn>8</mn></math></p><p>Now, finding variance, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mi mathvariant="normal">N</mi></mfrac><mo>∑</mo><msub><mi mathvariant="normal">f</mi><mi mathvariant="normal">i</mi></msub><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mmultiscripts><mo>-</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>(</mo><mover><mi mathvariant="normal">x</mi><mo>¯</mo></mover><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>22</mn></mfrac><mo>×</mo><mn>2048</mn><mo>-</mo><mo>(</mo><mn>8</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup><mo>=</mo><mo> </mo><mn>93</mn><mo>.</mo><mn>090964</mn><mo> </mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup><mo>=</mo><mo> </mo><mn>29</mn><mo>.</mo><mn>0909</mn><mo> </mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup></mfenced><mo>=</mo><mo> </mo><mfenced close="]" open="["><mrow><mn>29</mn><mo>.</mo><mn>0909</mn></mrow></mfenced><mo>=</mo><mn>29</mn></math></p></blockquote>

</details>

---

### Q20. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and variance of five observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>24</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>194</mn><mn>25</mn></mfrac></math> respectively and the mean of first four observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math>, then the variance of the first four observations in equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>77</mn><mn>12</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>105</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given: </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mfrac><mn>24</mn><mn>5</mn></mfrac></math> and variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>194</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>5</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mfrac><mn>24</mn><mn>5</mn></mfrac><mo>×</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>5</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>24</mn></math></p><p>Also, variance</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>5</mn></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>24</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>194</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>5</mn></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>154</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mi>th</mi></msup></math> observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>-</mo><mtext>sum of first</mtext><mo> </mo><mn>4</mn><mo> </mo><mtext>terms</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>-</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>×</mo><mn>4</mn><mo>=</mo><mn>10</mn></math></p><p>So, new variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>4</mn></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mn>4</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>7</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>154</mn><mo>-</mo><mn>100</mn></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>49</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q21. JEE Main 2024 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If the mean and variance of the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>65</mn><mo>,</mo><mn>68</mn><mo>,</mo><mn>58</mn><mo>,</mo><mn>44</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn><mo>,</mo><mn>45</mn><mo>,</mo><mn>60</mn><mo>,</mo><mi>α</mi><mo>,</mo><mi>β</mi><mo>,</mo><mn>60</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>&gt;</mo><mi>β</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>56</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn><mo>.</mo><mn>2</mn></math> respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6344**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">x</mi><mo>¯</mo></mover><mo>=</mo><mn>56</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup><mo>=</mo><mn>66</mn><mo>.</mo><mn>2</mn></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>σ</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>∑</mo><mrow></mrow><mrow></mrow></munderover></mstyle><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><menclose notation="top"><mi>x</mi></menclose></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><msup><mn>65</mn><mn>2</mn></msup><mo>+</mo><msup><mn>68</mn><mn>2</mn></msup><mo>+</mo><msup><mn>58</mn><mn>2</mn></msup><mo>+</mo><msup><mn>44</mn><mn>2</mn></msup><mo>+</mo><msup><mn>48</mn><mn>2</mn></msup><mo>+</mo><msup><mn>45</mn><mn>2</mn></msup><mo>+</mo><msup><mn>60</mn><mn>2</mn></msup><mo>+</mo><msup><mi>α</mi><mn>2</mn></msup><mo>+</mo><msup><mi>β</mi><mn>2</mn></msup><mo>+</mo><msup><mn>60</mn><mn>2</mn></msup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>56</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>66</mn><mo>.</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">β</mi><mn>2</mn></msup><mo>+</mo><mn>25678</mn></mrow><mn>10</mn></mfrac><mo>-</mo><mo>(</mo><mn>56</mn><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>66</mn><mo>.</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">β</mi><mn>2</mn></msup><mo>+</mo><mn>25678</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfenced><mrow><mn>3136</mn><mo>+</mo><mn>66</mn><mo>.</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">β</mi><mn>2</mn></msup><mo>=</mo><mn>32022</mn><mo>-</mo><mn>25678</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">α</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">β</mi><mn>2</mn></msup><mo>=</mo><mn>6344</mn></math></p>

</details>

---

### Q22. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The mean and standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> observations were found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> respectively. On rechecking it was found that an observation was read as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> in place of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>μ</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>σ</mi><mn>2</mn></msup></math> denote the mean and variance of the correct observations respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mfenced><mrow><mi>μ</mi><mo>+</mo><msup><mi>μ</mi><mn>2</mn></msup><mo>+</mo><msup><mi>σ</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2521**

**Detailed Solution:**

<p>Given: Incorrect mean, <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mn>12</mn></math> and incorrect standard deviation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">σ</mi><mo>'</mo></msup><mo>=</mo><mn>3</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><msub><mi>Σx</mi><mi mathvariant="normal">i</mi></msub><mn>15</mn></mfrac><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>Σx</mi><mi mathvariant="normal">i</mi></msub><mo>=</mo><mn>180</mn></math></p><p>Correct mean is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">μ</mi><mo>=</mo><mfrac><mrow><msub><mi>Σx</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mn>10</mn><mo>+</mo><mn>12</mn></mrow><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">μ</mi><mo>=</mo><mfrac><mn>182</mn><mn>15</mn></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">σ</mi><mo>'</mo></msup><mo>=</mo><msqrt><mfrac><mrow><mo>∑</mo><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup></mrow><mn>15</mn></mfrac><mo>-</mo><mn>144</mn></msqrt><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mo>∑</mo><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup></mrow><mn>15</mn></mfrac><mo>=</mo><mn>9</mn><mo>+</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mo>∑</mo><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>2295</mn></math></p><p>Correct <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>Σx</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>2295</mn><mo>-</mo><mn>100</mn><mo>+</mo><mn>144</mn><mo>=</mo><mn>2339</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup></math> (correct variance) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2339</mn><mn>15</mn></mfrac><mo>-</mo><mfrac><mrow><mn>182</mn><mo>×</mo><mn>182</mn></mrow><mrow><mn>15</mn><mo>×</mo><mn>15</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mfenced><mrow><mi mathvariant="normal">μ</mi><mo>+</mo><msup><mi mathvariant="normal">μ</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>15</mn><mfenced><mrow><mfrac><mn>182</mn><mn>15</mn></mfrac><mo>+</mo><mfrac><mrow><mn>182</mn><mo>×</mo><mn>182</mn></mrow><mrow><mn>15</mn><mo>×</mo><mn>15</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2339</mn><mn>15</mn></mfrac><mo>-</mo><mfrac><mrow><mn>182</mn><mo>×</mo><mn>182</mn></mrow><mrow><mn>15</mn><mo>×</mo><mn>15</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mfenced><mrow><mi mathvariant="normal">μ</mi><mo>+</mo><msup><mi mathvariant="normal">μ</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>15</mn><mfenced><mrow><mfrac><mn>182</mn><mn>15</mn></mfrac><mo>+</mo><mfrac><mn>2339</mn><mn>15</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>15</mn><mfenced><mrow><mi mathvariant="normal">μ</mi><mo>+</mo><msup><mi mathvariant="normal">μ</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">σ</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>2521</mn></math></p>

</details>

---

### Q23. JEE Main 2024 (27 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>10</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> observations such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi></msub><mo>=</mo><mn>50</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>∑</mo><mrow><mo>∀</mo><mi mathvariant="normal">k</mi><mo>&lt;</mo><mi mathvariant="normal">j</mi></mrow></munder><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi></msub><mo>·</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">j</mi></msub><mo>=</mo><mn>1100</mn></math>. Then the standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>10</mn></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>115</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math>**

**Detailed Solution:**

<p>Given: <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>∑</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi></msub><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>+</mo><mo>…</mo><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>10</mn></msub><mo>=</mo><mn>50</mn><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mrow><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>+</mo><mo>…</mo><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>10</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>2500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><munder><mo>∑</mo><mrow><mi mathvariant="normal">k</mi><mo>&lt;</mo><mi mathvariant="normal">j</mi></mrow></munder><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">k</mi></msub><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">j</mi></msub><mo>=</mo><mn>2500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><mo>×</mo><mn>1100</mn><mo>=</mo><mn>2500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>2500</mn><mo>-</mo><mn>2</mn><mfenced><mn>1100</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>300</mn></math></p><p> Standard deviation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">σ</mi><mo>=</mo><msqrt><mfrac><mrow><mo>∑</mo><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup></mrow><mi mathvariant="normal">n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>∑</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi></msub></mrow><mi mathvariant="normal">n</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">σ</mi><mo>=</mo><msqrt><mfrac><mrow><mo>∑</mo><msubsup><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>∑</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">i</mi></msub></mrow><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">σ</mi><mo>=</mo><msqrt><mfrac><mn>300</mn><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>50</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">σ</mi><mo>=</mo><msqrt><mn>30</mn><mo>-</mo><mn>25</mn></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p>

</details>

---

### Q24. JEE Main 2023 (15 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean and standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> respectively. Later on, it was observed that one observation was recorded as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> instead of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>. Then the correct variance is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>**

**Detailed Solution:**

<blockquote><p>Incorrect mean is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub></mstyle><mn>10</mn></mfrac><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>200</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>So, corrected mean is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>50</mn><mo>+</mo><mn>40</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mfrac><mrow><mn>200</mn><mo>-</mo><mn>10</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>19</mn></math></p><p>Incorrect variance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>10</mn></mfrac><mo>-</mo><mn>400</mn><mo>=</mo><mn>64</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>4640</mn></math></p><p>Now, corrected variance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>40</mn><mn>2</mn></msup><mo>-</mo><msup><mn>50</mn><mn>2</mn></msup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>19</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4640</mn><mo>-</mo><mn>900</mn></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>19</mn></mfenced><mn>2</mn></msup><mspace linebreak="newline"></mspace><mo>=</mo><mn>374</mn><mo>-</mo><mn>361</mn><mspace linebreak="newline"></mspace><mo>=</mo><mn>13</mn></math></p></blockquote>

</details>

---

### Q25. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

The mean and standard deviation of the marks of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> students were found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> respectively. Later, it was observed that two marks <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> were wrongly read as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> respectively. Then the correct variance is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **269**

**Detailed Solution:**

<blockquote><p>Let the observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>8</mn></msub><mo>,</mo><mo>&#160;</mo><mn>45</mn><mo>,</mo><mo>&#160;</mo><mn>50</mn></math>,</p><p>Mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>x</mi><mn>8</mn></msub><mo>+</mo><mn>45</mn><mo>+</mo><mn>50</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>x</mi><mn>8</mn></msub><mo>=</mo><mn>405</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Hence, new mean</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mover><mi>X</mi><mo>&#175;</mo></mover></mfenced><mi>new</mi></msub><mo>=</mo><mfrac><mrow><mn>405</mn><mo>+</mo><mn>20</mn><mo>+</mo><mn>25</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>45</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><msqrt><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>8</mn></munderover><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>45</mn><mn>2</mn></msup><mo>+</mo><msup><mn>50</mn><mn>2</mn></msup></mstyle><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>50</mn></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mo>=</mo><msqrt><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>8</mn></munderover><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>+</mo><mn>4525</mn></mstyle><mn>10</mn></mfrac><mo>-</mo><mn>2500</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>8</mn></munderover><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>21915</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mi>Variance</mi></mfenced><mi>new</mi></msub><mo>=</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>8</mn></munderover><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>20</mn><mn>2</mn></msup><mo>+</mo><msup><mn>25</mn><mn>2</mn></msup></mstyle><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>45</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mfenced><mi>Variance</mi></mfenced><mi>new</mi></msub><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>21915</mn><mo>+</mo><msup><mn>20</mn><mn>2</mn></msup><mo>+</mo><msup><mn>25</mn><mn>2</mn></msup></mstyle><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mn>45</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mfenced><mi>Variance</mi></mfenced><mi>new</mi></msub><mo>=</mo><mn>2294</mn><mo>-</mo><mn>2025</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mfenced><mi>Variance</mi></mfenced><mi>new</mi></msub><mo>=</mo><mn>269</mn></math></p><p>Hence this is the correct answer.</p></blockquote>

</details>

---

### Q26. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>Let the mean of the data</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>		</tr>		<tr>			<td style="text-align: center;">Frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>f</mi></mfenced></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>		</tr>	</tbody></table><p>be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> are respectively the mean deviation about the mean and the variance of the data, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mrow><mi>m</mi><mo>+</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfrac></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The mean of the below data is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>		</tr>		<tr>			<td style="text-align: center;">Frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>f</mi></mfenced></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>		</tr>	</tbody></table><p>Now finding mean we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>4</mn><mo>+</mo><mn>72</mn><mo>+</mo><mn>28</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>7</mn><mi>&#945;</mi><mo>+</mo><mn>72</mn></mrow><mrow><mn>64</mn><mo>+</mo><mi>&#945;</mi></mrow></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>16</mn></math></p><p>So, total number of observation will be, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><mo>=</mo><mn>80</mn></math></p><p>Now finding, mean deviation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">M</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>24</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>16</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>4</mn></mrow><mn>80</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math></p><p>Now finding, variance we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>16</mn><mo>+</mo><mn>24</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>16</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>80</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>22</mn><mn>5</mn></mfrac></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mi>&#945;</mi></mrow><mrow><mi>m</mi><mo>+</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>16</mn></mrow><mrow><mfrac><mn>8</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>22</mn><mn>5</mn></mfrac></mrow></mfrac><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q27. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the positive numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mrow><mn>2</mn><mo>,</mo></mrow></msub><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>4</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>5</mn></msub></math> be in a G.P. Let their mean and variance be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>10</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac></math> respectively, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime. If the mean of their reciprocals is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>31</mn><mn>10</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>=</mo><mn>14</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **211**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> positive numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>5</mn></msub></math> are in geometric progression. So, let the numbers be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi>a</mi><mi>r</mi></mfrac><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mi>r</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></math></p><p>According to question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mfrac><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mi>a</mi><mi>r</mi></mfrac><mo>+</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mstyle><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>10</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mfrac><msup><mi>r</mi><mn>2</mn></msup><mi>a</mi></mfrac><mo>+</mo><mfrac><mi>r</mi><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mi>a</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>a</mi><mi>r</mi></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></mstyle><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>40</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>a</mi></mfrac><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>r</mi></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><msup><mi>r</mi><mn>2</mn></msup></mstyle></mfrac></mrow></mfenced></mstyle><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>31</mn><mn>40</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>By <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>r</mi></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><msup><mi>r</mi><mn>2</mn></msup></mstyle></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>31</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>r</mi><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mi>r</mi></mstyle></mfrac><mo>=</mo><mfrac><mn>27</mn><mn>4</mn></mfrac><mo>+</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mi>t</mi><mo>=</mo><mfrac><mn>35</mn><mn>4</mn></mfrac></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>t</mi><mo>-</mo><mn>35</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>So, numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math></p><p>Variance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>64</mn></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>8</mn></mrow><mn>5</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>186</mn><mn>25</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>211</mn></math></p><p>Hence this is the required option.</p>

</details>

---

### Q28. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the mean of 6 observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and their variance be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>. Then their mean deviation about the mean is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Consider the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi></math>.</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Mean</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>12</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>18</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Variance</mi><mo>=</mo><mfenced><mfrac><mrow><munder><mo>&#8721;</mo><mrow></mrow></munder><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac></mfenced><mo>-</mo><msup><mfenced><mfrac><mrow><munder><mo>&#8721;</mo><mrow></mrow></munder><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mo>=</mo><mfenced><mfrac><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac></mfenced><mo>-</mo><msup><mfenced><mn>5</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>164</mn></math></p><p>We have <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>18</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>164</mn></math>.</p><p>Now solving above equations we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>8</mn></math>,</p><p>Now mean deviation about mean will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover></mstyle><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced close="|" open="|"><mrow><mn>1</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>2</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>4</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>10</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q29. JEE Main 2023 (11 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> have <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> elements each. Let the mean of the elements in sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> respectively and the variance of the elements in sets <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> respectively. A new set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> elements is formed by subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> from each element of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> to each element of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>. Then the sum of the mean and variance of the elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>38</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>38</mn></math>**

**Detailed Solution:**

<blockquote><p>Let the elements in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><msub><mi>x</mi><mn>5</mn></msub></mrow></mfenced></math></p><p>Now given mean is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p>Now subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> from each term we get, </p><p>New mean as <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mn>5</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mo>-</mo><mn>3</mn><mo>=</mo><mn>2</mn></math></p><p>So, sum of elements will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>10</mn></math></p><p>Also given variance,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Var</mo><mfenced><mi>X</mi></mfenced><mo>=</mo><mn>12</mn></math></p><p>Now we know that subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> from each term will not change the variance,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Var</mo><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>3</mn><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><msub><mi>x</mi><mn>5</mn></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mn>4</mn><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>80</mn></math></p><p>Now let elements in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>&#8230;</mo><msub><mi>y</mi><mn>5</mn></msub></mrow></mfenced></math></p><p>Given mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>&#8230;</mo><msub><mi>y</mi><mn>5</mn></msub></mrow></mfenced><mo>=</mo><mn>8</mn></math></p><p>Now adding each element by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> we get,</p><p>New mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><msub><mi>y</mi><mn>5</mn></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>10</mn></math></p><p>So, sum of elements will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>50</mn></math></p><p>Also given <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Var</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>&#8230;</mo><msub><mi>y</mi><mn>5</mn></msub></mrow></mfenced><mo>=</mo><mn>20</mn></math></p><p>Similarly new variance, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Var</mo><mfenced><mrow><msub><mi>y</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><mo>,</mo><msub><mi>y</mi><mn>2</mn></msub><mo>+</mo><mn>2</mn><mo>&#8230;</mo><msub><mi>y</mi><mn>5</mn></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>y</mi><mi>i</mi></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mn>100</mn><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>y</mi><mi>i</mi></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>120</mn><mo>&#215;</mo><mn>5</mn></math></p><p>Now finding, combined mean we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>5</mn></msubsup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mo>&#8721;</mo><mfenced><mrow><msub><mi>y</mi><mi>i</mi></msub><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>10</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>+</mo><mn>50</mn></mrow><mn>10</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p>And combined variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>3</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>y</mi><mi>i</mi></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mn>6</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>80</mn><mo>+</mo><mn>120</mn><mo>&#215;</mo><mn>5</mn></mrow><mn>10</mn></mfrac><mo>-</mo><mn>36</mn><mo>=</mo><mn>32</mn></math></p><p>Hence, the sum of combined mean and variance will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>38</mn></math></p></blockquote>

</details>

---

### Q30. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math>  be the mean and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> be the standard deviation of the distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>+</mo><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>-</mo><mn>3</mn></math></td>		</tr>	</tbody></table><p>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#931;</mi><msub><mi>f</mi><mi>i</mi></msub><mo>=</mo><mn>62</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>x</mi></mfenced></math> denotes the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>x</mi></math>, then<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><msup><mi>&#956;</mi><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfenced></math>  is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>+</mo><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>-</mo><mn>3</mn></math></td>		</tr>	</tbody></table><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>Mean</mtext><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>X</mi><mi>i</mi></msub><msub><mi>f</mi><mi>i</mi></msub></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mo>&#160;</mo><mn>2</mn><msup><mi>k</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#8211;</mo><mn>2</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup><mo>&#8211;</mo><mn>3</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mn>4</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#160;</mo><mo>+</mo><mn>5</mn><mi>k</mi><mo>&#160;</mo><mo>&#8211;</mo><mo>&#160;</mo><mn>15</mn></mrow><mn>62</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>9</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mi>k</mi><mo>-</mo><mn>16</mn></mrow><mn>62</mn></mfrac><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><mo>=</mo><mn>62</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>k</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>62</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi mathvariant="normal">k</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi mathvariant="normal">k</mi><mo>-</mo><mn>64</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>3</mn><mi mathvariant="normal">k</mi><mo>+</mo><mn>16</mn><mo>)</mo><mo>(</mo><mi mathvariant="normal">k</mi><mo>-</mo><mn>4</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>4</mn></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> in above equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mfrac><mn>156</mn><mn>62</mn></mfrac></math></p><p>Now finding variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>X</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><msub><mi>f</mi><mi>i</mi></msub></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac><mo>-</mo><msup><mfenced><mtext>Mean</mtext></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#183;</mo><mfenced><mrow><mn>2</mn><mi>k</mi></mrow></mfenced><mo>+</mo><mn>4</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>9</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>16</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>25</mn><mfenced><mrow><mi>k</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mn>62</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>156</mn><mn>62</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>29</mn><msup><mi mathvariant="normal">k</mi><mn>2</mn></msup><mo>+</mo><mn>27</mn><mi mathvariant="normal">k</mi><mo>-</mo><mn>72</mn></mrow><mn>62</mn></mfrac><mo>-</mo><msup><mi mathvariant="normal">&#956;</mi><mn>2</mn></msup></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> in above equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>500</mn><mn>62</mn></mfrac><mo>-</mo><msup><mi mathvariant="normal">&#956;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi mathvariant="normal">&#963;</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">&#956;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>500</mn><mn>62</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">&#963;</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">&#956;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>8</mn></math></p></blockquote>

</details>

---

### Q31. JEE Main 2023 (10 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>If the mean of the frequency distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td>Class :</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>10</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mn>20</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>-</mo><mn>30</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>-</mo><mn>40</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>-</mo><mn>50</mn></math></td>		</tr>		<tr>			<td>Frequency :</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>		</tr>	</tbody></table><p>is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>, then its variance is ________ .</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **151**

**Detailed Solution:**

<blockquote><p>Given that the mean for the frequency distribution is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn></math>.</p><p>We know that Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><menclose notation="top"><mi>x</mi></menclose></mfenced><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p>Now for the class interval <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>-</mo><mn>10</mn></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>0</mn><mo>+</mo><mn>10</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>5</mn></math>. </p><p>Similarly we can calculate <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math> for other class intervals.</p><p>Now we know that mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>28</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>15</mn><mo>+</mo><mi>x</mi><mo>&#215;</mo><mn>25</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>35</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>45</mn></mrow><mrow><mn>14</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>28</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>6</mn></math></p><p>Also we know that variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><msup><mi>&#963;</mi><mn>2</mn></msup></mfenced><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msup><mfenced><mrow><mover><mi>x</mi><mo>&#175;</mo></mover><mo>-</mo><msub><mi>x</mi><mi>i</mi></msub></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>28</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>28</mn><mo>-</mo><mn>15</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>28</mn><mo>-</mo><mn>25</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>28</mn><mo>-</mo><mn>35</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#215;</mo><msup><mfenced><mrow><mn>28</mn><mo>-</mo><mn>45</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><msup><mfenced><mn>23</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#215;</mo><msup><mfenced><mn>13</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>6</mn><mo>&#215;</mo><msup><mfenced><mn>3</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>&#215;</mo><msup><mfenced><mn>7</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#215;</mo><msup><mfenced><mn>17</mn></mfenced><mn>2</mn></msup></mrow><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>151</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q32. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> respectively. Later on, it was observed that two observations were considered as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> instead of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> respectively. If the correct variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are coprime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> are coprime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>315</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>316</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>314</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>317</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>317</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> respectively,</p><p>So, mean will be,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>9</mn><mo>+</mo><mn>10</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>x</mi><mn>12</mn></msub></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>12</mn></msub><mo>+</mo><mn>19</mn><mo>=</mo><mn>54</mn></math></p><p>Now removing the observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>10</mn></math> and adding the observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>14</mn></math>,</p><p>So, the new total sum of the observation will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>12</mn></msub><mo>+</mo><mn>7</mn><mo>+</mo><mn>14</mn><mo>=</mo><mn>54</mn><mo>-</mo><mn>19</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>14</mn></math></p><p>Now new mean will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>x</mi><mn>12</mn></msub><mo>+</mo><mn>7</mn><mo>+</mo><mn>14</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mn>56</mn><mn>12</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mtext>new</mtext></msub><mo>=</mo><mfrac><mn>14</mn><mn>3</mn></mfrac></math>
Now using the formula of the variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>12</mn><mn>2</mn></msubsup><mo>+</mo><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup></mrow><mn>12</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>9</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>12</mn><mn>2</mn></msubsup><mo>+</mo><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup><mo>-</mo><mn>81</mn><mo>&#215;</mo><mn>3</mn><mo>=</mo><mn>4</mn><mo>&#215;</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>12</mn><mn>2</mn></msubsup><mo>+</mo><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup><mo>=</mo><mn>291</mn></math></p><p>Now removing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mn>10</mn><mn>2</mn></msup></math> and adding <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mn>2</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mn>14</mn><mn>2</mn></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>12</mn><mn>2</mn></msubsup><mo>+</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>14</mn><mn>2</mn></msup><mo>=</mo><mn>355</mn></math>
New variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>N</mi></mfrac><mo>-</mo><mo>(</mo><mover><mi>x</mi><mo>&#175;</mo></mover><msup><mo>)</mo><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>355</mn><mn>12</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>14</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>281</mn><mn>36</mn></mfrac></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>=</mo><mfrac><mn>281</mn><mn>36</mn></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>281</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>317</mn></math> </p></blockquote>

</details>

---

### Q33. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.</mo><mn>25</mn></math> respectively. If  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mi>y</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<blockquote><p>Given, the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>,</mo><mo>&#160;</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn></math>.</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Mean</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>10</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>12</mn></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>52</mn></mrow><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mn>52</mn><mo>=</mo><mn>72</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>20</mn></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Variance</mi><mo>=</mo><mfenced><mfrac><mrow><munder><mo>&#8721;</mo><mrow></mrow></munder><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac></mfenced><mo>-</mo><msup><mfenced><mfrac><mrow><munder><mo>&#8721;</mo><mrow></mrow></munder><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mo>.</mo><mn>25</mn><mo>=</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>100</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>36</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>144</mn></mrow><mn>8</mn></mfrac></mfenced><mo>-</mo><msup><mfenced><mn>9</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>218</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>218</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>20</mn><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>218</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>182</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>91</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>20</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>91</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>13</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mn>3</mn><mi>x</mi><mo>-</mo><mn>2</mn><mi>y</mi><mo>=</mo><mn>25</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2023 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>If the mean and variance of the frequency distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>	</tbody></table><p>are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>08</mn></math> respectively, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi></math> is _____.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The mean and variance of the frequency distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>	</tbody></table><p>are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>08</mn></math> respectively, </p><p>Now mean is given by,</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>8</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>120</mn><mo>+</mo><mn>80</mn><mo>+</mo><mn>56</mn><mo>+</mo><mn>80</mn><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>12</mn><mi>&#946;</mi></mrow><mrow><mn>40</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfrac><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>360</mn><mo>+</mo><mn>9</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>=</mo><mn>360</mn><mo>+</mo><mn>6</mn><mi>&#945;</mi><mo>+</mo><mn>12</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#945;</mi><mo>-</mo><mn>3</mn><mi>&#946;</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mi>&#946;</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now variance is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>08</mn><mo>=</mo><mfrac><mrow><mn>16</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>36</mn><mi>&#945;</mi><mo>+</mo><mn>960</mn><mo>+</mo><mn>800</mn><mo>+</mo><mn>144</mn><mi>&#945;</mi><mo>+</mo><mn>784</mn><mo>+</mo><mn>1280</mn></mrow><mrow><mn>40</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></mrow></mfrac><mo>-</mo><msup><mn>9</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>96</mn><mo>.</mo><mn>08</mn><mo>=</mo><mfrac><mrow><mn>3904</mn><mo>+</mo><mn>180</mn><mi>&#945;</mi></mrow><mrow><mn>40</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>40</mn><mo>+</mo><mn>2</mn><mi>&#945;</mi></mrow></mfenced><mfenced><mrow><mn>96</mn><mo>.</mo><mn>08</mn></mrow></mfenced><mo>=</mo><mn>3904</mn><mo>+</mo><mn>180</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3843</mn><mo>.</mo><mn>20</mn><mo>+</mo><mo>(</mo><mn>192</mn><mo>.</mo><mn>16</mn><mo>)</mo><mi>&#945;</mi><mo>=</mo><mn>3904</mn><mo>+</mo><mn>180</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>12</mn><mo>.</mo><mn>16</mn><mo>)</mo><mi>&#945;</mi><mo>=</mo><mn>60</mn><mo>.</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn><mo>=</mo><mi>&#946;</mi></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mn>25</mn><mo>+</mo><mn>25</mn><mo>-</mo><mn>25</mn><mo>=</mo><mn>25</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>The mean and variance of a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> respectively. The mean and variance of another set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> respectively. If the variance of all the <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> numbers in the two sets is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that,</p><p>For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo></math></p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>12</mn></math> and Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn></math></p><p>For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo></math></p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn></math> and Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#963;</mi><mn>2</mn></msup></math></p><p>Now, For set <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>15</mn></mfrac><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><mo>&#8658;</mo><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>15</mn><mo>&#215;</mo><mn>12</mn></mstyle></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup></mrow><mn>15</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>15</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>14</mn></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup></mrow><mn>15</mn></mfrac><mstyle displaystyle="false"><mo>-</mo></mstyle><mstyle displaystyle="false"><msup><mn>12</mn><mn>2</mn></msup></mstyle><mstyle displaystyle="false"><mo>=</mo></mstyle><mstyle displaystyle="false"><mn>14</mn></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup><mo>=</mo><mfenced><mrow><mn>14</mn><mo>+</mo><mn>144</mn></mrow></mfenced><mo>&#215;</mo><mn>15</mn></math></p><p>Now for set <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover><msub><mi>y</mi><mi>i</mi></msub></mstyle><mn>15</mn></mfrac><mo>=</mo><mn>14</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><mstyle displaystyle="true"><mo>&#8658;</mo></mstyle><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><mstyle displaystyle="true"><msub><mstyle displaystyle="true"><mi>y</mi></mstyle><mi>i</mi></msub></mstyle><mo>=</mo><mn>15</mn><mo>&#215;</mo><mn>14</mn></mstyle></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover><msup><msub><mi>y</mi><mi>i</mi></msub><mn>2</mn></msup></mstyle><mn>15</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover><msub><mi>y</mi><mi>i</mi></msub></mstyle><mn>15</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>&#963;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msup><msub><mi>y</mi><mi>i</mi></msub><mn>2</mn></msup></mrow><mn>15</mn></mfrac><mstyle displaystyle="false"><mo>-</mo></mstyle><mstyle displaystyle="false"><msup><mn>14</mn><mn>2</mn></msup></mstyle><mstyle displaystyle="false"><mo>=</mo></mstyle><mstyle displaystyle="false"><msup><mi>&#963;</mi><mn>2</mn></msup></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover><msup><msub><mi>y</mi><mi>i</mi></msub><mn>2</mn></msup><mo>=</mo><mfenced><mrow><msup><mi>&#963;</mi><mn>2</mn></msup><mo>+</mo><mn>196</mn></mrow></mfenced><mo>&#215;</mo><mn>15</mn></math></p><p>Now, </p><p>The combined variance will be</p><p>​​​​​​<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mstyle displaystyle="false"><mo>=</mo></mstyle><mfrac><mrow><mfenced><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>15</mn><mo>+</mo><mfenced><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msup><msub><mi>y</mi><mi>i</mi></msub><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>15</mn></mrow><mrow><mn>15</mn><mo>+</mo><mn>15</mn></mrow></mfrac><mstyle displaystyle="false"><mo>-</mo></mstyle><mstyle displaystyle="false"><msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>i</mi><mo>=</mo><mn>15</mn></mrow></munderover></mstyle><msub><mi>y</mi><mi>i</mi></msub></mrow><mrow><mn>15</mn><mo>+</mo><mn>15</mn></mrow></mfrac></mstyle></mfenced><mn>2</mn></msup></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mstyle displaystyle="false"><mo>=</mo></mstyle><mfrac><mrow><mfenced><mrow><mn>14</mn><mo>+</mo><mn>144</mn></mrow></mfenced><mo>&#215;</mo><mn>15</mn><mo>+</mo><mfenced><mrow><msup><mi>&#963;</mi><mn>2</mn></msup><mo>+</mo><mn>196</mn></mrow></mfenced><mo>&#215;</mo><mn>15</mn></mrow><mn>30</mn></mfrac><mstyle displaystyle="false"><mo>-</mo></mstyle><mstyle displaystyle="false"><msup><mn>13</mn><mn>2</mn></msup></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>10</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>10</mn></math></p></blockquote>

</details>

---

### Q36. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>=</mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>7</mn></msub></math> be in an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>. If the standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mn>7</mn></msub></math> is 4 and the mean is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>+</mo><msub><mi>x</mi><mn>6</mn></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>9</mn><mo>+</mo><mfrac><mn>8</mn><msqrt><mn>7</mn></msqrt></mfrac></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>=</mo><msub><mi mathvariant="normal">x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>2</mn></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mi mathvariant="normal">x</mi><mn>7</mn></msub></math> be in an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math></p><p>And the standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mn>7</mn></msub></math> is 4 and the mean is <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover></math>,</p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>=</mo><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mi>x</mi><mn>7</mn></msub></math> which is an A.P, we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>+</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mn>9</mn><mo>+</mo><mn>6</mn><mi>d</mi></math></p><p>Now subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> from the series we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><mn>2</mn><mi>d</mi><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>6</mn><mi>d</mi></math></p><p>So, mean will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mi>new</mi></msub><mo>=</mo><mfrac><mrow><mn>21</mn><mi>d</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>3</mn><mi>d</mi></math></p><p>Now using the formula of variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mfenced><mrow><msup><mn>0</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup></mrow></mfenced><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mfenced><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>13</mn></mrow><mn>6</mn></mfrac></mfenced><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>=</mo><mn>4</mn><msup><mi>d</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mn>2</mn></math></p><p>So, mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mo>&#160;</mo><mn>9</mn><mo>+</mo><mi>d</mi><mo>+</mo><mn>9</mn><mo>+</mo><mn>2</mn><mi>d</mi><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mn>9</mn><mo>+</mo><mn>6</mn><mi>d</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>15</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>+</mo><msub><mi>x</mi><mn>6</mn></msub><mo>=</mo><mn>15</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>5</mn><mi>d</mi><mo>=</mo><mn>15</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>10</mn><mo>=</mo><mn>34</mn></math></p>

</details>

---

### Q37. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn></math>, then the sum of cubes of the remaining two observations is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1072</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1792</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1216</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1456</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1072</mn></math>**

**Detailed Solution:**

<p>Let the two observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>.</p><p>Given:</p><p>Mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>And</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>5</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>=</mo><mfrac><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>130</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>16</mn><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>130</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>9</mn></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>7</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mn>343</mn><mo>+</mo><mn>729</mn><mo>=</mo><mn>1072</mn></math></p>

</details>

---

### Q38. JEE Main 2023 (31 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the mean and standard deviation of marks of class A of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> students be respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>, and the mean and standard deviation of marks of class <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> students be respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>-</mo><mi>&#945;</mi></math>. If the mean and variance of the marks of the combined class of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>+</mo><mi>n</mi></math> students are respectively <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>350</mn></math> , then the sum of variances of classes <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>450</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>650</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>900</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math>**

**Detailed Solution:**

<p>Let the mean is denoted by <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><msub><mi>x</mi><mi>i</mi></msub><mo>&#175;</mo></mover></math>, variance by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><msub><mi>&#963;</mi><mi>i</mi></msub><mn>2</mn></msup></math>, so standard deviation will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#963;</mi><mi>i</mi></msub></math>, now as per given data we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mi>A</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>B</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><mi>A</mi><mo>+</mo><mi>B</mi></mtd></mtr><mtr><mtd><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>40</mn></mtd><mtd><mo>&#160;</mo></mtd><mtd><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>55</mn></mtd><mtd><mo>&#160;</mo></mtd><mtd><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mn>50</mn></mtd></mtr><mtr><mtd><msub><mi>&#963;</mi><mn>1</mn></msub><mo>=</mo><mi>&#945;</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><msub><mi>&#963;</mi><mn>2</mn></msub><mo>=</mo><mn>30</mn><mo>-</mo><mi>&#945;</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><msub><mi>&#963;</mi><mn>2</mn></msub><mo>=</mo><mn>350</mn></mtd></mtr><mtr><mtd><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>100</mn></mtd><mtd><mo>&#160;</mo></mtd><mtd><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mi>n</mi></mtd><mtd><mo>&#160;</mo></mtd><mtd><mn>100</mn><mo>+</mo><mi>n</mi></mtd></mtr></mtable></math></p><p>So, using the formula of mean in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>40</mn><mo>+</mo><mn>55</mn><mi>n</mi></mrow><mrow><mn>100</mn><mo>+</mo><mi>n</mi></mrow></mfrac><mo>=</mo><mn>50</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>200</mn></math></p><p>Now using the formula of variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>100</mn></mfrac><mo>-</mo><msup><mn>40</mn><mn>2</mn></msup><mo>=</mo><msup><mi>&#945;</mi><mn>2</mn></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>y</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>200</mn></mfrac><mo>-</mo><msup><mn>55</mn><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>30</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></math></p><p>So, variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><mo>&#8721;</mo><msubsup><mi>y</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>300</mn></mfrac><mo>-</mo><msup><mn>50</mn><mn>2</mn></msup><mo>=</mo><msup><mn>350</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>350</mn><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>1600</mn><mo>+</mo><msup><mi>&#945;</mi><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>100</mn><mo>+</mo><mfenced close="]" open="["><mrow><mn>3025</mn><mo>+</mo><msup><mfenced><mrow><mn>30</mn><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mo>&#215;</mo><mn>200</mn></mrow><mn>300</mn></mfrac><mo>-</mo><msup><mn>50</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>40</mn><mi>&#945;</mi><mo>+</mo><mn>300</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>30</mn></math> is not possible</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#963;</mi><mn>1</mn></msub><mmultiscripts><mo>+</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><msub><mi>&#963;</mi><mn>2</mn></msub><mmultiscripts><mo>=</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>20</mn><mn>2</mn></msup><mo>=</mo><mn>500</mn></math></p>

</details>

---

### Q39. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>If the variance of the frequency distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 400px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>		</tr>		<tr>			<td>Frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi mathvariant="normal">i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>		</tr>	</tbody></table><p>is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>We have,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 400px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mi>i</mi></msub><mo>=</mo><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub><msubsup><mi>d</mi><mi>i</mi><mn>2</mn></msubsup></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>f</mi><mi>i</mi></msub><msub><mi>d</mi><mi>i</mi></msub></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>9</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>12</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>16</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>54</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math></td>		</tr>	</tbody></table><p> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mi>x</mi><mn>2</mn></msubsup><mo>=</mo><msubsup><mi>&#963;</mi><mi>d</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msubsup><mi>d</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msub><mi>d</mi><mi>i</mi></msub></mrow><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>=</mo><mfrac><mn>150</mn><mrow><mn>45</mn><mo>+</mo><mi>&#945;</mi></mrow></mfrac><mo>-</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>150</mn><mo>=</mo><mn>135</mn><mo>+</mo><mn>3</mn><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>&#945;</mi><mo>=</mo><mn>15</mn><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q40. JEE Main 2023 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> be the set of all values of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math> for which the mean deviation about the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> consecutive positive integers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mn>100</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> . Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#981;</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>99</mn><mo>}</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8469;</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>{</mo><mn>9</mn><mo>}</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8469;</mi></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math>  be any natural number </p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn></math> are values of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>i</mi></msub></math> or observation.</p><p>Now mean of the observation is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>99</mn></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>100</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>99</mn><mo>)</mo></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfrac><mrow><mn>99</mn><mo>&#215;</mo><mn>100</mn></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>100</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfrac><mn>99</mn><mn>2</mn></mfrac></math></p><p>Mean deviation about mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></msubsup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mover><mi mathvariant="italic">x</mi><mo mathvariant="italic">&#175;</mo></mover></mrow></mfenced></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mfenced><mrow><mfrac><mn>99</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>97</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>95</mn><mn>2</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>99</mn></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mn>50</mn><mn>2</mn></mfrac><mo>[</mo><mn>1</mn><mo>+</mo><mn>99</mn><mo>]</mo></mrow><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>25</mn></math></p><p>So, it is true for every natural no. &#39; <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math> &#39; as there is no term of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub></math> in mean deviation.</p>

</details>

---

### Q41. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> respectively. If one observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> is omitted, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are respectively mean and variance of remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> observation, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>3</mn><mo>&#160;</mo><mi>b</mi><mo>-</mo><mn>5</mn></math> is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **37**

**Detailed Solution:**

<p>Given,</p><p>Mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observation is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>16</mn></math> respectively,</p><p>So using the formula of mean we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mi>S</mi><mn>7</mn></mfrac><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>=</mo><mn>56</mn></math></p><p>Now if we remove <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math> sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>56</mn><mo>-</mo><mn>14</mn><mo>=</mo><mn>42</mn></math> and new mean will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>42</mn><mn>6</mn></mfrac><mo>=</mo><mn>7</mn></math></p><p>Now using the formula of variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>14</mn><mn>2</mn></msup></mstyle><mn>7</mn></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>14</mn><mn>2</mn></msup></mstyle><mn>7</mn></mfrac><mo>-</mo><msup><mn>8</mn><mn>2</mn></msup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>14</mn><mn>2</mn></msup></mstyle><mn>7</mn></mfrac><mo>=</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>14</mn><mn>2</mn></msup><mo>=</mo><mn>560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>364</mn></math></p><p>Now, new variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mfrac><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>6</mn></mfrac><mo>-</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>364</mn><mn>6</mn></mfrac><mo>-</mo><msup><mn>7</mn><mn>2</mn></msup><mo>=</mo><mfrac><mn>35</mn><mn>3</mn></mfrac></math></p><p>Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>-</mo><mn>5</mn><mo>=</mo><mn>7</mn><mo>+</mo><mn>35</mn><mo>-</mo><mn>5</mn><mo>=</mo><mn>37</mn></math></p>

</details>

---

### Q42. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>11</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>13</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>40</mn><mo>,</mo><mn>41</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mn>61</mn><mo>,</mo><mn>62</mn><mo>,</mo><mn>63</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>90</mn><mo>,</mo><mn>91</mn></mrow></mfenced></math> be the two sets of observations. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">x</mi><mo>&#175;</mo></mover></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi mathvariant="normal">y</mi><mo>&#175;</mo></mover></math> are their respective means and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> is the variance of all the observations in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">X</mi><mo>&#8746;</mo><mi mathvariant="normal">Y</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mover><mi mathvariant="normal">x</mi><mo>&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="normal">y</mi><mo>&#175;</mo></mover><mo>-</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to ________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **603**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>11</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>13</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>40</mn><mo>,</mo><mn>41</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mn>31</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mn>61</mn><mo>,</mo><mn>62</mn><mo>,</mo><mn>63</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mn>90</mn><mo>,</mo><mn>91</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced><mi>Y</mi></mfenced><mo>=</mo><mn>31</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>11</mn></mrow><mn>41</mn></msubsup><mi mathvariant="normal">i</mi></mrow><mn>31</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>31</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mrow><mn>41</mn><mo>&#215;</mo><mn>42</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>26</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>y</mi><mo mathvariant="italic">&#175;</mo></mover><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>61</mn></mrow><mn>91</mn></msubsup><mi mathvariant="normal">i</mi></mrow><mn>31</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>31</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mrow><mn>91</mn><mo>&#215;</mo><mn>92</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>60</mn><mo>&#215;</mo><mn>61</mn></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>=</mo><mn>73</mn></math></p><p>Combined mean,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>31</mn><mo>&#215;</mo><mn>26</mn><mo>+</mo><mn>31</mn><mo>&#215;</mo><mn>76</mn></mrow><mrow><mn>31</mn><mo>+</mo><mn>31</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>26</mn><mo>+</mo><mn>76</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>51</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>62</mn></mfrac><mo>&#215;</mo><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>31</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>31</mn></munderover><msup><mfenced><mrow><msub><mi>y</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi mathvariant="normal">i</mi></msub><mo>&#8712;</mo><mi>X</mi></math> are in A.P. with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math> elements  common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> , same is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">y</mi><mi mathvariant="normal">i</mi></msub><mo>&#8712;</mo><mi mathvariant="normal">y</mi></math>, when written in increasing order.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>31</mn></munderover><msup><mfenced><mrow><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">i</mi><mo>=</mo><mn>1</mn></mrow><mn>31</mn></munderover><msup><mfenced><mrow><msub><mi mathvariant="normal">y</mi><mi mathvariant="normal">i</mi></msub><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mn>40</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mn>40</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>40</mn><mo>&#215;</mo><mn>41</mn><mo>&#215;</mo><mn>81</mn></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>19</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>21855</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>21855</mn><mn>62</mn></mfrac><mo>+</mo><mfrac><mn>21855</mn><mn>62</mn></mfrac><mo>=</mo><mn>705</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced close="|" open="|"><mrow><mover><mi mathvariant="italic">x</mi><mo mathvariant="italic">&#175;</mo></mover><mo>+</mo><mover><mi mathvariant="italic">y</mi><mo mathvariant="italic">&#175;</mo></mover><mo>-</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mo>|</mo><mn>26</mn><mo>+</mo><mn>76</mn><mo>-</mo><mn>705</mn><mo>|</mo><mo>=</mo><mn>603</mn></math></p>

</details>

---

### Q43. JEE Main 2023 (25 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean and variance of the marks obtained by the students in a test are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> respectively. Later, the marks of one of the students is increased from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> . If the new mean of the marks is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>2</mn></math>. then their new variance is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>04</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo><mn>08</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>96</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>92</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo><mn>96</mn></math>**

**Detailed Solution:**

<p>Let the number of observations of the data set is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>.</p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow></mrow></munder><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>10</mn><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow></mrow></munder><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>8</mn><mo>+</mo><mn>12</mn><mo>=</mo><mn>10</mn><mo>.</mo><mn>2</mn><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>n</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>10</mn><mo>.</mo><mn>2</mn><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>.</mo><mn>2</mn><mi>n</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>20</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munder><mo>&#8721;</mo><mrow></mrow></munder></mstyle><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>20</mn></mfrac><mo>-</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mo>&#8721;</mo><mrow></mrow></munder><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>104</mn><mo>&#215;</mo><mn>20</mn><mo>=</mo><mn>2080</mn></math></p><p>Now, new variance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><munder><mo>&#8721;</mo><mrow></mrow></munder><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mn>12</mn><mn>2</mn></msup></mstyle><mn>20</mn></mfrac><mo>-</mo><msup><mfenced><mrow><mn>10</mn><mo>.</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>2080</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>20</mn></mstyle><mn>20</mn></mfrac><mo>-</mo><mn>104</mn><mo>.</mo><mn>04</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>108</mn><mo>-</mo><mn>104</mn><mo>.</mo><mn>04</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>3</mn><mo>.</mo><mn>96</mn></math></p>

</details>

---

### Q44. JEE Main 2023 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let the six numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>6</mn></msub></math> be in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>10</mn></math>.If the mean of these six numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>19</mn><mn>2</mn></mfrac></math> and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>105</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi></math> and common difference be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>d</mi><mo>=</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now,</p><p>Given mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mn>19</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn><mi>d</mi></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><mi>a</mi><mo>+</mo><mn>15</mn><mi>d</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>19</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>a</mi><mo>+</mo><mn>5</mn><mi>d</mi><mo>=</mo><mn>19</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mi>ii</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mn>3</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>14</mn><mo>,</mo><mo>&#160;</mo><mn>17</mn></math>.</p><p>Now variance is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>64</mn><mo>+</mo><mn>121</mn><mo>+</mo><mn>196</mn><mo>+</mo><mn>289</mn></mrow><mn>6</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>19</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>699</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>361</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>105</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>210</mn></math></p>

</details>

---

### Q45. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let the mean and the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><msub><mi>x</mi><mn>20</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>, respectively. For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mi>R</mi></math>, if the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>,</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>20</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>178</mn></math>, then the square of the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Mean of observation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>,</p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>20</mn></mfrac><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>15</mn><mo>&#215;</mo><mn>20</mn><mo>=</mo><mn>300</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also variance is given as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>20</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>20</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>20</mn></mfrac><mo>-</mo><msup><mfenced><mn>15</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mi>ii</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>234</mn><mo>&#215;</mo><mn>20</mn><mo>=</mo><mn>4680</mn></math></p><p>Given mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>,</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>20</mn></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>178</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup></mrow><mn>20</mn></mfrac><mo>=</mo><mn>178</mn><mo>&#8658;</mo><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mi>&#945;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>3560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><mi>&#945;</mi><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mo>&#8721;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>3560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4680</mn><mo>+</mo><mn>600</mn><mi>&#945;</mi><mo>+</mo><mn>20</mn><msup><mi>&#945;</mi><mn>2</mn></msup><mo>=</mo><mn>3560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>+</mo><mn>30</mn><mi>&#945;</mi><mo>+</mo><mn>56</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>28</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo>-</mo><mn>28</mn></math></p><p>Square of maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p></blockquote>

</details>

---

### Q46. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> observations were calculated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> respectively by a student who took by mistake <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> instead of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> for one observation. Then, the correct standard deviation is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>10</mn></math> and mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>10</mn></mfrac><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>25</mn><mo>=</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>125</mn></math></p><p>Now new sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>15</mn><mo>=</mo><mn>140</mn></math></p><p>So, actual mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>140</mn><mn>10</mn></mfrac><mo>=</mo><mn>14</mn><mo>=</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mrow><mi>new</mi><mo>&#160;</mo></mrow></msub></math></p><p>Now finding variance </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>2400</mn></math></p><p>Removing observation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><mn>625</mn><mo>=</mo><mn>2400</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>1775</mn></math></p><p>Now adding observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><msup><mn>15</mn><mn>2</mn></msup><mo>=</mo><mn>2000</mn><mo>=</mo><msub><mfenced><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow></mfenced><mrow><mi>actual</mi><mo>&#160;</mo></mrow></msub></math></p><p>Now calculating actual standard deviation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mrow><mi>actual</mi><mo>&#160;</mo></mrow><mn>2</mn></msubsup><mo>=</mo><mfrac><msub><mfenced><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow></mfenced><mrow><mi>actual</mi><mo>&#160;</mo></mrow></msub><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mrow><mi>new</mi><mo>&#160;</mo></mrow></msub></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2000</mn><mn>10</mn></mfrac><mo>-</mo><msup><mn>14</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>200</mn><mo>-</mo><mn>196</mn><mo>=</mo><mn>4</mn></math></p><p>Calculating standard deviation, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mfenced><mrow><mi>S</mi><mo>.</mo><mi>D</mi></mrow></mfenced><mrow><mi>actual</mi><mo>&#160;</mo></mrow></msub><mo>=</mo><msqrt><mn>4</mn></msqrt><mo>=</mo><mn>2</mn></math></p></blockquote>

</details>

---

### Q47. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

The mean and standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> respectively. It was noticed that two of these observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> were wrongly recorded. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi></math> is the standard deviation of the data after omitting the two wrong observations from the data, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>38</mn><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **238**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Wrong mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>&#956;</mi><mn>1</mn></msub><mo>=</mo><mn>30</mn></math></p><p>Wrong standard deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>&#963;</mi><mn>1</mn></msub><mo>=</mo><mn>5</mn></math></p><p>Now mean ig given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>40</mn></mfrac><mo>=</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>1200</mn></math></p><p>Variance is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>40</mn></mfrac><mo>-</mo><msup><mn>30</mn><mn>2</mn></msup><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>925</mn><mo>&#215;</mo><mn>40</mn><mo>=</mo><mn>37000</mn></math></p><p>New sum of mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mo>&#39;</mo></msubsup><mo>=</mo><mn>1200</mn><mo>-</mo><mn>10</mn><mo>-</mo><mn>12</mn><mo>=</mo><mn>1178</mn></math></p><p>So, new mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msubsup><mi>&#956;</mi><mn>1</mn><mo>&#39;</mo></msubsup><mo>=</mo><mfrac><mn>1178</mn><mn>38</mn></mfrac><mo>=</mo><mn>31</mn></math></p><p>Now new variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>37000</mn><mo>-</mo><msup><mfenced><mn>10</mn></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mn>12</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>36756</mn></math></p><p>So, new S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mn>1</mn><mo>&#39;</mo></msubsup><mo>=</mo><msqrt><mfrac><mn>36756</mn><mn>38</mn></mfrac><mo>-</mo><msup><mfenced><mn>31</mn></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mi>&#963;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36756</mn><mo>-</mo><msup><mfenced><mn>31</mn></mfenced><mn>2</mn></msup><mo>&#215;</mo><mn>38</mn><mo>=</mo><mn>38</mn><msup><mi>&#963;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>38</mn><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>238</mn></math></p></blockquote>

</details>

---

### Q48. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean deviation about median for the number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>2</mn><mi>k</mi><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mn>16</mn><mo>,</mo><mn>21</mn><mo>,</mo><mn>24</mn></math> arranged in the ascending order, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> then the median is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.</mo><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<blockquote><p>Median is the central value (or middle observation) of statistical data if it is arranged in ascending or descending order.</p><p>Thus, if there are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> observations (variates) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mi>n</mi></msub></math> arranged in ascending or descending order, then</p><p>median <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mi>th</mi></msup></math> observation, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is odd</p><p>and median <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfrac><mi>n</mi><mn>2</mn></mfrac><mtext>&#160;th observation&#160;</mtext><mo>+</mo><mfenced><mrow><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mtext>&#160;th observation&#160;</mtext></mrow><mn>2</mn></mfrac></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is even.</p><p>Here we can see there are even number of terms,</p><p>So, median <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi><mo>+</mo><mn>12</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mi>k</mi><mo>+</mo><mn>6</mn></math></p><p>Mean deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#8721;</mo><mfrac><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>M</mi></mrow></mfenced><mi>n</mi></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>6</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>6</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>10</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>15</mn><mo>-</mo><mi>k</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>18</mn><mo>-</mo><mi>k</mi></mrow></mfenced></mrow><mn>8</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>58</mn><mo>-</mo><mn>2</mn><mi>k</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>5</mn></math></p><p>So, median <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>12</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>11</mn></math></p></blockquote>

</details>

---

### Q49. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The number of values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#8712;</mo><mi>N</mi></math> such that the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mn>43</mn><mo>-</mo><mi>a</mi></math> is a natural number is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** infinite

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>**

**Detailed Solution:**

<p>Calculating Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>12</mn><mo>+</mo><mi>a</mi><mo>+</mo><mn>43</mn><mo>-</mo><mi>a</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mn>13</mn></math></p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mn>49</mn><mo>+</mo><mn>144</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>43</mn><mo>-</mo><mi>a</mi></mrow></mfenced><msup><mrow></mrow><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mn>13</mn><mn>2</mn></msup><mo>&#8712;</mo><mi>N</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mi>n</mi></math> (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>5</mn><mi>n</mi><mo>=</mo><mn>0</mn></math> must have solution as natural numbers</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><mn>40</mn><mi>n</mi><mo>-</mo><mn>7</mn></math> always has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> at unit place for any value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>D</mi></math> can&#39;t be perfect square</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> can&#39;t be integer.</p>

</details>

---

### Q50. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let the mean and the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><msub><mi>x</mi><mn>5</mn></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>24</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>194</mn><mn>25</mn></mfrac></math> respectively. If the mean and variance of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> observation are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><mi>a</mi><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub></mrow></mfenced></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>24</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>24</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>24</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>194</mn><mn>25</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msubsup><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi><mn>2</mn></msubsup><mo>=</mo><mn>154</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Also given mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub></mrow><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>2</mn></mfrac><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>5</mn></msub><mo>=</mo><mn>10</mn></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>)</p><p>and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>4</mn><mn>2</mn></msubsup></mrow><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>49</mn><mn>4</mn></mfrac><mo>=</mo><mi>a</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>4</mn><mn>2</mn></msubsup><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>49</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>5</mn><mn>2</mn></msubsup><mo>=</mo><mn>154</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>-</mo><mn>49</mn></math> (from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>100</mn><mo>=</mo><mn>105</mn><mo>-</mo><mn>4</mn><mi>a</mi><mo>&#8658;</mo><mn>4</mn><mi>a</mi><mo>=</mo><mn>5</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>a</mi><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub><mo>=</mo><mn>15</mn></math></p>

</details>

---

### Q51. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Suppose a class has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> students. The average marks of these students in the mathematics examination is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>62</mn></math>, and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>. A student fails in the examination if he/she gets less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> marks, then in worst case, the number of students can fail is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<p>Applying the formula of variance we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></msubsup><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mn>7</mn></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>140</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>49</mn></math> (taking the least possibility)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mn>49</mn><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>169</mn></math></p><p>then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="|" close="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced open="|" close="|"><mrow><msub><mi>x</mi><mn>7</mn></msub><mo>-</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>140</mn><mo>-</mo><mn>169</mn><mo>=</mo><mo>-</mo><mn>29</mn></math> Negative Number which is not possible, therefore, no student can fail.</p>

</details>

---

### Q52. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The mean and standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> observations are found to be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> respectively. On rechecking it was found that, in the observations, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> was misread as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>. Then, the correct variance is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<p>Old mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mn>14</mn></msub><mo>+</mo><mn>5</mn></mrow><mn>15</mn></mfrac><mo>=</mo><mn>8</mn></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mn>14</mn></msub><mo>=</mo><mn>115</mn></math></p><p>Correct mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mn>14</mn></msub><mo>+</mo><mn>20</mn></mrow><mn>15</mn></mfrac><mo>=</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mi>new</mi></msub><mo>&#8658;</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mi>new</mi></msub><mo>=</mo><mn>9</mn></math></p><p>Given, old variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>&#8658;</mo><mfrac><mrow><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>x</mi><mn>2</mn></msub><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><msub><mi>x</mi><mn>14</mn></msub><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup></mrow><mn>15</mn></mfrac><mo>-</mo><msup><mn>8</mn><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#8658;</mo><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>x</mi><mn>2</mn></msub><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><msub><mi>x</mi><mn>14</mn></msub><mn>2</mn></msup><mo>=</mo><mn>1070</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>var</mi><mi>new</mi></msub><mo>=</mo><mfrac><mrow><msup><msub><mi>x</mi><mn>1</mn></msub><mn>2</mn></msup><mo>+</mo><msup><msub><mi>x</mi><mn>2</mn></msub><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><msub><mi>x</mi><mn>14</mn></msub><mn>2</mn></msup><mo>+</mo><msup><mn>20</mn><mn>2</mn></msup></mrow><mn>15</mn></mfrac><mo>-</mo><msup><mn>9</mn><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>1070</mn><mo>+</mo><mn>400</mn></mrow><mn>15</mn></mfrac><mo>-</mo><mn>81</mn><mo>=</mo><mn>17</mn></math></p>

</details>

---

### Q53. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>8</mn><mo>,</mo><mi>x</mi><mo>,</mo><mi>y</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#60;</mo><mi>y</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math> respectively. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>320</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>420</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>162</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>674</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>320</mn></math>**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>8</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>9</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>-</mo><msup><mfenced><mn>6</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>80</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>On solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>12</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>144</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>=</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>24</mn><mi>x</mi><mo>+</mo><mn>64</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>x</mi><mo>+</mo><mn>32</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math>  or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>8</mn></math> and when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mn>4</mn><mn>4</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>=</mo><mn>256</mn><mo>+</mo><mn>64</mn><mo>=</mo><mn>320</mn></math></p><p>(or) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><msup><mn>8</mn><mn>4</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>=</mo><mn>4096</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>4112</mn></math></p>

</details>

---

### Q54. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> and the standard deviation is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>. However, one observation was wrongly recorded. The sum of the correct and incorrect observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>70</mn></math>. If the mean of the correct set of observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>, then the variance of the correct set is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>**

**Detailed Solution:**

<p>By using the formula of mean we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>50</mn></mfrac><mo>=</mo><mn>15</mn><mo>&#8658;</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>750</mn></math></p><p>Now variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>50</mn></mfrac><mo>-</mo><msup><mn>15</mn><mn>2</mn></msup><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#8658;</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>11450</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mfenced><mi>new</mi></mfenced></munder><mo>=</mo><mn>50</mn><mo>&#215;</mo><mn>16</mn><mo>=</mo><mn>800</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mfenced><mi>new</mi></mfenced></munder><mo>-</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>800</mn><mo>-</mo><mn>750</mn><mo>=</mo><mn>50</mn></math></p><p>Hence, if wrong observation was <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> then corrected one is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mn>50</mn></math>.
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mn>70</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>10</mn></math></p><p>Therefore, the correct observation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mrow><mo>&#8721;</mo><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup></mrow><mfenced><mi>new</mi></mfenced></munder><mo>=</mo><mn>11450</mn><mo>-</mo><msup><mfenced><mn>10</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>60</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>14950</mn></math></p><p>Therefore, variance of the correct set <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>14950</mn><mn>50</mn></mfrac><mo>-</mo><msup><mfenced><mn>16</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>299</mn><mo>-</mo><mn>256</mn><mo>=</mo><mn>43</mn></math>.</p>

</details>

---

### Q55. JEE Main 2022 (26 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean of the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mn>8</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>10</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>8</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is the mean deviation of the numbers about the mean, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mi>M</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>75</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn></math>**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mn>6</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>10</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mn>6</mn></math> (given) </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mn>6</mn><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>.</mo><mn>8</mn></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>25</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>on solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>4</mn></math></p><p>Now, Mean deviation about Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><mfenced close="|" open="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mover><mi>x</mi><mo>&#175;</mo></mover></mrow></mfenced></mrow><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced close="|" open="|"><mrow><mn>3</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>4</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>8</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>5</mn><mo>-</mo><mn>6</mn></mrow></mfenced><mo>+</mo><mfenced close="|" open="|"><mrow><mn>10</mn><mo>-</mo><mn>6</mn></mrow></mfenced></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>M</mi><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mn>25</mn><mi>M</mi><mo>=</mo><mn>60</mn></math>.</p>

</details>

---

### Q56. JEE Main 2022 (25 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

If the mean deviation about the mean of the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mi>n</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is odd, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>5</mn><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mi>n</mi></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p>We know that mean deviation about the mean of odd natural number is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>M.D&#160;</mtext><mfenced><menclose notation="top"><mi>x</mi></menclose></mfenced><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced open="[" close="]"><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></mfenced></math></p><p>So, now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac><mfenced close="]" open="["><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>5</mn><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mi>n</mi></mfrac></math> (given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>20</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>21</mn></math></p>

</details>

---

### Q57. JEE Main 2021 (31 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math> respetively. If two observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>,</mo></math> then the variance of the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> observations is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>92</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>134</mn><mn>5</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>112</mn><mn>5</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>536</mn><mn>25</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>536</mn><mn>25</mn></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>,</mo><mo>&#160;</mo><mi>e</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> unknown observations.</p><p>Given that No. of observation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>7</mn><mo>,</mo></math> Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn><mo>,</mo></math> Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> sum of observations  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>No</mi><mo>.&#160;</mo><mi>of</mi><mo>&#160;</mo><mi>observation</mi><mo>&#160;</mo><mo>&#215;</mo><mi>Mean</mi><mo>=</mo><mn>7</mn><mo>&#215;</mo><mn>8</mn><mo>=</mo><mn>56</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> Mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> remaining observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>56</mn><mo>-</mo><mn>8</mn><mo>-</mo><mn>6</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>42</mn><mn>5</mn></mfrac></math></p><p>As, we know that,</p><p>Variance for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observations<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>16</mn><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>7</mn></mfrac><mo>-</mo><mn>64</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>+</mo><mn>64</mn><mo>+</mo><mn>36</mn><mo>=</mo><mn>560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mo>+</mo><msup><mi>e</mi><mn>2</mn></msup><mo>=</mo><mn>460</mn></math></p><p>Variance of remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>460</mn><mn>5</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>42</mn><mn>5</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>536</mn><mn>25</mn></mfrac></math></p>

</details>

---

### Q58. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `2`

An online exam is attempted by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> candidates out of which <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> are boys. The average marks obtained by boys is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math> with a variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo></math> The variance of marks obtained by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> girls is also <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo></math> The average marks of all <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> candidates is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> is the average marks of girls and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> is the variance of marks of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> candidates, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>+</mo><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **25**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> Boys, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math> Girls
<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mi>B</mi><mn>2</mn></msubsup><mo>=</mo><mn>2</mn><mo>,</mo><msub><mover accent="true"><mi>X</mi><mo stretchy="false">&#175;</mo></mover><mi>B</mi></msub><mo>=</mo><mn>12</mn><mspace width="1em"/><msubsup><mi>&#963;</mi><mi>G</mi><mn>2</mn></msubsup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover accent="true"><mi>X</mi><mo stretchy="false">&#175;</mo></mover><mi>G</mi></msub><mo>=</mo><mfrac><mrow><mn>50</mn><mo>&#215;</mo><mn>15</mn><mo>&#8722;</mo><mn>20</mn><mo>&#215;</mo><mn>12</mn></mrow><mn>30</mn></mfrac><mo>=</mo><mfrac><mn>510</mn><mn>30</mn></mfrac><mo>=</mo><mn>17</mn><mo>=</mo><mi>&#956;</mi></math>
Variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> condidates
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>20</mn><msubsup><mi>&#963;</mi><mi>B</mi><mn>2</mn></msubsup><mo>+</mo><mn>30</mn><msubsup><mi>&#963;</mi><mi>G</mi><mn>2</mn></msubsup></mrow><mrow><mn>20</mn><mo>+</mo><mn>30</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>20</mn><mo>&#8901;</mo><mn>30</mn></mrow><mrow><mo>(</mo><mn>20</mn><mo>+</mo><mn>30</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><msup><mfenced separators="|"><mrow><msub><mover accent="true"><mi>X</mi><mo stretchy="false">&#175;</mo></mover><mi>B</mi></msub><mo>&#8722;</mo><msub><mover accent="true"><mi>X</mi><mo stretchy="false">&#175;</mo></mover><mi>G</mi></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>30</mn><mo>&#215;</mo><mn>2</mn></mrow><mn>50</mn></mfrac><mo>+</mo><mfrac><mn>600</mn><mn>2500</mn></mfrac><mo>(</mo><mn>25</mn><mo>)</mo><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>+</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>17</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>25</mn></math></p>

</details>

---

### Q59. JEE Main 2021 (27 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> be an odd natural number such that the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn><mo>.</mo></math> Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p>Variance of n natural number is given by,</p><p>Variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mi>n</mi><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><mi>n</mi></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mi>n</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p>                  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>12</mn></mfrac><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac></math></p><p>And it is given that Variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>12</mn></mfrac><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>168</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q60. JEE Main 2021 (26 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

Let the mean and variance of four numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>&#160;</mo><mo>(</mo><mi>x</mi><mo>&#62;</mo><mi>y</mi><mo>)</mo></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> respectively. Then the mean of four numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>,</mo><mo>&#160;</mo><mn>7</mn><mo>+</mo><mn>2</mn><mi>y</mi><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>-</mo><mi>y</mi></math> is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>,</mo></math> Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>4</mn></mfrac><mo>=</mo><mn>5</mn><mo>,</mo><mn>10</mn><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>4</mn></mfrac><mo>-</mo><msup><mfenced><mrow><mo>&#8721;</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>20</mn><mo>,</mo><mo>&#160;&#160;</mo><mn>10</mn><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>4</mn></mfrac><mo>-</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>10</mn><mo>-</mo><mi>x</mi><mo>,</mo><mo>&#160;&#160;</mo><mn>40</mn><mo>=</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn><mo>=</mo><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn><mo>=</mo><mn>9</mn><mo>+</mo><mn>49</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>140</mn><mo>=</mo><mn>58</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>82</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mo>-</mo><mn>82</mn><mo>=</mo><mn>2</mn><mi>x</mi><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mo>=</mo><mn>2</mn><mi>x</mi><mi>y</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi><mo>=</mo><mn>9</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mrow><mn>10</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>9</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>9</mn><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>9</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>9</mn><mo>,</mo><mn>1</mn></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#62;</mo><mi>y</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>y</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>7</mn><mo>+</mo><mn>2</mn><mi>y</mi><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>x</mi><mo>-</mo><mi>y</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>10</mn><mo>+</mo><mn>4</mn><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>24</mn><mn>2</mn></mfrac><mo>=</mo><mn>12</mn></math></p>

</details>

---

### Q61. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> observations were calculated as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>5</mn></math> respectively. It was found that by mistake one data value was taken as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math> instead of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>&#946;</mi></msqrt></math> are the mean and standard deviation respectively for correct data, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>10</mn><mo>.</mo><mn>5</mn><mo>,</mo><mn>26</mn><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>10</mn><mo>.</mo><mn>5</mn><mo>,</mo><mn>25</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>11</mn><mo>,</mo><mn>25</mn><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>11</mn><mo>,</mo><mn>26</mn><mo>)</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>10</mn><mo>.</mo><mn>5</mn><mo>,</mo><mn>26</mn><mo>)</mo></math>**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>19</mn></msub><mo>+</mo><mn>25</mn></mrow><mn>20</mn></mfrac><mo>=</mo><mn>10</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi mathvariant="normal">x</mi><mn>19</mn></msub><mo>+</mo><mn>25</mn><mo>=</mo><mn>200</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>19</mn></msub><mo>=</mo><mn>175</mn></math></p><p>New mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>x</mi><mn>19</mn></msub><mo>+</mo><mn>35</mn></mrow><mn>20</mn></mfrac><mo>=</mo><mfrac><mrow><mn>175</mn><mo>+</mo><mn>35</mn></mrow><mn>20</mn></mfrac><mo>=</mo><mn>10</mn><mo>.</mo><mn>5</mn></math></p><p>S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>19</mn><mn>2</mn></msubsup><mo>+</mo><mo>(</mo><mn>25</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>20</mn></mfrac><mo>-</mo><mo>(</mo><mn>10</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>.</mo><mn>5</mn><mo>=</mo><msqrt><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>19</mn><mn>2</mn></msubsup><mo>+</mo><mo>(</mo><mn>25</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>20</mn></mfrac><mo>-</mo><mo>(</mo><mn>10</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi mathvariant="normal">x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi mathvariant="normal">x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi mathvariant="normal">x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi mathvariant="normal">x</mi><mn>19</mn><mn>2</mn></msubsup><mo>=</mo><mn>1500</mn></math></p><p>New <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.&#160;</mo><mo>=</mo><msqrt><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mi>x</mi><mn>19</mn><mn>2</mn></msubsup><mo>+</mo><mo>(</mo><mn>35</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>20</mn></mfrac><mo>-</mo><mo>(</mo><mn>10</mn><mo>.</mo><mn>5</mn><msup><mo>)</mo><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><mn>1500</mn><mo>+</mo><mo>(</mo><mn>35</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mn>20</mn></mfrac><mo>-</mo><mo>(</mo><mn>110</mn><mo>.</mo><mn>25</mn><mo>)</mo></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mn>26</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi><mo>)</mo><mo>=</mo><mo>(</mo><mn>10</mn><mo>.</mo><mn>5</mn><mo>,</mo><mn>26</mn><mo>)</mo></math></p>

</details>

---

### Q62. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let the mean and variance of the frequency distribution</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>4</mn></msub><mo>=</mo><mn>9</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math></td>		</tr>	</tbody></table><p>be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>8</mn></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub></math> is changed from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>,</mo></math> then the mean for the new data will be:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p>Given</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>2</mn></msub><mo>=</mo><mn>6</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>3</mn></msub><mo>=</mo><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>4</mn></msub><mo>=</mo><mn>9</mn></math></td>			<td style="text-align: center;">Total</td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>x</mi><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#946;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>+</mo><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msup><mfenced><mrow><mi>x</mi><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced><mn>2</mn></msup><mo>:</mo></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>&#945;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>&#946;</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi></math></td>		</tr>	</tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>4</mn></munderover></mstyle><msub><mi>f</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub></mrow><mrow><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>4</mn></munderover><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mo>+</mo><mn>8</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>=</mo><mfenced><mrow><mn>8</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>&#215;</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>&#945;</mi><mo>+</mo><mn>3</mn><mi>&#946;</mi><mo>=</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also, for the variance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mstyle displaystyle="true"><munderover><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced><mn>2</mn></msup><mo>&#160;</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow><mrow><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow></munderover></mstyle><munderover><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><mo>&#160;</mo></mrow><mrow><mi>i</mi><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow><mrow><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></mrow></munderover></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><mo>+</mo><mn>4</mn><mi>&#945;</mi><mo>+</mo><mn>9</mn><mi>&#946;</mi><mo>=</mo><mfenced><mrow><mn>8</mn><mo>+</mo><mi>&#945;</mi><mo>+</mo><mi>&#946;</mi></mrow></mfenced><mo>&#215;</mo><mn>6</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>640</mn><mo>+</mo><mn>40</mn><mi>&#945;</mi><mo>+</mo><mn>90</mn><mi>&#946;</mi><mo>=</mo><mn>544</mn><mo>+</mo><mn>68</mn><mi>&#945;</mi><mo>+</mo><mn>68</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>28</mn><mi>&#945;</mi><mo>-</mo><mn>22</mn><mi>&#946;</mi><mo>=</mo><mn>96</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mi>&#945;</mi><mo>-</mo><mn>11</mn><mi>&#946;</mi><mo>=</mo><mn>48</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#38;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>5</mn><mo>&#38;</mo><mi>&#946;</mi><mo>=</mo><mn>2</mn></math></p><p>so, new mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>32</mn><mo>+</mo><mn>35</mn><mo>+</mo><mn>18</mn></mrow><mn>15</mn></mfrac><mo>=</mo><mfrac><mn>85</mn><mn>15</mn></mfrac><mo>=</mo><mfrac><mn>17</mn><mn>3</mn></mfrac></math></p>

</details>

---

### Q63. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and variance of the following data: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>13</mn><mo>,</mo><mi>a</mi><mo>,</mo><mn>12</mn><mo>,</mo><mi>b</mi><mo>,</mo><mn>12</mn></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mn>4</mn></mfrac></math> respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>**

**Detailed Solution:**

<p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>13</mn><mo>+</mo><mi mathvariant="normal">a</mi><mo>+</mo><mn>12</mn><mo>+</mo><mi mathvariant="normal">b</mi><mo>+</mo><mn>12</mn></mrow><mn>8</mn></mfrac><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>60</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>72</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>12</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>37</mn><mn>4</mn></mfrac></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>13</mn><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mn>12</mn><mn>2</mn></msup><mo>+</mo><msup><mn>12</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>642</mn></math></p><p>So, variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>642</mn></mrow><mn>8</mn></mfrac><mo>-</mo><msup><mfenced><mn>9</mn></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>37</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>321</mn><mn>4</mn></mfrac><mo>-</mo><mn>81</mn><mo>=</mo><mfrac><mn>37</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>=</mo><mn>81</mn><mo>+</mo><mfrac><mn>37</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>321</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>=</mo><mn>81</mn><mo>-</mo><mn>71</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>80</mn></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>80</mn><mo>+</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>144</mn><mo>&#160;&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>64</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>80</mn><mo>-</mo><mn>64</mn><mo>=</mo><mn>16</mn><mo>.</mo></math></p>

</details>

---

### Q64. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The first of the two samples in a group has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> items with mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> and standard deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo></math> If the whole group has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math> items with mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>.</mo><mn>6</mn></math> and standard deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>13</mn><mo>.</mo><mn>44</mn></msqrt><mo>,</mo></math> then the standard deviation of the second sample is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>**

**Detailed Solution:**

<p>We have, number of terms in the first group <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>100</mn></math> with their mean <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><menclose notation="top"><mi>X</mi></menclose><mn>1</mn></msub><mo>=</mo><mn>15</mn></math> and number of terms in whole group is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>250</mn></math> and their mean <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>X</mi></menclose><mo>=</mo><mn>15</mn><mo>.</mo><mn>6</mn><mo>.</mo></math></p><p>Variance of first group<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>V</mi><mn>1</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>9</mn></math> and whole group is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>Var</mo><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>13</mn><mo>.</mo><mn>44</mn><mo>.</mo></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><msubsup><mi>&#963;</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><msub><mi>n</mi><mn>2</mn></msub></mrow><msup><mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></mfrac><msup><mfenced><mrow><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>-</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mn>150</mn><mo>,</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>16</mn><mo>,</mo><msub><mi>V</mi><mn>2</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>&#963;</mi><mn>2</mn></msub></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>.</mo><mn>44</mn><mo>=</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>150</mn><mo>&#215;</mo><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mn>250</mn></mfrac><mo>+</mo><mfrac><mrow><mn>100</mn><mo>&#215;</mo><mn>150</mn></mrow><msup><mfenced><mn>250</mn></mfenced><mn>2</mn></msup></mfrac><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#963;</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q65. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the mean and variance of six observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mi>a</mi><mo>,</mo><mi>b</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>3</mn></mfrac><mo>,</mo></math> respectively, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>a</mi><mo>-</mo><mi>b</mi><mo>|</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Given:</p><p>Mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>7</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>15</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>17</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>And,</p><p>Variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>20</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>10</mn><mn>2</mn></msup><mo>+</mo><msup><mn>11</mn><mn>2</mn></msup><mo>+</mo><msup><mn>15</mn><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>-</mo><msup><mn>10</mn><mn>2</mn></msup><mo>=</mo><mfrac><mn>20</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>495</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup></mrow><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>320</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>495</mn><mo>+</mo><msup><mi mathvariant="normal">a</mi><mn>2</mn></msup><mo>+</mo><msup><mi mathvariant="normal">b</mi><mn>2</mn></msup><mo>=</mo><mn>640</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>145</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Solve <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>8</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfenced open="|" close="|"><mrow><mi>a</mi><mo>-</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q66. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> distinct observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>.</mo><mn>5</mn></math> and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>25</mn><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> out of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn><mo>,</mo></math> then the remaining two observations are:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>18</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mn>8</mn><mo>,</mo><mn>13</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>11</mn></math>**

**Detailed Solution:**

Let the other two observations be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, then<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>7</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>6</mn><mo>.</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>21</mn><mo>-</mo><mi>a</mi></math></p><p>Then, other two numbers are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>21</mn><mo>-</mo><mi>a</mi></mrow></mfenced></math></p><p>Now, variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>25</mn></math>, therefore</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>.</mo><mn>25</mn><mo>=</mo><mfrac><mfenced><mrow><mn>4</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>25</mn><mo>+</mo><mn>49</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>21</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup></mrow></mfenced><mn>6</mn></mfrac><mo>-</mo><msup><mfenced><mrow><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mfenced><mrow><mn>10</mn><mo>.</mo><mn>25</mn></mrow></mfenced><mo>+</mo><mn>6</mn><msup><mfenced><mrow><mn>6</mn><mo>.</mo><mn>5</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>94</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>21</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>21</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>221</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>21</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>21</mn><mo>-</mo><mn>10</mn><mo>=</mo><mn>11</mn></math></p><p>So, remaining two observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo><mn>11</mn></math>.</p>

</details>

---

### Q67. JEE Main 2021 (18 Mar Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let in a series of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> observations, half of them are equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and remaining half are equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>a</mi></math>. Also by adding a constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> in each of these observations, the mean and standard deviation of new set become <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>, respectively. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>425</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>650</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>925</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>425</mn></math>**

**Detailed Solution:**

<p>Let observations are denoted by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>i</mi></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#60;</mo><mn>2</mn><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>a</mi><mo>+</mo><mi>a</mi><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>a</mi><mo>)</mo><mo>-</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>a</mi><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>a</mi><mo>)</mo></mrow><mrow><mn>2</mn><mi>n</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mn>0</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>&#963;</mi><mi>x</mi><mn>2</mn></msubsup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn><mi>n</mi></mrow></mfrac><mo>-</mo><mn>0</mn><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>&#963;</mi><mi mathvariant="normal">x</mi></msub><mo>=</mo><mi mathvariant="normal">a</mi></math></p><p>Now, adding a constant <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>y</mi><mo>&#175;</mo></mover><mo>=</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>+</mo><mi>b</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>=</mo><mn>5</mn></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>&#963;</mi><mi>y</mi></msub><mo>=</mo><msub><mi>&#963;</mi><mi>x</mi></msub></math> (No change in S.D.)  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>425</mn></math></p>

</details>

---

### Q68. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Consider a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>n</mi></math> numbers having variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo></math> In this set, the mean of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and the mean of the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>.</mo></math> A new set is constructed by adding <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> into each of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> numbers, and subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> from each of the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> numbers. If the variance of the new set is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>k</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **68**

**Detailed Solution:**

<p>Let, the number be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>3</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mi>n</mi></msub><mo>.</mo></math></p><p>Given, the mean of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi></math> numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and that of the remaining <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo></math> then by using the formula for combined mean, we get, the mean of the complete set as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mo>&#215;</mo><mn>6</mn><mo>+</mo><mi>n</mi><mo>&#215;</mo><mn>3</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mi>n</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn><mi>n</mi></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>=</mo><mn>5</mn><mo>.</mo></math></p><p>Also, the variance is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mi>&#956;</mi></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><msup><mfenced><msub><mi>b</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>-</mo><mo>(</mo><mn>5</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><msup><mfenced><msub><mi>b</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>=</mo><mn>29</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#8721;</mo><msup><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><msup><mfenced><msub><mi>b</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>87</mn><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Now, as per the given information, the distribution becomes</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mn>1</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mrow><mn>2</mn><mi mathvariant="normal">n</mi></mrow></msub><mo>+</mo><mn>1</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>1</mn></msub><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>-</mo><mn>1</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>b</mi><mi mathvariant="normal">n</mi></msub><mo>-</mo><mn>1</mn></math></p><p>Thus, the new variance is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><mo>(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><mo>(</mo><msub><mi>b</mi><mi>i</mi></msub><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mfenced><mrow><mn>12</mn><mi>n</mi><mo>+</mo><mn>2</mn><mi>n</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mi>n</mi><mo>-</mo><mi>n</mi></mrow></mfenced></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>&#8721;</mo><msub><mi>a</mi><mi>i</mi></msub></mrow></mfenced><mo>+</mo><mfenced><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>b</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>&#8721;</mo><msub><mi>b</mi><mi>i</mi></msub></mrow></mfenced></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>16</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><msub><mi>a</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8721;</mo><msup><mfenced><msub><mi>b</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>&#8721;</mo><msub><mi>a</mi><mi>i</mi></msub><mo>-</mo><mn>2</mn><mo>&#8721;</mo><msub><mi>b</mi><mi>i</mi></msub></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>16</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p>On putting the given values and value from the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>87</mn><mi>n</mi><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn><mo>(</mo><mn>12</mn><mi>n</mi><mo>)</mo><mo>-</mo><mn>2</mn><mo>(</mo><mn>3</mn><mi>n</mi><mo>)</mo></mrow><mrow><mn>3</mn><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>16</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>108</mn><mn>3</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>16</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>k</mi><mo>=</mo><mn>3</mn><mo>(</mo><mn>108</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>16</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>k</mi><mo>=</mo><mn>324</mn><mo>-</mo><mn>256</mn><mo>=</mo><mn>68</mn><mo>.</mo></math></p>

</details>

---

### Q69. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Consider the statistics of two sets of observations as follows:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td> </td>			<td>Size</td>			<td>Mean</td>			<td>Variance</td>		</tr>		<tr>			<td>Observation I</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>		</tr>		<tr>			<td>Observation II</td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>		</tr>	</tbody></table><p>If the variance of the combined set of these two observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>9</mn></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to ________.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><msubsup><mi>&#963;</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup></mrow><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><msub><mi>n</mi><mn>2</mn></msub></mrow><mfenced><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub></mrow></mfenced></mfrac><msup><mfenced><mrow><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>-</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>1</mn></msub><mo>=</mo><mn>10</mn><mo>,</mo><msub><mi>n</mi><mn>2</mn></msub><mo>=</mo><mi>n</mi><mo>,</mo><msubsup><mi>&#963;</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mn>2</mn><mo>,</mo><msubsup><mi>&#963;</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mn>2</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>17</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>17</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mi>n</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>10</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>10</mn><mi>n</mi></mrow><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>10</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><msup><mfenced><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>17</mn><mn>9</mn></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>20</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>10</mn><mo>)</mo><mo>+</mo><mn>10</mn><mi>n</mi></mrow><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>10</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>17</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1700</mn><mo>+</mo><mn>340</mn><mi>n</mi><mo>=</mo><mn>90</mn><mi>n</mi><mo>+</mo><mn>9</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>30</mn><mi>n</mi><mo>+</mo><mn>200</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>n</mi><mo>-</mo><mn>100</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>25</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mstyle displaystyle="true"><munder><mn>2</mn><munder><mo>&#8595;</mo><mfenced><mi>Rejected</mi></mfenced></munder></munder></mstyle></mfrac><mo>,</mo><mn>5</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q70. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Consider three observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math>. If the standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>c</mi><mo>+</mo><mn>2</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>, then which of the following is true?

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>d</mi><mn>2</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></math></p><p>mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><mn>3</mn></mfrac><mfenced><mrow><mo>=</mo><mover><mi>x</mi><mo>&#175;</mo></mover></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mi>a</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn><mi>b</mi></mrow><mn>3</mn></mfrac></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>b</mi><mo>+</mo><mn>2</mn><mo>,</mo><mi>c</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi></mrow></mfenced><mo>=</mo><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>4</mn><msup><mi>b</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>3</mn><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>9</mn><msup><mi>d</mi><mn>2</mn></msup></math></p>

</details>

---

### Q71. JEE Main 2021 (26 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>X</mi><mn>1</mn></msub><mo>,</mo><msub><mi>X</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>X</mi><mn>18</mn></msub></math> be eighteen observations such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><mfenced><mrow><msub><mi>X</mi><mi>i</mi></msub><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>36</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><msup><mfenced><mrow><msub><mi>X</mi><mi>i</mi></msub><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>90</mn></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are distinct real numbers. If the standard deviation of these observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math> is _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>&#945;</mi></mrow></mfenced><mo>=</mo><mn>36</mn><mo>,</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>18</mn><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>,</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><mn>2</mn><mi>&#946;</mi><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>18</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>18</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>90</mn></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>90</mn><mo>-</mo><mn>18</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>&#946;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>18</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>18</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>90</mn><mo>-</mo><mn>18</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>36</mn><mi>&#946;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>-</mo><mn>18</mn><msup><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>&#945;</mi><mi>&#946;</mi><mo>+</mo><mn>4</mn><mi>&#946;</mi><mo>-</mo><msup><mi>&#945;</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>&#945;</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>4</mn><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> are distinct <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>|</mo><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q72. JEE Main 2021 (24 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

If the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> natural numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi></math> is less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>,</mo></math> then the maximum possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msup><mi>x</mi><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mi>&#931;</mi><mi>x</mi></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup></mrow><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mn>9</mn><mo>+</mo><mi>k</mi></mrow><mn>10</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#60;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn><mo>+</mo><mn>10</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>81</mn><mo>-</mo><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>k</mi><mo>&#60;</mo><mn>1000</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>18</mn><mi>k</mi><mo>-</mo><mn>991</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>k</mi><mo>&#60;</mo><mfrac><mn>991</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#60;</mo><mfrac><mn>1000</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mn>10</mn><msqrt><mn>10</mn></msqrt></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mi>k</mi><mo>-</mo><mn>1</mn><mo>&#60;</mo><mfrac><mrow><mn>10</mn><msqrt><mn>10</mn></msqrt></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#60;</mo><mfrac><mrow><mn>10</mn><msqrt><mn>10</mn></msqrt></mrow><mn>3</mn></mfrac><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8804;</mo><mn>11</mn></math></p><p>Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>.</mo></math></p>

</details>

---

### Q73. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo largeop="true">&#931;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mi>n</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo largeop="true">&#931;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mi>n</mi><mi>a</mi><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math>, then the standard deviation of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mi>n</mi></msub></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><msqrt><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mi>n</mi><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mo>(</mo><mi>a</mi><mo>-</mo><mn>1</mn><mo>)</mo></msqrt></math>**

**Detailed Solution:**

<p>SD, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mo>=</mo><msqrt><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p>SD is independent of change of origin, so, for given data
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mo>=</mo><msqrt><mfrac><mrow><mi>&#931;</mi><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi></mrow></mfenced><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mi>&#931;</mi><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi></mrow></mfenced></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></msqrt></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><mi>n</mi><mi>a</mi></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mi>n</mi><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mi>a</mi><mo>-</mo><mn>1</mn></msqrt></math></p>

</details>

---

### Q74. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and the standard deviation of the data <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are the roots of the equation:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>18</mn><mo>=</mo><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>19</mn><mo>=</mo><mn>0</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>19</mn><mo>=</mo><mn>0</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>20</mn><mi>x</mi><mo>+</mo><mn>18</mn><mo>=</mo><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>19</mn><mo>=</mo><mn>0</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>25</mn><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>10</mn></math>
S.D. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mrow><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></msqrt><mo>=</mo><mn>2</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>83</mn></mrow><mn>5</mn></mfrac><mo>-</mo><mn>25</mn><mo>=</mo><mn>4</mn><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>62</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>62</mn><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>19</mn></math>
so equation whose roots are a and b is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>10</mn><mi>x</mi><mo>+</mo><mn>19</mn><mo>=</mo><mn>0</mn></math>

</details>

---

### Q75. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>, respectively. If five observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>14</mn></math> then the absolute difference of the remaining two observations is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

Assume, the two remaining observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>14</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>42</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>56</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>14</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>&#931;</mi><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mi>&#931;</mi><msub><mi>x</mi><mn>1</mn></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>100</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>196</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>7</mn></mfrac><mo>-</mo><msup><mfenced><mn>8</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>16</mn><mo>+</mo><mn>64</mn><mo>=</mo><mfrac><mrow><mn>460</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>560</mn><mo>=</mo><mn>460</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>100</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>48</mn></math>, solving equations <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced open="|" close="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q76. JEE Main 2020 (04 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>If the variance of the following frequency distribution:</p><p>Class:         <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mn>20</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>20</mn><mo>-</mo><mn>30</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>30</mn><mo>-</mo><mn>40</mn></math>
Frequency:   <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>x</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn></math>
is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is equal to _______ </p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given data can also be expressed as:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnlines="solid" frame="solid" rowlines="solid"><mtr><mtd><msub><mi>x</mi><mi>i</mi></msub></mtd><mtd><mn>15</mn></mtd><mtd><mn>25</mn></mtd><mtd><mn>35</mn></mtd></mtr><mtr><mtd><msub><mi>f</mi><mi>i</mi></msub></mtd><mtd><mn>2</mn></mtd><mtd><mi>x</mi></mtd><mtd><mn>2</mn></mtd></mtr></mtable></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mstyle displaystyle="true"><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub></mstyle><mstyle displaystyle="true"><mi>&#931;</mi><msub><mi>f</mi><mi>i</mi></msub></mstyle></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mn>30</mn><mo>+</mo><mn>25</mn><mi>x</mi><mo>+</mo><mn>70</mn></mstyle><mstyle displaystyle="true"><mn>4</mn><mo>+</mo><mi>x</mi></mstyle></mfrac><mo>=</mo><mfrac><mrow><mn>25</mn><mfenced><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mn>25</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>50</mn><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>f</mi><mi>i</mi></msub><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mrow><mi>&#931;</mi><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>=</mo><mfrac><mrow><mn>450</mn><mo>+</mo><mn>625</mn><mi>x</mi><mo>+</mo><mn>2450</mn></mrow><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>-</mo><msup><mn>25</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>50</mn><mo>=</mo><mfrac><mrow><mn>2900</mn><mo>+</mo><mn>625</mn><mi>x</mi></mrow><mrow><mn>4</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mn>625</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>675</mn><mo>(</mo><mn>4</mn><mo>+</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>2900</mn><mo>+</mo><mn>625</mn><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>50</mn><mi>x</mi><mo>=</mo><mn>200</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q77. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math> observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>.</mo><mn>5</mn><mo>,</mo></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> of these observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>14</mn><mo>,</mo><mn>15</mn><mo>,</mo></math> then the absolute difference of the remaining two observations is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Let remaining two observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mi>&#931;</mi><msub><mi>x</mi><mi>i</mi></msub></mstyle><mi>n</mi></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>14</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mn>8</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn><mo>+</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo mathvariant="italic">=</mo><mn>80</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mstyle displaystyle="true"><mi>&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mstyle><mi>n</mi></mfrac><mo>&#8722;</mo><msup><mfenced><mfrac><mstyle displaystyle="true"><mi>&#931;</mi><msub><mi>x</mi><mi>i</mi></msub></mstyle><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>13</mn><mo>.5</mo><mo>=</mo><mfrac><mrow><mn>25</mn><mo>+</mo><mn>49</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>100</mn><mo>+</mo><mn>225</mn><mo>+</mo><mn>196</mn><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>8</mn></mfrac><mo>&#8722;</mo><mn>100</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>908</mn><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mn>739</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>=</mo><mn>169</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>&#8722;</mo><mn>2</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>169</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>289</mn><mo>&#8722;</mo><mn>169</mn><mo>=</mo><mn>2</mn><mi>a</mi><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>=</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="|" open="|"><mrow><mi>a</mi><mo>&#8722;</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>289</mn><mo>&#8722;</mo><mn>240</mn><mo>=</mo><mn>49</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>a</mi><mo>&#8722;</mo><mi>b</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math>.</p></blockquote>

</details>

---

### Q78. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">x</mi><mi mathvariant="normal">i</mi></msub><mfenced><mrow><mn>1</mn><mo>&#8804;</mo><mi mathvariant="normal">i</mi><mo>&#8804;</mo><mn>10</mn></mrow></mfenced></math> be ten observation of a random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msub><mi mathvariant="normal">x</mi><mi>i</mi></msub><mo>-</mo><mi mathvariant="normal">p</mi></mrow></mfenced><mo>=</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><msub><mi mathvariant="normal">x</mi><mi>i</mi></msub><mo>-</mo><mi mathvariant="normal">p</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8800;</mo><mi mathvariant="normal">p</mi><mo>&#8712;</mo><mi mathvariant="normal">R</mi></math>, then the standard deviation of these observations is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mfrac><mn>3</mn><mn>5</mn></mfrac></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>10</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>10</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>10</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Standard Deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>S</mi><mo>.</mo><mi>D</mi><mo>.</mo></mrow></mfenced><mo>=</mo><msqrt><mfrac><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>p</mi></mrow></mfenced><mn>2</mn></msup></mstyle><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover></mstyle><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>p</mi></mrow></mfenced></mrow><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msqrt><mfrac><mn>9</mn><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mn>3</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mfrac><mn>9</mn><mn>10</mn></mfrac></math></p></blockquote>

</details>

---

### Q79. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

For the frequency distribution: Variate <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>x</mi></mfenced><mo>:</mo><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>x</mi><mn>15</mn></msub></math>
Frequency <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>f</mi></mfenced><mo>:</mo><msub><mi>f</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>f</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>f</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>,</mo><msub><mi>f</mi><mn>15</mn></msub></math> 
where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#60;</mo><msub><mi>x</mi><mn>3</mn></msub><mo>&#60;</mo><mo>&#8230;</mo><mo>&#60;</mo><msub><mi>x</mi><mn>15</mn></msub><mo>=</mo><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>f</mi><mi>i</mi></msub><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> the standard deviation cannot be

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

We know <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>&#8804;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mfenced><mrow><mi>M</mi><mo>-</mo><mi>m</mi></mrow></mfenced><mn>2</mn></msup></math>.<p>Where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> is upper bound of value of any random variable and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is lower bound of any random variable,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>&#8804;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><msup><mfenced><mrow><mn>10</mn><mo>-</mo><mn>0</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>&#60;</mo><mn>25</mn></math>, (removed equality sign because <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#62;</mo><mn>0</mn></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>5</mn><mo>&#60;</mo><mi>&#963;</mi><mo>&#60;</mo><mn>5</mn></math></p><p>From given options <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mo>&#8800;</mo><mn>6</mn></math>.</p>

</details>

---

### Q80. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

If the variance of the terms in an increasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>1</mn></msub><msub><mi>b</mi><mn>2</mn></msub><mo>,</mo><msub><mi>b</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>b</mi><mn>11</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>90</mn></math> then the common difference of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3**

**Detailed Solution:**

<p>Given<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">b</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">b</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">b</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><msub><mi mathvariant="normal">b</mi><mn>11</mn></msub><mo>,</mo></math> are in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">A</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> Variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi mathvariant="normal">b</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">b</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><msub><mi mathvariant="normal">b</mi><mn>11</mn></msub></mrow></mfenced><mo>=</mo></math>Variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>0</mn><mo>,</mo><mi mathvariant="normal">d</mi><mo>,</mo><mn>2</mn><mi mathvariant="normal">d</mi><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mn>10</mn><mi mathvariant="normal">d</mi><mo>)</mo><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>11</mn></msubsup><msubsup><mi>b</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>11</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>11</mn></msubsup><msub><mi>b</mi><mi>i</mi></msub></mrow><mn>11</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><msup><mi>d</mi><mn>2</mn></msup><mn>11</mn></mfrac><mo>&#183;</mo><mfrac><mrow><mn>10</mn><mo>.</mo><mn>11</mn><mo>.</mo><mn>21</mn></mrow><mn>6</mn></mfrac><mo>-</mo><msup><mi>d</mi><mn>2</mn></msup><mo>&#183;</mo><mfrac><mn>55</mn><mn>11</mn></mfrac><mo>&#183;</mo><mfrac><mn>55</mn><mn>11</mn></mfrac><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>35</mn><msup><mi>d</mi><mn>2</mn></msup><mo>-</mo><mn>25</mn><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>90</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>d</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mo>&#177;</mo><mn>3</mn></math></p><p>It is an increasing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>d</mi></math> is positive.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>d</mi><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q81. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>x</mi><mo>&#8712;</mo><mi>N</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>1</mn><mo>&#8804;</mo><mi>x</mi><mo>&#8804;</mo><mn>17</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mi>X</mi><mo>&#160;</mo><mi>and</mi><mo>&#160;</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>&#8712;</mo><mi>R</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>. If mean and variance of elements of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>216</mn></math> respectively then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>27</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>7</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mo>=</mo><mi>a</mi><mover><mi>x</mi><mo>&#175;</mo></mover><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>17</mn></mrow></mfenced></mrow><mn>17</mn></mfrac><mo>+</mo><mi>b</mi><mo>=</mo><mn>17</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>a</mi><mfenced><mrow><mn>17</mn><mo>&#215;</mo><mn>18</mn></mrow></mfenced></mrow><mrow><mn>17</mn><mo>&#215;</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mi>b</mi><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mfenced><msup><mi>X</mi><mn>2</mn></msup></mfenced><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><mo>&#8721;</mo></mstyle><msup><mi>x</mi><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mstyle displaystyle="true"><mo>&#8721;</mo></mstyle><mi>x</mi></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>17</mn><mn>2</mn></msup></mrow><mn>17</mn></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>17</mn></mrow><mn>17</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>17</mn><mo>&#183;</mo><mn>18</mn><mo>&#183;</mo><mn>35</mn></mrow><mrow><mn>6</mn><mo>&#183;</mo><mn>17</mn></mrow></mfrac><mo>-</mo><msup><mfenced><mfrac><mrow><mn>17</mn><mo>&#183;</mo><mn>18</mn></mrow><mrow><mn>2</mn><mo>&#183;</mo><mn>17</mn></mrow></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>105</mn><mo>-</mo><mn>81</mn><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#963;</mi><mfenced><msup><mi>Y</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mi>&#963;</mi><mfenced><msup><mi>X</mi><mn>2</mn></msup></mfenced><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#183;</mo><mn>24</mn><mo>=</mo><mn>216</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>216</mn><mn>24</mn></mfrac><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>17</mn><mo>-</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>17</mn><mo>-</mo><mn>27</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>=</mo><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>7</mn></math></p>

</details>

---

### Q82. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the observation <math><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mfenced separators="|"><mrow><mn>1</mn><mo>&#8804;</mo><mi>i</mi><mo>&#8804;</mo><mn>10</mn></mrow></mfenced></math> satisfy the equations  <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>10</mn></math>, <math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>40</mn></mrow></mrow></math> . If <math><mi>&#956;</mi></math> and <math><mi>&#955;</mi></math> are the mean and the variance of the observations, <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>-</mo><mn>3</mn><mo>,</mo><mi></mi><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>-</mo><mn>3</mn><mo>,</mo><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>-</mo><mn>3</mn><mo>,</mo></math> then the ordered pair <math><mfenced separators="|"><mrow><mi>&#956;</mi><mo>,</mo><mi>&#955;</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mfenced separators="|"><mrow><mn>3,3</mn></mrow></mfenced></math>
- **(B)** <math><mfenced separators="|"><mrow><mn>6,3</mn></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mn>6,6</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>3,6</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfenced separators="|"><mrow><mn>3,3</mn></mrow></mfenced></math>**

**Detailed Solution:**

Mean <math><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mo stretchy="false">∑</mo><mrow><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow></mrow></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mn>1</mn></math> <math><mo>∴</mo><mfenced close="}" open="{" separators="|"><mrow><mi mathvariant="normal">M</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mi></mi><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mn>2</mn><mo>=</mo><mn>3</mn></math>  
<math><mi>μ</mi><mo>=</mo><mi>v</mi><mi>a</mi><mi>r</mi><mi></mi><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mrow><mo stretchy="false">∑</mo><mrow><msup><mrow><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></mrow><mrow><mn>10</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mrow><mo stretchy="false">∑</mo><mrow><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>-</mo><mn>5</mn></mrow></mfenced></mrow></mrow></mrow><mrow><mn>10</mn></mrow></mfrac><mo>=</mo><mn>3</mn></math>

</details>

---

### Q83. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of <math><mn>20</mn></math> observations are found to be <math><mn>10</mn></math> and <math><mn>4</mn><mo>,</mo><mi></mi></math> respectively. On rechecking, it was found that an observation <math><mn>9</mn></math> was incorrect and the correct observation was <math><mn>11,</mn></math> then the correct variance is

**Options:**

- **(A)** <math><mn>3.99</mn></math>
- **(B)** <math><mn>4.01</mn></math>
- **(C)** <math><mn>4.02</mn></math>
- **(D)** <math><mn>3.98</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>3.99</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>20</mn></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>20</mn></mfrac><mo>-</mo><mn>100</mn><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>104</mn><mo>&#215;</mo><mn>20</mn><mo>=</mo><mn>2080</mn></math>
Actual mean <math><mo>=</mo><mfrac><mrow><mn>200</mn><mo>-</mo><mn>9</mn><mo>+</mo><mn>11</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>202</mn></mrow><mrow><mn>20</mn></mrow></mfrac></math>
Variance <math><mo>=</mo><mfrac><mrow><mn>2080</mn><mo>-</mo><mn>81</mn><mo>+</mo><mn>121</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>202</mn></mrow><mrow><mn>20</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>
<math><mo>=</mo><mfrac><mrow><mn>2120</mn></mrow><mrow><mn>20</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>10.1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>106</mn><mo>-</mo><mn>102.01</mn><mo>=</mo><mn>3.99</mn></math>

</details>

---

### Q84. JEE Main 2020 (08 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and the standard deviation (s.d.) of <math><mn>10</mn></math> observations are <math><mn>20</mn></math> and <math><mn>2</mn></math> respectively. Each of these <math><mn>10</mn></math> observations is multiplied by <math><mi>p</mi></math> and then reduced by <math><mi>q</mi><mo>,</mo></math> where <math><mi>p</mi><mo>&#8800;</mo><mn>0</mn></math> and <math><mi>q</mi><mo>&#8800;</mo><mn>0</mn><mo>.</mo></math> If the new mean and new s.d. become half of their original values, then <math><mi>q</mi></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mn>5</mn></math>
- **(B)** <math><mn>10</mn></math>
- **(C)** <math><mo>-</mo><mn>20</mn></math>
- **(D)** <math><mo>-</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mo>-</mo><mn>20</mn></math>**

**Detailed Solution:**

If each observation is multiplied with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> &amp; then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> is subtracted, then
New mean <math><msub><mrow><mover accent="true"><mrow><mi>x</mi></mrow><mo>-</mo></mover></mrow><mrow><mn>1</mn></mrow></msub><mo>=</mo><mi>p</mi><mover accent="true"><mrow><mi>x</mi></mrow><mo>-</mo></mover><mo>-</mo><mi>q</mi></math>
<math><mo>&#8658;</mo><mo>&#8201;</mo><mn>10</mn><mo>=</mo><mi>p</mi><mfenced separators="|"><mrow><mn>20</mn></mrow></mfenced><mo>-</mo><mi>q</mi><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced separators="|"><mrow><mn>1</mn></mrow></mfenced></math>
and new standard deviation
<math><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>p</mi></mrow></mfenced><msub><mrow><mi>&#963;</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>&#8201;</mo><mo>&#8658;</mo><mo>&#8201;</mo><mn>1</mn><mo>=</mo><mfenced close="|" open="|" separators="|"><mrow><mi>p</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn></mrow></mfenced><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8658;</mo><mo>&#8201;</mo><mo>&#8201;</mo><mfenced close="|" open="|" separators="|"><mrow><mi>p</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#8201;</mo><mo>&#8201;</mo><mo>&#8658;</mo><mo>&#8201;</mo><mi>p</mi><mo>=</mo><mo>&#177;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
If <math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn></math>  (from equation (1))
If <math><mi>p</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
<math><mi>q</mi><mo>=</mo><mo>-</mo><mn>20</mn></math>

</details>

---

### Q85. JEE Main 2020 (07 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If the mean and variance of eight numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>20</mn><mo>,</mo><mi>x</mi></math> and <math><mi>y</mi></math> be <math><mn>10</mn></math> and <math><mn>25</mn></math> respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#183;</mo><mi>y</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **54**

**Detailed Solution:**

Mean <math><mo>=</mo><mover accent="true"><mrow><mi mathvariant="normal">x</mi></mrow><mo>-</mo></mover><mo>=</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>13</mn><mo>+</mo><mn>20</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>16</mn><mo>&#8230;</mo><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi></mrow></mfenced></math>
Variance <math><msup><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mfrac><mrow><mrow><mo stretchy="false">&#8721;</mo><mrow><msup><mrow><mfenced separators="|"><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mover accent="true"><mrow><mi mathvariant="normal">x</mi></mrow><mo>-</mo></mover></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>25</mn></math>
<math><mfrac><mrow><mn>9</mn><mo>+</mo><mn>49</mn><mo>+</mo><mn>81</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>169</mn><mo>+</mo><mn>400</mn><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>8</mn></mrow></mfrac><mo>-</mo><mn>100</mn><mo>=</mo><mn>25</mn></math>
<math><mo>&#8658;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mi>y</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>148</mn><mo>&#8230;</mo><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">i</mi></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mfenced separators="|"><mn>16</mn></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>256</mn><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>54</mn></math>

</details>

---

### Q86. JEE Main 2020 (07 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If the variance of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> natural numbers is <math><mn>10</mn></math> and the variance of the first <math><mi>m</mi></math> even natural numbers is <math><mn>16</mn><mo>,</mo><mi></mi></math> then the value of  <math><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **18**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>var</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mfrac><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>10</mn></math></p><p><math><mo>&#8658;</mo><mfrac><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>10</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>120</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>var</mi><mfenced separators="|"><mrow><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>6</mn><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mn>2</mn><mi>m</mi></mrow></mfenced><mo>=</mo><mn>16</mn><mo>&#8658;</mo><mi>var</mi><mfenced separators="|"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mi>m</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn><mo>=</mo><mn>48</mn><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>18</mn></math></p>

</details>

---

### Q87. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the data <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mo>&#8230;</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>10</mn></mrow></msub></math> is such that the mean of first four of these is <math><mn>11</mn><mo>,</mo></math> the mean of the remaining six is <math><mn>16</mn></math> and the sum of squares of all of these is <math><mn>2000</mn></math>, then the standard deviation of this data is:

**Options:**

- **(A)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>2</mn></math>
- **(D)** <math><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>2</mn></math>**

**Detailed Solution:**

Let the numbers are <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mo>&#8230;</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>10</mn></mrow></msub><mfenced separators="|"><mrow><mi>N</mi><mo>=</mo><mn>10</mn></mrow></mfenced></math>
Given <math><mfenced close="}" open="" separators="|"><mrow><mtable><mtr><mtd><mrow><maligngroup></maligngroup><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>4.11</mn><mo>=</mo><mn>44</mn></mrow></mtd></mtr><mtr><mtd><mrow><maligngroup></maligngroup><msub><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msub><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>10</mn></mrow></msub><mo>=</mo><mn>6.16</mn><mo>=</mo><mn>96</mn></mrow></mtd></mtr></mtable></mrow></mfenced><mo>&#8658;</mo><mrow><mo stretchy="false">&#8721;</mo><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>=</mo><mn>140</mn></mrow></mrow></math>
<math><mo>&#8658;</mo><mi>&#160;</mi></math> variance <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>N</mi></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>N</mi></mfrac></mfenced><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>2000</mn><mn>10</mn></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mn>140</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>200</mn><mo>-</mo><mn>196</mn><mo>=</mo><mn>4</mn></math>
<math><mo>&#8658;</mo><mi>&#160;</mi></math> Standard deviation <math><mi>&#963;</mi><mo>=</mo><mn>2</mn><mo>.</mo></math>

</details>

---

### Q88. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If both the mean and the standard deviation of <math><mn>50</mn></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi mathvariant="normal">&#160;</mi><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>&#8230;</mo><mo>,</mo><mi mathvariant="normal">&#160;</mi><msub><mi>x</mi><mn>50</mn></msub></math> are equal to <math><mn>16</mn></math>, then the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mi mathvariant="normal">&#160;</mi><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mi mathvariant="normal">&#160;</mi><mo>&#8230;</mo><mo>,</mo><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mn>50</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></math> is

**Options:**

- **(A)** <math><mn>525</mn></math>
- **(B)** <math><mn>480</mn></math>
- **(C)** <math><mn>400</mn></math>
- **(D)** <math><mn>380</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>400</mn></math>**

**Detailed Solution:**

<p>For observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#8201;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mn>50</mn></msub></math></p><p>We have, mean, <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mi>&#160;</mi></msubsup></mrow><mn>50</mn></mfrac><mo>=</mo><mn>16</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>And, standard deviation, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#963;</mi><mo>=</mo><msqrt><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>50</mn></mfrac><mo>-</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>50</mn></mfrac><mo>=</mo><msup><mn>16</mn><mn>2</mn></msup><mo>+</mo><msup><mfenced><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>50</mn></mfrac><mo>=</mo><msup><mn>16</mn><mn>2</mn></msup><mo>+</mo><msup><mn>16</mn><mn>2</mn></msup><mo>=</mo><mn>512</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, the mean value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#8201;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#8201;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msup><mfenced><mrow><msub><mi>x</mi><mn>50</mn></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></math> will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>4</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>50</mn></mfrac><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><mn>8</mn><mo>&#160;</mo><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>16</mn><mo>&#215;</mo><mn>50</mn></mrow><mn>50</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>50</mn></mfrac><mo>-</mo><mn>8</mn><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mn>50</mn></mfrac><mo>+</mo><mn>16</mn></math></p><p> Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>512</mn><mo>-</mo><mn>8</mn><mo>&#215;</mo><mn>16</mn><mo>+</mo><mn>16</mn><mo>=</mo><mn>400</mn><mo>.</mo></math></p>

</details>

---

### Q89. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the standard deviation of the numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1,</mn><mo>&#160;</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>k</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>5</mn></msqrt></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> then <math><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math><msqrt><mn>6</mn></msqrt></math>
- **(B)** <math><mn>4</mn><msqrt><mfrac><mrow><mn>5</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>
- **(C)** <math><mn>2</mn><msqrt><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac></msqrt></math>
- **(D)** <math><mn>2</mn><msqrt><mn>6</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>2</mn><msqrt><mn>6</mn></msqrt></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi><mo>.</mo><mo>=</mo><msqrt><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>n</mi></mfrac></mfenced><mn>2</mn></msup></msqrt><mo>=</mo><msqrt><mn>5</mn></msqrt></math></p><p><math><mo>&#8658;</mo><mfrac><mrow><mrow><mo stretchy="false">&#8721;</mo><mrow><msubsup><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow><mrow><mn>2</mn></mrow></msubsup></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mrow><mo stretchy="false">&#8721;</mo><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow></mrow></mrow><mrow><mi>n</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>5</mn></math></p><p><math><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>+</mo><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mi>k</mi></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>5</mn></math></p><p><math><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mo>+</mo><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>16</mn></mrow></mfrac><mo>=</mo><mn>5</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>8</mn><mo>+</mo><mn>4</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><msup><mi>k</mi><mn>2</mn></msup></mrow><mn>16</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><mo>+</mo><mn>3</mn><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>80</mn></math></p><p><math><mo>&#8658;</mo><mn>3</mn><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>72</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>&#8658;</mo><mi>k</mi></mrow><mn>2</mn></msup><mo>=</mo><mn>24</mn><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>&#177;</mo><mn>2</mn><msqrt><mn>6</mn></msqrt></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>2</mn><msqrt><mn>6</mn></msqrt><mo>.</mo></math></p>

</details>

---

### Q90. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A student scores the following marks in five tests: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45,54,41,57,43</mn></math>. His score is not known for the sixth test. If the mean score is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math> in the six tests, then the standard deviation of the marks in six tests is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><mn>3</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>100</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><msqrt><mn>3</mn></msqrt></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>100</mn><msqrt><mn>3</mn></msqrt></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>10</mn><msqrt><mn>3</mn></msqrt></mfrac></math>**

**Detailed Solution:**

Given mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>41</mn><mo>+</mo><mn>45</mn><mo>+</mo><mn>54</mn><mo>+</mo><mn>57</mn><mo>+</mo><mn>43</mn><mo>+</mo><mi>x</mi></mrow><mn>6</mn></mfrac><mo>=</mo><mn>48</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>48</mn></math>
Now variance <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced><mn>2</mn></msup></mrow><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><msup><mn>9</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mn>0</mn><mn>2</mn></msup></mrow><mn>6</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>100</mn><mn>3</mn></mfrac></math>
Hence standard deviation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>10</mn><msqrt><mn>3</mn></msqrt></mfrac></math>.</p>

</details>

---

### Q91. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance for seven observations are <math><mn>8</mn></math> and <math><mn>16</mn></math> respectively. If <math><mn>5</mn></math> of the observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>12</mn><mo>,</mo><mn>14</mn><mo>,</mo></math> then the product of the remaining two observations is

**Options:**

- **(A)** <math><mn>48</mn></math>
- **(B)** <math><mn>45</mn></math>
- **(C)** <math><mn>49</mn></math>
- **(D)** <math><mn>40</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>48</mn></math>**

**Detailed Solution:**

<blockquote><p>Let the remaining two observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math><mi>y</mi></math>.</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mover accent="false"><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>N</mi></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>14</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mfrac><mrow><mn>42</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>14</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math>
Variance, </p><p>    <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>N</mi></mfrac><mo>-</mo><msup><mfenced><mover accent="false"><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>4</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>100</mn><mo>+</mo><mn>144</mn><mo>+</mo><mn>196</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>7</mn></mfrac><mo>-</mo><mn>64</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>460</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>7</mn></mfrac><mo>-</mo><mn>64</mn><mo>=</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>100</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get,</p><p><math><mi>x</mi><mo>=</mo><mn>6</mn><mo>,</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>8</mn></math> and <math><mi>x</mi><mi>y</mi><mo>=</mo><mn>48</mn></math></p></blockquote>

</details>

---

### Q92. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The mean and the variance of five observations are <math><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5.20</mn></math>, respectively. If three of the observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>; then the absolute value of the difference of the other two observations, is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math><mn>5</mn></math>
- **(C)** <math><mn>7</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>7</mn></math>**

**Detailed Solution:**

<p>Let rest two observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>.</p><p>Given mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mn>4</mn><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Given variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mo>.</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>9</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>16</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced separators="|"><mn>4</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mo>.</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>=</mo><mn>65</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Squaring equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>81</mn><mo>-</mo><mn>65</mn><mo>&#8658;</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>16</mn><mo>&#8658;</mo><mi>x</mi><mi>y</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>=</mo><mn>65</mn><mo>-</mo><mn>16</mn><mo>=</mo><mn>49</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfenced close="|" open="|" separators="|"><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q93. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The outcome of each of 30 items was observed; 10 items

gave an outcome $\frac{1}{2}-\mathrm{d}$ each, 10 items gave outcome $\frac{1}{2}$

each and the remaining 10 items gave outcome $\frac{1}{2}+\mathrm{d}$ each.

If the variance of this outcome data is $\frac{4}{3}$ then $|\mathrm{d}|$ equals:

**Options:**

- **(A)** $\frac{2}{3}$
- **(B)** 2
- **(C)** $\frac{\sqrt{5}}{2}$
- **(D)** $\sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\sqrt{2}$**

**Detailed Solution:**

Outcomes are $\left(\frac{1}{2}-d\right),\left(\frac{1}{2}-d\right), 0 \ldots, 10$ times, $\frac{1}{2}, \frac{1}{2}$,

$\ldots, 10$ times, $\frac{1}{2}+d, \frac{1}{2}+d, \ldots, 10$ times

$$

\text { Mean }=\frac{1}{30}\left(\frac{1}{2} \times 30\right)=\frac{1}{2}

$$

Variance of the outcomes is,

$$

\begin{aligned}

\sigma^{2} &=\frac{1}{30} \Sigma x_{i}^{2}-(\bar{x})^{2} \\

&=\frac{1}{30}\left[\left(\frac{1}{2}-d\right)^{2} \times 10+\left(\frac{1}{2}\right)^{2} \times 10+\left(\frac{1}{2}+d\right)^{2} \times 10\right]-\frac{1}{4} \\

\Rightarrow & \frac{4}{3}=\frac{1}{30}\left[30 \times \frac{1}{4}+20 d^{2}\right]-\frac{1}{4} \\

\Rightarrow & \frac{4}{3}=\frac{1}{4}+\frac{2}{3} d^{2}-\frac{1}{4} \\

\Rightarrow & d^{2}=2 \Rightarrow|d|=\sqrt{2}

\end{aligned}

$$

</details>

---

### Q94. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and standard deviation of <math><mn>5</mn></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>x</mi><mn>4</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>x</mi><mn>5</mn></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math><mn>3</mn><mo>,</mo></math> respectively, then the variance of <math><mn>6</mn></math> observations <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><mo>&#8230;</mo><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msub></math> and <math><mo>-</mo><mn>50</mn></math> is equal to

**Options:**

- **(A)** <math><mn>582.5</mn></math>
- **(B)** <math><mn>507.5</mn></math>
- **(C)** <math><mn>509.5</mn></math>
- **(D)** <math><mn>586.5</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>507.5</mn></math>**

**Detailed Solution:**

<blockquote><p>We have,</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub></mrow><mn>5</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub><mo>=</mo><mn>50</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced><mo>&#160;</mo></math>

Variance</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mi mathvariant="normal">S</mi><mo>.</mo><mi mathvariant="normal">D</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi mathvariant="normal">&#931;</mi><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>5</mn></mfrac><mo>-</mo><msup><mfenced separators="|"><mover><mi>x</mi><mo>&#175;</mo></mover></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math> 

<math><mo>&#8658;</mo><mfrac><mrow><msubsup><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><mn>100</mn><mo>=</mo><mn>9</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>4</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>5</mn><mn>2</mn></msubsup><mo>=</mo><mn>545</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced><mo>&#160;</mo></math>

Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">w</mi></mrow></msub><mo>=</mo><mfrac><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>+</mo><msub><mi>x</mi><mn>2</mn></msub><mo>+</mo><msub><mi>x</mi><mn>3</mn></msub><mo>+</mo><msub><mi>x</mi><mn>4</mn></msub><mo>+</mo><msub><mi>x</mi><mn>5</mn></msub><mo>-</mo><mn>50</mn></mrow><mn>6</mn></mfrac><mo>=</mo><mn>0</mn></math> 

New variance</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>6</mn></munderover></mstyle><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mn>6</mn></mfrac><mo>-</mo><msup><mfenced separators="|"><msub><mover><mi>x</mi><mo>&#175;</mo></mover><mrow><mi mathvariant="normal">n</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">w</mi></mrow></msub></mfenced><mn>2</mn></msup><mo>&#160;</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msubsup><mi>x</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>2</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>3</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>4</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>x</mi><mn>5</mn><mn>2</mn></msubsup><mo>+</mo><mn>2500</mn></mrow><mn>6</mn></mfrac><mo>-</mo><mn>0</mn></math>

<math><mo>=</mo><mfrac><mrow><mn>545</mn><mo>+</mo><mn>2500</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3045</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mn>507.5</mn></math></p></blockquote>

</details>

---

### Q95. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The mean of five observations is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and their variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9.20</mn><mo>.</mo></math> If three of the given five observations are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1,</mn><mo>&#160;</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>,</mo></math> then a ratio of other two observations is

**Options:**

- **(A)** <math><mn>10</mn><mo>:</mo><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>9</mn></math>
- **(C)** <math><mn>6</mn><mo>:</mo><mn>7</mn></math>
- **(D)** <math><mn>5</mn><mo>:</mo><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>:</mo><mn>9</mn></math>**

**Detailed Solution:**

<blockquote><p>Let, the two unknown terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>y</mi><mo>.</mo></math></p><p>The mean is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>N</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>8</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>25</mn><mo>=</mo><mn>12</mn><mo>+</mo><mi>x</mi><mo>+</mo><mi>y</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>=</mo><mn>13</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And, the variance is defined as <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>&#956;</mi></mrow></mfenced><mn>2</mn></msup></mrow><mi>N</mi></mfrac><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow><mi>N</mi></mfrac><mo>-</mo><msup><mi>&#956;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9.2</mn><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>64</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><mn>5</mn></mfrac><mo>-</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>34.2</mn><mo>&#215;</mo><mn>5</mn><mo>=</mo><mn>74</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>171</mn><mo>=</mo><mn>74</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>97</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and put in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math> to get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>97</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>13</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>97</mn><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>169</mn><mo>-</mo><mn>26</mn><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>26</mn><mi>x</mi><mo>+</mo><mn>72</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>x</mi><mo>+</mo><mn>36</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>9</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>9</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>4</mn></math> respectively.</p><p>Hence, the ratio of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mi>y</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>9</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>4</mn><mo>.</mo></math></p></blockquote>

</details>

---

### Q96. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A data consists of <math><mi>n</mi></math> observations: <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi>&#160;</mi><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>,</mo><mi>&#160;</mi><msub><mi>x</mi><mi>n</mi></msub><mo>.</mo></math> If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>n</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mi>n</mi></math>, then the standard deviation of this data is

**Options:**

- **(A)** <math><mn>5</mn></math>
- **(B)** <math><msqrt><mn>7</mn></msqrt></math>
- **(C)** <math><msqrt><mn>5</mn></msqrt></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><msqrt><mn>5</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced separators="|"><mrow><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>9</mn><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced separators="|"><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>5</mn><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced separators="|"><mrow><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><mn>2</mn><msub><mi>x</mi><mi>i</mi></msub><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>5</mn><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math> </p><p>Form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>+</mo><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced><mrow><mn>2</mn><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>+</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>14</mn><mi>n</mi></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>=</mo><mn>6</mn><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced><mo>&#160;</mo></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>-</mo><mfenced><mn>2</mn></mfenced></math>, we get </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mi>n</mi><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p><math><mo>&#8756;</mo></math> Variance, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mi>E</mi><mfenced separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mo>-</mo><msup><mfenced separators="|"><mrow><mi>E</mi><mfenced separators="|"><mi>x</mi></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mi>n</mi></mfrac><mo>-</mo><mfrac><mrow><mo>&#8721;</mo><mi>x</mi></mrow><mi>n</mi></mfrac><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>6</mn><mi>n</mi></mrow><mi>n</mi></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mi>n</mi><mi>n</mi></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mn>6</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>5</mn></math></p><p><math><mo>&#8756;</mo></math> Standard deviation, <math><mi>&#963;</mi><mo>=</mo><msqrt><mn>5</mn></msqrt></math>.</p></blockquote>

</details>

---

### Q97. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math><mn>5</mn></math> students of a class have an average height <math><mn>150</mn><mi>&#160;</mi><mi>c</mi><mi>m</mi></math> and variance <math><mn>18</mn><mi>&#160;</mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>.</mo></math> A new student, whose height is <math><mn>156</mn><mi>&#160;</mi><mi>c</mi><mi>m</mi><mo>,</mo></math> joined them. The variance <math><mfenced separators="|"><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">&#160;</mi><mi>c</mi><msup><mrow><mi>m</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math> of the height of these six students is:

**Options:**

- **(A)** <math><mn>22</mn></math>
- **(B)** <math><mn>16</mn></math>
- **(C)** <math><mn>18</mn></math>
- **(D)** <math><mn>20</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>20</mn></math>**

**Detailed Solution:**

Let  <math><msup><mrow><mn>1</mn></mrow><mrow><mi>s</mi><mi>t</mi></mrow></msup><mtext> </mtext><mn>5</mn></math>  students are   

 <math><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mtext> </mtext><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mtext> </mtext><msub><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msub><mtext> </mtext><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msub></math>  and  <math><msub><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msub></math> 

         <math><mo>∴</mo><mn>18</mn><mo>=</mo><mi>E</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mi>E</mi><mfenced separators="|"><mrow><mi>x</mi></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> 

         <math><mo>=</mo><mfrac><mrow><msubsup><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></msubsup></mrow><mrow><mn>5</mn></mrow></mfrac><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mn>150</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> 

         <math><mo>⇒</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>112590</mn></math> 

         <math><mo>∴</mo></math>  new variance <math><mi> </mi><mo>=</mo><mfrac><mrow><msubsup><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msubsup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msup><mrow><mn>156</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><msup><mrow><mo>(</mo><mn>151</mn><mo>)</mo></mrow><mrow><mn>2</mn></mrow></msup></math>           <math><mfenced close="]" open="[" separators="|"><mrow><mi mathvariant="normal">S</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">c</mi><mi mathvariant="normal">e</mi><mtext> </mtext><mi mathvariant="normal">n</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">w</mi><mtext> </mtext><mi mathvariant="normal">m</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi><mo>=</mo><mfrac><mrow><mn>150</mn><mo>×</mo><mn>5</mn><mo>+</mo><mn>156</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mn>151</mn></mrow></mfenced></math> 

         <math><mo>=</mo><mfrac><mrow><mn>112590</mn><mo>+</mo><mn>24336</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mn>22801</mn></math> 

         <math><mo>=</mo><mn>20</mn></math>

</details>

---

### Q98. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> observations and the sum of their squares are  <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>2475</mn></math>, respectively. Later on, three observations <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math> were found to be incorrect. If the incorrect observations are omitted, then the variance of the remaining observations is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>25</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>50</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.</mo><mn>00</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>.</mo><mn>00</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>.</mo><mn>00</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>400</mn></math> and

<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup><mo>=</mo><mn>2475</mn></math>

Variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>97</mn></math> observations<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mo>&#8721;</mo><msup><msub><mi>x</mi><mi>i</mi></msub><mn>2</mn></msup></mrow><mi>N</mi></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mrow><mo>&#8721;</mo><msub><mi>x</mi><mi>i</mi></msub></mrow><mi>N</mi></mfrac></mfenced><mn>2</mn></msup><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8756;</mo><mo>&#160;</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>=</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>=</mo><mn>50</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2425</mn><mn>97</mn></mfrac><mo>-</mo><msup><mfenced separators="|"><mfrac><mn>388</mn><mn>97</mn></mfrac></mfenced><mn>2</mn></msup></math>

<math><mo>=</mo><mfrac><mrow><mn>2425</mn></mrow><mrow><mn>97</mn></mrow></mfrac><mo>-</mo><mn>16</mn></math>

<math><mo>=</mo><mfrac><mrow><mn>2425</mn><mo>-</mo><mn>1552</mn></mrow><mrow><mn>97</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>873</mn></mrow><mrow><mn>97</mn></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q99. JEE Main 2017 (02 Apr)

*Type:* `singleCorrect` | *Level:* `1`

A box contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> green and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> yellow balls. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> balls are randomly drawn, one-by-one, with replacement, then the variance of the number of green balls drawn is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>
- **(B)** <math><mn>6</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mfrac><mrow><mn>6</mn></mrow><mrow><mn>25</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>For Bernoulli&#39;s trials</p><p>Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>.</mo><mi>p</mi><mo>.</mo><mi>q</mi></math>

Given, number of trials <math><mi>n</mi><mo>=</mo><mn>10</mn></math>

Probability of drawing a green ball <math><mi>p</mi><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>25</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math> and <math><mi>q</mi><mo>=</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

Hence, Variance <math><mo>=</mo><mn>10</mn><mo>&#215;</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math></p>

</details>

---

### Q100. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> be respectively the mean, mode and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> observations <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>...</mo><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mi>n</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mi>i</mi></msub><mo>=</mo><mo>-</mo><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>.</mo><mo>...</mo><mo>,</mo><mo>&#160;</mo><mi>n</mi><mi>,</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is any number.</p><p><strong>Statement I:</strong> Variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mi>n</mi></msub></math> is <math> <mrow> <msup> <mi>&#963;</mi> <mn>2</mn> </msup> </mrow> </math>.</p><p><strong>Statement II:</strong> Mean and mode of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mi>n</mi></msub></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mover><mi>x</mi><mo>&#175;</mo></mover><mo>-</mo><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>M</mi><mo>-</mo><mi>a</mi></math>, respectively.</p>

**Options:**

- **(A)** <strong>Statement <span style="font-size: 10pt; line-height: 115%; font-family: Arial, sans-serif; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">I</span></strong> and <strong>Statement <span style="font-size: 10pt; line-height: 115%; font-family: Arial, sans-serif; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">II</span></strong> are both true
- **(B)** <strong>Statement </strong><span style="font-family: Arial, sans-serif; font-size: 13.3333px;"><strong>I</strong> and <strong>Statement II</strong> are both false </span>
- **(C)** <strong>Statement </strong><span style="font-family: Arial, sans-serif; font-size: 13.3333px;"><strong>I</strong> is true and <strong>Statement </strong></span><span style="font-family: Arial, sans-serif; font-size: 13.3333px;"><strong>II</strong> is false</span>
- **(D)** <strong>Statement </strong><span style="font-family: Arial, sans-serif; font-size: 13.3333px;"><strong>I</strong> is false and <strong>Statement II</strong> is true</span>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <strong>Statement <span style="font-size: 10pt; line-height: 115%; font-family: Arial, sans-serif; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">I</span></strong> and <strong>Statement <span style="font-size: 10pt; line-height: 115%; font-family: Arial, sans-serif; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">II</span></strong> are both true**

**Detailed Solution:**

<p>Mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mi>&#160;</mi><msub><mi>d</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mstyle displaystyle="false"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mfenced separators="|"><mrow><mi>&#160;</mi><mfrac><mrow><mi>&#160;</mi><mo>-</mo><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>a</mi><mi>&#160;</mi></mrow><mi>n</mi></mfrac><mi>&#160;</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mstyle displaystyle="false"><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mrow><mi>&#160;</mi><msub><mi>x</mi><mi>i</mi></msub><mi>&#160;</mi></mrow><mi>n</mi></mfrac><mo>+</mo><mfrac><mrow><mi>&#160;</mi><mo>-</mo><mi>a</mi><mi>&#160;</mi></mrow><mi>n</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mstyle displaystyle="false"><mo>-</mo><menclose notation="top"><mi>x</mi></menclose><mo>+</mo><mfrac><mrow><mi>&#160;</mi><mo>-</mo><mi>a</mi><mi>&#160;</mi></mrow><mi>n</mi></mfrac><mi>n</mi></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mover><mi>x</mi><mo>&#8594;</mo></mover><mo>-</mo><mi>a</mi></math></p><p>And, the mode of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>d</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>d</mi><mn>3</mn></msub><mo>.</mo><mo>.</mo><mo>.</mo><mi>&#160;</mi><msub><mi>d</mi><mi>n</mi></msub></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>M</mi><mo>-</mo><mi>a</mi></math></p><p>Also, we know that the variance <math><msup><mrow><mi>&#963;</mi></mrow><mrow><mn>2</mn></mrow></msup></math> is unaffected by change of origin, hence it remains same.</p>

</details>

---

### Q101. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `1`

The variance of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> even natural numbers is :

**Options:**

- **(A)** <math> <mrow> <mn>4</mn> <mn>3</mn> <mn>7</mn> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>4</mn> <mn>3</mn> <mn>7</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>8</mn> <mn>3</mn> <mn>3</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mn>8</mn> <mn>3</mn> <mn>3</mn> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math> <mrow> <mn>8</mn> <mn>3</mn> <mn>3</mn> </mrow> </math>**

**Detailed Solution:**

Variance of a set of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>x</mi><mn>2</mn></msub><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mi>i</mi></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><msub><mi>x</mi><mi>n</mi></msub></mrow></mfenced></math> is given

<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>&#931;</mo><mrow><mi>i</mi><mo>= 1</mo></mrow><mi>n</mi></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mover><mi>x</mi><mo>&#175;</mo></mover></mrow></mfenced><mn>2</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover></math> is the average of the numbers.

We want the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mn>48</mn><mo>,</mo><mo>&#160;</mo><mn>50</mn><mo>,</mo><mo>&#160;</mo><mn>52</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mn>98</mn><mo>,</mo><mo>&#160;</mo><mn>100</mn></mrow></mfenced></math>

Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mover><mi>x</mi><mo>&#175;</mo></mover><mo>=</mo><mi>51</mi></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mover><mi>x</mi><mo>&#175;</mo></mover></mrow></mfenced></math> will be symmetric about <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math>,

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">&#8756;</mi><mspace width="0.5em"/><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>2</mn><mi>50</mi></mfrac><mspace width="0.5em"/><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>..&#160;</mo><msup><mi>49</mi><mn>2</mn></msup></mrow></mfenced></math>

Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>49</mn><mn>2</mn></msup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>49</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>50</mn><mn>2</mn></msup></mrow></mfenced><mo>&#160;</mo><mo>-</mo><mfenced><mrow><mo>&#160;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>6</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>48</mn><mn>2</mn></msup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msup><mn>50</mn><mn>2</mn></msup></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mn>50</mn></mfenced><mfenced><mn>51</mn></mfenced><mfenced><mn>101</mn></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mn>4</mn><mfenced><mrow><msup><mi>1</mi><mn>2</mn></msup><mo>+</mo><msup><mi>2</mi><mn>2</mn></msup><mo>+</mo></mrow></mfenced><mspace linebreak="newline"/></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mfenced><mn>50</mn></mfenced><mfenced><mn>51</mn></mfenced><mfenced><mn>101</mn></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>4</mn><mfenced><mn>25</mn></mfenced><mfenced><mn>26</mn></mfenced><mfenced><mn>51</mn></mfenced></mrow><mn>6</mn></mfrac></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>42925</mn><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mn>22100</mn></math>

 <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mn>20825</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mspace width="0.5em"/><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>2</mn><mi>50</mi></mfrac><mo>&#215;</mo><mi>20825</mi><mo>=</mo><mi>833</mi></math>

</details>

---

### Q102. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

Statement 1: The variance of first $n$ odd natural numbers is $\frac{n^2-1}{3}$
Statement 2: The sum of first $\mathrm{n}$ odd natural number is $n^2$ and the sum of square of first $n$ odd natural numbers is $\frac{n\left(4 n^2+1\right)}{3}$.

**Options:**

- **(A)** Statement 1 is true, Statement 2 is false.
- **(B)** Statement 1 is true, Statement 2 is true; Statement 2 is not a correct explanation for Statement 1.
- **(C)** Statement 1 is false, Statement 2 is true.
- **(D)** Statement 1 is true, Statement 2 is true, Statement 2 is a correct explanation for Statement 1.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) Statement 1 is true, Statement 2 is false.**

**Detailed Solution:**

Statement 2 : Sum of first $n$ odd natural numbers is not equal to $n^2$.
So, statement - 2 is false.

</details>

---

### Q103. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{x}_1, \mathrm{x}_2, \ldots \ldots, \mathrm{x}_{\mathrm{n}}$ be $\mathrm{n}$ observations, and let $\overline{\mathrm{x}}$ be their arithematic mean and $\sigma^2$ be their variance. 
Statement $1$: Variance of $2 x_1, 2 x_2, \ldots \ldots, 2 x_n$ is $4 \sigma^2$.
Statement $2$: Arithmetic mean of $2 \mathrm{x}_1, 2 \mathrm{x}_2, \ldots . ., 2 \mathrm{x}_{\mathrm{n}}$ is $4 \overline{\mathrm{x}}$.

**Options:**

- **(A)** Statement $1$ is false, statement $2$ is true
- **(B)** Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$
- **(C)** Statement $1$ is true, statement $2$ is true; statement $2$ is not a correct explanation for statement $1$
- **(D)** Statement $1$ is true, statement $2$ is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement $1$ is true, statement $2$ is false**

**Detailed Solution:**

$\sigma^2=\sum \frac{x_i^2}{n}-\left(\sum \frac{x_i}{n}\right)^2$
Variance of $2 x_1, 2 x_2, \ldots . ., 2 x_n=\sum \frac{\left(2 x_i\right)^2}{n}-\left(\sum \frac{2 x_i}{n}\right)^2=4\left[\sum \frac{x_i^2}{n}-\left(\sum \frac{x_i}{n}\right)^2\right]=4 \sigma^2$ Statement $1$ is true.
A.M. of $2 x_1, 2 x_2, \ldots \ldots, 2 x_n=\frac{2 x_1+2 x_2+\cdots+2 x_n}{n}=2\left(\frac{x_1+x_2+\cdots+x_n}{n}\right)=2 \bar{x}$
Statement $2$ is false.

</details>

---

### Q104. JEE Main 2010

*Type:* `singleCorrect` | *Level:* `1`

For two data sets, each of size 5 , the variances are given to be 4 and 5 and the corresponding means are given to be 2 and 4 , respectively. The variance of the combined data set is

**Options:**

- **(A)** $\frac{11}{2}$
- **(B)** 6
- **(C)** $\frac{13}{2}$
- **(D)** $\frac{5}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{11}{2}$**

**Detailed Solution:**

$\sigma_x^2=4$
$\sigma_y^2=5$
$\bar{x}=2$
$\bar{y}=4$
$\begin{aligned} \frac{\sum x_i}{5} & =2 \\ \sigma_x^2 & =\left(\frac{1}{2} \sum x_i^2\right)-(\bar{x})^2=\frac{1}{5}\left(\sum y_i^2\right)-16 \\ \sum x_i^2 & =40 \\ \sum y_i^2 & =105 \\ \sigma_z^2 & =\frac{1}{10}\left(\sum x_i^2+\sum y_i^2\right)-\left(\frac{\bar{x}+\bar{y}}{2}\right)^2=\frac{1}{10}(40+105)-9=\frac{145-90}{10}=\frac{55}{10}=\frac{11}{2}\end{aligned}$

</details>

---

### Q105. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `1`

Statement-1 : The variance of first $n$ even natural numbers is $\frac{n^2-1}{4}$
Statement-2 : The sum of first $n$ natural numbers is $\frac{n(n+1)}{2}$ and the sum of squares of first $n$ natural numbers is $\frac{n(n+1)(2 n+1)}{6}$

**Options:**

- **(A)** Statement-1 is true, Statement-2 is true; Statement-2 is a correct explanation for Statement-1
- **(B)** Statement-1 is true, Statement-2 is true; Statement-2 is not a correct explanation for Statement-1
- **(C)** Statement-1 is true, Statement-2 is false
- **(D)** Statement-1 is false, Statement-2 is true

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) Statement-1 is false, Statement-2 is true**

**Detailed Solution:**

Statement-2 is true
Statement-1:
Sum of $n$ even natural numbers $=n(n+1)$
$$
\begin{aligned}
& \text { Mean }(\bar{x})=\frac{n(n+1)}{n}=n+1 \\
& \text { Variance }=\left[\frac{1}{n} \sum\left(x_1\right)^2\right]-(\bar{x})^2=\frac{1}{n}\left[2^2+4^2+\ldots .+(2 n)^2\right]-(n+1)^2 \\
& =\frac{1}{n} 2^2\left[1^2+2^2+\ldots .+n^2\right]-(n+1)^2=\frac{4}{n} \frac{n(n+1)(2 n+1)}{6}-(n+1)^2 \\
& =\frac{(n+1)[2(2 n+1)-3(n+1)]}{3}=\frac{(n+1)[4 n+2-3 n-3]}{3}=\frac{(n+1)(n-1)}{3}=\frac{n^2-1}{3}
\end{aligned}
$$
$\therefore$ Statement 1 is false.

</details>

---

### Q106. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

The mean of the numbers $a, b, 8,5,10$ is 6 and the variance is $6.80$. Then which one of the following gives possible values of $a$ and $b$ ?

**Options:**

- **(A)** $a=0, b=7$
- **(B)** $a=5, b=2$
- **(C)** $a=1, b=6$
- **(D)** $a=3, b=4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a=3, b=4$**

**Detailed Solution:**

Mean of $a, b, 8,5,10$ is 6
$$
\begin{aligned}
& \Rightarrow \frac{a+b+8+5+10}{5}=6 \\
& \Rightarrow a+b=7
\end{aligned}
$$
Given that Variance is $6.8$
$$
\begin{aligned}
& \therefore \text { Variance }=\frac{\sum\left(\mathrm{X}_{\mathrm{i}}-\mathrm{A}\right)^2}{\mathrm{n}} \\
& =\frac{(\mathrm{a}-6)^2+(\mathrm{b}-6)^2+4+1+16}{5}=6.8
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow a^2+b^2=25 \\
& a^2+(7-a)^2=25 \\
& \Rightarrow a^2-7 a+12=0 \\
& \therefore a=4,3 \text { and } b=3,4
\end{aligned}
$$

</details>

---

### Q107. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `1`

Suppose a population $A$ has 100 observations $101,102, \ldots, 200$, and another population $B$ has 100 observations $151,152, \ldots, 250$. If $V_A$ and $V_B$ represent the variances of the two populations, respectively, then $\frac{V_A}{V_B}$ is

**Options:**

- **(A)** 1
- **(B)** 9/4
- **(C)** 4/9
- **(D)** 2/3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 1**

**Detailed Solution:**

$\sigma_x^2=\frac{\sum d_1^2}{n}$. (Here deviations are taken from the mean)
Since $A$ and $B$ both has 100 consecutive integers, therefore both have same standard deviation and hence the variance.
$\therefore \frac{V_A}{V_B}=1\left(\right.$ As $\sum d_i^2$ is same in both the cases).

</details>

---

### Q108. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `1`

In an experiment with 15 observations on $x$, the following results were available: $\Sigma x^2=2830, \Sigma x=170$ One observation that was 20 was found to be wrong and was replaced by the correct value 30 . The corrected variance is

**Options:**

- **(A)** $8.33$
- **(B)** $78.00$
- **(C)** $188.66$
- **(D)** $177.33$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $78.00$**

**Detailed Solution:**

$\Sigma x=170, \Sigma x^2=2830$ increase in $\Sigma x=10$, then
$\Sigma x^{\prime}=170+10=180$
Increase in $\Sigma \mathrm{x}^2=900-400=500$ then
$\Sigma x^{\prime 2}=2830+500=3330$
Variance $=\frac{1}{n} \Sigma x^{\prime 2}-\left(\frac{1}{n} \Sigma x^{\prime}\right)^2$
$=\frac{1}{15} \times 3330-\left(\frac{1}{15} \times 180\right)^2=222-144=78$

</details>

---

