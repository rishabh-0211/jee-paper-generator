# JEE Main Mathematics - Sequences and Series

## Topic 7: Summation of Series

**Total Questions:** 125

---

### Q1. JEE Main 2026 (06 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum $1 + \dfrac{1}{2}(1^2 + 2^2) + \dfrac{1}{3}(1^2 + 2^2 + 3^2) + \ldots$ upto 10 terms is equal to :

**Options:**

- **(A)** $130$
- **(B)** $155$
- **(C)** $\dfrac{315}{2}$
- **(D)** $\dfrac{325}{2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\dfrac{315}{2}$**

**Detailed Solution:**

The $n$-th term of the given series is:

$T_n = \dfrac{1}{n} (1^2 + 2^2 + \ldots + n^2)$

Using the formula for the sum of squares of the first $n$ natural numbers:

$T_n = \dfrac{1}{n} \left( \dfrac{n(n+1)(2n+1)}{6} \right) = \dfrac{(n+1)(2n+1)}{6} = \dfrac{2n^2 + 3n + 1}{6}$

The sum of the first 10 terms is $S_{10} = \sum_{n=1}^{10} T_n$

$S_{10} = \dfrac{1}{6} \left( 2 \sum_{n=1}^{10} n^2 + 3 \sum_{n=1}^{10} n + \sum_{n=1}^{10} 1 \right)$

Using the standard summation formulas:

$\sum_{n=1}^{10} n^2 = \dfrac{10 \times 11 \times 21}{6} = 385$

$\sum_{n=1}^{10} n = \dfrac{10 \times 11}{2} = 55$

$\sum_{n=1}^{10} 1 = 10$

Substituting these values into the sum expression:

$S_{10} = \dfrac{1}{6} (2 \times 385 + 3 \times 55 + 10)$

$S_{10} = \dfrac{1}{6} (770 + 165 + 10)$

$S_{10} = \dfrac{945}{6} = \dfrac{315}{2}$

Answer: $\dfrac{315}{2}$

</details>

---

### Q2. JEE Main 2026 (06 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $1^3 - 2^3 + 3^3 - \ldots + 15^3$ is:

**Options:**

- **(A)** $1706$
- **(B)** $1856$
- **(C)** $1982$
- **(D)** $2403$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1856$**

**Detailed Solution:**

The given series is $S = 1^3 - 2^3 + 3^3 - 4^3 + \ldots + 15^3$.

This can be rewritten as the sum of all cubes up to $15$ minus twice the sum of cubes of even numbers up to $14$:

$S = (1^3 + 2^3 + 3^3 + \ldots + 15^3) - 2(2^3 + 4^3 + 6^3 + \ldots + 14^3)$

$S = \sum_{k=1}^{15} k^3 - 2 \times 2^3 (1^3 + 2^3 + 3^3 + \ldots + 7^3)$

$S = \sum_{k=1}^{15} k^3 - 16 \sum_{k=1}^{7} k^3$

Using the formula for the sum of cubes $\sum_{k=1}^{n} k^3 = \left( \dfrac{n(n+1)}{2} \right)^2$:

$\sum_{k=1}^{15} k^3 = \left( \dfrac{15 \times 16}{2} \right)^2 = (120)^2 = 14400$

$\sum_{k=1}^{7} k^3 = \left( \dfrac{7 \times 8}{2} \right)^2 = (28)^2 = 784$

Substituting these values back into the expression for $S$:

$S = 14400 - 16 \times 784$

$S = 14400 - 12544 = 1856$

Answer: $1856$

</details>

---

### Q3. JEE Main 2026 (05 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first $10$ terms of the series $\dfrac{1}{1 + 1^4 \times 4} + \dfrac{2}{1 + 2^4 \times 4} + \dfrac{3}{1 + 3^4 \times 4} + \dfrac{4}{1 + 4^4 \times 4} + \ldots$ is $\dfrac{m}{n}$, $\gcd(m, n) = 1$, then $m + n$ is equal to :

**Options:**

- **(A)** $256$
- **(B)** $264$
- **(C)** $276$
- **(D)** $284$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $276$**

**Detailed Solution:**

The general term of the series is $T_r = \dfrac{r}{1 + 4r^4}$.

Factorizing the denominator:

$1 + 4r^4 = (1 + 2r^2)^2 - 4r^2 = (2r^2 - 2r + 1)(2r^2 + 2r + 1)$

Thus, $T_r = \dfrac{r}{(2r^2 - 2r + 1)(2r^2 + 2r + 1)}$

Multiplying and dividing by $4$:

$T_r = \dfrac{1}{4} \left[ \dfrac{4r}{(2r^2 - 2r + 1)(2r^2 + 2r + 1)} \right]$

$T_r = \dfrac{1}{4} \left[ \dfrac{1}{2r^2 - 2r + 1} - \dfrac{1}{2r^2 + 2r + 1} \right]$

The sum of the first $10$ terms is:

$S_{10} = \sum_{r=1}^{10} T_r = \dfrac{1}{4} \sum_{r=1}^{10} \left( \dfrac{1}{2r^2 - 2r + 1} - \dfrac{1}{2(r+1)^2 - 2(r+1) + 1} \right)$

This is a telescoping series, so all intermediate terms cancel out:

$S_{10} = \dfrac{1}{4} \left[ \left( \dfrac{1}{1} - \dfrac{1}{5} \right) + \left( \dfrac{1}{5} - \dfrac{1}{13} \right) + \ldots + \left( \dfrac{1}{2(10)^2 - 2(10) + 1} - \dfrac{1}{2(10)^2 + 2(10) + 1} \right) \right]$

$S_{10} = \dfrac{1}{4} \left[ 1 - \dfrac{1}{221} \right] = \dfrac{1}{4} \left( \dfrac{220}{221} \right) = \dfrac{55}{221}$

Given $S_{10} = \dfrac{m}{n}$ and $\gcd(m, n) = 1$.

Here, $m = 55$ and $n = 221$. Since $55 = 5 \times 11$ and $221 = 13 \times 17$, $\gcd(55, 221) = 1$.

Therefore, $m + n = 55 + 221 = 276$.

Answer: $276$

</details>

---

### Q4. JEE Main 2026 (05 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$\displaystyle\sum_{n=1}^{10} \left( \dfrac{528}{n(n+1)(n+2)} \right)$ is equal to:

**Options:**

- **(A)** $65$
- **(B)** $130$
- **(C)** $220$
- **(D)** $440$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $130$**

**Detailed Solution:**

Let $T_n = \dfrac{528}{n(n+1)(n+2)}$

$T_n = \dfrac{528}{2} \left( \dfrac{(n+2) - n}{n(n+1)(n+2)} \right)$

$T_n = 264 \left( \dfrac{1}{n(n+1)} - \dfrac{1}{(n+1)(n+2)} \right)$

The sum of the first $10$ terms is given by:

$S_{10} = \displaystyle\sum_{n=1}^{10} T_n = 264 \displaystyle\sum_{n=1}^{10} \left( \dfrac{1}{n(n+1)} - \dfrac{1}{(n+1)(n+2)} \right)$

This is a telescoping series, so most terms cancel out:

$S_{10} = 264 \left( \left( \dfrac{1}{1 \cdot 2} - \dfrac{1}{2 \cdot 3} \right) + \left( \dfrac{1}{2 \cdot 3} - \dfrac{1}{3 \cdot 4} \right) + \dots + \left( \dfrac{1}{10 \cdot 11} - \dfrac{1}{11 \cdot 12} \right) \right)$

$S_{10} = 264 \left( \dfrac{1}{2} - \dfrac{1}{11 \cdot 12} \right)$

$S_{10} = 264 \left( \dfrac{1}{2} - \dfrac{1}{132} \right)$

$S_{10} = 264 \left( \dfrac{66 - 1}{132} \right)$

$S_{10} = 264 \times \dfrac{65}{132}$

$S_{10} = 2 \times 65 = 130$

Answer: $130$

</details>

---

### Q5. JEE Main 2026 (02 April Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum $\dfrac{1^3}{1} + \dfrac{1^3 + 2^3}{1 + 3} + \dfrac{1^3 + 2^3 + 3^3}{1 + 3 + 5} + \cdots$ up to 8 terms, is:

**Options:**

- **(A)** $70$
- **(B)** $71$
- **(C)** $72$
- **(D)** $73$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $71$**

**Detailed Solution:**

The $n$-th term of the given series is:

$T_n = \dfrac{1^3 + 2^3 + \cdots + n^3}{1 + 3 + 5 + \cdots + (2n - 1)}$

Using the formulas for the sum of cubes of first $n$ natural numbers and the sum of first $n$ odd numbers:

$T_n = \dfrac{\left( \dfrac{n(n+1)}{2} \right)^2}{n^2} = \dfrac{n^2(n+1)^2}{4n^2} = \dfrac{(n+1)^2}{4}$

The sum of the series up to 8 terms is:

$S_8 = \sum_{n=1}^{8} T_n = \sum_{n=1}^{8} \dfrac{(n+1)^2}{4}$

$S_8 = \dfrac{1}{4} \left( 2^2 + 3^2 + \cdots + 9^2 \right)$

$S_8 = \dfrac{1}{4} \left( \sum_{k=1}^{9} k^2 - 1^2 \right)$

Using the formula $\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$:

$S_8 = \dfrac{1}{4} \left( \dfrac{9 \times 10 \times 19}{6} - 1 \right)$

$S_8 = \dfrac{1}{4} (285 - 1) = \dfrac{284}{4} = 71$

Answer: $71$

</details>

---

### Q6. JEE Main 2026 (02 April Shift 1)

*Type:* `numerical` | *Level:* `2`

If $\displaystyle\sum_{k=1}^{n} a_k = 6n^3$, then $\displaystyle\sum_{k=1}^{6} \left(\dfrac{a_{k+1} - a_k}{36}\right)^2$ is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **91**

**Detailed Solution:**

Given $\displaystyle\sum_{k=1}^{n} a_k = 6n^3$.

Let $S_n = 6n^3$. The $n$-th term of the sequence is given by $a_n = S_n - S_{n-1}$.

$a_n = 6n^3 - 6(n-1)^3$

$a_n = 6[n^3 - (n^3 - 3n^2 + 3n - 1)]$

$a_n = 6(3n^2 - 3n + 1)$

Replacing $n$ with $k$ and $k+1$, we get:

$a_k = 6(3k^2 - 3k + 1)$

$a_{k+1} = 6(3(k+1)^2 - 3(k+1) + 1) = 6(3k^2 + 3k + 1)$

Now, find the difference $a_{k+1} - a_k$:

$a_{k+1} - a_k = 6(3k^2 + 3k + 1) - 6(3k^2 - 3k + 1)$

$a_{k+1} - a_k = 6(6k) = 36k$

Substitute this into the given summation:

$\displaystyle\sum_{k=1}^{6} \left(\dfrac{a_{k+1} - a_k}{36}\right)^2 = \sum_{k=1}^{6} \left(\dfrac{36k}{36}\right)^2$

$\Rightarrow \displaystyle\sum_{k=1}^{6} k^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2$

Using the formula for the sum of squares of the first $n$ natural numbers, $\displaystyle\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$:

$\displaystyle\sum_{k=1}^{6} k^2 = \dfrac{6(6+1)(2(6)+1)}{6} = \dfrac{6 \times 7 \times 13}{6} = 91$

Answer: $91$

</details>

---

### Q7. JEE Main 2026 (02 April Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\alpha, \alpha + 2, \alpha \in \mathbb{Z}$, be the roots of the quadratic equation $x(x+2) + (x+1)(x+3) + (x+2)(x+4) + \ldots + (x+n-1)(x+n+1) = 4n$ for some $n \in \mathbb{N}$. Then $n + \alpha$ is equal to :

**Options:**

- **(A)** $0$
- **(B)** $1$
- **(C)** $2$
- **(D)** $3$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $2$**

**Detailed Solution:**

The given equation is:

$\sum_{k=0}^{n-1} (x+k)(x+k+2) = 4n$

Expanding the terms inside the summation:

$\sum_{k=0}^{n-1} (x^2 + 2(k+1)x + k(k+2)) = 4n$

Summing each term separately:

$n x^2 + 2x \sum_{k=0}^{n-1} (k+1) + \sum_{k=0}^{n-1} (k^2 + 2k) = 4n$

Using the standard summation formulas:

$n x^2 + 2x \dfrac{n(n+1)}{2} + \dfrac{(n-1)n(2n-1)}{6} + 2 \dfrac{(n-1)n}{2} = 4n$

$n x^2 + n(n+1)x + \dfrac{n(n-1)(2n+5)}{6} = 4n$

Since $n \in \mathbb{N}$, dividing the entire equation by $n$ gives:

$x^2 + (n+1)x + \dfrac{(n-1)(2n+5)}{6} - 4 = 0$

The roots of this quadratic equation are given as $\alpha$ and $\alpha + 2$.

Using the sum of the roots:

$\alpha + (\alpha + 2) = -(n+1)$

$2\alpha + 2 = -n - 1 \Rightarrow n = -2\alpha - 3$

Using the product of the roots:

$\alpha(\alpha + 2) = \dfrac{(n-1)(2n+5)}{6} - 4$

Substituting $n = -2\alpha - 3$ into the product equation:

$\alpha^2 + 2\alpha = \dfrac{(-2\alpha - 4)(-4\alpha - 1)}{6} - 4$

$6(\alpha^2 + 2\alpha) = 8\alpha^2 + 18\alpha + 4 - 24$

$6\alpha^2 + 12\alpha = 8\alpha^2 + 18\alpha - 20$

$2\alpha^2 + 6\alpha - 20 = 0$

$\alpha^2 + 3\alpha - 10 = 0$

$(\alpha + 5)(\alpha - 2) = 0$

Thus, $\alpha = -5$ or $\alpha = 2$.

If $\alpha = 2$, then $n = -2(2) - 3 = -7$, which is rejected since $n \in \mathbb{N}$.

If $\alpha = -5$, then $n = -2(-5) - 3 = 7$, which is valid.

Therefore, $n + \alpha = 7 + (-5) = 2$.

Answer: $2$

</details>

---

### Q8. JEE Main 2026 (28 January Shift 2)

*Type:* `numerical` | *Level:* `2`

If $\sum_{r=1}^{25}\left(\frac{r}{r^{4}+r^{2}+1}\right)=\frac{p}{q}$, where $p$ and $q$ are positive integers such that $\operatorname{gcd}(p, q)=1$, then $p+q$ is equal to $\_\_\_\_$。

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **976**

**Detailed Solution:**

$S = \sum \dfrac{r}{(r^2 + r + 1)(r^2 - r + 1)}$
$= \dfrac{1}{2} \sum_{r=1}^{25} \left( \dfrac{1}{r^2 - r + 1} - \dfrac{1}{r^2 + r + 1} \right)$
$= \dfrac{1}{2} \left[ \left( \dfrac{1}{1} - \dfrac{1}{3} \right) + \left( \dfrac{1}{3} - \dfrac{1}{7} \right) + \ldots + \left( \dfrac{1}{601} - \dfrac{1}{651} \right) \right]$
$= \dfrac{1}{2} \left[ \dfrac{1}{1} - \dfrac{1}{651} \right]$
$= \dfrac{1}{2} \left[ \dfrac{650}{651} \right] = \dfrac{325}{651}$
$\dfrac{p}{q} = \dfrac{325}{651} \Rightarrow p + q = 976$

</details>

---

### Q9. JEE Main 2026 (28 January Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The value of $\sum_{k=1}^{\infty}(-1)^{k+1}\left(\frac{k(k+1)}{k!}\right)$ is

**Options:**

- **(A)** 2/e
- **(B)** $1 / \mathrm{e}$
- **(C)** $\mathrm{e} / 2$
- **(D)** $\sqrt{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $1 / \mathrm{e}$**

**Detailed Solution:**

Evaluate $\sum_{k=1}^{\infty} (-1)^{k+1} \frac{k(k+1)}{k!}$.
Rewrite as $\sum_{k=1}^{\infty} (-1)^{k+1} \frac{k+1}{(k-1)!}$ and split: $\sum_{k=1}^{\infty} (-1)^{k+1} \frac{k}{(k-1)!} + \sum_{k=1}^{\infty} (-1)^{k+1} \frac{1}{(k-1)!}$.
The first sum, after rewriting $\frac{k}{(k-1)!} = \frac{1}{(k-2)!} + \frac{1}{(k-1)!}$ for $k \geq 2$, evaluates to 0 using the exponential series $\sum_{j=0}^{\infty} \frac{(-1)^j}{j!} = e^{-1}$.
The second sum with substitution $j = k-1$ gives $\sum_{j=0}^{\infty} (-1)^j \frac{1}{j!} = e^{-1} = \frac{1}{e}$.
Therefore, the total is $0 + \frac{1}{e} = \frac{1}{e}$.

</details>

---

### Q10. JEE Main 2026 (21 January Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The positive integer n, for which the solutions of the equation $x(x+2)+(x+2)(x+4)+\cdots+(x+2 n-2)(x+2 n)=\frac{8 n}{3}$ are two consecutive even integers, is :

**Options:**

- **(A)** 3
- **(B)** 12
- **(C)** 9
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 3**

**Detailed Solution:**

The sum has $n$ terms: $\sum_{k=1}^{n}(x+2k-2)(x+2k)$.
Expanding and summing gives $nx^2 + 2n^2x + \frac{4n(n^2-1)}{3} = \frac{8n}{3}$.
Dividing by $n$ and simplifying: $3x^2 + 6nx + 4n^2 - 12 = 0$.
Discriminant $= 36n^2 - 12(4n^2 - 12) = 12(12 - n^2)$.
Difference of roots $= \frac{2\sqrt{3(12-n^2)}}{3}$.
For two consecutive even integers, this difference $= 2$.
$\sqrt{36 - 3n^2} = 3 \Rightarrow n^2 = 9 \Rightarrow n = 3$.
For $n = 3$: $x = \frac{-9 \pm 3}{3} = -2$ or $-4$, which are consecutive even integers.

</details>

---

### Q11. JEE Main 2026 (21 January Shift 1)

*Type:* `numerical` | *Level:* `3`

Let $a_{1}=1$ and for $n \geqslant 1, a_{n+1}=\frac{1}{2} a_{n}+\frac{n^{2}-2 n-1}{n^{2}(n+1)^{2}}$. Then $\left|\sum_{n=1}^{\infty}\left(a_{n}-\frac{2}{n^{2}}\right)\right|$ is equal to $\_\_\_\_$.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **2**

**Detailed Solution:**

Let $b_n = a_n - \frac{2}{n^2}$.
$b_{n+1} = \frac{1}{2}a_n + \frac{n^2-2n-1}{n^2(n+1)^2} - \frac{2}{(n+1)^2}$.
Simplifying: $b_{n+1} = \frac{1}{2}b_n + \frac{(n+1)^2 + n^2 - 2n - 1 - 2n^2}{n^2(n+1)^2} = \frac{1}{2}b_n$.
So $b_n$ is GP with ratio $\frac{1}{2}$.
$b_1 = 1 - 2 = -1$, so $b_n = -\left(\frac{1}{2}\right)^{n-1}$.
$\sum_{n=1}^{\infty} b_n = -\frac{1}{1-\frac{1}{2}} = -2$.
$\left|\sum_{n=1}^{\infty}\left(a_n - \frac{2}{n^2}\right)\right| = 2$.

</details>

---

### Q12. JEE Main 2025 (8 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

$\begin{aligned}
& \text { If } \frac{1}{1^4}+\frac{1}{2^4}+\frac{1}{3^4}+\ldots . . \infty=\frac{\pi^4}{90}, \\
& \frac{1}{1^4}+\frac{1}{3^4}+\frac{1}{5^4}+\ldots . . \infty=\alpha, \\
& \frac{1}{2^4}+\frac{1}{4^4}+\frac{1}{6^4}+\ldots . \infty=\beta,
\end{aligned}$
then $\frac{\alpha}{\beta}$ is equal to

**Options:**

- **(A)** 23
- **(B)** 18
- **(C)** 15
- **(D)** 14

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 15**

**Detailed Solution:**

If $\frac{1}{1^4}+\frac{1}{2^4}+\frac{1}{3^4}+\ldots . . \infty=\frac{\pi^4}{90}....(i)$
$\begin{aligned} & \beta=\frac{1}{2^4}+\frac{1}{4^4}+\frac{1}{6^4}+\ldots, \\ & =\frac{1}{16}\left[\frac{1}{1^4}+\frac{1}{2^4}+\frac{1}{3^4}+\ldots . .\right],\end{aligned}$
$=\frac{1}{16} \times \frac{\pi^4}{90}$
using (ii) ________...(ii)
$\begin{aligned} & \alpha=\frac{1}{1^4}+\frac{1}{3^4}+\frac{1}{5^4}+\ldots . . \infty \\ & \left(\frac{1}{1^4}+\frac{1}{2^4}+\frac{1}{3^4}+\frac{1}{4^4}+\frac{1}{5^4}+\ldots . .\right) \\ & -\left(\frac{1}{2^4}+\frac{1}{4^4}+\frac{1}{6^4}+\ldots . .\right)\end{aligned}$
$\alpha=\frac{\pi^4}{90}-\frac{1}{16} \times \frac{\pi^4}{90} \quad[$ using (i) and (ii)]
$\begin{aligned} & \alpha=\frac{16-1}{16 \times 90} \times \pi^4=\frac{15}{16 \times 90} \pi^4=\frac{\pi^4}{96} \\ & \therefore \frac{\alpha}{\beta}=\frac{\frac{\pi^4}{96}}{\frac{\pi^4}{16 \times 90}}=\frac{16 \times 90}{96}=15\end{aligned}$

</details>

---

### Q13. JEE Main 2025 (4 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first 20 terms of the series
$\frac{4.1}{4+3.1^2+1^4}+\frac{4.2}{4+3.2^2+2^4}+\frac{4.3}{4+3.3^2+3^4}+\frac{4.4}{4+3.4^2+4^4}+\ldots$
is $\frac{m}{n}$, where $m$ and $n$ are coprime, then $m+n$ is equal to :-

**Options:**

- **(A)** $423$
- **(B)** $420$
- **(C)** $421$
- **(D)** $422$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $421$**

**Detailed Solution:**

$\begin{aligned} & \sum_{\mathrm{r}=1}^{20} \frac{4 \mathrm{r}}{4+3 \mathrm{r}^2+\mathrm{r}^4} \\ & \sum_{\mathrm{r}=1}^{20} \frac{4 \mathrm{r}}{\left(\mathrm{r}^2+\mathrm{r}+2\right)\left(\mathrm{r}^2-\mathrm{r}+2\right)} \\ & 2 \sum_{\mathrm{r}=1}^{20}\left(\frac{1}{\mathrm{r}^2-\mathrm{r}+2}-\frac{1}{\mathrm{r}^2+\mathrm{r}+2}\right) \\ & 2\left(\frac{1}{2}-\frac{1}{4}\right) \\ & \frac{1}{4}-\frac{1}{8} \\ & \frac{1}{8}-\frac{1}{14} \\ & \left(\frac{1}{382}-\frac{1}{422}\right) \\ & =2\left(\frac{1}{2}-\frac{1}{422}\right) \\ & =\frac{420}{422} \\ & =\frac{210}{211} \\ & \text { option }(3)\end{aligned}$

</details>

---

### Q14. JEE Main 2025 (4 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

$1+3+5^2+7+9^2+\ldots$ upto 40 terms is equal to

**Options:**

- **(A)** 43890
- **(B)** 41880
- **(C)** 33980
- **(D)** 40870

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 41880**

**Detailed Solution:**

$\left(1^2+5^2+9^2+\ldots \ldots \text { upto } 20 \text { terms }\right)+(3+7+11+$...upto 20 terms)
$\begin{aligned}
& =\sum_{\mathrm{r}=1}^{20}(4 \mathrm{r}-3)^2+\sum_{\mathrm{r}=1}^{20}(4 \mathrm{r}-1) \\
& =\sum_{\mathrm{r}=1}^{20}(4 \mathrm{r}-3)^2+(4 \mathrm{r}-1) \\
& =4 \sum_{\mathrm{r}=1}^{20}\left(4 \mathrm{r}^2-5 \mathrm{r}+2\right) \\
& =16 \sum_{\mathrm{r}=1}^{20} \mathrm{r}^2-20 \sum_{\mathrm{r}=1}^{20} \mathrm{r}+8 \sum_{\mathrm{r}=1}^{20} 1=41880
\end{aligned}$

</details>

---

### Q15. JEE Main 2025 (3 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum $1+\frac{1+3}{2!}+\frac{1+3+5}{3!}+\frac{1+3+5+7}{4!}+\ldots$ upto $\infty$ terms, is equal to

**Options:**

- **(A)** $6 e$
- **(B)** $4 e$
- **(C)** $3 e$
- **(D)** $2 e$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2 e$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{S}=1+\frac{1+3}{2!}+\frac{1+3+5}{3!}+\ldots \\ & =\sum_{\mathrm{r}=1}^{\infty} \frac{\mathrm{r}^2}{\mathrm{r}!} \\ & =\sum_{\mathrm{r}=1}^{\infty} \frac{(\mathrm{r}-1+1)}{(\mathrm{r}-1)!}=\sum_{\mathrm{r}=2}^{\infty} \frac{1}{(\mathrm{r}-2)!}+\sum_{\mathrm{r}=1}^{\infty} \frac{1}{(\mathrm{r}-1)!} \\ & =2 \mathrm{e}\end{aligned}$

</details>

---

### Q16. JEE Main 2025 (3 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum $1+3+11+25+45+71+.$. upto 20 terms, is equal to

**Options:**

- **(A)** $7240$
- **(B)** $7130$
- **(C)** $6982$
- **(D)** $8124$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $7240$**

**Detailed Solution:**

Given sum is
$S_n=1+3+11+25+45+71+\ldots+T_n$
First order differences are in A.P.
Thus, we can assume that
$\mathrm{T}_{\mathrm{n}}=\mathrm{an}^2+\mathrm{bn}+\mathrm{c}$
Solving $\left\{\begin{array}{c}T_1=1=a+b+c \\ T_2=3=4 a+2 b+c \\ T_3=11=9 a+3 b+c\end{array}\right\}$,
we get $\mathrm{a}=3, \mathrm{~b}=-7, \mathrm{c}=5$
Hence, general term of given series is
$\mathrm{T}_{\mathrm{n}}=3 \mathrm{n}^2-7 \mathrm{n}+5$
Hence, required sum equals
$\sum_{\mathrm{n}=1}^{\mathrm{n}=20}\left(3 \mathrm{n}^2-7 \mathrm{n}+5\right)=3\left(\frac{20 \cdot 21 \cdot 41}{6}\right)-7\left(\frac{20 \cdot 21}{2}\right)+5(20)=7240$

</details>

---

### Q17. JEE Main 2025 (2 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If the sum of the first 10 terms of the series $\frac{4.1}{1+4.1^4}+\frac{4.2}{1+4.2^4}+\frac{4.3}{1+4.3^4}+\ldots$ is $\frac{m}{n}$, where $\operatorname{gcd}(m, n)=1$, then $m+n$ is equal to______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **441**

**Detailed Solution:**

$\begin{aligned} & \mathrm{T}_{\mathrm{r}}=\frac{4 . \mathrm{r}}{1+4 . \mathrm{r}^4} \\ & \mathrm{~T}_{\mathrm{r}}=\frac{4 . \mathrm{r}}{\left(2 \mathrm{r}^2+2 \mathrm{r}+1\right)\left(2 \mathrm{r}^2-2 \mathrm{r}+1\right)} \\ & \mathrm{T}_{\mathrm{r}}=\frac{\left(2 \mathrm{r}^2+2 \mathrm{r}+1\right)-\left(2 \mathrm{r}^2-2 \mathrm{r}+1\right)}{\left(2 \mathrm{r}^2+2 \mathrm{r}+1\right)\left(2 \mathrm{r}^2-2 \mathrm{r}+1\right)}\end{aligned}$
$\begin{aligned} & \mathrm{T}_{\mathrm{r}}=\frac{1}{2 \mathrm{r}^2-2 \mathrm{r}+1}-\frac{1}{2 \mathrm{r}^2+2 \mathrm{r}+1} \\ & \mathrm{~T}_1=\frac{1}{1}-\frac{1}{5} \\ & \mathrm{~T}_2=\frac{1}{5}-\frac{1}{13}\end{aligned}$
$\begin{aligned} & \mathrm{T}_{10}=\frac{1}{181}-\frac{1}{221} \\ & \mathrm{~S}_{10}=1-\frac{1}{221}=\frac{220}{221}=\frac{\mathrm{m}}{\mathrm{n}} \\ & \mathrm{m}+\mathrm{n}=441\end{aligned}$

</details>

---

### Q18. JEE Main 2025 (29 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The value of \(\lim _{n \rightarrow \infty}\left(\sum_{k=1}^n \frac{k^3+6 k^2+11 k+5}{(k+3)!}\right)\) is:

**Options:**

- **(A)** \(4 / 3\)
- **(B)** 2
- **(C)** \(7 / 3\)
- **(D)** \(5 / 3\)

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) \(5 / 3\)**

**Detailed Solution:**

$\begin{aligned} & \lim _{n \rightarrow \infty} \sum_{k=1}^n \frac{k^3+6 k^2+11 k+5}{(k+3)!} \\ & =\lim _{n \rightarrow \infty} \sum_{k=1}^n \frac{k^3+6 k^2+11 k+6-1}{(k+3)!} \\ & =\lim _{n \rightarrow \infty} \sum_{k=1}^n \frac{(k+1)(k+2)(k+3)-1}{(k+3)!} \\ & =\lim _{n \rightarrow \infty} \sum_{k=1}^n \frac{(k+1)(k+2)(k+3)}{(k+3)!}-\frac{1}{(k+3)!} \\ & =\lim _{k=1} \sum_{k=1}^n\left(\frac{1}{k!}-\frac{1}{(k+3)!}\right)\end{aligned}$


$\begin{aligned} & =\lim _{k=1}\left(\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!} \ldots+\frac{1}{n!}-\frac{1}{4!}-\frac{1}{5!}-\frac{1}{6!} \ldots .-\frac{1}{(n+3)!}\right) \\ & \quad=\frac{1}{1}+\frac{1}{2}+\frac{1}{6}=\frac{10}{6}=\frac{5}{3}\end{aligned}$

</details>

---

### Q19. JEE Main 2025 (28 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

For positive integers $n$, if $4 a_n=\left(n^2+5 n+6\right)$ and $S_n=\sum_{k=1}^n\left(\frac{1}{a_k}\right)$, then the value of $507 S_{2025}$ is :

**Options:**

- **(A)** $540$
- **(B)** $675$
- **(C)** $1350$
- **(D)** $135$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $675$**

**Detailed Solution:**

$\begin{aligned} & S_n=\sum_{k=1}^n \frac{4}{K^2+5 k+6} \\ & =\sum_{k=1}^n \frac{4}{(K+2)(K+3)}=4 \sum_{K=1}^n\left(\frac{1}{K+2}-\frac{1}{K+3}\right)\end{aligned}$
$\begin{aligned} & =4\left[\frac{1}{3}-\frac{1}{4}\right] \\ & =4\left[\frac{1}{4}-\frac{1}{5}\right] \\ & =4\left[\frac{1}{n+2}-\frac{1}{n+3}\right] \\ & S_n=4\left[\frac{1}{3}-\frac{1}{n+3}\right]\end{aligned}$
$\begin{aligned} & S_{2025}=4\left[\frac{1}{3}-\frac{1}{2028}\right] \\ & S_{2025}=4\left[\frac{675}{2028}\right] \\ & 507 S_{2025}=675\end{aligned}$

</details>

---

### Q20. JEE Main 2025 (28 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

Let $\left\langle a_{\mathrm{n}}\right\rangle$ be a sequence such that $a_0=0, a_1=\frac{1}{2}$ and $2 a_{\mathrm{n}+2}=5 a_{\mathrm{n}+1}-3 a_{\mathrm{n}}, \mathrm{n}=0,1,2,3, \ldots$. Then $\sum_{\mathrm{k}=1}^{100} a_k$ is equal to

**Options:**

- **(A)** $3 \mathrm{a}_{99}-100$
- **(B)** $3 \mathrm{a}_{100}-100$
- **(C)** $3 \mathrm{a}_{99}+100$
- **(D)** $3 \mathrm{a}_{100}+100$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $3 \mathrm{a}_{100}-100$**

**Detailed Solution:**

$\begin{aligned} & a_0=0, a_1=\frac{1}{2} \\ & 2 a_{n+2}=5 a_{n+1}-3 a_n \\ & 2 x^2-5 x+3=0 \Rightarrow x=1,3 / 2 \\ & \therefore a_n=A l^n+B\left(\frac{3}{2}\right)^n\end{aligned}$


$\left.\begin{array}{ll}\mathrm{n}=0 & 0=\mathrm{A}+\mathrm{B} \\ \mathrm{n}=1 & \frac{1}{2}=\mathrm{A}+\frac{3}{2} \mathrm{~B}\end{array}\right] \begin{aligned} & \mathrm{A}=-1 \\ & \mathrm{~B}=1\end{aligned}$


$\begin{aligned} & \Rightarrow \mathrm{a}_{\mathrm{n}}=-1+\left(\frac{3}{2}\right)^{\mathrm{n}} \\ & \sum_{\mathrm{k}=1}^{100} \mathrm{a}_{\mathrm{k}}=\sum_{\mathrm{k}=1}^{100}(-1)+\left(\frac{3}{2}\right)^{\mathrm{k}}\end{aligned}$
$\begin{aligned} & =-100+\frac{\left(\frac{3}{2}\right)\left(\left(\frac{3}{2}\right)^{100}-1\right)}{\frac{3}{2}-1} \\ & =-100+3\left(\left(\frac{3}{2}\right)^{100}-1\right) \\ & =3 \cdot\left(\mathrm{a}_{100}\right)-100\end{aligned}$

</details>

---

### Q21. JEE Main 2025 (24 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let $S_n=\frac{1}{2}+\frac{1}{6}+\frac{1}{12}+\frac{1}{20}+\ldots$ upto $n$ terms. If the sum of the first six terms of an A.P. with first term -p and common difference p is $\sqrt{2026 \mathrm{~S}_{2025}}$, then the absolute difference betwen $20^{\text {th }}$ and $15^{\text {th }}$ terms of the A.P. is

**Options:**

- **(A)** $20$
- **(B)** $90$
- **(C)** $45$
- **(D)** $25$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $25$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{Sn}=\frac{1}{2}+\frac{1}{6}+\frac{1}{12}+\frac{1}{20} \ldots . \mathrm{N} \text { terms } \\ & \mathrm{S}_{2025}=\sum_{\mathrm{n}=1}^{2025} \frac{1}{\mathrm{n}(\mathrm{n}+1)}=\sum_{\mathrm{n}=1}^{2025}\left(\frac{1}{\mathrm{n}}-\frac{1}{\mathrm{n}+1}\right) \\ & =\left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right) \quad \ldots \cdots\left(\frac{1}{2025}-\frac{1}{2026}\right)\end{aligned}$


$\begin{aligned}
& =\frac{2025}{2026} \\
& \sqrt{2026 . \mathrm{S}_{2025}}=\sqrt{2025}=45
\end{aligned}$

Given : $\frac{6}{2}[-2 p+(6-1) p]=45$
$\begin{aligned}
& 9 \mathrm{p}=45 \\
& \mathrm{p}=5 \\
& \left|\mathrm{~A}_{20}-\mathrm{A}_{15}\right|=|-5+19 \times 5|-[-5+14 \times 5] \\
& =|90-65| \\
& =25
\end{aligned}$

</details>

---

### Q22. JEE Main 2025 (22 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If $\sum_{r=1}^n T_r=\frac{(2 n-1)(2 n+1)(2 n+3)(2 n+5)}{64}$, then $\lim _{n \rightarrow \infty} \sum_{r=1}^n\left(\frac{1}{T_r}\right)$ is equal to :

**Options:**

- **(A)** $0$
- **(B)** $\frac{2}{3}$
- **(C)** $1$
- **(D)** $\frac{1}{3}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{2}{3}$**

**Detailed Solution:**

$\begin{aligned} & \mathrm{T}_{\mathrm{n}}=\mathrm{S}_{\mathrm{n}}-\mathrm{S}_{\mathrm{n}-1} \\ & \Rightarrow \mathrm{~T}_{\mathrm{n}}=\frac{1}{8}(2 \mathrm{n}-1)(2 \mathrm{n}+1)(2 \mathrm{n}+3) \\ & \Rightarrow \frac{1}{\mathrm{~T}_{\mathrm{n}}}=\frac{8}{(2 \mathrm{n}-1)(2 \mathrm{n}+1)(2 \mathrm{n}+3)} \\ & \lim _{\mathrm{n} \rightarrow \infty} \sum_{\mathrm{r}=1}^{\mathrm{n}} \frac{1}{\mathrm{~T}_{\mathrm{r}}}=\lim _{\mathrm{n} \rightarrow \infty} 8 \sum_{\mathrm{r}=1}^{\mathrm{n}} \frac{1}{(2 \mathrm{n}-1)(2 \mathrm{n}+1)(2 \mathrm{n}+3)} \\ & =\lim _{\mathrm{n} \rightarrow \infty} \frac{8}{4} \sum\left(\frac{1}{(2 \mathrm{n}-1)(2 \mathrm{n}+1)}-\frac{1}{(2 \mathrm{n}+1)(2 \mathrm{n}+3)}\right) \\ & =\lim _{\mathrm{n} \rightarrow \infty} 2\left[\left(\frac{1}{1.3}-\frac{1}{3.5}\right)+\left(\frac{1}{3.5}-\frac{1}{5.7}\right)+\ldots\right] \\ & =\frac{2}{3}\end{aligned}$

</details>

---

### Q23. JEE Main 2024 (09 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\left(\frac{1}{\alpha+1}+\frac{1}{\alpha+2}+\ldots \ldots+\frac{1}{\alpha+1012}\right)-\left(\frac{1}{2 \cdot 1}+\frac{1}{4 \cdot 3}+\frac{1}{6 \cdot 5}+\ldots . .+\frac{1}{2024 \cdot 2023}\right)=\frac{1}{2024}$, then $\alpha$ is equal to________

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1011**

**Detailed Solution:**

$\begin{aligned} & \left(\frac{1}{\alpha+1}+\frac{1}{\alpha+2}+\ldots+\frac{1}{\alpha+2012}\right) \\ & -\left\{\left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)+\ldots+\left(\frac{1}{2023}-\frac{1}{2024}\right)\right\}=\frac{1}{2024} \\ & \Rightarrow\left(\frac{1}{\alpha+1}+\frac{1}{\alpha+2}+\ldots+\frac{1}{\alpha+2012}\right) \\ & -\left\{\left(\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}\right)+\ldots+\frac{1}{2023}\right. \\ & \left.-\frac{1}{2024}-2\left(\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2022}\right)\right\}=\frac{1}{2024} \\ & \end{aligned}$
$\begin{aligned} & \Rightarrow\left(\frac{1}{\alpha+1}+\frac{1}{\alpha+2}+\ldots+\frac{1}{\alpha+2012}\right) \\ & \quad-\left(\frac{1}{1}+\frac{1}{2}+\ldots+\frac{1}{2023}\right) \\ & \quad+\frac{1}{2024}+\left(\frac{1}{1}+\frac{1}{2}+\ldots+\frac{1}{1011}\right)=\frac{1}{2024} \\ & \Rightarrow \frac{1}{\alpha+1}+\frac{1}{\alpha+2}+\ldots+\frac{1}{\alpha+2012} \\ & \quad=\frac{1}{1012}+\frac{1}{1013}+\ldots+\frac{1}{2023} \\ & \Rightarrow \alpha=1011\end{aligned}$

</details>

---

### Q24. JEE Main 2024 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If the set $R=\{(a, b): a+5 b=42, a, b \in \mathbb{N}\}$ has $m$ elements and $\sum_{n=1}^m\left(1-i^{n !}\right)=x+i y$, where $i=\sqrt{-1}$, then the value of $m+x+y$ is

**Options:**

- **(A)** 12
- **(B)** 4
- **(C)** 8
- **(D)** 5

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 12**

**Detailed Solution:**

$\begin{aligned} & a+5 b=42, a, b \in N \\ & a=42-5 b, b=1, a=37 \\ & b=2, a=32 \\ & b=3, a=27 \\ & \vdots \\ & b=8, a=2\end{aligned}$
$\mathrm{R}$ has " 8 " elements $\Rightarrow \mathrm{m}=8$
$\begin{aligned} & \sum_{n=1}^8\left(1-i^{n !}\right)=x+i y \\ & \text { for } n \geq 4, i^{n !}=1 \\ & \Rightarrow(1-i)+\left(1-i^{2 !}\right)+\left(1-i^{3 !}\right) \\ & =1-I+2+1+1 \\ & =5-I=x+i y \\ & m+x+y=8+5-1=12\end{aligned}$

</details>

---

### Q25. JEE Main 2024 (06 Apr Shift 2)

*Type:* `numerical` | *Level:* `3`

If $\mathrm{S}(x)=(1+x)+2(1+x)^2+3(1+x)^3+\cdots+60(1+x)^{60}, x \neq 0$, and $(60)^2 \mathrm{~S}(60)=\mathrm{a}(\mathrm{b})^{\mathrm{b}}+\mathrm{b}$, where $a, b \in N$, then $(a+b)$ equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **3660**

**Detailed Solution:**

$\begin{aligned}
S(x)= & (1+x)+2(1+x)^2+3(1+x)^3+. .+60(1+x)^{60} \\
(1+x) S= & (1+x)^2+\ldots \ldots . \quad 59(1+x)^{60}+60(1+x)^{61} \\
& -x S=\frac{(1+x)(1+x)^{60}-1}{x}-60(1+x)^{61}
\end{aligned}$
Put $\mathrm{x}=60$
$-60 \mathrm{~S}=\frac{61\left((61)^{60}-1\right)}{60}-60(61)^{61}$
on solving 3660

</details>

---

### Q26. JEE Main 2024 (06 Apr Shift 1)

*Type:* `numerical` | *Level:* `3`

Let the first term of a series be $T_1=6$ and its $r^{\text {th }}$ term $T_r=3 T_{r-1}+6^r, r=2,3$,
$\qquad$ $n$. If the sum of the first $n$ terms of this series is $\frac{1}{5}\left(n^2-12 n+39\right)\left(4 \cdot 6^n-5 \cdot 3^n+1\right)$, then $n$ is equal to______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6**

**Detailed Solution:**

$\begin{aligned} & \mathrm{T}_{\mathrm{r}}=3 \mathrm{~T}_{\mathrm{r}-1}+6^{\mathrm{r}}, \mathrm{r}=2,3,4, \ldots \mathrm{n} \\ & \mathrm{T}_2=3 . \mathrm{T}_1+6^2 \\ & \mathrm{~T}_2=3.6+6^2...(1)\end{aligned}$
$\begin{aligned} & \mathrm{T}_3=3 \mathrm{~T}_2+6^3 \\ & \mathrm{~T}_3=3 \mathrm{~T}_2+6^3 \\ & \mathrm{~T}_3=3\left(3.6+6^2\right)+6^3 \\ & \mathrm{~T}_3=3^2 .6+3.6^2+6^3...(2)\end{aligned}$
$\begin{aligned} & \mathrm{T}_{\mathrm{r}}=3^{\mathrm{r}-1} \cdot 6\left[1+\frac{6}{3}+\left(\frac{6}{3}\right)^2+\ldots+\left(\frac{6}{3}\right)^{\mathrm{r}-1}\right] \\ & \mathrm{T}_{\mathrm{r}}=3^{\mathrm{r}-1} \cdot 6\left(1+2+2^2+\ldots+2^{\mathrm{r}-1}\right) \\ & \mathrm{T}_{\mathrm{r}}=6 \cdot 3^{\mathrm{r}-1} 1 \cdot \frac{\left(1-2^{\mathrm{r}}\right)}{(-1)} \\ & \mathrm{T}_{\mathrm{r}}=6 \cdot 3^{\mathrm{r}-1} \cdot\left(2^{\mathrm{r}}-1\right) \\ & \mathrm{T}_{\mathrm{r}}=\frac{6 \cdot 3^{\mathrm{r}}}{3} \cdot\left(2^{\mathrm{r}}-1\right)\end{aligned}$
$\begin{aligned} & \mathrm{T}_{\mathrm{r}}=2 \cdot\left(6^{\mathrm{r}}-3^{\mathrm{r}}\right) \\ & \mathrm{S}_{\mathrm{n}}=2 \Sigma\left(6^{\mathrm{r}}-3^{\mathrm{r}}\right) \\ & \mathrm{S}_{\mathrm{n}}=2 \cdot\left[\frac{6 .\left(6^{\mathrm{n}}-1\right)}{5}-\frac{3 .\left(3^{\mathrm{n}}-1\right)}{2}\right] \\ & \mathrm{S}_{\mathrm{n}}=2\left[\frac{12\left(6^{\mathrm{n}}-1\right)-15\left(3^{\mathrm{n}}-1\right)}{10}\right] \\ & \mathrm{S}_{\mathrm{n}}=\frac{3}{5}\left[4 \cdot 6^4-5 \cdot 3^{\mathrm{n}}+1\right] \\ & \therefore \mathrm{n}^2-12 \mathrm{n}+39=3 \\ & \mathrm{n}^2-12 \mathrm{n}+36=0 \\ & \mathrm{n}=6\end{aligned}$

</details>

---

### Q27. JEE Main 2024 (05 Apr Shift 2)

*Type:* `numerical` | *Level:* `2`

If $1+\frac{\sqrt{3}-\sqrt{2}}{2 \sqrt{3}}+\frac{5-2 \sqrt{6}}{18}+\frac{9 \sqrt{3}-11 \sqrt{2}}{36 \sqrt{3}}+\frac{49-20 \sqrt{6}}{180}+\ldots$ upto $\infty=2+\left(\sqrt{\frac{b}{a}}+1\right) \log _e\left(\frac{a}{b}\right)$, where $\mathrm{a}$ and $\mathrm{b}$ are integers with $\operatorname{gcd}(\mathrm{a}, \mathrm{b})=1$, then $11 \mathrm{a}+18 \mathrm{~b}$ is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **76**

**Detailed Solution:**

$\begin{aligned} & S=1+\frac{x}{2 \sqrt{3}}+\frac{x^2}{18}+\frac{x^3}{36 \sqrt{3}}+\frac{x^4}{180}+\ldots \infty \\ & \text { Put } \frac{x}{\sqrt{3}}=t, \text { where } x=\sqrt{3}-\sqrt{2} \\ & S=1+\frac{t}{2}+\frac{t^2}{6}+\frac{t^3}{12}+\frac{t^4}{20}+\ldots \\ & S=1+t\left(1-\frac{1}{2}\right)+t^2\left(\frac{1}{2}-\frac{1}{3}\right)+t^3\left(\frac{1}{3}-\frac{1}{4}\right)+t^4\left(\frac{1}{4}-\frac{1}{5}\right) \\ & S=\left(1+t+\frac{t^2}{2}+\frac{t^3}{3}+\frac{t^3}{4}+\ldots\right)-\left(\frac{t}{2}+\frac{t^2}{3}+\frac{t^3}{4}+\frac{t^4}{5}+\ldots\right) \\ & S=\left(t+\frac{t^2}{2}+\ldots\right)-\frac{1}{t}\left(t+\frac{t^2}{2}+\frac{t^3}{3}+\ldots\right)+2 \\ & S=2+\left(1-\frac{1}{t}\right)(-\log (1-t))=\left(\frac{1}{t}-1\right) \log (1-t)+2 \\ & S=2+\left(\frac{\sqrt{3}}{\sqrt{3}-\sqrt{2}}-1\right) \log \left(1-\frac{\sqrt{3}-\sqrt{2}}{\sqrt{3}}\right) \\ & S=2+\left(\frac{\sqrt{2}}{\sqrt{3}-\sqrt{2}}\right) \log e \frac{\sqrt{2}}{\sqrt{3}} \\ & S=2+\frac{(\sqrt{6}+2)}{2} \log e \frac{2}{3}=2+\left(\sqrt{\frac{3}{2}}+1\right) \log e \frac{2}{3} \\ & a=2, b=3 \\ & 11 a+18 b=11 \times 2+18 \times 3=76\end{aligned}$

</details>

---

### Q28. JEE Main 2024 (05 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If $\frac{1}{\sqrt{1}+\sqrt{2}}+\frac{1}{\sqrt{2}+\sqrt{3}}+\ldots+\frac{1}{\sqrt{99}+\sqrt{100}}=m$ and $\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\ldots+\frac{1}{99 \cdot 100}=n$, then the point $(\mathrm{m}, \mathrm{n})$ lies on the line

**Options:**

- **(A)** $11(x-1)-100(y-2)=0$
- **(B)** $11 x-100 y=0$
- **(C)** $11(x-2)-100(y-1)=0$
- **(D)** $11(x-1)-100 y=0$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $11 x-100 y=0$**

**Detailed Solution:**

$\begin{aligned} & \frac{1}{\sqrt{1}+\sqrt{2}}+\frac{1}{\sqrt{2}+\sqrt{3}}+\ldots+\frac{1}{\sqrt{99}+\sqrt{100}}=\mathrm{m} \\ & \frac{\sqrt{1}-\sqrt{2}}{-1}+\frac{\sqrt{2}-\sqrt{3}}{-1} \ldots \frac{\sqrt{99}-\sqrt{100}}{-1}=\mathrm{m}\end{aligned}$
$\begin{aligned}
& \sqrt{100}-1=\mathrm{m} \Rightarrow \mathrm{m}=9 \\
& \frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\ldots \frac{1}{99 \cdot 100}=\mathrm{n} \\
& \frac{1}{1}-\frac{1}{2}+\frac{1}{2}-\frac{1}{3} \ldots \frac{1}{99}-\frac{1}{100}=\mathrm{n} \\
& 1-\frac{1}{100}=\mathrm{n} \\
& \frac{99}{100}=\mathrm{n} \\
& (\mathrm{m}, \mathrm{n})=\left(9, \frac{99}{100}\right) \\
& \Rightarrow 11(9)-100\left(\frac{99}{100}\right) \\
& =99-99=0
\end{aligned}$
Ans.$11 x-100 y=0$

</details>

---

### Q29. JEE Main 2024 (04 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The value of $\frac{1 \times 2^2+2 \times 3^2+\ldots+100 \times(101)^2}{1^2 \times 2+2^2 \times 3+\ldots .+100^2 \times 101}$ is

**Options:**

- **(A)** $\frac{32}{31}$
- **(B)** $\frac{31}{30}$
- **(C)** $\frac{306}{305}$
- **(D)** $\frac{305}{301}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{305}{301}$**

**Detailed Solution:**

$\begin{aligned} & \frac{1 \times 2^2+2 \times 3^2+\ldots+100 \times(101)^2}{1^2 \times 2+2^2 \times 3+\ldots+100^2 \times 101}=\frac{\sum_{r=1}^{100} r(r+1)^2}{\sum_{r=1}^{100} r^2(r+1)} \\ & =\frac{\sum_{r=1}^{100}\left(r^3+2 r^2+r\right)}{\sum_{r=1}^{100}\left(r^3+r^2\right)}=\frac{\left(\frac{n(n+1)^2}{2}\right)+\frac{2 \cdot n(n+1)(2 n+1)}{6}+\frac{n(n+1)}{2}}{\left(\frac{n(n+1)}{2}\right)^2+\frac{n(n+1)(2 n+1)}{6}} \\ & =\frac{\frac{n(n+1)}{2}\left[\frac{n(n+1)}{2}+\frac{2}{3} \cdot(2 n+1)+1\right]}{\frac{n(n+1)}{2}\left[\frac{n(n+1)}{2}+\frac{(2 n+1)}{3}\right]} ; \text { Put n=100 } \\ & =\frac{\frac{100(101)}{2}+\frac{2}{3}(201)+1}{\frac{100 \times 101}{2}+\frac{201}{3}}=\frac{5185}{5117}=\frac{305}{301} \\ & \end{aligned}$

</details>

---

### Q30. JEE Main 2024 (31 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>−</mo><mn>3</mn><mo>⋅</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>−</mo><mn>3</mn><mo>⋅</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>−</mo><mn>3</mn><mo>⋅</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mo>.</mo><mo>...</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>45</mn><mn>109</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>45</mn><mn>109</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>55</mn><mn>109</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>55</mn><mn>109</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>55</mn><mn>109</mn></mfrac></math>**

**Detailed Solution:**

<p>General term of the given series is given by,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><mn>1</mn><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>4</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><mfenced><mrow><msup><mi>n</mi><mn>4</mn></msup><mo>-</mo><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><msup><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mi>n</mi></mrow></mfenced><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfrac><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mi>n</mi></mrow></mfenced></mrow><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mi>n</mi></mrow></mfenced><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>-</mo><mi>n</mi></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn><mo>+</mo><mi>n</mi></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mrow><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>1</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>89</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>109</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mo>-</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>109</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mn>55</mn></mrow><mn>109</mn></mfrac></math></p>

</details>

---

### Q31. JEE Main 2024 (30 Jan Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math> be the sum to n-terms of an arithmetic progression <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mo>…</mo><mo>…</mo></math>, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&lt;</mo><mfenced><mrow><mfrac><mn>6</mn><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>S</mi><mi>k</mi></msub></mrow></mfenced><mo>&lt;</mo><mn>42</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> equals ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<blockquote><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>AP</mi><mo>:</mo><mo> </mo><mn>3</mn><mo>,</mo><mn>7</mn><mo>,</mo><mn>11</mn><mo>,</mo><mn>15</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mn>6</mn><mo>+</mo><mn>4</mn><mi>n</mi><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mo>×</mo><mn>2</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi></math></p><p>Now, solving</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><mo>⇒</mo></mstyle><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><msub><mi>S</mi><mi>k</mi></msub><mo>=</mo><mn>2</mn><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mstyle displaystyle="false"><mi>n</mi></mstyle></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><mo>⇒</mo></mstyle><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mstyle displaystyle="false"><msub><mi>S</mi><mi>k</mi></msub></mstyle><mstyle displaystyle="false"><mo>=</mo></mstyle><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>3</mn></mfrac><mstyle displaystyle="false"><mo>+</mo></mstyle><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><mo>⇒</mo></mstyle><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><mstyle displaystyle="false"><msub><mi>S</mi><mi>k</mi></msub></mstyle><mstyle displaystyle="false"><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle><mfenced close="]" open="["><mstyle displaystyle="false"><mn>1</mn><mo>+</mo><mfrac><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>2</mn></mrow><mn>3</mn></mfrac></mstyle></mfenced></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn><mo>&lt;</mo><mfrac><mn>6</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mstyle displaystyle="false"><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></mstyle><msub><mi>S</mi><mi>k</mi></msub><mo>&lt;</mo><mn>42</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>40</mn><mo>&lt;</mo><mfrac><mn>6</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>×</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mfenced close="]" open="["><mfrac><mrow><mn>5</mn><mo>+</mo><mn>4</mn><mi>n</mi></mrow><mn>3</mn></mfrac></mfenced><mo>&lt;</mo><mn>42</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>40</mn><mo>&lt;</mo><mn>4</mn><mi>n</mi><mo>+</mo><mn>5</mn><mo>&lt;</mo><mn>42</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>35</mn><mo>&lt;</mo><mn>4</mn><mi>n</mi><mo>&lt;</mo><mn>37</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mi>n</mi><mo>=</mo><mn>9</mn></math></p></blockquote>

</details>

---

### Q32. JEE Main 2024 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>+</mo><msup><mn>13</mn><mn>2</mn></msup><mo>+</mo><msup><mn>19</mn><mn>2</mn></msup><mo>+</mo><msup><mn>26</mn><mn>2</mn></msup><mo>+</mo><mo>…</mo><mo>…</mo><mo>.</mo><mo>  </mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>n</mi><mn>4</mn></msup></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mn>55</mn><mi>k</mi><mo>+</mo><mn>40</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">k</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **353**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>8</mn><mn>2</mn></msup><mo>…</mo></math></p><p>Now, let <math xmlns="http://www.w3.org/1998/Math/MathML"><msqrt><msub><mi>t</mi><mi>n</mi></msub></msqrt><mo>=</mo><mi>a</mi><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>n</mi><mo>+</mo><mi>c</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>=</mo><mi>a</mi><mo>+</mo><mo> </mo><mi>b</mi><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mo>=</mo><mn>4</mn><mi>a</mi><mo>+</mo><mn>2</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn><mo>=</mo><mn>9</mn><mi>a</mi><mo>+</mo><mn>3</mn><mi>b</mi><mo>+</mo><mi>c</mi><mo> </mo><mo> </mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Now, solving equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>,</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo> </mo><mo>&amp;</mo><mo> </mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mi>b</mi><mo>=</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>,</mo><mo> </mo><mi>c</mi><mo>=</mo><mo>-</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>n</mi></msub><mo>=</mo><msup><mfenced><mrow><mfrac><msup><mi>n</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><mfrac><msup><mi>n</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>n</mi><mn>4</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>6</mn><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mfenced><mrow><mn>6</mn><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>5</mn><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>12</mn><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>n</mi><mo>+</mo><mn>4</mn><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mfenced><mrow><mn>6</mn><msup><mfenced><mfrac><mrow><mn>10</mn><mfenced><mrow><mn>10</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>5</mn><mfenced><mfrac><mrow><mn>10</mn><mo>·</mo><mn>11</mn><mo>·</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced><mo>-</mo><mn>12</mn><mfenced><mfrac><mrow><mn>10</mn><mo>·</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>4</mn><mo>·</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mfenced><mrow><mn>6</mn><msup><mfenced><mn>55</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>·</mo><mn>385</mn><mo>-</mo><mn>12</mn><mo>·</mo><mn>55</mn><mo>+</mo><mn>40</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>⇒</mo><mn>4</mn><mi>α</mi><mo>-</mo><mi>β</mi><mo>=</mo><mn>55</mn><mo>(</mo><mn>353</mn><mo>)</mo><mo>+</mo><mn>40</mn></math></p><p>Hence, on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>55</mn><mi>k</mi><mo>+</mo><mn>40</mn></math> we get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>353</mn></math></p>

</details>

---

### Q33. JEE Main 2023 (13 Apr Shift 2)

*Type:* `numerical` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mi>&#945;</mi></mfenced></math> denote the greatest integer <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8804;</mo><mi>&#945;</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><msqrt><mn>1</mn></msqrt></mfenced><mo>+</mo><mfenced open="[" close="]"><msqrt><mn>2</mn></msqrt></mfenced><mo>+</mo><mfenced open="[" close="]"><msqrt><mn>3</mn></msqrt></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced open="[" close="]"><msqrt><mn>120</mn></msqrt></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **825**

**Detailed Solution:**

<blockquote><p>Given,</p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msqrt><mn>1</mn></msqrt></mfenced><mo>+</mo><mfenced close="]" open="["><msqrt><mn>2</mn></msqrt></mfenced><mo>+</mo><mfenced close="]" open="["><msqrt><mn>3</mn></msqrt></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="]" open="["><msqrt><mn>120</mn></msqrt></mfenced></math></p><p>Now we now that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msqrt><mi>x</mi></msqrt></mfenced><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mtext>when</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>1</mn><mo>,</mo><mn>4</mn><mo>)</mo></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msqrt><mi>x</mi></msqrt></mfenced><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mtext>when</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>4</mn><mo>,</mo><mn>9</mn><mo>)</mo></math> and similarly <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><msqrt><mi>x</mi></msqrt></mfenced><mo>=</mo><mn>10</mn><mo>,</mo><mo>&#160;</mo><mtext>when</mtext><mo>&#160;</mo><mi>x</mi><mo>&#8712;</mo><mo>[</mo><mn>100</mn><mo>,</mo><mn>120</mn><mo>)</mo></math></p><p>Now using the above formula we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>E</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mspace linebreak="newline"></mspace><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>3</mn><mo>&#215;</mo><mn>1</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>2</mn><mo>+</mo><mn>7</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>19</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>21</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>r</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mi>r</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>770</mn><mo>+</mo><mn>55</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>E</mi><mo>=</mo><mn>825</mn></math></p></blockquote>

</details>

---

### Q34. JEE Main 2023 (13 Apr Shift 1)

*Type:* `numerical` | *Level:* `2`

<p>The sum to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#183;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>6</mn><mn>2</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is equal to<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mi>_</mi><mo>.</mo></math></p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1310**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>&#183;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>-</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>-</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>6</mn><mn>2</mn></msup><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>2</mn><mo>&#183;</mo><mo>(</mo><mn>2</mn><mi>r</mi><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mo>(</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>8</mn><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#183;</mo><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>21</mn></mrow><mn>6</mn></mfrac><mo>-</mo><mn>4</mn><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>10</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>44</mn><mo>&#183;</mo><mn>35</mn><mo>-</mo><mn>220</mn><mo>-</mo><mn>10</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1540</mn><mo>-</mo><mn>230</mn><mo>=</mo><mn>1310</mn></math></p></blockquote>

</details>

---

### Q35. JEE Main 2023 (12 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>&#62;</mo></math> be a sequence such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mrow><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>28</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><msub><mi>p</mi><mn>1</mn></msub><mo>&#160;</mo><msub><mi>p</mi><mn>2</mn></msub><mo>&#160;</mo><msub><mi>p</mi><mrow><mn>3</mn><mo>&#160;</mo></mrow></msub><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><msub><mi>p</mi><mi>m</mi></msub></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>p</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>p</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&#160;</mo><msub><mi>p</mi><mi>m</mi></msub></math> are the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> prime numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><mfrac><mstyle displaystyle="true"><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mstyle><mstyle displaystyle="true"><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mstyle></mfrac></math></p><p>Now we know that,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>S</mi><mi>n</mi></msub><mo>-</mo><msub><mi>S</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi></mrow><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac><mo>-</mo><mfrac><mrow><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>4</mn><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p>Now solving, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>k</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>k</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>k</mi><mfenced><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>k</mi><mo>+</mo><mn>2</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mn>1</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn><mo>.</mo><mo>-</mo><mn>0</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn><mo>&#183;</mo><mn>5</mn><mo>-</mo><mn>1</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>12</mn><mo>&#183;</mo><mn>13</mn><mo>-</mo><mn>9</mn><mo>&#183;</mo><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>12</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mfenced close="]" open="["><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>12</mn><mo>&#183;</mo><mn>13</mn><mo>-</mo><mn>0</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>5</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>13</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mn>28</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mfrac><mrow><mn>28</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>13</mn></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>28</mn><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><msub><mi>a</mi><mi>k</mi></msub></mfrac><mo>=</mo><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mn>7</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>13</mn></math></p><p>Hence, there are six prime numbers in multiplications,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>6</mn></math></p>

</details>

---

### Q36. JEE Main 2023 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>21</mn><mo>+</mo><mn>34</mn><mo>+</mo><mn>50</mn><mo>+</mo><mo>&#8230;</mo></math> to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> terms, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>60</mn></mfrac><mfenced><mrow><msub><mi>S</mi><mn>29</mn></msub><mo>-</mo><msub><mi>S</mi><mn>9</mn></msub></mrow></mfenced></math>  is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>223</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>226</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>227</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>223</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>21</mn><mo>+</mo><mn>34</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub><mspace linebreak="newline"></mspace><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>21</mn><mo>+</mo><mn>34</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub></math></p><p>Subtracting above equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mn>4</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>13</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><msub><mi>T</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>4</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>10</mn><mo>+</mo><mn>13</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>The above series is in AP.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>4</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow></mrow><mrow></mrow></munderover><mfrac><mrow><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>n</mi></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mrow><mn>3</mn><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mfenced><mrow><mfrac><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>29</mn></msub><mo>=</mo><mfrac><mrow><mn>29</mn><mo>&#215;</mo><mn>30</mn></mrow><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>59</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>29</mn></msub><mo>=</mo><mn>29</mn><mo>&#215;</mo><mn>15</mn><mo>&#215;</mo><mn>32</mn><mo>=</mo><mn>13920</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>9</mn></msub><mo>=</mo><mfrac><mrow><mn>9</mn><mo>&#215;</mo><mn>10</mn></mrow><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>19</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>9</mn></msub><mo>=</mo><mn>9</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>12</mn><mo>=</mo><mn>540</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>S</mi><mn>29</mn></msub><mo>-</mo><msub><mi>S</mi><mn>9</mn></msub></mrow><mn>60</mn></mfrac><mo>=</mo><mfrac><mrow><mn>13920</mn><mo>-</mo><mn>540</mn></mrow><mn>60</mn></mfrac><mo>=</mo><mn>223</mn></math>.</p><p>Therefore, the required answer is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>223</mn></math>.</p></blockquote>

</details>

---

### Q37. JEE Main 2023 (08 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub></math> be <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mi>th</mi></msup></math> term of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>23</mn><mo>+</mo><mn>35</mn><mo>+</mo><mn>50</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><mi>a</mi><mi>k</mi></msub></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>30</mn></msub><mo>-</mo><msub><mi>a</mi><mn>40</mn></msub></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11310</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11260</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11290</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11280</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11290</mn></math>**

**Detailed Solution:**

<blockquote><p>The given series is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub></math>, then we can write as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>23</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub><mspace linebreak="newline"></mspace><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>5</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>23</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math></p><p>Subtracting above equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>9</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></mrow></mfenced><mo>-</mo><msub><mi>a</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mi>n</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><mo>&#215;</mo><msup><mn>40</mn><mn>2</mn></msup><mo>-</mo><mn>3</mn><mo>&#215;</mo><mn>40</mn><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>4800</mn><mo>-</mo><mn>120</mn><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><mn>2345</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>30</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><msub><mi>a</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>30</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>3</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfenced><msup><mi>n</mi><mn>2</mn></msup></mfenced><mo>-</mo><mn>3</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfenced><mi>n</mi></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mrow><mn>3</mn><mfenced><mn>30</mn></mfenced><mfenced><mn>31</mn></mfenced><mfenced><mn>61</mn></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>3</mn><mfenced><mn>30</mn></mfenced><mfenced><mn>31</mn></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mn>10</mn><mo>&#215;</mo><mn>30</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>30</mn></msub><mo>=</mo><mn>13635</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>30</mn></msub><mo>-</mo><msub><mi>a</mi><mn>40</mn></msub><mo>=</mo><mn>13635</mn><mo>-</mo><mn>2345</mn><mo>=</mo><mn>11290</mn></math></p><p>Therefore, the required value is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11290</mn></math>.</p></blockquote>

</details>

---

### Q38. JEE Main 2023 (08 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `1`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>K</mi></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>K</mi></mrow><mi>K</mi></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><msup><mi>S</mi><mn>2</mn></msup><mi>j</mi></msub><mo>=</mo><mfrac><mi>n</mi><mi>A</mi></mfrac><mfenced><mrow><mi>B</mi><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>C</mi><mi>n</mi><mo>+</mo><mi>D</mi></mrow></mfenced></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>,</mo><mo>&#160;</mo><mi>D</mi><mo>&#160;</mo><mo>&#8712;</mo><mo>&#160;</mo><mi>N</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> Has least value then

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>C</mi><mo>+</mo><mi>D</mi></math> is not divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mn>5</mn><mo>(</mo><mi>D</mi><mo>-</mo><mi>C</mi><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>+</mo><mi>C</mi><mo>+</mo><mi>D</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>**

**Detailed Solution:**

<blockquote><p>Given that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>K</mi></msub><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>K</mi></mrow><mi>K</mi></mfrac></math></p><p>We know that <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>K</mi></msub><mo>=</mo><mfrac><mrow><mi>K</mi><mfenced><mrow><mi>K</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn><mi>K</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>K</mi><mo>+</mo><mn>1</mn></mrow><mn>2</mn></mfrac></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msup><mfenced><msub><mi>S</mi><mi>j</mi></msub></mfenced><mn>2</mn></msup><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mrow><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mfrac><mrow><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>6</mn></mrow><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mfrac><mrow><mn>2</mn><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>n</mi><mo>+</mo><mn>6</mn><mo>-</mo><mn>6</mn></mrow><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mfrac><mrow><mn>2</mn><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>9</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>13</mn><mi>n</mi></mrow><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>n</mi><mn>24</mn></mfrac><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>9</mn><mi>n</mi><mo>+</mo><mn>13</mn></mrow></mfenced></math></p><p>On comparing this with <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msub><msup><mi>S</mi><mn>2</mn></msup><mi>j</mi></msub><mo>=</mo><mfrac><mi>n</mi><mi>A</mi></mfrac><mfenced><mrow><mi>B</mi><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>C</mi><mi>n</mi><mo>+</mo><mi>D</mi></mrow></mfenced></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mn>24</mn><mo>,</mo><mo>&#160;</mo><mi>B</mi><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mi>C</mi><mo>=</mo><mn>9</mn><mo>,</mo><mo>&#160;</mo><mi>D</mi><mo>=</mo><mn>13</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow><mi>D</mi></mfrac><mo>=</mo><mfrac><mn>26</mn><mn>13</mn></mfrac><mo>=</mo><mn>2</mn></math></p><p>That means, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> is divisible by <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math>.</p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q39. JEE Main 2023 (06 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>c</mi><mi>d</mi><mfenced><mrow><mi>m</mi><mo>,</mo><mo>&#160;</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced><mn>2021</mn></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mn>2022</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup><mo>=</mo><mn>1012</mn><msup><mi>m</mi><mn>2</mn></msup><mi>n</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>240</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>220</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>240</mn></math>**

**Detailed Solution:**

<blockquote><p>Let</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mfenced><mn>2021</mn></mfenced><mn>2</mn></msup><mo>-</mo><msup><mfenced><mn>2022</mn></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>3</mn><mo>-</mo><mn>4</mn></mrow></mfenced><mfenced><mrow><mn>3</mn><mo>+</mo><mn>4</mn></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mn>2021</mn><mo>-</mo><mn>2022</mn></mrow></mfenced><mfenced><mrow><mn>2021</mn><mo>+</mo><mn>2022</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mo>-</mo><mfenced close="]" open="["><mrow><mn>3</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>15</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>4043</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup></math></p><p>The number of terms in the bracket are <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2022</mn><mn>2</mn></mfrac><mo>=</mo><mn>1011</mn></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mo>-</mo><mfrac><mn>1011</mn><mn>2</mn></mfrac><mfenced><mrow><mn>6</mn><mo>+</mo><mn>1010</mn><mo>&#215;</mo><mn>4</mn></mrow></mfenced><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mo>-</mo><mn>1011</mn><mo>&#215;</mo><mn>2023</mn><mo>+</mo><msup><mfenced><mn>2023</mn></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>2023</mn><mo>&#215;</mo><mn>1012</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><msup><mn>17</mn><mn>2</mn></msup><mo>&#215;</mo><mn>7</mn><mo>&#215;</mo><mn>1012</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>17</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>7</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>g</mi><mi>c</mi><mi>d</mi><mfenced><mrow><mn>17</mn><mo>,</mo><mn>7</mn></mrow></mfenced><mo>=</mo><mn>1</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>m</mi><mn>2</mn></msup><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><msup><mn>17</mn><mn>2</mn></msup><mo>-</mo><msup><mn>7</mn><mn>2</mn></msup><mo>=</mo><mn>240</mn></math></p><p>Hence this is the correct option.</p></blockquote>

</details>

---

### Q40. JEE Main 2023 (06 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>19</mn><mo>+</mo><mn>29</mn><mo>+</mo><mn>41</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3520</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3450</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3250</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3420</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3520</mn></math>**

**Detailed Solution:**

<blockquote><p>Let the given series be <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub></math>, then we can write as</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>19</mn><mo>+</mo><mn>29</mn><mo>+</mo><mn>41</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub><mspace linebreak="newline"></mspace><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>5</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>19</mn><mo>+</mo><mn>29</mn><mo>+</mo><mn>41</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub></math></p><p>Subtracting above equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>=</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>10</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><msub><mi>T</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></mfrac><mfenced><mrow><mn>12</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>5</mn><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><msub><mi>T</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>21</mn><mo>&#215;</mo><mn>41</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>20</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>20</mn></msub><mo>=</mo><mn>3520</mn></math></p></blockquote>

</details>

---

### Q41. JEE Main 2023 (01 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

<p>The sum <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo></mrow></mfrac></math>  is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><mi mathvariant="normal">e</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><mn>2</mn><mi mathvariant="normal">e</mi></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mi mathvariant="normal">e</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mn>4</mn><mi mathvariant="normal">e</mi></mrow></mfrac><mo>-</mo><mn>4</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>11</mn><mi mathvariant="normal">e</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><mn>2</mn><mi mathvariant="normal">e</mi></mrow></mfrac><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mi mathvariant="normal">e</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mn>4</mn><mi mathvariant="normal">e</mi></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>13</mn><mi mathvariant="normal">e</mi></mrow><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><mn>4</mn><mi mathvariant="normal">e</mi></mrow></mfrac><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><mn>2</mn><mi mathvariant="normal">n</mi><mo>(</mo><mn>2</mn><mi mathvariant="normal">n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>8</mn><mi mathvariant="normal">n</mi><mo>+</mo><mn>8</mn></mrow><mrow><mo>(</mo><mn>2</mn><mi mathvariant="normal">n</mi><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac><mo>+</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>!</mo></mrow></mfrac><mo>+</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo></mrow></mfrac><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>We know the expansion of exponential functions as,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mi mathvariant="normal">x</mi></msup><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mi>r</mi><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi mathvariant="normal">e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>=</mo><mn>1</mn><mo>-</mo><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8734;</mo><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msup><mfenced><mrow><mo>-</mo><mn>1</mn></mrow></mfenced><mi>r</mi></msup><mrow><mi>r</mi><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi mathvariant="normal">e</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mfrac><mn>1</mn><mrow><mfenced><mtext>even</mtext></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">e</mi><mo>-</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac><mo>=</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mfrac><mn>1</mn><mrow><mfenced><mtext>odd</mtext></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p>Now from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math>,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></mrow></mfenced><mo>+</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>!</mo></mrow></mfrac><mo>+</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mfrac><mrow><mi mathvariant="normal">e</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mfenced close="]" open="["><mfrac><mrow><mi mathvariant="normal">e</mi><mo>-</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mn>4</mn><mfenced><mfrac><mrow><mi mathvariant="normal">e</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfenced><mrow><mi mathvariant="normal">e</mi><mo>+</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac></mrow></mfenced><mn>4</mn></mfrac><mo>+</mo><mi mathvariant="normal">e</mi><mo>-</mo><mfrac><mn>1</mn><mi mathvariant="normal">e</mi></mfrac><mo>+</mo><mn>2</mn><mi mathvariant="normal">e</mi><mo>+</mo><mfrac><mn>2</mn><mi mathvariant="normal">e</mi></mfrac><mo>-</mo><mn>4</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>13</mn><mn>4</mn></mfrac><mi>e</mi><mo>+</mo><mfrac><mn>5</mn><mrow><mn>4</mn><mi>e</mi></mrow></mfrac><mo>-</mo><mn>4</mn></math></p>

</details>

---

### Q42. JEE Main 2023 (01 Feb Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>The sum to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>&#160;</mo></math>terms of the series</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math>is :-</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>59</mn><mn>111</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>55</mn><mn>111</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>56</mn><mn>111</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>58</mn><mn>111</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>55</mn><mn>111</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>4</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math></p><p>Here,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><mn>1</mn><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><msup><mi>n</mi><mn>4</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>n</mi><mrow><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>2</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>t</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mn>91</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>111</mn></mfrac></mrow></mfenced></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><msub><mi>t</mi><mn>1</mn></msub><mo>+</mo><msub><mi>t</mi><mn>2</mn></msub><mo>+</mo><msub><mi>t</mi><mn>3</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>t</mi><mn>10</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>111</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><mfrac><mn>55</mn><mn>111</mn></mfrac></math></p>

</details>

---

### Q43. JEE Main 2023 (31 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The sum <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>.</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>.</mo><msup><mn>5</mn><mn>2</mn></msup><mo>-</mo><mn>4</mn><mo>.</mo><msup><mn>7</mn><mn>2</mn></msup><mo>+</mo><mn>5</mn><mo>.</mo><msup><mn>9</mn><mn>2</mn></msup><mo>-</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn><mo>.</mo><msup><mn>29</mn><mn>2</mn></msup></math> is _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **6952**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>-</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#183;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><msup><mn>29</mn><mn>2</mn></msup></math></p><p>Now rewriting the above expression we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><munder><munder><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#183;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><msup><mn>29</mn><mn>2</mn></msup></mrow><mo>&#9183;</mo></munder><msub><mi>S</mi><mn>1</mn></msub></munder><mo>-</mo><mn>2</mn><munder><munder><mfenced open="[" close="]"><mrow><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#183;</mo><msup><mn>7</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>14</mn><mo>&#183;</mo><msup><mn>27</mn><mn>2</mn></msup></mrow></mfenced><mo>&#9183;</mo></munder><msub><mi>S</mi><mn>2</mn></msub></munder></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>3</mn><mo>&#183;</mo><msup><mn>5</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><msup><mn>29</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mi>r</mi><mo>&#183;</mo><msup><mfenced><mrow><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mi>r</mi><mo>&#183;</mo><mfenced><mrow><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>4</mn><mi>r</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mfenced><mrow><mn>4</mn><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mi>r</mi><mo>-</mo><mn>4</mn><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mi>r</mi><mo>-</mo><mn>4</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>r</mi><mn>2</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mn>4</mn><msup><mfenced><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac><mo>-</mo><mn>4</mn><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn><mo>&#215;</mo><mn>31</mn></mrow><mn>6</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfenced><mrow><mn>4</mn><msup><mfenced><mn>120</mn></mfenced><mn>2</mn></msup><mo>+</mo><mn>120</mn><mo>-</mo><mn>4960</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>52760</mn></math></p><p>Now solving <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>&#183;</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>4</mn><mo>&#183;</mo><msup><mn>7</mn><mn>2</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>14</mn><mo>&#183;</mo><msup><mn>27</mn><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mfenced><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><msup><mfenced><mrow><mn>4</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mfenced><mrow><mn>2</mn><mi>r</mi></mrow></mfenced><mfenced><mrow><mn>16</mn><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mn>8</mn><mi>r</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>32</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mi>r</mi><mo>-</mo><mn>16</mn><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><msup><mi>r</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>32</mn><msup><mfenced><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>8</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mfenced><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>8</mn></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mn>16</mn><mfenced><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mn>8</mn><mo>&#215;</mo><mn>15</mn></mrow><mn>6</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>32</mn><mo>&#215;</mo><mn>784</mn><mo>+</mo><mn>56</mn><mo>-</mo><mn>16</mn><mo>&#215;</mo><mn>140</mn><mo>=</mo><mn>22904</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msub><mi>S</mi><mn>1</mn></msub><mo>-</mo><mn>2</mn><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>52760</mn><mo>-</mo><mn>2</mn><mo>&#215;</mo><mn>22904</mn><mo>=</mo><mn>6952</mn></math></p>

</details>

---

### Q44. JEE Main 2023 (30 Jan Shift 1)

*Type:* `numerical` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><msup><mi>n</mi><mn>3</mn></msup><mo>(</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo><mo>)</mo><mo>+</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>!</mo><mo>)</mo></mrow><mrow><mo>(</mo><mi>n</mi><mo>!</mo><mo>)</mo><mo>(</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>)</mo><mo>!</mo><mo>)</mo></mrow></mfrac><mo>=</mo><mi>a</mi><mi>e</mi><mo>+</mo><mfrac><mi>b</mi><mi>e</mi></mfrac><mo>+</mo><mi>c</mi></math> where   <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>&#160;</mo><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi></math>  and  <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></math>  Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi></math> is  equal to _______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **26**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><msup><mi>n</mi><mn>3</mn></msup><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi><mo>!</mo></mrow><mrow><mi>n</mi><mo>!</mo><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><msup><mi>n</mi><mn>3</mn></msup><mfenced close="}" open="{"><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfenced></mrow><mrow><mi>n</mi><mo>!</mo><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi><mo>!</mo></mrow><mrow><mi>n</mi><mo>!</mo><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><msup><mi>n</mi><mn>3</mn></msup><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>3</mn><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>n</mi></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mrow><mn>3</mn><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mi>n</mi><mrow><mi>n</mi><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mrow><mi>e</mi><mo>-</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mn>2</mn></mfrac></mfenced><mo>-</mo><mfenced><mfrac><mrow><mi>e</mi><mo>+</mo><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup></mrow><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>3</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><mn>3</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mfenced><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>5</mn><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>5</mn><mo>,</mo><mo>&#160;</mo><mi>b</mi><mo>=</mo><mo>-</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>c</mi><mo>=</mo><mn>0</mn></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mi>b</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>25</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>26</mn></math></p>

</details>

---

### Q45. JEE Main 2023 (30 Jan Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>n</mi><mo>+</mo><mn>15</mn></mrow></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>25</mn></msub></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>51</mn><mn>144</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>49</mn><mn>138</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>50</mn><mn>141</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>52</mn><mn>147</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>50</mn><mn>141</mn></mfrac></math>**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mrow><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>16</mn><mi>n</mi><mo>+</mo><mn>15</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mfrac><mn>1</mn><mrow><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>3</mn><mn>2</mn></mfrac></mrow></mfenced></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mi>n</mi><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mrow><mo>-</mo><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mrow></mfenced></mfrac></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>3</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>7</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>5</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>45</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>43</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac></mrow></mfenced><mo>+</mo><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>47</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mfenced><mstyle displaystyle="true"><mfrac><mn>45</mn><mn>2</mn></mfrac></mstyle></mfenced></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>47</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>47</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>50</mn><mn>141</mn></mfrac></math></p>

</details>

---

### Q46. JEE Main 2023 (29 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>,</mo><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>,</mo><mo>&#8704;</mo><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mfrac><msub><mi>b</mi><mi>n</mi></msub><msup><mn>2</mn><mi>n</mi></msup></mfrac></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">T</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>8</mn></munderover><mfrac><mi mathvariant="normal">n</mi><msup><mn>2</mn><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msup></mfrac></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>7</mn></msup><mo>(</mo><mn>2</mn><mi>S</mi><mo>-</mo><mi>T</mi><mo>)</mo></math>  is equal to</p>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **461**

**Detailed Solution:**

<p>Given:</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mo>&#160;</mo><msub><mi mathvariant="normal">a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfrac><msub><mi>b</mi><mn>2</mn></msub><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>b</mi><mn>9</mn></msub><msup><mn>2</mn><mn>9</mn></msup></mfrac><mo>+</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mo>&#160;&#160;</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msub><mi>b</mi><mn>2</mn></msub><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>b</mi><mn>9</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac><mo>+</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>11</mn></msup></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>Subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mi>b</mi><mn>2</mn></mfrac><mo>+</mo><mfenced><mfrac><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>-</mo><msub><mi>b</mi><mn>1</mn></msub></mrow><msup><mn>2</mn><mn>2</mn></msup></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mstyle displaystyle="true"><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub></mstyle><mstyle displaystyle="true"><msup><mn>2</mn><mn>3</mn></msup></mstyle></mfrac></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mfrac><mstyle displaystyle="true"><msub><mi>b</mi><mn>10</mn></msub><mo>-</mo><msub><mi>b</mi><mn>9</mn></msub></mstyle><mstyle displaystyle="true"><msup><mn>2</mn><mn>10</mn></msup></mstyle></mfrac></mfenced><mo>-</mo><mfenced><mfrac><mstyle displaystyle="true"><msub><mi>b</mi><mn>10</mn></msub></mstyle><mstyle displaystyle="true"><msup><mn>2</mn><mn>11</mn></msup></mstyle></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfenced><mrow><mfrac><msub><mi>a</mi><mn>1</mn></msub><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>a</mi><mn>9</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>11</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>-</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac><mo>+</mo><mfenced><mrow><mfrac><msub><mi>a</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>+</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>a</mi><mn>9</mn></msub><msup><mn>2</mn><mn>9</mn></msup></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>-</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfenced><mrow><mfrac><msub><mi>a</mi><mn>1</mn></msub><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>a</mi><mn>9</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac></mrow></mfenced><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>4</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><msub><mi>b</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>-</mo><mfrac><msub><mi>b</mi><mn>10</mn></msub><msup><mn>2</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfenced><mrow><mfrac><msub><mi>a</mi><mn>1</mn></msub><mn>2</mn></mfrac><mo>-</mo><mfrac><msub><mi>a</mi><mn>9</mn></msub><msup><mn>2</mn><mn>10</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>2</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>8</mn><msup><mn>2</mn><mn>9</mn></msup></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mi>S</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfenced><msup><mn>2</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfrac><mi>T</mi><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>S</mi><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfenced><msup><mn>2</mn><mn>9</mn></msup></mfrac><mo>+</mo><mi>T</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>2</mn><mi>S</mi><mo>-</mo><mi>T</mi></mrow></mfenced><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfenced><msup><mn>2</mn><mn>9</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mn>7</mn></msup><mo>(</mo><mn>2</mn><mi>S</mi><mo>-</mo><mi>T</mi><mo>)</mo><mo>=</mo><msup><mn>2</mn><mn>8</mn></msup><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>b</mi><mn>1</mn></msub></mrow></mfenced><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><msub><mi>a</mi><mn>9</mn></msub></mrow></mfenced><mn>4</mn></mfrac></math></p><p>Given, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi mathvariant="normal">n</mi></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>9</mn></msub><mo>-</mo><msub><mi>a</mi><mn>8</mn></msub><mo>=</mo><mn>8</mn></math></p><p>Adding all equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>9</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>8</mn><mo>=</mo><mn>36</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>9</mn></msub><mo>=</mo><mn>37</mn><mo>&#160;</mo><mfenced><mrow><mo>&#8757;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></mrow></mfenced></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>7</mn></msup><mo>(</mo><mn>2</mn><mi>S</mi><mo>-</mo><mi>T</mi><mo>)</mo><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>37</mn></mrow></mfenced><mn>4</mn></mfrac></math></p><p>Also,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>-</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><msub><mi>b</mi><mn>2</mn></msub><mo>-</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>3</mn></msub><mo>-</mo><msub><mi>b</mi><mn>2</mn></msub><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>4</mn></msub><mo>-</mo><msub><mi>b</mi><mn>3</mn></msub><mo>=</mo><msub><mi>a</mi><mn>3</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mspace linebreak="newline"/><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#8942;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>10</mn></msub><mo>-</mo><msub><mi>b</mi><mn>9</mn></msub><mo>=</mo><msub><mi>a</mi><mn>9</mn></msub></math></p><p>Adding all equations, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mn>10</mn></msub><mo>-</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>a</mi><mn>9</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>10</mn></msub><mo>-</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>16</mn><mo>+</mo><mn>22</mn><mo>+</mo><mn>29</mn><mo>+</mo><mn>37</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>b</mi><mn>10</mn></msub><mo>=</mo><mn>130</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mn>7</mn></msup><mo>(</mo><mn>2</mn><mi>S</mi><mo>-</mo><mi>T</mi><mo>)</mo><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>-</mo><mfrac><mfenced><mrow><msub><mi>b</mi><mn>10</mn></msub><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>37</mn></mrow></mfenced><mn>4</mn></mfrac><mo>=</mo><msup><mn>2</mn><mn>9</mn></msup><mo>-</mo><mfrac><mfenced><mrow><mn>130</mn><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>37</mn></mrow></mfenced><mn>4</mn></mfrac><mo>=</mo><mn>461</mn></math></p><p> </p>

</details>

---

### Q47. JEE Main 2023 (24 Jan Shift 2)

*Type:* `numerical` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mtext>upto&#160;</mtext><mi>n</mi><mo>&#160;</mo><mtext>terms</mtext></mrow><mrow><mn>1</mn><mo>&#183;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>7</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mtext>upto&#160;</mtext><mi>n</mi><mo>&#160;</mo><mtext>terms</mtext></mrow></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math> then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **5**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>&#183;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>7</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p>Now we know that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced open="[" close="]"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math></p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#931;</mi><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mi>&#931;</mi><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>&#931;</mi><mi>n</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#931;</mi><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn><mo>&#215;</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#931;</mi><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p>So putting the value in the given equation we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><msup><mi>n</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>&#183;</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>5</mn><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>7</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mi>n</mi><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msup><mfenced close="]" open="["><mstyle displaystyle="true"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><mstyle displaystyle="true"><mfrac><mstyle displaystyle="true"><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mstyle displaystyle="true"><mfrac><mn>1</mn><mn>4</mn></mfrac></mstyle><mfenced close="]" open="["><mstyle displaystyle="true"><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle></mfenced></mrow><mstyle displaystyle="true"><mfrac><mstyle displaystyle="true"><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>3</mn></mstyle></mfrac><mo>+</mo><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>2</mn></mstyle></mfrac></mstyle></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mn>6</mn><mfenced close="]" open="["><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>4</mn><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced></mstyle></mfrac><mo>=</mo><mfrac><mn>9</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mstyle displaystyle="true"><mfenced close="]" open="["><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></mstyle><mstyle displaystyle="true"><mn>2</mn><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced></mstyle></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><mfenced close="]" open="["><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>6</mn><mfenced><mrow><mn>2</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>n</mi><mo>=</mo><mn>6</mn><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>5</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>5</mn><mi>n</mi><mo>=</mo><mn>24</mn><mi>n</mi><mo>+</mo><mn>30</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>19</mn><mi>n</mi><mo>-</mo><mn>30</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>5</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>25</mn><mi>n</mi><mo>+</mo><mn>6</mn><mi>n</mi><mo>-</mo><mn>30</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>5</mn><mi>n</mi><mo>+</mo><mn>6</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>5</mn></math></p>

</details>

---

### Q48. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>r</mi><mo>!</mo></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>!</mo><mo>-</mo><mn>21</mn><mo>!</mo></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>!</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>21</mn><mo>!</mo></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>!</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>20</mn><mo>!</mo></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn><mo>!</mo><mo>-</mo><mn>20</mn><mo>!</mo></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>22</mn><mo>!</mo><mo>-</mo><mn>2</mn><mfenced><mrow><mn>21</mn><mo>!</mo></mrow></mfenced></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mi>r</mi><mo>!</mo></math></p><p>Now on rearranging we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>r</mi></mrow></mfenced><mi>r</mi><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mi>r</mi><mo>&#183;</mo><mi>r</mi><mo>!</mo></mrow></mfenced><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mi>r</mi><mo>&#183;</mo><mi>r</mi><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mi>r</mi><mo>.</mo><mi>r</mi><mo>!</mo></mrow></mfenced><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mi>r</mi><mo>!</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>21</mn><mo>.</mo><menclose notation="bottom left"><mn>21</mn></menclose><mo>-</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><menclose notation="bottom left"><mn>21</mn></menclose><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>21</mn><mo>.</mo><menclose notation="bottom left"><mn>21</mn></menclose><mo>-</mo><menclose notation="bottom left"><mn>21</mn></menclose></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>.</mo><mn>21</mn><mo>!</mo><mo>=</mo><mfenced><mrow><mn>22</mn><mo>-</mo><mn>2</mn></mrow></mfenced><mn>21</mn><mo>!</mo><mo>=</mo><mn>22</mn><mo>!</mo><mo>-</mo><mn>2</mn><mo>.</mo><mn>21</mn><mo>!</mo></math></p></blockquote>

</details>

---

### Q49. JEE Main 2022 (29 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced close="}" open="{"><msub><mi>a</mi><mi>n</mi></msub></mfenced><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></msubsup></math> be a sequence such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>3</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn><mo>,</mo><mo>&#8704;</mo><mi>n</mi><mo>&#8805;</mo><mn>0</mn></math>.</p><p>Then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>25</mn></msub><msub><mi>a</mi><mn>23</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>25</mn></msub><msub><mi>a</mi><mn>22</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>23</mn></msub><msub><mi>a</mi><mn>24</mn></msub><mo>+</mo><mn>4</mn><msub><mi>a</mi><mn>22</mn></msub><msub><mi>a</mi><mn>24</mn></msub></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>483</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>528</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>575</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>624</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>528</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>=</mo><mn>0</mn><mo>,</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> </p><p>And <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>3</mn><msub><mi>a</mi><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>:</mo><mi>n</mi><mo>&#8805;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">a</mi><mi>n</mi></msub></mrow></mfenced><mo>+</mo><mn>1</mn></math></p><p>Now for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>0</mn><mo>&#160;&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>-</mo><msub><mi>a</mi><mn>0</mn></msub></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>1</mn></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>&#160;&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>2</mn></mfenced></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>2</mn><mo>&#160;&#160;</mo><msub><mi>a</mi><mn>4</mn></msub><mo>-</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>-</mo><msub><mi>a</mi><mn>2</mn></msub></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mn>3</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mspace linebreak="newline"></mspace><mo>.</mo><mspace linebreak="newline"></mspace><mo>.</mo></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mi>n</mi><mo>&#160;&#160;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mi>n</mi></msub></mrow></mfenced><mo>+</mo><mn>1</mn><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>n</mi></mfenced></math></p><p>Now adding all above equation upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mrow></mfenced><mo>-</mo><mn>2</mn><mfenced><mrow><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mn>0</mn></msub></mrow></mfenced><mo>-</mo><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p>Now replacing <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8594;</mo><mi>n</mi><mo>-</mo><mn>2</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>25</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>25</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>24</mn></msub><mo>=</mo><mn>25</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>24</mn></math></p><p>Now putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>23</mn></math> we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mn>23</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>22</mn></msub><mo>=</mo><mn>23</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>22</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><msub><mi>a</mi><mn>25</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>24</mn></msub></mrow></mfenced><mfenced><mrow><msub><mi>a</mi><mn>23</mn></msub><mo>-</mo><mn>2</mn><msub><mi>a</mi><mn>22</mn></msub></mrow></mfenced><mo>=</mo><mfenced><mn>24</mn></mfenced><mfenced><mn>22</mn></mfenced><mo>=</mo><mn>528</mn></math></p></blockquote>

</details>

---

### Q50. JEE Main 2022 (29 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#215;</mo><mn>4</mn><mo>&#215;</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>&#215;</mo><mn>5</mn><mo>&#215;</mo><mn>6</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn><mo>&#215;</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mi>k</mi><mn>101</mn></mfrac></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn><mi>k</mi></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **286**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mn>2</mn><mo>.</mo><mn>3</mn><mo>.</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>.</mo><mn>4</mn><mo>.</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>100</mn><mo>.</mo><mn>101</mn><mo>.</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mi>k</mi><mn>101</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>2</mn><mrow><mn>2</mn><mo>.</mo><mn>3</mn><mo>.</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mn>3</mn><mo>.</mo><mn>4</mn><mo>.</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>2</mn><mrow><mn>100</mn><mo>.</mo><mn>101</mn><mo>.</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>101</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>4</mn><mo>-</mo><mn>2</mn></mrow><mrow><mn>2</mn><mo>.</mo><mn>3</mn><mo>.</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>-</mo><mn>3</mn></mrow><mrow><mn>3</mn><mo>.</mo><mn>4</mn><mo>.</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><mn>102</mn><mo>-</mo><mn>100</mn></mrow><mrow><mn>100</mn><mo>.</mo><mn>101</mn><mo>.</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>101</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#215;</mo><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>&#215;</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>100</mn><mo>&#215;</mo><mn>101</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>101</mn><mo>&#215;</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>101</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>101</mn><mo>&#215;</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>k</mi></mrow><mn>101</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>101</mn><mrow><mn>2</mn><mo>&#215;</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mn>101</mn><mrow><mn>101</mn><mo>&#215;</mo><mn>102</mn></mrow></mfrac><mo>=</mo><mn>2</mn><mi>k</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mi>k</mi><mo>=</mo><mfrac><mn>101</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>102</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>34</mn><mi>k</mi><mo>=</mo><mn>286</mn></math></p></blockquote>

</details>

---

### Q51. JEE Main 2022 (29 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>20</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>60</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>180</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>200</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>256</mn></mfrac></math>, then the maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>198</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>202</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>212</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>218</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>212</mn></math>**

**Detailed Solution:**

<blockquote><p>Given,<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>20</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>60</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mo>&#160;</mo><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>180</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>200</mn><mo>-</mo><mi>a</mi></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>256</mn></mfrac></math></p><p>So, on simplifying we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>20</mn></mfrac><mfenced close="" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>20</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>40</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>60</mn><mo>-</mo><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open=""><mrow><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>180</mn><mo>-</mo><mi>a</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>200</mn><mo>-</mo><mi>a</mi></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>256</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>20</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>20</mn><mo>-</mo><mi mathvariant="normal">a</mi></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>200</mn><mo>-</mo><mi mathvariant="normal">a</mi></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>256</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>20</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>200</mn><mo>-</mo><mi>a</mi></mrow></mfenced><mo>=</mo><mn>256</mn><mo>&#215;</mo><mn>9</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>-</mo><mn>220</mn><mi>a</mi><mo>+</mo><mn>1696</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>8</mn><mo>,</mo><mn>212</mn></math></p><p>So, maximum value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>212</mn></math>.</p></blockquote>

</details>

---

### Q52. JEE Main 2022 (28 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mfrac><mn>10</mn><msup><mn>3</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfrac><mn>20</mn><msup><mn>3</mn><mn>10</mn></msup></mfrac><mo>+</mo><mfrac><mn>40</mn><msup><mn>3</mn><mn>9</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>10240</mn><mn>3</mn></mfrac><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is odd, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>.</mo><mi>n</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **12**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mfrac><mn>10</mn><msup><mn>3</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfrac><mn>20</mn><msup><mn>3</mn><mn>10</mn></msup></mfrac><mo>+</mo><mfrac><mn>40</mn><msup><mn>3</mn><mn>9</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mn>10240</mn><mn>3</mn></mfrac><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math></p><p>On rearranging we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mn>5</mn><mfenced><mrow><mfrac><msup><mn>2</mn><mn>0</mn></msup><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mfrac><msup><mn>2</mn><mn>1</mn></msup><msup><mn>3</mn><mn>11</mn></msup></mfrac><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><msup><mn>3</mn><mn>10</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>11</mn></msup><mn>3</mn></mfrac></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mn>5</mn><mfenced><mrow><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mfrac><mfenced><mrow><msup><mfenced><mn>6</mn></mfenced><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>6</mn><mo>-</mo><mn>1</mn></mrow></mfenced></mfrac></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>5</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>&#183;</mo><msup><mn>2</mn><mn>12</mn></msup><mo>&#183;</mo><msup><mn>3</mn><mn>12</mn></msup><mo>-</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac></mrow></mfenced><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>+</mo><msup><mn>2</mn><mn>12</mn></msup><mo>-</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>12</mn></msup></mfrac><mo>=</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mn>2</mn><mi>n</mi></msup><mo>&#183;</mo><mi>m</mi><mo>=</mo><msup><mn>2</mn><mn>12</mn></msup></math></p><p>On comparing both side we get,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mi>m</mi><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>12</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>&#183;</mo><mi>n</mi><mo>=</mo><mn>12</mn></math></p></blockquote>

</details>

---

### Q53. JEE Main 2022 (28 Jul Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Consider the sequence <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><msub><mi>a</mi><mn>3</mn></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mo>&#8230;</mo></math>
If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>2</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>3</mn></msub></mfrac></mfenced><mo>&#183;</mo><mfenced><mfrac><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>3</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>4</mn></msub></mfrac></mfenced><mo>&#183;</mo><mfenced><mfrac><mrow><msub><mi>a</mi><mn>3</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>4</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>5</mn></msub></mfrac></mfenced><mo>&#8230;</mo><mfenced><mfrac><mrow><msub><mi>a</mi><mn>30</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>31</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>32</mn></msub></mfrac></mfenced><mo>=</mo><msup><mn>2</mn><mi>&#945;</mi></msup><mfenced><mmultiscripts><mi>C</mi><mn>31</mn><none/><mprescripts/><none/><mn>61</mn></mmultiscripts></mfenced></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>30</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>31</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>60</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>61</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>60</mn></math>**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mfrac><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math></p><p> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mi>n</mi></msub><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><msub><mi>a</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub><msub><mi>a</mi><mi>r</mi></msub></math> is an A.P. with common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mn>2</mn></msub><mo>=</mo><msub><mi>a</mi><mn>2</mn></msub><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>4</mn><mo>,</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mn>2</mn><mi>r</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>2</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>3</mn></msub></mfrac></mfenced><mo>&#183;</mo><mfenced><mfrac><mrow><msub><mi>a</mi><mn>2</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>3</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>4</mn></msub></mfrac></mfenced><mo>&#8943;</mo><mfenced><mfrac><mrow><msub><mi>a</mi><mn>30</mn></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>31</mn></msub></mfrac></mrow><msub><mi>a</mi><mn>32</mn></msub></mfrac></mfenced><mo>=</mo><munderover><mo>&#8719;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfenced><mfrac><mrow><msub><mi>a</mi><mi>i</mi></msub><mo>+</mo><mfrac><mn>1</mn><msub><mi>a</mi><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac></mrow><msub><mi>a</mi><mrow><mi>i</mi><mo>+</mo><mn>2</mn></mrow></msub></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8719;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfenced><mfrac><mrow><msub><mi>a</mi><mi>i</mi></msub><msub><mi>a</mi><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>1</mn></mrow><mrow><msub><mi>a</mi><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow></msub><msub><mi>a</mi><mrow><mi>i</mi><mo>+</mo><mn>2</mn></mrow></msub></mrow></mfrac></mfenced><mo>=</mo><munderover><mo>&#8719;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfrac><mrow><msub><mi>T</mi><mi>r</mi></msub><mo>+</mo><mn>1</mn></mrow><msub><mi>T</mi><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8719;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mfenced><mfrac><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mn>7</mn><mo>&#8943;</mo><mn>61</mn></mrow><mrow><mn>4</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>8</mn><mo>&#8943;</mo><mn>62</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>1</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn><mo>&#183;</mo><mn>5</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>7</mn><mo>&#8943;</mo><mn>61</mn><mo>&#183;</mo><mn>62</mn></mrow><mrow><mn>2</mn><msup><mfenced><mrow><mn>4</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>8</mn><mo>&#8943;</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>62</mn><mo>!</mo></mrow><mrow><mn>2</mn><msup><mfenced><mrow><mn>4</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>8</mn><mo>&#8943;</mo><mn>62</mn></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>62</mn><mo>!</mo></mrow><mrow><msup><mn>2</mn><mn>61</mn></msup><mo>&#183;</mo><msup><mfenced><mrow><mn>31</mn><mo>!</mo></mrow></mfenced><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>62</mn><mfenced><mrow><mn>61</mn><mo>!</mo></mrow></mfenced></mrow><mrow><msup><mn>2</mn><mn>61</mn></msup><mo>&#183;</mo><mn>31</mn><mfenced><mrow><mn>31</mn><mo>!</mo></mrow></mfenced><mfenced><mrow><mn>30</mn><mo>!</mo></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mrow><mo>&#8722;</mo><mn>60</mn></mrow></msup><msup><mo>&#8901;</mo><mn>61</mn></msup><msub><mi>C</mi><mn>30</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mn>2</mn><mrow><mo>-</mo><mn>60</mn></mrow></msup><mo>&#183;</mo><mmultiscripts><mi>C</mi><mn>31</mn><none></none><mprescripts></mprescripts><none></none><mn>61</mn></mmultiscripts></math></p><p>Now on comparing with <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>2</mn><mi>&#945;</mi></msup><mfenced><mmultiscripts><mi>C</mi><mn>31</mn><none></none><mprescripts></mprescripts><none></none><mn>61</mn></mmultiscripts></mfenced></math></p><p>We get <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>60</mn></math></p></blockquote>

</details>

---

### Q54. JEE Main 2022 (27 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>&#215;</mo><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>4</mn><mn>3</mn></msup><mo>-</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>11</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>6</mn><mn>3</mn></msup><mo>-</mo><msup><mn>5</mn><mn>3</mn></msup><mo>+</mo><msup><mn>4</mn><mn>3</mn></msup><mo>-</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>15</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mn>30</mn><mn>3</mn></msup><mo>-</mo><msup><mn>29</mn><mn>3</mn></msup><mo>+</mo><msup><mn>28</mn><mn>3</mn></msup><mo>-</mo><msup><mn>27</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>15</mn><mo>&#215;</mo><mn>63</mn></mrow></mfrac></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **120**

**Detailed Solution:**

<blockquote><p>Given series, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>&#215;</mo><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>4</mn><mn>3</mn></msup><mo>-</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>2</mn><mo>&#215;</mo><mn>11</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>6</mn><mn>3</mn></msup><mo>-</mo><msup><mn>5</mn><mn>3</mn></msup><mo>+</mo><msup><mn>4</mn><mn>3</mn></msup><mo>-</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>3</mn><mo>&#215;</mo><mn>15</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mn>30</mn><mn>3</mn></msup><mo>-</mo><msup><mn>29</mn><mn>3</mn></msup><mo>+</mo><msup><mn>28</mn><mn>3</mn></msup><mo>-</mo><msup><mn>27</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>-</mo><msup><mn>1</mn><mn>3</mn></msup></mrow><mrow><mn>15</mn><mo>&#215;</mo><mn>63</mn></mrow></mfrac></math> </p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced close="]" open="["><mrow><msup><mfenced><mrow><mn>2</mn><mi>k</mi></mrow></mfenced><mn>3</mn></msup><mo>-</mo><msup><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>3</mn></msup></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mn>4</mn><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>k</mi><mfenced><mrow><mn>2</mn><mi>k</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msubsup><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><mfenced><mrow><mn>12</mn><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mn>6</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>3</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>3</mn><mi>n</mi><mo>+</mo><mi>n</mi></mrow><mrow><mi>n</mi><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mi>n</mi></math></p><p>So,<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mi>n</mi></math></p><p>Now finding <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>120</mn></math></p></blockquote>

</details>

---

### Q55. JEE Main 2022 (27 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfenced open="{" close="}"><mrow><mi>n</mi><mo>&#8712;</mo><mi mathvariant="normal">&#8484;</mi><mo>:</mo><mfenced open="|" close="|"><mrow><mi>f</mi><mfenced><mi>n</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>800</mn></mrow></mfenced></math>. Then, the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>n</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is equal to _______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **10620**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="|" open="|"><mrow><mi>f</mi><mfenced><mi>n</mi></mfenced></mrow></mfenced><mo>&#8804;</mo><mn>800</mn></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi><mo>-</mo><mn>801</mn><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mi>n</mi><mo>-</mo><mfrac><mn>801</mn><mn>2</mn></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>801</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mn>6409</mn><mn>16</mn></mfrac><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><msqrt><mn>6409</mn></msqrt><mn>4</mn></mfrac></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><msqrt><mn>6409</mn></msqrt><mn>16</mn></mfrac></mrow></mfenced><mo>&#8804;</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>1</mn><mo>-</mo><msqrt><mn>6409</mn></msqrt></mrow><mn>4</mn></mfrac><mo>&#8804;</mo><mi>n</mi><mo>&#8804;</mo><mfrac><mrow><mn>1</mn><mo>+</mo><msqrt><mn>6409</mn></msqrt></mrow><mn>4</mn></mfrac></math></p><p>Since given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is integer,</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mfenced close="}" open="{"><mrow><mo>-</mo><mn>19</mn><mo>,</mo><mo>-</mo><mn>18</mn><mo>-</mo><mn>17</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>20</mn></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><munder><mo>&#8721;</mo><mrow><mi>n</mi><mo>&#8712;</mo><mi>S</mi></mrow></munder><mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mo>&#8721;</mo><mfenced><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mn>2</mn><mo>&#8721;</mo><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mo>&#8721;</mo><mi>x</mi><mo>-</mo><mo>&#8721;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><mfenced close="]" open="["><mrow><msup><mn>19</mn><mn>2</mn></msup><mo>+</mo><msup><mn>18</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mn>19</mn><mn>2</mn></msup><mo>+</mo><msup><mn>20</mn><mn>2</mn></msup></mrow></mfenced><mo>-</mo><mn>20</mn><mo>-</mo><mn>40</mn></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mtext>as&#160;</mtext><mo>&#8721;</mo><mi>x</mi><mo>=</mo><mn>20</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mo>&#8721;</mo><mn>1</mn><mo>=</mo><mn>40</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>4</mn><mfenced close="]" open="["><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>19</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>2</mn><mfenced close="]" open="["><msup><mn>20</mn><mn>2</mn></msup></mfenced><mo>-</mo><mn>20</mn><mo>-</mo><mn>40</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>19</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mfenced><mrow><mn>2</mn><mo>&#215;</mo><mn>19</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>400</mn><mo>-</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>19</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>39</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mn>800</mn><mo>-</mo><mn>60</mn><mo>-</mo><mn>9880</mn><mo>+</mo><mn>800</mn><mo>-</mo><mn>60</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>10620</mn></math></p></blockquote>

</details>

---

### Q56. JEE Main 2022 (26 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mi>k</mi><mrow><msup><mi>k</mi><mn>4</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **166**

**Detailed Solution:**

<blockquote><p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mi>k</mi><mrow><msup><mi>k</mi><mn>4</mn></msup><mo>+</mo><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mrow><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>-</mo><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="}" open="{"><mrow><mtext>by&#160;using&#160;the&#160;formula&#160;</mtext><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mfrac><mn>1</mn><mfenced><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>-</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><msup><mi>k</mi><mn>2</mn></msup><mo>+</mo><mi>k</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>-</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>-</mo><mfrac><mn>1</mn><mn>111</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>111</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>55</mn><mn>111</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>166</mn></math></p></blockquote>

</details>

---

### Q57. JEE Main 2022 (25 Jul Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>21</mn></munderover><mfrac><mn>3</mn><mrow><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>87</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>29</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>14</mn><mn>87</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>21</mn><mn>29</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>29</mn></mfrac></math>**

**Detailed Solution:**

<blockquote><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>21</mn></munderover><mfrac><mn>3</mn><mrow><mfenced><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>21</mn></munderover><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>4</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>11</mn></mfrac></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>83</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>87</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>87</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><mfrac><mn>84</mn><mn>261</mn></mfrac><mo>=</mo><mfrac><mn>7</mn><mn>29</mn></mfrac></math></p></blockquote>

</details>

---

### Q58. JEE Main 2022 (25 Jul Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><msub><mi>b</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><mn>2</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math> for every natural number <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>2</mn></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>&#183;</mo><msub><mi>b</mi><mi>n</mi></msub></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **27560**

**Detailed Solution:**

<blockquote><p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>-</mo><msub><mi>a</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>2</mn></math></p><p>So the sequence is an A.P. with first term <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn></math> and common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>=</mo><mn>2</mn></math></p><p>i.e., <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>=</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></math></p><p>Also, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>n</mi></msub><mo>=</mo><msub><mi>b</mi><mi>n</mi></msub><mo>-</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub></math></p><p>We know <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>a</mi><mi>n</mi></msub><mo>&#183;</mo><msub><mi>b</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>3</mn></msup><mo>-</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><munderover><mrow><mn>2</mn><mo>&#8721;</mo></mrow><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>n</mi><mn>3</mn></msup><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>n</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>2</mn><msup><mfenced><mfrac><mrow><mn>15</mn><mo>&#183;</mo><mn>16</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>-</mo><mfrac><mrow><mn>15</mn><mo>&#183;</mo><mn>16</mn><mo>&#183;</mo><mn>31</mn></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>27560</mn></math></p></blockquote>

</details>

---

### Q59. JEE Main 2022 (29 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the infinite series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>22</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>35</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>+</mo><mfrac><mn>51</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac><mo>+</mo><mfrac><mn>70</mn><msup><mn>6</mn><mn>6</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>425</mn><mn>216</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>429</mn><mn>216</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>288</mn><mn>125</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>280</mn><mn>125</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>288</mn><mn>125</mn></mfrac></math>**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>5</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>22</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>35</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></math> (i)</p><p>Multiplying with <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math> both side</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>S</mi><mn>6</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>22</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></math> (ii)</p><p>On subtraction equation (i) - equation (ii)</p><p>We get, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>6</mn></mfrac><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>4</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>10</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>13</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo></math>(iii)</p><p>Again multiplying <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>6</mn></mfrac></math> both side,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>5</mn><mn>36</mn></mfrac><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>4</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>7</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>10</mn><msup><mn>6</mn><mn>4</mn></msup></mfrac><mo>+</mo><mfrac><mn>13</mn><msup><mn>6</mn><mn>5</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math>(iv)</p><p>On subtraction equation (iii) - equation (iv)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>36</mn></mfrac><mi>S</mi><mo>=</mo><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>6</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>6</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>3</mn><msup><mn>6</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>=</mo><mfrac><mn>8</mn><mn>5</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mfrac><mn>288</mn><mn>125</mn></mfrac></math></p>

</details>

---

### Q60. JEE Main 2022 (29 Jun Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced close="}" open="{"><msub><mi>a</mi><mi>n</mi></msub></mfenced><mrow><mi>n</mi><mo>=</mo><mn>0</mn></mrow><mo>&#8734;</mo></msubsup></math> be a sequence such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>0</mn></msub><mo>=</mo><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>0</mn></math>. Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>7</mn><mi>n</mi></msup></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>6</mn><mn>343</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>216</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>8</mn><mn>343</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>49</mn><mn>216</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>216</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi>a</mi><mi>n</mi></msub><mo>+</mo><mn>1</mn></math></p><p>Dividing by <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>&#183;</mo><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>49</mn></mfrac><mo>&#183;</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>7</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac><mo>=</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>49</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>7</mn><mi>n</mi></msup></mfrac><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><msup><mn>7</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac></math></p><p>Let
<math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>2</mn></mrow><mo>&#8734;</mo></munderover><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>7</mn><mi>n</mi></msup></mfrac><mo>=</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><msub><mi>a</mi><mn>3</mn></msub><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>-</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>7</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>7</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>49</mn></mfrac><mi>P</mi><mo>+</mo><mfrac><mn>1</mn><msup><mn>7</mn><mn>4</mn></msup></mfrac><mfenced><mfrac><mstyle displaystyle="true"><mn>1</mn></mstyle><mstyle displaystyle="true"><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mstyle></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mo>&#8757;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><msub><mi>a</mi><mn>3</mn></msub><mo>=</mo><mn>3</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>49</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>3</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>2</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>&#183;</mo><msup><mn>7</mn><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mn>36</mn><mi>P</mi></mrow><mn>49</mn></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>42</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>P</mi><mo>=</mo><mfrac><mn>7</mn><mn>216</mn></mfrac></math></p>

</details>

---

### Q61. JEE Main 2022 (28 Jun Shift 2)

*Type:* `numerical` | *Level:* `3`

Let for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mn>50</mn><mo>,</mo><msub><mrow><mo>&#160;</mo><mi>S</mi></mrow><mi>n</mi></msub></math> be the sum of the infinite geometric progression whose first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mn>2</mn></msup></math> and whose common ratio is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>26</mn></mfrac><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><msub><mi>S</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **41651**

**Detailed Solution:**

<p>We have, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mi>r</mi><mo>=</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><msup><mi>n</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mfrac></mrow></mfrac><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced close="]" open="["><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mfrac><mi>n</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mfrac><mrow><mi>n</mi><mo>+</mo><mn>2</mn><mo>-</mo><mn>2</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi mathvariant="normal">i</mi></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><msub><mi>S</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>From equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>-</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mi>n</mi></mrow></mfenced><mo>+</mo><mn>2</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mi>n</mi><mo>+</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mo>&#8943;</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>51</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>52</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>50</mn><mfenced><mn>51</mn></mfenced><mfenced><mn>101</mn></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>50</mn><mfenced><mn>51</mn></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mn>2</mn><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>52</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mn>25</mn></mfenced><mfenced><mn>17</mn></mfenced><mfenced><mn>101</mn></mfenced><mo>-</mo><mn>25</mn><mfenced><mn>51</mn></mfenced><mo>+</mo><mfenced><mfrac><mn>50</mn><mn>52</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>25</mn><mfenced><mrow><mn>1717</mn><mo>-</mo><mn>51</mn></mrow></mfenced><mo>+</mo><mfrac><mn>50</mn><mn>52</mn></mfrac></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>25</mn><mfenced><mn>1666</mn></mfenced><mo>+</mo><mfrac><mn>25</mn><mn>26</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>41650</mn><mo>+</mo><mfrac><mn>25</mn><mn>26</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mfrac><mn>1</mn><mn>26</mn></mfrac><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>50</mn></munderover><mfenced><mrow><msub><mi>S</mi><mi>n</mi></msub><mo>+</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>41650</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>41651</mn></math></p>

</details>

---

### Q62. JEE Main 2022 (27 Jun Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>20</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>30</mn><msup><mn>7</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn><mi>S</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>7</mn><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced><mn>3</mn></msup></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>7</mn><mn>3</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced><mn>4</mn></msup></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced><mn>3</mn></msup></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>20</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>S</mi><mn>7</mn></mfrac><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>12</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mn>20</mn><msup><mn>7</mn><mn>4</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>On subtracting the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math> from equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mi>S</mi></mrow><mn>7</mn></mfrac><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>4</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>6</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>8</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>6</mn><mi>S</mi></mrow><mn>49</mn></mfrac><mo>=</mo><mn>0</mn><mo>+</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>6</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math></p><p>On subtracting the equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>v</mi></mrow></mfenced></math> from  equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>i</mi><mi>i</mi><mi>i</mi></mrow></mfenced></math> , we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mfrac><mn>6</mn><mn>7</mn></mfrac><mo>-</mo><mfrac><mn>6</mn><mn>49</mn></mfrac></mrow></mfenced><mi>S</mi><mo>=</mo><mn>2</mn><mo>+</mo><mfrac><mn>2</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>2</mn><msup><mn>7</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>36</mn><mn>49</mn></mfrac><mi>S</mi><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>7</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><msup><mn>7</mn><mn>2</mn></msup></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#8734;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mi>S</mi><mo>=</mo><mn>2</mn><mo>&#183;</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>7</mn></mfrac></mrow></mfrac><mo>&#183;</mo><mfrac><mn>49</mn><mn>36</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;</mo><mo>&#160;</mo><mn>4</mn><mi>S</mi><mo>=</mo><msup><mfenced><mfrac><mn>7</mn><mn>3</mn></mfrac></mfenced><mn>3</mn></msup></math></p>

</details>

---

### Q63. JEE Main 2022 (27 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

If the sum of the first ten terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>65</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>325</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>1025</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2501</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>m</mi><mi>n</mi></mfrac></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> are co-prime numbers, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi></math> is equal to ______.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **276**

**Detailed Solution:**

<p>For the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>65</mn></mfrac><mo>+</mo><mfrac><mn>3</mn><mn>325</mn></mfrac><mo>+</mo><mfrac><mn>4</mn><mn>1025</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>2501</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mi>n</mi><mrow><mn>4</mn><msup><mi>n</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>n</mi><mrow><msup><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>-</mo><mo>(</mo><mn>2</mn><mi>n</mi><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac><mo>=</mo><mfrac><mi>n</mi><mrow><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>10</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><msub><mrow><mo>&#160;</mo><mi>T</mi></mrow><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>13</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>13</mn></mfrac><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mn>181</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>221</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>221</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>55</mn><mn>221</mn></mfrac><mo>=</mo><mfrac><mi>m</mi><mi>n</mi></mfrac></math></p><p>Hence, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>+</mo><mi>n</mi><mo>=</mo><mn>55</mn><mo>+</mo><mn>221</mn><mo>=</mo><mn>276</mn></math></p>

</details>

---

### Q64. JEE Main 2022 (26 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>min</mi><mfenced open="{" close="}"><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>max</mi><mfenced close="}" open="{"><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> is equal to _____.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1100**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>min</mi><mfenced close="}" open="{"><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>max</mi><mfenced close="}" open="{"><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>min</mi><mfenced><mrow><mi>i</mi><mo>,</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>min</mi><mfenced><mrow><mi>j</mi><mo>,</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mi>min</mi><mfenced><mrow><mi>i</mi><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><mfenced><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mn>19</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo></mrow></munder><mo>+</mo><munder><munder><mfenced><mrow><mn>2</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>2</mn><mo>&#8230;</mo><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mn>17</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo></mrow></munder><mo>+</mo><munder><munder><mfenced><mrow><mn>3</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>&#8230;</mo><mo>+</mo><mn>3</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mn>15</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo></mrow></munder><mo>&#160;</mo><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>max</mi><mfenced><mrow><mi>i</mi><mo>,</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mi>max</mi><mfenced><mrow><mi>j</mi><mo>,</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mi>max</mi><mfenced><mrow><mi>i</mi><mo>,</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munder><munder><mfenced><mrow><mn>10</mn><mo>+</mo><mn>10</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>10</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mn>19</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo></mrow></munder><mo>+</mo><munder><munder><mfenced><mrow><mn>9</mn><mo>+</mo><mn>9</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>9</mn></mrow></mfenced><mo>&#9183;</mo></munder><mrow><mn>17</mn><mo>&#160;</mo><mi>times</mi><mo>&#160;</mo></mrow></munder><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p>i.e. each element of the ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mi>i</mi><mo>,</mo><mi>j</mi></mrow></mfenced></math> will appear either in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>&#160;</mo><mtext>or</mtext><mo>&#160;</mo><mi>B</mi></math></p><p>So <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi></math> will be sum of all elements of the ordered pair </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>+</mo><mi>B</mi><mo>=</mo><mn>20</mn><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>10</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>20</mn><mo>&#215;</mo><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>10</mn><mo>&#215;</mo><mn>110</mn><mo>=</mo><mn>1100</mn></math></p>

</details>

---

### Q65. JEE Main 2022 (25 Jun Shift 1)

*Type:* `numerical` | *Level:* `3`

The greatest integer less than or equal to the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> terms of the sequence <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>,</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mo>,</mo><mfrac><mn>19</mn><mn>27</mn></mfrac><mo>,</mo><mfrac><mn>65</mn><mn>81</mn></mfrac><mo>,</mo><mo>&#8230;</mo></math> is equal to ______

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **98**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mn>5</mn><mn>9</mn></mfrac><mo>+</mo><mfrac><mn>19</mn><mn>27</mn></mfrac><mo>+</mo><mo>&#8943;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow><msup><mn>3</mn><mn>1</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup></mrow><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mrow><msup><mn>3</mn><mn>3</mn></msup><mo>-</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><msup><mn>3</mn><mn>3</mn></msup></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math> terms</p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mi>n</mi></msup></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>100</mn></msub><mo>=</mo><mn>100</mn><mo>&#8722;</mo><mfenced close="]" open="["><mfrac><mrow><mfrac><mn>2</mn><mn>3</mn></mfrac><mfenced close="]" open="["><mrow><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>100</mn></msup></mrow></mfenced></mrow><mrow><mn>1</mn><mo>&#8722;</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>98</mn><mo>+</mo><mn>2</mn><msup><mfenced><mfrac><mn>2</mn><mn>3</mn></mfrac></mfenced><mn>100</mn></msup></math>  <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mo>&#160;&#160;</mo><mfenced close="]" open="["><msub><mi>S</mi><mn>100</mn></msub></mfenced><mo>=</mo><mn>98</mn></math></p>

</details>

---

### Q66. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mo>&#160;</mo><mo>&#8230;</mo><mo>,</mo><mo>&#160;</mo><msub><mi>a</mi><mn>21</mn></msub></math> be an <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> such that <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfrac><mn>1</mn><mrow><msub><mi>a</mi><mi>n</mi></msub><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>.</mo></math> If the sum of this <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>189</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi mathvariant="normal">a</mi><mn>6</mn></msub><msub><mi mathvariant="normal">a</mi><mn>16</mn></msub></math> is equal to :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>57</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>48</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>36</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>72</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfrac><mn>1</mn><mrow><msub><mi>a</mi><mi>n</mi></msub><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;[let common difference of&#160;</mtext><mfenced open="" close="]"><mrow><mi>AP</mi><mo>&#160;</mo><mi>is</mi><mo>&#160;</mo><mi>d</mi><mo>=</mo><msub><mi mathvariant="normal">a</mi><mrow><mi mathvariant="normal">n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>-</mo><msub><mi mathvariant="normal">a</mi><mi mathvariant="normal">n</mi></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfenced><mrow><mfrac><mn>1</mn><msub><mi>a</mi><mi>n</mi></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mfrac></mrow></mfenced><mo>&#8658;</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mfenced close="]" open="["><mrow><mfenced><mrow><mfrac><mn>1</mn><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>2</mn></msub></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msub><mi>a</mi><mn>2</mn></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>3</mn></msub></mfrac></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mfenced><mrow><mfrac><mn>1</mn><msub><mi>a</mi><mn>20</mn></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>21</mn></msub></mfrac></mrow></mfenced></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mfenced><mrow><mfrac><mn>1</mn><msub><mi>a</mi><mn>1</mn></msub></mfrac><mo>-</mo><mfrac><mn>1</mn><msub><mi>a</mi><mn>21</mn></msub></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mi>d</mi></mfrac><mfenced><mfrac><mrow><msub><mi>a</mi><mn>21</mn></msub><mo>-</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>&#183;</mo><msub><mi>a</mi><mn>21</mn></msub></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>&#8658;</mo><mfrac><mrow><mn>20</mn><mi>d</mi></mrow><mrow><mi>d</mi><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>21</mn></msub></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>4</mn><mn>9</mn></mfrac><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><msub><mi>a</mi><mn>21</mn></msub><mo>=</mo><mn>45</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>20</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>45</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p>Now sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>21</mn></math> terms<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>21</mn><mn>2</mn></mfrac><mfenced><mrow><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>20</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>189</mn><mo>&#8658;</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>10</mn><mi>d</mi><mo>=</mo><mn>9</mn><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>2</mn><mo>)</mo></math></p><p>by using equation <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>1</mn><mo>)</mo></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo></math> we get <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>3</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math> otherwise <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>15</mn><mo>,</mo><mo>&#160;</mo><mi>d</mi><mo>=</mo><mo>-</mo><mfrac><mn>3</mn><mn>5</mn></mfrac></math></p><p>So, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>6</mn></msub><msub><mi>a</mi><mn>16</mn></msub><mo>=</mo><mfenced><mrow><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>5</mn><mi>d</mi></mrow></mfenced><mfenced><mrow><msub><mi>a</mi><mrow><mn>1</mn><mo>+</mo></mrow></msub><mo>+</mo><mn>15</mn><mi>d</mi></mrow></mfenced><mo>=</mo><mn>72</mn></math></p>

</details>

---

### Q67. JEE Main 2021 (01 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;Let&#160;</mtext><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>1</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>3</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#10878;</mo><mn>4</mn><mo>.</mo></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>The sum&#160;</mtext><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">n</mi><mo>=</mo><mn>4</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mrow><mfrac><mrow><mn>2</mn><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">S</mi></mrow><mi mathvariant="normal">n</mi></msub></mrow><mrow><mi mathvariant="normal">n</mi><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mi mathvariant="normal">n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></mrow></mfenced><mtext>&#160;is equal to :</mtext></math> </p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>e</mi><mo>-</mo><mn>2</mn></mrow><mn>6</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">e</mi><mn>6</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi mathvariant="normal">e</mi><mn>3</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi mathvariant="normal">e</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>&#160;Let&#160;</mtext><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>1</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>+</mo><mn>3</mn><mo>&#183;</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>&#183;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>&#10878;</mo><mn>4</mn><mo>.</mo><mspace linebreak="newline"></mspace><mi>General</mi><mo>&#160;</mo><mi>form</mi><mo>&#160;</mo><mi>of</mi><mo>&#160;</mo><msub><mi mathvariant="normal">S</mi><mi mathvariant="normal">n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></munderover><mi>r</mi><mo>(</mo><mi>n</mi><mo>-</mo><mi>r</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mspace linebreak="newline"></mspace></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>2</mn><msub><mrow><mo>&#160;</mo><mi mathvariant="normal">S</mi></mrow><mi>n</mi></msub></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mi>n</mi><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>3</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mrow><mfrac><mrow><mn>2</mn><msub><mi>S</mi><mi>n</mi></msub></mrow><mrow><mi>n</mi><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></mrow></mfenced><mspace linebreak="newline"/></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mrow><mfrac><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><mn>3</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo></mrow><mrow><mn>3</mn><mo>(</mo><mi>n</mi><mo>-</mo><mn>2</mn><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mn>1</mn><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>3</mn><mo>)</mo><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>e</mi><mo>-</mo><mn>1</mn></mrow><mn>3</mn></mfrac></math></p>

</details>

---

### Q68. JEE Main 2021 (31 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<p>The sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math> terms of the series  <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math> is :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>143</mn><mn>144</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>99</mn><mn>100</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><mn>121</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>120</mn><mn>121</mn></mfrac></math>**

**Detailed Solution:**

<p>Given that</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>&#215;</mo><msup><mn>4</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></math></p><p>Here <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>7</mn><mo>,</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>&#8712;</mo><mi>A</mi><mo>.</mo><mi>P</mi></math></p><p>First term <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo></math>Common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi><mo>&#160;</mo><mo>=</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><msub><mi>t</mi><mi>r</mi></msub><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mi>a</mi><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mi>d</mi><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>3</mn><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><mfenced><mrow><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>2</mn><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mrow><mo>(</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfrac><mrow><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>&#183;</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced close="}" open="{"><mrow><mfrac><mn>1</mn><msup><mi>r</mi><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>1</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>2</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>3</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mn>4</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><msup><mn>10</mn><mn>2</mn></msup></mfrac><mo>-</mo><mfrac><mn>1</mn><msup><mn>11</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>121</mn></mfrac><mo>=</mo><mfrac><mn>120</mn><mn>121</mn></mfrac></math></p>

</details>

---

### Q69. JEE Main 2021 (27 Aug Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></msup></math> at <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mn>2</mn></msup></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msup><mi>e</mi><mn>2</mn></msup></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msqrt><mi mathvariant="normal">e</mi></msqrt></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mn>2</mn></msup></math>**

**Detailed Solution:**

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8943;</mo><mo>&#8943;</mo><mo>&#183;</mo><mo>&#8943;</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8943;</mo><mo>&#8943;</mo></mrow></mfenced><mo>-</mo><mfenced><mrow><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#8943;</mo><mo>&#8943;</mo></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>x</mi><mo>-</mo><mfenced><mrow><mi>x</mi><mo>+</mo><mfrac><msup><mi>x</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mfrac><msup><mi>x</mi><mn>4</mn></msup><mn>4</mn></mfrac><mo>+</mo><mo>&#8943;</mo><mo>&#8943;</mo><mo>&#8943;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mi>x</mi><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>&#8467;</mi><mi>n</mi><mo>(</mo><mn>1</mn><mo>-</mo><mi>x</mi><mo>)</mo></math>
Put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>&#8467;</mi><mi>n</mi><mn>2</mn></math></p><p>Then, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mrow><mn>1</mn><mo>+</mo><mi>y</mi></mrow></msup><mo>=</mo><msup><mi>e</mi><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>-</mo><mi>&#8467;</mi><mi>n</mi><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>e</mi><mn>2</mn></msup></math></p>

</details>

---

### Q70. JEE Main 2021 (27 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

<p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>,</mo></math> is equal to</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>5</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>-</mo><mo>-</mo><mo>-</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mo>-</mo><mo>-</mo><mo>-</mo><mo>-</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mo>-</mo><mo>-</mo></mrow></mfenced><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mfrac><mn>3</mn><mn>4</mn></mfrac><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mo>-</mo><mo>-</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mo>-</mo><mo>-</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><msup><mi>x</mi><mn>3</mn></msup><mo>-</mo><mo>-</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>2</mn><mfenced><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mo>-</mo><mo>-</mo><mo>-</mo></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mn>2</mn></mfrac><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mfrac><msup><mi>x</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>-</mo><mo>-</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>&#8658;</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mo>+</mo><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi><mo>-</mo><msup><mi>x</mi><mn>2</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>ln</mi><mo>&#160;</mo><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac><mo>+</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mi>x</mi><mfenced><mfrac><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfrac></mfenced><mo>+</mo><mi>ln</mi><mfenced><mrow><mn>1</mn><mo>-</mo><mi>x</mi></mrow></mfenced></math></p>

</details>

---

### Q71. JEE Main 2021 (26 Aug Shift 1)

*Type:* `numerical` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mn>1</mn><none/><mprescripts/><none/><mn>1</mn></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>2</mn><none/><mprescripts/><none/><mn>2</mn></mmultiscripts><mo>+</mo><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>3</mn><none/><mprescripts/><none/><mn>3</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>15</mn><none/><mprescripts/><none/><mn>15</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>P</mi><mi>r</mi><none/><mprescripts/><none/><mi>q</mi></mmultiscripts><mo>-</mo><mi>s</mi><mo>,</mo><mo>&#160;</mo><mn>0</mn><mo>&#8804;</mo><mi>s</mi><mo>&#8804;</mo><mn>1</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mi>s</mi></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>q</mi><mo>+</mo><mi>s</mi></mrow></mmultiscripts></math> is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **136**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>P</mi><mn>1</mn><none></none><mprescripts></mprescripts><none></none><mn>1</mn></mmultiscripts><mo>+</mo><mn>2</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>2</mn><none></none><mprescripts></mprescripts><none></none><mn>2</mn></mmultiscripts><mo>+</mo><mn>3</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>3</mn><none></none><mprescripts></mprescripts><none></none><mn>3</mn></mmultiscripts><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><mmultiscripts><mi>P</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>15</mn></mmultiscripts><mo>=</mo><mmultiscripts><mi>P</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mo>-</mo><mi>s</mi></math></p><p>where, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#8804;</mo><mi>s</mi><mo>&#8804;</mo><mn>1</mn></math></p><p>Now,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow></mrow><mn>1</mn></msup><msub><mi>P</mi><mn>1</mn></msub><mo>+</mo><mn>2</mn><msup><mo>&#183;</mo><mn>2</mn></msup><msub><mi>P</mi><mn>2</mn></msub><mo>+</mo><mn>3</mn><msup><mo>&#8901;</mo><mn>3</mn></msup><msub><mi>P</mi><mn>3</mn></msub><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>15</mn><msup><mo>&#183;</mo><mn>15</mn></msup><msub><mi>P</mi><mn>15</mn></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>!</mo><mo>+</mo><mn>2</mn><mo>&#183;</mo><mn>2</mn><mo>!</mo><mo>+</mo><mn>3</mn><mo>&#183;</mo><mn>3</mn><mo>!</mo><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mn>15</mn><mo>&#183;</mo><mn>15</mn><mo>!</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>2</mn><mo>!</mo><mo>-</mo><mn>1</mn><mo>!</mo><mo>)</mo><mo>+</mo><mo>(</mo><mn>3</mn><mo>!</mo><mo>-</mo><mn>2</mn><mo>!</mo><mo>)</mo><mo>+</mo><mo>(</mo><mn>4</mn><mo>!</mo><mo>-</mo><mn>3</mn><mo>!</mo><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mo>(</mo><mn>16</mn><mo>!</mo><mo>-</mo><mn>15</mn><mo>!</mo><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced close="]" open="["><mrow><mo>&#8757;</mo><mi>n</mi><mo>&#183;</mo><mi>n</mi><mo>!</mo><mo>=</mo><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mi>n</mi><mo>!</mo><mo>=</mo><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mi>n</mi><mo>!</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>16</mn><mo>!</mo><mo>&#8722;</mo><mn>1</mn><mo>!</mo><mo>=</mo><mmultiscripts><mi>P</mi><mi>r</mi><none></none><mprescripts></mprescripts><none></none><mi>q</mi></mmultiscripts><mo>&#8722;</mo><mi mathvariant="normal">s</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">&#8658;</mo><mi>q</mi><mo>=</mo><mi>r</mi><mo>=</mo><mn>16</mn><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mi>s</mi><mo>=</mo><mn>1</mn></math></p><p>So,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mmultiscripts><mi>C</mi><mrow><mi>r</mi><mo>-</mo><mi>s</mi></mrow><none></none><mprescripts></mprescripts><none></none><mrow><mi>q</mi><mo>+</mo><mi>s</mi></mrow></mmultiscripts><mo>=</mo><mmultiscripts><mi>C</mi><mn>15</mn><none></none><mprescripts></mprescripts><none></none><mn>17</mn></mmultiscripts><mo>=</mo><mfrac><mrow><mn>17</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>136</mn></math></p>

</details>

---

### Q72. JEE Main 2021 (26 Aug Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>100</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math> when <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn></math> is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mn>4</mn><mn>101</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mn>4</mn><mn>101</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mn>4</mn><mn>101</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mn>4</mn><mn>201</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>-</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mn>4</mn><mn>101</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Adding and subtracting <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>2</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>100</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mrow><mi>x</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><mn>2</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>100</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfenced><mrow><mfrac><mn>2</mn><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mo>-</mo><mn>2</mn></mrow><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>100</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfenced><mfrac><mrow><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup></mrow><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></mfenced><mo>+</mo><mfrac><msup><mn>2</mn><mn>2</mn></msup><mrow><msup><mi>x</mi><mn>4</mn></msup><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><mfrac><msup><mn>2</mn><mn>100</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>100</mn></msup></msup><mo>+</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><mi>x</mi><mo>-</mo><mn>1</mn></mrow></mfrac><mo>-</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mi>x</mi><msup><mn>2</mn><mn>101</mn></msup></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>=</mo><mn>2</mn><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mn>2</mn><msup><mn>2</mn><mn>101</mn></msup></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mn>1</mn><mo>-</mo><mfrac><msup><mn>2</mn><mn>101</mn></msup><mrow><msup><mn>4</mn><mn>101</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p>

</details>

---

### Q73. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>&#8712;</mo><mi>N</mi><mo>,</mo></math> let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>.</mo><mo>(</mo><mi>&#945;</mi><mo>+</mo><mn>20</mn><mo>)</mo></mrow></mfrac><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>K</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><mfrac><msub><mi>A</mi><mi>k</mi></msub><mrow><mi>&#945;</mi><mo>+</mo><mi>k</mi></mrow></mfrac><mo>,</mo></math> where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#62;</mo><mn>0</mn><mo>.</mo></math> Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msup><mfenced><mfrac><mrow><msub><mi>A</mi><mn>14</mn></msub><mo>+</mo><msub><mi>A</mi><mn>15</mn></msub></mrow><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>13</mn></msub></mfrac></mfenced><mn>2</mn></msup></math> is equal to ____________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **9**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mn>20</mn></munderover><mfenced><mfrac><msub><mi>A</mi><mi>k</mi></msub><mrow><mi>&#945;</mi><mo>+</mo><mi>k</mi></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>A</mi><mn>0</mn></msub><mi>&#945;</mi></mfrac><mo>+</mo><mfrac><msub><mi>A</mi><mn>1</mn></msub><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><msub><mi>A</mi><mn>20</mn></msub><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><msub><mi>A</mi><mn>0</mn></msub><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>A</mi><mn>20</mn></msub><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced></mrow><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>A</mi><mn>0</mn></msub><mfenced close="]" open="["><mrow><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub><mfenced close="]" open="["><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>A</mi><mn>20</mn></msub><mfenced close="]" open="["><mrow><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>&#8230;</mo><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced></mrow></mfenced><mo>=</mo><mn>1</mn><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p>Hence, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>13</mn></msub></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>12</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>14</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math>.</p><p>Similarly, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>14</mn></msub></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>13</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>15</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math></p><p>And, coefficient of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>15</mn></msub></math> is</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>14</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>16</mn></mrow></mfenced><mo>&#8230;</mo><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>&#945;</mi><mo>+</mo><mn>20</mn></mrow></mfenced></math></p><p>Then, to find <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>14</mn></msub></math>, put <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>14</mn></math> in <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced></math>, then we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>14</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mo>-</mo><mn>14</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>13</mn><mo>)</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>6</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>14</mn><mo>!</mo><mo>&#183;</mo><mn>6</mn><mo>!</mo></mrow></mfrac></math></p><p>Similarly, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>15</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>15</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mo>-</mo><mn>15</mn><mo>)</mo><mo>(</mo><mo>-</mo><mn>14</mn><mo>)</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>5</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mrow><mn>15</mn><mo>!</mo><mo>&#183;</mo><mn>5</mn><mo>!</mo></mrow></mfrac></math></p><p>And, putting <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mo>-</mo><mn>13</mn></math>, we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>13</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mo>-</mo><mn>13</mn><mo>)</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>(</mo><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>(</mo><mn>7</mn><mo>)</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mn>13</mn><mo>!</mo><mo>&#183;</mo><mn>7</mn><mo>!</mo></mrow></mfrac></math></p><p>Hence,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>A</mi><mn>14</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>13</mn></msub></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>14</mn><mo>!</mo><mo>&#183;</mo><mn>6</mn><mo>!</mo></mrow></mfrac><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>13</mn><mo>!</mo><mo>&#215;</mo><mn>7</mn><mo>!</mo></mrow></mfenced><mo>=</mo><mfrac><mrow><mo>-</mo><mn>7</mn></mrow><mn>14</mn></mfrac><mo>=</mo><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msub><mi>A</mi><mn>15</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>13</mn></msub></mfrac><mo>=</mo><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mrow><mn>15</mn><mo>!</mo><mo>&#215;</mo><mn>5</mn><mo>!</mo></mrow></mfrac></mrow></mfenced><mo>&#215;</mo><mfenced><mrow><mo>-</mo><mn>13</mn><mo>!</mo><mo>&#215;</mo><mn>7</mn><mo>!</mo></mrow></mfenced><mo>=</mo><mfrac><mn>42</mn><mrow><mn>15</mn><mo>&#215;</mo><mn>14</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></math></p><p>Then,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msup><mfenced><mrow><mfrac><msub><mi>A</mi><mn>14</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>13</mn></msub></mfrac><mo>+</mo><mfrac><msub><mi>A</mi><mn>15</mn></msub><msub><mrow><mo>&#160;</mo><mi>A</mi></mrow><mn>13</mn></msub></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>100</mn><msup><mfenced><mrow><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>5</mn></mfrac></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>9</mn></math></p>

</details>

---

### Q74. JEE Main 2021 (20 Jul Shift 2)

*Type:* `numerical` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mfenced open="{" close="}"><msub><mi>a</mi><mi>n</mi></msub></mfenced><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></msubsup></math> be a sequence such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>1</mn><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>=</mo><mn>1</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math> for all <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>&#8805;</mo><mn>1</mn></math>. Then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>2</mn><mrow><mn>3</mn><mi>n</mi></mrow></msup></mfrac></mfenced></math> is equal to ________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **7**

**Detailed Solution:**

<p>We have,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>47</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>2</mn><mrow><mn>3</mn><mi>n</mi></mrow></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac></mfenced><mo>=</mo><mi>P</mi></math>(let)</p><p>And,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><mo>=</mo><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>a</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><msup><mn>8</mn><mi>n</mi></msup></mfrac><mo>+</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>64</mn><mfenced><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mn>8</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac></mfenced><mo>=</mo><mfrac><mrow><mn>16</mn><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mrow><msup><mn>8</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac><mo>+</mo><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>64</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msub><msup><mn>8</mn><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></msup></mfrac></mfenced><mo>=</mo><mn>16</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub><msup><mn>8</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msup></mfrac></mfenced><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>64</mn><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><msub><mi>a</mi><mn>1</mn></msub><mn>8</mn></mfrac><mo>-</mo><mfrac><msub><mi>a</mi><mn>2</mn></msub><msup><mn>8</mn><mn>2</mn></msup></mfrac></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><msub><mi>a</mi><mn>1</mn></msub><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>64</mn><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>64</mn></mfrac></mrow></mfenced><mo>=</mo><mn>16</mn><mfenced><mrow><mi>P</mi><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>64</mn><mi>P</mi><mo>-</mo><mn>8</mn><mo>-</mo><mn>1</mn><mo>=</mo><mn>16</mn><mi>P</mi><mo>-</mo><mn>2</mn><mo>+</mo><mi>P</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>47</mn><mi>P</mi><mo>=</mo><mn>7</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>47</mn><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfenced><mfrac><msub><mi>a</mi><mi>n</mi></msub><msup><mn>8</mn><mi>n</mi></msup></mfrac></mfenced><mo>=</mo><mn>7</mn></math></p>

</details>

---

### Q75. JEE Main 2021 (18 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><mo>!</mo><mfenced><mrow><msup><mi>r</mi><mn>3</mn></msup><mo>+</mo><mn>6</mn><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>r</mi><mo>+</mo><mn>5</mn></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mfenced><mrow><mn>11</mn><mo>!</mo></mrow></mfenced></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi></math> is equal to ___ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **160**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mi>r</mi><mo>!</mo><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced><mrow><mi>r</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mn>9</mn><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>8</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced close="]" open="["><mrow><mfenced close="}" open="{"><mrow><mo>(</mo><mi>r</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>!</mo><mo>-</mo><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>!</mo></mrow></mfenced><mo>-</mo><mn>8</mn><mfenced close="}" open="{"><mrow><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo><mo>-</mo><mi>r</mi><mo>!</mo></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>13</mn><mo>!</mo><mo>+</mo><mn>12</mn><mo>!</mo><mo>-</mo><mn>2</mn><mo>!</mo><mo>-</mo><mn>3</mn><mo>!</mo><mo>)</mo><mo>-</mo><mn>8</mn><mo>(</mo><mn>11</mn><mo>!</mo><mo>-</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>12</mn><mo>.</mo><mn>13</mn><mo>+</mo><mn>12</mn><mo>-</mo><mn>8</mn><mo>)</mo><mo>&#183;</mo><mn>11</mn><mo>!</mo><mo>-</mo><mn>8</mn><mo>+</mo><mn>8</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>(</mo><mn>160</mn><mo>)</mo><mo>(</mo><mn>11</mn><mo>)</mo><mo>!</mo></math></p><p>Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>160</mn></math></p>

</details>

---

### Q76. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>5</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>7</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>201</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>101</mn><mn>404</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>101</mn></mfrac></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>101</mn><mn>408</mn></mfrac></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>99</mn><mn>400</mn></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>25</mn><mn>101</mn></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mrow><msup><mn>3</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>5</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><msup><mn>7</mn><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>201</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mo>(</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup><mo>-</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>(</mo><mi>n</mi><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mfrac><mrow><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>-</mo><mi>n</mi></mrow><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow></mfrac></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>100</mn></munderover><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfenced><mrow><mfrac><mn>1</mn><mn>100</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>101</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>101</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced><mfrac><mn>100</mn><mn>101</mn></mfrac></mfenced><mo>=</mo><mfrac><mn>25</mn><mn>101</mn></mfrac></math></p>

</details>

---

### Q77. JEE Main 2021 (18 Mar Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></math> are natural numbers such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>100</mn><mi>&#945;</mi></msup><mo>-</mo><mn>199</mn><mi>&#946;</mi><mo>=</mo><mo>(</mo><mn>100</mn><mo>)</mo><mo>(</mo><mn>100</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>99</mn><mo>)</mo><mo>(</mo><mn>101</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>98</mn><mo>)</mo><mo>(</mo><mn>102</mn><mo>)</mo><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>.</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>199</mn><mo>)</mo><mo>,</mo></math> then the slope of the line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi><mo>)</mo></math> and origin is:<gwmw style="display:none;"></gwmw>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>540</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>550</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>530</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>510</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>550</mn></math>**

**Detailed Solution:**

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mo>(</mo><mn>100</mn><mo>)</mo><mo>(</mo><mn>100</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>99</mn><mo>)</mo><mo>(</mo><mn>101</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>98</mn><mo>)</mo><mo>(</mo><mn>102</mn><mo>)</mo><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mo>(</mo><mn>2</mn><mo>)</mo><mo>(</mo><mn>198</mn><mo>)</mo><mo>+</mo><mo>(</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>199</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><mn>99</mn></munderover><mfenced><mrow><mn>100</mn><mo>-</mo><mi>x</mi></mrow></mfenced><mfenced><mrow><mn>100</mn><mo>+</mo><mi>x</mi></mrow></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><mn>99</mn></munderover><msup><mn>100</mn><mn>2</mn></msup><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><mn>99</mn></munderover><msup><mi>x</mi><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><mfrac><mrow><mn>99</mn><mo>&#215;</mo><mn>100</mn><mo>&#215;</mo><mn>199</mn></mrow><mn>6</mn></mfrac><mo>=</mo><msup><mn>100</mn><mn>3</mn></msup><mo>-</mo><mn>199</mn><mo>&#215;</mo><mn>1650</mn></math></p><p>Given that, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mn>100</mn><mi>&#945;</mi></msup><mo>-</mo><mn>199</mn><mi>&#946;</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><mi>&#945;</mi><mo>=</mo><mn>3</mn></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#946;</mi><mo>=</mo><mn>1650</mn></math></p><p>The slope of line passing through <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mi>&#946;</mi></mrow></mfenced><mo>&#160;</mo><mo>&#38;</mo><mo>&#160;</mo><mfenced><mrow><mn>0</mn><mo>,</mo><mn>0</mn></mrow></mfenced></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>1650</mn><mo>-</mo><mn>0</mn></mrow><mrow><mn>3</mn><mo>-</mo><mn>0</mn></mrow></mfrac><mo>=</mo><mn>550</mn></math></p>

</details>

---

### Q78. JEE Main 2021 (16 Mar Shift 2)

*Type:* `numerical` | *Level:* `2`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>6</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>11</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>18</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>27</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>-terms, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>&#62;</mo><mn>1</mn></math>. If <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>24</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1093</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>12</mn></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>265</mn><mo>,</mo></math> then value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math> is equal to _____ .

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **16**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>2</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi>a</mi><mrow><mn>1</mn><mo>/</mo><mn>6</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>11</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>18</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><msub><mi>log</mi><msup><mi mathvariant="normal">a</mi><mrow><mn>1</mn><mo>/</mo><mn>27</mn></mrow></msup></msub><mi>x</mi><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi><mo>-</mo><mtext>terms</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mo>(</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>27</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi></math>-terms <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>)</mo><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi></math></p><p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>27</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>18</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mi>i</mi></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mn>0</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>6</mn><mo>+</mo><mn>11</mn><mo>+</mo><mn>18</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msub><mi>T</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>T</mi><mi>n</mi></msub><mo>&#160;</mo><mo>&#160;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced></math></p><p>Subtract <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mi>i</mi></mfenced><mo>&#160;</mo><mtext>from</mtext><mo>&#160;</mo><mfenced><mrow><mi>i</mi><mi>i</mi></mrow></mfenced><mo>&#160;</mo></math>we get, </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mtext>upto&#160;</mtext><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mtext>-term</mtext></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><mo>+</mo><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mi>&#931;</mi><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mi>n</mi><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>6</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mi>n</mi></msub><mfenced><mi>x</mi></mfenced><mo>=</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn><mo>)</mo></mrow><mn>6</mn></mfrac></mrow></mfenced><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>24</mn></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1093</mn></math> (Given)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi><mfenced><mrow><mn>48</mn><mo>+</mo><mfrac><mrow><mn>23</mn><mo>.</mo><mn>24</mn><mo>.</mo><mn>47</mn></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mn>1093</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math> ......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>1</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>12</mn></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>265</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>12</mn></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo><mo>=</mo><mn>265</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mo>(</mo><mn>2</mn><mi>x</mi><mo>)</mo><mfenced><mrow><mn>24</mn><mo>+</mo><mfrac><mrow><mn>11</mn><mo>.</mo><mn>12</mn><mo>.</mo><mn>23</mn></mrow><mn>6</mn></mfrac></mrow></mfenced><mo>=</mo><mn>265</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mn>2</mn><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></math> ......<math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mn>2</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>2</mn><mo>)</mo><mo>-</mo><mo>(</mo><mn>1</mn><mo>)</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mn>2</mn><mi>x</mi><mo>-</mo><msub><mi>log</mi><mi>a</mi></msub><mi>x</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>a</mi></msub><mn>2</mn><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mn>16</mn></math></p>

</details>

---

### Q79. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#60;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#60;</mo><mn>1</mn></math>, and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>b</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac></math>, then the value of <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mo>-</mo><mfenced><mfrac><mrow><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><mn>2</mn></mfrac></mfenced><mo>+</mo><mfenced><mfrac><mrow><msup><mi>a</mi><mn>3</mn></msup><mo>+</mo><msup><mi>b</mi><mn>3</mn></msup></mrow><mn>3</mn></mfrac></mfenced><mo>-</mo><mfenced><mfrac><mrow><msup><mi>a</mi><mn>4</mn></msup><mo>+</mo><msup><mi>b</mi><mn>4</mn></msup></mrow><mn>4</mn></mfrac></mfenced><mo>+</mo><mo>&#8230;</mo></math> is :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mfrac><mi>e</mi><mn>2</mn></mfrac></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>e</mi></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>e</mi><mn>2</mn></msup><mo>-</mo><mn>1</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mi>a</mi><mo>+</mo><msup><mi>tan</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>&#160;</mo><mi>b</mi><mo>=</mo><mfrac><mi>&#960;</mi><mn>4</mn></mfrac><mo>&#160;</mo><mn>0</mn><mo>&#60;</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mrow><mn>1</mn><mo>-</mo><mi>a</mi><mi>b</mi></mrow></mfrac><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi><mo>=</mo><mn>1</mn><mo>-</mo><mi>a</mi><mi>b</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>a</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>b</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>=</mo><mn>2</mn></math></p><p>Now <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mi>a</mi><mo>-</mo><mfrac><msup><mi>a</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>a</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>+</mo><mfenced open="[" close="]"><mrow><mi>b</mi><mo>-</mo><mfrac><msup><mi>b</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>+</mo><mfrac><msup><mi>b</mi><mn>3</mn></msup><mn>3</mn></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced><mo>+</mo><msub><mi>log</mi><mi>e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></math></p><p>(<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo></math> expansion of <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfenced></math>)</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi mathvariant="normal">e</mi></msub><mfenced open="[" close="]"><mrow><mfenced><mrow><mn>1</mn><mo>+</mo><mi>a</mi></mrow></mfenced><mfenced><mrow><mn>1</mn><mo>+</mo><mi>b</mi></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msub><mi>log</mi><mi>e</mi></msub><mn>2</mn></math></p>

</details>

---

### Q80. JEE Main 2021 (26 Feb Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>&#8734;</mo></munderover><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>n</mi><mo>+</mo><mn>10</mn></mrow><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>41</mn><mn>8</mn></mfrac><mi>e</mi><mo>+</mo><mfrac><mn>19</mn><mn>8</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>10</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>41</mn><mn>8</mn></mfrac><mi>e</mi><mo>+</mo><mfrac><mn>19</mn><mn>8</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>10</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mfrac><mn>41</mn><mn>8</mn></mfrac><mi>e</mi><mo>+</mo><mfrac><mn>19</mn><mn>8</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>10</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>41</mn><mn>8</mn></mfrac><mi>e</mi><mo>-</mo><mfrac><mn>19</mn><mn>8</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>41</mn><mn>8</mn></mfrac><mi>e</mi><mo>-</mo><mfrac><mn>19</mn><mn>8</mn></mfrac><msup><mi>e</mi><mrow><mo>-</mo><mn>1</mn></mrow></msup><mo>-</mo><mn>10</mn></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>6</mn><mi>n</mi><mo>+</mo><mn>10</mn></mrow><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>4</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>24</mn><mi>n</mi><mo>+</mo><mn>40</mn></mrow><mrow><mn>4</mn><mo>.</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mn>20</mn><mi>n</mi><mo>+</mo><mn>39</mn></mrow><mrow><mn>4</mn><mo>.</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><msup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>.</mo><mn>10</mn><mo>+</mo><mn>29</mn></mrow><mrow><mn>4</mn><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><msup><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>10</mn></mrow><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>29</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>10</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>29</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>11</mn><mrow><mfenced><mrow><mn>2</mn><mi>n</mi></mrow></mfenced><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>29</mn><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>!</mo></mrow></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>=</mo><mfrac><mn>1</mn><mrow><mn>1</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>=</mo><mfrac><mrow><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>2</mn></msub><mo>=</mo><mn>11</mn><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mrow><mn>2</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><mn>11</mn><mfenced open="[" close="]"><mfrac><mfenced open="" close="]"><mrow><mi>e</mi><mo>+</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></mfrac></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>3</mn></msub><mo>=</mo><mn>29</mn><mfenced open="[" close="]"><mrow><mfrac><mn>1</mn><mrow><mn>3</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>7</mn><mo>!</mo></mrow></mfrac><mo>+</mo><mo>&#8230;</mo></mrow></mfenced><mo>=</mo><mn>29</mn><mfenced open="[" close="]"><mfrac><mrow><mi>e</mi><mo>-</mo><mfrac><mn>1</mn><mi>e</mi></mfrac><mo>-</mo><mn>2</mn></mrow><mn>2</mn></mfrac></mfenced></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><msub><mi>S</mi><mn>1</mn></msub><mo>+</mo><msub><mi>S</mi><mn>2</mn></msub><mo>+</mo><msub><mi>S</mi><mn>3</mn></msub></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfrac><mi>e</mi><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>11</mn><mi>e</mi></mrow><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>11</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>29</mn><mi>e</mi></mrow><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>29</mn><mrow><mn>2</mn><mi>e</mi></mrow></mfrac><mo>-</mo><mn>4</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>41</mn><mi>e</mi></mrow><mn>8</mn></mfrac><mo>-</mo><mfrac><mn>19</mn><mrow><mn>8</mn><mi>e</mi></mrow></mfrac><mo>-</mo><mn>10</mn></math></p>

</details>

---

### Q81. JEE Main 2020 (04 Sep Shift 1)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mn>2</mn><mn>2</mn></msup><mo>&#183;</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mn>4</mn><mn>2</mn></msup><mo>&#183;</mo><mn>3</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mn>6</mn><mn>2</mn></msup><mo>&#183;</mo><mn>5</mn></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><mfenced><mrow><mn>1</mn><mo>-</mo><msup><mn>20</mn><mn>2</mn></msup><mo>&#183;</mo><mn>19</mn></mrow></mfenced><mo>=</mo><mi>&#945;</mi><mo>-</mo><mn>220</mn><mo>&#160;</mo><mi>&#946;</mi></math>, then an ordered pair <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo>,</mo><mo>&#160;</mo><mi>&#946;</mi></mrow></mfenced></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>97</mn></mrow></mfenced></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>103</mn><mo>)</mo></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>10</mn><mo>,</mo><mo>&#160;</mo><mn>103</mn></mrow></mfenced></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>97</mn></mrow></mfenced></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>(</mo><mn>11</mn><mo>,</mo><mo>&#160;</mo><mn>103</mn><mo>)</mo></math>**

**Detailed Solution:**

<p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">S</mi><mo>=</mo><mn>1</mn><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mn>1</mn><mo>&#8722;</mo><msup><mfenced><mrow><mn>2</mn><mi mathvariant="normal">r</mi></mrow></mfenced><mn>2</mn></msup><mfenced><mrow><mn>2</mn><mi mathvariant="normal">r</mi><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>1</mn><mo>+</mo><mn>10</mn><mo>&#8722;</mo><munderover><mo>&#8721;</mo><mrow><mi mathvariant="normal">r</mi><mo>=</mo><mn>1</mn></mrow><mn>10</mn></munderover><mfenced><mrow><mn>8</mn><msup><mi mathvariant="normal">r</mi><mn>3</mn></msup><mo>&#8722;</mo><mn>4</mn><msup><mi mathvariant="normal">r</mi><mn>2</mn></msup></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#8722;</mo><mfenced close="]" open="["><mrow><mn>8</mn><msup><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#8722;</mo><mn>4</mn><mfenced><mfrac><mrow><mn>10</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#8722;</mo><mfenced close="]" open="["><mrow><mn>2</mn><msup><mfenced><mn>110</mn></mfenced><mn>2</mn></msup><mo>&#8722;</mo><mn>140</mn><mo>&#215;</mo><mn>11</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#8722;</mo><mn>22</mn><mfenced><mrow><mn>1100</mn><mo>&#8722;</mo><mn>70</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#8722;</mo><mn>220</mn><mfenced><mrow><mn>110</mn><mo>&#8722;</mo><mn>7</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>&#8722;</mo><mn>220</mn><mi>&#946;</mi></math><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>11</mn><mo>&#8722;</mo><mn>220</mn><mfenced><mn>103</mn></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo></math> <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>&#945;</mi><mo>=</mo><mn>11</mn><mo>,</mo><mtext>&#8201;</mtext><mi>&#946;</mi><mo>=</mo><mn>103</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>&#945;</mi><mo mathvariant="italic">,</mo><mtext mathvariant="italic">&#8201;</mtext><mi>&#946;</mi></mrow></mfenced><mo>=</mo><mfenced><mrow><mn>11</mn><mo>,</mo><mtext>&#8201;</mtext><mn>103</mn></mrow></mfenced></math>.</p>

</details>

---

### Q82. JEE Main 2020 (03 Sep Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

If the sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mo>+</mo><mn>19</mn><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>+</mo><mn>19</mn><mfrac><mn>1</mn><mn>5</mn></mfrac><mo>+</mo><mn>18</mn><mfrac><mn>4</mn><mn>5</mn></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mtext>th&#160;</mtext></msup></math> term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>488</mn><mo>&#160;</mo></math>and the <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mtext>th&#160;</mtext></msup></math> term is negative, then :

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mtext>th&#160;</mtext></msup></math> term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn><mfrac><mn>2</mn><mn>5</mn></mfrac></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>41</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mtext>th&#160;</mtext></msup></math> term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>60</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mi>n</mi><mtext>th&#160;</mtext></msup></math> term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>-</mo><mn>4</mn></math>**

**Detailed Solution:**

<p>The given series is an arithmetic progression whose first term is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> and common difference is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn><mfrac><mn>3</mn><mn>5</mn></mfrac><mo>-</mo><mn>20</mn><mo>=</mo><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></math>.</p><p>According to question,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>488</mn><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced open="[" close="]"><mrow><mn>2</mn><mfenced><mn>20</mn></mfenced><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>488</mn><mo>=</mo><mfrac><mi>n</mi><mn>2</mn></mfrac><mfenced><mrow><mn>40</mn><mo>-</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mn>5</mn></mfrac><mo>+</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced><mo>&#8658;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>101</mn><mi>n</mi><mo>+</mo><mn>2440</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>61</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>40</mn><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><msub><mi>T</mi><mn>40</mn></msub><mo>=</mo><mn>20</mn><mo>+</mo><mfenced><mrow><mn>40</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced><mo>=</mo><mfrac><mn>22</mn><mn>5</mn></mfrac><mo>&#62;</mo><mn>0</mn></math></p><p>For <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>61</mn><mo>&#8658;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><msub><mi>T</mi><mn>61</mn></msub><mo>=</mo><mn>20</mn><mo>+</mo><mfenced><mrow><mn>61</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mo>-</mo><mfrac><mn>2</mn><mn>5</mn></mfrac></mrow></mfenced><mo>=</mo><mo>-</mo><mn>4</mn><mo>&#60;</mo><mn>0</mn></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><msub><mi>T</mi><mn>61</mn></msub><mo>=</mo><mo>-</mo><mn>4</mn></math></p>

</details>

---

### Q83. JEE Main 2020 (08 Jan Shift 2)

*Type:* `numerical` | *Level:* `2`

The sum, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>4</mn></mfrac></math>, is equal to

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **504**

**Detailed Solution:**

<p>Given,</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>4</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>7</mn></munderover><mn>2</mn><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi></mrow></mfenced></math></p><p>Now using <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow/><mrow/></munderover><mfenced><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math>, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow/><mrow/></munderover><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup></mrow></mfenced><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow/><mrow/></munderover><mfenced><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>n</mi><mn>3</mn></msup></mrow></mfenced><mo>=</mo><msup><mfenced open="[" close="]"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></math>, we can write
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mn>2</mn><msup><mfenced separators="|"><mfrac><mrow><mn>7</mn><mo>&#183;</mo><mn>8</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><mfenced separators="|"><mfrac><mrow><mn>7</mn><mo>&#183;</mo><mn>8</mn><mo>&#183;</mo><mn>15</mn></mrow><mn>6</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>7</mn><mo>&#183;</mo><mn>8</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math>
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>&#215;</mo><mn>49</mn><mo>&#215;</mo><mn>16</mn><mo>+</mo><mn>28</mn><mo>&#215;</mo><mn>15</mn><mo>+</mo><mn>28</mn></mrow></mfenced></math>
<math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>1568</mn><mo>+</mo><mn>420</mn><mo>+</mo><mn>28</mn></mrow></mfenced><mo>=</mo><mo>=</mo><mn>504</mn></math>.</p>

</details>

---

### Q84. JEE Main 2020 (08 Jan Shift 1)

*Type:* `numerical` | *Level:* `2`

The sum <math><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>20</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>k</mi></mrow></mfenced></mrow></mrow></math> is ___________.

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Value:** **1540**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mn>20</mn></munderover><mfrac><mrow><mi>k</mi><mo>(</mo><mi>k</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>20</mn></mrow></munderover><mrow><mfenced separators="|"><mrow><msup><mrow><mi>k</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>k</mi></mrow></mfenced></mrow></mrow></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>20</mn><mfenced separators="|"><mrow><mn>21</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>41</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>20</mn><mfenced separators="|"><mrow><mn>21</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>420</mn><mo>&#215;</mo><mn>41</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>20</mn><mo>&#215;</mo><mn>21</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2870</mn><mo>+</mo><mn>210</mn></mrow></mfenced></math>
<math><mo>=</mo><mn>1540</mn></math>

</details>

---

### Q85. JEE Main 2020 (07 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first <math><mn>40</mn></math> terms of the series, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>13</mn><mo>+</mo><mn>14</mn><mo>+</mo><mn>18</mn><mo>+</mo><mn>19</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is <math><mfenced separators="|"><mrow><mn>102</mn></mrow></mfenced><mi mathvariant="normal">m</mi><mo>,</mo></math><span style="display: none;"> </span> then<span style="display: none;"> </span> <math><mi mathvariant="normal">m</mi></math> is equal to

**Options:**

- **(A)** <math><mn>20</mn></math>
- **(B)** <math><mn>25</mn></math>
- **(C)** <math><mn>5</mn></math>
- **(D)** <math><mn>10</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>20</mn></math>**

**Detailed Solution:**

<math><mi>S</mi><mo>=</mo><munder accentunder="false"><mrow><mn>3</mn><mo>+</mo><mn>4</mn></mrow><mo>⏟</mo></munder><mo>+</mo><munder accentunder="false"><mrow><mn>8</mn><mo>+</mo><mn>9</mn></mrow><mo>⏟</mo></munder><mo>+</mo><munder accentunder="false"><mrow><mn>13</mn><mo>+</mo><mn>14</mn></mrow><mo>⏟</mo></munder><mo>+</mo><munder accentunder="false"><mrow><mn>18</mn><mo>+</mo><mn>19</mn></mrow><mo>⏟</mo></munder><mo>…</mo><mn>40</mn></math> terms 
<math><mi>S</mi><mo>=</mo><mn>7</mn><mo>+</mo><mn>17</mn><mo>+</mo><mn>27</mn><mo>+</mo><mn>37</mn><mo>+</mo><mn>47</mn><mo>+</mo><mo>…</mo><mn>20</mn></math> terms 
<math><msub><mrow><mi>S</mi></mrow><mrow><mn>40</mn></mrow></msub><mo>=</mo><mfrac><mrow><mn>20</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>×</mo><mn>7</mn><mo>+</mo><mfenced separators="|"><mrow><mn>19</mn></mrow></mfenced><mn>10</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mfenced close="]" open="[" separators="|"><mrow><mn>14</mn><mo>+</mo><mn>190</mn></mrow></mfenced><mo>=</mo><mn>10</mn><mfenced close="]" open="[" separators="|"><mrow><mn>2040</mn></mrow></mfenced><mo>=</mo><mfenced separators="|"><mrow><mn>102</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>20</mn></mrow></mfenced></math>  
<math><mo>&#8658;</mo><mi>m</mi><mo>=</mo><mn>20</mn></math>

</details>

---

### Q86. JEE Main 2019 (10 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>15</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn></mrow></mfenced></math> is equal to

**Options:**

- **(A)** <math><mn>620</mn></math>
- **(B)** <math><mn>1240</mn></math>
- **(C)** <math><mn>1860</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>660</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>620</mn></math>**

**Detailed Solution:**

<p>Given series is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="[" close="]"><mrow><mn>1</mn><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>15</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn></mrow></mfrac></mrow></mfenced><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn></mrow></mfenced></math></p><p>First, we find the sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mn>15</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>15</mn></mrow></mfrac></math></p><p>General term for the series, is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>r</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>r</mi></mrow></mfrac></math></p><p>Using, the sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>n</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mfrac><msup><mfenced separators="|"><mstyle displaystyle="true"><mfrac><mrow><mi>r</mi><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle></mfenced><mn>2</mn></msup><mfenced separators="|"><mstyle displaystyle="true"><mfrac><mrow><mi>r</mi><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mstyle></mfenced></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mfrac><mrow><mi>r</mi><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math><mo>&#8658;</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>(</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mi>r</mi><mo>)</mo></math></p><p><math><mo>&#8658;</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi></mrow></msub></mrow></mrow><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mrow><mo>+</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><mi>r</mi></mrow></mrow></mrow></mfenced></math></p><p>Now, using <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn><mo>&#215;</mo><mn>31</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mn>680</mn></math></p><p>Now, we will find the sum <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mn>15</mn></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>=</mo><mn>60</mn></math></p><p>Hence, the required sum<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>680</mn><mo>-</mo><mn>60</mn><mo>=</mo><mn>620</mn><mo>.</mo></math></p>

</details>

---

### Q87. JEE Main 2019 (10 Apr Shift 1)

*Type:* `singleCorrect` | *Level:* `2`

The sum <math><mfrac><mrow><mn>3</mn><mo>&#215;</mo><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mo>&#215;</mo><mo>(</mo><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>)</mo></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><mo>&#215;</mo><mo>(</mo><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>)</mo></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> upto <math><msup><mrow><mn>10</mn></mrow><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is

**Options:**

- **(A)** <math><mn>660</mn></math>
- **(B)** <math><mn>600</mn></math>
- **(C)** <math><mn>620</mn></math>
- **(D)** <math><mn>680</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mn>660</mn></math>**

**Detailed Solution:**

<math><mi>S</mi><mo>=</mo><mi>&#160;</mi><mfrac><mrow><mn>3</mn><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>12</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>5</mn><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>7</mn><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mn>10</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">s</mi></math>
Here the general terms is
<math><msub><mrow><mi>T</mi></mrow><mrow><mi>r</mi></mrow></msub><mo>=</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfenced></mrow><mrow><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>+</mo><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mfrac><mo>+</mo><mfrac><mrow><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><msup><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>r</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></mrow><mrow><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mi>r</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></mfrac></mrow></mfenced></mrow></mfrac></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mi>r</mi><mo>(</mo><mi>r</mi><mo>+</mo><mn>1</mn><mo>)</mo></math>
<math><mo>&#8658;</mo><mi>S</mi><mo>=</mo><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>r</mi><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mrow><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><msup><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mrow><munderover><mo stretchy="true">&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>10</mn></mrow></munderover><mrow><mi mathvariant="normal">r</mi></mrow></mrow></mrow></mrow></mrow></mfenced></math>
<math><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mfrac><mrow><mn>10.11.21</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>10.11</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><mn>385</mn><mo>+</mo><mn>55</mn></mrow></mfenced><mo>=</mo><mn>660</mn></math>

</details>

---

### Q88. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

Some identical balls are arranged in rows to form an equilateral triangle. The first row consists of one ball, the second row consists of two balls and so on. If <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math> more identical balls are added to the total number of balls used in forming the equilateral triangle, then all these balls can be arranged in a square, whose each side contains exactly <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> balls less than the number of balls each side of the triangle contains. Then the number of balls used to form the equilateral triangle is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>262</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>190</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>157</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>190</mn></math>**

**Detailed Solution:**

<p>Let, the number of balls on one side of the equilateral triangle is <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>,</mo></math> then the number of balls on each side of the square will be <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>-</mo><mn>2</mn><mo>.</mo></math></p><p>Then, total balls used in the triangle are <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi></math></p><p>Now, the sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> natural numbers is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p>And, the total balls used in the square is <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mo>&#160;</mo><mi>t</mi><mi>i</mi><mi>m</mi><mi>e</mi><mi>s</mi><mo>=</mo><msup><mfenced><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced><mn>2</mn></msup></math></p><p>From the given condition we can write
<math><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac><mo>+</mo><mn>99</mn><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>2</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mn>198</mn><mo>=</mo><mn>2</mn><mfenced separators="|"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow></mfenced></math></p><p><math><mo>&#8658;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>9</mn><mi>n</mi><mo>-</mo><mn>190</mn><mo>=</mo><mn>0</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mi>n</mi><mo>-</mo><mn>19</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mn>0</mn></math></p><p><math><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>19</mn></math> or <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mo>-</mo><mn>10</mn><mo>,</mo></math> neglected as <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is the number of balls and hence, it can&#39;t be negative.</p><p>Hence, number of balls in equilateral triangle</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>=</mo><mfrac><mrow><mn>19</mn><mo>&#8901;</mo><mn>20</mn></mrow><mn>2</mn></mfrac><mo>=</mo><mn>190</mn><mo>.</mo></math></p>

</details>

---

### Q89. JEE Main 2019 (09 Apr Shift 2)

*Type:* `singleCorrect` | *Level:* `1`

The sum of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>7</mn><mo>+</mo><mo>&#8230;</mo></math> upto <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>11</mn><mrow><mi>t</mi><mi>h</mi></mrow></msup></math> term is:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>945</mn></math>
- **(B)** <math><mn>916</mn></math>
- **(C)** <math><mn>946</mn></math>
- **(D)** <math><mn>915</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>946</mn></math>**

**Detailed Solution:**

<p>Given series is <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>3</mn><mo>+</mo><mn>3</mn><mo>&#215;</mo><mn>5</mn><mo>+</mo><mn>4</mn><mo>&#215;</mo><mn>7</mn><mo>+</mo><mn>5</mn><mo>&#215;</mo><mn>9</mn><mo>+</mo><mo>&#8230;</mo></math></p><p>Thus, the general term is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>r</mi></msub><mo>=</mo><mi>r</mi><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p>Hence, the sum of <math><mn>11</mn></math> terms of the series is <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>11</mn></msub><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>11</mn></munderover><mi>r</mi><mfenced separators="|"><mrow><mn>2</mn><mi>r</mi><mo>-</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>11</mn></msub><mo>=</mo><mn>2</mn><mo>&#8721;</mo><msup><mi>r</mi><mn>2</mn></msup><mo>-</mo><mo>&#8721;</mo><mi>r</mi></math></p><p>Using the formulae for <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>&#8721;</mo><msup><mi>r</mi><mn>2</mn></msup></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mrow><mo>&#8721;</mo><mi>r</mi></mrow><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mo>=</mo><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>,</mo></math> we get</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>11</mn></msub><mo>=</mo><mn>2</mn><mo>&#8901;</mo><mfrac><mrow><mn>11</mn><mfenced separators="|"><mrow><mn>11</mn><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>22</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>-</mo><mfrac><mrow><mn>11</mn><mfenced separators="|"><mrow><mn>11</mn><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>11</mn></msub><mo>=</mo><mn>44</mn><mo>&#215;</mo><mn>23</mn><mo>-</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msub><mi>S</mi><mn>11</mn></msub><mo>=</mo><mn>1012</mn><mo>-</mo><mn>66</mn><mo>=</mo><mn>946</mn><mo>.</mo></math></p>

</details>

---

### Q90. JEE Main 2019 (12 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

If the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>1</mn><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mn>2</mn><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><msubsup><mfenced separators="|"><mrow><mn>3</mn><mfrac><mn>3</mn><mn>4</mn></mfrac></mrow></mfenced><mi>&#160;</mi><mn>3</mn></msubsup><mo>+</mo><mo>&#8230;</mo></math> is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn><mi mathvariant="normal">K</mi></math>, then <math><mi>K</mi></math> is equal to :

**Options:**

- **(A)** <math><mn>9</mn></math>
- **(B)** <math><mn>27</mn></math>
- **(C)** <math><mn>54</mn></math>
- **(D)** <math><mn>108</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math><mn>27</mn></math>**

**Detailed Solution:**

<p>Given series, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mfenced separators="|"><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>6</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>9</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>12</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><msup><mfenced separators="|"><mfrac><mn>15</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mn>15</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><msup><mfenced><mfrac><mn>3</mn><mn>4</mn></mfrac></mfenced><mn>3</mn></msup><mfenced separators="|"><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mn>15</mn><mn>3</mn></msup></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>27</mn><mn>64</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mfenced open="[" close="]"><mrow><mo>&#8757;</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>=</mo><mi>n</mi></mrow></munderover><msup><mi>n</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced open="[" close="]"><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mrow></mfenced></math> </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>27</mn><mn>64</mn></mfrac><mo>&#215;</mo><mfrac><mrow><mn>225</mn><mo>&#215;</mo><mn>64</mn></mrow><mn>1</mn></mfrac><mo>=</mo><mn>27</mn><mo>&#215;</mo><mn>225</mn></math> </p><p>Since, given <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>225</mn><mi mathvariant="normal">K</mi><mo>=</mo><mn>27</mn><mo>&#215;</mo><mn>225</mn></math> </p><p><math><mo>&#8658;</mo><mi>K</mi><mo>=</mo><mn>27</mn></math></p>

</details>

---

### Q91. JEE Main 2019 (11 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `3`

Let $S_{n}=1+q+q^{2}+\ldots .+q^{n}$ and

$\mathrm{T}_{\mathrm{n}}=1+\left(\frac{\mathrm{q}+1}{2}\right)+\left(\frac{\mathrm{q}+1}{2}\right)^{2}+\ldots+\left(\frac{\mathrm{q}+1}{2}\right)^{\mathrm{n}}$

where $q$ is a real number and $q \neq 1$. If ${ }^{101} \mathrm{C}_{1}+{ }^{101} \mathrm{C}_{2} \cdot \mathrm{S}_{1}+\ldots .+{ }^{101} \mathrm{C}_{101} \cdot \mathrm{S}_{100}=\alpha \mathrm{T}_{100},$ then $\alpha$ is

equal to :

**Options:**

- **(A)** $2^{99}$
- **(B)** 202
- **(C)** 200
- **(D)** $2^{100}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $2^{100}$**

**Detailed Solution:**

$S_{n}=\left(\frac{1-q^{n+1}}{1-q}\right), T_{n}=\frac{1-\left(\frac{q+1}{2}\right)^{n+1}}{1-\left(\frac{q+1}{2}\right)}$

$\Rightarrow T_{100}=\frac{1-\left(\frac{q+1}{2}\right)^{101}}{1-\left(\frac{q+1}{2}\right)}$

$S n=\frac{1}{1-q}-\frac{q^{n+1}}{1-q}, T_{100}=\frac{2^{101}-(\mathrm{q}+1)^{101}}{2^{100}(1-\mathrm{q})}$

Now, ${ }^{101} C_{1}+{ }^{101} C_{2} S_{1}+{ }^{101} C_{3} S_{2}+\ldots+{ }^{101} C_{101} S_{100}$

$=\left(\frac{1}{1-q}\right)\left({ }^{101} C_{2}+\ldots+{ }^{101} C_{101}\right)$

$$

\begin{aligned}

& \quad-\frac{1}{1-q}\left({ }^{101} C_{2} q^{2}+{ }^{101} C_{3} q^{3}+\ldots+{ }^{101} C_{101} q^{101}\right)+101 \\

=& \frac{1}{1-q}\left(2^{101}-1-101\right)-\left(\frac{1}{1-q}\right)\left((1+q)^{101}-1\right.\\

\left.-{ }^{101} C_{1} q\right)+101 \\

=& \frac{1}{1-q}\left[2^{101}-102-(1+q)^{101}+1+101 q\right]+101 \\

=& \frac{1}{1-q}\left[2^{101}-101+101 q-(1+q)^{101}\right]+101 \\

=&\left(\frac{1}{1-q}\right)\left[2^{101}-(1+q)^{101}\right]=2^{100} T_{100}

\end{aligned}

$$

Hence, by comparison $\alpha=2^{100}$

</details>

---

### Q92. JEE Main 2019 (09 Jan Shift 2)

*Type:* `singleCorrect` | *Level:* `2`

The sum of the following series <math><mn>1</mn><mo>+</mo><mn>6</mn><mo>+</mo><mfrac><mrow><mn>9</mn><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>7</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>12</mn><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>9</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>15</mn><mo>(</mo><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mn>5</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>)</mo></mrow><mrow><mn>11</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> up to <math><mn>15</mn></math> terms, is:

**Options:**

- **(A)** <math><mn>7520</mn></math>
- **(B)** <math><mn>7510</mn></math>
- **(C)** <math><mn>7830</mn></math>
- **(D)** <math><mn>7820</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math><mn>7820</mn></math>**

**Detailed Solution:**

<p><math><msub><mrow><mi>t</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>3</mn><mi>n</mi><mfenced separators="|"><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mfrac><mrow><mn>3</mn><mi>n</mi><mo>&#215;</mo><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></math>

<math><mo>&#8756;</mo><msub><mrow><mi>S</mi></mrow><mrow><mn>15</mn></mrow></msub><mo>=</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><msub><mrow><mi>t</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mn>15</mn></mrow></munderover><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced separators="|"><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></mfenced></mrow></mrow></mrow></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mfenced close="]" open="["><mrow><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>n</mi><mn>3</mn></msup><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><msup><mi>n</mi><mn>2</mn></msup></mrow></mfenced></math></p><p>
<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac><mo>&#215;</mo><mfenced close="]" open="[" separators="|"><mrow><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn></mrow><mrow><mn>2</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mfrac><mrow><mn>15</mn><mo>&#215;</mo><mn>16</mn><mo>&#215;</mo><mn>31</mn></mrow><mrow><mn>6</mn></mrow></mfrac><mi>&#160;</mi></mrow></mfenced></math>   <math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced open="{" close="}"><mrow><mo>&#8721;</mo><msup><mi>n</mi><mn>3</mn></msup><mo>=</mo><msup><mfenced><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup><mo>,</mo><mo>&#160;</mo><mo>&#8721;</mo><msup><mi>n</mi><mn>2</mn></msup><mo>=</mo><mfenced><mfrac><mrow><mi>n</mi><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced></mrow><mn>6</mn></mfrac></mfenced></mrow></mfenced></math>

<math><mo>=</mo><mn>7200</mn><mo>+</mo><mn>620</mn></math>

<math><mo>=</mo><mn>7820</mn></math></p>

</details>

---

### Q93. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>31</mn><mn>16</mn></mfrac><mo>+</mo><mo>&#8230;</mo></math> is

**Options:**

- **(A)** <math><mn>39</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>19</mn></mrow></msup></mrow></mfrac></math>
- **(B)** <math><mn>38</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>
- **(C)** <math><mn>38</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>19</mn></mrow></msup></mrow></mfrac></math>
- **(D)** <math><mn>39</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>20</mn></mrow></msup></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mn>38</mn><mo>+</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>2</mn></mrow><mrow><mn>19</mn></mrow></msup></mrow></mfrac></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>+</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>7</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>15</mn><mn>8</mn></mfrac><mo>+</mo><mfrac><mn>31</mn><mn>16</mn></mfrac><mo>+</mo><mo>&#8230;</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mn>1</mn></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>8</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><mn>2</mn><mo>-</mo><mfrac><mn>1</mn><mn>16</mn></mfrac></mrow></mfenced><mo>+</mo><mo>&#8230;</mo><mi mathvariant="normal">u</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">&#160;</mi><mn>20</mn><mi mathvariant="normal">&#160;</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">s</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>40</mn><mo>-</mo><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mfrac><mn>1</mn><mn>8</mn></mfrac><mo>+</mo><mo>&#8230;</mo><mi mathvariant="normal">u</mi><mi mathvariant="normal">p</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">o</mi><mi>&#160;</mi><mn>20</mn><mi>&#160;</mi><mi mathvariant="normal">t</mi><mi mathvariant="normal">e</mi><mi mathvariant="normal">r</mi><mi mathvariant="normal">m</mi><mi mathvariant="normal">s</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>40</mn><mo>-</mo><mfenced separators="|"><mfrac><mrow><mn>1</mn><mo>-</mo><msup><mfenced separators="|"><mfrac><mn>1</mn><mn>2</mn></mfrac></mfenced><mn>20</mn></msup></mrow><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfrac></mfenced><mo>=</mo><mn>40</mn><mo>-</mo><mn>2</mn><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>19</mn></msup></mfrac><mo>=</mo><mn>38</mn><mo>+</mo><mfrac><mn>1</mn><msup><mn>2</mn><mn>19</mn></msup></mfrac></math>

</details>

---

### Q94. JEE Main 2018 (16 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>x</mi><mn>1</mn></msub></mfrac><mo>,</mo><mo>&#160;</mo><mfrac><mn>1</mn><msub><mi>x</mi><mn>2</mn></msub></mfrac><mo>,</mo><mo>&#8230;</mo><mo>,</mo><mfrac><mn>1</mn><msub><mi>x</mi><mi>n</mi></msub></mfrac><mo>(</mo><msub><mi>x</mi><mi>i</mi></msub><mo>&#8800;</mo><mn>0</mn></math> for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>2</mn><mo>,</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo><mo>&#160;</mo><mi>n</mi><mo>)</mo></math> be in A.P. such that <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>21</mn></msub><mo>=</mo><mn>20</mn></math><math> <mo>.</mo> </math> If <math> <mi>n</mi> </math> is the least positive integer for which <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mi>n</mi></msub><mo>&#62;</mo><mn>50</mn></math>, then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><mfenced separators="|"><mfrac><mn>1</mn><msub><mi>x</mi><mi>i</mi></msub></mfrac></mfenced></math> is equal to

**Options:**

- **(A)** <math><mrow><mn>3</mn></mrow></math>
- **(B)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>
- **(D)** <math><mi> </mi><mfrac><mrow><mn>13</mn></mrow><mrow><mn>8</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math><mfrac><mrow><mn>13</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><msub><mi>x</mi><mn>1</mn></msub></mfrac><mo>,</mo><mfrac><mn>1</mn><msub><mi>x</mi><mn>2</mn></msub></mfrac><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><mfrac><mn>1</mn><msub><mi>x</mi><mi>n</mi></msub></mfrac></math> are in A.P. and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>1</mn></msub><mo>=</mo><mn>4</mn></math> and <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>21</mn></msub><mo>=</mo><mn>20</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>a</mi><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></math></p><p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>21</mn></msub><mo>=</mo><mn>20</mn></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>+</mo><mn>20</mn><mo>&#183;</mo><mi>d</mi><mo>=</mo><mfrac><mn>1</mn><mn>20</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>d</mi><mo>=</mo><mo>&#8722;</mo><mfrac><mn>1</mn><mn>100</mn></mfrac></math>

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>x</mi><mn>n</mn></msub><mo>&#62;</mo><mi>50</mi></math>.</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><msub><mi>x</mi><mi>n</mi></msub></mfrac><mo>&#60;</mo><mfrac><mn>1</mn><mn>50</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mi>&#160;</mi><mfrac><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow><mn>100</mn></mfrac><mo>&#60;</mo><mi>&#160;</mi><mfrac><mn>1</mn><mn>50</mn></mfrac><mo>&#8658;</mo><mi>n</mi><mo>&#62;</mo><mn>24</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8757;</mo><mo>&#160;</mo><mi>n</mi><mo>=</mo><mn>25</mn></math></p><p>Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mn>25</mn></munderover><mfenced separators="|"><mfrac><mn>1</mn><msub><mi>x</mi><mi>i</mi></msub></mfrac></mfenced><mo>=</mo><mfrac><mn>25</mn><mn>2</mn></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>&#215;</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>100</mn></mfrac><mo>&#215;</mo><mn>24</mn></mrow></mfenced><mo>=</mo><mfrac><mn>13</mn><mn>4</mn></mfrac></math></p>

</details>

---

### Q95. JEE Main 2018 (15 Apr Shift 2 Online)

*Type:* `singleCorrect` | *Level:* `3`

Let $A_n=\left(\frac{3}{4}\right)-\left(\frac{3}{4}\right)^2+\left(\frac{3}{4}\right)^3-\ldots+(-1)^{n-1}\left(\frac{3}{4}\right)^n$ and $B_n=1-A_n$. Then, the least odd natural number $p$, so that $B_n>A_n$, for all $n \geq p$ is

**Options:**

- **(A)** 5
- **(B)** 7
- **(C)** 11
- **(D)** 9

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 7**

**Detailed Solution:**

$$
A_n=\left(\frac{3}{4}\right)-\left(\frac{3}{4}\right)^2+\left(\frac{3}{4}\right)^3-\ldots+(-1)^{n-1}\left(\frac{3}{4}\right)^n
$$
Which is a G.P. with $a=\frac{3}{4}, r=\frac{-3}{4}$ and number of terms $=n$
$$
\begin{aligned}
\therefore A_n &=\frac{\frac{3}{4} \times\left(1-\left(\frac{-3}{4}\right)^n\right)}{1-\left(\frac{-3}{4}\right)}=\frac{\frac{3}{4} \times\left(1-\left(\frac{-3}{4}\right)^n\right)}{\frac{7}{4}} \\
\Rightarrow A_n=\frac{3}{7}\left[1-\left(\frac{-3}{4}\right)^n\right] \\
\text { As, } B_n=1-A_n
\end{aligned}
$$
For least odd natural number $\mathrm{p}$, such that $B_n>A_n$
$$
\Rightarrow 1-A_n>A_n \Rightarrow 1>2 \times A_n \Rightarrow A_n < \frac{1}{2}
$$
From eqn. (1), we get
$$
\begin{aligned}
&\frac{3}{7} \times\left[1-\left(\frac{-3}{4}\right)^n\right] < \frac{1}{2} \Rightarrow 1-\left(\frac{-3}{4}\right)^n < \frac{7}{6} \\
&\Rightarrow 1-\frac{7}{6} < \left(\frac{-3}{4}\right)^n \Rightarrow \frac{-1}{6} < \left(\frac{-3}{4}\right)^n
\end{aligned}
$$
As $n$ is odd, then $\left(\frac{-3}{4}\right)^n=-\frac{3^n}{4}$
So $\frac{-1}{6} < -\left(\frac{3}{4}\right)^n \Rightarrow \frac{1}{6}>\left(\frac{3}{4}\right)^n$
$$
\log \left(\frac{1}{6}\right)=n \log \left(\frac{3}{4}\right) \Rightarrow 6.228 < n
$$
Hence, $n$ should be 7 .

</details>

---

### Q96. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

Let <math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mi>&#160;</mi><msub><mrow><mi>a</mi></mrow><mrow><mn>3</mn></mrow></msub><mo>,</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>49</mn></mrow></msub></math> be in <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>.</mo><mi>P</mi><mo>.</mo></math> such that <math><mrow> <munderover> <mi>&#931;</mi> <mrow> <mi>k</mi><mo>&#8289;</mo> <mo>=</mo> <mn>0</mn> </mrow> <mrow> <mn>1</mn> <mn>2</mn> </mrow> </munderover> </mrow><mrow><msub><mrow><mi>a</mi></mrow><mrow><mn>4</mn><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mn>416</mn></mrow></math> and <math><msub><mrow><mi>a</mi></mrow><mrow><mn>9</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>43</mn></mrow></msub><mo>=</mo><mn>66</mn><mo>.</mo></math> If <math><msubsup><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msubsup><mrow><mi>a</mi></mrow><mrow><mn>17</mn></mrow><mrow><mn>2</mn></mrow></msubsup><mo>=</mo><mn>140</mn><mi>m</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>33</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>66</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>68</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>34</mn></math>**

**Detailed Solution:**

<p><math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>5</mn></mrow></msub><mo>+</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>+</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>49</mn></mrow></msub><mo>=</mo><mn>416</mn></math>
Let common difference <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mo>&#160;</mo><mi>d</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><msub><mi>a</mi><mn>1</mn></msub><mi>&#160;</mi><mo>+</mo><mn>4</mn><mi>d</mi><mfenced close="}" open="{" separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>+</mo><mn>12</mn></mrow></mfenced><mo>=</mo><mn>416</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><msub><mi>a</mi><mn>1</mn></msub><mi>&#160;</mi><mo>+</mo><mn>4</mn><mi>d</mi><mfenced><mfrac><mrow><mn>12</mn><mfenced><mn>13</mn></mfenced></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>416</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn><msub><mi>a</mi><mn>1</mn></msub><mi>&#160;</mi><mo>+</mo><mn>24</mn><mi>d</mi><mfenced><mn>13</mn></mfenced><mo>=</mo><mn>416</mn></math>
<math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>24</mn><mi>d</mi><mo>=</mo><mn>32</mn></math>      <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>9</mn></msub><mo>+</mo><msub><mi>a</mi><mn>43</mn></msub><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>8</mn><mi>d</mi><mo>+</mo><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>42</mn><mi>d</mi><mo>=</mo><mn>66</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><msub><mi>a</mi><mn>1</mn></msub><mo>+</mo><mn>50</mn><mi>d</mi><mo>=</mo><mn>66</mn></math>
<math><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>+</mo><mn>25</mn><mi>d</mi><mo>=</mo><mn>33</mn></math>      <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mo>.</mo><mo>&#160;</mo><mo>(</mo><mi>i</mi><mi>i</mi><mo>)</mo></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mn>1</mn></msub><mo>=</mo><mn>8</mn><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mo>;</mo><mo>&#160;</mo><mi>&#160;</mi><mi>d</mi><mo>=</mo><mn>1</mn></math>
<math> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>i</mi><mo>=</mo><mn>1</mn> </mrow> <mrow> <mn>17</mn> </mrow> </munderover> <mrow> <msub> <mi>a</mi> <mi>i</mi> </msub> <msup> <mrow></mrow> <mn>2</mn> </msup> </mrow> </mstyle><mo>=</mo><mn>140</mn><mi>m</mi> </mrow> </math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mi>&#160;</mi><mo>.</mo><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>+</mo><msup><mfenced separators="|"><mrow><mi>a</mi><mo>+</mo><mn>16</mn><mi>d</mi></mrow></mfenced><mn>2</mn></msup><mo>=</mo><mn>140</mn><mi>m</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>17</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mfenced separators="|"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>+</mo><msup><mn>16</mn><mn>2</mn></msup></mrow></mfenced><mo>+</mo><mn>2</mn><mi>a</mi><mi>d</mi><mfenced separators="|"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>.</mo><mi>&#160;</mi><mo>+</mo><mi>&#160;</mi><mn>16</mn></mrow></mfenced><mo>=</mo><mn>140</mn><mi>m</mi></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>17</mn><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>d</mi><mn>2</mn></msup><mfenced separators="|"><mfrac><mrow><mn>16</mn><mo>&#215;</mo><mn>17</mn><mo>&#215;</mo><mn>33</mn></mrow><mn>6</mn></mfrac></mfenced><mo>+</mo><mn>2</mn><mi>a</mi><mi>d</mi><mfenced separators="|"><mfrac><mrow><mn>16</mn><mo>&#215;</mo><mn>17</mn></mrow><mn>2</mn></mfrac></mfenced><mo>=</mo><mn>140</mn><mi>m</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mfenced><mrow><mn>17</mn><mo>&#215;</mo><mn>64</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>8</mn><mo>&#215;</mo><mn>11</mn><mo>&#215;</mo><mn>17</mn></mrow></mfenced><mo>+</mo><mfenced><mrow><mn>8</mn><mo>&#215;</mo><mn>16</mn><mo>&#215;</mo><mn>17</mn></mrow></mfenced><mo>=</mo><mn>140</mn><mi>m</mi></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo></math> <math><mi>m</mi><mo>=</mo><mn>34</mn></math></p>

</details>

---

### Q97. JEE Main 2018 (08 Apr)

*Type:* `singleCorrect` | *Level:* `2`

<p>Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> be the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms and <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> be the sum of the first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>40</mn></math> terms of the series </p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>2</mn></mrow><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>4</mn></mrow><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>6</mn></mrow><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>-</mo><mn>2</mn><mi>A</mi><mo>=</mo><mn>100</mn><mi>&#955;</mi><mo>,</mo></math> then <math><mi>&#955;</mi></math> is equal to :</p>

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>496</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>232</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>248</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>464</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>248</mn></math>**

**Detailed Solution:**

<p>Given series, <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>2</mn></mrow><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>4</mn></mrow><mn>2</mn></msup><mo>+</mo><msup><mn>5</mn><mn>2</mn></msup><mo>+</mo><msup><mrow><mn>2</mn><mo>&#183;</mo><mn>6</mn></mrow><mn>2</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>&#160;</mo></math></p><p>Here, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mn>2</mn><mo>&#183;</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>20</mn></math> terms

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfenced separators="|"><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><mi>&#160;</mi><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>20</mn><mi>&#160;</mi><mi>terms</mi></mrow></mfenced><mo>+</mo><mfenced separators="|"><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><mi>&#160;</mi><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>10</mn><mi>&#160;</mi><mi>terms</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>20</mn><mo>&#183;</mo><mn>21</mn><mo>&#183;</mo><mn>41</mn></mrow><mn>6</mn></mfrac><mi>&#160;</mi><mo>+</mo><mn>4</mn><mfenced separators="|"><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced></math> 

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>A</mi><mo>=</mo><mn>4410</mn></math>

Similarly for <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>=</mo><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>40</mn><mo>&#160;</mo><mi>terms</mi></mrow></mfenced><mo>+</mo><mfenced><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>4</mn><mn>2</mn></msup><mo>+</mo><msup><mn>6</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mn>20</mn><mo>&#160;</mo><mi>terms</mi></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mfrac><mrow><mn>40</mn><mo>&#215;</mo><mn>41</mn><mo>&#215;</mo><mn>81</mn></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>4</mn><mo>&#215;</mo><mn>20</mn><mo>&#215;</mo><mn>21</mn><mo>&#215;</mo><mn>41</mn></mrow><mn>6</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>B</mi><mo>=</mo><mn>33620</mn></math>

Now, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi><mo>-</mo><mn>2</mn><mi>A</mi><mo>=</mo><mn>24800</mn></math><math><mo>=</mo><mn>100</mn><mi>&#955;</mi></math> (Given)

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>&#955;</mi><mo>=</mo><mn>248</mn></math></p>

</details>

---

### Q98. JEE Main 2017 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math><msub><mrow><mi>S</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>3</mn></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>,</mo><mo>+</mo><mi>n</mi></mrow><mrow><msup><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><msup><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><msup><mrow><mi>n</mi></mrow><mrow><mn>3</mn></mrow></msup></mrow></mfrac></math> . If <math><mn>100</mn><mi>&#160;</mi><msub><mrow><mi>S</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mi>n</mi><mo>,</mo></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>199</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>19</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>199</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>1</mn><msup><mn>1</mn><mn>3</mn></msup></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn></mrow><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></mrow><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow></mfrac><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mo>&#8230;</mo><mo>+</mo><mi>n</mi></mrow><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><mo>&#8230;</mo><mo>+</mo><msup><mi>n</mi><mn>3</mn></msup></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><msup><mfenced separators="|"><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac></mfenced><mn>2</mn></msup></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>2</mn><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mn>2</mn><mfenced><mrow><mfrac><mn>1</mn><mi>n</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math>

<math><msub><mrow><mi>S</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mn>2</mn><mrow><munderover><mo stretchy="false">&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mrow><mi>n</mi></mrow></munderover><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></mrow></mrow></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mn>2</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced><mo>=</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac></math>

Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mi>n</mi><mo>&#8658;</mo><mn>100</mn><mo>&#215;</mo><mfrac><mrow><mn>2</mn><mi>n</mi></mrow><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfrac><mo>=</mo><mi>n</mi></math>

<math><mi>n</mi><mo>+</mo><mn>1</mn><mo>=</mo><mn>200</mn></math>

<math><mi>n</mi><mo>=</mo><mn>199</mn></math></p>

</details>

---

### Q99. JEE Main 2017 (08 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the sum of the first <math> <mi>n</mi> </math> terms of the series <math><msqrt><mn>3</mn></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>75</mn></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>243</mn></msqrt><mo>+</mo><mi>&#160;</mi><msqrt><mn>507</mn></msqrt><mo>+</mo><mo>&#8230;</mo></math> is <math><mn>435</mn><msqrt><mn>3</mn></msqrt><mo>,</mo></math> then <math> <mi>n</mi> </math> equals:

**Options:**

- **(A)** <math> <mrow> <mn>13</mn> </mrow> </math>
- **(B)** <math> <mrow> <mn>15</mn> </mrow> </math>
- **(C)** <math> <mrow> <mn>29</mn> </mrow> </math>
- **(D)** <math> <mrow> <mn>18</mn> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math> <mrow> <mn>15</mn> </mrow> </math>**

**Detailed Solution:**

<math><msqrt><mn>3</mn></msqrt><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><msqrt><mn>25</mn></msqrt><mo>+</mo><mi> </mi><msqrt><mn>81</mn></msqrt><mo>+</mo><mi> </mi><msqrt><mn>169</mn></msqrt><mo>+</mo><mo>…</mo></mrow></mfenced><mo>=</mo><mn>435</mn><msqrt><mn>3</mn></msqrt></math>

<math><msqrt><mn>3</mn></msqrt><mi> </mi><mfenced close="]" open="[" separators="|"><mrow><mn>1</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>13</mn><mo>+</mo><mo>…</mo><msub><mrow><mi>T</mi></mrow><mrow><mi>n</mi></mrow></msub></mrow></mfenced><mo>=</mo><mn>435</mn><msqrt><mn>3</mn></msqrt></math>

<math><mo>=</mo><mi> </mi><msqrt><mn>3</mn></msqrt><mo>×</mo><mfrac><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mn>2</mn><mo>+</mo><mfenced separators="|"><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced><mn>4</mn></mrow></mfenced><mo>=</mo><mn>435</mn><msqrt><mn>3</mn></msqrt></math>

<math><mo>=</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>4</mn><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>4</mn><mi>n</mi><mo>=</mo><mn>870</mn></math>

<math><mo>=</mo><mn>4</mn><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mn>2</mn><mi>n</mi><mo>-</mo><mn>870</mn><mo>=</mo><mn>0</mn></math>

<math><mo>=</mo><mn>2</mn><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>-</mo><mi>n</mi><mo>-</mo><mn>435</mn><mo>=</mo><mn>0</mn></math>

<math><mi>n</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>±</mo><mi> </mi><msqrt><mn>1</mn><mo>+</mo><mn>4</mn><mo>×</mo><mn>2</mn><mo>×</mo><mn>435</mn></msqrt></mrow><mrow><mn>4</mn></mrow></mfrac></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn><mo>±</mo><mn>59</mn></mrow><mrow><mn>4</mn></mrow></mfrac></math>     <math> <mrow><mo>∵</mo><mi>n</mi> </mrow> </math> is <math> <mrow> <mo>+</mo><mi>v</mi><mi>e</mi> </mrow> </math>

<math><mo>∴</mo><mi>n</mi><mo>=</mo><mfrac><mrow><mn>1</mn><mo>+</mo><mn>59</mn></mrow><mrow><mn>4</mn></mrow></mfrac><mo>=15</mo><mi> </mi></math>

</details>

---

### Q100. JEE Main 2016 (03 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If the sum of the first ten terms of the series <math><msup><mrow><mfenced separators="|"><mrow><mn>1</mn><mfrac><mrow><mn>3</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>2</mn><mfrac><mrow><mn>2</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>3</mn><mfrac><mrow><mn>1</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mn>4</mn></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mn>4</mn><mfrac><mrow><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mo>&#8230;</mo><mo>.</mo><mo>,</mo></math> is <math><mfrac><mrow><mn>16</mn></mrow><mrow><mn>5</mn></mrow></mfrac><mi>m</mi></math> , then <math><mi>m</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>99</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>102</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math>**

**Detailed Solution:**

<p><math><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>8</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>12</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>16</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math> ........ upto ten terms

<math><msub><mrow><mi>T</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><msup><mrow><mfenced separators="|"><mrow><mfrac><mrow><mn>4</mn><mi>n</mi><mo>+</mo><mn>4</mn></mrow><mrow><mn>5</mn></mrow></mfrac></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></msup></math>

<math><msub><mrow><mi>T</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mn>16</mn><mfenced separators="|"><mrow><mfrac><mrow><msup><mrow><mi>n</mi></mrow><mrow><mn>2</mn></mrow></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mn>25</mn></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>16</mn><mn>25</mn></mfrac><mfenced separators="|"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfrac><mn>16</mn><mn>25</mn></mfrac><mstyle displaystyle="false"><munder><mo>&#8721;</mo><mrow></mrow></munder></mstyle><mfenced separators="|"><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>n</mi></msub><mo>=</mo><mfenced separators="|"><mfrac><mn>16</mn><mn>25</mn></mfrac></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mi>&#160;</mi><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>6</mn></mfrac><mo>+</mo><mfrac><mrow><mn>2</mn><mfenced separators="|"><mi>n</mi></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mn>2</mn></mfrac><mo>+</mo><mi>n</mi></mrow></mfenced></math>

Put <math><mi>n</mi><mo>=</mo><mn>10</mn><mi>&#160;</mi></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>16</mn><mn>25</mn></mfrac><mfenced separators="|"><mrow><mfenced separators="|"><mfrac><mrow><mn>10</mn><mo>&#183;</mo><mn>11</mn><mo>&#183;</mo><mn>21</mn></mrow><mn>6</mn></mfrac></mfenced><mo>+</mo><mfrac><mrow><mn>2</mn><mo>&#183;</mo><mn>10</mn><mo>&#183;</mo><mn>11</mn></mrow><mn>2</mn></mfrac><mo>+</mo><mn>10</mn></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>25</mn></mfrac><mi>&#160;</mi><mfenced separators="|"><mrow><mn>385</mn><mo>+</mo><mn>110</mn><mo>+</mo><mn>10</mn></mrow></mfenced><mo>=</mo><mfrac><mn>16</mn><mn>25</mn></mfrac><mo>&#183;</mo><mi>&#160;</mi><mn>505</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>16</mn><mn>5</mn></mfrac><mo>&#183;</mo><mn>101</mn></math>

Hence <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi><mo>=</mo><mn>101</mn></math></p>

</details>

---

### Q101. JEE Main 2015 (11 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If <math><mrow> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>n</mi><mo>=</mo><mn>1</mn> </mrow> <mn>5</mn> </munderover> <mrow></mrow> </mstyle> </mrow><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><mn>3</mn></mrow></mfrac><mo>,</mo></mrow></mrow><mi>&#160;</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to:

**Options:**

- **(A)** <math><mfrac><mrow><mn>55</mn></mrow><mrow><mn>336</mn></mrow></mfrac></math>
- **(B)** <math><mfrac><mrow><mn>17</mn></mrow><mrow><mn>105</mn></mrow></mfrac></math>
- **(C)** <math><mfrac><mrow><mn>19</mn></mrow><mrow><mn>112</mn></mrow></mfrac></math>
- **(D)** <math><mfrac><mrow><mn>1</mn></mrow><mrow><mn>6</mn></mrow></mfrac></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math><mfrac><mrow><mn>55</mn></mrow><mrow><mn>336</mn></mrow></mfrac></math>**

**Detailed Solution:**

<math><msub><mrow><mi>T</mi></mrow><mrow><mi>n</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced><mo>-</mo><mi>n</mi></mrow><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>3</mn><mo>)</mo></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>)</mo></mrow></mfrac><mo>-</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>3</mn></mrow></mfenced></mrow></mfrac></mrow></mfenced></math>

<math> <mrow> <mstyle displaystyle="true"> <munderover> <mo>&#8721;</mo> <mrow> <mi>n</mi><mo>=</mo><mn>1</mn> </mrow> <mn>5</mn> </munderover> <mrow> <msub> <mi>T</mi> <mi>n</mi> </msub> </mrow> </mstyle><mo>=</mo> </mrow> </math><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mfrac><mn>1</mn><mrow><mn>1</mn><mo>&#183;</mo><mn>2</mn><mo>&#183;</mo><mn>3</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn></mrow></mfrac><mo>+</mo><mfrac><mn>1</mn><mrow><mn>2</mn><mo>&#183;</mo><mn>3</mn><mo>&#183;</mo><mn>4</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>3</mn><mo>&#183;</mo><mn>4</mn><mo>&#183;</mo><mn>5</mn></mrow></mfrac><mo>&#8230;</mo><mo>+</mo><mfrac><mn>1</mn><mrow><mn>5</mn><mo>&#183;</mo><mn>6</mn><mo>&#183;</mo><mn>7</mn></mrow></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>&#183;</mo><mn>7</mn><mo>&#183;</mo><mn>8</mn></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>3</mn></mfrac><mfenced open="[" close="]" separators="|"><mrow><mfrac><mn>1</mn><mn>6</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mn>6</mn><mo>&#183;</mo><mn>56</mn></mrow></mfrac></mrow></mfenced><mi>&#160;</mi></math>

<math><mo>=</mo><mfrac><mrow><mn>1</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mfenced close="]" open="[" separators="|"><mrow><mfrac><mrow><mn>56</mn><mo>-</mo><mn>1</mn></mrow><mrow><mn>336</mn></mrow></mfrac></mrow></mfenced></math>

<math><mo>=</mo><mfrac><mrow><mn>55</mn></mrow><mrow><mn>3</mn><mfenced separators="|"><mrow><mn>336</mn></mrow></mfenced></mrow></mfrac><mo>=</mo><mfrac><mrow><mi>k</mi></mrow><mrow><mn>3</mn></mrow></mfrac></math>

<math><mo>&#8658;</mo><mi>k</mi><mo>=</mo><mfrac><mrow><mn>55</mn></mrow><mrow><mn>336</mn></mrow></mfrac></math>

</details>

---

### Q102. JEE Main 2015 (10 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The value of <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>16</mn></mrow><mn>30</mn></munderover><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><mi>r</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow></math> is equal to:

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7775</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7785</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7780</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7770</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7780</mn></math>**

**Detailed Solution:**

<p>Given value <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>16</mn></mrow><mn>30</mn></munderover><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><mi>r</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>30</mn></munderover><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><mi>r</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow><mo>-</mo><munderover><mo>&#8721;</mo><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mn>15</mn></munderover><mrow><mfenced separators="|"><mrow><mi>r</mi><mo>+</mo><mn>2</mn></mrow></mfenced><mo>(</mo><mi>r</mi><mo>-</mo><mn>3</mn><mo>)</mo></mrow></math>
<math><mo>=</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>n</mi><mfenced separators="|"><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>6</mn><mi>n</mi></mrow></mfenced><mo>-</mo><mfenced separators="|"><mrow><mfrac><mrow><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced separators="|"><mrow><mn>2</mn><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>6</mn></mrow></mfrac><mo>-</mo><mfrac><mrow><mi>m</mi><mfenced separators="|"><mrow><mi>m</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow><mrow><mn>2</mn></mrow></mfrac><mo>-</mo><mn>6</mn><mi>m</mi></mrow></mfenced></math>
where <math><mi>n</mi><mo>=</mo><mn>30</mn><mo>,</mo><mi>&#160;</mi><mi>m</mi><mo>=</mo><mn>15</mn></math>
<math><mo>=</mo><mn>8810</mn><mo>-</mo><mn>1030</mn></math>
<math><mo>=</mo><mn>7780</mn></math></p>

</details>

---

### Q103. JEE Main 2015 (04 Apr)

*Type:* `singleCorrect` | *Level:* `3`

The sum of first <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> terms of the series <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>1</mn><mn>3</mn></msup><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math> is

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>192</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>71</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>142</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>96</mn></math>**

**Detailed Solution:**

<p>Given, <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><msup><mn>1</mn><mn>3</mn></msup><mn>1</mn></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn></mrow></mfrac><mo>+</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><msup><mn>3</mn><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>5</mn></mrow></mfrac><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mo>&#160;</mo><msub><mi>T</mi><mi>n</mi></msub><mo>=</mo><mfrac><mrow><msup><mn>1</mn><mn>3</mn></msup><mo>+</mo><msup><mn>2</mn><mn>3</mn></msup><mo>+</mo><mo>...</mo><mo>+</mo><msup><mi>n</mi><mn>3</mn></msup></mrow><mrow><mn>1</mn><mo>+</mo><mn>3</mn><mo>+</mo><mo>...</mo><mo>+</mo><mfenced><mrow><mn>2</mn><mi>n</mi><mo>-</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup></mrow><mn>4</mn></mfrac><msup><mi>n</mi><mn>2</mn></msup></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>4</mn></mfrac></math>

Sum of <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math> terms</p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>9</mn></munderover><mfrac><msup><mfenced><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mn>2</mn></msup><mn>4</mn></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>1</mn><msup><mn>0</mn><mn>2</mn></msup></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>1</mn><mn>4</mn></mfrac><mfenced open="[" close="]"><mrow><mfenced><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mn>1</mn><msup><mn>0</mn><mn>2</mn></msup></mrow></mfenced><mo>-</mo><msup><mn>1</mn><mn>2</mn></msup></mrow></mfenced></math>   </p><p><math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>0</mn> <mo>&#183;</mo> <mn>1</mn> <mn>1</mn> <mo>&#183;</mo> <mn>2</mn> <mn>1</mn> </mrow> <mrow> <mn>6</mn> </mrow> </mfrac> <mo>-</mo> <mn>1</mn> </mrow> </mfenced> </mrow> </math>     </p><p><math> <mrow> <mo>=</mo> <mfrac> <mrow> <mn>1</mn> </mrow> <mrow> <mn>4</mn> </mrow> </mfrac> <mfenced close="]" open="[" separators=","> <mrow> <mn>3</mn> <mn>8</mn> <mn>4</mn> </mrow> </mfenced> <mo>=</mo> <mn>9</mn> <mn>6</mn> </mrow> </math></p>

</details>

---

### Q104. JEE Main 2014 (19 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

Let <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>&#8289;</mo><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mn>100</mn></mfrac></mrow></mfenced><mi>n</mi></math>, where <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>[</mo><mi>n</mi><mo>]</mo></math> denotes the greatest integer less than or equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>. Then <math xmlns="http://www.w3.org/1998/Math/MathML"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>56</mn></munderover><mi>f</mi><mfenced><mi>n</mi></mfenced></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>56</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1287</mn></math>
- **(C)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1399</mn></math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>689</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1399</mn></math>**

**Detailed Solution:**

<p>Given <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><mrow><mn>3</mn><mi>n</mi></mrow><mi>100</mi></mfrac></mrow></mfenced><mi>n</mi><mo>=</mo><mfenced close="]" open="["><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mi>100</mi></mrow><mi>300</mi></mfrac></mfenced><mi>n</mi></math></p><p>If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mn>100</mn></mrow><mn>300</mn></mfrac><mo>&#60;</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>n</mi><mo>+</mo><mn>100</mn><mo>&#60;</mo><mn>300</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>&#60;</mo><mfrac><mi>200</mi><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mn>22</mn></math></p><p>We know that for a number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>&#10877;</mo><mi>x</mi><mo>&#60;</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>0</mn></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mo>&#160;</mo><mo>&#8704;</mo><mo>&#160;</mo><mn>1</mn><mo>&#10877;</mo><mi>n</mi><mo>&#10877;</mo><mn>22</mn></math></p><p>Again, if <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mn>9</mn><mi>n</mi><mo>+</mo><mn>100</mn></mrow><mn>300</mn></mfrac><mo>&#60;</mo><mn>2</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mn>9</mn><mi>n</mi><mo>+</mo><mn>100</mn><mo>&#60;</mo><mn>600</mn></math></p><p><mo></mo> <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mfrac><mi>500</mi><mn>9</mn></mfrac></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>n</mi><mo>=</mo><mi>55</mi></math></p><p>We know that for a number <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>&#10877;</mo><mi>x</mi><mo>&#60;</mo><mn>2</mn><mo>,</mo><mo>&#160;</mo><mfenced close="]" open="["><mi>x</mi></mfenced><mo>=</mo><mn>1</mn></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8658;</mo><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>,</mo><mo>&#160;</mo><mn>23</mn><mo>&#10877;</mo><mi>n</mi><mo>&#10877;</mo><mn>55</mn></math></p><p>And, <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mo>(</mo><mi>n</mi><mo>)</mo><mo>=</mo><mn>2</mn></math> if <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>56</mn></math></p><p>Thus, <math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="false"><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mi>56</mi></munderover></mstyle><mi>f</mi><mfenced><mi>n</mi></mfenced><mo>=</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mn>22</mn></munderover><mn>0</mn><mo>&#215;</mo><mi>n</mi><mo>+</mo><munderover><mo>&#8721;</mo><mrow><mi>n</mi><mo>=</mo><mn>23</mn></mrow><mn>55</mn></munderover><mn>1</mn><mo>&#215;</mo><mi>n</mi><mo>+</mo><mn>2</mn><mo>&#215;</mo><mn>56</mn></math></p><p>           <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>0</mn><mo>+</mo><mfenced><mrow><mi>23</mi><mo>+</mo><mi>24</mi><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>+</mo><mi>55</mi></mrow></mfenced><mo>+</mo><mi>56</mi><mo>&#215;</mo><mn>2</mn></math></p><p>          <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mn>33</mn><mn>2</mn></mfrac><mfenced><mrow><mn>23</mn><mo>+</mo><mn>55</mn></mrow></mfenced><mo>+</mo><mn>112</mn></math></p><p>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>=</mo><mn>33</mn><mo>&#215;</mo><mn>39</mn><mo>+</mo><mn>112</mn></math></p><p>    <math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>=</mo><mn>1399</mn><mo>.</mo></math></p>

</details>

---

### Q105. JEE Main 2014 (12 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

If $1+x^4+x^5=\sum_{i=0}^5 a_i\left(1+x^i\right)$, for all $x$ in $R$, then $a_2$ is:

**Options:**

- **(A)** $-4$
- **(B)** 6
- **(C)** $-8$
- **(D)** 10

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $-4$**

**Detailed Solution:**

$$
\begin{aligned}
&1+x^4+x^5=\sum_{i=0}^5 a_i(1+x)^i \\
&=a_0+a_1(1+x)^1+a_2(1+x)^2+a_3(1+x)^3 \\
&\quad+a_4(1+x)^4+a_5(1+x)^5 \\
&\Rightarrow 1+x^4+x^5
\end{aligned}
$$
$$
\begin{aligned}
=a_0+a_1(1+x) &+a_2\left(1+2 x+x^2\right)+a_3\left(1+3 x+3 x^2+x^3\right) \\
&+a_4\left(1+4 x+6 x^2+4 x^3+x^4\right) \\
&+a_5\left(1+5 x+10 x^2+10 x^3+5 x^4+x^5\right) \\
\Rightarrow & 1+x^4+x^5 \\
=a_0+a_1+a_1 x+a_2+2 a_2 x+a_2 x^2+a_3+3 a_3 x \\
+3 a_3 x^2+a_3 x^3+a_4+4 a_4 x+6 a_4 x^2+4 a_4 x^3+a_4 x^4+a_5 \\
&+5 a_5 x+10 a_5 x^2+10 a_5 x^3+5 a_5 x^4+a_5 x^5
\end{aligned}
$$
$$
\begin{aligned}
\Rightarrow & 1+x^4+x^5 \\
=&\left(a_0+a_1+a_2+a_3+a_4+a_5\right) \\
&+x\left(a_1+2 a_2+3 a_3+4 a_4+5 a_5\right) \\
+x^2\left(a_2+\right.&\left.3 a_3+6 a_4+10 a_5\right)+x^3\left(a_3+4 a_4+10 a_5\right) \\
&+x^4\left(a_4+5 a_5\right)+x^5\left(a_5\right)
\end{aligned}
$$
On comparing the like coefficients, we get
$$
\begin{aligned}
&a_5=1 \\
&a_4+5 a_5=1 \\
&a_3+4 a_4+10 a_5=0
\end{aligned}
$$
and $a_2+3 a_3+6 a_4+10 a_5=0$
from (1) \& (2), we get $a_4=-4 \ldots(5)$
From (1), (3) \& (5), we get $a_3=+6$...(6)
Now, from $(1),(5)$ and $(6)$, we get
$a_2=-4$

</details>

---

### Q106. JEE Main 2014 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

If the sum <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>3</mn><msup><mn>1</mn><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>....</mo><mi mathvariant="normal">.</mi><mo>+</mo></math> up to <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math> terms is equal to <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>k</mi><mn>21</mn></mfrac><mi>,</mi></math> then <math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> is equal to

**Options:**

- **(A)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>240</mn></math>
- **(B)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>
- **(C)** <math> <mrow> <mn>60</mn></mrow> </math>
- **(D)** <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>180</mn></math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) <math xmlns="http://www.w3.org/1998/Math/MathML"><mn>120</mn></math>**

**Detailed Solution:**

<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mi>20</mi></msub><mo>=</mo><mfrac><mn>3</mn><msup><mi mathvariant="normal">1</mi><mn>2</mn></msup></mfrac><mo>+</mo><mfrac><mn>5</mn><mrow><msup><mi mathvariant="normal">1</mi><mn>2</mn></msup><mo>+</mo><msup><mi>2</mi><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mfrac><mn>7</mn><mrow><msup><mn>1</mn><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup></mrow></mfrac><mo>+</mo><mo>.</mo><mo>...</mo><mo>+</mo><mi>upto</mi><mo>&#160;</mo><mn>20</mn><mo>terms</mo></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>=</mi><munderover><mi>&#931;</mi><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>20</mi></munderover><mfrac><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mrow><msup><mi mathvariant="normal">1</mi><mn>2</mn></msup><mo>+</mo><msup><mn>2</mn><mn>2</mn></msup><mo>+</mo><msup><mn>3</mn><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>...&#160;</mo><msup><mi>r</mi><mn>2</mn></msup></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><munderover><mi>&#931;</mi><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>20</mi></munderover><mfrac><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow><mrow><mfrac><mi>r</mi><mn>6</mn></mfrac><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced><mfenced><mrow><mn>2</mn><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><munderover><mi>&#931;</mi><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>20</mi></munderover><mfrac><mn>1</mn><mrow><mi>r</mi><mfenced><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfenced></mrow></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><munderover><mi>&#931;</mi><mrow><mi>r</mi><mo>=</mo><mn>1</mn></mrow><mi>20</mi></munderover><mfenced><mrow><mfrac><mn>1</mn><mi>r</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced close="}" open="{"><mrow><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>1</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>3</mn></mfrac></mrow></mfenced><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mn>3</mn></mfrac><mo>-</mo><mfrac><mn>1</mn><mn>4</mn></mfrac></mrow></mfenced><mo>+</mo><mo>.</mo><mo>...</mo><mo>+</mo><mfenced close="]" open="["><mrow><mfrac><mn>1</mn><mi>20</mi></mfrac><mo>-</mo><mfrac><mn>1</mn><mi>21</mi></mfrac></mrow></mfenced></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mn>6</mn><mfenced><mrow><mn>1</mn><mo>-</mo><mfrac><mn>1</mn><mi>21</mi></mfrac></mrow></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>=</mo><mfrac><mrow><mn>6</mn><mo>&#215;</mo><mi>20</mi></mrow><mi>21</mi></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>=</mi><mfrac><mn>120</mn><mi>21</mi></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>=</mi><mfrac><mi>k</mi><mi>21</mi></mfrac></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>120</mn></math>

</details>

---

### Q107. JEE Main 2014 (06 Apr)

*Type:* `singleCorrect` | *Level:* `3`

If <math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mrow><mo>(</mo><mn>10</mn><mo>)</mo></mrow><mn>9</mn></msup><mo>+</mo><mn>2</mn><msup><mrow><mo>(</mo><mn>11</mn><mo>)</mo></mrow><mn>1</mn></msup><msup><mrow><mo>(</mo><mn>10</mn><mo>)</mo></mrow><mn>8</mn></msup><mo>+</mo><mn>3</mn><msup><mrow><mo>(</mo><mn>11</mn><mo>)</mo></mrow><mn>2</mn></msup><msup><mrow><mo>(</mo><mn>10</mn><mo>)</mo></mrow><mn>7</mn></msup><mo>+</mo><mn>......</mn><mo>+</mo><mn>10</mn><msup><mrow><mo>(</mo><mn>11</mn><mo>)</mo></mrow><mn>9</mn></msup><mi>&#160;</mi><mo>=</mo><mi>k</mi><msup><mrow><mo>(</mo><mn>10</mn><mo>)</mo></mrow><mn>9</mn></msup><mo>,</mo></math> then <math> <mi>k</mi> </math> is equal to :

**Options:**

- **(A)** <math > <mrow>  <mn>100</mn> </mrow></math>
- **(B)** <math > <mrow>  <mn>110</mn> </mrow></math>
- **(C)** <math> <mrow> <mfrac> <mrow> <mn>1</mn> <mn>2</mn> <mn>1</mn> </mrow> <mrow> <mn>1</mn> <mn>0</mn> </mrow> </mfrac> </mrow> </math>
- **(D)** <math> <mrow> <mfrac> <mrow> <mn>4</mn> <mn>4</mn> <mn>1</mn> </mrow> <mrow> <mn>1</mn> <mn>0</mn> <mn>0</mn></mrow> </mfrac> </mrow> </math>

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) <math > <mrow>  <mn>100</mn> </mrow></math>**

**Detailed Solution:**

<p>Let,<math> <mrow> <mi>S</mi><mo>=</mo><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>10</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>9</mn> </msup> <mo>+</mo><mn>2</mn><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>11</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>1</mn> </msup> <mi>&#160;</mi><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>10</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>8</mn> </msup> <mo>+</mo><mn>3</mn><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>11</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>2</mn> </msup> <mi>&#160;</mi><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>10</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>7</mn> </msup> <mo>+</mo><mn>......</mn><mo>+</mo><mn>10</mn><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>11</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>9</mn> </msup> <mi>&#160;</mi><mo>=</mo><mi>k</mi><msup> <mrow> <mrow><mo>(</mo> <mrow> <mn>10</mn> </mrow> <mo>)</mo></mrow> </mrow> <mn>9</mn> </msup> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo>=</mo><msup><mrow><mo>(</mo><mn>10</mn><mo>)</mo></mrow><mn>9</mn></msup><mfenced open="{" close="}"><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mo>+</mo><mn>3</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>....</mo><mo>+</mo><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>9</mn></msup></mrow></mfenced></math>

So,<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>1</mn><mo>+</mo><mn>2</mn><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mo>+</mo><mn>3</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>....</mo><mo>+</mo><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>9</mn></msup></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mi>k</mi><mo>=</mo><mfrac><mn>11</mn><mn>10</mn></mfrac><mo>+</mo><mn>2</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mn>3</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>3</mn></msup><mo>+</mo><mo>.</mo><mo>....</mo><mo>+</mo><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup></math>

Subtracting

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8722;</mo><mfenced><mfrac><mi>k</mi><mn>10</mn></mfrac></mfenced><mo>=</mo><mn>1</mn><mo>+</mo><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mo>+</mo><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>&#8230;</mo><mo>&#8230;</mo><mo>+</mo><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>9</mn></msup><mo>&#8722;</mo><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup></math>
Here,</p><p>First term <math> <mrow> <mo>=</mo><mn>1</mn> </mrow> </math>

Common ratio<math> <mrow> <mo>=</mo><mfrac> <mrow> <mn>11</mn> </mrow> <mrow> <mn>10</mn> </mrow> </mfrac> </mrow> </math>

Number of terms<math> <mrow> <mo>=</mo><mn>10</mn> </mrow> </math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8756;</mo><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mi>&#160;</mi><mfrac><mi>k</mi><mn>10</mn></mfrac><mo>=</mo><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mfenced open="[" close="]"><mfrac><mrow><mn>1</mn><mfenced open="{" close="}"><mrow><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow><mfenced open="{" close="}"><mrow><mfrac><mn>11</mn><mn>10</mn></mfrac><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mfrac></mfenced></math>

<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>10</mn><mfenced open="[" close="]"><mrow><mn>10</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mn>10</mn><mfenced open="{" close="}"><mrow><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mn>1</mn></mrow></mfenced></mrow></mfenced></math></p><p><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mfenced open="[" close="]"><mrow><mn>100</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>&#8722;</mo><mn>100</mn><msup><mfenced><mfrac><mn>11</mn><mn>10</mn></mfrac></mfenced><mn>10</mn></msup><mo>+</mo><mn>100</mn></mrow></mfenced></math>
<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi><mo>=</mo><mn>100</mn></math></p>

</details>

---

### Q108. JEE Main 2013 (25 Apr Online)

*Type:* `singleCorrect` | *Level:* `2`

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/qUZXCuXAiNjCg4RQauU-rswHZ1SfdF8cIsrZbf3hrgw.original.fullsize.png">

**Options:**

- **(A)** 2925
- **(B)** 1469
- **(C)** 1728
- **(D)** 1456

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 2925**

**Detailed Solution:**

Consider $1^2+3^2+5^2+\ldots \ldots+25^2$ $n^{\text {th }}$ term $\mathrm{T}_n=(2 n-1)^2, n=1, \ldots \ldots 13$
Now, $\mathrm{S}_n=\sum_{n=1}^{13} \mathrm{~T}_n=\sum_{n=1}^{13}(2 n-1)^2$
$$
\begin{aligned}
&=\sum_{n=1}^{13} 4 n^2+\sum_{n=1}^{13} 1-\sum_{n=1}^{13} 4 n \\
&=4 \sum n^2+13-4 \sum n
\end{aligned}
$$
$$
=4\left[\frac{n(n+1)(2 n+1)}{6}\right]+13-4 \frac{n(n+1)}{2}
$$
Put $n=13$, we get
$$
\begin{aligned}
&\mathrm{S}_n=26 \times 14 \times 9+13-26 \times 14 \\
&=3276+13-364 \\
&=2925 .
\end{aligned}
$$

</details>

---

### Q109. JEE Main 2013 (23 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series :
$(2)^2+2(4)^2+3(6)^2+\ldots$ upto 10 terms is :

**Options:**

- **(A)** 11300
- **(B)** 11200
- **(C)** 12100
- **(D)** 12300

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 12100**

**Detailed Solution:**

$2^2+2(4)^2+3(6)^2+\ldots \ldots$ upto 10 terms $=2^2\left[1^3+2^3+3^3+\ldots \ldots\right.$ upto 10 terms $]$
$=4 \cdot\left(\frac{10 \times 11}{2}\right)^2=12100$

</details>

---

### Q110. JEE Main 2013 (22 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum $\frac{3}{1^2}+\frac{5}{1^2+2^2}+\frac{7}{1^2+2^2+3^2}+\ldots$. upto 11-terms is:

**Options:**

- **(A)** $\frac{7}{2}$
- **(B)** $\frac{11}{4}$
- **(C)** $\frac{11}{2}$
- **(D)** $\frac{60}{11}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{11}{2}$**

**Detailed Solution:**

Given sum is
$$
\begin{aligned}
& \frac{3}{12}+\frac{5}{1^2+2^2}+\frac{7}{1^2+2^2+3^2}+\ldots . . \\
& n \text {th term }=\mathrm{T}_n \\
& =\frac{2 n+1}{\frac{n(n+1)(2 n+1)}{6}}=\frac{6}{n(n+1)} \\
& \text { or } \mathrm{T}_n=6\left[\frac{1}{n}-\frac{1}{n+1}\right] \\
& \therefore \quad \mathrm{S}_n= \\
& \sum \mathrm{T}_n=6 \sum \frac{1}{n}-6 \sum \frac{1}{n+1}=\frac{6 n}{n}-\frac{6}{n+1} \\
& =6-\frac{6}{n+1}=\frac{6 n}{n+1} \\
& S_{11}=\frac{6 \times 11}{11+1}=\frac{66}{12}=\frac{33}{6}=\frac{11}{2} \\
&
\end{aligned}
$$

</details>

---

### Q111. JEE Main 2013 (09 Apr Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series:
$1+\frac{1}{1+2}+\frac{1}{1+2+3}+\ldots \ldots$. upto 10 terms, is:

**Options:**

- **(A)** $\frac{18}{11}$
- **(B)** $\frac{22}{13}$
- **(C)** $\frac{20}{11}$
- **(D)** $\frac{16}{9}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{20}{11}$**

**Detailed Solution:**

$\mathrm{T}_r=\frac{1}{1+2+3+\ldots+r}=\frac{2}{r(r+1)}$
$\mathrm{S}_{10}=2 \sum_{r=1}^{10} \frac{1}{r(r+1)}=2 \sum_{r=1}^{10}\left[\frac{r+1}{r(r+1)}-\frac{r}{r(r+1)}\right]$
$=2 \sum_{r=1}^{10}\left(\frac{1}{r}-\frac{1}{r+1}\right)$
$=2\left[\left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)+\ldots+\left(\frac{1}{10}-\frac{1}{11}\right)\right]$
$=2\left[1-\frac{1}{11}\right]=2 \times \frac{10}{11}=\frac{20}{11}$

</details>

---

### Q112. JEE Main 2012 (26 May Online)

*Type:* `singleCorrect` | *Level:* `3`

If the sum of the series $1^2+2 \cdot 2^2+3^2+2 \cdot 4^2+5^2+$ ... $2.6^2+\ldots$ upto $\mathrm{n}$ terms, when $\mathrm{n}$ is even, is $\frac{n(n+1)^2}{2}$, then the sum of the series, when $\mathrm{n}$ is odd, is

**Options:**

- **(A)** $n^2(n+1)$
- **(B)** $\frac{n^2(n-1)}{2}$
- **(C)** $\frac{n^2(n+1)}{2}$
- **(D)** $n^2(n-1)$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $\frac{n^2(n+1)}{2}$**

**Detailed Solution:**

If $n$ is odd, the required sum is
$$
\begin{aligned}
& 1^2+2.2^2+3^2+2.4^2+\ldots . .+2(n-1)^2+n^2 \\
& =\frac{(n-1)(n-1+1)^2}{2}+n^2 \quad(\because n-1 \text { is even }) \\
& =\left(\frac{n-1}{2}+1\right) n^2=\frac{n^2(\mathrm{n}+1)}{2}
\end{aligned}
$$

</details>

---

### Q113. JEE Main 2012 (19 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $1+\frac{4}{3}+\frac{10}{9}+\frac{28}{27}+\ldots$ upto $n$ terms is

**Options:**

- **(A)** $\frac{7}{6} n+\frac{1}{6}-\frac{2}{3.2^{n-1}}$
- **(B)** $\frac{5}{3} n-\frac{7}{6}+\frac{1}{2.3^{n-1}}$
- **(C)** $n+\frac{1}{2}-\frac{1}{2.3^n}$
- **(D)** $n-\frac{1}{3}-\frac{1}{3.2^{n-1}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) $n+\frac{1}{2}-\frac{1}{2.3^n}$**

**Detailed Solution:**

Given series is
$1+\frac{4}{3}+\frac{10}{9}+\frac{28}{27}+\ldots . n$ terms
$=1+\left(1+\frac{1}{3}\right)+\left(1+\frac{1}{9}\right)+\left(1+\frac{1}{27}\right)+\ldots . n$ terms $=(1+1+1+\ldots+n$ terms $)$ $+\left(\frac{1}{3}+\frac{1}{9}+\frac{1}{27}+\ldots n\right.$ terms $)$ $=n+\frac{\frac{1}{3}\left(1-\frac{1}{3^n}\right)}{1-\frac{1}{3}}=n+\frac{1}{3} \times \frac{3}{2}\left[1-3^{-n}\right]$ $=n+\frac{1}{2}\left[1-3^{-n}\right]=n+\frac{1}{2}-\frac{1}{2.3^n}$

</details>

---

### Q114. JEE Main 2012 (12 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series
$$
\frac{1}{1+\sqrt{2}}+\frac{1}{\sqrt{2}+\sqrt{3}}+\frac{1}{\sqrt{3}+\sqrt{4}}+\ldots
$$
upto 15 terms is

**Options:**

- **(A)** 1
- **(B)** 2
- **(C)** 3
- **(D)** 4

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(C) 3**

**Detailed Solution:**

Given series is
$$
\begin{aligned}
& \frac{1}{1+\sqrt{2}}+\frac{1}{\sqrt{2}+\sqrt{3}}+\frac{1}{\sqrt{3}+\sqrt{4}}+\ldots . . \\
& n^{\text {th }} \text { term }=\frac{1}{\sqrt{n}+\sqrt{n+1}} \\
& \therefore 15^{\text {th }} \text { term }=\frac{1}{\sqrt{15}+\sqrt{16}}
\end{aligned}
$$
Thus, given series upto 15 terms is
$$
\frac{1}{1+\sqrt{2}}+\frac{1}{\sqrt{2}+\sqrt{3}}+\frac{1}{\sqrt{3}+\sqrt{4}}+\ldots \ldots+\frac{1}{\sqrt{15}+\sqrt{16}}
$$
This can be re-written as
$$
\frac{1-\sqrt{2}}{-1}+\frac{\sqrt{2}-\sqrt{3}}{-1}+\frac{\sqrt{3}-\sqrt{4}}{-1}+\ldots \ldots+\frac{\sqrt{15}-\sqrt{16}}{-1}
$$
(By rationalization)
$$
\begin{gathered}
=-1+\sqrt{2}-\sqrt{2}+\sqrt{3}-\sqrt{3}+\sqrt{4}+\ldots . .-\sqrt{14}+\sqrt{15} \\
-\sqrt{15}+\sqrt{16} \\
=-1+\sqrt{16}=-1+4=3
\end{gathered}
$$
Hence, the required sum $=3$

</details>

---

### Q115. JEE Main 2012 (07 May Online)

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $1^2+2.2^2+3^2+2.4^2+5^2+2.6^2+\ldots . .+2(2 m)^2$ is

**Options:**

- **(A)** $m(2 m+1)^2$
- **(B)** $m^2(m+2)$
- **(C)** $m^2(2 m+1)$
- **(D)** $m(m+2)^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $m(2 m+1)^2$**

**Detailed Solution:**

The sum of the given series $1^2+2.2^2+3^2+$ $2.4^2+5^2+2.6^2+\ldots \ldots . .+2(2 m)^2$ is $\frac{2 m\left(2 m+1^2\right.}{2} \leqslant m\left(2 m+1^2\right)$

</details>

---

### Q116. JEE Main 2012 (Offline)

*Type:* `singleCorrect` | *Level:* `3`

Statement $1$: The sum of the series $1+(1+2+4)+(4+6+9)+(9+12+16)+\ldots \ldots+(361+380+ 400)$ is $8000$.
Statement $2$: $\sum_{k=1}^n\left(k^3-(k-1)^3\right)=n^3$ for any natural number $n$.

**Options:**

- **(A)** Statement $1$ is false, statement $2$ is true.
- **(B)** Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$
- **(C)** Statement $1$ is true, statement $2$ is true; statement $2$ is not a correct explanation for statement $1$
- **(D)** Statement $1$ is true, statement $2$ is false

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) Statement $1$ is true, statement $2$ is true; statement $2$ is a correct explanation for statement $1$**

**Detailed Solution:**

Statement $1$ has $20$ terms whose sum is $8000$ 
And statement $2$ is true and supporting statement $1$. 
$\because k^{\text {th }}$ bracket is $(k-1)^2+k(k-1)+k^2=3 k^2-3 k+1$.

</details>

---

### Q117. JEE Main 2009

*Type:* `singleCorrect` | *Level:* `2`

The sum to the infinity of the series $1+\frac{2}{3}+\frac{6}{3^2}+\frac{10}{3^3}+\frac{14}{3^4}+\ldots \ldots$ is

**Options:**

- **(A)** 2
- **(B)** 3
- **(C)** 4
- **(D)** 6

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) 3**

**Detailed Solution:**

Let $S=1+\frac{2}{3}+\frac{6}{3^2}+\frac{10}{3^3}+\frac{14}{3^4}+\ldots$.
$\frac{1}{3} S=\frac{1}{3}+\frac{2}{3^2}+\frac{6}{3^3}+\frac{10}{3^4}+\ldots$
Dividing (1) \& (2)
$$
\begin{aligned}
& S\left(1-\frac{1}{3}\right)=1+\frac{1}{3}+\frac{4}{3^2}+\frac{4}{3^3}+\frac{4}{3^4}+\ldots . \\
& \frac{2}{3} S=\frac{4}{3}+\frac{4}{3^2}\left(1+\frac{1}{3}+\frac{1}{3^2}+\ldots . .\right) \Rightarrow \frac{2}{3} S=\frac{4}{3}+\frac{4}{3^2}\left(\frac{1}{1-\frac{1}{3}}\right)=\frac{4}{3}+\frac{4}{3^2} \frac{3}{2}=\frac{4}{3}+\frac{2}{3}=\frac{6}{2} \Rightarrow \frac{2}{3} S=\frac{6}{3} \Rightarrow S=3
\end{aligned}
$$

</details>

---

### Q118. JEE Main 2007

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $\frac{1}{2 !}-\frac{1}{3 !}+\frac{1}{4 !}-\ldots$ upto infinity is

**Options:**

- **(A)** $e^{-2}$
- **(B)** $e^{-1}$
- **(C)** $\mathrm{e}^{-1 / 2}$
- **(D)** $\mathrm{e}^{1 / 2}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $e^{-1}$**

**Detailed Solution:**

$e^{-x}=1-x+\frac{x^2}{2 !}-\frac{x^3}{3 !}+\frac{x^4}{4 !}-\cdots$
put $x=1$
$\frac{1}{2 !}-\frac{1}{3 !}+\frac{1}{4 !} \cdots=e^{-1}$.

</details>

---

### Q119. JEE Main 2006

*Type:* `singleCorrect` | *Level:* `3`

The value of $\sum_{k=1}^{10}\left(\sin \frac{2 k \pi}{11}+i \cos \frac{2 k \pi}{11}\right)$ is

**Options:**

- **(A)** i
- **(B)** 1
- **(C)** -1
- **(D)** -i

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) -i**

**Detailed Solution:**

$\sum_{k=1}^{10}\left(\sin \frac{2 k \pi}{11}+i \cos \frac{2 k \pi}{11}\right)=\sum_{k=1}^{10} \sin \frac{2 k \pi}{11}+i \sum_{k=1}^{10} \cos \frac{2 k \pi}{11}$
$=0+i(-1)=-i$

</details>

---

### Q120. JEE Main 2005

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $1+\frac{1}{4.2 !}+\frac{1}{16.4 !}+\frac{1}{64.6 !}+\ldots \ldots \ldots$ ad inf. is

**Options:**

- **(A)** $\frac{\mathrm{e}-1}{\sqrt{\mathrm{e}}}$
- **(B)** $\frac{\mathrm{e}+1}{\sqrt{\mathrm{e}}}$
- **(C)** $\frac{\mathrm{e}-1}{2 \sqrt{\mathrm{e}}}$
- **(D)** $\frac{e+1}{2 \sqrt{e}}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) $\frac{e+1}{2 \sqrt{e}}$**

**Detailed Solution:**

$\frac{e^x+e^{-x}}{2}=1+\frac{x^2}{2 !}+\frac{x^4}{4 !}+\frac{x^6}{6 !}+\ldots \ldots$
putting $x=1 / 2$ we get
$\frac{e+1}{2 \sqrt{e}}$

</details>

---

### Q121. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

The sum of series $\frac{1}{2 !}+\frac{1}{4 !}+\frac{1}{6 !}+\ldots$ is

**Options:**

- **(A)** $\frac{\left(\mathrm{e}^2-1\right)}{2}$
- **(B)** $\frac{(e-1)^2}{2 e}$
- **(C)** $\frac{\left(\mathrm{e}^2-1\right)}{2 \mathrm{e}}$
- **(D)** $\frac{\left(e^2-2\right)}{e}$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{(e-1)^2}{2 e}$**

**Detailed Solution:**

$\frac{\mathrm{e}^\alpha+\mathrm{e}^{-\alpha}}{2}=1+\frac{\alpha^2}{2 !}+\frac{\alpha^4}{4 !}+\frac{\alpha^6}{6 !}+\ldots \ldots$
$\frac{\mathrm{e}^\alpha+\mathrm{e}^{-\alpha}}{2}-1=\frac{\alpha^2}{2 !}+\frac{\alpha^4}{4 !}+\frac{\alpha^6}{6 !}+\ldots \ldots$
put $\alpha=1$, we get
$\frac{(\mathrm{e}-1)^2}{2 \mathrm{e}}=\frac{1}{2 !}+\frac{1}{4 !}+\frac{1}{6 !}+\ldots \ldots \ldots \ldots$

</details>

---

### Q122. JEE Main 2004

*Type:* `singleCorrect` | *Level:* `3`

The sum of the first $n$ terms of the series $1^2+2 \cdot 2^2+3^2+2 \cdot 4^2+5^2+2 \cdot 6^2+\ldots$ is $\frac{n(n+1)^2}{2}$ when $n$ is even. When $n$ is odd the sum is

**Options:**

- **(A)** $\frac{3 n(n+1)}{2}$
- **(B)** $\frac{\mathrm{n}^2(\mathrm{n}+1)}{2}$
- **(C)** $\frac{n(n+1)^2}{4}$
- **(D)** $\left[\frac{\mathrm{n}(\mathrm{n}+1)}{2}\right]^2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(B) $\frac{\mathrm{n}^2(\mathrm{n}+1)}{2}$**

**Detailed Solution:**

If $n$ is odd then $(n-1)$ is even $\Rightarrow$ sum of odd terms $=\frac{(n-1) n^2}{2}+n^2=\frac{n^2(n+1)}{2}$.

</details>

---

### Q123. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

The sum of the series $\frac{1}{1.2}-\frac{1}{2.3}+\frac{1}{3.4} \ldots \ldots \ldots \ldots \ldots \ldots .$. up to $\infty$ is equal to

**Options:**

- **(A)** $\log _e\left(\frac{4}{e}\right)$
- **(B)** $2 \log _e 2$
- **(C)** $\log _{\mathrm{e}} 2-1$
- **(D)** $\log _{\mathrm{e}} 2$

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) $\log _e\left(\frac{4}{e}\right)$**

**Detailed Solution:**

$\frac{1}{1.2}-\frac{1}{2.3}+\frac{1}{3.4} \ldots \ldots \ldots \ldots \ldots \ldots \ldots \ldots\infty$
Let $T_n=\frac{1}{n(n+1)}=\left(\frac{1}{n}-\frac{1}{n+1}\right)$
$\mathrm{S}=\mathrm{T}_1-\mathrm{T}_2+\mathrm{T}_3-\mathrm{T}_4+\mathrm{T}_5 \ldots \ldots \ldots \ldots \ldots$
$=\left(\frac{1}{1}-\frac{1}{2}\right)-\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right)-\left(\frac{1}{4}-\frac{1}{5}\right) \ldots \ldots \ldots$.
$=1-2\left[\frac{1}{2}-\frac{1}{3}+\frac{1}{4}-\frac{1}{5} \ldots \ldots \ldots \ldots \infty\right]$
$=1-2[-\log (1+1)+1]=2 \log 2-1=\log \left(\frac{4}{e}\right)$

</details>

---

### Q124. JEE Main 2003

*Type:* `singleCorrect` | *Level:* `3`

If $f(x)=x^n$, then the value of $f(1)-\frac{f^{\prime}(1)}{1}+\frac{f^{\prime \prime}(1)}{2 !}-\frac{f^{\prime \prime}(1)}{3 !}+\ldots \ldots \ldots \ldots . \frac{(-1)^n f^{\prime \prime}(1)}{n !}$ is

**Options:**

- **(A)** 1
- **(B)** $2^n$
- **(C)** $2^{\mathrm{n}}-1$
- **(D)** 0

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(D) 0**

**Detailed Solution:**

$\mathrm{f}(\mathrm{x})=\mathrm{x}^{\mathrm{n}} \Rightarrow \mathrm{f}(1)=1$
$\mathrm{f}^{\prime}(\mathrm{x})=\mathrm{nx} x^{\mathrm{n}-1} \Rightarrow \mathrm{f}^{\prime}(1)=\mathrm{n}$
$\mathrm{f}^{\prime \prime}(\mathrm{x})=\mathrm{n}(\mathrm{n}-1) \mathrm{x}^{\mathrm{n}-2} \Rightarrow \mathrm{f}^{\prime \prime}(1)=\mathrm{n}(\mathrm{n}-1)$
$\ldots \ldots \ldots \ldots \ldots \ldots \ldots \mathrm{f}^{\mathrm{n}}(\mathrm{x})=\mathrm{n} ! \Rightarrow \mathrm{f}^{\mathrm{n}}(1)=\mathrm{n} !$
$=1-\frac{\mathrm{n}}{1 !}+\frac{\mathrm{n}(\mathrm{n}-1)}{2 !}-\frac{\mathrm{n}(\mathrm{n}-1)(\mathrm{n}-2)}{3 !}+\ldots \ldots \ldots+(-1)^{\mathrm{n}} \frac{\mathrm{n} !}{\mathrm{n} !}$
$={ }^{\mathrm{n}} \mathrm{C}_0-{ }^{\mathrm{n}} \mathrm{C}_1+{ }^{\mathrm{n}} \mathrm{C}_2-{ }^{\mathrm{n}} \mathrm{C}_3+\ldots \ldots \ldots+(-1)^{\mathrm{n}}{ }^{\mathrm{n}} \mathrm{C}_{\mathrm{n}}=0$

</details>

---

### Q125. JEE Main 2002

*Type:* `singleCorrect` | *Level:* `3`

$1^3-2^3+3^3-4^3+\ldots .+9^3=$

**Options:**

- **(A)** 425
- **(B)** -425
- **(C)** 475
- **(D)** -475

<details>
<summary><b>View Answer & Solution</b></summary>

**Correct Option:** **(A) 425**

**Detailed Solution:**

<img src="https://cdn-question-pool.getmarks.app/pyq/jee_main/jkqZanl6hIE_duHejFWhVQSpobnSn-F94xA1h3IMIOI.original.fullsize.png">

</details>

---

