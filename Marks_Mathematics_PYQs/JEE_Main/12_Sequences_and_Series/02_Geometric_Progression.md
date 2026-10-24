# JEE Main Mathematics - Sequences and Series

## Topic 2: Geometric Progression

**Total Questions:** 62

---

### Q1. JEE Main 2026 (06 April Shift 1)

*Type:* `numerical` | *Level:* `2`

For the functions $f(\theta) = \alpha\tan^2\theta + \beta\cot^2\theta$, and $g(\theta) = \alpha\sin^2\theta + \beta\cos^2\theta$, $\alpha > \beta > 0$, let $\min_{0 < \theta < \pi/2}f(\theta) = \max_{0 < \theta < \pi}g(\theta)$. If the first term of a G.P. is $\left(\dfrac{\alpha}{2\beta}\right)$, its common ratio is $\left(\dfrac{2\beta}{\alpha}\right)$ and the sum of its first $10$ terms is $\dfrac{m}{n}$, $\gcd(m, n) = 1$, then $m + n$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1279**

**Detailed Solution:**

For the function $f(\theta) = \alpha\tan^2\theta + \beta\cot^2\theta$, applying the AM-GM inequality gives:

$\alpha\tan^2\theta + \beta\cot^2\theta \ge 2\sqrt{\alpha\tan^2\theta \cdot \beta\cot^2\theta} = 2\sqrt{\alpha\beta}$

Thus, $\min_{0 < \theta < \pi/2} f(\theta) = 2\sqrt{\alpha\beta}$.

For the function $g(\theta) = \alpha\sin^2\theta + \beta\cos^2\theta$, we can rewrite it as:

$g(\theta) = \alpha\sin^2\theta + \beta(1 - \sin^2\theta) = \beta + (\alpha - \beta)\sin^2\theta$

Since $\alpha > \beta > 0$, the maximum value of $g(\theta)$ occurs when $\sin^2\theta$ is maximum, which is $1$ (at $\theta = \pi/2$).

Thus, $\max_{0 < \theta < \pi} g(\theta) = \beta + (\alpha - \beta)(1) = \alpha$.

Given that $\min f(\theta) = \max g(\theta)$, we have:

$2\sqrt{\alpha\beta} = \alpha$

Squaring both sides (since $\alpha > 0$), we get:

$4\alpha\beta = \alpha^2 \Rightarrow \alpha = 4\beta$

For the given Geometric Progression (G.P.):

First term $a = \dfrac{\alpha}{2\beta} = \dfrac{4\beta}{2\beta} = 2$

Common ratio $r = \dfrac{2\beta}{\alpha} = \dfrac{2\beta}{4\beta} = \dfrac{1}{2}$

The sum of the first $10$ terms is:

$S_{10} = a\dfrac{1 - r^{10}}{1 - r} = 2\dfrac{1 - (1/2)^{10}}{1 - 1/2} = 4\left(1 - \dfrac{1}{1024}\right) = 4\left(\dfrac{1023}{1024}\right) = \dfrac{1023}{256}$

We are given $S_{10} = \dfrac{m}{n}$ with $\gcd(m, n) = 1$.

Since $256 = 2^8$ and $1023$ is odd, they are coprime. Therefore, $m = 1023$ and $n = 256$.

$m + n = 1023 + 256 = 1279$

Answer: $1279$

</details>

---

### Q2. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha=\dfrac{1}{4}+\dfrac{1}{8}+\dfrac{1}{16}+\ldots\infty$ and $\beta=\dfrac{1}{3}+\dfrac{1}{9}+\dfrac{1}{27}+\ldots\infty$. Then the value of $(0.2)^{\log_{\sqrt{5}}(\alpha)}+(0.04)^{\log_5(\beta)}$ is equal to:

**Options:**

- **(A)** $4$
- **(B)** $5$
- **(C)** $8$
- **(D)** $25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $8$**

**Detailed Solution:**

The sum of an infinite geometric progression is given by $S_{\infty} = \dfrac{a}{1-r}$.

For $\alpha$, $a = \dfrac{1}{4}$ and $r = \dfrac{1}{2}$:
$\alpha = \dfrac{\dfrac{1}{4}}{1 - \dfrac{1}{2}} = \dfrac{1}{2}$

For $\beta$, $a = \dfrac{1}{3}$ and $r = \dfrac{1}{3}$:
$\beta = \dfrac{\dfrac{1}{3}}{1 - \dfrac{1}{3}} = \dfrac{1}{2}$

Now, evaluating the first term:
$(0.2)^{\log_{\sqrt{5}}(\alpha)} = \left(5^{-1}\right)^{\log_{5^{1/2}}(1/2)}$
Using the property $\log_{a^k}(x) = \dfrac{1}{k}\log_a(x)$:
$\log_{5^{1/2}}(1/2) = 2\log_5(1/2) = \log_5(1/4)$
Thus, $\left(5^{-1}\right)^{\log_5(1/4)} = 5^{-\log_5(1/4)} = 5^{\log_5(4)} = 4$

Evaluating the second term:
$(0.04)^{\log_5(\beta)} = \left(5^{-2}\right)^{\log_5(1/2)}$
$\left(5^{-2}\right)^{\log_5(1/2)} = 5^{-2\log_5(1/2)} = 5^{\log_5(4)} = 4$

Adding both terms:
$(0.2)^{\log_{\sqrt{5}}(\alpha)} + (0.04)^{\log_5(\beta)} = 4 + 4 = 8$

Answer: $8$

</details>

---

### Q3. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\frac{6}{3^{26}}+\frac{10 \cdot 1}{3^{25}}+\frac{10 \cdot 2}{3^{24}}+\frac{10 \cdot 2^{2}}{3^{23}}+\ldots+\frac{10 \cdot 2^{24}}{3}$ is equal to :

**Options:**

- **(A)** $2^{26}$
- **(B)** $3^{25}$
- **(C)** $3^{26}$
- **(D)** $2^{25}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2^{26}$**

**Detailed Solution:**

The sum is $\frac{6}{3^{26}} + \sum_{r=0}^{24} \frac{10 \cdot 2^r}{3^{25-r}}$
$= \frac{6}{3^{26}} + 10 \cdot \frac{1}{3^{25}} \sum_{r=0}^{24} (2 \cdot 3)^r = \frac{6}{3^{26}} + \frac{10}{3^{25}} \cdot \frac{6^{25}-1}{5}$
$= \frac{6 + 2 \cdot 3(6^{25}-1)}{3^{26}} = \frac{6 + 2 \cdot 6^{25} \cdot 3 - 6}{3^{26}} = \frac{6 \cdot 6^{25}}{3^{26}}$
$= \frac{6^{26}}{3^{26}} = \left(\frac{6}{3}\right)^{26} = 2^{26}$

</details>

---

### Q4. JEE Main 2026 (28 January Shift 1)

*Type:* `numerical` | *Level:* `2`

In a G.P., if the product of the first three terms is 27 and the set of all possible values for the sum of its first three terms is $\mathbb{R}-(a, b)$, then $a^{2}+b^{2}$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **90**

**Detailed Solution:**

In the G.P., let the first three terms be $\frac{a}{r}, a, ar$.
From the product condition: $\frac{a}{r} \cdot a \cdot ar = a^3 = 27$, so $a = 3$.
The sum of first three terms is $S = \frac{3}{r} + 3 + 3r = 3(\frac{1}{r} + 1 + r)$.
For $r > 0$, by AM-GM: $\frac{1}{r} + r \geq 2$, so $S \geq 9$.
For $r < 0$: $\frac{1}{r} + r \leq -2$.
 So $S \leq -3$.
Thus the possible values of $S$ are $(-\infty, -3] \cup [9, \infty) = \mathbb{R} - (-3, 9)$.
Therefore $(a, b) = (-3, 9)$ and $a^2 + b^2 = 9 + 81 = 90$.

</details>

---

### Q5. JEE Main 2026 (24 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\left(\frac{1}{3}+\frac{4}{7}\right)+\left(\frac{1}{3^{2}}+\frac{1}{3} \times \frac{4}{7}+\frac{4^{2}}{7^{2}}\right)+\left(\frac{1}{3^{3}}+\frac{1}{3^{2}} \times \frac{4}{7}+\frac{1}{3} \times \frac{4^{2}}{7^{2}}+\frac{4^{3}}{7^{3}}\right)+\ldots$ upto infinite terms, is equal to

**Options:**

- **(A)** $\frac{4}{3}$
- **(B)** $\frac{6}{5}$
- **(C)** $\frac{5}{2}$
- **(D)** $\frac{7}{4}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{5}{2}$**

**Detailed Solution:**

The $n$-th bracket ($n \geq 1$) is $\sum_{k=0}^{n} \left(\frac{1}{3}\right)^{n-k}\left(\frac{4}{7}\right)^k = \frac{(4/7)^{n+1} - (1/3)^{n+1}}{4/7 - 1/3} = \frac{21}{5}\left[\left(\frac{4}{7}\right)^{n+1} - \left(\frac{1}{3}\right)^{n+1}\right]$.
Total sum $= \frac{21}{5}\left[\sum_{n=2}^{\infty}\left(\frac{4}{7}\right)^n - \sum_{n=2}^{\infty}\left(\frac{1}{3}\right)^n\right] = \frac{21}{5}\left[\frac{16/49}{3/7} - \frac{1/9}{2/3}\right]$
$= \frac{21}{5}\left[\frac{16}{21} - \frac{1}{6}\right] = \frac{21}{5} \cdot \frac{25}{42} = \frac{5}{2}$.

</details>

---

### Q6. JEE Main 2026 (24 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $729,81,9,1, \ldots$ be a sequence and $\mathrm{P}_{n}$ denote the product of the first $n$ terms of this sequence. 
 If $2 \sum_{n=1}^{40}\left(\mathrm{P}_{n}\right)^{\frac{1}{n}}=\frac{3^{\alpha}-1}{3^{\beta}}$ and $\operatorname{gcd}(\alpha, \beta)=1$, 
 then $\alpha+\beta$ is equal to

**Options:**

- **(A)** 74
- **(B)** 76
- **(C)** 73
- **(D)** 75

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 73**

**Detailed Solution:**

The sequence is $3^6, 3^4, 3^2, 3^0, 3^{-2}, \ldots$ so $a_n = 3^{8-2n}$.
$P_n = \prod_{k=1}^n 3^{8-2k} = 3^{\sum_{k=1}^n(8-2k)} = 3^{8n - n(n+1)} = 3^{n(7-n)}$
$(P_n)^{1/n} = 3^{7-n}$
$2\sum_{n=1}^{40} 3^{7-n} = 2(3^6+3^5+\cdots+3^{-33}) = 2 \cdot 3^6 \cdot \frac{1-3^{-40}}{1-1/3} = 3^7 - 3^{-33}$ 
$= \frac{3^{40}-1}{3^{33}}$
So $\alpha = 40,\; \beta = 33$.
Since $\gcd(40,33)=1$, we get $\alpha+\beta = 73$.

</details>

---

### Q7. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $a_{1}, \frac{a_{2}}{2}, \frac{a_{3}}{2^{2}}, \ldots, \frac{a_{10}}{2^{9}}$ be a G.P. of common ratio $\frac{1}{\sqrt{2}}$. If $a_{1}+a_{2}+\ldots+a_{10}=62$, then $a_{1}$ is equal to :

**Options:**

- **(A)** $2-\sqrt{2}$
- **(B)** $2(2-\sqrt{2})$
- **(C)** $\sqrt{2}-1$
- **(D)** $2(\sqrt{2}-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2(\sqrt{2}-1)$**

**Detailed Solution:**

The G.P. is $a_1, \frac{a_2}{2}, \frac{a_3}{2^2}, \ldots, \frac{a_{10}}{2^9}$ with common ratio $\frac{1}{\sqrt{2}}$.
So $\frac{a_n}{2^{n-1}} = a_1 \cdot \left(\frac{1}{\sqrt{2}}\right)^{n-1}$, giving $a_n = a_1 \cdot (\sqrt{2})^{n-1}$.
$\sum_{n=1}^{10} a_n = a_1 \cdot \frac{(\sqrt{2})^{10} - 1}{\sqrt{2} - 1} = a_1 \cdot \frac{31}{\sqrt{2} - 1} = 31a_1(\sqrt{2} + 1)$.
Setting this equal to 62: $a_1 = \frac{2}{\sqrt{2}+1} = 2(\sqrt{2}-1)$.

</details>

---

### Q8. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $a_{1}, a_{2}, a_{3}, \ldots$ be G.P. of increasing positive terms such that $a_{2} \cdot a_{3} \cdot a_{4}=64$ and $a_{1}+a_{3}+a_{5}=\frac{813}{7}$. Then $a_{3}+a_{5}+a_{7}$ is equal to :

**Options:**

- **(A)** $3244$
- **(B)** $3248$
- **(C)** $3252$
- **(D)** $3256$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $3252$**

**Detailed Solution:**

Let first term be $a$ and common ratio $r > 1$.
From $a_2 \cdot a_3 \cdot a_4 = 64$: $(ar)(ar^2)(ar^3) = a^3r^6 = 64 \Rightarrow ar^2 = 4$.
From $a_1 + a_3 + a_5 = \frac{813}{7}$: $a(1 + r^2 + r^4) = \frac{813}{7}$.
Substituting $a = \frac{4}{r^2}$: $4\left(\frac{1}{r^2} + 1 + r^2\right) = \frac{813}{7}$.
Let $u = r^2$: $28u^2 - 785u + 28 = 0$ gives $u = 28$ (since $r > 1$).
$a_3 + a_5 + a_7 = ar^2(1 + r^2 + r^4) = 4(1 + 28 + 784) = 3252$.

</details>

---

### Q9. JEE Main 2025 (7 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of the second, fourth and sixth terms of a G.P. of positive terms is 21 and the sum of its eighth, tenth and twelfth terms is 15309 , then the sum of its first nine terms is :

**Options:**

- **(A)** 760
- **(B)** 755
- **(C)** 750
- **(D)** 757

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 757**

**Detailed Solution:**

$\begin{aligned} & \mathrm{ar}+\mathrm{ar}^3+\mathrm{ar}^5=21, \quad \mathrm{ar}^7+\mathrm{ar}^9+\mathrm{ar}^{11}=15309 \\ & \Rightarrow \operatorname{ar}\left(1+\mathrm{r}^2+\mathrm{r}^4\right)=21, \quad \operatorname{ar}^7\left(1+\mathrm{r}^2+\mathrm{r}^4\right)=15309\end{aligned}$
$\mathrm{Eq}^{\mathrm{n}}\left({\overline{2)} \div \mathrm{eq}^{\mathrm{n}}(1) \quad \quad \quad \text { (2) }}_{(1)}^{(2)}\right.$
$\begin{aligned} & \Rightarrow \frac{\mathrm{a} \cdot \mathrm{r}^7}{\mathrm{ar}}=\frac{15309}{21} \Rightarrow \mathrm{r}^6=729 \\ & \Rightarrow \frac{\mathrm{a} \cdot\left(\mathrm{r}^9-1\right)}{\mathrm{r}-1}=\frac{\frac{7}{91}(19683-1)}{2}=\frac{7 \times 19682}{91 \times 2} \\ & =\frac{9841}{13}=757\end{aligned}$

</details>

---

### Q10. JEE Main 2025 (7 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{x}_1, \mathrm{x}_2, \mathrm{x}_3, \mathrm{x}_4$ be in a geometric progression. $2,7,9,5$ are subtracted respectively from $x_1, x_2, x_3$ $x_4$ then the resulting numbers are in an arithmetic progression. Then the value of $\frac{1}{24}\left(x_1 x_2 x_3 x_4\right)$ is :

**Options:**

- **(A)** 72
- **(B)** 18
- **(C)** 36
- **(D)** 216

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 216**

**Detailed Solution:**

$\mathrm{x}_1, \mathrm{x}_2, \mathrm{x}_3, \mathrm{x}_4 \rightarrow \text { G.P. }$
Let a, ar, $\mathrm{ar}^2, \mathrm{ar}^3 \rightarrow$ G.P.
Now $a-2, a r-7, a^2-9, \mathrm{ar}^3-5 \rightarrow$ A.P.
$2(\mathrm{ar}-7)=\mathrm{a}-2+\mathrm{ar}^2-9$....(i)
$2\left(\operatorname{ar}^2-9\right)=\mathrm{ar}-7+\mathrm{ar}^3-5$....(ii)
$\begin{aligned} & \text { Solving } \mathrm{r}=2, \mathrm{a}=-3 \\ & \therefore \text { Product }=\mathrm{x}_1, \mathrm{x}_2, \mathrm{x}_3, \mathrm{x}_4=\mathrm{a}^4 \mathrm{r}^6=81 \times 64\end{aligned}$
$\begin{aligned} & \text { Solving } \mathrm{r}=2, \mathrm{a}=-3 \\ & \therefore \text { Product }=\mathrm{x}_1, \mathrm{x}_2, \mathrm{x}_3, \mathrm{x}_4=\mathrm{a}^4 \mathrm{r}^6=81 \times 64\end{aligned}$

</details>

---

### Q11. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $a_1, a_2, a_3, \ldots$ be a G. P. of increasing positive numbers. If $\mathrm{a}_3 \mathrm{a}_5=729$ and $\mathrm{a}_2+\mathrm{a}_4=\frac{111}{4}$, then $24\left(a_1+a_2+a_3\right)$ is equal to

**Options:**

- **(A)** $131$
- **(B)** $130$
- **(C)** $129$
- **(D)** $128$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $129$**

**Detailed Solution:**

Let the $\mathrm{I}^{\text {st }}$ term of G.P. be a \& common ratio be r
$\begin{aligned}
\mathrm{a}_3 \mathrm{a}_5 & =\operatorname{ar}^2 \cdot \operatorname{ar}^4=729 \\
& =\mathrm{a}^2 \mathrm{r}^6=729 \\
& =\mathrm{ar}^3=27 \quad ....(i)
\end{aligned}$
$\begin{aligned} \mathrm{a}_2+\mathrm{a}_4 & =\mathrm{ar}+\mathrm{ar}^3=\frac{111}{4} \\ & =\mathrm{ar}=\frac{3}{4} \quad ....(ii)\end{aligned}$
$\text { (i) } \div \text { (ii) }$
$\begin{aligned}
& \frac{\mathrm{ar}^3}{\mathrm{ar}}=\frac{27}{3 / 4} \\
& \mathrm{r}^2=36 \\
& \mathrm{r}=6
\end{aligned}$
from (ii)
$a(6)=\frac{3}{4} \Rightarrow a=\frac{1}{8}$
Now, $24\left(a_1+a_2+a_3\right)$
$\begin{aligned}
& =24\left(a+a r+a^2\right) \\
& =24 a\left(1+r+r^2\right)
\end{aligned}$
$\begin{aligned} & =24 \times \frac{1}{8}(1+6+36) \\ & =3(43) \\ & =129\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $a_1, a_2, a_3, \ldots$ be a G.P. of increasing positive terms. If $a_1 a_5=28$ and $a_2+a_4=29$, then $a_6$ is equal to:

**Options:**

- **(A)** $628$
- **(B)** $812$
- **(C)** $526$
- **(D)** $784$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $784$**

**Detailed Solution:**

$\begin{aligned}
& a_1 a_5=28 \Rightarrow a^2 r^4=28 \\
& a_2+a_4=29 \Rightarrow a r+a r^3=29
\end{aligned}$
ar and $a r^3$ are roots of
$\begin{aligned}
& k^2-29 k+28=0 \\
& \Rightarrow \quad k=1, k=28 \\
& a r=1, a r^3=28 \\
& r^2=28, a^2=\frac{1}{28} \\
& a_6=a r^5 \Rightarrow r^4=28^2 \\
& \Rightarrow a_6=784
\end{aligned}$

</details>

---

### Q13. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $a, a r, a r^2$, $\qquad$ be an infinite G.P. If $\sum_{n=0}^{\infty} a r^n=57$ and $\sum_{n=0}^{\infty} a^3 r^{3 n}=9747$, then $a+18 r$ is equal to

**Options:**

- **(A)** 46
- **(B)** 38
- **(C)** 31
- **(D)** 27

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 31**

**Detailed Solution:**

$\begin{aligned}
& \sum_{n=0}^{\infty} \operatorname{ar}^{\mathrm{n}}=57 \\
& \mathrm{a}+\mathrm{ar}+\mathrm{ar}^2+\infty=57 \\
& \frac{\mathrm{a}}{1-\mathrm{r}}=57 \ldots(I)\\
& \sum_{\mathrm{n}=0}^{\infty} \mathrm{a}^3 \mathrm{r}^{3 \mathrm{n}}=9747 \\
& \mathrm{a}^3+\mathrm{a}^3 \cdot \mathrm{r}^3+\mathrm{a}^3 \cdot \mathrm{r}^6+\ldots \ldots \ldots . \ldots=9746 \\
& \frac{\mathrm{a}^3}{1-\mathrm{r}^3}=9746 \ldots(II)\\
& \frac{(\mathrm{I})^3}{(\mathrm{II})} \Rightarrow \frac{\frac{\mathrm{a}^3}{(1-\mathrm{r})^3}}{\frac{\mathrm{a}^3}{1-\mathrm{r}^3}}=\frac{57^3}{9717}=19 \\
& \mathrm{a}=19 \\
& \therefore \mathrm{a}+18 \mathrm{r}=19+18 \times \frac{2}{3}=31 \\
&
\end{aligned}$
On solving, $\mathrm{r}=\frac{2}{3}$ and $\mathrm{r}=\frac{3}{2}$ (rejected $)$
$\begin{aligned} & a=19 \\ & \therefore a+18 r=19+18 \times \frac{2}{3}=31\end{aligned}$

</details>

---

### Q14. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

In an increasing geometric progression of positive terms, the sum of the second and sixth terms is $\frac{70}{3}$ and the product of the third and fifth terms is 49 . Then the sum of the $4^{\text {th }}, 6^{\text {th }}$ and $8^{\text {th }}$ terms is equal to :

**Options:**

- **(A)** 96
- **(B)** 91
- **(C)** 84
- **(D)** 78

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 91**

**Detailed Solution:**

$\mathrm{T}_2+\mathrm{T}_6=\frac{70}{3}$
$\mathrm{ar}+\mathrm{ar}^5=\frac{70}{3}$
$\mathrm{~T}_3 \cdot \mathrm{T}_5=49$
$\mathrm{ar}^2 \cdot \mathrm{ar}^4=49$
$\mathrm{a}^2 \mathrm{r}^6=49$
$\mathrm{ar}^3=+7, \mathrm{a}=\frac{7}{\mathrm{r}^3}$
$\mathrm{ar}\left(1+\mathrm{r}^4\right)=\frac{70}{3}$
$\frac{7}{\mathrm{r}^2}\left(1+\mathrm{r}^4\right)=\frac{70}{3}, \mathrm{r}^2=\mathrm{t}$
$\frac{1}{\mathrm{t}}\left(1+\mathrm{t}^2\right)=\frac{10}{3}$
$3 \mathrm{t}^2-10 \mathrm{t}+3=0$
$\mathrm{t}=3, \frac{1}{3}$
Increasing G.P. 
$\mathrm{r}^2=3, \mathrm{r}=\sqrt{3}$
$\mathrm{T}_4+\mathrm{T}_6+\mathrm{T}_8$
$=\mathrm{ar}^3+\mathrm{ar}^5+\mathrm{ar}^7$
$=\operatorname{ar}^3\left(1+\mathrm{r}^2+\mathrm{r}^4\right)$
$=7(1+3+9)=91$

</details>

---

### Q15. JEE Main 2024 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $A B C$ be an equilateral triangle. A new triangle is formed by joining the middle points of all sides of the triangle $A B C$ and the same process is repeated infinitely many times. If $\mathrm{P}$ is the sum of perimeters and $Q$ is be the sum of areas of all the triangles formed in this process, then :

**Options:**

- **(A)** $\mathrm{P}^2=6 \sqrt{3} \mathrm{Q}$
- **(B)** $\mathrm{P}^2=36 \sqrt{3} \mathrm{Q}$
- **(C)** $\mathrm{P}=36 \sqrt{3} \mathrm{Q}^2$
- **(D)** $\mathrm{P}^2=72 \sqrt{3} \mathrm{Q}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\mathrm{P}^2=36 \sqrt{3} \mathrm{Q}$**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/17J8bqOsFolgCdOox8Oe6p344B5Zl2x_ra1NNsuT5c0.original.fullsize.png">
Area of first $\Delta=\frac{\sqrt{3} \mathrm{a}^2}{4}$
Area of second $\Delta=\frac{\sqrt{3} \mathrm{a}^2}{4} \frac{\mathrm{a}^2}{4}=\frac{\sqrt{3} \mathrm{a}^2}{16}$
Area of third $\Delta=\frac{\sqrt{3} \mathrm{a}^2}{64}$
sum of area $=\frac{\sqrt{3} \mathrm{a}^2}{4}\left(1+\frac{1}{4}+\frac{1}{16} \ldots\right)$
$\begin{aligned} & \mathrm{Q}=\frac{\sqrt{3} \mathrm{a}^2}{4} \frac{1}{\frac{3}{4}}=\frac{\mathrm{a}^2}{\sqrt{3}} \\ & \text { perimeter of } 1^{\text {st }} \Delta=3 \mathrm{a} \\ & \text { perimeter of } 2^{\text {nd }} \Delta=\frac{3 \mathrm{a}}{2} \\ & \text { perimeter of } 3^{\text {rd }} \Delta=\frac{3 \mathrm{a}}{4} \\ & \mathrm{P}=3 \mathrm{a}\left(1+\frac{1}{2}+\frac{1}{4}+\ldots\right) \\ & \mathrm{P}=3 \mathrm{a} \cdot 2=6 \mathrm{a} \\ & \mathrm{a}=\frac{\mathrm{P}}{6} \\ & \mathrm{Q}=\frac{1}{\sqrt{3}} \cdot \frac{\mathrm{P}^2}{36} \\ & \mathrm{P}^2=36 \sqrt{3} \mathrm{Q}\end{aligned}$

</details>

---

### Q16. JEE Main 2024 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `2`

If three successive terms of a G.P. with common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mfenced><mrow><mi>r</mi><mo>&gt;</mo><mn>1</mn></mrow></mfenced></math> are the length of the sides of a triangle and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mi>r</mi></mfenced></math> denotes the greatest integer less than or equal to r, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>−</mo><mi>r</mi></mrow></mfenced></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>→</mo><mi>G</mi><mo>.</mo><mi>P</mi><mo>.</mo></math></p><p>It is given that sum of any two sides is greater than the third side.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>&gt;</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>,</mo><mo> </mo><mi>a</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>&gt;</mo><mi>a</mi><mi>r</mi><mo>,</mo><mo> </mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>&gt;</mo><mi>a</mi></math></p><p>Case-I: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>−</mo><mi>r</mi><mo>−</mo><mn>1</mn><mo>&lt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>±</mo><msqrt><mn>1</mn><mo>-</mo><mn>4</mn><mo>×</mo><mn>1</mn><mo>×</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>±</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>∈</mo><mfenced><mrow><mfrac><mrow><mn>1</mn><mo>−</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Case-II: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>−</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>&gt;</mo><mn>0</mn></math> is always true.</p><p>Case-III: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>r</mi><mo>−</mo><mn>1</mn><mo>&gt;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>∈</mo><mfenced><mrow><mo>−</mo><mi>∞</mi><mo>,</mo><mfrac><mrow><mo>−</mo><mn>1</mn><mo>−</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>∪</mo><mfenced><mrow><mfrac><mrow><mo>−</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mi>∞</mi></mrow></mfenced><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Taking intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo> </mo><mtext>and</mtext><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>∈</mo><mfenced><mrow><mfrac><mrow><mo>−</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p>As <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&gt;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>r</mi><mo>∈</mo><mfenced><mrow><mn>1</mn><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="]" open="["><mi>r</mi></mfenced><mo>=</mo><mn>1</mn><mo> </mo><mtext>and</mtext><mo> </mo><mfenced close="]" open="["><mrow><mo>−</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mo>−</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>−</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mn>3</mn><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mfenced close="]" open="["><mi>r</mi></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mo>−</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q17. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> be two distinct positive real numbers. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mtext>th </mtext></msup></math> term of a GP, whose first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and third term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>, is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mtext>th </mtext></msup></math> term of another GP, whose first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and fifth term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mrow><mi>s</mi><mi>t</mi></mrow></msup><mo> </mo><mi>G</mi><mi>P</mi><mo>⇒</mo><mtext>First term</mtext><mo>=</mo><mi>a</mi><mo>,</mo><mo> </mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mfrac><mi>b</mi><mi>a</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mn>10</mn></msub><mo>=</mo><mi>a</mi><msup><mi>r</mi><mn>10</mn></msup><mo>=</mo><mi>a</mi><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mn>5</mn></msup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mi>n</mi><mi>d</mi></mrow></msup><mo> </mo><mi>G</mi><mi>P</mi><mo>⇒</mo><mtext>First term</mtext><mo>=</mo><mi>a</mi><mo>,</mo><mo> </mo><msub><mi>a</mi><mn>5</mn></msub><mo>=</mo><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><msup><mi>R</mi><mn>4</mn></msup><mo>=</mo><mi>b</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mi>p</mi></msub><mo>=</mo><mi>a</mi><msup><mi>R</mi><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mi>p</mi></msub><mo>=</mo><mi>a</mi><msup><mfenced close="]" open="["><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></msup><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, using the given condition of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>p</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>a</mi><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mn>5</mn></msup><mo>=</mo><mi>a</mi><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mfrac><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mn>5</mn></msup><mo>=</mo><msup><mfenced><mfrac><mi>b</mi><mi>a</mi></mfrac></mfenced><mfrac><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>5</mn><mo>=</mo><mfrac><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>p</mi><mo>=</mo><mn>21</mn></math></p></blockquote>

</details>

---

### Q18. JEE Main 2024 (29 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If each term of a geometric progression <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub><mo>,</mo><mo>…</mo></math> with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>≠</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub></math>, is the arithmetic mean of the next two terms and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>+</mo><mo>…</mo><mo>+</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>15</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>18</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>18</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>GP</mi><mo>:</mo><mo> </mo><mi mathvariant="normal">a</mi><mo>,</mo><mo> </mo><mi>ar</mi><mo>,</mo><mo> </mo><msup><mi>ar</mi><mn>2</mn></msup><mo>,</mo><mo> </mo><msup><mi>ar</mi><mn>3</mn></msup><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>Now, given: <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>ar</mi><mo>=</mo><msup><mi>ar</mi><mn>2</mn></msup><mo>+</mo><msup><mi>ar</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>2</mn><mo>=</mo><mi mathvariant="normal">r</mi><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mo>+</mo><mi mathvariant="normal">r</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">r</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>,</mo><mo> </mo><mn>1</mn><mo> </mo><mfenced close="]" open="["><mrow><mtext>Since</mtext><mo> </mo><mi>GP</mi><mo> </mo><mtext>is not constant so </mtext><mi>r</mi><mo>=</mo><mn>1</mn><mtext> is rejected</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">r</mi><mo>=</mo><mo>-</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>20</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>18</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced close="]" open="["><mrow><msup><mi mathvariant="normal">r</mi><mn>18</mn></msup><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>20</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub><mo>=</mo><mfrac><mfenced close="]" open="["><mrow><msup><mn>2</mn><mn>18</mn></msup><mo>-</mo><msup><mn>2</mn><mn>20</mn></msup></mrow></mfenced><mrow><mn>8</mn><mo>×</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub><mo>=</mo><mfrac><mrow><msup><mn>2</mn><mn>18</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>4</mn></mrow></mfenced></mrow><mn>24</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">S</mi><mn>20</mn></msub><mo>-</mo><msub><mi mathvariant="normal">S</mi><mn>18</mn></msub><mo>=</mo><mo>-</mo><msup><mn>2</mn><mn>15</mn></msup></math></p>

</details>

---

### Q19. JEE Main 2024 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If in a G.P. of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math> terms, the sum of all the terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math> times the sum of the odd terms of the G.P, then the common ratio of the G.P. is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>For the given GP, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">n</mi><mo>=</mo><mn>64</mn><mo>,</mo><mo> </mo><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><mn>7</mn><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">o</mi></msub><mo> </mo><mo>;</mo><mo> </mo><mfenced close="}" open="{"><mrow><mtext>where</mtext><mo> </mo><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">o</mi></msub><mo>→</mo><mtext>Sum of odd terms</mtext></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">a</mi><mo>+</mo><mi>ar</mi><mo>+</mo><msup><mi>ar</mi><mn>2</mn></msup><mo>+</mo><msup><mi>ar</mi><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>ar</mi><mn>63</mn></msup><mo>=</mo><mn>7</mn><mfenced><mrow><mi mathvariant="normal">a</mi><mo>+</mo><msup><mi>ar</mi><mn>2</mn></msup><mo>+</mo><msup><mi>ar</mi><mn>4</mn></msup><mo>…</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>ar</mi><mn>62</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>64</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>7</mn><mi mathvariant="normal">a</mi><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>64</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>64</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>7</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">r</mi><mn>64</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>=</mo><mfrac><mn>7</mn><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>1</mn><mo>+</mo><mi mathvariant="normal">r</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">r</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q20. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo></math>. be a G.P. of increasing positive numbers. Let the sum of its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mtext>th&#160;</mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mtext>th&#160;</mtext></msup></math> terms be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> and the product of its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mtext>rd&#160;</mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mtext>th&#160;</mtext></msup></math> terms be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><msub><mi>a</mi><mn>6</mn></msub></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo></math>. be a G.P. of increasing positive numbers,</p><p>And the sum of its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mtext>th&#160;</mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mtext>th&#160;</mtext></msup></math> terms be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>6</mn></msub><mo>+</mo><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><msup><mi>r</mi><mn>5</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>7</mn></msup><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And the product of its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mtext>rd&#160;</mtext></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mtext>th&#160;</mtext></msup></math> terms be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>5</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>&#183;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math></p><p>Now from putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></math> in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mi>r</mi><mn>2</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msup><mi>r</mi><mn>4</mn></msup><mn>3</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>a</mi><mi>r</mi><mo>&#183;</mo><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>&#8658;</mo><mi>a</mi><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p>Now finding the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><msub><mi>a</mi><mn>6</mn></msub></mrow></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup></mrow></mfenced><mfenced><mrow><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>5</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mo>&#183;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#183;</mo><mn>1</mn><mo>=</mo><mn>3</mn></math></p></blockquote>

</details>

---

### Q21. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the first term a and the common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> of a geometric progression be positive integers. If the sum of squares of its first three terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33033</mn></math>, then the sum of these three terms is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>241</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>231</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>210</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>231</mn></math>**

**Detailed Solution:**

<blockquote><p>Given that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>a</mi><mi>r</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>33033</mn><mo>,</mo><mo>&#160;</mo><mfenced><mrow><mi>a</mi><mo>,</mo><mi>r</mi><mo>&#8712;</mo><mi>N</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mo>=</mo><msup><mn>11</mn><mn>2</mn></msup><mo>&#215;</mo><mn>273</mn></math></p><p>On comparing both sides of the equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>11</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mn>273</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mn>272</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>16</mn><mo>&#215;</mo><mn>17</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>11</mn><mo>+</mo><mn>11</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mn>11</mn><mo>&#215;</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>+</mo><mn>44</mn><mo>+</mo><mn>176</mn><mo>=</mo><mn>231</mn></math>.</p><p>Therefore, the required value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>231</mn></math></p></blockquote>

</details>

---

### Q22. JEE Main 2023 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum and product of four positive consecutive terms of a G.P., are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1296</mn></math>, respectively, then the sum of common ratios of all such GPs is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>14</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p>Let us consider four positive consecutive terms of a G.P. as follow:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mfenced><mrow><mi>a</mi><mo>,</mo><mi>r</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p>Product <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>4</mn></msup><msup><mi>r</mi><mn>6</mn></msup><mo>=</mo><mn>1296</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>6</mn><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></math></p><p>Sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>126</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mo>+</mo><mfrac><mi>r</mi><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mo>+</mo><mfrac><msup><mi>r</mi><mn>2</mn></msup><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mo>+</mo><mfrac><msup><mi>r</mi><mn>3</mn></msup><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mn>126</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>r</mi><mrow><mo>-</mo><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>r</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>r</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mo>=</mo><mn>21</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>r</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mi>A</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mrow><mo>-</mo><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><msup><mi>r</mi><mrow><mn>3</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>=</mo><mo>(</mo><msup><mi>r</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>r</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup><msup><mo>)</mo><mn>3</mn></msup><mo>-</mo><mn>3</mn><mo>(</mo><msup><mi>r</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mi>r</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>A</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>A</mi></math></p><p>Therefore,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>A</mi><mn>3</mn></msup><mo>-</mo><mn>3</mn><mi>A</mi><mo>+</mo><mi>A</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>A</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><mi>A</mi><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msqrt><mi>r</mi></msqrt><mo>+</mo><mfrac><mn>1</mn><msqrt><mi>r</mi></msqrt></mfrac><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>3</mn><msqrt><mi>r</mi></msqrt></math></p><p>On squaring both sides:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>9</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>7</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn></math></p><p>Here, sum of roots<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q23. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let $\left\{a_k\right\}$ and $\left\{b_k\right\}, k \in \mathbb{N}$, be two G.P.s with common ratio $r_1$ and $r_2$ respectively such that $\mathrm{a}_1=\mathrm{b}_1=4$ and $\mathrm{r}_1&lt;\mathrm{r}_2$. Let $\mathrm{c}_{\mathrm{k}}=\mathrm{a}_{\mathrm{k}}+\mathrm{b}_{\mathrm{k}}, \mathrm{k} \in \mathbb{N}$. If $\mathrm{c}_2=5$ and $\mathrm{c}_3=\frac{13}{4}$ then $\sum_{\mathrm{k}=1}^{\infty} \mathrm{c}_{\mathrm{k}}-\left(12 \mathrm{a}_6+8 \mathrm{~b}_4\right)$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mi mathvariant="normal">k</mi></msub><mo>=</mo><msub><mi>a</mi><mi mathvariant="normal">k</mi></msub><mo>+</mo><msub><mi>b</mi><mi mathvariant="normal">k</mi></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><msub><mi mathvariant="normal">r</mi><mn>1</mn></msub></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><msubsup><mi>r</mi><mn>1</mn><mn>2</mn></msubsup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><msub><mi>r</mi><mn>2</mn></msub></math> and  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><msubsup><mi>r</mi><mn>2</mn><mn>2</mn></msubsup></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>2</mn></msub><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>4</mn><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>3</mn></msub><mo>=</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mo>=</mo><mfrac><mn>13</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>r</mi><mn>1</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>r</mi><mn>2</mn><mn>2</mn></msubsup><mo>=</mo><mfrac><mn>13</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><msub><mi>r</mi><mn>2</mn></msub></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>13</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>25</mn><mn>16</mn></mfrac><mo>-</mo><mn>2</mn><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>13</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>12</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msub><mi>r</mi><mn>1</mn></msub><mfenced><mrow><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>-</mo><msub><mi>r</mi><mn>1</mn></msub></mrow></mfenced><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><msub><mi>r</mi><mn>1</mn></msub><mo>-</mo><mn>8</mn><msubsup><mi>r</mi><mn>1</mn><mn>2</mn></msubsup><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>8</mn><msubsup><mi>r</mi><mn>1</mn><mn>2</mn></msubsup><mo>-</mo><mn>10</mn><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#177;</mo><msqrt><mn>100</mn><mo>-</mo><mn>96</mn></msqrt></mrow><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></math> </p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">k</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><msub><mi mathvariant="normal">c</mi><mi mathvariant="normal">k</mi></msub><mo>-</mo><mfenced><mrow><mn>12</mn><msub><mi>a</mi><mn>6</mn></msub><mo>+</mo><mn>8</mn><msub><mi>b</mi><mn>4</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>+</mo><msub><mi>c</mi><mn>2</mn></msub><mo>+</mo><msub><mi>c</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mn>12</mn><mo>&#215;</mo><mfenced open="{" close="}"><mrow><mn>4</mn><mo>&#215;</mo><mfenced><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac></mfenced></mrow></mfenced><mo>+</mo><mn>8</mn><mfenced open="{" close="}"><mrow><mn>4</mn><mo>&#215;</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>2</mn></msub><mo>+</mo><msub><mi>b</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mn>27</mn><mn>2</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>-</mo><msub><mi>r</mi><mn>1</mn></msub></mrow></mfrac><mo>+</mo><mfrac><mn>4</mn><mrow><mn>1</mn><mo>-</mo><msub><mi>r</mi><mn>2</mn></msub></mrow></mfrac><mo>-</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>24</mn><mo>-</mo><mn>15</mn><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q24. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo></math>. be a GP of increasing positive numbers. If the product of fourth and sixth terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> and the sum of fifth and seventh terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math> , then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>7</mn></msub></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **60**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><mo>,</mo><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo></math>. be a GP of increasing positive numbers,</p><p>And the product of fourth and sixth terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><mo>&#183;</mo><msub><mi mathvariant="normal">a</mi><mn>6</mn></msub><mo>=</mo><mn>9</mn><mo>&#8658;</mo><msup><mfenced><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn><mo>&#8658;</mo><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>=</mo><mn>3</mn></math></p><p>Also given the sum of fifth and seventh terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>24</mn></math>,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>7</mn></msub><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup><mo>=</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>8</mn><mo>&#8658;</mo><mi mathvariant="normal">r</mi><mo>=</mo><msqrt><mn>7</mn></msqrt></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>=</mo><mn>3</mn><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mn>3</mn><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>3</mn><msup><mi>r</mi><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>49</mn></mfrac></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>1</mn></msub><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>2</mn></msub><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><msub><mi mathvariant="normal">a</mi><mn>9</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>5</mn></msub><mo>+</mo><msub><mi mathvariant="normal">a</mi><mn>7</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>7</mn></msqrt></mfenced><mn>8</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msqrt><mn>7</mn></msqrt><mo>&#215;</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>7</mn></msqrt></mfenced><mn>3</mn></msup><mo>&#215;</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>7</mn></msqrt></mfenced><mn>8</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>7</mn></msqrt></mfenced><mn>4</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>49</mn></mfrac><mo>&#215;</mo><msup><mfenced><msqrt><mn>7</mn></msqrt></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>9</mn><mo>+</mo><mn>27</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>21</mn><mo>=</mo><mn>60</mn></math></p>

</details>

---

### Q25. JEE Main 2023 (24 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The 4<sup>th</sup> term of GP is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math> and its common ratio is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mi>m</mi></mfrac><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8712;</mo><mi>N</mi></math>. Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math> denote the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms of this GP. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>6</mn></msub><mo>&#62;</mo><msub><mi>S</mi><mn>5</mn></msub><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>7</mn></msub><mo>&#60;</mo><msub><mi>S</mi><mn>6</mn></msub><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math>, then the number of possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>4</mn></msub><mo>=</mo><mn>500</mn></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo></math> first term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo></math>common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>m</mi></mfrac><mo>,</mo><mo>&#160;</mo><mi>m</mi><mo>&#8712;</mo><mi>N</mi></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>500</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><msup><mi>m</mi><mn>3</mn></msup></mfrac><mo>=</mo><mn>500</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>a</mi><msup><mi>r</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>6</mn></msub><mo>&#62;</mo><msub><mi>S</mi><mn>5</mn></msub><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>6</mn></msub><mo>-</mo><msub><mi>S</mi><mn>5</mn></msub><mo>&#62;</mo><mn>1</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><msup><mi>m</mi><mn>5</mn></msup></mfrac><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><msup><mi>m</mi><mn>3</mn></msup></mfrac><mo>&#215;</mo><mfrac><mn>1</mn><msup><mi>m</mi><mn>2</mn></msup></mfrac><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>500</mn><msup><mi>m</mi><mn>2</mn></msup></mfrac><mo>&#62;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>&#60;</mo><mn>500</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>7</mn></msub><mo>-</mo><msub><mi>S</mi><mn>6</mn></msub><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><msup><mi>m</mi><mn>6</mn></msup></mfrac><mo>&#60;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><msup><mi>m</mi><mn>3</mn></msup></mfrac><mo>&#215;</mo><mfrac><mn>2</mn><msup><mi>m</mi><mn>3</mn></msup></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>500</mn><mo>&#215;</mo><mfrac><mn>2</mn><msup><mi>m</mi><mn>3</mn></msup></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>3</mn></msup><mo>&#62;</mo><msup><mn>10</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>&#62;</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mn>13</mn><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>22</mn></math></p><p>So, number of possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>.</p>

</details>

---

### Q26. JEE Main 2022 (28 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>x</mi><mn>20</mn></msub></math> be in geometric progression with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn></math> and the common ration <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>. A new data is constructed replacing each <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>i</mi></msub></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose></math> is the mean of new data, then the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **142**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>,</mo><msub><mi>x</mi><mn>20</mn></msub></math> are in G.P with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math> and first term as <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></p><p>Now using the formula for sum of G.P we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>20</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac><mo>=</mo><mn>6</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>20</mn></msup></mfrac></mrow></mfenced></math></p><p>Now new sum of G.P with new data will be<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mfenced><mrow><msub><mi>x</mi><mi>i</mi></msub><mo>-</mo><mi>i</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mi>i</mi></mfenced><mn>2</mn></msup><mo>-</mo><mn>2</mn><msub><mi>x</mi><mi>i</mi></msub><mi>i</mi></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mfenced><msub><mi>x</mi><mi>i</mi></msub></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>9</mn><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mn>20</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfrac><mo>=</mo><mn>12</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>40</mn></msup></mfrac></mrow></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>21</mn><mo>&#215;</mo><mn>41</mn><mo>=</mo><mn>2870</mn></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msub><mi>x</mi><mi>i</mi></msub><mi>i</mi><mo>=</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>.</mo><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mn>3</mn><mo>.</mo><mn>3</mn><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mn>4</mn><mo>.</mo><mn>3</mn><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mi>AGP</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mfrac><mn>11</mn><msup><mn>2</mn><mn>18</mn></msup></mfrac></mrow></mfenced></math></p><p>So, mean of the new data will be,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mfrac><mrow><mn>12</mn><mo>-</mo><mfrac><mn>12</mn><msup><mn>2</mn><mn>40</mn></msup></mfrac><mo>+</mo><mn>2870</mn><mo>-</mo><mn>6</mn><mfenced><mrow><mn>4</mn><mo>-</mo><mfrac><mn>11</mn><msup><mn>2</mn><mn>18</mn></msup></mfrac></mrow></mfenced></mrow><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><menclose notation="top"><mi>x</mi></menclose><mo>=</mo><mfrac><mn>2858</mn><mn>20</mn></mfrac><mo>+</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>12</mn></mrow><msup><mn>2</mn><mn>40</mn></msup></mfrac><mo>+</mo><mfrac><mn>66</mn><msup><mn>2</mn><mn>18</mn></msup></mfrac></mrow></mfenced><mo>&#215;</mo><mfrac><mn>1</mn><mn>20</mn></mfrac></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><menclose notation="top"><mi>x</mi></menclose></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mn>142</mn><mo>.</mo><mn>4</mn><mo>+</mo><mn>0</mn><mo>.</mo><mn>00001</mn></mrow></mfenced><mo>=</mo><mn>142</mn></math></p></blockquote>

</details>

---

### Q27. JEE Main 2022 (28 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><msub><mi>A</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math>  be an increasing geometric progression of positive real numbers. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>3</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>5</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>7</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>1296</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>+</mo><msub><mi>A</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>7</mn><mn>36</mn></mfrac></math>, then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>6</mn></msub><mo>+</mo><msub><mi>A</mi><mn>8</mn></msub><mo>+</mo><msub><mi>A</mi><mn>10</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>37</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>**

**Detailed Solution:**

<p>Given </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><msub><mi>A</mi><mn>3</mn></msub><msub><mi>A</mi><mn>5</mn></msub><msub><mi>A</mi><mn>7</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>1296</mn></mfrac></math>  </p><p>Expanding using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>n</mi></msub><mo>=</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> formula we get,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><msub><mi>A</mi><mn>1</mn></msub></mfenced><mfenced><mrow><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mfenced><mrow><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>6</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>1296</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msubsup><mi>A</mi><mn>1</mn><mn>4</mn></msubsup><msup><mi>r</mi><mn>12</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>1296</mn></mfrac><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Also given ,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub><mo>+</mo><msub><mi>A</mi><mn>4</mn></msub><mo>=</mo><mfrac><mn>7</mn><mn>36</mn></mfrac><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><mi>r</mi><mo>+</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mfrac><mn>7</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>1</mn></msub><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mn>36</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>Dividing equation (i) from equation (ii) we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math> </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>6</mn></msub><mo>+</mo><msub><mi>A</mi><mn>8</mn></msub><mo>+</mo><msub><mi>A</mi><mn>10</mn></msub><mo>=</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>5</mn></msup><mo>+</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>7</mn></msup><mo>+</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>9</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>A</mi><mn>1</mn></msub><msup><mi>r</mi><mn>3</mn></msup><mfenced open="[" close="]"><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><msup><mi>r</mi><mn>6</mn></msup></mrow></mfenced></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mfenced close="]" open="["><mrow><mn>6</mn><mo>+</mo><mn>36</mn><mo>+</mo><mn>216</mn></mrow></mfenced></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>43</mn></math></p>

</details>

---

### Q28. JEE Main 2022 (26 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>(</mo><mo>&#62;</mo><mn>0</mn><mo>)</mo><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><msub><mi>a</mi><mn>4</mn></msub><mo>,</mo><msub><mi>a</mi><mn>5</mn></msub></math> are in a G.P. ,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mn>4</mn></msub></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>5</mn></msub></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **40**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#62;</mo><mn>0</mn><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><msub><mi>a</mi><mn>4</mn></msub><mo>,</mo><msub><mi>a</mi><mn>5</mn></msub><mo>&#8594;</mo></math>G.P.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mn>4</mn></msub></math></p><p>Using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mi>a</mi><msup><mi>r</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math> and assuming <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mi>a</mi></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mo>+</mo><mi>r</mi><mo>=</mo><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mi>r</mi><mo>-</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mo>-</mo><mn>1</mn></math> &amp; <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>2</mn><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>3</mn></msup><mo>-</mo><mn>2</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>27</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>18</mn><mn>4</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p>When <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mi>a</mi><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math>  (rejected, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#62;</mo><mn>0</mn></math>)</p><p>So, at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>a</mi><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math> </p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>5</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>27</mn><mn>8</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mfrac><mn>8</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>81</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>27</mn><mo>=</mo><mn>40</mn></math></p>

</details>

---

### Q29. JEE Main 2022 (26 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced><mi>n</mi></msup></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced><mi>n</mi></msup></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>A</mi><mi>B</mi></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>11</mn><mn>9</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>11</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>11</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced><mi>n</mi></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfrac><mo>+</mo><mfrac><mfrac><mn>1</mn><mn>16</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>15</mn></mfrac><mo>=</mo><mfrac><mn>11</mn><mn>15</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup><msup><mfenced><mrow><mn>3</mn><mo>+</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></mrow></mfenced><mi>n</mi></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>4</mn></msup></mfrac><mo>-</mo><mo>&#8943;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mfrac><mfrac><mn>1</mn><mn>2</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfrac><mo>+</mo><mfrac><mfrac><mn>1</mn><mn>16</mn></mfrac><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>15</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>9</mn><mn>15</mn></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>A</mi><mi>B</mi></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>11</mn><mn>9</mn></mfrac></math></p>

</details>

---

### Q30. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the sum of an infinite <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>GP</mi></math>,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>,</mo><mo>&#8230;</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> and the sum of the squares of its each term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn><mo>,</mo></math> then the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>r</mi><mmultiscripts><mo>,</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mi>a</mi><msup><mi>r</mi><mn>4</mn></msup><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>6</mn></msup><mo>,</mo><mo>&#8230;</mo></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>2</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mn>15</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math> </p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>6</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo><mo>=</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mi>a</mi><mrow><mn>1</mn><mo>+</mo><mi>r</mi></mrow></mfrac></mfenced><mfenced><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac></mfenced><mo>=</mo><mn>150</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>a</mi><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mi>r</mi><mo>)</mo></mrow></mfrac><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>12</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>6</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>12</mn><mo>&#215;</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>25</mn></mfrac></mstyle></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>25</mn></mfrac></mstyle></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

In an increasing geometric series, the sum of the second and the sixth term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>2</mn></mfrac></math> and the product of the third and fifth term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn><mo>.</mo></math> Then, the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>4</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup><mo>,</mo><msup><mn>6</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> terms is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><mi>r</mi><mo>,</mo><mo>&#160;</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></math>....<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>+</mo><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mfrac><mn>25</mn><mn>2</mn></mfrac><mo>&#8658;</mo><mo mathvariant="italic">ar</mo><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mn>25</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>625</mn><mn>4</mn></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub><mo>&#183;</mo><msub><mi>T</mi><mn>5</mn></msub><mo>=</mo><mn>25</mn><mo>&#8658;</mo><mfenced><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mi>a</mi><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>6</mn></msup><mo>=</mo><mn>25</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>On dividing <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced><mn>2</mn></msup><msup><mi>r</mi><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>25</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mi>r</mi><mn>8</mn></msup><mo>-</mo><mn>17</mn><msup><mi>r</mi><mn>4</mn></msup><mo>+</mo><mn>4</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>4</mn><msup><mi>r</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>r</mi><mn>4</mn></msup><mo>-</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mn>4</mn><mo>&#8658;</mo><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mn>4</mn></math> (an increasing geometric series)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><msup><mi>r</mi><mn>6</mn></msup><mo>=</mo><mn>25</mn><mo>&#8658;</mo><msup><mfenced><mrow><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>25</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>4</mn></msub><mo>+</mo><msub><mi>T</mi><mn>6</mn></msub><mo>+</mo><msub><mi>T</mi><mn>8</mn></msub><mo>=</mo><mi>a</mi><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>5</mn></msup><mo>+</mo><mi>a</mi><msup><mi>r</mi><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mo mathvariant="italic">ar</mo><mn>3</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>r</mi><mn>4</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>=</mo><mn>35</mn></math></p>

</details>

---

### Q32. JEE Main 2021 (25 Feb Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub><mo>,</mo><msub><mi>A</mi><mn>2</mn></msub><mo>,</mo><msub><mi>A</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math> be squares such that for each <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#10878;</mo><mn>1</mn><mo>,</mo></math> the length of the side of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>n</mi></msub></math> equals the length of diagonal of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></math>. If the length of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>&#160;</mo><mi>cm</mi></math>, then the smallest value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> for which area of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>n</mi></msub></math> is less than one, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub></math> be the side length of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>n</mi></msub><mo>.</mo></math><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msqrt><mn>2</mn></msqrt><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>12</mn><mo>&#215;</mo><msup><mfenced><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><msub><mi>a</mi><mi>n</mi></msub></mfenced><mn>2</mn></msup><mo>&#60;</mo><mn>1</mn><mo>&#8658;</mo><mfrac><mn>144</mn><msup><mn>2</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><msup><mn>2</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>&#62;</mo><mn>144</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>&#8805;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>n</mi><mo>&#8805;</mo><mn>9</mn></math></p>

</details>

---

### Q33. JEE Main 2021 (24 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>6</mn></msup><mi>x</mi><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo></mrow></mfenced><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></mrow></msup></math> satisfies the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>t</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>sin</mi><mi>x</mi></mrow><mrow><mi>sin</mi><mi>x</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mi>cos</mi><mi>x</mi></mrow></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>3</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mfenced><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></mfenced><mi>ln</mi><mo>&#160;</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mn>2</mn><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi><mo>+</mo><msup><mi>cos</mi><mn>4</mn></msup><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>=</mo><msup><mn>2</mn><mfrac><mrow><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mi>x</mi></mrow></mfrac></msup><mo>=</mo><msup><mn>2</mn><mrow><msup><mi>cot</mi><mn>2</mn></msup><mi>x</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>t</mi><mo>+</mo><mn>8</mn><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mrow><msup><mi>cot</mi><mn>2</mn></msup><mi>x</mi></mrow></msup><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>&#8658;</mo><msup><mi>cot</mi><mn>2</mn></msup><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mfrac><mi>&#960;</mi><mn>2</mn></mfrac><mo>&#8658;</mo><mi>cot</mi><mo>&#160;</mo><mi>x</mi><mo>=</mo><msqrt><mn>3</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><mo>&#160;</mo><mi>sin</mi><mo>&#160;</mo><mi>x</mi></mrow><mrow><mi>sin</mi><mo>&#160;</mo><mi>x</mi><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>cos</mi><mo>&#160;</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msqrt><mn>3</mn></msqrt><mo>&#160;</mo><mi>cot</mi><mo>&#160;</mo><mi>x</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>4</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p>

</details>

---

### Q34. JEE Main 2020 (06 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>&#160;</mo><mtext>and</mtext><mo>&#160;</mo><mi>p</mi></math> be non-zero distinct real numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>p</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>(</mo><mi>a</mi><mi>b</mi><mo>+</mo><mi>b</mi><mi>c</mi><mo>+</mo><mi>c</mi><mi>d</mi><mo>)</mo><mi>p</mi><mo>+</mo><mfenced><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><msup><mi>c</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>0</mn></math>. Then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>&#160;</mo><mtext>are&#160;in&#160;A.P.</mtext></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>p</mi><mo>&#160;</mo><mtext>are&#160;in&#160;G.P.</mtext></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#160;</mo><mtext>are&#160;in&#160;G.P.</mtext></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#160;</mo><mtext>are&#160;in&#160;A.P.</mtext></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>b</mi><mo>,</mo><mi>c</mi><mo>,</mo><mi>d</mi><mo>&#160;</mo><mtext>are&#160;in&#160;G.P.</mtext></math>**

**Detailed Solution:**

<p>Rearranging the expression, we get
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>a</mi><mi>p</mi><mo>-</mo><mi>b</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>b</mi><mi>p</mi><mo>-</mo><mi>c</mi><msup><mo>)</mo><mn>2</mn></msup><mo>+</mo><mo>(</mo><mi>c</mi><mi>p</mi><mo>-</mo><mi>d</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mo>&#8658;</mo><mo>&#160;&#160;</mo></mtd><mtd><mi>a</mi><mi>p</mi><mo>-</mo><mi>b</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>b</mi><mi>p</mi><mo>-</mo><mi>c</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>c</mi><mi>p</mi><mo>-</mo><mi>d</mi><mo>=</mo><mn>0</mn></mtd></mtr></mtable></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtable columnalign="left"><mtr><mtd><mo>&#8658;</mo><mo>&#160;&#160;</mo></mtd><mtd><mi>p</mi><mo>=</mo><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>=</mo><mfrac><mi>c</mi><mi>b</mi></mfrac><mo>=</mo><mfrac><mi>d</mi><mi>c</mi></mfrac></mtd></mtr></mtable></math></p><p>Which is condition of GP.</p>

</details>

---

### Q35. JEE Main 2020 (05 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the second, third and fourth terms of a positive term G.P. is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math> and the sum of its sixth, seventh and eighth terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn></math>, then the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math> terms of this G.P. is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>26</mn></mfrac><mfenced><mrow><msup><mn>3</mn><mn>49</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>26</mn></mfrac><mfenced><mrow><msup><mn>3</mn><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>13</mn></mfrac><mfenced><mrow><msup><mn>3</mn><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>13</mn></mfrac><mfenced><mrow><msup><mn>3</mn><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>26</mn></mfrac><mfenced><mrow><msup><mn>3</mn><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>Let a, ar, ar<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mo>&#8230;</mo><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math> be terms of G.P. </p><p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>+</mo><msub><mi>T</mi><mn>3</mn></msub><mo>+</mo><msub><mi>T</mi><mn>4</mn></msub><mo>=</mo><mn>3</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo></math> ar <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mn>6</mn></msub><mo>+</mo><msub><mi mathvariant="normal">T</mi><mn>7</mn></msub><mo>+</mo><msub><mi mathvariant="normal">T</mi><mn>8</mn></msub><mo>=</mo><mn>243</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><msup><mi>r</mi><mn>5</mn></msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>243</mn></math></p><p>by (i) and (ii)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>4</mn></msup><mo>=</mo><mn>81</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>3</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>13</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">S</mi><mn>50</mn></msub><mo>=</mo><mfrac><mrow><mi mathvariant="normal">a</mi><mfenced><mrow><msup><mi mathvariant="normal">r</mi><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mn>3</mn><mn>50</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>26</mn></mfrac></math></p>

</details>

---

### Q36. JEE Main 2020 (05 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>10</mn></msup><mo>+</mo><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>1</mn></msup><mo>+</mo><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>9</mn></msup><mo>+</mo><msup><mn>3</mn><mn>10</mn></msup><mo>=</mo><mi>S</mi><mo>-</mo><msup><mn>2</mn><mn>11</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup><mo>-</mo><msup><mn>2</mn><mn>12</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>3</mn><mn>11</mn></msup><mn>2</mn></mfrac><mo>+</mo><msup><mn>2</mn><mn>10</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>.</mo><msup><mn>3</mn><mn>11</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mn>11</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>S</mi><mo>&#39;</mo></msup><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mo>+</mo><msup><mn>2</mn><mn>9</mn></msup><mo>&#183;</mo><mn>3</mn><mo>+</mo><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>9</mn></msup><mo>+</mo><msup><mn>3</mn><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>S</mi><mo>&#39;</mo></msup><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mfenced close="}" open="{"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>9</mn></msup><mo>+</mo><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>10</mn></msup></mrow></mfenced></math></p><p>G.P. <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8594;</mo><mi mathvariant="normal">a</mi><mo>=</mo><mn>1</mn><mo>,</mo><mi>r</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mi>n</mi><mo>=</mo><mn>11</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>S</mi><mo>&#39;</mo></msup><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup><mo>&#183;</mo><mfenced close="}" open="{"><mfrac><mrow><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>11</mn></msup><mo>-</mo><mn>1</mn></mrow><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>=</mo><msup><mn>2</mn><mn>11</mn></msup><mfenced><mrow><mfrac><msup><mn>3</mn><mn>11</mn></msup><msup><mn>2</mn><mn>11</mn></msup></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>3</mn><mn>11</mn></msup><mo>-</mo><msup><mn>2</mn><mn>11</mn></msup></math></p>

</details>

---

### Q37. JEE Main 2020 (03 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><msup><mn>16</mn><mrow><msub><mi>log</mi><mrow><mn>2</mn><mo>.</mo><mn>5</mn></mrow></msub><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>&#8734;</mo></mrow></mfenced></mrow></msup></math> is __________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><msup><mn>16</mn><mrow><msub><mi>log</mi><mrow><mn>2</mn><mo>.</mo><mn>5</mn></mrow></msub><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>&#8734;</mo></mrow></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>.</mo><msup><mn>16</mn><mrow><msub><mi>log</mi><mrow><mn>2</mn><mo>.</mo><mn>5</mn></mrow></msub><mfenced><mfrac><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></mrow></mfrac></mfenced></mrow></msup><mo>=</mo><msup><mfenced><mfrac><mn>4</mn><mn>25</mn></mfrac></mfenced><mrow><msub><mi>log</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></mfenced><mrow><mo>-</mo><mn>2</mn><msub><mi>log</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msub><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></mrow></msup><mo>=</mo><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mrow><mo>-</mo><mn>2</mn></mrow></msup><mo>=</mo><mn>4</mn></math></p>

</details>

---

### Q38. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>x</mi></mfenced><mo>&#60;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfenced open="|" close="|"><mi>y</mi></mfenced><mo>&#60;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math>, then the sum to infinity of the following series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>x</mi><mi>y</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>x</mi><mi>y</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8722;</mo><mi>x</mi><mi>y</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>+</mo><mi>x</mi><mi>y</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>&#8722;</mo><mi>x</mi><mi>y</mi></mrow><mrow><mfenced><mrow><mn>1</mn><mo>&#8722;</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced></mrow></mfrac></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>Multiply <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced></math> both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>S</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mo>(</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>S</mi><mo>=</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>S</mi><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><msup><mi>y</mi><mn>3</mn></msup></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><msup><mi>y</mi><mn>4</mn></msup></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfenced><mi>S</mi><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup><mo>+</mo><msup><mi>y</mi><mn>4</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac><mfenced><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>-</mo><mfrac><msup><mi>y</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mi>y</mi></mrow></mfrac><mfenced><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>-</mo><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup></mrow><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>y</mi><mo>)</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mrow><mi>x</mi><mo>+</mo><mi>y</mi><mo>-</mo><mi>x</mi><mi>y</mi></mrow><mrow><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo><mo>(</mo><mn>1</mn><mo>-</mo><mi>y</mi><mo>)</mo></mrow></mfrac></math></p>

</details>

---

### Q39. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The sum of the first three terms of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>&#160;</mo></math>and their products is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>. Then all such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math> lie in</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>9</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>3</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mo>-</mo><mn>3</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>9</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>&#160;</mo><mn>9</mn><mo>]</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>9</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math>**

**Detailed Solution:**

<p> Let terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>r</mi></mfrac><mo>,</mo><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi></math></p><p>then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>3</mn></msup><mo>=</mo><mn>27</mn><mo>&#160;&#160;</mo><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>3</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>3</mn><mi>r</mi></mfrac><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>3</mn><mfenced><mrow><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>+</mo><mi>r</mi></mrow></mfenced><mo>+</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>&#8805;</mo><mn>2</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>r</mi><mo>&#62;</mo><mn>0</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>+</mo><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>&#8804;</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#8704;</mo><mi>r</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>&#8712;</mo><mo>(</mo><mo>-</mo><mo>&#8734;</mo><mo>,</mo><mo>-</mo><mn>3</mn><mo>]</mo><mo>&#8746;</mo><mo>[</mo><mn>9</mn><mo>,</mo><mo>&#8734;</mo><mo>)</mo></math></p>

</details>

---

### Q40. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mi>x</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi></mrow></msup><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mrow></math> and <math><mi>y</mi><mo>=</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>&#8734;</mi></mrow></munderover><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn><mi>n</mi></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>,</mo></mrow></mrow></mrow></mrow></math> for <math><mn>0</mn><mo>&#60;</mo><mi>&#952;</mi><mo>&#60;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac><mo>,</mo></math> then:

**Options:**

- **(A)** <math><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>
- **(B)** <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>
- **(C)** <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>
- **(D)** <math><mi>x</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>y</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mi>y</mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math><mi>y</mi><mo>=</mo><mn>1</mn><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>+</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>+</mo><mo>&#8230;</mo></mrow></mrow></mrow></mrow></math>   </p><p>Above series is an infinite G.P, apply sum of infinite G.P.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><msup><mi>cos</mi><mn>2</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>y</mi></mfrac><mo>=</mo><msup><mi>sin</mi><mn>2</mn></msup><mi>&#952;</mi></math></p><p><math><mi>x</mi><mo>=</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mfenced separators="|"><mrow><mo>-</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">tan</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfenced></mrow></mfrac><mo>=</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mrow><mrow><msup><mrow><mi mathvariant="normal">sec</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfrac></math></p><p><math><mo>&#8658;</mo><mrow><mrow><msup><mrow><mi mathvariant="normal">cos</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi><mo>=</mo><mi>x</mi></mrow></mrow></math></p><p><math><mo>&#8658;</mo><mi></mi><mfrac><mrow><mn>1</mn></mrow><mrow><mi>y</mi></mrow></mfrac><mo>+</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p><p><math><mo>&#8658;</mo><mi>y</mi><mi></mi><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q41. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>a</mi></mrow><mrow><mi>n</mi></mrow></msub></math> be the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of a G.P. of positive terms. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>200</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>=</mo><mn>100</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>200</mn></munderover><msub><mi>a</mi><mi>n</mi></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>300</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>175</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>150</mn></math>**

**Detailed Solution:**

<p>Let GP is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><mrow><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>5</mn></msub><mo>+</mo><mo>&#8230;</mo><msub><mi>a</mi><mn>201</mn></msub><mo>=</mo><mn>200</mn><mo>&#8658;</mo></mrow><mfrac><mrow><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup><mo>(</mo><msup><mi>r</mi><mn>200</mn></msup><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>200</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msub><mi>a</mi><mrow><mn>2</mn><mi>n</mi></mrow></msub><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>+</mo><mo>&#8230;</mo><msub><mi>a</mi><mn>200</mn></msub><mo>=</mo><mn>100</mn><mo>=</mo><mfrac><mrow><mi>a</mi><mi>r</mi><mfenced separators="|"><mrow><msup><mi>r</mi><mn>200</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>100</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Form <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, <math><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>adding both,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><msub><mi>a</mi><mn>200</mn></msub><mo>+</mo><msub><mi>a</mi><mn>201</mn></msub><mo>=</mo><mn>300</mn><mo>&#8658;</mo><mi>r</mi><mfenced separators="|"><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mo>&#8230;</mo><msub><mi>a</mi><mn>200</mn></msub></mrow></mfenced><mo>=</mo><mn>300</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>200</mn></munderover><mfrac><mn>300</mn><mi>r</mi></mfrac><mo>=</mo><mn>150</mn></math></p>

</details>

---

### Q42. JEE Main 2020 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The product <math><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>&#8729;</mo><msup><mrow><mn>4</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>16</mn></mrow></mfrac></mrow></msup><mo>&#8729;</mo><msup><mrow><mn>8</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>48</mn></mrow></mfrac></mrow></msup><mo>&#8729;</mo><msup><mrow><mn>16</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>128</mn></mrow></mfrac></mrow></msup><mo>&#8729;</mo><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo><mi></mi><mi></mi><mo>.</mo></math> to <math><mi>&#8734;</mi></math> is equal to:

**Options:**

- **(A)** <math><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>
- **(B)** <math><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></math>**

**Detailed Solution:**

<p><math><msup><mrow><mn>2</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn></mrow><mrow><mn>16</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>48</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mi>&#8734;</mi></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mn>2</mn><mrow><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mi>&#8734;</mi></mrow></msup><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#8734;</mo></math>is an infinite G.P with  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mo>&#8734;</mo></msub><mo>=</mo><mfrac><mi>a</mi><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p>Using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msqrt><mn>2</mn></msqrt></math></p>

</details>

---

### Q43. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo></math>, be a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>&#60;</mo><mn>0</mn><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>16</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mn>4</mn><mi>&#955;</mi></math>, then <math><mi>&#955;</mi></math>, is equal to.

**Options:**

- **(A)** <math><mo>-</mo><mn>513</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>171</mn></math>
- **(C)** <math><mn>171</mn></math>
- **(D)** <math><mfrac><mrow><mn>511</mn></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>171</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>4</mn><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>r</mi><mo>=</mo><mn>4</mn><mo>&#8230;</mo><mfenced separators="|"><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><msub><mi>a</mi><mn>4</mn></msub><mo>=</mo><mn>16</mn><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><msup><mi>r</mi><mn>3</mn></msup><mo>=</mo><mn>16</mn><mo>&#8230;</mo><mfenced separators="|"><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn><mo>&#160;</mo><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>&#160;</mo><mo>&#160;</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>&#60;</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>a</mi></munderover><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mfenced separators="|"><mrow><msup><mi>r</mi><mn>9</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced open="[" close="]"><mrow><msup><mfenced separators="|"><mrow><mo>-</mo><mn>2</mn></mrow></mfenced><mn>9</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mfenced><mrow><mo>-</mo><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>3</mn></mfrac><mfenced separators="|"><mrow><mo>-</mo><mn>513</mn></mrow></mfenced><mo>=</mo><mn>4</mn><mi>&#955;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mo>=</mo><mo>-</mo><mn>171</mn></math>.</p>

</details>

---

### Q44. JEE Main 2020 (07 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The greatest positive integer <math><mi>k</mi><mo>,</mo><mi></mi></math> for which <math><msup><mrow><mn>49</mn></mrow><mrow><mi>k</mi></mrow></msup><mo>+</mo><mn>1</mn></math> is a factor of the sum <math><msup><mrow><mn>49</mn></mrow><mrow><mn>125</mn></mrow></msup><mo>+</mo><msup><mrow><mn>49</mn></mrow><mrow><mn>124</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mn>49</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>49</mn><mo>+</mo><mn>1</mn><mo>,</mo><mi></mi></math> is

**Options:**

- **(A)** <math><mn>32</mn></math>
- **(B)** <math><mn>63</mn></math>
- **(C)** <math><mn>60</mn></math>
- **(D)** <math><mn>35</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>63</mn></math>**

**Detailed Solution:**

<p>This series is a G.P. with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>49</mn><mn>125</mn></msup></math> and common ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>49</mn></mfrac></math>.</p><p>So, its sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced separators="|"><mn>49</mn></mfenced><mn>126</mn></msup><mo>-</mo><mn>1</mn></mrow><mn>48</mn></mfrac><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><msup><mfenced separators="|"><mn>49</mn></mfenced><mn>63</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mn>49</mn><mn>63</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>48</mn></mfrac></math></p>

</details>

---

### Q45. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of an infinite geometric series with positive terms is 3 and the sum of the cubes of its terms is $\frac{27}{19}$. Then the common ratio of this series is:

**Options:**

- **(A)** $\frac{1}{3}$
- **(B)** $\frac{2}{3}$
- **(C)** $\frac{2}{9}$
- **(D)** $\frac{4}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

Let the terms of infinite series are $a, a r, a r^{2}, a r^{3}, \ldots$

So, $\quad \frac{a}{1-r}=3$

Since, sum of cubes of its terms is $\frac{27}{19}$ that is sum of $a^{3}$,

$a^{3} r^{3}, \ldots \infty$ is $\frac{27}{19}$

So, $\frac{a^{3}}{1-r^{3}}=\frac{27}{19}$

$\Rightarrow \quad \frac{a}{1-r} \times \frac{a^{2}}{\left(1+r^{2}+r\right)}=\frac{27}{19}$

$\Rightarrow \frac{9\left(1+r^{2}-2 r\right) \times 3}{1+r^{2}+r}=\frac{27}{19}$

$\Rightarrow \quad 6 r^{2}-13 r+6=0$

$\Rightarrow(3 r-2)(2 r-3)=0$

$\Rightarrow r=\frac{2}{3},$ or $\frac{3}{2}$

As $|r|  < 1$

So, $r=\frac{2}{3}$

</details>

---

### Q46. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let $a_{1}, a_{2}, \ldots, a_{10}$ be a G.P. If $\frac{a_{3}}{a_{1}}=25,$ then $\frac{a_{9}}{a_{5}}$ equals :

**Options:**

- **(A)** $5^{4}$
- **(B)** $4\left(5^{2}\right)$
- **(C)** $5^{3}$
- **(D)** $2\left(5^{2}\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $5^{4}$**

**Detailed Solution:**

Let $a_{1}=a, a_{2}=a r, a_{3}=a r^{2} \ldots a_{10}=a r^{9}$

where $r=$ common ratio of given G.P.

Given, $\frac{a_{3}}{a_{1}}=25$

$\Rightarrow \frac{a r^{2}}{a}=25$

$\Rightarrow r=\pm 5$

Now, $\frac{a_{9}}{a_{5}}=\frac{a r^{8}}{a r^{4}}=r^{4}=(\pm 5)^{4}=5^{4}$

</details>

---

### Q47. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mn>5</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><mi>r</mi><mo>,</mo><mi>&#160;</mi><mn>5</mn><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math> are the lengths of the sides of a triangle, then <math><mi>r</mi></math> can not be equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfrac><mrow><mn>7</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<blockquote><p>Given, <math><mn>5</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><mi>r</mi><mo>,</mo><mi>&#160;</mi><mn>5</mn><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math> are the length of sides of triangle, then we know that the sum of two sides of a triangle is more than the third side i.e.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>5</mn><mi>r</mi><mo>&#62;</mo><mn>5</mn><msup><mi>r</mi><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>5</mn><msup><mi>r</mi><mn>2</mn></msup><mo>&#62;</mo><mn>5</mn><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>r</mi><mo>+</mo><mn>5</mn><msup><mi>r</mi><mn>2</mn></msup><mo>&#62;</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>,</mo></math></p><p><math><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>&#60;</mo><mn>0</mn></math></p><p><math><mfenced close="]" open="[" separators="|"><mrow><mi>r</mi><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced><mi>&#160;</mi><mfenced close="]" open="[" separators="|"><mrow><mi>r</mi><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi></mrow></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn></math> </p><p>The discriminant of the quadratic is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>1</mn><mo>&#215;</mo><mn>1</mn><mo>=</mo><mo>-</mo><mn>3</mn></math> and we know that if the discriminant of a quadratic is negative and its leading coefficient is positive then the quadratic is positive for all real numbers. </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>&#8712;</mo><mi>R</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>5</mn></mfenced></math></p><p>from <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>3</mn></mfenced><mo>,</mo></math></p><p><math><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>&#62;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#160;</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt><mi>&#160;</mi></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#62;</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mi>&#160;</mi><mo>-</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>&#8746;</mo><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mi>&#160;</mi><mi>&#8734;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>6</mn></mfenced></math></p><p>Now, taking intersection of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>4</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>5</mn></mfenced><mo>,</mo><mo>&#160;</mo><mfenced><mn>6</mn></mfenced><mo>,</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mfrac><mrow><mo>-</mo><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>5</mn></msqrt></mrow><mn>2</mn></mfrac></mrow></mfenced><mo>.</mo></math></p><p>Out of the given options only <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>4</mn></mfrac></math> is not in the interval obtained.</p></blockquote>

</details>

---

### Q48. JEE Main 2019 (09 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi></math> and <math><mi>c</mi></math> be three distinct real numbers in G.P. and <math><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mi>x</mi><mi>b</mi><mo>,</mo></math> then <math><mi>x</mi></math> cannot be:

**Options:**

- **(A)** <math><mo>-</mo><mn>3</mn></math>
- **(B)** <math><mn>2</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>2</mn></math>**

**Detailed Solution:**

Given <math><mi>a</mi><mo>,</mo><mi>&#160;</mi><mi>b</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi></math> are in G.P.

Let common ratio of G.P. be <math><mi>r</mi></math> , then <math><mi>b</mi><mo>=</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>&#160;</mi><mi>c</mi><mo>=</mo><mi>a</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

Given equation can be written as

<math><mi>a</mi><mo>+</mo><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mi>x</mi><mo>.</mo><mtext>&#8201;</mtext><mi>a</mi><mo>.</mo><mtext>&#8201;</mtext><mi>r</mi></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mi>r</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac><mo>+</mo><mn>1</mn></math>

As we know <math><mi>r</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo></math> then <math><mi>r</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac><mo>&#8805;</mo><mn>2</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8805;</mo><mn>3</mn></math>

<math><mi>r</mi><mo>&#60;</mo><mn>0</mn><mo>,</mo></math> then <math><mi>r</mi><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>r</mi></mrow></mfrac><mo>&#8804;</mo><mo>-</mo><mn>2</mn><mo>&#8658;</mo><mi>x</mi><mo>&#8804;</mo><mo>-</mo><mn>1</mn></math>

<math><mo>&#8658;</mo><mi>x</mi><mo>&#8712;</mo><mfenced close="]" separators="|"><mrow><mo>-</mo><mi>&#8734;</mi><mo>,</mo><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#8746;</mo><mfenced open="[" separators="|"><mrow><mn>3</mn><mo>,</mo><mtext>&#8201;</mtext><mi>&#8734;</mi></mrow></mfenced></math>

Hence, <math><mi>x</mi><mi>&#160;</mi><mo>&#8800;</mo><mn>2</mn><mo>.</mo></math>

</details>

---

### Q49. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is the first term of an infinite geometric progression whose sum is five, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> lies in the interval

**Options:**

- **(A)** <math><mfenced close="" open="[" separators="|"><mrow><mn>10</mn><mo>,</mo><mi> </mi><mfenced open="" separators="|"><mrow><mi>∞</mi></mrow></mfenced></mrow></mfenced></math>
- **(B)** <math><mfenced close="" separators="|"><mrow><mo>-</mo><mi>∞</mi><mo>,</mo><mfenced close="]" open="" separators="|"><mrow><mo>-</mo><mn>10</mn></mrow></mfenced></mrow></mfenced></math>
- **(C)** <math><mfenced separators="|"><mrow><mo>-</mo><mn>10</mn><mo>,</mo><mi> </mi><mn>0</mn></mrow></mfenced></math>
- **(D)** <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>10</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi> </mi><mn>10</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is the first term and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is the common ratio of an infinite G.P. and sum is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, then</p><p><math><mn>5</mn><mo>=</mo><mfrac><mrow><mi>b</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>r</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mi>r</mi><mo>=</mo><mfrac><mi>b</mi><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mi>b</mi><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>-</mo><mi>b</mi></mrow><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mi>r</mi><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>-</mo><mn>1</mn><mo>&#60;</mo><mfrac><mrow><mn>5</mn><mo>-</mo><mi>b</mi></mrow><mn>5</mn></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>5</mn><mo>&#60;</mo><mn>5</mn><mo>-</mo><mi>b</mi><mo>&#60;</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>10</mn><mo>&#60;</mo><mo>-</mo><mi>b</mi><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>0</mn><mo>&#60;</mo><mi>b</mi><mo>&#60;</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>&#8712;</mo><mfenced separators="|"><mrow><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>10</mn></mrow></mfenced></math></p>

</details>

---

### Q50. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `1`

If $b$ is the first term of an infinite G. P whose sum is five, then $b$ lies in the interval.

**Options:**

- **(A)** $(-\infty,-10)$
- **(B)** $(10, \infty)$
- **(C)** $(0,10)$
- **(D)** $(-10,0)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $(0,10)$**

**Detailed Solution:**

First term $=b$ and common ratio $=\mathrm{r}$
For infinite series, Sum $=\frac{b}{1-r}=5$ $\Rightarrow b=5(1-\mathrm{r})$
So, interval of $b=(0,10)$ as, $-1 < \mathrm{r} < 1$ for infinite GP.

</details>

---

### Q51. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the <math><msup><mrow><mn>3</mn></mrow><mrow><mi>r</mi><mi>d</mi></mrow></msup></math> and the <math><msup><mrow><mn>4</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> terms of a <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> is <math> <mrow> <mn>60</mn> </mrow> </math> and the product of its first three terms is <math> <mrow> <mn>1000.</mn> </mrow> </math> If the first term of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> is positive, then its <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is:

**Options:**

- **(A)** <math> <mrow> <mn>320</mn> </mrow> </math>
- **(B)** <math> <mrow> <mn>640</mn> </mrow> </math>
- **(C)** <math> <mrow> <mn>2430</mn> </mrow> </math>
- **(D)** <math> <mrow> <mn>7290</mn> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mn>320</mn> </mrow> </math>**

**Detailed Solution:**

<p>Let the <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>'</mo><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo><mo>'</mo></math> be

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>r</mi></mfrac><mo>,</mo><mi>a</mi><mo>,</mo><mi>a</mi><mi>r</mi><mo>,</mo><mi>a</mi><msup><mi>r</mi><mn>2</mn></msup></math>

Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>a</mi><mi>r</mi></mfrac><mo>&#183;</mo><mi>a</mi><mo>&#183;</mo><mi>a</mi><mi>r</mi><mo>=</mo><mn>1000</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>3</mn></msup><mo>=</mo><mn>1000</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>10</mn></math>

Also, <math><mi>a</mi><mi>r</mi><mo>+</mo><mi>a</mi><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>60</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>60</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>+</mo><msup><mi>r</mi><mn>2</mn></msup><mo>=</mo><mn>6</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>r</mi><mo>-</mo><mn>6</mn><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math>

So, <math><mi>r</mi><mo>=</mo><mn>2</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mo>-</mo><mn>3</mn></math>

As <math><msup><mrow><mn>1</mn></mrow><mrow><mi>s</mi><mi>t</mi></mrow></msup></math> term is positive <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>r</mi><mo>=</mo><mn>2</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">G</mi><mo>.</mo><mi mathvariant="normal">P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>'</mo><mn>5</mn><mo>'</mo><mo>,</mo><mo>&#160;</mo><mo>'</mo><mn>10</mn><mo>'</mo><mo>,</mo><mo>&#160;</mo><mo>'</mo><mn>20</mn><mo>'</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>

Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>&#183;</mo><msup><mfenced separators="|"><mn>2</mn></mfenced><mn>6</mn></msup><mo>=</mo><mn>320</mn><mo>.</mo></math></p>

</details>

---

### Q52. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The least positive integer $\mathrm{n}$ such that $1-\frac{2}{3}-\frac{2}{3^2}-\ldots .-\frac{2}{3^{n-1}} < \frac{1}{100}$, is:

**Options:**

- **(A)** 4
- **(B)** 5
- **(C)** 6
- **(D)** 7

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 5**

**Detailed Solution:**

$$
\begin{aligned}
&1-\frac{2}{3}-\frac{2}{3^2} \ldots \cdot \frac{2}{3^{n-1}} < \frac{1}{100} \\
&\Rightarrow 1-\frac{2}{3}\left[\frac{1}{3}+\frac{1}{3^2}+\frac{1}{3^3}+\ldots \frac{1}{3^{n-1}}\right] < \frac{1}{100} \\
&\Rightarrow \frac{1-2\left[\frac{1}{3}\left(\frac{1}{3^n}-1\right)\right]}{\frac{1}{3}-1} < \frac{1}{100} \\
&\Rightarrow 1-2\left[\frac{3^n-1}{2.3^n}\right] < \frac{1}{100} \\
&\Rightarrow 1-\left[\frac{3^n-1}{3^n}\right] < \frac{1}{100} \\
&\Rightarrow 1-1+\frac{1}{3^n} < \frac{1}{100}
\end{aligned}
$$

$$
\Rightarrow 100 < 3^n
$$
Thus, least value of $n$ is 5

</details>

---

### Q53. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

Let $\mathrm{G}$ be the geometric mean of two positive numbers $\mathrm{a}$ and $\mathrm{b}$, and $\mathrm{M}$ be the arithmetic mean of $\frac{1}{\mathrm{a}}$ and $\frac{1}{\mathrm{~b}}$. If $\frac{1}{\mathrm{M}}: \mathrm{G}$ is $4: 5$, then $\mathrm{a}: \mathrm{b}$ can be:

**Options:**

- **(A)** $1: 4$
- **(B)** $1: 2$
- **(C)** $2: 3$
- **(D)** $3: 4$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $1: 4$**

**Detailed Solution:**

$\mathrm{G}=\sqrt{a b}$
$$
\begin{aligned}
&\mathrm{M}=\frac{\frac{1}{a}+\frac{1}{b}}{2} \\
&\mathrm{M}=\frac{a+b}{2 a b}
\end{aligned}
$$
Given that $\frac{1}{\mathrm{M}}: \mathrm{G}=4: 5$

$$
\begin{aligned}
& \frac{2 a b}{(a+b) \sqrt{a b}}=\frac{4}{5} \\
\Rightarrow & \frac{a+b}{2 \sqrt{a b}}=\frac{5}{4} \\
\Rightarrow & \frac{a+b+2 \sqrt{a b}}{a+b-2 \sqrt{a b}}=\frac{5+4}{5-4}
\end{aligned}
$$
\{Using Componendo \& Dividendo
$$
\begin{aligned}
&\Rightarrow \frac{(\sqrt{a})^2+(\sqrt{b})^2+2 \sqrt{a b}}{(\sqrt{a})^2+(\sqrt{b})^2-2 \sqrt{a b}}=\frac{9}{1} \\
&\Rightarrow\left(\frac{\sqrt{b}+\sqrt{a})^2}{\sqrt{b}-\sqrt{a}}\right)^2=\frac{9}{1} \Rightarrow \frac{\sqrt{b}+\sqrt{a}}{\sqrt{b}-\sqrt{a}}=\frac{3}{1} \\
&\Rightarrow \frac{\sqrt{b}+\sqrt{a}+\sqrt{b}-\sqrt{a}}{\sqrt{b}+\sqrt{a}-\sqrt{b}+\sqrt{a}}=\frac{3+1}{3-1}
\end{aligned}
$$
\{Using Componendo \& Dividendo
$$
\sqrt{\frac{b}{a}}=\frac{4}{2}=2
$$

$$
\begin{aligned}
\frac{b}{a} &=\frac{4}{1} \\
\frac{a}{b} &=\frac{1}{4} \Rightarrow a: b=1: 4
\end{aligned}
$$

</details>

---

### Q54. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

In a geometric progression, if the ratio of the sum of first 5 terms to the sum of their reciprocals is 49 , and the sum of the first and the third term is 35. Then the first term of this geometric progression is:

**Options:**

- **(A)** 7
- **(B)** 21
- **(C)** 28
- **(D)** 42

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 28**

**Detailed Solution:**

According to Question
$$
\Rightarrow \frac{S_5}{S_5^{\prime}}=49
$$
(here, $S_5=$ Sum of first 5 terms and $S_5=$ Sum of their reciprocals)
$$
\begin{aligned}
&\Rightarrow \frac{\frac{a\left(r^5-1\right)}{(r-1)}}{\frac{a^{-1}\left(r^{-5}-1\right)}{\left(r^{-1}-1\right)}}=49 \\
&\Rightarrow \frac{a\left(r^5-1\right) \times\left(r^{-1}-1\right)}{a^{-1}\left(r^{-5}-1\right) \times(r-1)}=49 \\
&\text { or } \frac{a^2\left(1-r^5\right) \times(1-r) \times r^5}{\left(1-r^5\right) \times(1-\mathrm{r}) \times r}=49 \\
&\Rightarrow a^2 r^4=49 \Rightarrow a^2 r^4=7^2 \\
&\Rightarrow a r^2=7
\end{aligned}
$$
Also, given, $S_1+S_3=35$ $a+a r^2=35$
Now substituting the value of eq. (1) in eq. (2)
$a+7=35$
$a=28$

</details>

---

### Q55. JEE Main 2013 (07 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of the sequence <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>77</mn><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>.</mo><mn>777</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo></math> is :

**Options:**

- **(A)** <math> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>7</mn> <mn>9</mn> <mo>+</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>2</mn> <mn>0</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>
- **(B)** <math> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>9</mn> <mn>9</mn> <mo>+</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>2</mn> <mn>0</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>7</mn> <mn>9</mn> <mo>-</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>2</mn> <mn>0</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>9</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>9</mn> <mn>9</mn> <mo>-</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>2</mn> <mn>0</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math> <mrow> <mfrac> <mrow> <mn>7</mn> </mrow> <mrow> <mn>8</mn> <mn>1</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>7</mn> <mn>9</mn> <mo>+</mo> <mn>1</mn> <msup> <mn>0</mn> <mrow> <mo>-</mo> <mn>2</mn> <mn>0</mn> </mrow> </msup> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>0</mn><mo>&#183;</mo><mn>7</mn><mo>+</mo><mn>0</mn><mo>&#183;</mo><mn>7</mn><mn>7</mn><mo>+</mo><mn>0</mn><mo>&#183;</mo><mn>7</mn><mn>7</mn><mn>7</mn><mo>+</mo><mo>.</mo><mo>....</mo></math>,</p><p>Here, number of terms is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mo>(</mo><mn>0</mn><mo>&#183;</mo><mn>9</mn><mo>+</mo><mn>0</mn><mo>&#183;</mo><mn>99</mn><mo>+</mo><mn>0</mn><mo>&#183;</mo><mn>999</mn><mo>+</mo><mo>.</mo><mo>...)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mfrac><mn>9</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>99</mn><msup><mn>10</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>999</mn><msup><mn>10</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mfrac><mrow><mn>10</mn><mo>-</mo><mn>1</mn></mrow><mn>10</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mn>10</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>10</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mn>10</mn><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow><msup><mn>10</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>10</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>10</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><msup><mn>10</mn><mi>n</mi></msup></mfrac></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mn>10</mn><mi>n</mi></msup></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>10</mn></mfrac></mrow></mfrac></mrow></mfenced></math></p><p>For the sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>20</mn></math>.

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mn>2</mn><mn>0</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mn>0</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><msup><mn>0</mn><mrow><mn>2</mn><mn>0</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mn>0</mn></mrow></mfrac></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;S</mtext><mo>=</mo><mfrac><mn>7</mn><mn>9</mn></mfrac><mfenced><mrow><mn>2</mn><mn>0</mn><mo>-</mo><mfrac><mrow><mn>1</mn><mo>-</mo><mn>1</mn><msup><mn>0</mn><mrow><mo>-</mo><mn>2</mn><mn>0</mn></mrow></msup></mrow><mn>9</mn></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#8658;S</mtext><mo>=</mo><mfrac><mn>7</mn><mrow><mn>8</mn><mn>1</mn></mrow></mfrac><mfenced><mrow><mn>1</mn><mn>7</mn><mn>9</mn><mo>+</mo><mn>1</mn><msup><mn>0</mn><mrow><mo>-</mo><mn>2</mn><mn>0</mn></mrow></msup></mrow></mfenced></math></p>

</details>

---

### Q56. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `1`

The difference between the fourth term and the first term of a Geometrical Progresssion is 52. If the sum of its first three terms is 26 , then the sum of the first six terms of the progression is

**Options:**

- **(A)** 63
- **(B)** 189
- **(C)** 728
- **(D)** 364

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 728**

**Detailed Solution:**

Let $a, a r, a r^2, a r^3, a r^4, a r^5$ be six terms of a G.P. where ' $a$ ' is first term and $\mathrm{r}$ is common ratio.
According to given conditions, we have $a r^3-a=5 \Rightarrow a\left(r^3-1\right)=52$ and $a+a r+a r^2=26$ $\Rightarrow a\left(1+r+r^2\right)=26$
To find: $a\left(1+r+r^2+r^3+r^4+r^5\right)$
Consider
$$
\begin{aligned}
& a\left[1+r+r^2+r^3+r^4+r^5\right] \\
& =a\left[1+r+r^2+r^3\left(1+r+r^2\right)\right] \\
& =a\left[1+r+r^2\right]\left[1+r^3\right]
\end{aligned}
$$
Divide (1) by (2), we get
$$
\frac{r^3-1}{1+r+r^2}=2
$$
we know $r^3-1=(r-1)\left(1+r+r^2\right)$
$$
\begin{aligned}
& \therefore r-1=2 \Rightarrow r=3 \text { and } a=2 \\
& \therefore \quad a\left(1+r+r^2+r^3+r^4+r^5\right) \\
& \quad=a\left(1+r+r^2\right)\left(1+r^3\right) \\
& \quad=2(1+3+9)(1+27) \\
& \quad=26 \times 28=728
\end{aligned}
$$

</details>

---

### Q57. JEE Main 2008

*Type:* `singleCorrect` | *Level:* `1`

The first two terms of a geometric progression add up to 12. The sum of the third and the fourth terms is 48. If the terms of the geometric progression are alternately positive and negative, then the first term is

**Options:**

- **(A)** $-4$
- **(B)** $-12$
- **(C)** 12
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-12$**

**Detailed Solution:**

Let $a, a r, a r^2, \ldots$
$a+a r=12$
$a r^2+a r^3=48$
dividing (2) by (1), we have
$$
\begin{aligned}
& \frac{a r^2(1+r)}{a(r+1)}=4 \\
& \Rightarrow r^2=4 \text { if } r \neq-1 \\
& \therefore r=-2 \\
& \text { also, } a=-12 \quad \text { (using (1)). }
\end{aligned}
$$

</details>

---

### Q58. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `1`

In a geometric progression consisting of positive terms, each term equals the sum of the next two terms. Then the common ratio of this progression equals

**Options:**

- **(A)** $\frac{1}{2}(1-\sqrt{5})$
- **(B)** $\frac{1}{2} \sqrt{5}$
- **(C)** $\sqrt{5}$
- **(D)** $\frac{1}{2}(\sqrt{5}-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{1}{2}(\sqrt{5}-1)$**

**Detailed Solution:**

Given $a r^{n-1}=a r^n+a r^{n+1}$
$\begin{aligned}
& \Rightarrow 1=r+r^2 \\
& \therefore r=\frac{\sqrt{5}-1}{2} .
\end{aligned}$

</details>

---

### Q59. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{x}_1, \mathrm{x}_2, \mathrm{x}_3$ and $\mathrm{y}_1, \mathrm{y}_2, \mathrm{y}_3$ are both in G.P. with the same common ratio, then the points $\left(\mathrm{x}_1, \mathrm{y}_1\right),\left(\mathrm{x}_2, \mathrm{y}_2\right)$ and $\left(\mathrm{x}_3\right.$, $\mathrm{y}_3$ )

**Options:**

- **(A)** are vertices of a triangle
- **(B)** lie on a straight line
- **(C)** lie on an ellipse
- **(D)** lie on a circle

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) lie on a straight line**

**Detailed Solution:**

Taking co-ordinates as $\left(\frac{\mathrm{x}}{\mathrm{r}}, \frac{\mathrm{y}}{\mathrm{r}}\right) ;(\mathrm{x}, \mathrm{y}) \&(\mathrm{xr}, \mathrm{yr})$. Above coordinates satisfy the relation $\mathrm{y}=\mathrm{mx}$ Therefore lies on the straight line.

</details>

---

### Q60. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Sum of infinite number of terms of GP is 20 and sum of their square is 100. The common ratio of GP is

**Options:**

- **(A)** 5
- **(B)** 3/5
- **(C)** 8/5
- **(D)** 1/5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 8/5**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/_C5Np_GpLmu7Tqg0PGMgkSFjkPhcF9Kg5KjOyevPkHk.original.fullsize.png">

</details>

---

### Q61. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

Fifth term of a GP is 2, then the product of its 9 terms is

**Options:**

- **(A)** 256
- **(B)** 512
- **(C)** 1024
- **(D)** none of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 512**

**Detailed Solution:**

$\operatorname{ar}^4=2$
$\mathrm{a} \times \operatorname{ar} \times \mathrm{ar}^2 \times a r^3 \times \mathrm{ar}^4 \times \mathrm{ar}^5 \times a r^6 \times a r^7 \times a r^8$
$=a^9 r^{36}=\left(\operatorname{ar}^4\right)^9=2^9=512$

</details>

---

### Q62. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The value of $2^{1 / 4}, 4^{1 / 8}, 8^{1 / 6}+\ldots \ldots \infty$ is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3/2
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 2**

**Detailed Solution:**

No Solution Available

</details>

---

