# JEE Main Mathematics - Probability

## Topic 8: Random Variable and its Probability Distribution

**Total Questions:** 39

---

### Q1. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The probability distribution of a random variable $X$ is given below : 
 \(\begin{array}{|c|c|c|c|c|c|c|c|c|} \hline X & 4k & \dfrac{30}{7}k & \dfrac{32}{7}k & \dfrac{34}{7}k & \dfrac{36}{7}k & \dfrac{38}{7}k & \dfrac{40}{7}k & 6k \\ \hline P(X) & \dfrac{2}{15} & \dfrac{1}{15} & \dfrac{2}{15} & \dfrac{1}{5} & \dfrac{1}{15} & \dfrac{2}{15} & \dfrac{1}{5} & \dfrac{1}{15} \\ \hline \end{array}\) 
 If $\mathrm{E}(\mathrm{X})=\frac{263}{15}$, then $\mathrm{P}(\mathrm{X}<20)$ is equal to :

**Options:**

- **(A)** $\frac{11}{15}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{14}{15}$
- **(D)** $\frac{8}{15}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\frac{11}{15}$**

**Detailed Solution:**

$E(X) = \sum X_i P(X_i) = \dfrac{526k}{15 \times 7} = \dfrac{263}{15}$
$\Rightarrow k = \dfrac{7}{2}$
Substituting $k = \dfrac{7}{2}$, the values of $X$ become:
$X$: 14, 15, 16, 17, 18, 19, 20, 21
$P(X)$: $\dfrac{2}{15}$, $\dfrac{1}{15}$, $\dfrac{2}{15}$, $\dfrac{1}{5}$, $\dfrac{1}{15}$, $\dfrac{2}{15}$, $\dfrac{1}{5}$, $\dfrac{1}{15}$
$P(X < 20) = \sum_{X=14}^{19} P(X)$
$= \dfrac{2}{15} + \dfrac{1}{15} + \dfrac{2}{15} + \dfrac{1}{5} + \dfrac{1}{15} + \dfrac{2}{15} = \dfrac{11}{15}$

</details>

---

### Q2. JEE Main 2026 (22 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If a random variable $x$ has the probability distribution 
 $\begin{array}{|c|c|c|c|c|c|c|c|c|} \hline x & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\ \hline P(x) & 0 & 2k & k & 3k & 2k^{2} & 2k & k^{2}+k & 7k^{2} \\ \hline \end{array}$ 
 then $P(3 < x \leq 6)$ is equal to

**Options:**

- **(A)** 0.64
- **(B)** 0.22
- **(C)** 0.33
- **(D)** 0.34

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 0.33**

**Detailed Solution:**

Sum of all probabilities = 1
$\Rightarrow 0 + 2k + k + 3k + 2k^2 + 2k + (k^2+k) + 7k^2 = 1$ 
$\Rightarrow 10k^2 + 9k - 1 = 0$.
$\Rightarrow(10k-1)(k+1) = 0$ 
$\Rightarrow k = \frac{1}{10}$ (rejecting $k = -1$).
$P(3 < x \le 6) = P(4) + P(5) + P(6)$ 
$= 2k^2 + 2k + k^2 + k$ 
$= 3k^2 + 3k = 3(0.01) + 3(0.1) = 0.33$.

</details>

---

### Q3. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

A random variable $X$ takes values $0,1,2,3$ with probabilities $\frac{2 a+1}{30}, \frac{8 a-1}{30}, \frac{4 a+1}{30}, b$ respectively, where $\mathrm{a}, \mathrm{b} \in \mathbf{R}$. Let $\mu$ and $\sigma$ respectively be the mean and standard deviation of X such that $\sigma^{2}+\mu^{2}=2$. Then $\frac{\mathrm{a}}{\mathrm{b}}$ is equal to :

**Options:**

- **(A)** $12$
- **(B)** $30$
- **(C)** $60$
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $60$**

**Detailed Solution:**

Sum of probabilities $= 1$: $\frac{2a+1+8a-1+4a+1}{30} + b = 1 \Rightarrow b = \frac{29-14a}{30}$.
$\sigma^2 + \mu^2 = E(X^2) = 2$.
$E(X^2) = \frac{8a-1}{30} + \frac{4(4a+1)}{30} + \frac{9(29-14a)}{30} = \frac{-102a + 264}{30} = 2$.
$-102a + 264 = 60 \Rightarrow a = 2$.
$b = \frac{29 - 28}{30} = \frac{1}{30}$.
$\frac{a}{b} = \frac{2}{1/30} = 60$.

</details>

---

### Q4. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Let a random variable X take values $0,1,2,3$ with $\mathrm{P}(\mathrm{X}=0)=\mathrm{P}(\mathrm{X}=1)=\mathrm{p}, \mathrm{P}(\mathrm{X}=2)=\mathrm{P}(\mathrm{X}=3)$ and $\mathrm{E}\left(\mathrm{X}^2\right)=2 \mathrm{E}(\mathrm{X})$. Then the value of $8 \mathrm{p}-1$ is :

**Options:**

- **(A)** 0
- **(B)** 2
- **(C)** 1
- **(D)** 3

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

$\begin{aligned} & 2 p+2 q=\frac{1}{2} \\ & p+q \\ & E\left(x^2\right)=\sum_{i=0}^3 x_i^2 p\left(x_i\right)=0 \cdot p+1 \cdot p+4 \cdot q+9 q \\ & =p+13 q \\ & E(x)=\sum_{i=0}^3 x_i^2 p\left(x_i\right)=0 \cdot p+1 \cdot p+2 q+3 q=p+5 q \\ & p+13 q=2(p+5 q) \\ & p=3 q \\ & \text { So, } q=\frac{1}{8} \& p=\frac{3}{8} \quad \\ & \text { So, } 8 p-1=2 \quad \text { Option (2) }\end{aligned}$

</details>

---

### Q5. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A box contains 10 pens of which 3 are defective. A sample of 2 pens is drawn at random and let $X$ denote the number of defective pens. Then the variance of X is

**Options:**

- **(A)** $\frac{11}{15}$
- **(B)** $\frac{28}{75}$
- **(C)** $\frac{2}{15}$
- **(D)** $\frac{3}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{28}{75}$**

**Detailed Solution:**

\begin{array}{|r|c|c|c|}\hline x & \mathrm{x}=0 & \mathrm{x}=1 & \mathrm{x}=2 \\\hline \mathrm{P}(\mathrm{x}) & \frac{{ }^7 \mathrm{C}_2}{{ }^{10} \mathrm{C}_2} & \frac{{ }^7 \mathrm{C}_1^3 \mathrm{C}_1}{{ }^{10} \mathrm{C}_2} & { }^3{ }^{10} \mathrm{C}_2 \\\hline\end{array}
$\begin{aligned} & \mu=\Sigma \mathrm{x}_{\mathrm{i}} \mathrm{P}\left(\mathrm{x}_{\mathrm{i}}\right)=0+\frac{7}{15}+\frac{2}{15}=\frac{3}{5} \\ & \text { Variance }(\mathrm{x})=\Sigma \mathrm{P}_{\mathrm{i}}\left(\mathrm{x}_{\mathrm{i}}-\mu\right)^2=\frac{28}{75}\end{aligned}$

</details>

---

### Q6. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the probability that the random variable X takes the value $x$ is given by $P(X=x)=k(x+1) 3^{-x}$, $\mathrm{x}=0,1,2,3 \ldots \ldots$, where k is a constant, then $\mathrm{P}(\mathrm{X} \geq 3)$ is equal to

**Options:**

- **(A)** $\frac{7}{27}$
- **(B)** $\frac{4}{9}$
- **(C)** $\frac{8}{27}$
- **(D)** $\frac{1}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{9}$**

**Detailed Solution:**

$\sum_{x=0}^{\infty} k(x+1) 3^{-x}=1$
$\Rightarrow \frac{1}{\mathrm{k}}=1+\frac{2}{3}+\frac{3}{3^2}+\frac{4}{3^3}+$   ...(i)
$\frac{1}{3 \mathrm{k}}=\frac{1}{3}+\frac{2}{3^2}+\frac{3}{3^3}+\ldots$   ...(ii)
(i)- (ii) $\Rightarrow \frac{1}{\mathrm{k}}-\frac{1}{3 \mathrm{k}}=1+\frac{1}{3}+\frac{1}{3^2}+\ldots$
$\begin{aligned} & \Rightarrow \mathrm{k}=\frac{4}{9} \\ & \mathrm{P}(\mathrm{x} \geq 3)=1-\mathrm{P}(\mathrm{x}=0)-\mathrm{P}(\mathrm{x}=1)-\mathrm{P}(\mathrm{x}=2) \\ & =1-\mathrm{k}\left(1+\frac{2}{3}+\frac{3}{9}\right)=\frac{1}{9}\end{aligned}$

</details>

---

### Q7. JEE Main 2025 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\mathrm{A}=\left[\mathrm{a}_{i j}\right]$ be a $2 \times 2$ matrix such that $\mathrm{a}_{i j} \in\{0,1\}$ for all $i$ and $j$. Let the random variable X denote the possible values of the determinant of the matrix $A$. Then, the variance of $X$ is :

**Options:**

- **(A)** $\frac{3}{4}$
- **(B)** $\frac{5}{8}$
- **(C)** $\frac{3}{8}$
- **(D)** $\frac{1}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{3}{8}$**

**Detailed Solution:**

$\begin{array}{|c|c|c|c|}
\hline x & 0 & 1 & -1 \\
\hline P(x) & \frac{10}{16} & \frac{3}{16} & \frac{3}{16} \\
\hline
\end{array}$
$\begin{aligned} & \operatorname{Var}(x)=E\left(x^2\right)-[E(x)]^2 \\ & =\sum_{i=1}^3 x_i^2 P\left(x_i\right)-(\mu)^2 \\ & =1 \times \frac{3}{16}+1 \times \frac{3}{16} \quad[\mu=0] \\ & =\frac{6}{16}=\frac{3}{8}\end{aligned}$

</details>

---

### Q8. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three defective oranges are accidently mixed with seven good ones and on looking at them, it is not possible to differentiate between them. Two oranges are drawn at random from the lot. If $x$ denote the number of defective oranges, then the variance of $x$ is

**Options:**

- **(A)** 28/75
- **(B)** 18/25
- **(C)** $26 / 75$
- **(D)** $14 / 25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 28/75**

**Detailed Solution:**

There are 3 bad oranges and 7 good oranges. $\therefore \quad X=$ number of bad oranges drawn.
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/a1LXvsdOljerU8qA0xMcoSupG5Jos_kNLAO6k9UPwbs.original.fullsize.png">

$\therefore$ Variance
$\begin{aligned}
& =0^2 \cdot \frac{{ }^7 C_2}{{ }^{10} C_2}+1^2 \cdot\left(\frac{3 \times 7}{{ }^{10} C_2}\right)+2^2\left(\frac{3}{{ }^{10} C_2}\right) \\
& \quad-\left(0+1 \cdot \frac{3 \times 7}{{ }^{10} C_2}+2 \cdot \frac{3}{{ }^{10} C_2}\right)^2 \\
& =\frac{28}{75}
\end{aligned}$

</details>

---

### Q9. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

A coin is tossed three times. Let $X$ denote the number of times a tail follows a head. If $\mu$ and $\sigma^2$ denote the mean and variance of $X$, then the value of $64\left(\mu+\sigma^2\right)$ is :

**Options:**

- **(A)** $51$
- **(B)** $64$
- **(C)** $32$
- **(D)** $48$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $48$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/4O_KXgsn98hRiagfZ8QAVcUtISYhlulpXc4hRqAHjkc.original.fullsize.png">

$\begin{aligned} & \mu=\sum x_i P_i=\frac{1}{2} \\ & \sigma^2=\sum x_i^2 P_i-\mu^2 \\ & =\frac{1}{2}-\frac{1}{4}=\frac{1}{4} \\ & 64\left(\mu+\sigma^2\right)=64\left[\frac{1}{2}+\frac{1}{4}\right] \\ & =64 \times \frac{3}{4}=48\end{aligned}$

</details>

---

### Q10. JEE Main 2024 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Three balls are drawn at random from a bag containing 5 blue and 4 yellow balls. Let the random variables $X$ and $Y$ respectively denote the number of blue and yellow balls. If $\bar{X}$ and $\bar{Y}$ are the means of $X$ and $Y$ respectively, then $7 \bar{X}+4 \bar{Y}$ is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **17**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/iTxSG9yMrIsjsGOS363A7lr5BSowYiXRjXgnECbp-IM.original.fullsize.png">
$\begin{aligned} & 7 \overline{\mathrm{x}}=\frac{{ }^5 \mathrm{C}_1{ }^4 \mathrm{C}_2+{ }^5 \mathrm{C}_2 \cdot{ }^4 \mathrm{C}_1 \times 2+{ }^5 \mathrm{C}_3 \cdot{ }^4 \mathrm{C}_0 \times 3}{{ }^9 \mathrm{C}_3} \times 7 \\ & \frac{30+80+30}{84} \times 7 \\ & =\frac{140}{12}=\frac{70}{6}=\frac{35}{3}\end{aligned}$
$\begin{array}{|l|l|l|l|l|l|}
\hline yellow & 0 & 1 & 2 & 3 & 4 \\
\hline & & { }^5 \mathrm{C}_2{ }^4 \mathrm{C}_1 & { }^5 \mathrm{C}_1{ }^4 \mathrm{C}_2 & { }^5 \mathrm{C}_0{ }^4 \mathrm{C}_3 & 0 \\
\hline
\end{array}$
$4 \bar{y}=\frac{40+60+12}{84} \times 4=\frac{112}{21}=\frac{16}{3}$

</details>

---

### Q11. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

From a lot of 12 items containing 3 defectives, a sample of 5 items is drawn at random. Let the random variable $\mathrm{X}$ denote the number of defective items in the sample. Let items in the sample be drawn one by one without replacement. If variance of $X$ is $\frac{m}{n}$, where $\operatorname{gcd}(m, n)=1$, then $n-m$ is equal to _________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **71**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{a}=1-\frac{{ }^3 \mathrm{C}_5}{{ }^{12} \mathrm{C}_5} \\
& \mathrm{~b}=3 \cdot \frac{{ }^9 \mathrm{C}_4}{{ }^{12} \mathrm{C}_5} \\
& \mathrm{c}=3 \cdot \frac{{ }^9 \mathrm{C}_3}{{ }^{12} \mathrm{C}_5} \\
& \mathrm{~d}=1 \cdot \frac{{ }^9 \mathrm{C}_2}{{ }^{12} \mathrm{C}_5} \\
& \mathrm{u}=0 . \mathrm{a}+1 . b+2 \cdot c+3 \cdot \mathrm{d}=1.25 \\
& \sigma^2=0 . \mathrm{a}+1 . b+4 . c+9 \mathrm{~d}-\mathrm{u}^2 \\
& \sigma^2=\frac{105}{176}
\end{aligned}$
Ans. $176-105=71$

</details>

---

### Q12. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Three rotten apples are accidently mixed with fifteen good apples. Assuming the random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> to be the number of rotten apples in a draw of two apples, the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>37</mn><mn>153</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>57</mn><mn>153</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>47</mn><mn>153</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>153</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>40</mn><mn>153</mn></mfrac></math>**

**Detailed Solution:**

<p>Given apples are: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> bad, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> good</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be no. of bad apples.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow></mrow><mn>15</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow><mrow><msup><mrow></mrow><mn>18</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mn>15</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>×</mo><mn>13</mn><mo>!</mo></mrow></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mrow><mn>18</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>×</mo><mn>16</mn><mo>!</mo></mrow></mfrac></mstyle></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>15</mn><mo>×</mo><mn>14</mn></mrow><mrow><mn>18</mn><mo>×</mo><mn>17</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>5</mn><mo>×</mo><mn>7</mn></mrow><mrow><mn>3</mn><mo>×</mo><mn>17</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mn>35</mn><mn>51</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow></mrow><mn>3</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>×</mo><mn>15</mn></msup><msub><mi>C</mi><mn>1</mn></msub></mrow><mrow><msup><mrow></mrow><mn>18</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mo>×</mo><mn>15</mn></mrow><mrow><mn>9</mn><mo>×</mo><mn>17</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>17</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><msup><mrow></mrow><mn>3</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow><mrow><msup><mrow></mrow><mn>18</mn></msup><msub><mi>C</mi><mn>2</mn></msub></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mrow><mn>9</mn><mo>×</mo><mn>17</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>153</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>E</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mn>0</mn><mo>×</mo><mfrac><mn>35</mn><mn>51</mn></mfrac><mo>+</mo><mn>1</mn><mo>×</mo><mfrac><mn>5</mn><mn>17</mn></mfrac><mo>+</mo><mn>2</mn><mo>×</mo><mfrac><mn>3</mn><mn>153</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>E</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Var</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mi>E</mi><mfenced><msup><mi>X</mi><mn>2</mn></msup></mfenced><mo>−</mo><msup><mfenced><mrow><mi>E</mi><mfenced><mi>X</mi></mfenced></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Var</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mn>0</mn><mo>×</mo><mfrac><mn>35</mn><mn>51</mn></mfrac><mo>+</mo><mn>1</mn><mo>×</mo><mfrac><mn>5</mn><mn>17</mn></mfrac><mo>+</mo><mn>4</mn><mo>×</mo><mfrac><mn>1</mn><mn>51</mn></mfrac><mo>−</mo><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Var</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mfrac><mn>19</mn><mn>51</mn></mfrac><mo>−</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>Var</mi><mfenced><mi>X</mi></mfenced><mo>=</mo><mfrac><mn>40</mn><mn>153</mn></mfrac></math></p>

</details>

---

### Q13. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>The random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> follows binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>)</mo></math>, for which the difference of the mean and the variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mo>&#160;</mo><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>1</mn><mo>)</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#62;</mo><mn>1</mn><mo>)</mo></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that the difference between the mean and variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>p</mi><mo>-</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>p</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>q</mi><mo>)</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><msup><mi>p</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p><p>Also given that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>3</mn><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>p</mi><mn>2</mn></msup><msup><mi>q</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mi>p</mi><mo>&#183;</mo><msup><mi>q</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#183;</mo><mfrac><mrow><mi>n</mi><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mi>p</mi><mo>=</mo><mn>3</mn><mo>&#183;</mo><mi>n</mi><mo>&#183;</mo><mi>q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>p</mi><mo>=</mo><mn>3</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mi>p</mi><mn>2</mn></msup></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mi>p</mi><mo>=</mo><mn>3</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>p</mi><mo>)</mo></mrow><mi>p</mi></mfrac><mo>=</mo><mn>3</mn><mo>(</mo><mn>1</mn><mo>-</mo><mi>p</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>+</mo><mi>p</mi><mo>=</mo><mn>3</mn><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>n</mi><mo>=</mo><mn>4</mn></math>.</p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><mi>P</mi><mo>(</mo><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>)</mo><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>(</mo><mn>1</mn><mo>-</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>)</mo><mo>-</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>)</mo><mo>)</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>4</mn></msup><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mn>11</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q14. JEE Main 2023 (13 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>A coin is biased so that the head is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> times as likely to occur as tail. This coin is tossed until a head or three tails occur. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> denotes the number of tosses of the coin, then the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>38</mn><mn>16</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>15</mn><mn>16</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>16</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>81</mn><mn>64</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>16</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>It is given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>H</mi><mo>)</mo><mo>=</mo><mn>3</mn><mi>P</mi><mo>(</mo><mi>T</mi><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>P</mi><mo>(</mo><mi>H</mi><mo>)</mo><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mi>P</mi><mo>(</mo><mi>T</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>Since coin is tossed till either <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mi>H</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>T</mi></math> occurs. So, process will end in the maximum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> throws.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mi>i</mi></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>		</tr>		<tr>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mi>i</mi></mrow></mfenced></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#183;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></td>			<td style="text-align: center;"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></td>		</tr>	</tbody></table><p>Now we know that,</p><p>Mean is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>X</mi><mi>i</mi></msub><mi>P</mi><mfenced><msub><mi>X</mi><mi>i</mi></msub></mfenced></math> </p><p>Mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>3</mn><mn>16</mn></mfrac><mo>+</mo><mn>3</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>21</mn><mn>16</mn></mfrac></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q15. JEE Main 2023 (12 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

A fair <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math> faces die is rolled repeatedly until a number less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> appears. If the mean of the number of tosses required is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>9</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10**

**Detailed Solution:**

<p>Given,</p><p>A fair <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#160;</mo><mfenced><mrow><mi>n</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math> faces die is rolled repeatedly until a number less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> appears,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mspace linebreak="newline"></mspace><msub><mi>p</mi><mi>i</mi></msub><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>&#183;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>3</mn></msup></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>Now we know that, mean is given by,</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><msub><mi>p</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn><mo>&#183;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac><mo>+</mo><mfrac><mn>2</mn><mi>n</mi></mfrac><mo>&#183;</mo><mfenced><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac></mfenced><mo>+</mo><mfrac><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mfenced><mfrac><mrow><mo>&#160;</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mi>n</mi></mfrac></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>n</mi><mn>9</mn></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mi>S</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mi>n</mi><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>n</mi></mfrac><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mi>n</mi><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>Now subtracting equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>-</mo><mfenced><mn>3</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>n</mi><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfrac></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>n</mi><mn>9</mn></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>n</mi></mfrac></mrow></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mi>n</mi></mfrac></mstyle></mrow></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mi>n</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>10</mn></math></p>

</details>

---

### Q16. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

<p>Two dice <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> are rolled. Let the numbers obtained on <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi></math> respectively. If the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi></math> are co-prime, then the sum of the positive divisors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>31</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>**

**Detailed Solution:**

<p>Given that variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>p</mi><mi>q</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#8712;</mo><mfenced close="}" open="{"><mrow><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>0</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>1</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>2</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>3</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mo>-</mo><mn>5</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>3</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>4</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> case)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mn>5</mn></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> case)</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn></math></p><p>We know that variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><msub><mi>f</mi><mi>i</mi></msub><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><menclose notation="top"><mi>x</mi></menclose></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mstyle displaystyle="true"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><msub><mi>f</mi><mi>i</mi></msub></mrow></mfrac></math></p><p>Variance<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><msup><mn>0</mn><mn>2</mn></msup><mo>&#215;</mo><mn>6</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>1</mn><mn>2</mn></msup><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>&#215;</mo><mn>1</mn></mrow><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>36</mn></mfrac><mo>&#215;</mo><mfenced><mrow><mn>5</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>27</mn><mo>+</mo><mn>32</mn><mo>+</mo><mn>25</mn></mrow></mfenced><mo>=</mo><mfrac><mn>105</mn><mn>18</mn></mfrac><mo>=</mo><mfrac><mn>35</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mn>35</mn></math></p><p>Sum of divisors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>35</mn><mo>=</mo><mn>48</mn></math></p><p>Option <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced></math> is correct.</p>

</details>

---

### Q17. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the probability that the random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> takes values <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>k</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is a constant, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#8805;</mo><mn>2</mn><mo>)</mo></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>27</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>18</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>18</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>20</mn><mn>27</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>27</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The probability that the random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> takes values <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>k</mi><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><msup><mn>3</mn><mrow><mo>-</mo><mi>x</mi></mrow></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is a constant,</p><p> Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>0</mn><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mi>x</mi><mo>=</mo><mn>2</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>k</mi><msup><mn>3</mn><mn>0</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><msup><mn>3</mn><mn>1</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>k</mi></mrow><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Now finding,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Now on subtracting above two equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mi>S</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p><p>Now finding,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#8805;</mo><mn>2</mn><mo>)</mo><mo>=</mo><mi>P</mi><mo>(</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi>P</mi><mo>(</mo><mn>3</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#8805;</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mo>(</mo><mn>0</mn><mo>)</mo><mo>-</mo><mi>P</mi><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#8805;</mo><mn>2</mn><mo>)</mo><mo>=</mo><mn>1</mn><mo>-</mo><mfenced><mrow><mfrac><mi>k</mi><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>20</mn><mn>27</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>27</mn></mfrac></math></p></blockquote>

</details>

---

### Q18. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

In a binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">B</mi><mo>(</mo><mi>n</mi><mo>,</mo><mi>p</mi><mo>)</mo></math>, the sum and product of the mean &amp; variance are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> respectively, then find <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>(</mo><mi>n</mi><mo>+</mo><mi>p</mi><mo>-</mo><mi>q</mi><mo>)</mo></math> is equal to :-

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>51</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>53</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math>**

**Detailed Solution:**

<p>For the binomial distribution <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>(</mo><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>p</mi><mo>)</mo></math>,</p><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi></math> and Variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mi>q</mi></math></p><p>Sum of mean and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mo>+</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mi>p</mi><mo>(</mo><mn>1</mn><mo>+</mo><mi>q</mi><mo>)</mo><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><msup><mi>p</mi><mn>2</mn></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>25</mn></math>     ....(1)</p><p>Product of mean and variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mo>.</mo><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><msup><mi>p</mi><mn>2</mn></msup><mi>q</mi><mo>=</mo><mn>6</mn></math>      ....(2)</p><p>Put the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup><msup><mi>p</mi><mn>2</mn></msup></math> from equation (2) into equation (1):</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mi>q</mi></mfrac><mo>(</mo><mn>1</mn><mo>+</mo><mi>q</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>q</mi><mn>2</mn></msup><mo>+</mo><mn>12</mn><mi>q</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>25</mn><mi>q</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><msup><mi>q</mi><mn>2</mn></msup><mo>-</mo><mn>13</mn><mi>q</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mn>3</mn><mi>q</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>q</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>q</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>q</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math> accepted</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>p</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>n</mi><mo>&#183;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mi>n</mi><mo>&#183;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#183;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn><mi>n</mi></mrow><mn>9</mn></mfrac><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>9</mn></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>(</mo><mi>n</mi><mo>+</mo><mi>p</mi><mo>-</mo><mi>q</mi><mo>)</mo><mo>=</mo><mn>6</mn><mfenced><mrow><mn>9</mn><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><mn>52</mn></math></p>

</details>

---

### Q19. JEE Main 2023 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

There rotten apples are mixed accidently with seven good apples and four apples are drawn one by one without replacement. Let the random variable X denote the number of rotten apples. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> represent mean and variance of X, respectively, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mi>&#956;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#963;</mi><mn>2</mn></msup></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>**

**Detailed Solution:**

<p>There rotten apples are mixed accidently with seven good apples,</p><p>And four apples are drawn one by one without replacement.</p><p>Now the random variable X denote the number of rotten apples.</p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> represent mean and variance of X, respectively, </p><p>So, now plotting the table of given data we get,</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>P</mi><mo>(</mo><mi>X</mi><mo>)</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mi>P</mi><mo>(</mo><mi>X</mi><mo>)</mo></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>10</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>10</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><mn>10</mn></mfrac></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>30</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>10</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>30</mn></mfrac></math></td>		</tr>	</tbody></table><p>Now mean is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><mi>x</mi><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mfrac><mn>6</mn><mn>2</mn></mfrac><mo>=</mo><mi>&#956;</mi></math></p><p>And variance is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mo>&#8721;</mo><msup><mi>x</mi><mn>2</mn></msup><mi>P</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>-</mo><msup><mi>&#956;</mi><mn>2</mn></msup></math></p><p>So, by putting the value from above table we get,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#956;</mi><mn>2</mn></msup><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>9</mn><mn>30</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mfenced><mrow><msup><mi>&#963;</mi><mn>2</mn></msup><mo>+</mo><msup><mi>&#956;</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>20</mn></math></p>

</details>

---

### Q20. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

A bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> white and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> black balls. Three balls are drawn at random from the bag. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the number of white balls, among the drawn balls. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup></math> is the variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **56**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi><mo>=</mo></math> Number of white ball drawn,</p><p>And bag contains <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> white and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> black balls, total <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> balls are to be drawn,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>10</mn></mfrac></math></p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><mo>&#215;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>30</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"></math></p><table border="1" cellpadding="1" cellspacing="1" style="width: 200px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>X</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>10</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>30</mn></mfrac></math></td>		</tr>	</tbody></table><p>So, variance <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mo>&#8721;</mo><msub><mi>P</mi><mi>i</mi></msub><msubsup><mi>X</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><msup><mfenced><mrow><mo>&#8721;</mo><msub><mi>P</mi><mi>i</mi></msub><msub><mi>X</mi><mi>i</mi></msub></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>10</mn></mfrac><mo>-</mo><msup><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>56</mn><mn>100</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>100</mn><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>56</mn></math></p><p> </p></blockquote>

</details>

---

### Q21. JEE Main 2022 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A six faced die is biased such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>&#215;</mo><mi>P</mi></math>(a prime number)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#215;</mo><mi>P</mi></math>(a composite number)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mo>&#215;</mo><mi>P</mi><mfenced><mn>1</mn></mfenced></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a random variable that counts the number of times one gets a perfect square on some throws of this die. If the die is thrown twice, then the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>11</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>11</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>11</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>11</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>11</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>P</mi><mfenced><mtext>a&#160;prime&#160;number</mtext></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mtext>a&#160;composite&#160;number</mtext></mfenced></mrow><mn>1</mn></mfrac><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mn>1</mn></mfenced></mrow><mn>3</mn></mfrac><mo>=</mo><mi>k</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(a prime number)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mi>k</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math> (a composite number)<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>k</mi></math>,</p><p>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mn>1</mn></mfenced><mo>=</mo><mn>3</mn><mi>k</mi></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>k</mi><mo>+</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>3</mn><mi>k</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mtext>success</mtext><mo>)</mo><mo>=</mo><mi>P</mi><mfenced><mrow><mn>1</mn><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>3</mn><mi>k</mi><mo>+</mo><mi>k</mi><mo>=</mo><mfrac><mn>4</mn><mn>11</mn></mfrac></math></p><p>Number of trials, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> required mean<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>4</mn><mn>11</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>11</mn></mfrac></math></p></blockquote>

</details>

---

### Q22. JEE Main 2022 (27 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>E</mi><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>&#8230;</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math> be a sample space of raddom experiment such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><msub><mi>E</mi><mi>n</mi></msub></mfenced><mo>=</mo><mfrac><mi>n</mi><mn>36</mn></mfrac></math> for every <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>&#8230;</mo><mo>.</mo><mn>8</mn></math>. Then the number of elements in the set <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>A</mi><mo>&#8834;</mo><mi>S</mi><mo>:</mo><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#8805;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></mrow></mfenced></math> is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **19**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#8805;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is subset of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> can have elements;</p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>:<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow></mrow></mfenced></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><msub><mi>E</mi><mn>1</mn></msub></mfenced><mo>,</mo><mfenced open="{" close="}"><msub><mi>E</mi><mn>2</mn></msub></mfenced><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced open="{" close="}"><msub><mi>E</mi><mn>8</mn></msub></mfenced></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub></mrow></mfenced><mo>,</mo><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>3</mn></msub></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8942;</mo></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>E</mi><mn>5</mn></msub></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>4</mn></msub><mo>,</mo><msub><mi>E</mi><mn>5</mn></msub><mo>,</mo><msub><mi>E</mi><mn>6</mn></msub><mo>,</mo><msub><mi>E</mi><mn>7</mn></msub><mo>,</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>E</mi><mn>6</mn></msub></mrow></mfenced><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>3</mn></msub><mo>,</mo><msub><mi>E</mi><mn>4</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>E</mi><mn>7</mn></msub></mrow></mfenced><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo><msub><mi>E</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math></p><p>type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>1</mn></msub><mo>,</mo><msub><mi>E</mi><mn>2</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>&#8805;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math>;</p><p>Note: Type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> to Type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> elements can not be in set <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> as maximum probability of type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> elements.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>5</mn></msub><mo>,</mo><msub><mi>E</mi><mn>6</mn></msub><mo>,</mo><msub><mi>E</mi><mn>7</mn></msub><mo>,</mo><msub><mi>E</mi><mn>8</mn></msub></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>36</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><mn>36</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>36</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>13</mn><mn>18</mn></mfrac><mo>&#60;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p>Now for Type <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> acceptable elements let&#39;s call probability as <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>5</mn></msub><mo>=</mo><mfrac><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><mo>+</mo><msub><mi>n</mi><mn>3</mn></msub><mo>+</mo><msub><mi>n</mi><mn>4</mn></msub><mo>+</mo><msub><mi>n</mi><mn>5</mn></msub></mrow><mn>36</mn></mfrac><mo>&#8805;</mo><mfrac><mn>4</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>2</mn></msub><mo>+</mo><msub><mi>n</mi><mn>3</mn></msub><mo>+</mo><msub><mi>n</mi><mn>4</mn></msub><mo>+</mo><msub><mi>n</mi><mn>3</mn></msub><mo>&#8805;</mo><mn>28</mn><mo>.</mo><mn>8</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> possible ways <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><msub><mi>E</mi><mn>5</mn></msub><mo>,</mo><msub><mi>E</mi><mn>6</mn></msub><mo>,</mo><msub><mi>E</mi><mn>7</mn></msub><mo>,</mo><msub><mi>E</mi><mn>8</mn></msub><mo>,</mo><msub><mi>E</mi><mn>3</mn></msub><mo>&#160;</mo><mi>or</mi><mo>&#160;</mo><msub><mi>E</mi><mn>4</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>6</mn></msub><mo>=</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>3</mn></msub><mo>+</mo><msub><mi>n</mi><mn>4</mn></msub><mo>+</mo><msub><mi>n</mi><mn>3</mn></msub><mo>+</mo><msub><mi>n</mi><mn>6</mn></msub><mo>&#8805;</mo><mn>28</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>9</mn></math> possible ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>7</mn></msub><mo>&#8658;</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>n</mi><mn>7</mn></msub><mo>&#8805;</mo><mn>28</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>7</mn></math> possible ways</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>8</mn></msub><mo>&#8658;</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>n</mi><mi>n</mi></msub><mo>&#8805;</mo><mn>28</mn><mo>.</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>1</mn></math> possible way</p><p>Total <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>19</mn></math></p>

</details>

---

### Q23. JEE Main 2022 (24 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>A random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> has the following probability distribution:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>X</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>k</mi></math></td>		</tr>	</tbody></table><p>The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mrow><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mrow><mrow><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfrac></mfenced></math>is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>7</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>7</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>7</mn></mfrac></math>**

**Detailed Solution:**

<p>To find <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mrow><mn>1</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>4</mn></mrow><mrow><mi>x</mi><mo>&#8804;</mo><mn>2</mn></mrow></mfrac></mfenced></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><mi>B</mi></mfrac></mfenced></math></p><p>We know that</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mfrac><mi>A</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mi>B</mi></mfenced></mrow></mfrac></math></p><p>Given</p><table border="1" cellpadding="1" cellspacing="1" style="width: 300px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>x</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>k</mi></math></td>		</tr>	</tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>A</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mn>2</mn><mo>,</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mfenced close="}" open="{"><mrow><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>A</mi><mo>&#8745;</mo><mi>B</mi></mrow></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>B</mi></mfenced><mo>=</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;&#160;</mo><mi>P</mi><mfenced><mfrac><mi>A</mi><mi>B</mi></mfrac></mfenced><mo>=</mo><mfrac><mrow><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mi>k</mi></mrow><mrow><mi>k</mi><mo>+</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>4</mn><mi>k</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><mi>k</mi></mrow><mrow><mn>7</mn><mi>k</mi></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>7</mn></mfrac></math></p><p>Hence option <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> is correct.</p>

</details>

---

### Q24. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a random variable with distribution.</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mi>x</mi><mo>)</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></td>		</tr>	</tbody></table><p>If the mean of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><mn>3</mn></math> and variance of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msup><mi>&#963;</mi><mn>2</mn></msup></math> is equal to :</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **781**

**Detailed Solution:**

<p>Given mean is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#956;</mi><mo>=</mo><mo>&#8721;</mo><msub><mi>p</mi><mi>i</mi></msub><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mn>2</mn><mo>.</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mn>5</mn></mfrac><mo>-</mo><mi>a</mi><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>+</mo><mn>6</mn><mi mathvariant="normal">b</mi><mo>=</mo><mn>2</mn><mo>.</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>b</mi><mo>-</mo><mi>a</mi><mo>=</mo><mn>0</mn><mo>.</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Also <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msub><mi>p</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mi>a</mi><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mfrac><mn>4</mn><mn>15</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>Solving, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>Variance is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mo>&#8721;</mo><msub><mi>p</mi><mi>i</mi></msub><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup><mo>-</mo><msup><mi>&#956;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>(</mo><mn>4</mn><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>(</mo><mn>1</mn><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>(</mo><mn>9</mn><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>(</mo><mn>16</mn><mo>)</mo><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>(</mo><mn>36</mn><mo>)</mo><mo>-</mo><mn>5</mn><mo>.</mo><mn>29</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>7</mn><mo>.</mo><mn>81</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>100</mn><msup><mi>&#963;</mi><mn>2</mn></msup><mo>=</mo><mn>781</mn></math></p>

</details>

---

### Q25. JEE Main 2021 (27 Aug Shift 2)

*Type:* `numerical` | *Level:* `1`

<p>The probability distribution of random variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is given by:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi><mo>)</mo></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>K</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>K</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>K</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></td>		</tr>	</tbody></table><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mi>P</mi><mo>(</mo><mn>1</mn><mo>&#60;</mo><mi>X</mi><mo>&#60;</mo><mn>4</mn><mo>&#8739;</mo><mi>X</mi><mo>&#60;</mo><mn>3</mn><mo>)</mo></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>p</mi><mo>=</mo><mi>&#955;</mi><mi>K</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#931;</mi><mi>P</mi><mo>(</mo><mi>X</mi><mo>)</mo><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>K</mi><mo>+</mo><mn>2</mn><mi>K</mi><mo>+</mo><mn>2</mn><mi>K</mi><mo>+</mo><mn>3</mn><mi>K</mi><mo>+</mo><mi>K</mi><mo>=</mo><mn>1</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mi>P</mi><mo>(</mo><mn>1</mn><mo>&#60;</mo><mi>X</mi><mo>&#60;</mo><mn>4</mn><mo>&#8739;</mo><mi>X</mi><mo>&#60;</mo><mn>3</mn><mo>)</mo><mo>=</mo><mfrac><mrow><mi>P</mi><mo>(</mo><mi>X</mi><mo>=</mo><mn>2</mn><mo>)</mo></mrow><mrow><mi>P</mi><mo>(</mo><mi>X</mi><mo>&#60;</mo><mn>3</mn><mo>)</mo></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>=</mo><mfrac><mfrac><mrow><mn>2</mn><mi>K</mi></mrow><mrow><mn>9</mn><mi>K</mi></mrow></mfrac><mrow><mfrac><mi>K</mi><mrow><mn>9</mn><mi>K</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mrow><mn>9</mn><mi>K</mi></mrow></mfrac></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>P</mi><mo>=</mo><mi>&#955;</mi><mi>K</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mi>&#955;</mi><mo>&#215;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>30</mn></math>

</details>

---

### Q26. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be a random variable such that the probability function of a distribution is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mi>j</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><msup><mn>3</mn><mi>j</mi></msup></mfrac><mfenced><mrow><mi>j</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced><mo>.</mo></math> Then the mean of the distribution and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mo>(</mo><mi>X</mi></math> is positive and even<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo></math> respectively, are:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>16</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>**

**Detailed Solution:**

We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mi>j</mi></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><msup><mn>3</mn><mi>j</mi></msup></mfrac><mfenced><mrow><mi>j</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mo>&#8734;</mo></mrow></mfenced></math><p>Mean <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>&#931;</mi><msub><mi>X</mi><mi>i</mi></msub><msub><mi>P</mi><mi>i</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mi>r</mi><mo>&#183;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mi>r</mi></msup></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is even) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8734;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>9</mn></mfrac></mstyle><mstyle displaystyle="true"><mfrac><mn>8</mn><mn>9</mn></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q27. JEE Main 2020 (05 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

Four fair dice are thrown independently 27 times. Then the expected number of times, at least two dice show up a three or a five, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **11**

**Detailed Solution:**

<p>There are only two outcomes, success which stands for getting either 3 or 5, and failure, stands for getting any other outcome.</p><p>Probability for success<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>p</mi><mo>=</mo><mfrac><mn>2</mn><mn>6</mn></mfrac></math></p><p>Probability for failure<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>q</mi><mo>=</mo><mfrac><mn>4</mn><mn>6</mn></mfrac></math></p><p>Number of trials<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>=</mo><mn>27</mn></math></p><p>Number of dice<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn></math></p><p>Using Binomial Probability,</p><p>P(at least 2 shows 3 or 5) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mo>&#183;</mo><msup><mfenced><mfrac><mn>2</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><msup><mfenced><mfrac><mn>4</mn><mn>6</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup><mfenced><mfrac><mn>4</mn><mn>6</mn></mfrac></mfenced><mo>+</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mfrac><mn>2</mn><mn>6</mn></mfrac></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>384</mn><mo>+</mo><mn>128</mn><mo>+</mo><mn>16</mn></mrow><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>27</mn></mfrac></math></p><p>Expectation is numerically same as mean.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> expectation<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mi>p</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>27</mn><mo>&#183;</mo><mfrac><mn>11</mn><mn>27</mn></mfrac><mo>=</mo><mn>11</mn></math></p>

</details>

---

### Q28. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A random variable <math><mi>X</mi></math> has the following probability distribution:
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable><mtr><mtd><mtable><mtr><mtd><mi>X</mi><mo>:</mo></mtd><mtd><mn>1</mn></mtd><mtd><mtable><mtr><mtd><mn>2</mn></mtd><mtd><mn>3</mn></mtd><mtd><mtable><mtr><mtd><mn>4</mn></mtd><mtd><mn>5</mn></mtd></mtr></mtable></mtd></mtr></mtable></mtd></mtr></mtable></mtd></mtr><mtr><mtd><mi>P</mi><mfenced separators="|"><mi>X</mi></mfenced><mo>:</mo><mo>&#160;</mo><mtable><mtr><mtd><msup><mi>k</mi><mn>2</mn></msup></mtd><mtd><mtable><mtr><mtd><mn>2</mn><mi>k</mi></mtd><mtd><mi>k</mi></mtd><mtd><mtable><mtr><mtd><mn>2</mn><mi>k</mi></mtd><mtd><mn>5</mn><msup><mi>k</mi><mn>2</mn></msup></mtd></mtr></mtable></mtd></mtr></mtable></mtd></mtr></mtable></mtd></mtr></mtable></math>
Then, <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#62;</mo><mn>2</mn></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>12</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>23</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>23</mn></mrow><mrow><mn>36</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>W e know <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8721;</mo><msub><mi>P</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mn>6</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>k</mi><mo>=</mo><mn>1</mn></math></p><p><math><mn>6</mn><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>5</mn><mi>k</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math><mn>6</mn><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>6</mn><mi>k</mi><mo>-</mo><mi>k</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p><math><mfenced separators="|"><mrow><mn>6</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi></mi><mfenced separators="|"><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> (rejected) ; <math><mi>k</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#62;</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mi>k</mi><mo>+</mo><mn>2</mn><mi>k</mi><mo>+</mo><mn>5</mn><msup><mi>k</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>36</mn></mfrac><mo>=</mo><mfrac><mrow><mn>6</mn><mo>+</mo><mn>12</mn><mo>+</mo><mn>5</mn></mrow><mn>36</mn></mfrac><mo>=</mo><mfrac><mn>23</mn><mn>36</mn></mfrac></math></p>

</details>

---

### Q29. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

An unbiased coin is tossed <math><mn>5</mn></math> times. Suppose that a variable <math><mi>X</mi></math> is assigned the value <math><mi>k</mi></math> when <math><mi>k</mi></math> consecutive heads are obtained for <math><mi>k</mi><mo>=</mo><mn>3</mn><mo>,</mo><mi></mi><mn>4</mn><mo>,</mo><mi></mi><mn>5</mn><mo>,</mo><mi></mi></math> otherwise <math><mi>X</mi></math> takes the value <math><mo>-</mo><mn>1</mn><mo>.</mo></math> Then the expected value of <math><mi>X</mi><mo>,</mo><mi></mi></math> is

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(D)** <math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> represents the number of consecutive heads and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>k</mi></mfenced></math> is the corresponding probability while an unbiased coin is tossed <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> times, then</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;">	<tbody>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td>		</tr>		<tr>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced><mi>k</mi></mfenced></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>12</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>			<td><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></td>		</tr>	</tbody></table><p>Now, the expected value of variable <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>12</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mfrac><mn>11</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfenced><mn>3</mn></mfenced><mfrac><mn>5</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfenced><mn>4</mn></mfenced><mfrac><mn>2</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfenced><mn>5</mn></mfenced><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mn>12</mn><mo>-</mo><mn>11</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>28</mn><mo>-</mo><mn>24</mn></mrow><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>=</mo><mfrac><mn>4</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math></p>

</details>

---

### Q30. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A person throws two fair dice. He wins Rs. <math><mn>15</mn></math> for throwing a doublet (same numbers on the two dice), wins Rs <math><mn>12</mn></math> when the throw results in the sum of <math><mn>9</mn></math> , and loses Rs. <math><mn>6</mn></math> for any other outcome on the throw. Then the expected gain/loss (in Rs.) of the person is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> loss
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> gain
- **(C)** 2 gain
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> loss

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math> loss**

**Detailed Solution:**

win Rs. <math><mn>15</mn><mo>&#8594;</mo></math> number of cases <math><mo>=</mo><mn>6</mn></math>
win Rs.<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mn>12</mn><mo>&#8594;</mo></math> number of cases <math><mi>&#160;</mi><mo>=</mo><mn>4</mn></math>
loss Rs. <math><mn>6</mn><mo>&#8594;</mo></math> number of cases <math><mo>=</mo><mn>26</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> (expected gain/loss) <math><mi>&#160;</mi><mo>=</mo><mn>15</mn><mo>&#215;</mo><mfrac><mrow><mn>6</mn></mrow><mrow><mn>36</mn></mrow></mfrac><mo>+</mo><mn>12</mn><mo>&#215;</mo><mfrac><mrow><mn>4</mn></mrow><mrow><mn>36</mn></mrow></mfrac><mo>-</mo><mn>6</mn><mo>&#215;</mo><mfrac><mrow><mn>26</mn></mrow><mrow><mn>36</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

</details>

---

### Q31. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

In a game, a man wins Rs. <math><mn>100</mn></math> if he gets <math><mn>5</mn></math> or <math><mn>6</mn></math> on a throw of a fair die and loses Rs. <math><mn>50</mn></math> for getting any other number on the die. If he decides to throw the die either till he gets a five or a six or to a maximum of three throws, then his expected gain/loss (in rupees) is :

**Options:**

- **(A)** <math><mfrac><mrow><mn>400</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>  gain
- **(B)** <math><mfrac><mrow><mn>400</mn></mrow><mrow><mn>9</mn></mrow></mfrac></math>  gain
- **(C)** <math><mfrac><mrow><mn>400</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>  loss
- **(D)** <math><mn>0</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>0</mn></math>**

**Detailed Solution:**

<p>Probability of success i.e. getting a <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>=</mo><mi>P</mi><mfenced><mi>s</mi></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math>.</p><p>So, probability of failure i.e. getting any number other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mo>=</mo><mi>P</mi><mfenced><mi>f</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced><mi>s</mi></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></math>.</p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> be the amount that a man wins in a maximum of three throws.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> can take values :</p><p>Case I : First two throws are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, game stops</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>X</mi><mo>=</mo><mn>100</mn><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>100</mn></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Case II : First throw is other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and second and third throws are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>, game stops</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>X</mi><mo>=</mo><mn>50</mn><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>50</mn></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>9</mn></mfrac></math></p><p>Case III : First two throws are other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and last throw is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>X</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mn>0</mn></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>27</mn></mfrac></math></p><p>Case IV : All three throws are other than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>X</mi><mo>=</mo><mo>-</mo><mn>150</mn><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mi>X</mi><mo>=</mo><mo>-</mo><mn>150</mn></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>27</mn></mfrac></math></p><p>Therefore, expected gain or loss</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>E</mi><mfenced separators="|"><mi>X</mi></mfenced><mo>=</mo><mn>100</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mn>50</mn><mo>&#215;</mo><mfrac><mn>2</mn><mn>9</mn></mfrac><mo>+</mo><mn>0</mn><mo>&#215;</mo><mfrac><mn>4</mn><mn>27</mn></mfrac><mo>-</mo><mn>150</mn><mo>&#215;</mo><mfrac><mn>8</mn><mn>27</mn></mfrac><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q32. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

A bag contains 30 white balls and 10 red balls. 16 balls are drawn one by one randomly from the bag with replacement. If $X$ be the number of white balls drawn, then

$\left(\frac{\text { mean of } \mathrm{X}}{\text { standard deviation of } \mathrm{X}}\right)$ is equal to:

**Options:**

- **(A)** 4
- **(B)** $4 \sqrt{3}$
- **(C)** $3 \sqrt{2}$
- **(D)** $\frac{4 \sqrt{3}}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $4 \sqrt{3}$**

**Detailed Solution:**

$P($ white ball $)=\frac{30}{40}=\frac{3}{4}, Q$ (red ball) $=\frac{10}{40}=\frac{1}{4}, n=16$

$\frac{\text { Mean of } X}{\text { standard deviation of } X}=\frac{n P}{\sqrt{n P Q}}=\frac{\sqrt{n P}}{\sqrt{Q}}$ $=\sqrt{\frac{16 \times \frac{3}{4}}{\frac{1}{4}}}=\sqrt{48}=4 \sqrt{3}$

</details>

---

### Q33. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Two cards are drawn successively with replacement from a well-shuffled deck of <math><mn>52</mn></math> cards. Let <math><mi>X</mi></math> denote the random variable of number of aces obtained in the two drawn cards. Then <math><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>=</mo><mn>2</mn></mrow></mfenced></math> equals:

**Options:**

- **(A)** <math><mfrac><mrow><mn>24</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>52</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>49</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>25</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>25</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>**

**Detailed Solution:**

Using the concept of complementary events,

<math><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mi>P</mi><mfenced separators="|"><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow></mfenced></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>48</mn></mrow><mrow><mn>52</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>48</mn></mrow><mrow><mn>52</mn></mrow></mfrac></math>

<math><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>144</mn></mrow><mrow><mn>169</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>25</mn></mrow><mrow><mn>169</mn></mrow></mfrac></math>

</details>

---

### Q34. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the mean and the variance of a binomial variate <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math>  are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn></math> respectively, then the probability that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math> takes a value greater than or equal to one is:

**Options:**

- **(A)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>9</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>15</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><mi>n</mi><mi>p</mi><mo>=</mo><mn>2</mn></math>

<math><mi>n</mi><mi>p</mi><mi>q</mi><mo>=</mo><mn>1</mn></math>

<math><mo>&#8756;</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>p</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>q</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>

<math><mi>n</mi><mo>=</mo><mn>4</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi><mfenced separators="|"><mrow><mi>X</mi><mo>&#8805;</mo><mn>1</mn></mrow></mfenced><mo>=</mo><msup><mrow><mn>1</mn><mo>-</mo><mi>&#160;</mi></mrow><mn>4</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mi>&#160;</mi><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>0</mn></msup></math>

<math><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>15</mn></mrow><mrow><mn>16</mn></mrow></mfrac></math>

</details>

---

### Q35. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If $X$ has a binomial distribution, $B(n, p)$ with parameters $n$ and $p$ such that $P(X=2)=P(X=3)$, then $\mathrm{E}(\mathrm{X})$, the mean of variable $\mathrm{X}$, is

**Options:**

- **(A)** $2-\mathrm{p}$
- **(B)** $3-p$
- **(C)** $\frac{\mathrm{p}}{2}$
- **(D)** $\frac{p}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3-p$**

**Detailed Solution:**

Since $\mathrm{X}$ has a binomial distribution, $\mathrm{B}(n$,
p)
$$
\begin{aligned}
&\therefore \mathrm{P}(X=2)={ }^n \mathrm{C}_2(p)^2(1-p)^{n-2} \\
&\text { and } \mathrm{P}(X=3)={ }^n \mathrm{C}_3(p)^3(1-p)^{n-3} \\
&\text { Given } \mathrm{P}(X=2)=\mathrm{P}(X=3) \\
&\Rightarrow{ }^n \mathrm{C}_2 p^2(1-p)^{n-2}={ }^n \mathrm{C}_3(p)^3(1-p)^{n-3} \\
&\Rightarrow \frac{n !}{2 !(n-2) !} \cdot \frac{p^2(1-p)^n}{(1-p)^2} \\
&=\frac{n !}{3 !(n-3) !} \cdot \frac{p^3(1-p)^n}{(1-p)^3}
\end{aligned}
$$

$$
\begin{aligned}
&\Rightarrow \frac{1}{n-2}=\frac{1}{3} \cdot \frac{p}{1-p} \\
&\Rightarrow 3(1-p)=p(n-2) \\
&\Rightarrow 3-3 p=n p-2 p \\
&\Rightarrow n p=3-p \\
&\Rightarrow \mathrm{E}(X)=\text { mean }=3-p \\
&(\because \text { mean of } \mathrm{B}(n, p)=n p)
\end{aligned}
$$

</details>

---

### Q36. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

At a telephone enquiry system the number of phone cells regarding relevant enquiry follow Poisson distribution with an average of 5 phone calls during 10-minute time intervals. The probability that there is at the most one phone call during a 10-minute time period is

**Options:**

- **(A)** $\frac{6}{5^{\mathrm{e}}}$
- **(B)** $\frac{5}{6}$
- **(C)** $\frac{6}{55}$
- **(D)** $\frac{6}{e^5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{6}{e^5}$**

**Detailed Solution:**

$P(X=r)=\frac{e^{-m} m^r}{r !}$
$P(X \leq 1)=P(X=0)+P(X=1)$
$=e^{-5}+5 \times e^{-5}=\frac{6}{e^5}$

</details>

---

### Q37. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has Poisson distribution with mean 2. Then $P(X>1.5)$ equals

**Options:**

- **(A)** $\frac{2}{\mathrm{e}^2}$
- **(B)** 0
- **(C)** $1-\frac{3}{\mathrm{e}^2}$
- **(D)** $\frac{3}{\mathrm{e}^2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $1-\frac{3}{\mathrm{e}^2}$**

**Detailed Solution:**

$$
\begin{aligned}
& P(x=k)=e^{-\lambda} \frac{\lambda^k}{k !} \\
& P(x \geq 2)=1-P(x=0)-P(x=1) \\
& =1-e^{-\lambda}-e^{-\lambda}\left(\frac{\lambda}{1 !}\right) \\
& =1-\frac{3}{e^2} .
\end{aligned}
$$

</details>

---

### Q38. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

A random variable $X$ has the probability distribution:
\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline \mathrm{X}: & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline \mathrm{p}(\mathrm{X}): & 0.15 & 0.23 & 0.12 & 0.10 & 0.20 & 0.08 & 0.07 & 0.05 \\
\hline
\end{array}
For the events $E=\{X$ is a prime number $\}$ and $F=\{X < 4\}$, the probability $P(E \cup F)$ is

**Options:**

- **(A)** $0.87$
- **(B)** $0.77$
- **(C)** $0.35$
- **(D)** $0.50$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $0.77$**

**Detailed Solution:**

$P(E \cup F)=P(E)+P(F)-P(E \cap F)=0.62+0.50-0.35=0.77$

</details>

---

### Q39. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

A die is tossed 5 times. Getting an odd number is considered a success. Then the variance of distribution of success is

**Options:**

- **(A)** 8/3
- **(B)** 3/8
- **(C)** 4/5
- **(D)** 5/4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 5/4**

**Detailed Solution:**

The event follows binomial distribution with n = 5, p = 3/6 = 1/2
$q=1-p=1 / 2 \quad \therefore$ Variance $n p q=5 / 4$

</details>

---

