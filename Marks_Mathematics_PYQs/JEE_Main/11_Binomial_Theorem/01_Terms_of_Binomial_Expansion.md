# JEE Main Mathematics - Binomial Theorem

## Topic 1: Terms of Binomial Expansion

**Total Questions:** 143

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `numerical` | *Level:* `3`

If $(1 - x^3)^{10} = \sum\limits_{r=0}^{10} a_r x^r (1-x)^{30-2r}$, then $\dfrac{9a_9}{a_{10}}$ is equal to __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **30**

**Detailed Solution:**

The given equation is:

$(1 - x^3)^{10} = \sum\limits_{r=0}^{10} a_r x^r (1-x)^{30-2r}$

Using the algebraic identity $1 - x^3 = (1-x)(1+x+x^2)$, the left hand side can be written as:

$(1-x)^{10}(1+x+x^2)^{10} = \sum\limits_{r=0}^{10} a_r x^r (1-x)^{30-2r}$

Dividing both sides by $(1-x)^{30}$:

$\dfrac{(1-x)^{10}(1+x+x^2)^{10}}{(1-x)^{30}} = \sum\limits_{r=0}^{10} a_r \dfrac{x^r}{(1-x)^{2r}}$

$\left( \dfrac{1+x+x^2}{(1-x)^2} \right)^{10} = \sum\limits_{r=0}^{10} a_r \left( \dfrac{x}{(1-x)^2} \right)^r$

Let $y = \dfrac{x}{(1-x)^2}$.

The term inside the bracket on the left hand side can be simplified as:

$\dfrac{1+x+x^2}{(1-x)^2} = \dfrac{1-2x+x^2+3x}{(1-x)^2} = \dfrac{(1-x)^2+3x}{(1-x)^2} = 1 + 3\left(\dfrac{x}{(1-x)^2}\right) = 1 + 3y$

Substituting this into the equation, we get:

$(1 + 3y)^{10} = \sum\limits_{r=0}^{10} a_r y^r$

Using the binomial expansion, $(1 + 3y)^{10} = \sum\limits_{r=0}^{10} {^{10}C_{r}} (3y)^r = \sum\limits_{r=0}^{10} {^{10}C_{r}} 3^r y^r$.

Comparing the coefficients of $y^r$ on both sides, we obtain:

$a_r = {^{10}C_{r}} 3^r$

For $r = 9$ and $r = 10$:

$a_9 = {^{10}C_{9}} 3^9 = 10 \times 3^9$

$a_{10} = {^{10}C_{10}} 3^{10} = 1 \times 3^{10} = 3^{10}$

Therefore, the required value is:

$\dfrac{9a_9}{a_{10}} = \dfrac{9 \times 10 \times 3^9}{3^{10}} = \dfrac{90 \times 3^9}{3 \times 3^9} = \dfrac{90}{3} = 30$

Answer: $30$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficients of the middle terms in the binomial expansions of $(1 + \alpha x)^{26}$ and $(1 - \alpha x)^{28}$, $\alpha \neq 0$, are equal, then the value of $\alpha$ is:

**Options:**

- **(A)** $1$
- **(B)** $\dfrac{14}{13}$
- **(C)** $\dfrac{27}{7}$
- **(D)** $\dfrac{7}{27}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\dfrac{7}{27}$**

**Detailed Solution:**

The expansion of $(1 + \alpha x)^{26}$ has $27$ terms. The middle term is $T_{14}$.

The coefficient of the middle term is $^{26}C_{13} \alpha^{13}$.

The expansion of $(1 - \alpha x)^{28}$ has $29$ terms. The middle term is $T_{15}$.

The coefficient of the middle term is $^{28}C_{14} (-\alpha)^{14} = ^{28}C_{14} \alpha^{14}$.

Equating the two coefficients:

$^{26}C_{13} \alpha^{13} = ^{28}C_{14} \alpha^{14}$

Since $\alpha \neq 0$, dividing by $\alpha^{13}$ gives:

$\alpha = \dfrac{^{26}C_{13}}{^{28}C_{14}}$

Expanding the combinations using factorials:

$^{28}C_{14} = \dfrac{28!}{14! 14!} = \dfrac{28 \times 27 \times 26!}{14 \times 13! \times 14 \times 13!} = \dfrac{28 \times 27}{14 \times 14} \times \dfrac{26!}{13! 13!}$

$^{28}C_{14} = \dfrac{27}{7} \times ^{26}C_{13}$

Substituting this back:

$\alpha = \dfrac{^{26}C_{13}}{\dfrac{27}{7} \times ^{26}C_{13}} = \dfrac{7}{27}$

Answer: $\dfrac{7}{27}$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of $x^2$ in the expansion of $\left(2x^2 + \dfrac{1}{x}\right)^{10}$, $x \neq 0$, is :

**Options:**

- **(A)** $3240$
- **(B)** $3360$
- **(C)** $3480$
- **(D)** $3600$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3360$**

**Detailed Solution:**

The general term in the expansion of $\left(2x^2 + \dfrac{1}{x}\right)^{10}$ is given by:

$T_{r+1} = ^{10}C_{r} (2x^2)^{10-r} \left(\dfrac{1}{x}\right)^r$

$T_{r+1} = ^{10}C_{r} 2^{10-r} x^{20-2r} x^{-r}$

$T_{r+1} = ^{10}C_{r} 2^{10-r} x^{20-3r}$

For the coefficient of $x^2$, we equate the power of $x$ to $2$:

$20 - 3r = 2$

$3r = 18 \Rightarrow r = 6$

Substituting $r = 6$ in the coefficient part, we get:

Coefficient $= ^{10}C_{6} 2^{10-6}$

$= ^{10}C_{4} 2^4$

$= \dfrac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} \times 16$

$= 210 \times 16$

$= 3360$

Answer: $3360$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `numerical` | *Level:* `2`

If the sum of the coefficients of $x^7$ and $x^{14}$ in the expansion of $\left(\dfrac{1}{x^3} - x^4\right)^n$, $x \neq 0$, is zero, then the value of $n$ is __________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

The general term in the expansion of $\left(\dfrac{1}{x^3} - x^4\right)^n$ is given by:

$T_{r+1} = ^{n}C_{r} \left(x^{-3}\right)^{n-r} \left(-x^4\right)^r = (-1)^r \cdot ^{n}C_{r} \cdot x^{7r - 3n}$

For the coefficient of $x^7$, we set the exponent to $7$:

$7r_1 - 3n = 7 \Rightarrow r_1 = \dfrac{3n + 7}{7}$

For the coefficient of $x^{14}$, we set the exponent to $14$:

$7r_2 - 3n = 14 \Rightarrow r_2 = \dfrac{3n + 14}{7}$

Notice that $r_2 = r_1 + 1$.

The sum of the coefficients of $x^7$ and $x^{14}$ is zero:

$(-1)^{r_1} \cdot ^{n}C_{r_1} + (-1)^{r_2} \cdot ^{n}C_{r_2} = 0$

$(-1)^{r_1} \cdot ^{n}C_{r_1} + (-1)^{r_1 + 1} \cdot ^{n}C_{r_1 + 1} = 0$

$(-1)^{r_1} \left( ^{n}C_{r_1} - ^{n}C_{r_1 + 1} \right) = 0$

$^{n}C_{r_1} = ^{n}C_{r_1 + 1}$

Since $r_1 \neq r_1 + 1$, we must use the property $^{n}C_{x} = ^{n}C_{y} \Rightarrow x + y = n$:

$r_1 + (r_1 + 1) = n$

$2r_1 + 1 = n$

Substituting $r_1 = \dfrac{3n + 7}{7}$:

$2\left(\dfrac{3n + 7}{7}\right) + 1 = n$

$\dfrac{6n + 14}{7} + 1 = n$

$6n + 14 + 7 = 7n$

$n = 21$

Answer: $21$

</details>

---

### Q5. JEE Main 2026 (04 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the expansion of $\left(9x-\dfrac{1}{3\sqrt{x}}\right)^{18}$, $x>0$, if the term independent of $x$ is $(221)k$, then $k$ is equal to:

**Options:**

- **(A)** $84$
- **(B)** $78$
- **(C)** $168$
- **(D)** $198$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $84$**

**Detailed Solution:**

The general term in the expansion of $\left(9x - \dfrac{1}{3\sqrt{x}}\right)^{18}$ is given by:

$T_{r+1} = ^{18}C_{r} (9x)^{18-r} \left(-\dfrac{1}{3\sqrt{x}}\right)^r$

$T_{r+1} = ^{18}C_{r} 9^{18-r} \left(-\dfrac{1}{3}\right)^r x^{18-r} x^{-r/2}$

$T_{r+1} = ^{18}C_{r} 9^{18-r} \left(-\dfrac{1}{3}\right)^r x^{18 - \dfrac{3r}{2}}$

For the term independent of $x$, the exponent of $x$ must be zero:

$18 - \dfrac{3r}{2} = 0$

$\dfrac{3r}{2} = 18 \Rightarrow r = 12$

Substituting $r = 12$ into the general term:

$T_{13} = ^{18}C_{12} 9^{18-12} \left(-\dfrac{1}{3}\right)^{12}$

$T_{13} = ^{18}C_{12} 9^6 \left(\dfrac{1}{3}\right)^{12}$

$T_{13} = ^{18}C_{12} (3^2)^6 \dfrac{1}{3^{12}}$

$T_{13} = ^{18}C_{12} 3^{12} \dfrac{1}{3^{12}} = ^{18}C_{12}$

Now, calculating $^{18}C_{12}$:

$^{18}C_{12} = ^{18}C_{6} = \dfrac{18 \times 17 \times 16 \times 15 \times 14 \times 13}{6 \times 5 \times 4 \times 3 \times 2 \times 1}$

$^{18}C_{12} = 17 \times 13 \times 3 \times 2 \times 14$

$^{18}C_{12} = 221 \times 84$

Given that the term independent of $x$ is $221k$:

$221k = 221 \times 84$

$k = 84$

Answer: $84$

</details>

---

### Q6. JEE Main 2026 (04 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let the smallest value of $k \in \mathbb{N}$, for which the coefficient of $x^3$ in $(1+x)^3 + (1+x)^4 + (1+x)^5 + \ldots + (1+x)^{99} + (1+kx)^{100}$, $x \neq 0$, is $\left(43n + \dfrac{101}{4}\right)\left(^{100}C_3\right)$ for some $n \in \mathbb{N}$, be $p$. Then the value of $p + n$ is:

**Options:**

- **(A)** $10$
- **(B)** $11$
- **(C)** $12$
- **(D)** $13$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $11$**

**Detailed Solution:**

The coefficient of $x^3$ in the given expression is the sum of the coefficients of $x^3$ in each term.

The coefficient of $x^3$ in $\sum_{r=3}^{99} (1+x)^r + (1+kx)^{100}$ is:

$\sum_{r=3}^{99} {}^{r}C_3 + k^3 {}^{100}C_3$

Using the identity $\sum_{r=k}^{n} {}^{r}C_k = {}^{n+1}C_{k+1}$, we get:

$\sum_{r=3}^{99} {}^{r}C_3 = {}^{100}C_4$

Thus, the total coefficient of $x^3$ is ${}^{100}C_4 + k^3 {}^{100}C_3$.

Given that this coefficient is equal to $\left(43n + \dfrac{101}{4}\right) {}^{100}C_3$, we have:

${}^{100}C_4 + k^3 {}^{100}C_3 = \left(43n + \dfrac{101}{4}\right) {}^{100}C_3$

Dividing both sides by ${}^{100}C_3$:

$\dfrac{^{100}C_4}{^{100}C_3} + k^3 = 43n + \dfrac{101}{4}$

Using $\dfrac{^{n}C_r}{^{n}C_{r-1}} = \dfrac{n-r+1}{r}$, we get $\dfrac{^{100}C_4}{^{100}C_3} = \dfrac{100-4+1}{4} = \dfrac{97}{4}$.

Substituting this value:

$\dfrac{97}{4} + k^3 = 43n + \dfrac{101}{4}$

$k^3 = 43n + \dfrac{101}{4} - \dfrac{97}{4}$

$k^3 = 43n + 1$

$k^3 - 1 = 43n$

Since $n \in \mathbb{N}$, we must have $n \ge 1$, which implies $k^3 - 1 \ge 43 \Rightarrow k \ge 4$.

Checking the values of $k \ge 4$ to find the smallest integer $k$ such that $k^3 - 1$ is divisible by $43$:

For $k = 4$, $k^3 - 1 = 63$ (not divisible by $43$).

For $k = 5$, $k^3 - 1 = 124$ (not divisible by $43$).

For $k = 6$, $k^3 - 1 = 215 = 43 \times 5$.

Thus, the smallest value of $k$ is $p = 6$, and the corresponding value of $n$ is $5$.

Therefore, $p + n = 6 + 5 = 11$.

Answer: $11$

</details>

---

### Q7. JEE Main 2026 (28 January Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the coefficients of $x^{499}$ and $x^{500}$ in $(1+x)^{1000}+x(1+x)^{999}+x^{2}(1+x)^{998}+\ldots+x^{1000}$ is :

**Options:**

- **(A)** ${ }^{1002} C_{500}$
- **(B)** ${ }^{1002} C_{501}$
- **(C)** ${ }^{1001} C_{501}$
- **(D)** ${ }^{1000} C_{501}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) ${ }^{1002} C_{500}$**

**Detailed Solution:**

$S = (1+x)^{1000} + x(1+x)^{999} + x^2(1+x)^{998} + \cdots + x^{1000}$
This is a geometric series with first term $(1+x)^{1000}$, common ratio $\frac{x}{1+x}$, and 1001 terms.
$S = (1+x)^{1000} \cdot \dfrac{1 - \left(\frac{x}{1+x}\right)^{1001}}{1 - \frac{x}{1+x}}$
$= (1+x)^{1001} - x^{1001}$
Required sum = coefficient of $x^{499}$ + coefficient of $x^{500}$ in $(1+x)^{1001} - x^{1001}$ 
 $= {}^{1001}C_{499} + {}^{1001}C_{500} = {}^{1002}C_{500}$

</details>

---

### Q8. JEE Main 2026 (23 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of all possible values of $\mathrm{n} \in \mathbf{N}$, so that the coefficients of $x, x^{2}$ and $x^{3}$ in the expansion of $\left(1+x^{2}\right)^{2}(1+x)^{\mathrm{n}}$, are in arithmetic progression is :

**Options:**

- **(A)** 12
- **(B)** 7
- **(C)** 3
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 9**

**Detailed Solution:**

$(1+x^2)^2 = 1 + 2x^2 + x^4$. Multiply with $(1+x)^n$:
Coefficient of $x$: $n$.
Coefficient of $x^2$: $\binom{n}{2} + 2 = \frac{n(n-1)}{2} + 2$.
Coefficient of $x^3$: $\binom{n}{3} + 2n = \frac{n(n-1)(n-2)}{6} + 2n$.
For AP: $2\left(\frac{n(n-1)}{2}+2\right) = n + \frac{n(n-1)(n-2)}{6} + 2n$.
Simplifying: $n^3 - 9n^2 + 26n - 24 = 0$.
$(n-2)(n-3)(n-4) = 0 \Rightarrow n = 2, 3, 4$.
Sum $= 2 + 3 + 4 = 9$.

</details>

---

### Q9. JEE Main 2026 (21 January Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the coefficient of $x$ in the expansion of $\left(a x^{2}+b x+c\right)(1-2 x)^{26}$ is -56 and the coefficients of $x^{2}$ and $x^{3}$ are both zero, then $\mathrm{a}+\mathrm{b}+\mathrm{c}$ is equal to :

**Options:**

- **(A)** 1500
- **(B)** 1300
- **(C)** 1403
- **(D)** 1483

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 1403**

**Detailed Solution:**

In $(1-2x)^{26}$: $T_0 = 1$, $T_1 = -52$, $T_2 = 1300$, $T_3 = -20800$.
Coefficient of $x$: $b - 52c = -56$ ...(1)
Coefficient of $x^2$: $a - 52b + 1300c = 0$ ...(2)
Coefficient of $x^3$: $-52a + 1300b - 20800c = 0$ ...(3)
From (1): $b = 52c - 56$. Substituting in (2): $a = 1404c - 2912$.
Substituting in (3): $-26208c + 78624 = 0 \Rightarrow c = 3$.
Thus $b = 100$, $a = 1300$.
$a + b + c = 1300 + 100 + 3 = 1403$.

</details>

---

### Q10. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

In the expansion of $\left(\sqrt[3]{2}+\frac{1}{\sqrt[3]{3}}\right)^n, \mathrm{n} \in \mathrm{N}$, if the ratio of $15^{\text {at }}$ term from the beginning to the $15^{\text {th }}$ term from the end is $\frac{1}{6}$, then the value of ${ }^n C_3$ is:

**Options:**

- **(A)** 4060
- **(B)** 1040
- **(C)** 2300
- **(D)** 4960

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2300**

**Detailed Solution:**

$\begin{aligned}
& \mathrm{T}_{\mathrm{r}+1}={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}}\left(2^{1 / 3}\right)^{\mathrm{n}-\mathrm{r}}\left(\frac{1}{3^{1 / 3}}\right)^{\mathrm{r}} \\
& \mathrm{r}=14 \\
& \mathrm{~T}_{15}={ }^{\mathrm{n}} \mathrm{C}_{14}\left(2^{1 / 3}\right)^{\mathrm{n}-14}\left(\frac{1}{3^{1 / 3}}\right)^{14}
\end{aligned}$
$\mathrm{T}_{15}^{\prime}=15^{\mathrm{h}}$ term from last is $(\mathrm{n}-13)^{\mathrm{h}}$ term from beginning.
$\begin{aligned} & \mathrm{T}_{15}^{\prime}={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{n}-14}\left(2^{1 / 3}\right)^{14}\left(\frac{1}{3^{1 / 3}}\right)^{\mathrm{n}-14} \\ & \Rightarrow \frac{\mathrm{~T}_{15}}{\mathrm{~T}_{15}^{\prime}}=\frac{{ }^{\mathrm{n}} \mathrm{C}_{14}\left(2^{1 / 3}\right)^{\mathrm{n}-14}\left(\frac{1}{3^{1 / 3}}\right)^{14}}{{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{n}-14}\left(2^{1 / 3}\right)^{14}\left(\frac{1}{3^{1 / 3}}\right)^{\mathrm{n}-14}}=\frac{1}{6}\end{aligned}$
$\begin{aligned} & =\left(2^{1 / 3}\right)^{n-28}\left(3^{1 / 3}\right)^{n-28}=\frac{1}{6} \\ & =6^{\frac{n-28}{3}}=6^{-1}\end{aligned}$
$\text { So, }{ }^n \mathrm{C}_3={ }^{25} \mathrm{C}_3=2300$

</details>

---

### Q11. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For an integer $\mathrm{n} \geq 2$, if the arithmetic mean of all coefficients in the binomial expansion of $(x+y)^{2 n-3}$ is 16 , then the distance of the point $P\left(2 n-1, n^2-4 n\right)$ from the line $x+y=8$ is:

**Options:**

- **(A)** $\sqrt{2}$
- **(B)** $2 \sqrt{2}$
- **(C)** $5 \sqrt{2}$
- **(D)** $3 \sqrt{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $3 \sqrt{2}$**

**Detailed Solution:**

No. of terms in $(x+y)^{(2 n-3)} \Rightarrow\left[\begin{array}{c}(2 n-3+1) \\ (2 n-2)\end{array}\right].$ 
$\therefore$ sum of all coefficients $=2^{2 n-3}$
(Put $\mathrm{x}=\mathrm{y}=1$ )
$\therefore$ Arithmetic mean of all coefficients
$\begin{aligned}
& =\left(\frac{2^{2 n-3}}{2 n-2}\right)=16 \\
& \Rightarrow 2^{2 n-3}=2^5(n-1) \Rightarrow n=5 \\
& \therefore P\left(2 n-1, n^2-4 n\right)=(9,5)
\end{aligned}$

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zQOPegNaGroihIXObDobjfcSVyZC8NsiEeh7ci6YInA.original.fullsize.png"/>


$\begin{aligned} & x+y=8 \\ & \therefore P M=\left|\frac{9+5-8}{\sqrt{2}}\right|=\frac{6}{\sqrt{2}}=\frac{3 \times 2}{\sqrt{2}}=3 \sqrt{2}\end{aligned}$

</details>

---

### Q12. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

The sum of all rational terms in the expansion of $(2+\sqrt{3})^8$ is

**Options:**

- **(A)** $16923$
- **(B)** $3763$
- **(C)** $33845$
- **(D)** $18817$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $18817$**

**Detailed Solution:**

$S=(2+\sqrt{3})^8$
For sum of rational terms
$\begin{aligned} & ={ }^8 \mathrm{C}_0(2)^8+{ }^8 \mathrm{C}_2(2)^6 \cdot(\sqrt{3})^2+{ }^8 \mathrm{C}_4(2)^4(\sqrt{3})^4 \\ & \quad+\quad{ }^8 \mathrm{C}_6(2)^2(\sqrt{3})^6+{ }^8 \mathrm{C}_8(\sqrt{3})^8 \\ & =2^8+28 \times 2^6 \cdot 3+70.2^4 \cdot 9+28.2^2 .27+81 \\ & =256+5376+10080+3024+81 \\ & =18817\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (2 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The term independent of $x$ in the expansion of $\left(\frac{(x+1)}{\left(x^{2 / 3}+1-x^{1 / 3}\right)}-\frac{(x+1)}{\left(x-x^{1 / 2}\right)}\right)^{10}, x\gt1$ is:

**Options:**

- **(A)** $210$
- **(B)** $150$
- **(C)** $240$
- **(D)** $120$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $210$**

**Detailed Solution:**

$\begin{aligned} & \left(\frac{(x+1)}{\left(x^{\frac{2}{3}}+1-x^{\frac{1}{3}}\right)}-\frac{(x-1)}{\left(x-x^{\frac{1}{2}}\right)}\right)^{10} \\ & =\left(\left(x^{\frac{1}{3}}+1\right)-\left(\frac{\sqrt{x}+1}{\sqrt{x}}\right)\right)^{10} \\ & =\left(x^{\frac{1}{3}}-\frac{1}{\sqrt{x}}\right)^{10} \\ & T_{r+1}={ }^{10} C_r(x)^{\frac{10-r}{3}}(-1)^r(x)^{-\frac{r}{2}} \\ & \frac{10-r}{3}-\frac{r}{2}=0 \\ & (20-2 r)-3 r=0 \\ & r^{10}=4 \\ & \Rightarrow{ }^{10} C_4(-1)^4=210\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The least value of n for which the number of integral terms in the Binomial expansion of \((\sqrt[3]{7}+\sqrt[12]{11})^{\mathrm{n}}\) is 183, is :

**Options:**

- **(A)** 2184
- **(B)** 2196
- **(C)** 2148
- **(D)** 2172

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2184**

**Detailed Solution:**

$\begin{aligned}
& \text { General term }={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}}\left\{7^{1 / 3}\right\}^{\mathrm{n}-\mathrm{r}}\left(11^{1 / 12}\right)^{\mathrm{r}} \\
& ={ }^{\mathrm{n}} \mathrm{C}_{\mathrm{r}}\{7\}^{\frac{\mathrm{n}-\mathrm{r}}{3}}(11)^{\mathrm{r} / 12}
\end{aligned}$

For integral terms, r must be multiple of 12
$\therefore \mathrm{r}=12 \mathrm{k}, \mathrm{k} \in \mathrm{~W}$

Total values of $r=183$
Hence $\max r=12(182)$
$=2184$

Min value of $n=2184$

</details>

---

### Q15. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let the coefficients of three consecutive terms $T_r, T_{r+1}$ and $T_{r+2}$ in the binomial expansion of $(a+b)^{12}$ be in a G.P. and let $p$ be the number of all possible values of $r$. Let $q$ be the sum of all rational terms in the binomial expansion of $(\sqrt[4]{3}+\sqrt[3]{4})^{12}$. Then $\mathrm{p}+\mathrm{q}$ is equal to :

**Options:**

- **(A)** $283$
- **(B)** $287$
- **(C)** $295$
- **(D)** $299$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $283$**

**Detailed Solution:**

Coefficient of
$\begin{aligned}
& T_r, T_{r+1}, T_{r+2} \rightarrow G P \\
& \Rightarrow\left({ }^{12} C_r\right)^2={ }^{12} C_{r-1} \cdot{ }^{12} C_{r+1}
\end{aligned}$
$\Rightarrow\left({ }^{12} C_r\right)^2={ }^{12} C_{r-1} \cdot{ }^{12} C_{r+1}$
but no three consecutive binomial coefficient are in
GP
$\Rightarrow P=0$
Now for $\left(3^{1 / 4}+4^{1 / 3}\right)^{12}, T_{r+1}={ }^{12} C_r(4)^{K / 3}(3)^{\frac{12-K}{4}}$
for rational terms $\mathrm{K}=0,12$
sum of rational terms
$\begin{aligned}
& ={ }^{12} \mathrm{C}_0 4^0 \cdot 3^3+{ }^{12} \mathrm{C}_{12} \cdot 4^4 \cdot 3^0 \\
& =27+256=283=q \\
& \therefore p+q=283
\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (24 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Suppose A and B are the coefficients of $30^{\text {th }}$ and $12^{\text {th }}$ terms respectively in the binomial expansion of $(1+x)^{2 \mathrm{n}-1}$. If $2 \mathrm{~A}=5 \mathrm{~B}$, then n is equal to :

**Options:**

- **(A)** 22
- **(B)** 20
- **(C)** 21
- **(D)** 19

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 21**

**Detailed Solution:**

$\begin{aligned} & \mathrm{A}={ }^{2 \mathrm{n}-1} \mathrm{C}_{29} \quad \mathrm{~B}={ }^{2 \mathrm{n}-1} \mathrm{C}_{11} \\ & 2^{2 \mathrm{n}-1} \mathrm{C}_{29}=5{ }^{2 \mathrm{n}-1} \mathrm{C}_{11} \\ & 2 \frac{(2 \mathrm{n}-1)!}{29!(2 \mathrm{n}-30)!}=5 \frac{(2 \mathrm{n}-1)!}{(2 \mathrm{n}-12)!11!} \\ & \frac{1}{29 \ldots 12 \cdot 5}=\frac{1}{(2 \mathrm{n}-12)(2 \mathrm{n}-13) \ldots(2 \mathrm{n}-29) 2} \\ & \frac{1}{30 \cdot 29 \ldots 12}=\frac{1}{(2 \mathrm{n}-12)(2 \mathrm{n}-13) \ldots(2 \mathrm{n}-29) 12} \\ & 2 \mathrm{n}-12=30 \\ & \mathrm{n}=21\end{aligned}$

</details>

---

### Q17. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

For some $n \neq 10$, let the coefficients of the 5 th, 6 th and 7 th terms in the binomial expansion of $(1+\mathrm{x})^{\mathrm{n}+4}$ be in A.P. Then the largest coefficient in the expansion of $(1+\mathrm{x})^{\mathrm{n}+4}$ is:

**Options:**

- **(A)** $20$
- **(B)** $10$
- **(C)** $35$
- **(D)** $70$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $35$**

**Detailed Solution:**

$\begin{aligned} & (1+x)^{n+4} \\ & { }^{n+4} C_4,{ }^{n+4} C_5,{ }^{n+4} C_6, \rightarrow \text { A.P. } \\ & \Rightarrow 2 \times { }^{n+4} C_5={ }^{n+4} C_4+{ }^{n+4} C_6 \\ & \Rightarrow 4 \times{ }^{n+4} C_5=\left({ }^{n+4} C_4+{ }^{n+4} C_5\right)+\left({ }^{n+4} C_5+{ }^{n+4} C_6\right) \\ & \Rightarrow 4 \times{ }^{n+4} C_5={ }^{n+5} C_5+{ }^{n+5} C_6\end{aligned}$
$\begin{aligned} & \Rightarrow 4 \times \frac{(\mathrm{n}+4)!}{5!\cdot(\mathrm{n}-1)!}=\frac{(\mathrm{n}+6)!}{6!\cdot \mathrm{n}!} \\ & \Rightarrow 4=\frac{(\mathrm{n}+6)(\mathrm{n}+5)}{6 \mathrm{n}} \\ & \Rightarrow \mathrm{n}^2+11 \mathrm{n}+30=24 \mathrm{n} \\ & \Rightarrow \mathrm{n}^2-13 \mathrm{n}+30=0 \\ & \Rightarrow \mathrm{n}=3,10(\text { rejected }) \\ & \because \mathrm{n} \neq 10\end{aligned}$
$\therefore$ Largest binomial coefficient in expansion of
$\begin{aligned}
& (1+\mathrm{x})^7 \\
& (\because \mathrm{n}+4=7)
\end{aligned}$
is coeff. of middle term
$\Rightarrow{ }^7 \mathrm{C}_4={ }^7 \mathrm{C}_3=35$

</details>

---

### Q18. JEE Main 2025 (23 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If in the expansion of $(1+x)^{\mathrm{p}}(1-x)^{\mathrm{q}}$, the coefficients of $x$ and $x^2$ are 1 and -2 , respectively, then $\mathrm{p}^2+\mathrm{q}^2$ is equal to :

**Options:**

- **(A)** 18
- **(B)** 13
- **(C)** 8
- **(D)** 20

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 13**

**Detailed Solution:**

$\begin{aligned} & (1+\mathrm{x})^{\mathrm{p}}(1-\mathrm{x})^{\mathrm{q}}=\left({ }^{\mathrm{p}} \mathrm{C}_0+{ }^{\mathrm{p}} \mathrm{C}_1 \mathrm{x}+{ }^{\mathrm{p}} \mathrm{C}_2 \mathrm{x}^2+\ldots\right)\left({ }^{\mathrm{q}} \mathrm{C}_0-{ }^{\mathrm{q}} \mathrm{C}_1 \mathrm{x}+{ }^{\mathrm{q}} \mathrm{C}_2 \mathrm{x}^2+\ldots\right) \\ & \text { coff of } \mathrm{x} \equiv{ }^{\mathrm{p}} \mathrm{C}_0{ }^{\mathrm{q}} \mathrm{C}_1+{ }^{\mathrm{p}} \mathrm{C}_1{ }^{\mathrm{q}} \mathrm{C}_0=1 \\ & \mathrm{p}-\mathrm{q}=1 \\ & \text { coff of } \mathrm{x}^2 \equiv{ }^{\mathrm{p}} \mathrm{C}_0{ }^{\mathrm{q}} \mathrm{C}_2-{ }^{\mathrm{p}} \mathrm{C}_1{ }^{\mathrm{q}} \mathrm{C}_1+{ }^{\mathrm{p}} \mathrm{C}_2{ }^{\mathrm{q}} \mathrm{C}_0=-2 \\ & \frac{\mathrm{q}(\mathrm{q}-1)}{2}-\mathrm{pq}+\frac{\mathrm{p}(\mathrm{p}-1)}{2}=-2 \\ & \mathrm{q}^2-\mathrm{q}-2 \mathrm{pq}+\mathrm{p}^2-\mathrm{p}=-4 \\ & 1-(\mathrm{p}+\mathrm{q})=-4 \\ & \mathrm{p}+\mathrm{q}=5 \\ & \mathrm{p}=3 \\ & \mathrm{q}=2 \\ & \text { so } \mathrm{p}^2+\mathrm{q}^2=13\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (23 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

The sum of all rational terms in the expansion of $\left(1+2^{1 / 3}+3^{1 / 2}\right)^6$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **612**

**Detailed Solution:**

The general term of multinomial expansion is
$\frac{6!}{\alpha!\beta!\gamma!}(1)^\alpha\left(2^{\frac{1}{3}}\right)^\beta\left(3^{\frac{1}{2}}\right)^\gamma$

For terms to be rational $3 \mid \beta$ and $2 \mid \gamma$
$\begin{array}{c|c|c|c}
\beta & \gamma & \alpha & \text { Term } \\
\hline 0 & 0 & 6 & 1 \\
0 & 2 & 4 & 15.3=45 \\
0 & 4 & 2 & 15.3^2=135 \\
0 & 6 & 0 & 1.3^3=27 \\
3 & 0 & 3 & 20.2=40 \\
3 & 2 & 1 & 60.2 .3=360 \\
6 & 0 & 0 & 1.4=4
\end{array}$
$\Rightarrow$ Sum of rational terms
$=1+45+135+27+40+360+4=612$

</details>

---

### Q20. JEE Main 2025 (22 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $\alpha, \beta, \gamma$ and $\delta$ be the coefficients of $x^7, x^5, x^3$ and $x$ respectively in the expansion of $\left(x+\sqrt{x^3-1}\right)^5+\left(x-\sqrt{x^3-1}\right)^5, x\gt1$. If u and v satisfy the equations
$\begin{aligned}
& \alpha u+\beta v=18 \\
& \gamma u+\delta v=20
\end{aligned}$
then $u+v$ equals :

**Options:**

- **(A)** 5
- **(B)** 3
- **(C)** 4
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 5**

**Detailed Solution:**

$\begin{aligned}
& \left(x+\sqrt{x^3-1}\right)^5+\left(x-\sqrt{x^3-1}\right)^5 \\
& -\left[{ }^5 C_0 x^5+{ }^5 C_1 x^4\left(\sqrt{x^3-1}\right)+\ldots \ldots+{ }^5 C_5\left(\sqrt{x^3-1}\right)^5\right]+ \\
& {\left[{ }^5 C_0 x^5-{ }^5 C_1 x^4\left(\sqrt{x^3-1}\right)+\ldots \ldots .+{ }^{-5} C_5\left(\sqrt{x^3-1}\right)^5\right]} \\
& =2\left[x^5+{ }^5 C_2 x^3\left(x^3-1\right)+{ }^5 C_4\left(x^3-1\right)^2\right] \\
& =10 x^7+20 x^6+2 x^5-20 x^4-20 x^3+10 x
\end{aligned}$

Now
$\alpha=10, \beta=2, \gamma=-20, \delta=10$

Also,
$\begin{aligned}
& \left.\begin{array}{c}
10 u+2 v=18 \\
-20 u+10 v=20
\end{array}\right\} u=1, v=4 \\
& u+v=5
\end{aligned}$

</details>

---

### Q21. JEE Main 2024 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the coefficient of $x^{2 / 3}$ and $x^{-2 / 5}$ in the binomial expansion of $\left(x^{2 / 3}+\frac{1}{2} x^{-2 / 5}\right)^9$ is

**Options:**

- **(A)** $21 / 4$
- **(B)** $63 / 16$
- **(C)** $19 / 4$
- **(D)** $69 / 16$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $21 / 4$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{T}_{\mathrm{r}+1}={ }^9 \mathrm{C}_{\mathrm{r}}\left(\mathrm{x}^{2 / 3}\right)^{9-\mathrm{r}}\left(\frac{\mathrm{x}^{-2 / 5}}{2}\right)^{\mathrm{r}} \\ & ={ }^9 \mathrm{C}_{\mathrm{r}}\left(\frac{1}{2}\right)^{\mathrm{r}}(\mathrm{r})^{\left(6 \frac{2 \mathrm{r}}{3} \frac{2 \mathrm{r}}{5}\right)}\end{aligned}$
for coefficient of $x^{2 / 3}$, put $6-\frac{2 r}{3}-\frac{2 r}{5}=\frac{2}{3}$
$\Rightarrow \mathrm{r}=5$
$\therefore$ Coefficient of $\mathrm{x}^{2 / 3}$ is $={ }^9 \mathrm{C}_5\left(\frac{1}{5}\right)^5$
For coefficient of $x^{-2 / 5}$, put $6-\frac{2 r}{3}-\frac{2 r}{5}=-\frac{2}{5}$
$\Rightarrow \mathrm{r}=6$
Coefficient of $\mathrm{x}^{-2 / 5}$ is ${ }^9 \mathrm{C}_6\left(\frac{1}{2}\right)^6$
$\text {Sum }={ }^9 \mathrm{C}_5\left(\frac{1}{2}\right)^5+{ }^9 \mathrm{C}_6\left(\frac{1}{2}\right)^6=\frac{21}{4}$

</details>

---

### Q22. JEE Main 2024 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^{70}$ in $x^2(1+x)^{98}+x^3(1+x)^{97}+x^4(1+x)^{96}+\ldots+x^{54}(1+x)^{46}$ is ${ }^{99} \mathrm{C}_{\mathrm{p}}-{ }^{46} \mathrm{C}_{\mathrm{q}}$. Then a possible value of $p+q$ is :

**Options:**

- **(A)** 55
- **(B)** 83
- **(C)** 61
- **(D)** 68

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 83**

**Detailed Solution:**

$\begin{aligned}
& x^2(1+x)^{98}+x^3\left(1+x^{97}\right)+x^4(1+x)^{96}+\ldots \ldots \\
& x^{54}(1+x)^{46}
\end{aligned}$
Coeff. of $\mathrm{x}^{70}:{ }^{98} \mathrm{C}_{68}+{ }^{97} \mathrm{C}_{67}+{ }^{96} \mathrm{C}_{66}+\ldots \ldots \ldots$
$\begin{aligned}
& { }^{47} \mathrm{C}_{17}+{ }^{46} \mathrm{C}_{16} \\
& ={ }^{46} \mathrm{C}_{30}+{ }^{47} \mathrm{C}_{30}+\ldots \ldots \ldots . .{ }^{98} \mathrm{C}_{30} \\
& =\left({ }^{46} \mathrm{C}_{31}+{ }^{46} \mathrm{C}_{30}\right)+{ }^{47} \mathrm{C}_{30}+\ldots \ldots \ldots .{ }^{98} \mathrm{C}_{30}-{ }^{46} \mathrm{C}_{31} \\
& ={ }^{47} \mathrm{C}_{31}+{ }^{47} \mathrm{C}_{30}+\ldots \ldots \ldots . .{ }^{98} \mathrm{C}_{30}-{ }^{46} \mathrm{C}_{31} \\
& \ldots \ldots \\
& ={ }^{99} \mathrm{C}_{31}-{ }^{46} \mathrm{C}_{31}={ }^{99} \mathrm{C}_{\mathrm{p}}-{ }^{46} \mathrm{C}_{\mathrm{q}}
\end{aligned}$
Possible values of $(p+q)$ are $62,83,99,46$
$\Rightarrow p+q=83$

</details>

---

### Q23. JEE Main 2024 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the term independent of $x$ in the expansion of $\left(\sqrt{\mathrm{a}} x^2+\frac{1}{2 x^3}\right)^{10}$ is 105 , then $\mathrm{a}^2$ is equal to :

**Options:**

- **(A)** 2
- **(B)** 4
- **(C)** 6
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 4**

**Detailed Solution:**

$\left(\sqrt{\mathrm{a}} \mathrm{x}^2+\frac{1}{2 \mathrm{x}^3}\right)^{10}$
General term $={ }^{10} \mathrm{C}_{\mathrm{r}}\left(\sqrt{\mathrm{a}} \mathrm{x}^2\right)^{10-\mathrm{r}}\left(\frac{1}{2 \mathrm{x}^3}\right)^{\mathrm{r}}$
$\begin{aligned} & 20-2 r-3 r=0 \\ & \mathrm{r}=4 \\ & { }^{10} \mathrm{C}_4 \mathrm{a}^3 \cdot \frac{1}{16}=105 \\ & \mathrm{a}^3=8 \\ & \mathrm{a}^2=4\end{aligned}$
SECTION - B

</details>

---

### Q24. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If the second, third and fourth terms in the expansion of $(x+y)^n$ are 135,30 and $\frac{10}{3}$, respectively, then $6\left(n^3+x^2+y\right)$ is equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **806**

**Detailed Solution:**

${ }^{\mathrm{n}} \mathrm{C}_1 \mathrm{x}^{\mathrm{n}-1} \mathrm{y}=135$....(i)
${ }^n C_2 x^{n-2} y^2=30$....(ii)
${ }^{\mathrm{n}} \mathrm{C}_3 \mathrm{x}^{\mathrm{n}-3} \mathrm{y}^3=\frac{10}{3}$....(iii)
$\begin{aligned} & \text { By } \frac{(i)}{(\text { ii) }} \\ & \frac{{ }^n C_1}{{ }^n C_2} \frac{x}{y}=\frac{9}{2}...(iv) \\ & \text { By } \frac{(\text { ii) }}{(\text { iii) }} \\ & \frac{{ }^n C_2}{{ }^n C_3} \frac{x}{y}=9....(v)\end{aligned}$
$\begin{aligned} & \text { By } \frac{(\text { iv })}{(v)} \\ & \frac{{ }^n C_1{ }^n C_3}{{ }^n C_2{ }^n C_2}=\frac{1}{2} \\ & \frac{2 n^2(n-1)(n-2)}{6}=\frac{n(n-1)}{2} \frac{n(n-1)}{2} \\ & 4 n-8=3 n-3 \\ & \Rightarrow n=5 \\ & \text { put in (v) }\end{aligned}$
$\begin{aligned} & \frac{x}{y}=9 \\ & x=9 y \\ & \text { put in (i) } \\ & { }^5 C_1 x^4\left(\frac{x}{9}\right)=135 \\ & x^5=27 \times 9 \\ & \Rightarrow x=3, \quad y=\frac{1}{3} \\ & 6\left(n^3+x^2+y\right) \\ & =6\left(125+9+\frac{1}{3}\right) \\ & =806\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (05 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the constant term in the expansion of $\left(\frac{\sqrt[5]{3}}{x}+\frac{2 x}{\sqrt[3]{5}}\right)^{12}, x \neq 0$, is $\alpha \times 2^8 \times \sqrt[5]{3}$, then $25 \alpha$ is equal to :

**Options:**

- **(A)** 724
- **(B)** 742
- **(C)** 639
- **(D)** 693

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 693**

**Detailed Solution:**

$\begin{aligned} & \mathrm{T}_{\mathrm{r}+1}={ }^{12} \mathrm{C}_{\mathrm{r}}\left(\frac{3^{1 / 5}}{\mathrm{x}}\right)^{12-\mathrm{r}}\left(\frac{2 \mathrm{x}}{5^{1 / 3}}\right)^{\mathrm{r}} \\ & \mathrm{T}_{\mathrm{r}+1}=\frac{{ }^{12} \mathrm{C}_{\mathrm{r}}(3)^{\frac{12-\mathrm{r}}{5}}(2)^{\mathrm{r}}(\mathrm{x})^{2 \mathrm{r}-12}}{(5)^{\mathrm{r} / 3}} \\ & \mathrm{r}=6 \\ & \mathrm{~T}_7=\frac{{ }^{12} \mathrm{C}_6(3)^{6 / 5}(2)^6}{5^2}=\left(\frac{9 \times 11 \times 7}{25}\right) 2^8 \cdot 3^{1 / 5} \\ & 25 \alpha=693\end{aligned}$

</details>

---

### Q26. JEE Main 2024 (05 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

If the constant term in the expansion of $\left(1+2 x-3 x^3\right)\left(\frac{3}{2} x^2-\frac{1}{3 x}\right)^9$ is $\mathrm{p}$, then $108 \mathrm{p}$ is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **54**

**Detailed Solution:**

$\begin{aligned}
& \left(1+2 x-3 x^3\right)\left(\frac{3}{2} x^2-\frac{1}{3 x}\right)^9 \\
& \text { General term } m\left(\frac{3}{2} x^2-\frac{1}{3 x}\right)^9 \\
& ={ }^9 C_r \cdot \frac{3^{9-2 r}}{2^{9-r}}(-1)^r \cdot x^{18-3 r}
\end{aligned}$
Put $r=6$ to get coeff. of $x^0={ }^9 C_6 \cdot \frac{1}{6^3} \cdot x^0=\frac{7}{18} x^0$
Put $\mathrm{r}=7$ to get coeff. of $\mathrm{x}^{-3}={ }^9 \mathrm{C}_{\mathrm{r}} \cdot \frac{3^{-5}}{2^2}(-1)^7 \cdot \mathrm{x}^{-3}$
$\begin{aligned}
& =-{ }^9 C_7 \cdot \frac{1}{3^5 \cdot 2^2} \cdot x^{-3}=\frac{-1}{27} x^{-3} \\
& \left(1+2 x-3 x^3\right)\left(\frac{7}{18} x^0-\frac{1}{27} x^{-3}\right) \\
& \frac{7}{18}+\frac{3}{27}=\frac{7}{18}+\frac{1}{9}=\frac{7+2}{18}=\frac{9}{18}=\frac{1}{2} \\
& \therefore 108 \cdot \frac{1}{2}=54
\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the coefficients of $x^4, x^5$ and $x^6$ in the expansion of $(1+x)^n$ are in the arithmetic progression, then the maximum value of $n$ is:

**Options:**

- **(A)** 7
- **(B)** 21
- **(C)** 28
- **(D)** 14

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 14**

**Detailed Solution:**

$\begin{aligned} & \text { Coeff. of } x^4={ }^n C_4 \\ & \text { Coeff. of } x^5={ }^n C_5 \\ & \text { Coeff. of } x^6={ }^n C_6 \\ & { }^n C_4,{ }^n C_5,{ }^n C_6 \ldots . A P \\ & 2 C_5={ }^n C_4+{ }^n C_6 \\ & 2=\frac{{ }^n C_4}{{ }^n C_5}+\frac{{ }^n C_6}{{ }^n C_5} \quad\left\{\frac{{ }^n C_r}{{ }^n C_r}=\frac{n-r+1}{r}\right\} \\ & 2=\frac{5}{n-4}+\frac{n-5}{6} \\ & 12(n-4)=30+n^2-9 n+20 \\ & n^2-21 n+98=0 \\ & (n-14)(n-7)=0 \\ & n_{\max }=14 \quad n_{\min }=7\end{aligned}$

</details>

---

### Q28. JEE Main 2024 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo> </mo><mtext>and</mtext><mo> </mo><mi>n</mi></math> be the coefficients of seventh and thirteenth terms respectively in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>18</mn></msup></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mi>n</mi><mi>m</mi></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></math> is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>9</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>9</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>Given expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mrow></mfenced><mn>18</mn></msup></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mn>7</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mn>12</mn></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>m</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>12</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mn>13</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>12</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>2</mn><mn>3</mn></mfrac></mstyle></msup></mrow></mfrac></mfenced><mn>12</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>12</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>12</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>12</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>6</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>12</mn><none></none><mprescripts></mprescripts><none></none><mn>18</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>12</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>=</mo><mfrac><msup><mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>6</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>=</mo><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mi>m</mi><mi>n</mi></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msup><mfenced><mfrac><mi>n</mi><mi>m</mi></mfrac></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>=</mo><mfrac><mn>9</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q29. JEE Main 2024 (01 Feb Shift 1)

*Type:* `numerical` | *Level:* `3`

If the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>30</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>8</mn></msup><mo>;</mo><mi>x</mi><mo>≠</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi>α</mi></mfenced></math> equals _________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **678**

**Detailed Solution:**

<p>Given expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>8</mn></msup></math>.</p><p>Now, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>30</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>8</mn></msup></mrow><msup><mi>x</mi><mn>6</mn></msup></mfrac></math></p><p>So, we will find the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>36</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>7</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>8</mn></msup></math></p><p>General term of the given expansion is<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>6</mn></msup><msup><msub><mi>C</mi><msub><mi>r</mi><mn>1</mn></msub></msub><mn>7</mn></msup><msup><msub><mi>C</mi><msub><mi>r</mi><mn>2</mn></msub></msub><mn>8</mn></msup><msub><mi>C</mi><msub><mi>r</mi><mn>3</mn></msub></msub><msup><mfenced><mrow><mo>−</mo><mn>1</mn></mrow></mfenced><msub><mi>r</mi><mn>3</mn></msub></msup><msup><mi>x</mi><mrow><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mo>+</mo><mn>3</mn><msub><mi>r</mi><mn>3</mn></msub></mrow></msup></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mo>+</mo><mn>3</mn><msub><mi>r</mi><mn>3</mn></msub><mo>=</mo><mn>36</mn></math></p><p>Case-I:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;"> <tbody> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>2</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></td> </tr> </tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>12</mn></math> (Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub><mo>=</mo><mn>8</mn></math>)</p><p>Case II:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;"> <tbody> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>2</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td> </tr> </tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>15</mn></math> (Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub><mo>=</mo><mn>7</mn></math>)</p><p>Case III:</p><table border="1" cellpadding="1" cellspacing="1" style="width: 500px;"> <tbody> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>1</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>2</mn></msub></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> </tr> <tr> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> <td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></td> </tr> </tbody></table><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>r</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msub><mi>r</mi><mn>2</mn></msub><mo>=</mo><mn>18</mn></math> (Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>r</mi><mn>3</mn></msub><mo>=</mo><mn>6</mn></math>)</p><p>So, the required coefficient Is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mn>7</mn><mo>+</mo><mfenced><mrow><mn>15</mn><mo>×</mo><mn>21</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>15</mn><mo>×</mo><mn>35</mn></mrow></mfenced><mo>+</mo><mfenced><mn>35</mn></mfenced><mo>−</mo><mfenced><mrow><mn>6</mn><mo>×</mo><mn>8</mn></mrow></mfenced><mo>−</mo><mfenced><mrow><mn>20</mn><mo>×</mo><mn>7</mn><mo>×</mo><mn>8</mn></mrow></mfenced><mo>−</mo><mfenced><mrow><mn>6</mn><mo>×</mo><mn>21</mn><mo>×</mo><mn>8</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>15</mn><mo>×</mo><mn>28</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>7</mn><mo>×</mo><mn>28</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>α</mi><mo>=</mo><mo>−</mo><mn>678</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mfenced close="|" open="|"><mi>α</mi></mfenced><mo>=</mo><mn>678</mn></math></p>

</details>

---

### Q30. JEE Main 2024 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

In the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>5</mn></msup><mo>,</mo><mo> </mo><mi>x</mi><mo>≠</mo><mn>0</mn></math>, the sum of the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>13</mn></mrow></msup></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **118**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mi>x</mi></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mfenced><mfrac><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>x</mi><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mfenced><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>3</mn></msup><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><msup><mi>x</mi><mn>15</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup><msup><mi>x</mi><mn>15</mn></msup></mfrac><mo>-</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup><msup><mi>x</mi><mn>14</mn></msup></mfrac></math></p><p>Now for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math>, we will find coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>18</mn></msup></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup></math> which is not possible and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>17</mn></msup></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup></math> which will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>17</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>And for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>13</mn></mrow></msup></math> we will coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup></math> which will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts></math> and coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>17</mn></msup></math> which will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts></math>, so the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>13</mn></mrow></msup></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts><mo>=</mo><mn>136</mn><mo>-</mo><mn>17</mn><mo>=</mo><mn>119</mn></math></p><p>Hence, the sum will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>119</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>118</mn></math></p>

</details>

---

### Q31. JEE Main 2024 (30 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

Suppose <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>-</mo><mi>p</mi><mo>,</mo><mo> </mo><mi>p</mi><mo>,</mo><mo> </mo><mn>70</mn><mo>-</mo><mi>α</mi><mo>,</mo><mo> </mo><mi>α</mi></math> are the coefficient of four consecutive terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mi>n</mi></msup></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>α</mi><mo>-</mo><mn>3</mn><mi>p</mi></math> equals

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><mo>-</mo><mi>p</mi><mo>,</mo><mo> </mo><mi>p</mi><mo>,</mo><mo> </mo><mn>70</mn><mo>-</mo><mi>α</mi><mo>,</mo><mo> </mo><mi>α</mi></math> are the coefficient of four consecutive terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mi>n</mi></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>28</mn><mo>-</mo><mi>p</mi><mo>,</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mi>p</mi><mo>,</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>70</mn><mo>-</mo><mi>α</mi><mo> </mo><mo>&amp;</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mi>α</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>28</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>70</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mn>28</mn><mo> </mo><mo>&amp;</mo><mo> </mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mn>70</mn></math></p><p>We know that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>=</mo><mn>28</mn><mo> </mo><mtext>or</mtext><mo> </mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>28</mn></mmultiscripts><mo>=</mo><mn>28</mn></math>, </p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mn>28</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>,</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced><mo> </mo><mtext>or</mtext><mo> </mo><mfenced><mrow><mi>n</mi><mo>,</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>27</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math></p><p>Now, checking with <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mmultiscripts><mo>=</mo><mn>70</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>,</mo><mi>r</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>7</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>=</mo><mn>21</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>=</mo><mn>35</mn></math></p><p> Hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>α</mi><mo>-</mo><mn>3</mn><mi>p</mi><mo>=</mo><mn>70</mn><mo>-</mo><mn>63</mn><mo>=</mo><mn>7</mn></math></p></blockquote>

</details>

---

### Q32. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Number of integral terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="}" open="{"><mrow><msup><mn>7</mn><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced></msup><mo>+</mo><msup><mn>11</mn><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced></msup></mrow></mfenced><mn>824</mn></msup></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **138**

**Detailed Solution:**

<p>We know that,</p><p>General term in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>(</mo><mn>7</mn><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mo>(</mo><mn>11</mn><msup><mo>)</mo><mrow><mn>1</mn><mo>/</mo><mn>6</mn></mrow></msup></mrow></mfenced><mn>824</mn></msup></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>824</mn></mmultiscripts><mo>·</mo><msup><mn>7</mn><mfrac><mrow><mn>824</mn><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><mo>·</mo><msup><mn>11</mn><mfrac><mi>r</mi><mn>6</mn></mfrac></msup></math></p><p>For integral term, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> must be multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> and should be less than <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>824</mn></math></p><p>So, the series will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>12</mn><mo>,</mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo> </mo><mn>822</mn></math></p><p>Now, finding number of terms we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>822</mn><mo>=</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>137</mn><mo>=</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>138</mn></math></p><p>Hence, total integral terms will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>138</mn></math></p>

</details>

---

### Q33. JEE Main 2024 (27 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2012</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2008</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mn>2007</mn></msup></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **0**

**Detailed Solution:**

<p>Let, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">y</mi><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2008</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mn>2007</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mn>2007</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced><mn>2007</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><msup><mfenced close="]" open="["><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi mathvariant="normal">x</mi><mo>+</mo><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced><mn>2007</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mrow></mfenced><mn>2007</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi mathvariant="normal">y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mn>2007</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2007</mn></mmultiscripts><mfenced><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></mrow></mfenced></math></p><p>General term in the expansion is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi mathvariant="normal">x</mi></mrow></mfenced><mfenced><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none></none><mprescripts></mprescripts><none></none><mn>2007</mn></mmultiscripts><mo> </mo><msup><mi mathvariant="normal">x</mi><mrow><mn>3</mn><mi mathvariant="normal">r</mi></mrow></msup><mo> </mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi mathvariant="normal">r</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mn>2007</mn></msup><msub><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi></msub><mo> </mo><msup><mi mathvariant="normal">x</mi><mrow><mn>3</mn><mi mathvariant="normal">r</mi></mrow></msup><mo> </mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi mathvariant="normal">r</mi></msup><mo>-</mo><msup><mo> </mo><mn>2007</mn></msup><msub><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi></msub><mo> </mo><msup><mi mathvariant="normal">x</mi><mrow><mn>3</mn><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msup><mo> </mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi mathvariant="normal">r</mi></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>12</mn></msup></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">r</mi><mo>=</mo><mn>2012</mn></math></p><p>But, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>≠</mo><mfrac><mn>2012</mn><mn>3</mn></mfrac></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>2012</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>3</mn><mi mathvariant="normal">r</mi><mo>=</mo><mn>2011</mn></math></p><p>But, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">r</mi><mo>≠</mo><mfrac><mn>2011</mn><mn>3</mn></mfrac></math></p><p>Hence, there is no term containing <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2012</mn></msup></math>.</p><p>So coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>2012</mn></msup><mo>=</mo><mn>0</mn></math></p>

</details>

---

### Q34. JEE Main 2023 (13 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>5</mn></msup></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>9</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>26</mn><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>80</mn><mn>9</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p>General term of the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>5</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mn>5</mn><msub><mi>C</mi><mi>r</mi></msub></msub><mo>(</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><msup><mo>)</mo><mrow><mn>5</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#160;</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mrow><mn>5</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>15</mn><mo>-</mo><mn>5</mn><mi>r</mi></mrow></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>5</mn></msup></math>, we must have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn><mo>-</mo><mn>5</mn><mi>r</mi><mo>=</mo><mn>5</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>So, required coefficient is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>5</mn></mmultiscripts><mo>(</mo><mn>2</mn><msup><mo>)</mo><mn>3</mn></msup><mfenced><mfrac><mn>1</mn><mn>9</mn></mfrac></mfenced><mspace linebreak="newline"/><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>9</mn></mfrac><mspace linebreak="newline"/><mo>=</mo><mfrac><mn>80</mn><mn>9</mn></mfrac></math></p></blockquote>

</details>

---

### Q35. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> be the constant term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mfrac><mn>6</mn><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>,</mo><mi>n</mi><mo>&#8804;</mo><mn>15</mn><mo>.</mo></math> If the sum of the coefficients of the remaining terms in the expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>649</mn></math> and the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mi>n</mi></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mi>&#945;</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **36**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mfrac><mn>6</mn><msup><mi>x</mi><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>,</mo><mi>n</mi><mo>&#8804;</mo><mn>15</mn></math></p><p>Now  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><msup><mi>x</mi><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mn>6</mn><msup><mi>x</mi><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><mn>2</mn></mfrac></msup></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><mo>&#183;</mo><msup><mi>x</mi><mfrac><mrow><mo>-</mo><mn>3</mn><mi>r</mi></mrow><mn>2</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mfrac><mrow><mi>n</mi><mo>-</mo><mn>4</mn><mi>r</mi></mrow><mn>2</mn></mfrac></msup></math></p><p>Now we have to take, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>4</mn><mi>r</mi></math> for constant term so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mmultiscripts><mi>C</mi><mfrac><mi>n</mi><mn>4</mn></mfrac><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfrac><mi>n</mi><mn>4</mn></mfrac></msup></math></p><p>And sum of all coefficients will be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mn>1</mn></msqrt><mo>-</mo><mfrac><mn>6</mn><msup><mn>1</mn><mfrac><mn>3</mn><mn>2</mn></mfrac></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup></math></p><p>Also given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>-</mo><mn>5</mn></mrow></mfenced><mi>n</mi></msup><mo>-</mo><mmultiscripts><mi>C</mi><mfrac><mi>n</mi><mn>4</mn></mfrac><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfrac><mi>n</mi><mn>4</mn></mfrac></msup><mo>=</mo><mn>649</mn></math></p><p>Now by hit and trial we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>4</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mfrac><mn>4</mn><mn>4</mn></mfrac></msup><mo>=</mo><mo>-</mo><mn>24</mn></math></p><p>Now for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>-</mo><mn>4</mn><mi>r</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>8</mn><mo>&#8658;</mo><menclose notation="box"><mi>r</mi><mo>=</mo><mn>3</mn></menclose></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#955;</mi><mfenced><mi>&#945;</mi></mfenced><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mn>3</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mfenced><mrow><mo>-</mo><mn>24</mn></mrow></mfenced><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>6</mn></mrow></mfenced><mn>3</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>36</mn></math></p></blockquote>

</details>

---

### Q36. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the coefficients of three consecutive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></math>, which are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>3</mn><mo>:</mo><mn>5</mn></math>, is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>92</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>41</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>63</mn></math>**

**Detailed Solution:**

<p>Ratio of three consecutive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></math> is</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mo>:</mo><mo>:</mo><mn>1</mn><mo>:</mo><mn>3</mn><mo>:</mo><mn>5</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>3</mn></mrow><mi>r</mi></mfrac><mo>=</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>4</mn><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>2</mn><mo>-</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>5</mn><mi>r</mi><mo>+</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>8</mn><mi>r</mi><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mfenced><mrow><mn>4</mn><mi>r</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mn>1</mn><mo>=</mo><mn>8</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>12</mn><mi>r</mi><mo>-</mo><mn>9</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>8</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>r</mi><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>5</mn></math></p><p>Hence, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>7</mn></msup></math></p><p>Sum of consecutive terms is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>7</mn><mo>+</mo><mn>21</mn><mo>+</mo><mn>35</mn><mo>=</mo><mn>63</mn></math></p>

</details>

---

### Q37. JEE Main 2023 (11 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1011</mn><mi>th</mi></msup></math> term from the end in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>5</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>2022</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1024</mn></math> times <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1011</mn><mi>th</mi></msup></math> term from the beginning, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mfenced close="|" open="|"><mi>x</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math>**

**Detailed Solution:**

<p>Given,</p><p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1011</mn><mi>th</mi></msup></math> term from the end in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>5</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>2022</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1024</mn></math> times <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1011</mn><mi>th</mi></msup></math> term from the beginning,</p><p>So, according to question we have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mn>1013</mn></msub><msub><mi>T</mi><mn>1011</mn></msub></mfrac><mo>=</mo><mn>1024</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>1012</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mfenced><mn>1010</mn></msup><mo>&#183;</mo><msup><mfenced><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mn>1012</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>1010</mn><none></none><mprescripts></mprescripts><none></none><mn>2022</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mfenced><mn>1012</mn></msup><msup><mfenced><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mn>1010</mn></msup></mrow></mfrac><mo>=</mo><mn>1024</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mo>-</mo><mn>5</mn></mrow><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mstyle></mfenced><mn>2</mn></msup><msup><mfenced><mstyle displaystyle="true"><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mstyle></mfenced><mn>2</mn></msup></mfrac><mo>=</mo><mn>1024</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mn>5</mn><mn>4</mn></msup><mrow><msup><mn>2</mn><mn>6</mn></msup><msup><mi>x</mi><mn>4</mn></msup></mrow></mfrac><mo>=</mo><msup><mn>2</mn><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mfrac><mn>5</mn><mi>x</mi></mfrac></mfenced><mn>4</mn></msup><mo>=</mo><msup><mn>2</mn><mn>16</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mfrac><mn>5</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>32</mn><mfenced close="|" open="|"><mi>x</mi></mfenced><mo>=</mo><mn>10</mn></math></p><p>Note this question was bonus in Jee Main 2023 April session as answer key was not matching, so we have modified the question.</p>

</details>

---

### Q38. JEE Main 2023 (11 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of integral terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mrow></mfenced><mn>680</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **171**

**Detailed Solution:**

<blockquote><p>Given expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mrow></mfenced><mn>680</mn></msup></math>.</p><p>The general term in the expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mi>a</mi><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>680</mn></mmultiscripts><msup><mfenced><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mrow><mn>680</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><msup><mn>5</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfenced><mi>r</mi></msup><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>r</mi><mo>&#8804;</mo><mn>680</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>680</mn></mmultiscripts><msup><mfenced><mn>3</mn></mfenced><mfrac><mrow><mn>680</mn><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><msup><mfenced><mn>5</mn></mfenced><mfrac><mi>r</mi><mn>4</mn></mfrac></msup></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mn>3</mn></mfenced><mfrac><mrow><mn>680</mn><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><msup><mfenced><mn>5</mn></mfenced><mfrac><mi>r</mi><mn>4</mn></mfrac></msup></math> to be rational <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> should be a multiple of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>12</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>680</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>680</mn><mo>=</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>171</mn></math></p><p>That means <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> can take <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>171</mn></math> values.</p><p>Hence, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>171</mn></math>.</p></blockquote>

</details>

---

### Q39. JEE Main 2023 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math> and the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math> are equal, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>4</mn></msup></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>44</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in the expansion of  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math> is equal to the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math>.</p><p>We know that, the general term <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></math> in the expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math>  is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>b</mi><mi>r</mi></msup></math></p><p>Applying to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mrow><mi>a</mi><mi>x</mi></mrow></mfenced><mrow><mn>13</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mi>a</mi></mfenced><mrow><mn>13</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mi>x</mi></mfenced><mrow><mn>13</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><msup><mfenced><mi>b</mi></mfenced><mrow><mo>-</mo><mi>r</mi></mrow></msup></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math> for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>7</mn></msup></math>.</p><p>Thus,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><mfenced><mfrac><msup><mi>a</mi><mn>11</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac></mfenced></math></p><p>Similarly, applying to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>13</mn></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mrow><mi>a</mi><mi>x</mi></mrow></mfenced><mrow><mn>13</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mi>a</mi></mfenced><mrow><mn>13</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mi>x</mi></mfenced><mrow><mn>13</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><msup><mfenced><mi>b</mi></mfenced><mrow><mo>-</mo><mi>r</mi></mrow></msup></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mo>-</mo><mn>5</mn></math> for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mrow><mo>-</mo><mn>5</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>7</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mi>a</mi></mfenced><mn>7</mn></msup><msup><mfenced><mi>b</mi></mfenced><mrow><mo>-</mo><mn>6</mn></mrow></msup></math></p><p>Hence, applying the given condition we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><mfenced><mfrac><msup><mi>a</mi><mn>11</mn></msup><msup><mi>b</mi><mn>2</mn></msup></mfrac></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><msup><mfenced><mi>a</mi></mfenced><mn>7</mn></msup><msup><mfenced><mi>b</mi></mfenced><mrow><mo>-</mo><mn>6</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>4</mn></msup><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>13</mn></mmultiscripts></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>4</mn></msup><mo>=</mo><mfrac><mrow><mn>13</mn><mo>!</mo></mrow><mrow><mn>7</mn><mo>!</mo><mo>&#183;</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>11</mn><mo>!</mo></mrow><mrow><mn>13</mn><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>4</mn></msup><mo>=</mo><mfrac><mrow><mn>11</mn><mo>&#215;</mo><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>4</mn></msup><msup><mi>b</mi><mn>4</mn></msup><mo>=</mo><mn>22</mn></math></p></blockquote>

</details>

---

### Q40. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The absolute difference of the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>13</mn><mn>3</mn></msup><mo>-</mo><mn>13</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mn>3</mn></msup><mo>-</mo><mn>11</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>3</mn></msup><mo>-</mo><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>12</mn><mn>3</mn></msup><mo>-</mo><mn>12</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>12</mn><mn>3</mn></msup><mo>-</mo><mn>12</mn></math>**

**Detailed Solution:**

<blockquote><p>The given expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math>.</p><p>The general term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mi>n</mi></msup></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn mathvariant="italic">1</mn></mrow></msub><mo mathvariant="italic">=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mi>n</mi><mo mathvariant="italic">-</mo><mi>r</mi></mrow></msup><msup><mi>a</mi><mi>r</mi></msup></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>x</mi></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mfenced><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mi>r</mi><mo>-</mo><mi>r</mi></mrow></msup></mfenced><msup><mi>x</mi><mrow><mn>22</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mi>r</mi></mrow></msup></math></p><p>Now for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mfenced><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn></mrow></msup></mfenced></math></p><p>Now for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup><mo>&#8658;</mo><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mfenced><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>4</mn></mrow></msup></mfenced></math></p><p>We need the absolute difference, we get it by <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mrow><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mfenced><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn></mrow></msup></mfenced><mo>-</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mfenced><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mn>4</mn><mo>&#215;</mo><mn>2</mn></mrow></msup></mfenced></mrow></mfenced></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced open="|" close="|"><mrow><mn>924</mn><mo>-</mo><mn>2640</mn></mrow></mfenced><mo>=</mo><mn>1716</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>12</mn><mn>3</mn></msup><mo>-</mo><mn>12</mn></math></p><p>Hence the absolute difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>12</mn><mn>3</mn></msup><mo>-</mo><mn>12</mn></math>.</p></blockquote>

</details>

---

### Q41. JEE Main 2023 (08 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>t</mi></mfenced></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>t</mi></math>. if the constant term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow></mfrac></mrow></mfenced><mn>7</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#945;</mi></mfenced></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1275**

**Detailed Solution:**

<blockquote><p>The given expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow></mfrac></mrow></mfenced><mn>7</mn></msup></math>.</p><p>The general term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mi>n</mi></msup></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo mathvariant="italic">=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mi>n</mi><mo mathvariant="italic">-</mo><mi>r</mi></mrow></msup><msup><mi>a</mi><mi>r</mi></msup></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mfenced><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>7</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>2</mn><msup><mi>x</mi><mn>5</mn></msup></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mfenced><mfrac><msup><mn>3</mn><mrow><mn>7</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mn>2</mn><mi>r</mi></msup></mfrac></mfenced><msup><mi>x</mi><mrow><mn>14</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mn>5</mn><mi>r</mi></mrow></msup></math></p><p>Now for term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>14</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mn>5</mn><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>0</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#215;</mo><mfenced><mfrac><msup><mn>3</mn><mrow><mn>7</mn><mo>-</mo><mn>2</mn></mrow></msup><msup><mn>2</mn><mn>2</mn></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>6</mn></mrow><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><msup><mn>3</mn><mn>5</mn></msup><msup><mn>2</mn><mn>2</mn></msup></mfrac></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mo>=</mo><mfrac><mn>5103</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="]" open="["><mi>&#945;</mi></mfenced><mo>=</mo><mn>1275</mn></math></p><p>Hence this is the required answer.</p></blockquote>

</details>

---

### Q42. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

if the coefficients of three consecutive terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math> are the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#160;</mo><mo>:</mo><mo>&#160;</mo><mn>5</mn><mo>&#160;</mo><mo>:</mo><mn>20</mn><mo>&#160;</mo></math>then the coefficient of the fourth term is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2436</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5481</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1827</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3654</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3654</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>:</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mn>1</mn><mo>:</mo><mn>5</mn><mo>:</mo><mn>20</mn></math></p><p>Now using the formula <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac></math> we get,</p><p>.<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>6</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>20</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>5</mn><mi>r</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving above equations we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>29</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>So, the coefficient of forth term will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>29</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>29</mn><mo>&#215;</mo><mn>28</mn><mo>&#215;</mo><mn>27</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>3654</mn></math></p></blockquote>

</details>

---

### Q43. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>b</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> are equal, then</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>32</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>729</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>243</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>243</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>64</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>729</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>32</mn></math>**

**Detailed Solution:**

<blockquote><p>The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>b</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> are equal, then</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>b</mi><mi>x</mi></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mi>a</mi></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>b</mi></mrow></mfrac></mfenced><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mrow><mi>a</mi><mi>x</mi></mrow></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mi>a</mi><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi></mrow></mfrac></mrow></mfenced><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>11</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mo>-</mo><mn>7</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>Now equating coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msup><mo>&#160;</mo><mn>11</mn></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mfenced><mi>a</mi></mfenced><mn>6</mn></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mn>2</mn><mi>b</mi></mrow></mfrac></mfenced><mn>5</mn></msup><msup><mo>=</mo><mn>11</mn></msup><msub><mi>C</mi><mn>6</mn></msub><mo>&#160;</mo><msup><mi>a</mi><mn>5</mn></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>b</mi></mrow></mfrac></mrow></mfenced><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mn>6</mn></msup><mi>a</mi><mi>b</mi><mo>=</mo><mn>32</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>729</mn><mi>a</mi><mi>b</mi><mo>=</mo><mn>32</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q44. JEE Main 2023 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `1`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>18</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>15</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5005**

**Detailed Solution:**

<blockquote><p>Given,</p><p>Binomial expression <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>15</mn></msup></math></p><p>Now general term is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mn>4</mn></msup></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mi>x</mi><mrow><mn>60</mn><mo>-</mo><mn>7</mn><mi>r</mi></mrow></msup><mo>(</mo><mo>-</mo><mn>1</mn><msup><mo>)</mo><mi>r</mi></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>18</mn></msup><mo>,</mo></math> equate <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><mo>-</mo><mn>7</mn><mi>r</mi><mo>=</mo><mn>18</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>18</mn></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>6</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>=</mo><mn>5005</mn></math></p></blockquote>

</details>

---

### Q45. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>If the ratio of the fifth term from the beginning to the fifth term from the end in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mroot><mn>2</mn><mn>4</mn></mroot><mo>+</mo><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt><mo>:</mo><mn>1</mn></math>, then the third term from the beginning is:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><msqrt><mn>3</mn></msqrt></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><msqrt><mn>3</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>60</mn><msqrt><mn>3</mn></msqrt></math>**

**Detailed Solution:**

<blockquote><p>Given expansion is<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mroot><mn>2</mn><mn>4</mn></mroot><mo>+</mo><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mrow></mfenced><mi>n</mi></msup></math></p>We know that general term of an expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mi>a</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>a</mi><mi>r</mi></msup></math><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mi>th</mi></msup></math> term from beginning)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mn>4</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>(</mo><mroot><mn>2</mn><mn>4</mn></mroot><msup><mo>)</mo><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mfenced><mn>4</mn></msup></math></p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mi>th</mi></msup></math> term from end)</p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math>th term from the end in a binomial expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></math> from the beginning.<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>T</mi><mn>5</mn><mo>'</mo></msubsup><mo>=</mo><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mfenced><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msup><mo>(</mo><mroot><mn>2</mn><mn>4</mn></mroot><msup><mo>)</mo><mn>4</mn></msup></math></p><p>It is also given that the ratio of the fifth term from the beginning to the fifth term from the end is <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><mn>6</mn></msqrt><mo>:</mo><mn>1</mn></math>.</p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mn>5</mn></msub><msubsup><mi>T</mi><mn>5</mn><mo>&#39;</mo></msubsup></mfrac><mo>=</mo><mfrac><msqrt><mn>6</mn></msqrt><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mfrac><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow><mn>4</mn></mfrac></msup><mo>&#183;</mo><msup><mn>3</mn><mfrac><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow><mn>4</mn></mfrac></msup><mo>=</mo><msqrt><mn>6</mn></msqrt></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>(</mo><msqrt><mn>6</mn></msqrt><msup><mo>)</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow><mn>2</mn></mfrac></msup><mo>=</mo><mo>(</mo><msqrt><mn>6</mn></msqrt><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>n</mi><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>T</mi><mn>3</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mroot><mn>2</mn><mn>4</mn></mroot></mfenced><mn>8</mn></msup><msup><mfenced><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mn>45</mn><mo>&#215;</mo><mn>4</mn></mrow><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>60</mn><msqrt><mn>3</mn></msqrt></math></p><p>Hence, this is the correct option.</p></blockquote>

</details>

---

### Q46. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

Let the sixth term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><msup><mn>2</mn><mrow><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced></mrow></msup></msqrt><mo>+</mo><mroot><msup><mn>2</mn><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></mrow></msup><mn>5</mn></mroot></mrow></mfenced><mi mathvariant="normal">m</mi></msup></math> powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mrow><mfenced><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></mfenced><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></mrow></msup></math>, be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> . If the binomial coefficients of the second, third and fourth terms in the expansion are respectively the first, third and fifth terms of an A.P., then the sum of the squares of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>Given,</p><p>Binomial expression,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><msup><mn>2</mn><mrow><msub><mi>log</mi><mn>2</mn></msub><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced></mrow></msup></msqrt><mo>+</mo><mroot><msup><mn>2</mn><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo><msub><mi>log</mi><mn>2</mn></msub><mn>3</mn></mrow></msup><mn>5</mn></mroot></mrow></mfenced><mi mathvariant="normal">m</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced></msqrt><mo>+</mo><mroot><msup><mn>3</mn><mrow><mo>(</mo><mi>x</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow></msup><mn>5</mn></mroot></mrow></mfenced><mi mathvariant="normal">m</mi></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><msup><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><mfrac><mrow><mi>m</mi><mo>-</mo><mn>5</mn></mrow><mn>2</mn></mfrac></msup><mo>&#183;</mo><mfenced><msup><mn>3</mn><mrow><mi>x</mi><mo>-</mo><mn>2</mn></mrow></msup></mfenced><mo>=</mo><mn>21</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Also given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mo>,</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mo>,</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts></math> are in A.P.</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>m</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>m</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>m</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mi>m</mi><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mi>m</mi><mo>+</mo><mfrac><mrow><mi>m</mi><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mfenced><mrow><mi>m</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p>Solving for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mo>&#160;</mo><mo>,</mo><mo>&#160;</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn></math> (rejected), so  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>7</mn></math></p><p>Put in equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>&#183;</mo><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><mfrac><msup><mn>3</mn><mi>x</mi></msup><mn>9</mn></mfrac><mo>=</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>10</mn><mo>-</mo><msup><mn>3</mn><mi>x</mi></msup></mrow></mfenced><msup><mn>3</mn><mi>x</mi></msup><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>3</mn><mi>x</mi></msup><mo>=</mo><msup><mn>3</mn><mn>0</mn></msup><mo>,</mo><msup><mn>3</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn></math></p><p>Sum of the squares of all possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>4</mn></math>.</p>

</details>

---

### Q47. JEE Main 2023 (01 Feb Shift 2)

*Type:* `numerical` | *Level:* `1`

If the term without <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>22</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7315</mn><mo>&#160;</mo></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="|" close="|"><mi>&#945;</mi></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>General term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>22</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup></mfenced><mrow><mn>22</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mfenced><mi>x</mi></mfenced><mfrac><mrow><mn>44</mn><mo>-</mo><mn>11</mn><mi>r</mi></mrow><mn>3</mn></mfrac></msup><msup><mi>&#945;</mi><mi>r</mi></msup></math></p><p>For term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>44</mn><mo>-</mo><mn>11</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>5</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>7315</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mn>22</mn><mo>!</mo></mrow><mrow><mn>4</mn><mo>!</mo><mo>&#215;</mo><mn>18</mn><mo>!</mo></mrow></mfrac></mfenced><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>7315</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>7315</mn><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>7315</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>&#945;</mi><mn>4</mn></msup><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>&#945;</mi></mfenced><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q48. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If the constant term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><msup><mi>x</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mi>l</mi></msup></mfrac></mrow></mfenced><mn>9</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>84</mn></math> and the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn><mi>l</mi></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>&#945;</mi></msup><mi>&#946;</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#60;</mo><mn>0</mn></math> is an odd number, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mi>l</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **98**

**Detailed Solution:**

<p>Given,</p><p>The constant term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><msup><mi>x</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>4</mn><msup><mi>x</mi><mi>l</mi></msup></mfrac></mrow></mfenced><mn>9</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>84</mn></math> and the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>&#945;</mi></msup><mi>&#946;</mi></math></p><p>Now General Term of the binomial is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mfenced><mfrac><msup><mi>x</mi><mfrac><mn>5</mn><mn>2</mn></mfrac></msup><mn>2</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mrow><mo>-</mo><mn>4</mn></mrow><msup><mi>x</mi><mi>l</mi></msup></mfrac></mfenced><mi>r</mi></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mi>x</mi><mrow><mfrac><mn>45</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>l</mi><mi>r</mi></mrow></msup><msup><mn>2</mn><mrow><mn>3</mn><mo>-</mo><mn>9</mn></mrow></msup></math></p><p>Now for constant term <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>-</mo><mn>5</mn><mi>r</mi><mo>-</mo><mn>2</mn><mi>l</mi><mi>r</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mn>45</mn><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>l</mi></mrow></mfrac></math></p><p>So, coefficient of constant term will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>9</mn></msup><msup><mo>&#215;</mo><mn>9</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mn>2</mn><mrow><mn>3</mn><mi>r</mi><mo>-</mo><mn>9</mn></mrow></msup><mo>=</mo><mo>-</mo><mn>84</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>3</mn></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mfrac><mn>45</mn><mrow><mn>5</mn><mo>+</mo><mn>2</mn><mi>l</mi></mrow></mfrac></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>5</mn></math></p><p>Now coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn><mi>l</mi></mrow></msup><mo>=</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>15</mn></mrow></msup><mo>&#8658;</mo><mfrac><mn>45</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mi>l</mi><mi>r</mi><mo>=</mo><mo>-</mo><mn>15</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn><mo>&#160;&#160;</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>=</mo><mn>5</mn></math>
Now coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>15</mn></mrow></msup><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mn>59</mn><mo>&#160;</mo></mrow></msup><msub><mi>C</mi><mn>5</mn></msub><msup><mn>2</mn><mn>6</mn></msup><mo>=</mo><mo>-</mo><mn>63</mn><mfenced><msup><mn>2</mn><mn>7</mn></msup></mfenced><mo>=</mo><mi>&#946;</mi><mfenced><msup><mn>2</mn><mi>&#945;</mi></msup></mfenced></math></p><p>Hence, on comparing we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>7</mn><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>63</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>l</mi><mo>=</mo><mn>5</mn></math></p><p>So, the value of  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>&#945;</mi><mo>&#160;</mo><mi>l</mi><mo>-</mo><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced close="|" open="|"><mrow><mn>7</mn><mo>&#215;</mo><mn>5</mn><mo>-</mo><mfenced><mrow><mo>-</mo><mn>63</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>98</mn></math></p>

</details>

---

### Q49. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></math>, in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>9</mn></msup></math>, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5040**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>9</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of the expression is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mn>4</mn><mi>x</mi></mrow><mn>5</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>5</mn><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></mfenced><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>9</mn><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup></math></p><p>Now equating <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn><mi>r</mi><mo>=</mo><mo>-</mo><mn>6</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>So, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mn>5</mn></mrow></msup><msup><mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>&#215;</mo><msup><mfenced><mfrac><mn>4</mn><mn>5</mn></mfrac></mfenced><mn>4</mn></msup><msup><mfenced><mfrac><mn>5</mn><mn>2</mn></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5040</mn></math></p>

</details>

---

### Q50. JEE Main 2023 (31 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn></math>, be the smallest number such that the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>30</mn></msup></math> has a term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><msup><mi>x</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup><mo>,</mo><mi>&#946;</mi><mo>&#8712;</mo><mi>N</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>General term of the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mfrac><mn>2</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mn>30</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced><mrow><mn>30</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>30</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mi>r</mi></msup><mo>&#183;</mo><msup><mi>x</mi><mfrac><mrow><mn>60</mn><mo>-</mo><mn>11</mn><mi>r</mi></mrow><mn>3</mn></mfrac></msup></math></p><p>So, for term of the form <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><msup><mi>x</mi><mrow><mo>-</mo><mi>&#945;</mi></mrow></msup></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>60</mn><mo>-</mo><mn>11</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>&#60;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>11</mn><mi>r</mi><mo>&#62;</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>&#62;</mo><mfrac><mn>60</mn><mn>11</mn></mfrac><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>7</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>30</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>6</mn></msup><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p>We have also observed <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>30</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mn>6</mn></msup></math> is a natural number.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#945;</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q51. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>301</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>499</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>498</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>x</mi><mn>500</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>302</mn><none/><mprescripts/><none/><mn>501</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>301</mn><none/><mprescripts/><none/><mn>500</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>300</mn><none/><mprescripts/><none/><mn>500</mn></mmultiscripts></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>200</mn><none/><mprescripts/><none/><mn>501</mn></mmultiscripts></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>200</mn><none/><mprescripts/><none/><mn>501</mn></mmultiscripts></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>499</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>498</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>x</mi><mn>500</mn></msup></math></p><p>This is a geometric progression.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mo>&#183;</mo><mfenced open="{" close="}"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mfenced><mstyle displaystyle="true"><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mstyle></mfenced><mn>501</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mstyle displaystyle="true"><mfrac><mi>x</mi><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mstyle></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mfrac><mfenced><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>501</mn></msup><mo>-</mo><msup><mi>x</mi><mn>501</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>501</mn></msup></mfrac><mo>&#183;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>501</mn></msup><mo>-</mo><msup><mi>x</mi><mn>501</mn></msup></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>301</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>501</mn></msup><mo>-</mo><msup><mi>x</mi><mn>501</mn></msup></math> is given by</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>301</mn><none></none><mprescripts></mprescripts><none></none><mn>501</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>200</mn><none></none><mprescripts></mprescripts><none></none><mn>501</mn></mmultiscripts></math></p>

</details>

---

### Q52. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>15</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math> is equal to the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>15</mn></mrow></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> are positive real numbers, then for each such ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math>:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mi>b</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>=</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>3</mn><mi>b</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>=</mo><mn>3</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mo>=</mo><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mfenced><mi>a</mi></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mi>x</mi></mfenced><mrow><mn>45</mn><mo>-</mo><mfrac><mrow><mn>10</mn><mi>r</mi></mrow><mn>3</mn></mfrac></mrow></msup><msup><mfenced><mfrac><mn>1</mn><mi>b</mi></mfrac></mfenced><mi>r</mi></msup></math></p><p>For the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>15</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math>:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn><mo>-</mo><mfrac><mrow><mn>10</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>30</mn><mo>=</mo><mfrac><mrow><mn>10</mn><mi>r</mi></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>15</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mi>a</mi><mn>6</mn></msup><msup><mi>b</mi><mrow><mo>-</mo><mn>9</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math> is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mrow></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p>For the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>15</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>15</mn></msup></math> is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>-</mo><mfrac><mi>r</mi><mn>3</mn></mfrac><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mo>-</mo><mn>15</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>10</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>15</mn></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>6</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mi mathvariant="normal">a</mi><mn>9</mn></msup><mo>&#215;</mo><msup><mi mathvariant="normal">b</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>9</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mi>a</mi><mn>6</mn></msup><msup><mi>b</mi><mrow><mo>-</mo><mn>9</mn></mrow></msup><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>6</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mi mathvariant="normal">a</mi><mn>9</mn></msup><mo>&#215;</mo><msup><mi>b</mi><mrow><mo>-</mo><mn>6</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mi>a</mi><mn>9</mn></msup><msup><mi>b</mi><mn>6</mn></msup></mfrac><mo>=</mo><mfrac><msup><mi>a</mi><mn>6</mn></msup><msup><mi>b</mi><mn>9</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>3</mn></msup><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>a</mi><mi>b</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q53. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

If the co-efficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>9</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math>and the co-efficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>9</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> are equal, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

<p>Given,</p><p>The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>9</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math>and the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>9</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> are equal,</p><p>Now the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> is given by <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><msup><mi>&#945;</mi><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>&#946;</mi><mi>r</mi></msup></mfrac><mo>&#215;</mo><msup><mi>x</mi><mrow><mn>3</mn><mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mo>-</mo><mi>r</mi></mrow></msup></math></p><p>So, for <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>9</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn><mo>-</mo><mn>4</mn><mi>r</mi><mo>=</mo><mn>9</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>Hence, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">x</mi><mn>9</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><msup><mi>&#945;</mi><mn>5</mn></msup><msup><mi>&#946;</mi><mn>6</mn></msup></mfrac></math></p><p>Similarly, for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>9</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>&#946;</mi><msup><mi>x</mi><mn>3</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup><mo>=</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><msup><mi>&#945;</mi><mn>6</mn></msup><msup><mi>&#946;</mi><mn>5</mn></msup></mfrac></math></p><p>Now given both coefficient are equal,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><msub><mi>C</mi><mn>6</mn></msub></mfrac><mo>&#183;</mo><mfrac><msup><mi>&#945;</mi><mn>5</mn></msup><msup><mi>&#946;</mi><mn>6</mn></msup></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>11</mn><msub><mi>C</mi><mn>5</mn></msub></mfrac><mo>&#183;</mo><mfrac><msup><mi>&#945;</mi><mn>6</mn></msup><msup><mi>&#946;</mi><mn>5</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>&#946;</mi></mfrac><mo>=</mo><mo>-</mo><mi>&#945;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#945;</mi><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>&#945;</mi><mi>&#946;</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q54. JEE Main 2023 (29 Jan Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the coefficients of three consecutive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mo>)</mo><mi mathvariant="normal">n</mi></msup></math> be in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mo>&#160;</mo><mn>5</mn><mo>:</mo><mo>&#160;</mo><mn>8</mn></math>. Then the coefficient of the term, which is in the middle of these three terms, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1120**

**Detailed Solution:**

<p>Given,</p><p>The coefficients of three consecutive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mo>)</mo><mi mathvariant="normal">n</mi></msup></math> be in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mo>&#160;</mo><mn>5</mn><mo>:</mo><mo>&#160;</mo><mn>8</mn></math>.</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><msup><mo>)</mo><mi mathvariant="normal">n</mi></msup></math> is given by, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">t</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>(</mo><mn>2</mn><mi mathvariant="normal">x</mi><msup><mo>)</mo><mi mathvariant="normal">r</mi></msup></math></p><p>Now let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></math> are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>5</mn><mo>:</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>T</mi><mi>r</mi></msub><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi mathvariant="normal">n</mi></mmultiscripts><mo>(</mo><mn>2</mn><msup><mo>)</mo><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow></msup></mrow><mrow><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none/><mprescripts/><none/><mi mathvariant="normal">n</mi></mmultiscripts><mo>(</mo><mn>2</mn><msup><mo>)</mo><mi mathvariant="normal">r</mi></msup></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfrac><mrow><mi mathvariant="normal">n</mi><mo>!</mo></mrow><mrow><mo>(</mo><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>!</mo><mo>(</mo><mi mathvariant="normal">n</mi><mo>-</mo><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>!</mo></mrow></mfrac><mfrac><mrow><mi mathvariant="normal">n</mi><mo>!</mo><mo>(</mo><mn>2</mn><mo>)</mo></mrow><mrow><mi mathvariant="normal">r</mi><mo>!</mo><mo>(</mo><mi mathvariant="normal">n</mi><mo>-</mo><mi mathvariant="normal">r</mi><mo>)</mo><mo>!</mo></mrow></mfrac></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>r</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>&#8658;</mo><mn>5</mn><mi>r</mi><mo>=</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>4</mn><mi>r</mi><mo>+</mo><mn>4</mn></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>r</mi><mo>=</mo><mn>4</mn><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now taking other ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>(</mo><mn>2</mn><msup><mo>)</mo><mi mathvariant="normal">r</mi></msup></mrow><mrow><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>(</mo><mn>2</mn><msup><mo>)</mo><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mo>(</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>)</mo><mo>!</mo></mrow></mfrac><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>!</mo><mo>(</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>!</mo></mrow></mfrac></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>r</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>5</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>4</mn><mo>=</mo><mn>9</mn><mi>r</mi><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mn>2</mn></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi mathvariant="normal">n</mi><mo>+</mo><mn>4</mn><mo>=</mo><mn>5</mn><mi mathvariant="normal">n</mi><mo>-</mo><mn>4</mn><mo>&#8658;</mo><mi mathvariant="normal">n</mi><mo>=</mo><mn>8</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>So, coefficient of middle term will be</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><msup><mn>2</mn><mn>4</mn></msup><mo>=</mo><mn>16</mn><mo>&#215;</mo><mfrac><mrow><mn>8</mn><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>6</mn><mo>&#215;</mo><mn>5</mn></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>16</mn><mo>&#215;</mo><mn>70</mn><mo>=</mo><mn>1120</mn></math></p>

</details>

---

### Q55. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

Let he sum of the coefficient of first three terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>;</mo><mo>&#160;</mo><mi>x</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#8712;</mo><mi>N</mi></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>376</mn></math>. Then, the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> is equal to:

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **405**

**Detailed Solution:**

<p>We know that general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mrow><mo>-</mo><mn>3</mn></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mi>r</mi></msup><mo>&#160;</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#215;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mi>r</mi></msup><mo>&#160;</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><msub><mi>T</mi><mrow><mn>0</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mn>0</mn></msup><mo>&#160;</mo><msup><mi>x</mi><mi>n</mi></msup><mo>=</mo><msup><mi>x</mi><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#215;</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mn>1</mn></msup><mo>&#160;</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>3</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mn>2</mn></msup><mo>&#160;</mo><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>6</mn></mrow></msup></math></p><p>Now given sum is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>&#183;</mo><mn>3</mn><mo>+</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>=</mo><mn>376</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mn>9</mn><mo>=</mo><mn>376</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>1</mn><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow><mn>2</mn></mfrac><mo>&#183;</mo><mn>9</mn><mo>=</mo><mn>376</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>-</mo><mn>6</mn><mi>n</mi><mo>+</mo><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>9</mn><mi>n</mi><mo>=</mo><mn>752</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>15</mn><mi>n</mi><mo>-</mo><mn>750</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>250</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#177;</mo><msqrt><mn>25</mn><mo>+</mo><mn>3000</mn></msqrt></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mn>5</mn><mo>&#177;</mo><mn>55</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mfenced close="}" open="{"><mtext>ignoring&#160;negative&#160;sign</mtext></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#160;</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#160;</mo><msup><mn>3</mn><mi>r</mi></msup><mo>&#160;</mo><msup><mi>x</mi><mrow><mn>10</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup></math></p><p>So, for coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> we take </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p>So, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mn>2</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#160;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>=</mo><mn>45</mn><mo>&#215;</mo><mn>9</mn><mo>=</mo><mn>405</mn></math>.</p>

</details>

---

### Q56. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

Let the ratio of the fifth term from the beginning to the fifth term from the end in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mroot><mn>2</mn><mn>4</mn></mroot><mo>+</mo><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mrow></mfenced><mi>n</mi></msup></math>, in the increasing powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mroot><mn>6</mn><mn>4</mn></mroot><mo>:</mo><mn>1</mn></math>. If the sixth term from the beginning is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>&#945;</mi><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **84**

**Detailed Solution:**

<blockquote><p>Given,</p><p>The ratio of the fifth term from the beginning to the fifth term from the end in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mroot><mn>2</mn><mn>4</mn></mroot><mo>+</mo><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></mrow></mfenced><mi>n</mi></msup></math> in the increasing powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><mroot><mn>6</mn><mn>4</mn></mroot><mo>:</mo><mn>1</mn></math></p><p>Now according to given data we have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>T</mi><mn>5</mn></msub><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msub></mfrac><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><msup><mn>2</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msup><msup><mfenced><msup><mn>3</mn><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mn>4</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><msup><mn>2</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mn>4</mn></msup><msup><mfenced><msup><mn>3</mn><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mroot><mn>6</mn><mn>4</mn></mroot><mn>1</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mfrac><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow><mn>4</mn></mfrac></msup><msup><mn>3</mn><mfrac><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow><mn>4</mn></mfrac></msup><mo>=</mo><msup><mn>6</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>6</mn><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></msup><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>8</mn><mo>=</mo><mn>1</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>9</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>9</mn></mmultiscripts><msup><mfenced><msup><mn>2</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mn>4</mn></msup><msup><mfenced><msup><mn>3</mn><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mn>5</mn></msup><mo>=</mo><mfrac><mn>84</mn><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></math></p><p>Now comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mfrac><mi>&#945;</mi><mroot><mn>3</mn><mn>4</mn></mroot></mfrac></math>,</p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>84</mn></math></p></blockquote>

</details>

---

### Q57. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the coefficients of the middle terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac><mo>+</mo><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>,</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mi>x</mi></mrow></mfenced><mn>6</mn></msup><mo>,</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>, respectively form the first three terms of an A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is the common difference of this A.P., then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>d</mi></mrow><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **57**

**Detailed Solution:**

<blockquote><p>Let the coefficients of the middle terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac><mo>+</mo><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>4</mn></msup><mo>,</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mi>x</mi></mrow></mfenced><mn>6</mn></msup><mo>,</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>, respectively form the first three terms of an A.P. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math> is the common difference of this A.P., then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>d</mi></mrow><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></math> is equal to _____ .</p><p>Given,</p><p>Coefficients of middle terms of given expansions <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>1</mn><msqrt><mn>6</mn></msqrt></mfrac><mo>+</mo><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>4</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>&#946;</mi><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math> and<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mi>&#946;</mi><mn>2</mn></mfrac><mi>x</mi></mrow></mfenced><mn>6</mn></msup></math> are <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mfrac><mn>1</mn><mn>6</mn></mfrac><msup><mi>&#946;</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mo>-</mo><mi>&#946;</mi></mrow><mn>2</mn></mfrac></mfenced><mn>3</mn></msup></math> respectively,</p><p>Now it is given that middle terms are forming an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mo>-</mo><mi>&#946;</mi></mrow><mn>2</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mfrac><mn>1</mn><mn>6</mn></mfrac><msup><mi>&#946;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mo>.</mo><mn>2</mn><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>=</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>5</mn><msup><mi>&#946;</mi><mn>3</mn></msup></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mn>24</mn><mo>=</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>&#946;</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>&#946;</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>&#946;</mi><mo>+</mo><mn>10</mn><mi>&#946;</mi><mo>-</mo><mn>24</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#946;</mi><mfenced><mrow><mn>5</mn><mi>&#946;</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced><mrow><mn>5</mn><mi>&#946;</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>&#946;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>5</mn><mi>&#946;</mi><mo>-</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>2</mn></math> {which is not possible as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math>}</p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mfenced><mrow><mo>-</mo><mn>3</mn><mi>&#946;</mi></mrow></mfenced><mo>-</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>4</mn></mmultiscripts><mfrac><mn>1</mn><mn>6</mn></mfrac><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></math></p><p>Now putting the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>d</mi></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>d</mi></mrow><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>d</mi></mrow><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>50</mn><mo>-</mo><mn>2</mn><mfrac><mfenced><mrow><mo>-</mo><mn>6</mn><mi>&#946;</mi><mo>-</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced><msup><mi>&#946;</mi><mn>2</mn></msup></mfrac><mo>=</mo><mn>50</mn><mo>+</mo><mfrac><mn>12</mn><mi>&#946;</mi></mfrac><mo>+</mo><mn>2</mn><mo>=</mo><mn>57</mn></math></p></blockquote>

</details>

---

### Q58. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let for the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mi>th</mi></msup></math> term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math>, in the increasing powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn><mi>x</mi></math>, to be the greatest for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math>, the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>0</mn></msub></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is the ratio of the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>6</mn></msup></math> to the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>+</mo><msub><mi>n</mi><mn>0</mn></msub></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **24**

**Detailed Solution:**

<blockquote><p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><msup><mn>3</mn><mi>n</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math></p><p>Now if <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>9</mn></msub></math> is numerically greatest term, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>8</mn></msub><mo>&#8804;</mo><msub><mi>T</mi><mn>9</mn></msub><mo>&#8805;</mo><msub><mi>T</mi><mn>10</mn></msub></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></msup><msup><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mn>7</mn></msup><mo>&#8804;</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></msup><msup><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mn>8</mn></msup><mo>&#8805;</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mrow><mi>n</mi><mo>-</mo><mn>9</mn></mrow></msup><msup><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mn>9</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mo>!</mo><mn>7</mn><mo>!</mo></mrow></mfrac><mn>9</mn><mo>&#8804;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mo>!</mo><mn>8</mn><mo>!</mo></mrow></mfrac><mn>3</mn><mo>&#183;</mo><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mo>&#8805;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>9</mn></mrow></mfenced><mo>!</mo><mn>9</mn><mo>!</mo></mrow></mfrac><msup><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munder><mfrac><mn>9</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></mrow></mfrac><mo>&#9183;</mo></munder><mo>&#8804;</mo><munder><mrow><mfrac><mrow><mn>18</mn><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced><mn>8</mn></mrow></mfrac><mo>&#8805;</mo><mfrac><mn>36</mn><mrow><mn>9</mn><mo>.</mo><mn>8</mn></mrow></mfrac><mfrac><mn>9</mn><mn>4</mn></mfrac></mrow><mo>&#9183;</mo></munder></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>72</mn><mo>&#8804;</mo><mn>27</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn><mo>&#8805;</mo><mn>9</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>29</mn><mn>3</mn></mfrac><mo>&#8804;</mo><mi>n</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8804;</mo><mn>11</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>n</mi><mn>0</mn></msub><mo>=</mo><mn>10</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>3</mn><mo>+</mo><mn>6</mn><mi>x</mi></mrow></mfenced><mn>10</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mn>3</mn><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mn>6</mn><mi>x</mi></mrow></mfenced><mi>r</mi></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>6</mn><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mn>3</mn><mn>4</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>6</mn></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mn>3</mn><mn>7</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>3</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></mfrac><mo>&#183;</mo><mfrac><mrow><msup><mn>3</mn><mn>4</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>6</mn></msup></mrow><mrow><msup><mn>3</mn><mn>7</mn></msup><mo>&#183;</mo><msup><mn>6</mn><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>10</mn><mo>!</mo><mn>7</mn><mo>!</mo><mn>3</mn><mo>!</mo></mrow><mrow><mn>6</mn><mo>!</mo><mn>4</mn><mo>!</mo><mn>10</mn><mo>!</mo></mrow></mfrac><mo>&#183;</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mn>14</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>k</mi><mo>+</mo><msub><mi>n</mi><mn>0</mn></msub><mo>=</mo><mn>24</mn></math></p></blockquote>

</details>

---

### Q59. JEE Main 2022 (26 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

If the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>p</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>q</mi></msup><mo>,</mo><mi>p</mi><mo>,</mo><mi>q</mi><mo>&#8804;</mo><mn>15</mn></math>, are <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>5</mn></math> respectively, then the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **23**

**Detailed Solution:**

<blockquote><p>Given coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>p</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>q</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>p</mi></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>p</mi></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mo>=</mo><mo>-</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>p</mi><mo>-</mo><mi>q</mi><mo>=</mo><mo>-</mo><mn>3</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Now coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>p</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>q</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><mi>q</mi><mprescripts></mprescripts><none></none><mi>P</mi></mmultiscripts><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>P</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>P</mi></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mo>=</mo><mo>-</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>-</mo><mi>p</mi><mi>q</mi><mo>+</mo><mfrac><mrow><mi>p</mi><mfenced><mrow><mi>p</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mi>q</mi><mfenced><mrow><mi>q</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mo>-</mo><mn>5</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8943;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi><mo>=</mo><mn>8</mn><mo>,</mo><mi>q</mi><mo>=</mo><mn>11</mn></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>p</mi></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mi>q</mi></msup></math> will be,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>p</mi></mmultiscripts><mo>+</mo><msubsup><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mi>p</mi></mmultiscripts><mn>1</mn><mi>q</mi></msubsup><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><msubsup><mmultiscripts><mi>C</mi><mprescripts></mprescripts><none></none><mi>p</mi></mmultiscripts><mn>2</mn><mi>q</mi></msubsup><msub><mi>C</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>8</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>23</mn></math></p></blockquote>

</details>

---

### Q60. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the maximum value of the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>+</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mrow/><mfrac><mn>1</mn><mn>10</mn></mfrac></msup></msup><mi>t</mi></mfrac></mrow></mfenced><mn>15</mn></msup><mo>,</mo><mi>x</mi><mo>&#8805;</mo><mn>0</mn></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>&#160;</mo><mi mathvariant="normal">K</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6006**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>+</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>10</mn></mfrac></msup><mi>t</mi></mfrac></mrow></mfenced><mn>15</mn></msup></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mfenced><mrow><msup><mi>t</mi><mn>2</mn></msup><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mi>r</mi><mn>10</mn></mfrac></msup><msup><mi>t</mi><mi>r</mi></msup></mfrac></math></p><p>For independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>10</mn></math></p><p>So, Maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>10</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mi>x</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math> will be at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mtext>as&#160;</mtext><mfrac><mrow><mi>d</mi><mi>y</mi></mrow><mrow><mi>d</mi><mi>x</mi></mrow></mfrac><mfenced><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-2</mo><mi>x</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>10</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>3003</mn><mn>4</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mfrac><mn>3003</mn><mn>4</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mi>K</mi><mo>=</mo><mn>6006</mn></math></p></blockquote>

</details>

---

### Q61. JEE Main 2022 (29 Jun Shift 2)

*Type:* `numerical` | *Level:* `2`

Let the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mfrac></mrow></mfenced><mn>15</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math>, be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> respectively. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is a positive integer such <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi>r</mi><mo>.</mo></mrow><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mn>2</mn><mi>r</mi></msup></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>The <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mfrac></mrow></mfenced><mn>15</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mrow></mfenced><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p>For term having <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>15</mn><mo>-</mo><mi>r</mi></mrow><mn>5</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>5</mn></mfrac><mo>=</mo><mo>-</mo><mn>1</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>10</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>5</mn></msup><mo>&#183;</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>10</mn></msup></math></p><p>For term having <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>15</mn><mo>-</mo><mn>2</mn><mi>r</mi></mrow><mn>5</mn></mfrac><mo>=</mo><mo>-</mo><mn>3</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>15</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>0</mn></msup><mo>&#183;</mo><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>15</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>m</mi><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>5</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>5</mn></msup></math></p><p>On comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#183;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mi>r</mi></msup></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q62. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>5</mn></math> be an integer. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mi>n</mi></msup><mo>-</mo><mn>8</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>64</mn><mi>&#945;</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mi>n</mi></msup><mo>-</mo><mn>5</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>25</mn><mo>&#160;</mo><mi>&#946;</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi></math> is equal to:</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p>Using the binomial expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mi>x</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>x</mi><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>x</mi><mi>n</mi></msup></math></p><p>We get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mfrac><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mn>8</mn></mrow></mfenced><msup><mrow></mrow><mi>n</mi></msup><mo>-</mo><mn>8</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>64</mn></mfrac><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mn>8</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo></math>Similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mn>5</mn><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mfenced><mrow><mn>8</mn><mo>-</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mfenced><mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><mo>-</mo><msup><mn>5</mn><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup></mrow></mfenced></math></p><p>So, option (C) is the answer.</p>

</details>

---

### Q63. JEE Main 2022 (28 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expression of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup><mo>,</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>40</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><mn>200</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>39</mn><mn>200</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>11</mn><mn>50</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>33</mn><mn>200</mn></mfrac></math>**

**Detailed Solution:**

<p>General term of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><mfrac><msup><mn>5</mn><mrow><mn>11</mn><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup><msup><mn>2</mn><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup></mfrac><mo>&#183;</mo><msup><mi>x</mi><mrow><mn>33</mn><mo>-</mo><mn>5</mn><mi>r</mi></mrow></msup></math></p><p>The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> will be the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>0</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup><mo>+</mo><mn>3</mn><mo>&#215;</mo></math> coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>3</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>5</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>5</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>7</mn></msup><mo>&#183;</mo><mfrac><msup><mn>5</mn><mrow><mo>-</mo><mn>3</mn></mrow></msup><msup><mn>2</mn><mn>4</mn></msup></mfrac><mo>=</mo><mfrac><mn>330</mn><mrow><msup><mn>5</mn><mn>3</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>33</mn><mn>200</mn></mfrac></math></p>

</details>

---

### Q64. JEE Main 2022 (28 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

The number of positive integers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> such that the constant term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><msup><mi>x</mi><mi>k</mi></msup></mfrac></mrow></mfenced><mn>12</mn></msup><mo>,</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><mi>l</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is an odd integer, is ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

<p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><msup><mi>x</mi><mi>k</mi></msup></mfrac></mrow></mfenced><mn>12</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>3</mn><msup><mi>x</mi><mi>k</mi></msup></mfrac></mfenced><mi>r</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mn>3</mn><mi>r</mi></msup><mo>&#183;</mo><msup><mi>x</mi><mrow><mn>36</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>-</mo><mi>k</mi><mi>r</mi></mrow></msup></math></p><p>For the term to be independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>-</mo><mi>k</mi><mi>r</mi><mo>=</mo><mn>0</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mn>36</mn><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfrac></math> </p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> to be a whole number.</p><p>But for <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mn>3</mn><mi>r</mi></msup></math> to be in the form of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><mi>l</mi></math></p><p>Only <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></math> satisfies the above relation.</p>

</details>

---

### Q65. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `2`

If the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><msqrt><mi>x</mi></msqrt><msup><mn>5</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfrac><mo>+</mo><mfrac><msqrt><mn>5</mn></msqrt><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfrac></mrow></mfenced><mn>60</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mi>k</mi></msup><mi>l</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi><mo>,</mo><mi>k</mi><mo>&#8712;</mo><mi>N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>l</mi></math> is coprime to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><msup><mfenced><mfrac><msqrt><mi>x</mi></msqrt><msup><mn>5</mn><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle></msup></mfrac></mfenced><mrow><mn>60</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><msqrt><mn>5</mn></msqrt><msup><mi>x</mi><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>3</mn></mfrac></mstyle></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>60</mn><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>3</mn></mfrac><mo>=</mo><mn>10</mn><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>r</mi><mo>=</mo><mn>24</mn></math></p><p>Hence coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>10</mn></msup></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>24</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><msup><mn>5</mn><mn>3</mn></msup></math></p><p>Now, exponent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>24</mn><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts></math> will be the power of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>60</mn><mo>!</mo></mrow><mrow><mn>24</mn><mo>!</mo><mn>36</mn><mo>!</mo></mrow></mfrac><mo>&#160;</mo><mtext>i.e.</mtext><mo>&#160;</mo><mfrac><msup><mn>5</mn><mn>14</mn></msup><mrow><msup><mn>5</mn><mn>4</mn></msup><mo>&#183;</mo><msup><mn>5</mn><mn>8</mn></msup></mrow></mfrac><mo>=</mo><msup><mn>5</mn><mn>2</mn></msup></math></p><p>i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q66. JEE Main 2022 (25 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>101</mn></msup></math> in the expression
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>499</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>498</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>x</mi><mn>500</mn></msup><mo>,</mo><mi>x</mi><mo>&#62;</mo><mn>0</mn></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>&#160;</mo><mn>501</mn></msup><msub><mi>C</mi><mn>101</mn></msub><mo>&#215;</mo><msup><mn>5</mn><mn>399</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mrow><mo>&#160;</mo><mn>501</mn></mrow></msup><msub><mi>C</mi><mn>101</mn></msub><mo>&#215;</mo><msup><mn>5</mn><mn>400</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mrow><mo>&#160;</mo><mn>501</mn></mrow></msup><msub><mi>C</mi><mn>100</mn></msub><mo>&#215;</mo><msup><mn>5</mn><mn>400</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mn>500</mn></msup><msub><mi>C</mi><mn>101</mn></msub><mo>&#215;</mo><msup><mn>5</mn><mn>399</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>&#160;</mo><mn>501</mn></msup><msub><mi>C</mi><mn>101</mn></msub><mo>&#215;</mo><msup><mn>5</mn><mn>399</mn></msup></math>**

**Detailed Solution:**

<p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>499</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>498</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>x</mi><mn>500</mn></msup></math></p><p>Using sum of the G.P in the given expression we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>500</mn></msup><mfenced close="]" open="["><mrow><msup><mfenced><mfrac><mi>x</mi><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mn>501</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mfenced><mfrac><mi>x</mi><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>501</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>501</mn></msup></mrow><mrow><mo>-</mo><mn>5</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>501</mn></msup><mo>-</mo><mfrac><msup><mi>x</mi><mn>501</mn></msup><mn>5</mn></mfrac></math></p><p>Now coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>101</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac><msup><mfenced><mrow><mn>5</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>501</mn></msup></math> will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac><mfenced><mmultiscripts><mi>C</mi><mn>101</mn><none></none><mprescripts></mprescripts><none></none><mn>501</mn></mmultiscripts></mfenced><msup><mfenced><mn>5</mn></mfenced><mrow><mn>501</mn><mo>-</mo><mn>101</mn></mrow></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>5</mn><mn>399</mn></msup><mfenced><mmultiscripts><mi>C</mi><mn>101</mn><none></none><mprescripts></mprescripts><none></none><mn>501</mn></mmultiscripts></mfenced></math></p>

</details>

---

### Q67. JEE Main 2021 (01 Sep Shift 2)

*Type:* `numerical` | *Level:* `1`

If the sum of the coefficients in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4096</mn><mo>,</mo></math> then the greatest coefficient in the expansion is _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **924**

**Detailed Solution:**

<p>Sum of coefficients of the expression <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>n</mi></msup><mo>=</mo><mn>4096</mn><mo>=</mo><msup><mn>2</mn><mn>12</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>12</mn></math> </p><p>Now greatest binomial coefficient of the expression<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mi>n</mi></msup></math> is the middle term&#39;s coefficient so <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><mo>=</mo><mn>924</mn></math></p>

</details>

---

### Q68. JEE Main 2021 (31 Aug Shift 1)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><msup><mn>3</mn><mn>6</mn></msup><msup><mn>4</mn><mn>4</mn></msup></mfrac></mfenced><mi>k</mi></math> is the term, independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mi>x</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>12</mn></msup><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **55**

**Detailed Solution:**

<p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mi>x</mi><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>12</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term of an expression is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>&#160;</mo><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>y</mi><mi>r</mi></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>12</mn></mmultiscripts><msup><mfenced><mfrac><mi>x</mi><mn>4</mn></mfrac></mfenced><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>12</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>r</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>12</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>4</mn></mfrac></mfenced><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>(</mo><mo>-</mo><mn>12</mn><msup><mo>)</mo><mi>r</mi></msup><mo>&#183;</mo><msup><mi>x</mi><mrow><mn>12</mn><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mn>12</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>0</mn></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>So term independent from <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>5</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>12</mn></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>8</mn></msup></mfrac><mo>&#183;</mo><msup><mn>3</mn><mn>4</mn></msup><mo>&#183;</mo><msup><mn>4</mn><mn>4</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>12</mn></mmultiscripts><mo>&#183;</mo><mfrac><msup><mn>3</mn><mn>4</mn></msup><msup><mn>4</mn><mn>4</mn></msup></mfrac></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo><mi>r</mi><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>55</mn><mo>&#215;</mo><mfrac><msup><mn>3</mn><mn>6</mn></msup><msup><mn>4</mn><mn>4</mn></msup></mfrac></math></p><p>They given that it is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>k</mi><mo>&#160;</mo><mfrac><msup><mn>3</mn><mn>6</mn></msup><msup><mn>4</mn><mn>4</mn></msup></mfrac></math></p><p>So required value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mi>k</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>55</mn><mo>.</mo></math></p>

</details>

---

### Q69. JEE Main 2021 (27 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

A possible value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> for which the ninth term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="}" open="{"><mrow><msup><mn>3</mn><mrow><msub><mi>log</mi><mn>3</mn></msub><msqrt><msup><mn>25</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>7</mn></msqrt></mrow></msup><mo>+</mo><msup><mn>3</mn><mrow><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup></mrow></mfenced><mn>10</mn></msup></math> in the increasing powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>3</mn><mrow><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn><mo>,</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="}" open="{"><mrow><msup><mn>3</mn><mrow><msub><mi>log</mi><mn>3</mn></msub><msqrt><msup><mn>25</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>7</mn></msqrt></mrow></msup><mo>+</mo><msup><mn>3</mn><mrow><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><msub><mi>log</mi><mn>3</mn></msub><mfenced><mrow><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></msup></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="}" open="{"><mrow><msqrt><msup><mn>25</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>7</mn></msqrt><mo>+</mo><msup><mfenced><mrow><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>8</mn></mfrac></msup></mrow></mfenced><mn>10</mn></msup><mo>,</mo></math> using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mrow><mi>n</mi><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi></mrow></msup><mo>=</mo><msup><mi>x</mi><mi>n</mi></msup></math></p><p>Using the formula of the general term in the Binomial theorem for non negative integral index, i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>b</mi><mi>r</mi></msup><mo>&#160;</mo></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup><mo>,</mo></math> we get,  <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>9</mn></msub><mo>=</mo><msub><mi>T</mi><mrow><mn>8</mn><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mfenced><mrow><msup><mn>25</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>+</mo><mn>7</mn></mrow></mfenced><mo>&#215;</mo><msup><mfenced><mrow><msup><mn>5</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>180</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mn>25</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>7</mn></mrow><mrow><msup><mn>5</mn><mfenced><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn></mrow><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>4</mn><mo>,</mo></math> taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi><mo>=</mo><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>+</mo><mn>7</mn><mo>=</mo><mn>4</mn><mfenced><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>t</mi><mo>+</mo><mn>3</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>t</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mfenced><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>&#8658;</mo><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>&#8658;</mo><msup><mn>5</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mn>5</mn><mn>0</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>0</mn></math> (one of the possible value).</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q70. JEE Main 2021 (27 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup><mo>,</mo><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> are equal, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>**

**Detailed Solution:**

<p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mi>b</mi><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mfenced><mfrac><mn>1</mn><mrow><mi>b</mi><mi>x</mi></mrow></mfrac></mfenced><mi mathvariant="normal">r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mrow><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><mo>&#183;</mo><mfrac><mn>1</mn><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mi>r</mi></msup></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>So, the term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>5</mn></msup></mfrac><mo>&#183;</mo><msup><mi>x</mi><mn>7</mn></msup></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>-</mo><mfrac><mn>1</mn><mrow><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mn>11</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mfenced><mi>x</mi></mfenced><mrow><mn>11</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mo>&#160;</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><msup><mi>x</mi><mrow><mn>11</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><mo>&#183;</mo><mfrac><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><msup><mi>b</mi><mi>r</mi></msup></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mo>-</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>So, the term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>6</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>6</mn></msup></mfrac><msup><mi>x</mi><mrow><mo>-</mo><mn>7</mn></mrow></msup></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>5</mn></msup></mfrac><mo>=</mo><mmultiscripts><mi>C</mi><mn>6</mn><none></none><mprescripts></mprescripts><none></none><mn>11</mn></mmultiscripts><mo>&#183;</mo><mfrac><mn>1</mn><msup><mrow><mo>&#160;</mo><mi>b</mi></mrow><mn>6</mn></msup></mfrac></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi><mo>&#8800;</mo><mn>0</mn><mo>&#160;</mo><mo>&#8756;</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q71. JEE Main 2021 (25 Jul Shift 2)

*Type:* `numerical` | *Level:* `1`

If the co-efficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>8</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mi>x</mi><mn>3</mn></mfrac></mrow></mfenced><mi>n</mi></msup></math> are equal, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to :

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **55**

**Detailed Solution:**

We have, the co-efficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>7</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>8</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><mo>+</mo><mfrac><mi>x</mi><mn>3</mn></mfrac></mrow></mfenced><mi>n</mi></msup></math> are equal.<p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>7</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>7</mn></mrow></msup><mfrac><mn>1</mn><msup><mn>3</mn><mn>7</mn></msup></mfrac><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>8</mn></mrow></msup><mfrac><mn>1</mn><msup><mn>3</mn><mn>8</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>7</mn><mo>=</mo><mn>48</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>55</mn><mo>.</mo></math></p>

</details>

---

### Q72. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the greatest value of the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>&#945;</mi><mo>+</mo><mi>a</mi><mfrac><mrow><mi>cos</mi><mi>&#945;</mi></mrow><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mfrac><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>1</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>2</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mi>th</mi></msup></math><sup> </sup>term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>&#945;</mi><mo>+</mo><mi>a</mi><mfrac><mrow><mi>cos</mi><mi>&#945;</mi></mrow><mi>x</mi></mfrac></mrow></mfenced><mn>10</mn></msup></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mrow><mi>a</mi><mi>cos</mi><mi>&#945;</mi></mrow><mi>x</mi></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></math> will be independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mi>x</mi><mi>sin</mi><mi>&#945;</mi></mrow></mfenced><mn>5</mn></msup><mo>&#215;</mo><msup><mfenced><mfrac><mrow><mi>a</mi><mi>cos</mi><mi>&#945;</mi></mrow><mi>x</mi></mfrac></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><mo>&#215;</mo><msup><mi>a</mi><mn>5</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>5</mn></msup></mfrac><msup><mfenced><mrow><mi>sin</mi><mn>2</mn><mi>&#945;</mi></mrow></mfenced><mn>5</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub></math> will be greatest, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>sin</mi><mn>2</mn><mi>&#945;</mi><mo>=</mo><mn>1</mn></math></p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mfrac><msup><mi>a</mi><mn>5</mn></msup><msup><mn>2</mn><mn>5</mn></msup></mfrac><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>2</mn></math></p>

</details>

---

### Q73. JEE Main 2021 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum of all those terms which are rational numbers in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mrow></mfenced><mn>12</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>89</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>27</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>43</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>r</mi><mi>th</mi></msup></math> term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mrow></mfenced><mn>12</mn></msup></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>12</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mfrac><mi>r</mi><mn>3</mn></mfrac></msup><mo>&#183;</mo><msup><mfenced><mn>3</mn></mfenced><mfrac><mrow><mn>12</mn><mo>-</mo><mi>r</mi></mrow><mn>4</mn></mfrac></msup></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></math> will be rational number, when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>9</mn><mo>,</mo><mn>12</mn><mo>&#160;</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>0</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>8</mn><mo>,</mo><mn>12</mn><mo>&#160;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>12</mn></math> for rational term of the expansion</p><p>Therefore, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>+</mo><msub><mi>T</mi><mn>13</mn></msub><mo>=</mo><mn>1</mn><mo>&#215;</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mn>1</mn><mo>&#215;</mo><msup><mn>2</mn><mn>4</mn></msup><mo>&#215;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>27</mn><mo>+</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>43</mn><mo>.</mo></math></p>

</details>

---

### Q74. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `2`

The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo><mn>1</mn></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **210**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mfrac><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mfenced></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced><mn>10</mn></msup></math></p><p>Now the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>th</mi></msup></math> Term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#183;</mo><msup><mi>x</mi><mrow><mo>-</mo><mi>r</mi><mo>/</mo><mn>2</mn></mrow></msup><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup></math></p><p>For independent term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mn>5</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>210</mn></math></p>

</details>

---

### Q75. JEE Main 2021 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

<p>The ratio of the coefficient of the middle term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>20</mn></msup></math> and the sum of the coefficients of two middle terms in expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>19</mn></msup></math> is <u>          </u>.</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1**

**Detailed Solution:**

In <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is even, then the middle term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mi>n</mi><mn>2</mn></mfrac><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term.<p>So, Coefficient of middle term in <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>20</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts></math></p>In <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is odd, then the middle term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></mfenced><mrow><mi>t</mi><mi>h</mi></mrow></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow><mn>2</mn></mfrac></mfenced><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term.<p>So, Sum of Coefficient of two middle terms in</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>+</mo><mi>x</mi><msup><mo>)</mo><mn>19</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts></math></p><p>So required ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts><mrow><mmultiscripts><mi>C</mi><mn>9</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>19</mn></mmultiscripts></mrow></mfrac><mo>=</mo><mfrac><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts><mmultiscripts><mi>C</mi><mn>10</mn><none></none><mprescripts></mprescripts><none></none><mn>20</mn></mmultiscripts></mfrac><mo>=</mo><mn>1</mn></math></p>

</details>

---

### Q76. JEE Main 2021 (22 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

If the constant term, in binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mi>r</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is equal to ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **8**

**Detailed Solution:**

<p>The general term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>R</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>R</mi></mrow></msup><msup><mi>b</mi><mi>R</mi></msup><mo>.</mo></math></p><p>Thus, the general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mi>r</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>R</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mi>r</mi></msup></mrow></mfenced><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></msup><msup><mfenced><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>R</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>R</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mfenced><mrow><msup><mn>2</mn><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></msup><msup><mi>x</mi><mrow><mi>r</mi><mfenced><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></mfenced></mrow></msup></mrow></mfenced><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>R</mi></mrow></msup></math></p><p>Given, the constant term in the expansion is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mi>R</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></msup><mo>=</mo><mn>180</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math> </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>10</mn><mo>-</mo><mi>R</mi><mo>)</mo><mi>r</mi><mo>-</mo><mn>2</mn><mi>R</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>R</mi></mrow><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>(</mo><mi>R</mi><mo>-</mo><mn>10</mn><mo>)</mo></mrow><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></mfrac><mo>+</mo><mfrac><mn>20</mn><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>20</mn><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>Since <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is positive integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> is also an integer, hence, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> is such that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mi>R</mi></math> must divide <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>.</mo></math></p><p>This is possible, when the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mi>R</mi></math> can be one from the divisors of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>-</mo><mi>R</mi></math> can be from <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> and consequently, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math> can be <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math> respectively.</p><p>But for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mn>5</mn></math> equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> is  not satisfied, hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>8</mn></math></p><p>as <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>R</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mn>2</mn><mrow><mn>10</mn><mo>-</mo><mi>R</mi></mrow></msup><mo>=</mo><mn>180</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&#215;</mo><mn>8</mn></mrow><mrow><mn>10</mn><mo>-</mo><mn>8</mn></mrow></mfrac><mo>=</mo><mn>8</mn><mo>.</mo></math></p>

</details>

---

### Q77. JEE Main 2021 (20 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For the natural numbers <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>,</mo></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>-</mo><mi>y</mi><msup><mo>)</mo><mi>m</mi></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>y</mi><msup><mo>)</mo><mi>n</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>y</mi><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msub><msup><mi>y</mi><mrow><mi>m</mi><mo>+</mo><mi>n</mi></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mo>&#160;</mo><mi>n</mi><mo>,</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>88</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>80</mn></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>-</mo><mi>y</mi><msup><mo>)</mo><mi>m</mi></msup><mo>(</mo><mn>1</mn><mo>+</mo><mi>y</mi><msup><mo>)</mo><mi>n</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mi>y</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>m</mi><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>m</mi></msup><msup><mi>y</mi><mi>m</mi></msup></mrow></mfenced><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mi>y</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>y</mi><mi>n</mi></msup></mrow></mfenced></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mfenced><msub><mi>a</mi><mn>1</mn></msub></mfenced><mo>=</mo><mn>1</mn><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>n</mi><mo>-</mo><mi>m</mi><mo>=</mo><mn>10</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>y</mi><mn>2</mn></msup><mfenced><msub><mi>a</mi><mn>2</mn></msub></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>m</mi></mmultiscripts><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>+</mo><msup><mn>1</mn><mi>m</mi></msup><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>-</mo><mi>m</mi><mo>&#183;</mo><mi>n</mi><mo>+</mo><mfrac><mrow><mi>m</mi><mo>(</mo><mi>m</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>=</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>m</mi><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>m</mi><mi>n</mi><mo>-</mo><mo>(</mo><mi>n</mi><mo>+</mo><mi>m</mi><mo>)</mo><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mi>m</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mi>n</mi><mo>+</mo><mi>m</mi><mo>)</mo><mo>=</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>+</mo><mi>m</mi><mo>=</mo><mn>80</mn><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math></p><p>By equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>35</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>45</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>80</mn></math></p>

</details>

---

### Q78. JEE Main 2021 (20 Jul Shift 1)

*Type:* `numerical` | *Level:* `1`

The number of rational terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>4</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></mrow></mfenced><mn>120</mn></msup></math>is_______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **21**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>4</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>6</mn></mfrac></msup></mrow></mfenced><mn>120</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>120</mn></mmultiscripts><msup><mfenced><msup><mn>4</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></msup></mfenced><mrow><mn>120</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mn>5</mn></mfenced><mfrac><mi>r</mi><mn>6</mn></mfrac></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>120</mn></mmultiscripts><msup><mfenced><mn>2</mn></mfenced><mfrac><mrow><mn>120</mn><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><msup><mfenced><mn>5</mn></mfenced><mfrac><mi>r</mi><mn>6</mn></mfrac></msup></math>
 </p><p>For rational terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>6</mn><mi>&#955;</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>r</mi><mo>&#8804;</mo><mn>120</mn></math>, hence</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mn>120</mn></math></p><p>So, total number of rational terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math>.</p>

</details>

---

### Q79. JEE Main 2021 (20 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>256</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>101</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></msup></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>16</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>16</mn><none/><mprescripts/><none/><mrow><mo>-</mo><mn>100</mn></mrow></mmultiscripts></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mrow><mo>-</mo><mn>100</mn></mrow></mmultiscripts></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>101</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mn>100</mn></msup><msup><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>100</mn></msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mn>100</mn></msup><mo>&#183;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>100</mn></msup><mo>&#183;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mrow></mfenced><mn>100</mn></msup><mo>&#9183;</mo></munder><mrow><mi>No</mi><mo>&#160;</mo><mi>term</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><msup><mi>x</mi><mn>256</mn></msup></mrow></munder><mo>-</mo><munder><munder><mrow><mi mathvariant="normal">x</mi><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi mathvariant="normal">x</mi><mn>3</mn></msup></mrow></mfenced><mn>100</mn></msup></mrow><mo>&#9183;</mo></munder><mrow><mi>we</mi><mo>&#160;</mo><mi>find</mi><mo>&#160;</mo><mi>cofficient</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><msup><mi mathvariant="normal">x</mi><mn>255</mn></msup></mrow></munder></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>100</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><msup><mi>x</mi><mn>6</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mmultiscripts><mi>C</mi><mn>85</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><mfenced><mrow><mo>-</mo><msup><mi>x</mi><mn>255</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><msup><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>100</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><mi>x</mi><mo>-</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mn>85</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><msup><mi>x</mi><mn>256</mn></msup></math></p><p>Required coefficient</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>85</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mn>100</mn></mmultiscripts></math></p>

</details>

---

### Q80. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced close="]" open="["><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>1</mn></math>, is equal to ___.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **210**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="[" close="]"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mi>x</mi><mrow><mn>2</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mfrac><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn></mrow><msqrt><mi>x</mi></msqrt></mfrac></mfenced></mrow></mfenced><mn>10</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup><mo>-</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mn>10</mn></msup></math></p><p>General term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>10</mn><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><msup><mi>x</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mfrac><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow><mn>3</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mn>20</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mn>3</mn><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>5</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn></mrow><mrow><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>210</mn></math></p>

</details>

---

### Q81. JEE Main 2021 (17 Mar Shift 2)

*Type:* `numerical` | *Level:* `1`

Let the coefficients of third, fourth and fifth terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup><mo>,</mo><mo>&#160;</mo><mi>x</mi><mo>&#8800;</mo><mn>0</mn><mo>,</mo></math> be in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>:</mo><mn>8</mn><mo>:</mo><mn>3</mn><mo>.</mo></math> Then the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion, is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **4**

**Detailed Solution:**

<p>The general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>b</mi><mi>r</mi></msup><mo>.</mo></math></p><p>Hence, the general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mo>(</mo><mi>x</mi><msup><mo>)</mo><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mfrac><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>r</mi></msup><msup><mi>x</mi><mrow><mi>n</mi><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup></math></p><p>Given the coefficients of third, fourth and fifth terms are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn><mo>:</mo><mn>8</mn><mo>:</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>2</mn></msup></mrow></mfenced><mo>:</mo><mfenced><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>3</mn></msup></mrow></mfenced><mo>:</mo><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>4</mn></msup><mo>=</mo><mn>12</mn><mo>:</mo><mn>8</mn><mo>:</mo><mn>3</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>2</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>3</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>8</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>3</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>4</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfrac><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>3</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mi>a</mi></mrow></mfrac><mo>=</mo><mfrac><mn>8</mn><mn>3</mn></mfrac></math></p><p>On dividing the two equations, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>4</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>16</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>6</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>.</mo></math></p><p>For term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>3</mn><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> The coefficient is<math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>6</mn></mmultiscripts><msup><mfenced><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>=</mo><mfrac><mn>15</mn><mn>4</mn></mfrac><mo>.</mo></math></p><p>Hence, the nearest integer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>.</mo></math></p>

</details>

---

### Q82. JEE Main 2021 (17 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the fourth term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>7</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4480</mn><mo>,</mo></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mi>N</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>7</mn></msup><mo>.</mo><mo>&#160;</mo></math></p><p>The general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>x</mi><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>7</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mi>x</mi><mi>r</mi></msup><msup><mfenced><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mrow><mn>7</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>.</mo></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>4</mn></msub><mo>=</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>7</mn></mmultiscripts><msup><mi>x</mi><mn>4</mn></msup><msup><mfenced><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>3</mn></msup><mo>=</mo><mn>4480</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>7</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>5</mn></mrow><mrow><mn>3</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mn>1</mn></mrow></mfrac><msup><mi>x</mi><mrow><mn>4</mn><mo>+</mo><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup><mo>=</mo><mn>4480</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mfenced><mrow><mn>4</mn><mo>+</mo><mn>3</mn><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></mfenced></msup><mo>=</mo><mn>128</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mfenced><mrow><mn>4</mn><mo>+</mo><mn>3</mn><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></mfenced></msup><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup></math></p><p>Now, from the option only at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>LHS</mi><mo>=</mo><mi>RHS</mi><mo>.</mo></math></p>

</details>

---

### Q83. JEE Main 2021 (16 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of irrational terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mn>5</mn><mrow><mn>1</mn><mo>/</mo><mn>8</mn></mrow></msup></mrow></mfenced><mn>60</mn></msup></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> is divisible by :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup><mo>+</mo><msup><mn>5</mn><mrow><mn>1</mn><mo>/</mo><mn>8</mn></mrow></msup></mrow></mfenced><mn>60</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><msup><mfenced><msup><mn>3</mn><mrow><mn>1</mn><mo>/</mo><mn>4</mn></mrow></msup></mfenced><mrow><mn>60</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>.</mo><msup><mfenced><msup><mn>5</mn><mrow><mn>1</mn><mo>/</mo><mn>8</mn></mrow></msup></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>60</mn></mmultiscripts><msup><mfenced><mn>3</mn></mfenced><mfrac><mrow><mn>60</mn><mo>-</mo><mi>r</mi></mrow><mn>4</mn></mfrac></msup><mo>.</mo><msup><mn>5</mn><mfrac><mi>r</mi><mn>8</mn></mfrac></msup></math></p><p>For rational terms.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>8</mn></mfrac><mo>=</mo><mi>k</mi><mo>;</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>r</mi><mo>&#8804;</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mn>8</mn><mi>k</mi><mo>&#8804;</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>k</mi><mo>&#8804;</mo><mfrac><mn>60</mn><mn>8</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>k</mi><mo>&#8804;</mo><mn>7</mn><mo>.</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>6</mn><mo>,</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>60</mn><mo>-</mo><mn>8</mn><mi>k</mi></mrow><mn>4</mn></mfrac></math> is always divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math> for all value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></p><p>Total rational terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>8</mn></math></p><p>Total terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>61</mn></math></p><p>irrational terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>53</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><mn>53</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>52</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>52</mn></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>26</mn></math>.</p>

</details>

---

### Q84. JEE Main 2021 (26 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The maximum value of the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>t</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>+</mo><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>10</mn></mfrac></msup><mi>t</mi></mfrac></mrow></mfenced><mn>10</mn></msup></math>where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>&#8712;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>1</mn></mrow></mfenced></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>!</mo></mrow><mrow><mn>3</mn><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>.</mo><mn>10</mn><mo>!</mo></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>.</mo><mn>10</mn><mo>!</mo></mrow><mrow><mn>3</mn><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mo>.</mo><mn>10</mn><mo>!</mo></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mi>t</mi><msup><mi>x</mi><mfenced><mrow><mn>1</mn><mo>/</mo><mn>5</mn></mrow></mfenced></msup></mrow></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced close="]" open="["><mfrac><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mn>1</mn><mn>10</mn></mfrac></msup><mi>t</mi></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mi>t</mi></mfenced><mrow><mn>10</mn><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup><msup><mfenced><mi>x</mi></mfenced><mfrac><mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></mfenced><mn>5</mn></mfrac></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfrac><mi>r</mi><mn>10</mn></mfrac></msup></math></p><p>For the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>t</mi></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mo>-</mo><mn>2</mn><mi>r</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>5</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>6</mn></msub><mo>=</mo><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mfenced><mrow><mi>x</mi><msqrt><mn>1</mn><mo>-</mo><mi>x</mi></msqrt></mrow></mfenced><mo>;</mo></math> for maximum</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>f</mi><mo>&#39;</mo></msup><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>&#38;</mo><msup><mi>f</mi><mrow><mo>&#39;</mo><mo>&#39;</mo></mrow></msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>&#60;</mo><mn>0</mn></math></p><p>so <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><msub><mfenced><mi>x</mi></mfenced><mrow><mi>m</mi><mi>a</mi><mi>x</mi><mo>.</mo></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mo>&#183;</mo><mfrac><mn>1</mn><msqrt><mn>3</mn></msqrt></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mo>.</mo><mn>10</mn><mo>!</mo></mrow><mrow><mn>3</mn><msqrt><mn>3</mn></msqrt><msup><mfenced><mrow><mn>5</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p>

</details>

---

### Q85. JEE Main 2020 (06 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If the constant term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msqrt><mi mathvariant="normal">x</mi></msqrt><mo>-</mo><mfrac><mi mathvariant="normal">k</mi><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>405</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mi mathvariant="normal">k</mi></mfenced></math> equals :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><mfrac><mrow><mo>-</mo><mi>k</mi></mrow><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>r</mi></msup><msup><mfenced><msqrt><mi>x</mi></msqrt></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>&#183;</mo></mrow><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mo>-</mo><mi>k</mi></mrow></mfenced><mi>r</mi></msup><mo>&#183;</mo><msup><mi>x</mi><mrow><mn>5</mn><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mn>2</mn></mfrac></mrow></msup></math></p><p>for constant term</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mn>2</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mrow><mn>3</mn><mo>=</mo></mrow></msub><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><mo>&#183;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>405</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>10</mn><mo>(</mo><mn>9</mn><mo>)</mo></mrow><mn>2</mn></mfrac><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>405</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>k</mi><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced close="|" open="|"><mi>k</mi></mfenced><mo>=</mo><mn>3</mn></math></p>

</details>

---

### Q86. JEE Main 2020 (05 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>6</mn></msup></math> in powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>,</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **120**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>6</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></math></p><p>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>1</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><mo>=</mo><mn>15</mn><mo>+</mo><mn>15</mn><mo>&#183;</mo><mn>6</mn><mo>+</mo><mn>15</mn><mo>=</mo><mn>120</mn></math>.</p>

</details>

---

### Q87. JEE Main 2020 (05 Sep Shift 1)

*Type:* `numerical` | *Level:* `2`

The natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>, for which the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the binomial expansion of  <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mi>x</mi><mi>m</mi></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>22</mn></msup></math> is 1540, is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **13**

**Detailed Solution:**

<p>The general term in the binomial expansion,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>22</mn></mmultiscripts><msup><mfenced><msup><mi mathvariant="normal">x</mi><mi mathvariant="normal">m</mi></msup></mfenced><mrow><mn>22</mn><mo>-</mo><mi mathvariant="normal">r</mi></mrow></msup><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn><mi>r</mi></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">T</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><msup><mi mathvariant="normal">x</mi><mrow><mi mathvariant="normal">m</mi><mo>(</mo><mn>22</mn><mo>-</mo><mi>r</mi><mo>)</mo><mo>-</mo><mn>2</mn><mi mathvariant="normal">r</mi></mrow></msup></math></p><p>For the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>&#160;</mo><mi>m</mi><mo>-</mo><mi>m</mi><mo>&#160;</mo><mi>r</mi><mo>-</mo><mn>2</mn><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>22</mn><mo>&#160;</mo><mi>m</mi><mo>-</mo><mn>1</mn><mo>=</mo><mi>r</mi><mo>(</mo><mi>m</mi><mo>+</mo><mn>2</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>22</mn><mi>m</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>22</mn><mi>m</mi><mo>+</mo><mn>44</mn><mo>-</mo><mn>45</mn></mrow><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>22</mn><mo>-</mo><mfrac><mrow><mn>3</mn><mo>.</mo><mn>3</mn><mo>.</mo><mn>5</mn></mrow><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>&#8658;</mo><mn>22</mn><mo>-</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>5</mn></mrow><mrow><mi>m</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mn>22</mn><mo>-</mo><mi>r</mi></mrow><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts></math></p><p>So possible values of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">m</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>13</mn><mo>,</mo><mn>43</mn></math>, but <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>22</mn></mmultiscripts><mo>=</mo><mn>1540</mn><mo>&#8658;</mo><mn>22</mn><mo>-</mo><mi>r</mi><mo>=</mo><mn>3</mn><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>13</mn></math></p>

</details>

---

### Q88. JEE Main 2020 (04 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If for some positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>, the coefficients of three consecutive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></msup></math> are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>:</mo><mn>10</mn><mo>:</mo><mn>14</mn></math>, then the largest coefficient in the expansion is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>462</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>330</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>792</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>252</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>462</mn></math>**

**Detailed Solution:**

<p>Let three consecutive terms are <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></math>
So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>10</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>14</mn></mfrac></math></p><p>Using property <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac></math>, we have</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mn>3</mn><mi>r</mi><mo>+</mo><mn>6</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>n</mi><mo>-</mo><mn>12</mn><mi>r</mi><mo>+</mo><mn>18</mn><mo>=</mo><mn>0</mn></math></p><p>Solving both equations, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math>
Hence, the greatest coefficient will be of middle term, which is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mrow><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>5</mn><none/><mprescripts/><none/><mn>11</mn></mmultiscripts><mo>=</mo><mn>462</mn></math></p>

</details>

---

### Q89. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mn>9</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>18</mn><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mn>9</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mfrac><mrow><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mi>x</mi></mrow></mfrac></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>9</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mrow><mn>9</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mi>r</mi></msup><msup><mi>x</mi><mrow><mn>18</mn><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup></math></p><p>For the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mn>7</mn></msub><msup><mo>=</mo><mn>9</mn></msup><msub><mi>C</mi><mn>6</mn></msub><msup><mfenced><mfrac><mn>3</mn><mn>2</mn></mfrac></mfenced><mn>3</mn></msup><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mn>6</mn></msup><msup><mo>=</mo><mn>9</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>7</mn></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn></mrow></mfrac><msup><mfenced><mfrac><mn>1</mn><mn>6</mn></mfrac></mfenced><mn>3</mn></msup><mo>=</mo><mfenced><mfrac><mn>7</mn><mn>18</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>k</mi><mo>=</mo><msub><mi>T</mi><mn>7</mn></msub><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mn>7</mn><mn>18</mn></mfrac><mo>&#8658;</mo><mn>18</mn><mi>k</mi><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q90. JEE Main 2020 (03 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the number of integral terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup></math> is exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>, then the least value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is

**Options:**

- **(A)** 264
- **(B)** 128
- **(C)** 256
- **(D)** 248

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 256**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup><mo>+</mo><msup><mn>5</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></msup></mrow></mfenced><mi>n</mi></msup></math></p><p>General term <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mfenced><msup><mn>3</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><msup><mn>5</mn><mfrac><mn>1</mn><mn>8</mn></mfrac></msup></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mn>3</mn><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac></msup><msup><mn>5</mn><mfrac><mi>r</mi><mn>8</mn></mfrac></msup></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mi>r</mi><mn>8</mn></mfrac></math> must be integer.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mn>2</mn></mfrac><mo>&#8712;</mo><mi>I</mi><mo>&#8658;</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mn>6</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>r</mi><mn>8</mn></mfrac><mo>&#8712;</mo><mi>I</mi><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mn>24</mn><mo>,</mo><mo>&#160;</mo><mn>32</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>For rational term common powers<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mn>8</mn><mo>,</mo><mo>&#160;</mo><mn>16</mn><mo>,</mo><mo>&#160;</mo><mn>24</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>Number of integral term<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>33</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>s</mi></msub><mo>=</mo><mi>a</mi><mo>+</mo><mfenced><mrow><mi>s</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>&#160;</mo><mo>&#8658;</mo><msub><mi>T</mi><mn>33</mn></msub><mo>=</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mn>33</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>8</mn><mo>=</mo><mn>256</mn></math>.</p><p>Value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>256</mn></math>.</p><p>We can cross check to verify answer.</p>

</details>

---

### Q91. JEE Main 2020 (02 Sep Shift 2)

*Type:* `numerical` | *Level:* `2`

For a positive integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>,</mo><mo>&#160;</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mi>n</mi></msup></math> is expanded in increasing powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>. If three consecutive coefficients in this expansion are in the ratio, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mo>&#160;</mo><mn>5</mn><mo>:</mo><mo>&#160;</mo><mn>12</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **118**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>:</mo><mmultiscripts><mi mathvariant="normal">C</mi><mi mathvariant="normal">r</mi><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>:</mo><mmultiscripts><mi mathvariant="normal">C</mi><mrow><mi mathvariant="normal">r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi mathvariant="normal">n</mi></mmultiscripts><mo>=</mo><mn>2</mn><mo>:</mo><mn>5</mn><mo>:</mo><mn>12</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mi>r</mi></mfrac><mo>=</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>12</mn><mn>5</mn></mfrac></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>7</mn><mi>r</mi><mo>+</mo><mn>2</mn><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mi>n</mi><mo>-</mo><mn>17</mn><mi>r</mi><mo>-</mo><mn>12</mn><mo>=</mo><mn>0</mn></math> </p><p>On solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>118</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>34</mn></math></p>

</details>

---

### Q92. JEE Main 2020 (02 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn><mo>,</mo><mi>&#946;</mi><mo>&#62;</mo><mn>0</mn></math> be such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup><mo>=</mo><mn>4</mn></math>. If the maximum value of the term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>9</mn></mfrac></msup><mo>+</mo><mi>&#946;</mi><msup><mi>x</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></msup></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mi>k</mi></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>352</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>84</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>176</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>336</mn></math>**

**Detailed Solution:**

<p> <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mfenced><mrow><mi>&#945;</mi><msup><mi>x</mi><mfrac><mn>1</mn><mn>9</mn></mfrac></msup></mrow></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mrow><mi>&#946;</mi><msup><mi>x</mi><mrow><mo>-</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></mrow></msup></mrow></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mi>&#945;</mi><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>&#946;</mi><mi>r</mi></msup><msup><mfenced><mi>x</mi></mfenced><mrow><mfrac><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow><mn>9</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>6</mn></mfrac></mrow></msup></math></p><p>Term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">x</mi><mo>&#160;</mo><mo>&#8658;</mo></math>Power of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow><mn>9</mn></mfrac><mo>-</mo><mfrac><mi>r</mi><mn>6</mn></mfrac><mo>=</mo><mn>0</mn><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">T</mi><mn>5</mn></msub><mo>=</mo><mmultiscripts><mi mathvariant="normal">C</mi><mn>4</mn><none></none><mprescripts></mprescripts><none></none><mn>10</mn></mmultiscripts><msup><mi>&#945;</mi><mn>6</mn></msup><msup><mi>&#946;</mi><mn>4</mn></msup></math></p><p>Now Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#945;</mi><mn>3</mn></msup><mo>,</mo><msup><mi>&#946;</mi><mn>2</mn></msup></math> are two numbers. Clearly both are positive.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>M</mi><mo>.</mo><mo>&#8805;</mo><mi>G</mi><mo>.</mo><mi>M</mi><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><mrow><msup><mi>&#945;</mi><mn>3</mn></msup><mo>+</mo><msup><mi>&#946;</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac><mo>&#8805;</mo><msup><mfenced><mrow><msup><mi>&#945;</mi><mn>3</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>&#945;</mi><mn>3</mn></msup><msup><mi>&#946;</mi><mn>2</mn></msup><mo>&#8804;</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msup><mi>&#945;</mi><mn>6</mn></msup><msup><mi>&#946;</mi><mn>4</mn></msup><mo>&#8804;</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfrac><msub><mi>T</mi><mn>5</mn></msub><mrow><msup><mrow/><mn>10</mn></msup><msub><mi mathvariant="normal">C</mi><mn>4</mn></msub></mrow></mfrac><mo>&#8804;</mo><mn>16</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>T</mi><mn>5</mn></msub><mo>&#8804;</mo><mn>16</mn><msup><mo>.</mo><mn>10</mn></msup><msub><mi mathvariant="normal">C</mi><mn>4</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><msub><mi>T</mi><mrow><mn>5</mn><mi>max</mi></mrow></msub><mo>=</mo><mn>16</mn><msup><mo>&#215;</mo><mn>10</mn></msup><msub><mi mathvariant="normal">C</mi><mn>4</mn></msub><mo>=</mo><mn>10</mn><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>10</mn><mi>k</mi><mo>=</mo><mn>3360</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mi>k</mi><mo>=</mo><mn>336</mn></math></p>

</details>

---

### Q93. JEE Main 2020 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

In the expansion of <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mrow><mrow><mi mathvariant="normal">cos</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi><mrow><mrow><mi mathvariant="normal">sin</mi></mrow><mo>&#8289;</mo><mrow><mi>&#952;</mi></mrow></mrow></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>16</mn></mrow></msup><mo>,</mo></math> if <math><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is the least value of the term independent of <math><mi>x</mi></math> when <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>&#8804;</mo><mi>&#952;</mi><mo>&#8804;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>4</mn></mrow></mfrac></math> and <math><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub></math> is the least value of the term independent of <math><mi>x</mi></math> when <math><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>16</mn></mrow></mfrac><mo>&#8804;</mo><mi>&#952;</mi><mo>&#8804;</mo><mfrac><mrow><mi>&#960;</mi></mrow><mrow><mn>8</mn></mrow></mfrac><mo>,</mo></math> then the ratio <math><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>:</mo><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub></math> is equal to:

**Options:**

- **(A)** <math><mn>1</mn><mo>:</mo><mn>8</mn></math>
- **(B)** <math><mn>16</mn><mo>:</mo><mn>1</mn></math>
- **(C)** <math><mn>8</mn><mo>:</mo><mn>1</mn></math>
- **(D)** <math><mn>1</mn><mo>:</mo><mn>16</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>16</mn><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mi>x</mi><mrow><mi>cos</mi><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfrac></mfenced><mrow><mn>16</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mi>x</mi><mi>sin</mi><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfrac></mfenced><mi>r</mi></msup></math>
for <math><mi>r</mi><mo>=</mo><mn>8</mn></math> term is free from <math><mi>&#39;</mi><mi>x</mi><mi>&#39;</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>9</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><mfrac><mn>1</mn><mrow><msup><mi>sin</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>&#952;</mi><msup><mi>cos</mi><mn>8</mn></msup><mo>&#8289;</mo><mi>&#952;</mi></mrow></mfrac></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>9</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><mfrac><msup><mn>2</mn><mn>8</mn></msup><msup><mfenced separators="|"><mrow><mi>sin</mi><mo>&#8289;</mo><mn>2</mn><mi>&#952;</mi></mrow></mfenced><mn>8</mn></msup></mfrac></math>
In <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mi>&#960;</mi><mn>8</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></mrow></mfenced><mo>,</mo><msub><mi>l</mi><mn>1</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><msup><mn>2</mn><mn>8</mn></msup></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> Minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>1</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi mathvariant="normal">&#960;</mi><mn>4</mn></mfrac></math>)
In <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>&#8712;</mo><mfenced close="]" open="[" separators="|"><mrow><mfrac><mi>&#960;</mi><mn>16</mn></mfrac><mo>,</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></mrow></mfenced><mo>,</mo><msub><mi>l</mi><mn>2</mn></msub><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><mfrac><msup><mn>2</mn><mn>8</mn></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac></mfenced><mn>8</mn></msup></mfrac><mo>=</mo><mmultiscripts><mi>C</mi><mn>8</mn><none></none><mprescripts></mprescripts><none></none><mn>16</mn></mmultiscripts><mo>&#183;</mo><msup><mn>2</mn><mn>8</mn></msup><mo>&#183;</mo><msup><mn>2</mn><mn>4</mn></msup></math> (<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math>Minimum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>l</mi><mn>2</mn></msub></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#952;</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>8</mn></mfrac></math>)
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>l</mi><mn>2</mn></msub><msub><mi>l</mi><mn>1</mn></msub></mfrac><mo>=</mo><mfrac><mrow><mmultiscripts><mi>C</mi><mn>8</mn><none/><mprescripts/><none/><mn>16</mn></mmultiscripts><mo>.</mo><msup><mn>2</mn><mn>8</mn></msup><msup><mn>2</mn><mn>4</mn></msup></mrow><mrow><mmultiscripts><mi>C</mi><mn>8</mn><none/><mprescripts/><none/><mn>16</mn></mmultiscripts><mo>.</mo><msup><mn>2</mn><mn>8</mn></msup></mrow></mfrac><mo>=</mo><mn>16</mn></math>

</details>

---

### Q94. JEE Main 2020 (08 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If <math><mi>&#945;</mi></math> and <math><mi>&#946;</mi></math>, be the coefficients of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math>, respectively in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup></math>, then

**Options:**

- **(A)** <math><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mn>60</mn></math>
- **(B)** <math><mi>α</mi><mo>+</mo><mi>β</mi><mo>=</mo><mo>-</mo><mn>30</mn></math>
- **(C)** <math><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mn>60</mn></math>
- **(D)** <math><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mo>-</mo><mn>132</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mo>-</mo><mn>132</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><mo>=</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><msub><mi>C</mi><mn>0</mn></msub><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>4</mn></msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><msub><mi>C</mi><mn>4</mn></msub><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msub><mi>C</mi><mn>6</mn></msub><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></math></p><p><math><mo>=</mo><mn>2</mn><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup><mo>+</mo><mn>15</mn><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup></mrow></mfenced><mo>+</mo><mn>15</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>-</mo><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn><mo>+</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup></mrow></mfenced></mrow></mfenced></math></p><p><math><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>32</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn></mrow></msup><mo>-</mo><mn>48</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>4</mn></mrow></msup><mo>+</mo><mn>18</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Now given that <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>&#946;</mi></math> are the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msup><mi>x</mi><mn>2</mn></msup></math> respectively, hence</p><p><math><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>96</mn></math> and <math><mi>&#946;</mi><mo>=</mo><mn>36</mn></math></p><p><math><mo>&#8756;</mo><mi mathvariant="normal"></mi><mi>&#945;</mi><mo>-</mo><mi>&#946;</mi><mo>=</mo><mo>-</mo><mn>132</mn></math></p>

</details>

---

### Q95. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>7</mn></mrow></msup></math> in the expression <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>10</mn></msup><mo>+</mo><mi>x</mi><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>9</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>8</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>x</mi><mn>10</mn></msup></math>, is

**Options:**

- **(A)** <math><mn>210</mn></math>
- **(B)** <math><mn>330</mn></math>
- **(C)** <math><mn>120</mn></math>
- **(D)** <math><mn>420</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>330</mn></math>**

**Detailed Solution:**

<p>As the given series is in G.P., so its sum is</p><p><math><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow></mfrac></math></p><p><math><mfrac><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>11</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup><mo>&#215;</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow></mfrac></mrow></mfrac><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>11</mn></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>11</mn></mrow></msup></math></p><p>Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>7</mn></mrow></msup></math>, is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mn>11</mn><msub><mi>C</mi><mn>7</mn></msub></msub><mo>=</mo><msub><mn>11</mn><msub><mi>C</mi><mn>4</mn></msub></msub><mo>=</mo><mn>330</mn></math></p>

</details>

---

### Q96. JEE Main 2019 (12 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The term independent of <math><mi>x</mi></math> in the expansion of <math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>60</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow><mrow><mn>81</mn></mrow></mfrac></mrow></mfenced><mo>.</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math> is equal to

**Options:**

- **(A)** <math><mo>-</mo><mn>72</mn></math>
- **(B)** <math><mn>36</mn></math>
- **(C)** <math><mo>-</mo><mn>108</mn></math>
- **(D)** <math><mo>-</mo><mn>36</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mo>-</mo><mn>36</mn></math>**

**Detailed Solution:**

To find the coefficient of term independent of <math><mi>x</mi></math> in given expression, first let&#39;s find constant term and coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup></math> in the expansion of <math><mi mathvariant="normal">&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math>
<math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mrow><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>6</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#215;</mo><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mfrac><mrow><mn>3</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup><mi>&#160;</mi></math>
<math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mrow><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><mi>&#160;</mi><msup><mrow><mn>2</mn></mrow><mrow><mn>6</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>&#215;</mo><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup><mi>&#160;</mi><mo>&#215;</mo><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>12</mn><mo>-</mo><mn>4</mn><mi>r</mi></mrow></msup></math>
For constant term: <math><mi>&#160;</mi><mi>r</mi><mo>=</mo><mn>3</mn></math> , hence constant term = <math><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mi>&#160;</mi><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msup></math>
For coefficient of <math><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup><mi>&#160;</mi><mo>:</mo><mi>&#160;</mi><mi>r</mi><mo>=</mo><mn>5</mn></math> , hence coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup><msup><mrow><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>1</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup></math>
Given expression can be written as
<math><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>60</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>8</mn></mrow></msup></mrow><mrow><mn>81</mn></mrow></mfrac></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>&#160;</mi><mi>&#160;</mi><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>1</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>8</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></math>
Hence, coefficient of term independent of <math><mi mathvariant="normal">x</mi></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>60</mn></mrow></mfrac><msup><mrow><mo>&#215;</mo><mi mathvariant="normal">&#160;</mi></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>81</mn></mrow></mfrac><msup><mrow><mo>&#215;</mo></mrow><mrow><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">&#160;</mi><mn>6</mn></mrow></msup><msub><mrow><mi mathvariant="normal">C</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>&#215;</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>1</mn></mrow></msup><mo>&#215;</mo><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mn>5</mn></mrow></msup></math>
<math><mo>=</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mn>72</mn><mo>+</mo><mn>36</mn><mo>=</mo><mi mathvariant="normal">&#160;</mi><mo>-</mo><mn>36</mn></math>

</details>

---

### Q97. JEE Main 2019 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>18</mn></mrow></msup></math> in the product <math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup><mi>&#160;</mi></math> is

**Options:**

- **(A)** <math><mn>84</mn></math>
- **(B)** <math><mo>-</mo><mn>84</mn></math>
- **(C)** <math><mo>-</mo><mn>126</mn></math>
- **(D)** <math><mn>126</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>84</mn></math>**

**Detailed Solution:**

<math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
So, Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>18</mn></mrow></msup></math> in <math><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
<math><mo>=</mo></math> Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>18</mn></mrow></msup></math> in <math><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></msup></math>
<math><mo>=</mo><mi>&#160;</mi></math>Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>18</mn></mrow></msup></math> in <math><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced><mfenced close="]" open="[" separators="|"><mrow><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>0</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></mmultiscripts><mo>+</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></mmultiscripts><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced><mo>+</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo></mrow><mprescripts></mprescripts><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></mmultiscripts></mrow></mfenced></math>
<math><mo>=</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>6</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></mmultiscripts><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup><mo>=</mo><mmultiscripts><mrow><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub></mrow><mprescripts></mprescripts><mrow><mi>&#160;</mi></mrow><mrow><mn>9</mn></mrow></mmultiscripts><mo>=</mo><mfrac><mrow><mn>9.8</mn><mo>.</mo><mn>7</mn></mrow><mrow><mn>1.2</mn><mo>.</mo><mn>3</mn></mrow></mfrac><mo>=</mo><mn>84</mn></math>

</details>

---

### Q98. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The smallest natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> , such that the coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>23</mn><none/><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts></math> , is

**Options:**

- **(A)** <math><mn>58</mn></math>
- **(B)** <math><mn>38</mn></math>
- **(C)** <math><mn>35</mn></math>
- **(D)** <math><mn>23</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>38</mn></math>**

**Detailed Solution:**

<p>In the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mrow></mfenced><mi>n</mi></msup></math> the general term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><msub><mi>C</mi><mi>r</mi></msub><mprescripts></mprescripts><mi>&#160;</mi><mi>n</mi></mmultiscripts><msup><mfenced separators="|"><msup><mi>x</mi><mn>2</mn></msup></mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><msup><mi>x</mi><mn>3</mn></msup></mfrac></mfenced><mi>r</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mmultiscripts><msub><mi>C</mi><mi>r</mi></msub><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn><mi>r</mi><mo>-</mo><mn>3</mn><mi>r</mi></mrow></msup><mo>=</mo><mmultiscripts><msub><mi>C</mi><mi>r</mi></msub><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts><msup><mi>x</mi><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>5</mn><mi>r</mi></mrow></msup></math></p><p>For coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi><mo>-</mo><mn>5</mn><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></math></p><p>So, we have the coefficient as <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><msub><mi>C</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></msub><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts></math></p><p>Using, the given value and <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow><none/><mprescripts/><none/><mi>n</mi></mmultiscripts></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><msub><mi>C</mi><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac></msub><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts><mo>=</mo><mmultiscripts><mrow><msub><mi>C</mi><mn>23</mn></msub><mo>=</mo><mmultiscripts><msub><mi>C</mi><mrow><mi>n</mi><mo>-</mo><mn>23</mn></mrow></msub><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts></mrow><mprescripts/><mi>&#160;</mi><mi>n</mi></mmultiscripts></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mn>23</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>58</mn></math> and if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>5</mn></mfrac><mo>=</mo><mi>n</mi><mo>-</mo><mn>23</mn><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>38</mn></math></p><p>Thus, the minimum value of <math><mi>&#39;</mi><mi>n</mi><mi>&#39;</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>38</mn><mo>.</mo></math></p>

</details>

---

### Q99. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficients of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math>, are both zero, in the expansion of the expression <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mn>15</mn></msup></math>, in powers of <math><mi>x</mi></math> , then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>28</mn><mo>,</mo><mn>315</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>21</mn><mo>,</mo><mn>714</mn></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>28</mn><mo>,</mo><mn>861</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mo>-</mo><mn>54</mn><mo>,</mo><mn>315</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>28</mn><mo>,</mo><mn>315</mn></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>3</mn><mi>x</mi></mrow></mfenced><mn>15</mn></msup><mo>=</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mmultiscripts><mi>C</mi><mn>0</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><msup><mo>-</mo><mn>15</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mi>&#160;</mi><mn>3</mn><mi>x</mi><mi>&#160;</mi><msup><mo>+</mo><mrow><mi>&#160;</mi><mn>15</mn></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><mi>&#160;</mi><msup><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mn>2</mn></msup><msup><mo>-</mo><mn>15</mn></msup><msub><mi>C</mi><mn>3</mn></msub><msup><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><msup><mo>-</mo><mn>15</mn></msup><msub><mi>C</mi><mn>15</mn></msub><msup><mfenced separators="|"><mrow><mn>3</mn><mi>x</mi></mrow></mfenced><mn>15</mn></msup></mrow></mfenced></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi></math> Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> is: <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mi>&#160;</mi><mi>b</mi><mo>.</mo></mrow><mn>15</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mo>-</mo><mn>3</mn><mo>.</mo><msup><mi>a</mi><mn>15</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><msup><mn>3</mn><mrow><mn>2</mn><mo>.</mo></mrow></msup><msup><mo>.</mo><mn>15</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>=</mo><mn>0</mn></math></p><p>(Given)
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>b</mi><mo>-</mo><mn>45</mn><mi>a</mi><mo>+</mo><mn>945</mn><mo>=</mo><mn>0</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup></math> is:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mi>b</mi><mo>.</mo><mn>3</mn><msup><mo>.</mo><mn>15</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mo>+</mo><mn>9</mn><mi>a</mi><msup><mo>.</mo><mn>15</mn></msup><msub><mi>C</mi><mn>2</mn></msub><mo>-</mo><mn>27</mn><msup><mo>.</mo><mn>15</mn></msup><msub><mi>C</mi><mn>3</mn></msub><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mo>-</mo><mn>45</mn><mi>b</mi><mo>+</mo><mn>9</mn><mi>a</mi><mo>&#215;</mo><mfrac><mn>15</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>14</mn><mn>1</mn></mfrac><mo>-</mo><mn>27</mn><mo>&#215;</mo><mfrac><mn>15</mn><mn>3</mn></mfrac><mo>&#215;</mo><mfrac><mn>14</mn><mn>2</mn></mfrac><mo>&#215;</mo><mfrac><mn>13</mn><mn>1</mn></mfrac><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mo>-</mo><mi>b</mi><mo>+</mo><mn>21</mn><mi>a</mi><mo>-</mo><mn>273</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mi>b</mi><mo>-</mo><mn>21</mn><mi>a</mi><mo>+</mo><mn>273</mn><mo>=</mo><mn>0</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>ii</mi></mfenced></math></p><p>From <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi mathvariant="normal">i</mi></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>ii</mi></mfenced></math></p><p><math><mi>a</mi><mo>=</mo><mn>28</mn></math> and <math><mi>b</mi><mo>=</mo><mn>315</mn></math></p>

</details>

---

### Q100. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If some three consecutive coefficients in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>n</mi></msup></math> in powers of <math><mi>x</mi></math> are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>:</mo><mn>15</mn><mo>:</mo><mn>70</mn><mo>,</mo></math> then the average of these three coefficients is:

**Options:**

- **(A)** <math><mn>227</mn></math>
- **(B)** <math><mn>964</mn></math>
- **(C)** <math><mn>625</mn></math>
- **(D)** <math><mn>232</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>232</mn></math>**

**Detailed Solution:**

<p>From the given condition</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mo>:</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>:</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><mo>:</mo><mn>15</mn><mo>:</mo><mn>70</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub></mrow><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>15</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>70</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#160;</mi><mstyle displaystyle="true"><mfenced><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mi>r</mi><mo>!</mo></mrow></mfrac></mfenced></mstyle></mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle></mfenced></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>15</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#160;</mi><mstyle displaystyle="true"><mfenced><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced></mstyle></mrow><mfenced><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mstyle></mfenced></mfrac><mo>=</mo><mfrac><mn>15</mn><mn>70</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mi>r</mi><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>15</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mi>r</mi><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mi>r</mi><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>15</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>&#183;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>&#160;</mi><mstyle displaystyle="true"><mi>r</mi><mo>+</mo><mn>1</mn></mstyle></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>15</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>&#160;</mi><mstyle displaystyle="true"><mi>r</mi><mo>+</mo><mn>2</mn></mstyle></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>14</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mn>17</mn><mi>r</mi><mo>=</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>15</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>17</mn><mi>r</mi><mo>=</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>31</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>31</mn><mo>=</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>15</mn><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>16</mn></math> and <math><mi>r</mi><mo>=</mo><mn>1</mn></math></p><p>Hence, average <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>&#160;</mi><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>+</mo><mi>n</mi></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>&#160;</mi><mn>16</mn></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mo>+</mo><mn>16</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>+</mo><mn>16</mn></msup><msub><mi>C</mi><mn>3</mn></msub></mrow><mn>3</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>232</mn><mo>.</mo></math></p>

</details>

---

### Q101. JEE Main 2019 (09 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If the fourth term in the Binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><msup><mi>x</mi><mrow><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mn>8</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>6</mn></msup><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>&#215;</mo><msup><mn>8</mn><mn>7</mn></msup><mo>,</mo></math> then a value of <math><mi>x</mi></math> is

**Options:**

- **(A)** <math><msup><mrow><mn>8</mn></mrow><mrow><mo>–</mo><mn>2</mn></mrow></msup></math>
- **(B)** <math><mn>8</mn></math>
- **(C)** <math><msup><mrow><mn>8</mn></mrow><mrow><mn>3</mn></mrow></msup></math>
- **(D)** <math><msup><mrow><mn>8</mn></mrow><mrow><mn>2</mn></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><msup><mrow><mn>8</mn></mrow><mrow><mn>2</mn></mrow></msup></math>**

**Detailed Solution:**

<p>The general term in the binomial expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>b</mi><mi>r</mi></msup><mo>.</mo></math></p><p>Given, the fourth term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mfrac><mn>2</mn><mi>x</mi></mfrac><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>6</mn></msup></math> is </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>4</mn></msub><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>8</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mmultiscripts><mi>C</mi><mn>3</mn><none/><mprescripts/><none/><mn>6</mn></mmultiscripts><msup><mfenced separators="|"><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>8</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>6</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow></mfrac><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mfenced><msup><mn>2</mn><mn>3</mn></msup></mfenced><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>3</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow></mfrac></mfenced><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>2</mn><mn>21</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mn>20</mn></mfenced><msup><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mn>3</mn></msup><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>3</mn></msup><mo>=</mo><mn>20</mn><mo>&#215;</mo><msup><mn>2</mn><mn>21</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced open="[" close="]"><mrow><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced></mrow></mfenced><mn>3</mn></msup><mo>=</mo><msup><mfenced><msup><mn>2</mn><mn>7</mn></msup></mfenced><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mn>2</mn><mi>x</mi></mfrac></mfenced><mfenced><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mo>=</mo><msup><mn>2</mn><mn>7</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mfrac><mn>1</mn><mi>x</mi></mfrac></mfenced><mfenced><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></msup></mfenced><mo>=</mo><msup><mn>2</mn><mn>6</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><msup><mn>8</mn><mn>2</mn></msup></math></p><p>Taking <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi></math> both side to the base <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>8</mn></msub><mfenced><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi><mo>-</mo><mn>1</mn></mrow></msup></mfenced><mo>=</mo><msub><mi>log</mi><mn>8</mn></msub><mfenced><msup><mn>8</mn><mn>2</mn></msup></mfenced></math></p><p>Using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><msup><mi>m</mi><mi>n</mi></msup><mo>=</mo><mi>n</mi><msub><mi>log</mi><mi>a</mi></msub><mi>m</mi><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>(</mo><msub><mi>log</mi><mn>8</mn></msub><mrow><mi>x</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mfenced separators="|"><mrow><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><mi>t</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mi>t</mi></mfenced><mo>=</mo><mn>2</mn></math>                (Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mn>8</mn></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>t</mi></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>t</mi><mn>2</mn></msup><mo>-</mo><mi>t</mi><mo>-</mo><mn>2</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>t</mi><mo>=</mo><mn>2</mn></math> or <math><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>8</mn></msub><mi>x</mi><mo>=</mo><mn>2</mn></math> or <math><mo>-</mo><mn>1</mn></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi><mo>=</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>a</mi><mi>b</mi></msup><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mn>8</mn><mn>2</mn></msup></math> or <math><msup><mrow><mn>8</mn></mrow><mrow><mo>-</mo><mn>1</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>64</mn><mi>&#160;</mi></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>.</mo></math></p>

</details>

---

### Q102. JEE Main 2019 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the fourth term in the binomial expansion of <math><msup><mrow><mfenced separators="|"><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfrac></mrow></msup></msqrt><mo>+</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math> is equal to <math><mn>200</mn><mo>,</mo></math> and <math><mi>x</mi><mo>&#62;</mo><mn>1</mn><mo>,</mo></math> then the value of <math><mi>x</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(B)** <math><msup><mrow><mn>10</mn></mrow><mrow><mn>4</mn></mrow></msup></math>
- **(C)** <math><msup><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></msup></math>
- **(D)** <math><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>10</mn></math>**

**Detailed Solution:**

General term for the given binomial is 
<math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><msup><mrow><mfenced separators="|"><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfrac></mrow></msup></msqrt></mrow></mfenced></mrow><mrow><mn>6</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup></math>  
Given <math><msub><mrow><mi>T</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><mn>200</mn><mo>,</mo></math> putting <math><mi>r</mi><mo>=</mo><mn>3</mn></math>  
<math><mo>⇒</mo><msub><mrow><mi>T</mi></mrow><mrow><mn>4</mn></mrow></msub><mo>=</mo><msup><mrow><mtext> </mtext></mrow><mrow><mn>6</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>3</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfrac></mrow></msup></msqrt></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>12</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>3</mn></mrow></msup><mo>=</mo><mn>200</mn></math>  
<math><mo>⇒</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup><mo>⋅</mo><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup></mrow></mfenced><mo>=</mo><mn>10</mn></math>  
<math><mo>⇒</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></msup><mo>=</mo><mn>10</mn></math>  
<math><mo>⇒</mo><mfenced separators="|"><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></mrow></mfenced><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">g</mi></mrow><mrow><mn>10</mn></mrow></msub><mi>x</mi><mo>=</mo><mn>1</mn></math>  
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>10</mn><mo>,</mo><msup><mrow><mn>10</mn></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup></math>  
<math><mo>⇒</mo><mi>x</mi><mo>=</mo><mn>10</mn></math> <math><mo>(</mo></math> as <math><mi>x</mi><mo>&gt;</mo><mn>1</mn><mo>)</mo></math>

</details>

---

### Q103. JEE Main 2019 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the co-efficient of all even degree terms in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced><mn>6</mn></msup><msup><mrow><mo>+</mo><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced></mrow><mn>6</mn></msup><mo>,</mo><mo>&#160;</mo><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>1</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mn>2</mn><mn>6</mn></math>
- **(B)** <math><mn>32</mn></math>
- **(C)** <math><mn>24</mn></math>
- **(D)** <math><mn>29</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>24</mn></math>**

**Detailed Solution:**

<p><math><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>+</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mi>x</mi><mo>-</mo><msqrt><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mrow></mrow><mn>6</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mi>&#160;</mi><msup><mi>x</mi><mn>6</mn></msup><msup><mrow><mi>&#160;</mi><mo>+</mo></mrow><mrow><mi>&#160;</mi><mn>6</mn></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mi>x</mi><mn>4</mn></msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><msup><mrow><mo>+</mo><mi>&#160;</mi></mrow><mn>6</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mi>&#160;</mi><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mrow><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi></mrow><mn>6</mn></msup><msub><mi>C</mi><mn>6</mn></msub><msup><mrow><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>3</mn></msup></mrow></mfenced><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mrow></mrow><mn>6</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mi>&#160;</mi><msup><mi>x</mi><mn>6</mn></msup><msup><mrow><mi>&#160;</mi><mo>+</mo></mrow><mrow><mi>&#160;</mi><mn>6</mn></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>7</mn></msup><mo>-</mo><msup><mi>x</mi><mn>4</mn></msup></mrow></mfenced><msup><mrow><mo>+</mo><mi>&#160;</mi></mrow><mn>6</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mi>&#160;</mi><msup><mi>x</mi><mn>2</mn></msup><mfenced separators="|"><mrow><msup><mi>x</mi><mn>6</mn></msup><mo>-</mo><mn>2</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>6</mn></msub><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mi>x</mi><mn>9</mn></msup><mo>-</mo><mn>3</mn><msup><mi>x</mi><mn>6</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mi>&#160;</mi></math></p><p><math><mo>&#8756;</mo><mi>&#160;</mi></math> Sum of the coefficient of even power of <math><mi>x</mi><mi>&#160;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced><mrow><msup><mrow/><mn>6</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>-</mo><mn>6</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mo>-</mo><mn>3</mn><msup><mo>-</mo><mn>6</mn></msup><msub><mi>C</mi><mn>6</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>15</mn><mo>+</mo><mn>15</mn><mo>+</mo><mn>15</mn><mo>-</mo><mn>3</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>24</mn></math></p><p> </p>

</details>

---

### Q104. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The total number of irrational terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mn>7</mn><mfrac><mn>1</mn><mn>5</mn></mfrac></msup><mo>-</mo><msup><mn>3</mn><mfrac><mn>1</mn><mn>10</mn></mfrac></msup></mrow></mfenced><mn>60</mn></msup></math> is

**Options:**

- **(A)** <math><mn>48</mn></math>
- **(B)** <math><mn>55</mn></math>
- **(C)** <math><mn>54</mn></math>
- **(D)** <math><mn>49</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>54</mn></math>**

**Detailed Solution:**

<p>General term is <math><msup><mrow><mi>&#160;</mi></mrow><mrow><mn>60</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mn>7</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>60</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><msup><mrow><mn>3</mn></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>10</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup></math></p><p>We will get rational term when <math><mi>r</mi></math> is multiple of <math><mn>10</mn></math> and <math><mn>60</mn><mo>-</mo><mi>r</mi></math> is multiple of <math><mn>5</mn></math>.</p><p><math><mo>&#8756;</mo><mi>r</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>&#160;</mi><mn>10</mn><mo>,</mo><mi>&#160;</mi><mn>20</mn><mo>,</mo><mi>&#160;</mi><mn>30</mn><mo>,</mo><mi>&#160;</mi><mn>40</mn><mi>&#160;</mi><mo>,</mo><mn>50</mn><mo>,</mo><mi>&#160;</mi><mn>60</mn></math></p><p><math><mo>&#8756;</mo></math>Number of irrational term <math><mo>=</mo></math> Total terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo></math> Number of rational terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>60</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>7</mn><mo>=</mo><mn>54</mn></math>.</p>

</details>

---

### Q105. JEE Main 2019 (12 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

A ratio of the <math><msup><mrow><mn>5</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term from the beginning to the <math><msup><mrow><mn>5</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term from the end in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mfenced separators="|"><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup></math> is

**Options:**

- **(A)** <math><mn>1</mn><mo>:</mo><mn>4</mn><msup><mrow><mfenced separators="|"><mrow><mn>16</mn></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mfenced separators="|"><mn>36</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>:</mo><mn>1</mn></math>
- **(C)** <math><mn>2</mn><msup><mrow><mfenced separators="|"><mrow><mn>36</mn></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>:</mo><mn>1</mn></math>
- **(D)** <math><mn>1</mn><mo>:</mo><mn>2</mn><msup><mrow><mfenced separators="|"><mrow><mn>6</mn></mrow></mfenced></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><msup><mfenced separators="|"><mn>36</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>:</mo><mn>1</mn></math>**

**Detailed Solution:**

<p>Total number of terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mfenced separators="|"><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup><mo>=</mo><mn>10</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>11</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>5</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term from end <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>-</mo><mn>5</mn><mo>+</mo><mn>1</mn><mo>=</mo><msup><mn>7</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> from beginning.</p><p>We need to find a ratio of the <math><msup><mrow><mn>5</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term from the beginning to the <math><msup><mrow><mn>5</mn></mrow><mrow><mi mathvariant="normal">t</mi><mi mathvariant="normal">h</mi></mrow></msup></math> term from the end (i.e. <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term from beginning) in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mfenced separators="|"><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>10</mn></msup><mo>=</mo><mfrac><msub><mi>T</mi><mn>5</mn></msub><msub><mi>T</mi><mn>7</mn></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mrow/><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mfenced separators="|"><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfenced><mrow><mn>10</mn><mo>-</mo><mn>4</mn></mrow></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mfenced><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mfenced><mn>4</mn></msup></mrow><mrow><msup><mrow/><mn>10</mn></msup><msub><mi>C</mi><mn>6</mn></msub><msup><mfenced separators="|"><msup><mn>2</mn><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mfenced><mrow><mn>10</mn><mo>-</mo><mn>6</mn></mrow></msup><msup><mfenced separators="|"><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mfenced><mn>3</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mfenced><mn>6</mn></msup></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mo>=</mo><mi>n</mi></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mi>a</mi></mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced><mi>b</mi></mfenced><mi>r</mi></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mfenced><mrow><mn>10</mn><mo>!</mo></mrow></mfenced><mrow><mfenced><mrow><mn>4</mn><mo>!</mo></mrow></mfenced><mfenced><mrow><mn>6</mn><mo>!</mo></mrow></mfenced></mrow></mfrac><mo>&#215;</mo><msup><mfenced><mn>2</mn></mfenced><mn>2</mn></msup><mo>&#215;</mo><mfrac><mn>1</mn><mrow><mfenced><msup><mn>2</mn><mn>4</mn></msup></mfenced><mstyle displaystyle="true"><msup><mstyle displaystyle="true"><mfenced><mn>3</mn></mfenced></mstyle><mfrac><mn>4</mn><mn>3</mn></mfrac></msup></mstyle></mrow></mfrac></mstyle><mrow><mfrac><mfenced><mrow><mn>10</mn><mo>!</mo></mrow></mfenced><mrow><mfenced><mrow><mn>6</mn><mo>!</mo></mrow></mfenced><mfenced><mrow><mn>4</mn><mo>!</mo></mrow></mfenced></mrow></mfrac><mo>&#215;</mo><msup><mfenced><mn>2</mn></mfenced><mstyle displaystyle="true"><mfrac><mn>4</mn><mn>3</mn></mfrac></mstyle></msup><mo>&#215;</mo><mfrac><mn>1</mn><mrow><mfenced><msup><mn>2</mn><mn>6</mn></msup></mfenced><mstyle displaystyle="true"><msup><mfenced><mn>3</mn></mfenced><mn>2</mn></msup></mstyle></mrow></mfrac></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><msup><mfenced separators="|"><mn>36</mn></mfenced><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>:</mo><mn>1</mn></math></p>

</details>

---

### Q106. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let $(x+10)^{50}+(x-10)^{50}=\mathrm{a}_{0}+\mathrm{a}_{1} x+\mathrm{a}_{2} x^{2}+\ldots .+\mathrm{a}_{50} x^{50}$,

for all $x \in \mathbf{R} ;$ then $\frac{\mathrm{a}_{2}}{\mathrm{a}_{0}}$ is equal to :

**Options:**

- **(A)** 12.5
- **(B)** 12
- **(C)** 12.25
- **(D)** 12.75

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12.25**

**Detailed Solution:**

$(x+10)^{50}+(x-10)^{50}$

$=a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{50} x^{50}$

$\therefore \quad a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{50} x^{50}$

$=2\left({ }^{50} C_{0} x^{50}+{ }^{50} C_{2} x^{48} \cdot 10^{2}+{ }^{50} C_{4} x^{46} \cdot 10^{4}+\ldots\right)$

$\therefore \quad a_{0}=2 \cdot{ }^{50} C_{50} 10^{50}$

$\quad a_{2}=2 \cdot{ }^{50} C_{2} \cdot 10^{48}$

$\therefore \quad \frac{a_{2}}{a_{0}}=\frac{{ }^{50} C_{2} \times 10^{48}}{{ }^{50} C_{50} 10^{50}}$

$=\frac{50 \times 49}{2 \times 100}=\frac{49}{4}=12.25$

</details>

---

### Q107. JEE Main 2019 (11 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the real values of $x$ for which the middle term in the binomial expansion of $\left(\frac{x^{3}}{3}+\frac{3}{x}\right)^{8}$ equals 5670 is :

**Options:**

- **(A)** 0
- **(B)** 6
- **(C)** 4
- **(D)** 8

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 0**

**Detailed Solution:**

Middle Term, $\left(\frac{n}{2}+1\right)^{\text {th }}$ term in the binomial

expansion of $\left(\frac{x^{3}}{3}+\frac{3}{x}\right)^{8}$ is,

$T_{4+1}={ }^{8} C_{4}\left(\frac{x^{3}}{3}\right)^{4}\left(\frac{3}{x}\right)^{4}=5670$

$\Rightarrow \quad \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2} \times x^{12-4}=5670$

$\Rightarrow \quad x^{8}=81$

$\Rightarrow x^{8}-81=0$

$\therefore$ sum of all values of $x=$ sum of roots of equation $\left(x^{8}-81=\right.$ 0).

</details>

---

### Q108. JEE Main 2019 (10 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The positive value of <math><mi>&#955;</mi></math> for which the co-efficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> in the expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><msup><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mfrac><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mrow></mfenced><mn>10</mn></msup></math> is <math><mn>720</mn><mo>,</mo></math> is

**Options:**

- **(A)** <math><msqrt><mn>5</mn></msqrt></math>
- **(B)** <math><mn>3</mn></math>
- **(C)** <math><mn>4</mn></math>
- **(D)** <math><mn>2</mn><msqrt><mn>2</mn></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>4</mn></math>**

**Detailed Solution:**

Coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> in <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>

<math><mo>=</mo></math> coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msup></math> in <math><msup><mrow><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>

A general term in the expansion <math><msup><mrow><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mfrac><mrow><mi>&#955;</mi></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow/><mn>10</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced separators="|"><msqrt><mi>x</mi></msqrt></mfenced><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mfenced separators="|"><mfrac><mi>&#955;</mi><msup><mi>x</mi><mn>2</mn></msup></mfrac></mfenced><mi>r</mi></msup><msup><mo>=</mo><mn>10</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced><mi>&#955;</mi></mfenced><mi>r</mi></msup><msup><mfenced><mi>x</mi></mfenced><mrow><mn>5</mn><mo>-</mo><mn>5</mn><mfrac><mi>r</mi><mn>2</mn></mfrac></mrow></msup></math>

<math><mo>&#8658;</mo></math> coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>0</mn></mrow></msup><mo>=</mo><msup><mrow><mtext>&#8201;</mtext></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>2</mn></mrow></msub><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></math> (for <math><mi>r</mi><mo>=</mo><mn>2</mn></math> )

<math><mo>=</mo><mn>45</mn><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup></math>

Now <math><mn>45</mn><msup><mrow><mi>&#955;</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>=</mo><mn>720</mn></math>

<math><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mo>&#177;</mo><mn>4</mn></math>

</details>

---

### Q109. JEE Main 2019 (10 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

If the third term in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>5</mn></msup></math> equals <math><mn>2560</mn><mo>,</mo></math> then a possible value of <math><mi>x</mi></math> is

**Options:**

- **(A)** <math><mn>4</mn><msqrt><mn>2</mn></msqrt></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>8</mn></mfrac></math>
- **(C)** <math><mn>2</mn><mi> </mi><msqrt><mn>2</mn></msqrt></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>4</mn></mfrac></math>**

**Detailed Solution:**

<p>The general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></msup><msup><mi>b</mi><mi>r</mi></msup><mo>.</mo></math></p><p>Given, in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mrow></mfenced><mn>5</mn></msup><mo>,</mo></math> third term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mn>3</mn></msub><mo>=</mo><msup><mo>&#160;</mo><mn>5</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>2</mn></msup><mo>=</mo><mn>2560</mn></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mi>n</mi></mmultiscripts><mo>=</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mo>&#183;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>!</mo><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow></mfrac><msup><mfenced separators="|"><msup><mi>x</mi><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mn>2</mn></msup><mo>=</mo><mn>2560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>5</mn><mo>&#183;</mo><mn>4</mn><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>1</mn><mo>&#183;</mo><mn>3</mn><mo>!</mo></mrow></mfrac><mfenced separators="|"><msup><mi>x</mi><mrow><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mo>=</mo><mn>2560</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><msup><mi>x</mi><mrow><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mo>=</mo><mn>256</mn></math></p><p>Taking logarithm to the base <math><mn>2</mn></math> on both sides</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>log</mi><mn>2</mn></msub><mfenced separators="|"><msup><mi>x</mi><mrow><mn>2</mn><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></msup></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><mn>256</mn></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><msup><mi>m</mi><mi>n</mi></msup><mo>=</mo><mi>n</mi><msub><mi>log</mi><mi>a</mi></msub><mi>m</mi><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>log</mi><mi>a</mi></msub><mi>a</mi><mo>=</mo><mn>1</mn><mo>,</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mi>x</mi><mfenced><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></mfenced><mo>=</mo><msub><mi>log</mi><mn>2</mn></msub><msup><mn>2</mn><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>2</mn><msup><mfenced separators="|"><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced separators="|"><mrow><msub><mi>log</mi><mn>2</mn></msub><mi>x</mi></mrow></mfenced><mo>=</mo><mo>&#177;</mo><mn>2</mn></math></p><p>Using, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi><mo>=</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mo>&#8658;</mo><mi>x</mi><mo>=</mo><msup><mi>a</mi><mi>b</mi></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><msup><mn>2</mn><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>x</mi><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>Here, only <math><mi>x</mi><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math> is given in the options.</p>

</details>

---

### Q110. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math> in the expansion of the product <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mfenced open="{" close="}"><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></mrow></mfenced></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>107</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>108</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>155</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>106</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>106</mn></math>**

**Detailed Solution:**

We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>(</mo><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mo>)</mo></mrow><mn>6</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mn>6</mn></munderover><msup><mi>&#160;</mi><mn>6</mn></msup><msub><mi>C</mi><mi>r</mi></msub><msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>r</mn></msup></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mo>=</mo><mn>6</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>1</mn></msub><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>&#160;</mo><mo>&#8230;</mo><msup><mo>+</mo><mn>6</mn></msup><msub><mi>C</mi><mn>6</mn></msub><msup><mfenced separators="|"><mrow><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></math>
<math><mo>&#8756;</mo></math> Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>18</mn><mo>+</mo><mn>60</mn><mo>=</mo><mi>78</mi></math>
Again, coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>=</mo><mo>-</mo><mn>24</mn></math>
Constant term in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></mrow></mfenced></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>2</mn></math>.
Thus, the required coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup><mo>=</mo><mn>2</mn></math> (coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>2</mn></msup></math>) in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></mrow></mfenced><mo>-</mo></math>constant term in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mi>x</mi><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>6</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><mn>78</mn><mo>-</mo><mn>24</mn></mrow></mfenced><mo>-</mo><mn>2</mn></math>
<math><mo>=</mo><mn>106</mn></math>.

</details>

---

### Q111. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^{10}$ in the expansion of $(1+x)^2$ $\left(1+x^2\right)^3\left(1+x^3\right)^4$ is equal to

**Options:**

- **(A)** 52
- **(B)** 44
- **(C)** 50
- **(D)** 56

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 52**

**Detailed Solution:**

$\because(1+x)^2=1+2 x+x^2$,
$$
\left(1+x^2\right)^3=1+3 x^2+3 x^4+x^6,
$$
and $\left(1+x^3\right)^4=1+4 x^3+6 x^6+4 x^9+x^{12}$
So, the possible combinations for $x^{10}$ are:
$$
x \cdot x^9, x \cdot x^6 \cdot x^3, x^2 \cdot x^2 \cdot x^6, x^4 \cdot x^6
$$
Corresponding coefficients are $2 \times 4,2 \times 1 \times$ $4,1 \times 3 \times 6,3 \times 6$ or $8,8,18,18$.
$\therefore$ Sum of the coefficient is
$$
8+8+18+18=52
$$
Therefore, the coefficient of $x^{10}$ in the expansion of $(1+x)^2\left(1+x^2\right)^3\left(1+x^3\right)^4$ is 52 .

</details>

---

### Q112. JEE Main 2018 (15 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the degree of the polynomial, <math><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><msqrt><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>+</mo><mi mathvariant="normal">&#160;</mi><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><msqrt><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mn>5</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is the coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mi>n</mi></mrow></msup></math> in it, then the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>,</mo><mo>&#160;</mo><mi>m</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>8</mn><mo>,</mo><mi>&#160;</mi><mn>5</mn><msup><mfenced><mn>10</mn></mfenced><mn>4</mn></msup></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>12</mn><mo>,</mo><mi>&#160;</mi><mn>8</mn><msup><mfenced><mn>10</mn></mfenced><mn>4</mn></msup></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>12</mn><mo>,</mo><mo>&#160;</mo><msup><mfenced><mn>20</mn></mfenced><mn>4</mn></msup></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>24</mn><mo>,</mo><mo>&#160;</mo><msup><mfenced><mn>10</mn></mfenced><mn>8</mn></msup></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>12</mn><mo>,</mo><mo>&#160;</mo><msup><mfenced><mn>20</mn></mfenced><mn>4</mn></msup></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced open="[" close="]" separators="|"><mfrac><mn>2</mn><mrow><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>-</mo><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mfenced><mn>8</mn></msup><mo>+</mo><mi mathvariant="normal">&#160;</mi><msup><mfenced open="[" close="]" separators="|"><mfrac><mn>2</mn><mrow><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mrow></mfrac></mfenced><mn>8</mn></msup></math></p><p>Rationalizing denominators of both the brackets,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced open="[" close="]" separators="|"><mrow><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn><mi>&#160;</mi></msqrt><mi>&#160;</mi></mrow></mfenced><mn>8</mn></msup><mo>+</mo><mi>&#160;</mi><msup><mfenced open="[" close="]" separators="|"><mrow><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt><mi>&#160;</mi><mo>-</mo><mi>&#160;</mi><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn><mi>&#160;</mi></msqrt><mi>&#160;</mi></mrow></mfenced><mn>8</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]" separators="|"><mrow><msup><mrow/><mn>8</mn></msup><msub><mi>C</mi><mn>0</mn></msub><mi>&#160;</mi><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfenced><mn>8</mn></msup><msup><mo>+</mo><mn>8</mn></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfenced><mn>6</mn></msup><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mn>2</mn></msup><msup><mo>+</mo><mn>8</mn></msup><msub><mi>C</mi><mn>4</mn></msub><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfenced><mn>4</mn></msup><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mn>4</mn></msup><msup><mo>+</mo><mn>8</mn></msup><msub><mi>C</mi><mn>6</mn></msub><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></msqrt></mfenced><mn>2</mn></msup><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mn>6</mn></msup><msup><mo>+</mo><mn>8</mn></msup><msub><mi>C</mi><mn>8</mn></msub><msup><mfenced separators="|"><msqrt><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></msqrt></mfenced><mn>8</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced open="[" close="]"><mrow><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup><mo>+</mo><mn>28</mn><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>70</mn><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>28</mn><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>5</mn><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>4</mn></msup></mrow></mfenced></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>12</mn></math> and </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><msup><mn>5</mn><mn>4</mn></msup><mo>+</mo><mn>140</mn><msup><mo>.5</mo><mn>3</mn></msup><mo>+</mo><mn>70</mn><msup><mo>.5</mo><mn>4</mn></msup><mo>+</mo><mn>140</mn><msup><mo>.5</mo><mn>3</mn></msup><mo>+</mo><msup><mn>5</mn><mn>4</mn></msup></mrow></mfenced><mo>=</mo><mn>160000</mn><mo>=</mo><msup><mfenced separators="|"><mn>20</mn></mfenced><mn>4</mn></msup></math></p>

</details>

---

### Q113. JEE Main 2018 (15 Apr Shift 1 Online)

*Type:* `singleCorrect` | *Level:* `3`

If $n$ is the degree of the polynomial,
$$
\left[\frac{1}{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}}\right]^8+\left[\frac{1}{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}}\right]^8
$$
and $\mathrm{m}$ is the coefficient of $\mathrm{x}^{\mathrm{n}}$ in it, then the ordered pair $(\mathrm{n}, \mathrm{m})$ is equal to

**Options:**

- **(A)** $\left(12,(20)^4\right)$
- **(B)** $\left(8,5(10)^4\right)$
- **(C)** $\left(24,(10)^8\right)$
- **(D)** $\left(12,8(10)^4\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\left(12,8(10)^4\right)$**

**Detailed Solution:**

$$
\left[\frac{1}{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}}\right]^8+\left[\frac{1}{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}}\right]^8
$$
After rationalise the polynomial we get
$$
\begin{aligned}
&{\left[\frac{1}{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}} \times \frac{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}}{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}}\right]^8} \\
&+\left[\frac{1}{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}} \times \frac{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}}{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}}\right]^8
\end{aligned}
$$
$$
\left[\frac{\sqrt{5 x^3+1}+\sqrt{5 x^3-1}}{\left(5 x^3+1\right)-\left(5 x^3-1\right)}\right]^8+\left[\frac{\sqrt{5 x^3+1}-\sqrt{5 x^3-1}}{\left(5 x^3+1\right)-\left(5 x^3-1\right)}\right]^8
$$
$$
\begin{aligned}
&=\frac{1}{2^8}\left[\left(\sqrt{5 x^3+1}+\sqrt{5 x^3-1}\right)^8+\left(\sqrt{5 x^3+1}-\sqrt{5 x^3-1}\right)^8\right] \\
&\left.=\frac{1}{2^8}\left[\begin{array}{l}
\left.{ }^8 C_0\left(\sqrt{5 x^3+1}\right)^8+{ }^8 C_4\left(\sqrt{5 x^3+1}\right)^6\left(\sqrt{5 x^3-1}\right)^2\right)^4\left(\sqrt{5 x^3-1}\right)^4+ \\
{ }^8 C_6\left(\sqrt { 5 x ^ { 3 } + 1 } { } ^ { 2 } \left(\sqrt{\left.5 x^3-\right)^1}{ }^6+{ }^8 C_8\left(\sqrt{5 x^3-1}{ }^8\right.\right.\right.
\end{array}\right]\right) \\
&\frac{1}{2^8}\left[\begin{array}{l}
{ }^8 C_0\left(5 x^3+1\right)^4+{ }^8 C_2\left(5 x^3+1\right)^3\left(5 x^3-1\right)+8_{C_4} \\
\left(5 x^3+1\right)^2\left(5 x^3-1\right)^2+ \\
{ }^8 C_6\left(5 x^3+1\right)\left(5 x^3-1\right)^3+8_{C_8}\left(5 x^3-1\right)^4
\end{array}\right] \\
&
\end{aligned}
$$
So, the degree of polynomial is 12 ,
Now, coefficient of
$$
\begin{aligned}
&x^{12}=\left[{ }^8 \mathrm{C}_0 5^4+{ }^8 \mathrm{C}_2 5^4+{ }^8 \mathrm{C}_4 5^4+{ }^8 \mathrm{C}_6 5^4+{ }^8 \mathrm{C}_8 5^4\right] \\
&=5^4 \times \frac{2^8}{2}=5^4 \times 2^4 \times \frac{2^2}{2} \\
&=10^4 \times 2^3=8(10)^4
\end{aligned}
$$

</details>

---

### Q114. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>5</mn></mrow></msup></math> in the binomial expansion of <math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn><mi>&#160;</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>x</mi><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math> where <math><mi>x</mi><mo>&#8800;</mo><mn>0,1</mn></math> is

**Options:**

- **(A)** <math><mo>-</mo><mn>1</mn></math>
- **(B)** <math><mn>4</mn></math>
- **(C)** <math><mn>1</mn></math>
- **(D)** <math><mo>-</mo><mn>4</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>1</mn></math>**

**Detailed Solution:**

<math><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>-</mo><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mrow><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><msqrt><mi>x</mi></msqrt><mi>&#160;</mi><mfenced separators="|"><mrow><msqrt><mi>x</mi></msqrt><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math>

<math><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>-</mo><msup><mi>x</mi><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac></msup></mrow></mfenced><mn>10</mn></msup></math>

<math><msub><mrow><mi>t</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>10</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mo>&#8722;</mo><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup></math><math> <mrow> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mo>&#8722;</mo><mn>1</mn></mrow> <mo>)</mo></mrow></mrow> <mi>r</mi> </msup> </mrow> </math>

<math><msub><mrow><mi>t</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></msup></mrow></mfenced><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup></math>

<math><mo>&#8757;</mo><mi>&#160;</mi><mfrac><mrow><mn>10</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mo>-</mo><mn>5</mn></math>

<math><mfrac><mrow><mn>5</mn><mi>r</mi></mrow><mrow><mn>6</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>50</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo><mi>r</mi><mo>=</mo><mn>10</mn></math>

Hence, <math><msup><mrow></mrow><mrow><mn>10</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mn>10</mn></mrow></msub><msup><mrow><mfenced separators="|"><mrow><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>10</mn></mrow></msup><mo>=</mo><mn>1</mn><mi>&#160;</mi></math>

</details>

---

### Q115. JEE Main 2016 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the coefficients of <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>2</mn></mrow></msup></math> and <math><msup><mrow><mi>x</mi></mrow><mrow><mo>-</mo><mn>4</mn></mrow></msup></math>, in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>18</mn></msup><mo>,</mo><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math>, are <math> <mi>m</mi> </math> and <math> <mi>n</mi> </math> respectively, then <math><mfrac><mrow><mi>m</mi></mrow><mrow><mi>n</mi></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math><mn>27</mn></math>
- **(B)** <math><mn>182</mn></math>
- **(C)** <math><mfrac><mrow><mn>5</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>182</mn></math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>x</mi><mfrac><mn>1</mn><mn>3</mn></mfrac></msup></mrow></mfrac></mrow></mfenced><mn>18</mn></msup><mo>,</mo><mfenced separators="|"><mrow><mi>x</mi><mo>&#62;</mo><mn>0</mn></mrow></mfenced></math></p><p>General term, <math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><msup><mrow></mrow><mrow><mn>18</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><msup><mrow><mfenced separators="|"><mrow><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></mrow></mfenced></mrow><mrow><mn>18</mn><mo>-</mo><mi>r</mi></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup></mrow></mfrac></mrow></mfenced></mrow><mrow><mi>r</mi></mrow></msup><mo>=</mo><msup><mrow></mrow><mrow><mn>18</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub><mi>&#160;</mi><msup><mrow><mi>x</mi></mrow><mrow><mn>6</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mrow><mn>3</mn></mrow></mfrac></mrow></msup><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mi>r</mi></mrow></msup></mrow></mfrac></math>
Now,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="" open="" separators="|"><mtable><mtr><mtd><mn>6</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mo>-</mo><mn>2</mn></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>r</mi><mo>=</mo><mn>12</mn></mtd></mtr></mtable></mfenced></math> and, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="" open="" separators="|"><mtable><mtr><mtd><mn>6</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>r</mi></mrow><mn>3</mn></mfrac><mo>=</mo><mo>-</mo><mn>4</mn></mtd><mtd><mo>&#8658;</mo></mtd><mtd><mi>r</mi><mo>=</mo><mn>15</mn></mtd></mtr></mtable></mfenced></math>
Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac><mo>=</mo><mfrac><mrow><mtext>Coefficient&#160;of</mtext><mo>&#160;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>2</mn></mrow></msup></mrow><mrow><mtext>Coefficient&#160;of</mtext><mo>&#160;</mo><msup><mi>x</mi><mrow><mo>-</mo><mn>4</mn></mrow></msup></mrow></mfrac><mo>=</mo><mfrac><mfrac><mmultiscripts><mi>C</mi><mn>12</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mn>2</mn><mn>12</mn></msup></mfrac><mfrac><mmultiscripts><mi>C</mi><mn>15</mn><none/><mprescripts/><none/><mn>18</mn></mmultiscripts><msup><mn>2</mn><mn>15</mn></msup></mfrac></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mstyle displaystyle="true"><mfrac><mrow><mn>18</mn><mo>!</mo></mrow><mrow><mn>6</mn><mo>!</mo><mo>.</mo><mn>12</mn><mo>!</mo></mrow></mfrac></mstyle><mfrac><mrow><mn>18</mn><mo>!</mo></mrow><mrow><mn>3</mn><mo>!</mo><mo>.</mo><mn>15</mn><mo>!</mo></mrow></mfrac></mfrac><mo>&#215;</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>14</mn><mo>&#215;</mo><mn>13</mn></mrow><mrow><mn>6</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac><mo>&#215;</mo><msup><mn>2</mn><mn>3</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>182</mn></math></p>

</details>

---

### Q116. JEE Main 2016 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mfenced><mfrac><mrow><msup><mrow></mrow><mn>15</mn></msup><msub><mi>C</mi><mi>r</mi></msub></mrow><mrow><msup><mrow></mrow><mn>15</mn></msup><msub><mi>C</mi><mrow><mi>r</mi><mo>&#8722;</mo><mn>1</mn></mrow></msub></mrow></mfrac></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1240</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>560</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1085</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>680</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>680</mn></math>**

**Detailed Solution:**

Given <math> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn></mrow> <mrow> <mn>15</mn></mrow> </munderover> <mrow> <msup> <mi>r</mi> <mn>2</mn> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mrow></mrow> <mrow> <mn>15</mn></mrow> </msup> <msub> <mi>C</mi> <mi>r</mi> </msub> </mrow> <mrow> <msup> <mrow></mrow> <mrow> <mn>15</mn></mrow> </msup> <msub> <mi>C</mi> <mrow> <mi>r</mi><mo>&#8722;</mo><mn>1</mn></mrow> </msub> </mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> </mstyle></mrow> </math>

Here <math><mfrac><mrow><msup><mrow></mrow><mrow><mn>15</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi></mrow></msub></mrow><mrow><msup><mrow></mrow><mrow><mn>15</mn></mrow></msup><msub><mrow><mi>C</mi></mrow><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfrac></math><math><mo>=</mo><mfrac><mrow><mn>16</mn><mo>-</mo><mi>r</mi></mrow><mrow><mi>r</mi></mrow></mfrac></math>

<math> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn></mrow> <mrow> <mn>15</mn></mrow> </munderover> <mrow> <msup> <mi>r</mi> <mn>2</mn> </msup> <mrow><mo>(</mo> <mrow> <mfrac> <mrow> <msup> <mrow></mrow> <mrow> <mn>15</mn></mrow> </msup> <msub> <mi>C</mi> <mi>r</mi> </msub> </mrow> <mrow> <msup> <mrow></mrow> <mrow> <mn>15</mn></mrow> </msup> <msub> <mi>C</mi> <mrow> <mi>r</mi><mo>&#8722;</mo><mn>1</mn></mrow> </msub> </mrow> </mfrac> </mrow> <mo>)</mo></mrow></mrow> </mstyle></mrow> </math> <math><mo>=</mo><mi>&#160;</mi><mi>&#160;</mi> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>15</mn> </mrow> </munderover> <mrow> <msup> <mi>r</mi> <mn>2</mn> </msup> </mrow> </mstyle> </mrow> </math> <math><mfenced separators="|"><mrow><mfrac><mrow><mn>16</mn><mo>-</mo><mi>r</mi></mrow><mrow><mi>r</mi></mrow></mfrac></mrow></mfenced></math>

<math> <mo>=</mo><mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>15</mn> </mrow> </munderover> <mrow> <mi>r</mi> </mrow> </mstyle> </mrow> </math> <math><mfenced separators="|"><mrow><mn>16</mn><mo>-</mo><mi>r</mi></mrow></mfenced></math>

<math><mo>=</mo></math><math><mn>16</mn><mi>&#160;</mi><mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>15</mn> </mrow> </munderover> <mrow> <mi>r</mi> </mrow> </mstyle> </mrow><mo>-</mo><mi>&#160;</mi><mrow><mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>r</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>15</mn> </mrow> </munderover> <mrow> <msup> <mi>r</mi> <mn>2</mn> </msup> </mrow> </mstyle> </mrow></mrow></math>

<math><mo>=</mo></math><math><mfrac><mrow><mn>16</mn><mi>&#160;</mi><mo>&#215;</mo><mn>15</mn><mi>&#160;</mi><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>15</mn><mi>&#160;</mi><mo>&#215;</mo><mn>31</mn><mi>&#160;</mi><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<math><mo>=</mo></math><math><mn>8</mn><mi>&#160;</mi><mo>&#215;</mo><mn>15</mn><mi>&#160;</mi><mo>&#215;</mo><mn>16</mn><mo>-</mo><mn>5</mn><mi>&#160;</mi><mo>&#215;</mo><mn>8</mn><mi>&#160;</mi><mo>&#215;</mo><mn>31</mn></math>

<math><mo>=</mo></math><math><mn>1920</mn><mo>-</mo><mn>1240</mn><mo>=</mo><mn>680</mn></math>

</details>

---

### Q117. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the binomial expansion of <math><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><mo>+</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup></mrow></mfenced><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup></math> is

**Options:**

- **(A)** <math><mo>-</mo><mi> </mi><mn>496</mn></math>
- **(B)** <math><mo>-</mo><mn>400</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>496</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>400</mn></math>**

**Detailed Solution:**

The term independent of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> will come from

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced separators="|"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>5</mn></msup></mrow></mfenced><msup><mfenced separators="|"><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mi>x</mi></mfrac></mrow></mfenced><mn>8</mn></msup></math>

General term of  <math><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup></math> is <math> <mrow> <mmultiscripts> <mi>C</mi> <mprescripts></mprescripts> <none></none> <mn>8</mn> </mmultiscripts> <msub> <mrow></mrow> <mi>r</mi> </msub> <msup> <mrow> <mrow><mo>(</mo> <mrow> <mo>&#8722;</mo><mfrac> <mn>1</mn> <mi>x</mi> </mfrac> </mrow> <mo>)</mo></mrow> </mrow> <mi>r</mi> </msup> </mrow> </math><math><mi>&#160;</mi><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>8</mn><mo>-</mo><mi>r</mi></mrow></msup><mo>=</mo></math><math> <mrow> <mmultiscripts> <mi>C</mi> <mprescripts></mprescripts> <none></none> <mn>8</mn> </mmultiscripts> <msub> <mrow></mrow> <mi>r</mi> </msub> <msup> <mn>2</mn> <mrow> <mn>8</mn><mo>&#8722;</mo><mi>r</mi> </mrow> </msup> <msup> <mrow> <mo stretchy="false">(</mo><mo>&#8722;</mo><mn>1</mn><mo stretchy="false">)</mo> </mrow> <mi>r</mi> </msup> <msup> <mi>x</mi> <mrow> <mn>16</mn><mo>&#8722;</mo><mn>3</mn><mi>r</mi> </mrow> </msup> </mrow> </math>

From expansion

<math><mn>1</mn><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>+</mo><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup></math>

<math><mn>1</mn><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>&#8594;</mo></math> no constant term

<math><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>&#8594;</mo></math> for constant term

<math><mi>&#160;</mi><mi>r</mi><mo>=</mo><mn>5</mn><mi>&#160;</mi><mi>&#160;</mi><mo>&#8658;</mo></math> <math> <mrow> <mo>&#8722;</mo><mmultiscripts> <mi>C</mi> <mprescripts></mprescripts> <none></none> <mn>8</mn> </mmultiscripts> <msub> <mrow></mrow> <mn>3</mn> </msub> <msup> <mn>2</mn> <mn>3</mn> </msup> <msup> <mrow> <mo stretchy="false">(</mo><mo>&#8722;</mo><mn>1</mn><mo stretchy="false">)</mo> </mrow> <mn>5</mn> </msup> <mo>=</mo><mo>+</mo><mn>448</mn> </mrow> </math>

<math><mn>3</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>5</mn></mrow></msup><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><msup><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>x</mi></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>8</mn></mrow></msup><mo>&#8594;</mo></math> for constant term

<math><mi>r</mi><mo>=</mo><mn>7</mn><mo>&#8658;</mo></math> <math> <mrow> <mmultiscripts> <mi>C</mi> <mprescripts></mprescripts> <none></none> <mrow> <mn>38</mn> </mrow> </mmultiscripts> <msub> <mrow></mrow> <mn>7</mn> </msub> <msup> <mn>2</mn> <mn>1</mn> </msup> <msup> <mrow> <mo stretchy="false">(</mo><mo>&#8722;</mo><mn>1</mn><mo stretchy="false">)</mo> </mrow> <mn>7</mn> </msup> <mo>=</mo><mn>48</mn> </mrow> </math>

Hence, term independent from <math><mi>x</mi><mo>=</mo><mn>448</mn><mo>-</mo><mn>48</mn><mo>=</mo><mn>400</mn></math>

</details>

---

### Q118. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficient of the three successive terms in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mi>n</mi></msup></math> are in the ratio <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>:</mo><mn>7</mn><mo>:</mo><mn>42</mn></math>, then the first of these terms in the expansion is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>9</mn><mi>th</mi></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>6</mn><mi>th</mi></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>8</mn><mi>th</mi></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mi>th</mi></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mi>th</mi></msup></math>**

**Detailed Solution:**

<p>Let coefficient of first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mstyle><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mstyle></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mfrac><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#160;</mi><mn>7</mn><mi>r</mi><mo>+</mo><mn>7</mn><mo>=</mo><mi>n</mi><mo>-</mo><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>8</mn><mi>r</mi><mo>=</mo><mn>7</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>1</mn></mfenced></math> </p><p>Also,  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mstyle><mstyle displaystyle="true"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts></mstyle></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>42</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow><mrow><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>6</mn><mi>r</mi><mo>+</mo><mn>12</mn><mo>=</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>7</mn><mi>r</mi><mo>=</mo><mn>13</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8230;</mo><mfenced><mn>2</mn></mfenced></math> </p><p>Solving <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>6</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mi>th</mi></msup></math> term is the answer. </p>

</details>

---

### Q119. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `2`

The sum of coefficients of integral powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> in the binomial expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfenced><mtext>50</mtext></msup></math> is

**Options:**

- **(A)** <math> <mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>2</mn> <mtext>50</mtext> </msup> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </mrow> </math>
- **(B)** <math> <mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>3</mn> <mtext>50</mtext> </msup> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </mrow> </math>
- **(C)** <math> <mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>3</mn> <mtext>50</mtext> </msup> </mrow> </mfenced> </mrow> </mrow> </math>
- **(D)** <math> <mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>3</mn> <mtext>50</mtext> </msup> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mrow> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>2</mn> </mrow> </mfrac> <mfenced close=")" open="(" separators=","> <mrow> <msup> <mn>3</mn> <mtext>50</mtext> </msup> <mo>+</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </mrow> </math>**

**Detailed Solution:**

Integral Power Term is same as odd term in exapansion

Odd Term <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfenced><mtext>50</mtext></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><msqrt><mi>x</mi></msqrt></mrow></mfenced><mtext>50</mtext></msup></mrow><mn>2</mn></mfrac></math>

Sum of coefficients<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mtext>50</mtext></msup><mo>+</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mtext>50</mtext></msup></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mtext>50</mtext></msup></mrow><mn>2</mn></mfrac></math>

</details>

---

### Q120. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of <math> <mrow> <msup> <mrow> <mi></mi><mi></mi><mi></mi><mi></mi><mi></mi><mi>x</mi><mo>&#8289;</mo> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>1</mn> <mn>2</mn> </mrow> </msup> </mrow> </math>  in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup><mo>+</mo><msup><mi>x</mi><mn>253</mn></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup><mo>,</mo></math> (where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8804;22</mo></math> is any positive integer), is

**Options:**

- **(A)** <sup><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>253</mn></mmultiscripts></math></sup>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>n</mi></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mn>4</mn><none/><mprescripts/><none/><mn>10</mn></mmultiscripts></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup><mo>+</mo><msup><mi>x</mi><mn>253</mn></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mo>+</mo><msup><mi>x</mi><mi>n</mi></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup></math></p><p>Using the binomial expansion <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mi>n</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mn>0</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>n</mi></msup><msup><mi>b</mi><mn>0</mn></msup><mo>+</mo><mmultiscripts><mi>C</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup><mi>b</mi><mo>+</mo><mmultiscripts><mi>C</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></msup><msup><mi>b</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mmultiscripts><mi>C</mi><mi>n</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mn>0</mn></msup><msup><mi>b</mi><mi>n</mi></msup><mo>,</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mspace></mspace><mrow><mn>1</mn><mn>0</mn></mrow></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup><msup><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mn>0</mn></msup><mo>+</mo><msup><mspace></mspace><mrow><mn>1</mn><mn>0</mn></mrow></msup><msub><mi>C</mi><mn>1</mn></msub><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mn>9</mn></msup><msup><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mn>1</mn></msup><mo>+</mo><msup><mspace></mspace><mrow><mn>1</mn><mn>0</mn></mrow></msup><msub><mi>C</mi><mn>2</mn></msub><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mn>8</mn></msup><msup><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mspace></mspace><mrow><mn>1</mn><mn>0</mn></mrow></msup><msub><mi>C</mi><mrow><mn>1</mn><mn>0</mn></mrow></msub><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mn>0</mn></msup><msup><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup></math>

As <math> <mrow> <mn>2</mn> <mn>5</mn> <mn>3</mn> <mo>=</mo> <mn>2</mn> <mn>3</mn> <mo>&#215;</mo> <mn>1</mn> <mn>1</mn> </mrow> </math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>0</mn><mn>1</mn><mn>2</mn><mo>=</mo><mn>2</mn><mn>5</mn><mn>3</mn><mo>&#215;</mo><mn>4</mn></math>, also <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8804;22</mo></math>

<math> <mrow> <mo>&#8658;</mo> </mrow> </math>Coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>1012</mn></msup></math> will come only from the first term, i.e. in</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mspace></mspace><mn>10</mn></msup><msub><mi>C</mi><mn>0</mn></msub><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mrow><mn>2</mn><mn>5</mn><mn>3</mn></mrow></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn></mrow></msup><msup><mfenced><msup><mi>x</mi><mi>n</mi></msup></mfenced><mn>0</mn></msup><mo>=</mo><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>253</mn></msup></mrow></mfenced><mn>10</mn></msup></math></p><p>The general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced><mi>n</mi></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>n</mi></mmultiscripts><msup><mi>a</mi><mi>r</mi></msup></math></p><p>Hence, the general term in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mi>x</mi><mn>253</mn></msup></mrow></mfenced><mn>10</mn></msup></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><msup><mfenced><msup><mi>x</mi><mn>253</mn></msup></mfenced><mi>r</mi></msup><mo>=</mo><mmultiscripts><mi>C</mi><mi>r</mi><none/><mprescripts/><none/><mn>10</mn></mmultiscripts><mfenced><msup><mi>x</mi><mrow><mn>253</mn><mi>r</mi></mrow></msup></mfenced></math></p><p>Since, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1012</mn><mo>=</mo><mn>253</mn><mo>&#215;</mo><mn>4</mn><mo>,</mo></math> hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi><mo>=</mo><mn>4</mn></math></p><p>Thus, the required coefficient is<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mspace/><mn>10</mn></msup><msub><mi>C</mi><mn>4</mn></msub><mo>.</mo></math></p>

</details>

---

### Q121. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $\left(2+\frac{x}{3}\right)^{55}$ is expanded in the ascending powers of $x$ and the coefficients of powers of $x$ in two consecutive terms of the expansion are equal, then these terms are:

**Options:**

- **(A)** $7^{\text {th }}$ and $8^{\text {th }}$
- **(B)** $8^{\text {th }}$ and $9^{\text {th }}$
- **(C)** $28^{\text {th }}$ and $29^{\text {th }}$
- **(D)** $27^{\text {th }}$ and $28^{\text {th }}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7^{\text {th }}$ and $8^{\text {th }}$**

**Detailed Solution:**

Let $r^{\text {th }}$ and $(r+1)^{\text {th }}$ term has equal coefficient
$$
\begin{aligned}
&\left(2+\frac{x}{3}\right)^{55}=2^{55}\left(1+\frac{x}{6}\right)^{55} \\
&r^{\text {th }} \text { term }=2^{5555} C_r\left(\frac{x}{6}\right)^r
\end{aligned}
$$
Coefficient of $x^r$ is $2^{55}{ }^{55} C_r \frac{1}{6^r}$
$$
(r+1)^{\text {th }} \text { term }=2^{5555} C_{r+1}\left(\frac{x}{6}\right)^{r+1}
$$
Coefficient of $x^{r+1}$ is $2^{55}{ }^{55} C_{r+1} \cdot \frac{1}{6^{r+1}}$
Both coefficients are equal
$$
2^{5555} C_r \frac{1}{6^r}=2^{5555} C_{r+1} \frac{1}{6^{r+1}}
$$

$$
\begin{aligned}
&\frac{1}{|r| 55-r}=\frac{1}{\lfloor r+1 \mid 54-r} \cdot \frac{1}{6} \\
&6(r+1)=55-r \\
&6 r+6=55-r \\
&7 r=49 \\
&r=7 \\
&(r+1)=8
\end{aligned}
$$
Coefficient of $7^{\text {th }}$ and $8^{\text {th }}$ terms are equal.

</details>

---

### Q122. JEE Main 2014 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^{50}$ in the binomial expansion of $(1+x)^{1000}+x(1+x)^{999}+x^2(1+x)^{998}+\ldots$ $+x^{1000}$ is:

**Options:**

- **(A)** $\frac{(1000) !}{(50)(! 95 \varphi !}$
- **(B)** $\frac{(1000) !}{(49)(! 95) !}$
- **(C)** $\frac{(1001) !}{(51)(! 95 \phi !}$
- **(D)** $\frac{(1001) !}{(50)(! 95) !}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{(1001) !}{(50)(! 95) !}$**

**Detailed Solution:**

Let given expansion be
$$
\begin{aligned}
&\mathrm{S}=(1+x)^{1000}+x(1+x)^{999}+x^2 \\
&(1+x)^{998}+\ldots+\ldots+x^{1000}
\end{aligned}
$$
Put $1+x=t$
$$
\mathrm{S}=t^{1000}+x t^{999}+x^2(t)^{998}+\ldots+x^{1000}
$$
This is a G.P with common ratio $\frac{x}{t}$
$$
\begin{aligned}
\mathrm{S} &=\frac{t^{1000}\left[1-\left(\frac{x}{t}\right)^{1001}\right]}{1-\frac{x}{t}} \\
&=\frac{(1+x)^{1000}\left[1-\left(\frac{x}{1+x}\right)^{1001}\right]}{1-\frac{x}{1+x}} \\
=& \frac{(1+x)^{1001}\left[(1+x)^{1001}-x^{1001}\right]}{(1+x)^{1001}}
\end{aligned}
$$

$$
=\left[(1+x)^{1001}-x^{1001}\right]
$$
Now coeff of $x^{50}$ in above expansion is equal to coeff of $x^{50}$ in $(1+x)^{1001}$ which is ${ }^{1001} C_{50}=\frac{(1001) !}{50 !(951) !}$

</details>

---

### Q123. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

<p>The number of terms in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mn>101</mn></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><mn>100</mn></msup></math> in powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>301</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>302</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>202</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>202</mn></math>**

**Detailed Solution:**

<p><math> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <mtext>x</mtext> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>1</mn> </mrow> </msup> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>2</mn> </msup> <mo>-</mo> <mtext>x</mtext> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn> </mrow> </msup> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mtext>x</mtext></mrow></mfenced><mfenced close="}" open="{"><mrow><msup><mfenced><mrow><mn>1</mn><mo>+</mo><mtext>x</mtext></mrow></mfenced><mrow><mn>1</mn><mn>0</mn><mn>0</mn></mrow></msup><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mtext>x</mtext><mo>+</mo><msup><mtext>x</mtext><mn>2</mn></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn><mn>0</mn></mrow></msup></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mtext>x</mtext></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>+</mo><msup><mtext>x</mtext><mn>3</mn></msup></mrow></mfenced><mrow><mn>1</mn><mn>0</mn><mn>0</mn></mrow></msup></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8757;</mo><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup><mo>=</mo><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mfenced><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>a</mi><mi>b</mi><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow></mfenced></mrow></mfenced></math></p><p><math> <mrow> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>3</mn> </msup> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn> </mrow> </msup> </mrow> </math> has <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math> terms

<math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <mtext>x</mtext> </mrow> </mfenced> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>3</mn> </msup> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn> </mrow> </msup> <mo>=</mo> <mn>1</mn> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>3</mn> </msup> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn> </mrow> </msup> <mo>+</mo> <mtext>x</mtext> <msup> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mo>+</mo> <msup> <mtext>x</mtext> <mn>3</mn> </msup> </mrow> </mfenced> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn> </mrow> </msup> </mrow> </math>

<math> <mrow> <mo>&#8658;</mo> </mrow> </math> No. of  terms = <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn><mo>+</mo><mn>101</mn><mo>=</mo><mn>202</mn></math></p>

</details>

---

### Q124. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `2`

If the coefficients of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>3</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>x</mi><mn>4</mn></msup></math> in the expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>18</mn></msup></math> in powers of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math> are both zero, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>,</mo><mi>b</mi></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>4</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> <mn>2</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(B)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>6</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> <mn>2</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(C)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>6</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>2</mn> <mn>5</mn> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>
- **(D)** <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>4</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>2</mn> <mn>5</mn> <mn>1</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mfenced close=")" open="(" separators=","> <mrow> <mn>1</mn> <mn>6</mn> <mtext>, </mtext> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> <mn>2</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </mfenced> </mrow> </math>**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi><mi>x</mi><mo>+</mo><mi>b</mi><msup><mi>x</mi><mn>2</mn></msup></mrow></mfenced><msup><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn><mi>x</mi></mrow></mfenced><mn>18</mn></msup><mo>=</mo><msub><mi>a</mi><mn>0</mn></msub><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mi>x</mi><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>=</mtext><mfenced><mrow><mn>1</mn><mo>+</mo><mi>ax</mi><mo>+</mo><msup><mi>bx</mi><mn>2</mn></msup></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mspace/><mn>18</mn></msup><msub><mi mathvariant="normal">C</mi><mn>1</mn></msub><mo>&#183;</mo><mn>2</mn><mi mathvariant="normal">x</mi><mo>+</mo><msup><mspace/><mn>18</mn></msup><msub><mi mathvariant="normal">C</mi><mn>2</mn></msub><mo>&#183;</mo><msup><mn>2</mn><mn>2</mn></msup><msup><mi mathvariant="normal">x</mi><mn>2</mn></msup><mo>+</mo><mo>.....</mo><msup><mspace/><mn>18</mn></msup><msub><mo>C</mo><mn>18</mn></msub><msup><mfenced><mrow><mn>2</mn><mi mathvariant="normal">x</mi></mrow></mfenced><mn>18</mn></msup></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">a</mi><mn>3</mn></msub><mo>=</mo><msub><mrow><msup><mspace/><mrow><mo>-</mo><mn>18</mn></mrow></msup><mi mathvariant="normal">C</mi></mrow><mn>3</mn></msub><mo>&#215;</mo><mn>8</mn><mo>+</mo><msub><mrow><msup><mspace/><mn>18</mn></msup><mi mathvariant="normal">C</mi></mrow><mn>2</mn></msub><mo>&#215;</mo><mn>4</mn><mi mathvariant="normal">a</mi><mo>-</mo><mn>36</mn><mi mathvariant="normal">b</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi mathvariant="normal">a</mi><mn>4</mn></msub><mo>=</mo><msub><mrow><msup><mspace/><mn>18</mn></msup><mi mathvariant="normal">C</mi></mrow><mn>4</mn></msub><mo>&#215;</mo><mn>16</mn><mo>-</mo><msub><mrow><msup><mspace/><mn>18</mn></msup><mi mathvariant="normal">C</mi></mrow><mn>3</mn></msub><mo>&#215;</mo><mn>8</mn><mi mathvariant="normal">a</mi><mo>+</mo><msub><mrow><msup><mspace/><mn>18</mn></msup><mi mathvariant="normal">C</mi></mrow><mn>2</mn></msub><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mi mathvariant="normal">b</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn><mi>a</mi><mo>-</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>1088</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>64</mn><mi>a</mi><mo>-</mo><mn>6</mn><mi>b</mi><mo>=</mo><mn>480</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Solution of the above two equation gives.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>16</mn></math>
<math> <mrow> <mtext>b</mtext> <mo>=</mo> <mfrac> <mrow> <mn>2</mn> <mn>7</mn> <mn>2</mn> </mrow> <mrow> <mn>3</mn> </mrow> </mfrac> </mrow> </math></p>

</details>

---

### Q125. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If for positive integers $r>1, n>2$, the coefficients of the $(3 r)^{\text {th }}$ and $(r+2)^{\text {th }}$ powers of $x$ in the expansion of $(1+x)^{2 n}$ are equal, then $n$ is equal to:

**Options:**

- **(A)** $2 r+1$
- **(B)** $2 r-1$
- **(C)** $3 r$
- **(D)** $r+1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $2 r+1$**

**Detailed Solution:**

Expansion of $(1+x)^{2 n}$ is $1+{ }^{2 n} \mathrm{C}_1 x+{ }^{2 n} \mathrm{C}_2 x^2$ $+\ldots \ldots .+{ }^{2 n} \mathrm{C}_r x^n+{ }^{2 n} \mathrm{C}_{r+1} x^{n+1}+\ldots \ldots+{ }^{2 n} \mathrm{C}_{2 n} x^{2 n}$ As given ${ }^{2 n} \mathrm{C}_{r+2}={ }^{2 n} \mathrm{C}_{3 r}$
$$
\begin{aligned}
&\Rightarrow \frac{(2 n) !}{(r+2) !(2 n-r-2) !}=\frac{(2 n) !}{(3 r) !(2 n-3 r) !} \\
&\Rightarrow(3 r) !(2 n-3 r) !=(r+2) !(2 n-r-2) !
\end{aligned}
$$
Now, put value of $n$ from the given choices.
Choice (a) put $n=2 r+1$ in (1)
LHS : $(3 r) !(4 r+2-3 r) !=(3 r) !(r+2) !$
RHS : $(r+2) !(3 r) !$
$$
\Rightarrow \text { LHS }=\text { RHS }
$$

</details>

---

### Q126. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If the 7th term in the binomial expansion of $\left(\frac{3}{\sqrt[3]{84}}+\sqrt{3} \ln x\right)^9, x>0$, is equal to 729 , then $x$ can be:

**Options:**

- **(A)** $e^2$
- **(B)** $e$
- **(C)** $\frac{e}{2}$
- **(D)** $2 e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e$**

**Detailed Solution:**

Let $r+1=7 \Rightarrow r=6$
Given expansion is
$$
\left(\frac{3}{\sqrt[3]{84}}+\sqrt{3} \ln x\right)^9, x>0
$$
We have
$$
\mathrm{T}_{r+1}={ }^n \mathrm{C}_r(x)^{n-r} a^r \text { for }(x+a)^n \text {. }
$$
$\therefore$ According to the question
$$
\begin{aligned}
& 729={ }^9 \mathrm{C}_6\left(\frac{3}{\sqrt[3]{84}}\right)^3 \cdot(\sqrt{3} \ln x)^6 \\
& \Rightarrow 3^6=84 \times \frac{3^3}{84} \times 3^3 \times(6 \ln x) \\
& \Rightarrow(\ln x)^6=1 \Rightarrow(\ln x)^6=(\ln e)^6 \\
& \Rightarrow x=\mathrm{e}
\end{aligned}
$$

</details>

---

### Q127. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `1`

The ratio of the coefficient of $x^{15}$ to the term independent of $x$ in the expansion of $\left(x^2+\frac{2}{x}\right)^{15}$ is:

**Options:**

- **(A)** $7: 16$
- **(B)** $7: 64$
- **(C)** $1: 4$
- **(D)** $1: 32$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $1: 32$**

**Detailed Solution:**

$$
\begin{aligned}
& \mathrm{T}_{r+1}={ }^{15} \mathrm{C}_r\left(x^2\right)^{15-r} \cdot\left(2 x^{-1}\right)^r \\
& ={ }^{15} \mathrm{C}_r \times(2)^r \times x^{30-3 r}
\end{aligned}
$$
For independent term, $30-3 r=0 \Rightarrow r=10$
Hence the term independent of $x$,
$$
\mathrm{T}_{11}={ }^{15} \mathrm{C}_{10} \times(2)^{10}
$$
For term involve $x^{15}, 30-3 r=15 \Rightarrow r=5$
Hence coefficient of $x^{15}={ }^{15} \mathrm{C}_5 \times(2)^5$
Required ratio
$$
\begin{aligned}
& =\frac{{ }^{15} \mathrm{C}_5 \times(2)^5}{{ }^{15} \mathrm{C}_{10} \times(2)^{10}}=\frac{\frac{15 !}{10 ! 5 !}}{\frac{15 !}{5 ! 10 !} \times(2)^5} \\
& =1: 32 \\
&
\end{aligned}
$$

</details>

---

### Q128. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `2`

The middle term in the expansion of $\left(1-\frac{1}{x}\right)^n\left(1-x^n\right)$ in powers of $x$ is

**Options:**

- **(A)** $-{ }^{2 n} \mathrm{C}_{n-1}$
- **(B)** $-{ }^{2 n} \mathrm{C}_n$
- **(C)** ${ }^{2 n} \mathrm{C}_{n-1}$
- **(D)** ${ }^{2 n} \mathrm{C}_n$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) ${ }^{2 n} \mathrm{C}_n$**

**Detailed Solution:**

Given expansion can be re-written as
$$
\left(\frac{x-1}{x}\right)^n \cdot(1-x)^n=(-1)^n x^{-n}(1-x)^{2 n}
$$
Total number of terms will be $2 n+1$ which is odd ( $\because 2 n$ is always even)
$\therefore$ Middle term $=\frac{2 n+1+1}{2}=(n+1)$ th
Now, $T_{r+1}={ }^n C_r(1)^r x^{n-r}$
So, $\frac{{ }^{2 n} C_n \cdot x^{2 n-n}}{x^n \cdot(-1)^n}={ }^{2 n} C_n \cdot(-1)^n$
Middle term is an odd term. So, $n+1$ will be odd.
So, $n$ will be even.
$\therefore$ Required answer is ${ }^{2 n} \mathrm{C}_n$.

</details>

---

### Q129. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `1`

If $n={ }^m C_2$, then the value of ${ }^n C_2$ is given by

**Options:**

- **(A)** $3\left({ }^{m+1} C_4\right)$
- **(B)** ${ }^{m-1} C_4$
- **(C)** ${ }^{m+1} C_4$
- **(D)** $2\left({ }^{m+2} C_4\right)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $3\left({ }^{m+1} C_4\right)$**

**Detailed Solution:**

$n={ }^m \mathrm{C}_2=\frac{m(m-1)}{2}$
Since $m$ and $(m-1)$ are two consecutive natural numbers, therefore their product is an even natural number. So $\frac{m(m-1)}{2}$ is also a natural number.
Now $\frac{m(m-1)}{2}=\frac{m^2-m}{2}$

$$
\begin{aligned}
\therefore & \frac{m(m-1)}{2} \mathrm{C}_2=\frac{\left(\frac{m^2-m}{2}\right)\left(\frac{m^2-m}{2}-1\right)}{2} \\
& =\frac{m(m-1)\left(m^2-m-2\right)}{8} \\
& =\frac{m(m-1)\left[m^2-2 m+m-2\right]}{8} \\
& =\frac{m(m-1)[m(m-2)+1(m-2)]}{8} \\
& =\frac{m(m-1)(m-2)(m+1)}{8}
\end{aligned}
$$
<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/GmFZabZ9BxLMTQm8_bjMZITikozczSvtWUeTCPXDhFE.original.fullsize.png">

</details>

---

### Q130. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The number of terms in the expansion of $\left(y^{1 / 5}+x^{1 / 10}\right)^{55}$, in which powers of $x$ and $y$ are free from radical signs are

**Options:**

- **(A)** $\operatorname{six}$
- **(B)** twelve
- **(C)** seven
- **(D)** five

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\operatorname{six}$**

**Detailed Solution:**

Given expansion is $\left(y^{1 / 5}+x^{1 / 10}\right)^{55}$ The general term is
$$
T_{r+1}={ }^{55} \mathrm{C}_r\left(y^{1 / 5}\right)^{55-r} \cdot\left(x^{\frac{1}{10}}\right)^r
$$

$T_{r+1}$ would free from radical sign if powers of $y$ and $x$ are integers.
i.e. $\frac{55-r}{5}$ and $\frac{r}{10}$ are integer.
$\Rightarrow r$ is multiple of 10 .
Hence, $r=0,10,20,30,40,50$
It is an A.P.
Thus, $50=0+(k-1) 10$ $50=10 k-10 \Rightarrow k=6$
Thus, the six terms of the given expansion in which $x$ and $y$ are free from radical signs.

</details>

---

### Q131. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If $f(y)=1-(y-1)+(y-1)^2-(y-1)^3$ $+\ldots-(y-1)^{17}$ then the coefficient of $y^2$ in it is

**Options:**

- **(A)** ${ }^{17} \mathrm{C}_2$
- **(B)** ${ }^{17} \mathrm{C}_3$
- **(C)** ${ }^{18} \mathrm{C}_2$
- **(D)** ${ }^{18} \mathrm{C}_3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) ${ }^{18} \mathrm{C}_3$**

**Detailed Solution:**

Given function is
$$
\begin{array}{r}
f(y)=1-(y-1)+(y-1)^2-(y-1)^3 \\
+\ldots \ldots \ldots-(y-1)^{17}
\end{array}
$$
In the expansion of $(y-1)^n$
$$
T_{r+1}={ }^n \mathrm{C}_r y^{n-r}(-1)^r
$$
coeff of $y^2$ in $(y-1)^2={ }^2 \mathrm{C}_0$
coeff of $y^2$ in $(y-1)^3={ }^3 \mathrm{C}_1$
coeff of $y^2$ in $(y-1)^4={ }^4 \mathrm{C}_2$
So, coeff of termwise is
$$
\begin{aligned}
& { }^2 \mathrm{C}_0+{ }^3 \mathrm{C}_1+{ }^4 \mathrm{C}_2+{ }^5 \mathrm{C}_3+\ldots \ldots \ldots+{ }^{17} \mathrm{C}_{15} \\
& =1+{ }^3 \mathrm{C}_1+{ }^4 \mathrm{C}_2+{ }^5 \mathrm{C}_3+\ldots \ldots \ldots . .+{ }^{17} \mathrm{C}_{15} \\
& =\left({ }^3 \mathrm{C}_0+{ }^3 \mathrm{C}_1\right)+{ }^4 \mathrm{C}_2+{ }^5 \mathrm{C}_3+\ldots \ldots \ldots . .+{ }^{17} \mathrm{C}_{15} \\
& ={ }^4 \mathrm{C}_1+{ }^4 \mathrm{C}_2+{ }^5 \mathrm{C}_3+\ldots \ldots \ldots+{ }^{17} \mathrm{C}_{15}
\end{aligned}
$$

$$
\begin{aligned}
& ={ }^5 \mathrm{C}_2+{ }^5 \mathrm{C}_3+\ldots \ldots \ldots+{ }^{17} \mathrm{C}_{15} \\
& ={ }^{18} \mathrm{C}_{15}={ }^{18} \mathrm{C}_3
\end{aligned}
$$

</details>

---

### Q132. JEE Main 2011

*Type:* `singleCorrect` | *Level:* `3`

The coefficient of $x^7$ in the expansion of $\left(1-x-x^2+x^3\right)^6$ is

**Options:**

- **(A)** $-132$
- **(B)** $-144$
- **(C)** $132$
- **(D)** $144$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $-144$**

**Detailed Solution:**

$$
\begin{aligned}
& {\left[1-\mathrm{x}-\mathrm{x}^2(1-\mathrm{x})\right]^6=(1-\mathrm{x})^6\left(1-\mathrm{x}^2\right)^6} \\
& =\left[{ }^6 \mathrm{C}_0-{ }^6 \mathrm{C}_1 \mathrm{x}+{ }^6 \mathrm{C}_2 \mathrm{x}^2-{ }^6 \mathrm{C}_3 \mathrm{x}^3+{ }^6 \mathrm{C}_4 \mathrm{x}^4-{ }^6 \mathrm{C}_5 \mathrm{x}^5+{ }^6 \mathrm{C}_6 \mathrm{x}^6\right] \times\left[{ }^6 \mathrm{C}_0-{ }^6 \mathrm{C}_1 \mathrm{x}^2+{ }^6 \mathrm{C}_2 \mathrm{x}^4-{ }^6 \mathrm{C}_3 \mathrm{x}^6+\ldots .\right]
\end{aligned}
$$
Coefficient of $\mathrm{x}^7={ }^6 \mathrm{C}_1{ }^6 \mathrm{C}_3-{ }^6 \mathrm{C}_3{ }^6 \mathrm{C}_2+{ }^6 \mathrm{C}_5{ }^6 \mathrm{C}_1=120-300+36=-144$

</details>

---

### Q133. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `2`

In the binomial expansion of $(a-b)^n, n \geq 5$, the sum of $5^{\text {th }}$ and $6^{\text {th }}$ terms is zero, then $\frac{a}{b}$ equals

**Options:**

- **(A)** $\frac{5}{n-4}$
- **(B)** $\frac{6}{n-5}$
- **(C)** $\frac{n-5}{6}$
- **(D)** $\frac{n-4}{5}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{n-4}{5}$**

**Detailed Solution:**

${ }^n C_4 a^{n-4}(-b)^4+{ }^n C_5 a^{n-5}(-b)^5=0$
$\Rightarrow\left(\frac{a}{b}\right)=\frac{n-5+1}{5}$.

</details>

---

### Q134. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

For natural numbers $m, n$ if $(1-y)^m(1+y)^n=1+a_1 y+a_2 y^2+\ldots$, and $a_1=a_2=10$ then $(\mathrm{m}, \mathrm{n})$ is

**Options:**

- **(A)** (20, 45)
- **(B)** (35, 20)
- **(C)** (45, 35)
- **(D)** (35, 45)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) (35, 45)**

**Detailed Solution:**

$(1-y)^m(1+y)^n=\left[1-{ }^m C_1 y+{ }^m C_2 y^2-\ldots\right]\left[1+{ }^n C_1 y+{ }^n C_2 y^2+\ldots\right]$
$=1+(n-m)+\left\{\frac{m(m-1)}{2}+\frac{n(n-1)}{2}-m n\right\} y^2+\ldots .$.
$\therefore a_1=n-m=10$ and $a_2=\frac{m^2+n-m-n-2 m n}{2}=10$
So, $n-m=10$ and $(m-n)^2-(m+n)=20 \quad \Rightarrow m+n=80$
$$
\therefore \mathrm{m}=35, \quad \mathrm{n}=45
$$

</details>

---

### Q135. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

If the coefficient of $x^7$ in $\left[a x^2+\left(\frac{1}{b x}\right)\right]^{11}$ equals the coefficient of $x^{-7}$ in $\left[a x^2-\left(\frac{1}{b x}\right)\right]^{11}$, then $a$ and $b$ satisfy the relation

**Options:**

- **(A)** $a-b=1$
- **(B)** $a+b=1$
- **(C)** $\frac{a}{b}=1$
- **(D)** $a b=1$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $a b=1$**

**Detailed Solution:**

$$
\begin{aligned}
& T_{r+1} \text { in the expansion }\left[a x^2+\frac{1}{b x}\right]^{11}={ }^{11} C_r\left(a x^2\right)^{11-r}\left(\frac{1}{b x}\right)^r \\
& ={ }^{11} C_r(a)^{11-r}(b)^{-r}(x)^{22-2 r-r} \\
& \Rightarrow 22-3 r=7 \Rightarrow r=5 \\
& \therefore \text { coefficient of } x^7={ }^{11} C_5(a)^6(b)^{-5} ....(i)
\end{aligned}
$$
Again $T_{r+1}$ in the expansion $\left[a x-\frac{1}{b x^2}\right]^{11}={ }^{11} C_r(a x)^{11-r}\left(-\frac{1}{b x^2}\right)^r$ $={ }^{11} \mathrm{C}_{\mathrm{r}} \mathrm{a}^{11-\mathrm{r}}(-1)^{\mathrm{r}} \times(\mathrm{b})^{-\mathrm{r}}(\mathrm{x})^{-2 \mathrm{r}}(\mathrm{x})^{11-\mathrm{r}}$
Now $11-3 r=-7 \Rightarrow 3 r=18 \Rightarrow r=6$
$$
\begin{aligned}
& \therefore \text { coefficient of } x^{-7}={ }^{11} C_6 a^5 \times 1 \times(b)-6 \\
& \Rightarrow{ }^{11} C_5(a)^6(b)^{-5}={ }^{11} C_6 a^5 \times(b)^{-6} \\
& \Rightarrow a b=1
\end{aligned}
$$

</details>

---

### Q136. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `2`

If the coefficients of $r$ th, $(r+1)$ th and $(r+2)$ th terms in the binomial expansion of $(1+$ $y)^m$ are in A.P., then $m$ and $r$ satisfy the equation

**Options:**

- **(A)** $m^2-m(4 r-1)+4 r^2-2=0$
- **(B)** $m^2-m(4 r+1)+4 r^2+2=0$
- **(C)** $m^2-m(4 r+1)+4 r^2-2=0$
- **(D)** $m^2-m(4 r-1)+4 r^2+2=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $m^2-m(4 r+1)+4 r^2-2=0$**

**Detailed Solution:**

Given ${ }^m C,{ }^m C,{ }^m C_{r+1}$ are in A.P.
$$
\begin{aligned}
& 2{ }^m C_r={ }^m C_{r-1}+{ }^m C_{r+1} \\
& \Rightarrow 2=\frac{{ }^m C_{r-1}}{{ }^m C_r}+\frac{{ }^m C_{r+1}}{{ }^m C_r} \\
& =\frac{r}{m-r+1}+\frac{m-r}{r+1} \\
& \Rightarrow m^2-m(4 r+1)+4 r^2-2=0
\end{aligned}
$$

</details>

---

### Q137. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `2`

The coefficient of $x^n$ in expansion of $(1+x)(1-x)^n$ is

**Options:**

- **(A)** $(n-1)$
- **(B)** $(-1)^n(1-n)$
- **(C)** $(-1)^{n-1}(n-1)^2$
- **(D)** $(-1)^{n-1} n$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $(-1)^n(1-n)$**

**Detailed Solution:**

Coefficient of $x^n$ in $(1+x)(1-x)^n=(1+x)\left({ }^n C_0-{ }^n C_1 x+\ldots \ldots .+(-1)^{n-1}{ }^n C_{n-1} x^{n-1}+(-1)^n\right.$
$\left.{ }^n C_n x^n\right)$
$=(-1)^n{ }^n C_n+(-1)^{n-1}{ }^n C_{n-1}=(-1)^n(1-n)$

</details>

---

### Q138. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `1`

The coefficient of the middle term in the binomial expansion in powers of $x$ of $(1+\alpha x)^4$ and of $(1-\alpha x)^6$ is the same if $\alpha$ equals

**Options:**

- **(A)** $-\frac{5}{3}$
- **(B)** $\frac{3}{5}$
- **(C)** $\frac{-3}{10}$
- **(D)** $\frac{10}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{-3}{10}$**

**Detailed Solution:**

Coefficient of Middle term in $(1+\alpha \mathrm{x})^4=\mathrm{t}_3={ }^4 \mathrm{C}_2 \cdot \alpha^2$
Coefficient of Middle term in $(1-\alpha \mathrm{x})^6=\mathrm{t}_4={ }^6 \mathrm{C}_3(-\alpha)^3$
$$
{ }^4 \mathrm{C}_2 \alpha^2=-{ }^6 \mathrm{C}_3 \cdot \alpha^3 \Rightarrow-6=20 \alpha \Rightarrow \alpha=\frac{-3}{10}
$$

</details>

---

### Q139. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

The number of integral terms in the expansion of $(\sqrt{3}+8 \sqrt{5})^{256}$ is

**Options:**

- **(A)** 35
- **(B)** 32
- **(C)** 33
- **(D)** 34

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 33**

**Detailed Solution:**

$\mathrm{T}_{\mathrm{r}+1}={ }^{256} \mathrm{C}_{\mathrm{r}}(\sqrt{3})^{256-\mathrm{r}}(\sqrt[8]{5})^{\mathrm{r}}={ }^{256} \mathrm{C}_{\mathrm{r}}(3)^{\frac{256-\mathrm{r}}{2}}(5)^{\mathrm{r} / 8}$
Terms will be integral if $\frac{256-\mathrm{r}}{2} \& \frac{\mathrm{r}}{8}$ both are +ve integer. As $0 \leq \mathrm{r} \leq 256 \therefore \mathrm{r}=0,8,16,24, \ldots \ldots \ldots \ldots 256$
For above values of $\mathrm{r},\left(\frac{256-\mathrm{r}}{2}\right)$ is also an integer.

</details>

---

### Q140. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `2`

If $\mathrm{x}$ is positive, the first negative term in the expansion of $(1+x)^{27 / 5}$ is

**Options:**

- **(A)** 6th term
- **(B)** 7th term
- **(C)** 5th term
- **(D)** 8th term

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 8th term**

**Detailed Solution:**

$T_{r+1}=\frac{n(n-1)(n-2) \ldots \ldots \ldots(n-r+1)}{r !}(x)^r$
For first negative term, $n-r+1 < 0$ or $r>\frac{32}{5}$
$\therefore \mathrm{r}=7$. Therefore, first negative term is $\mathrm{T}_8$.

</details>

---

### Q141. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

$r$ and $n$ are positive integers $r>1, n>2$ and coefficient of $(r+2)^{\text {th }}$ term and $3 r^{\text {th }}$ term in the expansion of $(1+x)^{2 n}$ are equal, then $n$ equals

**Options:**

- **(A)** 3r
- **(B)** 3r + 1
- **(C)** 2r
- **(D)** 2r + 1

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 2r**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/zofvJp7Yjf71F-kot-YTTnkijPtec6wR_kz21dI9MD8.original.fullsize.png">

</details>

---

### Q142. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the coefficients in the expansion of $(a+b)^n$ is 4096 , then the greatest coefficient in the expansion is

**Options:**

- **(A)** 1594
- **(B)** 792
- **(C)** 924
- **(D)** 2924

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 924**

**Detailed Solution:**

We have $2^n=4096=2^{12} \Rightarrow n=12$; So middle term $=t_7 ; t_7=t_{6+1}={ }^{12} C_6=\frac{12 !}{6 ! 6 !}=924$

</details>

---

### Q143. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `2`

The coefficients of $x^p$ and $x^q$ in the expansion of $(1+x)^{p+q}$ are

**Options:**

- **(A)** equal
- **(B)** equal with opposite signs
- **(C)** reciprocals of each other
- **(D)** none of these

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) equal**

**Detailed Solution:**

We have $t_{p+1}={ }^{p+q} C_p x^p$ and $t_{q+1}={ }^{p+q} C_q x^q \quad{ }^{p+q} C_p={ }^{p+q} C_q$

</details>

---

