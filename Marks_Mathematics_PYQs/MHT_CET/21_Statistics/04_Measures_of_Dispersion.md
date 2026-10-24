# MHT CET Mathematics - Statistics

## Topic 4: Measures of Dispersion

**Total Questions:** 23

---

### Q1. MHT CET 2024 (11 May Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If for some $x \in \mathbb{R}^{+} \cup\{0\}$, the frequency distribution of the marks obtained by 20 students in a test is,
<img src="https://cdn.quizrr.in/question-assets/mhtcet/py35bdsq/OmvBBNSds9_lEC6ScG0UCqRCq9--0AhGFoc6JW8mdUg.original.fullsize.png"/>
then the mean of the marks is

**Options:**

- **(A)** $3.0$
- **(B)** $2.8$
- **(C)** $2.5$
- **(D)** $3.2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $2.8$**

**Detailed Solution:**

The total number of students is given as $20$. Therefore, the sum of the frequencies must be equal to $20$.

$\sum f_i = (x+1)^2 + (2x-5) + (x^2-3x) + x = 20$

Expanding and simplifying the equation:
$(x^2 + 2x + 1) + 2x - 5 + x^2 - 3x + x = 20$

$2x^2 + 2x - 4 = 20$

$2x^2 + 2x - 24 = 0$

$x^2 + x - 12 = 0$

$(x+4)(x-3) = 0$

Since it is given that $x \in \mathbb{R}^{+} \cup \{0\}$, we must have $x = 3$.

Now, substituting $x = 3$ to find the frequencies for each mark:
For marks $2$: $f_1 = (3+1)^2 = 16$
For marks $3$: $f_2 = 2(3) - 5 = 1$
For marks $5$: $f_3 = 3^2 - 3(3) = 0$
For marks $7$: $f_4 = 3$

The mean of the marks is given by the formula:
$\text{Mean } (\bar{x}) = \dfrac{\sum f_i x_i}{\sum f_i}$

$\bar{x} = \dfrac{16(2) + 1(3) + 0(5) + 3(7)}{20}$

$\bar{x} = \dfrac{32 + 3 + 0 + 21}{20}$

$\bar{x} = \dfrac{56}{20} = 2.8$

Answer: $2.8$

</details>

---

### Q2. MHT CET 2024 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In an experiment with 15 observations for $x$, the following results were available $\sum x^2=2830, \sum x=170$. One observation 20 was found to be wrong and was replaced by the correct value 30 . Then the corrected variance is

**Options:**

- **(A)** 78
- **(B)** 210
- **(C)** 225
- **(D)** 88

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 78**

**Detailed Solution:**

Given $n = 15$, $\sum x = 170$, and $\sum x^2 = 2830$.

The incorrect observation is $20$ and the correct observation is $30$.

Corrected $\sum x = 170 - 20 + 30 = 180$

Corrected $\sum x^2 = 2830 - (20)^2 + (30)^2$

Corrected $\sum x^2 = 2830 - 400 + 900 = 3330$

The formula for variance is $\sigma^2 = \dfrac{\sum x^2}{n} - \left(\dfrac{\sum x}{n}\right)^2$

Substituting the corrected values:

$\sigma^2 = \dfrac{3330}{15} - \left(\dfrac{180}{15}\right)^2$

$\sigma^2 = 222 - (12)^2$

$\sigma^2 = 222 - 144 = 78$

Answer: 78

</details>

---

### Q3. MHT CET 2024 (10 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The mean and variance of 7 observations are 8 and 16 respectively. If first five observations are $2,4,10,12,14$, then absolute difference of remaining two observations is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

Let the remaining two observations be $x$ and $y$.

Given the mean of 7 observations is 8:

$\dfrac{2 + 4 + 10 + 12 + 14 + x + y}{7} = 8$

$\dfrac{42 + x + y}{7} = 8$

$x + y = 14$

Given the variance of the 7 observations is 16:

$\sigma^2 = \dfrac{\sum x_i^2}{n} - (\bar{x})^2 = 16$

$\dfrac{2^2 + 4^2 + 10^2 + 12^2 + 14^2 + x^2 + y^2}{7} - 8^2 = 16$

$\dfrac{4 + 16 + 100 + 144 + 196 + x^2 + y^2}{7} - 64 = 16$

$\dfrac{460 + x^2 + y^2}{7} = 80$

$460 + x^2 + y^2 = 560$

$x^2 + y^2 = 100$

To find the absolute difference $|x - y|$, we use the identity:

$(x - y)^2 = 2(x^2 + y^2) - (x + y)^2$

$(x - y)^2 = 2(100) - (14)^2$

$(x - y)^2 = 200 - 196 = 4$

$|x - y| = 2$

Answer: 2

</details>

---

### Q4. MHT CET 2024 (10 May Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Mean and variance of six observations are 6 and 12 respectively. If each observation is multiplied by 3 , then new variance of the resulting observations is

**Options:**

- **(A)** 288
- **(B)** 36
- **(C)** 18
- **(D)** 108

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 108**

**Detailed Solution:**

Let the original observations be $x_1, x_2, \dots, x_6$.

Given that the variance of these observations is $\text{Var}(X) = 12$.

If each observation is multiplied by a constant $k$, the new variance becomes $k^2 \times \text{Var}(X)$.

Here, each observation is multiplied by $3$, so $k = 3$.

New variance $= 3^2 \times 12$

New variance $= 9 \times 12 = 108$

Answer: 108

</details>

---

### Q5. MHT CET 2024 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The variance of 20 observations is 5. If each observation is multiplied by 3 and then 8 is added to each number, then variance of resulting observations is

**Options:**

- **(A)** 35
- **(B)** 55
- **(C)** 25
- **(D)** 45

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 45**

**Detailed Solution:**

Let the original observations be $x_i$ and the new observations be $y_i$.

Given $\text{Var}(x) = 5$.

The new observations are formed by multiplying each original observation by 3 and adding 8, so $y_i = 3x_i + 8$.

Using the property of variance, $\text{Var}(ax + b) = a^2 \text{Var}(x)$.

Substituting $a = 3$ and $b = 8$, we get:

$\text{Var}(y) = 3^2 \text{Var}(x)$

$\text{Var}(y) = 9 \times 5 = 45$

Answer: 45

</details>

---

### Q6. MHT CET 2024 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The mean and the standard deviation of 10 observations are 20 and 2 respectively. Each of these 10 observations is multiplied by p and then reduced by $q$, where $p \neq 0$ and $q \neq 0$. If the new mean and new standard deviation (s.d.) become half of the original values, then q is equal to

**Options:**

- **(A)** $\quad-20$
- **(B)** -5
- **(C)** 10
- **(D)** -10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\quad-20$**

**Detailed Solution:**

Let the original observations be $x_1, x_2, \dots, x_{10}$.

Given original mean $\bar{x} = 20$ and original standard deviation $\sigma_x = 2$.

The new observations are $y_i = p x_i - q$.

The new mean is $\bar{y} = p \bar{x} - q = 20p - q$.

The new standard deviation is $\sigma_y = |p| \sigma_x = 2|p|$.

Given that the new mean and new standard deviation are half of the original values:

$\bar{y} = \dfrac{20}{2} = 10$

$\sigma_y = \dfrac{2}{2} = 1$

From the standard deviation condition:

$2|p| = 1 \Rightarrow |p| = \dfrac{1}{2} \Rightarrow p = \pm \dfrac{1}{2}$

From the mean condition:

$20p - q = 10 \Rightarrow q = 20p - 10$

If $p = \dfrac{1}{2}$, $q = 20\left(\dfrac{1}{2}\right) - 10 = 0$. Since it is given that $q \neq 0$, this value is rejected.

If $p = -\dfrac{1}{2}$, $q = 20\left(-\dfrac{1}{2}\right) - 10 = -10 - 10 = -20$.

Therefore, $q = -20$.

Answer: $\quad-20$

</details>

---

### Q7. MHT CET 2024 (04 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The mean and variance of seven observations are 8 and 16 respectively. If 5 of the observations are $2,4,10,12,14$, then the square root of product of remaining two observations is

**Options:**

- **(A)** $4 \sqrt{3}$
- **(B)** $3 \sqrt{3}$
- **(C)** $2 \sqrt{3}$
- **(D)** $5 \sqrt{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $4 \sqrt{3}$**

**Detailed Solution:**

Let the remaining two observations be $x$ and $y$.

Given mean $\bar{x} = 8$ and number of observations $n = 7$.

Sum of observations $= 7 \times 8 = 56$.

$2 + 4 + 10 + 12 + 14 + x + y = 56$

$42 + x + y = 56 \Rightarrow x + y = 14$

Given variance $\sigma^2 = 16$.

$\sigma^2 = \dfrac{\sum x_i^2}{n} - (\bar{x})^2$

$16 = \dfrac{2^2 + 4^2 + 10^2 + 12^2 + 14^2 + x^2 + y^2}{7} - 8^2$

$16 + 64 = \dfrac{4 + 16 + 100 + 144 + 196 + x^2 + y^2}{7}$

$80 \times 7 = 460 + x^2 + y^2$

$560 = 460 + x^2 + y^2 \Rightarrow x^2 + y^2 = 100$

Using the identity $(x+y)^2 = x^2 + y^2 + 2xy$:

$14^2 = 100 + 2xy$

$196 = 100 + 2xy \Rightarrow 2xy = 96 \Rightarrow xy = 48$

The square root of the product of the remaining two observations is $\sqrt{xy} = \sqrt{48} = 4\sqrt{3}$.

Answer: $4 \sqrt{3}$

</details>

---

### Q8. MHT CET 2024 (02 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Consider three observations $a, b$ and $c$ such that $b=a+c$. If the standard deviation of $\mathrm{a}+2, \mathrm{~b}+2, \mathrm{c}+2$ is d, then what holds true.

**Options:**

- **(A)** $\quad b^2=3\left(a^2+c^2+d^2\right)$
- **(B)** $\mathrm{b}^2=\mathrm{a}^2+\mathrm{c}^2+3 \mathrm{~d}^2$
- **(C)** $b^2=3\left(a^2+c^2\right)-9 d^2$
- **(D)** $\mathrm{b}^2=3\left(\mathrm{a}^2+\mathrm{c}^2\right)+9 \mathrm{~d}^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $b^2=3\left(a^2+c^2\right)-9 d^2$**

**Detailed Solution:**

Adding a constant to each observation does not change the standard deviation. Therefore, the standard deviation of $a, b, c$ is also $d$, and their variance is $d^2$.

The mean of the observations $a, b, c$ is given by:

$\bar{x} = \dfrac{a + b + c}{3}$

Since $b = a + c$, we can substitute $a + c$ with $b$:

$\bar{x} = \dfrac{b + b}{3} = \dfrac{2b}{3}$

The formula for the variance of three observations is:

$d^2 = \dfrac{a^2 + b^2 + c^2}{3} - (\bar{x})^2$

Substituting the mean into the variance formula:

$d^2 = \dfrac{a^2 + b^2 + c^2}{3} - \left(\dfrac{2b}{3}\right)^2$

$d^2 = \dfrac{a^2 + b^2 + c^2}{3} - \dfrac{4b^2}{9}$

Multiplying the entire equation by $9$ to clear the denominators:

$9d^2 = 3(a^2 + b^2 + c^2) - 4b^2$

$9d^2 = 3a^2 + 3b^2 + 3c^2 - 4b^2$

$9d^2 = 3a^2 + 3c^2 - b^2$

Rearranging the terms to solve for $b^2$:

$b^2 = 3a^2 + 3c^2 - 9d^2$

$b^2 = 3(a^2 + c^2) - 9d^2$

Answer: $b^2=3\left(a^2+c^2\right)-9 d^2$

</details>

---

### Q9. MHT CET 2024 (02 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The mean of 100 obseryations is 50 and their standard deviation is 5 , then the sum of all squares of all the observations is

**Options:**

- **(A)** 252500
- **(B)** 250500
- **(C)** 250000
- **(D)** 255000

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 252500**

**Detailed Solution:**

Given $n = 100$, $\bar{x} = 50$, and $\sigma = 5$.

The formula for variance is $\sigma^2 = \dfrac{\sum x_i^2}{n} - (\bar{x})^2$.

Substituting the given values:

$5^2 = \dfrac{\sum x_i^2}{100} - (50)^2$

$25 = \dfrac{\sum x_i^2}{100} - 2500$

$\dfrac{\sum x_i^2}{100} = 2525$

$\sum x_i^2 = 252500$

Answer: 252500

</details>

---

### Q10. MHT CET 2023 (11 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If variance of $x_1, x_2 \ldots \ldots, x_{\mathrm{n}}$ is $\sigma_x^2$, then the variance of $\lambda x_1, \lambda x_2, \ldots \ldots, \lambda x_n(\lambda \neq 0)$ is

**Options:**

- **(A)** $\lambda \cdot \sigma_x$
- **(B)** $\lambda \cdot \sigma_x^2$
- **(C)** $\lambda^2 \cdot \sigma_x$
- **(D)** $\lambda^2 \cdot \sigma_x^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\lambda^2 \cdot \sigma_x^2$**

**Detailed Solution:**

When each item of a data is multiplied by $\lambda$, variance is multiplied by $\lambda^2$.
$\therefore \quad$ New variance $=\lambda^2 \cdot \sigma_x^2$

</details>

---

### Q11. MHT CET 2023 (09 May Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the mean and S.D. of the data $3,5,7, \mathrm{a}, \mathrm{b}$ are 5 and 2 respectively, then $\mathrm{a}$ and $\mathrm{b}$ are the roots of the equation

**Options:**

- **(A)** $x^2-10 x+18=0$
- **(B)** $2 x^2-20 x+19=0$
- **(C)** $x^2-10 x+19=0$
- **(D)** $x^2-20 x+18=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $x^2-10 x+19=0$**

**Detailed Solution:**

$\text { Mean }=5$ ... [Given]
$\begin{aligned} & \therefore \quad \text { Mean }=\frac{\sum_{i=1}^{\mathrm{n}} x_i}{\mathrm{n}} \\ & \Rightarrow 5=\frac{3+5+7+\mathrm{a}+\mathrm{b}}{5} \\ & \Rightarrow \mathrm{a}+\mathrm{b}=10 ... (i)\end{aligned}$
$\begin{aligned}
& \text { S.D. }=2 ... [Given]\\
& \therefore \quad \text { S.D. }=\sqrt{\frac{\sum x_1^2}{\mathrm{n}}-(\bar{x})^2} \\
& \Rightarrow(2)^2=\frac{3^2+5^2+7^2+\mathrm{a}^2+\mathrm{b}^2}{5}-(5)^2 \\
& \Rightarrow 4=\frac{83+\mathrm{a}^2+\mathrm{b}^2}{5}-25 \\
& \Rightarrow \mathrm{a}^2+\mathrm{b}^2=62 ... (ii)
\end{aligned}$
...[Given]
Now, (i) $\Rightarrow a+b=10$
Squaring both sides, we get
$\begin{array}{ll} 
& (a+b)^2=100 \\
& a^2+2 a b+b^2=100 \\
& 38=2 a b ... [From (ii)]\\
\therefore \quad & a b=19
\end{array}$
Note that the required quadratic equation is expressed as
$\begin{aligned}
& x^2-(\mathrm{a}+\mathrm{b}) x+\mathrm{ab}=0 \\
\therefore \quad & x^2-10 x+19=0
\end{aligned}$

</details>

---

### Q12. MHT CET 2023 (09 May Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The standard deviation of the following distribution
\begin{array}{|c|c|c|c|}
\hline C.I. & 0-6 & 6-12 & 12-18 \\
\hline \mathrm{f}_{\mathrm{i}} & 2 & 4 & 6 \\
\hline
\end{array}
is

**Options:**

- **(A)** $5 \sqrt{2}$
- **(B)** $\sqrt {5}$
- **(C)** $2\sqrt {5}$
- **(D)** $20$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2\sqrt {5}$**

**Detailed Solution:**

\begin{array}{|c|c|c|c|c|c|}
\hline C.I. & \mathbf{f}_{\mathbf{i}} & \boldsymbol{x}_{\mathbf{i}} & \boldsymbol{x}_{\mathbf{i}}^{\mathbf{2}} & \mathbf{f}_{\mathbf{i}} \boldsymbol{x}_{\mathbf{i}} & \mathbf{f}_{\mathbf{i}} \boldsymbol{x}_{\mathbf{i}}^{\mathbf{2}} \\
\hline 0-6 & 2 & 3 & 9 & 6 & 18 \\
\hline 6-12 & 4 & 9 & 81 & 36 & 324 \\
\hline 12-18 & 6 & 15 & 225 & 90 & 1350 \\
\hline Total & \mathbf{1 2} & & & \mathbf{1 3 2} & \mathbf{1 6 9 2} \\
\hline
\end{array}
Here $\sum \mathrm{f}_{\mathrm{i}}=12, \sum \mathrm{f}_{\mathrm{i}} x_{\mathrm{i}}=132, \sum \mathrm{f}_{\mathrm{i}} x_{\mathrm{i}}^2=1692$
$\begin{aligned}
\therefore \quad \mathrm{V}(\mathrm{X}) & =\frac{1692}{12}-\left(\frac{132}{12}\right)^2 \\
& =141-121 \\
& =20
\end{aligned}$
$\therefore \quad$ Standard deviation $=\sqrt{20}=2 \sqrt{5}$

</details>

---

### Q13. MHT CET 2021 (24 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For the set of 50 observation, the sum of their squares is 3050 , their arithmetic mean is 6 . Hence the standard deviation of these observations is

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

We have $\mathrm{n}=50, \Sigma \mathrm{x}_{\mathrm{i}}^2=3050, \overline{\mathrm{x}}=6$
$\begin{aligned}
& \text { S.D. }=\sqrt{\frac{1}{n} \Sigma x_i^2-(\bar{x})^2} \\
& =\sqrt{\frac{3050}{50}-(6)^2}=\sqrt{61-36}=\sqrt{25}=5
\end{aligned}$

</details>

---

### Q14. MHT CET 2021 (24 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the standard deviation of data is 12 and mean is 72 , then coefficient of variation is

**Options:**

- **(A)** $15.67 \%$
- **(B)** $14.67 \%$
- **(C)** $13.67 \%$
- **(D)** $16.67 \%$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $16.67 \%$**

**Detailed Solution:**

$\begin{aligned} & \text { Coefficient of variation }=\frac{\text { Standard Deviation }}{\text { Mean }} \times 100 \\ & \frac{12}{72} \times 100 \%=16.67 \%\end{aligned}$

</details>

---

### Q15. MHT CET 2021 (23 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Given that total of 16 values is 528 and sum of the squares of deviation from 33 is 9158 . The variance is

**Options:**

- **(A)** 562.73
- **(B)** 570.375
- **(C)** 574.375
- **(D)** 572.375

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 572.375**

**Detailed Solution:**

We have $\mathrm{n}=16, \Sigma \mathrm{x}_{\mathrm{i}}=528$, and $\frac{528}{16}=33$ $\Rightarrow \overline{\mathrm{x}}=33$ and $\Sigma\left(\mathrm{x}_{\mathrm{i}}-\overline{\mathrm{x}}\right)^2=9158$
Variance $=\frac{1}{\mathrm{n}} \Sigma\left(\mathrm{x}_{\mathrm{i}}-\overline{\mathrm{x}}\right)^2=\frac{9158}{16}=527.375$

</details>

---

### Q16. MHT CET 2021 (23 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The arithmetic mean of marks in Mathematics for four divisions A, B, C and D were 80, 75, 70 and 72 respectively. Their standard deviations were $12,6,8$ and and 10 respectively. Then, division<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/rFMGAcLV72LwCOmiLrC7AGU2qj5IBbtymzeVX2T-7pw.original.fullsize.png">
has more uniformity.

**Options:**

- **(A)** D
- **(B)** B
- **(C)** C
- **(D)** A

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) B**

**Detailed Solution:**

$$
\begin{aligned}
& \text { We know that C.V. }=\frac{\text { Standard Deviation }}{\text { Mean }} \\
& \therefore(\text { C.V. })_A=\frac{12}{18}=0.15 \text { and }(\text { C.V. })_B=\frac{6}{75}=0.08 \\
& (\text { C.V. })_C=\frac{8}{70}=0.11 \text { and }(\text { C.V. })_D=\frac{10}{72}=0.14
\end{aligned}
$$
C.V. is the least for division B.

</details>

---

### Q17. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the variance of the data $2,4,5,6,8,17$ is 23.33 , then the variance of $4,8,10,12,16,34$ will be

**Options:**

- **(A)** 93.32
- **(B)** 25.33
- **(C)** 23.33
- **(D)** 48.66

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 93.32**

**Detailed Solution:**

We find that each element of new data is 2 times of each element in old data.
Variance of old data $=23.33$
$\therefore$ variance of new data $=(23.33)(2)^2=93.32$

</details>

---

### Q18. MHT CET 2021 (22 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A random variable $X \sim B(n, p)$, if values of mean and variance of $\mathrm{X}$ are 18,12 respectively, then $\mathrm{n}=$

**Options:**

- **(A)** 54
- **(B)** 18
- **(C)** 12
- **(D)** 55

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 54**

**Detailed Solution:**

We have $n p=18$ and $n p q=12$
$$
\begin{aligned}
& \therefore \mathrm{q}=\frac{12}{18}=\frac{2}{3} \quad \Rightarrow \mathrm{p}=1-\frac{2}{3}=\frac{1}{3} \\
& \therefore \mathrm{n}\left(\frac{1}{3}\right)=18 \quad \Rightarrow \mathrm{n}=54
\end{aligned}
$$

</details>

---

### Q19. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

For $\mathrm{X} \sim \mathrm{B}(\mathrm{n}, \mathrm{p})$, if $\mathrm{p}=0.6, \mathrm{E}(\mathrm{X})=6$, then $\operatorname{Var}(\mathrm{X})=$

**Options:**

- **(A)** 6.6
- **(B)** 24
- **(C)** 2.4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2.4**

**Detailed Solution:**

We have $p=0.6$ and $n p=6 \Rightarrow n=10$
$$
\therefore \operatorname{Var}(\mathrm{X})=\mathrm{npq}=(10)(0.6)(0.4)=2.4
$$

</details>

---

### Q20. MHT CET 2021 (21 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The mean of five observation is 4 and their variance is 5.2. If three of these observations are 1,2 and 6 , then the other two are

**Options:**

- **(A)** 2 and 9
- **(B)** 3 and 8
- **(C)** 4 and 7
- **(D)** 5 and 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 4 and 7**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/8rvOycJskdzM15sJraeC-tHnlNpQTN3nfnwpwqlhyjo.original.fullsize.png">

</details>

---

### Q21. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For two data sets each of size 5 , the variance are given to be 4 and 5 and the corresponding means are given to be 2 and 4 respectively. The variance of the combined data set is

**Options:**

- **(A)** $\frac{13}{2}$
- **(B)** $\frac{5}{2}$
- **(C)** $\frac{11}{2}$
- **(D)** $\frac{15}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{11}{2}$**

**Detailed Solution:**

We have $\mathrm{n}_1=5, \sigma_1{ }^2=4, \overline{\mathrm{x}}_1=2$ and $\mathrm{n}_2=5, \sigma_2{ }^2=5, \overline{\mathrm{x}}_2=4$
here combined mean $=\bar{x}_c=\frac{(5)(2)+(5)(4)}{(5)+(5)}=3$
$$
\mathrm{d}_1=\overline{\mathrm{x}}_1-\overline{\mathrm{x}}_{\mathrm{c}}=2-3=1 \text { and } \mathrm{d}_2=\overline{\mathrm{x}}_2-\overline{\mathrm{x}}_{\mathrm{c}}=4-3=1
$$
Combined variance $=$
$$
=\frac{\mathrm{n}_1\left(\sigma_1^2+\mathrm{d}_1^2\right)+\mathrm{n}_2\left(\sigma_2^2+\mathrm{d}_2^2\right)}{\mathrm{n}_1+\mathrm{n}_2}=\frac{5(4+1)+5(5+1)}{5+5}=\frac{11}{2}
$$

</details>

---

### Q22. MHT CET 2021 (21 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a meeting $60 \%$ of the members favour and $40 \%$ oppose a certain proposal. A member is selected at random and we take $\mathrm{X}=0$ if the opposed and $\mathrm{X}=1$ if he is in favour, then Var $\mathrm{X}=$

**Options:**

- **(A)** 0.36
- **(B)** 0.24
- **(C)** 0.6
- **(D)** 0.06

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 0.24**

**Detailed Solution:**

$$
\text { From the given data, we write }
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/mht_cet/K5mk61CFeYKtMTiWhnMkww6fdsBR1Lm5nLVRjgwrdV0.original.fullsize.png">



$$
\text { Variance }=\Sigma \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}^2-\left(\sum \mathrm{p}_{\mathrm{i}} \mathrm{x}_{\mathrm{i}}\right)^2=0.6-(0.6)^2=0.6-0.36=0.24
$$

</details>

---

### Q23. MHT CET 2021 (20 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the variance of the numbers $2,3,11$ and $x$ is $\frac{49}{4}$, then the values of $x$ are

**Options:**

- **(A)** $6, \frac{14}{3}$
- **(B)** $4, \frac{13}{5}$
- **(C)** $6, \frac{16}{3}$
- **(D)** $6, \frac{14}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $6, \frac{14}{3}$**

**Detailed Solution:**

Mean of given number is $\frac{2+3+11+x}{4}$ i.e. $\frac{16+x}{4}$
$$
\begin{aligned}
& \text { Variance }=\frac{1}{\mathrm{n}} \sum\left(\mathrm{x}_{\mathrm{i}}-\overline{\mathrm{x}}\right)^2 \\
& \therefore \frac{49}{4}=\frac{1}{4}\left[\left(\frac{16+\mathrm{x}}{4}-2\right)^2+\left(\frac{16+\mathrm{x}}{4}-3\right)^2+\left(\frac{16+\mathrm{x}}{4}-11\right)^2+\left(\frac{16+\mathrm{x}}{4}-\mathrm{x}\right)^2\right] \\
& \therefore 49=\frac{(8+\mathrm{x})^2}{16}+\frac{(4+\mathrm{x})^2}{16}+\frac{(\mathrm{x}-28)^2}{16}+\frac{(16-3 \mathrm{x})^2}{16} \\
& \therefore(49)(16)=\left(64+\mathrm{x}^2+16 \mathrm{x}\right)+\left(16+\mathrm{x}^2+8 \mathrm{x}\right)
\end{aligned}
$$

$$
\begin{aligned}
& +\left(\mathrm{x}^2-56 \mathrm{x}+784\right)+\left(256+9 \mathrm{x}^2-96 \mathrm{x}\right) \\
& \therefore 784=12 \mathrm{x}^2-128 \mathrm{x}+80+784+256 \\
& \therefore 12 \mathrm{x}^2-128 \mathrm{x}+336=0 \\
& \Rightarrow 3 \mathrm{x}^2-32 \mathrm{x}+84=0 \\
& \therefore \mathrm{x}=\frac{32 \pm \sqrt{(32)^2-(4)(3)(84)}}{2(3)}=\frac{32 \pm \sqrt{1024-1008}}{6}=\frac{32 \pm 4}{6} \\
& \therefore \mathrm{x}=\frac{36}{6} \text { or } \mathrm{x}=\frac{28}{6} \\
& \Rightarrow \mathrm{x}=6, \frac{14}{3}
\end{aligned}
$$

</details>

---

